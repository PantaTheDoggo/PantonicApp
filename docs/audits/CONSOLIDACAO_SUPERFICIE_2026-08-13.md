# Consolidação da superfície de contato — `G-SURFACE`, 2026-08-13

Relatório da consolidação encomendada pela `DP-P` (§20 do `P-0734`), aplicando a régua publicada pela
`T46` (guardrail 16, `G-SURFACE`). Três blocos:

- **Universo 1 — o plano `P-0734`**: `T47`, abaixo. **Concluído.**
- **Universo 2 — os artefatos publicados do framework**: `T48`, seção no meio. **Concluído.**
- **Bloco 3 — a superfície do `DP-Q`**: `T49`, `T50`, `T51a` e `T51b`, seção no fim. É a **segunda
  aplicação do `G-SURFACE`**, disparada pela decisão que resolveu as duas ocorrências de classe (c)
  que o universo 1 fez subir. **Concluído.**

Régua de classificação, idêntica nos dois universos:

- **(a) história** — narra o que aconteceu à época. **Não se toca.**
- **(b) texto vigente que contradiz o entendimento atual** — enunciado normativo, dossiê de tarefa
  ainda não executada, mitigação de risco, cláusula de aceitação. **Regulariza no ato.**
- **(c) contradição que só o dono resolve** — duas leituras defensáveis do objetivo, do requisito ou
  do caso de uso. **Para, registra e sobe** (`G-SCOPE`, `G-EXECREADY`).

Consolidar é tornar legível o que foi decidido, nunca decidir de novo. Nenhuma decisão ratificada
mudou de conteúdo: onde um dossiê ficou derrubado por rodada posterior, ele recebeu **marca de
revogação** no próprio topo, com o corpo intocado.

---

## Universo 1 — `docs/plans/P-0734-execucao-autonoma.md`

**Método.** Sonda programática sobre o arquivo (3 928 linhas, 7 rodadas de replanejamento empilhadas
nos §9 a §20), emitindo (i) o mapa de seções com faixas de linha e (ii) o índice de todos os
`DP-*`/`DA-*`/`DE-*` e dos 48 cards `T<n>` com o estado declarado de cada um; leitura dirigida só das
faixas que a sonda apontou como conflitantes. Nenhuma âncora herdada foi reutilizada — todas
re-derivadas.

**Recorte de vigência aplicado.** Dossiê de tarefa **já executada** narra o que foi encomendado à
época: é (a). Só entrou em (b) o dossiê de tarefa **ainda não executada** (`T12`..`T17`, `T26`,
`T27`, `T29`, `T30`, `T48`), o texto normativo dos §1 a §3, as mitigações do §6, o §7, o §8, a
cláusula de aceitação do §19 e os dossiês de decisão do bloco `## Dossiês fechados por decisão`, que
o plano consome como registro normativo vivo (a `T29`, por exemplo, os declara leitura obrigatória).

**Resultado: 17 ocorrências classificadas — 9 em (a), 6 em (b), 2 em (c).**

### Classe (b) — regularizadas no ato (6)

| # | âncora | o que contradizia | o que foi feito |
|---|---|---|---|
| b1 | §6, tabela de riscos, linha *"O dono perder consciência situacional ao sumir o round-trip por tarefa"* | Mitigação **viva** prometendo que a `T16` "mede quantos round-trips de fato desapareceram" — contagem como controle, derrubada pelo §19 reescrito na `T45`. Descreve o que uma tarefa **ainda não executada** vai fazer, logo não é história. É o `TK-40` | Mitigação reescrita para se apoiar no **registro qualitativo por ocorrência**, classificado pela causa (§19), mantendo o RDO como instrumento compensatório (`DA-5`). Nenhuma contagem reintroduzida; declarado que a cegueira aparece como acionamento legítimo que deixou de acontecer, não como número |
| b2 | `### DP-A` — *Transporte do pacote de retorno* (topo do dossiê) | O dossiê inteiro lia-se como vigente, sem marca nenhuma, embora a `DP-D` (`D2`, `D3`, `D4`) tenha apagado o objeto que ele transporta, a `DP-H` tenha realocado o `pacote` para dentro do laudo e a `DP-N` tenha reduzido o retorno do executor ao sinal. A revogação existia, mas só ~770 linhas adiante | **Marca de revogação parcial** inserida no topo, separando o que permanece normativo (princípio do transporte por arquivo, medição, proibição de prosa atravessar o orquestrador) do que caiu (o pacote de 8 campos, o RDO no início, o reviewer lendo pacote, a linha de confirmação), e nomeando os três blocos que passam a ser registro. **Corpo intocado** |
| b3 | `### DP-B` — *Política de autonomia, tetos e escalada* (topo do dossiê) | Mesmo defeito: a `DP-D` declara que revoga parte da `DP-B`, e o §10.3 diz cláusula a cláusula o que caiu, mas o dossiê não trazia marca. `A2` lê um pacote que não existe; o trio `entregue`/`parcial`/`bloqueado` do *"Domínio de entrada"*, de `A3` e de `A5` saiu do vocabulário de `status` | **Marca de revogação parcial** no topo, transcrevendo o veredito do §10.3 (os três tetos, a precedência do bloco A, o bloco B e a fronteira "obriga parada × segue com registro" permanecem) e apontando a tabela **vigente** em `.claude/skills/scrum-master/SKILL.md`, transcrita pela `T21b`. **Corpo intocado** |
| b4 | §9, cabeçalho de estado da `DP-D` | Declarava só "RATIFICADA pelo dono em 2026-08-10" — sem nenhum ponteiro para a revogação parcial que a `DP-E` lhe aplicou no dia seguinte. Ler o §9 isolado lê texto derrubado como vigente | Parágrafo de marca acrescentado logo abaixo do estado, apontando o §10.3 como a tabela cláusula a cláusula e registrando que a *Nota de derivação de 2026-08-11* deste mesmo §9 está revogada por inteiro |
| b5 | §9, `#### Nota de derivação de 2026-08-11 — status, A3 e o canal da pendência` | Bloco **revogado por inteiro** pela `DP-E` (§10.3 o diz explicitamente), mas sem marca alguma na própria âncora — o leitor que cai nele por Grep lê uma cadeia de derivações cuja premissa caiu no mesmo dia | **Marca de revogação total** no topo do bloco, com ponteiro para o §10.3, declarando que nada ali é instrução vigente e que o bloco fica como registro da derivação. **Corpo intocado** |
| b6 | `### T27`, bullet *"Só marcador vivo migra"* | Dossiê de tarefa **ainda não executada** cujo invariante de preservação lista "dossiês de decisão (`DP-A`..`DP-F`)" — enumeração fechada que ficou para trás de sete rodadas: hoje existem dossiês até `DP-P`. Executada como está, a `T27` reescreveria como marcador vivo o que é registro | Enumeração trocada por **todo dossiê de decisão deste plano** (`DP-A` em diante, incluindo os das rodadas dos §9 a §20), com a ressalva declarada de que **marca de revogação não é reescrita** — onde a `T47` marcou, a marca fica e o corpo continua intocado |

