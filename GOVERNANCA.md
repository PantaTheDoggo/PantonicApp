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

A doutrina é **agnóstica à tecnologia e à forma de entrega**: nada aqui depende de linguagem,
framework de interface, runtime ou plataforma da aplicação construída.

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

Nenhuma premissa nomeia stack. Linguagem, framework de interface e plataforma são escolhas de cada
projeto, nunca traços da identidade do framework.

## 2. Core comum e diversificação por camada

- Todo projeto **adota o mesmo core pantonico** (infracore + contracts genéricos + serviços de
  expressão), conforme o documento de arquitetura reusável.
- **O core é definido por portas.** Cada porta do runtime é um **contrato**, e o contrato é o que
  todo projeto da família herda — nunca o binding. A **implementação** de uma porta pertence à
  camada que declara a tecnologia: cada projeto realiza as portas na linguagem e no toolkit que
  escolher, e as duas em que o mundo externo encosta no núcleo — superfície de entrada e execução
  assíncrona — são realizadas pela camada de modalidade do projeto, fora do core reusável. Um
  plugin escrito contra a porta funciona sobre qualquer implementação que honre o contrato. Os
  contratos, porta a porta, moram em
  [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md) §4 — esta seção afirma a regra e não a
  duplica.
- A **diversificação acontece nas camadas inferiores da clean architecture**: domínio e casos de
  uso. Regra mental para o planejador:

  | Altura na clean architecture | Grau de especialização |
  |---|---|
  | Domínio (entidades, VOs, agregados) | Máxima — único por projeto |
  | Casos de uso / serviços de domínio | Alta — único por projeto (um plugin = um caso de uso) |
  | Serviços de expressão / ACL | Baixa — padrão do core |
  | Infraestrutura (infracore, adaptador de apresentação) | Nenhuma na **porta** — o contrato é idêntico entre todos os projetos; a **implementação** só é idêntica entre projetos da mesma stack |

  Quanto mais baixo (próximo ao domínio), mais especializadas as classes; quanto mais alto
  (infraestrutura), mais as aplicações Pantonic* se parecem entre si.

## 3. Operações agênticas

**Eixo de justificação — qualidade → rota → custo, nesta ordem.** O motor declarado da camada de
projeto é a **doutrina da qualidade**, e ela tem uma tese: a qualidade de um produto não se garante
agindo sobre o **produto**, mas sobre o **processo** que o gera. Guardrails executáveis, TDD, piso
de regressão, contexto limpo e validação por sprint (§4.5) existem por isso — são atos sobre o
processo, não inspeções do resultado. A **rota** vem em segundo: decidida no planejamento e mantida
fiel na execução (§7 itens 9 e 12), porque processo bom com rota errada entrega, com esmero, o
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
| **Dono / gerente** | humano | Última instância e **fonte da doutrina de produto**: decide o quê e o porquê, ratifica decisões (`DR-`/`DP-`), valida cada sprint (§4.5), aceita release, autoriza saída do piso de regressão (§4.4) e comando destrutivo (§7 item 13) | Não desempata, no meio de uma execução, o que o plano deveria ter decidido — a pergunta que chega até ele em execução é sintoma de plano não-pronto (§7 itens 11 e 12) |
| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**; **a revisão do README ao encerrar cada sprint** — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do dono como aceite (G-README dever 2, §7 item 14); sprint planejada sem essa tarefa é plano incompleto; **o risco de interrupção de cada card** — plano em que um executor frio pararia por dúvida sem contingência fechada não se libera (G-NOASK, §7 item 18) | Não executa: não implementa, não fecha tarefa, não transforma dúvida própria em pergunta ao executor |
| **Orquestração** | Melhor custo-benefício (Sonnet); o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão, e **para para pedir `/model`** quando a fase exige outro modelo | Conduzir um plano do começo ao fim: despachar cada tarefa ao papel competente com o dossiê fechado, rotear a linha de retorno do executor e o laudo do `reviewer` (aprovado segue, reprovado volta ao mesmo escopo, escalado sobe ao dono), registrar a telemetria medida e arquivar o resultado | Não implementa, não julga a entrega — o veredito é da revisão — e não decide arquitetura: obstáculo à rota e dossiê não fechado sobem ao **planejamento** (G-REPLAN e G-NOASK, §7 itens 17 e 18), nunca viram improviso do loop nem pergunta ao dono no meio da janela — ao dono chega, no relatório de encerramento, só o que o planejador classificar como estratégico. **Não revisa plano** — roteia a escalada ao planejamento, não replaneja |
| **Execução** | Melhor custo-benefício (Sonnet) | **Executar a tarefa — responsabilidade única**: implementar **uma** tarefa do checklist por vez, em contexto limpo, sob TDD (§4.4), entregando-a **tecnicamente correta** — testes da área tocada, conformance e piso de regressão verdes — e **sinalizando** o resultado (`review`, ou `blocked` com razão tipada) | Não decide, não pergunta ao dono, **não fica com dúvida** — dúvida é sinal de parada, não objeto de deliberação —, não replaneja escopo e não substitui a rota aprovada (G-EXECREADY, G-PLANFIDELITY e G-NOASK, §7 itens 12, 9 e 18): plano não-pronto, obstáculo à rota ou dúvida → para, registra o fato, sinaliza `blocked` e encerra; a escalada é ao planejamento, nunca direta ao dono. **Não se ocupa de teto nem de orçamento** — nem de turnos, nem de contexto: estouro se registra no corpo da tarefa como insumo do planejador, nunca vira decisão sua. **Não revisa plano.** Não escreve no diário de obras, não registra o resultado da própria entrega e não afere a própria aceitação — o veredito é da revisão |
| **Revisão** | O mais poderoso disponível (Opus) — as dimensões de maior peso do laudo são juízo puro, e reviewer no mesmo modelo de quem executou tende a ratificar; é o único gate entre a entrega e o `done` sem round-trip humano | Julgar a entrega de **uma** tarefa contra o dossiê dela e emitir o laudo, em contexto próprio e com a escrita restrita ao caminho do laudo — independência imposta pela lista de ferramentas. Onde a camada mecânica (guardas, conformance, piso, escopo) mediu vermelho, o laudo acompanha a medição | Não corrige o que aponta, não replaneja e não fecha tarefa: o laudo é o veredito, e o encaminhamento do que ele aponta é da orquestração |
| **Coleta** | O mais barato (Haiku ou equivalente) | Search, grep, leitura de codebase/documentos/prompts; filtra e devolve só o pertinente para o contexto dos agentes mais caros | Não edita, não conclui tarefa, não emite juízo sobre o que coletou |
| **Auditoria** | Melhor custo-benefício (Sonnet) | Medir aderência **sem alterar código**, em duas frentes permanentes: **clean architecture + DDD** (`pantonic-auditor-arch`) e **clean code** (`pantonic-auditor-cleancode`) | Não corrige o que aponta — cada apontamento vira item no diário de obras, priorizado pelo dono |
| **Redesenho** | O mais poderoso disponível (Opus) — separar complexidade acidental de essencial é juízo puro | Varrer a codebase pelo sweep mecânico, identificar procedimentos que ficaram complexos por acúmulo de correções e extensões e propor o redesenho **"do zero, hoje"** dentro das quatro camadas, cada proposta com o que **elimina** e o que **preserva**, riscos, os `TR-*` que protegem e a migração em passos atômicos, no relatório próprio (`pantonic-fora-da-caixa`) | Não implementa o que propõe e não altera código; não redesenha POC validada (`plugins/*/adhoc/`) e não sai das camadas — alvo cuja complexidade é **essencial** é declarado como tal em vez de virar proposta |
| **Benchmarking** | O mais barato (Haiku ou equivalente) | Descrever **um** repositório público já confirmado no esquema fixo de 16 dimensões (`D1..D16`), toda afirmação ancorada na URL exata do arquivo de onde saiu ou marcada `NÃO ENCONTRADO`, no relatório próprio (`pantonic-benchmarker`) | Não julga o PantonicApp e não escreve prosa de recomendação — a comparação é de outro estágio; não responde de memória de treino, não trata dois repositórios no mesmo contexto e não altera nenhum outro arquivo do repositório |

