# Conformidade com a matriz de responsabilidades — 2026-08-12

Régua: `GOVERNANCA.md` §3 (matriz de responsabilidades, autoridade exaustiva) e §7 item 15
(`G-SCOPE`). Veredito por ocorrência: **(a)** endossado pela linha do papel · **(b)** não endossado
e dispensável (sai ou é reescrito para o que a matriz declara) · **(c)** não endossado, ato real e
necessário — **lacuna da matriz**, que sobe ao dono e não se resolve no artefato.

## 1. Kit executável (`.claude/agents/`, `.claude/skills/`)

Universo varrido: 8 arquivos de agente e 11 `SKILL.md`, pelos verbos atributivos
(`atualiz|registr|escrev|grav|decid|marc|fecha|julg|aprova|delega|invoca|emite`) — 307 ocorrências
brutas, das quais as abaixo carregam atribuição de ato a um papel. As linhas citadas são as do
estado **anterior** à edição.

| # | Arquivo | Linha | Papel | O que o texto atribui | Veredito | Ação |
|---|---|---|---|---|---|---|
| 1 | `.claude/agents/pantonic-auditor-arch.md` | 108 | Auditoria → Planejamento | auditoria manda "registrar os tíquetes via `pantonic-planner`"; a matriz não declara registro de tíquete para Planejamento, e a linha de Auditoria diz que o apontamento vira item do diário priorizado pelo dono | b | reescrito para "cada apontamento vira item do diário de obras, priorizado pelo dono" |
| 2 | `.claude/agents/pantonic-auditor-cleancode.md` | 61-62 | Auditoria → Planejamento | idem, com ponteiro extra à skill `diario-de-obras` | b | mesma reescrita |
| 3 | `.claude/agents/pantonic-planner.md` | 42 | Planejamento | proibição "Implementar ou editar código de produção/teste" — repete "não faça o que é de outro papel" (Execução), já na coluna *Não faz* da matriz | b | bullet removido |
| 4 | `.claude/agents/pantonic-planner.md` | 43-44 | Planejamento | proibição de iniciar execução (redundante) **e** atribuição de `handover` ao planejamento, que a matriz não declara | b | bullet removido |
| 5 | `.claude/agents/pantonic-planner.md` | 45 | Planejamento | "não ler arquivos inteiros — peça dossiê ao `pantonic-scout`" restringe o exercício da **própria** responsabilidade | a | mantido |
| 6 | `.claude/agents/pantonic-benchmarker.md` | 68-70 | Benchmarking | "sem juízo sobre o Pantonic", "sem prosa de recomendação", "um repositório por invocação" — restrições sobre a própria descrição | a | mantido |
| 7 | `.claude/agents/pantonic-reviewer.md` | 85-88 | Revisão | não marcar `conforme` contra vermelho mecânico, não completar critério inverificável, não escrever percentual/veredito — restrições sobre o próprio laudo | a | mantido (`T37`/`DP-M` já resolveram) |
| 8 | `.claude/agents/pantonic-reviewer.md` | 33, 36 | Revisão / Orquestração | laudo gravado pelo gerador; `scrum-master` fecha o registro da tarefa | a | mantido |
| 9 | `.claude/agents/pantonic-executor.md` | 10, 26, 42-47 | Execução | não aferir a própria aceitação; Tier 3 nunca por iniciativa própria; plano não-pronto → para e escala | a | mantido (`T40`) |
| 10 | `.claude/agents/pantonic-scout.md` | 9, 26 | Coleta | devolve dossiê compacto, sem juízo | a | mantido |
| 11 | `.claude/agents/pantonic-fora-da-caixa.md` | 48 | Redesenho | propõe o recomeço mental, não implementa | a | mantido |
| 12 | `.claude/skills/guardrails-check/SKILL.md` | 28 | — | ponteiro `integration-executor` R-3: papel que a matriz **sequer cita** | b | ponteiro removido; fica `CLAUDE.md` global, Regra 7 |
| 13 | `.claude/skills/guardrails-check/SKILL.md` | 29 | Execução | "o executor só recomenda o passe completo **no handover**" — atribui `handover` à execução, contra a coluna *Não faz* | b | reescrito para "no sinal de retorno" |
| 14 | `.claude/skills/guardrails-check/SKILL.md` | 80 | — | "agente de refactor": papel que a matriz sequer cita | b | trocado por "auditor de clean code" |
| 15 | `.claude/skills/guardrails-check/SKILL.md` | 95-96 | Execução | manda colar o bloco de veredito nas "Notas de execução" **do diário de obras** — escrita no diário, negada à Execução | b | destino reescrito para o retorno de fechamento de quem rodou o gate (sinal da execução, ou relatório da auditoria) |
| 16 | `.claude/skills/guardrails-check/SKILL.md` | 110-111 | Execução | "registrar no diário de obras (`blocked` ou permanece `in-progress`)" — escrita e materialização de status, ambas fora da Execução | b | reescrito para "sinalizar `blocked` com a razão tipada, em vez de `review`" |
| 17 | `.claude/skills/guardrails-check/SKILL.md` | 27-28 | Execução | "o executor **não** roda Tier 3 por conta própria" — restringe o exercício da própria responsabilidade | a | mantido |
| 18 | `.claude/skills/diario-de-obras/SKILL.md` | 34-35 | Execução | "Handover **de execução** escreve o detalhe (o que foi feito, testes, consumo)" na seção do diário | b | reescrito para "O handover de fechamento" |
| 19 | `.claude/skills/diario-de-obras/SKILL.md` | 131-132 | Execução | "Notas de execução … preenchido **pelo executor** no handover" | b | reescrito para "preenchido no handover de fechamento" |
| 20 | `.claude/skills/diario-de-obras/SKILL.md` | 58-62 | Orquestração / Execução | `status` materializado só pelo `scrum-master`; executor é autor de `review` e `blocked` | a | mantido (fronteira da `DP-G`) |
| 21 | `.claude/skills/diario-de-obras/SKILL.md` | 92, 94 | Orquestração | `scrum-master` invoca o `pantonic-reviewer` e escreve o RDO | a | mantido |
| 22 | `.claude/skills/proximo-passo/SKILL.md` | 65-67 | Auditoria / Orquestração | autoriza delegar tarefa de execução a "`clean-code`" e "`architect-auditor`" — dois papéis que a matriz sequer cita, e a linha de Auditoria proíbe alterar código | b | cláusula removida; fica "despachar ao papel competente é critério do orquestrador" |
| 23 | `.claude/skills/proximo-passo/SKILL.md` | 151-159 | Orquestração | orquestrador escreve o bullet de fechamento e a linha de telemetria | a | mantido ("registrar a telemetria medida e arquivar o resultado") |
| 24 | `.claude/skills/audit-sweep/SKILL.md` | 3 | Auditoria | bloco/frente "pyside6" no `description`: a matriz declara **duas** frentes permanentes (arch, cleancode), e a bateria do próprio arquivo não tem esse bloco | b | `description` corrigido para "arch, DDD, cleancode, fora-da-caixa"; README regerado |
| 25 | `.claude/skills/audit-sweep/SKILL.md` | 10-11, 37 | Orquestração / Coleta | skill delega a bateria ao `pantonic-scout` e grava o dossiê no contexto principal | a | mantido (scout não escreve) |
| 26 | `.claude/skills/integrar-poc/SKILL.md` | 3 | — | "pipeline de 5 passos **do agente integrador**": papel que a matriz sequer cita | b | `description` reduzido a "pipeline de 5 passos"; README regerado |
| 27 | `.claude/skills/handover/SKILL.md` | 96-100 | Execução | o checkpoint dispara quando **o executor** conclui que vai estourar, e o entregável são "até 5 linhas **no diário**, na 'Notas de execução' da tarefa em curso" — escrita no diário, negada à Execução, e sem forma de sinal que a carregue | **c** | **não editado**: sobe ao dono |
| 28 | `.claude/skills/handover/SKILL.md` | 128-130 | Orquestração | orquestrador emite por conta própria o aviso de janela suja | a | mantido |
| 29 | `.claude/skills/handover/SKILL.md` | 134-138 | — | proibições sobre o próprio ato de fechar (não iniciar outra tarefa, não marcar `done` com vermelho, não deixar o diário desatualizado) | a | mantido |
| 30 | `.claude/skills/scrum-master/SKILL.md` | 236-240 | Orquestração | `scrum-master` **apaga** o laudo em todos os ramos | a | mantido: "rotear … o laudo do `reviewer`" cobre o ciclo de vida dele, e a rota é a da `DP-K` §14.4 |
| 31 | `.claude/skills/scrum-master/SKILL.md` | 16 | Orquestração | "não implementa, não julga entrega e não decide arquitetura" | a | mantido (poda da `T37` não se reabre) |
| 32 | `.claude/skills/scrum-master/SKILL.md` | 77, 173, 191 | Orquestração | materializa status, escreve o RDO, apensa a linha de telemetria | a | mantido |
| 33 | `.claude/skills/modelo-por-fase/SKILL.md` | 43-48 | — | "não decida sozinho"; só o dono inverte a tabela para execução | a | mantido (a decisão é do dono na matriz) |
| 34 | `.claude/skills/checar-versao-kit/SKILL.md` | 67-72, 90-91 | — | nunca atualiza sozinho; não executa a revisão de doutrina, só a torna visível | a | mantido |
| 35 | `.claude/skills/redacao-doc/SKILL.md` | — | — | ocorrências são exemplos de redação, não atribuição de ato a papel | a | mantido |
| 36 | `.claude/skills/bootstrap-pantonic/SKILL.md` | — | — | idem (procedimento sem papel nomeado) | a | mantido |

