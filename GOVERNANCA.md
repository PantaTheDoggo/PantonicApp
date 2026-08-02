# GOVERNANÇA — Projetos Pantonic*

> **Audiência:** este documento é escrito para o **agente de planejamento** de um projeto
> Pantonic*. Lendo este documento e o [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md), o
> agente deve ser capaz de idealizar um projeto funcional, consistente com a família Pantonic*,
> com processo suficiente para garantir a qualidade do produto.

---

## 1. Identidade de uma aplicação Pantonic*

Premissas repetíveis, válidas para todo projeto da família:

1. **Desktop-first** — aplicações majoritariamente desktop.
2. **Stack fixo** — Python + PySide6, arquitetura base **MVVM** (apropriada para desktop).
3. **Obsessão por clean architecture, clean code e melhores práticas** — não é aspiração, é
   guardrail (ver §7).
4. **Core comum reusável** — a camada de infraestrutura segue o core "pantonico" descrito em
   [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md). Nenhum projeto reinventa infraestrutura.
5. **Extensibilidade por plugins** — toda evolução funcional entra como plugin (ver §5).

## 2. Core comum e diversificação por camada

- Todo projeto **adota o mesmo core pantonico** (infracore + contracts genéricos + serviços de
  expressão), conforme o documento de arquitetura reusável.
- A **diversificação acontece nas camadas inferiores da clean architecture**: domínio e casos de
  uso. Regra mental para o planejador:

  | Altura na clean architecture | Grau de especialização |
  |---|---|
  | Domínio (entidades, VOs) | Máxima — único por projeto |
  | Casos de uso / serviços de domínio | Alta — único por projeto |
  | Serviços de expressão / ACL | Baixa — padrão do core |
  | Infraestrutura (infracore, UI shell) | Nenhuma — idêntico entre projetos |

  Quanto mais baixo (próximo ao domínio), mais especializadas as classes; quanto mais alto
  (infraestrutura), mais as aplicações Pantonic* se parecem entre si.

## 3. Operações agênticas

Todo projeto pantonico opera com três agentes, cada um no modelo adequado ao seu custo:

| Agente | Modelo | Responsabilidade |
|---|---|---|
| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decomposição em checklists de tarefas atômicas |
| **Execução** | Melhor custo-benefício (Sonnet) | Implementar uma tarefa do checklist por vez, TDD, em contexto limpo |
| **Coleta** | O mais barato (Haiku ou equivalente) | Search, grep, leitura de codebase/documentos/prompts; filtra e devolve só o pertinente para o contexto dos agentes mais caros |

Regras de operação:

- O agente de coleta existe para **proteger o contexto dos agentes caros**: varreduras amplas
  nunca são feitas diretamente pelo agente de planejamento ou de execução; são delegadas à
  coleta, que devolve dossiês compactos (caminhos, linhas, assinaturas — nunca arquivos inteiros).
- O agente de planejamento nunca executa; o agente de execução nunca replaneja escopo — se a
  tarefa se mostrar mal decomposta, ele para, registra o bloqueio no diário de obras e faz
  handover.