**Escada de revisão de plano.** Quem **suspeita** de que o plano precisa mudar é quem esbarra no
indício — quase sempre a execução, eventualmente a revisão ou a orquestração. Quem suspeita **não
revisa plano**: marca a tarefa como `blocked` com a razão tipada `premissa`, registra o indício
no corpo da tarefa e encerra. Quem **recebe** é o **planejador**, e só ele. Ele decide por si o que for
**técnico** (rota, decomposição, dimensionamento, arquivos-alvo, ordem das tarefas) e o que for
**tático** (fatiar, fundir, adiar ou reordenar tarefas dentro do plano vigente). Sobe ao **dono** o
que for **estratégico** — mudar o objetivo, a prioridade ou a doutrina — ou o que **altere o
escopo** acordado do plano. A orquestração roteia essa escalada; não a resolve. A forma da rodada que o planejador conduz —
entrada, saída e posição na fila — é o `G-REPLAN` (§7 item 17).

Regras de operação:

- O agente de coleta existe para **proteger o contexto dos agentes caros**: varreduras amplas
  nunca são feitas diretamente pelo agente de planejamento ou de execução; são delegadas à
  coleta, que devolve dossiês compactos (caminhos, linhas, assinaturas — nunca arquivos inteiros).
- **Papéis não são intercambiáveis** — a fronteira de cada um (o que faz e o que não faz) está na
  matriz de responsabilidades acima, que é o único lugar onde ela se declara; a adesão estrita a
  essa fronteira é o guardrail `G-SCOPE` (§7, item 15).
