# GOVERNANÇA — Projetos Pantonic*

> **Audiência:** este documento é escrito para o **agente de planejamento** de um projeto
> Pantonic*. Lendo este documento e o [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md), o
> agente deve ser capaz de idealizar um projeto funcional, consistente com a família Pantonic*,
> com processo suficiente para garantir a qualidade do produto.

---

## 1. Identidade do framework Pantonic*

O framework é **agnóstico a tecnologia e a plataforma**. Ele não prescreve linguagem, framework de
interface, runtime nem modalidade de entrega: atua **um nível acima da implementação**, em dois
níveis.

| Nível | O que doutrina | Onde mora |
|---|---|---|
| **Arquitetura** | como o software é estruturado — camadas, sentido das dependências, domínio, extensão | [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md) |
| **Projeto** | como o software é produzido — backlog, sprints, papéis, guardrails, disciplina de contexto agêntico | este documento (§3 a §9) |

Modalidades cobertas: **desktop, container, web e servidor**. O que muda entre elas é o **perfil**
(§1.1), nunca o núcleo da doutrina.

Premissas repetíveis, válidas para todo projeto da família:

1. **Clean architecture + DDD como base** — fundamentos pares, não alternativas: a CA dá as camadas
   e o sentido das dependências; o DDD dá o conteúdo do domínio (linguagem ubíqua, entidades,
   objetos de valor, agregados e suas invariantes). Ver
   [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md).
2. **Infracore como doutrina das camadas de aplicação e infraestrutura** — o passo pantônico além
   da CA+DDD: as camadas altas não ficam ao improviso de cada projeto, seguem o core descrito no
   documento de arquitetura.
3. **Um plugin = um caso de uso** — toda evolução funcional entra como plugin, e cada plugin
   responde por exatamente um caso de uso (§5).
4. **Core comum reusável** — nenhum projeto reinventa infraestrutura; o que é comum é herdado, não
   recriado (§2).
5. **Guardrails executáveis** — a obsessão por clean architecture e clean code não é aspiração: é
   verificada por teste e por script, e o que não é verificável não é guardrail (§7).

Nenhuma premissa nomeia stack. Linguagem, framework de interface e plataforma pertencem ao
**perfil** do projeto, nunca à identidade do framework.

### 1.1 Perfis

Um **perfil** é o conjunto de regras que só fazem sentido para uma modalidade de aplicação. O
núcleo é universal e cobrado de todo projeto; o perfil liga verificações adicionais.

| Camada | Conteúdo | Cobrança |
|---|---|---|
| **Núcleo (universal)** | CA+DDD, regra de dependência, ACL, plugin/caso de uso, egress único de filesystem, namespace de estado, gate de conformance, piso de regressão, disciplina de contexto e de projeto | todo projeto Pantonic*, sempre |
| **Perfil** | as regras da modalidade, e só elas | apenas o projeto que declara o perfil |

Perfis nomeados:

| Perfil | Modalidade | Ativa | Auditor |
|---|---|---|---|
| `desktop-pyside6` | aplicação desktop em Python + PySide6 | MVVM estrito (§7 item 3); ViewModel `QtCore`-only; geometria e estilo Qt só na shell e nas Views; infracore com binding Qt | `pantonic-auditor-pyside6` |
| `container` | serviço containerizado | 12-factor, concorrência/event loop, shutdown determinístico, observabilidade, empacotamento | `pantonic-auditor-container` |
| `web-servidor` | aplicação web ou serviço de rede | **nenhuma verificação própria ainda** — perfil declarado, conteúdo a escrever quando o primeiro projeto dessa modalidade existir | — |

**Como um projeto declara o seu:** arquivo `.claude/PERFIL` na raiz do repositório — uma linha, o
identificador do perfil. É artefato **do projeto**, não do kit: fica fora de `.claude/kit/` e o
`sync-kit` não o toca. **Na ausência do arquivo, o perfil é `desktop-pyside6`** — compatibilidade
com os consumidores existentes, que nasceram sob a premissa antiga.

Um projeto tem **exatamente um** perfil. Modalidade não coberta entra como perfil novo nesta seção
**antes** de o projeto nascer, nunca como exceção silenciosa dentro de um perfil vizinho.