### Lacuna da matriz aberta por esta varredura

- **(c) #27 — quem escreve o checkpoint de contexto.** `handover/SKILL.md:96-100` atribui à Execução
  escrever até 5 linhas nas "Notas de execução" do diário quando o contexto vai estourar. O ato é
  real e necessário (`CLAUDE.md` global, Regra 2: o contexto que morre precisa deixar o estado),
  mas a matriz nega à Execução escrever no diário e o domínio fechado do sinal (`review` /
  `blocked` com razão tipada) não carrega o conteúdo do checkpoint. Criar a responsabilidade no
  prompt seria a violação; a falta é da matriz e a decisão é do dono.

## 2. Doutrina, espelho e índices

Universo varrido: `GOVERNANCA.md` (839 linhas), `README.md` (933), `ARQUITETURA_PANTONICA.md` (513),
`docs/RUBRICA_DE_REVISAO.md` (259), `docs/RESIDENCIA_DOUTRINA.md` (188) e `docs/DOC_MAP.md` (102),
pelos mesmos verbos atributivos (`atualiz|registr|escrev|grav|decid|marc|fecha|julg|aprova|delega|
invoca|emite`) — **381 ocorrências brutas**, mais uma varredura complementar por papel que a matriz
sequer cita. As linhas citadas são as do estado **anterior** à edição. A **matriz** (§3, linhas
88-98) é a régua desta varredura e não é objeto dela. O §9 do `README.md` (handover) fica fora: é o
recorte do `TK-36`.