### Classe (c) — sobem ao dono, não resolvidas aqui (2)

Ambas são a mesma família: a **`DP-B`, ratificada em 2026-08-08**, prescreve paradas do loop que o
**§19, enunciado pelo dono em 2026-08-13**, pode classificar como a ineficiência que o plano existe
para eliminar. As duas leituras são defensáveis, nenhuma é resíduo de texto morto, e desempatar é
decidir — não consolidar. Registradas sem tocar no texto de nenhum dos dois lados.

**c1 — Estouro de teto de tool uses: `A4` da `DP-B` × invariante 5 do §3 × §19.**
`A4` manda **PARAR** para replanejamento em todo estouro de teto declarado ("estouro é decomposição
errada"). O invariante 5 do §3 (regime interino, decisão do dono de 2026-08-11, prorrogada em
2026-08-12) diz que o teto é **alarme, nunca bloqueio**, e que o consumo se registra em vez de
interromper. E o §19 reprova acionamento do dono em caminho feliz — um estouro de teto sem pendência
aberta não é questão do dono. *Leitura 1:* `A4` continua íntegra, porque governa o **loop depois** da
entrega, não a entrega, e o invariante 5 só protege o executor. *Leitura 2:* `A4` é exatamente uma
parada de caminho natural, e o regime interino a esvaziou junto com o resto do porteiro por teto.
**Não é matéria deste plano decidir** — o desdobramento do §15/`T17` item 4 manda a matéria inteira de
uso e teto para plano próprio, e a `DP-L` não se forma aqui. Sobe como pergunta de rota, não como
edição.

**c2 — Fim de janela: `B2` da `DP-B` × §19.**
`B2` encerra a janela por teto (dez tarefas ou 900 k tokens) com relatório e **PARA** — "encerramento
normal, não falha". O §19 diz que o dono **inicia o plano e nada mais**, e que a skill se encarrega
sozinha de **criar os contextos novos**; parar para que o dono limpe o contexto e invoque a
continuação é o caso exemplar de ineficiência, e **uma só** ocorrência já é achado. *Leitura 1:* o
fim de janela devolve ao dono, e o §19 tolera isso como limite físico de capacidade (`DA-11`).
*Leitura 2:* o fim de janela é do `scrum-master`, que abre o contexto seguinte por conta própria, e
só o **fim do plano** volta ao dono. A escolha muda o que a `T16` mede e o que a `T17` aprova.

### Classe (a) — história, não tocada (9)