## 2. Core comum e diversificação por camada

- Todo projeto **adota o mesmo core pantonico** (infracore + contracts genéricos + serviços de
  expressão), conforme o documento de arquitetura reusável.
- O core é **doutrina agnóstica com implementação hoje ligada ao perfil `desktop-pyside6`**: a
  abstração das portas do infracore (lifecycle, injeção, estado, sinais, filesystem) é etapa
  própria e ainda não executada. Até lá, projeto de outro perfil herda do core os **conceitos e os
  contratos**, não o binding.
- A **diversificação acontece nas camadas inferiores da clean architecture**: domínio e casos de
  uso. Regra mental para o planejador:

  | Altura na clean architecture | Grau de especialização |
  |---|---|
  | Domínio (entidades, VOs, agregados) | Máxima — único por projeto |
  | Casos de uso / serviços de domínio | Alta — único por projeto (um plugin = um caso de uso) |
  | Serviços de expressão / ACL | Baixa — padrão do core |
  | Infraestrutura (infracore, adaptador de apresentação) | Nenhuma — idêntico entre projetos do mesmo perfil |

  Quanto mais baixo (próximo ao domínio), mais especializadas as classes; quanto mais alto
  (infraestrutura), mais as aplicações Pantonic* se parecem entre si.

## 3. Operações agênticas

**Eixo de justificação — qualidade → rota → custo, nesta ordem.** O motor declarado da camada de
projeto é a **doutrina da qualidade**, e ela tem uma tese: a qualidade de um produto não se garante
agindo sobre o **produto**, mas sobre o **processo** que o gera. Guardrails executáveis, TDD, piso
de regressão, contexto limpo e validação por sprint (§4.5) existem por isso — são atos sobre o
processo, não inspeções do resultado. A **rota** vem em segundo: decidida no planejamento e mantida
fiel na execução (§7 itens 10 e 13), porque processo bom com rota errada entrega, com esmero, o
produto errado. O **custo** é o terceiro: **restrição de projeto**, não razão de ser. Modelo por
fase, orçamento de turnos e economia de contexto tornam a qualidade **sustentável** — nunca a
compram mais barata. Quando os três colidem, a ordem decide: nenhuma economia justifica abrir mão
de um guardrail, e nenhuma rota se muda para caber no orçamento.

**Matriz de responsabilidades — lugar canônico.** Quem responde pelo quê num projeto Pantonic* é
declarado **aqui e só aqui**; qualquer outra seção deste documento, agente ou skill **aponta** para
esta tabela em vez de repeti-la (padrão `DR-A`,
[docs/RESIDENCIA_DOUTRINA.md](docs/RESIDENCIA_DOUTRINA.md)). Cada papel agêntico opera no modelo
adequado ao seu custo — a coluna *Modelo* é a tabela vinculante do **modelo por fase**.

| Papel | Modelo | Responde por | Não faz |
|---|---|---|---|
| **Dono / gerente** | humano | Última instância e **fonte da doutrina de produto**: decide o quê e o porquê, ratifica decisões (`DR-`/`DP-`), valida cada sprint (§4.5), aceita release, autoriza saída do piso de regressão (§4.4) e comando destrutivo (§7 item 14) | Não desempata, no meio de uma execução, o que o plano deveria ter decidido — a pergunta que chega até ele em execução é sintoma de plano não-pronto (§7 itens 12 e 13) |
| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 12), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto | Não executa: não implementa, não fecha tarefa, não transforma dúvida própria em pergunta ao executor |
| **Execução** | Melhor custo-benefício (Sonnet) | Implementar **uma** tarefa do checklist por vez, em contexto limpo, sob TDD (§4.4); registrar o resultado no diário de obras e fazer handover | Não decide, não pergunta ao dono, não replaneja escopo e não substitui a rota aprovada (G-EXECREADY e G-PLANFIDELITY, §7 itens 13 e 10): plano não-pronto ou obstáculo à rota → para, registra `blocked` no diário e escala |
| **Coleta** | O mais barato (Haiku ou equivalente) | Search, grep, leitura de codebase/documentos/prompts; filtra e devolve só o pertinente para o contexto dos agentes mais caros | Não edita, não conclui tarefa, não emite juízo sobre o que coletou |
| **Auditoria** | Melhor custo-benefício (Sonnet) | Medir aderência **sem alterar código**, em duas frentes permanentes: **clean architecture + DDD** (`pantonic-auditor-arch`) e **clean code** (`pantonic-auditor-cleancode`); o perfil declarado acrescenta o seu auditor (§1.1) | Não corrige o que aponta — cada apontamento vira item no diário de obras, priorizado pelo dono |

