# P-0740 — O loop de módulos: a convergência da EXECUCAO-AUTONOMA sob a janela real

**Data:** 2026-09-18 · **Origem:** aferição empírica do `scrum-master` conduzida em janela de
orquestração (run de ponta a ponta sobre a `BKL-T4` do `P-0739`), mais a correção da premissa de
tamanho de janela · **Status:** `done` (2026-09-18 — rodadas `RP-2` e `RP-3` fechadas: o segundo bloqueio da `LM-T1` era **de aceite**, não de rota, `DM-12`; e a gramática de cabeçalho da `DM-5` recuou para a forma que os parsers leem, com a tarefa nova `LM-T4a` ensinando-lhes a de três campos, `DM-13`. A `LM-T1` fechou `done`, aprovada 100%, e a rodada `RP-5` — a primeira conduzida pelo `pantonic-consultant` — absorveu o `AE-8` e o `AE-7` com `DM-15`/`DM-16` e os cards `LM-T1a` e `LM-T7`; o plano passa a 9 tarefas) · **Iniciativa:** `EXECUCAO-AUTONOMA` · **Prefixo das
tarefas:** `LM-T<n>` · **Prefixo das decisões:** `DM-<n>` · **Checagem de versão do kit:** modo
hub — congelada em `0.0.0` (`DE-7`), comparação local × remoto suspensa, nada a comparar.

## 0. O objetivo, herdado sem emenda

O enunciado do dono que abriu a `EXECUCAO-AUTONOMA` em 2026-08-22 continua sendo o único alvo:

> transformar o trabalho de `proximo-passo` num agente autônomo, capaz de rodar sozinho todas as
> delegações e ajustes de modelo, e entregar ao cliente o entregável do plano, e não delegar ao
> humano uma tarefa rotineira e mecânica.

Este plano **não** reabre o objetivo. Ele converge as três iniciativas que o perseguiram, corrige
a premissa que as travou e substitui a unidade de trabalho.

## 1. O que o merge recolhe — estado medido em 2026-09-18

| plano | estado | o que fica | o que este plano absorve |
|---|---|---|---|
| `P-0734-EXA` | `superseded` (rebase pelo `P-0737`, 2026-08-22) | 52 tarefas entregues, registro histórico; `DP-A`..`DP-S` seguem **fonte normativa** citada pelo `scrum-master` | nada de tarefa; as decisões `DP-*` continuam válidas e não se reescrevem aqui |
| `P-0737-AUT` | `blocked` desde 2026-08-22 — "paralisado enquanto o `P-0738` não fecha; a razão é o custo fixo de contexto" | 3 de 10 fechadas (`AUT-T1`, `AUT-T5a`, `AUT-T5b`) | as **7 abertas** (`T2`, `T3`, `T4`, `T5c`, `T6`..`T10`), reagrupadas em módulos |
| `P-0738-CTX` | `done` — 17/17 | a medida do custo fixo; `CTX-T10` mediu **regressão** (DX-5 subiu 34%) | nada de tarefa — o plano cumpriu e fechou |

**A condição do bloqueio do `P-0737` já não se aplica:** o `P-0738` fechou. O plano ficou `blocked`
27 dias por uma condição satisfeita e por uma razão de fundo que a §2 invalida. Este plano o
sucede: ao ser registrado, `P-0737` passa a `superseded` (`DM-1`).

## 2. A premissa corrigida — e o que ela invalida

**Fato medido (2026-09-18, `docs/CUSTO_DO_PICKUP.md` `## 13`):** a janela é de **1M tokens**, não
200k. O `usage_1` de abertura de uma janela principal (60.472 tk) ocupa **6,0%**, não 30,2%. O E1
inteiro — `CLAUDE.md` global, memória, listagem de 17 skills e 9 agentes — soma 22.334 ch
(4.467–7.445 tk): **0,45%–0,74%** da janela.

**Causa raiz do travamento, encontrada no nosso próprio código:** `.claude/tools/ocupacao.py`
fixava `JANELA_TOKENS_DEFAULT = 200_000`, com gatilho em 50%. O aviso "ocupação cruzou o teto de
trabalho" vinha disparando a **~10% da janela real**. Corrigido em 2026-09-18 (denominador 1M,
sobrescrita por `PANTONIC_CONTEXT_TOKENS_MAX`, sufixo `k`/`M` aceito, `tests/test_ocupacao.py`
atualizado).

**O que isso invalida, nominalmente:**

- O motivo registrado do `blocked` do `P-0737` ("custo fixo de contexto").
- Toda rodada de corte em fonte nossa por ocupação de janela: o ganho máximo é 0,7 ponto
  percentual.
- A regra `B2` do `scrum-master` como gargalo — ela lia esse aviso e encerrava a janela cedo.
- **A tarefa atômica como unidade de trabalho** — que existia porque o contexto era escasso.

## 3. A aferição do `scrum-master` — o que o run mediu

Run de ponta a ponta sobre a `BKL-T4` do `P-0739`, conduzido por uma janela de orquestração real.
Resultado da tarefa: `done`, `ressalva` 85%, bloqueante `nenhuma`, suíte 132→142 verdes, guardas
todas exit 0. RDO em `docs/RDO/P-0739-BKL-T4-status-start-diretiva-transicao-e-projecoes.md`.

| papel | tokens | tool uses | duração |
|---|---|---|---|
| executor (sonnet) | 203,7k | 51 | 17 min |
| reviewer (opus) | 80,9k | 20 | 4 min |
| **total por tarefa** | **284,6k** | 71 | 21 min |

**A mecânica funciona:** os dez passos rodaram, a gramática de retorno de domínio fechado foi
respeitada pelos dois subagentes, o roteamento calculou certo (`A8` → `B1`), os instrumentos
produziram, e o reviewer achou uma dependência de ordem real que o executor não viu (`AE-10` do
`P-0739`). Passos não exercitados por falta de ocasião: `A1` (queda), `A2` (retorno inválido),
`A6`/`A7` (refazer/reprovar).

**Seis defeitos medidos — a matéria deste plano:**

1. **`.claude/estado/` não existia.** O Passo 4 grava ali `tarefa-corrente.json`, insumo do hook
   `SubagentStop` (`telemetria_hook.py`). O diretório nunca foi criado; o hook falha aberto
   (silêncio, exit 0), então a telemetria automática **nunca disparou e ninguém notou**. É a prova
   material de que o Passo 4 nunca tinha rodado.
2. **Dependência circular no Passo 3.** Ele manda materializar `ready`→`in-progress` no kanban,
   "ato exclusivo do `scrum-master`" — mas o verbo que faria isso (`backlog.py status`) era o
   entregável da tarefa na fila. A materialização saiu à mão: o trabalho manual que o instrumento
   existe para eliminar. (A `BKL-T4` entregou o verbo; a dependência de ordem com os marcadores
   `<!-- fila:gerada -->` está no `AE-10` do `P-0739`.)
3. **Contratos divergentes no mesmo pacote de fechamento.** `rdo.py close --tokens-k` exige `int`;
   `telemetria.py append --tokens_k` aceita decimal. O mesmo número medido não passa nos dois.
4. **`B1` encerra a janela por qualquer `pendencia=`**, sem distinguir pendência substantiva de
   observação transitória já resolvida. **É o gargalo:** o loop existe para conduzir o plano
   inteiro e para na primeira tarefa.
5. **Nenhuma provisão para mudança fora de banda do orquestrador.** Uma edição da própria
   orquestração em `ocupacao.py` quebrou `test_ocupacao.py`, entrou na verificação do executor
   como falha alheia, consumiu turnos de diagnóstico e virou o `pendencia=` que disparou `B1`. A
   causa do encerramento foi a orquestração, não a tarefa.
6. **O dossiê de evidência não carrega o contexto que o reviewer precisa.** Foi preciso injetar à
   mão a explicação do WIP; sem ela o reviewer julgaria a suíte vermelha e reprovaria entrega
   correta.

**Fatos repostos pela rodada `RP-1` (2026-09-18) — o que a autoria não levantou.** A `LM-T1` foi
autorada sem confrontar o entregável com as regras de versionamento vigentes; os quatro fatos
abaixo foram apurados na rodada e são a base da `DM-10`:

- **`F-1`** — `.gitignore:7-10` exclui `.claude/estado/` inteiro, com o comentário "fato de uma
  sessão numa máquina, nunca canônico do framework" (entrada criada pela `T55`). O literal das
  quatro linhas está transcrito no card da `LM-T1`.
- **`F-2`** — o idioma `.gitkeep` já existe no repositório e não está ignorado: `docs/RDO/.gitkeep`
  é versionado, e `.claude/tools/rdo.py:569` já o exclui da listagem do `INDEX.md` por não ser
  `.md`. Versionar um `.gitkeep` não inventa convenção nova.
- **`F-3`** — o hook não depende de o diretório ser versionado: `telemetria_hook.ler_estado:126-130`
  devolve `None` quando o arquivo não existe e `processar:172-174` trata isso como silêncio
  previsto; `_estado_path_default:203-204` resolve `<repo>/.claude/estado/tarefa-corrente.json` só
  no `main`, e `tests/test_telemetria_hook.py` injeta o caminho por `tmp_path` em todos os casos
  (`:148-150`, `:196`, `:216-218`). Nenhuma suposição sobre versionamento atravessa a `LM-T2`.
- **`F-4`** — a divergência de tipo do defeito 3 tem endereço exato: `.claude/tools/rdo.py:772`
  declara `"--tokens-k", required=True, type=int, dest="tokens_k"` e `:675` grava
  `"TOKENS_K": str(args.tokens_k)`; `.claude/tools/telemetria.py:150` declara `--tokens_k` sem
  `type` e valida por `_validar_numero_nao_negativo` (`:106`); o hook já emite o número na forma
  decimal de uma casa em `telemetria_hook.montar_args_append:152` (`f"{tokens_k:.1f}"`). Em
  `tests/test_rdo.py:231` o valor de fixture é `"80"` e a asserção de `:271` é
  `assert "80" in conteudo` — substring, que a forma `80.0` continua satisfazendo.

**Fatos repostos pela rodada `RP-3` (2026-09-18) — a gramática de cabeçalho que os instrumentos
aceitam hoje.** Apurados por leitura nesta rodada; são a base da `DM-13` e o texto que a `LM-T4a`
executa:

- **`F-5`** — `.claude/tools/rdo.py:85-89` define `_HEADER_BRACKET_RE`, a gramática de **dois**
  campos, usada por `extrair_dossie:210` e portanto compartilhada por `rdo.py close` e
  `review_evidence.py`:
  `r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) "` ·
  `r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)? · classe (?P<classe>.+?)"` ·
  `r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"`.
  Cabeçalho que não casa cai no ramo legado (`:230-240`), que exige `--esquema-legado --modelo
  --classe` — flags que só o `rdo.py close` expõe (`:819-824`); o `review_evidence.py` fixa
  `esquema_legado=False` (`:271`, `:568`) e não tem rota nenhuma. E não há onde encaixar o esforço
  na gramática atual: o grupo `classe` é `.+?` até o `]`, então `[… · classe implementacao · esforço
  medium]` faria `_normalizar_classe` (`:130-132`) receber `implementacao · esforço medium` e
  falhar do mesmo jeito.
- **`F-6`** — o parser **irmão** rejeita o mesmo cabeçalho, pela mesma razão:
  `.claude/tools/backlog.py:51` define
  `_BRACKET = rf"\[({_MODELOS})(?: \+ dono)? · classe ({_CLASSES})(?: · teto \d+)?\]"`, consumido
  por `SUBTAREFA_HEADER_RE:63` e `TAREFA_HEADER_RE:64`; o docstring do módulo publica a mesma
  gramática em `:12` e `:16`. Cabeçalho fora dela sai `header_valido=False` (`:226`) e o `Item`
  nasce sem `modelo` e sem `classe` (`:225`, `:255-256`) — é o `B3` do gate de delegação. Os grupos
  do `_BRACKET` são **posicionais**: `:229` e `:232` leem `mm.group(3)`/`mm.group(4)`, de modo que
  qualquer grupo **capturante** novo dentro dele desloca os índices e quebra a carga do backlog.
- **`F-7`** — nenhum instrumento, skill ou agente do kit conhece o campo `esforço`: busca por
  `esforço|esforco` em toda a árvore `.claude/` devolveu **nenhuma ocorrência** (medida nesta
  rodada, 2026-09-18). `DM-5` foi aplicada aos seis cards deste plano antes de existir em qualquer
  parser ou doutrina — é exatamente a dependência de ordem que o `AE-5` mediu.

## 4. Decisões (fechadas neste ato — o executor não as reabre)

- **`DM-1`** — `P-0737` passa a `superseded` no registro deste plano; `P-0734` permanece
  `superseded` e suas decisões `DP-*` seguem fonte normativa citável. Nenhum dos dois é retomado.
- **`DM-2` — a unidade de trabalho é o módulo coeso, não a tarefa atômica.** Um card cobre uma
  **disciplina fechada**: um tema, com os seus verbos, os seus testes e a sua verificação ponta a
  ponta no mesmo despacho. O teto de write-clusters do gate de delegação (item 5, "≥8 → dividir")
  **deixa de valer como limite de volume** e passa a valer como limite de **tema**: divide-se
  quando o card cruza dois assuntos, nunca quando cruza oito regiões do mesmo assunto.
- **`DM-3` — coesão é critério de aceite, não só de recorte.** Divergência interna do módulo
  (forma de mensagem, contrato de erro, exit code) é defeito da entrega ainda que cada parte passe
  no seu teste. O reviewer exercita o módulo ponta a ponta (passo 3b do `pantonic-reviewer`).
- **`DM-4` — o que não é do tema continua fora.** Módulo coeso é o oposto de tarefa grande:
  informação transversal ou "aproveitando que estou aqui" segue proibida, e card que a exija é
  card defeituoso.
- **`DM-5` — esforço é declarado no cabeçalho do card**, junto de modelo e classe:
  `### <ID> — <título> [<modelo> · esforço <low|medium|high|xhigh|max> · classe <classe>]`. Quem
  despacha aplica; quem executa calibra a profundidade à classe. Cabeçalho sem os três campos é
  tarefa fora da gramática e cai em `B3`.
- **`DM-6` — o executor nunca busca a próxima tarefa.** O card despachado é o contexto inteiro
  dele: não abre o diário para ver o que vem depois, não roda `backlog.py next`, não lê o plano
  além do próprio card e das seções citadas nominalmente. Já publicado em
  `.claude/agents/pantonic-executor.md` (seção "A tarefa que você recebeu é todo o seu mundo").
- **`DM-7` — a correção do denominador de ocupação está feita e não se refaz** (`ocupacao.py`,
  `PANTONIC_CONTEXT_TOKENS_MAX`, teste atualizado). Este plano a **usa** como premissa.
- **`DM-9` — o `scrum-master` fecha primeiro; o `P-0739` fecha depois, numa rodada única.** A
  ordem não é negociável e é a razão de ser do plano: enquanto a baseline do loop não estiver
  fechada (`LM-T1`..`LM-T4`), rodar o `P-0739` só reproduz os seis defeitos medidos na §3. O
  `P-0739` **não** avança por conta própria nesse intervalo — nem a `BKL-T5`, nem a rodada do
  `AE-10`. Ele é reagrupado em módulos pela `LM-T5` e fechado em rodada única pela `LM-T6`.
- **`DM-10` — o *diretório* `.claude/estado/` é canônico do framework; o *conteúdo* dele não.**
  (Decisão da rodada `RP-1`, 2026-09-18, sobre o `AE-2` — **técnica**, não escalada.) O `.gitignore`
  deixa de excluir o diretório e passa a excluir só o conteúdo, com a exceção do `.gitkeep`:
  `.claude/estado/*` seguido de `!.claude/estado/.gitkeep`, e o comentário reescrito para afirmar
  as duas coisas na mesma voz — o **slot** é do framework, a **sessão** é da máquina. O literal
  exato das linhas velhas e das novas está no card da `LM-T1`, que é a residência única dessa
  transcrição. Razões: (i) a garantia de existência do diretório passa a ser **estática e
  verificável por `git`**, em vez de depender de um passo em prosa do `scrum-master` ter rodado — e
  o defeito 1 da §3 é exatamente um passo em prosa que nunca rodou sem ninguém notar; (ii) o idioma
  já existe no repositório (`F-2`), então nada de convenção nova entra; (iii) nenhuma afirmação da
  `T55` cai — `tarefa-corrente.json` continua ignorado e o hook continua tratando ausência de
  estado como silêncio (`F-3`). **Rotas descartadas:** manter o ignore e migrar a garantia para o
  runtime do Passo 4 — a verificação viraria grep de prosa em `SKILL.md`, **sem poder
  discriminante**, porque o diretório existe na máquina de quem executa nos dois mundos (é o que
  torna o TF "`.claude/estado/` existe" do card velho inútil); versionar um `README.md` no lugar do
  `.gitkeep` — mesmo efeito, mais um arquivo para os listadores tratarem. A garantia em runtime
  **não** é abandonada: ela vira a linha literal do Passo 4 no entregável (c) da `LM-T1`, como
  segunda trava, e não como a trava única.
- **`DM-11` — `rdo.py close --tokens-k` passa a `float` e grava uma casa decimal.** (Decisão da
  mesma rodada; fecha um ponto que a `LM-T1` deixava em aberto — "o mesmo tipo" não dizia qual
  implementação.) Em `.claude/tools/rdo.py:772` o `type=int` vira `type=float`; em `:675` o valor
  passa a ser renderizado como `f"{args.tokens_k:.1f}"`, a **mesma forma** que
  `telemetria_hook.montar_args_append:152` já produz para `telemetria.py append` (`F-4`). Nenhuma
  importação cruzada entre `rdo.py` e `telemetria.py` se cria: a coerência exigida por `DM-3` é
  sobre o **literal aceito e gravado**, não sobre uma função compartilhada — e o par de CLIs não
  tem outra pergunta em comum que justificasse acoplá-los.
- **`DM-12` — o bloqueio da `LM-T1` é de *aceite*, não de rota; a cláusula do segundo bloqueio não
  se aplica, e a tarefa vai a `review`.** (Decisão da rodada `RP-2`, 2026-09-18, sobre o `AE-4` —
  **técnica**, não escalada.) Três partes, todas fechadas aqui.
  **(i) Veredito sobre a cláusula.** `G-REPLAN` mandava tratar segundo bloqueio `premissa` na mesma
  tarefa como premissa caída por inteiro (`superseded`). O fato medido a contradiz: a entrega da
  `LM-T1` **existe na árvore e passa** (145 testes, `.gitignore:11-12` na ordem prescrita,
  `.gitkeep` criado, `rdo.py` e os dois arquivos de teste editados — `AE-4`), o que confirma a rota
  de `DM-10`/`DM-11` em vez de derrubá-la. O que falhou foram duas linhas de `Verificação` do card,
  insatisfazíveis por comportamento documentado do `git`. A cláusula, como estava redigida, contava
  bloqueios e não distinguia rota inviável de card mal redigido — por isso foi **emendada** em
  `GOVERNANCA.md` §7 item 17 com o teste que discrimina ("existe entrega que satisfaz o entregável
  sob as decisões vigentes?": não existe → rota → `superseded`; existe → aceite → corrige-se a
  redação), mais dois tetos anti-abuso (terceiro bloqueio `premissa` na mesma tarefa é `superseded`;
  segundo bloqueio de aceite sobre a **mesma** verificação já reescrita é `superseded`). O plano
  **não** vira `superseded`.
  **(ii) Forma correta das verificações 3 e 5.** A pergunta "o caminho está ignorado?" é binária e
  se faz com a flag binária: `git check-ignore -q <path>` e o **exit code** (`1` = não ignorado, que
  é o efeito pretendido por `DM-10`). `git check-ignore -v` é diagnóstico e reporta o padrão
  decisivo **inclusive quando é negação** — imprime `.gitignore:12:!.claude/estado/.gitkeep` e sai
  `0`, e exigir dele "não imprimir linha nenhuma" é exigir o impossível. Para listar arquivo dentro
  de diretório não rastreado, `git status --porcelain` **colapsa o diretório** (`?? .claude/estado/`)
  e só o `-uall` produz o literal por arquivo. As duas verificações passam a usar `-q` + exit code e
  `--porcelain -uall`, com os literais **medidos** no `AE-4`, e a contingência 1 do card passa a ler
  o exit code em vez da saída de `-v`.
  **(iii) Disposição da `LM-T1`: `review`, não `ready`.** A entrega material existe, está completa e
  verde; `review` é exatamente "o entregável existe e aguarda aceite ou feedback de correção"
  (vocabulário de status da skill `diario-de-obras`). `ready` mandaria um executor novo refazer, em
  uma janela inteira, trabalho já feito — e ele chegaria a arquivos já modificados, caso que o card
  não prevê. A transição `blocked` → `review` é **legítima sem retorno novo de executor** porque o
  retorno do executor já ocorreu: ele produziu a entrega inteira e só então acionou a contingência 1
  do card; o que a rodada trocou foi o **critério contra o qual a entrega será julgada**, não a
  entrega. Quem julga a árvore contra o dossiê corrigido é o `pantonic-reviewer`, que é o que
  `review` significa. A transição foi publicada na tabela de transições da skill `diario-de-obras`
  (autoria do planejador, gatilho 1 — o `scrum-master` invoca o reviewer) para que o loop não
  improvise status, e o ramo `review` entrou na saída (c) do `G-REPLAN`.
- **`DM-13` — a gramática de cabeçalho que um plano *escreve* é a que os instrumentos *parseiam*;
  a aplicação de `DM-5` aos cards vem depois da publicação dela nos parsers.** (Decisão da rodada
  `RP-3`, 2026-09-18, sobre o `AE-5` — **tática**: ordem de tarefas dentro do plano vigente, nada
  escalado.) `DM-5` segue viva e intocada — esforço é campo do card, quem despacha aplica, quem
  executa calibra. O que esta decisão fixa é **quando** e **onde** ela se aplica. Três partes.
  **(i) Os seis cards deste plano voltam à gramática de dois campos, e o esforço vira campo do
  corpo.** O cabeçalho passa a `### <ID> — <título> [<modelo>[ + dono] · classe <classe>]` e o
  esforço desce para o campo `- **Esforço:** <low|medium|high|xhigh|max>`, logo abaixo do `Status`.
  Nada do conteúdo de `DM-5` se perde: o esforço continua declarado no card, que é o contexto
  inteiro do despacho (`DM-6`); muda só a **posição**. Efeito: o Passo 6 volta a produzir hoje, sem
  tocar uma linha de código, sem despachar executor e sem rodar suíte — e o `backlog.py` volta a ler
  os seis cards com `header_valido=True` (`F-6`), que o terceiro campo estava derrubando em
  silêncio.
  **(ii) Quem ensina os dois parsers é a `LM-T4a`, tarefa nova, antes da `LM-T4`.** A gramática de
  três campos entra em `rdo.py` e em `backlog.py` com o campo de esforço **opcional** — todo o
  corpus legado continua casando —, e só depois a `LM-T4` a publica na doutrina e a `LM-T5` a
  aplica aos cards do `P-0739`. A ordem é a decisão: parser, doutrina, cards; nunca cards primeiro.
  **(iii) Os seis cards deste plano ficam na forma (i) até o plano fechar.** Nenhuma tarefa os
  re-migra para três campos: re-migrar não entrega nada e paga outra rodada. A `LM-T5` afere o
  cabeçalho pela gramática vigente **na data do card**, não pela forma final (critério (iii) da
  rubrica, reescrito no mesmo ato).
  **Rotas descartadas** (as quatro da entrada do `AE-5`): (A) ensinar a gramática nova **agora**,
  como micro-entregável da `LM-T1` ou card antes da revisão — realoca alvo entre cards, gasta uma
  janela inteira de executor e sairia desta rodada com `Verificação` **não medida**, que é o defeito
  que a `RP-2` acabou de corrigir; (B) escotilha `--esquema-legado --modelo --classe` no
  `review_evidence.py` — também é código e janela de executor, carimba de *legado* um plano vivo e
  obriga três flags manuais em **todo** despacho de revisão deste plano, sem tocar o parser irmão
  (`F-6`), que continuaria devolvendo `header_valido=False`; (C) reordenar `LM-T3`/`LM-T4` à frente
  da `LM-T1` — não destrava nada, porque os cabeçalhos **delas** carregavam o mesmo terceiro campo e
  o Passo 6 delas falharia igual, e ainda deixa uma entrega verde pendurada; (D) reverter `DM-5`
  "não aplicada", com o esforço viajando só no despacho — perde o dado no card, que é o que `DM-6`
  proíbe. O que esta decisão faz é o (D) **sem** a perda: reverte a posição, preserva o campo.
- **`DM-8`** — os ajustes de `pantonic-executor` (`DM-5`, `DM-6`, módulo coeso) e de
  `pantonic-reviewer` (reconciliação de árvore, exercício ponta a ponta) foram publicados no ato
  do planejamento, em 2026-09-18. As tarefas abaixo **não** os reimplementam; a `LM-T5` os afere.
- **`DM-14` — no corpo do card, o vocabulário é o do esquema `DP-C`; "tema" fica na prosa.**
  (Decisão da rodada `RP-4`, 2026-09-18, sobre o `AE-6` — **técnica**, não escalada.) O campo
  `- **Tema:**` é **renomeado** para `- **Objetivo:**` nos sete cards; não coexistem. O conteúdo é o
  mesmo, linha por linha: renomear não perde nada, e duas enunciações do mesmo campo criariam
  residência dupla. A palavra "tema" continua viva onde ela é doutrina — em `DM-2`, `DM-4` e no
  critério (ii) da rubrica da `LM-T5` —, porque lá ela é **prosa sobre coesão**, não rótulo lido por
  máquina. Junto com o rótulo, esta decisão fecha os outros três desvios do mesmo esquema que a
  re-derivação do `AE-6` mediu em `rdo.py` e que o achado não tinha visto:
  **(i)** `rdo.py:262-268` exige **exatamente um** entre `Arquivos-alvo` e `Entregável`; `LM-T1`,
  `LM-T2`, `LM-T3` e `LM-T4` traziam os dois. Prevalece `Arquivos-alvo`, porque é dele que o
  `review_evidence.py` recorta o diff por arquivo (`review_evidence.py:109`, `:277`), e o texto do
  outro passa a viajar no campo `- **Produto do módulo:**` — rótulo fora do conjunto canônico, que o
  parser guarda como extra e nenhuma linha se perde. `LM-T5` e `LM-T6` seguem só com `Entregável`:
  não produzem diff de arquivo-alvo.
  **(ii)** `rdo.py:258` exige `pronto-quando`; `LM-T2`, `LM-T3` e `LM-T4` não tinham o campo e
  `LM-T5`/`LM-T6` o chamavam `Critério de pronto`, que normaliza para outra chave. Os dois últimos
  são renomeados; os três primeiros ganham o campo, derivado do que já estava escrito em
  `Produto do módulo`, `Testes` e `Verificação` — nenhum critério novo entra.
  **(iii)** `rdo.py:258` exige `verificacao`; em `LM-T4` o rótulo estava fora da gramática de
  `_CAMPO_RE` (`- **Verificação** (…):`, com o `:` fora do negrito, que o parser não lê como campo),
  e `LM-T5`/`LM-T6` não tinham o campo. `LM-T4` recebe a pontuação certa, sem alterar as três
  verificações medidas da `RP-2`; `LM-T5` e `LM-T6`, por serem `classe investigacao` sem artefato
  executável, recebem verificação **por efeito no arquivo**, na forma que a anatomia de card prevê.
  Nada disso muda rota, escopo, ordem, disposição de tarefa ou uma linha da entrega da `LM-T1`.

- **`DM-15` — o domínio das métricas de consumo é o mesmo nos dois verbos do pacote de fechamento,
  e a recusa tem a mesma forma.** (Decisão da rodada `RP-5`, 2026-09-18, sobre o `AE-8` —
  **técnica**, não escalada.) A `DM-11` fica **intocada**: tipo e forma gravada de `--tokens-k`
  seguem como estão, e a entrega da `LM-T1` não se refaz (`DB-23`, sem retroação). O que faltava à
  `DM-11` é a **guarda** — e guarda é do módulo inteiro, não de um argumento. Quatro partes.
  **(i) O domínio, por campo, idêntico nos dois CLIs.** `tool_uses`: **inteiro não negativo**.
  `tokens_k` e `duracao_s`: **número finito não negativo** — `nan` e `inf` ficam **fora** do
  domínio nos **dois** verbos (hoje os dois os aceitam e os gravam na série; medido na rodada).
  **(ii) A recusa, na mesma forma.** Corpo de mensagem idêntico, prefixo do instrumento diferente:
  `rdo: FALHOU - <campo>: '<valor>' <razão>` e `telemetria: FALHOU - <campo>: '<valor>' <razão>`,
  **exit 1** nos dois, com `<razão>` no vocabulário fechado `não é inteiro` · `não é numérico` ·
  `é negativo` · `não é finito` — as três primeiras já são literais vivos de
  `telemetria.py:58-80`; a quarta é nova e entra nos dois. Consequência no `rdo.py`: os **três**
  argumentos de consumo deixam de ser validados pelo `type=` do `argparse` — que produz **exit 2**
  e bloco de `usage`, forma que o irmão não tem e que nenhuma orquestração consegue distinguir de
  erro de digitação — e passam a ser validados em código, como `RdoValidationError`.
  **(iii) A guarda corre antes de qualquer outra checagem de `cmd_close`.** Argumento fora do
  domínio é recusado antes da checagem de `--plano`, do template e do destino. Efeito deliberado:
  a verificação do contrato de erro fica **barata e sem efeito em disco**, e a mensagem que sai é
  a do domínio, nunca a de plano inexistente — é o que dá poder discriminante à `Verificação` da
  `LM-T1a`.
  **(iv) Nenhuma importação cruzada** entre `rdo.py` e `telemetria.py`: a cláusula da `DM-11`
  continua valendo palavra por palavra. A coerência exigida por `DM-3` é sobre **domínio aceito** e
  **literal de recusa**; cada CLI a implementa na própria casa, e o que tranca o par são os testes
  espelhados da `LM-T1a`.
  **Extensão além do `AE-8`, apurada na rodada (o achado era indício, não apuração):** o `AE-8`
  relatava a divergência só em `--tokens-k` e afirmava que `telemetria.py` recusa "não-numérico" —
  as duas metades estão **incompletas**. Medido: (a) `telemetria.py append` **aceita** `nan` e
  `inf` e os grava literalmente na série, porque `float("nan") < 0` é falso
  (`_validar_numero_nao_negativo`, `telemetria.py:70-80`); (b) a divergência vale igual para
  `--tool-uses` (`-1` aceito pelo `rdo.py`, recusado pelo irmão) e para `--duracao-s` (`-60`
  idem); (c) **na direção contrária**, `rdo.py close --duracao-s` é `type=int` e **recusa com exit
  2 o literal que o próprio hook emite** para o irmão (`telemetria_hook.montar_args_append:153`
  escreve `f"{duracao_s:.1f}"`, e a série já tem `1020.648`, `104.928`): o mesmo número medido
  continua não passando nos dois, que é o defeito 3 da §3 ainda aberto depois da `DM-11`. Por isso
  a decisão é sobre os **três** campos, e não sobre `tokens_k`. A tabela de divergência medida, com
  um comando por linha, é **residência única** do card da `LM-T1a`.
  **Rotas descartadas:** (A) função de validação compartilhada, importada de um dos módulos pelo
  outro — proibida pela `DM-11`, e o par de CLIs não tem outra pergunta em comum que justificasse o
  acoplamento; (B) manter `type=float`/`type=int` no `argparse` e só acrescentar a guarda de sinal —
  deixaria `abc` saindo **exit 2** no `rdo.py` contra **exit 1** no irmão, isto é, resolveria o
  domínio e manteria a divergência de contrato de erro, que é justamente o objeto do `AE-8`;
  (C) alinhar pelo outro lado, fazendo `telemetria.py` recusar decimal em `duracao_s` — contradiz o
  literal que o hook já emite e que a série já contém; (D) normalizar a forma gravada nos dois
  (ex.: `1e3` → `1000.0` também no TSV) — `telemetria.py:79-80` preserva a forma original de
  propósito, com teste vivo, e nada no `AE-8` pede isso: fica **fora**, nominalmente.
- **`DM-16` — o papel que publica comando de aceite tem a ferramenta que o roda; `pantonic-planner`
  passa a ter `Bash`.** (Decisão do **dono**, 2026-09-18, item 5 da *Diretiva de execução do
  `P-0740`*, materializada pela rodada `RP-5`; o consultor **não a reabre**.) Quatro partes.
  **(i) O ato.** O frontmatter de `.claude/agents/pantonic-planner.md` passa a
  `tools: Read, Glob, Grep, Write, Edit, Bash` — o alinhamento que o dono pediu com todas as
  palavras: *planner e executor acessando a mesma ferramenta de validação*. Estado medido antes:
  `pantonic-executor` sem linha `tools:` (toolset aberto, inclui `Bash`), `pantonic-reviewer` com
  `Bash`, `pantonic-consultant` com `Bash`, `pantonic-planner` o **único** sem execução.
  **(ii) A consequência sobre a `DM-12`.** A `DM-12` segue viva e com a redação que tem; deixa de
  ser inexequível pelo papel a que se dirige. A partir desta decisão, "comando de aceite não se
  deduz, se roda" é exigível de **quem publica o card** — `pantonic-planner` e `pantonic-consultant`
  —, e `Verificação` publicada sem execução medida é **defeito de autoria**, aferido pelo critério
  (vii) da rubrica da `LM-T5`, que já está escrito. Nenhuma linha da `DM-12` é reescrita: a
  residência desta mudança é esta decisão.
  **(iii) O residual da `RP-4` fica fechado.** Aquela rodada registrou que rodou sem ferramenta de
  execução e que a orquestração teve de rodar os sete comandos por ela. Com `Bash` no papel, o
  arranjo deixa de existir; a rodada `RP-5` já operou assim (todo número publicado aqui foi medido
  nesta janela).
  **(iv) Projeção canônica no mesmo ato.** Definição de agente tem duas projeções versionadas —
  `.claude/README.md` (região marcada, regenerada por `kit_check -Mode generate`) e a tabela
  **Agentes** de `README.md` › *Anatomia do kit* (conferida por `check-readme.ps1`). As duas estão
  **vermelhas hoje** por atos do dono fora de ciclo de tarefa (`DM-8` reescreveu as descrições de
  executor e reviewer; o `pantonic-consultant` foi criado em 2026-09-18) — medido nesta rodada:
  `check-drift` **exit 1** com 6 problemas, `check-readme.ps1` **exit 1** com 1 problema. Quem toca
  a superfície fecha a projeção dela: a `LM-T7` regenera a primeira e acrescenta a linha que falta
  na segunda. **Rotas descartadas:** deixar as duas projeções para a `LM-T4` — ela tem `check-drift`
  exit 0 na `Verificação` 1 e **não o obtém hoje**, isto é, herdaria um aceite insatisfazível, que é
  a classe de defeito do `AE-4`; abrir card só para as projeções — mesmo tema, mesma superfície,
  mesma janela, e `DM-2` manda não partir o que é um assunto só.

- **`DM-17` — `.claude/agents/` é superfície de **ato do dono** nesta execução; card do plano
  não a declara em `Arquivos-alvo`.** (Decisão do escalonamento `ESC-1`, 2026-09-18,
  `pantonic-consultant`, sobre o `AE-11` — **tática**, nada escalado além do que já é do dono.)
  Cinco partes.
  **(i) O fato.** O `Edit` que gravaria `tools: ... , Bash` em `.claude/agents/pantonic-planner.md`
  foi **negado duas vezes pela camada de permissão do harness**, com instrução explícita de parar
  e explicar em vez de contornar. O executor parou no passo 1 (4 tool uses / 59,5k tk, **nenhum
  arquivo tocado**) — conduta correta de `G-EXECREADY`. **Não é defeito do card:** as quatro
  âncoras publicadas pela `RP-5` foram re-derivadas no despacho e bateram exatamente.
  **(ii) A regra.** Enquanto a permissão não for liberada por ato do dono, **nenhum card deste
  plano declara `.claude/agents/*` em `Arquivos-alvo`**. O que precisa ser publicado ali entra na
  fila de **atos do dono** (`LM-T8`), com o texto **literal** pronto no card, de modo que o ato
  seja transcrição e não autoria. Contornar por `Write`, `Bash` ou por outro agente é **lavagem
  de permissão** e está proibido para todos os papéis, **inclusive o consultor**.
  **(iii) O corte do módulo.** A `LM-T7` se parte pela **fronteira da permissão**, não pelo tema:
  projeções (despachável) × definição de agente (ato do dono). É o único corte que `DM-2` admite
  aqui — card cujo passo 1 é inexecutável não é módulo, é bloqueio, e os dois pedaços vivem em
  mundos de execução diferentes. O tema continua um em cada card.
  **(iv) `DM-12` no intervalo.** Sem `Bash`, o `pantonic-planner` segue inexequível quanto ao
  dever de rodar o aceite (`AE-7`, que a `DM-16` resolveu **em decisão** e a `LM-T8` ainda não
  pôde materializar). Até a `LM-T8` fechar, o dever é de **quem publica com ferramenta**: o
  `pantonic-consultant` (que conduz as rodadas de reparo desta execução) ou o `scrum-master`, que
  roda o comando no despacho e anexa a saída medida ao dossiê. Card autorado por planner com
  `Verificação` **não medida** não se despacha como está — mede-se antes. A rubrica da `LM-T5`
  **não muda**: o critério (vii) afere o **card publicado**, não o papel que o escreveu.
  **(v) Efeito na `LM-T4`.** `.claude/agents/pantonic-planner.md` sai dos `Arquivos-alvo` dela —
  medido na `ESC-1`: o arquivo **não** contém a régua antiga, a única ocorrência viva de
  `>8 write-clusters` nas seis superfícies é `.claude/skills/proximo-passo/SKILL.md:126` —, e a
  publicação da gramática nele vira o item (b) da `LM-T8`, depois da `LM-T4`. A dependência
  `LM-T4` → `LM-T7` **continua satisfeita** pela parte despachável: o `check-drift` exit 0 depende
  só da regeneração da projeção, medida.

- **`DM-18` — o item enumerado e a frase que o conta fecham no **mesmo** card; e verificação
  que não discrimina o invariante não é aceite.** (Decisão do escalonamento `ESC-2`, 2026-09-18,
  `pantonic-consultant`, sobre o `AE-12` — **tática**, nada escalado.) Cinco partes.
  **(i) Regra de autoria.** Card que acrescenta, remove ou renomeia **item de lista ou de tabela
  enumerada** fecha, no mesmo ato, **toda afirmação da mesma seção que conta ou qualifica esse
  conjunto**. A prosa que anuncia a tabela é parte do entregável, não vizinhança dele: quem mexe
  no conjunto responde pelo que a seção **afirma** sobre o conjunto.
  **(ii) Regra de aceite.** Se o instrumento que julga a seção **não** discrimina essa afirmação,
  a tarefa que fecha o item **estende o instrumento** — senão o verde do guarda é falso conforto.
  Caso medido: `check-readme.ps1` confronta tabela × disco, **anuncia `9 agente(s)`** e sai
  **exit 0** com a prosa duas linhas acima dizendo "oito". Cinco verificações verdes e o
  arquivo-alvo contradizendo a si mesmo.
  **(iii) Residência da lição.** Critério **(viii)** da rubrica de criação de tarefa, publicado
  pela `LM-T5` em `docs/RUBRICA_DE_REVISAO.md` — superfície **acessível** — e apensado ao item
  (b) da `LM-T8` para a publicação em `.claude/agents/pantonic-planner.md`, que é ato do dono
  (`AE-11`, `DM-17`). **Não se abre card para superfície inacessível**, e a lição não fica
  esperando o ato: ela já é exigível pela rubrica.
  **(iv) Sem retroação.** A `LM-T7` fica `done` com ressalva 90%: a entrega foi fiel ao card, e o
  defeito é de **autoria** — quem escreveu o card (este consultor, na `ESC-1`) prescreveu a linha
  da tabela e não a frase que a conta. O reparo mora na `LM-T7a`, card novo.
  **(v) Fronteira do invariante.** Entram na checagem as **duas** contagens que o script já
  calcula: agentes e skills. "Verificadores executáveis" e "declaração de projeções" ficam
  **fora**, nominalmente — não existe contagem deles em instrumento nenhum hoje, e autorar a
  gramática de uma contagem sem fato medido é o defeito que a `RP-1` já pagou.

- **`DM-19` — a função de atribuição **já tem residência**; a `LM-T2` consome um **comando**, e
  o módulo dela se parte em três.** (Decisão do escalonamento `ESC-3`, 2026-09-18,
  `pantonic-consultant`, sobre o `AE-14` — **tática**, nada escalado.) Quatro partes.
  **(i) A residência, medida.** A pergunta "este arquivo é da entrega ou é alheio?" já está
  implementada, inteira, em `confrontar_escopo` (`.claude/tools/review_evidence.py:282-333`),
  com os cinco baldes da `DB-25`/`DB-32`. **Nenhum módulo novo se cria** e nenhuma segunda
  implementação nasce — era isso que a `LM-T2` antiga mandava o executor decidir, e decidir é do
  planejamento (`CLAUDE.md` global, Regra 8).
  **(ii) O que falta é exposição.** `B0`/`B1` são **prosa** lida pelo `scrum-master`: o loop não
  importa função, ele **roda comando**. A `LM-T2a` acrescenta a flag `--atribuir` ao CLI que já
  consome aquelas funções, sem lógica de classificação nova; a `LM-T2` cita o comando na regra.
  **(iii) O corte, por sujeito.** Três cards: `LM-T2` (prosa do loop, `.claude/skills/scrum-master/SKILL.md`),
  `LM-T2a` (o verbo, `review_evidence.py`) e `LM-T2b` (o hook, `telemetria_hook.py`). Cada um
  tem **um** arquivo-alvo de produção e um sujeito testável próprio — ou a declaração explícita
  de que não tem (a `LM-T2`, que é redação).
  **(iv) Efeito na `LM-T3`:** ela **deixa de depender da `LM-T2`**. A frase "a mesma função que a
  `LM-T2` entrega, importada, não copiada" se satisfaz trivialmente, porque a `LM-T3` edita o
  **próprio** módulo onde a função mora. Fica no lugar da dependência uma **exclusão mútua** com
  a `LM-T2a` sobre `review_evidence.py`. Uma pergunta, uma implementação, três consumidores: o
  dossiê (`LM-T3`), o verbo (`LM-T2a`) e a prosa do loop (`LM-T2`).
- **`DM-20` — o `tokens_k` do hook é o `usage` da **última** mensagem, não a soma por
  `message.id`.** (Decisão do `ESC-3`, sobre o `AE-3` — **técnica**, não escalada.) A fórmula foi
  **calibrada**, não deduzida: seis transcripts reais desta janela, confrontados com o `<usage>`
  da notificação, e a última mensagem acerta **seis de seis**, enquanto a soma por `message.id`
  reproduz exatamente os seis valores inflados que o hook gravou. Causa identificada:
  `cache_read_input_tokens` é o contexto **inteiro** relido a cada turno — somá-lo turno a turno
  multiplica o total pelo número de turnos, e por isso o erro cresce com a tarefa (4,2× num
  despacho de 4 tool uses; 37× num de 96). A dedupe por `message.id` que o `T55` instalou
  **continua satisfeita** pela fórmula nova: com uma única mensagem, soma-por-id e
  última-mensagem coincidem. `tool_uses` e `duracao_s` ficam intocados — conferidos contra a
  notificação e corretos. A tabela de calibração é **residência única** do card `LM-T2b`.
  **Fora do alcance do código, registrado:** o `SubagentStop` **não dispara** quando o subagente é
  retomado por `SendMessage` (medido: os escalonamentos `ESC-1` e `ESC-2` não geraram linha). A
  compensação é de prosa — o Passo 9 manda o loop apender a linha —, não de instrumento.

- **`DM-21` — exigência **estrutural** não vira teste comportamental: ou vira o caso que só a
  implementação certa acerta, ou vira inspeção mecânica na `Verificação`, ou sai do card como
  `Restrição` declarada.** (Decisão do escalonamento `ESC-4`, 2026-09-18,
  `pantonic-consultant`, sobre o segundo achado do laudo da `LM-T3` — **tática**, nada escalado.)
  Quatro partes.
  **(i) O fato.** O card da `LM-T3` exigia `TR a seção nova chama \`confrontar_escopo\` e **não**
  reimplementa a classificação`. O reviewer mediu que **nenhum** dos três testes discrimina isso:
  uma reimplementação fiel da cobertura passaria em todos. Exigência sem poder discriminante é
  exigência que o laudo tem de marcar — e marcou.
  **(ii) As três saídas legítimas, nesta ordem de preferência.** (a) **Caso discriminante** —
  escolher a entrada em que a implementação certa e a reimplementação plausível **divergem**;
  para a pergunta de atribuição, essa entrada é o **alvo-diretório**, que casa por prefixo e que
  qualquer cópia por caminho exato erra. (b) **Inspeção mecânica** — `Select-String`/contagem com
  literal e valor esperado, publicada como linha de `Verificação`, nunca como teste `pytest`.
  (c) **Fora do card** — declarar como `Restrição`, sem prometer teste: honesto e barato.
  **(iii) Varredura medida no `ESC-4`.** Os cards vivos **não** têm outro TR estrutural — a única
  ocorrência do idioma no plano é a citação histórica dentro da `DM-19` (iv). O que havia era uma
  `Restrição` sem discriminante na `LM-T2a` (o primeiro balde obtido por diferença de conjuntos),
  fechada aqui pela saída (a): um teste novo de alvo-diretório sobre o verbo.
  **(iv) Residência da lição.** Critério **(ix)** da rubrica de criação de tarefa, publicado pela
  `LM-T5`, e apensado ao item (b) da `LM-T8` para a definição do planner (ato do dono) — a mesma
  rota da `DM-18` (iii), pela mesma razão: a superfície acessível recebe agora, a inacessível
  espera o ato sem travar a lição.

- **`DM-22` — o contrato de **falha** é do **módulo**, não do verbo: entrada inválida sai pelo
  mesmo canal, com a mesma forma de mensagem, em todos os verbos do instrumento.** (Decisão do
  escalonamento `ESC-5`, 2026-09-19, `pantonic-consultant`, sobre o `AE-17` — **técnica**, não
  escalada.) É a `DM-15` generalizada: lá o par era `rdo.py close` × `telemetria.py append`, aqui
  são dois verbos do **mesmo arquivo**, e o defeito é idêntico — a guarda mora no caminho de um
  verbo e o outro a pula. Três partes.
  **(i) A regra.** Verbo novo em instrumento existente herda a borda do instrumento: guarda de
  argumento com **residência única**, uma função chamada por todos os ramos, nunca duplicada e
  nunca embutida no caminho de um só. Card que acrescenta verbo declara, na `Verificação`, o
  **mesmo** argumento inválido rodado nos **dois** ramos — é o que teria pego o `AE-17`.
  **(ii) O que discrimina.** Medido no `ESC-5`: os dois ramos saem **exit 1** com plano
  inexistente; um por mensagem do módulo, outro por traceback de `FileNotFoundError`. **O exit
  code não discrimina** — a afirmação de aceite é sobre o **stderr**, como já era na `LM-T1a`
  (`DM-15` (iii)).
  **(iii) Residência do reparo:** a `LM-T3a`, que já é da mesma borda do mesmo módulo e ainda não
  rodou — não se abre card novo para acrescentar cinco linhas ao arquivo que um card aberto já
  vai tocar. O assunto do card passa a ser, nominalmente, **a borda do instrumento de evidência**
  (falha e recorte), e não dois assuntos colados: os dois defeitos são promessas que o
  instrumento faz na **entrada** e na **saída** da mesma pergunta.
- **`DM-23` — piso de regressão não é número no card; é **relação**, re-medida no despacho.**
  (Decisão do `ESC-5`, sobre o `AE-18` — **tática**, nada escalado.) Quatro partes.
  **(i) O fato, com a série inteira.** Nesta janela o total da suíte andou **145 → 153 → 156 →
  161 → 165** em seis tarefas, e o piso escrito nos cards envelheceu **cinco vezes em sete
  despachos** — `LM-T7a` (145→153), `LM-T3` (145→153), `LM-T4a` (153→156), `LM-T2a` (156→165,
  mais a baseline de arquivo 28→32). Todas corrigidas à mão pelo `scrum-master` no despacho. A
  causa não é desatenção de quem autorou: é **estrutural** — o número é medido no planejamento e
  consumido depois de outras tarefas da **mesma janela** terem fechado. Card que roda em série
  atrás de outros não pode carregar o total da suíte como constante.
  **(ii) A forma que substitui o número.** A linha de `Verificação` passa a afirmar uma
  **relação**: `python -m pytest tests/ -q` verde, **sem número fixo de piso** — o piso é o total
  que a árvore tiver **no despacho**, re-medido por quem despacha e registrado no dossiê; a
  entrega **soma os `<N>` testes novos** e **não reduz** esse total. O que o card fixa é o que
  não envelhece: o **delta** e os **nomes** dos testes novos.
  **(iii) O número não some, muda de estatuto.** Continua no card como **referência histórica,
  não como aceite**, com data e rodada (`165 passed` em 2026-09-19, `ESC-5`) — serve para quem
  despacha perceber deriva grande, e não para reprovar entrega.
  **(iv) Onde se aplica.** Agora, nos quatro cards vivos que ainda carregavam número
  (`LM-T2`, `LM-T2b`, `LM-T3a`, `LM-T4`); como critério **(x)** da rubrica da `LM-T5`; e no item
  (b) da `LM-T8` para a definição do planner. **Não** se aplica retroativamente a card `done`
  (`DB-23`). A mesma regra vale para baseline **por arquivo de teste** (`28 passed`), que
  envelhece pela mesma razão.

- **`DM-24` — o literal de um comando de aceite é o que foi **colado e rodado**; markdown
  inline não preserva literal.** (Decisão do escalonamento `ESC-6`, 2026-09-19,
  `pantonic-consultant`, sobre o `AE-19` — **tática**, nada escalado.) É a cláusula que faltava à
  `DM-12` ("comando de aceite não se deduz, se roda"): rodar **o comando** não basta se o que vai
  para o card é uma **transcrição** dele. Quatro partes.
  **(i) Forma de publicação.** Comando cujo literal contenha **crase**, **asterisco** ou
  **barra invertida** publica-se em **bloco cercado**, nunca em code span de uma linha — em code
  span a crase encerra o span e a transcrição vira outro literal. Foi assim que
  `| `B0` |` virou `| ``B0`` |` na `Verificação` 1 da `LM-T2`: um padrão que devolve **0 antes e
  0 depois**, isto é, que não discrimina mundo nenhum.
  **(ii) Padrão textual usa `-SimpleMatch`.** Salvo quando o regex é **deliberado e rodado**, todo
  `Select-String` de aceite leva `-SimpleMatch`. Medido no `ESC-6`: `-Pattern '- **Objetivo:**'`
  **sem** `-SimpleMatch` nem sequer executa — `Invalid pattern ... Nested quantifier '*'`; e
  `'roteada ao \*\*planejador\*\*'` executa, devolve 0 nos dois mundos e **parece** aceite.
  **(iii) O teste que fecha a classe inteira: o par de valores.** Toda linha de `Verificação` por
  efeito em arquivo publica **os dois** valores — o de antes e o de depois —, rodados. Padrão que
  devolve o **mesmo** valor nos dois mundos é **inválido por construção**, seja por escape
  (`AE-19`), por negrito inventado (`AE-19`), por regex inválido (`AE-19`) ou por já estar
  satisfeito antes da entrega (`AE-4`). Esta é a formulação geral de que a `DM-18` (ii) e o
  critério (vi) da rubrica eram casos particulares.
  **(iv) Residência da lição.** Critério **(xi)** da rubrica de criação de tarefa (`LM-T5`) e
  item (b) da `LM-T8` para a definição do planner — mesma rota da `DM-18` (iii) e da `DM-21`
  (iv). A `DM-12` **não** é reescrita: esta decisão é a residência da cláusula.

- **`DM-25` — `escalar` não é desfecho de tarefa: é desfecho da **pendência**. O bloco A fecha
  pelo veredito; o bloco B roteia a pendência.** (Decisão do escalonamento `ESC-7`, 2026-09-19,
  `pantonic-consultant`, sobre o `AE-9` — **técnica**, não escalada.) Quatro partes.
  **(i) O buraco, e por que ele é imediato.** O domínio fechado da recomendação tem quatro
  valores; o bloco A cobre três (`refazer` → `A6`, `seguir com ressalva` → `A8`, `seguir` →
  `A9`, mais `reprovado` por veredito em `A7`) e **não cobre `escalar`**. Como o bloco B só é
  avaliado depois de o bloco A dizer "segue", o `B1` que a `LM-T2` acabou de publicar é
  **inalcançável pela sua primeira condição** — a cadência nova não alcança o caso para o qual
  foi escrita.
  **(ii) A regra.** Linha nova `A8a`, entre `A7` e `A8`: com `recomendacao=escalar` e
  `bloqueante=nenhuma`, o RDO fecha **pelo veredito transcrito** (`aprovado` → `aprovado`;
  `ressalva` → `aprovado com ressalva`), cada achado sai com rota como em `A8`, e o fluxo
  **segue** ao bloco B, onde o `B1` registra a pendência como `AE-<n>` e a roteia ao consultor.
  Precedência declarada: `A6` e `A7` vencem `A8a`; `A8a` vence `A8` e `A9`. O caso `escalar`
  **com** bloqueante não precisa de texto próprio — `bloqueante` diferente de `nenhuma` implica
  `veredito=reprovado`, que é `A7`, e isso já está escrito no arquivo.
  **(iii) Por que não se renumera nada.** `A8a` é **sufixo**, pelo idioma que o kit já usa em
  `LM-T4a`/`BKL-T2a`: renumerar `A8`/`A9` invalidaria identificadores já citados em RDOs
  fechados e no diário. Em compensação, **toda** superfície que enumera as regras do bloco A
  entra na mesma entrega — são quatro no mesmo arquivo —, que é a `DM-18` (i) aplicada a si
  mesma: quem acrescenta item à lista fecha o que a seção afirma sobre a lista.
  **(iv) Nenhuma linha de código.** `rdo.py close` recebe `--recomendacao` como texto livre e
  calcula o desdobramento **pelo veredito** (`calcular_desdobramento(args.veredito)`) — isto é,
  o instrumento **já** faz o que a regra prescreve, e o que faltava era a prosa que manda o loop
  fazê-lo sem julgar. Residência: card `LM-T2c`, **antes** da `LM-T4`.

- **`DM-26` — o bloco A parte **primeiro por veredito, depois por recomendação**; e regra de
  roteamento nunca manda fazer o que o instrumento de fechamento recusa.** (Decisão do
  escalonamento `ESC-8`, 2026-09-19, `pantonic-consultant`, sobre o `AE-20` — **técnica**, não
  escalada.) Quatro partes.
  **(i) As duas lacunas são uma só.** A `A8a` (`DM-25`) resolveu `escalar` para entrega
  aprovada, e deixou aberto o caso em que o laudo **reprova e manda escalar**: por um lado a
  tripla (`reprovado`, `bloqueante=nenhuma`, `escalar`) caía em `A8a`, que manda fechar pelo
  veredito — e `rdo.py close --veredito reprovado` sai **exit 2**, `invalid choice` (medido);
  por outro, `escalar` com bloqueante e retentativas = 0 não casava regra nenhuma. É o mesmo
  buraco visto de dois lados: **entrega reprovada cujo laudo pede escalonamento, antes de a
  retentativa ser gasta**.
  **(ii) A regra `A6a`.** `veredito=reprovado` **e** `recomendacao=escalar`, em qualquer
  bloqueante e qualquer contador: **não** fecha RDO (`DP-F` item 3 — `blocked` não dispara RDO),
  **não** gasta retentativa, materializa `blocked` razão `premissa` com a pendência transcrita,
  registra `AE-<n>` e escala ao **consultor**, com a janela seguindo pelo que ele devolver. A
  razão de não refazer antes de escalar é econômica e está medida nesta janela: a retentativa é
  recurso escasso (duas por tarefa), e gastá-la numa rota que o laudo já pediu para rever é o
  erro que o `G-REPLAN` existe para evitar. Precedência: `A6` vence `A6a` (lá o laudo já mandou
  refazer); `A6a` vence `A7` e `A8a`.
  **(iii) O domínio de `A8a` passa a ser o veredito, não o bloqueante.** Condição nova:
  `recomendacao=escalar` **e** `veredito` ∈ {`aprovado`, `ressalva`}. Ela **subsume** a antiga —
  o arquivo já afirma que bloqueante diferente de `nenhuma` implica `veredito=reprovado` — e, de
  quebra, alinha a regra ao domínio que o `close` aceita. **Fecha-se a regra ao instrumento, não
  o contrário:** alargar `--veredito` para `reprovado` seria inventar um fechamento de RDO que a
  `DP-F` não prevê, e o instrumento está certo.
  **(iv) A partição, escrita.** `veredito=reprovado` é decidido por `A6`, `A6a` ou `A7` e
  **nunca** por `A8a`/`A8`/`A9`. Além de fechar o `AE-20`, essa frase fecha um caso que ninguém
  tinha reportado: entrega **reprovada** com recomendação `seguir` cairia hoje em `A9` e seria
  fechada como **aprovada**. Residência: card `LM-T2d`, **antes** da `LM-T4`.

> **`DM-27`..`DM-30` são atos do dono de 2026-09-19**, tomados sobre o relatório de encerramento da
> janela de 2026-09-18/19. Não vieram de rodada de replanejamento nem de escalonamento: são
> decisões de quem é dono da rota, e entram aqui pela mesma porta que a *Diretiva de execução* de
> 2026-09-18.

- **`DM-27` — `.claude/agents/` deixa de ser superfície vedada ao loop.** A permissão que a
  `DM-17` (ii) declarava indisponível foi **concedida pelo dono**. Consequência única e imediata: a
  `LM-T8` sai de `blocked` e vira `ready`, com o item (a) despachável e o item (b) atrás da
  `LM-T4`. Nada mais muda — a `DM-17` (i) e (iii) seguem valendo, e a `LM-T8` continua **fora da
  fila do marco 1**, porque não está no caminho crítico de tarefa nenhuma.
  **Medida no ato, e a correção que ela forçou (`DM-24` aplicada a permissão, não a comando):** a
  primeira varredura dos dois `settings.json` em 2026-09-19 não achou **nenhuma** regra
  `Edit`/`Write` sobre `.claude/agents/**` — só `Read` no global. A concessão do dono valia como
  decisão sem ter superfície onde morar, que é o `AE-11` prestes a se repetir no despacho.
  **Materializada no mesmo dia, por ato do dono**, em `.claude/settings.json`:
  `Edit(/.claude/agents/**)` e `Write(/.claude/agents/**)` no `permissions.allow` do projeto, ao
  lado das quatro regras de skill que já viviam lá. A `LM-T8` é despachável de fato, e não só de
  direito. **Lição, que é do método e não desta tarefa:** permissão concedida em conversa não é
  permissão instalada — mede-se a superfície antes de declarar a tarefa `ready`.

- **`DM-28` — técnica ainda não projetada se executa *ad-hoc*, e a execução ad-hoc é insumo de
  planejamento, não precedente.** Quando uma tarefa exigir uma técnica que o framework ainda não
  tem desenhada, o loop **não para para desenhá-la**: faz ad-hoc, entrega, e a lição do ad-hoc vai
  para o registro de insumo do plano que vai materializar a técnica. O que **não** se admite é o
  contrário — tratar o ad-hoc como doutrina por ter funcionado uma vez: enquanto a técnica não for
  planejada e publicada, ela não é fonte normativa e não se cita como tal. A figura do
  `pantonic-consultant` é o caso-mãe desta decisão, e é por ela que a `DM-30` da *Diretiva* de
  2026-09-18 chamava o agente de provisório.

- **`DM-29` — a lição do consultor tem residência desde já, e um card que a materializa.** Os
  insumos entram em `## 9. Insumos do ad-hoc para planejamento futuro` deste plano, numerados
  `I-<n>`, **conforme forem medidos** — não no fim. O card `LM-T9` os converte em
  `docs/consultant-spec.md`, e é **uma das últimas tarefas do plano**, por ordem do dono: a spec
  se escreve depois que a figura tiver rodado o plano inteiro, não no meio.

- **`DM-30` — o critério de admissão de matéria nova neste plano é coesão, não custo.** Declaração
  do dono em 2026-09-19: *"com os limites expandidos, nossa preocupação agora é a coesão e
  coerência do contexto ao invés de uso"*. Consequências medidas, aplicadas neste ato: (i) a
  `TK-54b` (fonte da bimodalidade de 8.611 tk) **não entra** — é matéria de custo, e o custo
  deixou de ser o critério; segue viva como tíquete despriorizado. (ii) A `TK-38` (comunicação
  agente↔humano) **não entra** — é matéria de coerência, portanto pertinente ao *critério*, mas
  cruza o tema deste plano, e `DM-4` proíbe o "aproveitando que estou aqui"; vai para a fila
  pós-plano com a evidência nova de 2026-09-19 apensada. (iii) O `_CARD-mapa-de-custo-da-janela`
  foi **eliminado** — a matéria dele morreu com a ratificação da `TK-54a` e com esta decisão.

- **`DM-31` — o loop roda em Opus enquanto o `P-0740` não encerrar (inversão registrada da tabela
  do §3).** Ato do dono em 2026-09-19, sobre a parada do Passo 1 do `scrum-master`: *"pode manter
  como opus durante esse plano"*. A tabela vinculante de `GOVERNANCA.md` §3 põe **Sonnet** na
  linha *Orquestração*, e o §3 (penúltimo bullet) admite a inversão **só** com OK explícito e
  registrado do dono — nunca por herança silenciosa. Este bullet **é** o registro, e é o que
  impede a próxima janela de parar de novo no mesmo gate. Alcance: **o contexto principal do loop,
  e só ele, e só até o `P-0740` encerrar**. Não alcança (i) os subagentes — o modelo de cada
  tarefa continua vindo do cabeçalho dela, gramática `[<modelo> · classe <classe>]`, e o despacho
  continua passando esse modelo ao `pantonic-executor`; (ii) nenhum outro plano, que volta ao
  default da tabela. O nudge do hook `modelo_por_fase_userpromptsubmit.py` segue disparando por
  palavra-chave: enquanto valer esta decisão, ele é falso positivo conhecido no loop deste plano.

- **`DM-32` — `reprovado` não é desfecho de RDO: a `A7` se fecha ao instrumento, como a `A8a`.**
  (Decisão do escalonamento `ESC-9`, 2026-09-19, `pantonic-consultant`, sobre o `AE-22` —
  **técnica**, não escalada.) Três partes.
  **(i) A rota (ii) do laudo está descartada.** Dar ao `rdo.py close` um caminho para `reprovado`
  seria (a) inventar um fechamento de RDO que a `DP-F` não prevê — o RDO nasce **só** na
  transição `review` → `done`, e `blocked`/`cancelled` não o disparam (Passo 9, fechamento c) —,
  (b) reabrir, em sentido contrário, o que o `DM-26` (iii) já decidiu para a lacuna irmã
  (*"fecha-se a regra ao instrumento, não o contrário"*), e (c) criar ramo morto na
  `calcular_desdobramento`, cuja docstring ancora a ausência do ramo na própria `DP-F` e no
  `G-DEADCODE`. O instrumento está certo pela terceira vez seguida; quem mente é a `A7`.
  **(ii) A ação nova da `A7`.** Não fecha RDO: materializa a tarefa como `blocked` razão
  `premissa`, com `bloqueante` e pendência do laudo transcritos na razão, registra `AE-<n>` e
  **PARA** — exatamente a forma do `A3b`, e pela mesma substância: duas execuções reprovadas
  derrubam a premissa de que o card é executável como está, o que é matéria de replanejamento e
  não de fechamento. A `A7` **continua** sendo parada de janela, e por isso a linha *"reprovação
  depois da última retentativa (`A7`)"* da seção *O que obriga parada* fica **literal**: nenhuma
  rota do loop muda aqui — só o desfecho que a regra manda materializar. Não se escala ao
  consultor como em `A6a`: lá a retentativa estava intacta e o laudo pedia revisão; aqui o
  recurso já foi gasto até o fim, e a escalada é a do `G-REPLAN`, nomeada no relatório de
  encerramento.
  **(iii) Nenhuma linha de código, e a frase de partição passa a ser verdadeira.** Feita a troca,
  a afirmação que a `LM-T2d` transcreveu — *"nenhuma regra mande fechar o que o instrumento
  recusa"* — deixa de ser falsa sobre a tabela, que é o único defeito que o `AE-22` relata. A
  `LM-T2d` **não se refaz**: está `done` aprovada 100% e entregou o que o card contratou.
  Residência: card `LM-T2e`, **à frente da `LM-T2b`** e, como as duas irmãs, **antes da `LM-T4`**
  (exclusão mútua do `.claude/skills/scrum-master/SKILL.md`).

- **`DM-33` — teste pré-existente que afirma a **saída que o card reescreve** é alvo da tarefa, não
  obstáculo a ela; e a fórmula do `ESC-3` está confirmada, inclusive pela linha que parecia
  exceção.** (Decisão do escalonamento `ESC-10`, 2026-09-19, `pantonic-consultant`, sobre o
  `AE-24` — **técnica**, não escalada.) Quatro partes.
  **(i) O produto (b) fica; a autorização é que estava estreita.** A normalização do modelo para
  minúsculas é o `AE-3` inteiro, e está medida: a série carrega **as duas** grafias do mesmo
  modelo (`Opus` 103 × `opus` 55, `Sonnet` 72 × `sonnet` 50, `Haiku` 10, na coluna 4 de
  `docs/telemetria.tsv`), e a **fonte** emite minúscula — o `meta.json` do subagente traz
  `"model":"sonnet"`. O teste `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv`
  não afirma um invariante alheio: ele afirma **a linha que este card reescreve**. Ajustar a
  grafia esperada não é afrouxar teste para o código passar — o caso, o nome e todas as outras
  colunas da asserção ficam, e o payload continua entregando `Sonnet` **maiúsculo**, o que
  transforma a asserção no guarda **ponta a ponta** da normalização, que antes ela não era.
  **(ii) A contingência vira Passo.** A colisão não é eventualidade: está **medida** (`1 failed,
  9 passed`, falha única na linha 274). `DP-G` manda materializar sem discricionariedade, e o que
  é certo entra como passo com literal, não como contingência — foi a forma de contingência,
  condicionada a *"afirmar a soma por `message.id`"*, que produziu o `blocked`. A autorização
  alcança **uma** linha, a 274, e só a grafia do modelo nela.
  **(iii) O trabalho já na árvore fica.** O executor aplicou (a), (b) e (c) e escreveu os quatro
  testes antes de parar; nada disso se refaz nem se descarta — o `A3b` interrompe a **execução**,
  não invalida arquivo medido. O card re-emitido abre com um **Passo 0 de conferência** do estado
  exato (`1 failed, 9 passed`), que devolve `blocked` se a árvore não estiver como medida, e
  proíbe reimplementar o que já está lá. Quem aplica a linha que falta é um **executor**, e quem
  julga é o **reviewer**: o consultor não escreve entrega de card, nem quando ela tem uma linha —
  fronteira que só vale se valer no caso barato.
  **(iv) A quarta medida confirma a fórmula, não a contradiz.** Medido agora sobre os quatro
  transcripts desta janela: a última entrada `assistant` com `usage` dá **exatamente** o
  `<usage>` da notificação em **4/4** (86,0k, 50,6k, 44,4k, 72,9k) — com o `ESC-3`, **10/10**. A
  linha exata da `LM-T2b` tem causa medida: o `SubagentStop` roda **depois** do subagente e
  importa o hook do disco naquele instante; o executor reescreveu `calcular_consumo` às 05:40 e o
  transcript fechou às 05:42, então a linha dele foi gravada **pelo código já corrigido** — o
  código velho teria gravado 371,6k para o mesmo transcript, e o gravado foi 72,9k. As três
  anteriores, fechadas antes das 05:40, batem **exatamente** com a soma por `message.id`. O que
  muda na redação é só o alcance da palavra *sempre*: o hook gravava para mais em toda execução
  fechada **antes** de o reparo entrar na árvore. A tabela de calibração do `ESC-3` permanece a
  residência única, agora com a tabela do `ESC-10` ao lado. Residência: card `LM-T2b`, que volta a
  `ready` **na mesma posição da fila**.

- **`DM-34` — a cláusula que faltava na regra do padrão de aceite; e entrega completa não volta
  para despacho, volta para laudo.** (Decisão do escalonamento `ESC-11`, 2026-09-19,
  `pantonic-consultant`, sobre o `AE-25` — **técnica**, não escalada.) Três partes.
  **(i) A linha 4 reparada, medida nos dois mundos.** `Select-String` é **case-insensitive por
  padrão**, então `'EXA-T55\tSonnet' -SimpleMatch` casa a linha nova, minúscula, e devolve 1 onde
  o card afirmava 0 — a linha era **inexequível**, não apenas imprecisa. Forma nova:
  `'EXA-T55\tsonnet' -SimpleMatch -CaseSensitive` → **1** na árvore entregue e **0** numa cópia
  pré-entrega (medido pelo consultor, os dois mundos, com o comando publicado); o mesmo padrão
  **sem** `-CaseSensitive` dá **1 nos dois** e não mede nada. A regra do `AE-23` ganha a cláusula
  do `AE-25`: *padrão de aceite é recorte do literal da fonte, rodado nos dois mundos **e com as
  opções que tornam a medida discriminante***. Os três casos (`AE-21`, `AE-23`, `AE-25`) seguem
  com residência no acumulador **`TK-55`** e leitura dentro do plano pela **`LM-T5`** — nenhum
  deles abre rodada própria.
  **(ii) Desfecho da `LM-T2b`: revisão, sem terceiro despacho.** O que faltou nas duas paradas foi
  **instrumento de aceite**, nunca produto: os três aceites substantivos do card saem como
  escritos, medidos pelo loop e re-medidos pelo consultor. Um terceiro executor não teria o que
  entregar — e, pior, **fabricaria a terceira parada**: o Passo 0 exige `1 failed, 9 passed` e a
  árvore está `10 passed`, de modo que o redespacho terminaria em `blocked` por um passo que já
  cumpriu a função. O estado é materializado **pelo instrumento** (`backlog.py status ... review`),
  nunca à mão. Autoria: o laudo julga **a árvore contra o card**, e a evidência `--desde 6eebccd`
  cobre os dois atos num delta só; autor de registro é o 2º executor, com a nota dos dois atos no
  RDO. As duas paradas foram `A3b`, que **não** consome retentativa: o contador chega ao laudo
  em 0.
  **(iii) Varredura estrutural do card, pedida pelo loop.** Confrontei **cada** passo e **cada**
  linha de aceite com a árvore de hoje, não de memória: Passos 0, 1 e 2 aplicados; `Verificação`
  1, 2 e 3 verdes (`10 passed`, `175 passed`, `cache_read_input_tokens` = 4); 4 reparada e medida
  nos dois mundos. **Nada mais no card pode fazê-lo parar uma terceira vez**, porque nada mais
  nele está por executar — o que resta é julgamento, que é do `reviewer`. Residência: card
  `LM-T2b`, cujo bloco de abertura passa a declarar o estado medido, os passos consumidos e a
  autoria.

- **`DM-35` — as quatro matérias do laudo da `LM-T2b`, alocadas por **onde a medida diz que elas
  moram**; e a varredura da `LM-T4` contra `DM-15`..`DM-34`.** (Decisão do escalonamento `ESC-12`,
  2026-09-19, `pantonic-consultant`, sobre o `AE-26` e os três itens do `AE-27` — **técnica**, não
  escalada.) Cinco partes.
  **(i) `AE-26` (bullet de `Status`) vira card de instrumento, antes da `LM-T4`.** Medido:
  `STATUS_BULLET_RE` (`.claude/tools/backlog.py:70`) exige ``- **Status:** `<estado>` ·
  AAAA-MM-DD``; dos cards do `P-0740`, **0** casam — 0 de 18 quando o `ESC-12` mediu, 0 de **21** depois de
  ele próprio acrescentar três cards, e é por isso que o aceite do card é **relação**, não
  literal (`AE-21`) —, e no repositório inteiro **15 de 34** bullets de `Status` casam. Não é defeito de um plano: é o **instrumento que não lê a gramática
  que o corpus usa**, e o `DM-34` mandou materializar estado por um instrumento que não alcança
  card nenhum deste plano. Rota: o **parser aprende a forma em prosa** e a escrita preserva a
  cauda — nunca o inverso, que seria reescrever 34 bullets e continuar com o planejador
  produzindo a forma que o leitor recusa. É o mesmo movimento da `LM-T4a` (`DM-13` (ii),
  `AE-5`/`AE-6`): **parser antes de doutrina**. Card `LM-T4b`, **antes da `LM-T4`**, que ganha o
  item (d) para publicar a gramática copiando o literal do card do instrumento.
  **(ii) `AE-27` item 1 (teste órfão) vira card próprio, fora do caminho crítico.** Medido: os
  dois testes têm corpo **byte a byte idêntico** (mesmo `usage`, mesmas duas entradas, mesmas
  asserções) e diferem só no nome e no docstring; o órfão (`:107`) nomeia o mecanismo que a
  entrega **removeu**. Rota: apagar o órfão, manter o novo, cuja prosa já está certa sob a
  fórmula nova. Não é matéria da `LM-T5` — aquela julga **autoria de card**, e isto é higiene de
  suíte, com literal e aceite próprios. Card `LM-T2f`, despachável em qualquer janela.
  **(iii) `AE-27` item 2 (alvos inflados) vira card de instrumento, antes da `LM-T6`.** Reproduzi
  a inflação e medi a causa, que é **de gramática, não de heurística**: `_parsear_campos`
  (`.claude/tools/rdo.py`) só encerra um campo quando encontra **outro campo canônico**, de modo
  que um bullet de prosa (`- **A calibração … — residência única desta tabela.**`) **não** encerra
  `Arquivos-alvo`, e todas as linhas indentadas seguintes — a tabela de calibração inteira —
  continuam alimentando o campo; daí `message.id`, `251.1`, `505.2`, `2330.8`, `946.9`, `.jsonl` e
  `telemetria_hook.py` virarem alvo. Emulei o reparo candidato (bullet de topo encerra o campo
  corrente) sobre os cards reais: `LM-T2b` **9 → 2** (exatamente a lista declarada) e `LM-T2e`,
  `LM-T3a`, `LM-T4`, `LM-T5` e `LM-T6` **inalterados** (1, 2, 5, 1, 2). A preocupação do laudo está
  certa e é a razão da prioridade: alvo inflado **afrouxa a autoridade mecânica da dimensão
  `escopo`**, que é contrato do `reviewer` e insumo do piloto. Card `LM-T3b`, **antes da `LM-T6`**.
  **(iv) `AE-27` item 3 (`docs/telemetria.tsv`) NÃO vira card: o código já está certo, a rubrica é
  que cala.** Medido agora: `_eh_registro_orquestracao('docs/telemetria.tsv')` → **True**, isto é,
  o arquivo já cai no balde **`registro_orquestracao`** da `DB-25` e **não** entra em
  `fora_dos_alvos` nem pesa no veredito mecânico — o mesmo valendo para `docs/RDO/`,
  `docs/RDO/INDEX.md` e o diário. A camada mecânica **resolveu**; o que faltou foi o `reviewer`
  saber que podia se apoiar nela, e isso é texto de **rubrica**. Residência: `LM-T5`, cujo
  `Arquivos-alvo` é exatamente `docs/RUBRICA_DE_REVISAO.md`, como insumo declarado — **não** se
  abre card de código para defeito que a medida não encontra no código.
  **(v) A `LM-T4` está despachável, com três emendas feitas neste ato.** Varri o card contra
  `DM-15`..`DM-34`, medindo o que ele afirma: (1) `check-drift` sai **exit 0** hoje (a `LM-T7`
  fechou e recolocou a projeção; `check-readme.ps1` também **exit 0**) — a nota da `RP-5` que
  dizia *exit 1* **envelheceu**, que é o `AE-21`, e o card passa a trazer a medida de hoje;
  (2) o card absorve `AUT-T8` (**status × veredito**) sem citar `DM-25`, `DM-26` **nem `DM-32`** —
  publicar status × veredito sem dizer que `reprovado` **não fecha RDO** (materializa `blocked`
  razão `premissa`, `A7`) escreveria doutrina contra a tabela que esta janela acabou de corrigir;
  a restrição entra no card; (3) o item (d) do `AE-26`. A baseline da `Verificação` 3 foi
  **re-medida** e continua valendo: **uma** ocorrência de `>8 write-clusters`, em
  `.claude/skills/proximo-passo/SKILL.md:126`. Todas as dependências estão `done` (`LM-T4a`,
  `LM-T7`, `LM-T2c`, `LM-T2d`); com a `LM-T4b` entra uma nova. **Marco:** concordo com o loop — o
  marco validável desta janela é a **`LM-T6`**, a única tarefa cujo produto é um **veredito do
  dono** (Diretiva item 2). A `LM-T9` está listada depois dela, mas **não é insumo do veredito** e
  não tem exclusão mútua com nada: corre antes da `LM-T6` ou na janela seguinte, à escolha do
  loop (Diretiva item 4).

- **`DM-36` — aceite não se contrata contra alvo que o card não alcança; e a auditoria de criação
  de card sobe na fila, partida em duas.** (Decisão do escalonamento `ESC-13`, 2026-09-19,
  `pantonic-consultant`, sobre o `AE-28` e sobre a antecipação da `LM-T5` pelo loop — **técnica**,
  não escalada.) Seis partes.
  **(i) A `Verificação` 2 da `LM-T4b`, reparada.** O executor está certo e parou no ponto mais
  barato. Medido por mim: `('ready','ready')` não está em `_TRANSICOES`, e o card mandava transitar
  para o estado em que a `LM-T2f` já está — **self-loop**, exit 1 garantido assim que o parser
  passasse a ler o bullet. Forma nova: o aceite de **escrita** é um teste sobre cópia da fixture
  `tests/fixtures/backlog/verde` em `tmp_path`, com bullet em prosa e transição `ready →
  in-progress`, que **está** na tabela. Medido no mundo de hoje, com esse mesmo arranjo: exit **3**,
  `linha de status ausente para ALF-T1`. Comando de aceite também **não muta o plano que o loop
  conduz** — contratar `backlog.py status` sobre um card real era, além de insatisfazível, efeito
  colateral em artefato vivo.
  **(ii) A máquina de estados NÃO entra no escopo do card.** Self-loop e no-op são decisão sobre a
  tabela de transições da `DP-F`; um card que ensina o instrumento a **ler e escrever um bullet**
  não reabre tabela de transição para caber num aceite que ele mesmo escreveu errado — é o inverso
  exato do `DM-26` (iii) e do `DM-32`. A restrição entrou no card.
  **(iii) `AE-29`, medido neste ato e maior que o `AE-28`:** mesmo com o parser corrigido,
  `backlog.py status` **não alcança tarefa nenhuma do `P-0740`**. Causa medida por introspeção: o
  plano é carregado com `id = "P-0740"` e a linha de índice do diário tem `id = "P-0740-LM"`, de
  modo que `_posicao_indice` devolve `None` e a transição morre em **exit 3**,
  `linha de índice ausente para P-0740`. Não é matéria deste plano: o contrato entre plano e índice
  é do **`backlog.py`**, isto é, do **`P-0739`**, que o dono estacionou até o `P-0740` encerrar.
  Consequência imediata e **emenda ao `DM-34`**: enquanto o `AE-29` estiver aberto, a materialização
  de estado pelo loop é **à mão, declarada** — não é improviso, é o único caminho disponível, e o
  `DM-34` (ii) passa a ler-se com esta ressalva. A `LM-T4b` continua valendo: ela fecha a metade que
  **é** deste plano (o bullet), e sem ela o `P-0739` corrigiria o índice para um leitor que
  continuaria sem ler o estado.
  **(iv) A regra de autoria de aceite vira critério de rubrica, não parágrafo de achado.** Os sete
  casos desta janela (`AE-19`, `AE-21`, `AE-23`, `AE-25`, `AE-26`, `AE-27` item 2, `AE-28`) têm
  **três autores diferentes** — planejador, consultor e loop —, o que os classifica como defeito de
  **método**. A `LM-T5` ganha os critérios **(xii)** (comando de aceite é recorte do literal da
  fonte, rodado nos dois mundos, com as opções que discriminam e com **alvo alcançável dentro do
  escopo declarado**) e **(xiii)** (baseline de corpus real é **relação**, re-medida no despacho),
  com os sete casos nomeados. Sem isso a `LM-T5` entregaria diagnóstico; com isso ela entrega régua.
  **(v) A `LM-T5` é antecipável — a dependência de `LM-T4` estava errada e foi dissolvida.** Medido:
  o critério (iii) da própria `LM-T5` afere a gramática **que os parsers aceitam**, e quem a ensinou
  foi a `LM-T4a`, fechada; `DM-2`..`DM-5` são decisões **deste plano**, que a `LM-T4` publica mas não
  cria. E a `LM-T5` **parte-se em duas**: a rubrica e o julgamento dos cards ficam na `LM-T5`,
  antecipável agora; o reagrupamento dos 6 cards do `P-0739` vai para a **`LM-T5a`**, atrás da
  `LM-T5` e da `LM-T4`, alinhada ao ato do dono que estaciona aquele plano. Não é partir um assunto
  só (`DM-2`): são dois — uma régua de autoria e o reagrupamento do backlog de **outro** plano —,
  unidos por conveniência de autoria, e mantê-los juntos faria a matéria urgente desta janela
  esperar pela que o dono adiou. As contagens da `LM-T5` viram **relação** pelo critério (xiii) que
  ela própria publica: eram 13 cards quando o card foi autorado, são **19** hoje.
  **(vi) Dependência da `LM-T4b` e da `LM-T4` em relação à `LM-T5`: nenhuma.** A `LM-T5` toca só
  `docs/RUBRICA_DE_REVISAO.md`; não há exclusão mútua com `backlog.py` nem com `GOVERNANCA.md`. O
  loop pode ordenar como julgar (Diretiva item 4) e **eu endosso a antecipação**: três cards
  seguidos parados por aceite é evidência suficiente. A única consequência técnica é que, fechada a
  `LM-T5`, a `LM-T4b` e a `LM-T4` devem ser **re-varridas sob os critérios (xii) e (xiii)** antes do
  despacho — varredura de consultor, barata, e é o que o `AE-14` ensinou sobre card sobrevivente.

- **`DM-37` — aceite órfão de entregável retirado; e a régua de autoria passa a ser comando, não
  item de checklist.** (Decisão do escalonamento `ESC-14`, 2026-09-19, `pantonic-consultant`, sobre
  o `AE-30` — **técnica**, não escalada.) Três partes.
  **(i) O reparo.** A `Verificação` 3 da `LM-T5` media
  `docs/plans/P-0739-backlog-instrumento.md`, arquivo que o `ESC-13` **proibiu** a mesma tarefa de
  tocar ao mover o segundo entregável para a `LM-T5a`. A linha **sai** da `LM-T5` — não precisa ser
  "movida", porque já está escrita como `Verificação` 1 da `LM-T5a` — e as duas que ficam foram
  reescritas na forma normativa, com as baselines re-medidas no `ESC-14` (**274** linhas na rubrica;
  **0** ocorrências de `LM-T`; **0** ocorrências de `Medido antes` nela contra **20** no plano) e
  com `-CaseSensitive` onde a caixa discrimina. A regra que faltava, e que passa a valer para toda
  emenda: **quem retira entregável de um card reconfere, no mesmo ato, as linhas de aceite que
  dependiam dele** — é o `DM-18` (i) aplicado à `Verificação`.
  **(ii) O loop está certo sobre o remédio, e eu assino a leitura dele.** O `AE-30` é o oitavo caso
  da décima segunda classe e viola a alínea (d) do critério **(xii)** — *alvo alcançável dentro do
  escopo declarado* — que é **este mesmo card** que vai publicar na rubrica; o defeito sobreviveu
  ao ato que escreveu a regra contra ele, três parágrafos acima. Doze critérios em vigor e oito
  defeitos numa janela é evidência suficiente: **checklist lido pelo autor não fecha defeito de
  autoria**. A `LM-T5` ganha o produto (b) — a **forma normativa** do bloco `Verificação`, com três
  elementos legíveis por máquina (comando cercado, linha `→` com o esperado, literal
  `**Medido antes: <valor>**`), que **20** itens deste plano já usam de fato — e a rubrica passa a
  **prescrever o passo mecânico**: card cujo `card_check` não sai 0 **não se despacha**.
  **(iii) O instrumento é card próprio, `LM-T5b`, logo depois da `LM-T5`.** Ele roda os comandos
  que o card publica e compara com o `Medido antes` declarado — isto é, compara o card com **o
  mundo**, que é a única coisa que nenhuma das oito falhas fez. Consequência sobre o `DM-36` (vi): a
  re-varredura da `LM-T4b` e da `LM-T4` que eu prometi fazer à mão passa a ser **mecânica**, rodada
  pelo loop, e eu entro só no que o instrumento recusar. **Insumo registrado, medido pelo loop
  (`GOVERNANCA.md` §4.2, nunca auto-relato):** 867k tk em cinco passagens do consultor
  (`ESC-9`..`ESC-13`) contra quatro tarefas fechadas e quatro executores despachados — número que
  não governa rota (`DP-Q`) e que é insumo direto da `LM-T5` e do veredito da `LM-T6`.

- **`DM-38` — a norma vale **no ato do despacho**, não em massa; e aceite de instrumento mede-se
  sobre **fixture**, nunca sobre artefato vivo.** (Decisão do escalonamento `ESC-15`, 2026-09-19,
  `pantonic-consultant`, sobre o `AE-31` — **técnica**, não escalada.) Cinco partes.
  **(i) Prospectiva na autoria, exigível no despacho — e não retroativa em massa.** A `### 8.1` que
  a `LM-T5` publicou já diz o que decide a questão: *"card cujo `card_check` não sai 0 não se
  despacha"*. Logo a norma **não** manda reautorar 16 cards agora: manda que **nenhum card seja
  despachado fora da forma**. Normaliza-se **um card por vez, no ato do despacho**, por quem
  despacha — com o instrumento quando ele existir, à mão enquanto não existe, como a própria
  `### 8.1` prescreve. Reautorar 20 cards de memória, numa janela cujo dado é que a memória do autor
  **não** fecha esta classe, seria comprar o defeito 20 vezes para prevenir 20 ocorrências dele. A
  contagem do laudo fica como está: **16 não passam** é o retrato verdadeiro da dívida, e ela se
  paga na ocasião em que cada card for ao executor.
  **(ii) Aceite de instrumento mede-se sobre fixture. É a regra geral que faltava, e ela fecha o
  padrão.** Três aceites consecutivos morreram pela alínea (d) do critério (xii) — `AE-28`
  (transição sobre card real), `AE-30` (arquivo de outro plano) e agora o `AE-31` item 1 (card vivo
  que não satisfaz a norma que o card vizinho publicou). A causa comum **não** é desatenção: é ter
  contratado aceite contra **artefato vivo**, que muda por ato de terceiro entre a autoria e o
  despacho. Passa a valer: *instrumento se afere sobre fixture, que o próprio card entrega e
  congela; artefato vivo é **uso** do instrumento, nunca aceite dele.* Materializado já: a
  `Verificação` da `LM-T5b` passa a rodar sobre três cards sintéticos
  (`tests/fixtures/card_check/plano-exemplo.md` — `EX-T1` conforme, `EX-T2` sem `Medido antes`,
  `EX-T3` com valor divergente), e a exigência de sair 0 na `LM-T3b` e 1 na `LM-T2e` **saiu**. Nota
  medida que confirma a escolha: **nem a `LM-T2e`** — o card que a auditoria aprovou — satisfaz a
  `### 8.1` em todos os itens (o item do `pytest` está inline, sem bloco cercado e sem
  `Medido antes`). Aceite apoiado nela nasceria morto em uma semana.
  **(iii) `AE-31` item 2 — o `Pronto quando` da `LM-T4b`.** Reparado: passa a falar da **fixture**,
  como a `Verificação` 2 desde o `ESC-13`. É o `AE-30` de novo, campo vizinho do mesmo card, e
  confirma a regra que o `DM-37` (i) já enunciou: **quem emenda uma linha de aceite varre os outros
  campos que a repetem** — `Pronto quando`, `Restrições`, `Contingências` e `Objetivo` citam o mesmo
  fato e envelhecem juntos.
  **(iv) `AE-31` item 3 — o invariante de contagem da `LM-T4`.** Reparado: `README.md` entra nos
  `Arquivos-alvo` e a `Verificação` ganha `check-readme.ps1` → **exit 0** (medido hoje: exit 0, 9
  agentes, 11 skills, 18 guardrails, 14 seções), declarado como **guarda de regressão**, com o
  executor obrigado a publicar no retorno o número de guardrails antes e depois. Publicar item novo
  em `GOVERNANCA.md` §7 sem fechar a tabela *Os guardrails* do `README.md` é exatamente o `AE-12`.
  **(v) `AE-31` item 4 — o numeral.** A rubrica publicada tem **quinze** critérios, `(i)`..`(xv)`;
  o executor numerou as duas aferições novas como `(xiv)` e `(xv)`, e o laudo julgou a decisão
  dentro do escopo. Fica **assim**: a referência canônica é a rubrica, não a prosa do card. O card
  da `LM-T5` está `done` e **não se reescreve** — ganha só a nota de reconciliação, porque corpo de
  card fechado é registro histórico. E registro o nono caso pelo que ele é: as três linhas de
  `Verificação` do card da **`LM-T5`** publicam `**Medido no ESC-14: 274**` em vez de
  `**Medido antes: 274**` — o card que normatizou a forma não a usa. Autor: eu. É o segundo caso
  em que a norma não sobrevive ao ato que a escreve, e é a evidência que sustenta (i) e (ii):
  enquanto for texto que o autor deve lembrar, não fecha. Por isso a `LM-T5b` é a próxima da fila.

- **`DM-39` — o silêncio é o defeito, não a regex; e o gate fica suspenso até o instrumento
  merecê-lo.** (Decisão do escalonamento `ESC-16`, 2026-09-19, `pantonic-consultant`, sobre o
  `AE-32` — **técnica**, não escalada.) Quatro partes.
  **(i) As quatro matérias vão num card só, `LM-T5c`, à frente da fila.** Elas tocam os **mesmos
  dois arquivos** (`card_check.py` e `docs/RUBRICA_DE_REVISAO.md`) e servem a **um** objetivo —
  tornar o instrumento confiável o bastante para virar gate; parti-las criaria exclusão mútua sobre
  os dois e entregaria, no meio, um gate que ainda não pode ser ligado (`DM-2`). A matéria 1 e a 2
  são o movimento `LM-T4a`/`LM-T4b` outra vez — **norma e parser no mesmo ato** —, e o laudo está
  certo sobre qual metade pesa: o **silêncio** é o defeito. Regra que sai daqui e vale para todo
  instrumento do loop: *instrumento que decide despacho não descarta entrada em silêncio — o que
  ele não sabe ler, ele **nomeia** e falha.*
  **(ii) Endosso a suspensão do gate, e ela é da alçada do loop.** Ligar hoje bloquearia card
  legítimo (matéria 3) e daria verde a card defeituoso (matéria 1) — o pior dos dois mundos, como o
  loop disse. Registro o alcance: o `card_check` roda como **instrumento de apoio** no gate de
  delegação, o loop segue re-derivando baseline à mão, e a frase da `### 8.1` (*"card cujo
  `card_check` não sai 0 não se despacha"*) fica **suspensa em efeito, não revogada em texto** —
  quem a reativa é a `LM-T5c`, que é também quem conserta o que a tornava perigosa. A `LM-T4b` e a
  `LM-T4`, portanto, **não** exigem `card_check` verde no despacho: exigem a conferência manual dos
  três elementos, como a própria `### 8.1` prescreve para o período sem instrumento.
  **(iii) A matéria 3 tem causa medida, e não é a que o card supunha.** *"Fora do aceite mecânico"*
  não precisa de porta própria: a recusa está **errada**, não o comando. `_rodar_comando` executa
  `subprocess.run(tokens)` **sem `shell=True`** (medido, `card_check.py:136`), então `;`, `|` e `$`
  dentro de um argumento citado são **texto**, não operadores — a varredura por substring recusa a
  forma canônica do kit por um risco que o modo de execução já elimina. A decisão é **recusar por
  token**, depois de `shlex.split`. O marcador `**Aferição: manual**` entra **só** como saída para
  item sem comando executável, e é **rejeitado** sobre comando que o instrumento consegue rodar —
  senão a porta dos fundos esvazia o gate no primeiro card difícil.
  **(iv) Uma quinta matéria, achada ao escrever o card — e pelo instrumento.** Ao publicar a
  `Verificação` da `LM-T5c` eu troquei a baseline dos itens 1..3 de `exit 1` (que valeria **nos
  dois mundos** — antes por fixture ausente, depois por item fora da forma, isto é, vacuosa) para
  **substring da saída**, e o `card_check` recusou: a saída capturada volta com a codificação
  trocada (`tarefa: 'EX-T4' nÃ£o encontrada`), porque `_rodar_comando` usa `text=True` **sem
  `encoding`** e o Windows decide pela `cp1252`. Efeito: **nenhum `Medido antes` com acento pode
  bater**, e o autor é empurrado a reescrever o literal da fonte sem acento — que é o `AE-23`
  induzido pelo próprio instrumento. Entrou como matéria 5 do card, com teste. Registro o método,
  porque é a primeira vez na janela que isto acontece: **o defeito apareceu porque eu rodei o
  instrumento contra o card que estava escrevendo**, que é precisamente o ciclo que a `### 8.1`
  prescreve. Com a baseline recortada antes do acento, a `LM-T5c` sai
  `card_check: OK — tarefa 'LM-T5c' fecha` (medido).
  **(v) Nada espera o pós-plano.** As cinco matérias cabem num card de esforço baixo e pagam-se
  no despacho seguinte. O que fica para depois do plano é só o **uso** do instrumento fora dele —
  varrer os cards do `P-0739` com o `card_check`, que é da `LM-T5a`, e o acumulador `TK-55`, que
  segue recebendo a série. E registro, porque é o décimo caso da classe e o primeiro que **um
  instrumento** cometeu em vez de um autor: o `card_check` deu verde a um card por não ter lido um
  item — exatamente o defeito que ele existe para pegar, agora um nível acima.

- **`DM-40` — a cadeia do `card_check` para aqui; instrumento fora do caminho crítico não atrasa
  marco.** (Decisão do escalonamento `ESC-17`, 2026-09-19, `pantonic-consultant`, sobre o `AE-33` e
  sobre a pergunta de rota do loop — **técnica**; o impedimento da `LM-T6`, registrado no card, é
  **estratégico** e sobe ao dono.) Cinco partes.
  **(i) Rota escolhida: (b), com recorte.** A cadeia `LM-T5` → `LM-T5b` → `LM-T5c` **para aqui**. O
  argumento do loop é o correto e eu o assino com o dado dele: o instrumento **nunca esteve no
  caminho crítico** — as três tarefas até o marco não dependem dele, e o loop re-derivou baseline à
  mão a janela inteira, inclusive quando o instrumento estava disponível. A curva 88% → 91% → 76%,
  com cada iteração achando defeito na anterior, é a assinatura de **especificação sendo descoberta
  pela implementação**, não de bug sendo consertado; e a Diretiva item 2 manda entregar no **marco
  validável**, não na perfeição. Regra que fica: *cadeia de reparo de instrumento fora do caminho
  crítico para no fim da janela corrente, não quando o instrumento ficar bom.*
  **(ii) As duas matérias do `AE-33` são re-especificação, não conserto — e por isso ficam melhores
  depois do piloto.** A matéria 1 não se resolve ajustando a âncora: o `card_check` lê o bloco
  `Verificação` pelo `rdo._parsear_campos`, que **achata o campo numa linha só**, de modo que
  `^\s*\d+\.` não tem como existir — a decisão devida é **ler o bloco bruto do card**, preservando
  linhas, e isso muda o contrato de leitura do instrumento. A matéria 2 é política de codificação
  **por tipo de filho** (o `python` que reconfigura `stdout`, o `python` simples em `cp1252`, o
  `pwsh` em OEM — e `pwsh` é a forma canônica do kit): a saída provável é forçar o ambiente do
  filho (`PYTHONIOENCODING`, `$OutputEncoding`) em vez de fixar `encoding` na leitura. Nenhuma das
  duas é linha trocada; as duas se decidem melhor com a evidência do piloto na mão.
  **(iii) O `AE-33` fica ABERTO e roteado ao pós-marco, sem card de código neste plano.** Não
  pré-autoro card para trabalho cuja especificação eu acabei de declarar dependente de evidência que
  ainda não existe — seria o `AE-14` de novo (card autorado antes das decisões que o governam). O
  achado segue no acumulador **`TK-55`**, e o card nasce no planejamento pós-marco.
  **(iv) O que não pode ficar como está é a superfície publicada.** A `### 8.1` prescreve *"card
  cujo `card_check` não sai 0 não se despacha"* e hoje o instrumento **reprova card conforme** — uma
  instrução publicada que, seguida, bloqueia despacho legítimo. É a lição do `AE-22` (arquivo
  carregando afirmação falsa sobre si mesmo), e fecha-se do jeito mais barato: o card **`LM-T5d`**,
  só a nota datada de suspensão, **fora do caminho crítico e não antes do marco**. Endosso também,
  e registro no texto da nota, a frase do loop: **o vermelho do `card_check` não é evidência**
  enquanto a matéria 1 estiver aberta.
  **(v) A cadeia vira insumo declarado do piloto.** O loop está certo em ver aí o material mais rico
  da janela: um instrumento que o próprio loop **especificou, construiu, mediu e corrigiu duas
  vezes**, com cada defeito pego por um agente diferente do que o produziu — `LM-T5b` achou o que a
  `LM-T5` não normatizou, o reviewer achou o falso verde do `LM-T5b`, o `LM-T5c` fechou-o e abriu um
  falso vermelho, e o consultor achou a matéria 5 rodando o instrumento contra o card que o
  reparava. Isso **é** medida do loop, e entra no piloto como insumo, qualquer que seja o corpus que
  o dono escolher.

- **`DM-41` — rótulo de campo termina na linha em que começa; e o reparo trivial continua sendo do
  dono do plano.** (Decisão do escalonamento `ESC-18`, 2026-09-19, `pantonic-consultant`, sobre o
  `AE-34` — **técnica**, não escalada.) Três partes.
  **(i) O reparo, feito.** O rótulo do `Pronto quando` da `LM-T4b` foi **requebrado** para que o
  `:**` caiba na primeira linha; **zero caractere de conteúdo alterado** — a decoração
  (`reparado pelo ESC-15, DM-38 (iii)`) fica, e a oração que sobrava virou a primeira frase do
  corpo. Medido depois: `review_evidence.py --tarefa LM-T4b --desde 6eebccd` → **exit 0**, dossiê
  gerado, contra o **exit 1** (`campo obrigatório ausente … 'pronto-quando'`) de antes.
  **(ii) O critério `(xvi)` entra na `LM-T5d`, e não espera o pós-marco.** É regra **fechada e
  mecânica** — não tem nada a descobrir, ao contrário do `AE-33` —, cabe no card que já vai à mesma
  seção do mesmo arquivo, e a `LM-T5d` segue **fora do caminho crítico**: o marco não atrasa um
  minuto. Guardá-la para o pós-marco seria deixar a regra mais barata da janela esperar pela mais
  cara. O card muda de título, porque agora são dois produtos sobre o mesmo assunto — *a rubrica
  posta em dia* —, e a frase que conta os critérios fecha no mesmo ato (`DM-18` (i)).
  **(iii) O loop está certo sobre a Regra 8, e o registro fica.** Ele recusou fazer um reparo de
  **uma requebra de linha** porque o plano é do consultor — e essa disciplina é o que produziu os
  treze achados desta janela. Abrir exceção pelo **tamanho** do defeito é exatamente como se perde
  uma regra: não por revogação, por conveniência. Fica registrado como precedente: *o tamanho do
  reparo não muda de quem ele é.*

- **`DM-42` — a fronteira entre razão e cauda é matéria **deste** plano; e ela espera o marco.**
  (Decisão do escalonamento `ESC-19`, 2026-09-19, `pantonic-consultant`, sobre o `AE-35` —
  **técnica**, não escalada.) Três partes.
  **(i) Residência: aqui, não no `P-0739`.** A pergunta do loop é a certa e a medida a responde. A
  gramática do bullet de `Status` **não** é herança do `P-0739`: ela foi **decidida nesta janela**,
  pelo `DM-35` (i), e contratada pela `LM-T4b` — que prometeu, com todas as letras, *"tudo que vier
  depois de ` — ` é cauda livre, lida e preservada"*. O que falta é **a fronteira**, que eu
  subespecifiquei ao autorar: medido por introspeção, o grupo da razão em `STATUS_BULLET_RE` é
  `(.+)` **guloso** e engole ` — cauda`, de modo que a transição seguinte a descarta. Isso é
  **completar o contrato do próprio card**, não matéria de outro plano — e mandá-la ao `P-0739`
  seria despejar dívida nossa numa fila que o dono estacionou. A fronteira, decidida agora: **a
  razão não contém ` — `; a cauda começa no primeiro ` — `**. Card `LM-T4c`.
  **(ii) Pós-marco, e por um motivo medido.** O caminho que perde a prosa **não é alcançável hoje**
  para card nenhum deste plano: o `AE-29` (índice `P-0740-LM` × id `P-0740`) faz `backlog.py status`
  morrer antes, em `linha de índice ausente`, de modo que o loop materializa estado à mão e **nunca
  percorre** o round-trip defeituoso. O defeito é **latente**, não vivo. Com duas tarefas até o
  marco e o marco já travado num impedimento do dono, a janela não gasta despacho com dívida
  latente. **Ressalva que vale enquanto o `LM-T4c` não fechar:** não se usa `backlog.py status` para
  tirar card de `blocked` — o que, medido, é o que já acontece.
  **(iii) O item 2 do `AE-35` vira critério `(xvii)`, no card que já cuida da rubrica.** *O aceite
  cobre o mundo que o próprio produto cria.* É variação nova do critério (xii) — não é alvo
  inalcançável, é **ramo não coberto**: a `LM-T4b` aferiu só o ramo em prosa e deixou sem nenhuma
  linha o ramo canônico que a escrita dela **emite**. Entra na `LM-T5d`, que segue fora do caminho
  crítico, com a contagem da seção indo a dezessete no mesmo ato (`DM-18` (i)).

- **`DM-43` — o produto (c) da `LM-T4` não tem decisão a tomar: tem forma ratificada a transcrever;
  o que estava errado era o aceite.** (Decisão do escalonamento `ESC-20`, 2026-09-19,
  `pantonic-consultant`, sobre o `AE-36` — **técnica**, e a pergunta de alçada do loop está
  respondida por medida, não por juízo.) Quatro partes.
  **(i) A alçada: não é estratégico, e a evidência é do próprio dono.** O loop levantou a questão
  certa — aposentar skill que o dono consome mudaria a superfície dele —, mas a premissa não se
  sustenta quando medida. `DU-5` do `P-0737` é **ratificação do dono em 2026-08-22**:
  *"`proximo-passo` é descontinuada; a responsabilidade é herdada pelo `scrum-master`"*, com a
  alternativa de coexistência **explicitamente recusada**. E o `AUT-T6` registra que a natureza da
  skill nova foi **fixada pelo dono em 2026-08-13** (`TK-36`): maquinário **agente↔agente**,
  *"transparente para o gerente do projeto — **ele não a invoca, não a lê e não a acompanha**"*.
  Quem declarou que esta superfície não é dele foi ele. Levar de volta ao dono uma decisão que ele
  já tomou duas vezes não é prudência: é devolver trabalho decidido, e é o que o `G-NOASK` chama de
  parada defeituosa. **Técnico.**
  **(ii) O defeito é do aceite, não do produto.** A `LM-T4` foi autorada quando o `AUT-T6` ainda
  era um card de outro plano, e herdou o produto sem herdar as consequências dele: `Arquivos-alvo`
  listavam como **alvo de edição** duas skills que a forma ratificada manda **remover**, o
  `Pronto quando` exigia reescrever o item 5 de uma delas, e três das quatro `Verificações`
  exigiam as duas **vivas**. Reparado: os dois diretórios entram como **REMOVIDOS**, a
  `passagem-de-bastao` entra como **NOVO**, e o gate passa a nascer na skill nova — mesmo conteúdo,
  outro lar, que é literalmente o que a `AUT-T6` chama de *transposição, não reescrita*.
  **(iii) A consequência que ninguém tinha escrito: a projeção.** Remover duas skills e criar uma
  muda a contagem do kit — medido hoje: `ls .claude/skills` → **11**, `check-readme.ps1` → exit 0
  **com 11 skills**. Depois da entrega são **10**, e as duas projeções (`.claude/README.md`
  regenerado por `kit_check -Mode generate`, e a tabela de skills da *Anatomia do kit* em
  `README.md`) fecham **no mesmo ato**, senão as `Verificações` 1 e 3 saem vermelhas. É o `DM-16`
  (iv) — *quem toca a superfície fecha a projeção dela* — e o invariante de contagem do `AE-12`,
  agora sobre skills. Os dois arquivos entraram nos `Arquivos-alvo`.
  **(iv) A varredura de ponteiro, medida e transformada em aceite.** A `AUT-T7` (superfícies que
  citam as aposentadas) já era absorvida por esta tarefa, mas **nenhuma linha a aferia**. Medido
  agora, pelo **caminho** e não pela palavra — *handover* sobrevive legitimamente em prosa, o
  caminho `.claude/skills/handover/` não: **4** citações de `proximo-passo/` e **3** de
  `handover/` nas cinco superfícies. Viraram as `Verificações` 4 e 5 do card, com os dois mundos
  publicados. Sem elas, a remoção deixaria ponteiro quebrado em quatro superfícies — que é
  exatamente o defeito que o `AE-12` custou.

- **`DM-44` — citação por **nome** é eixo próprio de varredura; e superfície de permissão não entra
  em card.** (Decisão do escalonamento `ESC-21`, 2026-09-19, `pantonic-consultant`, sobre o `AE-37`
  — **técnica**, não escalada.) Quatro partes.
  **(i) As duas matérias num card só, `LM-T4d`, com recomendação de vir antes da `LM-T3b`.** São o
  mesmo assunto — *regularizar a superfície que a aposentadoria deixou* (`G-SURFACE`, `GOVERNANCA.md`
  §7 item 16) —, e a matéria 2 (o item 17 citando a skill apagada) é duas trocas de nome dentro
  dele. A urgência é **assimétrica e medida**: `bootstrap-pantonic/SKILL.md:53` manda copiar
  `proximo-passo` e `handover` para projeto novo, e o kit se propaga a cinco derivados — projeto
  novo nasceria quebrado. A `LM-T3b` não tem urgência nenhuma, e o marco está travado no dono de
  qualquer forma. A ordem continua sendo do loop.
  **(ii) O mapa de sucessão fica fechado no card, porque senão o executor decide.** Citação sobre
  **escolher tarefa, diretiva, inbox ou fila** → `scrum-master` (`DU-5`: responsabilidade herdada);
  citação sobre **transição, fechamento, passagem de bastão ou herança de contexto** →
  `passagem-de-bastao`; **a palavra** *handover* em prosa **não** é citação de skill e não se toca.
  Citação que não couber nas duas regras **para e escala** — ampliar o mapa é decisão de consultor,
  não de execução (Regra 8).
  **(iii) `.claude/settings.json` sai do escopo e vira ato do dono.** As duas regras órfãs
  (`Edit(/.claude/skills/handover/**)` e `Edit(/.claude/skills/proximo-passo/**)`, linhas 5 e 6
  medidas) estão em **superfície de permissão** — a mesma que o `DM-27` registra como materializada
  **por ato do dono**. Regra de permissão não se altera por card de plano, e nenhum agente altera a
  própria permissão por instrução de outro agente. As duas são **inócuas** (concedem `Edit` sobre
  diretório inexistente), então esperar não custa: vão nomeadas ao relatório de encerramento.
  **(iv) O eixo que faltava ao critério (xii), e é o décimo sexto caso da série.** O aceite da
  `LM-T4` estava **certo no que media** — varredura por **caminho**, `.claude/skills/handover/` —, e
  incompleto **no eixo**: citação por **nome** (`` `handover` ``, com crase) é outra coisa, e vive em
  arquivos que não estavam nos `Arquivos-alvo`. Regra que sai daqui, e que o planejamento pós-marco
  leva à rubrica: *entregável que **remove ou renomeia** artefato varre os **dois** eixos — o
  caminho e o nome — e varre o kit **inteiro**, não só os arquivos-alvo; o que a varredura achar
  fora dos alvos vira card de regularização (`G-SURFACE`), nunca resíduo.* Não a escrevo na rubrica
  agora: a `LM-T5d` está fechada em escopo e a janela encerra na `LM-T3b` — a regra entra com o
  `AE-33` no pós-marco, onde a `LM-T5a` e o planejamento já têm residência.

> **`DM-45` são atos do dono de 2026-09-19**, tomados sobre o relatório de encerramento da janela
> de 2026-09-19. Entram pela mesma porta das `DM-27`..`DM-30`.

- **`DM-45` — quatro atos do dono sobre o relatório de encerramento.**

  **(i) O piloto muda de veículo: rota (B).** A `LM-T6` **não** roda sobre o `P-0739` — o corpus
  dela passa a ser **esta janela**, já medida: 11 tarefas fechadas, zero reprovações, zero
  retentativas consumidas, 18 achados (`AE-21`..`AE-39`), 14 passagens do consultor num contexto
  só, e `6.004,3k tk` decompostos em execução `1.389,9k` (23%), revisão `812,2k` (14%) e consultor
  `3.802,2k` (**63%**). O `P-0739` **permanece estacionado** e nada do ato do dono que o estacionou
  é desfeito; a `LM-T5a` sai do caminho do marco. **Consequência a executar antes do despacho da
  `LM-T6`:** o `Entregável` e o `Pronto quando` dela ainda falam da fila do `P-0739` e **precisam
  ser reescritos para o veículo (B)** — reescrita de card é do consultor, **não** do loop, e é a
  **primeira tarefa da próxima instanciação dele**.

  **(ii) As duas regras órfãs de permissão foram removidas.** `.claude/settings.json` linhas 5 e 6
  (`Edit(/.claude/skills/handover/**)` e `Edit(/.claude/skills/proximo-passo/**)`), que concediam
  edição sobre diretórios apagados pela `LM-T4`. Removidas **por ato do dono em 2026-09-19**,
  materializadas pelo loop no mesmo ato; `deny` e `hooks` intocados, JSON conferido. **Achado que
  a remoção expôs e que NÃO foi resolvido:** não existe regra de permissão para
  `.claude/skills/passagem-de-bastao/**`, a skill que a `LM-T4` criou — alargar permissão é ato do
  dono e não se faz por iniciativa do loop, então fica **registrado, não agido**.

  **(iii) O consultor que atinge o limite faz handover; o loop descomissiona e provisiona outro.**
  Ato do dono, motivado pelo `ESC-22` desta janela — o consultor caiu por *session limit* **sem
  devolver** as duas alocações do `AE-38` nem a varredura da `LM-T3b`, e o contexto inteiro dele
  (14 passagens, o cenário acumulado) morreu junto. Regra nova, vinculante para a próxima
  instanciação: **ao perceber que se aproxima do próprio limite, o consultor promove handover** —
  entrega o estado do cenário, os escalonamentos abertos e o que estava em curso —, e o
  **`scrum-master` descomissiona a instância e provisiona outra**, repassando esse handover. A
  **forma de comunicação fica ad-hoc neste plano** (`DM-28`: técnica ainda não projetada se executa
  ad-hoc, e o ad-hoc é insumo, não precedente) e **entra na spec do consultor** (`LM-T9`) para
  resolução no plano próprio. Enquanto não houver forma projetada, o ad-hoc **não** é fonte
  normativa e não se cita como tal.

  **(iv) O consultor ganha responsabilidade de telemetria própria: estatística do próprio
  acionamento.** Ato do dono. O consultor passa a **coletar estatísticas de cada acionamento** — o
  que o motivou, que classe de impedimento era, o que ficou **inconclusivo** — de modo a produzir
  um **panorama dos pontos inconclusivos**, que é insumo direto da **spec de robustez**. Base
  medida que justifica: nesta janela ele respondeu 14 acionamentos e consumiu **63%** do total,
  e hoje não há nenhum registro estruturado de *por que* cada acionamento existiu — só a linha de
  consumo em `docs/telemetria.tsv`, que mede custo e não mede **causa**. Sem esse panorama, a spec
  de robustez seria autorada sobre impressão. Entra na spec do consultor (`LM-T9`).

- **`DM-46` — o item (b) da `LM-T8` ganha **local** e **literal**; e a concessão de `Bash` fecha,
  no mesmo ato, as três frases do planner que ela torna falsas.** (Decisão do escalonamento
  `ESC-23`, 2026-09-19, `pantonic-consultant`, sobre o `AE-41` — **técnica e tática**, nada
  escalado.) Cinco partes.

  **(i) O card fica inteiro; não se parte.** A `### 8.2` de `docs/RUBRICA_DE_REVISAO.md` já
  reprovou a `LM-T8` por **(ii)/(xii)(d)**: *"dois estados de executabilidade no mesmo card — o
  `Pronto quando` condiciona o item (b) à `LM-T4`, e despacho nenhum fecha o card inteiro"*. Esse
  defeito morreu com o fechamento da `LM-T4`: hoje os três itens rodam no **mesmo** despacho, e o
  card volta a ser **um tema só** — a definição do `pantonic-planner`. Partir agora criaria dois
  cards sobre o **mesmo arquivo**, em exclusão mútua e sem tema próprio, que é o oposto da régua de
  partição (`DM-2`, `DM-4`): parte-se por assunto, nunca por volume. Rota escolhida: **emendar**.
  No mesmo ato o cabeçalho cai de `Opus + dono` para `Sonnet` — o ato do dono foi feito (`DM-27`) e
  o que sobra é transcrição literal, que é trabalho de classe `mecanica`.

  **(ii) O local de cada bloco, nomeado — nada fica com o executor.** Quatro pontos em
  `.claude/agents/pantonic-planner.md`: **(a)** gramática de cabeçalho — o bullet de `## Fatos
  estáveis (não redescobrir)` e a linha do esqueleto de `## Anatomia do card`, os dois pontos que
  hoje a enunciam na forma aposentada; **(b)** régua de tema — o **item 5 (*Dimensionamento*)** da
  Fase 4, cuja última frase é hoje a régua de volume que a `DM-2` substituiu (*"parta por ramo,
  nunca por volume arbitrário"*); **(c)** os cinco critérios de autoria (`DM-18`, `DM-21`..`DM-24`)
  — **item 12, novo**, no fim da Fase 4, depois do item 11 e antes de `### Fase 5`. **Seção nova
  fica recusada:** a Fase 4 já é a residência do dever de autoria conferido antes de gravar, e
  abrir seção para cinco critérios criaria uma segunda residência do mesmo assunto (`RP-6`).
  **(d)** Nada disso é autoria nova: as residências canônicas são `GOVERNANCA.md` §3 (*Gramática do
  card*; *A unidade de trabalho é o módulo coeso*) e `docs/RUBRICA_DE_REVISAO.md` (critérios
  (viii)..(xi)). O card **transcreve**, e o literal dos quatro pontos vai **dentro** do card, com o
  trecho `de` e o trecho `para` — o planner é papel sem card, então a transcrição é a única forma.

  **(iii) O achado que o escalonamento não trazia: a concessão de `Bash` deixa três frases falsas
  no mesmo arquivo.** Medido no `ESC-23`: `pantonic-planner.md` afirma hoje, em **três** pontos,
  que o papel **não** roda comando — o parágrafo de abertura (*"não lê codebase para se situar,
  **não roda comando e não mede**"*), a abertura do item **11** da Fase 4 (*"**Você não roda
  comando** — logo…"*) e um bullet de `## O que você NUNCA faz` (*"rodar comando, medir ou
  sondar"*). O item (a), como estava, acrescentaria o fato estável do `Bash` e deixaria o arquivo
  **contradizendo a si mesmo** — exatamente o defeito do `AE-12` que a `DM-18` (i) fechou, agora
  dentro do card que publica a própria `DM-18`. As três frases entram no item (a) com literal
  fechado. A fronteira que o literal preserva: `Bash` serve a **um** uso — rodar o comando de
  aceite que o próprio planner vai publicar (`DM-12`, `DM-24`) — e **não** é licença para
  levantamento próprio, que segue delegado (fase 1, `pantonic-scout`).

  **(iv) O parser já aprendeu a gramática que se publica.** Conferido no `ESC-23` **antes** de
  fixar o literal, que é a lição do `AE-5`: `.claude/tools/rdo.py:86` (`_HEADER_BRACKET_RE`) aceita
  `[ + dono]`, `[ · esforço …]` e o `[ · teto …]` legado, isto é, a forma de `GOVERNANCA.md` §3 é
  exatamente a que o parser lê; e `.claude/checks/kit_check.ps1:165` valida `tools:` como lista
  separada por vírgula, logo `Bash` no frontmatter não derruba o `validate`.

  **(v) A `Verificação` passa a discriminar bloco a bloco, com os dois valores rodados.** Doze
  linhas na forma normativa da `### 8.1`, **todas** medidas no `ESC-23` rodando o comando publicado
  nos **dois** mundos — a árvore atual e a árvore com os dez literais do card aplicados, restaurada
  no mesmo ato (`DM-12`, `DM-24` (iii)). Antes, a `Verificação` inteira media só o `tools:` e duas
  regressões de `kit_check`: **nenhuma** das três linhas provava o item (b), e foi esse vazio que o
  `AE-41` expôs. As duas linhas de `kit_check` permanecem, agora **declaradas** pelo que são —
  guarda de regressão, não discriminante.

- **`DM-47` — a `LM-T6` reescrita para o veículo (B): o piloto troca de corpus, não de
  propósito.** (Reescrita do consultor em 2026-09-19, por **ordem de fila do `scrum-master`**,
  executando a `DM-45` (i) do dono — **tática**, nada escalado. O `ESC-17` havia declarado o card
  não despachável e devolvido a escolha ao dono; ele escolheu **(B)**, e a `DM-45` (i) atribuiu a
  reescrita nominalmente ao consultor.) Cinco partes.

  **(i) O que saiu.** O `Entregável` mandava *"um run do loop sobre a fila de **módulos** que a
  `LM-T5` deixou no `P-0739`"* e o `Pronto quando` exigia *"o `P-0739` fecha `done`"*. As duas
  cláusulas morreram: a fila não existe mais na `LM-T5` (saiu para a `LM-T5a`, `DM-36` (iii)) e o
  `P-0739` **segue estacionado** por ato do dono. O `Objetivo` também dizia *"a rodada única que
  encerra o `P-0739`"* e foi reescrito no mesmo ato — deixá-lo seria manter no card a premissa que
  a reescrita existe para tirar.

  **(ii) O que entrou.** O corpus passa a ser a execução do **próprio `P-0740`** sob o loop, em
  duas janelas medidas: a de 2026-09-18/19 (11 tarefas fechadas, 7 em `aprovado 100%`, zero
  reprovações, zero retentativas consumidas, 39 linhas de `docs/telemetria.tsv`, 6.004,3k tk, 900
  tool uses, 3,06 h, decompostos em execução 23%, revisão 14% e consultor 63%) e a **corrente**,
  cuja fatia se re-mede no despacho. O produto continua idêntico: a série por módulo, a regra que
  encerrou cada janela, o confronto com a baseline de tarefa atômica da `BKL-T4` e o **veredito do
  dono**.

  **(iii) Onde o produto mora, e por que não é `Arquivos-alvo`.** O entregável é a seção **10** do
  próprio plano, mais uma linha em `CHANGELOG.md`. O card **não** ganha campo `Arquivos-alvo`: o
  `review_evidence.py` exige **exatamente um** entre `Arquivos-alvo` e `Entregável`, e ter os dois
  é o defeito que derrubou o laudo da `LM-T9` (`AE-40`). Conferido rodando o instrumento depois da
  reescrita: **exit 0**, com os alvos declarados lidos do `Entregável` — `docs/plans/P-0740-loop-de-modulos.md`
  e `CHANGELOG.md`, exatamente os dois que a tarefa edita.

  **(iv) O que é aceite e o que é relação declarada.** Nove linhas de `Verificação`, todas rodadas
  nos dois mundos (árvore atual e árvore com a seção 10 simulada pelos literais prescritos,
  restaurada no mesmo ato). As seis primeiras usam **regex ancorada em `^`**, deliberada e rodada
  (`DM-24` (ii)): sem a âncora, o padrão publicado casaria **a própria linha de comando**, que vive
  no mesmo arquivo, e o aceite mediria a si mesmo. A relação *uma linha de tabela por módulo
  fechado* fica como **`Restrição` declarada, sem promessa de teste** (`DM-21` (ii)(c)) — o total
  muda a cada despacho e constante nenhuma o aferiria sem envelhecer (`DM-23`); o comando que o
  re-mede vive no **Método de sondagem**, que é onde a re-medida de despacho pertence. `README.md`
  entra como **guarda de regressão**, não como edição.

  **(v) O que continua sendo do dono.** O **veredito**. O card fica despachável **até a medida** —
  a seção 10 fecha sem o dono —, e a `Contingência` 3 diz o que fazer se ele não estiver na janela:
  `blocked` razão `dependencia`, com a medida já publicada e só a linha do veredito vazia. Nem o
  consultor nem o loop escrevem essa linha.

- **`DM-48` — regra instalada em `settings.json` **não** é permissão efetiva; a única evidência de
  permissão é a edição que passa.** (Decisão do consultor em 2026-09-19, sobre o `AE-42` —
  **tática**, nada escalado. Emenda a lição da `DM-27`.) Três partes.
  **(i) O fato.** A `DM-27` registrou a permissão do dono como concedida porque a regra `Edit`
  sobre `.claude/agents/**` **estava instalada** em `.claude/settings.json`. Com a regra instalada,
  o gate verde (`card_check --tarefa LM-T8` → exit 0) e os literais conferidos, o `Edit` foi
  recusado assim mesmo: **`Blocked by classifier`**. O classificador do harness é uma **camada a
  mais**, independente da allowlist, e nenhuma leitura de `settings.json` a antecipa.
  **(ii) A regra de autoria.** Card cuja entrega toca superfície de permissão (definição de agente,
  `settings.json`, hook) **não** trata a allowlist como prova: a allowlist é condição
  **necessária**, não suficiente. Enquanto a permissão não tiver sido **exercida** ao menos uma vez
  na superfície, o card declara isso como risco nomeado e a devolução `blocked` razão `permissao`
  é desfecho **previsto**, não defeito de autoria — foi exatamente o que a `LM-T8` fez, com o
  executor acertando ao **não** contornar por `Bash`.
  **(iii) Alcance, declarado.** Esta decisão vale como **régua de autoria deste plano** e não
  reescreve doutrina publicada: promover a lição a `GOVERNANCA.md` exigiria card de superfície, que
  este plano não tem e que é matéria do dono. Fica como insumo nomeado para o relatório de
  encerramento, ao lado do ato de permissão que a `LM-T8` espera.

- **`DM-49` — as duas matérias do `AE-45` ganham residência na fila pós-marco como item `PM-1`; e a
  regra da superfície de permissão fica **reservada ao dono**, não decidida aqui.** (Decisão do
  escalonamento `ESC-25`, 2026-09-19, `pantonic-consultant`, sobre o `AE-45` — **tática na
  residência, com núcleo estratégico nomeado**.) Cinco partes.

  **(i) A classificação, partida onde ela de fato se parte.** Dar **residência** a uma matéria de
  replanejamento é trabalho de modelo funcional do plano, e é meu. Decidir **a regra** da matéria
  (i) do `AE-45` — o que o loop faz quando o classificador do harness recusa o executor — **não**
  é: qualquer resposta a ela mexe em uma de duas fronteiras que só o dono move, a de
  `GOVERNANCA.md` §3 (*a orquestração não implementa*) ou a da superfície de permissão (§7 item
  13). Registro a matéria, o que ela custa e as saídas que a janela já mediu; **não escolho entre
  elas**, e nada aqui autoriza a exceção do `AE-44` a virar rotina.

  **(ii) Por que não nasce card de execução agora.** Três razões, e bastam juntas: o plano está no
  **marco**, e quem o destrava é o veredito do dono; abrir card sobre `.claude/agents/**` antes da
  rota decidida é reincidir no ponto que o `AE-42` mediu — o card sairia autorado contra uma
  permissão que já recusou três vezes; e a matéria (i) é insumo do próprio veredito, porque é um
  limite **medido** do loop, não um defeito a esconder dele.

  **(iii) O item `PM-1` fecha as duas matérias juntas, e a razão é de superfície.** Não é
  conveniência: as duas tocam o **mesmo arquivo** (`.claude/agents/pantonic-planner.md`) e a mesma
  camada de permissão. Fechá-las em cards separados faria a segunda esbarrar na primeira — e
  qualquer card que mexa na `description` de um agente **regenera a projeção no mesmo ato**
  (`DM-16` (iv)), então o dever de superfície é um só. É a régua de tema da `DM-2` aplicada a um
  item de replanejamento: um assunto, um item.

  **(iv) Correção de fato ao laudo, que o `AE-45` (ii) herdou.** O laudo diz que a matéria (ii)
  *"depende da reprojeção de `.claude/README.md` que é da `LM-T7`"*. A `LM-T7` **já fechou** — o
  `check-drift` sai exit 0 hoje, medido neste escalonamento. A dependência real é outra, e é mais
  simples: mudar a `description` **reabre** o drift, logo o card que a mudar tem de **regenerar a
  projeção no mesmo ato**. Não há tarefa a esperar; há dever de superfície a cumprir dentro do
  próprio card.

  **(v) O que sobe ao dono, enumerado sem preferência.** Saídas que a janela mediu para a matéria
  (i), todas do dono porque todas mexem em fronteira dele: **(a)** alargar a permissão de modo que
  o **executor** passe na superfície `.claude/agents/**`; **(b)** declarar que tarefa sobre essa
  superfície é **ato do dono**, e o card nasce com ` + dono` no cabeçalho, com o dono aplicando o
  literal — foi o que aconteceu de fato, duas vezes; **(c)** declarar exceção nominal e permanente
  ao *a orquestração não implementa* para essa superfície, com a salvaguarda que o `AE-44`
  preservou ad-hoc (quem escreve não julga: a revisão continua em papel e contexto próprios);
  **(d)** tirar `.claude/agents/**` do escopo de plano conduzido pelo loop. O custo medido de
  **não** decidir já está na série: três recusas dentro de uma tarefa só, e um fechamento que só
  existiu por ato do dono na sessão (`AE-42`, `AE-44`).

- **`DM-50` — a escrita em `.claude/agents/**` deixa de ser edição livre e passa a ser aplicação
  mecânica de literais declarados, por instrumento; e ferramenta recusada ao executor vira desfecho
  nomeado (`G-TOOLDENY`).** (Decisão do `scrum-master` **por delegação expressa do dono** em
  2026-09-19 — *"eu já concedi permissão para você fazer funcionar, não quero ter que decidir sobre
  esse tema que é de baixo nível; você veja a melhor forma de resolver, e torne isso como a
  doutrina; o que não podemos é retornar a esse mesmo problema para a quarta vez"* —, autorada aqui
  pelo `pantonic-consultant` no `ESC-26`. Substitui a reserva ao dono que a `DM-49` (i) havia
  declarado: a matéria **desceu** de estratégica para técnica por ato de quem a tinha.) Cinco
  partes.

  **(i) O diagnóstico.** O impedimento nunca foi de conteúdo nem de card. As três recusas de
  2026-09-19 (`AE-11`, `AE-42`, `AE-44`) caíram sobre a **ferramenta de escrita** aplicada a
  `.claude/agents/**` — `Edit`/`Write` —, com o card correto, o gate verde e os literais
  conferidos. Tratar isso como problema de permissão foi o erro de enquadramento que fez o mesmo
  ponto voltar três vezes.

  **(ii) O descarte das quatro saídas da `DM-49` (v), com a razão de cada uma.** **(a)** alargar a
  allowlist — **já tentada e medida**: a regra `Edit` sobre `.claude/agents/**` está instalada em
  `.claude/settings.json` desde `de28d01` e a recusa continuou, logo existe camada **acima** do
  `settings.json` e a allowlist não é alavanca nossa. **(b)** card com ` + dono` — **recusada pelo
  dono** no mesmo ato que delegou esta decisão. **(c)** exceção permanente ao *a orquestração não
  implementa* — corrói a fronteira de `GOVERNANCA.md` §3, que é justamente o que separa quem
  escreve de quem julga. **(d)** tirar `.claude/agents/**` do escopo do loop — tira do kit uma
  superfície que ele precisa manter viva. Nenhuma das quatro ataca a causa do item (i).

  **(iii) A quinta saída, que a enumeração não tinha.** A edição de definição de agente passa a ser
  **aplicação mecânica de literais declarados, por instrumento**. Três peças, e valem juntas:
  **(1) instrumento** `.claude/tools/agentdef.py`, verbo único `apply`, que exige **ocorrência
  única** de cada `de`, é **tudo-ou-nada**, preserva encoding e line ending, recusa alvo fora de
  `.claude/agents/*.md` e tem borda de **residência única** (`DM-22`); **(2) forma de card** — quem
  muda definição de agente declara os literais em `de`/`para` e roda o instrumento na
  `Verificação`; a forma **já se provou**, foi a da `LM-T8`, dez literais e doze linhas de aceite,
  entregue sem um grau de liberdade para quem executa; **(3) guarda `G-TOOLDENY`** — ferramenta
  recusada ao executor não vira improviso nem silêncio: ele devolve `blocked motivo=ferramenta`,
  motivo **novo** no domínio fechado do retorno, nomeando ferramenta e caminho, e o loop roteia
  pela `A3c` ao **fallback declarado** daquela superfície; superfície sem fallback declarado é
  matéria de plano, não de janela. A exceção do `AE-44` **fecha** e a §3 volta a valer sem ressalva.

  **(iv) A condição que impede a quarta repetição, e é inegociável.** O card que implementar isto
  **prova a rota a partir de um contexto de executor**, com verificação discriminante — não supõe
  que funciona. Se o executor também for recusado ao rodar o instrumento, **essa medida é o
  achado**, e a escolha entre (b) e (d) se faz então **com dado**, não com hipótese. Por isso a
  contingência 1 da `LM-T10` declara a recusa como **entregável**, e não como fracasso: ou a rota
  funciona provada, ou se sabe exatamente por quê. O que não pode voltar a acontecer é descobrir
  isso no meio de uma tarefa de conteúdo.

  **(v) A partição, e a razão dela.** Dois cards, não um: **`LM-T10`** (o instrumento, os testes e
  a prova da rota) e **`LM-T11`** (o contrato de recusa: `G-TOOLDENY`, o motivo `ferramenta`, a
  `A3c` e o fim da exceção). São **dois temas** — um caminho de escrita e um contrato de retorno —,
  e há dependência dura entre eles nos dois sentidos que importam: a `LM-T11` **edita
  `.claude/agents/pantonic-executor.md`**, que é a superfície recusada, e só o instrumento da
  `LM-T10` a torna editável; e se a `LM-T10` fechar `blocked` pela contingência 1, a rota caiu e a
  `LM-T11` **não se despacha como está**. Juntá-las poria a doutrina refém de um experimento —
  exatamente o que a `DM-2` proíbe ao mandar partir por tema. **Medido na autoria, e por isso
  nenhum dos dois cards toca parser:** nenhum instrumento Python do kit lê o domínio de `motivo` —
  ele vive só em prosa, em `.claude/skills/scrum-master/SKILL.md` e
  `.claude/agents/pantonic-executor.md` —, e o `--razao` do `backlog.py` é texto livre. A lição do
  `AE-5` foi conferida antes de fixar a gramática nova, não depois.

## 5. Tarefas

### LM-T1 — O pacote de fechamento: estado, telemetria e contratos [Sonnet · classe implementacao]

- **Status:** `done` — fechada em 2026-09-18, **aprovada 100%**, bloqueante `nenhuma`, as sete dimensões `conforme`, recomendação `escalar` (RDO `docs/RDO/P-0740-LM-T1-o-pacote-de-fechamento-estado-telemetria-e-contratos.md`; laudo consumido e apagado, `DP-H`). A pendência do laudo está no `AE-8`, **absorvido pela `RP-5`** (`DM-15`; residência da correção: card `LM-T1a`) — nada pendente nesta tarefa, que não se refaz.
- **Esforço:** medium
- **Objetivo:** tudo que o loop escreve ao fechar uma tarefa, num módulo só. Cobre os defeitos 1 e 3
  e absorve a `AUT-T4`.
- **Depende de:** `DM-10` (forma do slot de estado), `DM-11` (tipo de `--tokens-k`), `DM-3`
  (coerência é aceite), e os fatos `F-1`..`F-4` da §3. Nenhuma tarefa anterior.
- **Arquivos-alvo:**
  - `.gitignore`
  - `.claude/estado/.gitkeep`
  - `.claude/tools/rdo.py`
  - `.claude/skills/scrum-master/SKILL.md`
  - `tests/test_rdo.py`
  - `tests/test_telemetria.py`
- **Produto do módulo:** (a) o **slot** `.claude/estado/` versionado — `.gitkeep` rastreável e conteúdo de
  sessão ainda ignorado, conforme `DM-10`, com o `.gitignore` reescrito no texto literal abaixo;
  (b) `rdo.py close --tokens-k` aceitando e gravando decimal de uma casa, conforme `DM-11`, de modo
  que o mesmo literal sirva a `telemetria.py append --tokens_k` sem conversão; (c) Passo 4 e Passo 9
  do `scrum-master` reescritos nos dois textos literais abaixo — o Passo 4 garante o diretório antes
  de gravar (segunda trava), o Passo 9 fixa que o mesmo literal vai às duas chamadas.
- **Texto novo, literal — `.gitignore`.** Substituir **estas quatro linhas** (`:7-10`):

  ```
  # Estado de sessão do loop autônomo (ex.: tarefa-corrente.json, escrito pelo `scrum-master` no
  # despacho e consumido pelo hook `SubagentStop` — T55) — fato de uma sessão numa máquina, nunca
  # canônico do framework.
  .claude/estado/
  ```

  por **estas seis**, na mesma posição do arquivo:

  ```
  # Slot de estado de sessão do loop autônomo. O diretório é canônico do framework e viaja
  # versionado (`.gitkeep`), para que o Passo 4 do `scrum-master` nunca grave em caminho
  # inexistente; o conteúdo (ex.: tarefa-corrente.json, escrito no despacho e consumido pelo hook
  # `SubagentStop` — T55) é fato de uma sessão numa máquina e nunca se versiona.
  .claude/estado/*
  !.claude/estado/.gitkeep
  ```

- **Texto novo, literal — `.claude/skills/scrum-master/SKILL.md`, Passo 4 (`:66`).** A linha 66 é a
  que começa com **`- **Ação:** gravar`** e segue com o caminho do arquivo de estado. Trocar o
  início dela, até o abre-parêntese de "objeto único", por:

  ```
  - **Ação:** garantir o diretório `.claude/estado/` (ele viaja versionado com `.gitkeep`, `DM-10`
    do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar
    `.claude/estado/tarefa-corrente.json` (objeto único:
  ```

  O resto da frase (`tarefa`, `projeto`, `modelo`, `plano`, `despachado_em` ISO 8601 …) fica
  intacto.
- **Texto novo, literal — `.claude/skills/scrum-master/SKILL.md`, Passo 9.** Na linha `:147`, trocar
  `--tool-uses <N> --tokens-k <N> --duracao-s <N> \` por
  `--tool-uses <N> --tokens-k <tokens_k> --duracao-s <N> \`; e apender, como parágrafo próprio logo
  depois do parágrafo que termina em "nunca copiado para o diário." (`:157`), esta frase:

  ```
  O `<tokens_k>` é o mesmo literal nas duas chamadas — decimal de uma casa (ex.: `203.7`), a forma
  que o hook `SubagentStop` já produz. O loop não converte, não arredonda e não trunca o número
  entre uma chamada e outra (`DM-11` do `P-0740`).
  ```

- **Contratos/classes:** `.claude/tools/rdo.py:772` —
  `"--tokens-k", required=True, type=int, dest="tokens_k",` passa a `type=float`; `:675` —
  `"TOKENS_K": str(args.tokens_k),` passa a `"TOKENS_K": f"{args.tokens_k:.1f}",`.
  `.claude/tools/telemetria.py` **não se edita**: `--tokens_k` (`:150`) já aceita o literal decimal
  por `_validar_numero_nao_negativo` (`:106`).
- **Coerência do módulo (aceite de `DM-3`):** o literal `203.7` entra sem erro nos dois CLIs e sai
  gravado nos dois artefatos (RDO e `docs/telemetria.tsv`) com a mesma grafia, sem conversão
  intermediária.
- **Restrições desta tarefa:** o `.gitignore` é tocado **só** nas quatro linhas transcritas acima —
  `.claude/settings.local.json`, `.claude/settings.json`, `__pycache__/`, `*.pyc`, o bloco de ruído
  de SO/editor, `*.log`, `scratchpad/`, `PantonicForDesktop/` e `PantonicForContainer/` ficam como
  estão. A negação `!.claude/estado/.gitkeep` vem **depois** de `.claude/estado/*`, nesta ordem, e
  nenhuma linha com `.claude/estado/` terminando em barra sobra no arquivo. Nenhum comando de git
  que altere índice ou HEAD (`git add`, `git commit`, `git stash`, `git checkout`, `git restore`):
  a árvore já carrega entregas não commitadas de outras tarefas e a desta também fica não
  commitada. `rdo.py` não importa `telemetria.py` (`DM-11`).
- **Não fazer:** não tocar `.claude/tools/telemetria_hook.py` nem `tests/test_telemetria_hook.py`
  (são a `LM-T2`); não tocar `.claude/tools/backlog.py`; não tocar `.claude/tools/telemetria.py`;
  não mexer em `--tool-uses` nem em `--duracao-s`, que continuam `int`; não criar
  `.claude/estado/tarefa-corrente.json` (quem o escreve é o Passo 4, em tempo de despacho).
- **Contingências:**
  - se `git check-ignore -q .claude/estado/.gitkeep` sair com exit code **0** depois da edição (= o
    caminho **está** ignorado, o oposto do pretendido) → conferir no `.gitignore` que
    `!.claude/estado/.gitkeep` está depois de `.claude/estado/*` e que nenhuma linha
    `.claude/estado/` com barra final sobrou; corrigir e repetir o comando. Se ainda sair `0`, parar
    e sinalizar `blocked` razão `premissa`. **Exit code `1` é o resultado esperado e não é erro**; a
    saída de `git check-ignore -v` **não** é critério aqui, porque com `-v` o git imprime o padrão
    decisivo mesmo quando ele é a negação que desfaz o ignore (`DM-12`).
  - se a ferramenta de escrita recusar arquivo vazio → gravar em `.claude/estado/.gitkeep` a única
    linha `# slot versionado; o conteudo deste diretorio e ignorado (ver .gitignore)` e devolver
    `contingência 2 acionada: .gitkeep com uma linha de comentário`.
  - se algum teste pré-existente de `tests/test_rdo.py` ficar vermelho pela forma decimal →
    ajustar **só** a asserção do literal de tokens desse teste, nada mais, e devolver
    `contingência 3 acionada: <nome do teste> ajustado`.
  - se `python -m pytest tests/test_telemetria.py -q --collect-only` já listar um teste cujo nome
    contenha `decimal` → não criar teste novo em `tests/test_telemetria.py`; citar o nome dele na
    linha de retorno e implementar só o TR de coerência, em `tests/test_rdo.py`.
- **Testes:** TF em `tests/test_rdo.py` — `rdo.py close --tokens-k 203.7` sai exit 0 e o RDO gerado
  contém `203.7`; TR em `tests/test_rdo.py` — `--tokens-k 80` grava `80.0` (uma casa decimal
  sempre, o que a regra concorrente `str(int)` daria como `80` e por isso discrimina); TF em
  `tests/test_telemetria.py` — `telemetria.py append --tokens_k 203.7` sai exit 0 e a linha
  apensada traz `203.7` na coluna `tokens_k`.
- **Verificação:** (as linhas 3, 4 e 5 trazem a saída **medida** com a entrega na árvore, `AE-4`;
  nenhuma delas é saída deduzida.)
  1. `python -m pytest tests/test_rdo.py tests/test_telemetria.py -q` → verde.
  2. `python -m pytest tests/ -q` → verde, total ≥ 145 (142 da baseline + os 3 TF deste card).
  3. `git check-ignore -q .claude/estado/.gitkeep` → **exit code 1** (= o caminho **não** está
     ignorado, que é o efeito de `DM-10`). Em PowerShell, ler com
     `git check-ignore -q .claude/estado/.gitkeep; $LASTEXITCODE` → imprime `1`. **Não** usar `-v`
     como critério: com `-v` o git reporta o padrão decisivo inclusive quando é negação, imprime
     `.gitignore:12:!.claude/estado/.gitkeep` e sai `0`, e isso **não** significa ignorado.
  4. `git check-ignore -v .claude/estado/tarefa-corrente.json` → imprime uma linha terminando em
     `.claude/estado/*` (medido: `.gitignore:11:.claude/estado/*`; o número da linha não é aceite,
     o padrão citado é).
  5. `git status --porcelain -uall .claude/estado/` → imprime exatamente `?? .claude/estado/.gitkeep`.
     O `-uall` é obrigatório: sem ele o git colapsa o diretório não rastreado e imprime
     `?? .claude/estado/`.
- **Pronto quando:** as cinco verificações acima saem como descrito, e `.gitignore` contém as duas
  linhas `.claude/estado/*` e `!.claude/estado/.gitkeep` nessa ordem, `rdo.py:772` diz `type=float`
  e o Passo 4 do `scrum-master` contém a palavra `garantir` antes de `gravar`.
- **Fora do escopo desta tarefa:** o hook `SubagentStop` e a fonte do número que ele grava são a
  `LM-T2` (`AE-3`); a atribuição de arquivo vermelho é a `LM-T3`.

### LM-T1a — O contrato de erro do pacote de fechamento: um domínio só para o consumo medido [Sonnet · classe implementacao]

- **Status:** `done` — fechada em 2026-09-18, **aprovada 100%**, bloqueante `nenhuma`, as sete dimensões `conforme`, recomendação `seguir`, sem pendência (RDO `docs/RDO/P-0740-LM-T1a-o-contrato-de-erro-do-pacote-de-fechamento-um-dominio-so-par.md`; laudo consumido e apagado, `DP-H`). O `AE-8` fecha aqui.
- **Esforço:** medium
- **Objetivo:** fechar o contrato de erro do módulo que a `LM-T1` entregou — os **três** números de
  consumo medido (`tool_uses`, `tokens_k`, `duracao_s`) passam a ter o **mesmo domínio** e a **mesma
  forma de recusa** nos dois verbos que os gravam. É o defeito 3 da §3 na parte que a `DM-11` não
  cobriu, e é o `AE-8` inteiro.
- **Depende de:** `DM-15` (o domínio e a forma da recusa), `DM-11` (a forma gravada de `--tokens-k`,
  que fica intocada), `DM-3` (coerência é aceite). Nenhuma tarefa anterior — a entrega da `LM-T1`
  já está na árvore. **Exclusão mútua com a `LM-T4a`:** as duas editam `.claude/tools/rdo.py` em
  regiões diferentes (aqui o `argparse` e o `cmd_close` do subcomando `close`; lá o
  `_HEADER_BRACKET_RE`) e **não podem estar abertas ao mesmo tempo** sobre ele; qualquer das duas
  ordens serve, e quem escolhe é quem despacha.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `.claude/tools/telemetria.py`
  - `tests/test_rdo.py`
  - `tests/test_telemetria.py`
- **Produto do módulo:** (a) em `rdo.py`, os três argumentos de consumo do subcomando `close`
  deixam de ser convertidos pelo `type=` do `argparse` e passam a ser validados em código, com a
  guarda rodando **antes** de qualquer outra checagem do `cmd_close`, recusando valor fora de
  domínio com `RdoValidationError` (exit 1); (b) em `telemetria.py`, `_validar_numero_nao_negativo`
  passa a recusar **não-finito** (`nan`, `inf`, `-inf`, em qualquer caixa) com a razão literal nova
  — o que vale para `tokens_k` **e** para `duracao_s`, que compartilham o validador; (c) o
  `--duracao-s` do `rdo.py close` passa a aceitar decimal e a gravar o valor com **uma casa**, a
  mesma forma que a `DM-11` fixou para `--tokens-k` e que o hook já emite para o verbo irmão.
- **A divergência medida (2026-09-18, rodada `RP-5`; residência única desta tabela — nenhum outro
  card a reenuncia). Um comando rodado por linha, exit code observado:**

  | literal | `rdo.py close` hoje | `telemetria.py append` hoje | depois desta tarefa |
  |---|---|---|---|
  | `tool_uses = -1` | aceita (segue para a gravação) | exit 1 · `tool_uses: '-1' é negativo` | exit 1 nos dois |
  | `tokens_k = -5` | aceita (grava `-5.0`) | exit 1 · `tokens_k: '-5' é negativo` | exit 1 nos dois |
  | `duracao_s = -60` | aceita (segue para a gravação) | exit 1 · `duracao_s: '-60' é negativo` | exit 1 nos dois |
  | `tokens_k = nan` | aceita (grava `nan`) | **aceita** (grava `nan` na série) | exit 1 nos dois · `não é finito` |
  | `tokens_k = inf` | aceita | **aceita** (grava `inf` na série) | exit 1 nos dois · `não é finito` |
  | `tokens_k = abc` | **exit 2** · bloco de `usage` do `argparse` | exit 1 · `tokens_k: 'abc' não é numérico` | exit 1 nos dois |
  | `duracao_s = 1020.6` (literal que o hook emite) | **exit 2** · `invalid int value: '1020.6'` | aceita | aceita nos dois |
  | `tokens_k = 1e3` | aceita (grava `1000.0`) | aceita (grava `1e3`) | segue como está — **fora do escopo** |

- **Textos literais das razões de recusa** (vocabulário fechado da `DM-15` (ii); os três primeiros
  já existem em `telemetria.py:58-80` e **não se reescrevem**, o quarto é novo nos dois módulos):
  `não é inteiro` · `não é numérico` · `é negativo` · `não é finito`. A linha inteira sai como
  `rdo: FALHOU - <campo>: '<valor>' <razão>` no `rdo.py` e como
  `telemetria: FALHOU - <campo>: '<valor>' <razão>` no irmão, com `<campo>` na forma da série
  (`tool_uses`, `tokens_k`, `duracao_s` — com sublinhado, nunca na forma da flag do `rdo.py`).
- **Coerência do módulo (aceite de `DM-3`):** o domínio de cada campo é **um só** para os dois
  verbos, e o corpo da mensagem de recusa é **idêntico**, variando só o prefixo do instrumento.
  Isso se exercita ponta a ponta, não por unidade: o mesmo literal recusado num CLI tem de ser
  recusado no outro, com a mesma razão. Sem importação cruzada entre os dois módulos (`DM-11`).
- **Testes** (oito; cada um com o valor que a **regra concorrente** — o código de hoje — dá sobre a
  mesma entrada, que é o que lhes dá poder discriminante):
  - `TF-close-tokens-k-negativo-recusa` — `close` com `--tokens-k -5` e `--plano` apontando arquivo
    **inexistente** sai exit 1 com `tokens_k: '-5' é negativo` no stderr. *Concorrente:* hoje sai
    exit 1 também, mas com `plano: arquivo não encontrado` — quem discrimina é a mensagem, e o
    teste prova de quebra que a guarda corre **antes** da checagem de `--plano` (`DM-15` (iii)).
  - `TF-close-tokens-k-nao-finito-recusa` — idem com `--tokens-k nan`: exit 1 com
    `tokens_k: 'nan' não é finito`. *Concorrente:* hoje o `type=float` converte `nan` sem reclamar
    e a execução segue até a checagem de plano.
  - `TF-close-tool-uses-negativo-recusa` — `--tool-uses -1`: exit 1 com
    `tool_uses: '-1' é negativo`. *Concorrente:* hoje o `argparse` converte e a execução segue.
  - `TF-close-tokens-k-nao-numerico-recusa-com-exit-1` — `--tokens-k abc`: exit **1** com
    `tokens_k: 'abc' não é numérico`. *Concorrente:* hoje sai **exit 2** com o bloco de `usage` do
    `argparse` — é esta linha que tranca a remoção do `type=`.
  - `TF-close-duracao-s-decimal-aceita-e-grava-uma-casa` — sobre o plano de fixture que os testes
    de `close` já usam, `--duracao-s 1020.6` fecha o RDO e o documento contém `1020.6`.
    *Concorrente:* hoje sai exit 2, `invalid int value: '1020.6'` — que é o literal que o hook
    emite para o verbo irmão.
  - `TR-close-consumo-valido-segue-igual` — o caminho feliz de hoje (`--tool-uses 5 --tokens-k 80
    --duracao-s 300`) continua fechando o RDO, com `80.0` e `300` legíveis no documento.
    *Concorrente:* guarda escrita com `>` no lugar de `>=` derrubaria o zero e o caminho feliz.
  - `TF-append-tokens-k-nao-finito-recusa-sem-escrever` — `append --tokens_k nan` sai exit 1 com
    `tokens_k: 'nan' não é finito` e **o TSV de destino não é criado**. *Concorrente:* medido hoje,
    sai exit 0 e grava a linha com o literal `nan` na coluna de tokens.
  - `TF-append-duracao-s-nao-finito-recusa` — `append --duracao_s inf` sai exit 1 com
    `duracao_s: 'inf' não é finito`. *Concorrente:* hoje sai exit 0 e grava `inf`. (Os dois campos
    passam pelo **mesmo** validador: um teste por termo, senão só metade da regra fica trancada.)
- **Verificação:** (toda linha abaixo foi **rodada** na rodada `RP-5` e traz a saída **medida** do
  mundo de antes; nenhuma é deduzida — `DM-12`):
  1. `python -m pytest tests/test_rdo.py tests/test_telemetria.py -q` → verde. Baseline medida:
     `47 passed` (40 + 7); depois desta tarefa, `55 passed` com os oito testes acima.
  2. `python -m pytest tests/ -q` → verde, piso ≥ **145** (medido na rodada `RP-5`: `145 passed`),
     mais os oito testes novos.
  3. Recusa de domínio no `rdo.py`, sem efeito em disco (a guarda corre antes da checagem de
     `--plano`, então nada é lido nem escrito):
     `python .claude/tools/rdo.py close --plano NAO-EXISTE.md --tarefa LM-T1 --tool-uses 5 --tokens-k -5 --duracao-s 60 --veredito aprovado --percentual 100 --bloqueante nenhuma --recomendacao seguir --pendencia-laudo nenhuma`
     → exit 1 e stderr contendo `rdo: FALHOU - tokens_k: '-5' é negativo`. **Antes (medido):**
     exit 1 e stderr `rdo: FALHOU - plano: arquivo não encontrado 'NAO-EXISTE.md'` — o exit code é
     o mesmo nos dois mundos, quem discrimina é a **mensagem**.
  4. Aceitação do literal do hook: o mesmo comando do item 3 com `--tokens-k 10 --duracao-s 1020.6`
     → exit 1 e stderr `rdo: FALHOU - plano: arquivo não encontrado 'NAO-EXISTE.md'` (isto é: o
     valor atravessou o domínio e o que falhou foi o plano). **Antes (medido):** exit **2** e
     `rdo.py close: error: argument --duracao-s: invalid int value: '1020.6'`.
  5. Recusa de domínio no `telemetria.py`, com o TSV de teste dentro de `.claude/estado/`, que o
     `.gitignore` exclui por `DM-10` (medido nesta rodada: `git check-ignore -q` sobre esse caminho
     → exit 0, isto é, ignorado):
     `python .claude/tools/telemetria.py append --data 2026-09-18 --projeto PantonicApp --tarefa X --modelo sonnet --tool_uses 1 --tokens_k nan --duracao_s 1 --fonte usage --file .claude/estado/rp5-verificacao.tsv`
     → exit 1, stderr contendo `telemetria: FALHOU - tokens_k: 'nan' não é finito`, e o arquivo
     `.claude/estado/rp5-verificacao.tsv` **não existe** ao fim. **Antes (medido):** exit 0,
     `telemetria: OK - linha adicionada`, com a linha gravada no arquivo. Apagar o arquivo depois
     da verificação, se ele existir.
- **Restrições desta tarefa:** a guarda do `rdo.py` corre **antes** da checagem de `--plano`
  (`DM-15` (iii)) — se rodar depois, a `Verificação` 3 sai com a mensagem de plano e a tarefa não
  prova nada. Nenhum `import` de um módulo no outro (`DM-11`). O corpo da mensagem é **igual** nos
  dois instrumentos; só o prefixo muda. `telemetria.py` continua **preservando a forma original**
  do literal aceito (`telemetria.py:79-80`, com teste vivo) — a guarda de finitude não pode
  normalizar valor nenhum. A gravação de `--tokens-k` segue `f"{...:.1f}"` (`DM-11`), e
  `--duracao-s` passa a ser gravada na **mesma** forma.
- **Não fazer:** não normalizar a forma gravada do irmão (`1e3` continua saindo `1e3` no TSV e
  `1000.0` no RDO — declarado fora do escopo pela `DM-15`); não mexer em `--percentual`,
  `--veredito` nem em nenhum outro argumento do `close` que não seja de consumo; não tocar
  `.claude/tools/telemetria_hook.py` nem `tests/test_telemetria_hook.py` (são a `LM-T2` item (c));
  não tocar o `_HEADER_BRACKET_RE` nem gramática de cabeçalho nenhuma (é a `LM-T4a`); não rodar
  `python .claude/tools/backlog.py check` nem tratá-lo como aceite (315 violações pré-existentes,
  `AE-1`); não reabrir a `LM-T1`, que está `done` e não se refaz.
- **Contingências:**
  1. se algum dos literais de `telemetria.py` citados aqui (`não é inteiro`, `não é numérico`,
     `é negativo`) não existir no arquivo exatamente como transcrito → parar e sinalizar `blocked`
     razão `premissa`, citando a linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho em teste **fora** de `tests/test_rdo.py` e
     `tests/test_telemetria.py` → seguir com a entrega e devolver na linha de retorno
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`;
  3. se alguma asserção **pré-existente** de `tests/test_rdo.py` quebrar por causa da casa decimal
     nova de `duracao_s` → ajustar **só** aquela asserção e devolver
     `contingência 3 acionada: <teste> ajustado para a forma de uma casa`. (Baseline medida na
     rodada: a única asserção que lê a duração é `tests/test_rdo.py:271`, `assert "80" in conteudo
     and "300" in conteudo`, que é **substring** e continua verdadeira com `300.0`.)
- **Pronto quando:** os três campos de consumo têm o mesmo domínio nos dois verbos e recusam fora
  dele com exit 1 e o mesmo corpo de mensagem; `nan` e `inf` são recusados **nos dois**; o literal
  de duração que o hook emite é aceito pelos dois; os oito testes nomeados existem nos dois
  arquivos de teste; e as cinco linhas de `Verificação` saem como escritas.

### LM-T2 — `B0` e `B1`: a cadência da janela na prosa do `scrum-master` [Sonnet · classe redacao]

- **Status:** `done` — fechada em 2026-09-19, **aprovada 100%**, bloqueante `nenhuma`, recomendação `escalar` (RDO `docs/RDO/P-0740-LM-T2-b0-e-b1-a-cadencia-da-janela-na-prosa-do-scrum-master.md`; laudo consumido e apagado, `DP-H`). Entregue sem redespacho: o bloqueio foi de aceite, corrigido pelo `ESC-6` (`DM-24`). Pendência: o `AE-9` segue aberto e deixa a primeira condição do `B1` inalcançável.
  lições das rodadas `RP-1`..`RP-5` e foi **recusada no `G-PLANREADY`** pelo loop, sem gastar
  executor (`AE-14`): mandava o executor decidir onde criar uma "função de atribuição" que não tinha
  residência, listava três testes sem sujeito executável e repetia um piso vencido. O módulo foi
  partido em três pela `DM-19`: **esta** carrega só a prosa do loop.
- **Esforço:** medium
- **Objetivo:** um só — o que faz a janela **continuar ou parar**, escrito na doutrina do loop.
  Cobre os defeitos 4 e 5 da §3 e absorve a `AUT-T3`. Nenhuma linha de código: esta tarefa edita
  **um** arquivo de prosa.
- **Depende de:** `LM-T2a` — as duas regras novas **citam o comando** que ela expõe, e publicar
  prosa que manda rodar um comando inexistente é o `AE-5` de novo (doutrina antes do instrumento).
  Mais `DM-19` (residência da atribuição) e a *Diretiva de execução do `P-0740`*, item 2 (a janela
  vai até o marco validável; pendência substantiva vira escalonamento ao consultor).
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Produto do módulo:** (a) regra **`B0`** nova, avaliada **antes** de `B1`; (b) `B1` reescrita em
  torno de **pendência substantiva** e roteada ao **consultor de plano**, com a janela seguindo;
  (c) as três superfícies do mesmo arquivo que citam `B1` postas em dia — a lista *O que obriga
  parada*, o Passo 10 e o relatório de encerramento —, mais a linha do Passo 9 sobre o número do
  hook, que o `AE-3` mediu errado cinco vezes nesta janela.
- **Âncoras medidas no `ESC-3` (2026-09-18; re-derivar no despacho, o arquivo é da orquestração):**
  `### Bloco B — continuar ou encerrar a janela` em `.claude/skills/scrum-master/SKILL.md:202`;
  cabeçalho da tabela em `:206-207`; linha `B1` em `:208`; `B2` `:209`; `B3` `:210`; `B4` `:211`;
  lista *O que obriga parada* em `:215-218`; Passo 9 em `:138-166`, com o parágrafo do `<usage>` em
  `:157-159`; Passo 10 em `:167-175`, com a linha `- **Ação:**` em `:173`; relatório de
  encerramento em `:237` (`- Plano conduzido e regra que encerrou a janela (\`A1\`..\`A9\` ou
  \`B1\`..\`B4\`, pelo identificador).`).
- **Passos, com os textos literais** (transcrever):
  1. Inserir, **antes** da linha `B1` da tabela do bloco B, a linha nova:
     ```
     | `B0` | vermelho de verificação, ou item de `pendencia=`, **atribuível a arquivo fora dos `Arquivos-alvo` da tarefa** — atribuição **medida** por `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --atribuir`, nunca julgada de memória | não é pendência da tarefa: registra `AE-<n>` com a atribuição medida, **não rebaixa** a entrega, não refaz laudo e **segue** por `B4` |
     ```
  2. Substituir a linha `B1` inteira por:
     ```
     | `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0` | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, instanciado uma vez por execução), que devolve decisão e reparo: a janela **segue** com o que ele devolver. **PARA** só se o consultor classificar o impedimento como **estratégico**; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) |
     ```
  3. Na linha 3 da seção (`Avaliado **depois** de \`A6\`..\`A9\`…`), acrescentar ao fim da frase:
     ```
     A precedência dentro do bloco é `B0` → `B1` → `B2` → `B3` → `B4`: o que é atribuível a arquivo alheio sai em `B0` e nunca chega a `B1`.
     ```
  4. Na lista *O que obriga parada*, substituir o trecho `ou pela recomendação \`escalar\` do laudo
     (\`B1\`), roteada ao planejador —` por:
     ```
     ou pela recomendação `escalar` do laudo (`B1`), roteada ao **consultor de plano** —
     ```
     e acrescentar, ao fim do mesmo bullet, a frase:
     ```
     Escalonamento ao consultor **não** encerra a janela: encerra-a só a classificação `estratégico` que ele devolver.
     ```
  5. No Passo 10, substituir a linha `- **Ação:** aplicar a tabela do bloco B, também por
     precedência.` pelo texto:
     ```
     - **Ação:** aplicar a tabela do bloco B, também por precedência, começando por `B0` — a atribuição de arquivo é **medida** pelo comando do `B0`, não julgada de memória.
     ```
  6. No relatório de encerramento, trocar `(\`A1\`..\`A9\` ou \`B1\`..\`B4\`, pelo identificador)`
     por:
     ```
     (`A1`..`A9` ou `B0`..`B4`, pelo identificador)
     ```
  7. No Passo 9, ao fim do parágrafo que manda apender a linha de `docs/telemetria.tsv`,
     acrescentar:
     ```
     O número da linha é o do bloco `<usage>` da notificação, **conferido**: o hook `SubagentStop` grava sozinho e já gravou valor inflado (`AE-3`); linha do hook que divergir do `<usage>` é corrigida à mão pelo loop. E o hook **não dispara** quando o subagente é retomado por `SendMessage` — nesse caso a linha é apensada pelo loop, como todas as outras.
     ```
- **Testes:** **nenhum `pytest`** — e isto é declaração, não omissão. As regras `B0`/`B1` são prosa
  lida pelo `scrum-master`; não há sujeito executável nesta tarefa. A versão anterior do card
  listava três TFs sobre "o comportamento do loop", que nenhum runner executa (`AE-14`). O que é
  executável — a atribuição — vive na `LM-T2a` e é testada lá.
- **Verificação:** (tarefa de redação: verificação **por efeito no arquivo-alvo**. Os itens 1 e 3
  foram **corrigidos pelo `ESC-6`** e re-rodados nos **dois** mundos, conforme `DM-24` (iii); os
  itens 2, 4 e 5 vieram do `ESC-3` e foram **reconferidos** aqui)
  1. Comando em **bloco cercado**, não em code span — o literal contém crase (`DM-24` (i)):
     ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '| `B0` |' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido no `ESC-6` nos dois mundos:** **0** antes da entrega (a linha não existia)
     e **1** depois. A forma anterior deste item usava crase **dupla**, artefato de escape do
     code span, e devolvia **0 nos dois mundos** — não discriminava nada, e é o `AE-19`.
  2. `pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'pendência substantiva' -SimpleMatch | Measure-Object).Count"`
     → ≥ 1. Baseline medida: **0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'roteada ao planejador' -SimpleMatch | Measure-Object).Count"
     ```
     → **0** (a rota velha desapareceu). **Medido:** **1** antes da entrega, na linha `:216`, e
     **0** depois. O padrão anterior deste item procurava `planejador` **em negrito**, que nunca
     existiu no arquivo: dava **0 nos dois mundos** (`AE-19`). Foi corrigido à mão pelo
     `scrum-master` no despacho — e é por isso que este item passou, enquanto o item 1, não
     conferido, parou a entrega.
  4. `pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '--atribuir' -SimpleMatch | Measure-Object).Count"`
     → ≥ 1 (a prosa cita o comando que a `LM-T2a` expõe). Baseline medida: **0**.
  5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o
     total que a árvore tiver **no despacho**, re-medido por quem despacha e registrado no
     dossiê; esta tarefa **não acrescenta teste** e **não pode reduzir** esse total — é o que
     tranca a suíte de conformance contra edição de doutrina. Referência histórica, não aceite:
     `165 passed` em 2026-09-19 (`ESC-5`).
- **Restrições desta tarefa:** o bloco A fica **intocado** — `A1`..`A9` não mudam de condição nem de
  ação. `B2`, `B3` e `B4` ficam **literais**: só a precedência passa a nomear `B0`. Nenhuma regra
  nova além de `B0`. O arquivo é da orquestração e muda fora do ciclo de tarefa: re-derivar as
  âncoras no despacho (contingência 1).
- **Não fazer:** não tocar `.claude/tools/review_evidence.py` (é a `LM-T2a`) nem
  `.claude/tools/telemetria_hook.py` (é a `LM-T2b`); não tocar `GOVERNANCA.md` (a doutrina da
  unidade de trabalho é a `LM-T4`); não tocar `.claude/agents/` (`DM-17`); não escrever teste
  `pytest` para regra de prosa; não commitar.
- **Contingências:**
  1. se qualquer um dos literais a substituir (passos 2, 4, 5, 6) não existir no arquivo exatamente
     como transcrito → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos` (esta tarefa não toca
     Python nenhum).
- **Pronto quando:** a tabela do bloco B tem `B0` antes de `B1` com os dois textos literais acima; a
  lista *O que obriga parada*, o Passo 9, o Passo 10 e o relatório de encerramento estão em dia com
  eles; e as cinco linhas de `Verificação` saem como escritas.

### LM-T2a — A atribuição como verbo: `review_evidence.py --atribuir` [Sonnet · classe implementacao]

- **Status:** `done` — fechada em 2026-09-19, **ressalva 91%**, bloqueante `nenhuma`, recomendação `escalar` (RDO `docs/RDO/P-0740-LM-T2a-a-atribuicao-como-verbo-review-evidence-py-atribuir.md`; laudo consumido e apagado, `DP-H`). Suíte 161 → 165. Pendências roteadas como `AE-17` e `AE-18`.
- **Esforço:** low
- **Objetivo:** um só — tornar **rodável** a pergunta que o `B0` da `LM-T2` faz: *este arquivo é da
  entrega ou é alheio?* A resposta já existe em código (`confrontar_escopo`); o que não existe é o
  **verbo**. Nenhuma lógica de classificação nova se escreve aqui.
- **Depende de:** `DM-19`. Nenhuma tarefa anterior. **Exclusão mútua com a `LM-T3a`** sobre
  `.claude/tools/review_evidence.py` (a `LM-T3` já fechou): as duas editam o arquivo em regiões
  diferentes — aqui o `main`/CLI, lá `coletar_estado_git` — e não podem estar abertas ao mesmo
  tempo; qualquer ordem serve.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Fatos medidos no `ESC-3` (2026-09-18):** `confrontar_escopo` (`review_evidence.py:282-333`) já
  devolve os cinco baldes da `DB-25`/`DB-32` (`fora_dos_alvos`, `de_outra_tarefa`,
  `registro_orquestracao`, `ato_do_dono`, `veredito`) e **não** devolve a lista do primeiro balde —
  os arquivos cobertos pelos alvos saem do laço por `continue`. As funções que alimentam a pergunta
  também já existem: `coletar_arquivos_tocados`, `extrair_arquivos_alvo` e
  `mapear_alvos_de_outras_tarefas`. `python .claude/tools/review_evidence.py … --atribuir` sai hoje
  **exit 2** com `review_evidence.py: error: unrecognized arguments: --atribuir`.
  `tests/test_review_evidence.py` está em **25 passed**; a suíte inteira, em **153**.
- **Produto do módulo:** a flag `--atribuir` no CLI de `review_evidence.py`: com ela, o script
  **não** monta dossiê — imprime a classificação de cada arquivo tocado desde `--desde` e sai
  **exit 0**, mesmo havendo arquivo sem atribuição (o verbo **informa**, quem julga é o reviewer
  pela rubrica).
- **Forma literal da saída** (residência única deste literal nesta tarefa; a prosa da `LM-T2` cita o
  comando, não o formato):
  ```
  atribuicao: <caminho> -> alvo-do-card
  atribuicao: <caminho> -> alvo-de-outra-tarefa (<ID>)
  atribuicao: <caminho> -> registro-da-orquestracao
  atribuicao: <caminho> -> ato-do-dono
  atribuicao: <caminho> -> sem-atribuicao
  atribuicao: OK - <N> arquivo(s), <M> sem atribuicao.
  ```
  Uma linha por arquivo, na ordem de `sorted()`, e a linha de resumo por último.
- **Restrições desta tarefa (o que garante "uma pergunta, uma implementação"):** o primeiro balde
  (`alvo-do-card`) é obtido por **diferença de conjuntos** sobre o que `confrontar_escopo` já
  devolveu — nunca por uma segunda checagem de cobertura. Nenhuma função de classificação nova;
  nenhuma cópia de `coberto()`; nenhum `import` de `review_evidence` em outro módulo.
- **Testes** (três, com a regra concorrente de cada):
  - `TF-atribuir-classifica-nos-cinco-baldes` — com a lista de tocados e os alvos injetados como os
    testes do módulo já fazem, a saída traz uma linha por arquivo com o balde certo, inclusive
    `alvo-do-card` para o arquivo coberto. *Concorrente:* hoje não há saída nenhuma — o argumento
    nem é reconhecido (exit 2).
  - `TF-atribuir-sai-0-mesmo-com-arquivo-sem-atribuicao` — exit **0** com pelo menos um
    `sem-atribuicao` na saída. *Concorrente:* uma implementação que devolvesse 1 (tratando o balde
    como falha) faria o `B0` do loop encerrar janela por informação, que é exatamente o defeito 4
    da §3.
  - `TR-atribuir-nao-monta-dossie` — com `--atribuir`, nenhum documento é escrito e o caminho de
    `--out` não é criado. *Concorrente:* implementar a flag depois da montagem do documento
    gravaria o dossiê como efeito colateral.
  - `TF-atribuir-alvo-diretorio-casa-por-prefixo` (acrescentado pelo `ESC-4`, `DM-21` (ii)(a)) —
    card cujo `Arquivos-alvo` declara um **diretório** e arquivo tocado **dentro** dele sai
    `alvo-do-card`. *Concorrente:* é este o caso em que uma segunda implementação por caminho
    **exato** — a reimplementação plausível que a `Restrição` proíbe — devolveria
    `sem-atribuicao`. É o teste que dá poder discriminante à exigência de "uma pergunta, uma
    implementação", que sozinha não é verificável (`DM-21` (i)).
- **Verificação:** (medida no `ESC-3` para o mundo de antes — `DM-12`)
  1. `python -m pytest tests/test_review_evidence.py -q` → verde. Baseline **re-medida no
     `ESC-4`**, depois da `LM-T3`: `28 passed`; depois desta tarefa, `32 passed` (quatro testes).
  2. `python -m pytest tests/ -q` → verde, piso ≥ **156** (re-medido no `ESC-4`: `156 passed`;
     o piso de 153 venceu com a `LM-T3`), mais os quatro testes novos.
  3. Execução real, sobre este plano:
     `python .claude/tools/review_evidence.py --plano docs/plans/P-0740-loop-de-modulos.md --tarefa LM-T3 --desde 428246c --atribuir`
     → exit **0**, com uma linha `atribuicao: .claude/tools/review_evidence.py -> alvo-do-card` e a
     linha de resumo. **Antes (medido):** exit **2**,
     `review_evidence.py: error: unrecognized arguments: --atribuir`.
  4. Regressão do caminho de dossiê: o mesmo comando **sem** `--atribuir` e com `--out` continua
     gerando o documento e saindo exit 0 (medido hoje: exit 0 para as onze tarefas do plano).
- **Não fazer:** não mudar `confrontar_escopo` nem nenhum dos cinco baldes (quem os altera é o
  `P-0739`, e a seção de arquivo vermelho do dossiê é a `LM-T3`); não tocar
  `.claude/skills/scrum-master/SKILL.md` (é a `LM-T2`); não criar módulo novo em `.claude/tools/`;
  não rodar `python .claude/tools/backlog.py check` como aceite (`AE-1`); não commitar.
- **Contingências:**
  1. se `confrontar_escopo` não devolver as quatro chaves citadas acima com esses nomes exatos →
     parar e sinalizar `blocked` razão `premissa`, citando a assinatura encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho **fora** de `tests/test_review_evidence.py` →
     seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos
     alvos`.
- **Pronto quando:** `--atribuir` existe, imprime os cinco baldes na forma literal acima, sai 0
  mesmo com arquivo sem atribuição, não monta dossiê e acerta o **alvo-diretório**; os quatro
  testes existem; e as quatro linhas de `Verificação` saem como escritas.

### LM-T2b — O número do hook: a fonte do `tokens_k` e a forma do `modelo` [Sonnet · classe implementacao]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `escalar`; pendência substantiva roteada pelo `B1` como `AE-27`, quatro achados de processo no laudo (um já fechado por `DM-33`/`DM-34`). RDO: `docs/RDO/P-0740-LM-T2b-o-numero-do-hook-a-fonte-do-tokens-k-e-a-forma-do-modelo.md`. Fecha o `AE-3`, com confirmação em produção. Estado anterior: `review` (desfecho do `ESC-11`/`DM-34`) — chegou ao laudo depois de **dois** `blocked` razão `premissa` pelo `A3b`, nenhum deles por defeito de produto e **nenhum consumindo retentativa** (a tarefa chega com 0 gastas). Os Passos 0 e 1 e a Contingência 1 estão **consumidos** pelo 2º despacho e não se re-executam. Estado anterior, para registro: `blocked` razão `premissa` (2026-09-19, `A3b`, **segundo bloqueio**) — **desfecho
  decidido no `ESC-11` (2026-09-19, `DM-34`): a tarefa não se redespacha.** O loop materializa
  `review` **pelo instrumento** (`python .claude/tools/backlog.py status LM-T2b review`) e despacha
  o `pantonic-reviewer` sobre o estado atual da árvore; o consultor não escreve estado à mão.
  Histórico das duas paradas, as duas por conduta **correta** do executor (Regra 8 — ele não alarga
  autorização nem conserta comando de aceite por conta própria): 1º despacho, `AE-24` (nenhuma
  contingência autorizava tocar a asserção pré-existente; resolvido pelo `DM-33`); 2º despacho,
  `AE-25` (a linha 4 da `Verificação` era inexequível; reparada pelo `DM-34`). **Nenhuma das duas
  consumiu retentativa** (`A3b` não consome): a tarefa chega ao laudo com o contador em **0**, e
  `A6` continua disponível se o veredito exigir. Card novo do `ESC-3` (`DM-20`), residência do item
  (c) da `LM-T2` antiga e do `AE-3`.
- **Estado medido no encerramento (`ESC-11`, 2026-09-19 — é o que o `reviewer` julga):** Passos 0,
  1 e 2 **aplicados** (a frase do Passo 2 está no docstring do teste, conferida);
  `python -m pytest tests/test_telemetria_hook.py -q` → **`10 passed`**;
  `python -m pytest tests/ -q` → **`175 passed`**; a asserção da linha 274 espera `sonnet` com o
  `_estado_valido` ainda entregando `Sonnet` maiúsculo; `cache_read_input_tokens` → **4**. As
  quatro linhas de `Verificação` saem como escritas, com a 4 já na forma reparada. **Os Passos 0 e
  1 e a Contingência 1 estão consumidos**: foram escritos contra a árvore **pré-entrega** e hoje
  disparariam `blocked` numa terceira execução (o Passo 0 exige `1 failed, 9 passed`, e a árvore
  está `10 passed`) — ficam como registro do 2º despacho e **não** se re-executam. É este o motivo
  técnico de a tarefa ir à revisão em vez de a um terceiro despacho (`DM-34` (ii)).
- **Autoria, para efeito de laudo (`DM-34` (ii)):** a entrega veio de **dois executores em
  contextos distintos** — o 1º aplicou (a), (b), (c) e os quatro testes novos; o 2º aplicou a
  asserção da linha 274 e a frase do docstring. O laudo julga **a árvore contra o card**, não o
  autor, e o recorte de evidência `--desde 6eebccd` cobre os dois atos num delta só, porque **não
  houve commit entre eles**. Autor de registro no RDO: o **2º executor**, com a nota de que a
  entrega se deu em dois atos, por `AE-24` e `AE-25`.
- **Esforço:** low
- **Objetivo:** um só — o número que o hook grava passa a ser o mesmo que a notificação mede, e a
  série passa a ter **uma** grafia por modelo.
- **Depende de:** `DM-20` (a fórmula, **calibrada** no `ESC-3` e **re-confirmada** no `ESC-10`) e
  `DM-33` (a autorização que destravou o card). Nenhuma tarefa anterior.
- **Arquivos-alvo:**
  - `.claude/tools/telemetria_hook.py`
  - `tests/test_telemetria_hook.py`
- **A calibração medida no `ESC-3` (2026-09-18) — residência única desta tabela.** Sobre os
  transcripts reais desta janela (`…/subagents/agent-*.jsonl`), três fórmulas foram computadas e
  confrontadas com o `<usage>` da notificação, que é o número verdadeiro:

  | subagente (tool uses) | `<usage>` medido | soma por `message.id` (hoje) | **usage da última mensagem** | última + soma dos `output` |
  |---|---|---|---|---|
  | executor (4) | 59,5k | 251,1k | **59,5k** | 61,6k |
  | executor (17) | 49,8k | 505,2k | **49,8k** | 54,2k |
  | executor (30) | 94,8k | 2330,8k | **94,8k** | 118,4k |
  | executor (13) | 75,3k | 946,9k | **75,3k** | 99,9k |
  | reviewer (25) | 69,6k | 941,8k | **69,6k** | 84,7k |
  | reviewer (20) | 64,0k | 918,5k | **64,0k** | 81,4k |

  Seis de seis: a **última** entrada `assistant` com `usage`, somando os quatro campos
  (`input_tokens + cache_creation_input_tokens + cache_read_input_tokens + output_tokens`), dá
  **exatamente** o número da notificação. A soma por `message.id` reproduz **exatamente** os valores
  errados que o hook gravou hoje (`251.1`, `505.2`, `2330.8`, `946.9`) — a causa está identificada,
  não suposta: `cache_read_input_tokens` é o contexto **inteiro** relido a cada turno, e somá-lo
  turno a turno multiplica o total pelo número de turnos.
- **Re-confirmação do `ESC-10` (2026-09-19) — quatro transcripts desta janela, medidos pelo
  consultor com as duas fórmulas sobre o `.jsonl` real:**

  | subagente (tool uses) | `<usage>` da notificação | soma por `message.id` | **usage da última mensagem** | o que o hook gravou |
  |---|---|---|---|---|
  | `LM-T3a` (36) | 86,0k | 1763,1k | **86,0k** | 1763,1k |
  | `LM-T2d` (17) | 50,6k | 334,7k | **50,6k** | 334,7k |
  | `LM-T2e` (7) | 44,4k | 212,5k | **44,4k** | 212,5k |
  | `LM-T2b` (9) | 72,9k | 371,6k | **72,9k** | **72,9k** |

  **Quatro de quatro** para a fórmula da última mensagem — com o `ESC-3`, **dez de dez**. A quarta
  linha, que saiu **exata** e parecia exceção, tem causa **medida, não suposta**: o
  `SubagentStop` roda **depois** que o subagente termina e importa `telemetria_hook.py` do disco
  **naquele instante**; o executor da `LM-T2b` reescreveu `calcular_consumo` às **05:40** e o
  transcript dele fechou às **05:42** (`mtime` dos dois arquivos, conferidos), de modo que o hook
  que gravou a linha dele **já era o corrigido**. A prova é numérica: o código velho teria gravado
  **371,6k** para esse mesmo transcript, e o gravado foi **72,9k**. Nas três anteriores — todas
  fechadas antes das 05:40 — o gravado bate **exatamente** com a soma por `message.id`. Ou seja, a
  quarta linha não contradiz a fórmula: é a fórmula funcionando **em produção, sobre a própria
  execução que a escreveu**. Consequência para a redação: *"o hook grava sempre para mais"* é
  verdade sobre toda execução fechada **antes** de o reparo entrar na árvore, e falsa depois —
  o card não usa mais a palavra *sempre* sem esse recorte (`AE-24`).
- **Produto do módulo:** (a) `calcular_consumo` passa a devolver, em `tokens_k`, o total de `usage`
  da **última** entrada `assistant` que tiver `usage`, em vez da soma por `message.id`; (b)
  `montar_args_append` passa a normalizar o `modelo` para **minúsculas** (`str(...).strip().lower()`);
  (c) o docstring do módulo (`:10`) e o de `calcular_consumo` passam a enunciar a fórmula nova e a
  razão medida, substituindo a nota de dedupe por `message.id`.

  **Por que minúscula, medido no `ESC-10`** (a redação anterior dizia só *"é a convenção da série"*,
  e isso é impreciso): a série tem **as duas** grafias do mesmo modelo — `Opus` 103 × `opus` 55,
  `Sonnet` 72 × `sonnet` 50, `Haiku` 10 (contagem da coluna 4 de `docs/telemetria.tsv`) —, que é
  exatamente o `AE-3`; e a **fonte** emite minúscula: o `meta.json` do subagente traz
  `"model":"sonnet"`. Normaliza-se para o que a fonte diz, não para o que a maioria do histórico
  tem. A série histórica **não** se reescreve (é dado, não alvo de tarefa).
- **Estado da árvore no despacho — medido pelo consultor no `ESC-10`, e é o que torna este card
  uma tarefa de uma linha:** o executor que devolveu `blocked` **já aplicou** (a), (b) e (c) e
  **já escreveu os quatro testes novos**, e esse trabalho **fica** — não se refaz e não se
  descarta (`git diff --stat HEAD`: `telemetria_hook.py` +50/−30 aproximado,
  `tests/test_telemetria_hook.py` +95). Medido agora:
  `python -m pytest tests/test_telemetria_hook.py -q` → **`1 failed, 9 passed`** (10 testes no
  módulo, contra 6 antes), e a **única** falha da árvore inteira é a asserção pré-existente de
  `tests/test_telemetria_hook.py:274`. `python -m pytest tests/ -q` → **`1 failed, 174 passed`**.
- **Passos:**
  0. **Conferir o estado acima antes de editar** (é conferência, não entrega): rodar
     `python -m pytest tests/test_telemetria_hook.py -q`. Se a saída **não** for
     `1 failed, 9 passed` com a falha em `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv`,
     a premissa deste card caiu → parar e sinalizar `blocked` razão `premissa`, citando a saída
     obtida. **Nada de (a), (b) ou (c) se reimplementa**: eles já estão na árvore, e reescrevê-los
     é retrabalho, não entrega.
  1. Em `tests/test_telemetria_hook.py`, **linha 274**, no teste
     `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv`, substituir a asserção
     ```
     assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tSonnet\t5\t1.0\t0.0\tusage"
     ```
     por
     ```
     assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage"
     ```
     — **só a grafia do modelo muda**. O `_estado_valido` do teste continua alimentando
     `"modelo": "Sonnet"` **maiúsculo**: é isso que faz a asserção passar a ser o guarda **ponta a
     ponta** da normalização (payload → `processar` → `telemetria.py` → linha do TSV), em vez de
     só repetir a grafia de entrada. O caso do teste **não** muda, o nome **não** muda, nenhuma
     outra asserção dele muda.
  2. No docstring desse mesmo teste, acrescentar a frase
     ```
     A grafia esperada do modelo é minúscula desde a `LM-T2b` (`AE-3`, `DM-33`): o payload entrega `Sonnet` e o hook normaliza — a asserção mede a normalização ponta a ponta, não a grafia de entrada.
     ```
     — se o teste não tiver docstring, criar com essa única frase.
- **Verificação:** (`DM-12`: toda baseline abaixo foi **rodada** pelo consultor no `ESC-10`, na
  árvore de hoje, e não deduzida)
  1. `python -m pytest tests/test_telemetria_hook.py -q` → **`10 passed`**. **Medido antes:
     `1 failed, 9 passed`**. É a linha que discrimina a entrega: o número de testes **não** muda
     (os quatro novos já existem), muda a falha virar verde.
  2. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total
     re-medido **no despacho**, e esta tarefa **não pode reduzi-lo**. Medido agora:
     **`1 failed, 174 passed`** → esperado depois: **`175 passed`**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/telemetria_hook.py -Pattern 'cache_read_input_tokens' | Measure-Object).Count"
     ```
     → ≥ 2 (o campo continua sendo somado **dentro** da última mensagem; o que muda é o escopo da
     soma, não os campos). **Medido agora: 4** — a baseline `2` publicada no `ESC-6` envelheceu
     com a entrega de (a) e (c), que é exatamente o `AE-21`; por isso o aceite é **relação** (≥ 2),
     não literal.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path tests/test_telemetria_hook.py -Pattern 'EXA-T55\tsonnet' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **1** (a asserção passou a esperar a grafia minúscula). **Medido nos dois mundos no
     `ESC-11`: 1** na árvore entregue e **0** numa cópia com a grafia pré-entrega — é o
     `-CaseSensitive` que faz a linha discriminar, e sem ele o mesmo padrão dá **1 nos dois
     mundos** e não mede nada, que é exatamente o `AE-25`. A forma anterior deste item
     (`'EXA-T55\tSonnet' -SimpleMatch`, esperando 0) era **inexequível**: sem `-CaseSensitive` ela
     casa a linha nova e devolve 1.

- **Restrições desta tarefa:** `tool_uses` e `duracao_s` ficam **como estão** — conferidos contra a
  notificação e certos (9 tool uses na `LM-T2b`, batendo). `fonte=usage` continua sendo a fonte
  declarada. Nenhuma mudança em `telemetria.py`. **Nenhuma outra asserção de teste pré-existente é
  tocada**: a autorização do `DM-33` alcança **uma** linha, a 274, e só a grafia do modelo nela.
- **Não fazer:** não reimplementar (a), (b) ou (c) — já estão na árvore (Passo 0); não tentar cobrir
  o caso do subagente **retomado por `SendMessage`** (medido no `ESC-3`: o `SubagentStop` não
  dispara, e a compensação é a linha do Passo 9 que a `LM-T2` publica); não tocar
  `docs/telemetria.tsv` — nem para reescrever as grafias antigas, nem para corrigir as três linhas
  infladas desta janela (a série é **dado**; a correção à mão é ato do loop, não desta tarefa); não
  tocar `.claude/skills/scrum-master/SKILL.md`; não commitar.
- **Contingências:**
  1. se a linha 274 não for a asserção transcrita acima (arquivo mexido desde a medida) → **não**
     procurar a asserção em outra linha por conta própria: parar e sinalizar `blocked` razão
     `premissa`, citando a linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho em teste **fora** de
     `tests/test_telemetria_hook.py` → seguir com a entrega e devolver
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.
- **Pronto quando:** `python -m pytest tests/test_telemetria_hook.py -q` sai `10 passed`; a suíte
  inteira sai `175 passed`; a asserção da linha 274 espera `sonnet` com o payload ainda entregando
  `Sonnet`; e as quatro linhas de `Verificação` saem como escritas.

### LM-T2c — `A8a`: a regra do bloco A para `recomendacao=escalar` [Sonnet · classe redacao]

- **Status:** `done` — fechada em 2026-09-19, **aprovada 100%**, bloqueante `nenhuma`, recomendação `escalar` (RDO `docs/RDO/P-0740-LM-T2c-a8a-a-regra-do-bloco-a-para-recomendacao-escalar.md`; laudo consumido e apagado, `DP-H`). **Primeiro fechamento da janela materializado pela regra escrita** (`A8a`, que esta própria tarefa entregou) e não por julgamento do loop. Pendência roteada como `AE-20`.
  aberto desde a `LM-T1` com rota "matéria da `LM-T2`" e que a `LM-T2` **não podia** fechar: as
  `Restrições` dela mandavam o bloco A ficar intocado. Buraco de **alocação**, não de entrega — a
  `LM-T2` fechou `done` aprovada 100% exatamente por obedecer à restrição.
- **Esforço:** low
- **Objetivo:** um só — o bloco A passa a ter regra para `recomendacao=escalar`. Sem ela, o `B1`
  que a `LM-T2` acabou de publicar é **inalcançável pela própria primeira condição**: o bloco B só
  é avaliado depois de o bloco A dizer "segue", e `escalar` não casa com `A6` (`refazer`), `A7`
  (`reprovado`), `A8` (`seguir com ressalva`) nem `A9` (`seguir`).
- **Depende de:** `LM-T2` (fechada — é a tabela dela que esta regra completa) e `DM-25`. **Precede
  a `LM-T4`**, que publica doutrina citando as tabelas de roteamento e tem o mesmo arquivo em
  `Arquivos-alvo`: publicar doutrina sobre um bloco A incompleto é a ordem invertida que a `DM-13`
  proíbe no eixo dela. As duas **não podem estar abertas ao mesmo tempo** sobre
  `.claude/skills/scrum-master/SKILL.md`.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Produto do módulo:** (a) a linha `A8a` na tabela do bloco A, com a precedência declarada; (b) as
  **quatro** superfícies do mesmo arquivo que enumeram as regras do bloco A postas em dia (Passo 7,
  gatilho do Passo 8, parágrafo do consumo do laudo, relatório de encerramento); (c) o corpus
  medido registrado em uma frase, para que a regra não pareça autorada de memória.
- **Fatos medidos no `ESC-7` (2026-09-19; re-derivar no despacho, o arquivo é da orquestração):**
  tabela do bloco A em `.claude/skills/scrum-master/SKILL.md:187-198`, com `A7` em `:196`, `A8` em
  `:197` e `A9` em `:198`; o parágrafo do consumo do laudo em `:199-204` (a enumeração
  ``` `A6`, `A7`..`A9` e `B1` ``` em `:203`); Passo 7 em `:124-128`, com a enumeração
  ``` lido por `A6`, `A8`, `A9` e `B1`. ``` quebrada entre `:126` e `:127`; gatilho do Passo 8 em
  `:132` (``` (regras `A1`..`A3b`) e passo 7 concluído (`A6`..`A9`) ```); relatório de encerramento
  em `:242`. **Baselines, com os comandos publicados abaixo:** `A8a` no arquivo → **0**
  ocorrências; a frase do produto (c) → **0**.
- **Corpus medido que a regra descreve (quatro ocorrências reais, janela de 2026-09-18/19):**
  `LM-T7` (veredito `ressalva`, 90%, bloqueante `nenhuma`, recomendação `escalar`), `LM-T3`
  (`ressalva` 91%), `LM-T2a` (`ressalva` 91%) e `LM-T2` (`aprovado` 100%). Em **todas** o
  `scrum-master` materializou o fechamento por julgamento próprio, porque a tabela não prescrevia o
  caso — improviso que a `DP-G` proíbe ("materializa **sem discricionariedade**"). Em nenhuma das
  quatro `bloqueante` era diferente de `nenhuma`; o caso `escalar` **com** bloqueante ainda não
  ocorreu, e é por isso que a regra o resolve por **precedência** (`A7` vence), e não por texto
  próprio.
- **Passos, com os textos literais** (transcrever):
  1. Inserir na tabela do bloco A, **entre** a linha `A7` e a linha `A8`, a linha nova:
     ```
     | `A8a` | `recomendacao=escalar` (com `bloqueante=nenhuma`) | **escalar não é desfecho de tarefa**: fecha o RDO pelo **veredito** transcrito — `aprovado` quando o veredito é `aprovado`, `aprovado com ressalva` quando é `ressalva` —, com cada achado do laudo saindo com rota, como em `A8`. A pendência **não** morre com o laudo: segue ao bloco B, onde o `B1` a registra como `AE-<n>` e a roteia ao consultor de plano. Precedência: `A6` e `A7` vencem esta regra — `bloqueante` diferente de `nenhuma` implica `veredito=reprovado`, que é `A7` —, e esta vence `A8` e `A9`, que leem a mesma recomendação |
     ```
  2. No Passo 7, substituir `lido por \`A6\`,` + quebra + `  \`A8\`, \`A9\` e \`B1\`.` por:
     ```
     lido por `A6`,
       `A8a`, `A8`, `A9` e `B1`.
     ```
     (a quebra de linha e a indentação de dois espaços são as do arquivo; só a lista muda).
  3. No gatilho do Passo 8, trocar `passo 7 concluído (\`A6\`..\`A9\`)` por:
     ```
     passo 7 concluído (`A6`..`A9`, inclusive `A8a`)
     ```
  4. No parágrafo que fecha o bloco A, trocar `\`A6\`, \`A7\`..\`A9\` e \`B1\`` por:
     ```
     `A6`, `A7`..`A9` (inclusive `A8a`) e `B1`
     ```
     e acrescentar, ao fim do mesmo parágrafo, a frase:
     ```
     A `A8a` existe porque o caso foi medido **quatro vezes** na janela de 2026-09-18/19 (`LM-T7`, `LM-T3`, `LM-T2a` e `LM-T2`), todas com `bloqueante=nenhuma`, e em todas o loop materializou o fechamento **por julgamento próprio** — improviso que a `DP-G` proíbe.
     ```
  5. No relatório de encerramento, trocar `(\`A1\`..\`A9\` ou \`B0\`..\`B4\`, pelo identificador)`
     por:
     ```
     (`A1`..`A9`, inclusive `A8a`, ou `B0`..`B4`, pelo identificador)
     ```
- **Testes:** **nenhum `pytest`** — declaração, não omissão (mesma razão da `LM-T2`, `AE-14`): a
  tabela do bloco A é prosa lida pelo `scrum-master`, sem sujeito executável. O que existe de
  executável nesta matéria já está trancado: `rdo.py close` aceita `--recomendacao "escalar"` como
  texto livre e calcula o desdobramento **pelo veredito**, que é exatamente o que a regra prescreve
  — nenhuma linha de código muda.
- **Verificação:** (`DM-24`: comando em bloco cercado, `-SimpleMatch`, e os **dois** valores
  rodados; as baselines abaixo foram medidas no `ESC-7` com estes mesmos comandos)
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '| `A8a` |' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0** — a célula não existe.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'escalar não é desfecho de tarefa' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'A8a' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 5** (a célula mais as quatro superfícies do produto (b)). **Medido antes: 0**. É esta
     linha que discrimina a entrega **completa** da entrega que só acrescenta a linha da tabela.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '`A8a`, `A8`, `A9` e `B1`' -SimpleMatch | Measure-Object).Count"
     ```
     → **1** (a enumeração do Passo 7). **Medido antes: 0**.
  5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total
     que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa **não acrescenta
     teste** e **não pode reduzir** esse total. Referência histórica, não aceite: `165 passed` em
     2026-09-19.
- **Restrições desta tarefa:** `A1`..`A3b`, `A6`, `A7`, `A8` e `A9` ficam **literais** — nenhuma
  condição e nenhuma ação delas muda; o que entra é uma linha nova e a precedência dela. O bloco B
  fica **intocado**: `B0` e `B1` são entrega fechada da `LM-T2` e já tratam a pendência. A
  numeração existente **não se renumera** — `A8a` é sufixo, pelo mesmo idioma de `LM-T4a`/`BKL-T2a`,
  justamente para não invalidar os identificadores já citados em RDOs e no diário.
- **Não fazer:** não tocar `.claude/tools/rdo.py` nem nenhum instrumento — a matéria é prosa e o
  `close` já faz o que a regra descreve; não tocar `GOVERNANCA.md` (é a `LM-T4`); não tocar
  `.claude/agents/` (`DM-17`); não escrever teste `pytest` para regra de prosa (`AE-14`); não
  commitar.
- **Contingências:**
  1. se qualquer um dos cinco literais a substituir não existir no arquivo exatamente como
     transcrito (o arquivo é da orquestração e muda fora do ciclo) → parar e sinalizar `blocked`
     razão `premissa`, citando a linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos` (esta tarefa não toca
     Python nenhum).
- **Pronto quando:** a tabela do bloco A tem `A8a` entre `A7` e `A8`, com o texto literal acima; as
  quatro superfícies do produto (b) citam `A8a`; a frase do corpus medido está no parágrafo do
  bloco A; e as cinco linhas de `Verificação` saem como escritas.

### LM-T2d — A partição do bloco A por veredito: `A6a` e o domínio de `A8a` [Sonnet · classe redacao]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `escalar`; pendência substantiva roteada pelo `B1` como `AE-22` (a `A7` ficou incoerente com o instrumento). RDO: `docs/RDO/P-0740-LM-T2d-a-particao-do-bloco-a-por-veredito-a6a-e-o-dominio-de-a8a.md`. Card novo do `ESC-8` (2026-09-19), residência única do `AE-20`. A `LM-T2c`
  está `done` aprovada 100% e **não se refaz**: o que ela entregou continua de pé, e esta tarefa
  fecha as duas lacunas que a regra nova deixou no bloco A.
- **Esforço:** low
- **Objetivo:** um só — o bloco A passa a ser uma **partição**: todo par (`veredito`,
  `recomendacao`) tem exatamente uma regra, e nenhuma regra manda fazer o que o instrumento de
  fechamento recusa.
- **Depende de:** `LM-T2c` (fechada — é a `A8a` dela que esta tarefa completa) e `DM-26`. **Precede
  a `LM-T4`**, pela mesma razão da `LM-T2c`: mesmo arquivo em `Arquivos-alvo` (exclusão mútua) e
  doutrina não se publica sobre tabela de roteamento incompleta.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Produto do módulo:** (a) a linha `A6a`, entre `A6` e `A7`; (b) a condição de `A8a` reescrita em
  torno do **veredito**, não do bloqueante; (c) a frase de partição no parágrafo do bloco A; (d) as
  quatro enumerações do mesmo arquivo postas em dia, como na `LM-T2c`.
- **As duas lacunas, medidas no `ESC-8` (2026-09-19):**
  1. **Regra que manda fazer o que o instrumento recusa.** A tripla (`reprovado`,
     `bloqueante=nenhuma`, `escalar`) casa `A8a`, que manda fechar o RDO **pelo veredito**; mas
     `python .claude/tools/rdo.py close --veredito reprovado` sai **exit 2** com
     `argument --veredito: invalid choice: 'reprovado' (choose from 'aprovado', 'ressalva')` — o
     `close` fecha `aprovado` ou `ressalva`, e `reprovado` é desfecho de **outra** natureza.
  2. **Combinação sem regra nenhuma.** `escalar` com `bloqueante` diferente de `nenhuma` e
     retentativas = 0 não casa nada: `A7` exige retentativas = 1, `A8a` exige `bloqueante=nenhuma`,
     `A6` exige `recomendacao=refazer`.
  As duas são **o mesmo buraco** visto de dois lados: *entrega reprovada cujo laudo recomenda
  escalar, antes de a retentativa ser gasta*. Baselines dos comandos publicados abaixo: `A6a` no
  arquivo → **0**; a condição velha de `A8a` → **1**; a frase de partição → **0**.
- **Passos, com os textos literais** (transcrever):
  1. Inserir na tabela do bloco A, **entre** a linha `A6` e a linha `A7`, a linha nova:
     ```
     | `A6a` | `veredito=reprovado` e `recomendacao=escalar` (qualquer `bloqueante`, qualquer contador de retentativas) | **não** fecha RDO e **não** gasta retentativa: materializa a tarefa como `blocked` razão `premissa`, com a pendência do laudo transcrita na razão, registra o achado como `AE-<n>` em `## Achados da execução` do plano e escala ao **consultor de plano**, que decide entre refazer com diretivas novas, emendar o card ou mudar a rota; a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2). Refazer antes de escalar gastaria a retentativa numa rota que o laudo já pediu para rever. Precedência: `A6` vence esta regra — lá o próprio laudo mandou refazer —, e esta vence `A7` e `A8a` |
     ```
  2. Na linha `A8a`, substituir a condição
     ```
     `recomendacao=escalar` (com `bloqueante=nenhuma`)
     ```
     por
     ```
     `recomendacao=escalar` e `veredito` ∈ {`aprovado`, `ressalva`}
     ```
     — nada mais da linha muda. A condição nova **subsume** a antiga (`bloqueante` diferente de
     `nenhuma` implica `veredito=reprovado`, o que o arquivo já afirma) e, ao mesmo tempo, impede
     que a regra mande fechar o que o `close` recusa.
  3. Acrescentar ao parágrafo que fecha o bloco A, depois da frase da `A8a`, a frase nova:
     ```
     O bloco A parte **primeiro por veredito, depois por recomendação**: `veredito=reprovado` é decidido por `A6`, `A6a` ou `A7` e **nunca por `A8a`, `A8` ou `A9`**, que só são alcançadas com veredito `aprovado` ou `ressalva`. É essa partição que impede entrega reprovada de ser fechada como aprovada por uma recomendação `seguir`, e é ela que garante que nenhuma regra mande fechar o que o instrumento recusa — medido: `rdo.py close --veredito reprovado` sai exit 2, `invalid choice`.
     ```
  4. No Passo 7, trocar a enumeração `` `A8a`, `A8`, `A9` e `B1`. `` por:
     ```
     `A6a`, `A8a`, `A8`, `A9` e `B1`.
     ```
  5. No gatilho do Passo 8, trocar `` (`A6`..`A9`, inclusive `A8a`) `` por:
     ```
     (`A6`..`A9`, inclusive `A6a` e `A8a`)
     ```
  6. No parágrafo do consumo do laudo, trocar `` `A6`, `A7`..`A9` (inclusive `A8a`) e `B1` `` por:
     ```
     `A6`, `A6a`, `A7`..`A9` (inclusive `A8a`) e `B1`
     ```
  7. No relatório de encerramento, trocar `` (`A1`..`A9`, inclusive `A8a`, ou `B0`..`B4`, pelo
     identificador) `` por:
     ```
     (`A1`..`A9`, inclusive `A6a` e `A8a`, ou `B0`..`B4`, pelo identificador)
     ```
- **Testes:** **nenhum `pytest`** — declaração, não omissão, pela mesma razão da `LM-T2` e da
  `LM-T2c` (`AE-14`): tabela de roteamento é prosa lida pelo `scrum-master`. E **nenhuma linha de
  código**: a lacuna 1 se fecha **restringindo a regra ao domínio que o instrumento já aceita**, não
  alargando o instrumento — `--veredito` continua com dois valores, porque `reprovado` não é
  fechamento de RDO, é `A7`.
- **Verificação:** (`DM-24`: bloco cercado, `-SimpleMatch`, os **dois** valores rodados; as
  baselines abaixo foram medidas no `ESC-8` com estes mesmos comandos, extraídos deste card)
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '| `A6a` |' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'A6a' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 5** (a célula mais as quatro enumerações). **Medido antes: 0**. É esta linha que
     discrimina a entrega completa da que só acrescenta a linha da tabela.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '`recomendacao=escalar` (com `bloqueante=nenhuma`)' -SimpleMatch | Measure-Object).Count"
     ```
     → **0** (a condição velha da `A8a` desapareceu). **Medido antes: 1**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'nunca por `A8a`, `A8` ou `A9`' -SimpleMatch | Measure-Object).Count"
     ```
     → **1** (a frase de partição). **Medido antes: 0**.
  5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total
     que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa não acrescenta
     teste e **não pode reduzir** esse total. Referência histórica, não aceite: `165 passed` em
     2026-09-19.
- **Restrições desta tarefa:** `A1`..`A3b`, `A6`, `A7`, `A8` e `A9` ficam **literais** — só a
  `A8a` tem a **condição** reescrita, e nada da ação dela muda. O bloco B fica **intocado**.
  Nenhuma renumeração: `A6a` é sufixo, pelo mesmo motivo da `A8a` (`DM-25` (iii)). Nenhum
  instrumento é tocado — em particular, **não** se alarga `--veredito` do `rdo.py close`.
- **Não fazer:** não tocar `.claude/tools/` (a lacuna se fecha na prosa, `DM-26` (iii)); não tocar
  `GOVERNANCA.md` (é a `LM-T4`); não tocar `.claude/agents/` (`DM-17`); não escrever teste `pytest`
  para regra de prosa; não commitar.
- **Contingências:**
  1. se qualquer um dos sete literais a substituir não existir no arquivo exatamente como
     transcrito → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.
- **Pronto quando:** `A6a` está entre `A6` e `A7` com o texto literal acima; a condição de `A8a`
  fala de **veredito**; a frase de partição está no parágrafo do bloco A; as quatro enumerações
  citam `A6a`; e as cinco linhas de `Verificação` saem como escritas.

### LM-T2e — A ação da `A7`: `reprovado` não fecha RDO [Sonnet · classe redacao]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `seguir`, pendência `nenhuma`, achado de processo `nenhum`. Fecha o `AE-22`: a frase de partição da `LM-T2d` passou a ser verdadeira. RDO: `docs/RDO/P-0740-LM-T2e-a-acao-da-a7-reprovado-nao-fecha-rdo.md`. Card novo do `ESC-9` (2026-09-19), residência única do `AE-22` e do
  `DM-32`.
- **Esforço:** low
- **Objetivo:** um só — a última regra do bloco A que manda fazer o que o instrumento de
  fechamento recusa passa a materializar o desfecho pela via que a `DP-F` prevê, e a frase de
  partição que a `LM-T2d` escreveu no mesmo arquivo passa a ser verdadeira.
- **Depende de:** `LM-T2d` (fechada — é a frase de partição dela que esta tarefa torna verdadeira)
  e `DM-32`. **Precede a `LM-T4`**, pela mesma razão da `LM-T2c` e da `LM-T2d`: mesmo arquivo em
  `Arquivos-alvo` (exclusão mútua viva) e doutrina não se publica sobre tabela de roteamento que
  se contradiz.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
- **Produto do módulo:** uma célula — a **ação** da linha `A7` da tabela do bloco A. A **condição**
  da `A7` não muda; nenhuma linha nova entra na tabela; nenhuma enumeração do arquivo muda, porque
  `A7` já é citada em todas.
- **O defeito, medido no `ESC-9` (2026-09-19):** a `A7` manda *"fecha o RDO como `reprovado`"* e o
  instrumento recusa esse desfecho em três pontos, os três re-medidos agora:
  `python .claude/tools/rdo.py close ... --veredito reprovado` sai **exit 2**
  (`argument --veredito: invalid choice: 'reprovado' (choose from 'aprovado', 'ressalva')`);
  `calcular_desdobramento('reprovado')` levanta `RdoValidationError: veredito inesperado:
  'reprovado'`; e o gatilho do Passo 9 é a entrada em `done`, que `blocked`/`cancelled` não
  disparam (`DP-F` item 3, fechamento c).
- **Passos, com o texto literal** (transcrever):
  1. Na tabela do bloco A, substituir a linha inteira
     ```
     | `A7` | `veredito=reprovado` e retentativas gastas = 1 | fecha o RDO como `reprovado`: **PARA** |
     ```
     por
     ```
     | `A7` | `veredito=reprovado` e retentativas gastas = 1 | `reprovado` **não é desfecho de RDO** e esta regra **não** fecha RDO: o RDO só nasce na transição `review` → `done` (`DP-F` item 3, fechamento c), e `rdo.py close --veredito` aceita só `aprovado` e `ressalva` (medido: exit 2, `invalid choice`; `calcular_desdobramento('reprovado')` levanta `RdoValidationError`). Materializa a tarefa como `blocked` razão `premissa` — reprovada duas vezes, o que caiu foi a premissa de que o card é executável como está —, com o `bloqueante` e a pendência do laudo transcritos na razão, e registra o achado como `AE-<n>` em `## Achados da execução` do plano: **PARA**. A escalada é a do `A3b`: a reprovação depois da última retentativa é nomeada no relatório de encerramento e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). Precedência: `A6` e `A6a` vencem esta regra; ela vence `A8a`, `A8` e `A9` |
     ```
     — nada mais do arquivo muda.
- **Testes:** **nenhum `pytest`** — declaração, não omissão, pela mesma razão da `LM-T2c` e da
  `LM-T2d` (`AE-14`): tabela de roteamento é prosa lida pelo `scrum-master`. E **nenhuma linha de
  código**: o `--veredito` do `rdo.py close` continua com dois valores (`DM-32` (i)).
- **Verificação:** (`DM-24`: bloco cercado, `-SimpleMatch`, os **dois** valores rodados; as
  baselines abaixo foram medidas no `ESC-9` com estes mesmos comandos, extraídos deste card, e
  **nos dois mundos** — a árvore de hoje e uma cópia com a substituição do Passo 1 já aplicada. Os
  padrões evitam acento e crase **por recorte de subcadeia do texto real**, nunca reescrevendo
  palavra do arquivo: reescrever `última` como `ultima` produz padrão que casa **0 antes e 0
  depois** e não mede nada — é o `AE-23`, achado no ato do despacho desta própria tarefa)
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'e retentativas gastas = 1 | fecha o RDO como' -SimpleMatch | Measure-Object).Count"
     ```
     → **0** (a ação velha da `A7` desapareceu). **Medido antes: 1**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'desfecho de RDO' -SimpleMatch | Measure-Object).Count"
     ```
     → **1** (a ação nova entrou). **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'materializa a tarefa como' -SimpleMatch | Measure-Object).Count"
     ```
     → **2** (`A6a` e `A7`). **Medido antes: 1**. É esta linha que discrimina a troca completa da
     que só apaga a ação velha.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'retentativa (' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**, **inalterado** (`DM-32` (ii)): o único casamento é a linha 230, da seção *O que
     obriga parada* (``… última retentativa (`A7`); plano não-pronto (`B3`) …``), que esta tarefa
     **não** toca. **Medido antes: 1; medido depois: 1**, na cópia com a substituição do Passo 1
     já aplicada — e o casamento é a **mesma linha 230** nos dois mundos, conferido. O padrão
     pega o acento pelo **que vem depois dele**, e por isso não o reescreve; a ação nova da `A7`
     também diz *"última retentativa"*, mas sem o parêntese — qualquer padrão sobre a expressão
     inteira iria a **2** e deixaria de ser invariante.
  5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total
     que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa não acrescenta
     teste e **não pode reduzir** esse total. Referência histórica, não aceite: `171 passed` em
     2026-09-19 (`ESC-9`).
- **Restrições desta tarefa:** `A1`..`A3b`, `A6`, `A6a`, `A8a`, `A8` e `A9` ficam **literais** — só
  a **ação** da `A7` muda, e a **condição** dela fica como está. O bloco B fica **intocado**. A
  seção *O que obriga parada e o que segue com registro* fica **intocada**: a `A7` continua
  encerrando a janela. Nenhum instrumento é tocado — em particular, **não** se alarga o
  `--veredito` do `rdo.py close` (`DM-32` (i)).
- **Não fazer:** não tocar `.claude/tools/` (a lacuna se fecha na prosa, `DM-26` (iii) e `DM-32`
  (i)); não tocar `GOVERNANCA.md` (é a `LM-T4`; a menção a *reprovado* em `GOVERNANCA.md` §3,
  linha da *Orquestração*, é sobre a **retentativa** do `A6`, não sobre fechamento de RDO —
  medido, nada a corrigir lá); não tocar `.claude/agents/` (`DM-17`); não refazer a `LM-T2d`; não
  escrever teste `pytest` para regra de prosa; não commitar.
- **Contingências:**
  1. se a linha literal da `A7` a substituir não existir no arquivo exatamente como transcrita →
     parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.
- **Pronto quando:** a linha `A7` da tabela do bloco A traz o texto literal acima; nenhuma outra
  linha do arquivo mudou; e as cinco linhas de `Verificação` saem como escritas.

### LM-T2f — O teste órfão da dedupe por `message.id` [Sonnet · classe mecanica]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação
  `seguir`, pendência `nenhuma`. Fecha o `AE-27` item 1: `deduplica_por_message_id` vai a **0** no
  arquivo de teste, o módulo sai `9 passed` e a suíte `187 passed` (antes: `10`/`188`). Um achado
  de processo, **com rota já dada e sem rebaixar dimensão**: a `Verificação` do card fixava
  `174 passed` como constante absoluta (defeito (xiii) da rubrica) e só não reprovou porque o
  `scrum-master` re-derivou a baseline no despacho — já indexado em `RUBRICA_DE_REVISAO.md` §8.2 e
  coberto pelo gate do `card_check.py`. RDO:
  `docs/RDO/P-0740-LM-T2f-o-teste-orfao-da-dedupe-por-message-id.md`; laudo consumido e apagado.
- **Esforço:** low
- **Objetivo:** um só — a suíte deixa de afirmar, por nome e por docstring, um mecanismo que a
  `LM-T2b` removeu.
- **Depende de:** `LM-T2b` (fechada — é a entrega dela que tornou o teste órfão). Nenhuma tarefa
  depende desta.
- **Arquivos-alvo:**
  - `tests/test_telemetria_hook.py`
- **O defeito, medido no `ESC-12`:** `test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas`
  (`:107`) e `test_tr_calcular_consumo_mesma_mensagem_duas_entradas_nao_dobra` (`:181`) têm corpo
  **byte a byte idêntico** — mesmo `usage` (10/8779/0/74), mesmas duas entradas com
  `message_id="msg_calibracao"`, mesmas asserções (`tokens_k == 8863/1000`, `tool_uses == 0`). O
  primeiro nomeia e descreve a **dedupe por `message.id`**, mecanismo que a `LM-T2b` removeu; o
  segundo descreve o **mesmo caso** sob a fórmula nova, com a prosa correta. O caso **não** se
  perde: ele fica no segundo.
- **Passos:**
  1. Apagar a função `test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas`
     **inteira** — do `def` até a última asserção —, junto com as linhas em branco que a separavam
     da função seguinte, deixando as duas linhas em branco de separação entre as funções que
     ficarem vizinhas. Nada mais do arquivo muda: o teste que **fica** é o `:181`, e ele **não** se
     renomeia.
- **Testes:** nenhum teste novo — esta tarefa **remove** duplicata. É a única tarefa do plano
  autorizada a **reduzir** o total da suíte, e a redução é de exatamente **1** (`DM-23` continua
  valendo para todas as outras).
- **Verificação:** (`DM-12`/`DM-24`: toda baseline abaixo foi rodada pelo consultor no `ESC-12`,
  com `-CaseSensitive` onde a caixa discrimina, `AE-25`)
  1. `python -m pytest tests/test_telemetria_hook.py -q` → **`9 passed`**. **Medido antes:
     `10 passed`**.
  2. `python -m pytest tests/ -q` → **`174 passed`**. **Medido antes: `175 passed`**, e o valor
     depois foi medido **de fato**, com
     `python -m pytest tests/ -q --deselect "tests/test_telemetria_hook.py::test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas"`
     → `174 passed, 1 deselected`, e não por subtração.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path tests/test_telemetria_hook.py -Pattern 'deduplica_por_message_id' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**. O nome não aparece em nenhum outro arquivo do kit (medido: 1
     ocorrência no repositório, esta).
- **Restrições desta tarefa:** o teste `:181` fica **literal** — nome, docstring e corpo. Nenhum
  outro teste é tocado. Nenhum arquivo de `.claude/` é tocado.
- **Não fazer:** não "fundir" os dois testes; não renomear o que fica; não tocar
  `.claude/tools/telemetria_hook.py`; não commitar.
- **Contingências:**
  1. se o corpo dos dois testes não for idêntico no ato do despacho (arquivo mexido desde a
     medida) → parar e sinalizar `blocked` razão `premissa`, citando a diferença encontrada.
- **Pronto quando:** o módulo sai `9 passed`, a suíte sai `174 passed`, e `deduplica_por_message_id`
  não aparece mais no arquivo.

### LM-T3b — O campo termina no bullet: `_parsear_campos` e a autoridade mecânica do `escopo` [Sonnet · classe implementacao]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `escalar`. Fecha o `AE-27` item 2: a extração da `LM-T2b` cai de **9** para **2** e as outras cinco ficam inalteradas (`1, 2, 8, 1, 2`). Pendência roteada como `AE-39`. RDO: `docs/RDO/P-0740-LM-T3b-o-campo-termina-no-bullet-parsear-campos-e-a-autoridade-mecanica-do-escopo.md` — card novo do `ESC-12` (2026-09-19), residência única do `AE-27` item 2.
- **Esforço:** low
- **Objetivo:** um só — o conjunto de `Arquivos-alvo` que o dossiê declara passa a ser o que o card
  lista, para que a dimensão `escopo` continue **mecânica** em vez de depender de julgamento sobre
  ruído.
- **Depende de:** `LM-T3a` (fechada — é o contrato do mesmo instrumento) e `DM-35` (iii).
  **Precede a `LM-T6`**: o piloto mede o loop de ponta a ponta, e a autoridade mecânica do
  `escopo` é um dos contratos que ele exercita.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py`
- **A causa, medida no `ESC-12` (é de gramática, não de heurística):** `_parsear_campos`
  (`.claude/tools/rdo.py:186`) encerra o campo corrente **só** quando a linha casa `_CAMPO_RE`
  (`- **Rótulo:** …`). Um bullet de prosa cujo rótulo não termina em `:**` — como
  `- **A calibração medida no \`ESC-3\` (2026-09-18) — residência única desta tabela.**` — **não**
  encerra nada, e todas as linhas indentadas seguintes (a tabela de calibração inteira) continuam
  sendo anexadas a `arquivos-alvo`. Depois, `_eh_caminho` aceita `251.1` e `message.id` como
  caminho, porque têm "extensão". Medido na `LM-T2b`: **9** alvos extraídos contra **2**
  declarados — `message.id`, `251.1`, `505.2`, `2330.8`, `946.9`, `.jsonl` e `telemetria_hook.py`
  entraram, gerando sete seções de diff vazias.
- **Produto do módulo:** (a) em `_parsear_campos`, **um bullet de topo encerra o campo corrente**,
  case ele `_CAMPO_RE` ou não — hoje só campo canônico encerra; linha indentada continua
  alimentando o campo, como hoje; (b) o docstring da função enuncia a regra e a razão medida
  (`AE-27` item 2), citando o caso da `LM-T2b`.
- **Testes** (dois, com a regra concorrente de cada):
  - `TF-campo-termina-em-bullet-de-prosa` — bloco sintético com `- **Arquivos-alvo:**`, dois
    sub-bullets de caminho, e **depois** um bullet de prosa (rótulo terminado em `.**`) seguido de
    linhas indentadas com crases contendo `\`x.y\`` e uma tabela: `extrair_arquivos_alvo` devolve
    **só** os dois caminhos. *Concorrente:* o código de hoje devolve os dois **mais** o que veio da
    prosa.
  - `TR-campo-multilinha-continua-valendo` — campo canônico seguido de sub-bullets indentados em
    várias linhas continua sendo lido **inteiro**. *Concorrente:* encerrar o campo em qualquer
    linha nova quebraria a lista de alvos de todos os cards, que é multilinha.
- **Verificação:** (`DM-12`: as baselines abaixo foram medidas pelo consultor no `ESC-12`,
  **emulando o reparo** sobre os cards reais deste plano, não sobre fixture)
  1. Extração sobre o card da `LM-T2b`, pelo instrumento:
     ```
     python -c "import sys;sys.path.insert(0,'.claude/tools');import rdo,review_evidence as r;from pathlib import Path;L=Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8').splitlines();i=next(k for k,x in enumerate(L) if x.startswith('### LM-T2b '));j=next(k for k in range(i+1,len(L)) if L[k].startswith('### '));print(len(r.extrair_arquivos_alvo(rdo._parsear_campos(L[i+1:j])[0])))"
     ```
     → **2**. **Medido antes: 9**; e **medido depois: 2**, na emulação do reparo.
  2. A mesma extração sobre `LM-T2e`, `LM-T3a`, `LM-T4`, `LM-T5` e `LM-T6` → **1, 2, 5, 1, 2**,
     **inalteradas**. Medidas nos dois mundos no `ESC-12`, iguais nos dois: é a linha que impede o
     reparo de cortar alvo legítimo.
  3. `python -m pytest tests/ -q` → verde, com **dois testes a mais** que o total re-medido no
     despacho (`DM-23`). Referência histórica, não aceite: `175 passed` em 2026-09-19.
- **Restrições desta tarefa:** `_eh_caminho` e `_classificar_campo_alvos`
  (`.claude/tools/review_evidence.py`) ficam **intocados** — a causa medida é o **limite do campo**,
  e alargar a gramática de caminho seria tratar o sintoma; `review_evidence.py` **não** está nos
  alvos. Nenhum outro campo do dossiê muda de semântica.
- **Não fazer:** não tocar `.claude/tools/review_evidence.py` nem `tests/test_review_evidence.py`;
  não mexer nos baldes da `DB-25` (o `registro_orquestracao` está **certo**, medido no `ESC-12`:
  `docs/telemetria.tsv` já cai nele); não tocar card nenhum do plano para "contornar" o parser; não
  commitar.
- **Contingências:**
  1. se `_parsear_campos` não estiver na forma citada (o `for` com `_CAMPO_RE.match`, o ramo de
     linha indentada e `em_extra`) → parar e sinalizar `blocked` razão `premissa`, citando a forma
     encontrada;
  2. se a `Verificação` 2 mudar para qualquer card → **parar e sinalizar `blocked` razão
     `premissa`**: o reparo estaria cortando alvo legítimo, e isso é decisão de consultor, não de
     execução.
- **Pronto quando:** a extração da `LM-T2b` devolve 2, as cinco extrações da `Verificação` 2 seguem
  em 1, 2, 5, 1, 2, os dois testes existem e a suíte fica verde sem reduzir o total.

### LM-T4b — O bullet de `Status` que o instrumento lê e escreve [Sonnet · classe implementacao]

- **Status:** `done` (2026-09-19) — **ressalva 91%**, bloqueante `nenhuma`, recomendação `escalar`; pendência e um achado roteados pelo `B1` como `AE-35`. Fecha a metade do `AE-26` que é deste plano: os **25** bullets de `Status` passam a ser lidos (`25 25`). RDO: `docs/RDO/P-0740-LM-T4b-o-bullet-de-status-que-o-instrumento-le-e-escreve.md`. O `blocked` anterior foi `A3b` **antes de qualquer edição** (`AE-28`) e **não consumiu retentativa** — o `blocked` anterior foi `A3b` com o executor parando **antes de editar qualquer arquivo-alvo** (`AE-28`), e **não consumiu retentativa**. Card novo do `ESC-12` (2026-09-19), residência única do `AE-26`.
- **Esforço:** low
- **Objetivo:** um só — o loop volta a materializar estado **pelo instrumento**, como o `DM-34`
  determinou, em vez de à mão.
- **Depende de:** `DM-35` (i). **Precede a `LM-T4`**, pela mesma razão da `LM-T4a` (`DM-13` (ii),
  `AE-5`/`AE-6`): a doutrina não publica gramática que o parser ainda não lê. **Sem exclusão mútua
  com a `LM-T4`** — arquivos diferentes.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `tests/fixtures/backlog/` (a fixture nova do aceite de escrita, `ESC-13`)
- **O defeito, medido no `ESC-12`:** `python .claude/tools/backlog.py status LM-T2b review` devolve
  `linha de status ausente`. `STATUS_BULLET_RE` (`:70`) exige
  ``- **Status:** `<estado>` · AAAA-MM-DD``; o corpus usa a forma em prosa com travessão. Contagem:
  **0 de 21** bullets de `Status` do `P-0740` casam (eram 18 antes de este mesmo escalonamento
  acrescentar três cards — o total é **re-medido no despacho**, nunca literal histórico,
  `AE-21`), e **15 de 34** no repositório inteiro. O
  `DM-34` mandou materializar estado pelo instrumento e o instrumento não alcança card nenhum deste
  plano.
- **Produto do módulo:** (a) a **leitura** passa a aceitar a forma em prosa — o estado entre crases
  é obrigatório; `· AAAA-MM-DD` e a razão viram **opcionais**; tudo que vier depois de ` — ` é
  **cauda livre**, lida e preservada, nunca interpretada; (b) a **escrita**
  (`transacionar_status`) reescreve **só o prefixo de máquina** (estado, data, razão) e **preserva
  a cauda** a partir de ` — `, para não apagar a prosa que o consultor e o loop escrevem ali; (c)
  o docstring enuncia as duas regras com a contagem medida.
- **Casos que o parser novo tem de aceitar** (literais reais, copiados do plano — são o aceite):
  ```
  - **Status:** `ready`
  - **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`
  - **Status:** `blocked` razão `premissa` (2026-09-19, `A3b`) — o executor parou antes de entregar
  - **Status:** `ready` · 2026-09-19
  - **Status:** `ready` · 2026-09-19 · destravada pelo dono
  ```
  **E recusar** (continua sendo `linha de status ausente`): linha sem estado entre crases
  (`- **Status:** pendente`) e estado fora de minúsculas (`- **Status:** `Ready``).
- **Testes** (três): `TF-status-em-prosa-e-lido` (os cinco literais acima devolvem o estado certo);
  `TR-status-canonico-continua-lido` (a forma estrita com `· data · razão` não regride);
  `TF-escrita-preserva-a-cauda` (transição de estado sobre um bullet com ` — prosa` mantém a prosa
  e troca só o prefixo). *Concorrentes:* hoje os cinco literais devolvem `linha de status ausente`,
  e a escrita substituiria o bullet inteiro.
- **Verificação:** (`DM-12`, medido no `ESC-12`)
  1. ```
     python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog;from pathlib import Path;L=[l for l in Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8').splitlines() if l.startswith('- **Status:**')];print(len(L),sum(1 for l in L if backlog.STATUS_BULLET_RE.match(l)))"
     ```
     → os **dois números iguais** (`<N> <N>`): todo bullet de `Status` do plano é lido. **Medido
     no `ESC-12`, com o comando publicado: `21 0`** — o segundo número é o que a entrega muda; o
     primeiro é o total do plano no despacho, **re-medido** por quem despacha e não fixado aqui
     (`DM-23`, `AE-21`: o total mudou de 18 para 21 durante o próprio `ESC-12`, quando os três
     cards novos entraram).
  2. `python -m pytest tests/test_backlog.py -q` → verde, com **três testes a mais** que o total
     re-medido no despacho. O aceite do caminho de **escrita** é o teste
     `TF-escrita-preserva-a-cauda`, que copia a fixture `tests/fixtures/backlog/verde` para o
     `tmp_path`, troca o bullet de `ALF-T1` pela forma em prosa
     ``- **Status:** `ready` (2026-01-01) — cauda em prosa que precisa sobreviver``, chama
     `transacionar_status(... 'ALF-T1', 'in-progress')` e exige **exit 0** com a cauda
     **preservada** na linha reescrita. **Medido no `ESC-13`, no mundo de hoje, com esse mesmo
     arranjo:** exit **3**, `linha de status ausente para ALF-T1` — a linha discrimina.
     **Por que sobre fixture e não sobre o plano real (`AE-28`, `AE-29`):** (a) comando de
     aceite não altera o estado do plano que o loop está conduzindo; (b) a transição escolhida
     é `ready → in-progress`, que **está** na tabela de `_TRANSICOES` — a que o card publicava
     antes (`LM-T2f` para `ready`, sendo ela já `ready`) é um **self-loop fora da tabela**, e
     exit 1 garantido; (c) medido no `ESC-13`, `backlog.py status` **não alcança tarefa nenhuma
     deste plano** nem com o parser corrigido, por causa do `AE-29` — que **não** é matéria
     deste card.
  3. `python -m pytest tests/ -q` → verde, com **três testes a mais** que o total re-medido no
     despacho (`DM-23`).
- **Restrições desta tarefa:** a tabela `_TRANSICOES` fica **intocada** — `('ready','ready')`
  continuar fora dela é decisão de `DP-F`, não de um card que ensina o instrumento a **ler e
  escrever um bullet**; inventar self-loop para satisfazer aceite é o inverso do `DM-26` (iii) e
  do `DM-32`. O vocabulário de estados **não** muda (`ready`, `in-progress`,
  `review`, `done`, `blocked`, `cancelled` — `DP-F`); `blocked` continua exigindo `--razao`; a
  forma **canônica** continua sendo a que a escrita produz. Nenhum card do plano é reescrito para
  caber no parser — é o parser que aprende (`DM-35` (i)).
- **Não fazer:** não tocar `.claude/tools/rdo.py` (é a `LM-T3b`); não tocar `GOVERNANCA.md` (a
  publicação é a `LM-T4`, item (d)); não tocar os cards do plano; não commitar.
- **Contingências:**
  1. se `STATUS_BULLET_RE` ou `transacionar_status` não estiverem na forma citada → parar e
     sinalizar `blocked` razão `premissa`, citando a encontrada;
  2. se a `Verificação` 1 não fechar com os **dois números iguais**, **parar** e sinalizar
     `blocked` razão `premissa`, citando o par obtido: aceitar um bullet ilegível é deixar o
     instrumento sem alcançar o plano de novo.
- **Pronto quando (reparado pelo `ESC-15`, `DM-38` (iii)):** o campo vizinho que a emenda do
  `ESC-13` deixou para trás. **Todos** os bullets de `Status` do plano são lidos (os dois
  números da `Verificação` 1 iguais); `backlog.py status` transita a tarefa da **fixture**
  (`tests/fixtures/backlog/verde`, cópia em `tmp_path`, `ready → in-progress`) preservando a
  cauda em prosa — **não** um card real, que o `AE-29` torna inalcançável e que aceite nenhum
  pode mutar
  preservando a cauda, os três testes existem e a suíte fica verde.

### LM-T3 — A evidência que basta ao reviewer [Sonnet · classe implementacao]

- **Status:** `done` — fechada em 2026-09-18, **ressalva 91%**, bloqueante `nenhuma`, recomendação `escalar` (RDO `docs/RDO/P-0740-LM-T3-a-evidencia-que-basta-ao-reviewer.md`; laudo consumido e apagado, `DP-H`). O `AE-13` fecha aqui — a atribuição por arquivo já valeu nesta própria revisão. Pendência roteada como `AE-15`.
- **Esforço:** medium
- **Objetivo:** o dossiê de evidência, de ponta a ponta. Cobre o defeito 6 e absorve a `AUT-T5c`.
- **Arquivos-alvo:** `.claude/tools/review_evidence.py` · `tests/test_review_evidence.py` ·
  `docs/RUBRICA_DE_REVISAO.md` (seção da camada mecânica)
- **Produto do módulo:** o dossiê passa a trazer, por arquivo vermelho, a **atribuição**: tocado por esta
  tarefa (dentro dos `Arquivos-alvo`) ou alheio (fora deles, com o estado git que o comprova). O
  reviewer deixa de precisar de injeção manual de contexto para não reprovar entrega correta.
- **Coerência do módulo (aceite de `DM-3`):** a atribuição usa a **mesma** função que já existe
  no módulo — `confrontar_escopo` (`:282-333`), com os cinco baldes da `DB-25`/`DB-32`. Uma
  pergunta, uma implementação, três consumidores: o dossiê (esta tarefa), o verbo `--atribuir`
  (`LM-T2a`) e a prosa `B0`/`B1` do loop (`LM-T2`). **Nenhuma** classificação nova se escreve
  aqui (`DM-19`).
- **Testes:** TF arquivo vermelho dentro dos alvos sai marcado como da entrega; TF arquivo vermelho
  fora dos alvos sai marcado como alheio com o estado git; TR a seção nova chama
  `confrontar_escopo` e **não** reimplementa a classificação (nenhum segundo laço de cobertura no
  módulo).
- **Verificação:** `python -m pytest tests/test_review_evidence.py -q` verde — baseline medida no
  `ESC-3`: `25 passed` · `python -m pytest tests/ -q` verde, piso ≥ **153** (medido no `ESC-3`:
  `153 passed`; o piso de 145 venceu com a `LM-T1a`). O piso é mínimo e a `LM-T2a`, se rodar
  antes, acrescenta três testes.
- **Pronto quando:** o dossiê gerado por `.claude/tools/review_evidence.py` traz, por arquivo
  vermelho, a atribuição "da entrega" ou "alheio" com o estado git que a comprova; os três testes
  nomeados em `Testes` existem em `tests/test_review_evidence.py`; `docs/RUBRICA_DE_REVISAO.md`
  descreve a atribuição na seção da camada mecânica; e as duas linhas de `Verificação` saem verdes
  com o piso ≥ **153**.
- **Depende de:** nada — **a dependência da `LM-T2` caiu no `ESC-3`** (`DM-19` (iv)): a função de
  atribuição já existe neste mesmo módulo e não nasce em tarefa nenhuma. Fica a **exclusão mútua**
  com a `LM-T2a` sobre `.claude/tools/review_evidence.py`: as duas editam o arquivo em regiões
  diferentes e não podem estar abertas ao mesmo tempo; qualquer ordem serve. **Esta tarefa fecha o
  `AE-13`**, que já custou duas injeções manuais de contexto na revisão.

### LM-T3a — O contrato do instrumento de evidência: a falha e o recorte [Sonnet · classe implementacao]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `seguir`, pendência `nenhuma`; achado de processo do laudo roteado como `AE-21`. RDO: `docs/RDO/P-0740-LM-T3a-o-contrato-do-instrumento-de-evidencia-a-falha-e-o-recorte.md`. Card do `ESC-4` (`AE-15`), **ampliado pelo `ESC-5`** com o `AE-17`. As duas
  matérias são o mesmo assunto sob `DM-22`: o que o instrumento de evidência promete na **borda** —
  entrada inválida e recorte declarado. Nem a `LM-T3` nem a `LM-T2a` se refazem: as duas estão
  `done` e o que faltou não estava nos cards delas.
- **Esforço:** low
- **Objetivo:** um só — fechar a borda do `review_evidence.py`: (a) a evidência `git` que acompanha
  cada atribuição passa a respeitar o mesmo `--desde` que a lista de tocados já respeita; (b) os
  **dois** verbos do módulo falham pelo mesmo canal, com a mesma forma de mensagem.
- **Depende de:** `DM-22` (contrato de falha é do módulo), `AE-15`, `AE-17`. Nenhuma tarefa
  anterior. **Sem exclusão mútua viva:** a `LM-T2a` e a `LM-T3`, que disputavam este arquivo,
  fecharam — esta é a única tarefa aberta sobre `.claude/tools/review_evidence.py`.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Fatos medidos (2026-09-18 no `ESC-4`; 2026-09-19 no `ESC-5`, com o verbo já entregue):**
  - `coletar_estado_git(root)` lê **só** `git status --porcelain=v1 --untracked-files=all` e **não
    recebe** `desde`; `coletar_arquivos_tocados` recebe e usa. O renderizador imprime
    `estado git: \`<XY>\`` ou `(sem entrada em \`git status\`)` quando a chave falta.
  - Na árvore de hoje o defeito do recorte **não aparece**, e é por isso que ninguém o viu:
    `git diff 428246c --name-status` = **30** linhas contra **45** de `git status --porcelain
    -uall` (a diferença são os não rastreados, que o `diff` nunca lista) — **nada** foi commitado
    desde a ref. Vira visível no primeiro dossiê **depois do marco de validação**, que é quando o
    commit acontece por diretiva do dono. `git diff <ref> --name-status` emite `<letra>\t<caminho>`
    (medido: `M\t.claude/README.md`), com avisos de CRLF em **stderr**, que `_git` já descarta.
  - **A borda de falha diverge entre os verbos do mesmo módulo** (`AE-17`), medido no `ESC-5`:
    com `--plano NAO-EXISTE.md`, o caminho do dossiê sai
    `review_evidence: FALHOU - plano: arquivo não encontrado 'NAO-EXISTE.md'` (exit 1) e o
    `--atribuir` sai com **traceback cru**, última linha
    `FileNotFoundError: [Errno 2] No such file or directory: 'NAO-EXISTE.md'` (exit 1 também — **o
    exit code não discrimina**, quem discrimina é o stderr). Causa: a guarda
    `if not plano_path.is_file()` mora em `montar_documento` (`:615-616`) e o ramo `if
    args.atribuir:` (`:706-725`) chama `rdo.extrair_dossie` direto, pulando-a. Com `--tarefa`
    inexistente os dois verbos **já** coincidem
    (`review_evidence: FALHOU - tarefa: 'LM-T99' não encontrada em '…'`), porque o ramo já captura
    `rdo.RdoValidationError` — o buraco é só o arquivo de plano.
- **Produto do módulo:** (a) `coletar_estado_git(root, desde=None)` compõe a evidência de duas
  fontes, com precedência declarada: o código `XY` da **árvore de trabalho** vence sempre; na
  ausência dele, e só quando `desde` é dado, entra a letra de `git diff <desde> --name-status`,
  marcada como commitada; (b) a guarda do plano vira **residência única** (`_exigir_plano`) e os
  dois verbos passam por ela, falhando com a mesma forma de mensagem e o mesmo exit 1.
- **Forma literal do valor commitado** (residência única deste literal):
  ```
  <letra> (commitado desde <ref>)
  ```
  Exemplo do que o dossiê passa a trazer: ``- `docs/DOC_MAP.md` — atribuição: alheio; estado git:
  `M (commitado desde 428246c)` ``. Para renomeação (`R100\t<velho>\t<novo>`), a chave é o
  **último** campo da linha e a letra é o primeiro campo inteiro (`R100`).
- **Passos:**
  1. `coletar_estado_git` ganha o parâmetro `desde: str | None = None`, mantendo a assinatura
     compatível (chamada sem o segundo argumento continua válida).
  2. Depois de preencher o mapa com o `git status` (código de duas letras, **inalterado**), e só se
     `desde` não for `None`, percorrer `_git(["diff", desde, "--name-status"], root)` e aplicar
     `setdefault(caminho, f"{letra} (commitado desde {desde})")` — `setdefault`, e não atribuição, é
     o que materializa a precedência da árvore de trabalho.
  3. Em `montar_documento`, passar o `desde` que a função já tem em mãos:
     `coletar_estado_git(root, desde)`.
  4. Extrair a guarda do plano para **uma** função, no mesmo módulo:
     ```python
     def _exigir_plano(plano_path: Path) -> None:
         """Guarda única da borda: caminho de plano que não existe falha pelo canal do módulo
         (`ReviewEvidenceValidationError` → `review_evidence: FALHOU - …`), em **todos** os verbos
         (`DM-22`, `AE-17`)."""
         if not plano_path.is_file():
             raise ReviewEvidenceValidationError(f"plano: arquivo não encontrado '{plano_path}'")
     ```
     Substituir por `_exigir_plano(plano_path)` as duas linhas de `montar_documento` que hoje
     testam `is_file()` e levantam a exceção — **sem** mudar a mensagem, que é a forma já publicada.
  5. No ramo `if args.atribuir:`, chamar `_exigir_plano(args.plano)` **dentro** do `try` existente,
     antes de `rdo.extrair_dossie`, e alargar o `except` para
     `except (ReviewEvidenceValidationError, rdo.RdoValidationError) as exc:` — a linha de impressão
     e o `return 1` ficam como estão.
- **Testes** (seis, com a regra concorrente de cada; os testes deste módulo criam **repo git real**
  em `tmp_path` — ver `_run_git` e `test_desde_recorta_tocados_a_partir_da_referencia`, que já
  commita duas vezes):
  - `TF-estado-git-de-arquivo-commitado-desde-a-ref` — repo com commit de baseline (a `ref`), depois
    um arquivo alterado **e commitado**; com `--desde <ref>`, a linha dele no dossiê traz
    `M (commitado desde <ref>)`. *Concorrente:* hoje traz `(sem entrada em \`git status\`)` — é
    exatamente a ressalva do laudo da `LM-T3`.
  - `TR-estado-da-arvore-de-trabalho-vence` — no mesmo repo, um arquivo alterado **sem** commit
    continua saindo com o código de duas letras do `git status` (ex.: ` M`), não com a forma
    commitada. *Concorrente:* dar precedência ao `diff` apagaria o código que o dossiê já publica, e
    a `LM-T3` seria rebaixada por regressão.
  - `TR-sem-desde-nada-muda` — chamada sem `desde`, a função devolve exatamente o mapa do
    `git status` e **nenhuma** chamada de `diff` acontece. *Concorrente:* chamar `git diff` sem ref
    quebra o modo árvore-inteira, que é o default do instrumento.
  - `TF-atribuir-com-plano-inexistente-falha-pelo-canal-do-modulo` — `main(["--plano",
    "<inexistente>", "--tarefa", "<qualquer>", "--atribuir"])` devolve **1** e o stderr contém
    `review_evidence: FALHOU - plano: arquivo não encontrado`. *Concorrente:* hoje o retorno também
    é 1, mas por **traceback** de `FileNotFoundError` — o teste tem de afirmar o **stderr**, nunca
    só o código de saída (`AE-17`).
  - `TR-dossie-com-plano-inexistente-nao-muda` — o mesmo caso **sem** `--atribuir` continua saindo
    exit 1 com a mesma mensagem. *Concorrente:* mover a guarda para fora de `montar_documento` sem
    cuidado deixaria o caminho do dossiê sem ela.
  - `TR-atribuir-com-tarefa-inexistente-continua-igual` — com plano válido e `--tarefa` inexistente,
    exit 1 e `review_evidence: FALHOU - tarefa: '<ID>' não encontrada em` — comportamento **já
    correto** hoje, que o alargamento do `except` não pode quebrar. *Concorrente:* trocar o `except`
    em vez de alargá-lo perderia este caso.
- **Verificação:** (medida no `ESC-5`, 2026-09-19; nenhuma linha deduzida — `DM-12`)
  1. `python -m pytest tests/test_review_evidence.py -q` → verde, com **seis testes a mais** que o
     total re-medido no despacho (`DM-23`: piso é relação, não número). Referência histórica, não
     aceite: `32 passed` em 2026-09-19.
  2. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total
     que a árvore tiver **no despacho**, re-medido por quem despacha e registrado no dossiê; esta
     entrega soma os seis testes novos e **não reduz** esse total. Referência histórica:
     `165 passed` em 2026-09-19.
  3. Contrato de falha, nos **dois** verbos, com o mesmo argumento inválido:
     `python .claude/tools/review_evidence.py --plano NAO-EXISTE.md --tarefa LM-T3a --desde 428246c --atribuir`
     → exit 1 e stderr contendo
     `review_evidence: FALHOU - plano: arquivo não encontrado 'NAO-EXISTE.md'`. **Antes (medido no
     `ESC-5`):** exit 1 com traceback, última linha
     `FileNotFoundError: [Errno 2] No such file or directory: 'NAO-EXISTE.md'`. O mesmo comando
     **sem** `--atribuir` já sai com a mensagem certa hoje e tem de continuar saindo.
  4. Regressão no corpus real (onde o defeito do recorte **não** aparece, e é isso que a linha
     afirma):
     `python .claude/tools/review_evidence.py --plano docs/plans/P-0740-loop-de-modulos.md --tarefa LM-T3a --desde 428246c --out docs/RDO/evidencia/P-0740-LM-T3a.md`
     → exit 0, e **nenhuma** linha da seção `## Arquivos tocados` contendo
     `(sem entrada em \`git status\`)`. Baseline medida: também nenhuma — com nada commitado desde a
     ref, os dois mundos coincidem; esta linha é regressão, e quem discrimina é o primeiro teste.
- **Restrições desta tarefa:** `confrontar_escopo` e os cinco baldes ficam **intocados** — esta
  tarefa não mexe em atribuição, só na borda do módulo. `coletar_arquivos_tocados` fica intocada. O
  renderizador de `## Arquivos tocados` não muda de forma: o que muda é o **valor** que ele recebe.
  A mensagem da guarda de plano **não** muda uma letra: ela já é a forma publicada, e o que se
  corrige é **quem passa por ela**.
- **Não fazer:** não acrescentar flag nova ao CLI; não mudar a forma literal da saída de
  `--atribuir` (é entrega fechada da `LM-T2a`); não tocar `docs/RUBRICA_DE_REVISAO.md` (a `LM-T3` já
  descreveu a atribuição em `## 3`); não tocar `.claude/skills/scrum-master/SKILL.md` (é a `LM-T2`);
  não rodar `backlog.py check` como aceite (`AE-1`); não commitar.
- **Contingências:**
  1. se `coletar_estado_git` não tiver a assinatura `(root: Path) -> dict[str, str]`, ou se a guarda
     de plano em `montar_documento` não for as duas linhas `if not plano_path.is_file(): raise
     ReviewEvidenceValidationError(...)` → parar e sinalizar `blocked` razão `premissa`, citando o
     que foi encontrado;
  2. se `python -m pytest tests/ -q` ficar vermelho **fora** de `tests/test_review_evidence.py` →
     seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos
     alvos`.
- **Pronto quando:** `coletar_estado_git` aceita `desde` e compõe as duas fontes com a árvore de
  trabalho vencendo; o dossiê traz `<letra> (commitado desde <ref>)` para arquivo commitado desde a
  ref; `_exigir_plano` é a **única** residência da guarda e os dois verbos falham pelo mesmo canal;
  os seis testes existem; e as quatro linhas de `Verificação` saem como escritas.

### LM-T4a — A gramática de três campos nos dois parsers de cabeçalho [Sonnet · classe implementacao]

- **Status:** `done` — fechada em 2026-09-19, **aprovada 100%**, bloqueante `nenhuma`, recomendação `seguir` (RDO `docs/RDO/P-0740-LM-T4a-a-gramatica-de-tres-campos-nos-dois-parsers-de-cabecalho.md`; laudo consumido e apagado, `DP-H`). Suíte 156 → 161.
- **Esforço:** low
- **Objetivo:** um só — o cabeçalho de tarefa como **gramática lida por máquina**. Ensina os dois
  parsers do kit a aceitar o campo `esforço` de `DM-5` **antes** de qualquer card voltar a escrevê-lo
  (`DM-13` (ii)). Não publica doutrina (é a `LM-T4`), não mexe no conteúdo do dossiê (é a `LM-T3`) e
  não reescreve cabeçalho de card nenhum (é a `LM-T5`, no `P-0739`).
- **Depende de:** `DM-5` (a gramática), `DM-13` (a ordem), os fatos `F-5`, `F-6` e `F-7` da §3, e a
  `LM-T1` fechada — ela é a última tarefa a tocar `.claude/tools/rdo.py` antes desta, e as duas não
  podem estar abertas ao mesmo tempo sobre o mesmo arquivo.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `.claude/tools/backlog.py`
  - `tests/test_rdo.py`
  - `tests/test_backlog.py`
- **Gramática a implementar** (residência única do literal nesta tarefa; nenhum outro card a
  reenuncia): `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>[ ·
  teto <n>]]`, com `<modelo>` ∈ `Opus|Sonnet|Haiku`, `<esforço>` ∈ `low|medium|high|xhigh|max`,
  `<classe>` ∈ `mecanica|implementacao|comportamental|investigacao|redacao`. O campo `esforço` é
  **opcional** e fica **entre** modelo e classe; ausente, o cabeçalho continua válido exatamente
  como é hoje. Forma fora dessa gramática **não** bloqueia: cai no tratamento que cada instrumento
  já tem para cabeçalho inválido (ramo legado no `rdo.py`, `header_valido=False` no `backlog.py`).
- **Passos:**
  1. Em `.claude/tools/rdo.py:85-89`, substituir o bloco inteiro do `_HEADER_BRACKET_RE` pelo
     **texto novo, literal**:
     ```python
     _HEADER_BRACKET_RE = re.compile(
         r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) "
         r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)?"
         r"(?: · esforço (?:low|medium|high|xhigh|max))?"
         r" · classe (?P<classe>.+?)"
         r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"
     )
     ```
  2. Em `.claude/tools/backlog.py:51`, substituir a linha
     `_BRACKET = rf"\[({_MODELOS})(?: \+ dono)? · classe ({_CLASSES})(?: · teto \d+)?\]"`
     pelo **texto novo, literal**:
     ```python
     _ESFORCOS = "low|medium|high|xhigh|max"
     _BRACKET = (
         rf"\[({_MODELOS})(?: \+ dono)?(?: · esforço (?:{_ESFORCOS}))?"
         rf" · classe ({_CLASSES})(?: · teto \d+)?\]"
     )
     ```
  3. Em `.claude/tools/backlog.py:12`, trocar a linha
     ``- tarefa de plano: `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]`,``
     por
     ``- tarefa de plano: `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>[ · teto <n>]]`,``
  4. Em `.claude/tools/backlog.py:16`, trocar a linha
     ``- subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]`, dentro da``
     por
     ``- subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo>[ · esforço <esforço>] · classe <classe>]`, dentro da``
  5. Escrever os cinco testes da seção **Testes**: dois em `tests/test_rdo.py` e três em
     `tests/test_backlog.py`. Todos afirmam sobre a constante de regex do próprio módulo, com a
     linha de cabeçalho literal escrita dentro do teste — sem fixture em disco e sem invocar CLI.
- **Testes** (cada afirmação vem com o valor que a **regra concorrente** daria sobre a mesma linha
  — é o que dá poder discriminante a cada uma):
  - `TF-rdo-3campos` — `_HEADER_BRACKET_RE.match("### XX-T1 — Título [Sonnet · esforço medium ·
    classe implementacao]")` devolve match com `group("modelo") == "Sonnet"` e
    `group("classe") == "implementacao"`. *Concorrente:* com a gramática de hoje (`F-5`) o match é
    `None`, e é esse `None` que leva `extrair_dossie` ao ramo legado e produz o exit 1 do `AE-5`.
  - `TR-rdo-2campos` — `_HEADER_BRACKET_RE.match("### XX-T2 — Título [Opus + dono · classe
    investigacao]")` continua devolvendo match, com `group("modelo") == "Opus"` e
    `group("classe") == "investigacao"`. *Concorrente:* com o campo `esforço` implementado como
    **obrigatório**, esta linha passa a dar `None` — é o que o teste tranca.
  - `TF-bkl-3campos` — `TAREFA_HEADER_RE.match("### XX-T1 — Título [Sonnet · esforço medium ·
    classe implementacao]")` devolve match com `group(1) == "XX-T1"`, `group(2) == "Título"`,
    `group(3) == "Sonnet"` e `group(4) == "implementacao"`. *Concorrente:* hoje o match é `None`, e
    é isso que faz o `Item` nascer `header_valido=False`, sem modelo e sem classe (`F-6`).
  - `TR-bkl-grupos-posicionais` — `TAREFA_HEADER_RE.match("### XX-T2 — Título [Opus + dono · classe
    investigacao · teto 3]")` devolve match com `group(3) == "Opus"` e
    `group(4) == "investigacao"`. *Concorrente:* com um grupo **capturante** no `_BRACKET`,
    `group(3)`/`group(4)` passam a devolver valores deslocados e o teste falha — é exatamente a
    leitura que `backlog.py:229` e `:232` fazem.
  - `TF-bkl-esforco-fora-do-vocabulario` — `TAREFA_HEADER_RE.match("### XX-T3 — Título [Sonnet ·
    esforço enorme · classe implementacao]")` devolve `None`. *Concorrente:* com o campo escrito
    como `.+?` em vez do vocabulário fechado, casaria — a gramática é fechada.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py tests/test_backlog.py -q` → verde. As duas suítes são
     alvo desta tarefa e os cinco testes novos são dela.
  2. `python -m pytest tests/ -q` → verde, piso ≥ **153** + os cinco testes novos (piso
     re-medido no `ESC-3`: `153 passed`; o de 145 venceu com a `LM-T1a`). Vermelho **fora** dos
     dois arquivos de teste alvo cai na contingência 2.
  3. Efeito no arquivo-alvo, com baseline **medida** (`F-7`: zero ocorrências de `esforço` em toda
     a árvore `.claude/`, 2026-09-18):
     `Select-String -Path .claude/tools/rdo.py,.claude/tools/backlog.py -Pattern 'esforço' -SimpleMatch`
     → ao menos **1** linha de `.claude/tools/rdo.py` e ao menos **3** de `.claude/tools/backlog.py`
     (as duas do docstring e a do `_BRACKET`). Antes da entrega: nenhuma linha de nenhum dos dois.
- **Restrições desta tarefa:** o grupo novo é **não capturante** nos dois arquivos — em
  `backlog.py` porque `:229` e `:232` leem `mm.group(3)`/`mm.group(4)` por posição (`F-6`), e em
  `rdo.py` por simetria, já que ninguém consome o valor. O campo `esforço` é **opcional**: o corpus
  de planos vivos (`P-0739` e os históricos) está inteiro na forma de dois campos e não pode deixar
  de casar.
- **Não fazer:** não acrescentar campo `esforco` ao `DossieTarefa` nem à saída do dossiê, e não
  mexer na mensagem do ramo legado (`rdo.py:230-240`) — o grupo novo é tolerado e descartado; quem
  consome esforço é quem despacha, não o instrumento. Não tocar `.claude/tools/review_evidence.py`:
  ele consome `extrair_dossie` e herda a gramática sem edição (e é alvo da `LM-T3`). Não rodar
  `python .claude/tools/backlog.py check` nem tratá-lo como aceite — são 315 violações
  pré-existentes em arquivos que esta tarefa não toca (`AE-1`), e ele sai `1` de qualquer forma.
  Não reescrever cabeçalho de card em plano nenhum: os deste plano estão congelados na forma de
  dois campos por `DM-13` (iii), e os do `P-0739` são da `LM-T5`. Não publicar a gramática em
  `GOVERNANCA.md` nem em skill: é a `LM-T4`.
- **Contingências:**
  1. se o literal citado no passo 1, 2, 3 ou 4 não existir no arquivo exatamente como transcrito
     (linha movida, texto diferente) → parar e sinalizar `blocked` razão `premissa`, citando a
     linha encontrada;
  2. se `python -m pytest tests/ -q` ficar vermelho em teste **fora** de `tests/test_rdo.py` e
     `tests/test_backlog.py` → seguir com a entrega e devolver na linha de retorno
     `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.
- **Pronto quando:** os dois parsers aceitam o cabeçalho de três campos e continuam aceitando o de
  dois; os cinco testes acima existem e passam; a busca do item 3 devolve as linhas nos dois
  arquivos.
- **Fora do escopo desta tarefa:** a publicação da gramática na doutrina (`LM-T4`); a migração dos
  cabeçalhos dos cards do `P-0739` (`LM-T5`); a atribuição de arquivo vermelho no dossiê (`LM-T3`).

### LM-T4 — A gramática da tarefa-módulo e a aposentadoria das duas skills [Opus · classe redacao]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `escalar`. Publica `DM-2`..`DM-5` e `AUT-T8`, aposenta `proximo-passo` e `handover`, cria `passagem-de-bastao`: skills 11 → **10**, guardrails 18 → **19** (`G-MODULO`). Pendência e dois achados roteados pelo `B1` como `AE-37`. RDO: `docs/RDO/P-0740-LM-T4-a-gramatica-da-tarefa-modulo-e-a-aposentadoria-das-duas-skills.md` — o `blocked` anterior foi `A3b` **sem nenhuma edição** (`AE-36`) e **não consumiu retentativa**.
- **Esforço:** high
- **Objetivo:** a doutrina da unidade de trabalho, num ato só. Absorve `AUT-T2` (`DP-I`, o artefato
  `tarefa`), `AUT-T6` (skill única de passagem de bastão), `AUT-T7` (superfícies que apontavam
  para a skill aposentada) e `AUT-T8` (status × veredito).
- **Arquivos-alvo (reescritos pelo `ESC-20`, `DM-43`):** `GOVERNANCA.md` (§3 e §7) ·
  **`README.md`** (tabela *Os guardrails*, `DM-38` (iv), **e** a tabela de skills da *Anatomia do
  kit*) · **`.claude/README.md`** (projeção regenerada — `DM-16` (iv): quem toca a superfície
  fecha a projeção dela) · `.claude/skills/scrum-master/SKILL.md` ·
  **`.claude/skills/passagem-de-bastao/SKILL.md` (NOVO)** ·
  **`.claude/skills/proximo-passo/SKILL.md` (REMOVIDO)** ·
  **`.claude/skills/handover/SKILL.md` (REMOVIDO)** · `docs/DOC_MAP.md`
- **Retirado dos alvos pelo `ESC-1` (`DM-17` (v)):** `.claude/agents/pantonic-planner.md`. A
  edição de arquivo de agente é negada pela camada de permissão do harness (`AE-11`); a
  publicação da gramática nele é o item (b) da `LM-T8`, **depois** desta tarefa. Nada se perde na
  varredura: medido na `ESC-1`, o arquivo não contém a régua antiga.
- **Produto do módulo:** (a) `DM-2`, `DM-3`, `DM-4` e `DM-5` publicados na doutrina, com a gramática de
  cabeçalho de três campos — **copiada do card da `LM-T4a`, que é a residência única do literal
  neste plano** e a única já implementada nos parsers — e o teto de write-clusters reinterpretado
  como limite de **tema**;
  (b) o gate de delegação — hoje no item 5 do
  `proximo-passo` — **nasce na skill nova** já na régua nova, e existe **uma vez só**; **(c) reescrito pelo `ESC-20` (`DM-43`) — não há decisão a tomar, há forma ratificada a
  transcrever:** `.claude/skills/proximo-passo/` e `.claude/skills/handover/` são **removidas** e
  nasce `.claude/skills/passagem-de-bastao/SKILL.md`, por **transposição, não reescrita**, nos
  termos do `AUT-T6` do `P-0737` — cujo dossiê é a fonte do detalhe e **não se copia para cá**
  (`DU-6`). A forma (b) foi **ratificada pelo dono em 2026-08-22** (`DU-5`): `proximo-passo`
  descontinuada, responsabilidade herdada pelo `scrum-master`. A natureza da skill nova foi
  **fixada pelo dono em 2026-08-13** (`TK-36`): maquinário **agente↔agente**, *"transparente
  para o gerente do projeto — ele não a invoca, não a lê e não a acompanha"*. As superfícies que
  citam as duas são atualizadas **no mesmo ato** (`AUT-T7`, absorvida por esta tarefa), e
  material sem portador vira linha no `TK-38`, nunca invenção na skill nova (`DU-9`);
  **(d) acrescentado pelo `ESC-12` (`DM-35` (i)):** a gramática do **bullet de `Status`** de um
  card publicada junto da de cabeçalho — estado entre crases obrigatório, `· AAAA-MM-DD` e razão
  opcionais, cauda em prosa depois de ` — ` —, **copiada do card da `LM-T4b`**, que é a
  residência única do literal e a única já implementada no parser (mesma regra do item (a) com a
  `LM-T4a`).
- **Coerência do módulo (aceite de `DM-3`):** nenhuma das seis superfícies fica citando a régua
  antiga — a varredura de citação é parte da entrega, não tarefa posterior.
- **Verificação:** (corrigida pela `RP-2`, `DM-12`; toda saída abaixo é **medida**, nenhuma é
  deduzida)
  1. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"`
     → exit 0, **depois de a entrega rodar `kit_check.ps1 -Mode generate`**, que é passo da
     tarefa e não da verificação: remover duas skills e criar uma terceira muda a projeção, e
     quem toca a superfície fecha a projeção dela (`DM-16` (iv), acrescentado pelo `ESC-20`). **Correção da `RP-5`:** o exit 0 citado aqui vinha do dossiê da `BKL-T4` e
     **envelheceu** — re-medido em 2026-09-18 pela `RP-5`, o comando sai **exit 1** com 6
     problemas (`.claude/README.md` diverge do regenerado, por atos do dono fora de ciclo:
     descrições de `DM-8` e criação do `pantonic-consultant`). Quem recoloca o exit 0 é a
     `LM-T7`, que regenera a projeção; por isso esta tarefa passa a depender dela. O aceite
     **não** é removido: ele é satisfazível assim que a `LM-T7` fecha. **Re-medido pelo `ESC-12` em 2026-09-19, com a `LM-T7` já fechada:**
     `check-drift` sai **exit 0** (`.claude/README.md == regenerado`, 9 agentes, 11 skills) e
     `.claude/checks/check-readme.ps1` sai **exit 0** (9 agentes, 11 skills, 18 guardrails, 14
     seções). O aceite está **satisfazível hoje**; a nota da `RP-5` acima fica como histórico, e
     a baseline que vale é esta — baseline de corpus real envelhece (`AE-21`).
  2. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o
     total que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa não
     acrescenta teste e **não pode reduzir** esse total — a suíte de conformance é o que tranca
     doutrina. Referência histórica, não aceite: `165 passed` em 2026-09-19 (`ESC-5`).
  3. ```
     pwsh -NoProfile -Command ".claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0** com **10 skills** (11 − 2 + 1). **Medido antes: exit 0 com 11 skills**
     (2026-09-19, `ESC-20`: 9 agentes, 11 skills, 18 guardrails, 14 seções; `ls .claude/skills`
     → 11). A tabela de skills da *Anatomia do kit* em `README.md` fecha **no mesmo ato**, senão
     esta linha sai vermelha — é o invariante de contagem do `AE-12` outra vez, agora sobre
     skills em vez de guardrails. Declarado como **guarda de regressão, não discriminante**
     (mesma natureza do item 3 da `LM-T2b`): esta tarefa publica itens novos em `GOVERNANCA.md`
     §7, e a **checagem 4** do `check-readme.ps1` confronta essa lista com a tabela *Os
     guardrails* do `README.md` — é o invariante de contagem do `AE-12` (critério (viii)), que
     o card não cobria. O executor publica no retorno o número de guardrails **antes e depois**,
     medido, e o `README.md` entra nos `Arquivos-alvo` porque fechar o item **é** fechar a
     tabela que o conta.
  4. Varredura da **aposentadoria**, com os caminhos exatos:
     ```
     pwsh -NoProfile -Command "(Test-Path .claude/skills/proximo-passo), (Test-Path .claude/skills/handover), (Test-Path .claude/skills/passagem-de-bastao) -join ' '"
     ```
     → **False False True**. **Medido antes: True True False**.
  5. Varredura das **citações órfãs**, pelo caminho e não pela palavra (a palavra *handover*
     sobrevive legitimamente em prosa; o **caminho** da skill, não):
     ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md,README.md,docs/DOC_MAP.md,.claude/README.md,.claude/skills/scrum-master/SKILL.md -Pattern '.claude/skills/proximo-passo/' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 4**. E o mesmo com `.claude/skills/handover/` → **0**,
     **Medido antes: 3**. São estas duas linhas que provam a `AUT-T7` feita — sem elas, a remoção
     deixa ponteiro quebrado em quatro superfícies.
  6. Varredura da régua antiga, com o literal exato — **caminhos corrigidos pelo `ESC-20`**, porque
     a lista anterior varria dois arquivos que esta mesma entrega **apaga**, e `Select-String -Path`
     sobre caminho inexistente **erra** em vez de devolver zero:
     ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md,README.md,docs/DOC_MAP.md,.claude/README.md,.claude/skills/scrum-master/SKILL.md,.claude/skills/passagem-de-bastao/SKILL.md,.claude/agents/pantonic-planner.md -Pattern '>8 write-clusters' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1** — a ocorrência única vive em
     `.claude/skills/proximo-passo/SKILL.md:126` (`**>8 write-clusters → dividir em sub-tarefas
     ANTES de delegar.**`), arquivo que **deixa de existir** nesta entrega; por isso a varredura
     nova olha a **skill nova**, que é onde a régua poderia renascer por transcrição descuidada.
     Medido no `ESC-20` com os caminhos novos, **sem** `passagem-de-bastao` (que ainda não existe):
     **0** — isto é, a linha só discrimina se a skill nova nascer limpa, que é o que ela afere.
- **Não fazer:** não rodar `python .claude/tools/backlog.py check` e não tratá-lo como aceite — ele
  linta `docs/DIARIO_DE_OBRAS.md` e os planos, que esta tarefa não toca, e sai `1` com qualquer
  violação; hoje são 315 violações pré-existentes, já encaminhadas ao `P-0739` (`AE-1`). Exigir
  "verde" dele era aceite insatisfazível, do mesmo defeito que o `AE-4`, e a `RP-2` o removeu.
  Não tocar `.claude/agents/pantonic-executor.md` nem
  `.claude/agents/pantonic-reviewer.md` — já publicados por `DM-8`; aferi-los é a `LM-T5`. Não
  reabrir o **item 17 (`G-REPLAN`) de `GOVERNANCA.md` §7**, emendado pela rodada `RP-2` em
  2026-09-18 (`DM-12`): a publicação de `DM-2`..`DM-5` na §7 é matéria de outros itens.
  Não tocar `.claude/skills/diario-de-obras/SKILL.md`, cuja tabela de transições a `RP-2` já
  atualizou. Não tocar `.claude/tools/rdo.py` nem `.claude/tools/backlog.py`: a gramática de três
  campos nos parsers é a `LM-T4a`, que roda antes desta (`DM-13` (ii)); aqui ela só se publica em
  doutrina.
- **Pronto quando:** `GOVERNANCA.md` §3 e §7 trazem `DM-2`, `DM-3`, `DM-4` e `DM-5` publicados com
  a gramática de cabeçalho copiada do card da `LM-T4a`; o gate de delegação existe **uma vez
  só**, na `.claude/skills/passagem-de-bastao/SKILL.md`, na régua nova; as duas skills
  aposentadas **não existem mais na árvore** e nenhuma superfície cita o caminho delas; as
  projeções (`.claude/README.md` e a tabela de skills do `README.md`) estão regeneradas com
  **10** skills; e as **seis** verificações acima passam como escritas — contagem corrigida no `ESC-15` **no mesmo ato** que acrescentou a verificação do `check-readme.ps1`, que é o `DM-18` (i) aplicado ao próprio card (`AE-12`, critério (viii)): quem acrescenta item à lista fecha a frase que a conta. (A sexta
  superfície da redação anterior, o arquivo do planner, saiu dos alvos pelo `DM-17` (v) e segue
  na varredura da `Verificação` 3 só como leitura.)
- **Depende de:** `LM-T4a` — a gramática que esta tarefa publica tem de já estar nos dois parsers,
  senão a doutrina passa a exigir um cabeçalho que os instrumentos do kit rejeitam (`AE-5`, `F-5`,
  `F-6`). E **`LM-T7`** — a `Verificação` 1 desta tarefa exige `check-drift` exit 0, que hoje sai
  **exit 1** (medido pela `RP-5`) e que só a regeneração da `LM-T7` recoloca em 0. A `LM-T8`
  (toolset, `blocked` por ato do dono) **não** é dependência desta tarefa: nada aqui precisa do
  `tools:` do planner (`DM-17` (v)). **Acrescentado pelo `ESC-7`:** e **`LM-T2c`** — esta tarefa
  publica doutrina que cita as tabelas de roteamento e tem o **mesmo** arquivo
  (`.claude/skills/scrum-master/SKILL.md`) em `Arquivos-alvo`; publicar sobre um bloco A
  incompleto é a ordem invertida que a `DM-13` proíbe no eixo dela, e as duas não podem estar
  abertas ao mesmo tempo sobre o arquivo. **Acrescentado pelo `ESC-8`:** e **`LM-T2d`**, pela
  mesma razão — ela fecha a partição do bloco A que a `A8a` deixou aberta (`AE-20`, `DM-26`).
  **Acrescentado pelo `ESC-12`:** e **`LM-T4b`**, que ensina ao `backlog.py` o bullet de
  `Status` que esta tarefa vai publicar como doutrina — parser antes de doutrina (`DM-13` (ii),
  `AE-5`/`AE-6`). Não há exclusão mútua entre as duas: arquivos diferentes.
- **Restrição acrescentada pelo `ESC-12` (`DM-35` (v)) — o que `AUT-T8` publica:** a doutrina de
  **status × veredito** que esta tarefa absorve tem de sair **conforme as decisões desta
  janela**, que o card foi autorado antes de conhecer: `DM-25` (`escalar` não é desfecho de
  tarefa; é desfecho da pendência), `DM-26` (o bloco A parte **primeiro por veredito**, e regra
  nenhuma manda fazer o que o instrumento de fechamento recusa) e, em especial, **`DM-32`** —
  **`reprovado` não é desfecho de RDO**: a `A7` materializa `blocked` razão `premissa` e para,
  porque o RDO só nasce na transição `review` → `done` (`DP-F` item 3) e `rdo.py close
  --veredito` aceita só `aprovado` e `ressalva` (medido: exit 2). Publicar `AUT-T8` sem isso
  escreveria doutrina **contra** a tabela de roteamento que a `LM-T2c`, a `LM-T2d` e a `LM-T2e`
  acabaram de fechar. Nenhuma linha do bloco A é reescrita aqui — ele está fechado; esta tarefa
  **publica** o que ele já diz.

### LM-T5 — Revisão da criação das tarefas [Opus · classe investigacao]

- **Status:** `done` (2026-09-19) — **ressalva 88%**, bloqueante `nenhuma`, recomendação `escalar`. Antecipada na fila pela Diretiva de execução item 4 (decisão do loop). Julgou **20** cards: 4 passam, 16 não passam, **nenhum por conteúdo — todos por linha de aceite**. Pendência e quatro achados roteados pelo `B1` como `AE-31`. RDO: `docs/RDO/P-0740-LM-T5-revisao-da-criacao-das-tarefas.md`.

> **Nota de reconciliação (`ESC-15`, `DM-38` (v)):** a rubrica entregue publica **quinze**
> critérios, `(i)`..`(xv)` — as duas aferições que este card prescrevia sem numeral saíram como
> `(xiv)` e `(xv)`, decisão do executor dentro do escopo, mantida pelo laudo. Onde o corpo abaixo
> disser "doze critérios", leia-se a rubrica: **ela** é a referência canônica. O corpo fica
> **literal** — card fechado é registro histórico, não se reescreve (`DM-33` (iii) aplicado à
> própria auditoria).

- **Esforço:** high
- **Objetivo:** julgar se os cards que o planejamento produz são **executáveis como módulo**. Tarefa
  pedida nominalmente pelo dono em 2026-09-18.
- **Entregável:** uma rubrica curta de **criação de tarefa**, publicada em
  `docs/RUBRICA_DE_REVISAO.md` como seção própria, aplicada retroativamente aos cards `LM-T1`..
  `LM-T4` deste plano — inclusive a `LM-T4a` — e aos 6 cards `ready` restantes do `P-0739`. Por
  card: passa / não passa,
  com o defeito nomeado quando não passa.
- **Método prescrito:** confrontar cada card contra (i) as três proibições do
  `pantonic-executor` — o card exige avaliar, decidir ou tratar ambiguidade?; (ii) `DM-2`/`DM-4` —
  é um tema só, fechado, sem transversal?; (iii) `DM-13` — o cabeçalho segue a gramática que os
  **parsers** aceitam na data do card (dois campos mais o campo `- **Esforço:**` no corpo enquanto
  a `LM-T4a` não fecha; três campos depois dela), e não uma forma que só a doutrina conhece — julgar
  pela forma final antes de o parser aceitá-la é o defeito que o `AE-5` mediu;
  (iv) o aceite de coerência de `DM-3` está declarado?; (v) os números de aceite são
  re-deriváveis por comando, não copiados?; (vi) todo entregável que **cria, versiona ou apaga**
  arquivo foi confrontado com a regra de versionamento vigente (`.gitignore`) e com o filtro do
  instrumento que vai julgá-lo — e a `Verificação` do card discrimina o mundo com a mudança do
  mundo sem ela?; (vii) **toda linha de `Verificação` publica saída observada, não deduzida** — o
  comando é citado com os argumentos exatos, o literal esperado veio de uma execução medida (dossiê
  ou achado), a pergunta binária usa a flag binária e o exit code em vez de uma flag de diagnóstico,
  e nenhum aceite exige "verde" de instrumento que a tarefa não pode deixar verde;
  (viii) **`DM-18`** — o card que mexe em item de lista ou de tabela enumerada fecha, no mesmo
  ato, a frase da **mesma seção** que conta ou qualifica o conjunto, e estende o instrumento que
  julga a seção quando ele não discrimina essa afirmação. Caso medido: `AE-12`;
  (ix) **`DM-21`** — nenhuma exigência **estrutural** ("usa a função X", "não reimplementa",
  "importada, não copiada") é prometida como teste comportamental: ou vem com o **caso** em que a
  implementação certa e a reimplementação plausível divergem, ou vira inspeção mecânica na
  `Verificação`, ou é declarada como `Restrição` sem teste. Caso medido: `AE-16`;
  (x) **`DM-23`** — nenhuma linha de `Verificação` carrega **total de suíte** como constante de
  aceite: o piso é relação ("não reduz o total re-medido no despacho, e soma os `<N>` testes
  novos"), e o número aparece só como referência histórica datada. Caso medido: `AE-18` — cinco
  correções manuais de piso em sete despachos da mesma janela;
  (xi) **`DM-24`** — toda linha de `Verificação` por efeito em arquivo publica **os dois** valores
  rodados (antes e depois), e padrão que devolve o **mesmo** valor nos dois mundos é inválido por
  construção; comando cujo literal tem crase, asterisco ou barra invertida vai em **bloco
  cercado**, e padrão textual leva `-SimpleMatch`. Caso medido: `AE-19`.
- **Insumo medido pelo loop, a citar (`ESC-14`, 2026-09-19):** a janela gastou **867k tk em cinco
  passagens do consultor** (`ESC-9`..`ESC-13`) contra **quatro tarefas fechadas** e quatro
  executores despachados. O número é **medido pelo loop**, não auto-relatado pelo consultor
  (`GOVERNANCA.md` §4.2), e entra aqui por dois motivos: é insumo direto do juízo desta tarefa
  sobre **quanto custa um card mal autorado** — cada parada de executor por aceite custou um
  despacho inteiro — e é insumo do veredito do dono na `LM-T6`. Não governa rota (`DP-Q`): é
  medida.
- **Insumo medido, a citar:** o `AE-1` do `TK-54` (card devolvido `blocked motivo=premissa` por
  coluna de classificação sem critério fechado, 63,2k tk gastos na triagem sem tocar arquivo), o
  `AE-10` do `P-0739` (dependência de ordem que o card não declarou) e o **`AE-2` deste plano**
  (entregável que mandava versionar `.claude/estado/` contra um `.gitignore` que o excluía, com
  `Verificação` que supunha o arquivo aparecendo em `git status`; 61,8k tk na triagem, nenhum
  arquivo tocado — é o caso medido do critério (vi)) e o **`AE-4` deste plano** (duas das cinco
  verificações do card reescrito eram insatisfazíveis por comportamento documentado do `git`:
  `check-ignore -v` reporta o padrão decisivo mesmo quando é negação, e `status --porcelain` sem
  `-uall` colapsa o diretório não rastreado; a entrega inteira foi produzida e devolvida `blocked`
  por um aceite que ninguém tinha rodado — é o caso medido do critério (vii)). São as quatro classes
  de defeito que a rubrica tem de pegar, e `AE-2` e `AE-4` são os **dois casos medidos na própria
  autoria deste plano**: no primeiro o card contradizia a configuração do repositório; no segundo, o
  comportamento real do instrumento de aceite. A rubrica nomeia os dois.
  **Mais dois insumos medidos, acrescentados pelo `ESC-1` e pelo `ESC-2`:** o `AE-11` (card
  impecável em conteúdo e **inexecutável por permissão** — o entregável não foi confrontado com a
  política de permissão vigente; 59,5k tk, nenhum arquivo tocado) e o `AE-12` (o card fechou o
  **item** e não fechou o **invariante da mesma seção** que o item quebra, com as cinco
  verificações verdes — é o caso medido do critério (viii)). São **seis** classes de defeito que
  a rubrica tem de pegar, e quatro delas foram medidas na autoria deste plano.
  **Mais dois insumos, do `ESC-3` e do `ESC-4`:** o `AE-14` (card **sobrevivente** de cinco
  rodadas de reparo, nunca reautorado sob as lições que elas compraram — recusado no gate, sem
  gastar executor: a auditoria varre **card antigo**, não só card novo) e o `AE-16` (exigência
  estrutural prometida como teste comportamental, que nenhum dos três testes discriminava). São
  **oito** classes, seis delas medidas na autoria deste plano.
  **Nona classe, do `ESC-5`:** o `AE-18` — número de aceite **medido no planejamento** que
  envelhece dentro da **mesma janela** que o consome, porque as tarefas fecham em série e cada
  uma move a suíte (série medida: 145 → 153 → 156 → 161 → 165 em seis tarefas). É o caso do
  critério (x), e o único das nove que **não** se corrige lendo melhor o card: corrige-se
  trocando constante por relação.
  **Décima classe, do `ESC-7`:** achado **órfão** — `AE-9` tinha rota "matéria da `LM-T2`" e
  sobreviveu à reescrita da `LM-T2` (`ESC-3`), que passou a proibir tocar o bloco A; ninguém
  reconferiu a rota contra as `Restrições` novas, e o buraco só apareceu no laudo da tarefa
  seguinte. A rubrica afere: **card reescrito re-declara as rotas de achado que aponta para
  ele**.
  **Décima segunda classe, do `ESC-13` — e é a que esta janela pagou sete vezes:** o **comando de
  aceite** é derivado que erra sem sinal, porque nada o confronta com a fonte. Sete casos medidos
  na mesma janela: `AE-19` (crase dupla, 0 → 0), `AE-21` (baseline de corpus real envelhecida
  entre autoria e despacho), `AE-23` (padrão que **reescreve** palavra da fonte — `ultima` por
  `última` —, 0 nos dois mundos), `AE-25` (padrão **sem a opção** que o torna discriminante —
  `Select-String` ignora caixa por padrão, 1 nos dois mundos), `AE-26` e `AE-27` item 2 (aceite
  apoiado em **contrato de instrumento que ninguém verificou**) e `AE-28` (aceite cujo **alvo é
  inalcançável dentro do escopo do card**: exigia do instrumento uma transição que a tabela de
  `DP-F` não tem). Três autores diferentes os produziram — planejador, consultor e o próprio
  loop —, o que o classifica como defeito **de método**, não de pessoa. A rubrica ganha por isso
  os critérios (xii) e (xiii) abaixo, e eles são o **produto central** desta tarefa: sem eles,
  ela é diagnóstico.
  **Décima primeira classe, do `ESC-8`:** regra de roteamento que **não parte o domínio** —
  a `A8a` cobriu `escalar` para entrega aprovada e deixou dois pares sem regra útil, um deles
  mandando fazer o que o instrumento recusa (`AE-20`). A rubrica afere: **regra nova de tabela
  declara o efeito sobre cada valor do domínio que toca, e confronta a ação com o domínio que o
  instrumento de fechamento aceita**.
- **Produto (b), acrescentado pelo `ESC-14` (`DM-37`) — a forma normativa do bloco
  `Verificação`, para que a régua saia **executável**, não como item de leitura.** A rubrica fixa,
  além dos critérios, a **forma** que todo item de `Verificação` tem de ter, com três elementos
  nomeados e legíveis por máquina: (1) o **comando**, em bloco cercado, exatamente como foi rodado;
  (2) o **valor esperado**, na linha iniciada por `→`; (3) o **valor medido antes**, no literal
  `**Medido antes: <valor>**`. É a forma que 20 itens deste plano já usam (medido no `ESC-14`), e a
  norma só a torna obrigatória e parseável. **Por que isto e não um décimo quarto critério:** a
  classe tem doze critérios e produziu oito defeitos numa janela — o `AE-30` inclusive **sobreviveu
  ao próprio ato que escreveu o critério contra ele**, três parágrafos acima da linha defeituosa.
  Checklist lido por autor não fecha defeito de autoria; o que fecha é **comando que falha
  ruidosamente no ato da autoria**. A rubrica, portanto, **prescreve o passo mecânico** —
  `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` — e declara que card cujo
  `card_check` não sai 0 **não se despacha**. O instrumento é a **`LM-T5b`**, que roda logo depois
  desta tarefa; enquanto ele não existe, o passo é a conferência manual dos três elementos, e a
  rubrica diz isso com data.
- **Critérios (xii) e (xiii), acrescentados pelo `ESC-13` (`DM-36` (iv)) — texto a publicar na
  rubrica, e a régua com que esta tarefa julga todo card:**
  **(xii) Comando de aceite é medida, não afirmação.** Ele (a) é **recorte do literal da fonte**,
  copiado do arquivo-alvo, nunca uma palavra reescrita de memória — acento, caixa e pontuação
  pertencem ao texto medido (`AE-23`); (b) foi **rodado nos dois mundos** pelo autor, e os dois
  valores aparecem no card — padrão que devolve o mesmo valor antes e depois é inválido por
  construção (`AE-19`, `DM-24`); (c) carrega **as opções que tornam a medida discriminante** —
  `-SimpleMatch` para texto, `-CaseSensitive` quando é a caixa que muda (`AE-25`); e (d) tem
  **alvo alcançável dentro do escopo declarado do card**: não exige estado, transição, permissão
  ou arquivo que o card não entrega, nem contrato de instrumento que o autor não verificou
  (`AE-26`, `AE-27` item 2, `AE-28`). O teste da alínea (d) é uma pergunta só: *executando só o
  que este card manda executar, este comando pode sair como o card diz?*
  **(xiii) Baseline de corpus real é relação, re-medida no despacho.** Nenhum número tirado do
  corpus — total de suíte, contagem de cards, número de ocorrências, total de linhas — entra no
  card como **constante de aceite**: entra como relação (`não reduz`, `sobe em N`, `os dois
  números iguais`), com o literal citado só como referência **datada**. Caso medido no próprio
  ato que escreveu este critério: o `ESC-12` publicou `18 18` como aceite da `LM-T4b` e, ao rodar
  o comando publicado, mediu `21 0` — o total do plano mudara durante a autoria, por causa dos
  cards que o mesmo ato acrescentava (`AE-21`, `DM-23`).
- **Segundo entregável — o reagrupamento do `P-0739` (`DM-9`) — RETIRADO desta tarefa pelo
  `ESC-13` (`DM-36` (iii)) e residente agora na `LM-T5a`.** O texto abaixo fica como registro do
  que a `LM-T5a` herda; **esta** tarefa não toca `docs/plans/P-0739-backlog-instrumento.md`.
  Razão: o dono estacionou o `P-0739` em 2026-09-19 (*"`P-0739` **não retorna** enquanto o
  `P-0740` não encerrar"*), e a auditoria de criação de card é matéria **urgente** desta janela
  enquanto o reagrupamento de outro plano não é — juntá-los faria a urgente esperar a que o ato
  do dono adiou. Antigo texto: Julgar os 6 cards `ready`
  restantes (`BKL-T5`..`BKL-T9`, mais o que a rodada do `AE-10` exigir) **não basta**: eles foram
  autorados sob a régua atômica e não se executam um a um sem reproduzir o defeito que este plano
  corrige. Esta tarefa **reescreve os 6 como módulos coesos** sob a gramática de `DM-2`..`DM-5`,
  na própria `docs/plans/P-0739-backlog-instrumento.md`, e **absorve a rodada de replanejamento do
  `AE-10`** (dependência de ordem entre `transacionar_status` e os marcadores
  `<!-- fila:gerada -->` que a `BKL-T6` item (a) insere): a ordem passa a ser fixada no
  reagrupamento, não numa rodada separada. Saída: o `P-0739` com uma fila nova, de módulos, pronta
  para fechar **numa rodada única**.
- **Pronto quando (reescrito pelo `ESC-13`, `DM-36` (v) — contagem é relação, não constante):** a
  seção nova em `docs/RUBRICA_DE_REVISAO.md` ≤ 50 linhas **mais** o que os critérios (xii) e
  (xiii) exigirem (teto novo: ≤ 70 linhas, medido contra `(Get-Content
  docs/RUBRICA_DE_REVISAO.md).Count` antes e depois); **todos** os cards deste plano que não são
  a própria auditoria nem o piloto, **contados no despacho** — eram 13 quando o card foi
  autorado, são **19** em 2026-09-19 (medido no `ESC-13`, **depois** de a `LM-T5a` entrar: 22 cards no
  plano, menos `LM-T5`, `LM-T5a` e `LM-T6`; re-contar no despacho, que é o critério (xiii)
  aplicado a esta própria linha) — julgados numa tabela, um por linha, com o defeito nomeado quando não passa; e os
  critérios (xii) e (xiii) publicados na rubrica com os sete casos medidos nomeados. O
  reagrupamento do `P-0739` **não** é aceite desta tarefa (é a `LM-T5a`). Texto anterior do
  aceite, mantido como histórico do que a `LM-T5a` herda: os **15** cards
  julgados numa tabela — os **9** deste plano que não são a própria auditoria nem o piloto
  (`LM-T1`, `LM-T1a`, `LM-T2`, `LM-T2a`, `LM-T2b`, `LM-T2c`, `LM-T3`, `LM-T3a`, `LM-T4a`,
  `LM-T4`, `LM-T7`, `LM-T7a`, `LM-T8` — **13**) e os 6 do `P-0739`, **19** no total (contagem
  atualizada pelo `ESC-7`, 2026-09-19); todo card reprovado sai com o defeito nomeado e a rota; e os 6 cards
  `ready` do `P-0739` reescritos como módulos, com cabeçalho de três campos, aceite de coerência
  declarado e a dependência de ordem do `AE-10` resolvida na fila — `AE-10` fechado no mesmo ato.
- **Verificação (reescrita pelo `ESC-14`, `DM-37`):** tarefa sem artefato executável — a
  verificação é por efeito no **único** arquivo-alvo, `docs/RUBRICA_DE_REVISAO.md`. A linha que
  media `docs/plans/P-0739-backlog-instrumento.md` **saiu**: ela media arquivo que esta tarefa
  está proibida de tocar desde o `ESC-13`, e sua residência é a `Verificação` 1 da **`LM-T5a`**,
  onde ela já está escrita — é o `AE-30`, oitavo caso da décima segunda classe, e o único cuja
  causa foi **a emenda que retirou o entregável sem reconferir o aceite que dependia dele**.
  1. ```
     pwsh -NoProfile -Command "(Get-Content docs/RUBRICA_DE_REVISAO.md).Count"
     ```
     → cresce em **≤ 70** sobre o valor do despacho (teto ampliado pelo `DM-36` (iv), que
     acrescentou dois critérios à seção). **Medido no `ESC-14`: 274** linhas hoje. Relação, não
     constante (critério (xiii)). `Measure-Object -Line` **não** serve aqui: ignora linha vazia e
     erra a conta.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'LM-T' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **ao menos uma linha por card julgado**, com o total de cards **re-contado no despacho**
     (medido no `ESC-13`: 19). **Medido no `ESC-14`: 0** — o arquivo não cita nenhum `LM-T`, então
     o item discrimina. O `-CaseSensitive` entra pelo critério (xii) (c): sem ele o padrão casaria
     grafia minúscula e mediria outra coisa (`AE-25`).
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'Medido antes' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: a rubrica publica a **forma normativa** do bloco `Verificação` (produto (b)
     abaixo), e o literal `Medido antes` é parte dela. **Medido no `ESC-14`: 0** na rubrica, contra
     **20** ocorrências no plano — a forma já é a prática dominante dos cards; o que falta é ela
     ser **norma legível por máquina**, que é o que a `LM-T5b` vai parsear.
- **Depende de:** **nada** — dependência de `LM-T4` **dissolvida pelo `ESC-13`** (`DM-36` (iii)),
  por medida: o critério (iii) afere *"a gramática que os **parsers** aceitam na data do card"*, e
  quem a ensinou aos parsers foi a `LM-T4a`, **fechada**; e `DM-2`..`DM-5` são decisões **deste
  plano**, que a `LM-T4` publica mas não cria. A rubrica, portanto, tem toda a matéria de que
  precisa **antes** da `LM-T4` — e, invertida a ordem, a `LM-T4` publica doutrina já conhecendo a
  regra de autoria que esta tarefa fixa. Nenhuma exclusão mútua: o alvo aqui é
  `docs/RUBRICA_DE_REVISAO.md`, que nenhuma outra tarefa aberta toca.

### LM-T5a — A decisão de reagrupamento do `P-0739` e o mapa de herança das superfícies mortas [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-19 — devolvida de `blocked` razão `premissa` pela **segunda** vez, agora com o
  **produto trocado** (`ESC-35`, saída (c) do `G-REPLAN`). Os dois bloqueios foram conduta correta e
  mediram coisas diferentes: o primeiro, que a **partição** não estava decidida (fechada no
  `ESC-34`); o segundo, que a **transcrição** depende de uma árvore que este plano ainda está
  mudando. **O loop não roda `status`** — o card já está `ready`.
- **Esforço:** low
- **Objetivo:** um só — deixar o `P-0739` com a **decisão** de reagrupamento e o **mapa de herança**
  escritos no próprio arquivo, para que a retomada não redecida nada e não tropece de novo em alvo
  morto. A **transcrição** dos três módulos **não** é desta tarefa: ela é o primeiro ato da
  retomada, com a árvore estável.
- **Depende de:** nada. Nada depende desta. O `P-0739` segue **estacionado** por ato do dono.
- **Arquivos-alvo:**
  - `docs/plans/P-0739-backlog-instrumento.md`
- **Por que o produto mudou, e por que isto não perde matéria:** a `BKL-T8` tem por alvos
  `.claude/skills/proximo-passo/SKILL.md` e `.claude/skills/handover/SKILL.md`, que a **`LM-T4`
  deste plano aposentou e removeu da árvore** (`f1afbd3`); o aceite herdado dela — *Grep
  `backlog.py` em `.claude/skills/` ≥ 3 arquivos* — ficou **inalcançável** (`AE-64`). Transcrever
  alvo morto produz card que bloqueia no despacho; suprimir a matéria perde entrega. A saída é
  **separar decisão de transcrição**: decisão carrega o contexto desta janela e se escreve agora;
  transcrição mede a árvore e se escreve quando a árvore parar. Os cinco cards ficam **intactos e
  `ready`** — nada se perde, e o plano estacionado não despacha nenhum deles.
- **Varredura já feita pelo consultor (`ESC-35`), e é ela que fecha a classe:** todos os caminhos
  citados nos cinco cards foram confrontados com a árvore de hoje. **Mortos: exatamente dois**, e
  os dois pela mesma `LM-T4` — `.claude/skills/proximo-passo/SKILL.md` e
  `.claude/skills/handover/SKILL.md`. Não são alvo morto, apesar de ausentes: `backlog_hook.py`
  (arquivo **a criar** pela matéria da `BKL-T7`), `GOVERNANCA_MEMORIAS.md` (doc global, fora do
  repo) e os padrões de nome de plano em prosa. **Não há terceira superfície morta**: a varredura
  não se repete na retomada.
- **Produto do módulo:**
  - **(a) A nota de replanejamento, datada, no `P-0739`**, com a partição decidida no `ESC-34`
    transcrita **sem re-decisão**: três módulos — `BKL-T10` (absorve `BKL-T5` + `BKL-T6`),
    `BKL-T11` (absorve `BKL-T7` + `BKL-T8`), `BKL-T12` (absorve `BKL-T9` sozinha) —, a ordem
    `BKL-T10` → `BKL-T11` → `BKL-T12`, o encerramento do `AE-10` pelo `AE-47` (a guarda de
    `transacionar_status` dissolveu a dependência de ordem com os marcadores
    `<!-- fila:gerada -->`), e a declaração de que **a transcrição dos três cards é o primeiro ato
    da retomada**, não desta tarefa.
  - **(b) O mapa de herança**, no mesmo bloco, contendo o literal `herdeira da matéria`:
    `proximo-passo` e `handover` → **`passagem-de-bastao`** é a **herdeira da matéria** de skill da
    `BKL-T8`, com `scrum-master` recebendo a parte de condução do loop. Isto **ratifica** o que a
    `LM-T4` já fez (ela criou a skill nova com o mesmo conteúdo) — não inventa sucessão. No mesmo
    parágrafo, a regra do número: o aceite herdado *"≥ 3 arquivos"* **não se transcreve**; ele se
    **re-deriva na retomada** sobre a árvore de então, pela relação *"toda skill que invoca o
    instrumento o cita"*, nunca por constante copiada (critério (xiii)/(xviii)).
  - **(c) Um bullet de ponteiro em cada um dos cinco cards**, na forma
    `- **Absorvida por:** <ID do módulo> na retomada (ESC-34/ESC-35)`, logo abaixo do bullet de
    `Status`. **O corpo dos cinco não se toca e o `Status` dos cinco não muda** — eles seguem
    `ready`, porque o plano está estacionado e a transcrição é da retomada.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern 'BKL-T10' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: a partição está escrita no arquivo que a consome. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern 'herdeira da matéria' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: o mapa de herança está escrito. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern 'Absorvida por' -SimpleMatch | Measure-Object).Count"
     ```
     → **5**: um ponteiro por card absorvido, nem mais nem menos. **Medido antes: 0**.
  4. ```
     python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog as b;from pathlib import Path;m=b.carregar(Path('.'));p=[x for x in m.planos if x.id=='P-0739'][0];print(sorted(t.id for t in p.tarefas if t.status=='ready'))"
     ```
     → `['BKL-T5', 'BKL-T6', 'BKL-T7', 'BKL-T8', 'BKL-T9']`, **inalterado**: esta tarefa **não**
     transcreve card nenhum, e é esta linha que o prova. **Medido antes: ['BKL-T5', 'BKL-T6',
     'BKL-T7', 'BKL-T8', 'BKL-T9']**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '- **Objetivo:**' -SimpleMatch | Measure-Object).Count"
     ```
     → **18**, **inalterado**: nenhum card entra nem sai do arquivo. **Medido antes: 18**.
  6. ```
     python -m pytest tests/ -q
     ```
     → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não toca código.
     **Medido antes: exit 0** — veredito invariante; referência **datada**: `201 passed` em
     2026-09-19.
- **Restrições desta tarefa:** **nenhuma tarefa do `P-0739` é executada**, e **nenhum card dele é
  reescrito** — nem o corpo, nem o `Status`. A partição **não se re-decide**: ela está fechada no
  `ESC-34` e aqui só se transcreve. O número do aceite da matéria da `BKL-T8` **não se escreve**:
  escreve-se a **regra** de re-derivação. Nenhum arquivo de `.claude/` é tocado. Nenhum card do
  `P-0740` é tocado.
- **Não fazer:** não criar os cards `BKL-T10`..`BKL-T12` (é a retomada que os escreve); não mudar o
  `Status` dos cinco; não apontar nada para `.claude/skills/proximo-passo/` nem
  `.claude/skills/handover/`, que não existem; não tratar `backlog.py check` como aceite (`AE-1`);
  não commitar.
- **Contingências:**
  1. se os cinco cards `BKL-T5`..`BKL-T9` não estiverem todos `ready` no despacho → parar e
     sinalizar `blocked` razão `premissa`, citando os estados encontrados;
  2. se a varredura do card não bater com a árvore no despacho — isto é, se aparecer **terceira**
     superfície morta entre os caminhos citados pelos cinco → **parar** e sinalizar `blocked` razão
     `premissa`, nomeando-a: decidir herança é do consultor.
- **Pronto quando:** a nota datada com a partição e o mapa de herança está no `P-0739`, os cinco
  ponteiros existem, **nenhum card foi criado, reescrito ou teve `Status` mudado** — e as **seis**
  linhas de `Verificação` saem nos valores declarados, três delas como `inalterado`.

### LM-T5b — `card_check.py`: a régua de autoria que roda [Sonnet · classe implementacao]

- **Status:** `done` (2026-09-19) — **ressalva 91%**, bloqueante `nenhuma`, recomendação `escalar`. O instrumento existe e pega o que foi contratado, mas o laudo **reproduziu um falso verde residual** e dois achados sobre o gate: roteados pelo `B1` como `AE-32`. RDO: `docs/RDO/P-0740-LM-T5b-card-check-py-a-regua-de-autoria-que-roda.md`. Card novo do `ESC-14` (2026-09-19), residência única do passo mecânico que
  o `DM-37` prescreve. **Sem ele a rubrica da `LM-T5` continua sendo leitura**, e a classe já
  provou que leitura não a fecha: oito defeitos numa janela, doze critérios em vigor, e o `AE-30`
  produzido **no mesmo ato** que escreveu o critério contra ele.
- **Esforço:** low
- **Objetivo:** um só — o autor de um card roda **um comando** contra o card que acabou de escrever
  e ele **falha ruidosamente** quando o aceite não mede o que diz medir.
- **Depende de:** `LM-T5` — é ela que fixa a **forma normativa** do bloco `Verificação` (produto
  (b)) que este instrumento lê. **Precede** o despacho da `LM-T4b` e da `LM-T4`: a re-varredura que
  o `DM-36` (vi) me atribuiu passa a ser **mecânica**, rodada pelo loop, em vez de leitura de
  consultor.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
  - `tests/test_card_check.py`
  - `tests/fixtures/card_check/` (os três cards sintéticos do aceite, `ESC-15`)
- **Produto do módulo:** um verbo só — `python .claude/tools/card_check.py --plano <plano>
  --tarefa <ID>` —, que: (a) recorta o bloco `Verificação` do card pelo mesmo parser de campos que
  o kit já usa (`rdo._parsear_campos`, **importado, nunca reescrito**); (b) para cada item, exige
  os **três elementos** da forma normativa — comando em bloco cercado, linha `→` com o esperado, e
  o literal `**Medido antes: <valor>**`; item incompleto é **falha nomeada**; (c) **roda** cada
  comando publicado e compara a saída com o `Medido antes` declarado — divergência é falha
  nomeada, porque significa que o card descreve um mundo que não é o que está na árvore; (d) sai
  **0** quando todos os itens fecham e **1** com uma linha por item que falhou, dizendo qual dos
  três elementos falta ou qual valor divergiu.
- **Contrato de segurança (não é detalhe — é o que torna (c) aceitável):** o instrumento só executa
  comando cujo primeiro token esteja numa **lista fechada** (`python`, `pwsh`) e recusa, com falha
  nomeada, qualquer linha com `;`, `&&`, `|` fora do bloco cercado, redirecionamento ou
  substituição de comando. Comando que ele recusa é reportado, **nunca** executado — e o autor o
  reescreve ou o declara fora do aceite mecânico.
- **Testes** (três): `TF-item-sem-medido-antes-falha`; `TF-divergencia-de-valor-falha` (card
  sintético cujo `Medido antes` não bate com a saída do comando); `TR-card-integro-sai-zero`.
  *Concorrentes:* sem (b) o instrumento aprovaria item sem baseline — o `AE-21` inteiro; sem (c)
  aprovaria baseline envelhecida — o `AE-23`, o `AE-25` e o `AE-30`.
- **Entregável de fixture (acrescentado pelo `ESC-15`, `DM-38` (ii)):** três cards sintéticos em
  `tests/fixtures/card_check/plano-exemplo.md`, escritos **por esta tarefa**: `EX-T1` conforme à
  `### 8.1` (os três elementos em todos os itens, com um comando cujo valor bate com a árvore de
  teste); `EX-T2` com um item **sem** `**Medido antes:**`; `EX-T3` com `**Medido antes:**` cujo
  valor **não** bate com a saída do comando. São eles o aceite — **nenhum card vivo do plano é
  aceite deste instrumento** (`DM-38` (ii)).
- **Verificação:** (forma normativa da `### 8.1` da `docs/RUBRICA_DE_REVISAO.md`; baselines medidas
  pelo consultor no `ESC-15`)
  1. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T1
     ```
     → **exit 0**. **Medido antes: exit 2** (`card_check.py` não existe; `python` sai 2 em
     `can't open file`).
  2. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T2
     ```
     → **exit 1**, com a linha do item nomeando o elemento ausente (`Medido antes`).
     **Medido antes: exit 2** (o instrumento não existe).
  3. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T3
     ```
     → **exit 1**, com a linha do item nomeando a divergência entre o valor declarado e a saída
     medida. **Medido antes: exit 2** (o instrumento não existe).
  4. ```
     python -m pytest tests/ -q
     ```
     → verde, com **três testes a mais** que o total re-medido no despacho (`DM-23`).
     **Medido antes: 175 passed** (2026-09-19 — relação, **re-medir no despacho**, critério (xiii)).
- **Restrições desta tarefa:** o instrumento **não corrige** card — só afere e reporta; quem
  reescreve é o autor. Não julga conteúdo do card (objetivo, passos, restrições): só o bloco
  `Verificação`. Não substitui o `pantonic-reviewer`: roda **antes** do despacho, não depois da
  entrega. `rdo.py`, `backlog.py` e `review_evidence.py` ficam **intocados** — este é instrumento
  novo, e a única importação é o parser de campos.
- **Não fazer:** não estender `backlog.py check` (é instrumento do `P-0739`, estacionado, e já sai
  vermelho com 315 violações pré-existentes, `AE-1`); não rodar comando fora da lista fechada; não
  tocar card nenhum do plano; não commitar.
- **Contingências:**
  1. se a forma normativa que a `LM-T5` publicou divergir dos três elementos citados aqui → parar e
     sinalizar `blocked` razão `premissa`, citando a forma publicada: quem manda é a rubrica, e o
     instrumento se ajusta a ela, nunca o contrário;
  2. se a `Verificação` 1 sair **1** por baseline envelhecida do próprio `LM-T3b` (o plano mudou
     entre a autoria e o despacho) → **não** é falha desta tarefa: reportar a divergência ao loop,
     que a devolve ao consultor — é exatamente o defeito que o instrumento existe para pegar.
- **Pronto quando:** `card_check.py` existe com o verbo único; sai **0** em `EX-T1` e **1** em
  `EX-T2` e `EX-T3`, nomeando em cada caso o elemento ausente ou o valor divergente; recusa
  comando fora da lista fechada; os três testes existem; e a suíte fica verde.

### LM-T5c — O gate ligável: onde começa um item, o silêncio proibido e a recusa por token [Sonnet · classe implementacao]

- **Status:** `done` (2026-09-19) — **ressalva 76%**, bloqueante `nenhuma`, recomendação `escalar`. O falso verde fechou, mas **abriu um falso vermelho** e a matéria 5 regrediu para filho `cp1252`: roteados pelo `B1` como `AE-33`. O gate segue **suspenso**. RDO: `docs/RDO/P-0740-LM-T5c-o-gate-ligavel-onde-comeca-um-item-o-silencio-proibido-e-a-recusa-por-token.md`. Card novo do `ESC-16` (2026-09-19), residência única das **quatro** matérias
  do `AE-32` — **mais a quinta matéria** que o `ESC-16` mediu ao rodar o instrumento contra este
  próprio card (codificação da saída capturada). Elas vêm num card só porque são **um assunto
  só** (`DM-2`): tornar o `card_check`
  confiável o bastante para virar gate. Partir em dois criaria exclusão mútua sobre os **mesmos
  dois arquivos** e entregaria, no meio do caminho, um instrumento que ainda não pode ser ligado.
- **Esforço:** low
- **Objetivo:** um só — o `card_check` deixa de dar verde a item que ele não leu, e deixa de recusar
  a forma de comando que o kit usa; com isso o gate da `### 8.1` pode ser ligado.
- **Depende de:** `LM-T5b` (fechada — é o instrumento dela que esta tarefa corrige) e `LM-T5`
  (fechada — é a `### 8.1` dela que esta tarefa emenda). **Precede o despacho da `LM-T4b`, da
  `LM-T4`, da `LM-T3b` e da `LM-T6`**: enquanto ela não fecha, o loop re-deriva baseline à mão, que
  é o custo que esta tarefa elimina.
- **Arquivos-alvo:**
  - `.claude/tools/card_check.py`
  - `docs/RUBRICA_DE_REVISAO.md`
  - `tests/test_card_check.py`
  - `tests/fixtures/card_check/`
- **As quatro matérias, medidas no `ESC-16` sobre o código entregue:**
  1. **Falso verde por descarte silencioso.** `_ITEM_HEAD_RE = re.compile(r"\d+\.\s*```")`
     (`:66`) só enxerga item cujo bloco cercado venha **imediatamente** após `N.`; item com prosa
     de abertura **não entra** na lista `heads` e portanto não é reportado. Quando **nenhum** item
     casa, o instrumento diz *"nenhum item reconhecido"* e falha (medido: `--tarefa LM-T3b` →
     **exit 1**); quando **alguns** casam, os demais somem sem uma linha sequer — que é o caso que
     o reviewer reproduziu (`Medido antes: 42` contra saída `999` → exit 0).
  2. **A norma não define onde começa o item.** A `### 8.1` diz *"o comando, em bloco cercado"* e
     não diz que ele abre o item; prosa antes é legítima pela letra, e é a forma do item 1 da
     `LM-T3b`, card que a `### 8.2` julga **"passa"**.
  3. **Recusa por substring, sobre execução sem shell.** `_METACARACTERE_RECUSADO_RE` (`:71`) varre
     a **string crua**, mas `_rodar_comando` executa `subprocess.run(tokens)` **sem `shell=True`**
     (`:136`, medido): `;`, `|` e `$` **dentro de um argumento citado** não são operadores, são
     texto. Efeito medido: os **4** itens da `LM-T2e` saem *"comando recusado"* (exit 1), e o item
     1 da `LM-T5a` também — a forma canônica do kit, `pwsh -NoProfile -Command "(Select-String …
     | Measure-Object).Count"`, é recusada por segurança que o modo de execução já garante.
  4. **O contrato de segurança não tem teste** — só a verificação em execução do reviewer.
  5. **A saída capturada vem com a codificação trocada, e isso inviabiliza baseline por texto.**
     Medido no `ESC-16`, rodando o próprio instrumento: `_rodar_comando` chama
     `subprocess.run(tokens, …, text=True)` **sem `encoding`**, de modo que o Windows decide pela
     `cp1252` e a saída chega como `tarefa: 'EX-T4' nÃ£o encontrada`. Consequência direta: **nenhum
     `Medido antes` com acento pode bater**, e o autor é empurrado a reescrever o literal da fonte
     sem acento — que é exatamente o `AE-23`, agora induzido pelo instrumento. O arquivo já tem
     `_forcar_utf8` para os próprios fluxos; falta aplicá-lo ao que ele lê do subprocesso.
- **Produto do módulo:** (a) `### 8.1` emendada: **o item começa em `N.` seguido imediatamente do
  bloco cercado**; prosa explicativa vai **depois** do `**Medido antes:**`, nunca antes do comando;
  (b) o instrumento varre `^\s*\d+\.` e **nomeia todo item numerado que não casar a forma** —
  `item N: fora da forma da 8.1 (bloco cercado não vem logo após "N.")` — e falha; **descarte
  silencioso é proibido**, e é esta metade que fecha o falso verde; (c) `_validar_comando` passa a
  decidir **por token**, depois de `shlex.split`: recusa quando um **token isolado** é operador de
  shell (`;`, `&&`, `||`, `|`, `>`, `>>`, `<`) ou começa por `$(`/crase, e **não** recusa pelo
  conteúdo de argumento citado — a justificativa é o modo de execução, e o docstring passa a
  dizê-la; (d) marcador **`**Aferição: manual**`**, na mesma linha do `**Medido antes:**`, aceito
  **somente** quando o comando é recusado por (c) ou quando o item não tem comando executável: o
  item é reportado como `manual`, **não** é executado, e continua exigindo os elementos 2 e 3. Se o
  comando **for** executável, o marcador é **rejeitado** com falha nomeada — senão vira porta dos
  fundos; (e) teste do contrato de segurança (matéria 4); (f) `_rodar_comando` decodifica a saída do
  subprocesso como **UTF-8** (`encoding="utf-8", errors="replace"`), de modo que `Medido
  antes` com acento volte a ser comparável (matéria 5).
- **Fixtures novas** (`tests/fixtures/card_check/plano-exemplo.md`, ao lado de `EX-T1`..`EX-T3`):
  `EX-T4` com item de prosa antes do bloco; `EX-T5` com `pwsh -NoProfile -Command "(… |
  Measure-Object).Count"` cujo valor bate; `EX-T6` com `**Aferição: manual**` sobre comando
  **executável**.
- **Testes** (cinco): `TF-item-numerado-fora-da-forma-e-nomeado`; `TF-token-de-shell-isolado-e-recusado`
  (e o contrato de segurança travado, matéria 4); `TR-pipe-dentro-de-argumento-citado-executa`;
  `TF-afericao-manual-sobre-comando-executavel-e-rejeitada`; `TF-saida-acentuada-do-subprocesso-e-comparavel`
  (matéria 5: comando que imprime texto acentuado, `Medido antes` com acento, tem de bater).
- **Verificação:** (forma da `### 8.1`, já na gramática que esta tarefa fixa; baselines medidas pelo
  consultor no `ESC-16`)
  1. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T4
     ```
     → **exit 1**, com a linha `item 1: fora da forma da 8.1`.
     **Medido antes: tarefa: 'EX-T4'** — **recorte** da saída de hoje
     (`card_check: FALHOU - tarefa: 'EX-T4' não encontrada em …`), não o código de saída: `exit 1`
     valeria **nos dois mundos** (antes por fixture ausente, depois por item fora da forma) e seria
     vacuoso (`DM-24`). O `card_check` confere valor não-`exit N` como **substring da saída**, então
     esta linha deixa de bater no instante em que a fixture nasce — que é o que ela precisa medir. O
     recorte **para antes do acento** por causa da matéria 5 abaixo, e volta a poder tê-lo quando
     ela fechar; cortar antes do acento é recorte do literal, não reescrita dele (`AE-23`).
  2. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T5
     ```
     → **exit 0**: `|` dentro de argumento citado deixa de ser recusa.
     **Medido antes: tarefa: 'EX-T5'** — pela mesma razão do item 1, a baseline é o
     literal da saída, não o código.
  3. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T6
     ```
     → **exit 1**, nomeando o marcador `Aferição: manual` sobre comando executável.
     **Medido antes: tarefa: 'EX-T6'** — literal da saída, pela razão do item 1.
  4. ```
     python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T1
     ```
     → **exit 0**, **inalterado**: a fixture conforme continua passando. **Medido antes: exit 0**.
  5. ```
     python -m pytest tests/ -q
     ```
     → verde, com **cinco testes a mais** que o total re-medido no despacho (`DM-23`).
     **Medido antes: 178 passed** (2026-09-19 — relação, **re-medir no despacho**, critério (xiii)).
- **Restrições desta tarefa:** a lista fechada de executáveis (`python`, `pwsh`) **não** se alarga.
  O instrumento continua **sem** `shell=True` — é essa propriedade que justifica (c), e perdê-la
  invalidaria a decisão inteira. A `### 8.2` (o julgamento dos 20 cards) fica **intocada**: o
  veredito da `LM-T3b` como *"passa"* é registro do que a rubrica dizia **naquele dia**, e
  re-julgar card é tarefa de auditoria, não desta. Nenhum card do plano é reautorado aqui
  (`DM-38` (i): normaliza-se no ato do despacho).
- **Não fazer:** não ligar o gate por conta própria — o `Status` do gate é decisão do loop,
  registrada no `DM-39` (ii); não tocar `.claude/tools/rdo.py`; não tocar os outros cards do plano;
  não commitar.
- **Contingências:**
  1. se `_rodar_comando` não estiver sem `shell=True` no despacho → parar e sinalizar `blocked`
     razão `premissa`: a premissa de (c) caiu;
  2. se a emenda à `### 8.1` tornar **qualquer** das fixtures `EX-T1`..`EX-T3` inválida → parar e
     sinalizar `blocked` razão `premissa`, citando qual: norma nova que invalida o aceite vigente é
     decisão de consultor.
- **Pronto quando:** a `### 8.1` diz onde o item começa; nenhum item numerado é descartado em
  silêncio; `|` e `;` dentro de argumento citado executam; `**Aferição: manual**` existe e é
  rejeitado sobre comando executável; saída acentuada de subprocesso é comparável; os **cinco**
  testes existem; e as cinco linhas de `Verificação` saem como escritas.

### LM-T5d — A rubrica posta em dia: a suspensão do gate e o critério do rótulo [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-17` (2026-09-19). **Fora do caminho crítico**, e
  **explicitamente não antes do marco**: existe só para que a superfície publicada não prescreva um
  gate que hoje reprova card conforme.
- **Esforço:** medium — era `low` com três produtos; o `ESC-28` acrescentou o `(xviii)` e o `ESC-31`
  o produto (e), e esforço declarado que não acompanha o produto é a mesma prosa defasada que este
  plano vem fechando.
- **Objetivo:** um só — a rubrica de autoria fica em dia com o que esta janela mediu: quem a ler
  sabe que o gate está **suspenso em efeito** e por quê, e encontra o critério do **rótulo de
  campo** que o `AE-34` custou.
- **Depende de:** `LM-T5c` (fechada — é o estado dela que a nota descreve). Nada depende desta.
- **Arquivos-alvo:**
  - `docs/RUBRICA_DE_REVISAO.md`
- **Produto do módulo:** um parágrafo datado na `### 8.1`, logo abaixo da frase do gate, com quatro
  fatos e nenhum juízo novo: (a) o gate está **suspenso em efeito desde 2026-09-19**, por decisão do
  loop endossada pelo consultor (`DM-39` (ii), `DM-40` (i)); (b) a conferência dos três elementos
  segue **manual**, como a própria seção já prescreve para o período sem instrumento; (c) **o
  vermelho do `card_check` não é evidência** enquanto o `AE-33` item 1 estiver aberto — ele produz
  **item fantasma** sobre card conforme; (d) o ponteiro: `AE-33` no `P-0740`, e a reativação do gate
  depende dele.
- **Produto (b), acrescentado pelo `ESC-18` (`DM-41`) — o critério `(xvi)` da rubrica:**
  **rótulo de campo termina na mesma linha em que começa.** Decoração no rótulo (data, `ESC-n`,
  `DM-n`, ressalva) é permitida **enquanto o `:**` couber na primeira linha**; o parser de
  campos do kit lê **linha a linha**, de modo que rótulo quebrado faz o campo **desaparecer**,
  não apenas ficar feio. Caso medido: `AE-34` — o `Pronto quando` da `LM-T4b` quebrou depois de
  `(iii) —` e `review_evidence.py` saiu **exit 1**, `campo obrigatório ausente em 'LM-T4b':
  'pronto-quando'`, com a entrega **pronta e verde**. É o décimo terceiro caso da classe e o
  **primeiro a derrubar o instrumento de evidência**, não o comando de aceite; e é o mais barato
  de todos de aferir, porque quem gera o dossiê **já falha ruidosamente** — o critério só nomeia
  a causa para quem escreve.
- **Produto (c), acrescentado pelo `ESC-19` (`DM-42` (iii)) — o critério `(xvii)` da rubrica:**
  **o aceite cobre o mundo que o próprio produto cria.** Quando o módulo **emite** uma forma, a
  `Verificação` exercita **essa** forma, e não só a que ele consome: produto que escreve num
  formato e é aferido noutro deixa o ramo que ele mesmo produz sem nenhuma linha que o discrimine.
  Caso medido: `AE-35` item 2 — a `LM-T4b` aferiu **só** o ramo em prosa; o ramo canônico
  `· data · razão — cauda`, que é exatamente o que a escrita dela emite ao transitar para
  `blocked` com `--razao`, não tinha **nenhuma** linha de aceite, e é nele que a cauda se perde
  (`AE-35` item 1). É a variação nova do critério (xii): não é alvo inalcançável, é **ramo não
  coberto** — e o décimo quarto caso da série.
- **Produto (d), acrescentado pelo `ESC-28` — o critério `(xviii)` da rubrica:** **o valor
  publicado no literal `Medido antes` é invariante ao que outras entregas movem.** Ele mede o que
  **este** card possui — exit code do comando, veredito binário, recorte do arquivo-alvo —, nunca
  um total de corpus que qualquer outra entrega desloca (total de suíte, contagem de módulo
  compartilhado, contagem de cards ou de insumos do próprio plano). Quando a pergunta é sobre
  corpus, o comando publica o **veredito** (`exit 0`, `iguais`, `1`) e o número absoluto desce para
  a prosa como referência **datada**, fora do literal. É o (x)/(xiii) levado até onde o instrumento
  o lê: a norma já dizia *relação, nunca constante*, mas a forma normativa exige o literal
  `Medido antes` e o `card_check` o compara como **substring literal** — de modo que o card
  obediente ao (xiii) era **re-congelado pelo gate**. Caso medido: `AE-49` — a baseline de suíte da
  `LM-T11` envelheceu **três vezes na mesma janela** (187, 191, 197), duas delas custando
  escalonamento ao consultor, e a `LM-T5a`, que escrevia *"Medido no `ESC-6`"* justamente para
  obedecer ao (xiii), reprovava no gate por `elemento ausente - Medido antes`.
- **Produto (e), acrescentado pelo `ESC-31` — a `## 3` reconciliada com o que a janela mediu:** a
  última frase da `## 3. Autoridade da evidência` afirma hoje que o reviewer *"não depende de
  injeção manual de contexto do orquestrador (`AE-13`)"*. Medido nesta janela: **falso em seis de
  seis revisões** — o loop injetou contexto em todo despacho de reviewer, e sem isso a atribuição
  seria ambígua. A frase **não se apaga e não se inverte**: ela está certa sobre o que fala, que é
  a marcação `da entrega`/`alheio` **por arquivo**. O que entra é um parágrafo **datado**, logo
  abaixo dela, com três fatos e nenhum juízo novo: (a) a atribuição do dossiê é **por arquivo** e
  segue dispensando injeção manual para a pergunta de **escopo**; (b) **enquanto o commit for por
  marco** (diretiva de execução do dono, 2026-09-18, item 3), o recorte `--desde <commit>` acumula
  as entregas do marco e um mesmo arquivo-alvo carrega autoria de várias tarefas — neste regime a
  injeção manual de contexto **é obrigatória** e faz parte do despacho do reviewer, não é desvio de
  quem orquestra; (c) o que suspende essa obrigação é **capacidade**, não card: atribuição por
  **hunk**. Caso medido: a diretiva do dono previu a obrigação *"até a `LM-T3` fechar a
  atribuição"*, a `LM-T3` **fechou** e a obrigação permaneceu, porque ela resolveu atribuição por
  **arquivo** e a ambiguidade é por **hunk** (`AE-55`, `AE-56`).
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'suspenso em efeito' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-33' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **≥ 1** (o ponteiro do achado). **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-34' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **≥ 1** (o critério `(xvi)` e seu caso medido). **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-35' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **≥ 1** (o critério `(xvii)` e seu caso medido). **Medido antes: 0**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'AE-49' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **≥ 1** (o critério `(xviii)` e seu caso medido). **Medido antes: 0**.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'enquanto o commit for por marco' -SimpleMatch | Measure-Object).Count"
     ```
     → **1** (o parágrafo datado da `## 3`). **Medido antes: 0**.
- **Restrições desta tarefa:** a frase do gate **não se apaga** — suspende-se em efeito, com data,
  e quem a reativa é o card que fechar o `AE-33`. A `### 8.2` fica **intocada**. Nenhum critério
  **existente** é reescrito: o `(xvi)` **entra ao lado**, como item novo da mesma tabela, e a
  frase que conta os critérios da seção fecha no mesmo ato (`DM-18` (i)) — de **quinze** para
  **dezoito**, porque o `ESC-19` acrescentou o `(xvii)` e o `ESC-28` o `(xviii)` ao mesmo card. Na
  `## 3`, a frase do `AE-13` **não se apaga nem se inverte**: o parágrafo novo entra **abaixo**
  dela e a delimita. A diretiva do dono **não** é emendada por este card — o parágrafo a **cita** e
  a aplica.
- **Não fazer:** não tocar `.claude/tools/card_check.py` (o reparo é matéria do `AE-33`, pós-marco);
  não reautorar card nenhum; não commitar.
- **Contingências:**
  1. se a frase do gate não estiver na `### 8.1` no despacho → parar e sinalizar `blocked` razão
     `premissa`, citando o que encontrou.
- **Pronto quando:** a `### 8.1` traz a nota datada; os critérios `(xvi)`, `(xvii)` e `(xviii)`
  estão na tabela com os casos `AE-34`, `AE-35` e `AE-49` nomeados e a contagem da seção fechada em
  **dezoito**; a `## 3` traz o parágrafo datado que delimita a frase do `AE-13`; as **seis** linhas
  de `Verificação` saem como escritas; e **nada além dessas duas seções** mudou no arquivo.

### LM-T4c — A fronteira entre razão e cauda no bullet de `Status` [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-19` (2026-09-19), residência única do `AE-35` item 1.
  **Declarado PÓS-MARCO**: não entra antes da `LM-T6`, por decisão registrada no `DM-42` (ii).
- **Esforço:** low
- **Objetivo:** um só — a cauda em prosa sobrevive **também** no ramo canônico, que é o que o
  próprio módulo emite ao transitar para `blocked` com `--razao`.
- **Depende de:** `LM-T4b` (fechada — é o módulo dela que esta tarefa completa). Nada depende desta.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **A causa, medida no `ESC-19` por introspeção — é de gramática, não de escrita:**
  `STATUS_BULLET_RE` (`:76`) é
  `` ^- \*\*Status:\*\* `([a-z-]+)`(?: · \d{4}-\d{2}-\d{2}(?: · (.+))?|.*?)(?: — (.+))?$ ``. O grupo
  da razão é `(.+)` **guloso** e o da cauda é opcional, de modo que **nada força a divisão no
  ` — `**. Medido sobre a linha que o próprio módulo escreve
  (`- **Status:** `blocked` · 2026-09-19 · premissa — cauda viva`): `razao='premissa — cauda viva'`
  e `cauda=None`; na transição seguinte para `ready`, `razao` vira `None` por não haver `--razao`,
  `cauda` já era `None`, e a linha sai **`- **Status:** `ready` · <hoje>`** — a prosa **some**. O
  ramo em prosa (`(2026-01-01) — cauda viva`) está **correto** e não se toca: `razao=None`,
  `cauda='cauda viva'`.
- **A fronteira, decidida aqui (era o que faltava no `DM-35` (i), e é decisão de consultor, não de
  execução):** a **razão não contém ` — `**; a **cauda começa no primeiro ` — `** da linha e vai até
  o fim. Em consequência, o grupo da razão passa a excluir o travessão (p. ex. `([^—]+?)`, com
  `strip`), e a cauda continua livre e não interpretada.
- **Produto do módulo:** (a) `STATUS_BULLET_RE` separa razão e cauda **nos dois ramos**, pela
  fronteira acima; (b) o docstring do módulo (`:21`) enuncia a fronteira com o caso medido; (c)
  nada mais muda — escrita, vocabulário, `_TRANSICOES` e forma canônica ficam como estão.
- **Testes** (dois): `TF-ramo-canonico-separa-razao-de-cauda` (a linha do caso medido devolve
  `razao='premissa'` e `cauda='cauda viva'`); `TR-round-trip-blocked-ready-preserva-a-cauda` (sobre
  cópia de fixture em `tmp_path`: `ready → blocked --razao premissa → ready`, com a cauda intacta
  no fim). *Concorrentes:* hoje o primeiro devolve a razão suja e o segundo perde a prosa.
- **Verificação:**
  1. ```
     python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog;m=backlog.STATUS_BULLET_RE.match('- **Status:** `blocked` · 2026-09-19 · premissa — cauda viva');print('razao-limpa' if m.group(2)=='premissa' and m.group(3)=='cauda viva' else 'razao-suja')"
     ```
     → **razao-limpa**. **Medido antes: razao-suja**. Saída deliberadamente **ASCII**, para não
     depender da codificação do filho (`AE-33` item 2).
  2. ```
     python -m pytest tests/test_backlog.py -q
     ```
     → verde, com **dois testes a mais** que o total re-medido no despacho (`DM-23`).
     **Medido antes: exit 0** — veredito invariante; a relação *dois a mais* é do reviewer, que
     mede o módulo antes e depois na mesma janela. Referência **datada**, e não aceite:
     `45 passed` em 2026-09-19 (`ESC-28`; era `41` na autoria, e o reparo do `AE-47` somou 4 TF ao
     mesmo módulo).
  3. ```
     python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog;from pathlib import Path;L=[l for l in Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8').splitlines() if l.startswith('- **Status:**')];print('iguais' if len(L)==sum(1 for l in L if backlog.STATUS_BULLET_RE.match(l)) else 'divergem')"
     ```
     → **iguais**, **inalterado**: a leitura dos bullets do plano não regride. **Medido antes:
     iguais** — o comando publica o **veredito**, não os dois totais: a contagem de cards do plano
     é corpus que qualquer outra entrega move (era `26 26` na autoria, é `29 29` em 2026-09-19), e
     veredito binário é invariante a ela (`ESC-28`).
- **Restrições desta tarefa:** a **escrita** não muda — `transacionar_status` já preserva a cauda
  que o leitor lhe entrega, e o defeito é do **leitor**. `_TRANSICOES`, vocabulário de estados e
  forma canônica ficam intocados. Nenhum card do plano é reescrito.
- **Não fazer:** não tocar `docs/plans/P-0739-backlog-instrumento.md` (o plano está estacionado por
  ato do dono, e esta matéria **não** é dele — `DM-42` (i)); não tocar `card_check.py`; não
  commitar.
- **Contingências:**
  1. se `STATUS_BULLET_RE` não estiver na forma citada → parar e sinalizar `blocked` razão
     `premissa`, citando a encontrada;
  2. se a `Verificação` 3 deixar de sair com os dois números iguais → **parar**: a fronteira nova
     estaria cortando bullet legítimo, e isso é decisão de consultor.
- **Pronto quando:** o ramo canônico separa razão de cauda, o round-trip `blocked → ready` preserva
  a prosa, os dois testes existem, e as três linhas de `Verificação` saem como escritas.

### LM-T4d — Regularização de superfície da aposentadoria: a citação por **nome** [Sonnet · classe mecanica]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação `escalar`. Fecha o `AE-37`: `proximo-passo` e `handover` com crase vão a **0** nas oito superfícies, e o `bootstrap-pantonic` deixa de mandar copiar skill inexistente. Pendência e dois achados roteados pelo `B1` como `AE-38`. RDO: `docs/RDO/P-0740-LM-T4d-regularizacao-de-superficie-da-aposentadoria-a-citacao-por-nome.md` — card novo do `ESC-21` (2026-09-19), residência única do `AE-37`.
  **Recomendação de ordem (a ordem é do loop, Diretiva item 4): antes da `LM-T3b`**, por urgência
  assimétrica medida — enquanto o `bootstrap-pantonic` mandar copiar skill que não existe, **todo
  projeto novo do framework nasce quebrado**, e o kit se propaga a cinco derivados.
- **Esforço:** low
- **Objetivo:** um só — nenhuma superfície viva cita **pelo nome** uma skill que a `LM-T4`
  aposentou; cada citação passa a apontar para quem herdou a responsabilidade.
- **Depende de:** `LM-T4` (fechada — é a aposentadoria dela que deixou o resíduo). Nada depende
  desta.
- **Arquivos-alvo:**
  - `.claude/skills/bootstrap-pantonic/SKILL.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
  - `.claude/global/docs/GOVERNANCA_MEMORIAS.md`
  - `GOVERNANCA.md` (**só** o item 17 da §7, e **só** o nome — ver `Restrições`)
  - `README.md` (**só** a linha 17 da tabela *Os guardrails*, e **só** o nome)
- **Fora do escopo, por decisão do `ESC-21` (`DM-44` (iii)):** `.claude/settings.json`, que traz
  `Edit(/.claude/skills/handover/**)` e `Edit(/.claude/skills/proximo-passo/**)` (linhas 5 e 6,
  medidas). É **superfície de permissão**, e regra de permissão não se altera por card: vai ao
  relatório de encerramento como **ato do dono**, junto do `DM-27` que a criou. As duas regras são
  **inócuas** — concedem `Edit` sobre diretório inexistente —, então a espera não custa nada.
- **O resíduo, medido no `ESC-21`:** citações **por nome** sobreviveram fora dos `Arquivos-alvo` da
  `LM-T4`, que varreu por **caminho** e estava certa no que media. Contagem com crase (a forma da
  citação normativa): `` `proximo-passo` `` → **5**, `` `handover` `` → **3**. As duas que importam:
  `.claude/skills/bootstrap-pantonic/SKILL.md:53` (manda **copiar** as duas para projeto novo) e
  `.claude/settings.json:5-6` (regra de permissão órfã, fora de escopo). As demais são ponteiros
  normativos em `diario-de-obras/SKILL.md` e um em `.claude/global/docs/GOVERNANCA_MEMORIAS.md:154`.
- **O mapa de sucessão — fechado aqui, para que o executor não decida nada (`DU-5`, `TK-36`):**
  - citação sobre **escolher a próxima tarefa, ler a diretiva, drenar inbox ou apurar a fila** →
    **`scrum-master`** (a `DU-5` diz, com todas as letras, que a responsabilidade da `proximo-passo`
    é **herdada pelo `scrum-master`**);
  - citação sobre **transição entre tarefas, fechamento, passagem de bastão ou herança de contexto**
    → **`passagem-de-bastao`**;
  - **a palavra** *handover* em prosa (`handover ao dono`, `handover de execução`) **não é citação
    de skill e não se toca** — é exatamente o eixo que o `AE-37` nomeia: nome ≠ palavra.
- **Passos:**
  1. `bootstrap-pantonic/SKILL.md:53`: na lista de skills a copiar, **remover** `proximo-passo` e
     `handover` e **acrescentar** `passagem-de-bastao`.
  2. `diario-de-obras/SKILL.md` e `.claude/global/docs/GOVERNANCA_MEMORIAS.md`: reapontar cada
     citação com crase pelo **mapa de sucessão** acima. Citação que **não** couber em nenhuma das
     duas regras do mapa → **parar** e sinalizar `blocked` razão `premissa`, citando a linha: o mapa
     é fechado, e ampliá-lo é decisão de consultor.
  3. `GOVERNANCA.md` §7 item 17 e a linha 17 da tabela *Os guardrails* do `README.md`: trocar
     **apenas o nome da skill** citada, pelo mapa. Nada mais desses dois itens muda.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md -Pattern 'proximo-passo' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md -Pattern 'passagem-de-bastao' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md,.claude/skills/diario-de-obras/SKILL.md,.claude/global/docs/GOVERNANCA_MEMORIAS.md,GOVERNANCA.md,README.md,docs/DOC_MAP.md,.claude/README.md,.claude/skills/scrum-master/SKILL.md -Pattern '`proximo-passo`' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 5**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md,.claude/skills/diario-de-obras/SKILL.md,.claude/global/docs/GOVERNANCA_MEMORIAS.md,GOVERNANCA.md,README.md,docs/DOC_MAP.md,.claude/README.md,.claude/skills/scrum-master/SKILL.md -Pattern '`handover`' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 3**.
  5. ```
     pwsh -NoProfile -Command ".claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0**, **inalterado** — guarda de regressão: trocar o **nome** citado na linha 17 não
     pode mexer na contagem de guardrails que a `LM-T4` fechou em 19. **Medido antes: exit 0**
     (o valor vai **sem ponto final** dentro do negrito: `exit 0.` seria lido como texto e não como
     código de saída — defeito meu, pego pelo `card_check` no `ESC-21`).
- **Restrições desta tarefa:** o **item 17** (`G-REPLAN`) tem **só o nome da skill** trocado — a
  substância dele continua fechada (`DM-12`, e é a proibição que a `LM-T4` respeitou corretamente);
  esta autorização é **estreita e explícita**, e é o `DM-33` (ii) aplicado de novo: o que colide com
  proibição vira **passo autorizado**, nunca improviso do executor. A palavra *handover* em prosa
  **não** se toca. `.claude/settings.json` **não** se toca (ato do dono). Nenhuma skill é criada,
  apagada ou renomeada aqui.
- **Não fazer:** não editar `.claude/settings.json`; não reabrir a substância do `G-REPLAN`; não
  tocar `.claude/agents/` (`DM-17`); não regenerar projeção (a contagem de skills não muda); não
  commitar.
- **Contingências:**
  1. citação que não couber no mapa de sucessão → `blocked` razão `premissa`, com a linha citada;
  2. se a `Verificação` 5 sair diferente de 0 → seguir com a entrega e devolver
     `contingência 2 acionada: check-readme exit <n>` — a contagem de guardrails é da `LM-T4`, não
     desta tarefa.
- **Pronto quando:** o `bootstrap-pantonic` copia `passagem-de-bastao` e não cita as aposentadas;
  nenhuma das oito superfícies varridas cita `` `proximo-passo` `` ou `` `handover` ``; o item 17
  cita a skill certa; e as cinco linhas de `Verificação` saem como escritas.

### LM-T6 — Piloto medido do loop e o veredito do dono [Opus + dono · classe investigacao]

- **Status:** `done` (2026-09-19) — **O MARCO FECHOU.** Veredito do dono **APROVADO**, e o gate
  independente confirmou: **aprovado 100%**, bloqueante `nenhuma`, recomendação `escalar`,
  pendência roteada pelo `B1` como `AE-46`. RDO:
  `docs/RDO/P-0740-LM-T6-piloto-medido-do-loop-e-o-veredito-do-dono.md`; laudo consumido e apagado.
  Fechou em duas etapas e um redespacho de re-derivação (`AE-43`), que provou que a série
  duplicada **não** havia contaminado o total. Reescrita para o veículo (B) pelo consultor (`DM-47`). **Medida publicada em 2026-09-19; o veredito do dono veio no mesmo dia**
  (`blocked` razão `dependencia`, Contingência 3 do card): 21 módulos em 4 janelas, total
  **3.712,8k tk / 1.098 tool uses / 11.147,7 s**, com o confronto contra a baseline da `BKL-T4`
  em **-37,9% tk, -26,3% tool uses, -57,9% duração**; as 9 linhas de `Verificação` batem
  (1,1,1,1,1,1,1, exit 0, exit 0) e a divergência com o corpus está registrada pela Contingência
  2. A linha `**Veredito do dono:**` fica **vazia** — nem o executor nem o loop a escrevem.
  Despachável **sem** esperar tarefa nenhuma: o corpus está fechado e medido.

> **Veículo fixado em (B) por ato do dono** (`DM-45` (i), 2026-09-19), **card reescrito pelo
> consultor** por ordem de fila do `scrum-master` no mesmo dia (`DM-47`). O `ESC-17` havia
> declarado este card **não despachável** porque o `Entregável` mandava rodar o loop sobre a fila
> de módulos do `P-0739` e o `Pronto quando` exigia aquele plano em `done` — duas coisas que o ato
> do dono de 2026-09-19 tornou impossíveis: o `P-0739` **segue estacionado** e não retorna enquanto
> o `P-0740` não encerrar. O impedimento está **resolvido**: o piloto muda de **veículo**, não de
> propósito. O corpus passa a ser a execução deste plano sob o loop — já medida, já fechada —, e o
> produto continua sendo o mesmo de sempre: **a medida do loop e o veredito do dono**. O texto do
> `ESC-17` fica no `AE-` correspondente como registro; este card não o repete.

- **Esforço:** high
- **Objetivo:** a **medida** do loop de módulos e o **veredito do dono** sobre ela. Um tema só: o
  piloto responde, com número medido, se o objetivo que o dono abriu em 2026-08-22 foi atingido —
  se o loop fecha módulo sozinho e a que custo. Absorve `AUT-T9` (conformidade) e `AUT-T10`
  (`README`, `CHANGELOG`, veredito).
- **Corpus (fechado, e é o veículo (B)):** a execução do **próprio `P-0740`** sob o loop, não a de
  outro plano. Duas janelas, as duas medidas: a de **2026-09-18/19** (11 tarefas fechadas, **7** em
  `aprovado 100%`, **zero** reprovações, **zero** retentativas consumidas, 39 linhas de
  `docs/telemetria.tsv`, **6.004,3k tk**, **900** tool uses, **3,06 h**, com o consumo decomposto em
  execução `1.389,9k` (23%), revisão `812,2k` (14%) e consultor `3.802,2k` (63%) — `DM-45` (i)) e a
  janela **corrente**, cuja fatia se re-mede no despacho pelo comando do *Método de sondagem*. O
  `P-0739` **não** entra: segue estacionado por ato do dono, e nada nesta tarefa o desestaciona.
- **Entregável:** uma seção nova no próprio plano, `docs/plans/P-0740-loop-de-modulos.md` — nível
  2, numerada **10**, com o título *O piloto medido — a série do loop sobre o próprio plano* —,
  contendo, nesta ordem: **(a)** a **série por módulo**, uma tabela com as colunas, nesta ordem,
  `módulo`, `tokens_k`, `tool_uses`, `duracao_s` e `janela`, com **uma linha por módulo fechado** e
  uma última linha de total, rotulada `total do piloto` em negrito; **(b)** a linha rotulada
  `Decomposição por papel:` em negrito, com os três valores e os três percentuais — execução,
  revisão e consultor —, que é o número que a janela anterior produziu e que nenhuma baseline
  antiga tinha; **(c)** a linha rotulada `Contra a baseline de tarefa atômica:` em negrito,
  confrontando o custo por módulo desta série com os `284,6k tk / 71 tool uses / 21 min` por tarefa
  atômica da `BKL-T4` (§3 deste plano), dizendo em quanto o módulo coeso ficou acima ou abaixo;
  **(d)** o **número de módulos fechados por janela** e a **regra que encerrou cada janela**, com o
  fato que a disparou; **(e)** a linha rotulada `Veredito do dono:` em negrito, que o dono preenche
  — é dele, e não de quem executa nem de quem orquestra. Mais uma linha em `CHANGELOG.md` sob
  `## [Não lançado]`, com o literal fechado abaixo.
- **Texto literal da linha do `CHANGELOG.md`** (transcrição, não autoria):
  ```
  - Piloto do loop de módulos medido sobre a execução do próprio `P-0740` (veículo (B), decisão do
    dono de 2026-09-19): a série por módulo, a decomposição de consumo por papel e o confronto com
    a baseline de tarefa atômica da `BKL-T4` ficam publicados na seção 10 do plano, com o veredito
    do dono.
  ```
- **Método de sondagem:** (corpus fechado acima; nenhum dado bruto entra em contexto — só os
  agregados abaixo)
  1. **Re-medir a fatia da janela corrente** antes de compor a série, porque ela cresce enquanto o
     plano roda (`DM-23`): `pwsh -NoProfile -Command "(Select-String -Path docs/telemetria.tsv
     -Pattern 'PantonicApp\tLM-T' | Measure-Object).Count"` — **50** em 2026-09-19, **referência
     histórica, não aceite**: o número que vale é o que o comando devolver no despacho.
  2. **Fonte de cada número:** `docs/telemetria.tsv` para consumo, tool uses e duração; o bullet de
     `- **Status:**` de cada card para veredito e percentual; `docs/RDO/` para a regra de parada de
     cada janela. **Nada se estima e nada se lembra** — número sem linha de origem não entra.
  3. **Teto do agregado:** a seção inteira cabe em **60 linhas**. Se a série não couber, corta-se
     detalhe por módulo, nunca a decomposição por papel nem o confronto com a baseline — são eles
     que respondem a pergunta do dono.
- **Restrições desta tarefa:** a relação *uma linha de tabela por módulo fechado* é **declarada,
  não prometida como teste** (`DM-21` (ii)(c)): o total de módulos muda a cada despacho e nenhuma
  constante o aferiria sem envelhecer (`DM-23`). Quem confere a cobertura linha a linha é a
  revisão, contra a saída do comando do *Método de sondagem* 1. O `README.md` entra como **guarda
  de regressão, não como edição**: nada nele muda aqui, e as verificações 8 e 9 provam que ele
  segue coerente com o disco.
- **Não fazer:** não desestacionar o `P-0739` nem tocar `docs/plans/P-0739-backlog-instrumento.md`
  — o estacionamento é ato do dono e esta tarefa não o desfaz; não rodar o loop sobre plano nenhum
  para "gerar corpus" (o corpus já existe e está medido); não escrever o veredito no lugar do dono;
  não estimar número que a telemetria não tenha; não editar `README.md`; não commitar.
- **Contingências:**
  1. se algum módulo fechado **não** tiver linha em `docs/telemetria.tsv` → **seguir com a série**,
     marcando a célula com `sem linha de telemetria` e registrando o módulo na seção: buraco de
     instrumento é fato do piloto, não impedimento dele;
  2. se a soma da série divergir do total declarado no corpus acima → **seguir com o medido agora**
     e registrar as duas somas lado a lado: quem manda é a medida do despacho, e a divergência é
     insumo, não erro a esconder;
  3. se o dono não estiver disponível para o veredito no mesmo despacho → parar e sinalizar
     `blocked` razão `dependencia`, com a seção **já publicada** e só a linha do veredito vazia: a
     medida fecha sem ele, o veredito não.
- **Verificação:** (forma normativa do bloco `Verificação`, publicada em
  `docs/RUBRICA_DE_REVISAO.md` pela `LM-T5`. Todo valor abaixo foi rodado no ato da reescrita,
  2026-09-19. As linhas 1 a 6 usam **regex ancorada em `^`** — deliberada e rodada (`DM-24` (ii)):
  a âncora faz o padrão casar **só** a linha real da seção entregue, e não a própria linha de
  comando, que vive neste mesmo plano indentada; sem a âncora, todo padrão contaria a si mesmo. As
  linhas 8 e 9 são **guarda de regressão, não discriminante**, e estão
  declaradas como tal.)
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^## 10\. O piloto medido' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A seção existe, no nível e com o título prescritos.)
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^\| módulo \| tokens_k \| tool_uses \| duracao_s \| janela \|' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A tabela da série existe, com as cinco colunas na ordem
     prescrita.)
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^\| \*\*total do piloto\*\* \|' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A tabela fecha em total — sem ele a série é lista, não medida.)
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^\*\*Decomposição por papel:\*\*' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (O número novo da janela anterior — execução, revisão,
     consultor — está publicado.)
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^\*\*Contra a baseline de tarefa atômica:\*\*' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (O confronto com os `284,6k tk / 71 tool uses / 21 min` da
     `BKL-T4` está publicado — é ele que responde se o módulo coeso ganhou ou perdeu.)
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^\*\*Veredito do dono:\*\*' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A linha do veredito existe. O **conteúdo** dela é do dono, e a
     `Contingência` 3 diz o que fazer se ele não estiver na janela.)
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'Piloto do loop de módulos medido sobre a execução do próprio' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A linha do `CHANGELOG.md`, no literal transcrito acima.)
  8. ```
     pwsh -NoProfile -Command ".claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0**. **Medido antes: exit 0** (2026-09-19). Regressão, não discriminante: nada de
     `README.md` muda nesta tarefa, e esta linha existe para provar que continua assim.
  9. ```
     pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0**. **Medido antes: exit 0** (2026-09-19). Regressão, não discriminante: a tarefa
     não toca definição de agente nem skill, então a projeção não se move.
- **Depende de:** `LM-T1`, `LM-T2`, `LM-T3`, `LM-T4`, `LM-T5` — **todas fechadas**. Nenhuma tarefa
  aberta a bloqueia: o corpus do veículo (B) está fechado e medido, e módulo que fechar depois
  entra na série pela re-medida do *Método de sondagem* 1, no despacho. O `P-0739` **não** é
  dependência desta tarefa e não volta a ser.
- **Pronto quando:** (o fato que tem de existir ao final, `classe investigacao`) existe, no plano,
  a seção **10** com a série por módulo somada em total, a decomposição de consumo por papel, o
  confronto explícito com a baseline de tarefa atômica da `BKL-T4` e o número de módulos fechados
  por janela com a regra que encerrou cada uma — **todos com a linha de origem** —, mais a linha do
  `CHANGELOG.md`; e a linha do **veredito do dono** está preenchida por ele. Desfecho negativo é
  desfecho: se a medida disser que o loop **não** atingiu o objetivo de 2026-08-22, isso é o
  resultado do piloto e se publica como tal.

### LM-T7 — As duas projeções canônicas do kit [Sonnet · classe mecanica]

- **Status:** `done` — fechada em 2026-09-18, **ressalva 90%**, bloqueante `nenhuma`, recomendação `escalar` (RDO `docs/RDO/P-0740-LM-T7-as-duas-projecoes-canonicas-do-kit.md`; laudo consumido e apagado, `DP-H`). Pendência roteada como `AE-12`. **Reescrita pelo `ESC-1` (2026-09-18)**: o card cobria também a concessão de
  `Bash` ao `pantonic-planner`, e esse passo é inexecutável por qualquer agente desta sessão
  (`AE-11`). A parte de definição de agente saiu para a `LM-T8`, pendente de ato do dono; o que
  ficou aqui está **despachável agora** e não depende dela (`DM-17` (iii)).
- **Esforço:** low
- **Objetivo:** pôr as duas projeções versionadas do kit em dia com as definições de agente que já
  estão em disco. Um tema só, mecânico: **a projeção**, nunca a definição. As duas estão vermelhas
  hoje por atos do dono fora de ciclo de tarefa — `DM-8` reescreveu as descrições de executor e
  reviewer, e o `pantonic-consultant` foi criado em 2026-09-18.
- **Depende de:** `DM-16` (iv) e `DM-17`. Nenhuma tarefa anterior. **Precede a `LM-T4`:** a
  `Verificação` 1 da `LM-T4` exige `check-drift` exit 0, que hoje sai **exit 1**; quem o recoloca
  em 0 é o passo 2 desta tarefa — e só ele, medido na `RP-5`.
- **Arquivos-alvo:**
  - `.claude/README.md`
  - `README.md`
  - `CHANGELOG.md`
- **Produto do módulo:** (a) a linha do `pantonic-consultant` na tabela **Agentes** de `README.md` ›
  *Anatomia do kit*, que é escrita à mão e não é gerada; (b) `.claude/README.md` regenerado **pelo
  instrumento**, nunca à mão; (c) uma linha em `CHANGELOG.md` sob `## [Não lançado]`.
- **Passos, com os textos literais** (transcrever; não reescrever com outras palavras):
  1. Em `README.md`, na tabela **Agentes** da seção *Anatomia do kit*, inserir **imediatamente
     antes** da linha que começa com `| ` + crase + `pantonic-scout` (âncora medida na `ESC-1`:
     uma única ocorrência no arquivo) a linha:
     ```
     | `pantonic-consultant` | Opus | Consultor de **um** plano em execução: instanciado uma vez, mantido de standby com o cenário inteiro e acionado a cada escalonamento para desbloquear impedimento de executor e reparar o modelo funcional do plano. Não implementa entrega, não julga e não commita. |
     ```
  2. Regenerar a projeção do kit pelo instrumento, sem editar a região marcada à mão:
     `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode generate; exit $LASTEXITCODE"`
     → exit 0, com a saída medida `kit_check: generate OK - README.md regenerado: 9 agente(s),
     11 skill(s).` O efeito medido no arquivo foi de **3 inserções e 2 remoções** em
     `.claude/README.md`.
  3. Em `CHANGELOG.md`, como primeiro item da seção `## [Não lançado]`:
     ```
     - Projeções canônicas do kit em dia com as definições de agente em disco: `.claude/README.md`
       regenerado por `kit_check -Mode generate` e a tabela de Agentes de `README.md` passa a listar
       o `pantonic-consultant`. `check-drift` e `check-readme.ps1` voltam a exit 0.
     ```
- **Verificação:** (toda linha foi **rodada** na `RP-5` e na `ESC-1`, com a saída de antes **e** a de
  depois medidas; nenhuma é deduzida — `DM-12`)
  1. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"`
     → **exit 0**. **Antes (medido):** exit **1**, `kit_check: check-drift FALHOU (6 problema(s))`,
     com `README.md diverge do regenerado (5 linha(s) diferente(s))`. Medido também que o passo 2
     sozinho leva este comando a exit 0, com a saída `kit_check: check-drift OK - .claude/README.md
     == regenerado (9 agente(s), 11 skill(s)); materializacao do alvo 'projeto' == canonico.`
  2. `pwsh -NoProfile -Command "& .claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"`
     → **exit 0**. **Antes (medido):** exit **1**, `check-readme: FALHOU (1 problema(s))` —
     `Agente 'pantonic-consultant' (.claude/agents/pantonic-consultant.md) não aparece na tabela de
     Agentes de 'Anatomia do kit'.` **Depois, medido na `ESC-1` com a linha do passo 1 inserida e
     revertida no mesmo ato:** exit 0, `check-readme: OK - 9 agente(s), 11 skill(s), 18
     guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.`
  3. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode validate | Out-Null; exit $LASTEXITCODE"`
     → **exit 0**, inalterado (medido antes: exit 0, `kit_check: OK - 9 agente(s), 11 skill(s) e 21
     entrada(s) canonica(s) validados; VERSION == KIT_VERSION ('0.0.0')`).
  4. Efeito nos dois arquivos-alvo, com baseline medida na `ESC-1` (**zero** ocorrências de
     `pantonic-consultant` em cada um deles hoje):
     `pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'pantonic-consultant' -SimpleMatch | Measure-Object).Count"`
     → ≥ 1, e o mesmo comando sobre `.claude/README.md` → ≥ 1.
  5. `python -m pytest tests/ -q` → verde, piso ≥ **145** (medido: `145 passed`). Esta tarefa não
     acrescenta teste; o piso tranca a suíte de conformance contra edição de doutrina.
- **Restrições desta tarefa:** `.claude/README.md` só muda **pelo passo 2** — editar a região
  marcada à mão faz o `check-drift` divergir de novo na regeneração seguinte. A tabela de
  `README.md` é **outra** superfície, não gerada: ali a linha se escreve à mão, com o literal do
  passo 1. **Nenhum arquivo de `.claude/agents/` é tocado** (`DM-17` (ii)): esta tarefa projeta o
  que já está lá e não altera definição de agente nenhuma.
- **Não fazer:** não editar `.claude/agents/pantonic-planner.md` nem qualquer outro arquivo de
  `.claude/agents/` — a edição é negada pela camada de permissão do harness e contorná-la por
  `Write`/`Bash` é proibido (`AE-11`, `DM-17`); se o passo 2 alterar algo fora das regiões marcadas,
  parar. Não publicar `DM-2`..`DM-5` em doutrina (é a `LM-T4`); não tocar `GOVERNANCA.md`, skill
  nenhuma nem instrumento de `.claude/tools/`; não rodar `python .claude/tools/backlog.py check`
  nem tratá-lo como aceite (`AE-1`); não commitar (commit é ato do loop, no marco de validação).
- **Contingências:**
  1. se a tabela **Agentes** de `README.md` já contiver uma linha `pantonic-consultant` → não
     duplicar: seguir para o passo 2 e devolver `contingência 1 acionada: linha já existia`;
  2. se, depois do passo 2, o `check-drift` continuar exit 1 por problema que **não** seja
     divergência de tabela de agentes/skills (ex.: materialização do alvo `projeto`) → seguir com a
     entrega e devolver `contingência 2 acionada: <o problema que restou>`;
  3. se o `check-readme.ps1` apontar problema **adicional** ao do `pantonic-consultant` → seguir com
     a entrega, corrigir só o do consultor e devolver `contingência 3 acionada: <problema
     remanescente>`.
- **Pronto quando:** a tabela **Agentes** de `README.md` lista o `pantonic-consultant`;
  `.claude/README.md` está regenerado pelo instrumento; `CHANGELOG.md` traz a linha sob
  `## [Não lançado]`; e as cinco linhas de `Verificação` saem como escritas — em especial
  `check-drift` e `check-readme.ps1` em **exit 0**, que hoje saem 1.

### LM-T7a — O invariante de contagem da seção *Anatomia do kit* [Sonnet · classe implementacao]

- **Status:** `done` — fechada em 2026-09-18, **aprovada 100%**, bloqueante `nenhuma`, recomendação `seguir` (RDO `docs/RDO/P-0740-LM-T7a-o-invariante-de-contagem-da-secao-anatomia-do-kit.md`; laudo consumido e apagado, `DP-H`). O `AE-12` fecha aqui. Aberta pelo `ESC-2` (2026-09-18) sobre o `AE-12`; residência única do reparo.
  A `LM-T7` **não** se refaz: ela entregou o que o card mandava, e o card é que não mandou fechar a
  frase que conta a tabela.
- **Esforço:** low
- **Objetivo:** um só — a prosa que **conta** a tabela de *Anatomia do kit* passa a ser conferida
  pelo mesmo guarda que confere a tabela. Enquanto o invariante não estiver no instrumento, o verde
  dele é falso conforto: hoje o script **anuncia** `9 agente(s)` e sai exit 0 com o README dizendo
  "oito agentes" duas linhas acima da tabela de nove.
- **Depende de:** `DM-18`; a `LM-T7` fechada (a nona linha da tabela é entrega dela). Nenhuma outra
  tarefa, e nenhuma outra depende desta.
- **Arquivos-alvo:**
  - `README.md`
  - `.claude/checks/check-readme.ps1`
- **Produto do módulo:** (a) `check-readme.ps1` ganha a **checagem 5** — a frase de contagem da
  seção *Anatomia do kit* tem de declarar o mesmo número de **agentes** e de **skills** que o script
  já conta do disco; (b) a frase corrigida em `README.md`.
- **Fatos medidos no `ESC-2` (2026-09-18), que são a baseline desta tarefa:**
  - `README.md:760`, literal, ocorrência **única** de `O kit são` no arquivo:
    `O kit são oito agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,`
  - disco: **9** arquivos em `.claude/agents/*.md`, **11** diretórios em `.claude/skills/`,
    **4** executáveis em `.claude/checks/`;
  - `check-readme.ps1` → **exit 0**, com
    `check-readme: OK - 9 agente(s), 11 skill(s), 18 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.`
    — isto é, o script **já calcula** `$agentCount` e `$skillCount` (`:230`) e não os confronta com a
    prosa. Nenhuma contagem nova se inventa nesta tarefa;
  - `README.md` **não** tem região marcada (`<!-- kit:agents:begin -->` só existe em
    `.claude/README.md`): a linha 760 é escrita à mão e **não** é regenerada por `kit_check`.
- **Gramática da checagem 5** (residência única do literal nesta tarefa): dentro da seção
  `## <N>. Anatomia do kit`, a **primeira** linha que começa com `O kit são ` é a frase de contagem;
  dela se extraem o token imediatamente anterior a ` agentes` e o imediatamente anterior a
  ` skills`. Cada token vale como número se for **dígito** ou se estiver no mapa por extenso de
  `zero` a `vinte`; token fora disso é erro nomeado, nunca silêncio.
- **Textos literais das três mensagens de erro** (o `<N>` é o que a prosa declara, o `<M>` é o que o
  disco tem):
  ```
  Divergência na contagem de agentes: a frase de 'Anatomia do kit' declara <N> vs <M> agente(s) em .claude/agents/.
  Divergência na contagem de skills: a frase de 'Anatomia do kit' declara <N> vs <M> skill(s) em .claude/skills/.
  Frase de contagem de 'Anatomia do kit' ausente ou com numeral fora do vocabulário (dígito ou por extenso até vinte): '<token>'.
  ```
- **Passos — a ordem é o que produz a evidência, e não se inverte:**
  1. Implementar a checagem 5 em `.claude/checks/check-readme.ps1`, no mesmo idioma das quatro
     existentes (acumular em `$errors`, nunca `exit` no meio), com o mapa de numerais e as três
     mensagens literais acima.
  2. Rodar o guarda **com a prosa ainda velha**:
     `pwsh -NoProfile -Command "& .claude/checks/check-readme.ps1; exit $LASTEXITCODE"` → tem de sair
     **exit 1** com a primeira mensagem, na forma `declara 8 vs 9 agente(s)`. Registrar a saída na
     linha de retorno da entrega. **É este passo que prova que a checagem discrimina** — e ele só
     existe porque a correção da prosa vem depois.
  3. Só então corrigir `README.md:760`, trocando **uma** palavra:
     ```
     O kit são nove agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,
     ```
- **Verificação:** (o "antes" de cada linha foi **rodado** no `ESC-2`; o item 2 é a saída que o
  passo 2 desta tarefa produz — `DM-12`)
  1. `pwsh -NoProfile -Command "& .claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"`
     → exit 0. **Antes (medido):** exit 0 **também** — o exit code, sozinho, não discrimina nada
     aqui; quem discrimina é o item 2.
  2. A saída do passo 2 (guarda pronto, prosa velha) foi **exit 1** com
     `Divergência na contagem de agentes: a frase de 'Anatomia do kit' declara 8 vs 9 agente(s) em .claude/agents/.`
     Se esse passo sair exit 0, a checagem **não** está discriminando: contingência 2.
  3. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"`
     → exit 0, regressão (medido no `ESC-2`, depois da `LM-T7`: exit 0).
  4. `python -m pytest tests/ -q` → verde, piso ≥ **145** (medido: `145 passed`). Esta tarefa não
     acrescenta teste `pytest`: não há harness de `pytest` para os `.ps1` do kit (medido: nenhum
     arquivo de `tests/` invoca `pwsh`), e inventar um é outro tema.
  5. `pwsh -NoProfile -Command "Select-String -Path README.md -Pattern 'O kit são' -SimpleMatch"`
     → uma linha, com `nove agentes`. **Antes (medido):** `README.md:760:O kit são oito agentes,
     onze skills, quatro verificadores executáveis e a declaração de projeções,`.
- **Restrições desta tarefa:** a checagem 5 acumula em `$errors` como as outras quatro — o script
  tem de continuar reportando **todos** os problemas numa passada. A frase corrigida muda **uma**
  palavra: `oito` → `nove`; nada mais da linha se reescreve. `README.md` não é gerado — não rodar
  `kit_check -Mode generate` aqui.
- **Não fazer:** não estender a checagem a "verificadores executáveis" nem à "declaração de
  projeções" — o script **não conta** nenhum dos dois hoje, e autorar a contagem sem fato medido é o
  defeito que a `RP-1` já pagou; fica fora do escopo, nominalmente (`DM-18` (v)). Não tocar
  `.claude/agents/` (`DM-17`), `.claude/README.md` (é gerado, e a `LM-T7` já o regenerou),
  `GOVERNANCA.md` (a contagem de guardrails já tem a checagem 4) nem instrumento de
  `.claude/tools/`. Não commitar.
- **Contingências:**
  1. se `README.md:760` não for o literal transcrito acima → parar e sinalizar `blocked` razão
     `premissa`, citando a linha encontrada;
  2. se o passo 2 sair **exit 0** → a checagem não discrimina; corrigir a implementação e repetir o
     passo 2 antes de tocar a prosa. Se persistir depois de uma correção, parar e devolver
     `blocked` razão `premissa` com a saída obtida;
  3. se `python -m pytest tests/ -q` ficar vermelho em qualquer teste → seguir com a entrega e
     devolver `contingência 3 acionada: <arquivo::teste> vermelho fora dos alvos` (esta tarefa não
     toca Python nenhum).
- **Pronto quando:** `check-readme.ps1` tem a checagem 5 com as três mensagens literais; a saída do
  passo 2 (exit 1, `declara 8 vs 9`) está registrada na linha de retorno; `README.md:760` declara
  `nove agentes`; e as cinco linhas de `Verificação` saem como escritas.

### LM-T8 — A concessão de `Bash` ao `pantonic-planner` e a publicação na definição dele [Sonnet · classe mecanica]

- **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma`, recomendação
  `escalar`, pendência roteada pelo `B1` como `AE-45`. Os dez literais entraram na primeira passada
  e as **doze** linhas de `Verificação` saíram nos valores declarados (`1,1,0,0,2,0,1,5,1,1,
  exit 0, exit 0`), com diff de 70 inserções / 11 remoções e line endings intactos. A entrega saiu
  pela **orquestração**, por ato do dono, depois de três recusas ao executor — circunstância
  registrada no `AE-44`, exceção nomeada e **não-precedente**; a revisão foi independente. Dois
  achados de processo do laudo, ambos com rota para a fila pós-marco: a `description` do
  frontmatter segue falsa sob a concessão (congelada pelo `Não fazer` do card, e movê-la reabre
  `check-drift` — fecha junto com a `LM-T7`), e a ausência de rota fechada para tarefa que edite
  `.claude/agents/**`. RDO:
  `docs/RDO/P-0740-LM-T8-a-concessao-de-bash-ao-pantonic-planner-e-a-publicacao-na-de.md`; laudo
  consumido e apagado. Reparada antes disso pelo `ESC-23` (`DM-46`), depois do `blocked`
  `premissa` do `AE-41`. O item (b) ganhou **local** e **literal** nos quatro pontos do arquivo; a
  `Verificação` passou a discriminar bloco a bloco, com os dois valores rodados; e o item (a)
  absorveu as **três** frases do mesmo arquivo que a concessão de `Bash` torna falsas (`DM-46`
  (iii)). Com a `LM-T4` fechada, os três itens são executáveis no **mesmo** despacho — acabou o
  defeito de *"dois estados de executabilidade"* que a `### 8.2` da rubrica marcou neste card.
  Modelo rebaixado de `Opus + dono` para `Sonnet` no mesmo ato: o ato do dono foi feito (`DM-27`)
  e o que sobrou é **transcrição**.
- **Esforço:** low
- **Objetivo:** materializar a decisão do dono (`DM-16`) na única superfície onde ela mora — o
  arquivo de definição do `pantonic-planner` — e publicar ali a doutrina que a `LM-T4` fixou. Um
  tema só: **a definição de agente**.
- **Depende de:** nada. A permissão foi concedida pelo dono em 2026-09-19 (`DM-27`) e a `LM-T4`
  fechou em 2026-09-19.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
  - `CHANGELOG.md`
- **Produto do módulo:** (a) o frontmatter do planner com `Bash`, o fato estável correspondente no
  corpo e as **três** frases do mesmo arquivo que a concessão torna falsas, reescritas no mesmo ato
  (`DM-18` (i), `DM-46` (iii)); (b) a doutrina da `LM-T4` publicada em **quatro** pontos nomeados
  do mesmo arquivo — gramática de cabeçalho (dois pontos), régua de tema (item 5 da Fase 4) e os
  cinco critérios de autoria (item 12, novo, da Fase 4); (c) uma linha em `CHANGELOG.md` sob
  `## [Não lançado]`.
- **Passos:** aplicar, na ordem, as dez substituições literais abaixo. Cada uma traz o trecho **de**
  (texto exato que está no arquivo hoje, conferido no `ESC-23`, ocorrência **única**) e o trecho
  **para**. Nenhuma exige escolher local, redigir frase ou decidir coisa alguma.
- **Textos literais:** (transcrição, não autoria)

  **1. Frontmatter, linha 5 de `.claude/agents/pantonic-planner.md`.** De:
  ```
  tools: Read, Glob, Grep, Write, Edit
  ```
  Para:
  ```
  tools: Read, Glob, Grep, Write, Edit, Bash
  ```

  **2. Parágrafo de abertura do corpo** (a concessão torna falsa a frase "não roda comando e não
  mede"). De:
  ```
  Você roda no modelo mais caro e o seu contexto é o ativo mais escasso da sessão. Você **não lê
  codebase para se situar, não roda comando e não mede**: fatos entram como dossiê do
  `pantonic-scout` ou como resultado de tarefa de investigação executada por outro papel. Sua
  única matéria-prima é decisão; seu único produto é plano fechado.
  ```
  Para:
  ```
  Você roda no modelo mais caro e o seu contexto é o ativo mais escasso da sessão. Você **não lê
  codebase para se situar e não sonda**: fatos entram como dossiê do
  `pantonic-scout` ou como resultado de tarefa de investigação executada por outro papel. Sua
  única matéria-prima é decisão; seu único produto é plano fechado. Você **tem `Bash`**, e ele
  serve a **um** uso: rodar o comando de aceite que você mesmo vai publicar num card, antes de
  publicá-lo — não é licença para levantamento próprio.
  ```

  **3. Último bullet da lista de `## Fatos estáveis (não redescobrir)`** — acrescentar logo depois
  do bullet `- Plano novo: …`, que hoje encerra a lista. De:
  ```
  - Plano novo: `docs/plans/P-NNNN-<slug>.md` + uma linha em `docs/plans/_INBOX.md`; `NNNN` = id
    declarado no cabeçalho do inbox; data de origem no cabeçalho do plano, nunca no nome.
  ```
  Para:
  ```
  - Plano novo: `docs/plans/P-NNNN-<slug>.md` + uma linha em `docs/plans/_INBOX.md`; `NNNN` = id
    declarado no cabeçalho do inbox; data de origem no cabeçalho do plano, nunca no nome.
  - Ferramenta de execução: você **tem** `Bash` (decisão do dono, 2026-09-18 — planner e
    executor acessam a mesma ferramenta de validação). Comando de aceite que você escreve num
    card **se roda antes de publicar**, e o literal esperado é a saída **medida**, nunca a
    deduzida da ferramenta: `Verificação` publicada sem execução é defeito de autoria.
  ```

  **4. Bullet da gramática de cabeçalho, em `## Fatos estáveis (não redescobrir)`** — o primeiro
  dos dois pontos que enunciam a forma aposentada. De:
  ```
  - Cabeçalho de tarefa: `### <ID> — <título> [<modelo> · classe <classe>]`, com `<modelo>` ∈
    `Opus|Sonnet|Haiku` e `<classe>` ∈ `mecanica|implementacao|comportamental|investigacao|redacao`
    (gramática lida por `.claude/tools/rdo.py` e `review_evidence.py`). Nenhum teto se escreve no
    card: a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel.
  ```
  Para:
  ```
  - Cabeçalho de tarefa: `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe
    <classe>[ · teto <n>]]`, com `<modelo>` ∈ `Opus|Sonnet|Haiku`, `<esforço>` ∈
    `low|medium|high|xhigh|max` e `<classe>` ∈
    `mecanica|implementacao|comportamental|investigacao|redacao`. O campo `esforço` é **opcional**
    e fica **entre** modelo e classe; ` + dono` marca aceite do dono; ` · teto <n>` é sufixo
    **legado**, tolerado e ignorado — não se escreve em card novo. Gramática lida por
    `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py` e `.claude/tools/backlog.py`;
    residência canônica em `GOVERNANCA.md` §3 (*Gramática do card*). Nenhum teto se escreve no
    card: a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel.
  ```

  **5. Linha do esqueleto de `## Anatomia do card`** — o segundo ponto. O trecho `de` inclui a
  linha seguinte porque é ela que torna a ocorrência única no arquivo. De:
  ```
  ### <ID> — <título> [<modelo> · classe <classe>]
  - **Objetivo:**
  ```
  Para:
  ```
  ### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>]
  - **Objetivo:**
  ```
  O `[ · teto <n>]` **não** entra no esqueleto: é forma legada, tolerada na leitura e proibida na
  escrita — quem autora card novo não escreve teto (`GOVERNANCA.md` §3).

  **6. Item 5 (*Dimensionamento*) da Fase 4** — a régua de tema substitui a régua de volume. De:
  ```
     tabela **antes** de registrar. Card que passa de ~80 linhas ou muda mais de um contrato é sinal
     de tarefa grande — parta por ramo, nunca por volume arbitrário.
  ```
  Para:
  ```
     tabela **antes** de registrar. Card que passa de ~80 linhas ou muda mais de um contrato é sinal
     de tarefa grande. **A régua de partição é o tema, nunca o volume** (`GOVERNANCA.md` §3, *A
     unidade de trabalho é o módulo coeso*): o card cobre uma **disciplina fechada** — um tema, com
     os seus verbos, os seus testes e a sua verificação ponta a ponta no mesmo despacho —, e nunca
     um fragmento do tema partido para caber num contexto. Divide-se quando o card cruza **dois
     assuntos**, nunca quando cruza muitas regiões do mesmo assunto: o teto de regiões editadas do
     gate de delegação não é limite de volume, é limite de **tema**, e a contagem de regiões é
     medida informativa de quem dimensiona. O que não é do tema continua fora — transversal,
     matéria alheia e "aproveitando que estou aqui" seguem proibidos (`G-EXECREADY`, §7 item 12).
  ```

  **7. Abertura do item 11 da Fase 4** (a concessão torna falsa a frase "Você não roda comando").
  De:
  ```
     Você não roda comando — logo, todo literal que uma linha de `Verificação` afirma ("imprime X",
  ```
  Para:
  ```
     Você **roda** o comando — logo, todo literal que uma linha de `Verificação` afirma ("imprime X",
  ```

  **8. Bullet de `## O que você NUNCA faz`** (terceira frase que a concessão torna falsa). De:
  ```
  - Ler arquivos inteiros para "se situar", rodar comando, medir ou sondar — delegue à coleta ou
    autore a investigação como tarefa.
  ```
  Para:
  ```
  - Ler arquivos inteiros para "se situar", sondar codebase ou medir corpus — delegue à coleta ou
    autore a investigação como tarefa. Rodar comando é exceção nomeada e única: o comando de
    aceite que você publica num card.
  ```

  **9. Item 12 da Fase 4, novo** — os cinco critérios de autoria. Inserir **imediatamente antes**
  da linha `### Fase 5 — Registro e parada`, deixando uma linha em branco entre o item 12 e esse
  cabeçalho. Texto a inserir:
  ```
  12. **Cinco critérios de autoria, fechados em execução medida** (cada um com o caso que o mediu;
     a residência acessível é `docs/RUBRICA_DE_REVISAO.md`, critérios (viii)..(xi) — aqui eles valem
     como dever de autoria, não como régua de revisão):
     (i) **Item enumerado e a frase que o conta fecham no mesmo card** (`DM-18`) — card que
     acrescenta, remove ou renomeia item de lista ou de tabela enumerada fecha, no mesmo ato, toda
     afirmação da **mesma seção** que conta ou qualifica o conjunto; e se o instrumento que julga a
     seção não discrimina essa afirmação, a tarefa **estende o instrumento**, senão o verde do
     guarda é falso conforto (2026-09-18, `AE-12`: `check-readme.ps1` anunciou `9 agente(s)`, saiu
     exit 0, e a prosa duas linhas acima dizia "oito").
     (ii) **Exigência estrutural não vira teste comportamental** (`DM-21`) — "usa a função X", "não
     reimplementa", "importada, não copiada" sai por uma de três, nesta ordem: o **caso
     discriminante** em que a implementação certa e a reimplementação plausível divergem; **inspeção
     mecânica** na `Verificação` (`Select-String`/contagem com literal e valor esperado, nunca
     `pytest`); ou `Restrição` declarada, sem prometer teste (2026-09-18, `AE-16`).
     (iii) **Guarda de borda tem residência única** (`DM-22`) — verbo novo em instrumento existente
     herda a borda do instrumento: uma função de guarda chamada por **todos** os ramos, nunca
     duplicada nem embutida no caminho de um só. Card que acrescenta verbo declara na `Verificação`
     o **mesmo** argumento inválido rodado nos **dois** ramos, e a afirmação de aceite é sobre o
     **stderr** — o exit code não discrimina (2026-09-19, `AE-17`).
     (iv) **Piso de regressão é relação, nunca constante** (`DM-23`) — nenhuma linha de
     `Verificação` carrega total de suíte como número de aceite: o piso é o total **re-medido no
     despacho**, a entrega soma os `<N>` testes novos e **não reduz** esse total; o número fica no
     card como **referência histórica datada**, não como aceite. Vale igual para baseline por
     arquivo de teste (2026-09-19, `AE-18`: o piso escrito nos cards envelheceu cinco vezes em sete
     despachos da mesma janela).
     (v) **O literal do comando é o que foi colado e rodado** (`DM-24`) — comando cujo literal
     contenha **crase**, **asterisco** ou **barra invertida** publica-se em **bloco cercado**, nunca
     em code span; todo `Select-String` de aceite leva `-SimpleMatch`, salvo regex deliberado e
     rodado; e toda linha de `Verificação` por efeito em arquivo publica **os dois** valores
     rodados, antes e depois — padrão que devolve o **mesmo** valor nos dois mundos é inválido por
     construção (2026-09-19, `AE-19`).
  ```

  **10. `CHANGELOG.md`, sob `## [Não lançado]`** — primeiro bullet do bloco. Texto a inserir:
  ```
  - `pantonic-planner` ganha `Bash` no toolset (decisão do dono, 2026-09-18): planner e executor
    passam a acessar a mesma ferramenta de validação, e o dever "comando de aceite não se deduz,
    se roda" deixa de ser inexequível pelo papel a que se dirige.
  ```

- **Verificação:** (forma normativa do bloco `Verificação`, publicada em
  `docs/RUBRICA_DE_REVISAO.md` pela `LM-T5`. **Todo** valor abaixo foi rodado no `ESC-23`, nos
  **dois** mundos — árvore atual e árvore com os dez literais aplicados, restaurada no mesmo ato —
  `DM-12`, `DM-24` (iii). As linhas 11 e 12 são **guarda de regressão, não discriminante**, e estão
  declaradas como tal.)
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'tools: Read, Glob, Grep, Write, Edit, Bash' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (Literal 1: o frontmatter. O padrão é a linha **inteira** com
     `Bash`, e não `^tools:` — o `^tools:` casa nos dois mundos e não discrimina mundo nenhum.)
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '- Ferramenta de execução: você **tem**' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (Literal 3: o fato estável do `Bash` no corpo.)
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'não roda comando e não mede','Você não roda comando —','rodar comando, medir ou sondar' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 3**. (Literais 2, 7 e 8: as três frases que a concessão torna falsas
     — um padrão por frase, e o zero só sai com as três fechadas.)
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '### <ID> — <título> [<modelo> · classe <classe>]' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 2**. (Literais 4 e 5: a gramática aposentada sai dos dois pontos.)
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '[<modelo>[ + dono][ · esforço <esforço>] · classe' -SimpleMatch | Measure-Object).Count"
     ```
     → **2**. **Medido antes: 0**. (Literais 4 e 5: a gramática vigente entra nos dois pontos. Sai
     **2**, e não 1, porque os dois pontos são independentes — a linha 4 sozinha não distingue
     "removeu os dois" de "removeu um e não pôs nada".)
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'parta por ramo, nunca por volume arbitrário' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**. (Literal 6: a régua de volume sai do item 5 da Fase 4, o
     *Dimensionamento*.)
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'não é limite de volume, é limite de' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (Literal 6: a régua de tema entra no lugar dela.)
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'DM-18','DM-21','DM-22','DM-23','DM-24' -SimpleMatch | Measure-Object).Count"
     ```
     → **5**. **Medido antes: 0**. (Literal 9: um padrão por critério; o arquivo não cita decisão
     de plano hoje, então o 5 só sai com os cinco publicados.)
  9. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '12. **Cinco critérios de autoria' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (Literal 9: os cinco critérios entram como **item 12 da Fase 4**
     — numerados na sequência do item 11, não como seção nova.)
  10. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern ' no toolset (decisão do dono, 2026-09-18): planner e executor' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (Literal 10, a linha do `CHANGELOG.md`.)
  11. ```
     pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode validate | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0**. **Medido antes: exit 0** (2026-09-19, medido no despacho do `ESC-23`).
     Regressão, não discriminante: conferido no `ESC-23` que `kit_check.ps1:165` aceita `tools:`
     como lista separada por vírgula, logo o `Bash` novo no frontmatter não pode derrubá-lo.
  12. ```
     pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0**. **Medido antes: exit 0** (2026-09-19, medido no despacho do `ESC-23`).
     Regressão, não discriminante: a `description` do planner **não** muda nesta tarefa, então a
     projeção `.claude/README.md` não se move e o drift não reabre.
- **Restrições desta tarefa:** tudo é **transcrição literal** — cada trecho `para` está escrito
  acima por inteiro e não se reescreve, não se resume e não se "melhora" na passagem. O card passa
  de ~80 linhas por **volume de literal**, e volume não parte card: a régua de partição é o
  **tema**, e o tema é um só — a definição do `pantonic-planner` (`DM-2`, `DM-4`).
- **Não fazer:** não alterar `description` nem `model` de agente nenhum; não tocar
  `.claude/agents/pantonic-executor.md` nem `.claude/agents/pantonic-reviewer.md` (publicados por
  `DM-8`) nem `.claude/agents/pantonic-consultant.md` (figura provisória do dono); não regenerar
  `.claude/README.md` aqui (é a `LM-T7`, e a `description` intocada não o afeta); não mexer em
  `GOVERNANCA.md` nem em `docs/RUBRICA_DE_REVISAO.md` — eles são as **residências canônicas** do
  que este card transcreve, e já estão publicados; não tocar `.claude/settings.json`; não commitar.
- **Contingências:**
  1. se algum trecho `de:` não for encontrado **literalmente**, ou ocorrer mais de uma vez no
     arquivo → parar e sinalizar `blocked` razão `premissa`, citando o trecho e a contagem medida:
     o arquivo mudou entre o `ESC-23` e o despacho, e quem reconcilia o literal é o consultor;
  2. se a `Verificação` 11 sair ≠ 0 → parar e sinalizar `blocked` razão `premissa`, colando a
     mensagem do instrumento;
  3. se a `Verificação` 12 sair ≠ 0 → **seguir com a entrega** e reportar a saída no retorno: a
     projeção não é produto desta tarefa e o drift tem dono próprio (`LM-T7`).
- **Pronto quando:** as doze linhas de `Verificação` saem nos valores declarados — isto é: o
  `tools:` do planner declara `Bash`; o fato estável do `Bash` está no corpo; as três frases que a
  concessão tornava falsas sumiram do arquivo; a gramática aposentada não está em nenhum dos dois
  pontos e a vigente está nos dois; a régua de tema substituiu a de volume no item 5 da Fase 4; os
  cinco critérios estão no item 12 da Fase 4; a linha está no `CHANGELOG.md`; e o `kit_check` segue
  em exit 0 nos dois modos.

### LM-T9 — `consultant-spec`: a figura ad-hoc vira especificação [Opus · classe redacao]

- **Status:** `done` · 2026-09-19
- **Esforço:** high
- **Objetivo:** converter os insumos de `## 9` — medidos durante a execução deste plano, não
  lembrados depois — em **um** documento, `docs/consultant-spec.md`, que descreva a figura do
  consultor de plano como ela **se comportou**: quando é acionada, o que decide sozinha, o que
  escala, qual é a fronteira com o `pantonic-planner` e qual é o custo dela. Um tema só: **a
  especificação da figura**. A `DM-28` é a régua: até este documento existir e ser aceito, o
  `pantonic-consultant` é ad-hoc e não se cita como fonte normativa.
- **Depende de:** `LM-T6`. É penúltima por ordem do dono (2026-09-19, `DM-29`) — a spec se escreve
  depois que a figura tiver conduzido o plano inteiro, porque insumo de uma janela só não sustenta
  uma especificação. Na prática: despachar depois que a `LM-T6` fechar, com `## 9` já contendo os
  `I-<n>` das janelas posteriores a esta.
- **Arquivos-alvo:**
  - `docs/consultant-spec.md` — o documento (novo).
  - `docs/DOC_MAP.md` — a entrada de navegação do documento novo.
  - `CHANGELOG.md` — a linha do bloco não lançado.
- **Produto do módulo:** `docs/consultant-spec.md` respondendo, com o insumo medido ao lado de cada
  resposta: (a) **gatilho** — o que aciona o consultor e o que não aciona; (b) **domínio de
  decisão** — o que ele fecha sozinho (técnico/tático) e o que sobe ao dono (estratégico,
  `G-NOASK`); (c) **fronteira com o `pantonic-planner`** — ele autorou cards novos nesta janela, e
  o documento tem de dizer se isso é da figura ou empréstimo; (d) **instrumento** — por que nasce
  com `Bash` (`DM-12`, `DM-24`); (e) **custo e teto** — 68,5% da janela num papel só é o número
  que a spec precisa endereçar, com a regra de quando **não** acionar. **Segunda medida, da janela
  de 2026-09-19:** **63%** (`3.802,2k` de `6.004,3k`), em **14** acionamentos — a spec tem **duas**
  janelas medidas e trata o número como **série**, não como constante (`DM-23`, `AE-21`); (f) **encerramento** — como
  a figura termina (decisão de janela × poluição, Regra 2);
  **(g) e (h), acrescentados por ato do dono em 2026-09-19 (`DM-45` (iii) e (iv)):**
  **(g) fim de vida por limite, e a sucessão** — o consultor **promove handover ao perceber que se
  aproxima do próprio limite** (estado do cenário, escalonamentos abertos, o que estava em curso),
  e o `scrum-master` **descomissiona a instância e provisiona outra**, repassando esse handover. A
  spec fixa **a forma de comunicação**, que nesta janela ficou **ad-hoc** por `DM-28` e por isso
  **não é fonte normativa** até ser projetada no plano próprio. Lastro medido: o `ESC-22`, em que a
  queda por *session limit* levou junto o contexto de 14 passagens e deixou o `AE-38` sem alocação
  e a `LM-T3b` sem varredura — o loop seguiu por medida própria no gate, mas o cenário acumulado
  **morreu**;
  **(h) estatística do próprio acionamento** — o consultor registra, a cada acionamento, **o que o
  motivou, que classe de impedimento era e o que ficou inconclusivo**, produzindo o **panorama dos
  pontos inconclusivos**. A spec diz **o que se coleta, onde mora e quem lê**. Destino declarado:
  **insumo da spec de robustez**. Lastro medido: 14 acionamentos e **63%** do consumo desta janela
  (`3.802,2k` de `6.004,3k`) sem **nenhum** registro estruturado de causa — `docs/telemetria.tsv`
  mede **custo**, não **motivo**; sem o panorama, a spec de robustez seria autorada sobre impressão.
- **Restrições desta tarefa (copiadas inline):**
  - **Descrever o medido, não o desejado.** Toda afirmação da spec sai de um `I-<n>` de `## 9` ou
    de um `AE-<n>`/`ESC-<n>` deste plano, citado pelo identificador. Afirmação sem lastro medido
    não entra — nem como recomendação.
  - **Não é doutrina ainda.** O documento é especificação de figura provisória: não altera
    `GOVERNANCA.md`, não cria guardrail `G-*`, não se declara fonte normativa. Promover a doutrina
    é ato posterior do dono (`DM-28`).
  - `redacao-doc`: sem narrativa de proveniência, sem citação de interlocutor, sem ID de processo
    no corpo — os identificadores entram como **lastro citado**, em nota ou tabela, não como
    historinha.
  - Não editar `.claude/agents/pantonic-consultant.md`. A definição do agente é outra superfície e
    outro tema; se a spec concluir que a definição diverge, o achado sai como `AE-<n>` com rota.
- **Não fazer:** não escrever a spec do `pantonic-planner` nem redesenhar o `scrum-master`; não
  absorver `TK-38`, `TK-54b` nem a matéria de confiabilidade (`DM-30`); não antecipar esta tarefa
  para antes da `LM-T6`.
- **Pronto quando:** `docs/consultant-spec.md` existe, cobre as **oito** perguntas (a)..(h) — contagem fechada no mesmo ato que acrescentou (g) e (h), `DM-18` (i) —, cada uma
  com pelo menos um identificador de lastro, está indexado no `docs/DOC_MAP.md` e tem linha no
  `CHANGELOG.md`.
- **Verificação:** (os comandos foram extraídos deste card e rodados verbatim na autoria,
  2026-09-19 — `DM-24`; reescrita na forma normativa da rubrica pelo `ESC-28`, com o literal
  `**Medido antes:**` que o `card_check` lê e **nenhuma** constante de corpus como aceite)
  1. ```
     pwsh -NoProfile -Command "[int](Test-Path docs/consultant-spec.md)"
     ```
     → **1** depois. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/DOC_MAP.md -Pattern 'consultant-spec' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1** depois. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "if (Test-Path docs/consultant-spec.md) { [int]((Select-String -Path docs/consultant-spec.md -Pattern 'I-' -SimpleMatch | Measure-Object).Count) } else { 0 }"
     ```
     → depois, **≥** a contagem de insumos `I-<n>` medida no despacho pelo comando de insumo
     abaixo. **Medido antes: 0** — o arquivo ainda não existe, e é isso que torna o valor
     **invariante**: ele mede o alvo do card, não o corpus que outras entregas movem (`ESC-28`).

  **Insumo do despacho, fora da lista e sem número de item** (não é aceite, é o número que o
  executor precisa ter à mão):

  ```
  pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^- \*\*.I-\d' | Measure-Object).Count"
  ```

  mede quantos insumos `I-<n>` existem em `## 9` **no momento do despacho** — referência
  **datada**, nunca aceite: **8** na autoria (2026-09-19) e **10** em 2026-09-19 depois da
  `LM-T10`, que é a prova de que publicar essa contagem como constante envelheceria (`AE-49`).
  *Nota de autoria, `DM-24`:* a primeira forma deste comando usava `-SimpleMatch` com o padrão
  `- **I-` e devolveu **1** — casou a própria linha em que estava publicada e **nenhum** dos
  insumos, porque o identificador vem entre crases. Mesma classe do `AE-19`, pega antes do
  despacho por ter sido rodada. A forma acima é ancorada em início de linha, o que exclui a
  publicação.

### LM-T10 — A escrita mecânica em definição de agente: o instrumento e a prova da rota [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-19 — primeira tarefa da fila da próxima janela (`DM-50`).
- **Esforço:** medium
- **Objetivo:** um só — tornar a escrita em `.claude/agents/**` uma **aplicação mecânica de
  literais declarados**, feita por instrumento, e **provar em campo** que essa via funciona a
  partir de um contexto de executor. Enquanto a prova não existir, a rota da `DM-50` é hipótese.
- **Depende de:** `DM-50`, que a decide. Nenhuma tarefa aberta.
- **Arquivos-alvo:**
  - `.claude/tools/agentdef.py` (novo)
  - `tests/test_agentdef.py` (novo)
  - `.claude/agents/pantonic-planner.md`
  - `.claude/README.md`
- **Contrato do instrumento** (fechado aqui; o executor implementa, não desenha):
  `python .claude/tools/agentdef.py apply --arquivo <caminho> --de <texto> --para <texto>`, com
  `--de`/`--para` **repetíveis** e lidos **em pares, na ordem**. Comportamento, verbo único:
  1. **Alvo restrito.** `--arquivo` só é aceito se casar `.claude/agents/*.md` — glob **não
     recursivo**, de modo que `.claude/agents/sub/x.md` é recusado tanto quanto `README.md`. Fora
     disso: exit **1**, imprimindo `agentdef: alvo fora de '.claude/agents/*.md'` seguido do
     caminho recebido.
  2. **Pares completos.** `--de` e `--para` em número igual; senão exit **1**, imprimindo
     `agentdef: --de e --para vem em pares`.
  3. **Ocorrência única.** Cada `de` ocorre **exatamente uma vez** no conteúdo atual. Zero: exit
     **1**, `agentdef: literal nao encontrado`. Mais de uma: exit **1**,
     `agentdef: literal nao e unico`. As duas mensagens terminam com o trecho recebido.
  4. **Tudo ou nada.** Os pares são **todos validados antes** de qualquer escrita: se um falha,
     **nenhum byte** do arquivo muda. Um implementador que aplique par a par enquanto valida passa
     nos outros testes e falha neste — é o caso que separa a implementação certa da plausível.
  5. **Preserva o arquivo.** Encoding `utf-8` e o **line ending original** (ler e escrever com
     `newline=''`): um arquivo `CRLF` continua `CRLF` depois do `apply`.
  6. **Sucesso.** exit **0**, imprimindo `agentdef: ` seguido do caminho, do número de pares
     aplicados e do saldo de linhas.
  7. **Borda de residência única** (`DM-22`): a validação dos itens 1 a 3 mora em **uma** função,
     chamada por todos os ramos do verbo — nunca duplicada no caminho de um só.
- **Testes** (`tests/test_agentdef.py`, nomes fixados aqui):
  `test_apply_aplica_par_unico`; `test_apply_recusa_alvo_fora_de_agents` (dois casos: `README.md` e
  um caminho **aninhado** sob `.claude/agents/`, que é o que separa o glob não recursivo do
  recursivo); `test_apply_recusa_literal_ausente`; `test_apply_recusa_literal_nao_unico`;
  `test_apply_nao_escreve_quando_um_par_falha` (compara os **bytes** do arquivo antes e depois);
  `test_apply_preserva_crlf` (fixture gravada com `CRLF`; leitura em modo texto padrão a
  converteria para `LF` e o teste cairia).
- **O par literal a aplicar — e é ele que prova a rota.** Fecha a matéria (b) do `PM-1`: a
  `description` do `pantonic-planner` afirma hoje algo que a concessão de `Bash` (`DM-16`,
  `DM-27`, `LM-T8`) tornou falso. Par único, aplicado **pelo instrumento**:
  ```
  de:   não mede nada por conta própria
  para: não sonda codebase por conta própria
  ```
- **Passos:**
  1. Escrever `.claude/tools/agentdef.py` conforme o contrato acima.
  2. Escrever `tests/test_agentdef.py` com os seis testes nomeados.
  3. Aplicar o par literal **rodando o instrumento pelo `Bash`**, com o alvo
     `.claude/agents/pantonic-planner.md`.
  4. Regenerar a projeção no **mesmo ato** (`DM-16` (iv)): `kit_check.ps1 -Mode generate` — a
     `description` alimenta `.claude/README.md`, e sem isso o `check-drift` abre vermelho.
- **Restrições desta tarefa:** o par literal é aplicado **rodando o instrumento**, nunca por `Edit`
  ou `Write` sobre o arquivo de agente. É essa execução que constitui a prova da rota: aplicar por
  edição direta deixa o arquivo igual e a prova **inexistente**, e a tarefa fica sem entregar o que
  o `DM-50` pediu. O instrumento **não** decide conteúdo: ele aplica literal declarado no card.
- **Não fazer:** não tocar `.claude/agents/pantonic-executor.md` nem
  `.claude/skills/scrum-master/SKILL.md` — o motivo `ferramenta` e a guarda `G-TOOLDENY` são a
  `LM-T11`, e esta tarefa existe justamente para tornar aquela executável; não alterar `model` nem
  `name` de agente nenhum; não estender `rdo.py`, `backlog.py`, `review_evidence.py` nem
  `card_check.py`; não criar verbo além de `apply`; não commitar.
- **Contingências:**
  1. se o `Bash` que roda o instrumento for **recusado** ao executor → **essa medida é o
     entregável**, não uma falha: devolver `blocked motivo=premissa` colando a **linha literal da
     recusa** e o **comando exato** que a produziu, e registrar no corpo da tarefa qual ferramenta
     foi recusada sobre qual caminho. **Não** contornar por outra ferramenta, **não** pedir ao loop
     que aplique. É com esse dado que a `DM-50` decide entre as saídas (b) e (d), e é ele que
     impede a quarta repetição do problema;
  2. se o par literal já estiver aplicado no arquivo (o `de` não for encontrado) → **seguir** com o
     restante da tarefa e registrar o fato: o instrumento e os testes são o entregável principal, e
     a `Verificação` 4 e 5 continuam discriminando;
  3. se `kit_check.ps1 -Mode generate` alterar mais que a linha da `description` no
     `.claude/README.md` → parar e sinalizar `blocked` razão `premissa`, colando o diff: projeção
     que se move além do esperado é achado, não resíduo.
- **Verificação:** (forma normativa publicada pela `LM-T5`; todo valor abaixo foi rodado na autoria,
  2026-09-19 — `DM-12`, `DM-24`)
  1. ```
     python -m pytest tests/test_agentdef.py -q
     ```
     → verde, com os **seis** testes nomeados acima. **Medido antes: exit 4** (o arquivo de teste
     não existe; `pytest` sai 4 em *file or directory not found*).
  2. ```
     python .claude/tools/agentdef.py apply --arquivo README.md --de a --para b
     ```
     → **exit 1**, nomeando a recusa de alvo fora do diretório de agentes. **Medido antes: exit 2**
     (o instrumento não existe; `python` sai 2 em *can't open file*).
  3. ```
     python .claude/tools/agentdef.py apply --arquivo .claude/agents/pantonic-planner.md --de Fase --para Etapa
     ```
     → **exit 1**, nomeando a ocorrência não-única, **sem alterar o arquivo**.
     **Medido antes: exit 2** (o instrumento não existe). O literal `Fase` foi escolhido por ser medidamente não-único
     no alvo: 19 ocorrências em 2026-09-19.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'não mede nada por conta própria' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**. (A afirmação falsa sai da `description`.)
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'não sonda codebase por conta própria' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (E entra a verdadeira, no lugar dela.)
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/README.md -Pattern 'não sonda codebase por conta própria' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A projeção foi regenerada no mesmo ato — `DM-16` (iv). Sem esta
     linha, a tarefa fecharia verde deixando o `check-drift` vermelho para a tarefa seguinte.)
  7. ```
     pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"
     ```
     → **exit 0**. **Medido antes: exit 0** (2026-09-19). Regressão, não discriminante — e aqui ela
     só continua verde **porque** o passo 4 rodou; é a guarda que pega o esquecimento.
  8. ```
     python -m pytest tests/ -q
     ```
     → verde, **somando** os seis testes novos ao total re-medido no despacho e **sem reduzi-lo**
     (`DM-23`). **Medido antes: 191 passed** (2026-09-19, re-medido no `ESC-27` — o reparo do instrumento de índice somou 4 TF ao piso de 187; relação, **re-medir no despacho**).
- **Pronto quando:** as oito linhas de `Verificação` saem nos valores declarados; o instrumento
  existe com o verbo único e a borda de residência única; os seis testes existem com os nomes
  fixados; a `description` do `pantonic-planner` deixou de afirmar o falso **por aplicação do
  instrumento**, e a projeção `.claude/README.md` fechou no mesmo ato. Se a contingência 1 casar, o
  critério de pronto é **a medida da recusa**, registrada com o comando literal — e a tarefa fecha
  `blocked`, que é desfecho e não fracasso.

### LM-T11 — O contrato de recusa de ferramenta: `G-TOOLDENY`, o motivo `ferramenta` e o fim da exceção do `AE-44` [Opus · classe redacao]

- **Status:** `done` · 2026-09-19 — segunda tarefa da fila da próxima janela (`DM-50`).
- **Esforço:** medium
- **Objetivo:** um só — fechar o **contrato de recusa de ferramenta**: ferramenta negada ao
  executor deixa de ser improviso ou silêncio e passa a ser um desfecho **nomeado, devolvido e
  roteado**. Com ele, a exceção do `AE-44` fecha e a `GOVERNANCA.md` §3 volta a valer sem ressalva.
- **Depende de:** `LM-T10` — **duas** vezes, e as duas são estruturais: (1) esta tarefa edita
  `.claude/agents/pantonic-executor.md`, que é a superfície recusada, e o único caminho decidido
  para editá-la é o instrumento que a `LM-T10` entrega; (2) se a `LM-T10` fechar `blocked` pela
  contingência 1 dela, a rota da `DM-50` caiu e **este card não se despacha como está** — volta ao
  consultor com o dado da recusa.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `README.md`
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/agents/pantonic-executor.md`
  - `CHANGELOG.md`
- **Produto do módulo:** (a) `G-TOOLDENY` publicada como item **20** de `GOVERNANCA.md` §7, com a
  linha correspondente na tabela *Os guardrails* do `README.md` **no mesmo ato** — a lista e a
  frase que a conta fecham juntas (`DM-18` (i)), e é o `check-readme.ps1` que reprova se
  divergirem; (b) o motivo **`ferramenta`** no domínio fechado do retorno do executor, nas duas
  superfícies que o enunciam; (c) a regra de roteamento **`A3c`** na tabela do `scrum-master`; (d)
  o encerramento explícito da exceção do `AE-44`; (e) a linha em `CHANGELOG.md`.
- **Textos literais** (transcrição; cada `de` ocorre uma vez, conferido na autoria em 2026-09-19):

  **1. `GOVERNANCA.md` §7, item 20, novo** — inserir depois do item 19 (`G-MODULO`), que hoje
  encerra a lista:
  ```
  20. **G-TOOLDENY — ferramenta recusada ao executor é desfecho nomeado, nunca improviso nem
      silêncio** — quando o harness nega ao executor a ferramenta de que o card depende, ele
      **não** contorna por outra ferramenta, **não** pede a terceiro que aplique e **não** segue
      em silêncio: devolve `blocked motivo=ferramenta`, nomeando a **ferramenta** negada e o
      **caminho** sobre o qual foi negada, e cola a linha literal da recusa. Quem recebe é o loop,
      que roteia pela `A3c`: a superfície tem **fallback declarado** — outro instrumento que faça a
      mesma escrita —, e então a tarefa segue por ele; ou não tem, e então a recusa é **matéria de
      plano**, não de janela. Superfície de escrita sem fallback declarado é defeito de
      planejamento. Medida que o originou: três recusas do classificador sobre
      `.claude/agents/**` dentro de uma tarefa só, em 2026-09-19 (`AE-11`, `AE-42`, `AE-44`).
  ```

  **2. `README.md`, tabela *Os guardrails*, linha 20, nova** — inserir depois da linha 19:
  ```
  | 20 | `G-TOOLDENY`: ferramenta recusada ao executor vira `blocked motivo=ferramenta` com a ferramenta, o caminho e a linha literal da recusa — nunca contorno por outra ferramenta, delegação a terceiro ou silêncio; o loop roteia pela `A3c` ao fallback declarado da superfície, e superfície sem fallback é matéria de plano | **Instrução de agente** + roteamento da skill `scrum-master` |
  ```

  **3. `.claude/skills/scrum-master/SKILL.md`, passo 4** — a gramática do retorno. De:
  ```
  <tarefa> blocked motivo=<dependencia|premissa> <uma linha de razão>
  ```
  Para:
  ```
  <tarefa> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>
  ```

  **4. `.claude/skills/scrum-master/SKILL.md`, passo 5** — o vocabulário aceito na recepção. De:
  ```
  `motivo=` fora do par
    `dependencia|premissa`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`.
  ```
  Para:
  ```
  `motivo=` fora do trio
    `dependencia|premissa|ferramenta`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`.
  ```

  **5. `.claude/skills/scrum-master/SKILL.md`, tabela de roteamento** — inserir a linha `A3c`
  imediatamente depois da linha `A3b`:
  ```
  | `A3c` | `status=blocked` com `motivo=ferramenta` | materializa `blocked` com a razão, **sem** reclassificar o motivo; lê o **fallback declarado** da superfície no card e, havendo, **redespacha a mesma tarefa** por ele, **sem** consumir retentativa — a tarefa não falhou, a ferramenta foi negada; não havendo fallback declarado, **PARA** e a recusa sobe como matéria de plano, com a ferramenta, o caminho e a linha literal da recusa. **Não** despacha o `reviewer` e **não** escreve RDO |
  ```

  **6. `.claude/agents/pantonic-executor.md`** — o desfecho novo. Aplicar **pelo instrumento da
  `LM-T10`**, nunca por edição direta. De:
  ```
  **Como devolver um card defeituoso** — é o sinal `blocked` com `motivo=premissa` (roteamento
  ```
  Para:
  ```
  **Como devolver uma ferramenta recusada** — quando o harness nega a ferramenta de que o card
  depende (`G-TOOLDENY`), a linha é `blocked` com `motivo=ferramenta`, nomeando a ferramenta, o
  caminho e colando a recusa literal:

      <tarefa> blocked motivo=ferramenta ferramenta=<nome> caminho=<caminho>: <linha literal da recusa>

  Você **não** contorna por outra ferramenta, **não** pede a terceiro que aplique e **não** segue
  em silêncio. O domínio fechado do motivo é `<dependencia|premissa|ferramenta>`.

  **Como devolver um card defeituoso** — é o sinal `blocked` com `motivo=premissa` (roteamento
  ```

  **7. `CHANGELOG.md`, sob `## [Não lançado]`:**
  ```
  - A recusa de ferramenta ao executor deixa de ser improviso e vira desfecho nomeado: guarda
    `G-TOOLDENY`, motivo `ferramenta` no domínio fechado do retorno e regra de roteamento `A3c` ao
    fallback declarado da superfície. A exceção aberta em 2026-09-19, em que a orquestração
    implementou uma tarefa por instrução do dono, fica **fechada** e não é precedente.
  ```
- **Coerência do módulo (aceite de `DM-3`):** depois desta tarefa, **nenhuma** das quatro
  superfícies enuncia o domínio antigo de dois termos. A varredura é parte da entrega, e a
  `Verificação` 4 a mede.
- **Restrições desta tarefa:** o literal 6 é aplicado **rodando o instrumento da `LM-T10`**, nunca
  por `Edit` ou `Write` — é a segunda prova da rota da `DM-50`, agora em produção e não em
  fixture. A exceção do `AE-44` **não** se reescreve no achado: ela fica onde está, como registro
  do que foi feito, e o que esta tarefa publica é o seu **encerramento**.
- **Não fazer:** não mexer em `.claude/tools/agentdef.py` nem nos testes dele (são da `LM-T10`);
  não estender `rdo.py`, `backlog.py`, `review_evidence.py` nem `card_check.py` — **medido na
  autoria: nenhum deles lê o domínio de `motivo`**, que vive só em prosa nas duas superfícies, e o
  `--razao` do `backlog.py` é texto livre; não alterar `description`, `model` ou `name` de agente
  nenhum; não regenerar `.claude/README.md` (a `description` não muda aqui); não commitar.
- **Contingências:**
  1. se o instrumento da `LM-T10` recusar o literal 6 por não-unicidade ou ausência → parar e
     sinalizar `blocked` razão `premissa`, colando a saída do instrumento: o arquivo mudou entre a
     autoria e o despacho, e quem reconcilia o literal é o consultor;
  2. se a `Verificação` 1 sair com número de guardas diferente de **20** → parar e sinalizar
     `blocked` razão `premissa`: a lista e a tabela divergiram, e é exatamente o invariante que
     esta linha existe para pegar;
  3. se o `Bash` que roda o instrumento for recusado ao executor → devolver `blocked
     motivo=premissa` com a linha literal da recusa — o motivo `ferramenta` ainda **não** existe no
     domínio quando esta tarefa começa, e é ela que o cria.
- **Verificação:** (forma normativa publicada pela `LM-T5`; todo valor abaixo foi rodado na autoria,
  2026-09-19 — `DM-12`, `DM-24`)
  1. ```
     pwsh -NoProfile -Command ".claude/checks/check-readme.ps1"
     ```
     → **exit 0**, anunciando **20 guardrail(s)**. **Medido antes: 19 guardrail(s)**. É o
     invariante de contagem do `AE-12`: a checagem 4 confronta a lista de `GOVERNANCA.md` §7 com a
     tabela do `README.md`, e sai vermelha se só uma das duas receber a guarda nova.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern '^20\. \*\*G-TOOLDENY' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A guarda existe na doutrina, no número que a sucede.)
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '^\| 20 \| .G-TOOLDENY.' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (E na tabela que o instrumento conta.)
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md,.claude/agents/pantonic-executor.md -Pattern '<dependencia|premissa>' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**. (O domínio de dois termos some das superfícies — aceite de
     coerência do módulo.)
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md,.claude/agents/pantonic-executor.md -Pattern '<dependencia|premissa|ferramenta>' -SimpleMatch | Measure-Object).Count"
     ```
     → **2**. **Medido antes: 0**. (E o de três entra nas **duas** superfícies. Sai **2**, e não 1,
     porque cada superfície enuncia o domínio por conta própria e fechar só uma deixaria o executor
     e o loop falando línguas diferentes.)
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '^\| .A3c. \|' | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (A regra de roteamento existe: sem ela o motivo novo chega ao
     loop e cai em *retorno inválido*.)
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'recusa de ferramenta ao executor deixa de ser improviso' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  8. ```
     python -m pytest tests/ -q
     ```
     → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta
     teste, e é a suíte de conformance que tranca doutrina. **Medido antes: exit 0** — veredito
     **invariante** ao que outros cards entregam, que é o que os critérios (x)/(xiii) pedem e o que
     o `card_check` sabe conferir. Referência **datada**, e não aceite: `197 passed` em 2026-09-19
     (`ESC-28`); a mesma baseline, publicada como constante, envelheceu três vezes nesta janela
     (187, 191, 197).
- **Pronto quando:** as oito linhas de `Verificação` saem nos valores declarados; a guarda existe
  nas duas superfícies que a contam; o domínio de três termos é o único enunciado; a `A3c` roteia o
  motivo novo; a linha do `CHANGELOG.md` está lá; e o literal do executor foi aplicado **pelo
  instrumento**, não por edição direta.

### LM-T12 — A enumeração em prosa que nenhum instrumento lê: as duas contagens do README e a `A3c` nas três listas do loop [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-29` (2026-09-19), **primeiro da fila restante**: o item
  (c) corrige a skill que **governa o loop enquanto ele roda**, e errar rota custa mais do que
  adiar a `LM-T4c`.
- **Esforço:** medium
- **Objetivo:** um só — fechar o invariante de contagem do `DM-18` (i) na metade que o instrumento
  **não** enxerga. A `LM-T11` publicou o vigésimo guardrail e deixou duas frases de prosa do
  `README.md` falsas com o guarda **verde**; e publicou a `A3c` na tabela do bloco A sem entrar nas
  três enumerações da própria skill que roteia por ela.
- **Depende de:** nada. Nada depende desta.
- **Arquivos-alvo:**
  - `README.md` — as duas frases de contagem da seção *Os guardrails*.
  - `.claude/checks/check-readme.ps1` — o guarda passa a ler as duas frases.
  - `.claude/skills/scrum-master/SKILL.md` — as três enumerações que ignoram a `A3c`.
  - `CHANGELOG.md` — a linha do bloco não lançado.
- **Produto do módulo:**
  - **(a) As duas frases do `README.md`, com o literal exato.** A primeira linha de prosa da seção
    *Os guardrails* passa a ser, verbatim:
    `Vinte regras mínimas obrigatórias, válidas em todo projeto da família, sem exceção.`
    Na frase das três formas, **só** o numeral do meio muda: `**doze**` vira `**treze**`. O resto
    da frase — inclusive a oração *"uma delas soma as duas formas, e por isso aparece nas duas
    contagens"* — fica **literal**. Recontagem medida no `ESC-29` sobre a coluna *Como é
    enforceada* da própria tabela: **20** linhas, **7** com `Teste executável`, **13** com
    `Gate de review`, `Instrução de agente` ou `Gate de planejamento`, **1** com
    `Enforcement de permissão`, e **1** linha nas duas primeiras classes (a de número oito) — de
    modo que `teste + gate - ambos + permissão` fecha em **20**.
  - **(b) O guarda lê as duas frases.** `.claude/checks/check-readme.ps1` ganha, na checagem que já
    compara a tabela de guardrails com `GOVERNANCA.md` §7, duas conferências novas, **reusando o
    `$numeralMap` que o próprio script já tem** (por extenso até vinte):
    - a linha da seção que casa `regras mínimas obrigatórias` tem o numeral igual ao número de
      linhas da tabela (`$readmeGuardrailCount`);
    - a linha da seção que casa `regras falham como teste executável` tem os dois numerais iguais
      às contagens derivadas da coluna *Como é enforceada* pelos literais `Teste executável` e
      `Gate de review|Instrução de agente|Gate de planejamento`, e a identidade
      `teste + gate - ambos + permissão` fecha no total da tabela (`Enforcement de permissão` é o
      terceiro literal).

    Frase ausente, numeral fora do vocabulário ou divergência **falham** com mensagem que nomeia o
    número declarado e o medido, no mesmo formato das mensagens que o script já emite. A linha de
    sucesso do guarda passa a citar as frases conferidas.
  - **(c) A `A3c` nas três enumerações de `.claude/skills/scrum-master/SKILL.md`.** Literais:
    - no *Passo 8 — Roteamento, bloco A*, campo `Gatilho`: `regras A1..A3b` vira `regras A1..A3c`;
    - no *Relatório de encerramento*, primeiro bullet: `inclusive A6a e A8a` vira
      `inclusive A3c, A6a e A8a`;
    - na seção *O que obriga parada e o que segue com registro*, a `A3c` entra nos **dois**
      bullets, porque é a única regra do bloco A com desfecho **condicional**: em *Obriga parada*,
      como recusa de ferramenta **sem** fallback declarado; em *Segue com registro*, como recusa
      de ferramenta **com** fallback declarado, que redespacha a mesma tarefa sem consumir
      retentativa. No mesmo ato cai o advérbio **sempre** do bullet de parada — ele afirma que a
      escalada chega só pelo `pendencia=` ou pela recomendação `escalar`, e a `A3c` é o
      contraexemplo: ela nem despacha o `reviewer`, então não há laudo de onde a recomendação
      viesse.
  - **(d) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal
    `a enumeração em prosa entra no guarda`.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'Vinte regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'Dezenove regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count"
     ```
     → **0** (a frase falsa não sobrevive). **Medido antes: 1**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '**treze** dependem de gate de review' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '**doze** dependem de gate de review' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: o guarda passa a citar a frase que lê. **Medido antes: 0** — é este zero que mede o
     defeito, porque o invariante estava guardado só na metade que o script enxerga.
  6. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0**, com a saída citando as frases conferidas. **Medido antes: exit 0** — veredito
     invariante (critério (xviii)); hoje ele sai verde **com as duas frases falsas**, e é por isso
     que este item sozinho não discrimina: quem discrimina são os itens de literal acima.
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'A3c' -SimpleMatch -CaseSensitive | Measure-Object).Count"
     ```
     → **≥ 5**: a linha da tabela mais as quatro citações novas. **Medido antes: 1**.
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'chega **sempre** pelo' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  9. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'a enumeração em prosa entra no guarda' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  10. ```
      python -m pytest tests/ -q
      ```
      → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta
      teste. **Medido antes: exit 0** — veredito invariante (critério (xviii)); referência
      **datada**, e não aceite: `197 passed` em 2026-09-19.
- **Restrições desta tarefa:** a tabela de guardrails do `README.md` **não** é reescrita — nenhuma
  linha entra, sai ou muda de coluna; o que muda é a prosa que a conta. A tabela do bloco A da
  skill também fica **intocada**: a `A3c` já está lá, e o defeito é das enumerações. Nenhum
  guardrail novo é criado. Nenhum card do plano é reescrito. `GOVERNANCA.md` §7 não é tocado: ele é
  a fonte, e está certo.
- **Não fazer:** não estender o guarda para outras seções do `README.md` (a classe é conhecida, mas
  o alvo deste card é a seção *Os guardrails*); não tocar `.claude/tools/card_check.py`; não criar
  fixture sintética de kit para provar o guarda (o `-Root` existe, e a prova do mundo sem a mudança
  são os itens de literal); não commitar.
- **Contingências:**
  1. se a recontagem da coluna *Como é enforceada* der números diferentes de **7**, **13** e **1**
     no despacho (alguém mexeu na tabela) → **usar os números medidos no ato**, escrever a frase
     com eles e **reportar a divergência no retorno**: o aceite é a identidade
     `teste + gate - ambos + permissão = total`, não os três literais;
  2. se `pwsh -NoProfile -File .claude/checks/check-readme.ps1` já sair **exit 1** antes de
     qualquer edição → parar e sinalizar `blocked` razão `premissa`, citando a saída: o guarda
     estaria quebrado por outra causa, e este card não a investiga.
- **Pronto quando:** as duas frases do `README.md` dizem a verdade e o guarda as **lê**; a `A3c`
  aparece nas três enumerações da skill e o advérbio `sempre` saiu do bullet de parada; a linha do
  `CHANGELOG.md` existe; e as **dez** linhas de `Verificação` saem nos valores declarados.

### LM-T13 — O contrato de razão do escritor: não se emite o que o leitor não relê [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-30` (2026-09-19), pendência do laudo da `LM-T4c` roteada
  pelo `B1`. Não depende de nada e nada depende dela.
- **Esforço:** low
- **Objetivo:** um só — fechar a assimetria medida entre o **leitor** e o **escritor** de `razão` em
  `.claude/tools/backlog.py`. A `LM-T4c` deu ao leitor a fronteira estrita (`([^—]+?)`: razão não
  contém travessão) e a Restrição dela congelou o escritor, que segue interpolando `--razao`
  verbatim. O resultado é uma borda **não round-trippável**, medida ponta a ponta no `ESC-30` sobre
  cópia da fixture `verde`: `status ALF-T1 blocked --razao 'premissa — suja'` sai **exit 0** e grava
  `· premissa — suja — cauda viva`; a releitura do mesmo arquivo devolve `razao='premissa'` e
  `cauda='suja — cauda viva'` — o texto do operador migra de campo **em silêncio**.
- **Depende de:** nada.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` — a checagem nova em `transacionar_status`.
  - `tests/test_backlog.py` — os dois TF.
  - `CHANGELOG.md` — a linha do bloco não lançado.
- **Produto do módulo:**
  - **(a) A rota decidida é VALIDAR, não normalizar nem tolerar** (decisão do consultor, `ESC-30`).
    Normalizar mutaria em silêncio o texto que o operador escreveu — é a classe que o `TK-55`
    acumula. Tolerar deixaria uma borda lossy medida no instrumento que o próprio loop usa para
    materializar `A3a`, `A3b` e `A3c`. Validar é fail-closed, custa uma linha e devolve o erro a
    quem pode corrigi-lo. O campo `razão` é **motivo** (`dependencia`, `premissa`, `ferramenta`);
    prosa livre é matéria da **cauda** e da nota, que continuam aceitando travessão.
  - **(b) A checagem, em `transacionar_status`**, ao lado da que já recusa `blocked` sem `--razao` e
    **antes** de qualquer escrita (a função já declara que nenhum arquivo é tocado antes de todas as
    checagens passarem): `razao` contendo o caractere travessão (`—`, U+2014) devolve
    `ResultadoStatus(1, ...)` com mensagem que **nomeia o caractere e o motivo** — a fronteira do
    leitor —, contendo o literal `travessão`. Nenhuma outra transição muda de comportamento.
  - **(c) Os dois TF em `tests/test_backlog.py`**, sobre cópia da fixture `verde` em `tmp_path`,
    nunca contra o repositório: `test_tf_razao_com_travessao_recusada` (exit 1, mensagem citando o
    literal, e **árvore intacta** pela comparação de hashes que o arquivo já usa) e
    `test_tf_razao_legitima_faz_round_trip` (razão sem travessão escrita e **relida igual**, com a
    cauda preservada ao lado).
  - **(d) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal
    `o escritor de razão para de emitir o que o leitor não relê`.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog.py -Pattern 'travessão' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: a checagem nova nomeia o caractere. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'test_tf_razao_com_travessao_recusada' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'test_tf_razao_legitima_faz_round_trip' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog.py -Pattern '([^—]+?)' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**, **inalterado**: o leitor **não** é tocado por esta tarefa — quem muda é o escritor.
     **Medido antes: 1**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'o escritor de razão para de emitir o que o leitor não relê' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  6. ```
     python -m pytest tests/test_backlog.py -q
     ```
     → verde, com **dois testes a mais** que o total re-medido no despacho (`DM-23`).
     **Medido antes: exit 0** — veredito invariante (critério (xviii)); referência **datada**, e não
     aceite: `47 passed` em 2026-09-19.
  7. ```
     python -m pytest tests/ -q
     ```
     → verde, **sem reduzir** o total re-medido no despacho. **Medido antes: exit 0** — veredito
     invariante; referência **datada**: `197 passed` em 2026-09-19.
- **Restrições desta tarefa:** o **leitor** não muda — `STATUS_BULLET_RE` fica literal, e é isso que
  a `Verificação` 4 tranca. A cauda e a nota continuam aceitando travessão: o contrato novo é só do
  campo `razão`. Nenhum outro verbo do instrumento ganha validação nesta tarefa. Nenhum card do
  plano é reescrito. `docs/plans/P-0739-backlog-instrumento.md` não é tocado (plano estacionado).
- **Não fazer:** não normalizar, substituir nem escapar o travessão — a rota decidida é recusar; não
  estender a recusa a outros caracteres (`·` round-trippa, medido no `ESC-30`); não tocar
  `card_check.py` nem `check-readme.ps1`; não commitar.
- **Contingências:**
  1. se a recusa nova fizer qualquer teste existente ficar vermelho → **parar** e sinalizar
     `blocked` razão `premissa`, citando o teste: haveria um chamador legítimo emitindo travessão em
     `razão`, e isso muda a rota decidida neste card;
  2. se `transacionar_status` já recusar travessão no despacho → parar e sinalizar `blocked` razão
     `premissa`: alguém fechou a borda antes, e o card ficou sem objeto.
- **Pronto quando:** `--razao` com travessão sai **exit 1** sem tocar arquivo nenhum, a razão
  legítima faz round-trip com a cauda preservada, os dois TF existem, o leitor está intacto, a linha
  do `CHANGELOG.md` existe e as **sete** linhas de `Verificação` saem nos valores declarados.


### LM-T14 — A superfície do próprio guarda: a enumeração que ele não fechou e o numeral que para em vinte [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-30` (2026-09-19), veículo declarado do `AE-52` e do limite
  medido do `$numeralMap`. Não depende de nada e nada depende dela.
- **Esforço:** low
- **Objetivo:** um só — fechar, em `.claude/checks/check-readme.ps1`, os dois resíduos que a
  `LM-T12` deixou **no próprio arquivo que ela estendeu**: (a) a enumeração em prosa do
  `.SYNOPSIS`/`.DESCRIPTION` segue dizendo *"qualquer uma das 5 checagens mecânicas abaixo"* e
  listando `1..5`, sem a checagem `4b` que a `LM-T12` acrescentou — o card que fecha a classe
  reproduziu a classe (`AE-52`); (b) o `$numeralMap` vai só até `vinte` e a captura do numeral é de
  **um token** (`^(\S+) regras`), de modo que na vigésima primeira regra a frase por extenso
  (*"Vinte e uma regras mínimas obrigatórias"*) é lida como `Vinte` e o guarda falha com `20 vs 21`.
  É **fail-closed** — não há falso verde, e isso foi medido —, mas a mensagem acusa divergência onde
  há vocabulário curto.
- **Depende de:** nada.
- **Arquivos-alvo:**
  - `.claude/checks/check-readme.ps1` — o bloco de documentação e o vocabulário de numerais.
  - `CHANGELOG.md` — a linha do bloco não lançado.
- **Produto do módulo:**
  - **(a) A enumeração fechada no mesmo ato.** O literal `das 5 checagens mecânicas` vira
    `das 6 checagens mecânicas`, e a lista `1..5` ganha o item `6.`, cuja primeira oração é, verbatim:
    `As duas frases de contagem em prosa da seção "Os guardrails"` — seguida da descrição do que a
    checagem confere: o numeral da frase de regras mínimas obrigatórias igual ao número de linhas da
    tabela, e os numerais da frase das três formas iguais às contagens derivadas da coluna *Como é
    enforceada*, com a identidade `teste + gate - ambos + permissão` fechando no total. O item
    registra que, no corpo do script, ela vive no bloco rotulado `4b`, por adjacência com a checagem
    de guardrails, e que a numeração da prosa conta **checagens**, não rótulos.
  - **(b) O numeral deixa de parar em vinte.** Duas mudanças, juntas, porque uma sem a outra não
    resolve: a captura do numeral da frase de regras passa de `^(\S+) regras mínimas obrigatórias`
    para `^(.+?) regras mínimas obrigatórias` (forma composta é mais de um token), e o `$numeralMap`
    ganha as entradas de `vinte e um` a `trinta`, **incluindo as formas femininas** de um e dois
    (`vinte e uma`, `vinte e duas`), já que a frase concorda com *regras*. O ramo de dígito
    (`^\d+$`) e o `ToLower()` que o script já aplica ficam como estão, e a mensagem de vocabulário
    passa a dizer até onde o mapa vai.
  - **(c) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal
    `o guarda passa a contar acima de vinte`.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'das 6 checagens mecânicas' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'das 5 checagens mecânicas' -SimpleMatch | Measure-Object).Count"
     ```
     → **0** (a contagem falsa não sobrevive). **Medido antes: 1**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'As duas frases de contagem em prosa' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**: o item novo da enumeração. **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'vinte e uma' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: o mapa passou de vinte, com a forma feminina. **Medido antes: 0**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '^(.+?) regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**: a captura aceita a forma composta. **Medido antes: 0**.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '^(\S+) regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**: a captura de um token não sobrevive. **Medido antes: 1**.
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'o guarda passa a contar acima de vinte' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  8. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0** sobre o repo real, com a seção *Os guardrails* ainda em vinte regras: a mudança do
     vocabulário **não** altera o veredito de hoje. **Medido antes: exit 0** — veredito invariante
     (critério (xviii)).
  9. ```
     python -m pytest tests/ -q
     ```
     → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta
     teste. **Medido antes: exit 0** — veredito invariante; referência **datada**, e não aceite:
     `197 passed` em 2026-09-19.
- **Prova por mutação, fora do repo** (mesma técnica com que o laudo da `LM-T12` provou a checagem
  `4b`; o parâmetro `-Root` existe para isto e **nada** se escreve no repo real): copiar a raiz para
  um diretório temporário; na cópia, acrescentar uma vigésima primeira linha à tabela da seção
  *Os guardrails* e o item correspondente em `GOVERNANCA.md` §7, e escrever a frase como
  `Vinte e uma regras mínimas obrigatórias`; rodar o guarda com `-Root` apontando para a cópia.
  Esperado **exit 0**. Em seguida, na mesma cópia, voltar a frase para `Vinte regras mínimas
  obrigatórias`: esperado **exit 1**, com a mensagem citando `20` e `21`. Os dois resultados vão no
  retorno da tarefa, com as saídas verbatim.
- **Restrições desta tarefa:** nenhuma **checagem** muda de comportamento sobre o repo de hoje — o
  que muda é a documentação do script e o vocabulário de numerais. A frase do `README.md` **não** é
  tocada (ela está certa: são vinte). `GOVERNANCA.md` §7 não é tocado no repo real. A checagem de
  *Anatomia do kit*, que compartilha o `$numeralMap`, não muda de contrato: ela só passa a aceitar
  mais numerais. Nenhum card do plano é reescrito.
- **Não fazer:** não renumerar as checagens do corpo do script (o rótulo `4b` fica); não estender o
  guarda a outras seções do `README.md`; não trocar a frase por extenso por dígito no `README.md`;
  não commitar.
- **Contingências:**
  1. se `pwsh -NoProfile -File .claude/checks/check-readme.ps1` já sair **exit 1** antes de qualquer
     edição → parar e sinalizar `blocked` razão `premissa`, citando a saída;
  2. se a prova por mutação **não** sair `exit 0` com a forma composta depois da mudança → **parar**:
     a captura ou o mapa estariam errados, e publicar o guarda assim seria falso verde sobre a
     própria correção.
- **Pronto quando:** a enumeração do script diz **seis** e descreve a checagem das duas frases; o
  vocabulário passa de vinte com a forma composta capturada; a prova por mutação saiu nos dois
  sentidos; a linha do `CHANGELOG.md` existe; e as **nove** linhas de `Verificação` saem nos valores
  declarados.

### LM-T15 — O vocabulário do guarda, nos quatro sítios: aceite por ausência, não por presença [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-32` (2026-09-19), resíduo medido da própria `LM-T14`
  (`AE-57`). **Não é investimento novo: é a terminação da entrega de ontem** — a distinção que o
  `ESC-31` usou para adiar a atribuição por hunk (construir capacidade nova para servir poucas
  revisões) **não** se aplica aqui, porque nada se constrói: fecha-se o que já foi aberto.
- **Esforço:** low
- **Objetivo:** um só — deixar as **quatro** conferências de numeral do
  `.claude/checks/check-readme.ps1` coerentes entre si. A `LM-T14` estendeu o `$numeralMap` até
  `trinta` e consertou **uma** captura e **uma** mensagem; as irmãs ficaram para trás, e o guarda
  hoje **recusa** um numeral que está no próprio mapa.
- **Depende de:** nada. Nada depende desta.
- **Arquivos-alvo:**
  - `.claude/checks/check-readme.ps1`
  - `CHANGELOG.md` — a linha do bloco não lançado.
- **Produto do módulo:**
  - **(a) As quatro capturas passam a aceitar numeral composto, com âncora que impede a captura
    gulosa.** Literais medidos no `ESC-32` (os quatro foram rodados contra o `README.md` de hoje e
    devolveram, nesta ordem, `nove`, `dez`, `Sete`, `treze`):
    - `(\S+) agentes` vira `^O kit são (.+?) agentes`;
    - `(\S+) skills` vira `agentes, (.+?) skills`;
    - `\*\*(\S+)\*\* regras falham como teste executável` vira
      `^\*\*(.+?)\*\* regras falham como teste executável`;
    - `falham como teste executável, \*\*(\S+)\*\* dependem de gate de review` vira a mesma forma
      com `(.+?)` no lugar de `(\S+)`.

    A âncora não é decoração: `(.+?) agentes` sem ela captura *"O kit são nove"*, porque a busca é
    da posição zero — foi medido antes de prescrever.
  - **(b) As quatro mensagens de vocabulário dizem a mesma coisa.** As **três** que ainda anunciam
    `por extenso até vinte` passam a `por extenso até trinta`, que é o que o mapa entrega desde a
    `LM-T14`. Nenhuma outra palavra das mensagens muda.
  - **(c) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal
    `o vocabulário do guarda fica coerente entre os quatro sítios`.
- **Verificação:** (a forma deste bloco é o produto do `ESC-32`: cada troca de literal vai em
  **par** — presença do novo **e ausência do velho, contada no arquivo inteiro**. A ausência é o
  que cobre os irmãos; a presença sozinha foi o que deixou passar o `AE-52` e o `AE-57`.)
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'por extenso até vinte' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**: nenhum sítio sobra anunciando o teto antigo. **Medido antes: 3**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'por extenso até trinta' -SimpleMatch | Measure-Object).Count"
     ```
     → **4**: os quatro sítios anunciam o mesmo teto. **Medido antes: 1**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '(\S+) agentes' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '(\S+) skills' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '\*\*(\S+)\*\* regras falham' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'falham como teste executável, \*\*(\S+)\*\* dependem' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '^O kit são (.+?) agentes' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**: a captura nova, ancorada. **Medido antes: 0**.
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'o vocabulário do guarda fica coerente entre os quatro sítios' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  9. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0** sobre o repo real, **inalterado**: as contagens de hoje (nove agentes, dez
     skills, vinte regras, sete/treze/uma) continuam conferindo. **Medido antes: exit 0** — veredito
     invariante (critério (xviii)).
  10. ```
      python -m pytest tests/ -q
      ```
      → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta
      teste. **Medido antes: exit 0** — veredito invariante; referência **datada**, e não aceite:
      `201 passed` em 2026-09-19.
- **Prova por mutação, fora do repo** (foi ela que achou o `AE-57`, e é ela que fecha a parte
  **comportamental**, que nenhuma contagem de literal alcança): sobre cópia da raiz num diretório
  temporário, escrever nas **quatro** frases numerais compostos que o mapa conhece — *"O kit são
  vinte e uma agentes"* e *"vinte e duas skills"* na *Anatomia do kit* (com a tabela e o disco
  ajustados para casar), *"Vinte e uma regras mínimas obrigatórias"* e
  *"**vinte e uma** regras falham como teste executável"* na seção *Os guardrails* — e rodar o
  guarda com `-Root` apontando para a cópia. Esperado **exit 0** nos quatro. Em seguida, quebrar
  **um** número de cada vez e exigir **exit 1** a cada quebra, com a mensagem citando o declarado e
  o medido. As oito saídas vão verbatim no retorno da tarefa. Nada se escreve no repo real.
- **Restrições desta tarefa:** o `README.md` **não** é tocado — as frases de hoje estão certas, e a
  prova de numeral composto acontece na cópia. O `$numeralMap` **não** muda: ele já vai a `trinta`.
  Nenhuma checagem muda de veredito sobre o repo de hoje, e a `Verificação` 9 é quem tranca isso.
  Nenhuma seção nova entra na enumeração do `.SYNOPSIS` — a contagem de **seis** checagens continua
  certa, porque nada se acrescenta, só se uniformiza.
- **Não fazer:** não renumerar checagens; não estender o guarda a outras seções; não mexer no
  `README.md` nem em `GOVERNANCA.md`; não tocar `card_check.py`; não commitar.
- **Contingências:**
  1. se alguma das quatro capturas novas devolver token diferente do medido no `ESC-32` (`nove`,
     `dez`, `Sete`, `treze`) no despacho → **parar** e sinalizar `blocked` razão `premissa`, citando
     o token obtido: a âncora estaria errada, e publicar captura gulosa é falso verde;
  2. se a prova por mutação **não** sair `exit 0` com os quatro numerais compostos → **parar**: é o
     mesmo defeito do `AE-57` reaparecendo, e desta vez o card existia para fechá-lo.
- **Pronto quando:** as quatro capturas aceitam numeral composto com âncora provada, as quatro
  mensagens anunciam `até trinta`, a prova por mutação saiu nos dois sentidos para os quatro
  sítios, a linha do `CHANGELOG.md` existe, e as **dez** linhas de `Verificação` saem nos valores
  declarados.

### LM-T16 — A spec conferida contra a árvore: o censo, o consumo e o insumo que ninguém citou [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-37` (2026-09-19), pendência do laudo da `LM-T9` roteada
  pelo `B1`. **O commit do marco 3 espera por ela**: o artefato que o dono lê para validar carrega
  três afirmações que a própria árvore falsifica, e commit congela texto.
- **Esforço:** low
- **Objetivo:** um só — as afirmações factuais de `docs/consultant-spec.md` passam a bater com a
  árvore que as mede. **Nenhum juízo da spec se reabre**: as respostas às perguntas (a)..(h), a
  estrutura e as conclusões ficam **literais**; o que muda são números e o censo, mais a citação do
  insumo que ficou de fora.
- **Depende de:** nada. Nada depende desta.
- **Arquivos-alvo:**
  - `docs/consultant-spec.md`
- **Produto do módulo:** os valores abaixo foram **medidos no `ESC-37`** contra
  `docs/telemetria.tsv` e `## 9` do plano; o executor **transcreve, não recalcula** — e a
  `Verificação` 1 e 8 re-medem por comando, que é o aceite que faltava a este card na primeira vez.
  - **(a) O censo passa de três para quatro instâncias.** O título `As três instâncias medidas` vira
    `As quatro instâncias medidas`, e a tabela ganha a linha que faltava, com estes valores:
    - `1ª` — `9 passagens`, `2.639,1k` tk, `68,5%`, *decisão de janela, cenário coeso* (inalterada);
    - `2ª` — `14 acionamentos`, `3.802,2k` tk, `63%`, *queda por limite de sessão, sem resposta*
      (inalterada);
    - `3ª` — **`4 acionamentos`** (`ESC-23`..`ESC-26`), **`857,7k` tk**, *sucessora provisionada
      após a queda; encerrada por ato do dono no fechamento do marco* — **linha nova**;
    - `4ª` — **`10 acionamentos`** (`ESC-27`..`ESC-36`), **`2.776,3k` tk**, *em curso na medida* —
      é a linha hoje rotulada `3ª`, com o consumo que ela declara não ter.

    A tabela ganha uma coluna **`recorte`**: `3ª` recebe `ESC-23`..`ESC-26` e `4ª` recebe
    `ESC-27`..`ESC-36`. A `1ª` e a `2ª` recebem `—`, com a razão dita em uma linha: elas
    **precedem a marcação `-consultor` na telemetria** (as linhas `ESC-1`..`ESC-21` não a têm),
    então o recorte delas não é derivável da árvore e o ordinal vem do registro em prosa — isso é
    informação para quem lê, não lacuna a preencher por dedução.

    Toda contagem desta tabela leva o **recorte nomeado** *até o* `ESC-36`,
    e **não** *"até agora"*: a série do consultor é incrementada pelo **próprio ato de escalonar**,
    inclusive pelo escalonamento que corrigiu este card (`ESC-38`). Recorte fechado por evento é o
    que devolve a constante à condição de constante.
  - **(b) A frase do consumo não medido cai.** A oração iniciada por
    `A 3ª instância não tem consumo publicado` é substituída pelo fato: a figura **passou a ter**
    linha de telemetria por acionamento, apensada pelo `scrum-master`, e são **`14 linhas de
    telemetria`** (`ESC-23-consultor`..`ESC-36-consultor`) em `docs/telemetria.tsv`, **uma por
    acionamento** — contagem **até o `ESC-36`**, recorte que a própria frase declara. O literal
    `14 linhas de telemetria` é **obrigatório**, porque é ele que a `Verificação` 8 confronta com a
    árvore **dentro do mesmo recorte**. Na `## 9`, a oração `não apensa linha a ele` recebe o mesmo tratamento: o que se
    descreve passa a ser o estado medido, não a ausência.
  - **(c) O total passa de `33` para `37 acionamentos até o ``ESC-36```**
    (`9 + 14 + 4 + 10`), nas **duas** ocorrências do literal `33 acionamentos` — nenhuma sobra, que
    é a regra do par (`ESC-32`), e o recorte entra **junto** do número, pela razão de (a).
  - **(d) A classe de gatilho que o censo omitia entra.** Com a `3ª` instância entra o gatilho do
    `ESC-26` — **ato do dono no fechamento de marco** —, que não é despacho do loop nem laudo: a
    frase `Três classes, todas medidas, e nenhuma outra apareceu` passa a **quatro** classes, com a
    nova nomeada e lastreada.
  - **(e) O `I-3` passa a ser citado.** Dos dez insumos `I-1`..`I-10` de `## 9` do plano, **nove**
    aparecem na spec; falta o `I-3`, medido no `ESC-37` — e é ele que sustenta a pergunta (c). Entra
    na resposta que já o assume, sem reabrir juízo nenhum.
  - **(g) O ordinal sai da prosa: as sete ocorrências passam a nomear o recorte.** `3ª instância`
    aparece **7** vezes em `docs/consultant-spec.md`, **todas** referindo o grupo
    `ESC-27`..`ESC-36` e **todas fora** da tabela (o rótulo de linha é a célula `| 3ª |`, que não é
    esta frase). As sete passam a `instância do recorte` seguido de `ESC-27`..`ESC-36` entre
    crases. **Inclui o título da seção (h)** — *"Panorama medido dos dez acionamentos da 3ª
    instância"* —, cujos **dois** números fecham juntos (`ESC-34`): `dez` continua verdadeiro
    **dentro do recorte nomeado** e permanece; o ordinal sai. Renomear o ordinal em vez de tirá-lo
    da prosa faria o próximo censo renumerar referência de novo — é a classe do `AE-71`, e o que a
    mata é o rótulo deixar de ser posição relativa.
  - **(f) A spec cita o achado de divergência** que a cláusula do card original exigia e que a
    `LM-T9` fechou por veredito em vez de abrir: o ponteiro `AE-69` entra no texto, na seção que
    trata da fronteira entre a figura e a sua definição.
- **Verificação:**
  1. ```
     python -c "import re;from pathlib import Path;p=Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8');m=re.search(r'^## 9\..*$',p,re.M);c=p[m.start():];f=re.search(r'^## 10\.',c,re.M);c=c[:f.start()] if f else c;s=Path('docs/consultant-spec.md').read_text(encoding='utf-8');ins=sorted(set(re.findall(r'\bI-(\d+)\b',c)),key=int);cit=set(re.findall(r'\bI-(\d+)\b',s));print([f'I-{n}' for n in ins if n not in cit])"
     ```
     → `[]`: **todo** insumo de `## 9` é citado na spec. **Medido antes: ['I-3']** — a linha antiga
     contava **linhas** com `I-` na spec contra a **contagem** de insumos do plano, populações
     diferentes, e saía verde com o `I-3` ausente. Esta compara **conjuntos**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'As quatro instâncias medidas' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'As três instâncias medidas' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'A 3ª instância não tem consumo publicado' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'não apensa linha a ele' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern '33 acionamentos' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**: as duas ocorrências fecham juntas. **Medido antes: 2**.
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern '37 acionamentos' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**. **Medido antes: 0**.
  8. ```
     python -c "import re;from pathlib import Path;t=Path('docs/telemetria.tsv').read_text(encoding='utf-8');n=len([m for m in re.findall(r'ESC-(\d+)-consultor',t) if 23<=int(m)<=36]);s=Path('docs/consultant-spec.md').read_text(encoding='utf-8');print('iguais' if re.search(rf'{n} linhas de telemetria',s) else 'divergem')"
     ```
     → `iguais`: o número que a spec publica é **re-medido contra a árvore que o gera**, não
     conferido por presença. **Medido antes: divergem** — veredito **binário** e recorte
     **fechado** (`ESC-23`..`ESC-36`): nenhum dos dois lados envelhece, porque acionamento novo do
     consultor cai **fora** do recorte (`ESC-38`).
  9. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'AE-69' -SimpleMatch | Measure-Object).Count"
     ```
     → **≥ 1**: o ponteiro do achado de divergência. **Medido antes: 0**.
  11. ```
      pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern '3ª instância' -SimpleMatch | Measure-Object).Count"
      ```
      → **0**: nenhuma das sete sobra, e é **uma** linha que cobre **todas** — escopo por
      **ocorrência medida**, não por seção. **Medido antes: 7**.
  12. ```
      pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'instância do recorte' -SimpleMatch | Measure-Object).Count"
      ```
      → **≥ 7**: a forma nova ocupa o lugar das sete. **Medido antes: 0**.
  13. ```
      pwsh -NoProfile -Command "(Select-String -Path docs/consultant-spec.md -Pattern 'dez acionamentos da 3ª instância' -SimpleMatch | Measure-Object).Count"
      ```
      → **0**: o título da seção (h) fecha os **dois** números juntos — `dez` fica, o ordinal sai.
      **Medido antes: 1**.
  10. ```
      python -m pytest tests/ -q
      ```
      → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não toca código.
      **Medido antes: exit 0** — veredito invariante; referência **datada**: `201 passed`.
- **Restrições desta tarefa:** **número de série do consultor não entra sem recorte nomeado** — nem
  no texto da spec, nem em literal de aceite: a série cresce a cada escalonamento, e o ato de
  despachar este card a move. **Nenhum juízo da spec se reabre** — as respostas às oito perguntas,
  a estrutura das seções e as conclusões ficam literais; muda o que a árvore falsifica. Nenhum
  número é **recalculado** pelo executor: os quatro valores de censo e consumo estão prescritos
  acima e foram medidos no `ESC-37`. Nenhum outro arquivo é tocado — nem o plano, nem a telemetria,
  nem os `AE-<n>` (o `AE-69` é registrado pelo loop, e aqui só se cita).
- **Não fazer:** não reescrever a spec; não reabrir a fronteira com o `pantonic-planner` (é matéria
  do plano que o dono declarou); não apagar as linhas `1ª` e `2ª` da tabela; não commitar.
- **Contingências:**
  1. se qualquer um dos quatro valores prescritos divergir da árvore no despacho (a telemetria
     ganhou linha nova) → **usar o medido no ato** e reportar a divergência no retorno: o aceite é a
     `Verificação` 8, que re-mede, não o literal;
  2. se a correção do censo exigir mexer em resposta de pergunta (a)..(h) para não ficar
     contraditória → **parar** e sinalizar `blocked` razão `premissa`, nomeando a resposta: reabrir
     juízo da spec é decisão de consultor, não desta tarefa.
- **Pronto quando:** as quatro instâncias estão na tabela, com coluna de recorte e consumo medido;
  o total leva o recorte; a quarta classe de gatilho está nomeada; o `I-3` é citado; o `AE-69` está
  apontado; **nenhuma das sete ocorrências de ordinal sobra na prosa**; nenhum juízo mudou — e as
  **treze** linhas de `Verificação` saem nos valores declarados, com a 1 e a 8 **re-medindo contra
  a fonte** e a 11 cobrindo as sete de uma vez.

### LM-T17 — Um referente, um rótulo: o censo fecha por token, não por frase [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-19 — card novo do `ESC-40` (2026-09-19), pendência do laudo da `LM-T16`. **É a
  última rodada de correção sobre `docs/consultant-spec.md` neste plano** (teto declarado em `## 6`):
  achado novo depois dela vai ao plano que o dono declarou sobre a figura, não a outro card.
- **Esforço:** low
- **Objetivo:** um só — o mesmo evento deixa de ter dois rótulos no mesmo documento. Hoje a spec diz
  `três instanciações` (`:7`) e `As quatro instâncias medidas` (`:28`), e chama o grupo
  `ESC-27`..`ESC-36` ora de `3ª instância` (`:63-64`) ora de `instância do recorte` (`:134-135`).
- **Depende de:** nada. Nada depende desta.
- **Arquivos-alvo:**
  - `docs/consultant-spec.md`
- **Causa medida, e é do aceite anterior, não da entrega:** a `Verificação` 11 da `LM-T16` usou
  `Select-String -SimpleMatch`, que casa **linha a linha** e não enxerga texto quebrado por
  soft-wrap. A população real de ocorrências era **8**, não 7: `grep -c '3ª instância'` devolve
  **0**, e a regex multilinha `3ª\s+instância` devolve **1**, em `:63-64`. Some-se `:144`
  (*"quatro na 3ª"*), que é referência **sem o substantivo** e escapa de qualquer busca pelo literal
  composto. **Por isso este card afere por token, com regex sobre o texto inteiro** — o rótulo
  `3ª` só pode sobrar **uma** vez, na célula da tabela, e qualquer forma em prosa (quebrada,
  abreviada, com ou sem substantivo) cai na mesma contagem.
- **Produto do módulo:** três substituições, todas com o literal prescrito e medidas no `ESC-40`.
  - **(a) `:7`** — `três instanciações` vira `quatro instanciações`. É a linha do **Método**, e é a
    que contradiz o título da tabela.
  - **(b) `:63-64`** — `Medido no primeiro acionamento da 3ª instância:` (quebrada entre as duas
    linhas) vira `Medido no primeiro acionamento da instância do recorte` seguido de
    `ESC-27`..`ESC-36` entre crases.
  - **(c) `:143-145`** — a frase dos cards autorados fecha **por inteiro** (`ESC-34`), porque
    carrega **três** números e um deles é série que o próprio ato de escrever incrementa: `quatro
    na 3ª` vira `quatro na instância do recorte` + o corte, e `que levou o plano de 29 a 33
    entregas` ganha o recorte — `de 29 a 33 entregas até o` + `ESC-36` entre crases. Sem o recorte,
    o número morre no escalonamento seguinte, que é o `AE-70` de novo; `quatro na 1ª` e `as
    partições de dois cards em três` ficam **literais**, porque são verdadeiros e fechados.
- **Verificação:** (todas por **regex sobre o texto inteiro**, nunca por casamento linha a linha —
  é a lição do `AE-73` posta no instrumento do próprio aceite)
  1. ```
     python -c "import re;from pathlib import Path;print(len(re.findall(r'3ª',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))"
     ```
     → **1**: sobra **só** a célula da tabela. Uma linha cobre **toda** forma em prosa — quebrada,
     abreviada, com ou sem substantivo. **Medido antes: 3**.
  2. ```
     python -c "import re;from pathlib import Path;print(len(re.findall(r'três instanciações',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))"
     ```
     → **0**. **Medido antes: 1**.
  3. ```
     python -c "import re;from pathlib import Path;print(len(re.findall(r'quatro instanciações',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))"
     ```
     → **1**. **Medido antes: 0**.
  4. ```
     python -c "import re;from pathlib import Path;print(len(re.findall(r'instância do recorte',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))"
     ```
     → **9**: as sete de antes mais as duas novas. **Medido antes: 7**.
  5. ```
     python -c "import re;from pathlib import Path;print(len(re.findall(r'33\s+entregas até o',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))"
     ```
     → **1**: o número da série ganha recorte nomeado. **Medido antes: 0**.
  6. ```
     python -c "import re;from pathlib import Path;print(len(re.findall(r'4ª',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))"
     ```
     → **1**, **inalterado**: a prosa **não** troca um ordinal por outro — o rótulo ordinal vive só
     na tabela, onde um recenseamento futuro o corrige na mesma célula do recorte. **Medido antes: 1**.
  7. ```
     python -m pytest tests/ -q
     ```
     → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não toca código.
     **Medido antes: exit 0** — veredito invariante; referência **datada**: `201 passed`.
- **Restrições desta tarefa:** **nenhum juízo da spec se reabre** — respostas, estrutura e
  conclusões ficam literais; muda rótulo e recorte. **Nenhum ordinal novo entra na prosa**: o
  substituto é sempre o recorte. A tabela de `§1` **não** se toca: ela já está correta desde a
  `LM-T16`, e a `Verificação` 6 tranca isso. Nenhum outro arquivo é tocado.
- **Não fazer:** não renumerar o bloco `Verificação` da `LM-T16` no plano (card fechado é registro,
  `DM-33` (iii) — a ordem `1..9, 11, 12, 13, 10` fica como está, com o defeito registrado no
  `AE-73`); não reabrir a fronteira com o `pantonic-planner`; não commitar.
- **Contingências:**
  1. se a contagem de `3ª` no despacho não for **3** → **usar o medido no ato** e reportar: o
     aceite é *sobrar exatamente a célula da tabela*, não o número de partida;
  2. se alguma das três substituições exigir mexer em juízo para não ficar contraditória → **parar**
     e sinalizar `blocked` razão `premissa`, nomeando a passagem.
- **Pronto quando:** `3ª` aparece **uma** vez e só na tabela, `quatro instanciações` substituiu
  `três`, as duas referências novas nomeiam o recorte, a frase dos cards autorados carrega o corte
  `até o` `ESC-36`, nenhum juízo mudou — e as **sete** linhas de `Verificação` saem nos valores
  declarados.






## 6. Ordem de execução

> **Diretiva do dono, 2026-09-18 (posterior à `DM-13`):** a **sequência** abaixo deixa de ser
> vinculante — *"o scrum-master pode executar os cards na melhor ordem, só me interessa a entrega
> validável"*. As **dependências declaradas em cada card** continuam valendo. Texto integral da
> diretiva (consultor de plano, marco validável, commit no marco, toolset do `AE-7`) em
> `docs/DIARIO_DE_OBRAS.md`, bloco *Diretiva de execução do `P-0740`*.

`LM-T1` → `LM-T2` → `LM-T3` → `LM-T4a` → `LM-T4` → `LM-T5` → `LM-T6`.

`LM-T1` e `LM-T2` são independentes entre si e podem trocar de ordem; `LM-T3` exige `LM-T2`;
`LM-T4a` exige `LM-T1` fechada (as duas tocam `.claude/tools/rdo.py` e não podem estar abertas ao
mesmo tempo sobre ele); `LM-T4` exige `LM-T4a` (publicar em doutrina uma gramática que os parsers
ainda rejeitam é o `AE-5` de novo); `LM-T5` exige `LM-T4`, e `LM-T6` exige todas. A ordem
**parser → doutrina → cards** é a `DM-13` e não se inverte.

**Acrescentado pela `RP-5` (2026-09-18), sem fixar sequência — a fila é do `scrum-master`:**
`LM-T1a` e `LM-T7` **não dependem de tarefa nenhuma** e estão despacháveis desde já. Duas
dependências declaradas entram no grafo: (1) **exclusão mútua** entre `LM-T1a` e `LM-T4a` sobre
`.claude/tools/rdo.py` — as duas editam o arquivo em regiões diferentes e não podem estar abertas
ao mesmo tempo, em qualquer das duas ordens; (2) **`LM-T4` passa a exigir `LM-T7`**, porque a
`Verificação` 1 dela pede `check-drift` exit 0 e só a `LM-T7` o recoloca. O plano passa a **9**
tarefas.

**Atualizado pelo `ESC-1` (2026-09-18):** a `LM-T7` foi partida em duas pela fronteira de
permissão (`DM-17` (iii)) — `LM-T7` (projeções, `ready`, sem dependência) e `LM-T8` (definição de
agente, `blocked` por **ato do dono**). A dependência `LM-T4` → `LM-T7` fica **satisfeita pela
parte despachável**; a `LM-T8` **não** entra no caminho crítico de nenhuma tarefa: o item (a)
dela é independente e o item (b) roda depois da `LM-T4`. O plano passa a **10** tarefas, das
quais 9 despacháveis pelo loop.

**Atualizado pelo `ESC-2` (2026-09-18):** a `LM-T7` fechou `done` (ressalva 90%) e o reparo do
`AE-12` entrou como `LM-T7a` (`ready`, `README.md` + `.claude/checks/check-readme.ps1`), que
**não é dependência de nenhuma tarefa** e de nada depende além da `LM-T7` fechada. O plano passa
a **11** tarefas, 10 despacháveis pelo loop (a `LM-T8` segue `blocked` por ato do dono).

**Atualizado pelo `ESC-3` (2026-09-18):** a `LM-T2` foi partida em três (`DM-19` (iii)) —
`LM-T2` (prosa do loop), `LM-T2a` (o verbo `--atribuir`) e `LM-T2b` (o hook) —, e a **`LM-T3`
deixou de depender da `LM-T2`**. Dependências vivas agora: `LM-T2` exige `LM-T2a` (a prosa cita
o comando); `LM-T4a` exige `LM-T1` (fechada); `LM-T4` exige `LM-T4a` e `LM-T7` (fechada);
`LM-T5` exige `LM-T4`; `LM-T6` exige todas. **Exclusões mútuas** (mesmo arquivo, regiões
disjuntas, qualquer ordem): `LM-T2a` × `LM-T3` sobre `review_evidence.py`. Despacháveis sem
dependência nenhuma: `LM-T2a`, `LM-T2b`, `LM-T3` e `LM-T4a`. O plano passa a **13** tarefas, 12
despacháveis pelo loop.

**Atualizado pelo `ESC-4` (2026-09-18):** a `LM-T3` fechou `done` (ressalva 91%) e o reparo do
`AE-15` entrou como **`LM-T3a`** (`ready`, sem dependência), que herda da `LM-T2a` a **exclusão
mútua** sobre `.claude/tools/review_evidence.py` — a da `LM-T3` caducou com o fechamento dela.
Despacháveis sem dependência nenhuma: `LM-T2a`, `LM-T2b`, `LM-T3a` e `LM-T4a`. O plano passa a
**14** tarefas, 13 despacháveis pelo loop.

**Atualizado pelo `ESC-5` (2026-09-19):** fecharam `LM-T4a` (100%) e `LM-T2a` (ressalva 91%).
Com elas, **caiu a última exclusão mútua** sobre `.claude/tools/review_evidence.py` — a `LM-T3a`
é a única tarefa aberta sobre o arquivo — e a `LM-T2` ficou **liberada** (dependia da `LM-T2a`).
Nenhum card novo: o `AE-17` foi absorvido **dentro** da `LM-T3a` (`DM-22` (iii)). Fila aberta,
sem dependência nenhuma: `LM-T2`, `LM-T2b`, `LM-T3a`. Com dependência: `LM-T4` (exige `LM-T4a`,
fechada, e `LM-T7`, fechada — **liberada**), `LM-T5` (exige `LM-T4`), `LM-T6` (exige todas).
`LM-T8` segue `blocked` por ato do dono. O plano segue com **14** tarefas, 6 fechadas.

**Atualizado pelo `ESC-6` (2026-09-19):** a `LM-T2` está em **`review`** — entrega na árvore,
aguardando o `pantonic-reviewer`, sem redespacho de executor (`AE-19`). Nenhum card novo, nenhuma
dependência nova. Fila aberta para executor: `LM-T2b`, `LM-T3a` e `LM-T4` (esta última já
liberada, exige `LM-T4a` e `LM-T7`, ambas fechadas).

**Atualizado pelo `ESC-7` (2026-09-19):** a `LM-T2` fechou `done` **aprovada 100%** e o `AE-9`,
órfão desde a `LM-T1`, ganhou residência: card novo **`LM-T2c`** (`ready`, `DM-25`), que **vem
antes da `LM-T4`** — as duas tocam `.claude/skills/scrum-master/SKILL.md` e a `LM-T4` publica
doutrina que cita as tabelas de roteamento. Fila aberta para executor: `LM-T2c`, `LM-T2b`,
`LM-T3a` e, depois da `LM-T2c`, `LM-T4`. O plano passa a **15** tarefas, 7 fechadas.

**Fila da próxima janela, fixada pelo `ESC-8` (2026-09-19) — recomendação, não vínculo (a ordem
é do `scrum-master`, Diretiva item 4):**
`LM-T2d` → `LM-T2b` → `LM-T3a` → `LM-T4` → `LM-T5` → `LM-T6`, com a `LM-T8` correndo **fora da
fila do loop**, quando o dono liberar a permissão.
- **`LM-T2d`** (`ready`, Sonnet, low, prosa) — fecha a partição do bloco A (`AE-20`); **antes da
  `LM-T4`**, exclusão mútua com ela sobre `.claude/skills/scrum-master/SKILL.md`.
- **`LM-T2b`** (`ready`, Sonnet, low, código) — a fórmula do hook (`DM-20`); independente, e
  cada janela sem ela custa correção manual de linha de telemetria por tarefa fechada.
- **`LM-T3a`** (`ready`, Sonnet, low, código) — a borda do `review_evidence.py` (`AE-15`,
  `AE-17`); **sem exclusão mútua viva** — `LM-T2a` e `LM-T3` fecharam, e ela é a única tarefa
  aberta sobre o arquivo. Vale fechá-la **antes do commit do marco**: o `AE-15` só morde depois
  que houver commit entre `<ref>` e `HEAD`.
- **`LM-T4`** (`ready`, Opus, high, doutrina) — exige `LM-T4a` ✓, `LM-T7` ✓, `LM-T2c` ✓ e
  `LM-T2d`; é o fim da baseline do loop.
- **`LM-T5`** (`ready`, Opus, high) — exige `LM-T4`; audita a criação de card com os **onze**
  critérios e reagrupa o `P-0739`.
- **`LM-T6`** (`ready`, Opus + dono, high) — exige todas; é o piloto medido e o veredito do dono.
- **`LM-T8`** (`blocked`, ato do dono) — toolset do planner; não está no caminho crítico de nada.
**Exclusões mútuas vivas:** só uma — `.claude/skills/scrum-master/SKILL.md`, entre `LM-T2d` e
`LM-T4`. A de `.claude/tools/review_evidence.py` **caducou** com o fechamento da `LM-T2a`.

**Atualizado pelo ato do dono (2026-09-19), sobre o relatório de encerramento da janela:** o marco 1
foi **commitado** em `6eebccd` (oito entregas + `BKL-T4`, suíte 165 verde), e o recorte de evidência
passa a ser `--desde 6eebccd`. Consequência do `AE-15`, agora ativa: há commit entre `<ref>` e
`HEAD`, e o próximo dossiê gerado sofre o defeito até a `LM-T3a` fechar — **a `LM-T3a` sobe ao topo
da fila**, à frente da `LM-T2d` e da `LM-T2b`, que não têm urgência de ordem. Duas tarefas entram no
grafo: a **`LM-T8`**, liberada por `DM-27`, com o item (a) despachável a qualquer momento e fora do
caminho crítico; e a **`LM-T9`** (`DM-29`), **penúltima**, atrás da `LM-T6`. O plano passa a **17**
tarefas. Fila recomendada: `LM-T3a` → `LM-T2d` → `LM-T2b` → `LM-T4` → `LM-T5` → `LM-T6` → `LM-T9`,
com `LM-T8` (a) corrida em qualquer janela. A ordem segue sendo do `scrum-master` (Diretiva item 4);
o que esta atualização fixa são **dependências**, não sequência.

**Atualizado pelo `ESC-9` (2026-09-19, `pantonic-consultant`, `DM-32`):** entra a **`LM-T2e`** —
a ação da `A7`, residência única do `AE-22` —, e o plano passa a **18** tarefas. Ela vai **à
frente da `LM-T2b`**: a `LM-T2d` deixou no
`.claude/skills/scrum-master/SKILL.md` uma afirmação **falsa sobre a própria tabela** (a frase de
partição diz que nenhuma regra manda fechar o que o instrumento recusa, e a `A7` ainda manda), e
superfície publicada do kit não fica com contradição viva enquanto corre tarefa que não depende
dela — a `LM-T2b` não toca esse arquivo e nada perde no adiamento. Fila recomendada:
`LM-T2e` → `LM-T2b` → `LM-T4` → `LM-T5` → `LM-T6` → `LM-T9`, com `LM-T8` (a) corrida em qualquer
janela (`LM-T3a` e `LM-T2d` fecharam em 2026-09-19, as duas aprovadas 100%). **Exclusão mútua
viva, atualizada:** `.claude/skills/scrum-master/SKILL.md`, agora entre **`LM-T2e`** e `LM-T4` —
a da `LM-T2d` caducou com o fechamento dela.

**Atualizado pelo `ESC-12` (2026-09-19, `pantonic-consultant`, `DM-35`):** entram **três** cards
e o plano passa a **21** tarefas. Fila recomendada: **`LM-T4b`** → `LM-T4` → **`LM-T3b`** →
`LM-T5` → `LM-T6`, com **`LM-T2f`** e `LM-T8` (a) corridos em qualquer janela e a `LM-T9` à
escolha do loop (não é insumo do veredito do dono). Razões, todas medidas no `ESC-12`: a
`LM-T4b` vem **antes da `LM-T4`** porque doutrina não publica gramática que o parser recusa
(medido: **0** bullets de `Status` do plano são lidos pelo instrumento, de 21); a `LM-T3b` vem
**antes da `LM-T6`** porque o piloto exercita a autoridade mecânica da dimensão `escopo`, hoje
inflada (9 alvos declarados onde o card lista 2). **Exclusão mútua viva:** continua sendo uma
só, `.claude/skills/scrum-master/SKILL.md`, agora sem par aberto — `LM-T4b` toca
`backlog.py`, `LM-T3b` toca `rdo.py`, `LM-T2f` toca `tests/test_telemetria_hook.py`, e nenhuma
das três colide com a `LM-T4`. **Marco da janela:** a **`LM-T6`** (Diretiva item 2) — é a única
tarefa cujo produto é o **veredito do dono**.

**Atualizado pelo `ESC-13` (2026-09-19, `pantonic-consultant`, `DM-36`):** o loop **antecipou a
`LM-T5`** pela Diretiva item 4, e o consultor **endossa**: três cards seguidos parados por linha
de aceite, sete achados da mesma família na janela, e a `LM-T5` é a auditoria que os fecha. Para
que a antecipação seja possível, a dependência `LM-T5 → LM-T4` foi **dissolvida** (medida: a
gramática que a rubrica afere é a dos **parsers**, ensinada pela `LM-T4a`, fechada) e a `LM-T5`
foi **partida**: a rubrica fica nela; o reagrupamento do `P-0739` vai para a **`LM-T5a`**, nova,
atrás da `LM-T5` e da `LM-T4`. O plano passa a **22** tarefas. Fila recomendada: **`LM-T5`** →
`LM-T4b` → `LM-T4` → `LM-T3b` → `LM-T6`, com `LM-T2f`, `LM-T8` (a), `LM-T9` e `LM-T5a` fora do
caminho crítico do marco — a `LM-T5a` inclusive cabe na janela seguinte, porque o `P-0739` está
estacionado por ato do dono. **Condição que o consultor acrescenta:** fechada a `LM-T5`, a
`LM-T4b` e a `LM-T4` são **re-varridas** sob os critérios (xii) e (xiii) da rubrica antes do
despacho — varredura de consultor, e é o que o `AE-14` ensinou sobre card sobrevivente.

**Atualizado pelo `ESC-14` (2026-09-19, `DM-37`):** entra a **`LM-T5b`** (`card_check.py`), logo
atrás da `LM-T5`, e o plano passa a **23** tarefas. Fila recomendada: `LM-T5` → **`LM-T5b`** →
`LM-T4b` → `LM-T4` → `LM-T3b` → `LM-T6`. A re-varredura prometida no `DM-36` (vi) passa a ser
**mecânica**: o loop roda `card_check.py` sobre a `LM-T4b` e a `LM-T4` antes de despachá-las, e
o consultor entra só no que o instrumento recusar. `LM-T2f`, `LM-T8` (a), `LM-T9` e `LM-T5a`
seguem fora do caminho crítico do marco, que continua sendo a **`LM-T6`**.

**Atualizado pelo `ESC-16` (2026-09-19, `DM-39`):** entra a **`LM-T5c`** — o reparo do
`card_check` e a emenda da `### 8.1` — e o plano passa a **24** tarefas. Fila recomendada:
**`LM-T5c`** → `LM-T4b` → `LM-T4` → `LM-T3b` → `LM-T6`. Ela vem **primeiro** porque todo
despacho feito antes dela é pago em re-derivação manual de baseline pelo loop, e porque a
`### 8.1` publicada prescreve um gate cujo instrumento, hoje, pode dar **verde a item que não
leu**. **Gate suspenso em efeito** (`DM-39` (ii), decisão do loop endossada pelo consultor):
até a `LM-T5c` fechar, o `card_check` é **apoio** no gate de delegação e a conferência dos três
elementos é **manual**, como a própria `### 8.1` prescreve para o período sem instrumento — a
`LM-T4b` e a `LM-T4` **não** exigem `card_check` verde no despacho.

**Atualizado pelo `ESC-17` (2026-09-19, `DM-40`):** a cadeia do `card_check` **para aqui**
(rota (b) da pergunta do loop). Entra só a **`LM-T5d`** — a nota de suspensão do gate na
`### 8.1` —, **fora do caminho crítico e não antes do marco**; o plano passa a **25** tarefas.
As duas matérias do `AE-33` ficam **abertas**, para o planejamento pós-marco, porque são
re-especificação e não conserto (`DM-40` (ii)). Fila recomendada até o marco: `LM-T4b` →
`LM-T4` → `LM-T3b` → `LM-T6`, sem nada de instrumento no meio. **Atenção ao marco:** a
`LM-T6` carrega um **impedimento estratégico declarado** no topo do card — o `Entregável` dela
supõe a fila de módulos do `P-0739`, que a `LM-T5` não produz mais (`DM-36` (iii)) e que
exigiria desestacionar aquele plano contra ato do dono. A escolha entre desestacionar o
`P-0739` e mudar o **veículo** do piloto é do dono, e sobe no relatório de encerramento; até
lá o corpo do card fica intocado.

**Atualizado pelo `ESC-19` (2026-09-19, `DM-42`):** a `LM-T4b` fechou e o plano passa a **26**
tarefas com a **`LM-T4c`** — a fronteira entre razão e cauda no bullet de `Status` —,
**declarada pós-marco**: o caminho que perde a prosa é **latente**, não vivo, porque o `AE-29`
faz `backlog.py status` morrer antes de chegar nele para card deste plano (medido). Fila até o
marco, **inalterada**: `LM-T4` → `LM-T3b` → `LM-T6`. Fora do caminho crítico: `LM-T4c`,
`LM-T5d`, `LM-T2f`, `LM-T8` (a), `LM-T9` e `LM-T5a`. **Ressalva operacional enquanto a
`LM-T4c` não fechar:** não se usa `backlog.py status` para tirar card de `blocked` — que é,
medido, o que já acontece.

**Atualizado pelo `ESC-21` (2026-09-19, `DM-44`):** a `LM-T4` fechou **aprovada 100%** — skills
**11 → 10**, guardrails **18 → 19**, projeções regeneradas (conferido: `check-readme.ps1` sai
exit 0 com *9 agentes, 10 skills, 19 guardrails*) — e o plano passa a **27** tarefas com a
**`LM-T4d`**, a regularização da citação **por nome** que a aposentadoria deixou. Recomendo-a
**antes da `LM-T3b`**, por urgência assimétrica medida: o `bootstrap-pantonic` manda copiar
skill que não existe mais, e o kit se propaga a cinco derivados; a `LM-T3b` não tem urgência e
o marco está travado no dono de qualquer forma. A ordem segue sendo do loop (Diretiva item 4).
**Ato do dono a nomear no relatório:** `.claude/settings.json` linhas 5-6, com regras de `Edit`
sobre os dois diretórios apagados — inócuas, mas fora do alcance de card (`DM-44` (iii)).

**Atualizado pelo `ESC-23` (2026-09-19, `DM-46`):** a **`LM-T8`** sai de `blocked` e volta a
`ready`, **inteira** — some a partição informal *"`LM-T8` (a)"* que as linhas acima carregavam:
ela existia porque o item (b) esperava a `LM-T4`, que fechou, e porque o card tinha dois estados
de executabilidade, defeito que o reparo fechou. Um despacho só fecha o card. O cabeçalho passa a
`Sonnet · classe mecanica` (era `Opus + dono`): o ato do dono foi feito (`DM-27`) e o que resta é
transcrição literal. A `LM-T8` continua **fora do caminho crítico** de qualquer tarefa e pode
correr em qualquer janela. Nada mais muda na fila.

**Atualizado em 2026-09-19 (`DM-47`, `DM-48`):** o **marco destravou**. A `LM-T6` foi reescrita
para o veículo (B) e passa a `ready` **sem dependência aberta** — o corpus é a execução deste
próprio plano, fechada e medida, e o `P-0739` sai do grafo de vez: não é dependência da `LM-T6` e
não volta a ser. Cai com isso a `LM-T5a` do caminho do marco (`DM-45` (i)). Fila até o encerramento:
**`LM-T6` → `LM-T9`**, com `LM-T4c`, `LM-T5d`, `LM-T8` e `LM-T5a` fora do caminho crítico. A
`LM-T8` segue `blocked` razão `permissao` pelo `AE-42` — **não** por defeito de card: o reparo do
`ESC-23` está intacto, o gate sai exit 0, e o que falta é ato do dono sobre o classificador do
harness, já na fila do relatório de encerramento. A ordem continua sendo do loop (Diretiva item 4).

**Atualizado pelo `ESC-26` (2026-09-19, `DM-50`):** o **marco fechou** — `LM-T6` `done`, veredito
do dono **APROVADO**, gate independente `aprovado 100%`. O plano ganha **duas** tarefas, `LM-T10` e
`LM-T11`, e a fila da **próxima janela** é: **`LM-T10` → `LM-T11`**, nessa ordem e sem nada entre
elas — a `LM-T11` edita `.claude/agents/pantonic-executor.md`, que é a superfície recusada, e só o
instrumento da `LM-T10` a torna editável. **Ponto de parada declarado:** se a `LM-T10` fechar
`blocked` pela contingência 1 dela (o executor também recusado ao rodar o instrumento), a `LM-T11`
**não se despacha** — volta ao consultor com a medida da recusa, e é com ela que se escolhe entre
as saídas (b) e (d) da `DM-49` (v). Depois das duas: `LM-T4c`, `LM-T5d` e `LM-T5a`, fora do
caminho crítico, e a **`LM-T9` por último** — a ordem do dono (`DM-29`) manda a spec do consultor
vir depois de a figura ter conduzido o plano, e duas janelas a mais de acionamento são insumo
dela, não atraso. A ordem continua sendo do loop (Diretiva item 4).

**Fila pós-marco — itens de replanejamento** (`DM-49`)

> **O que este bloco é** (`DM-49`): a residência dos **itens de replanejamento** que este plano
> roteou ao pós-marco. Item de replanejamento **não é card** e **não se despacha**: ele nomeia
> matéria que o planejamento seguinte tem de fechar, com o que fecha e o que depende. Card
> declarado pós-marco (`LM-T4c`, `LM-T5d`, `LM-T9`) **não entra aqui** — é card, vive na §5 e tem
> `Status` próprio. O bloco é **aberto**: quem rotear matéria nova ao pós-marco acrescenta a linha
> aqui, em vez de deixá-la só no achado.

- **`PM-1` — a rota da superfície de permissão, e a `description` do `pantonic-planner`.**
  Origem: `AE-45` (i) e (ii), roteados pelo `ESC-25` (`DM-49`). **FECHADO pelo `ESC-26`**
  (2026-09-19): as duas matérias saíram da fila pós-marco e viraram card desta janela. A matéria
  (a) foi **decidida** pelo `scrum-master`, por delegação expressa do dono, e está na `DM-50` —
  a quinta saída, que a enumeração da `DM-49` (v) não tinha: escrita em `.claude/agents/**` por
  **instrumento**, mais a guarda `G-TOOLDENY`. A matéria (b), a `description` falsa, é o **par
  literal** que a `LM-T10` aplica — ela é, ao mesmo tempo, o conserto e a **prova da rota**.
  Residência: `DM-50`, cards `LM-T10` e `LM-T11`. Nada de `PM-1` fica pendente.
- **`PM-2` — as duas matérias de re-especificação do `card_check`.** Origem: `AE-33`, roteado pelo
  `ESC-17` (`DM-40` (ii) e (iii)), com residência no acumulador `TK-55`. Linha de índice: o
  conteúdo **não** se repete aqui — mora no `AE-33` e no `DM-40`.

**Atualizado pelo `ESC-29` (2026-09-19):** entra a `LM-T12` — a enumeração em prosa que nenhum
instrumento lê —, **primeira da fila restante**, antes de `LM-T4c`, `LM-T5d`, `LM-T5a` e da `LM-T9`
(que o `DM-29` mantém por último). Ela **não depende de nada e nada depende dela**; a posição não é
de grafo, é de risco: o item (c) conserta as enumerações da `.claude/skills/scrum-master/SKILL.md`
pelas quais o loop roteia **enquanto roda**, e a `A3c`, publicada na tabela pela `LM-T11`, não está
em nenhuma delas. O plano passa a **30** tarefas.

**Atualizado pelo `ESC-30` (2026-09-19):** entram a `LM-T13` (o contrato de razão do escritor,
pendência do laudo da `LM-T4c`) e a `LM-T14` (a superfície do próprio guarda: a enumeração do `.SYNOPSIS`
que a `LM-T12` não fechou, `AE-52`, e o numeral que para em vinte). **Nenhuma das duas depende de
nada e nada depende delas** — não há restrição de grafo a declarar; as duas são `low` e fecham resíduo
de card já entregue **nesta** janela, o que recomenda executá-las enquanto o cenário está quente:
fila sugerida `LM-T13` → `LM-T14` → `LM-T5d` → `LM-T5a` → `LM-T9` (`DM-29` mantém a `LM-T9` por
último), e a ordem segue sendo do `scrum-master`. Uma exclusão mútua a observar: `LM-T13` e `LM-T14`
tocam arquivos distintos (`backlog.py` e `check-readme.ps1`) e podem trocar de ordem sem conflito.
O plano passa a **32** tarefas.

**Atualizado pelo `ESC-32` (2026-09-19):** entra a `LM-T15` — o vocabulário do guarda nos quatro
sítios —, **primeira da fila restante**: ela termina a entrega da `LM-T14`, e terminar não é investir.
Fila sugerida `LM-T15` → `LM-T5d` → `LM-T5a` → `LM-T9` (`DM-29` mantém a `LM-T9` por último). Nenhuma
dependência nova entra no grafo. O plano passa a **33** tarefas.

**Marco 3, declarado pelo `ESC-32` porque o plano não o declarava:** o marco 1 foram os oito módulos
(`6eebccd`), o marco 2 foi o piloto medido e o veredito do dono na `LM-T6` (`f1afbd3`), e o **marco 3
é o fechamento do plano na `LM-T9`** — `33/33`, com `docs/consultant-spec.md` como o artefato que o dono
lê para validar (`DM-29` põe a `LM-T9` por último exatamente por isso). Não há marco intermediário entre
a `LM-T14` e o fim: as quatro tarefas restantes são regularização de superfície e reagrupamento, nenhuma
com produto que o dono valide sozinho. **Consequência para a janela:** ela segue até a `LM-T9`, e o
commit único do marco 3 acontece lá (Diretiva de execução, item 3) — a menos que a capacidade do
contexto de quem conduz imponha parada antes, que é decisão do `scrum-master` e não do plano.

**Atualizado pelo `ESC-33` (2026-09-19) — teto de saturação para `.claude/checks/check-readme.ps1`:**
o `AE-59` (o `$numeralMap` definido dentro do `else` do bloco *Anatomia do kit* e consumido de fora
pelo bloco `4b`) **não** abre card neste plano, e **nenhuma matéria nova sobre esse arquivo abre card
no `P-0740`** — acumula no tíquete pós-marco. **Teste de saturação aplicado** (vale como regra geral,
aplicado aqui a esta superfície): uma superfície satura quando o achado seguinte **exige precondição
mais rara que o anterior** e o **veredito do instrumento se manteve correto** em todos os mundos
medidos. A série mede isso: `AE-51` era falso no instante da publicação, num contrato que o adotante
lê; `AE-52` era interno ao docstring; `AE-57` morde na vigésima primeira regra; `AE-59` morde apenas
se o `README.md` perder um título de seção — mundo em que as checagens 1, 2 e 5 também caem e o
guarda **já** sai `exit 1`. Em nenhum deles houve falso verde: o `AE-59` é fail-open em **diagnóstico**
(exceção em vez de mensagem nomeada) e fail-closed em **veredito**. E, pelo teste que o `ESC-32`
fixou, ele é **capacidade e não término**: o acoplamento é anterior à trinca `LM-T12`/`LM-T14`/
`LM-T15` e nenhuma delas o abriu — logo vale a mesma resposta do `ESC-31`, que adiou capacidade de
retorno remoto a três tarefas do marco. **Reparo já desenhado e medido, para quem o planejar não
começar frio:** o `$numeralMap` é literal de hashtable **sem dependência** de estado da seção (o
primeiro uso de `$countLine` vem depois dele), então o conserto é **hoisting** para o escopo do script,
acima do primeiro consumidor — mudança de posição, não de comportamento, que devolve ao bloco a
mensagem `Seção 'Anatomia do kit' não encontrada` que ele já tem escrita. Fila inalterada:
`LM-T5d` → `LM-T5a` → `LM-T9`, e a `LM-T9` é o marco 3.

**Atualizado pelo `ESC-34` (2026-09-19):** a `LM-T5a` volta de `blocked` razão `premissa` com a
**partição prescrita** (três módulos, `BKL-T10`/`BKL-T11`/`BKL-T12`, com o mapeamento de matéria, a
ordem e o encerramento do `AE-10` pelo `AE-47`) — o bloqueio foi conduta correta: decidir partição é
planejamento, não execução. Fila final: `LM-T5a` → `LM-T9` (marco 3). **O teto de saturação do
`AE-60` passa a cobrir também `docs/RUBRICA_DE_REVISAO.md` e `.claude/tools/review_evidence.py`:
matéria de contagem em prosa e de citação por faixa de linha nesses dois arquivos **não abre card
no `P-0740`** — acumula no tíquete pós-marco, pelo mesmo teste (precondição mais rara, veredito
correto, nenhum instrumento lendo a prosa, nenhum falso verde). **Regra de prescrição adotada no
mesmo ato, e esta é para quem escreve card daqui em diante:** card que manda fechar uma frase de
contagem manda re-derivar a **frase inteira**, e a `Verificação` carrega a **ausência de cada
expressão numérica antiga dela** — não só da que o autor lembrou. Caso medido: a `LM-T5d` soletrou
`de quinze para dezoito` e deixou, na **mesma frase**, `e não um décimo sexto critério`, que sobreviveu
defasado com dezoito critérios na tabela (`AE-61` item (i)) — é a regra do par do `ESC-32` aplicada
**dentro** da frase, não entre irmãos.

**Atualizado pelo `ESC-35` (2026-09-19) — decisão e transcrição se separam:** a `LM-T5a` bloqueou
pela segunda vez, e o obstáculo não era redação: a matéria da `BKL-T8` aponta para `proximo-passo` e
`handover`, que **a `LM-T4` deste plano aposentou e removeu** (`f1afbd3`), e o aceite herdado dela
(`≥ 3` arquivos com `backlog.py` em `.claude/skills/`) ficou inalcançável (`AE-64`). O card passa a
entregar **a decisão** — partição do `ESC-34`, mapa de herança e regra de re-derivação do número —,
e a **transcrição** dos três módulos vira o **primeiro ato da retomada do `P-0739`**, quando a árvore
estiver parada. O critério é o mesmo do `ESC-34`, aplicado com mais precisão: **decisão** carrega
contexto e envelhece se adiada; **transcrição** mede árvore e envelhece se antecipada.

**Varredura de superfície morta, feita uma vez pelo consultor no `ESC-35` e não se repete:** todos
os caminhos citados pelos cinco cards `ready` do `P-0739` foram confrontados com a árvore de hoje.
**Mortos: exatamente dois**, ambos pela `LM-T4` — `.claude/skills/proximo-passo/SKILL.md` e
`.claude/skills/handover/SKILL.md`. **Herdeira: `passagem-de-bastao`** (ratificação do que a `LM-T4`
já fez, com a parte de condução do loop ficando no `scrum-master`). Não são alvo morto, apesar de
ausentes: `backlog_hook.py` (arquivo a **criar** pela matéria da `BKL-T7`), `GOVERNANCA_MEMORIAS.md`
(doc global) e os padrões de nome de plano em prosa. **Não há terceira**, e é por isso que a `BKL-T10`
e a `BKL-T12` não vão bater no mesmo obstáculo.

**Marco 3, confirmado:** a `LM-T9` depende só da `LM-T6` (fechada) e **não** depende da `LM-T5a`.
O marco 3 é despachável com ou sem ela.

**Atualizado pelo `ESC-37` (2026-09-19) — o marco 3 se move uma tarefa:** entra a `LM-T16`, que
confere `docs/consultant-spec.md` contra a árvore (censo de instâncias, consumo publicado, total de
acionamentos, classe de gatilho omitida, `I-3` não citado). **O marco 3 passa a ser o fechamento do
plano na `LM-T16`**, e o commit **espera por ela**: o artefato que o dono lê para validar carrega três
afirmações que o repositório falsifica, e commit **congela** texto — é o mesmo argumento do `ESC-36`,
aplicado ao documento mais lido do marco. A `LM-T9` **não** se reabre (está `done`, com RDO); a `LM-T16`
corrige fato medido e **não toca juízo nenhum** da spec. O plano passa a **34** tarefas.

**Por que card e não reparo direto do consultor** (a exceção ao que o `ESC-36` fez): o documento descreve
**a própria figura que o repararia**, e o censo em causa conta as instâncias dela. Quem achou as três
falsificações foi o **reviewer**, olhando de fora; manter a correção sob mão independente e sob gate é
o que sustenta o valor do artefato para quem o lê. O consultor prescreve os literais medidos; não os
escreve no documento sobre si.

**Atualizado pelo `ESC-40` (2026-09-19) — teto prospectivo sobre o artefato da figura:** entra a
`LM-T17` (um referente, um rótulo), o marco 3 passa a ser o fechamento do plano **nela**, e o plano
vai a **35** tarefas. **Esta é a última rodada de correção sobre `docs/consultant-spec.md` neste
plano.** Achado novo sobre esse arquivo depois dela **não abre card**: vai ao plano que o dono
declarou sobre a figura, com o achado registrado. O teto é **prospectivo**, e a razão de ser declarado
agora é de governança, não de cansaço: são quatro rodadas sobre o documento que formaliza a **própria**
figura que decide quantas rodadas fazer, e quem limita esse laço tem de ser a regra escrita, não o
juízo de quem está dentro dele. **O teste de saturação do `AE-60` foi aplicado e NÃO disparou** aqui,
e é por isso que esta rodada acontece: o achado do `ESC-40` **não** exige precondição mais rara — ele
aparece na primeira leitura, na linha do **Método** e na tabela — e o veredito **não** se manteve
correto: o documento afirma `três` e `quatro` instâncias ao mesmo tempo. Contradição interna no
artefato de validação não é resíduo cosmético; é o artefato falhando no que ele existe para sustentar.

## 7. Fora de escopo (explícito)

- **Rodada de corte em fonte nossa** (`CLAUDE.md`, skills, agentes, memória): a §2 mediu que o
  ganho máximo é 0,7 ponto percentual. Não se abre.
- **`TK-54b`** (fonte da bimodalidade de 8.611 tk): segue viva como tíquete, fora deste plano —
  e **despriorizada** por `DM-30`, que tira o custo do posto de critério.
- **`TK-38`** (comunicação agente↔humano): pertinente ao critério novo — é matéria de coerência —,
  mas fora do tema deste plano por `DM-4`/`DM-30`. Evidência nova de 2026-09-19 apensada ao
  tíquete: o dono pediu, em prompt próprio, um glossário de `A10`, `B6` e congêneres para ler o
  próprio relatório de encerramento — **segunda ocorrência medida** da mesma classe, depois da
  `EXA-T25`.
- **Confiabilidade de agente e de instrumento** (a classe que reúne `AE-1`, `AE-3`, `AE-18`,
  `AE-19` e a projeção de índice desatualizada medida em 2026-09-19): fila pós-plano, por ato do
  dono. Insumos acumulam no tíquete, não aqui.
- *(retirado de fora de escopo em 2026-09-18, no mesmo ato de autoria)* — o `AE-10` do `P-0739`
  **não** é mais rodada separada: foi absorvido pela `LM-T5`, que resolve a dependência de ordem
  dentro do reagrupamento. O `P-0739` não recebe rodada de replanejamento própria; ele espera a
  `LM-T5` e fecha na `LM-T6`.
- **Desabilitar ferramentas do harness:** `enableArtifact: false` e `disableWorkflows: true` já
  aplicados em 2026-09-18. `disableBundledSkills` **não** se aplica — é tudo-ou-nada e levaria
  junto `claude-api`, `code-review` e `security-review`.
- **Baixar `effortLevel` global:** decisão do dono, fora deste plano. `DM-5` resolve esforço por
  tarefa, que é o recorte útil.

## 8. Riscos

- **`DM-2` afrouxa o recorte e o card vira tarefa grande disfarçada.** Mitigação: `DM-4` mantém a
  proibição de transversal, e a `LM-T5` existe exatamente para pegar isso antes do despacho.
- **`B0`/`B1` da `LM-T2` passam a deixar passar pendência que deveria parar a janela.** Mitigação:
  a definição é por atribuição de arquivo, mecânica, e `recomendacao=escalar` continua dominante.
- **O piloto da `LM-T6` mede de novo uma tarefa por janela.** Aí o gargalo não era `B1`, e o
  achado é o entregável — desfecho negativo é desfecho.
- **A `LM-T1a` e a `LM-T4a` são despachadas em paralelo sobre `.claude/tools/rdo.py` e uma
  sobrescreve a outra.** Mitigação: a exclusão mútua está declarada nos dois lugares que quem
  despacha lê — no `Depende de` da `LM-T1a` e na §6 —, e as regiões são disjuntas (`argparse`/
  `cmd_close` contra `_HEADER_BRACKET_RE`), então a colisão é de **estado de trabalho**, não de
  conteúdo: basta fechar uma antes de abrir a outra.
- **A guarda da `LM-T1a` recusa um valor que a série histórica já contém e trava um fechamento
  real.** Mitigação: o domínio recusa só negativo e não-finito; a série medida não tem nenhum dos
  dois, e o caminho feliz está trancado por `TR-close-consumo-valido-segue-igual`. Se aparecer,
  o sintoma é exit 1 com a razão nomeada — diagnóstico imediato, não silêncio.

- **Outro card do plano declara `.claude/agents/*` em `Arquivos-alvo` e repete o bloqueio de
  permissão.** Mitigação: `DM-17` (ii) proíbe a declaração, a `LM-T4` já foi emendada e a `LM-T5`
  afere `Arquivos-alvo` contra o filtro do instrumento que julga o card — o caso medido do
  `AE-11` entra como quinto insumo da rubrica, ao lado de `AE-1`, `AE-10`, `AE-2` e `AE-4`.

- **Outro card fecha um item enumerado e deixa a frase da seção contando errado.** Mitigação:
  `DM-18` (i)/(ii) é regra de autoria e de aceite, o critério (viii) da rubrica da `LM-T5` a
  afere card a card, e a `LM-T7a` põe o invariante **no instrumento** — a partir dela o guarda
  pega sozinho, que é o único regime que não depende de ninguém lembrar.

- **Outro card anterior às rodadas `RP-1`..`RP-5` chega ao gate sem ter sido reautorado.**
  Mitigação: sobraram **três** nessa condição (`LM-T4`, `LM-T5`, `LM-T6`) e os pisos delas já
  foram re-medidos aqui; a `LM-T5` audita a criação de tarefa e recebeu o `AE-14` como insumo,
  com a regra explícita de varrer **card sobrevivente**, não só card novo. O custo de pegar tarde
  está medido: a `LM-T2` foi recusada no gate, sem gastar executor.

- **Outro card promete, como teste, uma propriedade que nenhum teste discrimina.** Mitigação:
  `DM-21` nomeia as três saídas legítimas, o critério (ix) da rubrica da `LM-T5` afere card a
  card, e a varredura do `ESC-4` mediu que **nenhum** card vivo está nessa condição hoje — o
  único caso aberto (a `Restrição` da `LM-T2a`) já recebeu o caso discriminante.

- **Outro card vivo carrega número de suíte como aceite e nasce vencido.** Mitigação: `DM-23`
  trocou constante por relação nos quatro cards que ainda a tinham (`LM-T2`, `LM-T2b`, `LM-T3a`,
  `LM-T4`), e o critério (x) da rubrica da `LM-T5` pega o caso na criação. O custo de não ter
  pegado antes está medido: cinco correções manuais em sete despachos, todas no gate, nenhuma
  delas tendo chegado a gastar executor.

- **Outro card publica comando de aceite cujo literal não é o que foi rodado.** Mitigação:
  `DM-24` fixa a forma (bloco cercado, `-SimpleMatch`) e o teste que fecha a classe inteira — os
  **dois** valores rodados, e padrão que dá o mesmo valor nos dois mundos é inválido; o critério
  (xi) da rubrica da `LM-T5` afere. A varredura do `ESC-6` já rodou os comandos de **todos** os
  cards vivos e corrigiu os três que estavam fora (`LM-T2` itens 1 e 3, `LM-T2b` item 3, `LM-T5`
  itens 2 e 3).

- **Outro achado fica órfão porque o card dono da matéria foi reescrito com restrição que a
  exclui.** Mitigação medida aqui: a rota de um `AE-<n>` é **premissa do card que a carrega** —
  quando uma rodada reescreve o card (`ESC-3` partiu a `LM-T2` em três), a rota tem de ser
  reconferida contra as `Restrições` novas. O `AE-9` atravessou seis rodadas com a rota
  "matéria da `LM-T2`" sem que ninguém a reconferisse; custou um ciclo inteiro de tarefa para
  aparecer, e apareceu pelo laudo, não pela autoria. Entra como insumo da `LM-T5`.

- **Regra nova de roteamento nasce sem partição do domínio.** Mitigação: `DM-26` (iv) fixa a
  partição por veredito e a frase entra no arquivo; a lição geral — *toda regra nova de tabela
  declara o que acontece com **cada** valor do domínio que ela toca, e confronta a ação com o
  que o instrumento de fechamento aceita* — é o critério (vii) da rubrica da `LM-T5` aplicado a
  tabela de roteamento, e o caso medido (`AE-20`) entra como insumo dela.

## 9. Insumos do ad-hoc para planejamento futuro

> **O que esta seção é** (`DM-28`, `DM-29`): o registro do que a execução **ad-hoc** mediu sobre uma
> técnica que o framework ainda não tem desenhada. Cada item é um fato da execução, numerado
> `I-<n>`, gravado **quando medido** — não reconstruído no fim. A `LM-T9` os consome e produz
> `docs/consultant-spec.md`. Enquanto a spec não existir, nada daqui é doutrina e nada daqui se
> cita como fonte normativa.

**Técnica em observação:** o **consultor de plano** (`pantonic-consultant`), figura ad-hoc criada
por ato do dono em 2026-09-18. Insumos da janela de 2026-09-18/19, todos medidos:

- **`I-1` — a figura se pagou, e o número diz quanto.** Nove passagens (`RP-5`, `ESC-1`..`ESC-8`)
  num **contexto só**: 2.639,1k tk, 68,5% dos 3.850,3k da janela. Contra o regime anterior — quatro
  rodadas **frias** de planejador (`RP-1`..`RP-4`) que custaram **423,7k tk para fechar UMA**
  tarefa, redescobrindo o mesmo cenário a cada vez. A janela fechou **oito** tarefas a 481,3k/tarefa
  contra 625k/tarefa da anterior.
- **`I-2` — nenhuma das nove passagens releu o plano.** O cenário ficou no contexto; cada passagem
  entrou só com o delta (o laudo e o retorno do executor). É **este** o mecanismo que produziu o
  `I-1`, e não o modelo nem o prompt: o que barateia é a permanência, não a instrução.
- **`I-3` — o que ela absorveu foi autoria de card, não execução.** Onze achados (`AE-8`, `AE-9`,
  `AE-11`, `AE-12`, `AE-14`..`AE-20`) e **nenhum** de execução; oito tarefas despachadas com **zero
  reprovações e zero refações**. As quatro ressalvas vieram de coisa que o card não mandou fazer,
  ou mandou de um jeito que o instrumento não aceita.
- **`I-4` — o domínio de decisão se sustentou sem round-trip com o dono.** Nas nove passagens a
  classificação saiu **técnica ou tática** em todas, e **nada** subiu ao dono como decisão
  (`G-NOASK`). O que subiu foi relatório e um **ato** (a permissão da `LM-T8`) — que é outra coisa.
- **`I-5` — a fronteira com o `pantonic-planner` não está onde a definição diz.** Na prática a
  figura **autorou cards novos** (`LM-T7a`, `LM-T3a`, `LM-T2c`, `LM-T2d`, mais as partições de
  `LM-T7` e de `LM-T2` em três), que é ato de planejamento. O que ela **não** fez em nenhuma
  passagem: reabrir o objetivo do plano. A spec tem de dizer se autorar card é da figura ou
  empréstimo do planner — hoje é fato medido sem regra.
- **`I-6` — ela não funciona sem instrumento de execução.** Nasceu com `Bash` por causa do `AE-7`
  e da `DM-12` (*comando de aceite não se deduz, se roda*), e **três** fechamentos seguidos
  (`ESC-6`, `ESC-7`, `ESC-8`) dependeram disso: em cada um, comandos extraídos do card e rodados
  verbatim antes do despacho pegaram literal corrompido ou piso vencido. Papel de reparo de plano
  sem ferramenta de medida reproduz o `AE-19`.
- **`I-7` — o custo se concentra num papel só, e isso é o risco da figura.** 68,5% da janela.
  Nenhum critério mediu **quando não acionar** — toda pendência substantiva virou passagem, por
  `B1`. A spec precisa da regra de não-acionamento e de um teto, ou a figura vira o gargalo que
  ela removeu.
- **`I-8` — o encerramento foi por decisão de janela, não por poluição.** As nove passagens
  couberam num contexto **coeso** do começo ao fim — um plano, um cenário (Regra 2). O limite de
  formato que a spec tem de nomear é o da **troca de plano**, não o da duração.

- **`I-9` — a figura morre inteira quando o limite chega, e o cenário morre com ela.** Medido no
  `ESC-22` (2026-09-19): o consultor terminou por `rate_limit` HTTP 429 (*session limit*) **sem
  devolver** as duas alocações do `AE-38` nem a varredura final da `LM-T3b`, e a notificação veio
  **sem bloco `<usage>`** — o consumo daquela passagem é `PARCIAL — trecho pré-queda não medido` e
  **nenhuma linha de telemetria** foi apensada por ela, porque telemetria é medida e não estimativa
  (`GOVERNANCA.md` §4.2). O que se perdeu não foi trabalho entregue — o `AE-38` estava registrado e
  a `LM-T3b` foi gateada por medida do loop —, foi o **contexto acumulado de 14 passagens**, que é
  justamente o ativo que justifica a figura existir (`DM-28`, item 1 da *Diretiva*: ela não é
  efêmera). **A ausência de fim de vida é, portanto, defeito estrutural da figura, não incidente.**
  É o lastro da pergunta (g) da `LM-T9`, e da regra nova do dono (`DM-45` (iii)).

- **`I-10` — mede-se o custo do consultor e não se mede a causa dele.** Medido nesta janela: **14
  acionamentos**, **`3.802,2k` tk**, **63%** do total — contra 23% de execução e 14% de revisão.
  `docs/telemetria.tsv` registra **quanto** cada acionamento custou e **nada** sobre *por que ele
  existiu*, que classe de impedimento o motivou ou o que ficou **inconclusivo** ao fim dele. Com
  `I-7` (68,5% na janela anterior), são **duas** janelas em que um papel só concentra a maior parte
  do consumo **sem** que se saiba o que o convoca. É o lastro da pergunta (h) da `LM-T9` e da
  responsabilidade nova do dono (`DM-45` (iv)), e o destino declarado da coleta é a **spec de
  robustez**.

## 10. O piloto medido — a série do loop sobre o próprio plano

Corpus: a execução do próprio `P-0740` sob o loop (veículo (B), `DM-45` (i), `DM-47`). Origem: as **50**
linhas `PantonicApp\tLM-T` de `docs/telemetria.tsv`, re-medidas no despacho (2026-09-19), para consumo,
`tool_uses` e duração; o bullet `- **Status:**` de cada card para veredito; `## 9` e `## Achados da execução` para a regra de parada. Nada estimado.

| módulo | tokens_k | tool_uses | duracao_s | janela |
|---|---|---|---|---|
| LM-T1 | 201,3 | 57 | 599,0 | 1 |
| LM-T7 | 163,2 | 42 | 316,3 | 2 |
| LM-T1a | 164,4 | 55 | 453,8 | 2 |
| LM-T7a | 139,3 | 33 | 515,6 | 2 |
| LM-T3 | 152,0 | 48 | 565,6 | 2 |
| LM-T4a | 147,4 | 60 | 434,9 | 2 |
| LM-T2a | 162,6 | 51 | 524,1 | 2 |
| LM-T2 | 152,1 | 37 | 512,2 | 2 |
| LM-T2c | 130,2 | 33 | 292,0 | 2 |
| LM-T3a | 142,3 | 51 | 352,8 | 3 |
| LM-T2d | 106,2 | 40 | 243,8 | 3 |
| LM-T2e | 98,1 | 23 | 158,5 | 3 |
| LM-T2b | 186,8 | 43 | 517,1 | 3 |
| LM-T4b | 256,8 | 74 | 904,3 | 3 |
| LM-T5 | 250,4 | 56 | 784,7 | 3 |
| LM-T5b | 180,9 | 48 | 683,9 | 3 |
| LM-T5c | 212,7 | 72 | 915,6 | 3 |
| LM-T4 | 468,2 | 151 | 1.366,5 | 3 |
| LM-T4d | 145,6 | 50 | 400,1 | 3 |
| LM-T3b | 154,1 | 52 | 441,6 | 3 |
| LM-T2f | 98,2 | 22 | 165,3 | 4 |
| **total do piloto** | **3.712,8** | **1.098** | **11.147,7** | 21 módulos, 4 janelas |

**Decomposição por papel:** janela 3 — execução `1.389,9k` (**23%**), revisão `812,2k` (**14%**),
consultor `3.802,2k` (**63%**) de `6.004,3k` (`DM-45` (i)); execução e revisão conferem exatas
contra as linhas 21–45 da fatia, e o consultor não apensa linha nenhuma. Janela 2: consultor
`2.639,1k` de `3.850,3k` (**68,5%**, `## 9` `I-1`). Janela 1: planejador frio `423,7k` de `625,0k`.

**Contra a baseline de tarefa atômica:** a `BKL-T4` (§3) custou `284,6k tk / 71 tool uses / 21 min`
por tarefa, medidos em executor + reviewer. Na mesma base, os 21 módulos desta série custam
`176,8k / 52,3 / 8,8 min` por módulo — **37,9% abaixo** em tokens, **26,3% abaixo** em tool uses,
**57,9% abaixo** em duração. Com o papel que a `BKL-T4` não tinha, as janelas 1–3 somam `10.479,6k`
para 20 módulos = `524,0k`/módulo, **84,1% acima** da baseline.

**Módulos fechados por janela, e a regra que encerrou cada uma:**
- **Janela 1** (2026-09-18, `RP-1`..`RP-4`): **1** módulo, `aprovado 100%`. Sem regra de parada
  registrada — o regime mudou com a criação do consultor por ato do dono em 2026-09-18 (`## 9`).
- **Janela 2** (2026-09-18/19, `RP-5`, `ESC-1`..`ESC-8`): **8** módulos — 5 `aprovado 100%`, 3 ressalva, **0** reprovações.
  Encerrou por **decisão de janela, não por poluição** (`I-8`); fato: a nona e última passagem do consultor fechou o cenário e o relatório subiu ao dono (`ESC-8`).
- **Janela 3** (2026-09-19, `ESC-9`..`ESC-22`): **11** módulos — 7 `aprovado 100%`, 4 ressalva, **0** reprovações, **0** retentativas.
  Encerramento declarado na `LM-T3b` e relatado ao dono (`DM-45`); fato: `ESC-22` — o consultor caiu por `rate_limit`
  HTTP 429 (*session limit*) sem devolver o `AE-38` nem a varredura da `LM-T3b`, e a janela seguiu "com o que há".
- **Janela 4** (corrente, 2026-09-19): **1** módulo fechado (`LM-T2f`, `aprovado 100%`) até este despacho; **aberta**, sem
  regra de parada porque não encerrou. Fora da série, na fatia: `LM-T8` (**2** linhas, `blocked` por `permissao`) e `LM-T6` (**1**).

**Divergência medida × corpus declarado (`Contingência` 2):** o corpus do card declara **duas** janelas e **39 linhas**
de `docs/telemetria.tsv` para a de 2026-09-18/19. Medido agora: a fatia tem **50** linhas e a série separa **4** janelas;
a janela de `6.004,3k` é a **3** e ocupa **25** linhas (21–45), com **660** tool uses e **1,88 h** na fatia — os `900` e
as `3,06 h` do corpus contam o consultor, que não apensa telemetria (`ESC-22`). Manda a medida do despacho.

**Veredito do dono:** **APROVADO** (2026-09-19). Dado sobre `docs/MODO_DE_OPERACAO.md` — a
descrição comparada do modo de operação antes e depois dos artefatos, autorada nesta janela a
pedido do dono, porque um piloto em tempo real não era possível. Palavra dele: *"O veredito está
ok, pode dar continuidade do plano."* O aceite é da **medida e do modo de operação descrito**, e
não revoga nenhum dos cinco limites declarados na §6 daquele documento — os caminhos de
recuperação do loop seguem não exercitados, e o corpus segue sendo o próprio repositório do
framework.

## Achados da execução

- **`AE-1` (2026-09-18, aberto no ato do planejamento) — `backlog.py check` não distingue linha de
  índice de linha de tabela ilustrativa.** Medido nesta janela: 315 achados no total, 23 deles em
  regiões do `docs/DIARIO_DE_OBRAS.md` anteriores a esta sessão (portanto pré-existentes) e 35 em
  regiões novas — e **todos os 35 são falsos positivos**, vindos das tabelas de exemplo trabalhado
  dentro do card `### TK-54a` (bloco `C`) e das tabelas do extrato. O lint casa qualquer
  `| <algo> | ...` como linha de índice e emite `C-3` (status fora do vocabulário) e `C-9` (sem
  residência em plano vivo). **Consequência:** o sinal do lint está afogado em ruído, e um `C-3`
  verdadeiro passa despercebido. **Rota:** matéria da `LM-T1` **não** — é do instrumento
  `backlog.py`, que a `BKL-T4` acabou de tocar; encaminhado ao `P-0739` como candidato de rodada,
  junto do `AE-10`. Não se corrige aqui.

- **`AE-2` (2026-09-18, medido no despacho da `LM-T1`) — o entregável (a) da `LM-T1` contradiz
  `.gitignore:7-10`.** O card manda versionar `.claude/estado/` com `.gitkeep`; o `.gitignore`
  exclui o diretório inteiro desde a `T55`, com motivo declarado: "fato de uma sessão numa
  máquina, nunca canônico do framework". As duas afirmações não coexistem — ou o diretório é
  canônico do framework (e o ignore muda), ou não é (e o entregável (a) muda de forma). O executor
  parou em 10 tool uses / 61,8k tk sem tocar arquivo, o que é o comportamento correto de
  `G-EXECREADY`. **Entrada da rodada `RP-1`** (`G-REPLAN`): a decisão é do planejador, e toca
  `.gitignore`, arquivo fora dos `Arquivos-alvo` do card. **ABSORVIDO em 2026-09-18 pela `RP-1`**
  → decisão `DM-10` (o diretório é canônico, o conteúdo não; `.gitignore` passa a
  `.claude/estado/*` + `!.claude/estado/.gitkeep`) e `DM-11` (tipo de `--tokens-k`, ponto vizinho
  que estava aberto no mesmo card). `LM-T1` reescrita e de volta a `ready`; nada pendente neste
  achado.
- **`AE-3` (2026-09-18, medido nesta janela) — o hook `SubagentStop` disparou pela primeira vez e
  gravou consumo divergente do medido.** Com `.claude/estado/tarefa-corrente.json` gravado à mão no
  Passo 4, o hook produziu a linha `2026-09-18 PantonicApp LM-T1 Sonnet 10 319.5 87.3 usage` — mas
  o `<usage>` da notificação mediu **61.794 tk** (61,8k), não 319,5k; e o `modelo` saiu capitalizado
  contra a convenção minúscula da série. A linha foi corrigida à mão nesta janela. **Prova material
  de que o defeito 1 era real** (o hook nunca tinha rodado) e **matéria da `LM-T2`** item (c), que
  já toca `telemetria_hook.py`: o teste do hook tem de fixar a fonte do número e a forma do campo
  `modelo`. Não se corrige aqui.
  **Cinco ocorrências novas, medidas na janela de 2026-09-18** (todas com `fonte=usage`, todas
  **para mais**, todas corrigidas à mão pelo loop): gravou `6242.6k` contra 167,9k medidos;
  `251.1k` contra 59,5k; `505.2k` contra 49,8k; `2330.8k` contra 94,8k; `946.9k` contra 75,3k. E
  **não dispara** quando o subagente é retomado por `SendMessage` — os escalonamentos `ESC-1` e
  `ESC-2` não geraram linha nenhuma. **ABSORVIDO em 2026-09-18 pelo `ESC-3`** → `DM-20`, com a
  fórmula **calibrada** contra seis transcripts reais (acerto de 6/6), e card `LM-T2b` como
  residência. O caso do `SendMessage` fica **fora do alcance do código** e vira linha do Passo 9,
  publicada pela `LM-T2`.

- **`AE-11` (2026-09-18, medido no primeiro despacho da `LM-T7`) — a camada de permissão do
  harness nega a edição de arquivo de definição de agente, e nenhum papel da sessão pode
  contorná-la.** O `Edit` que gravaria `tools: Read, Glob, Grep, Write, Edit, Bash` em
  `.claude/agents/pantonic-planner.md` foi **negado duas vezes**, com instrução explícita de parar
  e explicar em vez de contornar por `Write` ou `Bash`. O executor parou no passo 1 e devolveu
  `blocked motivo=premissa`: 4 tool uses / 59,5k tk, **nenhum arquivo tocado**. As quatro âncoras
  do card, re-derivadas no despacho, bateram **exatamente** com o que a `RP-5` publicou — o card
  estava certo e o mundo é que não admite o ato. **Classe nova de defeito de autoria:** um card
  pode ser impecável em conteúdo e inexecutável por **permissão**; a autoria precisa confrontar o
  entregável com a política de permissão vigente, do mesmo modo que a `RP-1` ensinou a confrontá-lo
  com o `.gitignore` (`AE-2`) e a `RP-2`, com o comportamento real do instrumento de aceite
  (`AE-4`). **ABSORVIDO no mesmo dia pelo `ESC-1`** → `DM-17`, `LM-T7` reescrita (projeções,
  `ready`) e `LM-T8` nova (`blocked`, ato do dono). Insumo medido da rubrica da `LM-T5`.

- **`AE-12` (2026-09-18, pendência do laudo da `LM-T7`) — o card fechou o item e não fechou o
  invariante da mesma seção que o item quebra.** A `LM-T7` acrescentou a nona linha à tabela
  **Agentes** de `README.md` › *Anatomia do kit*; a frase que **conta** essa tabela,
  `README.md:760`, continua dizendo `O kit são oito agentes, onze skills, …`. O card prescreveu a
  linha e não a frase, e **nenhuma das cinco verificações discrimina o vão**: o
  `check-readme.ps1` confronta tabela × disco, **anuncia `9 agente(s)`** e sai **exit 0**.
  Entrega mecanicamente fiel, verde em todo instrumento, arquivo-alvo contradizendo a si mesmo —
  laudo `ressalva` 90%, bloqueante `nenhuma`, única dimensão fora de `conforme`:
  `criterio-de-pronto` `parcial`. **Defeito de autoria, não de execução:** quem escreveu o card
  foi este consultor, no `ESC-1`. **ABSORVIDO no mesmo dia pelo `ESC-2`** → `DM-18`, card novo
  `LM-T7a` (prosa + checagem 5 no `check-readme.ps1`), critério (viii) na rubrica da `LM-T5` e a
  publicação na definição do planner apensada ao item (b) da `LM-T8`. **Sem retroação** sobre a
  `LM-T7`, que fica `done`.
- **`AE-13` (2026-09-18, segundo achado do laudo da `LM-T7`) — o dossiê sem atribuição obrigou
  injeção manual pela segunda vez.** O dossiê apresentou **32** arquivos tocados desde `428246c`,
  entre eles `.claude/agents/pantonic-planner.md` — que o card nomeava na lista *Não fazer* —, e
  a reconciliação só foi possível com a injeção manual da orquestração, confirmada por `mtime`
  (planner 21:42 × alvos 22:56). É o **defeito 6 da §3 medido em operação pela segunda vez** (a
  primeira está no `AE-8` (ii)). **Rota já aberta e inalterada: `LM-T3`**, que entrega a
  atribuição por arquivo no dossiê. Registrado **sem ação** e sem retroação (`DB-23`): não abre
  rodada, não emenda card, não muda a fila.

- **`AE-14` (2026-09-18, medido no gate de delegação da `LM-T2`) — card autorado antes das
  lições do plano manda o executor decidir.** O loop **recusou despachar** a `LM-T2` pelo
  `G-PLANREADY`, sem gastar executor nenhum — conduta correta da Regra 8 do `CLAUDE.md` global.
  Três defeitos, todos de substância: (1) `Produto do módulo` e `Coerência do módulo` exigiam uma
  "função de atribuição" compartilhada por `B0`/`B1`, mas os três `Arquivos-alvo` eram um SKILL
  de prosa, o `telemetria_hook.py` e o teste dele — **nenhum lugar onde a função pudesse morar**,
  isto é, o executor teria de decidir módulo e assinatura; (2) três dos cinco testes afirmavam
  sobre o **comportamento do loop**, que é prosa lida pelo `scrum-master` e não tem runner; (3) o
  piso `≥ 145` já estava vencido (a árvore está em **153** desde a `LM-T1a`) — o `AE-4` outra vez,
  em versão barata. **Causa comum:** o card é **anterior** às rodadas `RP-1`..`RP-5` e nunca foi
  reautorado sob as lições que elas compraram; não tinha passos literais, âncora, baseline nem
  contingência. **ABSORVIDO no mesmo dia pelo `ESC-3`** → `DM-19`, `LM-T2` reescrita e partida em
  `LM-T2`/`LM-T2a`/`LM-T2b`, `LM-T3` liberada da dependência, pisos re-medidos em `LM-T3`,
  `LM-T4a` e `LM-T4`. **Insumo medido da rubrica da `LM-T5`:** card sobrevivente de uma revisão de
  plano é card **não** reautorado — a auditoria tem de varrer os cards antigos contra as lições
  novas, não só os cards novos.

- **`AE-15` (2026-09-18, pendência do laudo da `LM-T3`) — a evidência git da atribuição ignora o
  recorte `--desde`.** `coletar_estado_git(root)` lê só `git status`, que enxerga a **árvore de
  trabalho**; a lista de arquivos tocados, essa sim, recorta por `--desde`. Consequência: arquivo
  **já commitado** entre `<ref>` e `HEAD` sai com atribuição e **sem** a prova — `(sem entrada em
  \`git status\`)`. Não mordeu ainda porque nada está commitado desde `428246c` (medido no
  `ESC-4`: `git diff 428246c --name-status` = 30 linhas, `git status --porcelain -uall` = 45, a
  diferença sendo só os não rastreados); morderá no **primeiro dossiê gerado depois do marco de
  validação**, que é quando o commit acontece por diretiva do dono. **ABSORVIDO no mesmo dia pelo
  `ESC-4`** → card novo `LM-T3a`, com `git diff <ref> --name-status` como segunda fonte e a
  árvore de trabalho vencendo em caso de empate. **Sem retroação:** a `LM-T3` fica `done`.
- **`AE-16` (2026-09-18, segundo achado do laudo da `LM-T3`) — exigência estrutural prometida
  como teste comportamental.** O card exigia `TR ... chama \`confrontar_escopo\` e não
  reimplementa a classificação`; nenhum dos três testes discrimina isso — uma reimplementação
  fiel passaria em todos. **Defeito de autoria** (o card é deste consultor, `ESC-3`), não de
  execução. **ABSORVIDO no mesmo dia pelo `ESC-4`** → `DM-21` (três saídas legítimas: caso
  discriminante, inspeção mecânica, `Restrição` sem teste), critério (ix) da rubrica da `LM-T5`,
  item (b) da `LM-T8`, e o caso discriminante já aplicado à `LM-T2a` (teste novo de
  alvo-diretório). **Varredura medida:** nenhum outro card vivo tem TR do mesmo feitio.

- **`AE-17` (2026-09-19, pendência do laudo da `LM-T2a`) — o contrato de falha do verbo novo
  ficou aberto.** Com `--plano` inexistente, `--atribuir` sai com **traceback cru** de
  `FileNotFoundError`, enquanto o verbo irmão do **mesmo arquivo** sai `review_evidence: FALHOU -
  plano: arquivo não encontrado`. Causa estrutural: a guarda `plano_path.is_file()` mora em
  `montar_documento` e o ramo `--atribuir` chama `rdo.extrair_dossie` direto, pulando-a; os
  quatro testes do card só exercitam o caminho feliz. **Mesma classe do `AE-8`** — dois verbos do
  mesmo módulo com contratos de erro divergentes —, agora dentro de um arquivo só. Medido no
  `ESC-5`: os dois ramos saem **exit 1**, e quem discrimina é o **stderr**. **ABSORVIDO no mesmo
  dia pelo `ESC-5`** → `DM-22` e ampliação da `LM-T3a`, que já é da mesma borda e ainda não
  rodou. **Sem retroação:** a `LM-T2a` fica `done`.
- **`AE-18` (2026-09-19, segunda ressalva do laudo da `LM-T2a`) — número de aceite medido no
  planejamento envelhece dentro da própria janela que o consome.** As linhas 1 e 2 da
  `Verificação` da `LM-T2a` **nasceram vencidas**: baseline `28` e piso `156`, medidos no
  `ESC-3`/`ESC-4`, contra `32` e `165` na árvore real do despacho. **Série medida da janela:**
  145 → 153 → 156 → 161 → 165, seis tarefas; **cinco** correções manuais de piso em **sete**
  despachos (`LM-T7a`, `LM-T3`, `LM-T4a` e duas vezes na `LM-T2a`), todas feitas pelo
  `scrum-master` no gate. Não é defeito de atenção: é o efeito de tarefas que fecham **em série**
  sobre um número que o card fixou **antes**. **ABSORVIDO no mesmo dia pelo `ESC-5`** → `DM-23`
  (piso vira relação re-medida no despacho; o número fica como referência histórica datada),
  aplicada aos quatro cards vivos que ainda a carregavam, mais o critério (x) da rubrica da
  `LM-T5` e o item (b) da `LM-T8`.

- **`AE-19` (2026-09-19, medido no despacho e no retorno da `LM-T2`) — o comando de aceite foi
  rodado, mas o que foi publicado no card era uma **transcrição** dele, e a transcrição mudou o
  literal.** A `Verificação` 1 da `LM-T2` procurava a célula do `B0` com crase **dupla** —
  artefato de escape de code span de markdown —, e o padrão devolve **0 antes e 0 depois**: não
  discrimina mundo nenhum. O executor aplicou os sete passos, viu o item 1 falhar e devolveu
  `blocked motivo=premissa` **corretamente** (14 tool uses / 78,4k tk): ele não pode decidir que
  um aceite escrito está errado (Regra 8). **Bloqueio de aceite, não de rota** — o teste da
  cláusula emendada pela `RP-2` (`GOVERNANCA.md` §7 item 17) dá "existe entrega que satisfaz o
  entregável", e o `scrum-master` mediu que dá: `B0` presente, `B1` reescrita, rota velha
  removida, `--atribuir` citado, suíte 165 verde. **Segunda ocorrência da mesma classe no mesmo
  card:** o item 3 procurava `planejador` **em negrito**, que nunca existiu no arquivo (0 nos
  dois mundos); esse o loop corrigiu à mão no despacho e não conferiu o item 1. **Varredura do
  `ESC-6` sobre os cards vivos, com cada comando rodado:** `LM-T2b` item 3 publicava baseline
  **1** e o comando devolve **2** (o valor viera de um `grep` diferente do comando publicado);
  `LM-T5` item (3) já estava **satisfeito antes** da entrega (18 ocorrências) e o `-SimpleMatch`
  dele é obrigatório porque sem ele o padrão **nem compila**; `LM-T5` item (2) media 0 e
  discrimina; `LM-T4`, `LM-T8` e `LM-T3a` saíram **limpos**. **ABSORVIDO no mesmo dia pelo
  `ESC-6`** → `DM-24`, `LM-T2` → `review` sem redespacho, itens corrigidos em `LM-T2`, `LM-T2b` e
  `LM-T5`, critério (xi) da rubrica e item (b) da `LM-T8`.

- **`AE-20` (2026-09-19, pendência do laudo da `LM-T2c`) — a `A8a` nasceu incompleta: duas
  combinações do bloco A ficaram sem regra útil.** (1) A tripla (`reprovado`,
  `bloqueante=nenhuma`, `escalar`) casa `A8a`, que manda fechar **pelo veredito** — e
  `rdo.py close --veredito reprovado` **recusa** com exit 2, `invalid choice: 'reprovado'`
  (medido no `ESC-8`): regra que manda fazer o que o instrumento não aceita. (2) `escalar` com
  `bloqueante` diferente de `nenhuma` e retentativas = 0 **não casa regra nenhuma** — `A7` exige
  retentativas = 1, `A8a` exigia `bloqueante=nenhuma`, `A6` exige `refazer`. **Não rebaixa a
  entrega:** a `LM-T2c` fechou `done` aprovada 100% e a `A8a` funcionou no primeiro caso real da
  janela — foi o **primeiro fechamento materializado pela regra escrita**, e não pelo julgamento
  do loop, depois de quatro improvisos. **ABSORVIDO no mesmo dia pelo `ESC-8`** → `DM-26`
  (partição por veredito; `A6a` nova; domínio de `A8a` pelo veredito) e card `LM-T2d`, **antes**
  da `LM-T4`. A rodada fechou, no mesmo ato, um caso que ninguém tinha reportado: entrega
  **reprovada** com recomendação `seguir` cairia em `A9` e seria fechada como **aprovada**.
- **Notas de execução:**
  - 2026-09-19 `blocked` — rotulo 3a instancia em 7 pontos das respostas (a)..(h); renumerar so na tabela deixaria a prosa contraditoria; Contingencia 2 do card

### RP-1 — rodada de replanejamento sobre o `AE-2` (2026-09-18, `pantonic-planner`)

- **Classificação da mudança: técnica.** Forma de um entregável e tipo de um argumento de CLI —
  não muda objetivo, prioridade, doutrina nem escopo do plano. **Nada escalado ao dono**
  (`G-NOASK`, `GOVERNANCA.md` §7 item 18); as decisões `DM-1`..`DM-9`, a §2 e a §7 seguem
  intocadas.
- **Rota escolhida:** versionar o **slot** e continuar ignorando a **sessão** — `.gitignore:7-10`
  vira `.claude/estado/*` + `!.claude/estado/.gitkeep`, com o comentário reescrito para dizer as
  duas coisas (`DM-10`). A alternativa de manter o ignore e migrar a garantia para o runtime do
  Passo 4 foi descartada por falta de poder discriminante na verificação (o diretório existe na
  máquina do executor nos dois mundos); a garantia em runtime sobrevive como segunda trava, no
  texto literal do Passo 4.
- **O que a rodada alterou:** §3 ganhou o bloco de **fatos repostos** `F-1`..`F-4` (o `.gitignore`
  vigente, o precedente `docs/RDO/.gitkeep`, a independência do hook quanto a versionamento, e os
  endereços exatos da divergência de tipo). §4 ganhou `DM-10` e `DM-11`. A `LM-T1` foi reescrita
  por inteiro: `.gitignore` entrou nominalmente nos `Arquivos-alvo` (agora um caminho por bullet),
  os três textos novos entraram **literais** no card, o TF "`.claude/estado/` existe no
  repositório limpo" — que passava nos dois mundos — foi substituído por três verificações de
  `git` que discriminam, e o card ganhou `Depende de`, `Contratos/classes`, `Restrições desta
  tarefa`, quatro contingências fechadas, `Pronto quando` binário e `Fora do escopo`. A `LM-T2`
  ganhou o fato de contorno (`F-3`: nada nela supõe versionamento, e ela não toca `.gitignore`);
  a `LM-T3` não tinha suposição alguma sobre `.claude/estado/` e ficou **intocada**. A `LM-T5`
  ganhou o critério (vi) da rubrica e o `AE-2` como terceiro insumo medido. Status: `LM-T1` →
  `ready`, plano → `in-progress`, índice do diário → `in-progress 0/6`.
- **Causa-raiz na autoria:** fase 4 da auto-auditoria do `pantonic-planner`. O entregável (a)
  criava um arquivo versionado e a `Verificação` supunha esse arquivo aparecendo em `git status`,
  mas nenhum passo do protocolo mandava confrontar entregável de versionamento com a **regra de
  configuração vigente** que decide se o arquivo existe para o git. O teste de interrupção (item
  8) cobre referente não verificado e instrumento não sondado; não cobria regra de repositório que
  **nega** o entregável. O defeito era barato de pegar: uma leitura de `.gitignore` na autoria.
- **Verificação que teria evitado o bloqueio:** antes de publicar, confrontar todo entregável que
  cria, versiona, move ou apaga arquivo com `.gitignore`/`.gitattributes` e com o filtro do
  instrumento que vai julgá-lo; e recusar critério de pronto que passa igual com e sem a mudança.
- **Classe de erro: nova.** Publicada em `.claude/agents/pantonic-planner.md`, fase 4, item 10, no
  mesmo ato (precedente do dono, 2026-09-17: publicar é consequência do plano, não pergunta), com
  linha em `CHANGELOG.md`. Registrada também como critério (vi) da rubrica de criação de tarefa da
  `LM-T5`, com o `AE-2` nomeado como caso medido.

- **`AE-4` (2026-09-18, medido no segundo despacho da `LM-T1`) — duas das cinco verificações do
  card reescrito pela `RP-1` são insatisfazíveis como escritas, e a entrega material está correta.**
  Medido nesta janela, com a entrega do executor na árvore: `python -m pytest tests/ -q` → **145
  passed** (142 + os 3 TF do card, acima do piso); `.gitignore:11-12` com `.claude/estado/*` e
  `!.claude/estado/.gitkeep` nessa ordem; `git check-ignore -q .claude/estado/.gitkeep` → **exit
  1** (o arquivo **não** está ignorado, que é o efeito pretendido); `git check-ignore -v
  .claude/estado/tarefa-corrente.json` → imprime `.gitignore:11:.claude/estado/*` (o conteúdo de
  sessão segue ignorado); `git status --porcelain -uall .claude/estado/` → `?? .claude/estado/.gitkeep`;
  `rdo.py` e os dois arquivos de teste editados. Os dois defeitos de redação:
  **(i) verificação 3** manda `git check-ignore -v .claude/estado/.gitkeep` "não imprimir linha
  nenhuma" — impossível por desenho do git: com `-v` ele reporta o padrão decisivo **inclusive
  quando é negação**, imprimindo `.gitignore:12:!.claude/estado/.gitkeep` e saindo `0`. O comando
  que responde à pergunta pretendida é `git check-ignore -q <path>`, cujo **exit 1** significa "não
  ignorado". Reproduzido pelo executor em repositório isolado (git 2.42.0.windows.2), o que descarta
  estado local.
  **(ii) verificação 5** manda `git status --porcelain .claude/estado/` imprimir
  `?? .claude/estado/.gitkeep`, mas o git **colapsa diretório não rastreado** e imprime
  `?? .claude/estado/`; o literal esperado só sai com `-uall`.
  **Classe do defeito:** comando de aceite publicado sem ter sido **rodado** na autoria
  (`G-PLANREADY`: número/aceite re-derivável por comando) — vizinha do `AE-2`, mas distinta: lá o
  card contradizia a **configuração do repositório**, aqui contradiz o **comportamento real do
  instrumento**. **Entrada da rodada `RP-2`**. **ABSORVIDO em 2026-09-18 pela `RP-2`** → decisão
  `DM-12` (o bloqueio é de aceite, não de rota; verificações 3 e 5 e contingência 1 reescritas;
  `LM-T1` a `review`), mais a emenda do `G-REPLAN` em `GOVERNANCA.md` §7 item 17. Nada pendente
  neste achado.

### RP-2 — rodada de replanejamento sobre o `AE-4` (2026-09-18, `pantonic-planner`)

- **Classificação da mudança: técnica.** Redação de aceite de um card, disposição de status de uma
  tarefa e o critério doutrinário que separa bloqueio de rota de bloqueio de aceite. Não muda
  objetivo, prioridade nem escopo do plano. **Nada escalado ao dono** (`G-NOASK`, `GOVERNANCA.md`
  §7 item 18); `DM-1`..`DM-11`, a §2 e a §7 do plano seguem intocadas, e a rota de `DM-10`/`DM-11`
  sai **confirmada pelo fato medido**, não revista.
- **Veredito sobre a cláusula do segundo bloqueio: não se aplica.** Este foi o segundo `blocked
  premissa` da `LM-T1` depois de uma rodada, mas a premissa **não** caiu: a entrega existe na árvore
  e passa (`AE-4`). A cláusula, como redigida, contava bloqueios e não discriminava rota inviável de
  card mal redigido — foi **emendada** em `GOVERNANCA.md` §7 item 17 com o teste "existe entrega que
  satisfaz o entregável do card sob as decisões vigentes?" (não existe → rota → `superseded`; existe
  → aceite → corrige-se a redação), mais dois tetos anti-abuso: terceiro bloqueio `premissa` na
  mesma tarefa é `superseded`, e segundo bloqueio de aceite sobre a **mesma** verificação já
  reescrita é `superseded`. A saída (c) do `G-REPLAN` ganhou o ramo **`review`**, e a transição
  `blocked` → `review` — autoria do planejador, gatilho 1 — foi publicada na tabela de transições de
  `.claude/skills/diario-de-obras/SKILL.md`, para que o loop não improvise status.
- **O que a rodada alterou:** §4 ganhou `DM-12`. A `LM-T1` teve reescritas a **verificação 3**
  (`git check-ignore -q` + exit code `1`, com a advertência explícita sobre o `-v`), a
  **verificação 4** (literal medido), a **verificação 5** (`--porcelain -uall`, com a razão do
  colapso de diretório), o piso da **verificação 2** (≥ 145) e a **contingência 1** (lê exit code,
  não saída de `-v`); o `Status` passou a `review` com a nota de atribuição para quem revisa. A
  `LM-T2` e a `LM-T3` tiveram o piso de suíte atualizado de 142 para 145 — número medido, não
  herdado. A `LM-T4` teve o aceite `backlog.py check` verde **removido**: era insatisfazível pela
  mesma classe de defeito (o lint sai `1` com qualquer violação e há 315 pré-existentes, `AE-1`, em
  arquivos que a tarefa não toca), e no lugar entraram três verificações com saída medida, entre
  elas a varredura da régua antiga pelo literal `>8 write-clusters`, cuja baseline de hoje é uma
  ocorrência em `.claude/skills/proximo-passo/SKILL.md:126`. A `LM-T5` ganhou o critério (vii) da
  rubrica e o `AE-4` como quarto insumo medido. Status: `LM-T1` → `review`, plano → `in-progress`,
  índice do diário → `in-progress 0/6`.
- **Causa-raiz na autoria:** fase 4 da auto-auditoria do `pantonic-planner`, de novo — e num ponto
  que o item 10, publicado pela `RP-1`, chegou a tangenciar sem fechar. O item 10 exige critério de
  pronto que **discrimine** e chega a recomendar `git check-ignore` como exemplo de comando que
  separa; nenhum passo do protocolo exigia que a **saída esperada** do comando fosse um fato
  observado. O planejador não roda comando — e por isso escreveu o que "sabia" que a ferramenta
  imprime. Nos dois casos o que ele sabia estava errado: `-v` reporta a negação decisiva, e
  `--porcelain` colapsa diretório não rastreado. O card ficou com aceite impossível, e o executor,
  corretamente, produziu a entrega e parou na contingência.
- **Verificação que teria evitado o bloqueio:** antes de publicar, toda linha de `Verificação` com
  literal esperado tem de trazer saída **observada** — pedida como dossiê na fase 1, nunca deduzida
  do conhecimento da ferramenta; e pergunta binária ("está ignorado?", "existe?", "casa?") se
  escreve com a flag binária e o exit code, nunca com flag de diagnóstico, cuja saída serve a outra
  pergunta.
- **Classe de erro: nova.** Distinta do item 10 (regra de configuração do repositório): esta é sobre
  o comportamento do **instrumento de aceite**. Publicada em `.claude/agents/pantonic-planner.md`,
  fase 4, item 11, mais o gatilho correspondente na fase 1, no mesmo ato, com linha em
  `CHANGELOG.md`. Registrada também como critério (vii) da rubrica de criação de tarefa da `LM-T5`,
  com `AE-2` e `AE-4` nomeados como os dois casos medidos.

- **`AE-5` (2026-09-18, medido no Passo 6 da `LM-T1`) — a gramática de cabeçalho da `DM-5` quebra
  o instrumento que gera o dossiê de evidência, e o loop não consegue despachar o reviewer.**
  `python .claude/tools/review_evidence.py --plano docs/plans/P-0740-loop-de-modulos.md --tarefa
  LM-T1 --desde 428246c --out …` sai **exit 1** com `cabeçalho de 'LM-T1' não declara
  modelo/classe (plano legado) — faltando: --esquema-legado, --modelo, --classe`. Duas medidas
  sobre esse retorno: (i) o cabeçalho **declara** modelo e classe — o que ele não segue é a
  gramática de **dois** campos da `DP-C` (`[<modelo> · classe <classe>]`), porque a `DM-5` inseriu
  o terceiro (`esforço`); (ii) as três flags que a mensagem manda usar **não existem** no
  `review_evidence.py` (`--help` lista só `--plano`, `--tarefa`, `--root`, `--max-diff-chars`,
  `--out`, `--desde`) — a mensagem vem de `extrair_dossie` (`rdo.py:190`), que é **compartilhada**
  pelos dois instrumentos, e só o `rdo.py close` expõe a escotilha (`rdo.py:819-824`), enquanto o
  `review_evidence.py` fixa `esquema_legado=False` (`:271`, `:568`). **Consequência medida:** o
  Passo 6 não produz, o `pantonic-reviewer` não pode ser despachado com o dossiê que ele exige, e a
  `LM-T1` — entregue e verde — fica sem rota de fechamento. O Passo 9 (`rdo.py close`) **tem** rota,
  pela escotilha. **Classe do defeito:** dependência de ordem não declarada — a `DM-5` foi aplicada
  aos cards no ato do planejamento, mas quem publica a gramática na doutrina é a `LM-T4` e quem
  toca o `review_evidence.py` é a `LM-T3`, ambas **depois** da `LM-T1` na fila. É a mesma classe do
  `AE-10` do `P-0739`. **Entrada da rodada `RP-3`**. Não é bloqueio de execução da `LM-T1`: a
  entrega existe e passa (145 testes); o que não produz é o instrumento da **orquestração**.
  **ABSORVIDO em 2026-09-18 pela `RP-3`** → decisão `DM-13` (a gramática que o plano escreve é a que
  os parsers leem; os seis cards voltam à forma de dois campos com o esforço em campo do corpo, e a
  gramática de três campos entra nos parsers pela tarefa nova `LM-T4a`, antes da `LM-T4`) e fatos
  `F-5`..`F-7` na §3. O Passo 6 volta a produzir sem tocar código; a `LM-T1` segue em `review`, sem
  redespacho. Nada pendente neste achado.

### RP-3 — rodada de replanejamento sobre o `AE-5` (2026-09-18, `pantonic-planner`)

- **Classificação da mudança: tática.** Ordem de tarefas dentro do plano vigente, mais a forma de
  um campo de cabeçalho — não muda objetivo, prioridade, doutrina nem escopo. **Nada escalado ao
  dono** (`G-NOASK`, `GOVERNANCA.md` §7 item 18); `DM-1`..`DM-12`, a §2 e a §7 seguem intocadas, e
  `DM-5` permanece viva e literalmente como estava: o que a `DM-13` fixa é **quando** e **onde** ela
  se aplica.
- **Objeto do bloqueio (teste do `G-REPLAN`):** não é bloqueio de tarefa — a `LM-T1` não foi
  devolvida, a entrega dela existe, passa (145 testes) e continua em `review`. O que falhou foi o
  **Passo 6 da orquestração**, que não conseguiu gerar o dossiê. Por isso a rodada não mexe em uma
  linha da entrega nem na disposição da tarefa.
- **O que a rodada alterou:** §3 ganhou os fatos `F-5`, `F-6` e `F-7` (as duas gramáticas de
  cabeçalho realmente implementadas, com os grupos posicionais do `backlog.py`, e a medida de que
  `esforço` não existe em nenhum lugar da árvore `.claude/`); §4 ganhou `DM-13`; os **seis**
  cabeçalhos de card voltaram à forma de dois campos, com `- **Esforço:** <valor>` como campo do
  corpo; nasceu a `LM-T4a` (`Sonnet · classe implementacao`, esforço `low`), que ensina a gramática
  de três campos aos dois parsers com o campo opcional; a `LM-T4` ganhou `Depende de: LM-T4a`, a
  proibição de tocar os dois instrumentos e o ponteiro para a residência única do literal; a `LM-T5`
  teve o critério (iii) da rubrica reescrito (cabeçalho se julga pela gramática que os parsers
  aceitam **na data do card**) e passou a julgar 11 cards; a §6 passou a
  `LM-T1 → LM-T2 → LM-T3 → LM-T4a → LM-T4 → LM-T5 → LM-T6`. Status: `LM-T1` segue em `review`,
  plano segue `in-progress`, índice do diário → `in-progress 0/7`.
- **Custo comparado das rotas, que é parte da decisão:** as rotas (A) e (B) custavam uma janela de
  executor cada — e nesta janela já se gastaram duas rodadas (112,4k + 114,3k) e dois despachos
  (61,8k + 73,0k) sem fechar tarefa; a (C) não destravava nada, porque os cabeçalhos das tarefas
  reordenadas carregavam o mesmo terceiro campo. A rota escolhida custa **uma edição de plano** e
  nenhum token de executor, e ainda deixa a dívida real (o parser) com card próprio e ordem
  declarada.
- **Causa-raiz na autoria:** fase 1 da coleta do `pantonic-planner`, no bullet que já existe —
  "plano que introduz ou usa convenção de identificador, caminho ou nome de artefato verifica,
  ainda aqui, que os instrumentos do gate de aceite (`review_evidence.py`, `rdo.py close`,
  `backlog check`) aceitam essa convenção; se não aceitam, a correção do instrumento é tarefa do
  plano, nunca achado adiado". `DM-5` é exatamente uma convenção nova de cabeçalho, e a verificação
  não foi exercida: a decisão foi **aplicada aos cards no mesmo ato em que foi tomada**, antes de
  qualquer parser conhecê-la. O erro não é de falta de regra; é de regra existente não exercida.
- **Classe de erro: conhecida — não se publica lição nova.** É a mesma classe do `AE-10` do
  `P-0739` (dependência de ordem não declarada) e já está coberta pelo bullet citado da fase 1,
  publicado em 2026-09-16 (`RP-2` do `P-0739`). `.claude/agents/pantonic-planner.md` **não** foi
  editado por esta rodada. O registro que sobra é operacional e cabe no próprio plano: convenção
  nova só desce para os cards depois de existir no parser — é a `DM-13`, e a `LM-T5` a afere pelo
  critério (iii) reescrito.

- **`AE-6` (2026-09-18, medido logo após a `RP-3`) — o corpo do card repete, em campo, o defeito
  que a `RP-3` corrigiu no cabeçalho.** Com a gramática de cabeçalho recuada, o gerador avança e
  para no campo: `python .claude/tools/review_evidence.py --plano … --tarefa LM-T1 --desde 428246c`
  → **exit 1**, `campo obrigatório ausente em 'LM-T1': 'objetivo'`. Medido em `rdo.py:258`, os
  obrigatórios são `objetivo`, `verificacao` e `pronto-quando`; o conjunto canônico (`:94-101`)
  acrescenta `arquivos-alvo`, `entregavel` e `dossie-fechado-por`. O card `LM-T1` traz
  `Arquivos-alvo`, `Entregável`, `Verificação` e `Pronto quando` — e **`Tema`** onde o esquema
  `DP-C` exige **`Objetivo`**, porque a `DM-2` adotou "tema" como o vocabulário do módulo coeso.
  **Falta exatamente um campo, nos seis cards.** Mesma raiz do `AE-5`: vocabulário novo aplicado
  aos cards antes de qualquer parser do kit o conhecer. **Entrada da rodada `RP-4`.**
  **Absorvido pela `DM-14`** (rodada `RP-4`, 2026-09-18): o rótulo foi renomeado para `Objetivo` nos
  sete cards. A re-derivação do achado mostrou que "falta exatamente um campo" subestimava o
  desvio — o mesmo esquema `DP-C` era violado em mais três pontos (`Arquivos-alvo` e `Entregável`
  juntos; `pronto-quando` ausente ou com outro rótulo; `verificacao` ausente ou com o `:` fora do
  negrito), todos fechados na mesma decisão. Nada pendente neste achado.

### RP-4 — rodada de replanejamento sobre o `AE-6` (2026-09-18, `pantonic-planner`)

- **Classificação da mudança: tática.** Rótulo de campo no corpo do card, dentro do plano vigente —
  não muda objetivo, prioridade, doutrina, escopo nem rota. **Nada escalado ao dono** (`G-NOASK`).
  `DM-1`..`DM-13`, a §2, a §6 e a §7 seguem intocadas; `DM-2` permanece literal, e "tema" continua
  sendo o vocabulário dela.
- **Objeto do bloqueio:** como na `RP-3`, não é bloqueio de tarefa. A `LM-T1` não foi devolvida,
  a entrega existe, passa e continua em `review`; o que falhava era o Passo 6 da orquestração,
  que não conseguia gerar o dossiê de evidência.
- **O que a rodada alterou:** §4 ganhou `DM-14`; os sete cards (`LM-T1`, `LM-T2`, `LM-T3`,
  `LM-T4a`, `LM-T4`, `LM-T5`, `LM-T6`) tiveram `Tema` → `Objetivo`; `LM-T1`..`LM-T4` tiveram
  `Entregável` → `Produto do módulo` (fica um só campo de alvo, `Arquivos-alvo`); `LM-T2`, `LM-T3`
  e `LM-T4` ganharam `Pronto quando`; `LM-T5` e `LM-T6` tiveram `Critério de pronto` → `Pronto
  quando` e ganharam `Verificação` por efeito no arquivo; `LM-T4` teve a pontuação do rótulo
  `Verificação` corrigida. Status inalterado: `LM-T1` em `review`, plano `in-progress`.
- **Causa-raiz na autoria: a mesma do `AE-5`, já publicada** — vocabulário novo aplicado aos cards
  antes de qualquer parser do kit o conhecer (`DM-13` (ii): parser, doutrina, cards; nunca cards
  primeiro). Classe de erro conhecida; **nenhuma lição nova** foi publicada em
  `.claude/agents/pantonic-planner.md`.
- **Residual desta rodada, a fechar por quem orquestra:** o ambiente desta janela rodou **sem
  ferramenta de execução** (Bash desabilitado), então os dois comandos de aceite **não** foram
  rodados aqui. As correções foram derivadas linha a linha do código do parser
  (`rdo.py:92`, `:94-101`, `:135-144`, `:155-183`, `:258`, `:262-268`), não da memória — mas isso é
  dedução, e `DM-12` diz que aceite se roda. O aceite é:
  `python .claude/tools/review_evidence.py --plano docs/plans/P-0740-loop-de-modulos.md --tarefa
  LM-T1 --desde 428246c --out docs/RDO/evidencia/P-0740-LM-T1.md` → exit 0, mais o mesmo comando
  sem `--out` para `LM-T2`, `LM-T3`, `LM-T4a`, `LM-T4`, `LM-T5` e `LM-T6` → exit 0.

- **`AE-7` (2026-09-18, medido no despacho da `RP-4`) — a `DM-12` exige do planejador um ato que o
  agente `pantonic-planner` não consegue executar.** A `DM-12` (rodada `RP-2`) publicou a lição
  "comando de aceite não se deduz, se roda". No despacho da `RP-4` a orquestração tornou isso
  condição de retorno, e o agente devolveu, literalmente: `Error: No such tool available: Bash.
  Bash is disabled for this session, in subagents as well as here.` O `pantonic-planner` tem
  `Read`, `Glob`, `Grep`, `Write`, `Edit` — **nenhuma ferramenta de execução**. Ele acertou ao
  recusar-se a afirmar `exit 0` não medido, que é a própria `DM-12`; mas a consequência é que
  **nenhum comando de aceite publicado por ele pode ter sido rodado por ele**, e a `DM-12`, como
  redigida, é inexequível pelo papel a que se dirige. Foi a orquestração que rodou os sete
  comandos, todos `exit 0`, e gerou `docs/RDO/evidencia/P-0740-LM-T1.md` (261 linhas). **Rotas
  possíveis, nenhuma escolhida aqui:** dar execução ao `pantonic-planner`; ou transferir o dever da
  `DM-12` a quem tem execução (a orquestração roda o comando no despacho e devolve o output à
  rodada); ou manter a `DM-12` como dever de **autoria conjunta**, com o comando rodado por quem
  despacha antes de o card ser publicado. **Não se decide aqui** — é matéria de rodada própria ou
  da `LM-T5`, que audita a criação de tarefa. Registrado sem ação (`DB-23`).
  **ABSORVIDO em 2026-09-18 pela `RP-5`** → rota escolhida pelo **dono** (item 5 da *Diretiva de
  execução do `P-0740`*): a primeira das três — dar execução ao `pantonic-planner`. Decisão
  `DM-16`, materializada no card `LM-T7`; as outras duas rotas (transferir o dever à orquestração;
  autoria conjunta) foram descartadas com motivo na própria decisão. Nada pendente neste achado.

- **`AE-8` (2026-09-18, pendência do laudo da `LM-T1`, registrada por `B1`) — o contrato de erro
  do módulo de fechamento diverge entre os dois verbos.** Exercício ponta a ponta do reviewer
  (passo 3b, `DM-3`), medido nos dois CLIs reais: com `type=float` (`DM-11`), `rdo.py close
  --tokens-k` passou a **aceitar** `-5` (grava `-5.0`), `1e3` (grava `1000.0`) e `nan` (grava
  `nan k tokens`) — domínio que o `type=int` anterior recusava com exit 2 —, enquanto
  `telemetria.py append --tokens_k` recusa negativo e não-numérico com exit 1, por
  `_validar_numero_nao_negativo`. **Não rebaixa a entrega**, que seguiu o contrato literal do card
  (o laudo deu 100%, sete dimensões `conforme`): o buraco é do card e da `DM-11`, que fixaram o
  tipo e esqueceram a guarda. **Entrada da rodada `RP-5`**, que fecha o contrato de erro do módulo.
  Três achados de processo do mesmo laudo, preservados aqui porque o laudo foi consumido:
  (i) `kit_check.ps1 -Mode check-drift` sai **exit 1** e trava o veredito mecânico de `guardas` por
  divergência de README vinda de `.claude/agents/pantonic-executor.md` e `pantonic-reviewer.md` —
  que o próprio dossiê classifica como ato do dono fora do ciclo de tarefa; o instrumento não cruza
  a atribuição que ele mesmo calcula. Rota: `LM-T3`. (ii) o dossiê deixou 4 arquivos "sem
  atribuição" e **só a injeção manual da orquestração** permitiu marcar `escopo` — sem ela, entrega
  correta seria reprovada; é o defeito 6 da §3, medido em operação. Rota: `LM-T3`. (iii) a
  verificação 3 original travou o segundo despacho com a entrega completa na árvore — defeito do
  card, nunca da execução; já corrigido pela `RP-2`/`DM-12`, sem ação adicional.
  **ABSORVIDO em 2026-09-18 pela `RP-5`** → decisão `DM-15` (domínio único por campo e recusa na
  mesma forma nos dois verbos) e card `LM-T1a`. **Duas correções de fato ao próprio achado**, as
  duas medidas na rodada: (1) `telemetria.py append` **não** recusa todo não-numérico — ele
  **aceita** `nan` e `inf` e os grava na série, porque `float("nan") < 0` é falso; a guarda de
  finitude entra nos **dois** instrumentos; (2) a divergência não é só de `--tokens-k`: vale para
  `--tool-uses` e `--duracao-s`, e neste último **na direção contrária** — `rdo.py close`
  (`type=int`) recusa com exit 2 o literal de uma casa decimal que o hook emite para o irmão e que
  a série já contém, de modo que o defeito 3 da §3 seguia aberto depois da `DM-11`. O achado (i)
  deste registro (`check-drift` exit 1 travando o veredito mecânico de `guardas`) tem **duas**
  rotas agora: a causa material — o `.claude/README.md` fora de sincronia — é fechada pela
  `LM-T7`; a regra geral (o instrumento não cruza a atribuição que ele mesmo calcula) segue com a
  `LM-T3`, intocada.
- **`AE-9` (2026-09-18, medido no Passo 8 da `LM-T1`) — o bloco A não tem regra para
  `recomendacao=escalar`.** O domínio fechado da recomendação é {`seguir`, `seguir com ressalva`,
  `refazer`, `escalar`}. O bloco A cobre `refazer` (`A6`), `reprovado` (`A7`), `seguir com
  ressalva` (`A8`) e `seguir` (`A9`) — **`escalar` não casa com nenhuma**. Ele só aparece no `B1`,
  que é avaliado *depois* de o bloco A dizer "segue", e cujo texto ("**PARA**, mesmo com veredito
  `aprovado`") pressupõe uma tarefa já fechada. Nesta janela a orquestração materializou o
  fechamento como `aprovado` — as sete dimensões `conforme`, 100%, bloqueante `nenhuma`, e o
  próprio laudo dizendo que a pendência não rebaixa a entrega — e registrou aqui que a tabela não
  prescrevia o caso. **Matéria da `LM-T2`**, que já reescreve o bloco B e responde pela cadência:
  ou `escalar` ganha regra própria no bloco A, ou o `B1` passa a declarar o fechamento que ele
  pressupõe. Registrado sem decidir (`DB-23`).
  **ABSORVIDO em 2026-09-19 pelo `ESC-7`**, depois de a rota original falhar: a matéria estava
  alocada à `LM-T2`, e a `LM-T2` — como o `ESC-3` a reescreveu — tinha `Restrições` mandando o
  **bloco A ficar intocado**; ela fechou `done` aprovada 100% justamente por obedecê-las, e o
  achado ficou órfão. **Buraco de alocação, não de entrega.** Rota escolhida: a primeira das duas
  — `escalar` ganha regra própria (`A8a`), porque a segunda faria o `B1` declarar fechamento de
  tarefa, que é matéria do bloco A, e criaria residência dupla para a mesma decisão. Decisão
  `DM-25`, card `LM-T2c`, **antes** da `LM-T4`. **Urgência medida:** sem a regra, o `B1` entregue
  pela `LM-T2` é inalcançável pela própria primeira condição, e o loop já improvisou o caso
  **quatro vezes** nesta janela.

### RP-5 — rodada de reparo sobre o `AE-8` e o `AE-7` (2026-09-18, `pantonic-consultant`)

- **Quem conduziu:** o **consultor de plano** (`pantonic-consultant`), instanciado uma vez para
  esta execução por decisão do dono (item 1 da *Diretiva de execução do `P-0740`*), no lugar de
  abrir rodada fria de planejador. É a primeira rodada do `P-0740` conduzida assim, e a primeira
  em que **todo** número publicado foi medido dentro da própria rodada.
- **Classificação da mudança: tática.** Contrato de erro de um módulo já entregue e toolset de um
  papel, os dois dentro do plano vigente — não muda objetivo, prioridade, rota nem escopo.
  **Nada escalado ao dono** (`G-NOASK`): a matéria (b) **já é** decisão do dono, e esta rodada a
  materializa em card, não a reabre.
- **Objeto:** nenhum dos dois é bloqueio de tarefa. A `LM-T1` está `done`, aprovada 100%, e **não
  se refaz** (`DB-23`, sem retroação): o `AE-8` é buraco de **card** e de **decisão** (`DM-11`
  fixou o tipo e esqueceu a guarda), e o `AE-7` é impedimento de **papel**, já resolvido pelo dono.
- **O que a rodada alterou:** §4 ganhou `DM-15` (domínio e forma de recusa iguais nos dois verbos
  do pacote de fechamento) e `DM-16` (o planner ganha `Bash`; projeções canônicas fechadas no mesmo
  ato); §5 ganhou dois cards `ready` — `LM-T1a` (residência do contrato de erro) e `LM-T7`
  (residência do toolset e das duas projeções); a `LM-T4` teve a `Verificação` 1 corrigida e passou
  a declarar dependência da `LM-T7`; §6 ganhou as duas dependências novas e a nota de exclusão
  mútua sobre `rdo.py`; §8 ganhou dois riscos. O plano passa a **9** tarefas. Status inalterado:
  `LM-T1` `done`, plano `in-progress`.
- **Fatos re-derivados no passo 1 (achado é indício, não apuração) — os dois achados estavam
  incompletos:**
  1. O `AE-8` afirmava que `telemetria.py append` "recusa negativo e não-numérico". Medido:
     **aceita `nan` e `inf`** e os grava literalmente na série (`float("nan") < 0` é falso). A
     divergência de domínio, portanto, não é "um CLI frouxo e um estrito": é **cada um frouxo de um
     jeito**.
  2. O `AE-8` falava só de `--tokens-k`. Medido: a mesma divergência vale para `--tool-uses` e
     `--duracao-s`; e, **na direção contrária**, `rdo.py close --duracao-s` (ainda `type=int`)
     recusa com **exit 2** o literal de uma casa decimal que `telemetria_hook.montar_args_append`
     emite para o irmão e que a série já contém (`1020.648`, `104.928`). O defeito 3 da §3 — "o
     mesmo número medido não passa nos dois" — continuava **aberto** depois da `DM-11`, por um
     campo que ninguém tinha olhado. É a lição do **instrumento irmão**: corrigir um de um par sem
     confrontar o outro com a mesma gramática deixa metade do defeito vivo.
  3. A `Verificação` 1 da `LM-T4` publicava `kit_check -Mode check-drift → exit 0 (medido em
     2026-09-18)`. Medido nesta rodada: **exit 1**, 6 problemas. O número era verdadeiro quando
     medido e envelheceu com atos do dono posteriores (descrições de `DM-8`, criação do
     `pantonic-consultant`) — aceite copiado de dossiê de outra tarefa não sobrevive à árvore
     compartilhada. Corrigido no card, com a rota (a `LM-T7` recoloca o exit 0) em vez de remoção
     do aceite.
- **Rota de cada matéria:**
  **(a) `AE-8`** → `DM-15` + card `LM-T1a`. Domínio único por campo nos dois verbos (`tool_uses`
  inteiro não negativo; `tokens_k`/`duracao_s` número finito não negativo), recusa com **exit 1** e
  corpo de mensagem idêntico nos dois, vocabulário fechado de quatro razões, guarda do `rdo.py`
  correndo antes da checagem de `--plano` (o que torna a verificação barata e sem efeito em disco).
  Sem importação cruzada — a cláusula da `DM-11` fica intacta.
  **(b) `AE-7`** → `DM-16` + card `LM-T7`. A decisão é do dono e não se reabre: o
  `pantonic-planner` recebe `Bash`, e com isso a `DM-12` deixa de ser inexequível pelo papel a que
  se dirige, sem que uma linha dela seja reescrita. Como a tarefa toca superfície de agente, ela
  fecha no mesmo ato as **duas projeções canônicas** que estão vermelhas hoje por atos do dono fora
  de ciclo (`check-drift` exit 1, `check-readme.ps1` exit 1) — e é isso que devolve à `LM-T4` um
  aceite satisfazível.
- **Disciplina da rodada (o que a diferencia das quatro anteriores):** nenhum comando entrou em
  card sem ter sido rodado aqui. Foram medidos, com exit code observado: os seis literais de
  domínio nos dois CLIs, o piso da suíte (`145 passed`), o par de suítes alvo (`47 passed`),
  `check-drift` (1), `check-readme.ps1` (1), `kit_check -Mode validate` (0), o efeito de
  `-Mode generate` sobre `.claude/README.md` (3 inserções, 2 remoções, e `check-drift` indo a 0 —
  **medido em cópia e revertido no mesmo ato**, com o arquivo restaurado ao hash original), a linha
  `tools:` do planner e o `git check-ignore` do caminho de TSV temporário usado na `Verificação` 5
  da `LM-T1a`. **Nenhuma entrega de card foi implementada pela rodada** — reparo de plano é do
  consultor, o código do módulo é do executor.
- **Custo evitado, para a série:** as quatro rodadas anteriores custaram 423,7k tk porque cada uma
  redescobriu o cenário. Esta nasceu com o cenário no contexto e mediu tudo que publicou; o consumo
  medido entra em `docs/telemetria.tsv` pelo loop.

### ESC-1 — escalonamento da execução, sobre o `AE-11` (2026-09-18, `pantonic-consultant`)

- **Quem conduziu:** o consultor já instanciado para esta execução — **sem rodada nova, sem
  contexto novo**: o cenário do plano já estava no contexto desde a `RP-5`, e o escalonamento
  chegou por mensagem do `scrum-master`. É exatamente o arranjo que o item 1 da *Diretiva de
  execução do `P-0740`* criou para não repetir os 423,7k tk das quatro rodadas frias.
- **Classificação da mudança: tática.** Corte de um card pela fronteira de permissão e regra de
  intervalo para o dever da `DM-12`, dentro do plano vigente — não muda objetivo, rota, escopo nem
  prioridade. **Nada escalado ao dono como decisão**; o que vai a ele é um **ato**, nominado abaixo.
- **Objeto do bloqueio:** não é premissa de plano nem defeito de card. O executor devolveu
  `blocked motivo=premissa` porque a `Edit` do passo 1 foi **negada pela camada de permissão do
  harness**, duas vezes, com instrução de parar. Conduta correta em três níveis: o executor não
  contornou, o `scrum-master` não contornou, e o consultor **não tentou editar o arquivo** — pedir
  a outro agente a edição negada seria lavagem de permissão (`DM-17` (ii)).
- **A pergunta que resolveu o caso:** *de que, de fato, o `tools:` do planner é pré-requisito?*
  Confrontadas as cinco linhas de `Verificação` do card com os passos, só a linha do
  `Select-String '^tools:'` dependia dele; `check-drift`, `check-readme.ps1`, `validate` e o piso da
  suíte dependem da **projeção**, que ninguém bloqueou. O módulo, portanto, era dois: a permissão é
  que revelou a costura.
- **O que a rodada alterou:** §4 ganhou `DM-17`; a `LM-T7` foi **reescrita** como card de projeções
  (`ready`, sem dependência, despachável agora) e a `LM-T8` nasceu `blocked` por ato do dono,
  carregando o toolset e a publicação posterior na definição do planner; a `LM-T4` perdeu
  `.claude/agents/pantonic-planner.md` dos `Arquivos-alvo`, teve o `Pronto quando` ajustado de seis
  para cinco superfícies e a dependência esclarecida (depende da `LM-T7`, **não** da `LM-T8`); §6
  ganhou o grafo atualizado; §8, um risco; `AE-11` registrado e absorvido no mesmo dia. O plano
  passa a **10** tarefas, **9** delas despacháveis pelo loop.
- **Números medidos nesta passagem** (todos rodados aqui, `DM-12`): `check-readme.ps1` com a linha
  do `pantonic-consultant` inserida → **exit 0**, `check-readme: OK - 9 agente(s), 11 skill(s), 18
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida` — medido em edição
  **revertida no mesmo ato**, com `README.md` restaurado ao hash original `74711aa`; baseline de
  `pantonic-consultant` nos dois READMEs → **zero** ocorrências em cada; varredura de
  `>8 write-clusters` nas seis superfícies da `LM-T4` → **uma** linha, em
  `.claude/skills/proximo-passo/SKILL.md:126`, nenhuma no arquivo do planner.
- **O que fica pendente de ato do dono, em uma linha:** liberar a regra de permissão para
  `.claude/agents/` (skill `update-config`/`settings.json`) **ou** aplicar ele mesmo os três textos
  literais da `LM-T8` — até lá a `DM-16` está decidida e não materializada, e a `DM-12` segue
  inexequível pelo `pantonic-planner`, com o dever de medir transferido a quem tem ferramenta
  (`DM-17` (iv)).
- **Efeito na fila:** nenhuma tarefa do plano depende da `LM-T8`. A janela segue pela `LM-T7`
  (projeções) e pela `LM-T1a`, que continuam sem dependência entre si.

### ESC-2 — escalonamento da execução, sobre o `AE-12` (2026-09-18, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor já instanciado — terceira passagem no mesmo contexto
  (`RP-5`, `ESC-1`, `ESC-2`), sem rodada fria nenhuma. O laudo da `LM-T7` foi consumido e apagado
  (`DP-H`); o conteúdo chegou por mensagem do `scrum-master`.
- **Classificação da mudança: tática.** Um invariante de seção que passa a viver no instrumento e
  uma regra de autoria — dentro do plano vigente, sem tocar objetivo, rota, escopo nem prioridade.
  **Nada escalado ao dono** (`G-NOASK`); o único ato dele continua sendo o da `LM-T8`.
- **Objeto:** não é bloqueio nem defeito de execução. A `LM-T7` fechou `done` com **ressalva 90%**,
  bloqueante `nenhuma`, e entregou os três passos literais como escritos — `check-drift` 0,
  `check-readme.ps1` 0, `validate` 0, as duas contagens ≥ 1, `145 passed`, nenhuma contingência,
  nenhum arquivo de `.claude/agents/` tocado. A dimensão fora de `conforme` foi
  `criterio-de-pronto` `parcial`, e a causa é **autoria**: o card prescreveu a linha da tabela e não
  a frase que conta a tabela.
- **O fato, medido nesta passagem:** `README.md:760` diz `O kit são oito agentes, onze skills, …` e
  a tabela logo abaixo lista **nove** desde a entrega; o disco tem 9 agentes, 11 skills, 4
  verificadores; `check-readme.ps1` **anuncia `9 agente(s)`** e sai **exit 0**. Cinco verificações
  verdes e o arquivo-alvo contradizendo a si mesmo — o guarda confronta tabela × disco e nunca
  olhou para a prosa. `O kit são` ocorre **uma** vez no arquivo, e `README.md` **não** tem região
  marcada (só `.claude/README.md` tem), então a frase é escrita à mão e ninguém a regenera.
- **O que a rodada decidiu:** `DM-18`, em cinco partes — a frase que conta o conjunto é parte do
  entregável de quem mexe no conjunto (i); se o instrumento não discrimina a afirmação, a tarefa
  estende o instrumento (ii); a lição mora no critério **(viii)** da rubrica da `LM-T5`, superfície
  **acessível**, e só a publicação no arquivo do planner fica apensada ao item (b) da `LM-T8` (iii);
  sem retroação sobre a `LM-T7` (iv); e a fronteira do invariante são as **duas** contagens que o
  script já calcula, ficando "verificadores" e "projeções" nominalmente fora, porque contagem sem
  fato medido é o defeito da `RP-1` (v).
- **O que a rodada alterou:** §4 ganhou `DM-18`; card novo **`LM-T7a`** (`ready`, `README.md` +
  `.claude/checks/check-readme.ps1`), com a ordem de passos que **produz** a evidência — implementa
  a checagem, roda com a prosa velha para ver o exit 1, só então corrige a prosa; `LM-T5` ganhou o
  critério (viii), dois insumos medidos novos (`AE-11` e `AE-12`) e a contagem de cards julgados
  atualizada de 11 para **15**; `LM-T8` teve o item (b) estendido; §6 e §8 atualizadas; `AE-12`
  registrado e absorvido, `AE-13` registrado **sem ação**.
- **`AE-13`, registrado e não agido** (rota já aberta): o dossiê de evidência sem atribuição por
  tarefa apresentou 32 arquivos tocados desde `428246c` e obrigou injeção manual pela **segunda**
  vez, com reconciliação por `mtime`. É o defeito 6 da §3 medido em operação de novo, e quem o fecha
  é a `LM-T3`, já na fila.
- **Autocrítica, porque o achado é da autoria e não da execução:** quem escreveu a `LM-T7` foi este
  consultor, no `ESC-1`, e o card passou pelo mesmo crivo que cobrou dos outros — verificação
  medida, âncora literal, baseline observada — e **ainda assim** fechou o item sem fechar o
  invariante. É a prova de que a disciplina de medir o comando **não** substitui a de perguntar o
  que mais a seção afirma sobre o que o card muda; daí a regra ir para o instrumento (`LM-T7a`), e
  não só para a rubrica: o que depende de alguém lembrar volta a falhar.
- **Estado da janela na saída desta rodada:** fechadas `RP-5`, `ESC-1` e `LM-T7` (`done`, ressalva
  90%); `LM-T8` `blocked` por ato do dono; despacháveis agora `LM-T1a`, `LM-T4a` e `LM-T7a`.
  Consumo acumulado medido até aqui: 522,9k tk. Nada commitado; `--desde 428246c` segue sendo o
  recorte.

### ESC-3 — escalonamento da execução, sobre o `AE-14` e o `AE-3` (2026-09-18, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor, quarta passagem no mesmo contexto (`RP-5`, `ESC-1`,
  `ESC-2`, `ESC-3`). Nenhuma rodada fria; nenhum cenário redescoberto.
- **Classificação da mudança: tática.** Partição de um card por sujeito, residência de uma função
  que já existia e fórmula de um instrumento de medida — tudo dentro do plano vigente, sem tocar
  objetivo, rota, escopo nem prioridade. **Nada escalado ao dono**; o único ato dele segue sendo o
  da `LM-T8`.
- **Objeto:** **recusa de despacho**, não bloqueio de execução. O loop parou a `LM-T2` no
  `G-PLANREADY` e **não gastou executor** — é a primeira vez nesta execução que o gate pega um card
  defeituoso **antes** do gasto, e o número que isso poupou está no contraste com o `AE-2` (61,8k
  tk numa triagem que só descobriu o defeito depois do despacho).
- **A pergunta que resolveu o caso:** *onde mora a função de atribuição?* Medido:
  `confrontar_escopo` (`review_evidence.py:282-333`) **já é** a função, com os cinco baldes da
  `DB-25`/`DB-32`, e já é consumida pela geração do dossiê. O card antigo mandava criar de novo o
  que existe, num conjunto de arquivos-alvo onde ela não caberia — daí o executor ter de **decidir**,
  que é o que a Regra 8 proíbe. Com a residência achada, o resto se resolveu sozinho: o loop não
  importa função, ele **roda comando**; a `LM-T3` não depende de tarefa nenhuma; e o que sobrou de
  código (o hook) é outro sujeito, logo outro card.
- **O que a rodada alterou:** §4 ganhou `DM-19` (residência + partição) e `DM-20` (a fórmula do
  hook, calibrada); a `LM-T2` foi **reescrita** como card de redação com sete passos literais e a
  declaração explícita de que **não tem teste `pytest`**; nasceram `LM-T2a` (o verbo `--atribuir`)
  e `LM-T2b` (o hook); a `LM-T3` perdeu a dependência da `LM-T2`, ganhou a exclusão mútua com a
  `LM-T2a` e teve os pisos corrigidos; `LM-T4a` e `LM-T4` tiveram o piso vencido (145) trocado pelo
  medido (**153**); `AE-3` foi absorvido com as cinco ocorrências novas; `AE-14` foi registrado e
  absorvido; §6 e §8 atualizadas. O plano passa a **13** tarefas, 12 despacháveis.
- **A calibração, que é o achado técnico da passagem:** o hook somava `usage` por `message.id`, e
  `cache_read_input_tokens` é o contexto **inteiro** relido a cada turno — somá-lo turno a turno
  multiplica o total pelo número de turnos (erro de 4,2× num despacho de 4 tool uses, 37× num de
  96). Confrontadas três fórmulas contra o `<usage>` de **seis** transcripts reais desta janela, a
  **última mensagem** acerta 6/6 e a soma por `message.id` reproduz exatamente os seis valores
  inflados que o hook gravou. A dedupe do `T55` continua satisfeita (com uma mensagem só, as duas
  fórmulas coincidem), e `tool_uses`/`duracao_s` estavam certos e ficam intocados. **Isto não é
  dedução:** é a mesma disciplina do `DM-12` aplicada a uma fórmula — rodou-se sobre corpus real
  antes de publicar.
- **O que a `LM-T2` antiga ensina sobre o plano, e não só sobre si mesma:** ela **sobreviveu** a
  cinco rodadas de reparo sem ser reautorada. As rodadas consertaram o card que estava sendo
  despachado e os vizinhos que o achado tocava; ninguém varreu os cards **antigos** contra as
  lições novas. Sobraram três na mesma condição (`LM-T4`, `LM-T5`, `LM-T6`) — os pisos delas foram
  re-medidos aqui, e a regra "varrer card sobrevivente, não só card novo" entrou como insumo
  medido da `LM-T5`.
- **Estado da janela na saída desta rodada:** fechadas `LM-T1a` (100%), `LM-T7` (ressalva 90%),
  `LM-T7a` (100%) e as rodadas `RP-5`, `ESC-1`, `ESC-2`, `ESC-3`. `LM-T8` `blocked` por ato do dono.
  Despacháveis sem dependência: `LM-T2a`, `LM-T2b`, `LM-T3`, `LM-T4a`. Piso da suíte: **153**.
  Nada commitado; `--desde 428246c` segue sendo o recorte.

### ESC-4 — escalonamento da execução, sobre o `AE-15` e o `AE-16` (2026-09-18, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor, quinta passagem no mesmo contexto (`RP-5`, `ESC-1`,
  `ESC-2`, `ESC-3`, `ESC-4`).
- **Classificação da mudança: tática.** Uma fonte de evidência que passa a respeitar o recorte que
  a atribuição já respeitava, e uma regra de autoria sobre o que um teste pode prometer — dentro do
  plano vigente, sem tocar objetivo, rota, escopo nem prioridade. **Nada escalado ao dono**; o
  único ato dele segue sendo o da `LM-T8`.
- **Objeto:** nenhum dos dois é bloqueio. A `LM-T3` fechou `done` com **ressalva 91%**, bloqueante
  `nenhuma`, e a entrega **provou-se no próprio ato** — registro que vale mais que o percentual: o
  dossiê da revisão dela marcou os três `Arquivos-alvo` como `da entrega` e os outros 29 como
  `alheio`, e foi a **primeira revisão desta janela sem injeção manual de contexto**. Nas três
  anteriores (`LM-T7`, `LM-T1a`, `LM-T7a`) a injeção foi obrigatória. O **`AE-13` fecha aqui**, e o
  defeito 6 da §3 deixa de custar uma intervenção humana por revisão.
- **`AE-15` — o defeito real, e por que ele não apareceu.** `coletar_estado_git` lê só
  `git status`, que enxerga a árvore de trabalho; a lista de tocados, essa sim, recorta por
  `--desde`. Arquivo commitado entre `<ref>` e `HEAD` sai com atribuição e sem prova. Medido aqui:
  `git diff 428246c --name-status` = **30** linhas contra **45** de `git status --porcelain -uall`
  — a diferença é só o não rastreado, porque **nada** foi commitado desde a ref. O defeito é
  invisível hoje **por construção da janela**, e vira visível no primeiro dossiê depois do marco de
  validação, que é quando o commit acontece. Rota: card novo `LM-T3a`, com `git diff <ref>
  --name-status` como segunda fonte, a árvore de trabalho vencendo em empate (`setdefault`, não
  atribuição) e o literal `<letra> (commitado desde <ref>)`. O teste discriminante **não** pode
  rodar sobre o corpus de hoje: exige repo temporário com commit depois da ref — que é o que os
  testes do módulo já sabem fazer (`_run_git`,
  `test_desde_recorta_tocados_a_partir_da_referencia`).
- **`AE-16` — a lição, que não é só da `LM-T3`.** O card exigia, como TR, que a seção nova
  *chamasse* `confrontar_escopo` e *não reimplementasse* a classificação — propriedade
  **estrutural**, que uma reimplementação fiel satisfaria em todos os testes. `DM-21` fixa as três
  saídas legítimas: **caso discriminante** (a entrada em que a implementação certa e a cópia
  plausível divergem — para atribuição, o **alvo-diretório**, que casa por prefixo e que cópia por
  caminho exato erra), **inspeção mecânica** na `Verificação`, ou **`Restrição` sem teste**. A
  varredura medida nesta passagem encontrou **nenhum** outro TR estrutural em card vivo; o único
  caso aberto era uma `Restrição` da `LM-T2a`, que recebeu aqui o teste de alvo-diretório. Lição no
  critério (ix) da rubrica da `LM-T5` e no item (b) da `LM-T8` — mesma rota da `DM-18` (iii).
- **O padrão que estas cinco passagens desenham, e que o dono vai querer ver na `LM-T6`:** dos seis
  achados que o consultor absorveu (`AE-8`, `AE-11`, `AE-12`, `AE-14`, `AE-15`, `AE-16`), **quatro**
  são de **autoria de card** e nenhum é de execução — os executores entregaram fielmente em todas as
  tarefas desta janela, e as duas ressalvas vieram de coisa que o card não mandou fazer. O gargalo
  medido do loop deixou de ser a execução: é a **criação da tarefa**, que é exatamente o que a
  `LM-T5` audita.
- **O que a rodada alterou:** §4 ganhou `DM-21`; card novo **`LM-T3a`**; `LM-T2a` ganhou o quarto
  teste (alvo-diretório), teve a exclusão mútua reapontada para a `LM-T3a` e os pisos re-medidos
  (28 no arquivo, **156** na suíte); `LM-T5` ganhou o critério (ix), dois insumos medidos (`AE-14`,
  `AE-16`) e a contagem de cards julgados atualizada de 15 para **18**; `LM-T8` teve o item (b)
  estendido; `AE-15` e `AE-16` registrados e absorvidos; §6 e §8 atualizadas. O plano passa a
  **14** tarefas, 13 despacháveis.
- **Estado da janela na saída desta rodada:** fechadas `LM-T7` (90), `LM-T1a` (100), `LM-T7a` (100)
  e `LM-T3` (91) — quatro tarefas, todas com RDO. `LM-T8` `blocked` por ato do dono. Despacháveis
  sem dependência: `LM-T2a`, `LM-T2b`, `LM-T3a`, `LM-T4a`. Piso da suíte: **156**. Consumo
  acumulado medido: **1.503,5k tk**. Nada commitado; `--desde 428246c`.

### ESC-5 — escalonamento da execução, sobre o `AE-17` e o `AE-18` (2026-09-19, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor, sexta passagem no mesmo contexto (`RP-5`, `ESC-1`..`ESC-5`).
- **Classificação da mudança: tática.** Uma guarda de borda que ganha residência única e um número
  de aceite que vira relação — dentro do plano vigente, sem tocar objetivo, rota, escopo nem
  prioridade. **Nada escalado ao dono**; o único ato dele segue sendo o da `LM-T8`.
- **Objeto:** duas ressalvas de laudo, nenhuma bloqueante, nenhuma de execução. A `LM-T4a` fechou
  **100%** e a `LM-T2a`, **91%** com o verbo entregue como prescrito — forma literal, exit 0
  informativo, sem montar dossiê, alvo-diretório casando por prefixo (o caso discriminante que o
  `ESC-4` acrescentou **pegou** o que tinha de pegar).
- **`AE-17` — o contrato de falha do verbo.** Medido aqui: com `--plano NAO-EXISTE.md`, o dossiê sai
  `review_evidence: FALHOU - plano: arquivo não encontrado 'NAO-EXISTE.md'` e o `--atribuir` sai com
  traceback de `FileNotFoundError` — **os dois com exit 1**, o que significa que quem afirma o
  contrato tem de afirmar o **stderr**. Causa: a guarda `is_file()` mora em `montar_documento`
  (`:615-616`) e o ramo `--atribuir` (`:706-725`) chama `extrair_dossie` direto. Com `--tarefa`
  inexistente os dois já coincidem, porque o ramo captura `RdoValidationError` — o buraco era só o
  arquivo de plano. `DM-22` generaliza a `DM-15` (que fechou o par `rdo.py` × `telemetria.py`) para
  **verbos do mesmo arquivo**: guarda de borda com residência única, e card que acrescenta verbo
  roda o **mesmo** argumento inválido nos **dois** ramos. **Sem card novo:** o reparo entra na
  `LM-T3a`, que já é da mesma borda do mesmo módulo e ainda não rodou — o assunto dela passa a ser,
  nominalmente, *a borda do instrumento de evidência*, entrada e saída da mesma pergunta.
- **`AE-18` — e este é sobre o método, não sobre a tarefa.** As duas primeiras linhas de
  `Verificação` da `LM-T2a` **nasceram vencidas**. Série medida da janela: **145 → 153 → 156 → 161
  → 165** em seis tarefas, com **cinco** correções manuais de piso em **sete** despachos. A causa
  não é desatenção de quem autorou os cards — este consultor —, é estrutural: o número é medido no
  planejamento e consumido depois de outras tarefas da **mesma janela** terem fechado. `DM-23` troca
  **constante por relação**: o piso é o total que a árvore tiver no despacho, re-medido por quem
  despacha; a entrega soma os `<N>` testes novos e não reduz esse total. O que o card fixa é o que
  não envelhece — o **delta** e os **nomes**. O número fica, com data e rodada, como **referência
  histórica**, que é o que ele sempre foi de fato.
- **Por que isto não é remendo:** das nove classes de defeito que a rubrica da `LM-T5` vai aferir,
  esta é a **única** que não se corrige lendo o card com mais cuidado. As outras oito são erros de
  autoria que um critério pega; esta é uma propriedade do **regime** — janela longa, tarefas em
  série, árvore compartilhada — e só se corrige mudando o que o card promete. O sintoma tinha sido
  tratado cinco vezes à mão, no gate, e nenhuma das cinco chegou a gastar executor: o `scrum-master`
  absorveu o custo silenciosamente. Um custo absorvido em silêncio cinco vezes é exatamente o que
  vira defeito permanente quando o loop rodar sem ninguém olhando.
- **O que a rodada alterou:** §4 ganhou `DM-22` e `DM-23`; a `LM-T3a` foi **reescrita** (título,
  objetivo, produto (b), passos 4-5, três testes novos e a `Verificação` 3 do contrato de falha);
  `LM-T2`, `LM-T2b` e `LM-T4` tiveram o piso numérico trocado pela relação; `LM-T5` ganhou o
  critério **(x)** e a nona classe de insumo; `LM-T8` teve o item (b) estendido com as lições da
  `DM-22` e da `DM-23`; `AE-17` e `AE-18` registrados e absorvidos; §6 e §8 atualizadas. **Nenhum
  card novo** — o plano segue com 14 tarefas, 6 fechadas.
- **Estado da janela na saída desta rodada:** fechadas `LM-T7` (90), `LM-T1a` (100), `LM-T7a` (100),
  `LM-T3` (91), `LM-T4a` (100) e `LM-T2a` (91) — seis tarefas, todas com RDO, **nenhuma reprovada e
  nenhuma refeita**. Suíte **165 passed**. Fila aberta sem dependência: `LM-T2`, `LM-T2b`, `LM-T3a`.
  Liberadas por fechamento: `LM-T2` (dependia da `LM-T2a`) e `LM-T4` (dependia da `LM-T4a` e da
  `LM-T7`). `LM-T8` `blocked` por ato do dono. Consumo acumulado medido: **2.171,9k tk**. Nada
  commitado; `--desde 428246c`.

### ESC-6 — escalonamento da execução, sobre o `AE-19` (2026-09-19, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor, sétima passagem no mesmo contexto (`RP-5`, `ESC-1`..`ESC-6`).
- **Classificação da mudança: tática.** Correção de redação de aceite em três cards e a cláusula de
  doutrina que fecha a classe — dentro do plano vigente, sem tocar objetivo, rota, escopo nem
  prioridade. **Nada escalado ao dono.**
- **Veredito sobre o bloqueio, pelo teste da própria `RP-2`** (`GOVERNANCA.md` §7 item 17,
  emendado por esta execução): *"existe entrega que satisfaz o entregável do card sob as decisões
  vigentes?"* — **existe, e está na árvore**. Logo é bloqueio **de aceite**, não de rota: a rodada
  corrige a redação, a `LM-T2` vai a **`review`** sem redespacho e **não se refaz**, exatamente
  como a `LM-T1` na `RP-2` (`DM-12` (iii)). O executor parou certo: ele não pode decidir que um
  aceite escrito está errado (Regra 8), e gastou 14 tool uses / 78,4k tk sem inventar rota.
- **A causa, com nome e sobrenome — e ela é deste consultor.** A `DM-12` que eu herdei da `RP-2` e
  repito em todo card diz que comando de aceite **se roda**. Rodei os comandos; o que foi para o
  card foi uma **transcrição** deles, dentro de code span de markdown, e a transcrição **mudou o
  literal**: a crase que delimita o span virou crase dupla dentro do padrão. Um comando escrito em
  markdown inline **não é o comando que roda**. `DM-24` é a cláusula que faltava, e o teste que ela
  fixa fecha a classe inteira: **publicar os dois valores rodados** — o de antes e o de depois —,
  porque padrão que devolve o **mesmo** valor nos dois mundos é inválido por construção, seja por
  escape, por negrito inventado, por regex que nem compila ou por já estar satisfeito antes da
  entrega.
- **A varredura, com cada comando rodado** (é o que a `DM-24` (iii) passa a exigir, e foi feito aqui
  card a card): `LM-T2` item 1 — crase dupla, **0 nos dois mundos**, corrigido e re-rodado (**0**
  antes, **1** depois); `LM-T2` item 3 — `planejador` em negrito que nunca existiu no arquivo, **0
  nos dois mundos**, corrigido (**1** antes, **0** depois) — este o `scrum-master` já tinha
  consertado à mão no despacho, e foi por não conferir o item 1 que a entrega parou; `LM-T2b` item
  3 — baseline publicada **1**, comando devolve **2** (`telemetria_hook.py:11` no docstring e `:93`
  no código), porque o número viera de um `grep` diferente do comando publicado; `LM-T5` item (3) —
  **já satisfeito antes** da entrega (**18** ocorrências), trocado por **delta de 6** (`DM-23`), e
  o `-SimpleMatch` dele é obrigatório porque sem ele o padrão **nem compila** (`Nested quantifier
  '*'`); `LM-T5` item (2) — mede **0** hoje, discrimina, mantido; `LM-T3a`, `LM-T4` e `LM-T8` —
  **limpos**.
- **A correção foi verificada pelo próprio método que ela institui:** os dois comandos corrigidos
  foram **extraídos do arquivo do plano** e executados verbatim, como um executor os leria —
  `893` → `1`, `901` → `0`, exit 0 nos dois. Não é transcrição conferida a olho: é o literal do
  card, rodado.
- **O que a rodada alterou:** §4 ganhou `DM-24`; `LM-T2` foi a `review` com os itens 1 e 3 da
  `Verificação` reescritos em **bloco cercado** e com os dois valores medidos; `LM-T2b` teve a
  baseline do item 3 corrigida; `LM-T5` teve os itens (2) e (3) reescritos e ganhou o critério
  **(xi)**; `LM-T8` teve o item (b) estendido; `AE-19` registrado e absorvido; §6 e §8 atualizadas.
  **Nenhum card novo** — o plano segue com 14 tarefas, 6 fechadas e 1 em `review`.
- **O padrão das sete passagens, que é o insumo mais caro da `LM-T5` e do veredito da `LM-T6`:** dos
  oito achados que o consultor absorveu (`AE-8`, `AE-11`, `AE-12`, `AE-14`, `AE-15`, `AE-16`,
  `AE-17`, `AE-18`, `AE-19`), **nenhum** é de execução — os executores entregaram fielmente em
  todas as sete tarefas despachadas, e as quatro ressalvas vieram de coisa que o card não mandou
  fazer ou mandou errado. O gargalo medido deste loop é, sem ambiguidade, a **criação da tarefa**;
  e a metade dele que sobrou depois de nove critérios de rubrica é a que não se corrige lendo
  melhor: literal que envelhece (`DM-23`) e literal que a própria escrita corrompe (`DM-24`).
- **Estado da janela na saída desta rodada:** fechadas `LM-T7` (90), `LM-T1a` (100), `LM-T7a` (100),
  `LM-T3` (91), `LM-T4a` (100) e `LM-T2a` (91); `LM-T2` em **`review`**. Suíte **165 passed**. Fila
  para executor: `LM-T2b`, `LM-T3a`, `LM-T4`. `LM-T8` `blocked` por ato do dono. Consumo acumulado
  medido: **2.652,7k tk**. Nada commitado; `--desde 428246c`.

### ESC-7 — escalonamento da execução, sobre o `AE-9` (2026-09-19, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor, oitava passagem no mesmo contexto (`RP-5`, `ESC-1`..`ESC-7`).
- **Classificação da mudança: tática.** Uma regra que faltava numa tabela de roteamento, dentro do
  plano vigente — sem tocar objetivo, rota, escopo nem prioridade. **Nada escalado ao dono.**
- **Objeto:** pendência de laudo de uma tarefa **aprovada 100%**. A `LM-T2` fechou com a correção
  do `ESC-6` funcionando, sem redespacho de executor — o que fecha, na prática, o ciclo que o
  `AE-19` abriu.
- **O achado, e por que ele é estrutural.** O `B1` que a `LM-T2` acabou de publicar tem como
  primeira condição `recomendacao=escalar`; o bloco B só é avaliado **depois** de o bloco A dizer
  "segue"; e o bloco A **não tem regra para `escalar`** — cobre `refazer` (`A6`), `reprovado`
  (`A7`), `seguir com ressalva` (`A8`) e `seguir` (`A9`). A cadência nova é, portanto,
  **inalcançável pela própria primeira condição**. E não é teoria: nesta janela **quatro** laudos
  vieram com `escalar` (`LM-T7`, `LM-T3`, `LM-T2a`, `LM-T2`) e em todos o loop materializou o
  fechamento **por julgamento próprio**, porque a tabela calava — improviso que a `DP-G` proíbe.
- **Por que o achado ficou órfão, que é a lição de método desta passagem.** O `AE-9` estava
  registrado desde a `LM-T1` com rota *"matéria da `LM-T2`"*. No `ESC-3` eu **reescrevi** a `LM-T2`
  e lhe dei `Restrições` mandando o **bloco A ficar intocado** — sem reconferir o achado que
  apontava para ela. A `LM-T2` fechou 100% justamente por obedecer à restrição, e a matéria ficou
  sem dono por seis rodadas. **A rota de um achado é premissa do card que a carrega:** card
  reescrito re-declara as rotas que apontam para ele. Entrou como décima classe de insumo da
  `LM-T5`.
- **A decisão (`DM-25`), em uma frase:** `escalar` **não é desfecho de tarefa, é desfecho da
  pendência** — o bloco A fecha pelo **veredito transcrito** e o bloco B roteia a pendência. Linha
  nova `A8a`, entre `A7` e `A8`, com precedência declarada (`A6` e `A7` vencem; `A8a` vence `A8` e
  `A9`). O caso `escalar` **com** bloqueante não precisa de texto próprio, porque `bloqueante`
  diferente de `nenhuma` implica `veredito=reprovado`, que já é `A7` — e isso já está escrito no
  arquivo. **Nenhuma linha de código:** `rdo.py close` recebe `--recomendacao` como texto livre e
  calcula o desdobramento pelo **veredito**, isto é, o instrumento já faz o que a regra prescreve; o
  que faltava era a prosa que manda o loop fazê-lo **sem julgar**.
- **Rota descartada:** fazer o `B1` declarar o fechamento que ele pressupõe (a segunda alternativa
  registrada no `AE-9`). Recusada porque poria decisão de **desfecho de tarefa** — matéria do bloco
  A — dentro de uma regra do bloco B, criando residência dupla para a mesma decisão, que é o que a
  `DB-2` proíbe.
- **Ordem: a `LM-T2c` vem antes da `LM-T4`**, e por dois motivos independentes, não por preferência:
  as duas têm `.claude/skills/scrum-master/SKILL.md` em `Arquivos-alvo` (exclusão mútua), e a
  `LM-T4` publica doutrina que **cita** as tabelas de roteamento — publicar sobre um bloco A
  incompleto é a ordem invertida que a `DM-13` proíbe no eixo dela. A dependência entrou declarada
  no card da `LM-T4`.
- **Disciplina da rodada (`DM-24` aplicada a si mesma):** os quatro comandos de `Verificação` do
  card novo foram **extraídos do arquivo do plano e executados verbatim** depois de escritos —
  linhas `1205`, `1209`, `1213` e `1218`, exit 0, saída **0** nos quatro, que é exatamente a
  baseline declarada. Depois da entrega eles têm de dar `1`, `1`, `≥5` e `1`; é o par de valores
  que a `DM-24` (iii) exige.
- **O que a rodada alterou:** §4 ganhou `DM-25`; card novo **`LM-T2c`** (`ready`, prosa, um arquivo,
  cinco passos literais, sem `pytest` e com a declaração de por quê); `LM-T4` passou a depender da
  `LM-T2c`; `AE-9` absorvido depois de seis rodadas órfão; `LM-T5` ganhou a décima classe de insumo
  e a contagem de cards julgados subiu para **19**; §6 e §8 atualizadas. O plano passa a **15**
  tarefas, **7** fechadas.
- **Estado da janela na saída desta rodada:** `LM-T7` (90), `LM-T1a` (100), `LM-T7a` (100), `LM-T3`
  (91), `LM-T4a` (100), `LM-T2a` (91) e `LM-T2` (100) fechadas — **sete**, nenhuma reprovada,
  nenhuma refeita. Suíte **165 passed**. Fila para executor: `LM-T2c`, `LM-T2b`, `LM-T3a` e, depois
  da `LM-T2c`, `LM-T4`. `LM-T8` `blocked` por ato do dono. Consumo acumulado medido: **3.161,1k
  tk**. Nada commitado; `--desde 428246c`.

### ESC-8 — escalonamento da execução, sobre o `AE-20`, e fechamento do cenário da janela (2026-09-19, `pantonic-consultant`)

- **Quem conduziu:** o mesmo consultor, **nona e última passagem desta janela** no mesmo contexto
  (`RP-5`, `ESC-1`..`ESC-8`). O loop encerra por **decisão de janela**, não por poluição: o contexto
  seguiu coeso — um plano, um cenário — do começo ao fim.
- **Classificação da mudança: tática.** Partição de domínio numa tabela de roteamento, dentro do
  plano vigente. **Nada escalado ao dono** como decisão; o que vai a ele é o relatório da janela e o
  ato da `LM-T8`.
- **Marco que vale registrar:** a `LM-T2c` fechou `done` **aprovada 100%** e foi o **primeiro
  fechamento desta janela materializado pela regra escrita** (`A8a`), e não pelo julgamento do loop.
  Nas quatro ocorrências anteriores de `recomendacao=escalar` o `scrum-master` decidiu o
  desdobramento sozinho, por falta de regra. A doutrina alcançou o caso que a produziu.
- **`AE-20`, e por que as duas lacunas são uma só.** A `A8a` resolveu `escalar` para entrega
  **aprovada** e deixou aberto o caso em que o laudo **reprova e manda escalar**: por um lado a
  tripla (`reprovado`, `bloqueante=nenhuma`, `escalar`) caía em `A8a`, que manda fechar pelo
  veredito — e `rdo.py close --veredito reprovado` sai **exit 2**, `invalid choice` (medido aqui);
  por outro, `escalar` com bloqueante e retentativas = 0 não casava regra nenhuma. `DM-26` fecha as
  duas com a `A6a` (não fecha RDO, não gasta retentativa, materializa `blocked` razão `premissa`,
  escala ao consultor e a janela segue) e com o domínio de `A8a` passando a ser o **veredito**.
  **Fecha-se a regra ao instrumento, não o contrário:** alargar `--veredito` para `reprovado` seria
  inventar um fechamento de RDO que a `DP-F` não prevê.
- **Um caso que ninguém tinha reportado, fechado de quebra:** entrega **reprovada** com recomendação
  `seguir` cairia hoje em `A9` e seria fechada como **aprovada**. A frase de partição ("o bloco A
  parte primeiro por veredito, depois por recomendação") o elimina.
- **Disciplina (`DM-24`, terceira aplicação seguida):** os quatro comandos de `Verificação` do card
  novo foram **extraídos do plano e rodados verbatim** — linhas `1349`, `1353`, `1358` e `1362`,
  exit 0, saídas `0`, `0`, **`1`** e `0`, que são exatamente as baselines declaradas. Os quatro
  discriminam: depois da entrega têm de dar `1`, `≥5`, `0` e `1`.

#### Cenário desta janela — o que não está escrito em decisão nenhuma e o próximo consultor precisa saber

1. **O gargalo medido deste loop é a autoria de card, não a execução.** Oito tarefas despachadas,
   **zero reprovadas, zero refeitas**; onze achados absorvidos pelo consultor (`AE-8`, `AE-9`,
   `AE-11`, `AE-12`, `AE-14`..`AE-20`) e **nenhum** deles de execução. As quatro ressalvas vieram de
   coisa que o card não mandou fazer, ou mandou de um jeito que o instrumento não aceita.
2. **Card antigo é o risco vivo da próxima janela.** `LM-T4`, `LM-T5` e `LM-T6` foram autorados em
   2026-09-18, **antes** de `DM-15`..`DM-26`; só os pisos delas foram corrigidos. O `AE-14` já
   custou um gate inteiro por isso. Varrer os três contra as decisões novas **antes** do despacho —
   é barato e o gate do loop já sabe fazê-lo.
3. **Comando de aceite se extrai do plano e se roda verbatim antes do despacho** (`DM-24`). Foi
   assim que `ESC-6`, `ESC-7` e `ESC-8` fecharam, e é a única defesa contra o literal que a própria
   escrita corrompe. O par de valores (antes/depois) é o que prova que o aceite discrimina.
4. **A árvore acumula oito entregas não commitadas desde `428246c`.** No commit do marco, o `AE-15`
   passa a morder o primeiro dossiê gerado depois dele — por isso a `LM-T3a` deve fechar **antes**
   do commit, não depois.
5. **A série de telemetria desta janela foi mantida à mão.** O hook grava número inflado (até 37×) e
   **não dispara** quando o subagente é retomado por `SendMessage` — nenhuma das oito passagens do
   consultor gerou linha. A `LM-T2b` fecha a primeira metade; a segunda é compensada por prosa
   (Passo 9), e não tem conserto de instrumento.
6. **A figura do consultor se pagou.** As quatro rodadas frias de replanejamento desta execução
   (`RP-1`..`RP-4`) custaram **423,7k tk** para fechar **uma** tarefa, redescobrindo o cenário a
   cada vez. As nove passagens do consultor rodaram **num contexto só**, absorveram onze achados,
   produziram seis cards novos e duas decisões por passagem em média, e nenhuma delas precisou
   reler o plano. O número da janela inteira — **3,67M tk para oito tarefas fechadas** — tem de ser
   lido com isso em conta na `LM-T6`.

- **`AE-21` — baseline de corpus real citada em card envelhece igual a piso de suíte, e o `DM-23`
  não a cobre.** Achado de processo do laudo da `LM-T3a` (2026-09-19), rota prescrita pelo próprio
  laudo. A linha 4 de `Verificação` da `LM-T3a` afirmava *"Baseline medida: também nenhuma"* — medida
  verdadeira quando o card foi autorado, e **falsa no despacho**: o commit do marco 1 (`6eebccd`)
  pôs commits entre `428246c` e `HEAD`, e a baseline re-medida no ato deu **52** linhas
  ``(sem entrada em `git status`)``. A linha que era **vacuosa** (0 → 0) virou **discriminante**
  (52 → 0) — a favor da entrega, desta vez, mas por sorte do calendário, não por desenho. Os
  literais de piso (`32 passed`, `165 passed`) já estavam protegidos pelo `DM-23` (piso é relação,
  re-medida no despacho); **baseline de corpus real não estava**. Rota: item de replanejamento do
  `P-0740` que estende o `DM-23` a **toda** baseline de corpus real citada em card — re-medida no
  despacho e registrada no dossiê de evidência, nunca literal histórico no card. Residência
  natural: a `LM-T5` (revisão da criação das tarefas), que já é a tarefa que varre a autoria de
  card. **Não abre rodada própria.**

- **`AE-22` — a `A7` manda fechar o que o instrumento recusa, e a frase de partição da `LM-T2d`
  torna isso uma afirmação falsa no arquivo.** Achado do laudo da `LM-T2d` (2026-09-19, veredito
  `aprovado 100%`, recomendação `escalar`), roteado pelo `B1` ao `pantonic-consultant`. Medido: a
  regra `A7` do bloco A continua mandando *"fecha o RDO como `reprovado`"*, e o instrumento de
  fechamento **recusa** esse desfecho em três pontos — `rdo.py close --veredito` aceita só
  `aprovado` e `ressalva` (exit 2, `invalid choice`), `calcular_desdobramento` levanta
  `RdoValidationError` para `reprovado`, e o gatilho do Passo 9 só dispara em `done`. A `LM-T2d`
  **entregou exatamente o que o card contratou** e não podia tocar a `A7`, congelada como literal
  pelas `Restrições` do card; mas a frase de partição que o mesmo card mandou transcrever afirma
  que *"nenhuma regra mande fechar o que o instrumento recusa"* — de modo que o arquivo passa a
  carregar uma afirmação falsa sobre a própria tabela. A partição do bloco A, portanto, **não fecha
  de fato** enquanto a ação da `A7` não for decidida. Rota, a decidir pelo consultor: reescrever a
  ação da `A7` (`reprovado` não fecha RDO — materializa o desfecho por outra via) **ou** dar ao
  instrumento um caminho para `reprovado`. A `LM-T2d` **não se refaz**: está `done` aprovada 100%. **ABSORVIDO no mesmo dia pelo `ESC-9`** → `DM-32` (rota (i): a `A7` não fecha RDO; materializa `blocked` razão `premissa` e **PARA**, como o `A3b`) e card **`LM-T2e`**, à frente da `LM-T2b` e antes da `LM-T4`.

- **`AE-23` — padrão de aceite que reescreve palavra do arquivo mede zero nos dois mundos; terceiro
  caso do mesmo derivado nesta série.** Achado do `scrum-master` **no ato do despacho** da
  `LM-T2e`, ao rodar as baselines do card antes de delegar (item 3 do gate), e devolvido ao
  `pantonic-consultant` — que o autorou. A linha 4 de `Verificação` da `LM-T2e` publicava
  `-Pattern 'ultima retentativa'` com baseline **1**; medido no despacho: **0**. Causa: o arquivo
  escreve **`última`**, com acento (`grep -c "última retentativa"` → 1; `grep -c "ultima
  retentativa"` → 0), e a regra que o consultor aplicou aos padrões — *"sem acento e sem crase,
  para não dependerem de escape do shell"* — tirou um caractere que **pertence ao texto da
  fonte**, não um que só atrapalharia o shell. Efeito: 0 antes, 0 depois — a linha vendida como o
  invariante que prova que a seção *O que obriga parada* ficou intocada **passaria igual se o
  executor apagasse a seção inteira**. Agravante medido no reparo: a ação nova da `A7` também
  contém *"última retentativa"*, de modo que o padrão acentuado iria a **2** — o invariante
  correto é o recorte `'retentativa ('`, 1 → 1, casando só a linha 230. **Reparo:** feito no card
  pelo `ESC-9` (linha 4 e a regra do cabeçalho da `Verificação`), **antes** do despacho; a rota,
  a ação da `A7` e a posição na fila não mudam. **Varredura do plano inteiro, medida agora:**
  extraídos os 24 padrões de `Select-String` de todos os cards e confrontados com os arquivos-alvo
  reais, **nenhum outro padrão deste plano sofre do defeito** — os padrões acentuados dos demais
  cards (`escalar não é desfecho de tarefa`, `pendência substantiva`, `esforço`, `O kit são`)
  casam ≥ 1, e os que casam 0 são todos **pós-estado declarado** (`>8 write-clusters`,
  `recomendacao=escalar (com bloqueante=nenhuma)`, `desfecho de RDO`, `consultant-spec`,
  `roteada ao planejador`). A `LM-T2c` e a `LM-T2d` estão limpas: **nada a consertar
  retroativamente**. **Residência:** o defeito é de **método**, não desta linha — é o terceiro
  caso do mesmo derivado no plano (`AE-19`, crase dupla, 0 → 0; `AE-21`, baseline de corpus que
  envelhece) e entra no acumulador **`TK-55`** (confiabilidade de derivado que erra sem sinal
  porque nada o confronta com a fonte), gated pelo encerramento do `P-0740`; dentro do plano,
  quem o lê é a **`LM-T5`**, mesma residência do `AE-19` e do `AE-21` — a regra que os três pedem
  é uma só: *padrão de aceite é recorte do literal da fonte, rodado nos dois mundos, nunca
  reescrito de memória*. **Não abre rodada própria.** O que o `B1` leva ao relatório de
  encerramento é a linha do `TK-55`.

- **`AE-24` — o produto (b) da `LM-T2b` colide com um teste pré-existente, e as contingências do
  card não alcançam a colisão.** Achado do executor da `LM-T2b` (2026-09-19), devolvido como
  `blocked` razão `premissa` — conduta correta, e é o `A3b` funcionando como desenhado: ele parou
  antes de entregar em vez de decidir por conta própria. Medido: o teste
  `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv` em
  `tests/test_telemetria_hook.py` afirma a linha do TSV com `modelo="Sonnet"` **literal**; o produto
  (b) do card manda `montar_args_append` normalizar o modelo para minúsculas, o que faz `sonnet` ≠
  `Sonnet` e derruba a asserção. A **contingência 2** do card autoriza ajustar teste pré-existente
  só quando ele *"afirmar a soma por `message.id` como resultado esperado"* — a grafia do modelo
  não é esse caso, e o executor não podia alargar a autorização sozinho (Regra 8). **Dado novo,
  medido pelo loop no mesmo ato e que o card não previa:** a linha que o hook gravou para esta
  própria execução saiu **exata** (72,9k contra 72.887 do `<usage>`), enquanto as três anteriores
  desta janela saíram infladas ×20,5, ×6,6 e ×4,8 — o defeito do `AE-3` é **real mas não
  universal**, e a frase do card *"grava sempre para mais"* é forte demais como está. As duas
  matérias vão juntas ao consultor porque incidem no mesmo card. **ABSORVIDO no mesmo dia pelo `ESC-10`** → `DM-33`: o produto (b) fica, a autorização de ajustar a asserção da linha 274 vira **Passo** do card (não contingência), o trabalho já aplicado na árvore permanece com um Passo 0 de conferência, e a `LM-T2b` volta `ready` na mesma posição da fila. A frase *"grava sempre para mais"* foi corrigida no card: vale para execução fechada **antes** de o reparo entrar na árvore. A quarta linha deixou de ser exceção — é a fórmula funcionando sobre a própria execução que a escreveu, com causa medida (`mtime` do hook 05:40 × fim do transcript 05:42; 371,6k pela fórmula velha contra 72,9k gravados).

- **`AE-25` — a linha 4 da `Verificação` da `LM-T2b` é inexequível: `Select-String` é
  case-insensitive por padrão.** Achado do executor no re-despacho da `LM-T2b` (2026-09-19),
  devolvido como `blocked` razão `premissa` — segunda vez que este card para, e de novo por conduta
  **correta**: ele rodou o comando publicado *literalmente como escrito* e recusou-se a alterá-lo
  por conta própria (Regra 8). Medido pelo loop nos três modos:
  `-Pattern 'EXA-T55\tSonnet' -SimpleMatch` → **1** (casa a linha nova, minúscula, porque
  `Select-String` ignora caixa sem `-CaseSensitive`); o mesmo com `-CaseSensitive` → **0**, que é o
  número que o card quer dizer; e `'EXA-T55\tsonnet' -SimpleMatch -CaseSensitive` → **1**. **A
  entrega não está em causa:** `pytest tests/test_telemetria_hook.py -q` → `10 passed` e
  `pytest tests/ -q` → `175 passed`, os dois exatamente os alvos do card, e a asserção da linha 274
  espera `sonnet` com o payload ainda entregando `Sonnet`. O que falhou foi o **derivado de
  aceite**, não o produto. **Confirmação em produção, no mesmo ato:** a linha que o hook gravou
  para esta execução saiu **52,5k contra 52.480 do `<usage>`** — o reparo do `AE-3` funciona.
  **Terceiro caso da família nesta janela** (`AE-21`, `AE-23`, `AE-25`), e o segundo em que o
  padrão publicado não mede o que a prosa do card afirma: a residência do acumulador é o `TK-55`,
  e quem lê dentro do plano é a `LM-T5`. A regra que os três pedem já está enunciada no `AE-23` —
  *padrão de aceite é recorte do literal da fonte, rodado nos dois mundos* — e este caso acrescenta
  a cláusula que faltava: **e com as opções que tornam a medida discriminante** (aqui,
  `-CaseSensitive`, sem o qual o padrão não distingue o mundo velho do novo). **ABSORVIDO no mesmo dia pelo `ESC-11`** → `DM-34`: linha 4 reparada com `-CaseSensitive` e medida nos dois mundos (1 na árvore entregue, 0 na cópia pré-entrega), e a `LM-T2b` vai **à revisão sem terceiro despacho** — redespachá-la dispararia `blocked` no próprio Passo 0, que já cumpriu a função.

- **`AE-26` — `backlog.py status` não materializa tarefa nenhuma deste plano: a gramática do
  instrumento e a forma dos cards divergem.** Medido pelo loop em 2026-09-19, ao tentar cumprir o
  `DM-34` (*"o estado quem materializa é você, pelo instrumento"*): `python .claude/tools/backlog.py
  status LM-T2b review` devolve **`linha de status ausente para LM-T2b`**. Causa: o
  `STATUS_BULLET_RE` (`backlog.py:70`) exige ``- **Status:** `<estado>` · AAAA-MM-DD[ · <razão>]``,
  com separador `·` e data, e os cards deste plano escrevem a forma em prosa, com travessão
  (``- **Status:** `ready` — card novo do `ESC-3`…``). **Não é o caso de um card:** dos **18**
  cards `LM-*` do plano, **0** casam a gramática estrita e 10 casam a forma em prosa — o
  instrumento não alcança nenhum. **Não bloqueou nada:** a materialização de status seguiu à mão,
  como em toda esta janela e nas anteriores, e o laudo não depende dela. O achado é do mesmo
  acumulador dos três anteriores (`TK-55`), com a diferença de que este não é um derivado errado e
  sim um **contrato não honrado entre instrumento e artefato**, e de escopo do plano inteiro — por
  isso a rota é a `LM-T5` (que já lê `AE-19`, `AE-21`, `AE-23`, `AE-25`) **com precedência sobre
  elas**: decidir se os cards passam a nascer na gramática estrita, se o parser passa a aceitar a
  forma em prosa, ou se o `DM-34` deixa de mandar usar o instrumento. **Não abre rodada própria** e
  não altera a rota de nenhuma tarefa aberta. **ABSORVIDO no mesmo dia pelo `ESC-12`** → `DM-35` (i) e card **`LM-T4b`**, à frente da `LM-T4`: o parser aprende a forma em prosa (0 de 18 casam hoje; 15 de 34 no repositório) e a escrita passa a preservar a cauda. Enquanto a `LM-T4b` não fecha, a materialização à mão pelo loop é o procedimento **declarado**, não improviso.

- **`AE-27` — três matérias de contrato abertas pelo laudo da `LM-T2b`, todas de dossiê e de
  instrumento, nenhuma de entrega.** Laudo de 2026-09-19 (`aprovado 100%`, bloqueante `nenhuma`,
  recomendação `escalar`), roteado pelo `B1` ao consultor. As três:
  1. **Teste órfão que a restrição do card deixou de pé.** `DM-33` alcançava só a linha 274, e com
     isso `test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas`
     (`tests/test_telemetria_hook.py:107`) sobreviveu com **nome e docstring afirmando um mecanismo
     que a entrega removeu** (a dedupe por `message.id`), enquanto o teste novo
     `test_tr_calcular_consumo_mesma_mensagem_duas_entradas_nao_dobra` (`:181`) o **duplica**, com
     fixture e asserções idênticas. Não é defeito da entrega — ela estava proibida de tocá-lo.
  2. **O extrator de `Arquivos-alvo` do instrumento de evidência infla o conjunto.** O dossiê
     declarou **9** alvos onde o card lista **2**: `review_evidence.py` varre os *code spans* do
     card inteiro e promoveu a alvo `message.id`, `251.1`, `505.2`, `2330.8`, `946.9`, `.jsonl` e
     `telemetria_hook.py`, gerando sete seções de diff vazias. Consequência que importa: inflar o
     conjunto de alvos **afrouxa a autoridade mecânica da dimensão `escopo`** — qualquer `.py`
     citado em prosa vira alvo. Matéria do contrato do instrumento, vizinha da `LM-T3a`.
  3. **`docs/telemetria.tsv` é proibido pelo card e escrito pelo módulo sob teste em produção.** O
     estado git não distingue escrita do hook de edição do executor, e a resolução da dimensão
     `escopo` dependeu da atribuição `alheio` **mais** contexto injetado pelo orquestrador — isto
     é, a camada mecânica sozinha não resolveu.
  O quarto achado do laudo — as duas paradas `A3b` como defeito de dossiê e de instrumento, nunca
  de execução — **já está fechado** por `DM-33` e `DM-34`. As três acima vão ao consultor junto do
  `AE-26`, com o qual a 2 e a 3 compartilham a matéria (contrato entre instrumento e artefato). **ABSORVIDO no mesmo dia pelo `ESC-12`** → `DM-35`: item 1 → card **`LM-T2f`** (fora do caminho crítico; os dois testes têm corpo byte a byte idêntico, medido); item 2 → card **`LM-T3b`** (a causa é o **limite do campo** em `_parsear_campos`, medida: 9 → 2 alvos na `LM-T2b`, e 1/2/5/1/2 inalterados nos demais cards); item 3 → **não vira card**, porque `_eh_registro_orquestracao('docs/telemetria.tsv')` já devolve **True** (medido) e o balde `registro_orquestracao` da `DB-25` já tira o arquivo do veredito — o resíduo é de **rubrica** e vai à `LM-T5`, cujo alvo é `docs/RUBRICA_DE_REVISAO.md`; item 4 → já fechado por `DM-33` e `DM-34`.

- **`AE-28` — a `Verificação` 2 da `LM-T4b` é insatisfazível dentro do escopo do próprio card.**
  Achado do executor no despacho da `LM-T4b` (2026-09-19), devolvido como `blocked` razão
  `premissa` **antes de editar qualquer arquivo-alvo** — triagem na fase de plano interno, que é o
  momento mais barato possível para o achado aparecer. Conferido pelo loop, ponto a ponto:
  a `Verificação` 2 manda `backlog.py status LM-T2f ready` sair **0** depois do reparo; a `LM-T2f`
  **já nasceu `ready`** (linha 1767 deste plano); com o `STATUS_BULLET_RE` corrigido pelo produto
  (a) do próprio card, esse token passa a ser **lido**, o `atual` da transição vira `ready`, e
  `('ready','ready')` **não está** em `_TRANSICOES` (`backlog.py:891-904`, conferido por
  introspeção). O comando passa a cair em *"transição fora da tabela de §2.7"*, **exit 1** — nunca
  exit 0. Hoje ele sai `linha de status ausente` (exit 3) **só porque o parser não lê o bullet**:
  a baseline do card está certa, e é o alvo que é inalcançável. As três saídas possíveis —
  self-loop em `_TRANSICOES`, tratar `atual == estado` como no-op, ou outra — são **decisão de
  máquina de estados**, fora do *Produto do módulo* e contra as *Restrições*; o executor enumerou
  as três e **não escolheu**, que é a conduta que o `G-NOASK` e a Regra 8 pedem. **Sétimo achado
  da família nesta janela** (`AE-19`, `AE-21`, `AE-23`, `AE-25`, `AE-26`, `AE-27` item 2, `AE-28`)
  e **terceiro card seguido** cuja linha de aceite não sobrevive ao contato com a árvore. O padrão
  já não é sobre uma linha: é sobre **como o aceite é autorado**, e a residência disso é a
  `LM-T5`. **ABSORVIDO no mesmo dia pelo `ESC-13`** → `DM-36` (i) e (ii): a `Verificação` 2 passa a medir o caminho de escrita sobre **cópia da fixture** `tests/fixtures/backlog/verde` em `tmp_path`, com transição `ready → in-progress` (que **está** em `_TRANSICOES`) e cauda em prosa que tem de sobreviver — medido no mundo de hoje: exit **3**, `linha de status ausente para ALF-T1`. A tabela de transições **não** entra no escopo do card.

- **`AE-29` — `backlog.py status` não alcança tarefa nenhuma deste plano, e o bullet de `Status` é
  só metade da causa.** Achado do `pantonic-consultant` no `ESC-13` (2026-09-19), medindo o mundo
  **depois** do reparo que a `LM-T4b` contrata — e não o mundo de hoje, que é o que o `AE-26` já
  descreve. Método: cópia do repositório, `STATUS_BULLET_RE` relaxado em memória, `carregar()` e
  `transacionar_status()` chamados por introspeção. Resultado: com o parser corrigido, **20 de 21**
  bullets passam a ser lidos e a transição **ainda** morre em **exit 3**,
  `linha de índice ausente para P-0740`. Causa: o plano é carregado com `id = "P-0740"` (do arquivo)
  e a linha de índice do diário tem `id = "P-0740-LM"`; `_posicao_indice` casa por **igualdade de
  id** e não encontra nada. Medido também que a rota óbvia não serve: casar por prefixo é **ambíguo**
  (`P-0729` tem cinco linhas de índice), e casar por caminho do plano não funciona porque
  `LinhaIndice.arquivo` não guarda o caminho do plano (zero casamentos para **todos** os planos,
  medido). **Alcance:** não é defeito de card nem deste plano — é o contrato entre plano e índice
  no `backlog.py`, cuja residência é o **`P-0739`** (*"O pickup vira instrumento"*), hoje
  **estacionado por ato do dono** até o `P-0740` encerrar. **Rota:** registrar aqui e levar ao
  `P-0739` no retorno dele, pela `LM-T5a`, que é quem reabre aquele plano para reescrita — sem
  abrir card de código neste plano. **Consequência imediata, e é emenda ao `DM-34`:** enquanto o
  `AE-29` estiver aberto, o loop materializa estado **à mão**, e isso é **procedimento declarado**,
  não improviso — o `DM-34` (ii) mandava usar o instrumento, e o instrumento não alcança. A
  `LM-T4b` **não** perde razão de ser: ela fecha a metade que é deste plano, e sem ela o `P-0739`
  consertaria o índice para um leitor que continuaria sem ler o estado.

- **`AE-30` — a `Verificação` 3 da `LM-T5` mede um arquivo que a própria `LM-T5` está proibida de
  tocar.** Achado do loop no gate de delegação (2026-09-19), **antes de despachar** — nenhum
  executor gasto. Medido: a `Verificação` 3 do card exige que
  `Select-String docs/plans/P-0739-backlog-instrumento.md -Pattern '- **Objetivo:**' -SimpleMatch`
  **suba em 6** sobre o valor do despacho (re-medido agora: **18**, batendo com o `ESC-6`); mas o
  `ESC-13` (`DM-36` (iii)) retirou o segundo entregável desta tarefa e escreveu no mesmo card que
  *"**esta** tarefa não toca `docs/plans/P-0739-backlog-instrumento.md`"*. A linha de aceite ficou
  órfã do entregável que a justificava: ela pertence agora à `LM-T5a`. As outras duas verificações
  estão íntegras e foram conferidas por mim no gate — rubrica com **274** linhas e **0**
  ocorrências de `LM-T`, que discrimina —, e a contagem de cards a julgar bate: **22** cards no
  plano menos `LM-T5`, `LM-T5a` e `LM-T6` = **19**, exatamente o que o `Pronto quando` prevê como
  relação. **Oitavo achado da décima segunda classe, e o mais instrutivo de todos:** ele viola a
  alínea (d) do critério **(xii)** — *"alvo alcançável dentro do escopo declarado do card"* — que é
  **este mesmo card** que vai publicar na rubrica. O defeito sobreviveu ao ato que escreveu a regra
  contra ele, o que confirma, melhor que qualquer argumento, que a classe é de **método** e não de
  atenção: quem acabara de enunciar a regra não a aplicou ao próprio texto três parágrafos abaixo.
  Reforça o que a `LM-T5` tem de produzir: a régua precisa virar **passo de conferência executável
  na autoria**, não mais um critério para ler com cuidado. **ABSORVIDO no mesmo dia pelo `ESC-14`** → `DM-37`: a linha sai da `LM-T5` (já reside como `Verificação` 1 da `LM-T5a`), as duas que ficam foram reescritas na forma normativa com baselines re-medidas, e a classe deixa de ser tratada por critério de leitura: nasce o card **`LM-T5b`** (`card_check.py`), que roda os comandos do card e os confronta com o mundo.

- **`AE-31` — a pendência e os quatro achados do laudo da `LM-T5`.** Laudo de 2026-09-19
  (`ressalva 88%`, bloqueante `nenhuma`, recomendação `escalar`), roteado pelo `B1`. A entrega
  ficou de pé — 20 cards julgados, a forma normativa publicada em `### 8.1`, a frase de ciclo na
  rubrica, crescimento 69 ≤ 70 — e a única dimensão fora de `conforme` é `criterio-de-pronto`
  (`parcial`).
  1. **Pendência, e é a que bloqueia a `LM-T5b`:** a norma da `8.1` torna a `Verificação` 1 da
     `LM-T5b` **inalcançável** — ela exige `card_check --tarefa LM-T3b` sair **0**, mas os itens 2
     e 3 da `LM-T3b` não trazem os três elementos (sem bloco cercado, sem `Medido antes`), e o
     item 3 da **própria `LM-T5b`** também não. Decisão devida **antes** do despacho da `LM-T5b`:
     a norma é **prospectiva** (e a baseline do aceite muda de card) ou **retroativa** (e os cards
     abertos se reautoram)? É de novo a alínea (d) do critério (xii), agora entre dois cards.
  2. **`LM-T4b`:** o `Pronto quando` exige `backlog.py status` transitar **card real** — alvo que o
     próprio card declara inalcançável pelo `AE-29`, depois de o `ESC-13` mover a `Verificação` 2
     para fixture. A emenda corrigiu o aceite e deixou o `Pronto quando` para trás: mesma causa do
     `AE-30`, agora no campo vizinho.
  3. **`LM-T4`:** publica `DM-2`..`DM-5` em `GOVERNANCA.md` §7, lista que a **checagem 4** do
     `.claude/checks/check-readme.ps1` conta contra a tabela *"Os guardrails"* do `README.md`;
     `.claude/README.md` não está nos `Arquivos-alvo` e o guarda não está na `Verificação`. Mesma
     classe do `AE-12`, critério (viii).
  4. **A numeração dos critérios:** o card fala em *"doze critérios"* enumerando **treze**, e
     prescreve mais duas aferições sem numeral (`ESC-7`, rota de achado órfã; `ESC-8`, partição de
     domínio). A entrega as publicou como **(xiv)** e **(xv)** — decisão de notação dentro do
     arquivo-alvo e dentro do escopo, que o laudo não rebaixou. O planejamento reconcilia o
     numeral no card.
  **Nono caso da décima segunda classe, achado pelo reviewer e o mais direto de todos:** as três
  linhas de `Verificação` do **próprio card da `LM-T5`** publicam a baseline como
  `**Medido no ESC-14: 274**`, fora do literal `**Medido antes: <valor>**` que essa mesma tarefa
  foi mandada normatizar — **o card não passaria no `card_check` que ele prescreve**. Não é ironia:
  é a medida de que a norma precisa do instrumento para valer, que é exatamente a tese da
  `LM-T5b`. **ABSORVIDO no mesmo dia pelo `ESC-15`** → `DM-38`: item 1 → a norma é **exigível no despacho**, card a card, e o aceite da `LM-T5b` migra para **fixture** (`EX-T1`/`EX-T2`/`EX-T3`), com a regra geral nova *aceite de instrumento mede-se sobre fixture, artefato vivo é uso*; item 2 → `Pronto quando` da `LM-T4b` reparado para a fixture; item 3 → `README.md` nos `Arquivos-alvo` da `LM-T4` e `check-readme.ps1` → exit 0 na `Verificação`, como guarda de regressão do invariante de contagem; item 4 → numeral reconciliado por nota, com a rubrica como referência canônica e o card fechado intocado.

- **`AE-32` — o `card_check` tem falso verde residual, e o gate da `### 8.1` não pode ser ligado
  como está.** Laudo da `LM-T5b` (2026-09-19, `ressalva 91%`, bloqueante `nenhuma`, recomendação
  `escalar`), roteado pelo `B1`. O instrumento **existe e pega o que foi contratado** — as três
  fixtures saem como o card manda, o contrato de segurança está implementado e o parser é
  importado, não reescrito. Três matérias:
  1. **Falso verde, reproduzido pelo reviewer:** item numerado cujo bloco cercado **não vem logo
     após `N.`** é descartado **em silêncio**, e o card sai `exit 0` com a baseline envelhecida
     por conferir. Caso rodado: item com prosa de abertura declarando `Medido antes: 42` contra
     comando que imprime `999` → **exit 0**. É a classe inteira que o instrumento existe para
     fechar, sobrevivendo dentro dele.
  2. **A `### 8.1` não define de forma parseável onde começa um item.** Prosa antes do bloco
     cercado — que é a forma do item 1 da `LM-T3b`, card que a própria `### 8.2` julga *"passa"* —
     é legítima pela norma escrita e **invisível** para o `_ITEM_HEAD_RE`. Rota: emenda à `8.1`
     fixando `N.` seguido **imediatamente** do bloco cercado, mais o dever de o instrumento
     **nomear** todo item numerado que não casar (em vez de ignorá-lo).
  3. **"Fora do aceite mecânico" não tem mecanismo.** O card manda o autor *"reescrever o comando
     recusado ou declará-lo fora do aceite mecânico"*, e a segunda via não existe — sem flag, sem
     marcador. Medido: os **4** itens da `LM-T2e` e o item 1 da `LM-T5a` usam
     `pwsh -Command "…; exit $LASTEXITCODE"`, são **recusados** pelo contrato de segurança e
     portanto **nunca** sairiam 0 — contra a regra da `8.1` de que *card cujo `card_check` não sai
     0 não se despacha*. Ligar o gate hoje bloquearia card legítimo.
  4. **O contrato de segurança não tem teste.** O `Pronto quando` exige *"recusa comando fora da
     lista fechada"*; o reviewer **verificou em execução** que metacaractere e token fora da lista
     são recusados sem executar o alvo, mas nenhum dos três testes trava esse comportamento.
  **Consequência operacional imediata, e é minha:** o gate *"card cujo `card_check` não sai 0 não
  se despacha"* **não entra em vigor** nesta janela. O `card_check` roda como **instrumento de
  apoio** no gate de delegação — o loop lê o que ele reporta e continua re-derivando as baselines à
  mão —, e só vira gate quando os itens 1 a 3 fecharem. Décimo caso da décima segunda classe, e o
  primeiro **dentro do próprio instrumento** que a classe produziu. **ABSORVIDO no mesmo dia pelo `ESC-16`** → `DM-39` e card **`LM-T5c`**, à frente da fila, com as quatro matérias num assunto só — mais uma **quinta**, achada no `ESC-16` ao rodar o instrumento contra o card que o repara: a saída do subprocesso volta em `cp1252` e inviabiliza `Medido antes` com acento (`DM-39` (iv)); a suspensão do gate decidida pelo loop está **endossada** e registrada em `DM-39` (ii) — efeito suspenso, texto não revogado, reativação pela própria `LM-T5c`.

- **`AE-33` — o `card_check` trocou falso verde por falso vermelho, e o gate segue inligável.**
  Laudo da `LM-T5c` (2026-09-19, `ressalva 76%` — o mais baixo da janela —, bloqueante `nenhuma`,
  recomendação `escalar`), roteado pelo `B1`. O falso verde do `AE-32` **fechou**: o reviewer
  reproduziu o caso original (item fora da forma com `Medido antes: 42` contra saída `999`) e hoje
  ele sai `exit 1` nomeando o item. Mas duas matérias novas:
  1. **Falso vermelho por marcador de item mal ancorado.** O card prescreveu em (b) varrer
     `^\s*\d+\.` sobre um texto que o parser que ele próprio manda reusar
     (`rdo._parsear_campos`) **já achatou numa linha só** — decisão não fechada, que a execução
     resolveu como *"dígito precedido de espaço em qualquer lugar"*. Efeito medido: card
     **conforme** à `### 8.1`, com prosa legítima depois do `Medido antes` citando `8.1` ou
     `Python 3.12`, sai `exit 1` com **itens fantasma** — no próprio card da `LM-T5c`, "item 8"
     duas vezes. Rota: ancorar o marcador em **quebra de linha do markdown cru**, ou reservar uma
     linha do dossiê de campos sem achatamento.
  2. **A matéria 5 fechou só para um tipo de filho, e regrediu outro.** `encoding="utf-8"` fixo
     fez passar o filho que reconfigura `stdout` para UTF-8 (o próprio `card_check` aninhado:
     literal com acento fecha `exit 0`), mas filho `python` simples emite `cp1252` (`b'caf\xe9'`)
     e **era comparável antes** — agora não é; e `pwsh` emite **OEM** (`b'n\xc6o'`), que não é
     comparável em nenhum dos dois mundos — sendo `pwsh` a **forma canônica de comando do kit**.
     Rota: decodificar por tentativa (UTF-8, depois locale/OEM), ou impor `PYTHONIOENCODING` /
     `OutputEncoding` ao filho.
  **Consequência operacional, e confirma a decisão do `DM-39` (ii):** o gate *"card cujo
  `card_check` não sai 0 não se despacha"* **continua suspenso**. Ligá-lo hoje reprovaria card
  conforme — o erro simétrico do que o `AE-32` descrevia, e pior para o loop, porque bloqueia
  despacho legítimo. O `card_check` segue como **instrumento de apoio**, com a ressalva nova de que
  o vermelho dele **não** é evidência até a matéria 1 fechar. Décimo primeiro e décimo segundo
  casos da décima segunda classe. **ROTEADO pelo `ESC-17`** → `DM-40`: as duas matérias são **re-especificação** (ler o bloco bruto em vez do campo achatado por `rdo._parsear_campos`; política de codificação por tipo de filho) e ficam **abertas**, para o planejamento **pós-marco**, com residência no acumulador `TK-55` — nenhum card de código nasce agora. O gate segue **suspenso**, a frase *o vermelho do `card_check` não é evidência* entra na `### 8.1` pelo card **`LM-T5d`** (fora do caminho crítico, não antes do marco), e a cadeia inteira vira **insumo do piloto** (`DM-40` (v)).

- **`AE-34` — rótulo de campo que quebra de linha torna o card ilegível para o instrumento de
  evidência, e o laudo fica bloqueado.** Achado do loop no Passo 6 da `LM-T4b` (2026-09-19), com a
  **entrega já pronta e verificada** (`25 25`, `41 passed`, `186 passed`). Medido:
  `review_evidence.py --tarefa LM-T4b` sai **exit 1**,
  `campo obrigatório ausente em 'LM-T4b': 'pronto-quando'`. Causa isolada por comparação: o rótulo
  do campo foi decorado e **quebrou de linha** — `- **Pronto quando (reparado pelo ESC-15, DM-38
  (iii) — o campo vizinho que a emenda do` na linha 2176, com o `):**` que o fecha caindo na
  **linha seguinte** —, e o parser lê **linha a linha**. A decoração em si **não** é o defeito: a
  `LM-T5` tem `- **Pronto quando (reescrito pelo ESC-13, DM-36 (v) — contagem é relação, não
  constante):**` e é lida sem problema, porque **cabe numa linha**. Varredura do plano inteiro:
  só a `LM-T4b` está afetada; `LM-T5`, `LM-T4` e `LM-T3b` geram dossiê com `exit 0`.
  **Décimo terceiro caso da classe, e o primeiro a derrubar o instrumento de evidência** — os
  anteriores derrubavam comando de aceite. Regra que ele pede, e que é mecânica:
  **rótulo de campo termina na mesma linha em que começa**; decoração no rótulo é permitida
  enquanto o `:**` couber na primeira linha. Rota: reparo do card (uma requebra, zero caractere de
  conteúdo alterado) e critério novo na rubrica de autoria, vizinho do (xii). **ABSORVIDO no mesmo dia pelo `ESC-18`** → `DM-41`: rótulo requebrado (medido depois: `review_evidence.py --tarefa LM-T4b` → **exit 0**, dossiê gerado) e o critério `(xvi)` acrescentado ao card **`LM-T5d`**, que passa a ser *a rubrica posta em dia* e segue fora do caminho crítico.

- **`AE-35` — a fronteira razão/cauda no bullet de `Status`, e o aceite que só exercitou um ramo.**
  Laudo da `LM-T4b` (2026-09-19, `ressalva 91%`, bloqueante `nenhuma`, recomendação `escalar`),
  roteado pelo `B1`. A entrega fechou o que era deste plano — os **25** bullets de `Status` passam
  a ser lidos (`25 25`), a cauda sobrevive à transição sobre fixture, a recusa continua recusando e
  `_TRANSICOES` ficou intocada. Duas matérias:
  1. **Pendência:** o módulo entregue reescreve **razão e cauda no mesmo campo**, e com isso o
     round-trip `blocked → ready` **perde a prosa**. Decisão devida: onde mora o reparo da
     fronteira — neste plano ou no `P-0739` (gramática do `backlog.py`), que o dono **estacionou**.
     Não é defeito de execução: o card contratou preservar a cauda, e ela é preservada no caminho
     que o card mandou exercitar.
  2. **Achado:** a `Verificação` 2 e os três testes exercitam **só o ramo em prosa** (sem razão de
     máquina); **nenhuma** linha de aceite discrimina o ramo canônico `· data · razão — cauda` —
     que é justamente a forma que a escrita do módulo **emite** ao transitar para `blocked` com
     `--razao`. É a classe do critério (xii): o aceite não cobre o mundo que o produto cria.
  Décimo quarto caso da série, e o primeiro em que o buraco do aceite está no **ramo que o próprio
  produto gera**, não no que ele lê. **ABSORVIDO no mesmo dia pelo `ESC-19`** → `DM-42`: item 1 → residência **neste plano** (a gramática é do `DM-35` (i), não herança do `P-0739`), card **`LM-T4c`**, **pós-marco**, porque o `AE-29` torna o caminho defeituoso inalcançável hoje; item 2 → critério **`(xvii)`** na `LM-T5d`.

- **`AE-36` — o produto (c) da `LM-T4` contradiz os `Arquivos-alvo`, o `Pronto quando` e três das
  quatro `Verificações` do mesmo card.** Achado do executor no despacho da `LM-T4` (2026-09-19),
  devolvido como `blocked` razão `premissa` **sem nenhuma edição** — quarta vez nesta janela que um
  executor para diante de matéria que exigiria decisão sua, e a segunda em que o faz antes de tocar
  arquivo. Medido por ele: o produto (c) manda registrar *"o que permanece, o que migra para o
  `scrum-master` e o que é aposentado"* sobre `proximo-passo`/`handover`, e a forma **ratificada**
  que ele absorve (`AUT-T6`, `DU-5`/`DU-9` do `P-0737` — *"transcrever, não deliberar"*) manda
  **apagar** `.claude/skills/proximo-passo/` e `.claude/skills/handover/` e criar
  `passagem-de-bastao`. Mas, no mesmo card: os `Arquivos-alvo` listam os **dois** arquivos como
  alvos de edição; o `Pronto quando` exige *"o item 5 do gate de delegação em
  `.claude/skills/proximo-passo/SKILL.md` está **reescrito**"*; e três das quatro `Verificações`
  exigem os dois **vivos** e a contagem de skills **intacta** — a 1 (`check-drift` exit 0, que
  compara o `.claude/README.md` com o regenerado), a 3 (`check-readme.ps1` exit 0 com **11
  skills**, re-medido no despacho) e a 4 (`Select-String -Path` sobre esses caminhos). Apagar as
  duas skills derruba 1, 3 e 4; mantê-las contraria a forma ratificada que o card absorve.
  **Escolher entre as duas rotas, ou autorar a partição de três vias, seria decisão do executor** —
  e ele não a tomou, que é a conduta do `G-NOASK` e da Regra 8. Os produtos (a), (b) e (d) estão
  **intocados** e não são objeto do impedimento: a matéria é só o (c). Décimo quinto caso da série,
  e o de maior alcance — o primeiro em que a contradição é **entre o produto e o aceite do mesmo
  card**, e em que a rota escolhida muda a **superfície pública do kit** (duas skills a menos, uma
  a mais), o que toca contagem de projeção, `DOC_MAP` e qualquer consumidor. **ABSORVIDO no mesmo dia pelo `ESC-20`** → `DM-43`: **técnico** — a rota do (c) já estava ratificada pelo dono (`DU-5`, 2026-08-22; natureza da skill nova fixada por ele em `TK-36`, 2026-08-13, como superfície **agente↔agente** que *ele não invoca, não lê e não acompanha*), e o que estava errado era o **aceite** do card. `Arquivos-alvo`, `Pronto quando` e as `Verificações` 1, 3 e 4 foram reescritos para o mundo pós-remoção, com duas verificações novas (diretórios ausentes; citações por caminho: **4** e **3** medidas hoje) e a regeneração das duas projeções no mesmo ato (11 → **10** skills).

- **`AE-37` — a aposentadoria fechou por caminho e deixou ponteiro quebrado por nome em cinco
  superfícies vivas.** Laudo da `LM-T4` (2026-09-19, `aprovado 100%`, bloqueante `nenhuma`,
  recomendação `escalar`), roteado pelo `B1`. A entrega está íntegra — os dois literais copiados
  das residências únicas, o bloco A intocado, a doutrina de status × veredito conforme `DM-25`,
  `DM-26` e `DM-32`, as seis verificações verdes, skills 11 → 10, guardrails 18 → 19. Duas
  matérias, e a primeira é de método:
  1. **Varredura por caminho não alcança citação por nome.** As `Verificações` 5 e 6 medem
     `.claude/skills/proximo-passo/` e `.claude/skills/handover/` — **caminhos** —, e a citação por
     **nome** sobrevive em superfície viva **fora dos `Arquivos-alvo`**: `.claude/settings.json:6`
     (`Edit(/.claude/skills/proximo-passo/**)`, regra de permissão para diretório que deixou de
     existir), `.claude/skills/bootstrap-pantonic/SKILL.md:53` (**manda copiar** as duas skills
     apagadas — um projeto novo nasceria quebrado), `.claude/skills/diario-de-obras/SKILL.md:45` e
     `.claude/global/docs/GOVERNANCA_MEMORIAS.md:154`. Rota: card único de **regularização de
     superfície** (`G-SURFACE`, §7 item 16) no replanejamento, com varredura por **nome** além da
     varredura por caminho.
  2. **A proibição do card colidiu com a própria aposentadoria.** O *Não fazer* proibia reabrir o
     **item 17** (`G-REPLAN`) e não previu que o próprio item 17 **cita a skill que a tarefa
     apaga** — `GOVERNANCA.md:804` e `README.md:748`, os dois **dentro** dos `Arquivos-alvo`. O
     executor obedeceu e **reportou**, conduta correta por `G-PLANFIDELITY`/`G-NOASK`. Rota: a
     mesma rodada libera o item 17 para a troca de um nome.
  **Décimo sexto caso da série**, e o primeiro em que o aceite estava **certo no que media** e
  incompleto **no eixo**: caminho, não nome. É material direto para o critério (xii) — a régua
  ganha o eixo que faltava. **ABSORVIDO no mesmo dia pelo `ESC-21`** → `DM-44` e card **`LM-T4d`** (as duas matérias num assunto só, recomendado **antes da `LM-T3b`** por urgência assimétrica medida no `bootstrap-pantonic`), com o mapa de sucessão fechado no card e `.claude/settings.json` **fora do escopo**, como ato do dono no relatório de encerramento.

- **`AE-38` — o colapso de enumeração que a autorização estreita não previu, e um ponteiro
  pré-existente.** Laudo da `LM-T4d` (2026-09-19, `aprovado 100%`, bloqueante `nenhuma`,
  recomendação `escalar`), roteado pelo `B1`. A entrega fecha o `AE-37`: `` `proximo-passo` `` e
  `` `handover` `` vão a **0** nas oito superfícies, o `bootstrap-pantonic` deixa de mandar copiar
  skill inexistente, a palavra *handover* em prosa ficou intacta e o `.claude/settings.json` não
  foi tocado. Duas matérias:
  1. **Pendência:** a linha 17 da tabela *Os guardrails* do `README.md` enumerava **duas** skills
     (`scrum-master`/`proximo-passo`) que o mapa de sucessão **colapsa numa só**, e o texto
     publicado ficou *"roteamento das skills `scrum-master`/`scrum-master`"* (`README.md:748`) —
     redundância visível em documento canônico. O card autorizou trocar *"só o nome"* e **não
     fechou o caso do colapso**; a execução obedeceu à restrição estreita **corretamente**, e o
     laudo não a rebaixou por isso. O mesmo padrão, redundante mas **não falso**, aparece no
     *Enforcement* do item 17 (`GOVERNANCA.md:804`). Rota: autorização estreita **nova** para
     colapsar as duas enumerações.
  2. **Achado pré-existente, não introduzido pela entrega:**
     `.claude/skills/diario-de-obras/SKILL.md:301` cita *"ver skill `passagem-de-bastao` §2"*, e a
     skill sucessora **não tem seção 2** — usa *Parte 1..4*, e a matéria está na *Parte 3*. Medido
     em `de28d01`: a `handover` removida **também** não tinha seção 2, logo a imprecisão é
     **anterior** à `LM-T4d` e fora do mandato dela. Rota: tíquete de correção de ponteiro.
  **Décimo sétimo caso da série**, e o primeiro em que o defeito nasce da **autorização estreita**
  fazendo exatamente o que devia: proibir o executor de decidir. Não é argumento contra a
  autorização estreita — é a demonstração de que ela precisa **prever o caso que cria**, que é o
  eixo do `DM-18` (i) aplicado a autorização em vez de a contagem.

- **`ESC-22` — queda do consultor por limite de sessão, sem resposta.** 2026-09-19: o
  `pantonic-consultant` terminou por erro de API (`rate_limit`, HTTP 429, *session limit*, reseta
  às 09:10 `America/Sao_Paulo`) **sem devolver** as duas alocações do `AE-38` nem a varredura final
  da `LM-T3b`. Notificação **sem bloco `<usage>`**: o consumo desta passagem é `PARCIAL — trecho
  pré-queda não medido`, e nenhuma linha de telemetria é apensada por ela (`GOVERNANCA.md` §4.2 —
  telemetria é medida, nunca estimada). **Nada se perde:** o `AE-38` está registrado com as duas
  matérias e a rota que o laudo sugeriu, e vai ao relatório de encerramento como matéria de
  planejamento pós-marco. **Consequência para a `LM-T3b`:** a varredura do consultor era
  conveniência, **não gate** — o gate de delegação é do loop, que re-deriva toda baseline no
  despacho (`proximo-passo`, item 3, hoje na `passagem-de-bastao`), e a ordem da fila é do loop
  pela Diretiva de execução item 4. O loop segue e gateia a `LM-T3b` por medida própria; se a
  medida recusar, a janela encerra com o que há, que é o `B3`.

- **`AE-39` — o invariante de aceite publicado como literal envelheceu em um dia e quase disparou
  um `blocked` indevido.** Laudo da `LM-T3b` (2026-09-19, `aprovado 100%`, bloqueante `nenhuma`,
  recomendação `escalar`). A entrega fecha o `AE-27` item 2: a extração da `LM-T2b` cai de **9**
  para **2**, e as outras cinco ficam inalteradas — re-medidas pelo reviewer **nos dois mundos**
  (pré-reparo `1, 2, 8, 1, 2`; pós-reparo `1, 2, 8, 1, 2`). O defeito: a `Verificação` 2 e o
  `Pronto quando` do card publicam `1, 2, **5**, 1, 2`, e a extração da `LM-T4` é **8** desde a
  reescrita legítima do `ESC-20` — mudança de **outro card**, não deste. **Lida ao pé da letra, a
  Contingência 2 mandaria `blocked` razão `premissa`**, e só não o fez porque o gate de delegação
  re-mediu e publicou `1, 2, 8, 1, 2` no despacho, conferindo os oito caminhos um a um para
  descartar inflação. Com o consultor indisponível (`ESC-22`), esse `blocked` teria encerrado a
  janela num **falso bloqueio**. Rota, ao planejamento pós-marco: corrigir o literal do card,
  revisar a linha `LM-T3b` da `### 8.2` — que o julga *"passa"* — e escrever **contingência de
  invariante em relação** (*"inalteradas entre os dois mundos"*), **nunca em literal**.
  **Décimo oitavo e último caso da série nesta janela**, e o que melhor a resume: é o critério
  (x)/(xiii) da própria rubrica **dentro do card que a `### 8.2` aprova**, e o único em que o
  defeito foi neutralizado **antes** de custar qualquer coisa — pelo gate, por medida, no despacho.

- **`AE-40` — o card da `LM-T9` não gera dossiê de evidência: tem `Arquivos-alvo` **e**
  `Entregável`.** Achado do loop em 2026-09-19, ao conferir os instrumentos depois de materializar
  o `DM-45`. Medido: `review_evidence.py --tarefa LM-T9` sai **exit 1**,
  `'LM-T9' precisa de exatamente um entre 'Arquivos-alvo' e 'Entregável' (tem os dois)`. **É
  pré-existente**, não introduzido pela emenda do `DM-45` — a emenda expandiu o **conteúdo** do
  `Entregável` e não criou campo nenhum; os dois já conviviam desde a autoria do card. Conferido
  que é isolado: `LM-T6`, `LM-T5a` e `LM-T4c` geram dossiê com `exit 0`. Consequência se não for
  reparado: a `LM-T9` chega ao Passo 6 e **o laudo não pode ser gerado**, que é exatamente o que o
  `AE-34` causou na `LM-T4b` — com a diferença de que lá o rótulo estava quebrado e aqui há um
  campo a mais. Rota: reparo do card pelo consultor — decidir qual dos dois campos é o dele, já que
  a `LM-T9` tem produto documental (`Entregável`) **e** três arquivos nomeados. **Décimo nono caso
  da série**, e o terceiro em que o defeito derruba um **instrumento** em vez de um comando de
  aceite (`AE-26`, `AE-34`, `AE-40`).
- **`AE-41` — o item (b) da `LM-T8` nomeia o que publicar e não onde: o local ficaria com o
  executor.** Devolução `blocked` razão `premissa` em 2026-09-19, no primeiro despacho da tarefa
  depois que a `DM-27` e o fechamento da `LM-T4` a destravaram. O executor conferiu as âncoras e
  **elas batem** — `pantonic-planner.md:5`, `:27` e `:283` nos literais citados —, e o item (a) é
  executável como está. O que não fecha é o item (b): ele manda publicar a **régua de tema** e os
  cinco critérios de autoria (`DM-18`, `DM-21`..`DM-24`) no arquivo do planner, mas os **dois**
  pontos que o card nomeia (`:27` e `:283`) são ambos da **gramática de cabeçalho**. Para a régua
  de tema e os critérios não há ponto nomeado, e os candidatos medidos pelo executor são pelo menos
  três — o bullet de `## Fatos estáveis`, as *Regras de autoria* da Fase 3, e o item 5
  (*Dimensionamento*) da Fase 4, hoje *"parta por ramo, nunca por volume arbitrário"* (linhas
  193-196) — mais a hipótese de seção nova. `Pronto quando` e `Verificação` **não discriminam**
  nenhum deles: a linha 1 mede só o `tools:` e as linhas 2-3 são regressão de `kit_check`. Escolher
  o local é **decisão**, e decisão não é do executor (`G-NOASK`, `GOVERNANCA.md` §7 item 18;
  `CLAUDE.md` global, Regra 8). Rota: reparo do card pelo consultor (`ESC-23`) — fixar o local de
  cada bloco e dar a `Verificação` que o discrimine, ou partir o card, deixando o item (a) seguir
  sozinho. **Vigésimo caso da série**, e o segundo em que o defeito é de *onde publicar* e não de
  *o que publicar*. **ABSORVIDO no mesmo dia pelo `ESC-23`** → `DM-46` e card `LM-T8`
  reescrito: local nomeado nos quatro pontos, literal `de`/`para` dentro do card, `Verificação`
  de doze linhas discriminando bloco a bloco com os dois valores rodados, e o card de volta a
  `ready` — **inteiro**, num despacho só. O `ESC-23` mediu ainda um defeito que o achado não
  trazia: a concessão de `Bash` torna **falsas três frases** do mesmo arquivo, que o item (a)
  passa a fechar no mesmo ato (`DM-46` (iii)).
- **`AE-42` — a `LM-T8` não é barrada pelo card, e sim pelo classificador de permissão do
  harness.** Segunda devolução `blocked` da mesma tarefa em 2026-09-19, **logo depois** do reparo
  do `ESC-23`/`DM-46` e com o gate verde: `python .claude/tools/card_check.py --tarefa LM-T8` sai
  **exit 0**, e o executor conferiu os literais antes de tentar editar. A recusa veio do harness:
  `Edit` em `.claude/agents/pantonic-planner.md` (literal 1, o `tools:` ganhando `Bash`) devolveu
  **`Blocked by classifier`**. O executor **não contornou por `Bash`**, e agiu certo — mudança de
  configuração de agente é superfície de permissão, e superfície de permissão só o dono altera
  (`GOVERNANCA.md` §7 item 13). **Não é reparável por consultor**: o card, os literais, os quatro
  locais e os doze comandos de aceite estão todos fechados e medidos; nenhuma emenda de plano
  levanta um classificador. **É a terceira vez que esta tarefa para na mesma classe de causa** —
  `AE-11` (regra ausente nos dois `settings.json`), `DM-27` (o dono concede em conversa; a regra
  `Edit`/`Write` sobre `.claude/agents/**` é instalada e a lição fica: *permissão concedida em
  conversa não é permissão instalada*) e agora `AE-42`, em que a regra **está** instalada e mesmo
  assim o classificador barra. A lição da `DM-27` ganha um segundo andar: **regra instalada em
  `settings.json` não é permissão efetiva** — o classificador do harness é uma camada a mais, e a
  única evidência de permissão é a **edição que passa**. Rota: ato do dono, nomeado no relatório
  de encerramento desta janela. **Vigésimo primeiro caso da série.**
- **`AE-43` — o loop dobrou duas linhas da série, e uma delas entrou na medida publicada do
  marco.** Achado do próprio loop em 2026-09-19, ao somar a janela para o relatório. O hook
  `SubagentStop` grava sozinho a linha do **executor**, mas **não** grava a do `pantonic-reviewer`
  nem a do `pantonic-consultant` — medido nesta janela: a linha `LM-T2f-revisao` e as duas de
  consultor (`ESC-23`, `ESC-24`) faltavam e foram apensadas à mão, corretamente; já as da `LM-T8`
  redespachada e da `LM-T6` **o hook havia gravado**, e o loop apensou por cima, criando
  `LM-T8-redespacho` (4 / 66,4k / 57,7 s) e uma segunda `LM-T6` (47 / 122,6k / 533,4 s). A regra
  existe e é do `scrum-master` (*'o número da linha é o do bloco `<usage>` da notificação,
  **conferido**'*) — o que faltou foi **conferir antes de apensar**, não a regra. As duas linhas
  foram removidas no mesmo ato e a série está correta.
  **A medida publicada do marco NÃO foi afetada, e isso foi medido, não suposto.** O loop suspeitou
  que a §10 da `LM-T6` tivesse somado a duplicata — ela existia em disco quando o marco mediu — e
  redespachou o executor do marco para re-derivar. Resultado: o total **não muda** —
  **3.712,8k tk / 1.098 tool uses / 11.147,7 s** em 21 módulos, idêntico ao publicado —, porque a
  linha duplicada pertencia à **`LM-T8`**, que está `blocked` por `permissao` e que a §10 **já
  declarava fora da série**. A decomposição por papel e os três percentuais de confronto com a
  baseline da `BKL-T4` (-37,9% / -26,3% / -57,9%) seguem válidos, com as âncoras conferindo exatas.
  A única frase corrigida no card foi a da janela 4, cuja composição mudou sem mudar o total.
  **Lição, e é do loop:** a suspeita estava certa em existir e errada em concluir — o loop chegou a
  publicar aqui um delta esperado (`3.646,4k`) **derivado por subtração**, que a medida derrubou;
  é o mesmo defeito (`DM-23`) que a `LM-T2f` apontou nesta janela, cometido pelo próprio
  orquestrador. **Vigésimo segundo caso da série**, e o primeiro em que o defeito é do **loop** e
  não de card nem de instrumento.
- **`AE-44` — a `LM-T8` foi implementada pela orquestração, por instrução direta do dono, depois de
  três recusas do classificador ao executor.** 2026-09-19. Sequência medida: (1) despacho limpo →
  `blocked premissa` por defeito de card (`AE-41`); (2) despacho depois do reparo → recusa do
  `Edit` em `.claude/agents/pantonic-planner.md` (`AE-42`); (3) o dono reliberou a permissão e
  autorizou expressamente a via alternativa; o loop tentou **repassar essa autorização dentro do
  prompt de um subagente** e o **próprio despacho** foi recusado — corretamente, e a lição é do
  loop: autorização do dono vale na sessão em que ele a deu, e não se delega adiante; (4)
  redespacho **sem** essa instrução → recusado de novo, já com a reliberação feita; (5) o loop
  aplicou os dez literais por Python **na própria sessão**. As doze linhas de `Verificação` saíram
  nos valores declarados, e o diff ficou em 70 inserções / 11 remoções, sem alterar line ending.
  **A exceção é nomeada e não vira precedente** (`DM-28`): a `GOVERNANCA.md` §3 diz que a
  orquestração **não implementa**, e continua dizendo. O que a levantou foi ato do dono, não
  julgamento do loop. **A independência da revisão foi preservada** — quem julgou a entrega foi o
  `pantonic-reviewer`, em contexto próprio, e não quem a escreveu. Rota: enquanto a recusa se
  repetir sobre `.claude/agents/**`, **toda** tarefa que edite definição de agente cai nesta mesma
  exceção; se isso persistir, é matéria de plano — não de improviso por tarefa.
  **Vigésimo terceiro caso da série.**
- **`AE-45` — a pendência substantiva do laudo da `LM-T8`, roteada pelo `B1`.**
  **ROTEADO pelo `ESC-25`** → `DM-49` e item **`PM-1`** da fila pós-marco (§6), que fecha (i) e
  (ii) no mesmo item porque as duas tocam o mesmo arquivo e a mesma camada de permissão. A matéria
  (i) foi depois **decidida pelo `scrum-master` por delegação do dono** — `DM-50`, cards `LM-T10`
  e `LM-T11` —, e a reserva ao dono que a `DM-49` (i) declarava está **encerrada**. `DM-49` (iv)
  corrige um fato da matéria (ii): a dependência **não** é esperar a `LM-T7`, que já fechou, e sim
  regenerar a projeção no mesmo ato do card que tocar a `description` (`DM-16` (iv)). O laudo saiu
  `aprovado 100%`, bloqueante `nenhuma`, e **recomendação `escalar`** — desfecho da `A8a`: o RDO
  fecha pelo veredito e a pendência **não** morre com o laudo. Três matérias, todas de
  **planejamento pós-marco**, nenhuma de execução:
  **(i)** *superfície de permissão sem rota fechada* — tarefa que edite `.claude/agents/**` não tem
  caminho definido quando o executor é recusado; a exceção do `AE-44` é nominalmente
  não-precedente e a rota dela é condicional (*"se isso persistir"*), mas o laudo observou que **já
  persistiu por três despachos dentro da própria tarefa** (`AE-11`, `DM-27`, `AE-42`). Enquanto não
  houver rota, toda tarefa futura de definição de agente reincide.
  **(ii)** *a `description` do `pantonic-planner` segue falsa* — `.claude/agents/pantonic-planner.md:3`
  ainda diz *"não mede nada por conta própria"*, o que a concessão de `Bash` torna falso. A `LM-T8`
  **não podia** fechá-la: o `Não fazer` do próprio card congela `description` e `model`, e com
  razão — mover a `description` reabre `check-drift`. É divergência interna do módulo que
  sobreviveu à entrega **por desenho do card**, e fecha junto com a reprojeção de
  `.claude/README.md` (`LM-T7`).
  **(iii)** consequência das duas: o `P-0740` precisa de um item de replanejamento na fila
  pós-marco que feche (i) e (ii) na mesma linha.
  Nada disto bloqueia tarefa aberta do plano, e nada disto é improviso de janela.
- **`AE-46` — o documento que fundamentou o veredito do marco não tinha residência decidida.**
  **CONCORDÂNCIA do consultor no `ESC-26`, com uma ressalva de fato, medida e não bloqueante:** a
  decisão de versionar está certa e a razão dela também — documento citado por marco aprovado e
  por RDO não fica fora da árvore, e o cabeçalho do próprio documento impede que ele vire segunda
  residência. A ressalva é de conteúdo, não de residência: ele afirma *"18 guardas nomeadas"* e
  são **19** — `check-readme.ps1` sai exit 0 anunciando `9 agente(s), 10 skill(s), 19
  guardrail(s)` —, e o erro subestima justamente um resultado desta iniciativa (a `LM-T4` levou
  18 → 19 com a `G-MODULO`). É a classe do `AE-12`: prosa que conta um conjunto sem fechar com o
  artefato que o conta. Outros três números dele estão **certos hoje e envelhecem** (linhas de
  `docs/telemetria.tsv`, registros de `docs/RDO/`, consumo do consultor), pela razão da `DM-23`.
  Corrigir antes de commitar é ato do loop, não matéria de card.
  Pendência do laudo da `LM-T6` (`aprovado 100%`, recomendação `escalar`), roteada pelo `B1`.
  Medido: `docs/MODO_DE_OPERACAO.md` estava **untracked** no momento do veredito. Ele foi autorado
  nesta janela a pedido do dono — um piloto em tempo real não era possível, e ele pediu a
  **descrição comparada** do modo de operação para avaliar —, foi a base sobre a qual o dono
  escreveu **APROVADO**, e é citado pelo RDO da `LM-T6`. O commit do marco força a decisão, porque
  arquivo untracked não entra nele por omissão. **Decisão do loop, e ela é de residência, não de
  conteúdo: versiona.** Documento citado por um marco aprovado e por RDO não fica fora da árvore.
  Não cria segunda residência de doutrina porque o próprio cabeçalho dele declara que **não é
  doutrina** e remete ao planejamento a pergunta de onde cada fato deve morar — o que o mantém como
  **material de veredito datado**, e não como superfície normativa. **Vigésimo quinto caso da
  série**, e o primeiro em que o achado é sobre o **artefato do aceite**, não sobre a entrega.

- **`AE-47` (2026-09-19, medido no `ESC-27`) — `backlog.py start` estava quebrado para toda tarefa
  de todo plano, por cinco defeitos encadeados; reparado pelo consultor.** O Passo 3 do
  `scrum-master` exige materializar `ready`→`in-progress` por ato de instrumento;
  `python .claude/tools/backlog.py start LM-T10` saía **exit 3** (`linha de índice ausente para
  P-0740`), sem escrever byte. Medidos, em cadeia: (1) `_posicao_indice` casava a linha de índice
  por **igualdade exata**, mas o índice publica o id do plano com sufixo mnemônico (`P-0740-LM`) e
  `PLANO_HEADER_RE` só declara `P-0740` — nenhum plano casava, e o guarda disparava em
  `backlog.py:709`, `:726` (`next`) e `:1026` (`status`/`start`); (2) `transacionar_status` repetia
  o casamento exato num `next(...)` **sem guarda** (`StopIteration`); (3)
  `.index("<!-- fila:gerada -->")` estourava `ValueError` porque os marcadores **não existem** no
  diário e só chegam com a `BKL-T6` (`AE-10` batendo em produção, com o `P-0739` parado por `DM-9`);
  (4) `LM-T5` e `LM-T6` carregavam o bullet de `Status` **depois** de um blockquote de
  reconciliação, e `_extrair_status` só lê o 1º bullet não-branco após o heading — os dois cards
  eram invisíveis ao instrumento e `start` teria publicado `21/29` sobre os `23/29` corretos;
  (5) `_escrever_atomico` gravava em modo texto do Windows, virando para **CRLF** todo arquivo
  tocado, contra `.gitattributes` (`* text=auto eol=lf`, cujo motivo declarado é manter o
  drift-guard `DP-5` utilizável). **Reparo** (escrita de código do consultor, classe "ajuste de
  instrumento do loop", nenhum card a cobria): residência única do casamento em
  `_posicao_indice`/`_linha_indice` (`backlog.py:629-657`), com sufixo fechado `[A-Za-z0-9]+`;
  guarda do bloco gerado que projeta card + linha de índice e **declara** a omissão em
  `ResultadoStatus.mensagem`, impressa pelo CLI (`:1105`, `:1231`) — pular em silêncio é a classe
  que o `TK-55` acumula; `newline="\n"` na escrita atômica (`:1013`); os dois bullets de `Status`
  movidos para a 1ª posição, texto verbatim. **4 TF novos** (`tests/test_backlog.py:968`, `:993`,
  `:1008`, `:1028`) sobre cópia da fixture `verde` — o defeito sobrevivera à suíte porque o próprio
  helper `_inserir_bloco_gerado` inseria os marcadores na cópia, isto é, os testes confirmavam um
  mundo que a fonte não tem. **Medido:** suíte `187 → 191 passed`; `start LM-T10` exit 0 tocando os
  dois arquivos; `card_check` da `LM-T10` e da `LM-T11` de volta a exit 0 depois de o `Medido antes`
  das duas ser re-medido de `187` para `191` (as duas estavam vermelhas por esse número). **Não
  reparado, com dono declarado:** `_bloco_fila_corrente` segue casando por id exato — quando a
  `BKL-T6` inserir os marcadores, ele precisa da mesma residência **e** de uma definição de "pai
  vivo": medido que a regra ingênua emitiria 12 bullets, **10 deles lixo** (7 planos legados com
  todos os cards `status=None`; `P-0735`/`P-0737`/`P-0738` com `Status` de arquivo defasado do
  índice) — insumo do produto (b) da `LM-T5a`. `backlog.py next` segue exit 3 por motivo
  **independente e pré-existente** (`_mensagem_e2` avalia todos os candidatos do repo e os planos
  legados não têm bullet de `Status`): escopo da guarda `DB-37`/`DB-40` é decisão de desenho, não
  bloqueia esta janela porque a ordem da fila é do `scrum-master`. **Para o `TK-55`, como evidência
  acumulada:** o defeito (1) publicou-se e ninguém notou por um dia; o parser de índice ingere
  célula de tabela ilustrativa como id (`AE-1`); e `docs/DIARIO_DE_OBRAS.md:138` (linha do `TK-54`)
  tem coluna extra e não fecha com `|`, o que apaga o tíquete inteiro do modelo do instrumento
  **sem sinal nenhum**.

- **`AE-48` (2026-09-19, laudo da `LM-T10`, `aprovado 100%`, bloqueante `nenhuma`, recomendação
  `seguir`) — três achados alvo `dossiê`, todos com a mesma rota: item de replanejamento do
  `P-0740`.** Registrados aqui porque o laudo morre no consumo (`DP-K` §14.4) e o `close` só
  transporta os cinco campos do pacote. (i) **O "Pronto quando" exigia aplicação POR INSTRUMENTO,
  mas aplicar por instrumento e aplicar por `Edit` deixam o repositório byte a byte idêntico:**
  nenhuma das três entradas de julgamento prova qual ocorreu — a prova saiu do registro de chamadas
  de ferramenta e da ordem de `mtime` (instrumento criado 18:24:52Z, invocado 18:25:25Z, `mtime` do
  alvo 18:25:26Z, nenhuma chamada de `Edit`/`Write` sobre o arquivo de agente na janela). Rota: card
  que exige aplicação por instrumento publica também **no caminho de sucesso** o comando literal e o
  exit code no registro da tarefa, por simetria com a Contingência 1, que já exige isso no caminho
  de recusa. (ii) **O contrato fechado de 7 itens deixa dois modos de falha do verbo sem forma
  definida**, medidos na revisão: (a) `--arquivo .claude/agents/naoexiste.md` sai com traceback
  `FileNotFoundError`, fora da forma `agentdef: …` de todas as outras recusas; (b) pares com
  literais **sobrepostos** ou repetidos (`--de abc --para xyz --de bc --para QQ`) saem exit 0
  anunciando `pares=2` com um par não aplicado, enquanto o item 6 manda imprimir o número de pares
  **aplicados**. Fechar qualquer um dos dois exigiria decisão do executor (`G-NOASK`): a decisão é
  do planejamento. (iii) **Sete itens de contrato e seis testes nomeados — o item 2 (pares
  completos) ficou sem teste nomeado.** Exercitado à mão na revisão (`--de` duplo com um `--para`
  único): exit 1 e a mensagem `agentdef: --de e --para vem em pares` — a validação existe e responde
  certo; o furo é de **cobertura declarada**, não funcional. Rota: somar o teste do item 2 à lista
  de nomes fixados.

- **`AE-49` (2026-09-19, medido no `ESC-28`) — a norma pedia relação e o gate exigia constante:
  baseline de corpus como aceite envelheceu três vezes numa janela.** A mesma linha de aceite da
  `LM-T11` (`python -m pytest tests/ -q`) reprovou no `card_check` três vezes em 2026-09-19, sempre
  pelo mesmo motivo e nunca por defeito de entrega: `187 passed` na autoria → `191` depois do
  reparo do `AE-47` → `197` depois da `LM-T10`. Duas dessas vezes custaram escalonamento ao
  consultor (`ESC-27`, `ESC-28`). Varrido o resto da fila, **quatro** dos cinco cards abertos
  estavam vermelhos pela mesma classe: `LM-T4c` item 2 (`41 passed` num módulo que o `AE-47` moveu
  para `45`) e item 3 (`26 26` de contagem de cards, hoje `29 29`); `LM-T9` com o insumo `I-<n>`
  medido em `8` e hoje em `10`, além de bloco `Verificação` em forma pré-normativa e dois campos
  onde a gramática admite um (`Arquivos-alvo` **e** `Entregável`, o que fazia `rdo.extrair_dossie`
  recusar o card antes de olhar a `Verificação`); `LM-T5a` com o item 1 **reprovado por obedecer à
  doutrina** — escrevia `**Medido no ESC-6: 18**`, exatamente o que o critério (xiii) manda
  (*relação, literal só como referência datada*), e o gate devolveu `elemento ausente - Medido
  antes`. **Causa medida, e não é autoria de card:** `docs/RUBRICA_DE_REVISAO.md` `### 8.1` obriga o
  literal `**Medido antes: <valor>**` em todo item, enquanto `card_check._bate_com_medido`
  (`.claude/tools/card_check.py:181-189`) compara esse valor como **substring literal** da saída,
  com uma única exceção — `exit N`, conferido contra o returncode. A norma (critérios (x) e (xiii))
  dizia *relação, nunca constante*; o instrumento, que é o gate, **re-congelava** a constante.
  Enquanto a lacuna existiu, todo card cuja linha de aceite tocasse corpus nascia perecível: cada
  entrega alheia o invalidava, e o custo de manutenção caía em escalonamento. **Decisão (consultor,
  técnica/tática, nada ao dono):** rota **(a)** — a baseline é **relação**, e o que faltava não era
  decidir e sim tornar a relação expressável na gramática que o instrumento lê. Critério
  **`(xviii)`** da rubrica: *o valor publicado no literal `Medido antes` é invariante ao que outras
  entregas movem* — mede o que **este** card possui (exit code, veredito binário, recorte do
  arquivo-alvo), nunca total de corpus (suíte, módulo compartilhado, contagem de cards ou de
  insumos do plano); pergunta sobre corpus vira **veredito** publicado pelo comando (`exit 0`,
  `iguais`, `1`), e o número absoluto desce para a prosa como referência **datada**, fora do
  literal. **Nenhuma linha de código foi necessária:** os dois modos de comparação que o
  `card_check` já tem bastam. **Aplicado:** `LM-T11` item 8 e `LM-T4c` item 2 passam a `Medido
  antes: exit 0`; `LM-T4c` item 3 troca `print(len(L),sum(...))` por `print('iguais' if ... else
  'divergem')` com `Medido antes: iguais`; `LM-T5a` item 1 publica `Medido antes: 18` (invariante
  porque o arquivo medido é o `P-0739`, estacionado, que nenhum card aberto toca) e o item 2, que
  era marcador numerado sem bloco cercado, vira prosa sem número; `LM-T9` troca `Entregável` por
  `Produto do módulo`, reescreve a `Verificação` em três itens normativos com `Medido antes: 0` e
  rebaixa a contagem de insumos a *insumo do despacho*. **Onde a doutrina entra:** não na `RUBRICA`
  por ato do consultor — ela é arquivo-alvo da `LM-T5d`, cuja restrição manda fechar a contagem da
  seção no mesmo ato, e editá-la agora quebraria o card. A `LM-T5d` foi **amendada**: `Produto (d)`
  com o texto do `(xviii)`, contagem de **dezessete** para **dezoito**, quinta linha de
  `Verificação` (`AE-49` na rubrica, `Medido antes: 0`) e `Pronto quando` fechado junto. **Medido
  depois:** `card_check` exit 0 nos cinco cards abertos (`LM-T11`, `LM-T4c`, `LM-T5d`, `LM-T5a`,
  `LM-T9`) e suíte em `197 passed`. **Fato colateral, sem ação:** `.claude/README.md` e
  `docs/telemetria.tsv` estão CRLF na árvore contra `.gitattributes` (`* text=auto eol=lf`) — mesma
  classe do item 5 do `AE-47`, mas **não** é o `agentdef.py`, que grava com `newline=""` e preservou
  LF em `.claude/agents/pantonic-planner.md`; evidência para o `TK-55`.

- **`AE-50` (2026-09-19, laudo da `LM-T11`, `ressalva 88%`, bloqueante `nenhuma`, recomendação
  `escalar`) — a lista e a tabela fecharam; as frases em prosa que as contam, não, e nenhum
  instrumento as lê.** Roteado pelo `B1`; atribuição **medida**
  (`review_evidence.py --atribuir`): `README.md` e `.claude/skills/scrum-master/SKILL.md` saem
  `alvo-do-card`, logo a pendência **não** é do `B0` e não se descarta como matéria de arquivo
  alheio. (i) **Duas** frases de contagem do `README.md` ficaram falsas, não uma: `:753`
  (*"…doze dependem de gate de review ou de instrução de agente"*, onde a recontagem da tabela dá
  **13**) e `:726` (*"Dezenove regras mínimas obrigatórias"*, onde são **vinte**) — esta segunda o
  executor não reportou, o reviewer a mediu. O `check-readme.ps1` sai **exit 0** com as duas falsas
  porque confronta linhas de tabela contra a lista de `GOVERNANCA.md` §7 e **não lê prosa**: o
  invariante do `DM-18` (i) está guardado na metade que o instrumento enxerga e desguardado na que
  ele não enxerga. (ii) A regra **`A3c`** entrou na tabela de roteamento sem as **três** enumerações
  da própria skill que nomeiam o conjunto: `.claude/skills/scrum-master/SKILL.md:134`
  (`regras A1..A3b`, intervalo que não a alcança), `:252` (`A1..A9, inclusive A6a e A8a`, que é a
  convenção do arquivo para sub-regra com letra) e a seção *O que obriga parada e o que segue com
  registro* (`:230-236`), onde a `A3c` é a **única** regra do bloco A com desfecho **condicional** e
  não aparece em nenhum dos dois bullets — o bullet de parada ainda diz que a escalada chega
  **"sempre"** pelo `pendencia=` ou pela recomendação `escalar`, o que a `A3c` passa a contrariar.
  **Classe, não novidade:** `AE-12` / rubrica §8 critério (viii) para (i), critério (xv) para (ii).
  O card invocou o princípio do `DM-18` (i) no Produto (a) mas **não deu literal** para nenhuma das
  frases, atribuiu o enforcement ao instrumento errado, e nenhuma das oito linhas de `Verificação`
  discrimina qualquer um dos dois pontos — por isso é achado de **dossiê**, não defeito de entrega,
  e por isso `rota` ficou `conforme`: o executor devolveu em vez de redigir, que é o que o
  `G-NOASK` manda. O `parcial` em `criterio-de-pronto` é o §6 invariante 3 aplicado à cláusula
  inverificável. **Fato colateral, fora dos alvos e sem rebaixar a entrega:** a varredura do domínio
  antigo de dois termos dá **zero** nas quatro superfícies normativas; restam
  `docs/DIARIO_HISTORICO.md` (registro histórico, legítimo) e `docs/MODO_DE_OPERACAO.md:54`
  (material datado de avaliação da `LM-T6`, não normativo).

- **`AE-51` (2026-09-19, pendência do laudo da `LM-T11` roteada pelo `B1` ao consultor no `ESC-29`)
  — o guarda cobre a tabela e a prosa que a conta envelhece sozinha; terceira instância do critério
  (viii) na mesma janela.** A `LM-T11` publicou o vigésimo guardrail (`G-TOOLDENY`) na tabela da
  seção *Os guardrails* do `README.md` e deixou **duas** frases de prosa da mesma seção falsas:
  `README.md:726` (*"Dezenove regras mínimas obrigatórias"* — são **vinte**) e `README.md:753`
  (*"**Sete** … **doze** dependem de gate de review ou de instrução de agente … e uma é negada pelo
  sistema de permissões"* — a recontagem do `ESC-29` sobre a coluna *Como é enforceada* dá
  **7 / 13 / 1** com **1** linha nas duas primeiras classes, e `7 + 13 - 1 + 1 = 20`). O
  `check-readme.ps1` saiu **exit 0** com as duas falsas, e continua saindo: ele confronta as
  **linhas de tabela** do README com a lista de `GOVERNANCA.md` §7 e **não lê prosa** na seção de
  guardrails — embora já leia prosa na seção *Anatomia do kit*, onde converte numeral por extenso
  pelo `$numeralMap`. O invariante do `DM-18` (i) estava guardado na metade que o instrumento
  enxerga e desguardado na que ele não enxerga. **Segundo achado, na mesma pendência:** a `A3c`
  entrou na tabela do bloco A de `.claude/skills/scrum-master/SKILL.md` sem entrar em **nenhuma**
  das três enumerações da própria skill — `:134` (`regras A1..A3b`), `:252` (`A1..A9, inclusive A6a
  e A8a`) e a seção *O que obriga parada e o que segue com registro*, onde a `A3c` é a **única**
  regra do bloco A com desfecho **condicional** (redespacha havendo fallback declarado; **PARA** não
  havendo) e não aparece em nenhum dos dois bullets; o bullet de parada ainda afirma que a escalada
  chega **"sempre"** pelo `pendencia=` ou pela recomendação `escalar`, o que a `A3c` contradiz,
  porque ela não despacha o `reviewer` e portanto não há laudo de onde a recomendação viesse.
  Atribuição **medida** (`review_evidence.py --atribuir`): os dois arquivos saem `alvo-do-card`,
  logo não é matéria alheia e o `B0` não a descarta. **Decisão (consultor, técnica/tática, nada ao
  dono):** **card novo `LM-T12`** no `P-0740` — *A enumeração em prosa que nenhum instrumento lê* —,
  **primeiro da fila restante**, antes de `LM-T4c`, `LM-T5d`, `LM-T5a` e `LM-T9` (`DM-29`
  preservado). A posição não é de grafo (não depende de nada, nada depende dela) e sim de risco: o
  item (c) conserta as enumerações pelas quais o loop roteia **enquanto roda**. O card entrega
  (a) as duas frases com literal prescrito; (b) o `check-readme.ps1` lendo-as, **reusando o
  `$numeralMap` que ele já tem**, com a identidade `teste + gate - ambos + permissão = total` como
  aceite (e não os três literais, que a Contingência 1 cobre); (c) a `A3c` nas três enumerações,
  entrando nos **dois** bullets da seção de parada por ser condicional, com a queda do advérbio
  *sempre*; (d) a linha do `CHANGELOG.md`. Dez linhas de `Verificação`, todas rodadas antes da
  publicação, seis delas discriminando o mundo com a mudança do mundo sem ela (`0→1`, `1→0` em
  literal), e `card_check` **exit 0 na primeira rodada**. Plano passa a **30** tarefas, `25/30`.
  **Questão de fundo:** é **classe**, não acidente, e é a **terceira** instância na mesma janela —
  `AE-12` (que autorou o critério (viii)), `AE-49` (o instrumento enxergando **demais**: congelava
  como constante o que a norma mandava publicar como relação) e este (`AE-51`, o instrumento
  enxergando **de menos**: guarda a tabela, não lê a frase que a conta). Raiz comum: **o invariante
  mora em dois lugares e o guarda cobre um**. Ela **não se fecha escrevendo mais doutrina** — o
  critério (viii) já manda estender o instrumento no mesmo ato e foi violado com tudo verde —, fecha
  **no guarda**, e é o que a `LM-T12` faz para a seção *Os guardrails*. Nenhum critério novo foi
  acrescentado à rubrica por este achado, deliberadamente. A **generalização** — toda frase de
  contagem publicada em superfície guardada entra no guarda que a julga, varrida em `README.md`,
  `GOVERNANCA.md`, `RUBRICA_DE_REVISAO.md` e nas skills — vai como evidência ao **`TK-55`**
  (*derivado que erra sem sinal porque nada o confronta com a fonte*), gated pelo encerramento do
  `P-0740`. **Caso imediato da mesma classe, fechado pelo loop no ato do registro:**
  `docs/DIARIO_DE_OBRAS.md:126` publicava *"29 tarefas, 23 fechadas"* em prosa que nenhum
  instrumento lê — o `done/total` que o `backlog.py` projeta vive no campo `Status` da linha, não no
  Título —, corrigido para *"30 tarefas, 25 fechadas"* nesta mesma passagem.

- **`AE-52` (2026-09-19, laudo da `LM-T12`, `aprovado 100%`, bloqueante `nenhuma`, recomendação
  `seguir`) — o card que fecha a classe reproduziu a classe dentro do próprio arquivo-alvo.** A
  `LM-T12` acrescentou a checagem **4b** ao `.claude/checks/check-readme.ps1` e **não** mandou
  fechar, no mesmo ato, a enumeração em prosa do `.SYNOPSIS` do próprio script — *"qualquer uma das
  **5** checagens mecânicas abaixo"*, itens 1..5 —, que agora não descreve a conferência das duas
  frases. É exatamente o critério (viii) que este card existia para fechar, uma camada acima. **Não
  rebaixa a entrega:** o executor seguiu o card, e estender o cabeçalho sem prescrição seria desvio
  de rota (`G-PLANFIDELITY`). Rota: o consultor emenda o card seguinte que tocar o script. **Limite
  conhecido do guarda novo, medido e sem falso verde:** o `$numeralMap` do script vai só até
  `vinte`; na 21ª regra a frase por extenso (*"Vinte e um"*) será lida como o token `Vinte` e o
  guarda falhará com `20 vs 21` — **fail-closed**, mas o remédio será escrever o numeral em dígito
  ou estender o mapa. **O guarda foi provado por mutação, fora do repo** (`-Root` sobre cópia em
  `TEMP`): cinco mutações independentes foram **vistas falhar** — `20→19`, numeral fora do
  vocabulário (`Cinquenta`), `Sete→Oito`, `treze→doze` e a frase das formas ausente —, e a
  identidade `teste + gate - ambos + permissão` foi vista falhar isolada ao crescer a tabela para 21
  linhas. Recontagem independente do reviewer pela coluna *Como é enforceada*: `Teste executável` =
  **7** (1-6, 8); gate/instrução/planejamento = **13** (7-12, 14-20); permissão = **1** (13); ambos
  = **1** (8); `7 + 13 - 1 + 1 = 20` = linhas da tabela — os 7/13/1 do executor conferem sem
  divergência, logo a Contingência 1 não foi acionada.

- **`AE-53` (2026-09-19, pendência do laudo da `LM-T4c` roteada pelo `B1`) — o contrato de razão do
  `backlog.py` ficou assimétrico: o leitor tem fronteira estrita e o escritor aceita texto livre.**
  Veredito `aprovado 100%`, bloqueante `nenhuma`, recomendação `escalar`. Atribuição **medida**
  (`review_evidence.py --atribuir`): `.claude/tools/backlog.py` e `tests/test_backlog.py` saem
  `alvo-do-card`, logo não é matéria alheia e o `B0` não a descarta. **O fato:** a `LM-T4c` decidiu
  e implementou a fronteira do **leitor** — a razão não contém ` — `, a cauda começa no primeiro
  ` — ` — e a Restrição do card congelou o **escritor** ("nada mais muda"). Mas o card **não
  decidiu** o que fazer com um `--razao` que contenha travessão, e o escritor aceita texto livre.
  Medido pelo reviewer ponta a ponta sobre cópia da fixture `verde` em `tmp`:
  `status ALF-T1 blocked --razao 'premissa — suja'` grava `· premissa — suja — cauda viva`. Duas
  bordas medidas em que a razão **não é round-trippável**. **A decisão que falta, e é de
  planejamento:** o escritor **valida** (recusa `--razao` com travessão), **normaliza** (substitui
  ou escapa), ou a degradação é **aceitável** e se documenta como tal. **Por que não rebaixou a
  entrega:** o par de testes nomeados pelo card é suficiente para o que o card prometeu e cego para
  o contrato que ele deixou aberto — o TF fixa a linha canônica e o TR o round-trip com razão
  limpa, e nenhum dos dois toca razão com travessão, que é exatamente onde a fronteira nova cria
  comportamento novo. Foi o exercício ponta a ponta pela CLI que expôs as bordas, não a leitura do
  diff. **Padrão de aceite que o laudo propõe para card que mexe em regex de corpus:** confronto
  old-vs-new sobre o corpus inteiro — aqui, 46 bullets de `Status` em `docs/plans/*.md` +
  `docs/DIARIO_DE_OBRAS.md`, com **0** bullets perdendo match, **5** mudando de grupos, e as 5 sendo
  exatamente o defeito que a tarefa foi corrigir. É mais barato e mais forte que a `Verificação` 3
  do card, que mede um plano só.

- **`AE-54` (2026-09-19, `ESC-30`) — o contrato de razão era assimétrico entre leitor e escritor, e
  o card que fechou a classe da prosa reproduziu a classe no próprio arquivo.** Duas pendências num
  escalonamento só, as duas roteadas ao consultor pelo `B1`. **(1) A assimetria (pendência do laudo
  da `LM-T4c`).** A `LM-T4c` deu ao **leitor** a fronteira estrita (`STATUS_BULLET_RE` captura a
  razão como `([^—]+?)`) e a Restrição do card congelou o **escritor**, que segue interpolando
  `--razao` verbatim — a assimetria é consequência da Restrição, não desvio do executor. Reproduzido
  no `ESC-30`, ponta a ponta sobre cópia da fixture `verde`:
  `transacionar_status(..., 'blocked', razao='premissa — suja')` sai **exit 0** e grava
  `· premissa — suja — cauda viva`; a releitura do mesmo arquivo devolve `razao='premissa'` e
  `cauda='suja — cauda viva'` — o texto do operador **muda de campo em silêncio**. Medido também o
  que **não** é defeito: `·` na razão round-trippa sem perda, então a borda é só do travessão (`—`,
  U+2014). **Rota decidida: VALIDAR** — o escritor recusa, exit 1, mensagem nomeando o caractere e a
  fronteira do leitor, antes de qualquer escrita. *Normalizar* mutaria em silêncio o texto do
  operador, que é a classe que o `TK-55` acumula; *tolerar* deixaria uma borda lossy medida no
  instrumento que o próprio loop usa para materializar `A3a`, `A3b` e `A3c`; *validar* é
  fail-closed, custa uma linha e não restringe nada real, porque `razão` é **motivo**
  (`dependencia`, `premissa`, `ferramenta`) e prosa livre é matéria da cauda e da nota, que seguem
  aceitando travessão. Card **`LM-T13`** (`low`, 7 linhas de `Verificação`, com um item `inalterado`
  trancando o leitor, que esta tarefa **não** toca). **(2) O `AE-52`.** O laudo da `LM-T12` achou
  que o card que fecha a classe da enumeração em prosa **reproduziu a classe**: a checagem `4b`
  entrou em `.claude/checks/check-readme.ps1` e a enumeração do próprio `.SYNOPSIS` — *"qualquer uma
  das 5 checagens mecânicas abaixo"*, itens `1..5` — não foi fechada no mesmo ato. O card não a
  prescrevera, então a entrega não foi rebaixada (`G-PLANFIDELITY`), e a rota declarada pelo laudo
  era emendar *"o card seguinte que tocar o script"* — mas **medido que não existe**: nenhum card
  aberto toca o arquivo (`LM-T5d` → `RUBRICA_DE_REVISAO.md`, `LM-T5a` → `P-0739`, `LM-T9` →
  `consultant-spec`). Sem veículo, o resíduo esperaria o fim do plano. **Rota: card próprio
  `LM-T14`**, e **não** anexo ao `LM-T13`: arquivos, temas e técnicas distintos, e juntá-los
  compraria o defeito que este plano corrige (`DM-2`/`DM-4`, `G-MODULO`). O mesmo card absorve o
  **limite medido do `$numeralMap`** (para em `vinte`; na vigésima primeira regra a frase por
  extenso é lida como `Vinte` e o guarda falha com `20 vs 21` — **fail-closed, sem falso verde**,
  mas com mensagem que acusa divergência onde há vocabulário curto): medido que estender o mapa
  **não basta**, porque a captura é de um token (`^(\S+) regras mínimas obrigatórias`), então o card
  prescreve as duas metades juntas — captura `^(.+?) …` e mapa de `vinte e um` a `trinta` com as
  formas femininas (`vinte e uma`, `vinte e duas`), já que a frase concorda com *regras* — mais
  **prova por mutação nos dois sentidos**, a mesma técnica com que o laudo da `LM-T12` provou a
  `4b`. **Classe:** o `AE-52` é a **quarta** instância do critério (viii) nesta janela (`AE-12`
  autorou, `AE-49` o instrumento enxergando demais, `AE-51` enxergando de menos) e a mais eloquente,
  porque o defeito apareceu **no ato de fechá-lo**: o guarda que lê a prosa da seção que guarda não
  tem quem leia a **sua** prosa. Isso não muda a conclusão do `ESC-29` — a classe fecha **no guarda,
  não na rubrica** —, apenas mostra o alcance que a generalização precisa ter, e reforça a rota já
  declarada ao **`TK-55`**: *todo guarda que conta é ele próprio superfície contada*. Nenhum
  critério novo foi acrescentado à rubrica, de novo deliberadamente. **Estado:** plano passa a **32**
  tarefas, `27/32`; `## 6` atualizado com a fila sugerida `LM-T13` → `LM-T14` → `LM-T5d` → `LM-T5a`
  → `LM-T9` (`DM-29` intacto) e com a declaração de que **não há restrição de grafo** entre as duas
  novas. `card_check` **exit 0** nos cinco cards abertos; suíte `197 passed`; `tests/test_backlog.py`
  em `47`.

- **`AE-55` (2026-09-19, pendência do laudo da `LM-T13` roteada pelo `B1`) — o recorte do dossiê de
  evidência não discrimina autoria **dentro** do arquivo, e é consequência direta da diretiva de
  commitar só no marco.** Veredito `aprovado 100%`, bloqueante `nenhuma`, recomendação `escalar`.
  **O fato:** `--desde f1afbd3` acumula **sete** entregas desta janela, e os três `Arquivos-alvo` da
  `LM-T13` carregam **três autorias sobrepostas** — a própria `LM-T13`, a fronteira do leitor da
  `LM-T4c` (fechada no mesmo dia) e o reparo `AE-47`/`ESC-27` do consultor —, com o `CHANGELOG.md`
  somando linhas de **três** tarefas (`LM-T11`, `LM-T12`, `LM-T13`). **Segunda ocorrência na mesma
  janela:** a lição 3 do RDO da `LM-T4c` já a registrara, sobre os mesmos dois arquivos. **A tensão
  de norma:** a `docs/RUBRICA_DE_REVISAO.md` §3 (`AE-13`) declara a injeção manual de contexto
  **dispensável**, e nesta janela ela foi **obrigatória em todas as seis revisões** — o loop a
  injetou a cada despacho de reviewer, e sem ela a atribuição por arquivo seria ambígua. **Rota
  declarada pelo laudo:** item de replanejamento do `P-0740` — ou **commit por tarefa**, ou
  **atribuição por hunk** no `review_evidence.py`. A primeira contraria a diretiva de execução do
  dono (item 3, 2026-09-18: *"Commit acontece no marco, não por tarefa"*), que também declarou a
  injeção manual **obrigatória até a `LM-T3` fechar a atribuição** — a `LM-T3` fechou, e o problema
  permanece porque ela resolveu atribuição **por arquivo**, não **por hunk**. Escalado ao consultor
  como `ESC-31`.

- **`AE-56` (2026-09-19, `ESC-31`) — o reviewer precisa de fronteira, não de commit: o dilema do
  laudo era falso, e a norma é que estava errada.** Pendência da `LM-T13` roteada pelo `B1`,
  primeira da janela a tocar uma **decisão registrada do dono**. O laudo ofereceu duas rotas —
  **commit por tarefa** (revoga o item 3 da diretiva de execução de 2026-09-18) ou **atribuição por
  hunk** no `review_evidence.py` (card novo). **As duas partem da mesma premissa não examinada:** a
  de que a fronteira de evidência de uma tarefa só existe como commit. Medido no `ESC-31`, neste
  repo: `GIT_INDEX_FILE=<temp> git add -A && git write-tree` devolveu a árvore
  `65826eed410466dc96dbdab18b4358c33a1d125a` com o **índice real intocado**
  (`git diff --cached --stat` vazio) e o working tree inalterado (26 entradas, as mesmas). Uma
  árvore por tarefa, sem `HEAD`, sem índice, sem histórico — a diretiva do dono proíbe **commit**,
  não **marco**. A terceira via é `review_evidence.py --desde <tree-ish>` com a árvore gravada pelo
  loop no fechamento de cada tarefa: uma flag no instrumento e uma linha de estado no loop, **sem**
  parser de hunk e **sem** tocar a diretiva. **Decisão (consultor, técnica/tática):** nenhuma das
  três se executa agora. Restam quatro tarefas e, passado o marco, o commit devolve a discriminação
  ao `--desde` sozinho; construir fronteira-sem-commit para servir quatro revisões é a economia que
  esta janela recusou em cada escalonamento. Vai como **matéria pós-marco**, candidata a tíquete
  próprio, **com o desenho já medido** para que quem a planeje não comece frio. O que se faz agora é
  **fechar a divergência entre norma e prática**, que é o defeito real: `docs/RUBRICA_DE_REVISAO.md`
  `## 3` afirma que o reviewer *"não depende de injeção manual de contexto do orquestrador
  (`AE-13`)"*, e isso foi **falso em seis de seis revisões desta janela**. A frase **não se apaga nem
  se inverte** — está certa sobre o que fala, a marcação `da entrega`/`alheio` **por arquivo**;
  ganha abaixo dela um parágrafo datado com (a) a atribuição por arquivo seguindo dispensável para a
  pergunta de escopo, (b) a injeção manual **obrigatória enquanto o commit for por marco**, como
  parte do despacho e não desvio de quem orquestra, e (c) a condição que a suspende sendo
  **capacidade** (atribuição por hunk), não card. Entregue como **produto (e) da `LM-T5d`**, que é o
  card *"a rubrica posta em dia"* e já é dono do arquivo — abrir card novo para consertar uma frase
  seria o inverso do que esta janela decidiu oito vezes; no mesmo ato a `LM-T5d` passa de `low` a
  **`medium`** (quatro produtos, não três), ganha a sexta linha de `Verificação`
  (`enquanto o commit for por marco`, `Medido antes: 0`) e troca *"nada mais do arquivo mudou"* por
  *"nada além dessas duas seções"*. `card_check` **exit 0**. **Classificação: NÃO estratégico**, e o
  critério fica explícito porque é a primeira vez que a pergunta aparece: *estratégico é o que muda
  escopo ou rota do plano, ou revoga/emenda decisão do dono* — decidir **sobre** uma diretiva não é
  emendá-la. A diretiva condicionou a obrigação a *"até a `LM-T3` fechar a atribuição"*: lida pelo
  **rótulo**, a `LM-T3` fechou e a obrigação teria caído; lida pela **substância**, o dono a
  condicionou a uma **capacidade** e nomeou a `LM-T3` como veículo esperado — a capacidade não
  fechou (fechou por arquivo; a ambiguidade é por hunk), a condição segue não satisfeita e a
  obrigação se mantém **por força da frase dele**. Governa a substância, pelo precedente do próprio
  kit: o `RP-2` já emendou `GOVERNANCA.md` §7 item 17 exatamente para deixar de contar rótulos e
  passar a olhar o objeto. Manter a injeção manual **executa** a diretiva; não a emenda. O que sobe
  ao dono é a **oferta** da fronteira-sem-commit com o custo medido, pelo relatório de encerramento e
  nunca por interrupção (`G-NOASK`) — ele decide no marco, com o plano fechado. **Fato a registrar
  sem decisão anexa:** a previsão do dono foi cumprida (a `LM-T3` fechou) e **não bastou**; é a
  segunda ocorrência da mesma classe na janela (a lição 3 do RDO da `LM-T4c` já a registrara sobre
  os mesmos dois arquivos), e as duas ficam como evidência do tíquete pós-marco.

- **`AE-57` (2026-09-19, pendência do laudo da `LM-T14` roteada pelo `B1`) — a classe do `AE-52`
  reincide pela terceira vez, agora entre irmãs do próprio bloco que a `LM-T14` veio fechar.**
  Veredito `ressalva 91%`, bloqueante `nenhuma`, recomendação `escalar`. **(i)** Três das **quatro**
  mensagens de vocabulário do `.claude/checks/check-readme.ps1` ainda anunciam *"por extenso até
  vinte"* contra um `$numeralMap` que agora vai a **trinta** — o Produto (b) do card pediu *"a
  mensagem de vocabulário passa a dizer até onde o mapa vai"* no **singular**, sem nomear qual das
  quatro, e a Restrição declarou que a checagem de *Anatomia do kit* compartilha o mapa e *"só passa
  a aceitar mais numerais"*, sem exigir que as mensagens dela deixassem de anunciar o teto antigo.
  **(ii)** O teto do numeral foi fechado **só** na frase de *regras mínimas obrigatórias*; as
  capturas irmãs do mesmo script seguem de **um token** — `(\S+) agentes` / `(\S+) skills` na
  *Anatomia do kit* e `\*\*(\S+)\*\*` na frase das três formas —, de modo que a classe reincide na
  primeira forma composta dessas frases. **Medido pelo reviewer em cópia fora do repo:** com
  `**vinte e uma**` na frase das formas — numeral que **está** no mapa —, o guarda **recusa** com
  *"numeral fora do vocabulário (dígito ou por extenso até vinte)"*. **Fail-closed preservado em
  todos os mundos testados: nenhum falso verde**, e o guarda segue `exit 0` sobre o repo real.
  **Por que nenhuma das nove linhas de `Verificação` pegou:** todas saíram nos valores declarados —
  a divergência **interna ao módulo** não aparece em nenhuma delas. **Lição de autoria que o laudo
  extrai, e é a mais transferível da janela:** linha de aceite por literal (`das 6 checagens`,
  `vinte e uma`) prova **presença**, nunca **coerência entre irmãos do mesmo bloco**; o aceite de
  coerência do módulo (`DM-3`) precisa de um comando que **rode o caminho completo**, não de mais um
  `Select-String`. Rota: card de regularização das quatro mensagens e das capturas irmãs. Escalado
  ao consultor como `ESC-32`.

- **`AE-58` (2026-09-19, `ESC-32`) — o que esgotou não foi o aceite por literal, foi o aceite por
  presença; e a prova está nos quatro pares da própria janela.** Terceira reincidência da classe em
  três cards consecutivos (`AE-51` → `AE-52` → `AE-57`), todos autorados pelo consultor sob
  escalonamento, todos com `card_check` verde. **Diagnóstico, medido e não inferido:** comparando os
  itens de `Verificação` escritos nos três cards, a correlação é de **quatro por quatro** — onde o
  item foi escrito em **par** (presença do literal novo **e ausência do velho, contada no arquivo
  inteiro**) o resíduo **não** reincidiu (`Dezenove… → 0` e `**doze**… → 0` na `LM-T12`;
  `das 5 checagens → 0` na `LM-T14`); onde foi escrito **só como presença**, o irmão ficou para trás
  (`regras mínimas obrigatórias ≥ 1` na `LM-T12` deixou o `.SYNOPSIS`, `AE-52`; `vinte e uma ≥ 1` na
  `LM-T14` deixou três mensagens e quatro capturas, `AE-57`). A razão é lógica, não estilística:
  presença é afirmação **existencial** e nunca alcança irmão nenhum; ausência é afirmação
  **universal** sobre o bloco, e é ela que cobre o que o autor não enumerou. **Regra adotada:** toda
  troca de literal vai em **par**; e quando a coerência é **comportamental** — o caminho completo
  aceita o que diz aceitar —, nenhuma contagem basta e vale a **prova por mutação**. Registre-se que
  o `AE-57` **não** foi achado por leitura nem pelo gate, e sim pela prova por mutação exigida na
  própria `LM-T14`: a técnica que fecha a classe já estava em uso quando a classe reincidiu —
  faltava aplicá-la a todos os irmãos. **Convergência:** a consequência decresce (contrato público →
  docstring interna → mensagens internas com recusa fail-closed latente, sem falso verde em nenhum
  mundo testado), mas o mecanismo **não** é auto-limitante: ele para quando a forma do aceite muda.
  **Classificação: NÃO estratégico** — pelo critério do `ESC-31`, isto muda a **forma da linha de
  aceite** (técnica de autoria), não o escopo, não a rota e nenhuma decisão do dono; se mudasse, a
  janela teria encerrado no `ESC-28`, quando o critério (xviii) mudou o que pode ir em `Medido
  antes`. **Ações, e o que deliberadamente não se fez:** (1) card **`LM-T15`** (`low`, primeiro da
  fila) fecha o resíduo concreto — as quatro capturas passam a numeral composto com âncora **provada
  antes de prescrever** (`nove`, `dez`, `Sete`, `treze`; sem âncora, `(.+?) agentes` captura *"O kit
  são nove"*) e as três mensagens que ainda anunciam `por extenso até vinte` passam a `até trinta`
  —, com o bloco `Verificação` **em pares** e a prova por mutação nos quatro sítios; a objeção de
  economia do `ESC-31` não se aplica, porque **terminar entrega não é investir em capacidade**, e a
  distinção é verificável: nada se acrescenta ao guarda e nenhum veredito sobre o repo de hoje muda;
  (2) a **`LM-T5a`** ganhou a linha de **caminho completo** que lhe faltava — `card_check` sobre os
  cards reescritos do `P-0739`, `Medido antes: exit 1` → `exit 0`, e o `Pronto quando` exige exit 0
  **para os seis** —, porque é o card em que coerência entre irmãos **é** o produto e o aceite era
  contagem de presença; (3) **nenhum critério novo na rubrica**, assimetria deliberada em relação ao
  `ESC-28`: lá havia contradição entre norma e instrumento, que só se resolve na norma; aqui a regra
  simplesmente não existia, e regra que depende do autor lembrar é o checklist que a `### 8.1` já
  declara insuficiente — a exigência **mecânica** (o `card_check` recusar bloco de aceite feito só
  de contagem de presença quando o card declara aceite de coerência, `DM-3`) vai para o **`AE-33`**,
  dono do reparo do instrumento, pós-marco. **Achado colateral reproduzível, para o `AE-33` item
  1:** escrever um decimal na **prosa** de um item de `Verificação` cria **item fantasma** — `8.1`
  fez o `card_check` reprovar a `LM-T5a` com *"item 8: fora da forma"*; reescrita a frase sem o
  decimal, verde. **Marco 3, declarado no mesmo ato porque o plano não o declarava:**
  `docs/plans/P-0740-loop-de-modulos.md:816` fixava a `LM-T6` como marco validável — esse era o
  marco 2, commitado em `f1afbd3`. O **marco 3 é o fechamento do plano na `LM-T9`** (`33/33`), com
  `docs/consultant-spec.md` como artefato de validação do dono (razão pela qual o `DM-29` a pôs por
  último); não há marco intermediário, porque as quatro tarefas restantes são regularização e
  reagrupamento. A janela **segue até a `LM-T9`**, com commit único lá, salvo parada por capacidade
  do contexto de quem conduz — decisão do `scrum-master`, não do plano.

- **`AE-59` (2026-09-19, pendência do laudo da `LM-T15` roteada pelo `B1`) — a classe do `AE-52`
  **não** reincidiu numa quinta superfície; o que sobrou é resíduo de **escopo de módulo**, que é
  outra coisa.** Veredito `aprovado 100%`, bloqueante `nenhuma`, recomendação `escalar`. **O que
  fechou:** a forma **em par** funcionou — a ausência contada no arquivo inteiro é universal e
  alcança os irmãos, e é ela, não a presença, que **prova** que nenhum quinto sítio sobrou (grep no
  repo inteiro: zero `extenso até vinte`, zero `(\S+)` no script). Os cinco sítios devolvem `nove`,
  `dez`, `Sete`, `treze` e `Vinte` sobre o `README.md` de hoje, e o guarda segue `exit 0` sobre o
  repo real. **O resíduo novo, de outra natureza:** `$numeralMap` é definido **dentro** do `else`
  aninhado do bloco *Anatomia do kit* (`check-readme.ps1:131`) e **consumido de fora** pelo bloco
  `4b` (`:264`, `:290`, `:295`). Medido pelo reviewer em fixture fora do repo: **com o título da
  seção ausente**, o guarda morre em `You cannot call a method on a null-valued expression`, stdout
  vazio, exit 1 **sem** o diagnóstico previsto (*"Seção Anatomia do kit não encontrada"*). Não é
  defeito da `LM-T15` — o card proibia mexer em estrutura —, e **nenhum** dos três cards da trinca
  (`LM-T12`, `LM-T14`, `LM-T15`) declarou esse acoplamento como alvo. Escalado como `ESC-33`.
  **Falso positivo registrado para que um card futuro não o "conserte":** a assimetria aparente de
  `.ToLower()` entre os dois sítios da *Anatomia* e os três do bloco `4b` **não** é uma quinta
  instância da classe — hashtable de PowerShell é case-insensitive por construção, e o reviewer
  mediu numeral composto em caixa alta passando nos cinco sítios. **Prova por mutação reproduzida
  pelo reviewer, fora do repo:** fixture de 21 agentes / 22 skills / 21 guardrails com numeral
  composto nos cinco sítios sai `exit 0`; **dez** quebras (cinco por divergência, cinco por numeral
  fora do vocabulário) saem `exit 1`, cada uma citando declarado vs medido ou o token recusado com
  `até trinta`. Repo real **inalterado**: md5 dos quatro arquivos e o `git status` idênticos antes e
  depois, cópia descartada. **Nota de consumo, informativa e não crítica:** 42 tool uses / 108,0k num
  card de esforço `low`, o maior das quatro irmãs do dia — o custo está na **fixture da prova por
  mutação**, não na edição, e isso é esperado para card cuja parte comportamental só se prova fora
  do repo.

- **`AE-60` (2026-09-19, `ESC-33`) — a superfície saturou: teto declarado, e a série
  classificada.** O `AE-59` (`$numeralMap` definido dentro do `else` do bloco *Anatomia do kit* em
  `.claude/checks/check-readme.ps1:131` e consumido de fora pelo bloco `4b` em `:264`, `:290`,
  `:295`; com o título da seção ausente o script morre em `You cannot call a method on a null-valued
  expression`, exit 1 sem o diagnóstico previsto) **não vira card no `P-0740`**. **Enquadramento,
  pelo teste que o `ESC-32` fixou:** o acoplamento é **anterior** à trinca
  `LM-T12`/`LM-T14`/`LM-T15` e nenhuma delas o abriu — é **capacidade, não término**, e recebe a
  mesma resposta que o `ESC-31` deu à atribuição por hunk. **Correção de enunciado que muda o
  peso:** o modo de falha é fail-open em **diagnóstico** e fail-**closed** em **veredito** — nos dez
  mundos mutados pelo reviewer o guarda saiu `exit 1`, sem falso verde em nenhum; e o único mundo em
  que a exceção aparece é o `README.md` sem título de seção, no qual as checagens 1, 2 e 5 também
  caem e o guarda já reprovaria. É **menos** consequente que o resíduo de prosa que motivou os três
  cards anteriores, porque aquele mentia com o guarda **verde**. **Reparo desenhado e verificado,
  para quem o planejar não começar frio:** o `$numeralMap` é literal de hashtable **sem
  dependência** de estado da seção (o primeiro uso de `$countLine` vem depois dele), então o
  conserto é **hoisting** para o escopo do script, acima do primeiro consumidor — mudança de
  posição, não de comportamento, que devolve ao bloco a mensagem `Seção 'Anatomia do kit' não
  encontrada` que ele já tem escrita. Registrado junto o **falso positivo** isolado pelo reviewer,
  para que nenhum card futuro o "conserte": a assimetria aparente de `.ToLower()` entre os dois
  sítios da *Anatomia* e os três do `4b` **não** é instância da classe — hashtable de PowerShell é
  case-insensitive por construção, medido com numeral composto em caixa alta passando nos cinco
  sítios. **Decisão de fundo — teto de saturação, declarado em `## 6` do plano:** nenhuma matéria
  nova sobre `.claude/checks/check-readme.ps1` abre card no `P-0740`; acumula no tíquete pós-marco.
  **Teste de saturação** (regra geral, aplicada aqui a esta superfície): uma superfície satura
  quando o achado seguinte **exige precondição mais rara que o anterior** e o **veredito do
  instrumento se manteve correto** em todos os mundos medidos. A série mede exatamente isso —
  `AE-51` falso no instante da publicação, num contrato que o adotante lê, e com **falso verde**;
  `AE-52` interno ao docstring; `AE-57` mordendo na vigésima primeira regra; `AE-59` mordendo só num
  `README.md` já quebrado. **Classificação da série, que é informação do dono e não alarme:** o
  plano **não** está descobrindo escopo mais rápido do que fecha — está gastando **profundidade de
  inspeção num artefato secundário**. Os três fatos que sustentam a leitura, para o relatório de
  encerramento: o plano cresceu de **29 para 33** cards numa janela, com **quatro** dos cinco cards
  novos autorados pelo consultor sob escalonamento; **quatro** dos sete escalonamentos
  (`ESC-27`..`ESC-33`) terminaram no **mesmo arquivo**, que não é o loop e sim um guarda do README
  que o plano tocou porque a `LM-T11` publicou um guardrail; e, no mesmo intervalo, **dez tarefas
  fecharam com zero reprovações e zero retentativas**. O mecanismo é conhecido e nomeado: cada
  revisão competente acha o próximo defeito do arquivo que acabou de ser tocado, e o consultor vinha
  convertendo **cada achado em card** — o defeito de processo é do consultor, não do loop nem do
  reviewer, e a correção é o teto acima, que fica escrito no plano e não depende de ninguém lembrar.
  **Não estratégico:** não muda escopo (as 33 entregas ficam), não muda rota (fila `LM-T5d` →
  `LM-T5a` → `LM-T9` e marco 3 na `LM-T9`), não toca decisão do dono.

- **`AE-61` (2026-09-19, laudo da `LM-T5d`, `ressalva 88%`, bloqueante `nenhuma`, recomendação
  `seguir com ressalva`) — dois achados, cada um com rota, fechados pelo `A8`.** **(i) Quinta
  recorrência da classe da contagem, agora na `RUBRICA` e por um motivo novo: o card soletrou UM
  token onde a frase tinha DOIS.** O card mandava fechar *"a frase que conta os critérios da
  seção"*, mas soletrou só `de quinze para dezoito`; a **mesma** frase da `### 8.1` carrega uma
  segunda expressão de contagem — *"e não um décimo sexto critério"* — que o card **não nomeou** e
  que sobreviveu defasada com dezoito critérios na tabela. Não é o mesmo mecanismo das quatro
  anteriores (`AE-51`, `AE-52`, `AE-57`, `AE-59`), que eram **irmãos não enumerados**: aqui o irmão
  está **dentro da mesma frase** que o card mandou consertar. **Rota:** card que fecha frase de
  contagem prescreve **todas** as expressões de contagem da frase, não a primeira. Não abre card
  aqui — a `RUBRICA` não está sob o teto de saturação do `AE-60` (que é de
  `.claude/checks/check-readme.ps1`), mas o resíduo é de **uma expressão em uma frase** e vai ao
  tíquete pós-marco junto com o item (ii). **(ii) Citação por número de linha que se desloca em
  silêncio, alvo `doutrina`.** `review_evidence.py` cita a rubrica por **faixa de linha** nos
  docstrings (`RUBRICA_DE_REVISAO.md:63-77` escopo, `:79-92` testes, `:94-106` guardas); as três já
  estavam **7 linhas** defasadas antes desta entrega e agora estão **14**, porque toda inserção na
  rubrica as desloca e **nenhum guarda falha**. **Rota:** item pós-marco — citar por **âncora de
  seção**, nunca por número de linha. **O que a entrega fez certo, e é o contraste que importa:** a
  frase do `AE-13` sobreviveu **intacta**, o parágrafo novo entrou **abaixo** dela, a `### 8.2` e o
  `card_check.py` ficaram intocados (mtime 07:27 contra 17:37 do alvo) e as seis linhas de
  `Verificação` saem como escritas ao serem re-rodadas. **A lição:** o defeito que sobrou é
  **invisível** à `Verificação` por `Select-String` — nenhuma das seis linhas conta critérios, e a
  única frase que os conta ficou **internamente contraditória depois da própria edição da entrega**.
  Aceite por ocorrência de literal não discrimina **coerência de prosa**; enquanto a classe não
  tiver varredura mecânica, ela reincide por baixo de seis linhas verdes.

- **`AE-62` (2026-09-19) — a `LM-T5a` voltou `blocked` razão `premissa`: o card manda reescrever seis
  cards como módulos sem fechar a partição, e três impossibilidades foram medidas antes de qualquer
  edição.** Conduta correta de `G-EXECREADY`: **nenhum arquivo tocado**, 9 tool uses. **(i) A
  partição não está prescrita em lugar nenhum.** O card manda *"reescrever os 6 cards `ready` como
  módulos coesos"* (`docs/plans/P-0740-loop-de-modulos.md:3216`, `:3226`, `:3268`) sem dizer
  **quantos** módulos, **qual card absorve qual matéria**, a **ordem** da fila nova e **onde entra a
  dependência do `AE-10`** — nem em `DM-2`..`DM-5`, nem no texto herdado da `LM-T5`, nem no `AE-12`
  do `P-0739`. Decidir isso é planejamento, e o executor recusou performar (`G-PLANREADY` item 3:
  decisão adiada acaba tomada pelo executor, no modelo mais barato e sem o contexto de quem
  decidiu). **(ii) A `Verificação` 2 e o `Pronto quando` exigem `card_check … --tarefa <ID>` exit 0
  "para os seis" sem nomear os seis IDs** — o executor não tem como saber quais aferir. **(iii) Duas
  impossibilidades aritméticas, medidas.** A `Verificação` 1 exige que `- **Objetivo:**` **suba em
  6** sobre a baseline; o executor mediu **18** pelo comando do próprio card, batendo com o
  `Medido antes: 18`. Subir 6 só se satisfaz **acrescentando** seis cards sem remover nenhum —
  incompatível com *"reescritos"* e com *"fila nova"*: reescrita in loco dos `ready` dá **+0**, e
  substituir os cinco por seis módulos dá **+1**. E a Contingência 1 do card **dispara**: há **5**
  cards `ready` no `P-0739` (`BKL-T5`, `BKL-T6`, `BKL-T7`, `BKL-T8`, `BKL-T9`), **não 6** — a
  `BKL-T4` fechou em 2026-09-18, **depois** do `AE-12` que contava seis. O card carrega um número de
  corpus envelhecido no próprio enunciado do escopo, não só na `Verificação`. Escalado como
  `ESC-34`.

- **`AE-63` (2026-09-19, `ESC-34`) — a partição que o card mandava executar sem tê-la decidido:
  fechada, com três impossibilidades corrigidas na raiz.** A `LM-T5a` voltou `blocked` razão
  `premissa` sem tocar arquivo, e a recusa foi **conduta correta** (`A3b`, Regra 8): o card mandava
  *"reescrever os 6 cards como módulos coesos"* sem prescrever **quantos** módulos, **qual absorve
  qual matéria**, a **ordem** e **onde entra o `AE-10`** — decidir partição é planejamento, e o
  executor varreu `DM-2`..`DM-5`, o texto herdado da `LM-T5` e o `AE-12` sem achar a decisão em
  lugar nenhum (`AE-62`). **Partição decidida pelo consultor, medida no ato (`ready 5`, `done
  11`):** três módulos em série nova de identificadores — **`BKL-T10`** (absorve `BKL-T5` `drain` +
  `BKL-T6` migração: mesmo par de superfícies, e é a migração que torna `drain`/`check` aferíveis
  sobre o estado real), **`BKL-T11`** (absorve `BKL-T7` hook + `BKL-T8` skills: os dois respondem
  *quem chama* o instrumento, e metade sem a outra deixa o pickup na heurística que o plano
  aposenta) e **`BKL-T12`** (absorve `BKL-T9` sozinha: produto é veredito do dono, marco do
  `P-0739`, e `DM-4` não deixa módulo com desfecho do dono dividir card com entrega de agente);
  ordem `BKL-T10` → `BKL-T11` → `BKL-T12`. **O `AE-10` encerra no `BKL-T10`, no texto:** a
  dependência de ordem que ele nomeava **deixou de existir** quando o `AE-47` (`ESC-27`) pôs em
  `transacionar_status` a guarda que projeta card e linha de índice e **declara** a ausência dos
  marcadores em vez de estourar — os marcadores entram na migração e o módulo cita o `AE-47`. **As
  três impossibilidades, corrigidas na premissa e não no número:** (1) o `+6` sobre 18 era
  insatisfazível por qualquer leitura de *"reescrever"* — com IDs novos e os cinco antigos ficando
  no arquivo como `cancelled` **por absorção** (corpo literal, `DM-33` (iii)), a relação vira **três
  entram, nenhum sai**, `18 → 21`, com `Medido antes: 18` re-medido e invariante enquanto a tarefa
  não roda; (2) a `Verificação` 2, que o `ESC-32` acrescentara sem os IDs, virou **três** linhas
  nomeadas de `card_check`, cada uma com `Medido antes: exit 1` medido (`tarefa não encontrada`);
  (3) o `5 vs 6` do corpo e da contingência foi corrigido com o fato que o explica — a `BKL-T4`
  fechou em 2026-09-18, **depois** do `AE-12` que contava seis. **Item novo, na forma do `ESC-32`:**
  um comando só que imprime o conjunto de `ready` do `P-0739`, afirmando **presença dos três e
  ausência dos cinco** pelo parser (`Medido antes: ['BKL-T5', …, 'BKL-T9']` →
  `['BKL-T10', 'BKL-T11', 'BKL-T12']`). `card_check` **exit 0**; o card volta a `ready` **por ato de
  replanejamento** (saída (c) do `G-REPLAN`), e o loop **não** roda `status`. **Sobre o `AE-61`:** o
  resíduo concreto do item (i) — *"e não um décimo sexto critério"*, sobrevivendo dentro da **mesma
  frase** que a `LM-T5d` mandou fechar, confirmado em 1 ocorrência contra 9 critérios `(x…)` hoje na
  tabela — vai ao **tíquete pós-marco**, com o teto do `AE-60` **estendido** a
  `docs/RUBRICA_DE_REVISAO.md` e `.claude/tools/review_evidence.py` (item (ii), citação por faixa de
  linha, 14 linhas defasadas, nenhum guarda falhando): mesmo teste de saturação, e abrir card
  reativaria o mecanismo que o `AE-60` parou. **Regra de prescrição adotada no mesmo ato**, sem
  critério novo na rubrica: *card que manda fechar frase de contagem manda re-derivar a **frase
  inteira**, e a `Verificação` carrega a ausência de **cada** expressão numérica antiga dela* — a
  regra do par aplicada **dentro** da frase. **Classificação: não estratégico.** Escopo intacto (33
  entregas), rota intacta (`LM-T5a` → `LM-T9`, marco 3 na `LM-T9`), decisão do dono intacta
  (`P-0739` segue estacionado; esta tarefa **reescreve** cards e não executa nenhum). A hipótese de
  diferir a `LM-T5a` inteira para a retomada do `P-0739` foi considerada e **rejeitada**: o produto
  dela só tem consumidor depois do fechamento do `P-0740`, mas a **decisão** de partição tomada
  agora é a única que se toma com o contexto inteiro desta janela — adiada, ela renasce fria e é
  redesenhada do zero, que é exatamente o custo que criou este papel.

- **`AE-64` (2026-09-19) — a `LM-T5a` voltou `blocked` razão `premissa` pela SEGUNDA vez, e agora o
  obstáculo é que a matéria a reagrupar aponta para superfícies que este mesmo plano destruiu.**
  Conduta correta de novo: **nenhum arquivo tocado**, 34 tool uses, Contingência 2 do card acionada
  e as três saídas possíveis enumeradas em vez de uma escolhida. **O fato, confirmado na medida pelo
  loop:** a matéria da `BKL-T8` que a `BKL-T11` deve absorver tem por alvos
  `.claude/skills/proximo-passo/SKILL.md` (passos 1-3 e 5) e `.claude/skills/handover/SKILL.md`
  (§2) — **as duas foram aposentadas e removidas da árvore pela `LM-T4`**, commitada em `f1afbd3`
  (medido agora: `.claude/skills/` tem **10** entradas, nenhuma delas as duas). E o aceite herdado
  da `BKL-T8` — *Grep `backlog.py` em `.claude/skills/` ≥ **3** arquivos* — ficou **inalcançável**:
  mede **1** hoje (`diario-de-obras`), no máximo **2** somando `scrum-master`. **As três saídas, e
  por que nenhuma é do executor:** (a) transcrever alvos inexistentes; (b) suprimir a matéria, o que
  contraria o *"nenhuma matéria perdida"* do próprio Objetivo do card; (c) reapontar para
  `passagem-de-bastao`, a sucessora — mas **card nenhum a nomeia herdeira dessa matéria**, e o
  número do aceite teria de ser re-derivado. Escolher entre elas é decisão de rota, e a Regra 8 a
  proíbe ao executor. **A classe:** não é defeito de redação do card, que o `ESC-34` já corrigiu; é
  **interferência entre planos** — o `P-0740` aposentou superfícies que a matéria estacionada do
  `P-0739` referencia, e o reagrupamento herdou o texto sem que ninguém confrontasse os alvos com a
  árvore de hoje. **Contagem para o teto do `G-REPLAN`** (`GOVERNANCA.md` §7 item 17, emendado pelo
  `RP-2`): este é o **segundo** bloqueio `premissa` desta tarefa; o teto anti-abuso é o terceiro.
  Escalado como `ESC-35`.

- **`AE-65` (2026-09-19, `ESC-35`) — decisão e transcrição se separam: o plano matou a superfície que
  a matéria estacionada referencia, e o corte certo não era escolher entre (a), (b) e (c).** A
  `LM-T5a` voltou `blocked` razão `premissa` pela **segunda** vez, sem tocar arquivo, com a
  Contingência 2 acionada — e a partição do `ESC-34` **não** foi contestada. O obstáculo é uma
  camada abaixo: a matéria da `BKL-T8` tem por alvos `.claude/skills/proximo-passo/SKILL.md` e
  `.claude/skills/handover/SKILL.md`, que **a `LM-T4` deste mesmo plano aposentou e removeu da
  árvore** (`f1afbd3`), e o aceite herdado dela (*Grep `backlog.py` em `.claude/skills/` ≥ **3**
  arquivos*) ficou **inalcançável**: mede **1** hoje (`AE-64`). **Decisão (consultor,
  técnica/tática):** nenhuma das três saídas enumeradas pelo executor, e sim o corte que as dissolve
  — **o card troca de produto**. Entrega **a decisão** (a partição do `ESC-34` transcrita sem
  re-decisão, o mapa de herança e a regra de re-derivação do número) e **não** a transcrição;
  escrever os três módulos `BKL-T10`..`BKL-T12` passa a ser o **primeiro ato da retomada do
  `P-0739`**, com a árvore parada. **Critério, enunciado aqui pela primeira vez e válido para além
  deste card:** *decisão carrega contexto e envelhece se adiada; transcrição mede a árvore e
  envelhece se antecipada* — é o refinamento do argumento com que o `ESC-34` recusou diferir a
  tarefa inteira, e mostra que aquele argumento cobria a partição, não a transcrição. **Por que não
  a rota (c) pura:** reapontar para `passagem-de-bastao` e re-derivar o número **desbloquearia** o
  card, mas deixaria de pé o mecanismo que o bloqueou duas vezes — transcrever aceite herdado contra
  árvore móvel —, e os aceites dos outros módulos poderiam esconder mais números inalcançáveis como
  o `≥ 3`. Com o produto trocado **não há número herdado a transcrever nem alvo morto a apontar**, e
  o terceiro bloqueio, que esgotaria o teto anti-abuso do `G-REPLAN` (`GOVERNANCA.md` §7 item 17,
  emendado pelo `RP-2`) e levaria a matéria ao dono, perde por onde vir. **Varredura, feita uma vez
  e que não se repete:** todos os caminhos citados pelos cinco cards `ready` do `P-0739` foram
  confrontados com a árvore de hoje — **mortos: exatamente dois**, ambos pela `LM-T4`; **não** são
  alvo morto, apesar de ausentes, o `backlog_hook.py` (arquivo a **criar** pela matéria da
  `BKL-T7`), o `GOVERNANCA_MEMORIAS.md` (doc global, fora do repo) e os padrões de nome de plano
  citados em prosa; os outros vinte caminhos existem. **Não há terceira superfície morta**, logo a
  `BKL-T10` e a `BKL-T12` não batem no que a `BKL-T11` bateu — e a Contingência 2 do card novo manda
  parar caso apareça uma, porque decidir herança é do consultor. **Herança decidida (ratificação,
  não invenção):** `passagem-de-bastao` é herdeira da matéria de skill da `BKL-T8` — a `LM-T4` já a
  criou *"como NOVO… mesmo conteúdo"* — e o `scrum-master` fica com a parte de condução do loop; o
  número `≥ 3` **não se transcreve**, escreve-se a **regra** (*toda skill que invoca o instrumento o
  cita*) e re-deriva-se na retomada, critério (xiii)/(xviii) aplicado a um número que hoje vale `1`.
  **Card reescrito, `card_check` exit 0**, seis linhas de `Verificação`, **três delas `inalterado`**
  — o conjunto de `ready` do `P-0739` e a contagem de `- **Objetivo:**` provam que a tarefa **não**
  transcreve card nenhum, e a aritmética do `+3` do `ESC-34` saiu junto com a transcrição, porque
  pertence à retomada. Card volta a `ready` por ato de replanejamento (saída (c) do `G-REPLAN`); o
  loop **não** roda `status`. **Marco 3 confirmado:** a `LM-T9` depende só da `LM-T6` (fechada) e
  **não** da `LM-T5a` — o marco é despachável com ou sem ela, e as duas não têm dependência entre
  si. **Não estratégico:** escopo intacto (33 entregas, nenhuma some — o que muda é o produto de
  uma), rota intacta (marco 3 na `LM-T9`), decisão do dono intacta (`P-0739` segue estacionado e
  nenhuma tarefa dele é executada).

- **`AE-66` (2026-09-19, pendência do laudo da `LM-T5a` roteada pelo `B1`) — a nota da decisão
  nasceu com identificador colidente e deixou de pé o item que ela supera.** Veredito
  `aprovado 100%`, bloqueante `nenhuma`, recomendação `escalar`. **(i) Colisão de identificador.** O
  card mandou a nota datada **sem fixar o identificador dela**; a entrega escolheu `AE-13`, próximo
  livre da série local do `P-0739` (`AE-10`..`AE-12`) — mas **`AE-13` já nomeia achado vivo e
  diferente no `P-0740`** (12 citações, inclusive em `docs/RUBRICA_DE_REVISAO.md` §3, que a `LM-T5d`
  acabou de editar). A decisão de nome foi tomada pela **entrega** porque o card não a fechou; sob
  `G-NOASK` o executor não tinha a quem perguntar, e escolher o próximo livre da série local é a
  leitura defensável. **A causa é de autoria:** as séries `AE-<n>` são **por plano** e ninguém
  declarou isso, então duas séries vivas colidem sem que nenhum instrumento perceba. **(ii) O
  `AE-12` do próprio `P-0739` não foi reconciliado.** O Produto fechado em (a)(b)(c) não previu
  isso: o `AE-12` (`P-0739` linhas 2973, 2975, 2977) conta **`6 tarefas ready restantes`** e **`os 6
  cards`** — medido hoje: **5** ready, **11** done, **16** no total — e atribui à `LM-T5` a
  reescrita dos cards que a nota nova devolve à **retomada**. Os dois itens ficam vivos e
  **divergentes na mesma seção**, e a retomada do `P-0739` abriria lendo os dois. A entrega não
  podia fechar isso: reconciliar achado é **ato de autoria em plano estacionado**, fora do alcance
  da execução e da revisão. Escalado como `ESC-36`. **Lição medida, e é a síntese da tarefa:** três
  despachos para um card — dois bloqueios em Opus (67,1k e 119,8k) e a execução limpa em Sonnet
  (72,5k / 20 tool uses). **O que destravou não foi refinar o card, foi trocar o produto** (decisão
  em vez de transcrição), e os dois bloqueios mediram coisas **diferentes**, ambos conduta correta.
  A revisão saiu barata por uma escolha de autoria: **três das seis linhas de `Verificação` provam o
  que a tarefa NÃO fez** (conjunto `ready`, contagem de `Objetivo`, suíte), por comando
  re-derivável em vez de prosa — e foram elas que dispensaram varredura manual do diff para atestar
  que nenhum card foi criado ou reescrito.

- **`AE-67` (2026-09-19, `ESC-36`) — a série `AE-<n>` é por plano, e ninguém tinha escrito isso; o
  `AE-12` do `P-0739` fechou junto.** A nota entregue pela `LM-T5a` no `P-0739` recebeu o
  identificador `AE-13`, próximo livre da série **local** daquele arquivo (`AE-1`..`AE-12`),
  enquanto `AE-13` também nomeia achado vivo e diferente no `P-0740`, citado **14** vezes (re-medido
  no ato), inclusive em `docs/RUBRICA_DE_REVISAO.md` §3. **Veredito: colisão aparente, escolha da
  entrega correta.** As séries **são** por plano — os dois arquivos começam em `AE-1` e a prosa dos
  dois já desambigua (*"o `AE-10` do `P-0739`"*, *"o `AE-2` deste plano"*); o defeito é de
  **autoria**, não de execução: a regra nunca foi escrita, e sob `G-NOASK` o executor não tinha a
  quem perguntar. **Decisão (consultor, técnica/tática):** não renomear — renomear transferiria a
  ambiguidade para a série local sem fechar a classe —, e sim **escrever a regra onde a retomada
  tropeçaria**, dentro da própria nota: *a série `AE-<n>` é por plano, e citação de achado de outro
  plano leva sempre o qualificador `AE-<n>` **do** `<plano>`*. A publicação em doutrina do kit é
  **pós-marco**, roteada ao **`TK-55`**, que é literalmente o acumulador de derivado que aponta
  errado **sem sinal** — nenhum instrumento confere séries de achado. **Segunda pendência, fechada
  no mesmo ato:** o `AE-12` do `P-0739` declarava *"6 tarefas `ready` restantes"* e *"os 6 cards"*, e
  atribuía a reescrita à `LM-T5` do `P-0740`; medido agora, são **5** `ready`, **11** `done`, **16**
  no total — a `BKL-T4` fechou em 2026-09-18, **depois** daquela redação — e a reescrita passou a
  ser o primeiro ato da retomada (`ESC-35`). Reconciliado por parágrafo datado **abaixo** do texto
  original, que fica **literal** como registro, fechando as **duas** expressões de contagem juntas —
  é a regra do `ESC-34` (*frase de contagem fecha por inteiro*) aplicada a um **achado** em vez de a
  um card, e o caso mostra que a regra não é sobre cards, é sobre qualquer prosa que conte. **Por
  que sem card e por que antes do commit:** é reparo de rótulo e supersessão do **produto do próprio
  card do consultor**, não execução do `P-0739` — nenhuma tarefa executada, nenhum card criado ou
  reescrito, nenhum `Status` mudado, o que foi **provado** re-rodando as três linhas `inalterado` da
  `LM-T5a` depois da edição (conjunto `ready` idêntico, `- **Objetivo:**` em 18) mais o `card_check`
  da `LM-T9` verde; e porque o commit do marco **congela** o texto, e identificador ambíguo com
  contagem falsa dentro da árvore que o dono valida é o derivado-que-mente que esta janela passou
  inteira fechando. **Lição de autoria que o laudo mediu e que vale registrar como técnica, não como
  elogio:** três das seis linhas de `Verificação` da `LM-T5a` provam o que a tarefa **NÃO** fez
  (conjunto de `ready` inalterado, contagem de `Objetivo` inalterada, suíte verde), por comando
  re-derivável — e foram elas que dispensaram varredura manual de diff na revisão. É a **terceira**
  forma de aceite usada nesta janela, ao lado da presença (`≥ 1`) e do par presença-ausência
  (`ESC-32`): o aceite por **invariância**, que é o único que cabe quando o produto é decisão e não
  código. **Classificação: não estratégico** — escopo, rota e decisões do dono intactos; a `LM-T9`
  segue sendo o marco 3 e não depende desta matéria.

- **`AE-68` (2026-09-19, pendência do laudo da `LM-T9` roteada pelo `B1`) — o artefato de validação
  do marco 3 carrega três afirmações que o próprio repositório falsifica.** Veredito `ressalva 88%`,
  bloqueante `nenhuma`, recomendação `escalar`. **As três, medidas pelo reviewer contra a árvore:**
  (1) a spec afirma que *"a figura não apensa linha de telemetria"* (§1 e §9) contra **14** linhas
  `ESC-23`..`ESC-36-consultor` em `docs/telemetria.tsv`; (2) a tabela de §1 marca a terceira
  instância com consumo *"não medido"*, quando `ESC-27`..`ESC-36` têm `tool_uses`, `tokens_k` e
  `duracao_s` **publicados**; (3) o censo *"três instanciações / 33 acionamentos"* **omite a
  instância `ESC-23`..`ESC-26`** — que é justamente a sucessora provisionada após a morte por limite
  do `ESC-22`, matéria empírica da pergunta (g) — e com ela a classe de gatilho do `ESC-26` (ato do
  dono no fechamento de marco), o que derruba o *"nenhuma outra apareceu em 33 acionamentos"* da
  pergunta (a). **Segundo achado — a pendência do executor, respondida pelo reviewer:** a cláusula
  *"se a spec concluir que a definição diverge, o achado sai como `AE-<n>` com rota"* **exigia
  achado próprio** — o `I-5` é insumo que **põe** a pergunta, não achado com rota, e a spec a
  **fechou** com veredito. **Terceiro — a `Verificação` item 3 do card não discrimina o que o
  Objetivo pede:** conta **linhas** com o literal `I-` na spec (12) contra a contagem de insumos
  `I-<n>` de `## 9` (10) — **populações diferentes**. Ela sai verde com o `I-3` (*"o que ela absorveu
  foi autoria de card, não execução; oito tarefas com zero reprovações"*) **não citado em lugar
  nenhum** da spec, justamente o insumo que sustenta a pergunta (c). **Quarto, de higiene e já
  fechado pelo loop:** o dossiê de evidência reportou `grep.exe.stackdump` sem atribuição —
  reconciliado como resíduo de crash do `grep.exe` do msys (1729 B, stack trace de `msys-2.0.dll`),
  **não autoria**, untracked e a caminho do commit do marco; removido e coberto por `*.stackdump` no
  `.gitignore` **antes** do commit. **A lição do laudo, e é a mais importante do marco:** os três
  defeitos **não são de redação** — são de **conferência contra a árvore**, classe que **nenhuma**
  das três linhas de `Verificação` do card toca, porque todas medem **presença**. *Card de redação
  cujo produto é "descrever o medido" precisa de pelo menos uma linha de aceite que **RE-MEDE** a
  afirmação central contra a fonte, e não a presença dela no texto.* É a quarta forma de aceite que
  esta janela descobre, depois da presença, do par presença-ausência (`ESC-32`) e da invariância
  (`AE-67`). Escalado como `ESC-37`. **O commit do marco 3 fica retido até a decisão**, porque é
  ele que congela o texto que o dono lê.

- **`AE-69` (2026-09-19, `ESC-37`) — o artefato de validação do marco afirmava sobre a figura três
  coisas que a árvore falsifica; e a divergência entre a definição e a prática, que a cláusula do
  card exigia, fica aberta com rota.** O laudo da `LM-T9` (`ressalva 88%`, bloqueante `nenhuma`,
  `escalar`) mediu em `docs/consultant-spec.md`: (1) *"a figura não apensa linha de telemetria"* (§1
  e §9) contra **14** linhas `ESC-23-consultor`..`ESC-36-consultor` em `docs/telemetria.tsv`; (2) a
  3ª linha da tabela de §1 marcando consumo *"não medido"* quando `ESC-27`..`ESC-36` têm
  `tool_uses`, `tokens_k` e `duracao_s` publicados; (3) o censo *"três instanciações / 33
  acionamentos"* **omitindo a instância `ESC-23`..`ESC-26`** — a sucessora provisionada após a morte
  por limite do `ESC-22`, que é a matéria empírica da pergunta (g) — e, com ela, a classe de gatilho
  do `ESC-26` (**ato do dono no fechamento de marco**), o que derruba o *"nenhuma outra apareceu"* da
  pergunta (a). Mais dois: (4) a cláusula *"se a spec concluir que a definição diverge, o achado sai
  como `AE-<n>` com rota"* exigia **achado próprio**, e a spec fechou a pergunta por veredito; (5) a
  `Verificação` 3 do card contava **linhas** com o literal `I-` na spec (12) contra a **contagem** de
  insumos `I-<n>` de `## 9` (10) — populações diferentes —, saindo verde com o `I-3` **não citado em
  lugar nenhum**, justamente o insumo que sustenta a pergunta (c). **Valores medidos no `ESC-37`,
  para transcrição:** quatro instâncias — `1ª` `9 passagens` / `2.639,1k`; `2ª` `14 acionamentos` /
  `3.802,2k`; `3ª` **`4 acionamentos`** (`ESC-23`..`ESC-26`) / **`857,7k`**, encerrada por ato do
  dono; `4ª` **`10 acionamentos`** (`ESC-27`..`ESC-36`) / **`2.776,3k`** — total **`37`**
  acionamentos (`9+14+4+10`), **14** linhas de telemetria, e `I-3` como **único** insumo não citado
  (diferença de conjuntos, não contagem). **Decisão (consultor, técnica/tática):** corrigir
  **antes** do commit, porque commit congela e este é o texto que o dono lê **para validar** —
  validar a figura sobre premissa falsa a respeito dela é o defeito que esta janela inteira
  combateu —; e corrigir **por card com gate** (`LM-T16`, `low`, dez linhas de `Verificação`,
  `card_check` exit 0), **não** por reparo direto do consultor, **exceção declarada ao que o
  `ESC-36` fez**: o documento descreve a figura que o repararia e o censo conta as instâncias dela,
  e quem achou as três falsificações foi o **reviewer**, de fora. O consultor prescreve os literais
  medidos; não escreve no documento sobre si. O marco 3 **passa a ser o fechamento do plano na
  `LM-T16`**; a `LM-T9` **não** se reabre (está `done`, com RDO), e a correção **não toca juízo
  nenhum** da spec — respostas (a)..(h), estrutura e conclusões ficam literais. **Quarta forma de
  aceite, adotada no card e nomeada pelo laudo:** *conferência contra a fonte* — a `Verificação` 8
  extrai o número que a spec publica e o **re-mede** contra `docs/telemetria.tsv`, imprimindo
  `iguais`/`divergem` (`Medido antes: divergem: arvore=14`), e a `Verificação` 1 compara
  **conjuntos** de insumos (`Medido antes: ['I-3']`). Com ela, a janela fecha com quatro formas
  medidas: **presença** (`≥ 1`), **par presença-ausência** (`ESC-32`), **invariância** (`AE-67`) e
  **conferência contra a fonte** (`ESC-37`) — e a regra que as ordena: *card cujo produto é descrever
  o medido não se aceita por presença do texto, e sim por re-medida da afirmação central*. **O
  achado próprio que a cláusula exigia, aberto aqui com rota:** a definição em
  `.claude/agents/pantonic-consultant.md` **diverge da prática medida, por omissão e não por
  violação**. Sustentaram-se: não commitar (zero commits em 11 acionamentos), não falar com o dono
  (tudo pelo relatório do `scrum-master`, `G-NOASK`), não reabrir objetivo de plano, não julgar
  entrega. **Não estavam previstos e aconteceram:** autorar card (cinco novos, `LM-T12`..`LM-T16`;
  três reescritos, `LM-T5a` duas vezes, `LM-T9`, `LM-T5d`), declarar o **marco 3** que o plano não
  declarava, declarar **teto de saturação** de superfície e **editar arquivo de outro plano**
  (`P-0739`, `ESC-36`) — todos atos de **planejamento**, isto é, exatamente a fronteira com o
  `pantonic-planner` que a própria definição declara **inexistente até plano do dono**. E uma
  afirmação da definição que o registro falsifica: *"Responde curto."* **Rota:** nenhuma correção de
  doutrina agora — a matéria é do **plano que o dono declarou** sobre a figura, e esta spec é o
  insumo dele; o marco entrega o insumo **verdadeiro**, não a decisão. **Tensão registrada para o
  dono ler junto:** a spec da figura foi escrita a partir dos rastros da figura e corrigida sob
  prescrição dela; o único olhar independente que a atravessou foi o do reviewer, e foi ele que
  achou as três falsificações — é a razão material de a `LM-T16` ser card com gate.
  **Classificação: não estratégico** — o escopo ganha uma tarefa de correção factual, a rota não
  muda (o marco continua sendo o fechamento do plano, uma tarefa adiante), nenhuma decisão do dono é
  tocada, e nada sobe a ele senão pelo relatório de encerramento.

- **`AE-70` (2026-09-19, `ESC-38`) — a quarta forma de aceite nasceu violando o critério (xviii), e o
  que a pegou foi o gate: invariância é propriedade do recorte, não do valor.** A `Verificação` 8 da
  `LM-T16`, criada no `ESC-37` para conferir a spec contra a árvore, publicava
  `Medido antes: divergem: arvore=14` — uma **constante de corpus** embutida no literal, sobre
  `docs/telemetria.tsv`, que é o corpus mais móvel do repositório: **toda** ação do loop o move,
  inclusive a de escalonar para o consultor. O `Medido antes` morreu **entre a autoria e o
  despacho**, pelo ato de registrar o próprio escalonamento que autorou o card: o `scrum-master`
  apensou a linha `ESC-37-consultor` e o gate mediu `divergem: arvore=15`. Sexta recorrência da
  classe da contagem nesta janela, e a primeira **dentro do remédio contra ela**. **Diagnóstico, que
  emenda o critério (xviii) sem reescrevê-lo:** ao fixar o (xviii) no `ESC-28`, invariância foi
  tratada como propriedade do **valor**; ela é propriedade do **recorte**. `14` não é constante
  enquanto o recorte for *"a árvore hoje"*; `14 até o ESC-36` é constante para sempre, porque nenhum
  acionamento futuro entra num intervalo fechado. **Regra adotada:** *número de série que o próprio
  ato de medi-lo incrementa não se publica como total — publica-se com recorte **fechado, nomeado
  pelo último evento contado**; recorte fechado devolve a constante à condição de constante.*
  **Correção aplicada nos dois lados, não só no valor** (corrigir o número seria repetir o defeito
  no despacho seguinte): a `Verificação` 8 passa a contar **só** `ESC-23`..`ESC-36` e a imprimir
  **veredito binário** (`iguais`/`divergem`, sem `arvore=N`), com `Medido antes: divergem` — é o
  `iguais`/`divergem` que o `ESC-28` já usara na `LM-T4c`, agora aplicado ao próprio remédio; a
  tabela do produto (a) declara que **toda** contagem leva o recorte `até o ESC-36` e **não** *"até
  agora"*, nomeando a causa (a série cresce pelo ato de escalonar); o produto (b) publica `14 linhas
  de telemetria`, **uma por acionamento**, com a contagem `até o ESC-36` na mesma frase; o produto
  (c) passa a `37 acionamentos até o ESC-36`, preservando o literal que a `Verificação` 7 confere; e
  entra a `Restrição` **número de série do consultor não entra sem recorte nomeado**, nem no texto
  da spec nem em literal de aceite. **Prova de invariância, medida:** a árvore já tem **15** linhas
  `-consultor` (a `ESC-37` incluída) e o item 8 mede **14** no recorte, saindo `divergem` — o
  acionamento que corrigiu o card não o envelhece, e o que responder a este também não. `card_check`
  **exit 0**. **Fato de processo que fecha a série das recorrências com sinal invertido:** o defeito
  foi interceptado **pelo instrumento, antes do despacho**, com zero tokens de executor, zero
  arquivos tocados e zero revisões gastas — `AE-51`, `AE-52` e `AE-57` custaram um card cada,
  `AE-59` foi barrado pelo teto do `AE-60`, `AE-61` foi ao tíquete, e este custou **um
  `card_check`**. É a `### 8.1` cumprindo o que prometeu: *o que fecha defeito de autoria é comando
  que falha ruidosamente no ato da autoria*. **Classificação: não estratégico**, e a correção é de
  **forma**, não de valor — escopo e rota intactos (34 tarefas, marco 3 no fechamento pela
  `LM-T16`), nenhuma decisão do dono tocada.

- **`AE-71` (2026-09-19) — a `LM-T16` voltou `blocked` razão `premissa`: renumerar a instância na
  tabela deixaria a prosa das respostas contraditória, e o card escopou só a tabela.** Conduta
  correta: arquivo **restaurado ao original**, `git status` confirma `?? docs/consultant-spec.md`
  **sem diff**, e a Contingência 2 do próprio card (*mexer em resposta (a)..(h) para não ficar
  contraditória → `blocked`*) foi acionada em vez de contornada. **O fato, confirmado na medida pelo
  loop:** o rótulo `3ª instância` aparece **7** vezes em `docs/consultant-spec.md`
  (`:37`, `:50`, `:62`, `:87`, `:90`, `:123`, `:296` — inclusive no título *"Panorama medido dos dez
  acionamentos da 3ª instância"*), **todas** referindo o grupo `ESC-27`..`ESC-36`, que o Produto (a)
  renomeia para **4ª**. Os Produtos (a)..(f) escopam a **tabela de §1**; as sete ocorrências vivem
  nas respostas (a), (b), (c), (d) e (h), fora do escopo. Renomear só a tabela publicaria um
  documento que se contradiz em sete pontos. **A classe:** é a contagem de novo, e numa forma que a
  janela ainda não tinha visto — não é frase que **conta** (`AE-51`, `AE-57`, `AE-61`) nem irmão não
  enumerado (`AE-52`, `AE-59`) nem constante de corpus (`AE-49`, `AE-70`), e sim **rótulo ordinal
  que o próprio recenseamento reordena**. Corrigir o censo **renumera referências**, e o card que
  corrige censo tem de escopar **todas** elas, não a tabela. Escalado como `ESC-39`. **Sétima
  recorrência da classe na janela, e a segunda barrada antes de qualquer escrita** — a anterior pelo
  `card_check` (`AE-70`), esta pela contingência que o próprio card carregava.

- **`AE-72` (2026-09-19, `ESC-39`) — rótulo ordinal é posição relativa, e recenseamento move
  posição: o censo sai da prosa e vira recorte.** A `LM-T16` voltou `blocked` razão `premissa`,
  **sem diff**, com a **Contingência 2 do próprio card** acionada: o Produto (a) renomeava o grupo
  `ESC-27`..`ESC-36` de `3ª` para `4ª` **na tabela de §1**, mas o rótulo `3ª instância` aparece **7**
  vezes em `docs/consultant-spec.md`, todas referindo o mesmo grupo e **todas fora** do escopo
  declarado — renomear só a tabela publicaria, no artefato que o dono lê para validar, um documento
  que se contradiz em sete pontos. **Classe nova, a sétima da janela:** não é frase que **conta**
  (`AE-51`, `AE-57`, `AE-61`), nem irmão não enumerado (`AE-52`, `AE-59`), nem constante de corpus
  (`AE-49`, `AE-70`) — é **rótulo ordinal que o próprio recenseamento renumera**; corrigir censo
  **move referência**, e card que corrige censo tem de escopar **as referências**, não a seção.
  **Rota decidida: a prosa deixa de usar ordinal.** As sete ocorrências passam a `instância do
  recorte` + `ESC-27`..`ESC-36`; a tabela **mantém** o ordinal como rótulo de linha e ganha coluna
  **`recorte`** (`3ª` = `ESC-23`..`ESC-26`, `4ª` = `ESC-27`..`ESC-36`), onde o ordinal é inofensivo
  porque um recenseamento futuro o corrige **na mesma célula** em que o corte aparece. O título da
  seção (h) — *"Panorama medido dos dez acionamentos da 3ª instância"* — fecha os **dois** números
  juntos (`ESC-34`): `dez` continua verdadeiro dentro do recorte nomeado e permanece, o ordinal sai.
  **A rota de eliminar ordinal em toda a tabela foi medida e recusada por falta de lastro:** as
  linhas `ESC-1`..`ESC-21` da telemetria **não têm a marcação `-consultor`** (ela começa no
  `ESC-23`), então o recorte da `1ª` e da `2ª` instância **não é derivável da árvore** — elas recebem
  `—` na coluna nova, com a razão escrita, o que é **informação para quem lê** e não lacuna a
  preencher por dedução; prescrever corte não medido seria o único vício que esta janela recusou em
  todos os escalonamentos. **Por que não recorre:** as duas versões anteriores do card escoparam por
  **seção**, e seção não é onde o defeito mora; esta escopa por **ocorrência medida**, e a
  `Verificação` 11 é **uma** linha que cobre **as sete** — `3ª instância` → `0`, `Medido antes: 7` —,
  a mesma afirmação universal do `ESC-32` que parou a série do `README`/guarda. Mais duas linhas:
  `instância do recorte` → `≥ 7` (`Medido antes: 0`) e `dez acionamentos da 3ª instância` → `0`
  (`Medido antes: 1`). `card_check` **exit 0** com treze itens. **A hipótese de mandar o artefato
  como está, com o ordinal defeituoso e um `AE-<n>` de registro, foi recusada por mérito:** as outras
  duas afirmações falsas eram sobre telemetria e consumo, mas esta é o **censo**, e o que ele omite é
  a instância que morreu por limite e a sucessora provisionada — **a matéria empírica da pergunta
  (g)**; um censo que omite a morte, no documento com que o dono decide se formaliza a figura, erra
  no único ponto em que o artefato precisa estar certo. **Fato de processo que a janela fecha:** esta
  é a terceira rodada sobre o mesmo artefato e a **segunda barrada antes de qualquer escrita** — a
  anterior pelo `card_check` (`AE-70`), esta pela contingência que o próprio card carregava. Nenhuma
  das três custou execução desperdiçada nem revisão: o custo dos defeitos de autoria do consultor
  passou a ser pago por **gate**, não por executor nem por reviewer. **Classificação: não
  estratégico** — escopo e rota intactos (34 tarefas, marco 3 no fechamento pela `LM-T16`), nenhuma
  decisão do dono tocada.

- **`AE-73` (2026-09-19, pendência do laudo da `LM-T16` roteada pelo `B1`) — a correção do censo
  ficou pela metade e o documento passou a se contradizer; e a afirmação universal que deveria
  impedir isso tem ponto cego de quebra de linha.** Veredito `ressalva 88%`, bloqueante `nenhuma`,
  recomendação `escalar`. **(i) O artefato ainda carrega três afirmações que o próprio censo novo
  falsifica**, medidas pelo reviewer e confirmadas pelo loop: `docs/consultant-spec.md:7` diz
  *"medido ao longo de **três** instanciações"* contra `:28` *"As **quatro** instâncias medidas"*; e
  **o mesmo evento** aparece rotulado `3ª instância` (`:63-64`) e `instância do recorte
  ESC-27..ESC-36` (`:134-135`). **(ii) A `Verificação` 11 não mede o que promete.** Foi autorada
  como **afirmação universal** sobre 7 ocorrências, mas o comando que a mede
  (`Select-String -SimpleMatch`, **linha a linha**) não discrimina texto quebrado por **soft-wrap**:
  a população real é **8** — medido, `grep -c '3ª instância'` → **0** e regex multilinha
  `3ª\s+instância` → **1**, sobrevivente em `:63-64` (`…acionamento da 3ª\n   instância:…`). E
  referência **sem o substantivo** (`quatro na 3ª`, `:144`) escapa de qualquer busca pelo literal
  composto. **(iii) O bloco `Verificação` do card numera `1..9, 11, 12, 13` e só então `10`** — os
  treze itens exigidos pelo `Pronto quando` só se contam à mão, e a ordem quebrada é exatamente o
  que o parser de itens da `RUBRICA` `### 8.1` lê. **A lição, e ela generaliza:** *tarefa de
  renomear referente em prosa não se afere por contagem de literal linha-a-linha — o aceite de uma
  renomeação é (a) **regex multilinha** sobre o literal e (b) uma **leitura do referente**: o mesmo
  evento não pode aparecer com dois rótulos no mesmo documento.* É a quinta forma de aceite que a
  janela descobre, depois de presença, par presença-ausência, invariância e conferência contra a
  fonte — e a primeira em que o defeito não está no valor nem no recorte, e sim no **instrumento de
  medida do próprio aceite**. **Nota de custo do laudo:** o consumo da tarefa não tem anomalia para
  `classe redacao low`; *o custo desta tarefa não está nos turnos, está na terceira reescrita do
  card*. Escalado como `ESC-40`. **O commit do marco 3 segue retido.**

- **`AE-74` (2026-09-19, `ESC-40`) — o aceite media frase e o defeito era de token; e o limite do
  laço passa a ser regra escrita, não juízo de quem está dentro dele.** A `LM-T16` fechou
  `ressalva 88%` deixando a spec **internamente contraditória** em quatro pontos: `:7` *"medido ao
  longo de **três** instanciações"* contra `:28` *"As **quatro** instâncias medidas"*; o mesmo evento
  rotulado `3ª instância` (`:63-64`) e `instância do recorte` (`:134-135`); e `:144` *"quatro na
  **3ª**"*, referência **sem substantivo**. **Causa medida, e é do aceite, não da entrega:** a
  `Verificação` 11 usava `Select-String -SimpleMatch`, que casa **linha a linha** e não enxerga
  soft-wrap — `grep -c '3ª instância'` devolve **0** e a regex multilinha devolve **1**; a população
  real era **8**, não 7. **Decisão: mais um card (`LM-T17`, `low`, sete linhas, `card_check` exit
  0), com o aceite medindo TOKEN e não frase** — `len(re.findall(r'3ª', spec))` → **1**
  (`Medido antes: 3`), porque `3ª` só pode sobrar na célula da tabela e **toda** forma em prosa,
  quebrada, abreviada ou futura, cai na mesma contagem. É a primeira linha de aceite da janela
  **completa por construção** para a pergunta que faz, e não apenas mais ampla que a anterior — a
  quinta forma (`regex multilinha + leitura de referente`, nomeada pelo laudo) entra com a metade
  mecânica fechada. **As três substituições fecham os números por inteiro (`ESC-34`):** `:7`
  `três`→`quatro instanciações`; `:63-64` → `instância do recorte` + corte; e `:143-145`, que
  carrega **três** números — incluindo `de 29 a 33 entregas`, série que o próprio ato de escrever
  incrementa —, ganha o recorte `até o ESC-36`, sem o qual morreria no escalonamento seguinte
  (`AE-70` de novo). O bloco `Verificação` da `LM-T16`, com a numeração `1..9, 11, 12, 13, 10`
  herdada do patch do `ESC-39`, **não** se renumera: card fechado é registro (`DM-33` (iii)), e o
  defeito fica anotado. **O teste de saturação do `AE-60` foi aplicado e NÃO disparou**, e é isso que
  autoriza esta rodada: o achado **não** exige precondição mais rara (aparece na primeira leitura,
  na linha do *Método* e na tabela) e o veredito **não** se manteve correto (o documento afirma
  `três` e `quatro` ao mesmo tempo) — contradição interna no artefato de validação não é resíduo
  cosmético, é o artefato falhando no que existe para sustentar, e a pergunta (g) depende desse
  número. A hipótese de mandar assim, levantada pelo loop, foi pesada e recusada por isso.
  **Governança, e é a parte que não é sobre o card:** são **quatro** rodadas sobre o documento que
  formaliza a **própria figura que decide quantas rodadas fazer**, com o único olhar independente
  sendo o do reviewer. Quem limita esse laço não pode ser o juízo de quem está dentro dele, então o
  limite virou **regra escrita em `## 6`**: *esta é a última rodada de correção sobre
  `docs/consultant-spec.md` neste plano; achado novo depois dela não abre card e vai ao plano que o
  dono declarou sobre a figura*. É o teto do `AE-60` aplicado **prospectivamente** em vez de depois
  do fato. **Classificação: não estratégico** — escopo ganha uma correção (35 tarefas), a rota não
  muda (marco 3 segue sendo o fechamento do plano, agora na `LM-T17`), nenhuma decisão do dono é
  tocada, e o que sobe a ele sobe pelo relatório: quatro rodadas, o teto declarado, e a tensão de
  autoria registrada.

- **`AE-75` (2026-09-19, laudo da `LM-T17`, `aprovado 100%`, bloqueante `nenhuma`, recomendação
  `escalar`) — o teto prospectivo do `AE-74` entrou em ação na primeira oportunidade, e foi o
  reviewer quem o invocou.** A entrega fechou o que se propôs: o token `3ª` caiu de **3** para
  **1**, sobrevivendo só na célula da tabela; as seis linhas de regex saíram nos valores declarados
  (`1, 0, 1, 9, 1, 1`) e a bateria inteira da `LM-T16`, re-rodada sobre a árvore de hoje, sai
  **verde nas nove linhas** — prova de que a terceira rodada não desfez a segunda (`201 passed`).
  **Os achados restantes, todos roteados pelo teto e nenhum abrindo card:** (i) `docs/consultant-spec.md`
  §10 publica *"o empréstimo é fato medido **nove** vezes"* **sem recorte**, e a árvore mede **11** —
  a figura autorou a `LM-T16` (`ESC-37`) e a `LM-T17` (`ESC-40`) **depois** do `ESC-36`, de modo que
  o artefato carrega um número que **o próprio ato de escalonar falsificou**; (ii) §6 traz *"de 29
  para 33 cards numa janela"*, hoje **35** — reincidência do `AE-71`, *card que corrige censo tem de
  escopar todas as referências, não a tabela*, e este censou três sítios (`:7`, `:63-64`,
  `:143-145`) em vez de todos os números de série do documento; (iii) §1 `:42-45` atribui as **14**
  linhas `ESC-23-consultor`..`ESC-36-consultor` à instância do recorte `ESC-27`..`ESC-36`, que a
  mesma tabela conta em **10** acionamentos — a marcação `-consultor` começa no `ESC-23`, e quem não
  participou da janela lê 14 acionamentos onde há 10. **Rota dos três: o plano que o dono declarou
  sobre a figura**, por aplicação direta do teto escrito em `## 6` pelo `ESC-40` (*última rodada de
  correção sobre `docs/consultant-spec.md` neste plano; achado novo depois dela não abre card*). É a
  primeira vez na janela em que a regra que limita o laço opera **sem** consultar quem está dentro
  dele — que era exatamente o objetivo dela. **Dois achados fora do teto, com rota própria:** (iv) o
  dossiê de evidência **não isolou a autoria julgada** — `docs/consultant-spec.md` está `untracked`
  (`??`), então `review_evidence.py` cola o arquivo inteiro truncado em 4000 caracteres em vez do
  diff, e a terceira autoria do dia só se separou por comparação manual; (v) **alvo `rubrica`:** a
  `RUBRICA_DE_REVISAO.md` §6 nomeia o alvo do achado como `dossiê` e o gerador só aceita `dossie`
  (`rdo.py laudo --achado-processo` falha com *alvo 'dossiê' fora de ['dossie', …]*) — é o defeito
  (iii) da própria §8 aplicado à régua: **a doutrina publica uma grafia que o parser rejeita**.
  **A lição que o laudo extrai, e fecha a série das cinco formas de aceite:** *o que o token não
  cobre é **referente*** — os dois primeiros achados saíram da **leitura ponta a ponta** do
  documento, não de contagem nenhuma. Aceite completo por construção **para a pergunta que faz** não
  é aceite completo **para a coerência do artefato**.