| # | âncora | por que é história |
|---|---|---|
| a1 | `DA-9`, §1 | Já marcada: *"REVOGADA em 2026-08-08 pelo dono; substituída pela `DA-11`"*. A régua já estava aplicada; nada a fazer |
| a2 | `### T34` (card cancelado por absorção, 2026-08-12) | Corpo preservado **de propósito** como material absorvido pelo plano seguinte (`T17` item 4). Preservação é a decisão, não o descuido |
| a3 | Snapshots de fila dentro de rodadas antigas (§10.4, §13.3/13.4, §15/§16.6) | Registram como a fila estava naquela rodada. A **única** fila viva é a do §5, que está correta e já sem a `T34` |
| a4 | §5, parágrafos narrativos das inserções e reordenações de fila (2026-08-11, 08-12, 08-13) | Narram por que cada bloco entrou onde entrou. A sequência bold no topo do §5 é a parte viva, e está consistente |
| a5 | §5, contagem de round-trips previstos ("três", "um quarto", "um quinto") | Narrativa de ratificações **já ocorridas**; a `T45` já a declarara fora do alvo pela mesma razão. Não é critério de aceitação por contagem |
| a6 | `## Achados da execução` (bloco inteiro) | Achados registrados no fechamento de cada tarefa, com data. Reescrever falsificaria o registro |
| a7 | Dossiês de tarefas já executadas que citam `pacote de retorno` ou vocabulário morto (`T10`, `T20`, `T21a`, `T21b`, `T31`, `T38`, `T39`, `T45`) | Descrevem o que foi encomendado à época, e o entregável correspondente já os quitou nos artefatos. O texto do card é o registro da encomenda |
| a8 | Contagens datadas de arquivos-alvo em `T26` e `T27` (*"contagem medida em 2026-08-11"*) | Medições declaradas com data, e a `T26` já traz a instrução de **remedir na entrada**. Não são afirmações de estado atual |
| a9 | `DP-C` — *Formato estruturado da tarefa no plano* | Vigente e não contradita: a `DP-H`, a `DP-K` e o dossiê da `T29` a declaram expressamente não revogada. Verificada e mantida sem marca |

### Verificação de fechamento — os quatro em exit 0