Regras de operação:

- O agente de coleta existe para **proteger o contexto dos agentes caros**: varreduras amplas
  nunca são feitas diretamente pelo agente de planejamento ou de execução; são delegadas à
  coleta, que devolve dossiês compactos (caminhos, linhas, assinaturas — nunca arquivos inteiros).
- **Papéis não são intercambiáveis** — a fronteira de cada um (o que faz e o que não faz) está na
  matriz de responsabilidades acima, que é o único lugar onde ela se declara.
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
- **Economia de contexto** — saída verbosa de ferramenta (logs, listagens, builds) entra inteira
  no contexto e degrada qualidade/custo; filtrar na origem, não depois (`~/.claude/CLAUDE.md`
  Regra 3, dono).
- **Disciplina de coleta** — `git status --short`/`git log --oneline` no lugar dos completos;
  listagem de diretório nunca recursiva sem excluir `build/`, `.venv/`, `node_modules/`; arquivo
  > 500 linhas via Grep + Read com `offset`/`limit`, nunca leitura integral; comando verboso
  não-teste redireciona a saída para arquivo e lê só o fim.
- **Batching de chamadas independentes** — leituras/greps sem dependência entre si vão na mesma
  mensagem; N leituras em 1 turno custam 1 reenvio de contexto, em N turnos custam N reenvios.

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

**Filiação ágil — Scrum modulado para programação agêntica.** Este fluxo não é invenção do
framework: **backlog, sprints e tarefas derivam de metodologia ágil**, na linhagem **Scrum**, e a
estrutura é preservada — itens priorizados num backlog, trabalho fatiado em sprints com entregável
ao fim de cada uma, tarefas decompostas a partir dos itens, e revisão a cada ciclo. O que muda é
**quem consome o backlog**: um agente com contexto finito, que parte frio a cada tarefa, em vez de
uma equipe humana com memória entre reuniões. Daí as modulações — e só elas:

| Prática Scrum | Como fica em programação agêntica |
|---|---|
| Product/sprint backlog | **diário de obras** — índice, status por item e priorização explícita (§4.2); planos completos em `docs/plans/` |
| Sprint com entregável ao fim | **plano** (`P-NNNN`) com tarefas na ordem de execução; o entregável passa pelo gate de validação antes de a sprint seguinte começar (§4.5) |
| Item de backlog / história | **tarefa atômica** — uma por contexto (§4.3), com teto de turnos por classe (§3) |
| Time auto-organizado | **papéis fixos e não intercambiáveis** — matriz de responsabilidades (§3) |
| Cerimônias (daily, planning, review) | **atos escritos**: dossiê de tarefa, handover e veredito de validação no diário — o que só existe em conversa não sobrevive à troca de contexto e, portanto, não existe |
| Definition of done | **critério de pronto** no dossiê + guardrails executáveis (§7), gate de conformance e piso de regressão (§4.4) |

Duas práticas ágeis **não** viajam. Estimativa em story points: a unidade de esforço agêntico é o
**orçamento de turnos** por classe de tarefa (§3), medido em `docs/telemetria.tsv`, nunca estimado
por analogia. E auto-organização de escopo: o executor não escolhe o que fazer nem redefine a
tarefa — decidir é fase do planejamento (§3, §7 itens 10 e 13).

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
- **Veredito de validação da sprint** — o diário é onde a validação do gerente/cliente sobre o
  entregável fica registrada (aprovada/reprovada, com data). A regra do gate mora na §4.5; aqui
  ficam só os vereditos. Sprint sem veredito escrito conta como **não validada**.
- **Fechamento enxuto** — o diário de obras é o único registro canônico de uma tarefa; o relatório
  final ao orquestrador é ponteiro + deltas, nunca repete o que já está escrito aqui.