- **Modelo por fase é vinculante, não preferência.** Uma preferência de dono ("usar modelo caro
  sempre") não pode inverter a tabela acima para um agente de **execução** — mudar o `model:` de
  um executor para um modelo mais caro exige OK explícito e registrado, nunca herança silenciosa
  de uma memória genérica (custo real medido: executor em Opus com 71 turnos e ~189k de contexto
  numa única tarefa atômica, ~30% do limite de 5h — ver auditoria de consumo referenciada em
  `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`).
- **Gatilho operacional do modelo por fase:** a regra acima é vinculante, mas precisa de gatilho —
  a skill `modelo-por-fase` **do kit versionado** (`.claude/skills/modelo-por-fase/`; `DM-7`,
  2026-07-30, rebaseia `DP-G3` — skill que só existisse em `~/.claude` não viajaria no subtree)
  detecta a fase da tarefa e o modelo ativo, **para** e pede o `/model` correto ao dono (fato
  técnico medido: um agente não troca o próprio modelo — só o dono, via `/model`, ou o harness,
  via hook global). A **regra** mora aqui, versionada (§3.1); a skill é o gatilho e o **hook** é o
  enforcement, canônico no kit e projetado no ponto de carga que o harness lê — nenhum dos dois é
  superfície de doutrina.
- **Delegar a um subagente protege o contexto do orquestrador (Regra 2 do CLAUDE.md), não reduz
  o consumo total.** O subagente parte frio e paga de novo CLAUDE.md + definição do agente +
  skills carregadas em todos os seus turnos. Tarefa pequena (< ~15 turnos estimados) prefere
  execução inline a abrir um subagente.
- **Diretriz de dimensionamento de tarefa (do planejador).** Quem planeja delimita o escopo de
  cada tarefa atômica, e a delimita para satisfazer três critérios: **(a)** caber num contexto
  **coerente e coeso**; **(b)** ser **autossuficiente em contexto para a execução** — o dossiê
  entrega tudo de que a execução precisa, sem leitura ad hoc no meio dela; **(c)** respeitar uma
  estimativa de **50% de ocupação da janela, com tolerância até 60%**. O número não é arbitrário
  nem constante mágica: vem da literatura sobre **decaimento de desempenho de agentes em função do
  enchimento do contexto**, e **é revisável** — cai, e esta diretriz se reescreve, se a literatura
  indicar outro valor. A diretriz é de quem dimensiona e só dele: quem executa não se ocupa de
  teto, de orçamento nem de ocupação — a responsabilidade do executor é executar a tarefa.
  Capacidade **nunca interrompe tarefa em curso** (§4.3); estouro de teto, de orçamento ou de
  contexto é **registrado no corpo da tarefa** e vira insumo para revisão do plano e para eventual
  reexecução da tarefa, havendo suspeita de degradação acentuada por enchimento de contexto.
- **Orçamento de turnos por tarefa atômica — régua interna de quem dimensiona, nunca gate.**
  Subordinado à diretriz acima e endereçado ao **planejador**: os números abaixo dimensionam a
  tarefa antes de ela ser delegada e alimentam a série medida; **não recusam entrega, não roteiam
  e não encerram tarefa nem janela**. Esta tabela é a **única** residência de número de teto —
  nenhum dossiê de tarefa carrega teto. O teto único de
  ~≤40 tool uses tratava tarefas de naturezas diferentes como se custassem o mesmo. Cada classe tem
  número próprio, calibrado pela série medida das linhas `Consumo:` deste repositório (26 registros
  em 2026-08-01), nunca por estimativa:

  | Classe de tarefa | Teto | Como reconhecer |
  |---|---|---|
  | Mecânica / pontual | **≤15** | 1 write-cluster, arquivo(s) já conhecido(s), sem contrato novo |
  | Implementação padrão | **≤40** | vários write-clusters numa camada; contrato novo mas verificação direta |
  | Comportamental multi-camada | **≤60**, com **partição por ramo**: ramo que não cabe no número vira outra tarefa | muda contrato ou fluxo; ciclo editar-rodar-depurar (sync→async, timing de teste) |
  | Investigação / mapeamento | **sem default** — o teto é régua interna de quem dimensiona; o dossiê prescreve o **método de sondagem** | o entregável é descoberta, não mudança de código |
  | Redação de doutrina / planejamento | **≤30** | edita `GOVERNANCA.md`/plano/skill; o custo é decisão, não build |
  | Rodada de replanejamento | **≤50** | fechar a decisão e reescrever os dossiês que ela invalida, no mesmo contexto |

  A **classe é escolhida antes de delegar** e fica registrada. Cruzar o número da classe é
  **alarme para quem dimensiona, nunca bloqueio**: nenhuma entrega para, é recusada ou fica
  incompleta por ter cruzado o número, e nenhum ramo de roteamento se abre por causa dele — quem
  executa sequer se ocupa dele. Escolher classe mais generosa **depois** de cruzar o número é
  falsificação da série: vale a classe registrada antes da delegação.

  O **≤30** da última classe é correção da série sobre a estimativa inicial de ≤25: das 7 tarefas de
  redação já medidas, 5 estouravam ≤25 e só 2 estouram ≤30. Quando série medida e estimativa
  divergem, manda a série.

  **Rodada de replanejamento** — o caso em que fechar a decisão e reescrever os dossiês que ela
  invalida acontecem no mesmo contexto — tem linha própria na tabela. A série medida
  dessas rodadas (19, 21, 39, 43 e 48 tool uses) não cabe em ≤30, e três das cinco o cruzam;
  parti-la entre contextos obrigaria a repagar a leitura da decisão em cada fatia, que é justamente
  o custo que a divisão existe para evitar. O **≤30** continua valendo para redação ou planejamento
  de entregável único. **Custo e consumo são informativos e não têm valor em isolamento** — só
  rendem insight analisados em conjunto, na série medida —, e por isso o controle real não é o
  número: é dividir antes de delegar. O registro **qualitativo** por tarefa — o que o número
  sozinho não diz — reside no card **"Lições aprendidas na tarefa"** do laudo de revisão, e é
  preenchido quando houver o que observar; sem observação, o número isolado daquela tarefa se
  desconsidera.
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
  no contexto e degrada qualidade/custo; filtrar na origem, não depois
  (`.claude/global/CLAUDE.md` Regra 3, dono).
- **Disciplina de coleta** — `git status --short`/`git log --oneline` no lugar dos completos;
  listagem de diretório nunca recursiva sem excluir `build/`, `.venv/`, `node_modules/`; arquivo
  > 500 linhas via Grep + Read com `offset`/`limit`, nunca leitura integral; comando verboso
  não-teste redireciona a saída para arquivo e lê só o fim.
- **Batching de chamadas independentes** — leituras/greps sem dependência entre si vão na mesma
  mensagem; N leituras em 1 turno custam 1 reenvio de contexto, em N turnos custam N reenvios.
- **Disciplina de instrumento** — cinco regras de método, medidas na janela de 2026-09-16
  (`docs/plans/_CARD-revisao-critica-pickup-opus.md`, achados 2-4: seis turnos perdidos). **(a)**
  `--help` antes do primeiro uso de um instrumento do kit numa janela — flag chutada custa um turno
  de correção. **(b)** Sonda que escreve (laudo, RDO, linha de série) aponta o destino para o
  scratchpad pelo flag de diretório, nunca para o caminho canônico — a sonda que "quase gravou" um
  laudo falso só falhou porque a pasta não existia. **(c)** Número que um registro consome (range
  de linhas, contagem, piso) é calculado **na mesma chamada** que o consome, nunca citado antes de
  existir. **(d)** `&&` só encadeia passos em que a falha do anterior deve abortar o seguinte —
  `grep` sem match sai 1 e derruba a checagem seguinte, que então custa outra chamada. **(e)**
  Instrumento antes de protocolo — rodar o instrumento primeiro e ler o protocolo de quem o consome
  só se ele produzir; protocolo lido antes de evidência que não veio é leitura paga sem uso.

### 3.1 Residência e precedência da doutrina

Duas perguntas independentes decidem onde um artefato fica, e valem separadas:

- **Residência** — de quem é o conteúdo e onde ele é canônico. Resposta única, versionada no kit.
- **Ponto de carga** — de onde o harness lê o conteúdo para que ele tenha efeito. Imposto pela
  ferramenta.

Três classes cobrem todo artefato do repositório e da máquina que o executa:

| Classe | O que é | Regra |
|---|---|---|
| **Canônico** | conteúdo do framework: doutrina, skills, agentes, hooks, verificadores e ferramentas | versionado no kit, fonte única; qualquer outra cópia é projeção dela |
| **Ponto de carga** | caminho que o harness lê — `.claude/settings.json`, `~/.claude/` e o que vive sob eles | recebe projeção por comando idempotente e nunca é residência |
| **Local de máquina** | configuração de quem opera a máquina: `permissions.allow`, `additionalDirectories`, preferência de modelo e de esforço, linha de status | nunca é canônico; a materialização o preserva intacto |

**Invariante — nada canônico mora só num ponto de carga.** Conteúdo do framework que existe apenas
em `~/.claude` ou num arquivo de configuração ignorado pelo git não chega a consumidor nenhum, e a
doutrina que o invoca fica sem meio de cumprimento fora da máquina onde nasceu. Onde o harness impõe
um ponto de carga não-versionado, o canônico fica no kit e um materializador o projeta ali; a
divergência entre canônico e projeção é falha de verificador, nunca estado tolerado.

O canônico da doutrina tem quatro superfícies. Esta tabela **decide** o que mora em cada uma e quem
vence quando duas dizem coisas diferentes sobre o mesmo assunto — prescreve a topologia correta.

| Superfície | Mora aqui | Não mora aqui |
|---|---|---|
| Doutrina global — canônica em `.claude/global/CLAUDE.md`, projetada em `~/.claude/CLAUDE.md` | Regra sempre-ativa que vale para **qualquer** projeto do dono, Pantonic ou não | Qualquer regra que só faça sentido dentro do framework Pantonic |
| `GOVERNANCA.md` / `ARQUITETURA_PANTONICA.md` — kit | Regra sempre-ativa **do framework**: identidade, camadas, operações agênticas, guardrails, versionamento | Passo a passo de procedimento; preferência pessoal do dono; estado de trabalho |
| Skill — `.claude/skills/*/SKILL.md` | Procedimento reexecutável, com gatilho declarado e passos na ordem de execução | Regra que precisa valer sem ninguém invocar a skill; estado volátil (backlog, versões, progresso) |
| Agente — `.claude/agents/*.md` | Papel (o que faz e o que não faz) + fatos estáveis que ele precisa saber a frio | Doutrina geral copiada do `GOVERNANCA.md`; estado volátil; dossiê de tarefa |

Hook **não é uma quinta superfície**: é mecanismo de enforcement de uma regra que já mora em uma das
quatro, e hook sem regra escrita atrás dele é doutrina invisível. A declaração do hook é canônica e
versionada; o arquivo de configuração que o harness lê é ponto de carga, produzido por
materialização.

**Precedência, quando duas superfícies colidem:**

1. **Específico vence geral.** Dentro de um projeto Pantonic, `GOVERNANCA.md` vence a doutrina
   global; dentro de uma tarefa, o dossiê vence a skill, que vence o agente. O geral só vale onde
   o específico é silencioso.
2. **Empate → canônico vence projeção.** Projeção não arbitra: divergência entre ela e o canônico é
   defeito de materialização, e o remédio é rematerializar.
3. **Sem desempate → escala ao dono.** Exauridas as regras 1 e 2, a ambiguidade não se resolve
   embaixo: nenhum agente arbitra por palpite, por antiguidade ou por recência. O desempate do
   framework é o dono. A regra de recência governa o desenvolvimento do framework, dentro dos
   planos, e não é critério de desempate de doutrina publicada. Escalar é parar e perguntar; o
   agente não escolhe para informar depois — é a mesma rota que a Regra 8 da doutrina global dá ao
   executor diante de plano ambíguo.

Colisão não se resolve com as duas cópias vivas: quem aplica a regra 1 **apaga a cópia perdedora ou
a reduz a ponteiro**, no mesmo ato. Duplicata é a próxima divergência. Projeção é caso à parte —
tem origem declarada e dono único, e nunca se edita no destino.

**Teste de residência — a pergunta zero, depois as quatro; a primeira que der "sim" decide:**

0. É **ponto de carga** ou **configuração de quem opera a máquina**? Então não mora: recebe. A
   pergunta que resta é qual canônico se projeta nele.
1. Vale para um projeto **não-Pantonic** do dono? → doutrina global.
2. É regra **sempre-ativa do framework**, que precisa valer sem ninguém invocar nada? →
   `GOVERNANCA.md` (ou `ARQUITETURA_PANTONICA.md`, se for regra de arquitetura).
3. É **procedimento reexecutável com gatilho** ("quando acontecer X, fazer estes passos")? → skill.
4. É **papel + fatos estáveis** de quem executa? → agente.

Nenhuma das quatro: não é doutrina. É estado de trabalho, e o lar é o diário de obras.

**Governança das memórias do harness** — incluindo a fila de candidatos, em que o agente enfileira e
**só o dono promove** — passa na pergunta 1: é doutrina global, canônica em
`.claude/global/docs/GOVERNANCA_MEMORIAS.md` (§8) e projetada no ponto de carga
`~/.claude/docs/GOVERNANCA_MEMORIAS.md`.

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
| Item de backlog / história | **tarefa atômica** — uma por contexto (§4.3); quem a dimensiona é o **planejador**, sob a *Diretriz de dimensionamento de tarefa* (§3) |
| Time auto-organizado | **papéis fixos e não intercambiáveis** — matriz de responsabilidades (§3) |
| Cerimônias (daily, planning, review) | **atos escritos**: dossiê de tarefa, handover e veredito de validação no diário — o que só existe em conversa não sobrevive à troca de contexto e, portanto, não existe |
| Definition of done | **critério de pronto** no dossiê + guardrails executáveis (§7), gate de conformance e piso de regressão (§4.4) |

Duas práticas ágeis **não** viajam. Estimativa em story points: o recorte de uma tarefa sai da
*Diretriz de dimensionamento de tarefa* (§3), exercida pelo **planejador** e aferida depois pelo
consumo medido em `docs/telemetria.tsv` — nunca estimada por analogia, e nunca observada pelo
executor. E auto-organização de escopo: o executor não escolhe o que fazer nem redefine a
tarefa — decidir é fase do planejamento (§3, §7 itens 9 e 12).

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
- Cada item de trabalho carrega um **status**. A lista de valores, a máquina de transições e o
  alcance de cada estado por objeto (tarefa, plano/iniciativa, tíquete) têm **residência única** —
  skill `diario-de-obras`, seção "Status — residência única". Nenhum outro artefato reenuncia a
  lista: quem precisa de um estado aponta para lá.
- Possui um **índice abrangente no topo** (uma linha por item: ID, título, status, âncora), de
  modo que o agente de execução encontre seu trabalho **sem ler seções irrelevantes** ao seu
  contexto. O índice é atualizado a cada mudança de status.
- Itens concluídos são condensados periodicamente para um histórico append-only, mantendo o
  diário enxuto (mesma disciplina ATIVO × HISTÓRICO usada nos demais docs do projeto).
- **Diretiva de priorização** — uma linha fixa no topo do diário, logo abaixo do título,
  registrando a prioridade vigente (ex.: "Priorize iniciativa X"). Vazia por padrão (prioridade
  fica a cargo do agente, heurística: destravar `blocked` → concluir `in-progress`, WIP de 1
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
- **Fronteira de registro — três artefatos, nenhum repetindo o outro.** O **diário** é o kanban:
  índice, status, diretiva de priorização e ponteiro. O **RDO** (`docs/RDO/<plano>-<tarefa>-<slug>.md`,
  um arquivo por tarefa) é o **registro canônico da tarefa**: dossiê recebido, laudo, desdobramento e
  ponteiros para os artefatos tocados. O `docs/telemetria.tsv` é a fonte única do número de consumo.
  Quem precisa do detalhe de uma tarefa abre o RDO dela; o diário guarda a linha de status que aponta
  para lá. Duplicar conteúdo entre os três cria fontes que divergem na primeira edição.
- **Fechamento enxuto** — o detalhe da execução mora no RDO da tarefa, e o relatório final ao
  orquestrador é ponteiro + deltas. **Achado de execução tem um registro só:** bloqueio, obstáculo
  ou fato que contradiz o plano é escrito uma vez, como entrada `AE-<n>` em `## Achados da
  execução` do plano; nota da tarefa, `Fila corrente` e célula do índice recebem apenas `AE-<n>` +
  `caminho:linhas`, e o handover ao dono cabe em ≤ 8 linhas com o ponteiro. O mesmo fato escrito
  cinco vezes numa janela — um terço dela gasto no fechamento de um bloqueio (caso medido,
  2026-09-16) — é o defeito que esta regra fecha.
- **Telemetria pela notificação, não pelo auto-relato** — o consumo de uma tarefa é registrado
  pelo **orquestrador** como uma linha em `docs/telemetria.tsv`, lendo o bloco `<usage>` da
  notificação de conclusão do subagente (dado medido) — nunca copiando a estimativa que o próprio
  subagente eventualmente escreve no texto do handover (auto-relato subestima: caso medido
  registrou ~90k autorrelatado contra ~140k reais, ~35% de subestimativa). Cria série histórica
  para detectar regressão de consumo por tarefa, mesmo racional do piso de regressão de testes
  aplicado a custo. O registro do consumo, na série e no diário, é escrito pelo **orquestrador** a
  partir do dado medido da notificação.
- **Fonte única da série** — `docs/telemetria.tsv` (append-only, colunas `data`, `projeto`,
  `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte` ∈ `{usage, contado,
  nao_medido}`) é a **fonte da série de consumo**; o diário/histórico **aponta** para ela
  (`Consumo: ver docs/telemetria.tsv`) em vez de copiar o número. Duplicar a medição em prosa
  recriaria duas fontes que divergem à primeira edição. Registro qualitativo que não cabe em
  coluna (estouro de teto, execução inline, ressalva sobre a medida) continua no bullet do diário,
  ao lado do ponteiro — o que não se repete é o **número**. Bullets `Consumo:` anteriores à adoção
  desta regra ficam como estão: são registro histórico, já espelhado na série. **`contado` exige
  contagem efetiva** — chamadas contadas no transcript, não estimadas de memória; contagem não
  feita entra como `nao_medido` (caso medido, 2026-09-16: `contado` = 14 contra 29 reais).

### 4.3 Execução em contexto limpo

- **Um contexto sustenta um cenário coerente** e segue enquanto tudo que entra pertence a esse
  cenário. Duas condições independentes o governam, e basta uma cair para o contexto acabar:
  - **Coesão** — entrando material de outro cenário, ou material que contradiz o que já está lá, o
    contexto está **poluído**, e contexto poluído não se recupera, se substitui. A violação é
    **fatal e imediata**: para-se ao primeiro sinal, sem terminar o que está aberto, porque o que
    for decidido depois do sinal já é decisão poluída. Sinais de poluição, em checagem obrigatória
    e lista não exaustiva: material de outra tarefa, outro plano ou outra iniciativa entrou no
    contexto; premissa que sustentava o trabalho foi derrubada no meio dele; a rota bifurcou ou uma
    decisão do dono contradiz o que já foi ingerido; duas fontes do mesmo fato divergem sem
    descarte imediato; entrou informação ambígua ou controversa que muda o que já foi feito.
    Corrigir o próprio erro, sobrescrever valor errado e refinar detalhe não poluem: a contradição
    é fatal quando atinge o **cenário** (premissa, rota, contrato), e não quando atinge um detalhe
    que o próprio contexto já substituiu. A parada é **não graciosa**: nada do produzido depois do
    sinal se aproveita, não há fechamento cerimonioso e quem executa retorna a quem orquestra
    **demandando contexto limpo para a reexecução**.
  - **Capacidade** — não é condição de execução: dimensiona a tarefa antes de ela ser delegada
    (§3, *Diretriz de dimensionamento de tarefa*) e **nunca interrompe tarefa em curso**. Quem
    executa não para, não parte a entrega e não devolve trabalho por ocupação de janela.
- **Para quem executa, uma tarefa por contexto.** Para quem orquestra, conduzir um plano **é** uma
  tarefa: o contexto atravessa várias tarefas atômicas, porque o cenário é o mesmo, e encerra na
  troca de plano ou iniciativa — troca de cenário — ou, de forma planejada, na ocupação da janela,
  o que vier antes. Esse encerramento é ato da **orquestração, entre tarefas** — nunca dentro de
  uma tarefa, nunca do executor. O hook `PreToolUse` `.claude/tools/ocupacao.py`, que lê o
  transcript da sessão principal, calcula a ocupação contra a janela e injeta o aviso quando ela
  cruza o limiar, é **aviso informativo** à orquestração: não é gate, não recusa entrega e não
  interrompe tarefa.
- Ao concluir (ou bloquear) uma tarefa, quem executa **sinaliza** o resultado (`review`, ou
  `blocked` com razão tipada) e encerra o próprio contexto — o contexto **do executor**, um por
  tarefa. Registrar o fechamento no diário de obras e abrir a tarefa seguinte em contexto limpo
  **do executor** são da orquestração (§3); a janela de orquestração é outra coisa e **não**
  fecha junto — ela segue as regras do bullet anterior, e não encerra por tarefa concluída.
- **Acionamento do dono — a causa decide.** Dirimir ambiguidade e resolver conflito, sobretudo de
  **requisito** e de **aceitação**, é responsabilidade do dono, e é ilimitada: nenhum teto de
  acionamentos governa a aceitação de uma entrega, porque um limite desses seria arbitrário. Nenhum
  agente decide aspecto de aceitação sem estar **inequivocamente** seguro de ter a melhor solução —
  na dúvida, escala (§3.1, item 3), e escalar é o comportamento desejado. **Escalar tem um canal,
  e ele não passa pelo meio da execução:** quem executa para, registra o fato, bloqueia e encerra;
  o planejamento recebe, decide o que é seu e leva ao dono, numa rodada com contexto, opções e
  insumos, só o estratégico (G-NOASK, §7 item 18). Pergunta que chega ao dono no meio de uma
  execução pede resolução inesperada, sem contexto e sem insumos — é falha de planejamento, não
  acionamento legítimo. A entrega é ineficiente
  quando o framework aciona o dono em **caminho feliz ou caminho natural**, sem pendência aberta e
  sem demanda que seja dele: parar para que ele limpe o contexto e invoque a tarefa seguinte o põe a
  **mediar execução normal**, e uma única ocorrência dessas é defeito.
- **Retomada sem tarefa nomeada** — quando o usuário abre um contexto novo e pede apenas para
  seguir o backlog ("execute o próximo passo"), o ponto de entrada é a skill `proximo-passo`: ela
  drena o inbox de planos, aplica a diretiva de priorização (ou a heurística padrão), escolhe uma
  única tarefa e delega ao agente de execução. O handover final sempre reporta a tarefa feita, a
  iniciativa/plano de origem, e o **índice de conclusão do plano** (`<done>/<total>` no diário).
- **Checkpoint intermediário** — é da **orquestração**: quando a janela de orquestração se
  encerra (coesão ou ocupação) com tarefas do plano ainda abertas, quem orquestra grava até 5
  linhas de ponteiro de estado no plano em curso (skill `handover`, seção "Checkpoint
  intermediário"), teto de 2 tool uses, para que a janela seguinte retome sem redescobrir o que já
  foi pago. A tarefa que não chegou a ser entregue volta ao estado em que estava — nunca `done`.
- **Dois casos que não são checkpoint** — contexto acabando **dentro** de uma tarefa não é evento
  a mitigar: é sintoma de que o recorte errou o dimensionamento (§3), registra-se o fato no corpo
  da tarefa e a matéria volta ao planejamento, sem retomar a tarefa pela metade. E o **sinal de
  poluição** não gera ponteiro de retomada, porque não há retomada: nada se inicia depois do
  sinal e o retorno a quem orquestra é a declaração de poluição mais a demanda de reexecução em
  contexto limpo.

### 4.4 TDD obrigatório

Todo desenvolvimento segue TDD, garantindo prioritariamente dois tipos de teste:

- **Funcionais (TF)** — verificam se a função faz o que deve fazer; derivados dos casos de uso e
  requisitos do PRD, definidos já no Sprint Plan.
- **Regressão (TR)** — verificam que um estado funcional anterior não quebrou (ausência de
  colaterais).

**Cadência de testes** — Tier 1 roda no máximo 2× por tarefa (após implementar, após corrigir),
nunca a cada micro-edição; tier superior só no fechamento (`.claude/global/CLAUDE.md` Regra 7;
skill `test-tiers`).

**Piso de regressão — comportamentos trancados, nunca percentual.** O piso é o conjunto de
**comportamentos** que o projeto já garante e não pode perder. Ele **não é** percentual de
cobertura, e percentual de cobertura **não** vale como piso, meta ou critério de pronto em nenhum
ponto desta doutrina: piso percentual premia manter teste de código morto para não derrubar a
métrica — exatamente o que `G-DEADCODE` (§7, item 8) proíbe. Escrito como comportamento, o piso
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
- **O caso de uso é um artefato, não uma pasta.** Dentro do plugin ele tem residência própria,
  depende só de contracts e é apenas invocado pela superfície de apresentação — caminho, forma e o
  que não pode morar nele estão em
  [ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md) §9.1, que é o texto normativo.

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

**Grau de aderência da implementação atual: medido.** Esta seção declara a **doutrina**; o grau em
que a implementação de referência (`PantonicVideo`) de fato a segue é registrado nos relatórios de
auditoria de arquitetura em `docs/audits/` daquele repositório, não inferido. Os plugins estendem
DDD na escrita, nos métodos do agregado, e não na leitura, que ainda projeta o agregado em
estruturas primitivas — 49 projeções `list[dict]` em 14 módulos, e 5 de 15 plugins anotam a porta
com `Protocol`. A camada de casos de uso não tem artefato próprio naquele projeto: nenhuma classe
de caso de uso, com a orquestração dispersa em 14 adaptadores de apresentação (5.216 linhas) e numa
fachada de serviço (781 linhas, 18 métodos públicos). A residência que fecha esse vão é a §9.1 do
documento de arquitetura; a medição vale como fato do case de referência, nunca como conformidade
já alcançada.

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
2. **Architecture** — modelo conceitual da arquitetura com base em **clean architecture + DDD**,
   **partindo do core pantonico**
   ([ARQUITETURA_PANTONICA.md](ARQUITETURA_PANTONICA.md)) e especializando as camadas baixas.
   Determina os limites de cada camada e as responsabilidades de cada uma; **cada responsabilidade
   é mapeada aos casos de uso e requisitos do PRD** (rastreabilidade Feature → UC/RF →
   responsabilidade).
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
3. **Egress único de filesystem** — só o componente de filesystem escreve em disco (regra G6 da
   arquitetura), verificado por teste AST.
4. **Namespace de estado** — plugin só escreve em `plugins.<nome>.*`, salvo whitelist explícita;
   verificado por teste de boundary.
5. **Gate de conformance** — a suíte de conformance é bloqueante: nenhuma tarefa é `done` com
   conformance vermelho.
6. **Piso de regressão** — o piso nunca desce; mudanças comportamentais intencionais exigem
   registro de decisão no doc de estado vigente do projeto.
7. **Disciplina de contexto** — um contexto sustenta um cenário coerente: material de outro
   cenário, ou que contradiz o já ingerido, polui o contexto e obriga **parada não graciosa** no
   ato, sem aproveitar nada do produzido depois do sinal e demandando
   **contexto limpo para a reexecução** (residência canônica: `.claude/global/CLAUDE.md`, Regra 2;
   texto operacional em §4.3). Ocupação de janela não é matéria deste guardrail: é diretriz de
   dimensionamento de quem planeja (§3). Varreduras amplas só via agente de coleta; docs grandes
   acessados via índice/DOC_MAP, nunca lidos integralmente.
8. **G-DEADCODE — nada de código morto testado** — todo símbolo de produção (função/classe/módulo
   fora de `tests/`) precisa de **ao menos um chamador de produção** alcançável a partir de um entry
   point real (plugin registrado, superfície de serviço no contrato, bootstrap). Cobertura por teste
   **não** confere "vivo": símbolo testado sem chamador é o pior caso, porque a suíte verde o
   **mascara**. Ao abandonar uma rota, os módulos da rota abandonada morrem **no mesmo commit** —
   nunca ficam como fantasmas testados. *Enforcement:* check executável de símbolo de produção órfão
   (alcançabilidade por AST a partir dos entry points, allowlist explícita e mínima) no kit de
   conformance; a revisão de fechamento confere os chamadores de produção de cada símbolo novo e
   rejeita módulo novo sem chamador não-teste.
9. **G-PLANFIDELITY — a rota é do dono** — conduta universal de executor (não doutrina específica
   de Pantonic), promovida ao `CLAUDE.md` global (Regra 8, `V2M-T3`, 2026-07-30): o executor não
   substitui a arquitetura/rota aprovada por uma alternativa própria sob pressão de obstáculo
   técnico — ver texto normativo lá. *Enforcement:* gate de review — a revisão confronta a entrega
   com a rota do dossiê e confirma que nenhuma bifurcação arquitetural ocorreu sem decision record.
10. **G-PREMISE — premissa que embasa abandono exige prova, não asserção** — afirmar *"a informação X
   não existe / não é obtível"* só sustenta abandono ou bifurcação de rota com um **spike que a
   comprove**, revisável pelo dono, **antes** do abandono. Um achado não **reverte** achado anterior
   de outra sprint sem reconciliação explícita registrada. Corolário: se a solução do obstáculo
   apareceu na rota alternativa, verifique **primeiro** se ela cabe na rota original — normalmente
   cabe. *Enforcement:* gate de review no fechamento da tarefa que abandona/bifurca; o decision record
   cita o spike e reconcilia qualquer achado contraditório.
11. **G-PLANREADY — plano só é executável quando fechado** (dever do **planejador**) — antes de um
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
12. **G-EXECREADY — o executor não decide, não pergunta e recusa plano não-pronto** (dever do
   **executor**) — conduta universal de executor (não doutrina específica de Pantonic), promovida
   ao `CLAUDE.md` global (Regra 8, `V2M-T3`, 2026-07-30): nunca inicia o trabalho fazendo perguntas
   ao dono, e recusa performar enquanto o plano não estiver pronto por G-PLANREADY — ver texto
   normativo lá. Complementa G-PLANFIDELITY (não muda rota) e o modelo por fase (§3): a decisão
   nunca desce para o modelo barato. *Enforcement:* instrução no arquivo do agente
   `pantonic-executor`; a `proximo-passo` só delega tarefa de plano fechado; gate de review.
13. **Allowlist de subcomandos destrutivos** — **Comando destrutivo não é decisão de agente.**
   Reescrita de histórico, descarte de trabalho não commitado e remoção de branch/repositório
   ficam negados em `.claude/settings.json` (`permissions.deny`) para todo agente com `Bash`. O
   modo de falha correto é **ruidoso** — comando negado, agente reporta ao dono — nunca
   silencioso. Ampliar a lista é rotina; encurtá-la exige ato explícito do dono registrado no
   diário. *Enforcement:* `permissions.deny` em `.claude/settings.json` (`Bash(git push
   --force*)`, `Bash(git push -f*)`, `Bash(git reset --hard*)`, `Bash(git branch -D*)`,
   `Bash(git clean -fdx*)`, `Bash(gh repo delete*)`).
14. **G-README — o README é documento canônico, não artefato acessório** (`DR-7`, 2026-08-05) — o
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
15. **G-SCOPE — o agente se atém estritamente às suas responsabilidades declaradas; o que não está
   escrito é proibido.** A residência do escopo de cada papel é a **matriz de responsabilidades**
   (§3), que é autoridade **exaustiva**: o que ela não declara, nenhum agente faz. Prompt de agente
   **não cria** responsabilidade por conta própria — descrever-se fazendo o que a matriz não declara
   é violação, não extensão. Proibição em prompt só se justifica quando restringe o exercício da
   **própria** responsabilidade declarada; a que apenas repete "não faça o que é de outro papel" é
   redundante e sai. Encontrada a violação em **artefato existente**, a resposta é a mesma que a do
   prompt novo: artefato do framework que atribui a um agente ato **não endossado** pela matriz — ou
   que carrega papel que a matriz **sequer cita** — é **não-conformidade grave**, que se para e
   regulariza, em vez de enfileirar como dívida. A lacuna oposta **não se resolve no ato**: quando o
   ato atribuído é **real e necessário** mas a matriz não o declara, a falta é **da matriz**, e criar
   a responsabilidade no prompt é exatamente a violação — registra-se e **sobe ao dono**, que decide
   (mesma regra da `DP-M`, §16.5). *Enforcement:* instrução em todo arquivo de agente e em toda skill
   que carrega papel; gate de review sobre prompt novo ou alterado, e varredura dos artefatos já
   existentes.
16. **G-SURFACE — mudança de decisão estruturante regulariza a superfície de contato inteira, no
   ato.** O gatilho é a **decisão estruturante**: correção ou modificação de **objetivo-chave**,
   **requisito** ou **caso de uso** — a que altera o que o trabalho *é*. Não é toda mudança:
   refinar redação, corrigir número ou trocar âncora não dispara a regra. Disparada, a ação é
   **imediata** e cobre **toda a superfície de contato** da decisão, não só o artefato em que ela
   foi tomada — regularização a posteriori não é opção. A rodada de planejamento que fecha a
   decisão estruturante **emite os cards de regularização no mesmo ato**, e a fila não avança sem
   eles. O custo de adiar é o que a regra existe para evitar: o agente seguinte, que não tem o
   contexto do ato, para para pedir a regularização — e, no pior caso, ingere texto vigente e texto
   derrubado lado a lado, que é o sinal de poluição da Regra 2 (§4.3). *Enforcement:* gate de
   planejamento — a rodada que fecha a decisão estruturante emite os cards de regularização, e o
   plano não avança sem eles — somado ao gate de review.
17. **G-REPLAN — bloqueio por premissa é gatilho de revisão do plano, não pendência do dono**
   (dever do **planejador**; roteamento da **orquestração**). Tarefa devolvida `blocked` com razão
   `premissa` (card defeituoso, rota inviável, fato que contradiz o plano) **não** fica parada
   esperando o dono e **não** é contornada despachando a tarefa seguinte do mesmo plano: ela abre,
   no mesmo ato, uma **rodada de replanejamento** — item de classe *Rodada de replanejamento* (§3),
   no modelo do planejamento — que passa a ser a **próxima tarefa** do plano (topo da fila, acima
   de toda tarefa `ready` dele), e o plano vai a `blocked` com a razão até a rodada fechar. A rodada
   tem entrada, saída e residência fixas. **Entrada:** o achado registrado no corpo da tarefa e em
   `## Achados da execução` do plano. **Saída:** (a) a decisão nova, com id, na tabela de decisões;
   (b) os cards que a decisão invalida reescritos — inclusive o fato que faltou na §1; (c) a tarefa
   bloqueada de volta a `ready` (ou `cancelled`, se a rota mudou) e o plano de volta ao estado
   anterior; (d) o achado marcado como absorvido, com ponteiro para a decisão; (e) a **lição para o
   planejador** — a verificação de autoria que teria evitado o bloqueio — aplicada ao arquivo do
   agente `pantonic-planner` quando a classe de erro for nova. **Residência:** uma entrada `RP-<n>`
   sob `## Achados da execução` do plano, com a classificação da mudança. O planejador decide
   sozinho o que for técnico ou tático (escada de revisão de plano, §3) e leva ao dono, em **uma**
   rodada de decisões, só o que for estratégico ou alterar escopo; o dono não desempata card.
   Segundo bloqueio `premissa` na mesma tarefa depois de uma rodada é sinal de que a premissa caiu
   por inteiro: o plano vira `superseded` e o sucessor nasce fechado. *Enforcement:* roteamento
   `A3b` da skill `scrum-master` (escala ao planejador, não ao dono); guardrail da `proximo-passo`
   (tarefa `blocked premissa` no plano priorizado → a próxima tarefa é a rodada, nunca outra do
   plano); seção "Rodada de replanejamento" do agente `pantonic-planner`; ledger
   `docs/telemetria.tsv` (a rodada é medida na classe própria).
18. **G-NOASK — interrupção para escalar ao dono durante a execução é falha de planejamento**
   (dever do **planejador**; conduta do **executor** e da **orquestração**; decisão do dono,
   2026-09-16, sobre o caso medido em `docs/plans/_CARD-revisao-critica-pickup-opus.md`). A
   pergunta que chega ao dono no meio de uma execução pede dele uma resolução **inesperada, sem
   contexto e sem insumos** — o oposto da rodada de decisões do planejamento, que chega com
   contexto, opções, recomendação e consequência. Três deveres. **(1) Quem executa nunca fica com
   dúvida e nunca escala direto ao dono** — executor, e a orquestração enquanto conduz a janela: ao
   primeiro sinal de dúvida (referente ausente, instrumento que não produz, obstáculo à rota, dois
   caminhos possíveis), **para, registra o fato** (`AE-<n>` em `## Achados da execução` do plano),
   **bloqueia** (`blocked` razão `premissa`) **e encerra**. Não classifica a dúvida ("é do dono?",
   "é evento intrínseco?") — ponderar já é decidir; não pergunta; não escolhe "o óbvio". **(2) O
   destino do bloqueio é o planejamento** (G-REPLAN): a rodada decide o que é técnico ou tático e
   leva ao dono, em uma rodada, só o estratégico. Ao dono, durante a janela, não chega pergunta
   nenhuma; a orquestração fala com ele **só no relatório de encerramento**, e toda opção de rota
   apresentada ali — ou na rodada de decisões do planejador — inclui a alternativa **registrar e
   não agir** quando ela existir (no caso medido era a mais barata, faltou da lista e foi escolhida
   por "outro"). **(3) O planejador nunca libera plano com alto risco de interrupção**: a
   auto-auditoria percorre cada card à procura dos pontos em que um executor frio pararia —
   referente não verificado no repositório, instrumento não sondado com a chamada exata,
   contingência ausente para o caso observável, número não re-derivável por comando dado — e cada
   ponto vira contingência fechada, fato na §1 ou partição da tarefa, **ou o card não sai**. Plano
   com ponto de interrupção sem contingência é plano aberto (G-PLANREADY condição 5).
   *Enforcement:* instrução nos agentes `pantonic-executor` (parada por dúvida) e
   `pantonic-planner` (teste de interrupção, fase 4); `scrum-master` e `proximo-passo` (nenhuma
   pergunta ao dono entre o despacho e o relatório de encerramento; `B1` roteia ao planejador);
   gate de review — decisão tomada pela entrega que o card não fechou, e parada por dúvida que o
   card não previu, são achado de processo de alvo `dossiê`.

Esses guardrails são materializados em cada projeto como: instruções nos arquivos de agente
(`.claude/agents/*.md`, CLAUDE.md do projeto) **e** testes de conformance executáveis — a regra
que não é testável por código deve, no mínimo, constar como checklist de review.

### 7.1 Revisão e deprecação de guardrails

Um framework que só adiciona regra apodrece: o custo de ler a doutrina cresce a cada rodada de
trabalho e nenhuma regra jamais sai. Esta seção é a **porta de saída** — a única forma legítima de
remover um guardrail de §7.

**Gatilho.** A revisão pendura-se no **fechamento de um plano** — a linha do plano (`P-NNNN`) indo
a `done` no índice de `docs/DIARIO_DE_OBRAS.md` —, nunca em calendário e nunca em número de versão.
Data no calendário vira cerimônia executada sem material novo para julgar; o fechamento de um plano
é exatamente o momento em que há material novo para julgar. Cada fechamento abre uma **rodada** de
revisão.

Operacionalizada pela skill `checar-versao-kit`, que arma o gatilho na criação do plano seguinte:
confrontado o índice do diário com o **registro das rodadas** abaixo, um plano fechado depois da
última rodada registrada deixa a revisão **pendente**, e a skill reporta ao dono. A skill não
executa a revisão: ela é tarefa nomeada, com registro próprio no diário.

Um plano pode fechar sem que nenhum plano novo seja criado logo depois; nesse caso o aviso aparece
na próxima criação de plano. O atraso é aceito por desenho — o gatilho troca pontualidade por custo
zero de cerimônia.

**Escopo.** Entram só as guardrails com **≥2 rodadas de idade** — as que já constavam de §7 na
**penúltima** rodada registrada. Regra recém-adicionada não teve tempo de agir; cobrar evidência
dela é medir ruído. Enquanto o registro abaixo não tiver duas rodadas deste regime, a rodada
`1.4.0` faz as vezes de penúltima: entram as guardrails que já constavam de §7 nela.

**Isenção por enforcement executável.** Guardrail cujo cumprimento é verificado por um **check executável ativo** — teste de
conformance, gate de CI, script do kit — **não entra na pergunta**: o check verde é a evidência de
vida. A pergunta vale para guardrail **advisória ou procedimental**, cujo único rastro possível é o
registro escrito. Motivo: regra preventiva enforçada por código só produz caso citável quando
alguém a **viola**; funcionando, ela é silenciosa, e a pergunta a condenaria justamente por
sucesso. A isenção **não é declarativa** — quem a invoca **nomeia o check** (caminho do teste, ou o
comando do gate) e confirma que ele roda hoje. Check inexistente, desabilitado (`skip`, `xfail`) ou
neutralizado (allowlist que cobre todos os casos) **não isenta**: a regra volta à pergunta, e o
check morto é achado próprio, a reportar.

**Pergunta única, aplicada a cada guardrail em escopo e não isenta:**

> Esta regra mudou algum comportamento desde a penúltima rodada registrada? Cite o caso.

**Caso citável** é uma ocorrência **registrada** no intervalo — diário de obras (do hub **ou de um
consumidor**), `CHANGELOG.md`, nota de fechamento de tarefa, decision record — em que a regra
bloqueou algo, forçou uma correção ou embasou uma decisão. Duas exclusões, porque são o modo de
falha da pergunta: **suíte verde não é caso** (é a regra sendo satisfeita, não agindo) e
**lembrança sem registro não é caso** (se ninguém escreveu, não conta). A evidência de guardrail de
arquitetura mora no consumidor, não no hub — o hub não tem código de produção, e avaliar essas
regras só pelo registro dele responde "não" por construção.

**Resultado.** Sem caso citável, a guardrail é marcada **`OBSOLETA desde <rodada>`** no próprio
item, identificada a rodada pelo plano que a disparou (`P-NNNN`); ela **permanece em vigor** por
**uma rodada** de transição e é **removida na rodada seguinte** — a remoção é uma tarefa nomeada
como qualquer outra, com registro no diário. Um único caso citável
durante a transição desfaz a marcação. **Zero marcações numa rodada é resultado legítimo; não
registrar a rodada não é** — revisão sem registro não aconteceu.

**Registro das rodadas.** Cada rodada entra na lista abaixo sob o rótulo `<P-NNNN> — <AAAA-MM-DD>`,
com o plano cujo fechamento a disparou, as guardrails avaliadas, as que ficaram fora por idade e o
resultado item a item.

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
  **Marco zero do regime de rodadas por plano:** contam os planos fechados a partir de 2026-08-01;
  tudo anterior a essa data está coberto por esta rodada.
- **`P-0731` — 2026-08-08** (primeira rodada do regime por fechamento de plano): 14 guardrails em §7,
  **13 em escopo**, **1 fora por idade** (**G-README**, nascido depois da rodada anterior). As 13
  foram identificadas por nome e conteúdo, não por número: a numeração deslocou quando o guardrail de
  fronteira MVVM saiu de §7.
  **Seis isentas por enforcement executável**, com o check nomeado e confirmado rodando no consumidor
  `PantonicVideo` (**17 passed**, nenhum `skip`/`xfail` — o único `pytest.skip` é guarda condicional
  de `plugins/` ausente): regra de dependência → `tests/conformance/test_layer_imports.py`; ACL →
  `tests/conformance/test_acl_no_external_in_plugins.py`; egress G6 →
  `tests/conformance/test_filesystem_egress.py`; namespace de estado →
  `tests/boundary/test_state_writer_namespacing.py`; gate de conformance → a própria suíte
  bloqueante (as quatro acima no consumidor, mais `python -m pytest` como passo da bateria de
  fechamento de toda tarefa do hub); allowlist de subcomandos destrutivos → `permissions.deny` em
  `.claude/settings.json`, 6 entradas ativas.
  **Sete na pergunta, todas com caso citável:** piso de regressão (a suíte que ancorou o
  comportamento vigente do detector de código morto foi escrita **antes** da troca do mecanismo, e só
  por causa dele); disciplina de contexto (o índice de docs mandando ler integralmente um documento
  que passou do limite de tamanho virou achado registrado); **G-DEADCODE** (embasou a troca da tabela
  de exceções por arquivo declarativo do projeto e a recusa de criar verificador sem alvo);
  **G-PLANFIDELITY** (o executor parou diante de um dossiê que prescrevia suíte inexistente em vez de
  inventar rota alternativa, e classificou como consequência mecânica — não bifurcação — uma edição
  adjacente ao alvo); **G-PREMISE** (duas declarações de aderência ficaram "não auditado" em vez de
  afirmar conformidade antes da medida); **G-PLANREADY** (o gate reprovou um dossiê publicado e forçou
  partição em duas fatias, com a decisão de arquitetura subindo ao dono); **G-EXECREADY** (o mesmo
  episódio, do lado do executor: recusou performar e não decidiu no lugar de quem planeja).
  **Resultado da rodada: 0 marcações.** Resultado item a item em `docs/DIARIO_DE_OBRAS.md`.
  **Achado próprio da rodada:** o ratchet do piso comportamental roda **sem alvo** — o hub ganhou
  suíte mas nunca declarou o arquivo de piso, e nenhum consumidor materializa o kit de checks, de modo
  que o check passa por vacuidade em toda parte. Não isentou o guardrail nesta rodada porque o caso
  citável veio do registro, não do check.

## 8. Documentação mínima de um projeto Pantonic*

| Documento | Papel |
|---|---|
| `README.md` (raiz) | **Documento canônico** — o contrato entre o framework e o cliente, e a porta de entrada humana (§7 item 14, §9). Não é derivado nem acessório |
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
(2026-08-05) esse status é **guardrail** — §7 item 14 (G-README): o README é o **contrato entre o
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

**Congelamento pré-lançamento.** O framework não foi lançado: a versão é `0.0.0` e não anda até que
o dono decida publicar. Enquanto congelada:

- **Não há bump.** A exigência de que os três artefatos de versão se movam juntos reduz-se a um: a
  linha no `CHANGELOG.md` sob `[Não lançado]`, que registra toda mudança canônica.
- **O hub não publica tag nova.** A branch `kit` segue distribuindo o kit; o que fica suspenso é a
  criação de `kit-v<versão>`.
- **A checagem de versão não compara e não toca a rede.** Ela reporta a versão congelada e encerra.
- **As tags `kit-v*` e as seções numeradas do `CHANGELOG.md` já existentes permanecem** como
  histórico de desenvolvimento pré-lançamento; nenhuma é revogada ou reescrita.
- **Descongelar é ato do dono.** O ato fixa a primeira versão publicada e reativa o mecanismo
  completo de versionamento, tag e checagem.

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
não carrega. A partir do lançamento, o hub publica uma tag git `kit-v<versão>` na branch `kit` (o
subtree de `.claude/`) a cada mudança canônica. Cada projeto consumidor materializa a versão que
recebeu em `.claude/kit/KIT_VERSION`. A checagem compara as duas com uma única chamada de rede —
`git ls-remote --tags <url> "kit-v*"` — que não faz fetch nem toca a árvore de trabalho do
consumidor; enquanto a versão está congelada, essa chamada fica suspensa.

**Resultados possíveis da checagem.** Sob congelamento vale o primeiro; os demais descrevem o
mecanismo em vigor a partir do lançamento.
- **Versão congelada (`0.0.0`)** → reporta "congelada — nada a comparar" e encerra, sem chamada de
  rede.
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

**Critério de pronto.** Qualquer tarefa que edite `.claude/` do hub só está pronta com o registro
que o regime vigente exige: sob congelamento, a linha no `CHANGELOG.md` sob `[Não lançado]`; fora
dele, o bump de `.claude/KIT_VERSION` acompanhando a mudança. No regime numerado, o bump é o
critério porque uma versão que não sobe quando o conteúdo muda deixa a checagem cega — o guarda
vira teatro.

**Paridade `VERSION` × `.claude/KIT_VERSION`.** `VERSION` (raiz — o framework: doutrina + kit) e
`.claude/KIT_VERSION` (o que o subtree publica) carregam **sempre o mesmo valor**; divergência entre
eles é defeito. A exigência não tem exceção: sob congelamento os dois carregam `0.0.0`. Semver com
significado declarado, operante a partir do lançamento: **MAJOR** = exige ação do consumidor
(artefato removido/renomeado, doutrina invertida); **MINOR** = artefato ou guardrail novo compatível
com o que já existe; **PATCH** = correção redacional, sem mudança de comportamento. Fora do
congelamento, toda tarefa que edite `.claude/` ou a doutrina bumpa os dois arquivos **e** escreve
uma linha correspondente no `CHANGELOG.md` (raiz) — os três se movem juntos, nunca um sem os
outros dois. Sob congelamento, o conjunto reduz-se à linha no `CHANGELOG.md`.

**O que se distribui, executa.** Agentes e skills são instruções que rodam com as ferramentas
que o frontmatter concede; um artefato adulterado no hub vira execução em todo consumidor. O
passo de sync verifica a assinatura do commit de origem antes de aplicar. **Fora de escopo,
registrado:** varredura de conteúdo artefato por artefato — custo alto, e o corpus inteiro a
deixa em aberto.