| comando | saída literal | exit |
|---|---|---|
| `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` | `kit_check: OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0').` | 0 |
| `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | `kit_check: check-drift OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s)).` | 0 |
| `pwsh -NoProfile -File .claude/checks/check-readme.ps1` | `check-readme: OK - 8 agente(s), 11 skill(s), 16 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.` | 0 |
| `python -m pytest` (raiz do hub) | `39 passed in 3.51s` | 0 |

**Invariantes conferidos.** Nenhuma decisão ratificada mudou de conteúdo — as quatro marcas de
revogação (b2, b3, b4, b5) são blocos novos acima de corpo intocado. Nenhum card foi cancelado ou
criado. As contagens do espelho não se moveram (16 guardrails, 14 seções) e o piso da suíte continua
em 39. O diff desta tarefa toca dois arquivos: o plano e este relatório.

---

## Universo 2 — artefatos publicados do framework

**Universo fechado:** `GOVERNANCA.md`; `README.md`; `.claude/` (agentes, skills, checks, geradores e
o índice do kit); `docs/DOC_MAP.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/CONSUMIDORES.md`,
`ARQUITETURA_PANTONICA.md`, `CHANGELOG.md`. Fora do alvo, declarado: `docs/DIARIO_HISTORICO.md`,
`docs/DIARIO_DE_OBRAS.md`, `docs/plans/` (universo 1), `docs/benchmark/`, as entradas de `CHANGELOG.md`
de versão já publicada e a matriz de responsabilidades do §3.

**Eixo.** Esta metade mede os artefatos contra os **objetivos, requisitos e casos de uso vigentes**
da iniciativa. Não é a varredura contra a matriz de responsabilidades: aquela é
`CONFORMIDADE_MATRIZ_2026-08-12.md`, eixo distinto, lido antes desta rodada para não repagar o que já
fora medido.

**Método.** Sonda programática sobre os 35 arquivos do universo (doze padrões: objeto morto *pacote de
retorno*, vocabulário de `status` derrubado, termos abolidos *revisor*/*inspetor*, `--observacoes`,
contagem de acionamento/round-trip como controle, ato de execução acoplado a diário/handover/consumo,
ciclo de vida do laudo, contagem de guardrails, prescrição de parada por teto) — 495 linhas brutas
indexadas por arquivo, seguidas de leitura dirigida só das faixas apontadas como conflitantes.

**Resultado: 28 ocorrências classificadas — 13 em (b), 3 em (c) (todas herdadas, nenhuma nova), 12 em
(a).** Duas medições fecharam em zero e valem como invariante conferido: **nenhuma** ocorrência de
*revisor*/*inspetor* no texto vivo (`DP-H`, termo único `reviewer`) e **nenhuma** de `--observacoes`
(`DP-M`).

### Classe (b) — regularizadas no ato (13 ocorrências em 6 arquivos)

| # | âncora | o que contradizia | o que foi feito |
|---|---|---|---|
| b1 | `CHANGELOG.md`, série das subidas de guardrail (logo após a entrada do `G-SCOPE`, *14 → 15*) | A série registrava a subida anterior e parava ali: o guardrail 16 (`G-SURFACE`), publicado hoje, não tinha entrada. Um changelog que omite a mudança canônica do dia é registro que mente por ausência | Entrada nova do `G-SURFACE` no lugar onde a série registra as subidas — enunciado do guardrail, espelho do `README.md` §10 subindo junto, *15 → 16*. **Sem bump de versão** (`DE-7`, congelamento em `0.0.0`) |
| b2 | `GOVERNANCA.md` §4.2, bullet *"Cada item de trabalho carrega um **status**"* | Reenunciava a lista **derrubada** — `backlog`, `in progress`, `in review` —, os três valores que a `DP-F` aposentou. A doutrina, que é a fonte, contradizia a residência única declarada na skill `diario-de-obras` | Bullet reescrito para **apontar** a residência única (skill `diario-de-obras`, seção "Status — residência única"), com a lista, a máquina de transições e o alcance por objeto, e a proibição explícita de qualquer artefato reenunciar a lista |
| b3 | `GOVERNANCA.md` §4.2, heurística da diretiva de priorização | *"destravar `blocked` → concluir `in progress`"* — grafia morta do mesmo par da `DP-F` | `in-progress` |
| b4 | `GOVERNANCA.md` §7 item 8 (`G-DEADCODE`), cláusula *Enforcement* | *"o handover declara os chamadores de produção de cada símbolo novo"* — pendura o enforcement num ato que a `DP-N` tirou da execução: quem executa sinaliza e nada mais, e não invoca `handover` | *"a revisão de fechamento **confere** os chamadores de produção de cada símbolo novo e rejeita módulo novo sem chamador não-teste"* — o gate migra para onde o entendimento vigente o põe, sem mudar o que a regra exige |
| b5 | `GOVERNANCA.md` §7 item 9 (`G-PLANFIDELITY`), cláusula *Enforcement* | *"o handover cita a rota do plano e confirma que nenhuma bifurcação…"* — mesmo defeito, mesmo ato morto | *"a revisão confronta a entrega com a rota do dossiê e confirma que nenhuma bifurcação arquitetural ocorreu sem decision record"* |
| b6 | `README.md` §10, linha 8 do espelho | *"**gate de review** no handover"* — espelho fiel de uma fonte que acabou de ser regularizada (b4) | *"**gate de review** no fechamento da tarefa"* |
| b7 | `README.md` §10, linha 9 do espelho | *"o handover confirma que não houve bifurcação sem decision record"* (espelho de b5) | *"a revisão confirma que não houve bifurcação sem decision record"* |
| b8 | `README.md` §11, parágrafo *"O ciclo típico, ponta a ponta"* | Publicava o ciclo **derrubado**: *"o handover fecha; **o gerente limpa o contexto e invoca a próxima**"* — o executor fechando por handover (`DP-N`) e o dono mediando execução normal, que o §19 declara defeito de entrega em ocorrência única | Ciclo reescrito na forma vigente: o executor implementa, o gate de guardrails verifica e a execução **devolve o sinal**; a revisão julga a entrega, e quem orquestra materializa o status, registra a tarefa e **abre o contexto seguinte** |
| b9 | `.claude/README.md`, seção *Ciclo típico* (prosa fora da região gerada) | Mesmo ciclo derrubado, na porta de entrada do kit: *"executor → `guardrails-check` → `handover` → usuário limpa contexto e invoca a próxima"*. É o primeiro texto que um consumidor lê ao adotar o kit | *"executor → `guardrails-check` → sinal de retorno → `pantonic-reviewer` → quem orquestra materializa o status, registra a tarefa e abre o contexto seguinte"*. Região não gerada, preservada pelo `-Mode generate`; `check-drift` conferido em exit 0 |
| b10 | `.claude/skills/scrum-master/SKILL.md`, *"O que obriga parada e o que segue com registro"*, bullet *Segue com registro* | *"a rota é escrita **pela execução** no RDO"* — atribui à execução escrever no registro canônico, contra a `DP-G`/`DP-N` (o executor devolve o achado como **uma linha do sinal**) e contra a `DP-H` (o RDO é escrito por quem fecha) | *"a rota chega pelo laudo, ou pela linha de achado do sinal do executor, e é transcrita no RDO por quem fecha a tarefa; o loop só verifica que existe"* |
| b11–b13 | `.claude/tools/review_evidence.py` — docstring do módulo, docstring de `confrontar_escopo` e a string do veredito mecânico na saída | Três menções vivas ao **objeto morto** *pacote de retorno* (`DP-A` revogada; `DP-H`/`DP-N`: o `pacote` existe **dentro do laudo** e não é objeto devolvido pela execução). Uma delas é impressa no documento que o `reviewer` lê, propagando o objeto morto a cada revisão | *"declaração de desvio **na entrega**"* nos três pontos. Mudança textual, comportamento intocado — a faixa `parcial` continua sem resolver sozinha, e os 10 testes do gerador seguem verdes |

### Classe (c) — nenhuma nova; três herdadas, já escaladas ao dono

Esta varredura **não abriu** contradição nova de dono. As três que cruzou já estavam registradas e
escaladas, e o texto de nenhuma delas foi tocado — decidir aqui seria exatamente o que o
`G-EXECREADY` proíbe:

- **`A4` e `B2` de `.claude/skills/scrum-master/SKILL.md`** — as duas entradas de classe (c) do
  universo 1 (`c1` e `c2` acima) se materializam nestas linhas da tabela de roteamento: estouro de
  teto que manda **PARAR** para replanejamento, e fim de janela por teto que encerra e devolve ao
  dono. Confrontadas com o invariante 5 do §3 do plano (teto é alarme, nunca bloqueio) e com o §19
  (acionamento em caminho feliz é defeito; a skill cria os contextos novos sozinha). **Remissão a
  `c1`/`c2`** — nenhuma edição.
- **Checkpoint intermediário escrito pela execução** — `GOVERNANCA.md` §4.3 (*"o executor grava um
  checkpoint intermediário"*), espelhado em `README.md` §9 e prescrito em
  `.claude/skills/handover/SKILL.md`. Contradiz a `DP-N` pela mesma raiz que a matriz já apontara:
  o ato é real e necessário, mas o domínio fechado do sinal não o carrega. É a lacuna `#27`/`#46` de
  `CONFORMIDADE_MATRIZ_2026-08-12.md`, **já no dono**; a correção nasce na fonte (§4.3) e desce.
  Nenhuma edição.

