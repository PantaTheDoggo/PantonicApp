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
- **Delegar a um subagente protege o contexto do orquestrador (Regra 2 do CLAUDE.md), não reduz
  o consumo total.** O subagente parte frio e paga de novo CLAUDE.md + definição do agente +
  skills carregadas em todos os seus turnos. Tarefa pequena (< ~15 turnos estimados) prefere
  execução inline a abrir um subagente.
- **Orçamento de turnos por tarefa atômica**: ~≤40 tool uses esperado no agente de execução.
  Estourar é sinal de tarefa mal decomposta ou de thrashing (editar-testar-editar sem plano
  interno) — reportar no handover, não só continuar.

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

Esses guardrails são materializados em cada projeto como: instruções nos arquivos de agente
(`.claude/agents/*.md`, CLAUDE.md do projeto) **e** testes de conformance executáveis — a regra
que não é testável por código deve, no mínimo, constar como checklist de review.

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

Os agentes (§3) e os fluxos (§4–§6) estão materializados como kit copiável em
[.claude/](.claude/README.md): agentes `pantonic-planner`, `pantonic-executor` e
`pantonic-scout`, e skills `bootstrap-pantonic`, `diario-de-obras`, `proximo-passo`,
`integrar-poc`, `guardrails-check` e `handover`. Todo projeto novo copia esse kit no bootstrap e
ajusta apenas os "fatos estáveis" dos agentes.

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

**Mecanismo.** O hub mantém `KIT_VERSION` na raiz (versão canônica do kit) e, a cada mudança
canônica, publica uma tag git `kit-v<versão>` na branch `kit` (o subtree de `.claude/`). Cada
projeto consumidor materializa a versão que recebeu em `.claude/kit/KIT_VERSION`. A checagem
compara as duas com uma única chamada de rede — `git ls-remote --tags <url> "kit-v*"` — que não
faz fetch nem toca a árvore de trabalho do consumidor.

**Os três resultados possíveis da checagem:**
- **Versões iguais** → segue em silêncio; não vale o turno do dono para confirmar o óbvio.
- **Divergentes** → reporta a versão local, a versão remota, e pergunta *"atualizar agora ou
  postergar?"*. A resposta do dono é registrada no próprio plano que está sendo criado. O agente
  nunca atualiza sozinho, seja qual for a resposta.
- **Sem rede / remote inacessível** → reporta "não verificado" e segue com o trabalho. Falha de
  rede não bloqueia a tarefa nem é tratada como se fosse "versões iguais" — a incerteza é
  reportada, não escondida.

**Critério de pronto.** Qualquer tarefa que edite `.claude/` do hub só está pronta se o bump de
`KIT_VERSION` acompanhar a mudança. Uma versão que não sobe quando o conteúdo muda deixa a
checagem cega — o guarda vira teatro.
