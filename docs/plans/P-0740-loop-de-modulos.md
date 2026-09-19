# P-0740 — O loop de módulos: a convergência da EXECUCAO-AUTONOMA sob a janela real

**Data:** 2026-09-18 · **Origem:** aferição empírica do `scrum-master` conduzida em janela de
orquestração (run de ponta a ponta sobre a `BKL-T4` do `P-0739`), mais a correção da premissa de
tamanho de janela · **Status:** `in-progress` (2026-09-18 — rodadas `RP-2` e `RP-3` fechadas: o segundo bloqueio da `LM-T1` era **de aceite**, não de rota, `DM-12`; e a gramática de cabeçalho da `DM-5` recuou para a forma que os parsers leem, com a tarefa nova `LM-T4a` ensinando-lhes a de três campos, `DM-13`. A `LM-T1` fechou `done`, aprovada 100%, e a rodada `RP-5` — a primeira conduzida pelo `pantonic-consultant` — absorveu o `AE-8` e o `AE-7` com `DM-15`/`DM-16` e os cards `LM-T1a` e `LM-T7`; o plano passa a 9 tarefas) · **Iniciativa:** `EXECUCAO-AUTONOMA` · **Prefixo das
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
  **Medida no ato (`DM-24` aplicada a permissão, não a comando):** varridos os dois
  `settings.json` em 2026-09-19, **nenhuma regra `Edit`/`Write` sobre `.claude/agents/**` existe**
  — o global tem apenas `Read(.../.claude/agents/**)`. A concessão é do dono e vale; o que **não**
  está medido é a **superfície** onde ela mora. Antes de despachar a `LM-T8`, confirmar que a
  regra está em `settings.json`, sob pena de reproduzir o `AE-11` — impedimento de permissão
  descoberto pelo executor, no meio da tarefa, que nenhum agente da sessão pode suprir.

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

- **Status:** `ready` — card novo do `ESC-3` (`DM-20`), residência do item (c) da `LM-T2` antiga e
  do `AE-3`.
- **Esforço:** low
- **Objetivo:** um só — o número que o hook grava passa a ser o mesmo que a notificação mede. Hoje
  ele grava **sempre para mais**, com `fonte=usage`, e a série só não está corrompida porque o loop
  corrigiu cinco linhas à mão nesta janela.
- **Depende de:** `DM-20` (a fórmula, **calibrada** no `ESC-3`). Nenhuma tarefa anterior.
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
- **Produto do módulo:** (a) `calcular_consumo` passa a devolver, em `tokens_k`, o total de `usage`
  da **última** entrada `assistant` que tiver `usage`, em vez da soma por `message.id`; (b)
  `montar_args_append` passa a normalizar o `modelo` para **minúsculas** (`str(...).strip().lower()`),
  que é a convenção da série; (c) o docstring do módulo (`:10`) e o de `calcular_consumo` passam a
  enunciar a fórmula nova e a razão medida, substituindo a nota de dedupe por `message.id`.
- **Testes** (quatro, com a regra concorrente de cada):
  - `TF-consumo-usa-a-ultima-mensagem` — transcript sintético com três entradas `assistant` de
    `message.id` distintos e `usage` crescente (ex.: totais 10k, 30k, 60k): `calcular_consumo`
    devolve `60.0`. *Concorrente:* o código de hoje devolve `100.0` — é a diferença que a tabela de
    calibração mediu em escala real.
  - `TR-consumo-uma-mensagem-so-nao-muda` — transcript com **duas entradas da mesma mensagem**
    (mesmo `message.id`, mesmo `usage`), o caso da calibração histórica do `T55`: continua
    devolvendo o valor de uma (não o dobro). *Concorrente:* somar por entrada dobrava — o defeito
    que a dedupe corrigiu e que a fórmula nova não pode reintroduzir.
  - `TR-tool-uses-e-duracao-intocados` — no mesmo transcript do primeiro teste, `tool_uses` conta
    todos os blocos `tool_use` de todas as entradas e a duração segue vindo do primeiro e do último
    `timestamp`. *Concorrente:* aplicar "só a última mensagem" também a `tool_uses` derrubaria a
    contagem, que hoje está **certa** (medido: 4, 13, 17, 20, 25 e 30 batem com a notificação).
  - `TF-modelo-minusculo-no-append` — `montar_args_append` com `modelo="Sonnet"` devolve
    `--modelo sonnet`. *Concorrente:* hoje devolve `Sonnet`, e a série fica com duas grafias do
    mesmo modelo (`AE-3`).