### Classe (a) — conferidas e não tocadas (12)

| # | âncora | por que não se toca |
|---|---|---|
| a1 | `CHANGELOG.md`, seções `1.0.0`..`2.0.0` | Versões já publicadas, correspondentes a tags existentes. História declarada pelo próprio cabeçalho do arquivo |
| a2 | `CHANGELOG.md`, entradas do `[Não lançado]` que narram rodadas anteriores (vocabulário de `status`, tabela de tetos, remoção de perfil, *15 → 14* do MVVM) | Narram o que aconteceu à época e continuam verdadeiras como registro. A única lacuna era a **ausência** da subida seguinte, quitada em b1 |
| a3 | `GOVERNANCA.md` §7.1, registro das rodadas de revisão de guardrails (*"14 guardrails avaliadas"*, *"14 guardrails em §7"*) | Contagens **datadas** de rodadas ocorridas, não afirmação de estado atual |
| a4 | `GOVERNANCA.md` §4.3, *"Acionamento do dono — a causa decide"* | Texto vigente **conforme**: classifica pela causa, declara o acionamento legítimo ilimitado e a ocorrência única em caminho feliz como defeito. Régua, não objeto |
| a5 | `GOVERNANCA.md` §4.3, *"quem executa **sinaliza** o resultado (`review`, ou `blocked` com razão tipada)"* | Conforme `DP-G`/`DP-N`; já regularizado na rodada da matriz |
| a6 | `GOVERNANCA.md` §4.2, *"Fronteira de registro — três artefatos"* e a telemetria pela notificação | Conforme `DP-H`: diário, RDO e `telemetria.tsv` sem duplicação, consumo registrado por quem orquestra |
| a7 | `README.md` §7, espelho do vocabulário de `status` | Espelha a lista e **aponta** para a residência única, sem recopiar a máquina de transições — a forma que a `DP-F` prescreve |
| a8 | `ARQUITETURA_PANTONICA.md` (arquivo) | Nenhuma ocorrência do vocabulário da iniciativa: "pacote" ali é pacote instalável Python e "entregue" é ato de porta de software. Fora do alcance desta régua |
| a9 | `docs/CONSUMIDORES.md`, `docs/RESIDENCIA_DOUTRINA.md` | O primeiro é registro de sync por máquina; o segundo, classificação **datada** das regras do `CLAUDE.md` global. Nenhum enuncia objetivo da iniciativa |
| a10 | `.claude/agents/pantonic-executor.md` e `.claude/agents/pantonic-reviewer.md` | Conformes: o executor sinaliza `review`/`blocked` com razão tipada e encerra; o reviewer emite o laudo pelo gerador, com o `pacote` **dentro** do laudo e o laudo declarado consumido e descartado |
| a11 | `.claude/skills/diario-de-obras/SKILL.md` (residência de `status`), `guardrails-check/SKILL.md`, `proximo-passo/SKILL.md` | Conformes: sete estados com alcance por objeto, `superseded` restrito a plano/iniciativa, autoria do executor limitada a `review`/`blocked`, gate obrigatório **antes de sinalizar `review`**, e o `handover` invocado por quem orquestra — nunca pela execução |
| a12 | `.claude/tools/rdo.py`, `rdo_template.md`, `.claude/checks/*` | O `pacote` do `rdo.py` é o do laudo (`DP-H`, cinco campos), o laudo é declarado efêmero, não há `--observacoes` (`DP-M`), e os checks não enunciam superfície da iniciativa |

### Achados fora de escopo (uma linha cada)

- `.claude/README.md`, nota dos auditores: *"apontamentos aceitos viram tíquetes no diário de obras
  via `pantonic-planner`"* — resíduo do **eixo da matriz** (a rodada de 2026-08-12 corrigiu os dois
  arquivos de agente e o índice do kit ficou para trás); fora desta régua, não editado.
- `docs/DOC_MAP.md` declara `GOVERNANCA.md` e `docs/plans/*.md` abaixo de 500 linhas (hoje 862 e
  3 928) e não indexa o `README.md` (939) — é o `TK-06`, já indexado, fora desta régua.
- `tests/test_review_evidence.py`, docstring de `test_escopo_violado_gera_fato_sem_inventar_parcial`,
  ainda cita *"pacote de retorno"*: `tests/` está fora do universo declarado desta varredura.

### Verificação de fechamento — os quatro em exit 0