- **Telemetria pela notificação, não pelo auto-relato** — o consumo de uma tarefa é registrado
  pelo **orquestrador** como uma linha em `docs/telemetria.tsv`, lendo o bloco `<usage>` da
  notificação de conclusão do subagente (dado medido) — nunca copiando a estimativa que o próprio
  subagente eventualmente escreve no texto do handover (auto-relato subestima: caso medido
  registrou ~90k autorrelatado contra ~140k reais, ~35% de subestimativa). Cria série histórica
  para detectar regressão de consumo por tarefa, mesmo racional do piso de regressão de testes
  aplicado a custo. O executor grava no diário o placeholder literal
  `Consumo: (preenchido pelo orquestrador via notificação)` — nunca um número próprio.
- **Fonte única da série** — `docs/telemetria.tsv` (append-only, colunas `data`, `projeto`,
  `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte` ∈ `{usage, contado,
  nao_medido}`) é a **fonte da série de consumo**; o diário/histórico **aponta** para ela
  (`Consumo: ver docs/telemetria.tsv`) em vez de copiar o número. Duplicar a medição em prosa
  recriaria duas fontes que divergem à primeira edição. Registro qualitativo que não cabe em
  coluna (estouro de teto, execução inline, ressalva sobre a medida) continua no bullet do diário,
  ao lado do ponteiro — o que não se repete é o **número**. Bullets `Consumo:` anteriores à adoção
  desta regra ficam como estão: são registro histórico, já espelhado na série.

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
  colaterais).

**Cadência de testes** — Tier 1 roda no máximo 2× por tarefa (após implementar, após corrigir),
nunca a cada micro-edição; tier superior só no fechamento (`~/.claude/CLAUDE.md` Regra 7; skill
`test-tiers`).

**Piso de regressão — comportamentos trancados, nunca percentual.** O piso é o conjunto de
**comportamentos** que o projeto já garante e não pode perder. Ele **não é** percentual de
cobertura, e percentual de cobertura **não** vale como piso, meta ou critério de pronto em nenhum
ponto desta doutrina: piso percentual premia manter teste de código morto para não derrubar a
métrica — exatamente o que `G-DEADCODE` (§7, item 9) proíbe. Escrito como comportamento, o piso
**reforça** `G-DEADCODE`: sumiu o chamador de produção, o comportamento sai do piso por ato
explícito, e nenhum teste sobrevive só para segurar um número.

O piso responde a três perguntas:

1. **Como se mede** — por uma **lista versionada** de comportamentos trancados, no repositório do
   projeto (`tests/piso_comportamental.txt`), uma linha por comportamento no formato
   `<pytest nodeid> — <comportamento em uma frase>`. Um comportamento entra no piso quando o par
   TF+TR que o tranca fica verde; a unidade é a frase, não o arquivo nem a contagem de testes.
2. **Como se prova que não desceu** — por comando, não por leitura: o check de ratchet
   (`.claude/checks/ratchet_piso.py`, invocado pela skill `guardrails-check`) compara a lista com a
   coleta real da suíte e **falha nomeando o comportamento perdido** quando um nodeid do piso
   desapareceu. Handover que não roda o check não fecha a tarefa.
3. **O que fazer quando um comportamento é removido de propósito** — tirar do piso é **decisão do
   dono**, nunca efeito colateral de refactor: o dono registra o ato no diário de obras (qual
   comportamento, por quê, em que commit) e só então a linha sai de `tests/piso_comportamental.txt`,
   no mesmo commit que remove o teste. Sem esse registro, teste do piso que some é regressão, não
   simplificação. Teste cujo significado muda intencionalmente é **reescrito** — e a linha do piso
   é reescrita junto —, nunca deletado.

### 4.5 Validação por sprint — gate do gerente/cliente

**Nenhuma sprint avança sem validação visual do gerente/cliente sobre o entregável.** É **gate**,
não recomendação: enquanto o veredito não estiver registrado no diário (§4.2), a sprint seguinte
não começa e nenhuma tarefa dela é delegada.

- **O que se valida** — o entregável **em funcionamento**, visto por quem pediu: o executável, a
  tela, a saída real do incremento. Suíte verde não substitui. Teste prova que o código faz o que o
  agente **entendeu**; a validação visual prova que é o que o dono **quis** — e é o único gate que
  cobre sentido, que nenhum script cobre.
