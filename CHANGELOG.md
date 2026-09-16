# Changelog

Todas as mudanças notáveis do framework Pantonic* (doutrina em `GOVERNANCA.md`/`ARQUITETURA_*` +
kit agêntico em `.claude/`) são registradas aqui. `VERSION` (raiz) e `.claude/KIT_VERSION` carregam
sempre o mesmo valor — ver `GOVERNANCA.md` §10.

Versionamento: [Semantic Versioning](https://semver.org/lang/pt-BR/), com significado declarado em
`GOVERNANCA.md` §10 — MAJOR exige ação do consumidor, MINOR adiciona artefato/guardrail
compatível, PATCH corrige redação.

A versão está congelada em `0.0.0` (`DE-7`) até decisão de publicar. Enquanto durar o
congelamento, toda mudança canônica é registrada sob `## [Não lançado]`, a única seção viva. As
seções numeradas abaixo (`1.0.0`..`2.0.0`) são o histórico de desenvolvimento pré-lançamento,
correspondem às tags `kit-v1.0.0`..`kit-v2.0.0` já publicadas e permanecem como registro — não são
reescritas nem revogadas.

## [Não lançado]

- `G-NOASK` (`GOVERNANCA.md` §7 item 18, 2026-09-16, decisão do dono): interrupção para escalar
  ao dono durante a execução é falha de planejamento — quem executa (executor e orquestração)
  não fica com dúvida e não escala direto: para, registra `AE-<n>`, bloqueia `premissa` e
  encerra; o planejador não libera plano com alto risco de interrupção (teste de interrupção,
  fase 4 item 8). Matriz §3 (execução, orquestração, planejamento), §4.3 (canal de escalada),
  `pantonic-executor`, `pantonic-planner`, `pantonic-reviewer` (`--escalar` vai ao planejamento;
  decisão não fechada pelo card é achado `dossiê`), `scrum-master` (`B1` roteia ao planejador;
  nenhuma pergunta entre despacho e relatório), `proximo-passo`, `handover` (≤ 8 linhas) e
  README §10 (itens 17 e 18) alinhados. Achados do card
  `docs/plans/_CARD-revisao-critica-pickup-opus.md` absorvidos: registro único do achado
  (§4.2 "Fechamento enxuto"), disciplina de instrumento (§3, cinco regras), opção "registrar e
  não agir" em toda rodada de decisões, `contado` exige contagem efetiva (§4.2) —
  `docs/telemetria.tsv` linha `BKL-AE2-pickup` corrigida de 14 para 29 (contagem do card).
  `rdo.py laudo` passa a recusar `--plano`/`--tarefa` em forma de caminho (TR em
  `tests/test_rdo.py`).
- `G-REPLAN` (`GOVERNANCA.md` §7 item 17, 2026-09-16): bloqueio de tarefa por `premissa` abre uma
  rodada de replanejamento como próxima tarefa do plano, roteada ao planejador (não ao dono);
  `scrum-master` `A3b`, `proximo-passo` e `diario-de-obras` alinhados. `pantonic-planner` ganha
  inventário de corpus (fase 1), teste do parser frio (fase 4) e `idem`/`análogo` no léxico
  proibido. Origem: `P-0739` `AE-1`/`RP-1`.
- `.claude/agents/pantonic-planner.md` reescrito como doutrina operacional do papel de planejamento (2026-09-15): protocolo em cinco fases com duas saídas antes do plano (campanha de investigação delegada ao `pantonic-scout`/tarefa `investigacao`; rodada única de decisões ao dono), anatomia do card autossuficiente para executor frio (camada, domínio, restrições inline, contingências fechadas), auto-auditoria G-PLANREADY + teste do executor frio + léxico proibido, e proibição de publicar plano com questão aberta. Motivo: executores ignorando restrições e decidindo sob plano com dúvida pendurada; sessões de planejamento longas com medição própria. `.claude/README.md` regenerado.
- `GOVERNANCA.md` §4.3 reconciliada (`DX-10`/`G-SURFACE`): a doutrina deixa inequívoco que a
  janela de orquestração atravessa as tarefas atômicas do mesmo plano e só encerra na troca de
  plano ou iniciativa (ou, de forma planejada, na ocupação da janela) — o "contexto limpo" pago
  a cada tarefa concluída é o do **executor**, nunca o fechamento da janela de orquestração.
  `.claude/tools/ocupacao.py` e a `DX-14` item 3 (encerramento planejado entre tarefas) não mudam.
- `rdo.py`/`review_evidence.py` reconciliados com a gramática nova do cabeçalho de tarefa
  (`G-SURFACE`, `DX-15`): o segmento ` · teto <N>` do cabeçalho vira opcional e é descartado no
  parse — cabeçalho histórico com o segmento continua parseando, mas o número não sobrevive em
  `DossieTarefa` nem no RDO gerado; `_CLASSE_TETO_DEFAULT` permanece como conjunto normativo de
  classes, só para mensagens de erro.
- Kit executável reconciliado com a mesma diretriz (`G-SURFACE`): as skills de fluxo
  (`proximo-passo`, `scrum-master`, `diario-de-obras`) e a docstring de `.claude/tools/ocupacao.py`
  perdem o texto que orçava teto a quem executa e mandava parar por número. O gate de delegação
  passa a enunciar **decomposição** como dimensionamento do planejador, com ponteiro para
  `GOVERNANCA.md` §3; a gramática de cabeçalho de tarefa passa a `### <ID> — <título> [<modelo> ·
  classe <classe>]` e o consumo medido vira **medida e registro, nunca critério de rota**; o
  `scrum-master` declara que **não revisa plano** e que encerramento por poluição de contexto não é
  gracioso; o proxy de ocupação é reclassificado como **aviso informativo à orquestração entre
  tarefas** (valor `0.50`, hook e comportamento inalterados).
- Superfície de papéis reconciliada com a diretriz de dimensionamento (`G-SURFACE`): teto e
  orçamento saem do horizonte do **executor** — cuja responsabilidade única passa a ser executar a
  tarefa — e entram no do **planejador**, que dimensiona cada tarefa e detém com exclusividade a
  **revisão de plano**. A escada de escalada fica escrita uma única vez, em `GOVERNANCA.md` §3
  abaixo da matriz de responsabilidades (suspeita → `blocked` com razão `premissa` → planejador
  decide o técnico e o tático → dono decide o estratégico e o que altera escopo), com ponteiro nos
  três artefatos que a exercem. Na skill `handover`, contexto poluído passa a retorno **não
  gracioso** (sem ponteiro de retomada) e contexto acabando dentro de uma tarefa passa a sintoma de
  **tarefa mal dimensionada**, devolvido ao planejamento em vez de retomado pela metade; o
  checkpoint de ponteiro de estado fica para o encerramento planejado da janela de orquestração.
- A disciplina de contexto se parte em duas normas de naturezas diferentes. **Poluição** é regra
  final de execução — parada não graciosa no ato, nada do produzido depois do sinal se aproveita e
  retorno a quem orquestra demandando contexto limpo para a reexecução —, canônica em
  `.claude/global/CLAUDE.md` (Regra 2), com texto operacional em `GOVERNANCA.md` §4.3 e guardrail
  em §7 item 7. **Capacidade** deixa de ser condição de execução e vira **diretriz de
  dimensionamento de quem planeja**, canônica em `GOVERNANCA.md` §3, com os três critérios, a
  estimativa de 50% de ocupação (tolerância a 60%), a proveniência e a cláusula de revisão;
  capacidade nunca interrompe tarefa em curso, e `.claude/tools/ocupacao.py` fica como aviso
  informativo à orquestração. A tabela de classes passa a ser a única residência de número de
  teto, que sai do dossiê de tarefa (`CTX-T1`).
- O vocabulário de `status` do kanban ganha residência única em
  `.claude/skills/diario-de-obras/SKILL.md` (`## Status — residência única`), com sete estados:
  `triage`, `ready`, `blocked`, `in-progress`, `review`, `done`, `cancelled`. `backlog` deixa de ser
  status e designa só o conjunto dos itens elegíveis; `in progress` e `in review` passam a
  `in-progress` e `review`; `superseded` fica restrito a plano e iniciativa, e a tarefa tornada
  obsoleta é `cancelled`. O `README.md` §7 espelha a lista e aponta para a residência, sem recopiar a
  máquina de transições nem o alcance por objeto (`EXA-T25`).
- A golden rule de escopo de agente entra em `GOVERNANCA.md` §7 como **guardrail 15** (`G-SCOPE`) —
  o agente se atém estritamente às responsabilidades declaradas, e o que não está escrito é
  proibido, com a matriz de responsabilidades do §3 como autoridade exaustiva; o §3 passa a apontar
  para o guardrail e o espelho do `README.md` §10 sobe no mesmo ato — 14 → 15 guardrails
  (`EXA-T36`).
- A golden rule de superfície de contato entra em `GOVERNANCA.md` §7 como **guardrail 16**
  (`G-SURFACE`) — mudança de decisão estruturante (objetivo-chave, requisito ou caso de uso)
  regulariza no ato a superfície de contato inteira, não só o artefato onde a decisão foi tomada, e
  a rodada de planejamento que fecha a decisão emite os cards de regularização no mesmo ato, sem a
  fila avançar sem eles; o espelho do `README.md` §10 sobe junto — 15 → 16 guardrails (`EXA-T46`).
- A tabela de tetos de turnos (`GOVERNANCA.md` §3) ganha o caso da **rodada de replanejamento** —
  fechar uma decisão e reescrever, no mesmo contexto, os dossiês que ela invalida — com teto **≤50**,
  dentro da classe de redação/planejamento e sem criar classe nova. Calibrado pela série medida
  dessas rodadas (19, 21, 39, 43 e 48 tool uses), três das cinco acima de ≤30. O `README.md`
  espelha, inclusive no gatilho de checkpoint por dois terços do teto.
- Conceito de **perfil** removido do hub: nenhuma marcação `*[perfil ...]*`, nenhum
  `.claude/PERFIL`, nenhum default no hub; conteúdo desktop preservado em `PantonicForDesktop/` e o
  de container em `PantonicForContainer/` (`V2E-T1`..`T4c`).
- Guardrail de MVVM sai da lista de `GOVERNANCA.md` §7 — 15 → 14 guardrails (`V2E-T2`).
- `.claude/checks/dead_code.py` troca as constantes de Qt pelo arquivo opcional
  `.claude/framework-virtuals.txt` do projeto; quem dependia das exceções de Qt passa a declará-las,
  com o modelo pronto para copiar em `PantonicForDesktop/.claude/framework-virtuals.txt`
  (`V2E-T5b`).
- Versão congela em `0.0.0` e as superfícies de versionamento são reconciliadas (`V2E-T9a`,
  `T9c`..`T9e`; esta entrada corresponde à fatia `T9d`).
- Gatilho de revisão da porta de saída de guardrail (`GOVERNANCA.md` §7.1) deixa de pender do
  fechamento de um MINOR e passa a pender do fechamento de um plano (`V2E-T9b`).
- O core deixa de ser descrito por componentes concretos e passa a ser descrito por **dez portas de
  contrato de runtime** (sinais, estado, filesystem, log, registro de plugins, injeção, raiz de
  dados, lifecycle de plugin, superfície de entrada, execução assíncrona): cada porta prescreve
  responsabilidade, operações, invariantes e modos de falha, com a implementação do case sempre
  citada como referência nomeada, nunca como regra universal; a superfície de entrada expõe
  estado/comando/alerta/apresentação/lifecycle e a execução assíncrona mantém a regra de que
  trabalho pesado ou bloqueante nunca corre na thread que atende à entrada. `GOVERNANCA.md` e
  `README.md` passam a espelhar a mesma doutrina, sem duplicar o texto (`V2P-T1`, `T2`, `T4`, `T8`).
- O caso de uso ganha residência própria dentro do plugin: mora em `plugins/<nome>/use_case.py`,
  numa classe `<Nome>UseCase` com um método público de execução, depende só de `contracts` (portas +
  domínio) por injeção, e é exatamente um por plugin — o `plugin.py`/adaptador de apresentação só
  invoca, e a POC de `adhoc/` é orquestrada por ele, não é ele. O manifesto (`manifest.json`) ganha o
  campo obrigatório `use_case` (o nome reconhecido pelo dono, a mesma frase do PRD, único entre
  plugins), com unicidade validada no load. **Nota de migração:** manifesto de plugin já existente
  sem o campo `use_case` não é reconhecido pela validação de load até declará-lo — não há default
  silencioso nem inferência automática do nome (`V2P-T3`).
- A cadeia de auditoria ganha critério objetivo e executável para o caso de uso por plugin:
  `audit-sweep` coleta a existência de `use_case.py`, a classe `^class \w+UseCase` dentro dele e o
  campo `use_case` do manifesto (com a regra de divergência para ausente/vazio/repetido);
  `pantonic-auditor-arch` aplica o mesmo critério nas verificações de "caso de uso por plugin" e "use
  cases finos" (dependência restrita a `contracts`) (`V2P-T5`).
- `bootstrap-pantonic` e `integrar-poc` passam a produzir a residência do caso de uso por padrão:
  projeto novo já nasce com `plugins/<nome>/use_case.py` e o campo `use_case` no manifesto, e POC
  integrada ganha o caso de uso como artefato de saída obrigatório da dissecção, com `plugin.py`
  roteando ao caso de uso em vez de direto a `adhoc` (`V2P-T6`).
- Primeira rodada da porta de saída de guardrails sob o regime da `DE-8`, disparada pelo fechamento
  do plano anterior: 13 dos 14 guardrails vigentes revisados (`G-README` fora por idade), com 6
  isentos por enforcement executável já em produção (regra de dependência, ACL, egress G6, namespace
  de estado, gate de conformance e allowlist de subcomandos destrutivos) (`V2P-T7`).
- A régua de residência (`GOVERNANCA.md` §3.1) separa **autoridade** de **ponto de carga** em três
  classes — canônico, ponto de carga e local de máquina —, com o manifesto único
  `.claude/projecoes.json` como residência canônica das projeções e o materializador
  `.claude/tools/materializar.py` (`apply`/`check`/`drift`) como único caminho de escrita nos
  pontos de carga. O `kit_check` ganha exigência nova cobrindo o canônico (`-Mode validate`) e a
  materialização (`-Mode check-drift`). Os treze artefatos que só existiam em `~/.claude/` (4 hooks
  registrados, 6 skills, 1 agente, 2 docs de doutrina) mais o `CLAUDE.md` global são promovidos a
  projeção de canônico versionado (`RPC-T1..T7`).

## 2.0.0 — 2026-08-05

Fecha a iniciativa `PANTONIC-V2` (`SPRINT-PANTONICV2`, quatro estágios encadeados: benchmarking →
confronto → melhoria → documentação). Consolida o que os MINORs `1.1.0`..`1.5.0` (abaixo) já foram
entregando estágio a estágio, mais o fechamento do Estágio 4:

- **Estágio 1 — Benchmarking** (`P-0729-v2-benchmarking`, T1..T9): 21 frameworks públicos
  avaliados no esquema fixo de 16 dimensões; instituiu o versionamento do próprio kit (`1.1.0`) e o
  agente coletor `pantonic-benchmarker` (`1.2.0`).
- **Estágio 2 — Confronto** (`P-0729-v2-confronto`, T1..T6): diagnóstico do framework contra a
  prática pública registrada; autoria do plano de candidatos do Estágio 3B.
- **Estágio 3A — Doutrina herdada do `P-0722`** (`P-0729-v2-melhoria`, T1..T5): `GOVERNANCA.md` §7
  de 8 para 13 guardrails (`G-DEADCODE`, `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY`,
  `G-EXECREADY`), gate de publicação de plano, contador sequencial de planos, skill
  `modelo-por-fase`, `G-PLANFIDELITY`/`G-EXECREADY` promovidas ao `CLAUDE.md` global, check
  executável de código morto (`dead_code.py`) — ver `1.3.0`/`1.4.0`.
- **Estágio 3B — Mudanças adotadas do benchmarking** (`P-0729-v2-melhoria-candidatos`, T1..T19,
  `T12` partida em `T12a`/`T12b`): checagem MAJOR/MINOR de versão do kit, piso de regressão
  versionado (`tests/piso_comportamental.txt`) com ratchet executável, mapa de residência da
  doutrina e repatriação do que pertencia ao kit, série de telemetria append-only
  (`docs/telemetria.tsv`) escrita pelos dois pontos de fechamento — ver `1.5.0`.
- **Estágio 4 — README espelho e fechamento** (`P-0729-v2-documentacao`, T1..T4 nesta versão; `T5`,
  teste de aceitação pelo dono, permanece aberta como próxima tarefa): `docs/DOC_MAP.md` verificado
  e reancorado (`T1`); `README.md` canônico na raiz — 527 linhas, 13 seções, cada uma com
  `> Fonte da verdade:` declarada, incluindo as afirmações desfavoráveis exigidas em §10/§13 (`T2`);
  guarda executável `.claude/checks/check-readme.ps1` (5 checagens mecânicas: agentes, skills,
  versão, contagem de guardrails, fonte-da-verdade por seção) pendurado como item 8 do
  `guardrails-check` (`T3`); este fechamento de versão (`T4`).
- `GOVERNANCA.md` §9 passa a apontar `README.md` como a porta de entrada humana do framework.
- Skill `proximo-passo`, passo 5: a regra "decisão pendente é o próximo passo" ganha o escopo do
  que **conta** como ponto do dono — só **arquitetura** e **requisitos**. Evento intrínseco do
  projeto (desbloqueio de plano cuja dependência registrada foi satisfeita, flip de status, avanço
  para a fase seguinte de uma iniciativa já aprovada) é consequência mecânica e o agente executa,
  sem consultar. Correção do dono em 2026-08-05, sobre um caso medido: o Estágio 4 da
  `SPRINT-PANTONICV2` foi apresentado como decisão quando a própria heurística do passo 2 já
  mandava destravá-lo. É o erro simétrico ao de decidir arquitetura sozinho (Regra 8 global).

**Justificativa do MAJOR.** A superfície que o consumidor consome mudou: guardrails vinculantes
novos (§7 foi de 8 para 14 itens ao longo da iniciativa, incluindo o contrato novo do piso de
regressão que exige `tests/piso_comportamental.txt` no lado do consumidor), artefatos novos no kit
(`dead_code.py`, `ratchet_piso.py`, `check-readme.ps1`, skill `modelo-por-fase`) e o `README.md`
canônico como novo ponto de decisão. Não é só acréscimo compatível — o piso de regressão *muda de
formato* (contagem/percentual → lista versionada), o que exige uma ação do consumidor para não
quebrar a checagem. MAJOR é o número correto, não o placar da iniciativa.

**Nota de migração — `PantonicVideo` (único consumidor real hoje).** Medido nesta tarefa,
2026-08-05: o `PantonicVideo` está em estado **pré-kit** — não tem `.claude/KIT_VERSION` nenhum
(nem `.claude/kit/KIT_VERSION` nem `.claude/KIT_VERSION`), sua cópia de `.claude/` é manual, não
via `git subtree`/`sync-kit.ps1`. Por isso o diff relevante para aquele projeto não é incremental
(`1.5.0` → `2.0.0`); é a distância entre uma cópia manual antiga e o kit inteiro publicado até
`2.0.0`. Ao passar a consumir via `sync-kit.ps1`:
  - **Guardrails novas que passam a valer:** os 6 guardrails do Estágio 3A/3B (`G-DEADCODE`,
    `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY`, `G-EXECREADY`, allowlist de subcomandos
    destrutivos) e o contrato novo do piso de regressão — o `PantonicVideo` precisa criar
    `tests/piso_comportamental.txt` (`V2K-T14`) para o gate `ratchet_piso.py` (item 7 do
    `guardrails-check`) não falhar por ausência de arquivo.
  - **Colisão com `.claude/kit-exclude.txt`, encontrada nesta tarefa:** a entrada
    `skills/guardrails-check` (declarada para proteger o perfil local do `PantonicVideo`,
    `P-0721` Fase 1a) protege exatamente o caminho onde o hub acabou de adicionar o item 8 (guarda
    do espelho, `check-readme.ps1`) na `T3` deste estágio. Consequência: o `sync-kit.ps1`, ao
    respeitar o override, **não vai propagar** o item 8 nem a linha `Espelho:` do veredito para o
    `PantonicVideo` — quem mantém o `skills/guardrails-check` local daquele projeto precisa
    incorporar essa checagem manualmente se quiser o mesmo guarda lá (esse `README.md`/
    `check-readme.ps1` não fazem parte do subtree em si — só a entrada de `guardrails-check` que os
    invoca é o ponto de colisão). As outras duas entradas do `kit-exclude.txt`
    (`agents/pantonic-executor`, `skills/integrar-poc`) não colidem com nenhum artefato novo desta
    iniciativa.
  - Esta nota é só **relato**; nenhuma alteração foi feita em `d:\workspaces\PantonicVideo`
    (`GOVERNANCA.md` §10a) — a divergência de versão daquele projeto é reportada ao dono, não
    aplicada por agente.

## 1.5.0 — 2026-08-04

- `V2K-T13`: checagem de versão do kit passa a distinguir MAJOR de MINOR/PATCH — divergência em
  MAJOR é reportada como incompatível e para (sem perguntar se atualiza/posterga); divergência em
  MINOR/PATCH mantém o comportamento anterior (`checar-versao-kit`, `GOVERNANCA.md` §10, `C-14`).
- `V2K-T14`: piso de regressão deixa de ser contagem/percentual de testes e passa a ser lista
  versionada de comportamentos trancados (`tests/piso_comportamental.txt`); remover um
  comportamento é ato do dono no mesmo commit que remove o teste (`GOVERNANCA.md` §4.4, `C-11`a).
- `V2K-T15`: `.claude/checks/ratchet_piso.py` (novo) materializa o ratchet do piso comportamental;
  `guardrails-check` ganha item 7 bloqueante que o invoca (`C-11`b).
- `V2K-T16`: `docs/RESIDENCIA_DOUTRINA.md` (novo) classifica os 36 itens do `~/.claude/CLAUDE.md`
  global em `global`/`Pantonic`/`dividir`, ratificado pelo dono (`C-12`a).
- `V2K-T17`: residência da doutrina do `~/.claude/CLAUDE.md` global corrigida — a disciplina de
  coleta condensada (git, listagens, arquivos grandes, comandos verbosos), o batching de chamadas
  independentes e a cadência de testes passam a viajar em `GOVERNANCA.md` §3/§4.4 (kit); a
  telemetria medida pela notificação (nunca auto-relato) passa a residir em `GOVERNANCA.md` §4.2.
  O que era só duplicata (onboarding ATIVO/HISTÓRICO, DOC_MAP, fatos estáveis de agente, modelo
  por fase, orçamento de turnos) saiu do global, que mantém apenas o princípio condensado
  apontando para o kit.
- `V2K-T18`: `docs/telemetria.tsv` (novo) — formato append-only da série de consumo (`data`,
  `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte`), semeado com 39
  linhas re-derivadas dos bullets `Consumo:` existentes no diário/histórico (`C-13`a).
- `V2K-T19`: a série de telemetria passa a ser escrita pelos dois pontos de fechamento — a skill
  `handover` e o passo 5 da skill `proximo-passo` apendem uma linha a `docs/telemetria.tsv`
  (`fonte` ∈ `{usage, contado, nao_medido}`) e o diário passa a **apontar**
  (`Consumo: ver docs/telemetria.tsv`) em vez de copiar o número; `GOVERNANCA.md` §4.2 declara o
  TSV **fonte única** da série, com o registro qualitativo (estouro de teto, execução inline)
  seguindo no bullet do diário ao lado do ponteiro (`C-13`b).
- **Nota de versão.** O `DK-9` (`docs/plans/P-0729-v2-melhoria-candidatos.md` §5) reservava
  `1.4.0` para este fechamento, mas essa versão já havia sido consumida pelo fechamento do Estágio
  3A; o Bloco C fecha em `1.5.0` por decisão do dono (2026-08-04). Continuam sendo **dois** bumps
  MINOR na iniciativa, como o `DK-9` previu — mudou só o número do segundo.

## 1.4.0 — 2026-07-30

- `GOVERNANCA.md` §7 passa de **8 para 13 guardrails**: **G-DEADCODE** (proibição de código morto
  testado — cobertura por teste não confere "vivo"; rota abandonada morre no mesmo commit),
  **G-PLANFIDELITY** (executor não troca a rota arquitetural aprovada; para e escala),
  **G-PREMISE** (premissa que embasa abandono de rota exige spike, não asserção),
  **G-PLANREADY** (dever do planejador — 5 condições de fechamento de plano) e **G-EXECREADY**
  (dever do executor — não decide, não pergunta, recusa plano não-pronto). Cada uma nasce com
  enforcement declarado (`V2M-T1`, `docs/plans/P-0729-v2-melhoria.md` §3; doutrina herdada do
  `P-0722`, ratificada em 2026-07-22).
- **G-PLANREADY item 5 — gate de publicação** (decisão do dono 2026-07-29, doutrina nova): plano
  não se publica em aberto; trabalho que depende de insumo futuro divide-se em dois planos, e o
  dependente é autorado já fechado como a última tarefa do plano que produz o insumo.
- **Contador sequencial de planos materializado** (`V2M-T4`): a regra já normativa no
  `GOVERNANCA.md` §7 (`G-PLANREADY` item 1, `P-NNNN-<slug>.md` com `NNNN` monotônico global,
  nunca reutilizado) ganha registro executável — `docs/plans/_INBOX.md` passa a ser o registro do
  contador, com o próximo id declarado no cabeçalho (`P-0730`); elimina a colisão de nomenclatura
  por data que gerou dois `P-0722` e quatro `P-0729`. Superfícies do kit alinhadas
  (`.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`); os
  planos existentes `P-0721`..`P-0729` são grandfathered — mantêm o nome atual, não renomeados.
- Materializado o enforcement nos três artefatos do kit que executam essas regras: `G-EXECREADY`
  virou o **passo 1** do protocolo do agente `pantonic-executor` (recusa plano não-pronto antes de
  qualquer edição), `G-PLANREADY` virou gate explícito da skill `proximo-passo` (não delega tarefa
  de plano aberto) e da skill `diario-de-obras` (operação "Registrar plano" verifica o gate antes
  de apensar) (`V2M-T1`).
- `GOVERNANCA.md` §3 ganhou o **gatilho operacional do modelo por fase**: ponteiro para a skill
  `modelo-por-fase` do kit versionado, com a residência declarada sob a régua de §3.1 — a regra
  mora na doutrina versionada, a skill é gatilho e o hook (global) é enforcement (`V2M-T1`; a
  skill em si é a `V2M-T2`).
- Criada a skill `.claude/skills/modelo-por-fase/SKILL.md` — gatilho operacional da regra de
  modelo por fase: três gatilhos (início de tarefa/subagente, troca de fase na mesma sessão,
  nudge do hook global), gate de parada (pedir `/model` explícito ao dono, nunca decidir/trocar
  sozinho) e a convenção de anúncio da Regra 5. Reside **no kit versionado**, não em
  `~/.claude/skills/` — `DM-7` (2026-07-30) rebaseia a `DP-G3` de 2026-07-22 pela régua de
  residência de `GOVERNANCA.md` §3.1 (skill que só existe fora do repo não viaja no subtree).
  Revisado também `~/.claude/hooks/modelo_por_fase_userpromptsubmit.py` (global, fora do kit):
  falso positivo medido (prompt de retomada de backlog classificado como "execução mecânica"
  quando o trabalho real era orquestração/delegação) corrigido com uma lista de exclusão
  checada antes da classificação (`V2M-T2`).
- **G-PLANFIDELITY e G-EXECREADY promovidas ao `~/.claude/CLAUDE.md` global** como Regra 8
  (conduta universal de executor, não doutrina específica de Pantonic): `GOVERNANCA.md` itens 10
  e 13 passam a apontar para o texto normativo global em vez de duplicá-lo (nome do item e
  *Enforcement* preservados). Absorvido no mesmo ato o `TK-01` (achado fora de escopo da
  `V2M-T2`): `GOVERNANCA.md` §3 e o bullet acima corrigidos para descrever a skill
  `modelo-por-fase` como residente no kit versionado, não `~/.claude/skills/` (`V2M-T3`).
- **`V2M-T5` fechada — check executável de código morto testado (G-DEADCODE), Estágio 3A
  encerrado 5/5.** `.claude/checks/dead_code.py` (alcançabilidade por AST a partir de entry
  points, três rodadas de ajuste estrutural — auto-vivo para POC/seed de diretório, import
  relativo em `_resolve_import_targets`, override de virtual Qt) wireado como item **6**,
  bloqueante, do "Checklist executável" de `.claude/skills/guardrails-check/SKILL.md`. Baseline do
  `PantonicVideo` confirmado em `exit 0` pela campanha `SPRINT-DEADCODE` daquele repositório (92
  símbolos removidos, `docs/plans/P-0730-limpeza-codigo-morto.md`), destravando o gate que estava
  bloqueado desde 2026-07-30. Confirmado nesta sessão: `python .claude/checks/dead_code.py`
  (root = PantonicApp) e `--root D:\workspaces\PantonicVideo` → `OK - 0 achado(s)` nos dois; fixture
  sintética (`orphan_helper` referenciado só por teste) → exit 1, 1 achado exato.
- `.claude/skills/scrum-master/SKILL.md` condensada de 22.443 para 14.980 chars (prosa —
  justificativa, racional e exemplo — virou ponteiro para `GOVERNANCA.md` ou caiu; passo, gate,
  contador e roteamento ficam idênticos); a 7ª âncora `G-SURFACE`, viva desde a `CTX-T1c`, é
  removida, fechando o achado e tornando a `CTX-T1e` desnecessária (`CTX-T9`).

## 1.3.0 — 2026-07-30

- Criado o validador estrutural do kit `.claude/checks/kit_check.ps1 -Mode validate`: confere a
  estrutura de `.claude/` (agentes, skills, checks) e a paridade `VERSION` == `.claude/KIT_VERSION`
  exigida por `GOVERNANCA.md` §10 (`V2K-T1`, `docs/plans/P-0729-v2-melhoria-candidatos.md` §3).
- Adicionados os modos `-Mode generate` e `-Mode check-drift` ao mesmo script: o índice
  `.claude/README.md` passa a ser **gerado** a partir do disco e a deriva entre índice e conteúdo
  real vira falha detectável (defeito medido na adoção: 8/9 agentes e 6/8 skills listados)
  (`V2K-T2`, mesmo plano).
- Declarado em `GOVERNANCA.md` §9 que o enforcement do kit é **código**: `.claude/README.md` é
  artefato derivado que não se edita à mão, `kit_check.ps1` é o comando canônico, e regra do kit
  não verificável pelo script nasce com o motivo escrito. Os dois modos foram pendurados no gate
  `guardrails-check` (item 5 do checklist executável + linha `Kit:` no veredito) (`V2K-T3`, mesmo
  plano; fecha o Bloco A de enforcement executável).
- Declarada a topologia da própria doutrina em `GOVERNANCA.md` §3.1: tabela das quatro superfícies
  (CLAUDE.md global · doutrina versionada · skill · agente) com o que mora e o que não mora em cada
  uma, duas regras de precedência (específico vence geral; empate → versionado vence
  não-versionado) e o teste de residência em quatro perguntas. Hook é declarado mecanismo de
  enforcement, não quinta superfície (`V2K-T4`, mesmo plano; fecha o Bloco A).
- Regra nova no passo de handover da skill `proximo-passo`: quando a tarefa executada deixa um
  ponto para o dono decidir, o próximo passo sugerido é **a decisão**, com fato medido, implicação
  de cada opção, o que trava sem resposta e recomendação — não a próxima tarefa do backlog.

## 1.2.0 — 2026-07-29

- Criado o agente coletor `pantonic-benchmarker` (Haiku, somente `Read/Write/Glob/Grep/WebFetch`)
  e materializado o esquema fixo de 16 dimensões em `docs/benchmark/_ESQUEMA.md`; agente listado
  em `.claude/README.md` (`V2B-T2`, `docs/plans/P-0729-v2-benchmarking.md` §5).

## 1.1.0 — 2026-07-29

- Instituído o controle de versão do framework: `VERSION` (raiz) e `.claude/KIT_VERSION` passam a
  carregar sempre o mesmo valor, com a regra de paridade e o significado de MAJOR/MINOR/PATCH
  documentados em `GOVERNANCA.md` §10 (`V2B-T1`, `docs/plans/P-0729-v2-benchmarking.md` §5).

## 1.0.1 — versão anterior publicada por tag (`kit-v1.0.1`)

## 1.0.0 — versão anterior publicada por tag (`kit-v1.0.0`)