- **Verificação:** (baseline medida no `ESC-3` — `DM-12`)
  1. `python -m pytest tests/test_telemetria_hook.py -q` → verde, com **quatro testes a mais**
     que o total re-medido no despacho (`DM-23`). Referência histórica, não aceite: `6 passed`
     em 2026-09-18 — este arquivo não foi tocado por nenhuma tarefa fechada depois disso.
  2. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o
     total que a árvore tiver **no despacho**, re-medido por quem despacha; esta entrega soma os
     quatro testes novos e **não reduz** esse total. Referência histórica: `165 passed` em
     2026-09-19.
  3. `pwsh -NoProfile -Command "(Select-String -Path .claude/tools/telemetria_hook.py -Pattern 'cache_read_input_tokens' | Measure-Object).Count"`
     → ≥ 2 (o campo continua sendo somado **dentro** da última mensagem; o que muda é o escopo da
     soma, não os campos). **Baseline re-medida no `ESC-6` com o comando publicado: 2**
     ocorrências — `telemetria_hook.py:11`, no docstring do módulo, e `:93`, em
     `calcular_consumo`. A baseline anterior deste item dizia **1**, porque foi tirada de um
     `grep` diferente do comando publicado, e não do comando publicado (`AE-19`, `DM-24`).
     Como o docstring é **alvo** da própria tarefa (produto (c)), o item vale como regressão do
     campo, não como contagem exata.
- **Restrições desta tarefa:** `tool_uses` e `duracao_s` ficam **como estão** — os dois foram
  conferidos contra a notificação e estão certos. `fonte=usage` continua sendo a fonte declarada: o
  número passa a ser o do `<usage>`, que é o que essa palavra sempre afirmou. Nenhuma mudança em
  `telemetria.py` (o contrato de erro dele é da `LM-T1a`, fechada).
- **Não fazer:** não tentar cobrir o caso do subagente **retomado por `SendMessage`** — medido no
  `ESC-3`: o evento `SubagentStop` **não dispara** nessa retomada, e nenhuma linha de código do kit
  alcança isso; a compensação é a linha do Passo 9 que a `LM-T2` publica (o loop apende à mão). Não
  tocar `docs/telemetria.tsv` (a série é dado, não alvo de tarefa); não tocar
  `.claude/skills/scrum-master/SKILL.md` (é a `LM-T2`); não commitar.
- **Contingências:**
  1. se a assinatura de `calcular_consumo` ou de `montar_args_append` não for a citada aqui → parar
     e sinalizar `blocked` razão `premissa`, citando a encontrada;
  2. se algum teste **pré-existente** de `tests/test_telemetria_hook.py` afirmar a soma por
     `message.id` como resultado esperado → ajustar **só** a asserção desse teste, mantendo o caso, e
     devolver `contingência 2 acionada: <teste> ajustado para a fórmula da última mensagem`.
- **Pronto quando:** `calcular_consumo` devolve o `usage` da última mensagem; o modelo sai
  minúsculo; os quatro testes existem; os docstrings enunciam a fórmula nova com a razão medida; e
  as três linhas de `Verificação` saem como escritas.

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

- **Status:** `ready` — card novo do `ESC-8` (2026-09-19), residência única do `AE-20`. A `LM-T2c`
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

- **Status:** `ready` — card do `ESC-4` (`AE-15`), **ampliado pelo `ESC-5`** com o `AE-17`. As duas
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

- **Status:** `ready`
- **Esforço:** high
- **Objetivo:** a doutrina da unidade de trabalho, num ato só. Absorve `AUT-T2` (`DP-I`, o artefato
  `tarefa`), `AUT-T6` (skill única de passagem de bastão), `AUT-T7` (superfícies que apontavam
  para a skill aposentada) e `AUT-T8` (status × veredito).
- **Arquivos-alvo:** `GOVERNANCA.md` (§3 e §7) · `.claude/skills/scrum-master/SKILL.md` ·
  `.claude/skills/proximo-passo/SKILL.md` · `.claude/skills/handover/SKILL.md` ·
  `docs/DOC_MAP.md`
- **Retirado dos alvos pelo `ESC-1` (`DM-17` (v)):** `.claude/agents/pantonic-planner.md`. A
  edição de arquivo de agente é negada pela camada de permissão do harness (`AE-11`); a
  publicação da gramática nele é o item (b) da `LM-T8`, **depois** desta tarefa. Nada se perde na
  varredura: medido na `ESC-1`, o arquivo não contém a régua antiga.