- **Modelo por fase é vinculante, não preferência.** Uma preferência de dono ("usar modelo caro
  sempre") não pode inverter a tabela acima para um agente de **execução** — mudar o `model:` de
  um executor para um modelo mais caro exige OK explícito e registrado, nunca herança silenciosa
  de uma memória genérica (custo real medido: executor em Opus com 71 turnos e ~189k de contexto
  numa única tarefa atômica, ~30% do limite de 5h — ver auditoria de consumo referenciada em
  `~/.claude/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`).
- **Gatilho operacional do modelo por fase:** a regra acima é vinculante, mas precisa de gatilho —
  a skill `modelo-por-fase` **do kit versionado** (`.claude/skills/modelo-por-fase/`; `DM-7`,
  2026-07-30, rebaseia `DP-G3` — skill que só existisse em `~/.claude` não viajaria no subtree)
  detecta a fase da tarefa e o modelo ativo, **para** e pede o `/model` correto ao dono (fato
  técnico medido: um agente não troca o próprio modelo — só o dono, via `/model`, ou o harness,
  via hook global). A **regra** mora aqui, versionada (§3.1); a skill é só o gatilho e o **hook**
  em `settings.json` continua global — nenhum dos dois é superfície de doutrina.
- **Delegar a um subagente protege o contexto do orquestrador (Regra 2 do CLAUDE.md), não reduz
  o consumo total.** O subagente parte frio e paga de novo CLAUDE.md + definição do agente +
  skills carregadas em todos os seus turnos. Tarefa pequena (< ~15 turnos estimados) prefere
  execução inline a abrir um subagente.
- **Orçamento de turnos por tarefa atômica — teto graduado por classe.** O teto único de ~≤40 tool
  uses tratava tarefas de naturezas diferentes como se custassem o mesmo. Cada classe tem teto
  próprio, calibrado pela série medida das linhas `Consumo:` deste repositório (26 registros em
  2026-08-01), nunca por estimativa:

  | Classe de tarefa | Teto | Como reconhecer |
  |---|---|---|
  | Mecânica / pontual | **≤15** | 1 write-cluster, arquivo(s) já conhecido(s), sem contrato novo |
  | Implementação padrão | **≤40** | vários write-clusters numa camada; contrato novo mas verificação direta |
  | Comportamental multi-camada | **≤60**, com **teto numérico por ramo obrigatório no dossiê** | muda contrato ou fluxo; ciclo editar-rodar-depurar (sync→async, timing de teste) |
  | Investigação / mapeamento | **sem default** — o teto é **prescrito no dossiê** junto do método de sondagem | o entregável é descoberta, não mudança de código |
  | Redação de doutrina / planejamento | **≤30** | edita `GOVERNANCA.md`/plano/skill; o custo é decisão, não build |

  A **classe é escolhida no dossiê, antes de delegar**, e fica registrada nele. Estourar o teto da
  classe é sinal de decomposição errada — **replanejar, não continuar** (reportar no handover, não
  só seguir). Escolher classe mais generosa **depois** do estouro é falsificação da série: vale a
  classe registrada antes da delegação.

  O **≤30** da última classe é correção da série sobre a estimativa inicial de ≤25: das 7 tarefas de
  redação já medidas, 5 estouravam ≤25 e só 2 estouram ≤30. Quando série medida e estimativa
  divergem, manda a série.
- **Decisão que escolhe mecanismo de plataforma exige sonda de viabilidade junto da
  recomendação, não só depois.** Medido na iniciativa do hub único de governança (`P-0721`/
  `P-0725`, 2026-07): três premissas caíram por sondagem curta demais antes de escolher o
  mecanismo — symlink de arquivo exige privilégio elevado no Windows, os filhos não eram
  repositórios git, e os filhos já tinham cópia manual dos docs de doutrina. Cada uma exigiu
  retrabalho de plano que uma sonda de 1-2 comandos, feita antes da recomendação, teria evitado.
- **Um plano que absorve uma fase de outro herda as tarefas, não o título da fase.** "Fase X
  absorvida pela Fase Y" é uma afirmação numa granularidade mais grossa que o objeto afirmado;
  medido em `P-0725` (2026-07-26) quando uma fase de quatro tarefas do plano de origem se
  espalhou por duas fases do plano sucessor e uma tarefa (autorar o materializador) não caiu em
  nenhuma das duas — só apareceu quando um passo posterior tentou consumi-la e o insumo não
  existia. Rebase que absorve fase de outro plano mapeia tarefa a tarefa, não fase a fase.

### 3.1 Residência e precedência da doutrina

A doutrina Pantonic vive em quatro superfícies. Esta tabela **decide** o que mora em cada uma e
quem vence quando duas dizem coisas diferentes sobre o mesmo assunto — não descreve a topologia
atual, prescreve a correta.

| Superfície | Mora aqui | Não mora aqui | Versionada |
|---|---|---|---|
| `~/.claude/CLAUDE.md` — global do dono | Regra sempre-ativa que vale para **qualquer** projeto do dono, Pantonic ou não | Qualquer regra que só faça sentido dentro do framework Pantonic | Não |
| `GOVERNANCA.md` / `ARQUITETURA_PANTONICA.md` — kit | Regra sempre-ativa **do framework**: identidade, camadas, operações agênticas, guardrails, versionamento | Passo a passo de procedimento; preferência pessoal do dono; estado de trabalho | Sim |
| Skill — `.claude/skills/*/SKILL.md` | Procedimento reexecutável, com gatilho declarado e passos na ordem de execução | Regra que precisa valer sem ninguém invocar a skill; estado volátil (backlog, versões, progresso) | Sim |
| Agente — `.claude/agents/*.md` | Papel (o que faz e o que não faz) + fatos estáveis que ele precisa saber a frio | Doutrina geral copiada do `GOVERNANCA.md`; estado volátil; dossiê de tarefa | Sim |

Hook (`settings.json`) **não é uma quinta superfície**: é mecanismo de enforcement de uma regra que
já mora em uma das quatro. Hook sem regra escrita atrás dele é doutrina invisível — e não viaja.

**Precedência, quando duas superfícies colidem:**

1. **Específico vence geral.** Dentro de um projeto Pantonic, `GOVERNANCA.md` vence o CLAUDE.md
   global; dentro de uma tarefa, o dossiê vence a skill, que vence o agente. O geral só vale onde
   o específico é silencioso.
2. **Empate → versionado vence não-versionado.** Se as duas superfícies têm a mesma
   especificidade, ganha a que viaja no kit. Um consumidor que recebe o kit por `git subtree`
   **não recebe** o que está fora do repositório (achado `BM-00§D15`): regra que só existe no
   `~/.claude` do dono não chega a consumidor nenhum e, por isso, não é doutrina do framework.

Colisão não se resolve com as duas cópias vivas: quem aplica a regra 1 ou 2 **apaga a cópia
perdedora ou a reduz a ponteiro**, no mesmo ato. Duplicata é a próxima divergência.

**Teste de residência — quatro perguntas na ordem; a primeira que der "sim" decide:**

1. Vale para um projeto **não-Pantonic** do dono? → `~/.claude/CLAUDE.md` global.
2. É regra **sempre-ativa do framework**, que precisa valer sem ninguém invocar nada? →
   `GOVERNANCA.md` (ou `ARQUITETURA_PANTONICA.md`, se for regra de arquitetura).
3. É **procedimento reexecutável com gatilho** ("quando acontecer X, fazer estes passos")? → skill.
4. É **papel + fatos estáveis** de quem executa? → agente.

Nenhuma das quatro: não é doutrina. É estado de trabalho, e o lar é o diário de obras.

**Ponteiro, não cópia:** a governança das memórias do harness — incluindo a fila de candidatos, em
que o agente enfileira e **só o dono promove** — passa na pergunta 1 e mora em
`~/.claude/docs/GOVERNANCA_MEMORIAS.md` (§8), **fora do kit e fora da distribuição**.

## 4. Fluxo de desenvolvimento

### 4.1 Regra básica

Todo procedimento mais complexo **invoca o agente de planejamento** para criar um **checklist de
tarefas atômicas**, descritivo o suficiente para que o agente de execução **não precise fazer
buscas transversais** à tarefa (o custo de contexto da exploração é pago uma vez, no
planejamento — com apoio do agente de coleta).

Uma tarefa atômica bem escrita contém: objetivo, arquivos-alvo (caminho exato), contratos/classes
envolvidos, testes que devem passar ao final e critério de pronto.

### 4.2 Diário de obras

Todo planejamento é arquivado num documento centralizado, o **diário de obras**, que funciona
também como um kanban adaptado:

- Recebe planejamentos completos (sprints) e tíquetes avulsos.
- Cada item de trabalho carrega um **status**: `backlog`, `in progress`, `in review`, `blocked`,
  `done`, `cancelled`.
- Possui um **índice abrangente no topo** (uma linha por item: ID, título, status, âncora), de
  modo que o agente de execução encontre seu trabalho **sem ler seções irrelevantes** ao seu
  contexto. O índice é atualizado a cada mudança de status.
- Itens concluídos são condensados periodicamente para um histórico append-only, mantendo o
  diário enxuto (mesma disciplina ATIVO × HISTÓRICO usada nos demais docs do projeto).
- **Diretiva de priorização** — uma linha fixa no topo do diário, logo abaixo do título,
  registrando a prioridade vigente (ex.: "Priorize iniciativa X"). Vazia por padrão (prioridade
  fica a cargo do agente, heurística: destravar `blocked` → concluir `in progress`, WIP de 1
  iniciativa por vez → bugs → demais por FIFO). Só muda por escrita explícita no diário — nunca
  inferida de uma conversa que não persistiu a decisão, para sobreviver à troca de contexto.
- **Entrada de planos paralelos** — quando múltiplos agentes de planejamento rodam em paralelo,
  nenhum escreve plano completo direto no diário (risco de conflito de edição). Cada um grava seu
  plano em `docs/plans/P-<MMDD>-<slug>.md` e apensa **uma linha** a `docs/plans/_INBOX.md`
  (append-only). O inbox é drenado para o índice do diário na próxima sessão que o utilizar.
- **Dossiê de tarefa aponta e verifica.** "Arquivos-alvo" carrega `caminho:linha`; "Verificação"
  carrega o **comando**, copiado do terminal, não a intenção de verificar. `caminho:linha` é
  ponteiro de leitura — envelhece e **não** se mantém; tratá-lo como contrato custa mais do que
  entrega.

### 4.3 Execução em contexto limpo

- **Toda tarefa ocorre dentro de um contexto limpo.** O agente nunca desenvolve várias tarefas
  no mesmo contexto.
- Ao concluir (ou bloquear) uma tarefa, o agente atualiza o diário de obras e **faz handover para
  o usuário**, que limpa o contexto e invoca a próxima tarefa em nova sessão.
- **Retomada sem tarefa nomeada** — quando o usuário abre um contexto novo e pede apenas para
  seguir o backlog ("execute o próximo passo"), o ponto de entrada é a skill `proximo-passo`: ela
  drena o inbox de planos, aplica a diretiva de priorização (ou a heurística padrão), escolhe uma
  única tarefa e delega ao agente de execução. O handover final sempre reporta a tarefa feita, a
  iniciativa/plano de origem, e o **índice de conclusão do plano** (`<done>/<total>` no diário).
- **Contexto acabando sem plano de parada** — quando o consumo cruza **2/3 do teto da classe**
  (§3) com a tarefa ainda aberta, o executor grava um **checkpoint intermediário** (skill
  `handover`, seção "Checkpoint intermediário"): até 5 linhas de ponteiro de estado, teto de
  2 tool uses, para que o contexto seguinte retome sem redescobrir o que já foi pago.

### 4.4 TDD obrigatório

Todo desenvolvimento segue TDD, garantindo prioritariamente dois tipos de teste:

- **Funcionais (TF)** — verificam se a função faz o que deve fazer; derivados dos casos de uso e
  requisitos do PRD, definidos já no Sprint Plan.
- **Regressão (TR)** — verificam que um estado funcional anterior não quebrou (ausência de
  colaterais). Formam um **piso de regressão**: o número de testes verdes nunca diminui; um teste
  cujo significado muda intencionalmente é reescrito, nunca deletado.

## 5. Fluxo de extensão (plugins)

A extensão de capacidades ocorre **exclusivamente por plugins**: incrementos funcionais
**atômicos**, com propósito e operação específicos, **não conflitantes** com outros plugins
(comunicação apenas por sinais e estado — nunca acoplamento direto; ver arquitetura §9).

Fluxo de trabalho para toda nova funcionalidade:

1. **POC separada** — cria-se uma prova de conceito fora da aplicação, com a finalidade
   pretendida, funcionando standalone.
2. **Estresse e validação** — a POC é estressada até que o **cliente valide** o atendimento da
   necessidade. Nada é integrado antes dessa validação.
3. **Integração** — os agentes **dissecam a POC nas camadas da clean architecture** (o que é
   domínio, o que é caso de uso, o que vira serviço/ACL, o que fica como código ad-hoc do
   plugin) e inserem o código na aplicação Pantonic*, seguindo a doutrina de integração do
   documento de arquitetura (§9).
4. **Teste do conjunto** — TF do plugin + suíte de conformance + piso de regressão completo.

## 6. Fluxo de projeto — os quatro artefatos iniciais

Um projeto Pantonic* inicia com quatro artefatos, produzidos nesta ordem pelo agente de
planejamento:

1. **PRD** — coleta os objetivos da aplicação; determina casos de uso, elementos de domínio,
   requisitos, estruturas de dados e **linguagem ubíqua** necessários para construir as camadas
   de domínio e de casos de uso segundo a clean architecture.
2. **Architecture** — modelo conceitual da arquitetura com base em MVVM + clean architecture,
   **partindo do core pantonico** ([ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md)) e
   especializando as camadas baixas. Determina os limites de cada camada e as responsabilidades
   de cada uma; **cada responsabilidade é mapeada aos casos de uso e requisitos do PRD**
   (rastreabilidade Feature → UC/RF → responsabilidade).
3. **Spec** — especifica as classes Python que materializam as responsabilidades do Architecture:
   filesystem proposto, assinaturas das classes, docstrings, e técnicas de projeto que garantam o
   desacoplamento tecnológico (inversão de dependência, strategy, unit of work, etc.).
4. **Sprint Plan** — organiza o Spec nos checklists a serem registrados no diário de obras,
   prontos para handover de execução. Os checklists são ordenados para que **os entregáveis sejam
   rapidamente testáveis pelo usuário** (fatias verticais finas antes de camadas horizontais
   completas). O Sprint Plan também define os **testes funcionais** que validarão a efetividade
   do desenvolvimento, além dos demais critérios de aceite.

## 7. Guardrails dos agentes

Todos os agentes operam sob guardrails que evidenciam a obsessão por clean architecture e clean
code, impedindo violação de camadas e princípios. Mínimo obrigatório em todo projeto:

1. **Regra de dependência inviolável** — `infracore ← contracts ← services ← plugins`, nunca no
   sentido inverso. Enforcement automatizado por testes de conformance (análise AST de imports),
   não por convenção.
2. **ACL** — toda dependência externa (biblioteca, OS, filesystem, rede) pertence a exatamente um
   serviço; nenhum outro módulo a importa.
3. **MVVM estrito** — geometria/estilo Qt só na shell e Views; ViewModel é QtCore-only (sem
   widgets); Model é puro (sem Qt).
4. **Egress único de filesystem** — só o componente de filesystem escreve em disco (regra G6 da
   arquitetura), verificado por teste AST.
5. **Namespace de estado** — plugin só escreve em `plugins.<nome>.*`, salvo whitelist explícita;
   verificado por teste de boundary.
6. **Gate de conformance** — a suíte de conformance é bloqueante: nenhuma tarefa é `done` com
   conformance vermelho.
7. **Piso de regressão** — o piso nunca desce; mudanças comportamentais intencionais exigem
   registro de decisão no doc de estado vigente do projeto.
8. **Disciplina de contexto** — uma tarefa por contexto; varreduras amplas só via agente de
   coleta; docs grandes acessados via índice/DOC_MAP, nunca lidos integralmente.
9. **G-DEADCODE — nada de código morto testado** — todo símbolo de produção (função/classe/módulo
   fora de `tests/`) precisa de **ao menos um chamador de produção** alcançável a partir de um entry
   point real (plugin registrado, superfície de serviço no contrato, bootstrap). Cobertura por teste
   **não** confere "vivo": símbolo testado sem chamador é o pior caso, porque a suíte verde o
   **mascara**. Ao abandonar uma rota, os módulos da rota abandonada morrem **no mesmo commit** —
   nunca ficam como fantasmas testados. *Enforcement:* check executável de símbolo de produção órfão
   (alcançabilidade por AST a partir dos entry points, allowlist explícita e mínima) no kit de
   conformance; o handover declara os chamadores de produção de cada símbolo novo; review de
   fechamento rejeita módulo novo sem chamador não-teste.
10. **G-PLANFIDELITY — a rota é do dono** — conduta universal de executor (não doutrina específica
   de Pantonic), promovida ao `CLAUDE.md` global (Regra 8, `V2M-T3`, 2026-07-30): o executor não
   substitui a arquitetura/rota aprovada por uma alternativa própria sob pressão de obstáculo
   técnico — ver texto normativo lá. *Enforcement:* gate de review — o handover cita a rota do
   plano e confirma que nenhuma bifurcação arquitetural ocorreu sem decision record.
11. **G-PREMISE — premissa que embasa abandono exige prova, não asserção** — afirmar *"a informação X
   não existe / não é obtível"* só sustenta abandono ou bifurcação de rota com um **spike que a
   comprove**, revisável pelo dono, **antes** do abandono. Um achado não **reverte** achado anterior
   de outra sprint sem reconciliação explícita registrada. Corolário: se a solução do obstáculo
   apareceu na rota alternativa, verifique **primeiro** se ela cabe na rota original — normalmente
   cabe. *Enforcement:* gate de review no fechamento da tarefa que abandona/bifurca; o decision record
   cita o spike e reconcilia qualquer achado contraditório.
12. **G-PLANREADY — plano só é executável quando fechado** (dever do **planejador**) — antes de um
   plano ser registrado como pronto, cinco condições:
   1. **Nomenclatura sequencial.** `P-NNNN-<slug>.md`, com `NNNN` contador global monotônico
      (não a data), zero-padded, **nunca reusado**; próximo id = maior registrado no `_INBOX.md` + 1.
      A data de origem vira campo de cabeçalho. Motivo: `P-<MMDD>` colide — houve dois `P-0722` no
      mesmo dia.
   2. **Tarefas `T1..Tn` sequenciais**, em ordem de dependência, cada uma com objetivo, "pronto
      quando" e modelo da fase. Uma tarefa por contexto.
   3. **Todas as decisões tomadas no fechamento — nada postergado.** Nenhuma escolha owner-gated
      fica "a resolver na execução": decisão adiada acaba tomada pelo executor, no modelo mais
      barato e sem o contexto de quem decidiu — a fase intelectual vazando para a fase de execução.
   4. **Linear.** Sem referência para frente, sem ramo condicional não resolvido, sem "TBD". O
      executor lê de cima a baixo e sabe o que fazer sem inferir.
   5. **Gate de publicação — plano não se publica em aberto.** Um plano só é registrado no
      `_INBOX.md` e no diário quando está **fechado**: sem questão pendente, sem bloco a preencher,
      sem tarefa cujo conteúdo dependa de artefato que ainda não existe. Plano aberto é escolhível
      pela `proximo-passo` e **para o executor no meio**, forçando o retrabalho de revisitar a
      questão no pior momento. Revisar um plano publicado é legítimo e esperado; publicá-lo
      incompleto não é. **Consequência operacional:** quando parte do trabalho depende de um insumo
      futuro, não se publica um plano com um vão — **divide-se em dois**: o fechado agora, e o
      dependente, autorado **já fechado** como a última tarefa do plano que produz o insumo. Um
      plano por nascer não é backlog invisível: ele tem dono, é uma tarefa nomeada de outro plano.
   *Enforcement:* checklist de fechamento de plano (as 5 condições); a skill `diario-de-obras`
   ("Registrar plano") verifica o gate antes de apensar; a `proximo-passo` recusa delegar tarefa de
   plano que viole qualquer uma; o executor recusa performar (G-EXECREADY); o `_INBOX.md` é o
   registro do contador sequencial.
13. **G-EXECREADY — o executor não decide, não pergunta e recusa plano não-pronto** (dever do
   **executor**) — conduta universal de executor (não doutrina específica de Pantonic), promovida
   ao `CLAUDE.md` global (Regra 8, `V2M-T3`, 2026-07-30): nunca inicia o trabalho fazendo perguntas
   ao dono, e recusa performar enquanto o plano não estiver pronto por G-PLANREADY — ver texto
   normativo lá. Complementa G-PLANFIDELITY (não muda rota) e o modelo por fase (§3): a decisão
   nunca desce para o modelo barato. *Enforcement:* instrução no arquivo do agente
   `pantonic-executor`; a `proximo-passo` só delega tarefa de plano fechado; gate de review.
14. **Allowlist de subcomandos destrutivos** — **Comando destrutivo não é decisão de agente.**
   Reescrita de histórico, descarte de trabalho não commitado e remoção de branch/repositório
   ficam negados em `.claude/settings.json` (`permissions.deny`) para todo agente com `Bash`. O
   modo de falha correto é **ruidoso** — comando negado, agente reporta ao dono — nunca
   silencioso. Ampliar a lista é rotina; encurtá-la exige ato explícito do dono registrado no
   diário. *Enforcement:* `permissions.deny` em `.claude/settings.json` (`Bash(git push
   --force*)`, `Bash(git push -f*)`, `Bash(git reset --hard*)`, `Bash(git branch -D*)`,
   `Bash(git clean -fdx*)`, `Bash(gh repo delete*)`).

Esses guardrails são materializados em cada projeto como: instruções nos arquivos de agente
(`.claude/agents/*.md`, CLAUDE.md do projeto) **e** testes de conformance executáveis — a regra
que não é testável por código deve, no mínimo, constar como checklist de review.

### 7.1 Revisão e deprecação de guardrails

Um framework que só adiciona regra apodrece: o custo de ler a doutrina cresce a cada MINOR e
nenhuma regra jamais sai. Esta seção é a **porta de saída** — e é a única forma legítima de remover
um guardrail de §7.

**Gatilho.** A revisão pendura-se no **fechamento de uma versão MINOR do kit**, nunca em
calendário. Data no calendário vira cerimônia executada sem material novo para julgar; o fechamento
de MINOR é exatamente o momento em que há material. Operacionalizada pela skill `checar-versao-kit`,
que já resolve a versão local: quando o MINOR corrente é maior que o da **última revisão
registrada** abaixo, a revisão está pendente e a skill reporta ao dono.

**Escopo.** Entram só as guardrails com **≥2 MINORs de idade** — introduzidas em MINOR ≤ (corrente
− 2). Regra recém-adicionada não teve tempo de agir; cobrar evidência dela é medir ruído.

**Isenção por enforcement executável** (decisão do dono, 2026-08-01, calibragem medida na rodada
`1.4.0`). Guardrail cujo cumprimento é verificado por um **check executável ativo** — teste de
conformance, gate de CI, script do kit — **não entra na pergunta**: o check verde é a evidência de
vida. A pergunta vale para guardrail **advisória ou procedimental**, cujo único rastro possível é o
registro escrito. Motivo: regra preventiva enforçada por código só produz caso citável quando
alguém a **viola**; funcionando, ela é silenciosa, e a pergunta a condenaria justamente por
sucesso. A isenção **não é declarativa** — quem a invoca **nomeia o check** (caminho do teste, ou o
comando do gate) e confirma que ele roda hoje. Check inexistente, desabilitado (`skip`, `xfail`) ou
neutralizado (allowlist que cobre todos os casos) **não isenta**: a regra volta à pergunta, e o
check morto é achado próprio, a reportar.

**Pergunta única, aplicada a cada guardrail em escopo e não isenta:**

> Esta regra mudou algum comportamento nos últimos 2 MINORs? Cite o caso.

**Caso citável** é uma ocorrência **registrada** no intervalo — diário de obras (do hub **ou de um
consumidor**), `CHANGELOG.md`, nota de fechamento de tarefa, decision record — em que a regra
bloqueou algo, forçou uma correção ou embasou uma decisão. Duas exclusões, porque são o modo de
falha da pergunta: **suíte verde não é caso** (é a regra sendo satisfeita, não agindo) e
**lembrança sem registro não é caso** (se ninguém escreveu, não conta). A evidência de guardrail de
arquitetura mora no consumidor, não no hub — o hub não tem código de produção, e avaliar essas
regras só pelo registro dele responde "não" por construção.

**Resultado.** Sem caso citável, a guardrail é marcada **`OBSOLETA desde <versão>`** no próprio
item, **permanece em vigor** por **um MINOR** de transição e é **removida no MINOR seguinte** — a
remoção é uma tarefa nomeada como qualquer outra, com registro no diário. Um único caso citável
durante a transição desfaz a marcação. **Zero marcações numa rodada é resultado legítimo; não
registrar a rodada não é** — revisão sem registro não aconteceu.

**Registro das rodadas:**

- **`1.4.0` — 2026-08-01** (primeira aplicação, `V2K-T9`): 14 guardrails avaliadas, 8 em escopo
  (itens 1-8, doutrina original), 6 fora por idade (itens 9-13 nascidos em `1.4.0`; item 14 ainda
  não lançado). Casos citáveis encontrados para os itens **1, 3, 6, 7, 8**; **sem caso** para os
  itens **2 (ACL)**, **4 (egress G6)** e **5 (namespace de estado)**. A rodada mediu um defeito de
  calibragem da própria pergunta: guardrail **preventivo** enforçado por teste automático só produz
  caso citável quando alguém o **viola**, de modo que a pergunta não distingue "regra morta" de
  "regra que funcionou tão bem que ninguém a violou". Os três foram **retidos sem marcação** e a
  calibragem, escalada ao dono.
  **Encerrada em 2026-08-01** pela decisão do dono — **isenção por enforcement executável** (regra
  acrescentada acima). Os três são **isentos**, com o check nomeado e confirmado rodando no
  consumidor `PantonicVideo`: ACL → `tests/conformance/test_acl_no_external_in_plugins.py`;
  egress G6 → `tests/conformance/test_filesystem_egress.py`; namespace de estado →
  `tests/boundary/test_state_writer_namespacing.py` — os três executados em 2026-08-01, **11
  passed**, nenhum `skip`/`xfail` (os `pytest.skip` presentes são guarda de `plugins/` ausente, que
  existe no consumidor). **Resultado final da rodada: 0 marcações.** Resultado item a item em
  `docs/DIARIO_DE_OBRAS.md` (`V2K-T9`).

## 8. Documentação mínima de um projeto Pantonic*

| Documento | Papel |
|---|---|
| `PRD.md`, `ARCHITECTURE.md`, `SPEC.md`, `SPRINT_PLAN.md` | Os quatro artefatos do §6 |
| Diário de obras | Kanban + arquivo de planejamentos (§4.2) |
| Doc de estado vigente (AS-IS) | Baseline, decisões (`D-*`), piso de regressão |
| `docs/DOC_MAP.md` | Índice de navegação, obrigatório quando qualquer doc passar de 500 linhas |
| Lições aprendidas | Append-only, um heading por incidente real |

Disciplina: docs separados em **ATIVO** (pequeno, estado vigente) e **HISTÓRICO** (append-only)
desde o primeiro dia; CLAUDE.md do projeto ≤ 200 linhas, só regras que mudam comportamento.

## 9. Kit agêntico reusável

Os agentes (§3) e os fluxos (§4–§6) estão materializados como kit em
[.claude/](.claude/README.md): agentes `pantonic-planner`, `pantonic-executor` e
`pantonic-scout`, e skills `bootstrap-pantonic`, `diario-de-obras`, `proximo-passo`,
`integrar-poc`, `guardrails-check` e `handover`. Cada projeto consumidor **materializa** esse kit
a partir do hub via `git subtree` — nunca copia manualmente. `.claude/kit/` é o subtree do branch
`kit` deste repo; `.claude/kit/sync-kit.ps1` aplica a versão publicada sobre a árvore local,
respeitando os overrides declarados em `kit-exclude.txt`. O consumidor ajusta apenas os "fatos
estáveis" dos agentes — nunca os artefatos do próprio subtree (eles vêm do hub). Mecanismo de
versionamento e atualização: §10. Provado ponta a ponta em `PantonicVideo`
(`P-0725-governanca-hub-unico.md` Fase 4/5).

**Enforcement do kit é executável.** `.claude/README.md` é artefato **derivado** do conteúdo real
de `.claude/` (agentes, skills, checks) e **não se edita à mão** — regenerá-lo a partir do disco é
a única forma legítima de mudá-lo. O comando canônico do enforcement é
`pwsh .claude/checks/kit_check.ps1 -Mode validate` (estrutura do kit, incluindo a paridade de
versão de §10) e `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` (índice derivado versus
disco), ambos pendurados no gate `guardrails-check` que roda ao fim de toda tarefa. O enforcement
do kit é **código**, não convenção escrita: regra do kit que não puder ser verificada por esse
script nasce com o motivo escrito de por que não pode.

## 10. Versionamento e atualização do kit

O kit agêntico (§9) é versionado e a atualização de um consumidor a partir do hub segue uma
regra única, sem exceção de severidade.

**(a) Atualização é sempre iniciada pelo usuário.** Nenhum agente sincroniza o kit por conta
própria em nenhuma circunstância — nem quando a divergência aparenta ser "só um patch". Detectar
que a versão local diverge da versão do hub e agir sobre essa divergência são dois atos
distintos: um agente pode fazer o primeiro (reportar), nunca o segundo (atualizar). Não existe
threshold de severidade que justifique pular essa separação.

**(b) Checagem de versão na criação de todo plano.** O gatilho é a criação de um plano novo — é
o momento em que se decide trabalho futuro, logo o momento certo de saber se a doutrina base
usada por esse trabalho está desatualizada.

**Mecanismo.** O hub mantém `.claude/KIT_VERSION` (versão canônica do kit) — dentro do prefixo
`.claude/`, não na raiz do repo, porque é o prefixo que o `git subtree split` publica; a versão
viaja dentro do próprio artefato que ela versiona, em vez de ficar num arquivo solto que o subtree
não carrega. A cada mudança canônica, o hub publica uma tag git `kit-v<versão>` na branch `kit` (o
subtree de `.claude/`). Cada projeto consumidor materializa a versão que recebeu em
`.claude/kit/KIT_VERSION`. A checagem compara as duas com uma única chamada de rede —
`git ls-remote --tags <url> "kit-v*"` — que não faz fetch nem toca a árvore de trabalho do
consumidor.

**Os três resultados possíveis da checagem:**
- **Versões iguais** → segue em silêncio; não vale o turno do dono para confirmar o óbvio.
- **Divergentes** → reporta a versão local, a versão remota, e pergunta *"atualizar agora ou
  postergar?"*. A resposta do dono é registrada no próprio plano que está sendo criado. O agente
  nunca atualiza sozinho, seja qual for a resposta.
- **Sem rede / remote inacessível** → reporta "não verificado" e segue com o trabalho. Falha de
  rede não bloqueia a tarefa nem é tratada como se fosse "versões iguais" — a incerteza é
  reportada, não escondida.

**(c) Registro de consumidores é derivado, nunca editado à mão.** `docs/CONSUMIDORES.md` lista os
projetos consumidores do kit; as três colunas derivadas (`Versão instalada`, `Último sync`, `Modo`)
são escritas por `kit_check.ps1 -Mode consumers` a partir do carimbo `SYNC_STATE` que cada
consumidor grava em `.claude/kit/` a cada sync efetivo — nunca preenchidas à mão. A coluna
`Consumidor` é a única entrada mantida manualmente.

**Critério de pronto.** Qualquer tarefa que edite `.claude/` do hub só está pronta se o bump de
`.claude/KIT_VERSION` acompanhar a mudança. Uma versão que não sobe quando o conteúdo muda deixa a
checagem cega — o guarda vira teatro.

**Paridade `VERSION` × `.claude/KIT_VERSION` (V2B-T1).** `VERSION` (raiz — o framework: doutrina +
kit) e `.claude/KIT_VERSION` (o que o subtree publica) carregam **sempre o mesmo valor**;
divergência entre eles é defeito, não estado válido. Semver com significado declarado: **MAJOR** =
exige ação do consumidor (artefato removido/renomeado, doutrina invertida); **MINOR** = artefato ou
guardrail novo compatível com o que já existe; **PATCH** = correção redacional, sem mudança de
comportamento. Toda tarefa que edite `.claude/` ou a doutrina bumpa os dois arquivos **e** escreve
uma linha correspondente no `CHANGELOG.md` (raiz) — os três se movem juntos, nunca um sem os
outros dois.

**O que se distribui, executa.** Agentes e skills são instruções que rodam com as ferramentas
que o frontmatter concede; um artefato adulterado no hub vira execução em todo consumidor. O
passo de sync verifica a assinatura do commit de origem antes de aplicar. **Fora de escopo,
registrado:** varredura de conteúdo artefato por artefato — custo alto, e o corpus inteiro a
deixa em aberto.