| comando | saída literal | exit |
|---|---|---|
| `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` | `kit_check: OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0').` | 0 |
| `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | `kit_check: check-drift OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s)).` | 0 |
| `pwsh -NoProfile -File .claude/checks/check-readme.ps1` | `check-readme: OK - 8 agente(s), 11 skill(s), 16 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.` | 0 |
| `python -m pytest` (raiz do hub) | `39 passed in 8.18s` | 0 |

**Invariantes conferidos.** Nenhum guardrail nasceu ou saiu — o 16 é da `T46`, e a contagem fecha em
**16 × 16** com **14 seções** de fonte da verdade válida. Nenhum bump de versão (`0.0.0`, `DE-7`).
Nenhuma decisão ratificada mudou de conteúdo, e nenhuma contradição de dono foi decidida aqui. O
diff desta tarefa toca sete arquivos: `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`,
`.claude/README.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/review_evidence.py` e
este relatório.

**Fechamento da consolidação.** Os dois universos estão varridos contra a régua do `G-SURFACE`, o
relatório único cobre os dois, e o texto vigente do framework — doutrina, espelho, kit executável e
índices — descreve os mesmos objetivos que o plano consolidado enuncia. O que resta em aberto são as
três contradições de classe (c), todas no dono e todas registradas.

---

## Bloco 3 — a superfície do `DP-Q`: número arbitrário não governa fluxo

**Origem.** As duas ocorrências de classe (c) que o universo 1 fez subir (`TK-41`) foram decididas
pelo dono em 2026-08-13 (`DP-Q`, §21 do `P-0734`), e a decisão emitiu no mesmo ato os cards de
regularização — `T49` (a régua na doutrina), `T50` (a regra no loop) e `T51`, partida em `T51a`
(instrumento) e `T51b` (descrição). Este bloco registra a varredura das quatro.

**Régua de corte, em uma linha:** **medir e registrar consumo permanece; decidir por consumo sai.**
Onde o código ou o texto usava o número para reprovar, rotear, encerrar ou recusar, o poder cai;
onde ele informa, dimensiona ou alimenta a série, fica. **Nenhum número novo entra no lugar dos que
caem** — derivá-lo agora repetiria o defeito que a decisão nomeia. A classificação (a)/(b)/(c) é a
mesma dos dois universos acima.

**Universo fechado e declarado**, com a contagem bruta de `teto` medida em 2026-08-13:
`.claude/tools/rdo.py` (25), `.claude/tools/review_evidence.py` (21), `.claude/tools/rdo_template.md`
(1), `docs/RUBRICA_DE_REVISAO.md` (2), `.claude/skills/diario-de-obras/SKILL.md` (2),
`.claude/README.md`, `docs/RESIDENCIA_DOUTRINA.md` (3), `.claude/agents/pantonic-executor.md`,
`.claude/agents/pantonic-reviewer.md`, `tests/test_rdo.py` (3), `tests/test_review_evidence.py` (4),
mais `GOVERNANCA.md`, `README.md`, `.claude/skills/scrum-master/SKILL.md` e as âncoras do próprio
plano. **Fora do alvo, declarado:** `docs/telemetria.tsv` e a doutrina de telemetria do §4.2 — a
série é justamente o agregado que a decisão preserva —, `docs/DIARIO_DE_OBRAS.md`,
`docs/DIARIO_HISTORICO.md`, os RDOs já emitidos e as entradas de `CHANGELOG.md` de versão publicada.

**Resultado: 27 ocorrências classificadas — 18 em (b), nenhuma nova em (c), 9 em (a).** A contagem
bruta era ponto de partida, não alvo: a maioria das ocorrências de `teto` no universo é **medição
legítima** ou **limite de tamanho de campo**, e permanece.

### Classe (b) — regularizadas no ato (18 ocorrências)

| # | âncora | o que contradizia | o que foi feito | card |
|---|---|---|---|---|
| b1 | `GOVERNANCA.md` §3, bullet do orçamento de turnos por tarefa atômica | A tabela de tetos por classe operava como gate: o número decidia se a tarefa parava e se um ramo de roteamento se abria | Bullet reescrito como **referência informativa de dimensionamento, nunca gate** — "não recusam entrega, não roteiam e não encerram tarefa nem janela", e cruzar o número da classe é **alarme, nunca bloqueio**; o registro qualitativo ganha residência nomeada no card "Lições aprendidas na tarefa" do laudo | `T49` |
| b2 | `GOVERNANCA.md` §4.3, condição **Capacidade** | A cláusula do *proxy operante* elegia o teto de tool uses por classe como critério de fim de janela — número arbitrário encerrando trabalho legítimo, que é o vício em forma explícita | Cláusula removida: o instrumento da capacidade é a **medida de ocupação da janela** e, enquanto ela não existir, o encerramento se apoia em **coesão** e no fim natural do trabalho. "Nenhum número arbitrário faz esse papel" ficou escrito | `T49` |
| b3 | `GOVERNANCA.md` §4.3, checkpoint intermediário | O gatilho era **numérico** — "2/3 do teto da classe" | Gatilho **qualitativo**: quem executa conclui que o contexto acaba antes da tarefa, e o mesmo checkpoint responde ao sinal de poluição | `T49` |
| b4 | `README.md`, espelho da tabela de classes | Espelhava o teto com poder de porteiro | *"referência informativa de dimensionamento, nunca porteiro: cruzá-lo é alarme, não bloqueio"* | `T49` |
| b5 | `README.md`, espelho do §4.3 (verbete de contexto e item 7 do §10) | Espelhava o fim de janela pelo proxy numérico | Espelho reescrito nas duas condições — coesão e capacidade —, sem número que encerre | `T49` |
| b6 | `docs/plans/P-0734`, §3 item 5 (invariante de execução) e a marca do `### DP-B` | O regime de teto do plano e o dossiê ratificado da política de autonomia ainda enunciavam o roteamento por estouro | Regime do plano fixado pela `DP-Q`; `### DP-B` recebeu **marca de revogação parcial** com o corpo intocado — caem `A4` e os dois números do bloco B, permanecem o teto de retentativa, a precedência do bloco A e a fronteira "obriga parada × segue com registro" | `T49` |
| b7 | `.claude/skills/scrum-master/SKILL.md`, bloco A, linha `A4` | Estouro de teto **roteava**: mandava PARAR e devolver ao replanejamento — consumo decidindo fluxo | Linha removida da tabela; o consumo medido é declarado **alarme, nunca bloqueio** e não é condição de nenhuma linha de roteamento | `T50` |
| b8 | `.claude/skills/scrum-master/SKILL.md`, bloco B, linha `B2` | Encerrava a janela por **dez tarefas fechadas** ou **900 k tokens acumulados** — os dois números que a decisão derruba nominalmente | `B2` passou a medir **coesão** (sinal de poluição) e **ocupação da janela**, sem número no lugar dos que caíram | `T50` |
| b9 | `.claude/skills/scrum-master/SKILL.md`, lista "Obriga parada" | Dois itens de teto na lista de parada obrigatória | Os dois itens saíram; a lista guarda só parada de **causa** | `T50` |
| b10 | `.claude/tools/rdo.py`, `calcular_desdobramento` | `orcamento_estourado = args.tool_uses > dossie.teto` abria um terceiro ramo de desdobramento: o gerador **decidia por consumo** | Assinatura passou a `calcular_desdobramento(veredito)` — dois ramos por veredito, nenhum por consumo. O valor continua **medido, transcrito e impresso** no RDO | `T51a` |
| b11 | `tests/test_rdo.py`, teste do ramo por estouro | O teste trancava o gate removido | **Reescrito**, não apagado: tranca o comportamento novo — `--tool-uses` acima do teto do cabeçalho continua medido e registrado e **não** abre ramo. Piso **39** preservado | `T51a` |
| b12 | `docs/RUBRICA_DE_REVISAO.md`, dimensão `registro` | A dimensão media consumo sem dizer que a **grandeza** não pontua, deixando aberta a leitura de que número alto rebaixa a marcação | Fecho explícito: mede-se **existência e procedência** do registro, nunca a grandeza; o número não pontua dimensão, não reprova entrega, não abre desdobramento e não é fundamento de achado; o qualitativo mora no card "Lições aprendidas na tarefa", a critério do reviewer | `T51b` |
| b13 | `.claude/agents/pantonic-executor.md`, bullet "Economia de turnos" | *"orçamento esperado ~≤40 tool uses (… sinalizar ao `scrum-master`, não só continuar)"* — o número **roteava**: estourar obrigava a sinalizar | O orçamento da classe é referência informativa de dimensionamento; cruzá-lo é alarme, nunca bloqueio — não recusa entrega, não roteia, não encerra a tarefa e não muda o que se entrega. O consumo é medido no encerramento por quem orquestra | `T51b` |
| b14 | `.claude/agents/pantonic-reviewer.md`, "Fatos estáveis" | O prompt não declarava que consumo é informação e não nota, deixando o juízo sem fronteira nesse ponto | Bullet novo: consumo não marca dimensão, não reprova e não abre rota; a `registro` julga existência e procedência, nunca a grandeza | `T51b` |
| b15 | `.claude/agents/pantonic-reviewer.md`, "Fatos estáveis" e "Proibições" | A residência do registro qualitativo de consumo não estava nomeada no papel que a preenche | Card **"Lições aprendidas na tarefa"** nomeado como residência única, com preenchimento **discricionário** — só quando houver o que observar; sem observação, o número isolado se desconsidera. Proibição nova: não pontua, não reprova e não escala por consumo | `T51b` |
| b16 | `docs/RESIDENCIA_DOUTRINA.md`, item 7.7, coluna "Ação na `T17`" | Prescrevia ao `CLAUDE.md` global manter *"estourar = replanejar, não continuar"* — porteiro numérico numa ação ainda **não executada** | Prescrição reescrita: o global mantém que o dimensionamento por tarefa atômica é **referência informativa**, alarme e nunca bloqueio, e cita o kit | `T51b` |
| b17 | `docs/RESIDENCIA_DOUTRINA.md`, `DR-C` | Tratava a divergência ≤40 × ≤30 como contradição **de gate** ("teto de turnos") | Renomeada para divergência de **orçamento**: nenhum dos dois números governa fluxo, de modo que ela degrada o dimensionamento antes de delegar, não a aceitação da entrega | `T51b` |
| b18 | `docs/plans/P-0734`, `DA-11` (§1) e o card `T6b` (§4) | Os dois enunciavam *"até ele existir, o proxy operante continua sendo o teto de tool uses por classe"* — premissa ratificada que a decisão derruba | **Marca de revogação parcial** nos dois, no formato das anteriores: corpo intocado, marca no topo. Permanecem as duas condições e as consequências; cai a cláusula de enforcement | `T51b` |