- **Produto do módulo:** (a) `DM-2`, `DM-3`, `DM-4` e `DM-5` publicados na doutrina, com a gramática de
  cabeçalho de três campos — **copiada do card da `LM-T4a`, que é a residência única do literal
  neste plano** e a única já implementada nos parsers — e o teto de write-clusters reinterpretado
  como limite de **tema**;
  (b) o gate de delegação do `proximo-passo` (item 5) reescrito para a régua nova; (c) a decisão
  registrada sobre `proximo-passo`/`handover`: o que permanece, o que migra para o
  `scrum-master` e o que é aposentado, com as superfícies que as citam atualizadas no mesmo ato.
- **Coerência do módulo (aceite de `DM-3`):** nenhuma das seis superfícies fica citando a régua
  antiga — a varredura de citação é parte da entrega, não tarefa posterior.
- **Verificação:** (corrigida pela `RP-2`, `DM-12`; toda saída abaixo é **medida**, nenhuma é
  deduzida)
  1. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"`
     → exit 0. **Correção da `RP-5`:** o exit 0 citado aqui vinha do dossiê da `BKL-T4` e
     **envelheceu** — re-medido em 2026-09-18 pela `RP-5`, o comando sai **exit 1** com 6
     problemas (`.claude/README.md` diverge do regenerado, por atos do dono fora de ciclo:
     descrições de `DM-8` e criação do `pantonic-consultant`). Quem recoloca o exit 0 é a
     `LM-T7`, que regenera a projeção; por isso esta tarefa passa a depender dela. O aceite
     **não** é removido: ele é satisfazível assim que a `LM-T7` fecha.
  2. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o
     total que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa não
     acrescenta teste e **não pode reduzir** esse total — a suíte de conformance é o que tranca
     doutrina. Referência histórica, não aceite: `165 passed` em 2026-09-19 (`ESC-5`).
  3. Varredura da régua antiga, com o literal exato:
     `Select-String -Path GOVERNANCA.md,.claude/skills/proximo-passo/SKILL.md,.claude/skills/scrum-master/SKILL.md,.claude/skills/handover/SKILL.md,.claude/agents/pantonic-planner.md,docs/DOC_MAP.md -Pattern '>8 write-clusters' -SimpleMatch`
     → **nenhuma linha**. Baseline medida hoje, antes da entrega: **uma** ocorrência,
     `.claude/skills/proximo-passo/SKILL.md:126` (`**>8 write-clusters → dividir em sub-tarefas
     ANTES de delegar.**`). A verificação discrimina o mundo com a mudança do mundo sem ela.
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
  a gramática de cabeçalho copiada do card da `LM-T4a`; o item 5 do gate de delegação em
  `.claude/skills/proximo-passo/SKILL.md` está reescrito na régua nova; a decisão sobre
  `proximo-passo`/`handover` está registrada e as **cinco** superfícies dos `Arquivos-alvo` não
  citam mais a régua antiga; e as três verificações acima passam como escritas. (A sexta
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

### LM-T5 — Revisão da criação das tarefas [Opus · classe investigacao]

- **Status:** `ready`
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
  **Décima primeira classe, do `ESC-8`:** regra de roteamento que **não parte o domínio** —
  a `A8a` cobriu `escalar` para entrega aprovada e deixou dois pares sem regra útil, um deles
  mandando fazer o que o instrumento recusa (`AE-20`). A rubrica afere: **regra nova de tabela
  declara o efeito sobre cada valor do domínio que toca, e confronta a ação com o domínio que o
  instrumento de fechamento aceita**.
- **Segundo entregável — o reagrupamento do `P-0739` (`DM-9`).** Julgar os 6 cards `ready`
  restantes (`BKL-T5`..`BKL-T9`, mais o que a rodada do `AE-10` exigir) **não basta**: eles foram
  autorados sob a régua atômica e não se executam um a um sem reproduzir o defeito que este plano
  corrige. Esta tarefa **reescreve os 6 como módulos coesos** sob a gramática de `DM-2`..`DM-5`,
  na própria `docs/plans/P-0739-backlog-instrumento.md`, e **absorve a rodada de replanejamento do
  `AE-10`** (dependência de ordem entre `transacionar_status` e os marcadores
  `<!-- fila:gerada -->` que a `BKL-T6` item (a) insere): a ordem passa a ser fixada no
  reagrupamento, não numa rodada separada. Saída: o `P-0739` com uma fila nova, de módulos, pronta
  para fechar **numa rodada única**.
- **Pronto quando:** a seção nova em `docs/RUBRICA_DE_REVISAO.md` ≤ 50 linhas; os **15** cards
  julgados numa tabela — os **9** deste plano que não são a própria auditoria nem o piloto
  (`LM-T1`, `LM-T1a`, `LM-T2`, `LM-T2a`, `LM-T2b`, `LM-T2c`, `LM-T3`, `LM-T3a`, `LM-T4a`,
  `LM-T4`, `LM-T7`, `LM-T7a`, `LM-T8` — **13**) e os 6 do `P-0739`, **19** no total (contagem
  atualizada pelo `ESC-7`, 2026-09-19); todo card reprovado sai com o defeito nomeado e a rota; e os 6 cards
  `ready` do `P-0739` reescritos como módulos, com cabeçalho de três campos, aceite de coerência
  declarado e a dependência de ordem do `AE-10` resolvida na fila — `AE-10` fechado no mesmo ato.
- **Verificação:** tarefa sem artefato executável — a verificação é por efeito nos arquivos-alvo.
  (1) Abrir `docs/RUBRICA_DE_REVISAO.md` e contar a seção nova: `(Get-Content
  docs/RUBRICA_DE_REVISAO.md).Count` antes e depois da edição; a diferença é ≤ 50.
  (2) `Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'LM-T' -SimpleMatch` → ao menos
  **19** linhas, uma por ID julgado. **Medido no `ESC-6`: 0** hoje — o arquivo não cita nenhum
  `LM-T`, então o item discrimina.
  (3) `Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '- **Objetivo:**'
  -SimpleMatch` → o total **sobe em 6** sobre o valor re-medido no despacho (`DM-23`: relação,
  não constante). **Medido no `ESC-6`: 18** ocorrências **antes** da entrega — o campo já existe
  nos cards antigos do plano, de modo que "os 6 cards aparecem com o campo" **já era verdade**
  antes de a tarefa começar (`AE-4`/`DM-24` (iii)); o que discrimina é o **delta**. O
  `-SimpleMatch` é obrigatório: medido no `ESC-6`, sem ele o comando **nem executa**
  (`Invalid pattern '- **Objetivo:**' ... Nested quantifier '*'`).
- **Depende de:** `LM-T4` (a gramática que a rubrica afere e que o reagrupamento aplica nasce lá).

### LM-T6 — Piloto medido do loop e o veredito do dono [Opus + dono · classe investigacao]

- **Status:** `ready`
- **Esforço:** high
- **Objetivo:** a **rodada única** que encerra o `P-0739` com o `scrum-master` já corrigido, e que ao
  mesmo tempo é a medida do loop. Absorve `AUT-T9` (conformidade) e `AUT-T10` (`README`,
  `CHANGELOG`, veredito).
- **Entregável:** um run do loop sobre a fila de **módulos** que a `LM-T5` deixou no `P-0739`,
  conduzido até o plano fechar ou até uma regra de parada casar. Mais a série de consumo por
  módulo, a regra que encerrou a janela e o número de módulos fechados **por janela** — a medida
  que responde se o objetivo de 2026-08-22 foi atingido. Mais `README.md` e `CHANGELOG.md`
  atualizados e o veredito do dono.
- **Pronto quando:** o `P-0739` fecha `done` (16/16 + o que o reagrupamento tiver mudado no
  total), **ou** o registro medido da regra que impediu, com o fato que a disparou — desfecho
  negativo é desfecho. Em qualquer dos dois casos, a série de consumo por módulo é comparável com
  a linha medida da `BKL-T4` (284,6k tk / 71 tool uses / 21 min por tarefa atômica), que é a
  baseline contra a qual o ganho do módulo coeso se afere.
- **Verificação:** tarefa sem artefato executável — a verificação é por efeito nos arquivos do run.
  (1) Abrir `docs/plans/P-0739-backlog-instrumento.md` e ler o estado do plano no cabeçalho: `done`,
  ou a regra de parada registrada em `## Achados da execução` com o fato que a disparou.
  (2) Abrir `docs/telemetria.tsv` e confirmar uma linha por módulo fechado no run, com o consumo
  medido — é a série que se compara à baseline de 284,6k tk da `BKL-T4`.
  (3) `README.md` e `CHANGELOG.md` atualizados, e o veredito do dono registrado no plano.
- **Depende de:** `LM-T1`, `LM-T2`, `LM-T3`, `LM-T4`, `LM-T5`.

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

### LM-T8 — A concessão de `Bash` ao `pantonic-planner` e a publicação na definição dele [Opus + dono · classe mecanica]

- **Status:** `ready` — **permissão liberada pelo dono em 2026-09-19** (`DM-27`). A razão do
  `blocked` era **ato do dono**, não premissa de plano, e o ato foi feito: `.claude/agents/` deixa
  de ser superfície vedada ao loop. O conteúdo já estava fechado e transcrito abaixo, e não se
  reabre. O item (a) é despachável desde já; o item (b) segue exigindo a `LM-T4` fechada.
- **Esforço:** low
- **Objetivo:** materializar a decisão do dono (`DM-16`) na única superfície onde ela mora — o
  arquivo de definição do `pantonic-planner` — e, depois da `LM-T4`, publicar ali a gramática que a
  doutrina tiver fixado. Um tema só: **a definição de agente**.
- **Depende de:** nada, para o item (a) — a permissão que era a dependência foi concedida em
  2026-09-19 (`DM-27`). O item (b) depende da `LM-T4` fechada.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
  - `CHANGELOG.md`
- **Produto do módulo:** (a) o frontmatter do `pantonic-planner` com `Bash` e o fato estável
  correspondente no corpo; (b) **depois da `LM-T4`**, a gramática de cabeçalho e a régua de tema
  publicadas nos dois pontos do mesmo arquivo que as enunciam hoje na forma antiga — o bullet de
  `## Fatos estáveis (não redescobrir)` que transcreve `### <ID> — <título> [<modelo> · classe
  <classe>]` e o esqueleto de `## Anatomia do card`, **mais** o critério de autoria da `DM-18`
  (item enumerado e a frase que o conta fecham no mesmo card; verificação que não discrimina o
  invariante não é aceite), o da `DM-21` (exigência estrutural vira caso discriminante, inspeção
  mecânica ou `Restrição` — nunca teste comportamental), o da `DM-22` (guarda de borda com
  residência única; verbo novo herda a borda do instrumento), o da `DM-23` (piso de regressão é
  relação re-medida no despacho, nunca constante) e o da `DM-24` (o literal do comando é o que
  foi colado e rodado; os dois valores publicados; bloco cercado e `-SimpleMatch`), na fase 4 do
  protocolo; (c) uma linha em `CHANGELOG.md` sob
  `## [Não lançado]`.
- **Textos literais do item (a)** (transcrição, não autoria — é o que torna o ato do dono barato):
  1. Linha 5 de `.claude/agents/pantonic-planner.md` (medida na `RP-5` e re-derivada na `ESC-1`:
     `tools: Read, Glob, Grep, Write, Edit`) passa a ser:
     ```
     tools: Read, Glob, Grep, Write, Edit, Bash
     ```
  2. Último bullet da lista da seção `## Fatos estáveis (não redescobrir)`:
     ```
     - Ferramenta de execução: você **tem** `Bash` (decisão do dono, 2026-09-18 — planner e
       executor acessam a mesma ferramenta de validação). Comando de aceite que você escreve num
       card **se roda antes de publicar**, e o literal esperado é a saída **medida**, nunca a
       deduzida da ferramenta: `Verificação` publicada sem execução é defeito de autoria.
     ```
  3. Em `CHANGELOG.md`, sob `## [Não lançado]`:
     ```
     - `pantonic-planner` ganha `Bash` no toolset (decisão do dono, 2026-09-18): planner e executor
       passam a acessar a mesma ferramenta de validação, e o dever "comando de aceite não se deduz,
       se roda" deixa de ser inexequível pelo papel a que se dirige.
     ```
- **Verificação:** (a linha 1 é a única que muda de valor com esta tarefa; as duas outras já foram
  medidas e são regressão)
  1. `pwsh -NoProfile -Command "Select-String -Path .claude/agents/pantonic-planner.md -Pattern '^tools:'"`
     → uma linha, `tools: Read, Glob, Grep, Write, Edit, Bash`. **Antes (medido na `RP-5` e
     confirmado no despacho bloqueado da `ESC-1`):**
     `.claude/agents/pantonic-planner.md:5:tools: Read, Glob, Grep, Write, Edit`.
  2. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode validate | Out-Null; exit $LASTEXITCODE"`
     → exit 0 (medido antes: exit 0 — a edição de frontmatter não pode derrubá-lo).
  3. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"`
     → exit 0. Pressupõe a `LM-T7` fechada; a `description` do planner **não** muda aqui, então o
     drift não reabre.
- **Não fazer:** não alterar `description` nem `model` de agente nenhum; não tocar
  `.claude/agents/pantonic-executor.md` nem `.claude/agents/pantonic-reviewer.md` (publicados por
  `DM-8`) nem `.claude/agents/pantonic-consultant.md` (figura provisória do dono); não regenerar
  `.claude/README.md` aqui (é a `LM-T7`, e a `description` intocada não o afeta).
- **Pronto quando:** o `tools:` do planner declara `Bash`; o fato estável do texto 2 está no corpo;
  o `CHANGELOG.md` traz a linha; e — quando o item (b) for executável — a definição do planner não
  enuncia mais a gramática de cabeçalho na forma que a `LM-T4` aposentou.
- **Enquanto o item (a) desta tarefa não fechar** vale a regra de intervalo da `DM-17` (iv) — o
  intervalo encurtou com a `DM-27`, mas não acabou: a concessão é de permissão ao loop, e o
  `tools:` do planner só declara `Bash` depois que o item (a) rodar. Até lá: o dever da
  `DM-12` é de quem publica **com** ferramenta — `pantonic-consultant` ou `scrum-master`, que roda
  o comando no despacho e anexa a saída medida. Card autorado por planner com `Verificação` não
  medida não se despacha como está.

### LM-T9 — `consultant-spec`: a figura ad-hoc vira especificação [Opus · classe redacao]

- **Status:** `ready`
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
- **Entregável:** `docs/consultant-spec.md` respondendo, com o insumo medido ao lado de cada
  resposta: (a) **gatilho** — o que aciona o consultor e o que não aciona; (b) **domínio de
  decisão** — o que ele fecha sozinho (técnico/tático) e o que sobe ao dono (estratégico,
  `G-NOASK`); (c) **fronteira com o `pantonic-planner`** — ele autorou cards novos nesta janela, e
  o documento tem de dizer se isso é da figura ou empréstimo; (d) **instrumento** — por que nasce
  com `Bash` (`DM-12`, `DM-24`); (e) **custo e teto** — 68,5% da janela num papel só é o número
  que a spec precisa endereçar, com a regra de quando **não** acionar; (f) **encerramento** — como
  a figura termina (decisão de janela × poluição, Regra 2).
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
- **Pronto quando:** `docs/consultant-spec.md` existe, cobre as seis perguntas (a)..(f), cada uma
  com pelo menos um identificador de lastro, está indexado no `docs/DOC_MAP.md` e tem linha no
  `CHANGELOG.md`.
- **Verificação:** (os três comandos foram extraídos deste card e rodados verbatim na autoria,
  2026-09-19 — `DM-24`; os valores `antes` estão ao lado e o card não fixa piso numérico, `DM-23`)
  ```
  pwsh -NoProfile -Command "[int](Test-Path docs/consultant-spec.md)"
  ```
  → `0` antes; **`1`** depois.
  ```
  pwsh -NoProfile -Command "(Select-String -Path docs/DOC_MAP.md -Pattern 'consultant-spec' -SimpleMatch | Measure-Object).Count"
  ```
  → `0` antes; **≥1** depois.
  ```
  pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0740-loop-de-modulos.md -Pattern '^- \*\*.I-\d' | Measure-Object).Count"
  ```
  → mede quantos insumos `I-<n>` existem em `## 9` no momento do despacho (valor na autoria,
  2026-09-19: **8**). A relação de aceite, re-medida no despacho (`DM-23`): a contagem de
  identificadores `I-` citados em `docs/consultant-spec.md` é **≥** a contagem medida aqui.
  *Nota de autoria, `DM-24`:* a primeira forma deste comando usava `-SimpleMatch` com o padrão
  `- **I-` e devolveu **1** — casou a própria linha em que estava publicada e **nenhum** dos oito
  insumos, porque o identificador vem entre crases. Mesma classe do `AE-19`, pega antes do
  despacho por ter sido rodada. A forma acima é ancorada em início de linha, o que exclui a
  publicação, e foi medida em **8**.

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