| # | Arquivo | Linha | Papel | O que o texto atribui | Veredito | Ação |
|---|---|---|---|---|---|---|
| 37 | `GOVERNANCA.md` | 88-98 | todos | a própria matriz de responsabilidades | a | régua da varredura, não objeto dela — não editada |
| 38 | `GOVERNANCA.md` | 102-103 | Coleta / Planejamento / Execução | varredura ampla nunca é feita pelos agentes caros, é delegada à coleta | a | mantido: a linha da Coleta declara "devolve só o pertinente para o contexto dos agentes mais caros" |
| 39 | `GOVERNANCA.md` | 139 | Execução | estouro do teto de turnos se "reporta **no handover**" — a matriz não declara `handover` para a Execução, cujo retorno é o **sinal** | b | reescrito para "reportar no sinal de retorno" (mesma correção do `#13`) |
| 40 | `GOVERNANCA.md` | 250-253 | Planejamento / Coleta | planejamento cria o checklist de tarefas atômicas, com apoio da coleta | a | mantido |
| 41 | `GOVERNANCA.md` | 267-275 | Orquestração | índice do diário atualizado a cada mudança de status; diretiva de priorização escrita no diário | a | mantido (materializar status e arquivar o resultado são da orquestração; a diretiva é do dono) |
| 42 | `GOVERNANCA.md` | 276-279 | Planejamento | planos paralelos gravam o plano em `docs/plans/` e apensam uma linha ao `_INBOX.md` | a | mantido: o artefato do plano é o entregável declarado do Planejamento |
| 43 | `GOVERNANCA.md` | 295-302 | Orquestração | consumo registrado **pelo orquestrador** a partir do `<usage>` da notificação | a | mantido ("registrar a telemetria medida") |
| 44 | `GOVERNANCA.md` | 333-334 | Execução | "**o agente atualiza o diário de obras** e faz handover para o usuário" ao concluir ou bloquear — escrita no diário e fechamento, ambos negados à Execução | b | reescrito: quem executa **sinaliza** (`review` / `blocked` com razão tipada) e encerra o próprio contexto; o registro do fechamento no diário e a abertura da tarefa seguinte são da orquestração |
| 45 | `GOVERNANCA.md` | 335-339 | Orquestração | `proximo-passo` drena o inbox, aplica a diretiva, escolhe **uma** tarefa e delega à execução | a | mantido ("despachar cada tarefa ao papel competente") |
| 46 | `GOVERNANCA.md` | 340-344 | Execução | "**o executor grava um checkpoint intermediário**" (skill `handover`) quando o consumo cruza 2/3 do teto | **c** | **não editado**: é a **fonte** da mesma lacuna do `#27` — sobe ao dono |
| 47 | `GOVERNANCA.md` | 378-380 | Dono | o dono registra no diário a remoção de um comportamento do piso | a | mantido ("autoriza saída do piso de regressão") |
| 48 | `GOVERNANCA.md` | 517-527 | Execução | `G-PLANFIDELITY`: o executor não substitui a rota, para e escala | a | mantido |
| 49 | `GOVERNANCA.md` | 529-554 | Planejamento | `G-PLANREADY` como **dever do planejador**: fechar as cinco condições antes de publicar | a | mantido (decomposição em tarefas atômicas fechadas é a linha do Planejamento) |
| 50 | `GOVERNANCA.md` | 555-561 | Execução | `G-EXECREADY`: não decide, não pergunta, recusa plano não-pronto | a | mantido |
| 51 | `GOVERNANCA.md` | 573-584 | Planejamento / Dono | `G-README` dever 2: tarefa de revisão do README no encerramento da sprint, com aceite do dono | a | mantido (declarado na linha do Planejamento) |
| 52 | `GOVERNANCA.md` | 611-620 | — | a skill `checar-versao-kit` reporta ao dono e **não executa** a revisão de doutrina | a | mantido (restringe o próprio ato de reportar) |
| 53 | `GOVERNANCA.md` | 660-710 | — | registro das rodadas de revisão de guardrails | a | história do que aconteceu à época — não se reescreve |
| 54 | `GOVERNANCA.md` | 778-807 | — | nenhum agente sincroniza o kit por conta própria; reportar sim, atualizar nunca; a resposta é do dono | a | mantido (a decisão é do dono na matriz; a restrição é sobre o próprio ato de reportar) |
| 55 | `README.md` | 402-403 | Execução | "ele para, **marca `blocked` no diário** com a razão e **faz handover**" — escrita no diário e materialização de status, ambas negadas à Execução | b | reescrito para "para, **sinaliza** `blocked` com a razão tipada e escala"; a fonte (matriz, linha da Execução) já dizia "sinaliza `blocked` e escala" — o espelho é que divergia |
| 56 | `README.md` | 316-320 | Dono / Orquestração | teto é alarme; a classe é escolhida e registrada no dossiê **antes** da delegação | a | mantido |
| 57 | `README.md` | 399-401 | Planejamento / Execução | planejador nunca executa; executor não decide, não pergunta e não muda a rota | a | mantido (espelho fiel da matriz) |
| 58 | `README.md` | 420-426 | Dono | aprovação do plano, desbloqueio de `blocked` e remoção de comportamento do piso | a | mantido |
| 59 | `README.md` | 460-499 | Orquestração | gate de delegação, uma tarefa por invocação, recusa de plano aberto; a diretiva é escrita pelo dono | a | mantido |
| 60 | `README.md` | 561-564 | Dono | diretiva de priorização, registro de remoção do piso e triagem de achados no fechamento da sprint | a | mantido |
| 61 | `README.md` | 617-682 | — | §9, handover | — | **fora do escopo**: recorte do `TK-36` |
| 62 | `README.md` | 697-709 | — | espelho da tabela de guardrails da §7 (enforcement por linha) | a | mantido; contagem 15 × 15 preservada |
| 63 | `README.md` | 740-742 | Planejamento / Execução / Revisão | tabela de agentes espelhando a matriz | a | mantido |
| 64 | `README.md` | 754-762 | — | tabela de skills: gatilho de cada uma, sem papel nomeado | a | mantido |
| 65 | `README.md` | 832 | Orquestração | "Quem escreve a linha é **o orquestrador**", nos dois pontos de fechamento | a | mantido |
| 66 | `ARQUITETURA_PANTONICA.md` | 155, 393 | — | "**agente de integração**" (harness e pipeline de 5 passos): papel que a matriz **sequer cita** — mesma família do `#26` | b | trocado por "harness de integração de POC" e "Pipeline de integração da POC (5 passos)" |
| 67 | `ARQUITETURA_PANTONICA.md` | 389-390 | Redesenho / Auditoria | a plataforma "não refatora, **não audita**, não reescreve" a POC preservada em `plugins/<nome>/adhoc/` | a | mantido: a linha do Redesenho já declara "não redesenha POC validada (`plugins/*/adhoc/`)" |
| 68 | `ARQUITETURA_PANTONICA.md` | 53 | — | linguagem ubíqua falada por dono, planejador, executor, código e teste | a | mantido: nomeia papéis, não atribui ato |
| 69 | `ARQUITETURA_PANTONICA.md` | 189-331, 463 | — | "escreve", "registrar", "invocar", "marca" são atos das **portas de software**, não de papéis agênticos | a | fora do alvo do verbo atributivo |
| 70 | `docs/RUBRICA_DE_REVISAO.md` | 8-9, 22, 42-58, 257-258 | Revisão | o reviewer marca as sete dimensões e emite o laudo pelo gerador; não corrige, não replaneja, não edita os arquivos da tarefa e não escreve percentual nem veredito | a | mantido (`T37`/`DP-M` não se reabre) |
| 71 | `docs/RUBRICA_DE_REVISAO.md` | 137-143 | Revisão / Orquestração | dimensão `registro`: o reviewer **julga** a auditabilidade do registro; "consumo registrado por ponteiro" não nomeia sujeito | a | mantido: julgar é a linha da Revisão; registrar é a da Orquestração |
| 72 | `docs/RUBRICA_DE_REVISAO.md` | 244-252 | Revisão / Dono | achado de processo exige rota; requisito faltante sobe ao dono pelo `--escalar` e a revisão o **registra sem resolvê-lo** | a | mantido |
| 73 | `docs/RESIDENCIA_DOUTRINA.md` | arquivo | — | classifica as regras do `CLAUDE.md` global por residência; a decisão do dono está registrada em §6 | a | registro de decisão à época — não se reescreve |
| 74 | `docs/DOC_MAP.md` | arquivo | — | as ocorrências dos verbos são estado de plano ("plano fechado", "done") e navegação, sem papel atribuído | a | mantido; a desatualização do índice é o `TK-06`, fora desta tarefa |

**Partição:** 38 ocorrências classificadas — **32 (a)**, **4 (b)**, **1 (c)**, mais 1 linha fora do
escopo (`TK-36`). Arquivos editados: `GOVERNANCA.md`, `README.md`, `ARQUITETURA_PANTONICA.md`.

### Lacuna da matriz aberta por esta varredura

- **(c) #46 — quem grava o checkpoint de contexto (fonte da doutrina).** `GOVERNANCA.md:340-344`
  atribui ao **executor** gravar o checkpoint intermediário quando o consumo cruza 2/3 do teto da
  classe. É a **fonte** do que o `#27` encontrou em `handover/SKILL.md:96-100`: o mesmo ato, a mesma
  falta. O ato é real e necessário (o contexto que morre precisa deixar o estado, e o próprio §4.3
  o exige), mas a matriz nega à Execução escrever no diário e o domínio fechado do sinal (`review` /
  `blocked` com razão tipada) não carrega o conteúdo do checkpoint. Criar a responsabilidade aqui
  seria a violação; a falta é da matriz e a decisão é do dono. Como a correção nasce na fonte e
  desce, `#27` e `#46` se resolvem no mesmo ato — e nenhum dos dois se resolve nesta tarefa.