### Classe (c) — nenhuma nova; as duas herdadas foram **quitadas** por esta rodada

As ocorrências `c1`/`c2` do universo 1, materializadas em `A4` e `B2` da skill `scrum-master`
(remissão registrada no universo 2), eram exatamente a matéria que subiu ao dono e voltou decidida.
Estão quitadas em b7 e b8, e o `TK-41` fecha com elas. Esta varredura **não abriu** contradição nova
de dono: a matéria geral de limites não se doutrina aqui — ela se revê inteira no plano próprio já
previsto, e nenhum número novo entrou no lugar dos que caíram.

### Classe (a) — conferidas e não tocadas (9)

| # | âncora | por que não se toca |
|---|---|---|
| a1 | `docs/telemetria.tsv` e a doutrina de telemetria do `GOVERNANCA.md` §4.2 | A série é o **agregado** a que a decisão atribui o valor: custo e consumo só rendem insight analisados em conjunto. Preservada por desenho, alimentada sem exceção |
| a2 | `.claude/skills/diario-de-obras/SKILL.md`, as duas linhas do **teto de retentativa** (`review` → `in-progress` e `review` → `blocked`) | Não é teto de consumo: é o limite de reexecução, parada de **causa**, declarada íntegra pela própria decisão |
| a3 | `docs/RUBRICA_DE_REVISAO.md`, as duas ocorrências de `teto` na dimensão `registro` | Limite de **tamanho** dos campos do dossiê de evidência, não consumo. A ambiguidade do termo ficou desfeita no texto acrescentado em b12 |
| a4 | `.claude/tools/review_evidence.py` (21 ocorrências) e `tests/test_review_evidence.py` (4) | Todas são `teto_chars` — truncamento de trecho de diff. Medidas em `T51a` e conferidas ocorrência a ocorrência: nenhuma decide fluxo |
| a5 | `.claude/tools/rdo_template.md`, linha `**Consumo:**` | É a **transcrição** do valor medido contra o teto do cabeçalho — medir e registrar é exatamente o que permanece |
| a6 | `GOVERNANCA.md` §3, a tabela de classes, e §4.3, o teto de trabalho de ~50% da janela | A primeira dimensiona antes de delegar (b1 já lhe tirou o poder de gate); o segundo é a **condição de capacidade**, que a decisão preserva nominalmente como um dos dois critérios de fim de janela |
| a7 | `.claude/skills/proximo-passo/SKILL.md`, o bloco de decomposição (*"o teto é alarme, a divisão é o controle"*) | Já enuncia a régua vigente, com a série medida como evidência; prescreve teto no dossiê para **dimensionar**, não para barrar |
| a8 | `.claude/skills/redacao-doc/SKILL.md`, exemplo *"O teto é alarme, não controle."* | Exemplo de redação sobre a frase, não enunciado normativo sobre fluxo |
| a9 | RDOs já emitidos, bullets de fechamento do diário e entradas de `CHANGELOG.md` de versão publicada | Narram o que aconteceu à época e continuam verdadeiros como registro |