- **Quem valida** — o dono/gerente, na figura de cliente (matriz de responsabilidades, §3). Nenhum
  agente valida a própria entrega, e validação não se infere de conversa: ou está escrita, ou não
  aconteceu.
- **Reprovação não vira tarefa de outra sprint** — volta como rodada nova da **mesma** sprint, até
  o entregável ser aceito. O que a reprovação ensinou entra no diário junto do veredito, para que a
  rodada seguinte não repita a causa.
- **Sprint sem entregável mostrável é decomposição errada** — se ao fim do ciclo não há o que
  mostrar, o corte do plano está no eixo errado (fatia técnica em vez de fatia de valor) e o corte
  é replanejado. Em sprint de doutrina ou documentação, o entregável mostrável é o **documento**, e
  a leitura corrida pelo dono é a validação.

## 5. Fluxo de extensão (plugins)

A extensão de capacidades ocorre **exclusivamente por plugins**, e a unidade de extensão é
normativa: **um plugin = um caso de uso** (§1, premissa 3). Caso de uso, no sentido de CA+DDD
([ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md) §1.1), é um objetivo do usuário levado do
início ao fim, com nome que o dono reconhece e resultado que ele consegue validar. O plugin é a
materialização verificável desse caso de uso: um caso de uso = um plugin = um manifest = um teste
funcional que o valida.

Consequências operacionais, todas verificáveis na revisão de um plugin novo:

- **Plugin sem caso de uso nomeável não entra.** Se o propósito só se descreve em termos técnicos
  ("camada de X", "utilidades de Y"), o que está na mesa é infraestrutura (infracore) ou serviço
  (ACL), não plugin.
- **Caso de uso espalhado por dois plugins é decomposição errada** — vira acoplamento disfarçado,
  já que plugins só podem conversar por sinais e estado.
- **Dois casos de uso num plugin só** também é defeito: quebra a atomicidade e impede validar um
  sem o outro. Divide-se antes de integrar.
- Plugins continuam **não conflitantes** entre si: comunicação apenas por sinais e estado, nunca
  acoplamento direto nem referência entre plugins (ver arquitetura §9).

Fluxo de trabalho para toda nova funcionalidade:

1. **POC separada** — cria-se uma prova de conceito fora da aplicação, com a finalidade
   pretendida, funcionando standalone.
2. **Estresse e validação** — a POC é estressada até que o **cliente valide** o atendimento da
   necessidade. Nada é integrado antes dessa validação. Esta valida a **ideia** antes de custar
   integração; não dispensa o gate de sprint sobre o entregável já integrado (§4.5) — são dois
   momentos distintos do mesmo princípio, e ambos são do dono (matriz de responsabilidades, §3).
3. **Integração** — os agentes **dissecam a POC nas camadas da clean architecture** (o que é
   entidade, VO ou agregado; o que é caso de uso; o que vira serviço/ACL; o que fica como código
   ad-hoc do plugin), usando a escada de classificação de
   [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md) §1.1, e inserem o código na aplicação
   Pantonic*, seguindo a doutrina de integração do documento de arquitetura (§9).
4. **Teste do conjunto** — TF do plugin + suíte de conformance + piso de regressão completo.

**Estado da aderência: não auditado.** A regra acima é doutrina. O grau em que os plugins já
existentes na implementação de referência de fato mapeiam **um** caso de uso cada **ainda não foi
medido** — a medição é a `T14` de
[docs/plans/P-0730-v2-identidade.md](docs/plans/P-0730-v2-identidade.md). Até o relatório existir,
nenhum documento afirma conformidade aqui como fato consumado (G-PREMISE, §7).

## 6. Fluxo de projeto — os quatro artefatos iniciais

Um projeto Pantonic* inicia com quatro artefatos, produzidos nesta ordem pelo agente de
planejamento:

1. **PRD** — coleta os objetivos da aplicação; determina casos de uso, elementos de domínio,
   requisitos, estruturas de dados e **linguagem ubíqua** necessários para construir as camadas
   de domínio e de casos de uso segundo **clean architecture + DDD** (§1, premissa 1). É aqui que
   o domínio é modelado, com o vocabulário definido em
   [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md) §1.1: o PRD nomeia o **contexto
   delimitado** da aplicação, lista as **entidades**, os **objetos de valor** e os **agregados**
   com suas **invariantes**, e fixa a **linguagem ubíqua** — um termo por conceito, sem sinônimos
   concorrentes. Esse vocabulário é o mesmo que aparecerá em classes, campos, sinais, plugins e
   testes; termo novo que surja na execução volta ao PRD em vez de nascer só no código. Cada caso
   de uso listado aqui é candidato a **exatamente um plugin** (§5).
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
3. **MVVM estrito** — *[perfil `desktop-pyside6`, §1.1]* geometria/estilo Qt só na shell e Views;
   ViewModel é QtCore-only (sem widgets); Model é puro (sem Qt). Projeto de outro perfil não é
   cobrado por este item; a regra universal correspondente é a **separação de apresentação e
   domínio**, coberta pelos itens 1 e 2.
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
15. **G-README — o README é documento canônico, não artefato acessório** (`DR-7`, 2026-08-05) — o
   `README.md` da raiz do hub é o **contrato entre o framework e o cliente**, não artefato
   acessório nem derivado: um framework corretamente construído é **rejeitado** por um README
   desatualizado, confuso ou equivocado. Três deveres: **(1)** nenhuma mudança de doutrina fecha sem
   o README refletindo-a **na mesma sprint**; **(2)** toda sprint encerra com uma **atividade
   própria de revisão do README**, autorada pelo **planejador** como tarefa nomeada do plano — é aí
   que o aceite do dono é colhido, e nenhum bump de versão fecha sem ele; **(3)** o guarda executável
   cobre **estrutura, não sentido** — ele é **instrumento do planejador dentro dessa atividade**,
   nunca critério de pronto automático, porque o único teste de sentido que existe é a leitura do
   dono. Evidência de campo: os desvios de identidade que abriram o Estágio 5 foram identificados
   pelo dono **lendo o README**, não os artefatos. *Enforcement:* a tarefa de encerramento de sprint
   (dever 2), que roda `pwsh .claude/checks/check-readme.ps1` para a paridade estrutural e registra o
   veredito do dono. **Não é gate mecânico** (`DR-8`, 2026-08-05 — decisão do dono): pendurar o
   aceite como bloqueio automático na skill `handover` foi **rejeitado**, por gerar artefato
   especializado e confuso no lugar de uma responsabilidade clara de quem planeja.

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
| `README.md` (raiz) | **Documento canônico** — o contrato entre o framework e o cliente, e a porta de entrada humana (§7 item 15, §9). Não é derivado nem acessório |
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

**Porta de entrada humana do framework:** `README.md` (raiz do hub) é o espelho canônico — um
humano decide sobre o framework lendo só esse arquivo, sem abrir nenhum outro artefato; guarda de
drift em `.claude/checks/check-readme.ps1` (`P-0729-v2-documentacao.md`, Estágio 4). Desde a `DR-7`
(2026-08-05) esse status é **guardrail** — §7 item 15 (G-README): o README é o **contrato entre o
framework e o cliente**, não artefato acessório nem derivado.

**Colisão registrada, ainda aberta.** O preâmbulo vigente do README (`README.md:5-11`) declara o
oposto desta seção — *"não existe para convencer ninguém a adotar o framework: quem lê já o usa"*.
A `DR-7` resolve a colisão **a favor desta seção e do G-README**; remover a frase e reescrever o
preâmbulo é dívida da `V2I-T11` (`docs/plans/P-0730-v2-identidade.md` `### T11`). Até lá, em caso
de conflito prevalece este parágrafo, não o preâmbulo.

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
- **Divergentes em MINOR/PATCH** → reporta a versão local, a versão remota, e pergunta *"atualizar
  agora ou postergar?"*. A resposta do dono é registrada no próprio plano que está sendo criado. O
  agente nunca atualiza sozinho, seja qual for a resposta.
- **Divergentes em MAJOR** → não é divergência comum: reporta como **incompatível** e para, sem a
  pergunta de atualização — padrão de `BM-19§D10` (CLI v1.x consome só templates v1.x.x). A regra
  `(a)` continua valendo sem exceção de severidade: o agente nunca atualiza sozinho; decidir como
  prosseguir é do dono.
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