### Achados fora de escopo (uma linha cada)

- `.claude/skills/handover/SKILL.md`, seção "Checkpoint intermediário": o gatilho ainda é
  *"o consumo cruza **2/3 do teto da classe**"*, número que dispara encerramento e contradiz o §4.3
  reescrito em b3 — fora do universo declarado da `T51`, **não editado**; pede tíquete.
- O card **"Lições aprendidas na tarefa"** é nomeado pela doutrina (§3), pela skill `scrum-master` e
  agora pelo prompt do `reviewer`, mas **nenhum gerador o emite**: nem o documento do
  `rdo.py laudo` nem o `rdo_template.md` têm o card. Residência **nomeada e não materializada** —
  os instrumentos estão fechados pela `T51a`, então aqui é achado, não edição.

### Verificação de fechamento — os quatro em exit 0

| comando | saída literal | exit |
|---|---|---|
| `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` | `kit_check: OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0').` | 0 |
| `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | `kit_check: check-drift OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s)).` | 0 |
| `pwsh -NoProfile -File .claude/checks/check-readme.ps1` | `check-readme: OK - 8 agente(s), 11 skill(s), 16 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.` | 0 |
| `python -m pytest` (raiz do hub) | `39 passed in 2.63s` | 0 |

**Invariantes conferidos.** Nenhum guardrail nasceu ou saiu (**16 × 16**), **14 seções** de fonte da
verdade válida, nenhum bump de versão (`0.0.0`, `DE-7`), piso de regressão em **39**. Nenhum teste
foi apagado ou afrouxado — o que verificava gate removido foi reescrito. Nenhum número novo entrou no
lugar dos que caíram, e nenhuma parada de **causa** foi enfraquecida: `pendencia=`, `escalar`,
`premissa`, reprovação após a última retentativa e plano não-pronto seguem íntegros, e a escalada
por ambiguidade ou conflito de requisito e de aceitação segue **ilimitada**.

**Fechamento do bloco.** Medir consumo continua em toda parte — série, RDO e laudo —, decidir por
consumo não existe em lugar nenhum do framework, e o registro qualitativo tem residência nomeada e
discricionária. O que resta em aberto são os dois achados acima, ambos fora do universo declarado.
