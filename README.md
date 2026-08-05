# PantonicApp — framework de governança e arquitetura para aplicações desktop construídas por agentes de IA

**Versão do framework:** `2.0.0` · **Idioma do corpus:** PT-BR · **Licença de uso:** repositório público de referência.

Este arquivo é o **espelho das implementações**. Ele não existe para convencer ninguém a adotar o
framework: quem lê já o usa. Existe porque conhecer o **conceito** de um procedimento não basta para
argumentar sobre ele — é preciso conhecer a **forma que o acordo tomou** no repositório. O caso que
motivou esta reescrita está registrado: ao descrever de memória o próprio procedimento de escolha da
próxima tarefa, o dono o definiu como "uma pilha FIFO"; a implementação real é uma diretiva de
priorização persistida com precedência total sobre uma heurística de quatro níveis, na qual FIFO é o
**quarto** critério de desempate. O conceito estava certo e a prática, irreconhecível.

Por isso cada procedimento aqui responde três coisas na mesma seção: **o que é**, **por que foi
adotado** (a evidência ou o episódio que o produziu) e **onde o gerente intervém**. Cada seção declara
a sua **fonte da verdade** na primeira linha, e um guarda executável (`.claude/checks/check-readme.ps1`)
falha quando este espelho diverge do disco — um espelho sem guarda nasce fiel e envelhece mentindo,
com autoridade, porque é o único arquivo lido.

| § | Seção |
|---|---|
| 1 | O que é e o que ele governa |
| 2 | As cinco premissas de arquitetura |
| 3 | O modelo econômico |
| 4 | Modelo por fase |
| 5 | O fluxo plano → execução |
| 6 | O procedimento `próxima tarefa` |
| 7 | O diário de obras |
| 8 | Planos: o que é um plano fechado |
| 9 | Handover e uma tarefa por contexto |
| 10 | Os guardrails |
| 11 | Anatomia do kit |
| 12 | Memória e telemetria |
| 13 | Distribuição e versão |
| 14 | Decisões e a evidência medida que as motivou |
| 15 | O que a V2 mudou |

---

## 1. O que é e o que ele governa

> Fonte da verdade: `GOVERNANCA.md` §1

O PantonicApp é um framework de **governança e arquitetura** para uma família de aplicações desktop
em Python com PySide6, construídas por agentes de IA. Ele tem duas metades que se sustentam
mutuamente: uma doutrina de arquitetura, que fixa como o código se organiza em camadas e como uma
capacidade nova entra sem contaminar o núcleo; e uma doutrina de operação, que fixa como o trabalho é
planejado, decomposto, executado, verificado e registrado quando quem digita não é uma pessoa. As
duas metades viajam juntas para cada projeto consumidor como um kit versionado de agentes, skills e
scripts de verificação.

O que ele governa são três coisas, nesta ordem de importância. **Custo**: um agente cobra por turno,
reenviando o contexto inteiro a cada um, e o framework trata isso como restrição de projeto, não como
detalhe de fatura — daí o orçamento de turnos por classe de tarefa, o modelo escolhido por fase do
trabalho e a disciplina de coleta. **Rota**: quem decide arquitetura é o planejamento, no modelo caro
e com o contexto de quem decidiu; um executor que troca a rota sob pressão técnica, ou que pergunta
ao dono no meio da execução, está movendo a fase intelectual para a fase barata. **Qualidade**: as
regras de camada, de acoplamento e de teste são guardrails, isto é, coisas que **falham**, não
convenções que alguém deveria lembrar de conferir.

O que ele deliberadamente deixa de fora também é parte do desenho. Ele não governa produto —
prioridade de negócio, escopo funcional e a decisão de fazer ou não fazer continuam sendo do dono. Não
governa infraestrutura de execução dos agentes: hooks, atalhos e preferências do harness ficam fora do
kit, porque o que não viaja no pacote distribuído não chega a consumidor nenhum e, por isso, não conta
como doutrina do framework. E não tenta ser genérico: fora de desktop Python/PySide6 com MVVM, boa
parte das suas decisões perde o sentido, e isso é premissa assumida, não limitação a corrigir.

## 2. As cinco premissas de arquitetura

> Fonte da verdade: `GOVERNANCA.md` §1

Cinco premissas valem para todo projeto da família. Elas não são configuráveis — são o que define um
projeto como sendo "Pantonic", e cada uma impõe uma consequência prática ao código.

1. **Desktop-first.** As aplicações são majoritariamente desktop. *Consequência:* uma classe inteira
   de preocupações some do desenho — sessão, multi-tenant, escalabilidade horizontal, latência de
   rede como caso comum — e o esforço se concentra em responsividade da UI, trabalho fora da thread
   gráfica e persistência local.
2. **Stack fixo: Python + PySide6, arquitetura base MVVM.** Não há suporte a outro toolkit gráfico
   nem a outra linguagem. *Consequência:* a separação é verificável e verificada — geometria e estilo
   Qt só existem na shell e nas Views, o ViewModel é QtCore-only (nunca importa widgets) e o Model é
   Python puro, sem nenhum import de Qt. Não é estilo de código: é teste de conformance.
3. **Obsessão por clean architecture e clean code — como guardrail, não como aspiração.**
   *Consequência:* a regra de dependência `infracore ← contracts ← services ← plugins` é analisada
   por AST nos imports, e nunca no sentido inverso. Um projeto que "valoriza qualidade" negocia sob
   pressão de entrega; um projeto com gate vermelho não consegue entregar violando a regra.
4. **Core comum reusável.** A camada de infraestrutura é a mesma em todos os projetos da família.
   *Consequência:* a especialização é máxima no domínio e nos casos de uso, e tende a zero conforme
   se sobe para serviços de expressão, ACL e infraestrutura — quanto mais alto o nível, mais os
   projetos se parecem entre si. Nenhum projeto reinventa infraestrutura.
5. **Extensibilidade exclusivamente por plugins.** Toda evolução funcional entra como plugin atômico.
   *Consequência:* plugins se comunicam apenas por sinais e por um namespace de estado próprio
   (`plugins.<nome>.*`), nunca por acoplamento direto, e toda dependência externa — biblioteca, SO,
   filesystem, rede — pertence a exatamente um serviço, que é o único autorizado a importá-la. Não
   existe "adicionar um jeitinho no core".

A quarta premissa tem uma régua explícita, que o planejamento usa para decidir onde uma classe nova
deve nascer:

| Altura na clean architecture | Grau de especialização |
|---|---|
| Domínio (entidades, objetos de valor) | Máxima — único por projeto |
| Casos de uso / serviços de domínio | Alta — único por projeto |
| Serviços de expressão / ACL | Baixa — padrão do core |
| Infraestrutura (infracore, shell de UI) | Nenhuma — idêntica entre projetos |

Quanto mais baixo, mais especializada a classe; quanto mais alto, mais os projetos da família se
parecem entre si. Uma classe muito especializada nascendo na infraestrutura não é sinal de que a
régua precisa de exceção — é sinal de que a responsabilidade foi colocada na camada errada.

O caminho de uma capacidade nova é igualmente fixo: prova de conceito **fora** da aplicação, estresse
até o cliente validar, dissecação da POC nas camadas da arquitetura (o que é domínio, o que é caso de
uso, o que vira serviço/ACL, o que fica ad-hoc do plugin) e, só então, integração com teste funcional
do plugin mais a suíte de conformance e o piso de regressão completo. Nada é integrado antes da
validação do cliente.

## 3. O modelo econômico

> Fonte da verdade: `GOVERNANCA.md` §3

**O que é.** Todo o resto do framework deriva de uma conta:

> **custo total ≈ Σ, por turno, de (tamanho do contexto reenviado × peso do modelo)**

Três consequências operacionais saem dela.

**Número de turnos importa tanto quanto tamanho de contexto.** Um contexto de 100 mil tokens
reenviado em 40 turnos custa 40 reenvios. Governar o tamanho sem governar a contagem deixa a maior
alavanca solta. Daí três práticas obrigatórias: leituras e buscas independentes vão **na mesma
mensagem** (N leituras em 1 turno custam 1 reenvio; em N turnos, N); a suíte de testes roda no máximo
duas vezes por tarefa — depois de implementar e depois de corrigir —, nunca a cada micro-edição; e
nunca se relê um arquivo recém-editado "para conferir", porque a ferramenta de edição já falha
ruidosamente quando não aplica a mudança.

**Saída de ferramenta entra inteira no contexto.** Por isso a disciplina de coleta é normativa e não
sugestão: `git status --short` e `git log --oneline` no lugar dos completos; listagem de diretório
nunca recursiva sem excluir `build/`, `.venv/` e `node_modules/`; arquivo acima de 500 linhas acessado
por Grep mais Read com `offset`/`limit`, nunca integralmente; comando verboso não-teste redireciona a
saída para arquivo e lê só o fim.

**O contraintuitivo: delegar a um subagente é higiene de contexto, não economia de tokens.** O
subagente parte frio e paga de novo as instruções globais, a definição do próprio agente e as skills
carregadas — em *todos* os seus turnos. Ele protege o contexto do orquestrador, o que é valioso, mas
não reduz o consumo total. Tarefa pequena, abaixo de uns quinze turnos estimados, sai mais barata
executada inline do que delegada.

**Orçamento de turnos por classe de tarefa.** Cada tarefa atômica recebe um teto **antes** de ser
delegada, escolhido pela classe do trabalho:

| Classe de tarefa | Teto | Como reconhecer |
|---|---|---|
| Mecânica / pontual | ≤15 | um bloco de escrita, arquivos já conhecidos, sem contrato novo |
| Implementação padrão | ≤40 | vários blocos numa camada; contrato novo, verificação direta |
| Comportamental multi-camada | ≤60, com teto por ramo no dossiê | muda contrato ou fluxo; ciclo editar-rodar-depurar |
| Investigação / mapeamento | prescrito caso a caso, junto do método de sondagem | o entregável é descoberta, não mudança de código |
| Redação de doutrina / planejamento | ≤30 | o custo é decisão, não build |

**Por que foi adotado.** O teto único anterior, de ~40 chamadas para tudo, tratava naturezas
diferentes como se custassem o mesmo. A calibração usou a série medida do próprio repositório (26
registros em 2026-08-01) e contrariou a estimativa: para redação de doutrina, a proposta inicial de
≤25 seria estourada por **cinco de sete** tarefas medidas, enquanto ≤30 é estourado por duas. Quando
série medida e estimativa divergem, manda a série. E o teto é alarme, não controle: a série
`UXROUND3` registrou executores fechando 56/35, 61/40 e 112/50 sem parar no teto — o controle real é
**dividir a tarefa antes de delegar**, acima de oito regiões de escrita distintas.

**Onde o gerente intervém.** Em dois pontos. Primeiro, na classe: ela é escolhida e registrada no
dossiê **antes** da delegação, e escolher uma classe mais generosa *depois* do estouro é falsificar a
série — se um estouro se repete numa mesma classe, o sinal é de decomposição errada, e a resposta é
replanejar, não afrouxar o número. Segundo, na leitura da série: `docs/telemetria.tsv` é append-only e
existe justamente para que uma regressão de consumo por tarefa seja visível sem depender da memória
de ninguém.

## 4. Modelo por fase

> Fonte da verdade: `GOVERNANCA.md` §3

**O que é.** A cada fase do trabalho corresponde um modelo, e a tabela é **vinculante** — não é
preferência, não é default sobrescrevível por gosto:

| Fase | Modelo | Responsabilidade |
|---|---|---|
| Planejamento (intelectual) | O mais poderoso disponível — Opus | PRD, arquitetura, specs, decomposição em checklists de tarefas atômicas |
| Execução | Melhor custo-benefício — Sonnet | Implementar uma tarefa do checklist por vez, com TDD, em contexto limpo |
| Coleta / varredura | O mais barato — Haiku | Search, grep, leitura de codebase e documentos; devolve dossiê compacto |

Duas ressalvas fazem parte da regra. Um modelo ainda mais caro que o de planejamento **nunca** é
escolha automática: só entra sob solicitação explícita do dono, mesmo em planejamento. E subir o
`model:` de um agente de **execução** exige OK explícito e registrado — nunca herança silenciosa de
uma preferência genérica escrita em memória.

O gatilho operacional é a skill `modelo-por-fase`, que viaja no kit versionado. Ela classifica a fase
da tarefa, confere contra o modelo ativo e **para** para pedir o `/model` correto. Não corrige
sozinha, por um fato técnico medido: um agente não troca o próprio modelo — só o dono, pelo comando, ou
o harness, por hook. O hook de aviso continua fora do kit, porque é mecanismo de enforcement de uma
regra que já mora na doutrina versionada, e não uma superfície de doutrina em si.

**Por que foi adotado.** Um executor rodando no modelo de planejamento consumiu **71 turnos e ~189 mil
tokens de contexto numa única tarefa atômica** — algo em torno de 30% do limite de cinco horas, gasto
com uma tarefa só. O número não foi estimado; veio da auditoria de consumo. A regra também protege o
sentido inverso: decidir arquitetura no modelo barato é o mesmo defeito com o sinal trocado, e é o que
os guardrails `G-EXECREADY` e `G-PLANFIDELITY` fecham.

**Onde o gerente intervém.** Quando o gate dispara, ele para e pede uma ação humana: trocar o modelo
com `/model` e confirmar. Três respostas são legítimas — trocar (o caso normal), autorizar
explicitamente a exceção (que fica registrada, com motivo, no plano ou no diário), ou reclassificar a
fase se o gate errou a classificação. O que **não** é legítimo é o agente decidir sozinho e seguir:
uma exceção não registrada vira precedente silencioso e a tabela deixa de valer na prática.

## 5. O fluxo plano → execução

> Fonte da verdade: `GOVERNANCA.md` §4

**O que é.** O coração do framework. Todo procedimento mais complexo é antecedido por um
**planejamento consolidado**: um plano em formato de checklist, com tarefas numeradas `T1..Tn` em
ordem de dependência, que decompõe a iniciativa em **tarefas atômicas**. Uma tarefa atômica é definida
por uma propriedade operacional, não por tamanho: ela é executável por um agente que **não conhece o
projeto**, num contexto limpo, sem precisar fazer nenhuma busca transversal. O custo de contexto da
exploração é pago **uma vez**, no planejamento — com apoio do agente de coleta —, e não a cada
execução.

Num projeto novo, o planejamento produz **quatro artefatos**, nesta ordem, cada um consumindo o
anterior:

1. **PRD** — coleta os objetivos da aplicação e determina casos de uso, elementos de domínio,
   requisitos, estruturas de dados e a **linguagem ubíqua** com que as camadas de domínio e de casos
   de uso serão escritas.
2. **Architecture** — o modelo conceitual em MVVM mais clean architecture, **partindo do core comum**
   e especializando as camadas baixas. Fixa os limites de cada camada e mapeia **cada
   responsabilidade** a um caso de uso ou requisito do PRD; a rastreabilidade é parte do artefato,
   não um anexo dele.
3. **Spec** — as classes Python que materializam essas responsabilidades: estrutura de arquivos
   proposta, assinaturas, docstrings e as técnicas de projeto que garantem o desacoplamento
   tecnológico (inversão de dependência, strategy, unit of work).
4. **Sprint Plan** — organiza o Spec nos checklists que vão para o diário, ordenados para que os
   entregáveis sejam **rapidamente testáveis pelo usuário**: fatias verticais finas antes de camadas
   horizontais completas. É ele que define os testes funcionais que validam a efetividade do
   desenvolvimento, junto dos demais critérios de aceite.

Uma tarefa atômica bem escrita carrega, no mínimo:

- **Objetivo** — uma frase.
- **Arquivos-alvo** — com `caminho:linha` quando a âncora já existe; `caminho §seção` quando a linha
  ainda não é estável; `caminho (novo)` quando a própria tarefa cria o arquivo. `caminho:linha` é
  ponteiro de leitura, envelhece e **não** se mantém: tratá-lo como contrato custa mais do que
  entrega.
- **Contratos/classes** envolvidos.
- **Testes** — o TF novo, o TR que tranca, e as suítes a rodar.
- **Verificação** — o **comando copiado do terminal**, não a intenção de verificar.
- **Pronto quando** — critério objetivo, verificável sem interpretação.

Planejador e executor são papéis distintos, em modelos distintos, com deveres opostos e simétricos. O
planejador nunca executa e é responsável por fechar todas as decisões antes de publicar (§8). O
executor nunca replaneja: ele **não decide, não pergunta ao dono e não muda a rota**. Se a tarefa se
mostrar mal decomposta, ou se surgir um obstáculo que ameace a arquitetura aprovada, ele para, marca
`blocked` no diário com a razão e faz handover — não improvisa uma alternativa própria.

O desenvolvimento é TDD, com dois tipos de teste garantidos prioritariamente: **funcionais (TF)**,
derivados dos casos de uso e requisitos, definidos já no plano; e **de regressão (TR)**, que trancam o
comportamento contra colaterais. O conjunto de comportamentos trancados forma o **piso de regressão** —
uma lista versionada em `tests/piso_comportamental.txt`, uma linha por comportamento no formato
`<pytest nodeid> — <comportamento em uma frase>`. O piso **não é** percentual de cobertura, e
percentual não vale como piso, meta nem critério de pronto em nenhum ponto da doutrina. Provar que o
piso não desceu é por comando, não por leitura: o ratchet (`.claude/checks/ratchet_piso.py`) compara a
lista com a coleta real da suíte e falha **nomeando** o comportamento perdido.

**Por que foi adotado.** Duas evidências. A primeira é a economia: contexto acumulado é reenviado
inteiro a cada turno e mistura escopo entre tarefas não relacionadas, então a tarefa atômica em
contexto limpo é o que torna o custo previsível — o preço é que cada tarefa recomeça fria, e um plano
ruim dói imediatamente. A segunda é o piso comportamental: piso percentual premia manter teste de
código morto para não derrubar a métrica, que é exatamente o que o guardrail `G-DEADCODE` proíbe.
Escrito como comportamento, o piso **reforça** a proibição em vez de contradizê-la.

**Onde o gerente intervém.** Em três momentos. Na **aprovação do plano**, que é quando a rota é
escolhida — depois disso, mudar a arquitetura exige um decision record novo, não uma conversa no meio
da execução. No **desbloqueio**: uma tarefa `blocked` carrega a razão registrada, e cabe ao gerente
decidir se a razão caiu (caso em que o desbloqueio é mecânico e o agente executa) ou se a rota precisa
ser revista. E na **remoção de um comportamento do piso**, que é ato do dono e nunca efeito colateral
de refactor: ele registra no diário qual comportamento, por quê e em que commit, e só então a linha sai
do arquivo, no mesmo commit que remove o teste. Teste cujo significado muda de propósito é
**reescrito**, junto com a linha do piso — nunca deletado.

## 6. O procedimento `próxima tarefa`

> Fonte da verdade: `.claude/skills/proximo-passo/SKILL.md`

**O que é.** O ponto de entrada canônico do fluxo "abro um contexto novo, digo *execute o próximo
passo do backlog* e recebo um relatório". Ele **não** é uma fila FIFO. A sequência real tem cinco
passos, e FIFO aparece só no fim do segundo, como último desempate.

**Passo 1 — drenar os dois inboxes, antes de escolher qualquer coisa.** O inbox de planos
(`docs/plans/_INBOX.md`, append-only) tem suas linhas novas promovidas para o índice do diário; a fila
de candidatos a memória é apresentada ao dono, item a item, para promover ou descartar. Sem essa
drenagem, um plano registrado por outra sessão fica invisível e a fila de memória acumula até a
disciplina degradar.

**Passo 2 — ler a diretiva de priorização.** É uma linha fixa no topo de `docs/DIARIO_DE_OBRAS.md`,
logo abaixo do título. Se ela nomear uma iniciativa ou um bug, tem **precedência total** sobre tudo o
que vem a seguir: pula direto para a próxima tarefa daquela âncora, mesmo que outra iniciativa esteja
mais antiga no índice. Só quando ela está vazia entra a heurística padrão, nesta ordem:

1. Itens `blocked` cuja razão registrada **já não se aplica** — destravar vem antes de começar.
2. Itens `in progress`, com WIP de 1 iniciativa por vez — nunca se abre uma segunda enquanto a
   primeira está em andamento.
3. Tíquetes avulsos de bug.
4. Demais itens `backlog`, por ordem de entrada no índice — **FIFO, o quarto critério**.

Se houver duas ou mais iniciativas `in progress` com a diretiva vazia, o desempate **não** é por FIFO
nem por "momentum": o procedimento pergunta ao dono, porque empate de WIP é prioridade que ninguém
persistiu.

**Passo 3 — escolher uma única tarefa atômica.** Localizada por Grep pelo ID, lendo só a seção
correspondente. Para retomar uma sprint em andamento, o atalho é a linha `Próxima tarefa da sprint`, e
não a leitura sequencial da seção.

**Passo 4 — gate de delegação.** Antes de despachar o executor, sete verificações, das quais estas
mudam o resultado com mais frequência: o alvo é único, sem cláusula "investigue X" (nem introduzida
pelo próprio orquestrador ao transcrever); números de aceite — piso, contagem de suíte, call sites —
são **re-derivados por um comando barato agora**, nunca copiados do plano, porque contagens envelhecem
dentro da própria sprint; string destinada a `assert` é citação colada do output, nunca paráfrase; e o
volume é contado em regiões de escrita, com **mais de oito regiões obrigando a dividir antes de
delegar**. Antes disso ainda roda o gate `G-PLANREADY`: tarefa de plano aberto não é delegada, é
devolvida ao planejamento.

**Passo 5 — handover.** O relatório final traz a tarefa executada e o status, a iniciativa de origem,
o índice de conclusão do plano (`<done>/<total>`), a próxima tarefa sugerida **sem iniciá-la** e a
recomendação de limpar o contexto. E aplica a regra "decisão pendente é o próximo passo": se a
execução deixou algo para o dono decidir, o próximo passo sugerido é **a decisão**, apresentada com o
fato medido que a originou, o que cada opção implica, o que fica bloqueado sem resposta e uma
recomendação com motivo.

Cinco travas cercam a escolha, e cada uma existe porque o modo de falha já aconteceu: nunca mais de
uma tarefa por invocação; **nunca** tarefa de plano `superseded`, que é terminal e não é
"continuado" — se ele parece a próxima coisa a fazer, o erro está na leitura do estado, não no plano
vivo; nunca tarefa de plano travado por decisão do dono ainda não resolvida, caso em que os pontos
pendentes são apresentados e o procedimento para, sem iniciar implementação nem redescobrir o que o
plano já responde; nunca duas iniciativas com planos vivos disputando a mesma rota, caso em que se
rebaseia antes de escolher; e, se não houver item escolhível, isso é reportado explicitamente — não
se inventa trabalho nem se reabre item terminal.

Uma sexta trava é de método, com série medida por trás (cerca de 45 chamadas de busca perdidas):
busca que precisa do **texto** pede o texto, não a lista de arquivos; tarefa de sprint no diário é
um bullet dentro da seção da sprint, e não um heading próprio; o padrão de busca é **colado do texto
real**, nunca suposto, porque uma aspa ou um pipe espúrio faz o padrão casar tudo ou nada; e
deslocamento posicional dentro de um arquivo se faz com `offset`/`limit` de leitura, não com o
deslocamento da busca, que conta ocorrências e não linhas.

**Por que foi adotado.** A diretiva persistida existe porque prioridade dita numa conversa não
sobrevive à troca de contexto — o contexto seguinte não a conhece, e escolheria outra coisa com toda a
convicção. O gate de delegação existe porque a série mostrou executores estourando o teto sem parar,
e a divisão prévia é o único controle que funciona. E o escopo do que conta como decisão do dono foi
corrigido sobre um caso medido: o desbloqueio de uma fase cuja dependência já havia sido satisfeita foi
apresentado como pergunta quando a própria heurística já mandava executá-lo — escalar evento
intrínseco devolve ao dono trabalho que o plano já resolveu, e é o erro simétrico ao de decidir
arquitetura sozinho.

**Onde o gerente intervém.** Reordenar prioridade é **escrever a diretiva no diário**, não pedir numa
mensagem: a linha no topo de `docs/DIARIO_DE_OBRAS.md` é a única forma de prioridade que sobrevive à
troca de contexto, e o procedimento a respeita acima de qualquer heurística. Só conta como decisão do
dono o que for **arquitetura** ou **requisitos**; flip de status, desbloqueio de dependência satisfeita
e avanço para a fase seguinte de uma iniciativa já aprovada são consequência mecânica, e o agente
executa sem consultar.

## 7. O diário de obras

> Fonte da verdade: `.claude/skills/diario-de-obras/SKILL.md`

**O que é.** `docs/DIARIO_DE_OBRAS.md` é o kanban central e a **única fonte de verdade de status**.
Ele tem quatro partes fixas:

- **A diretiva de priorização**, primeira linha abaixo do título (§6).
- **O índice**, no topo, com **uma linha por item**: ID, título, status, âncora. É por ele que um
  agente localiza o seu trabalho sem ler seções irrelevantes, e ele é atualizado a cada mudança de
  status.
- **Uma seção por sprint ou tíquete**, em apêndice cronológico. Sprints multi-tarefa carregam, logo
  abaixo do objetivo, a linha `Próxima tarefa da sprint`, atualizada a cada handover.
- **As notas de execução** de cada tarefa: até cerca de cinco linhas mais ponteiros.

A forma no arquivo é literal, e cabe numa tela:

```markdown
# Diário de Obras — <projeto>

**Diretiva de priorização:** <vazio = heurística padrão | "Priorize <iniciativa/bug>">

## Índice
| ID | Título | Status | Âncora |
|---|---|---|---|
| S1-T3 | <título curto> | in progress | `## S1 — <sprint>` |
| TK-042 | <título curto> | backlog | `## TK-042` |

## <um heading por sprint ou tíquete, em apêndice cronológico>
```

Os IDs são `S<n>-T<m>` para tarefa de sprint e `TK-<seq>` para tíquete avulso. Os status válidos são
sete, e três deles são terminais: `backlog`, `in progress`, `in review`, `blocked` (que **exige** razão
registrada), `done` (entregue e de pé), `cancelled` (nunca feito, descartado) e `superseded` (feito ou
parcial, porém tornado obsoleto por um entendimento novo — o trabalho pode sobreviver no código, a
rota não). Os três terminais saem do backlog e não são escolhíveis.

Quando uma iniciativa gera um plano derivado, a reconciliação com o plano de origem é **imediata e
explícita**, em uma de três formas: **(A)** fato novo que muda o próximo passo mas não a rota → o
plano de origem vai a `blocked`, com a razão apontando o fato; **(B)** a premissa que o sustentava
caiu → o plano de origem inteiro vira `superseded`, com ponteiro para o substituto; **(C)** é um passo
de validação com implementação ainda pendente na mesma iniciativa → a validação é postergada, como
`blocked`, até todas as implementações fecharem. A regra de convergência é dura: uma iniciativa tem no
máximo **um** plano vivo por vez, e é sempre o mais recente cuja premissa não foi contradita.

A condensação mantém o documento navegável. Quando itens terminais dominam, ou o diário passa de ~500
linhas, as seções concluídas migram para `docs/DIARIO_HISTORICO.md` (append-only), deixando no diário
só a linha de índice com ponteiro. Uma única seção acima de ~300 linhas migra para um satélite próprio.
O gatilho tem dono declarado: é o fechamento de cada tarefa que o dispara — não existe "alguém
verifica".

**Por que foi adotado.** O índice no topo existe para que o custo de localizar trabalho seja uma linha
de leitura, e não a varredura de um documento inteiro. A trava da célula de índice tem defeito medido
por trás: handovers sucessivos apensando parágrafos à coluna "Título" fizeram uma célula crescer de
~2,5 mil para ~5 mil caracteres, e cada agente futuro passou a pagar essa leitura em toda tarefa. Por
isso a célula fica limitada a status, uma ou duas frases e um ponteiro; detalhe de execução vai para a
seção da tarefa ou para uma seção do próprio plano. A reconciliação obrigatória de planos derivados
tem a mesma origem: dois planos vivos disputando a mesma rota fazem o procedimento de escolha
"continuar" um plano já superado, às vezes refazendo perguntas já respondidas.

**Onde o gerente intervém.** O diário é onde ele lê o estado do projeto **sem abrir plano nenhum** —
índice, status, diretiva. É também onde ele escreve: a diretiva de priorização, o registro de remoção
de um comportamento do piso, e a triagem de achados no fechamento de uma sprint. Esse último é um gate:
uma sprint não flipa para `done` enquanto houver achado na seção `## Achados da execução` do plano sem
rota decidida — cada um sai como tarefa em plano derivado, como decisão do dono, ou rejeitado com uma
linha de motivo.

## 8. Planos: o que é um plano fechado

> Fonte da verdade: `GOVERNANCA.md` §7

**O que é.** Um plano só é publicável quando está **fechado**. Isso é um guardrail nomeado —
`G-PLANREADY` — e é dever do **planejador**, não do executor. Cinco condições:

1. **Nomenclatura sequencial.** `P-NNNN-<slug>.md`, com `NNNN` sendo um contador global monotônico
   (não a data), zero-padded e **nunca reusado**. O próximo id é o maior registrado no
   `docs/plans/_INBOX.md` mais um; a data de origem vira campo de cabeçalho.
2. **Tarefas `T1..Tn` sequenciais**, em ordem de dependência, cada uma com objetivo, "pronto quando"
   e o modelo da fase. Uma tarefa por contexto.
3. **Todas as decisões tomadas no fechamento — nada postergado.** Nenhuma escolha que pertença ao
   dono fica "a resolver na execução".
4. **Linear.** Sem referência para frente, sem ramo condicional não resolvido, sem "TBD". O executor
   lê de cima a baixo e sabe o que fazer sem inferir.
5. **Gate de publicação.** Um plano só é registrado no `_INBOX.md` e no diário quando não tem questão
   pendente, bloco a preencher, nem tarefa cujo conteúdo dependa de artefato que ainda não existe.

A consequência operacional da condição 5 é a parte que costuma ser esquecida: quando parte do
trabalho depende de um insumo futuro, **não se publica um plano com um vão — divide-se em dois**. O
fechado agora, e o dependente, autorado **já fechado** como a última tarefa do plano que produz o
insumo. Um plano por nascer não é backlog invisível: ele tem dono, e é uma tarefa nomeada de outro
plano.

O enforcement é distribuído por três artefatos, para que a regra não dependa de boa vontade: a skill
`diario-de-obras`, na operação de registrar plano, verifica o gate **antes** de apensar; a skill
`proximo-passo` recusa delegar tarefa de plano que viole qualquer condição; e o agente executor recusa
performar (`G-EXECREADY`). O `_INBOX.md` é, ele próprio, o registro do contador sequencial.

Revisar um plano publicado é legítimo e esperado — publicá-lo incompleto não é. Quando a premissa que
sustentava um plano cai, ele não é "continuado": vira `superseded`, com ponteiro para o substituto, e
nenhuma tarefa nova sai dele. O código já entregue permanece; a rota é que morreu. E a rota abandonada
tem os módulos deletados **no mesmo commit** — não ficam como fantasmas testados.

Planos que antecipam várias rodadas de perguntas mantêm uma tabela única de decisões (id → valor → uma
linha de motivo), referenciada pelas seções, em vez de repetir cada regra em prosa em cada seção.

**Por que foi adotado.** O gate de publicação existe porque um plano aberto é **escolhível** pelo
procedimento de próxima tarefa e **para o executor no meio**, forçando o retrabalho de revisitar a
questão no pior momento possível — quando o contexto de quem decidiu já não existe. Decisão adiada
acaba tomada pelo executor, no modelo mais barato: é a fase intelectual vazando para a fase de
execução. A numeração sequencial tem causa igualmente medida: a nomenclatura por data colidiu — houve
**dois `P-0722` e quatro `P-0729`** —, e o contador monotônico eliminou a ambiguidade. Os planos
anteriores foram mantidos com o nome antigo, sem renomeação.

**Onde o gerente intervém.** No fechamento das decisões, antes da publicação: um plano devolvido ao
planejamento por estar aberto é o comportamento correto, não um atraso. E na revisão de rota: quando a
execução esbarra num obstáculo que ameaça a arquitetura aprovada, o executor para e escala — quem
decide bifurcar é o gerente, com decision record aprovado **antes** de a alternativa ser codada. Uma
revisão de rota registrada declara o que mudou, o que **não** mudou e não deve ser revisitado, e o que
sai do escopo.

## 9. Handover e uma tarefa por contexto

> Fonte da verdade: `.claude/skills/handover/SKILL.md`

**O que é.** Toda tarefa termina com um handover, e a próxima começa em contexto limpo, invocada pelo
usuário. O fluxo tem quatro passos.

**Gate.** Se a tarefa está sendo dada como concluída, a verificação de guardrails já passou — no
mínimo os diretórios tocados mais a suíte de conformance verde. Sem gate verde, o destino é `blocked`
ou permanece `in progress`, **nunca** `done`.

**Registro no diário.** Status final, mais as notas de execução: o que foi feito, os arquivos tocados
com `caminho:linha`, o **comando de verificação colado do terminal**, os testes criados (TF/TR), os
desvios do plano e o piso de regressão antes × depois. O registro vai para a seção da tarefa ou para
uma seção do próprio plano — **nunca** para a célula do índice. O consumo entra como **ponteiro**
(`Consumo: ver docs/telemetria.tsv`), nunca como número em prosa.

**Achado fora de escopo.** Qualquer coisa encontrada durante a execução que exija ação futura — falha
de teste pré-existente, risco, recomendação — vira, **na mesma sessão**, uma entrada apensada à seção
`## Achados da execução` ao final do plano de origem, mais uma linha de índice no diário apontando para
ela. Nota em prosa não satisfaz o guardrail: um achado sem índice transfere a forense para o próximo
gate, e um achado registrado fora do plano perde o contexto e vira pilha indecidível quando o plano
acaba.

**Decisões e lições.** Mudança comportamental intencional vira decision record no documento de estado
vigente do projeto; incidente com diagnóstico não-óbvio vira entrada no documento de lições
aprendidas. Os dois são registros curtos e datados, e existem para que a segunda ocorrência do mesmo
problema custe uma leitura em vez de uma investigação inteira.

**Nota-forward de obsolescência.** Quando a execução descobre que um plano ou uma auditoria envelheceu
de um jeito que afeta as tarefas **restantes** do mesmo plano — arquivo movido, contagem mudada,
escopo invalidado —, isso é registrado junto da sugestão de próxima tarefa. O plano histórico não se
edita; a nota no diário é o canal vivo.

**Mensagem final.** Até cerca de quinze linhas, **ponteiro mais deltas**, nunca repetindo o que já foi
escrito no diário: tarefa e status, o que validar e como, iniciativa de origem, índice de conclusão do
plano, próxima tarefa sugerida sem iniciá-la, e a recomendação explícita de limpar o contexto.

Existe uma variante para o caso em que a tarefa **não** acabou e o contexto vai acabar antes dela: o
**checkpoint intermediário**. Ele dispara quando o consumo cruza **dois terços do teto da classe**
(≤15 → 10; ≤40 → 27; ≤60 → 40; ≤30 → 20), ou antes disso, se o executor concluir por qualquer motivo
que vai estourar. O entregável são **cinco linhas**: o que já está descoberto e decidido (inclusive as
rotas descartadas — descarte é achado), o que falta, os arquivos tocados, o **próximo passo exato** e o
que não precisa ser refeito. O teto do próprio checkpoint é de **duas chamadas de ferramenta** — uma
busca pela âncora e uma edição. Depois dele, a tarefa fica `in progress` com o ponto de parada
anotado: nunca `done`, nunca `blocked`, porque não há impedimento externo — acabou o orçamento.

Fecham o procedimento uma trava e três proibições. A trava vale para **qualquer** agente: depois do
handover, se o usuário pedir a próxima tarefa no mesmo contexto, o agente não inicia — responde com o
ID e o título, repete a recomendação de limpar o contexto e aguarda; a trava só cai se o usuário, já
avisado, insistir explicitamente. As proibições: não iniciar outra tarefa no mesmo contexto, mesmo que
"pequena"; não marcar `done` com conformance vermelho ou piso abaixo do registrado; e não deixar o
diário desatualizado — se o handover não atualizou o diário, o handover não aconteceu.

**Por que foi adotado.** Contexto acumulado degrada a qualidade da resposta, mistura escopo entre
tarefas não relacionadas e é reenviado inteiro a cada turno — o mesmo material é pago repetidamente,
com qualidade decrescente. O checkpoint nasceu do modo de falha oposto: sem ele, a descoberta já paga
(onde está o código, o que já foi decidido, o que já foi descartado) morre com o contexto, e o
contexto seguinte a reexecuta do zero, pagando duas vezes pelo mesmo achado. O teto de duas chamadas
existe porque um checkpoint que custa mais do que a descoberta que preserva virou relatório e perdeu a
razão de existir.

**Onde o gerente intervém.** Ele é o destinatário do handover e o dono do gatilho de limpeza: se a
recomendação de `/clear` for ignorada seguidamente, o efeito é acumular contexto e degradar tudo o que
vier depois. É também quem decide o destino de cada achado no fechamento da sprint, e quem valida o
que ficou `in review`. Se o próprio gerente emendar instruções e fechar dois entregáveis distintos na
mesma janela sem passar por handover, o agente emite o aviso por conta própria — a disciplina não
depende de o dono lembrar.

## 10. Os guardrails

> Fonte da verdade: `GOVERNANCA.md` §7

Quatorze regras mínimas obrigatórias, válidas em todo projeto da família. A coluna do meio é a parte
honesta desta seção: ela distingue o que **falha por si** do que ainda depende de alguém ler um
checklist.

| # | Regra | Como é enforceada |
|---|---|---|
| 1 | Regra de dependência inviolável: `infracore ← contracts ← services ← plugins`, nunca no inverso | **Teste executável** (conformance, análise AST de imports) |
| 2 | ACL: toda dependência externa pertence a exatamente um serviço; nenhum outro módulo a importa | **Teste executável** (conformance) |
| 3 | MVVM estrito: geometria/estilo Qt só na shell e Views; ViewModel sem widgets; Model sem Qt | **Teste executável** (conformance) |
| 4 | Egress único de filesystem: só o componente de filesystem escreve em disco | **Teste executável** (AST) |
| 5 | Namespace de estado: plugin só escreve em `plugins.<nome>.*`, salvo whitelist explícita | **Teste executável** (boundary) |
| 6 | Gate de conformance: nenhuma tarefa é `done` com conformance vermelho | **Teste executável** (bloqueante) |
| 7 | Piso de regressão nunca desce; remoção intencional exige registro de decisão | **Teste executável** (ratchet contra a lista versionada) |
| 8 | Disciplina de contexto: uma tarefa por contexto; varredura ampla só via agente de coleta; doc grande via índice | **Instrução de agente** |
| 9 | `G-DEADCODE`: todo símbolo de produção precisa de ao menos um chamador de produção alcançável; rota abandonada morre no mesmo commit | **Teste executável** (alcançabilidade por AST) + **gate de review** no handover |
| 10 | `G-PLANFIDELITY`: o executor não substitui a rota arquitetural aprovada por alternativa própria sob pressão técnica | **Gate de review** (o handover confirma que não houve bifurcação sem decision record) |
| 11 | `G-PREMISE`: premissa que embasa abandono de rota exige spike que a comprove, não asserção | **Gate de review** no fechamento da tarefa que abandona ou bifurca |
| 12 | `G-PLANREADY`: plano só é publicável fechado — id sequencial, tarefas ordenadas, decisões todas tomadas, linear, sem vão | **Gate de review** (checklist de 5 condições, verificado ao registrar o plano) |
| 13 | `G-EXECREADY`: o executor não decide, não pergunta ao dono e recusa performar plano não-pronto | **Instrução de agente** + **gate de review** |
| 14 | Allowlist de subcomandos destrutivos: reescrita de histórico, descarte de trabalho não commitado e remoção de branch/repo ficam negados | **Enforcement de permissão** (lista de negação nas configurações, falha ruidosa) |

Cinco dos quatorze são **apenas** instrução de agente ou gate de review — dependem de o agente
obedecer ao que está escrito e de alguém conferir no fechamento. O framework não esconde isso: uma
regra que não pode virar script nasce com o motivo escrito de por que não pode. O item 14 tem o modo
de falha declarado como **ruidoso**: o comando é negado e o agente reporta ao dono, nunca falha em
silêncio; ampliar a lista de negação é rotina, encurtá-la exige ato explícito do dono registrado no
diário.

A distribuição por tipo de enforcement é a leitura rápida da tabela: **sete** regras falham como
teste executável, **cinco** dependem de gate de review ou de instrução de agente, uma delas soma as
duas formas, e uma é negada pelo próprio sistema de permissões. As três formas não são
intercambiáveis — um teste falha sem ninguém presente, um gate de review falha só se alguém
executar o gate, e uma instrução de agente falha apenas se o agente obedecer. Ler a coluna do meio é
saber exatamente quanto do framework sobrevive a um dia ruim.

Um framework que só adiciona regra apodrece — o custo de ler a doutrina cresce a cada versão e nada
jamais sai. Por isso existe uma porta de saída declarada, e ela é a **única** forma legítima de remover
um guardrail desta lista: um gatilho de revisão que reavalia a doutrina periodicamente, exigindo que a
remoção seja um ato registrado, com motivo, e não erosão silenciosa.

## 11. Anatomia do kit

> Fonte da verdade: `.claude/README.md`

O kit são nove agentes, nove skills e quatro verificadores executáveis, que viajam juntos para todo
projeto consumidor. O índice abaixo é derivado do conteúdo real do diretório e verificado por script
nos dois sentidos — item listado aqui sem arquivo no disco, e arquivo no disco sem item aqui, são as
duas falhas.

**Agentes**

| Agente | Modelo | Quando dispara |
|---|---|---|
| `pantonic-planner` | Opus | Produzir os quatro artefatos iniciais ou decompor um procedimento complexo em tarefas atômicas. Não implementa. |
| `pantonic-executor` | Sonnet | Implementar **uma** tarefa atômica por contexto, com TDD e guardrails. Não replaneja escopo. |
| `pantonic-scout` | Haiku | Buscas, greps e leitura de codebase e documentos; devolve dossiê compacto para preservar o contexto dos caros. |
| `pantonic-auditor-arch` | Opus | Auditoria de clean architecture: checklist de desvios de camada com ações de recuperação. Não altera código. |
| `pantonic-auditor-cleancode` | Sonnet | Auditoria de clean code: code smells, coesão e acoplamento. Não altera código. |
| `pantonic-auditor-pyside6` | Sonnet | Auditoria do uso de Qt: threading, signals/slots, ownership, layouts, model/view, performance. |
| `pantonic-auditor-container` | Sonnet | Auditoria de empacotamento e runtime de container: Dockerfile, 12-factor, event loop, shutdown, observabilidade. |
| `pantonic-fora-da-caixa` | Opus | Varrer procedimentos que ficaram complexos por acúmulo e propor o redesenho "como se recomeçasse hoje". |
| `pantonic-benchmarker` | Haiku | Produzir, a partir de um repositório público confirmado, um relatório de benchmarking em esquema fixo de 16 dimensões. |

**Skills**

| Skill | Quando dispara |
|---|---|
| `bootstrap-pantonic` | Criar um projeto novo da família — os quatro artefatos, a estrutura de docs e o esqueleto do core. |
| `diario-de-obras` | Registrar plano novo, abrir tíquete avulso, mudar status ou condensar itens concluídos. |
| `proximo-passo` | Contexto novo pedindo "siga o backlog": drena os inboxes, aplica a diretiva, escolhe uma tarefa e delega. |
| `handover` | Fechar, bloquear ou interromper qualquer tarefa; atualiza o diário e prepara a troca de contexto. |
| `guardrails-check` | Antes de marcar qualquer tarefa como concluída: camadas, ACL, MVVM, egress, namespace de estado, conformance, piso, kit e espelho. |
| `integrar-poc` | Uma prova de conceito foi validada e precisa virar plugin, dissecada nas camadas da arquitetura. |
| `modelo-por-fase` | Início de tarefa ou troca de fase: confere o modelo ativo contra a tabela vinculante e para para pedir o correto. |
| `checar-versao-kit` | Criação de um plano novo: compara a versão local do kit com a publicada no hub — e nunca atualiza sozinha. |
| `audit-sweep` | Antes de invocar qualquer auditor: roda a fase mecânica de greps no modelo barato e grava o dossiê. |

Os verificadores executáveis vivem em `.claude/checks/` e são invocados pelo gate de fechamento de
tarefa:

- `kit_check.ps1` — valida a estrutura do kit e a paridade de versão (`-Mode validate`), regenera o
  índice derivado a partir do disco (`-Mode generate`), detecta deriva entre índice e conteúdo real
  (`-Mode check-drift`) e escreve as colunas derivadas do registro de consumidores (`-Mode consumers`).
- `dead_code.py` — alcançabilidade de símbolos de produção por AST a partir dos entry points reais;
  materializa `G-DEADCODE`.
- `ratchet_piso.py` — compara a lista versionada de comportamentos trancados com a coleta real da
  suíte e falha nomeando o comportamento perdido.
- `check-readme.ps1` — o guarda de drift deste espelho: agentes, skills, versão, contagem de
  guardrails e a fonte da verdade declarada de cada seção.

O ciclo típico, ponta a ponta: `bootstrap-pantonic` produz os quatro artefatos iniciais e o esqueleto
do core; as tarefas entram no diário; para cada tarefa, em contexto limpo, o executor implementa, o
gate de guardrails verifica e o handover fecha; o gerente limpa o contexto e invoca a próxima.
Capacidade nova entra por `integrar-poc`, depois da validação do cliente.

**Por que foi adotado.** Os auditores são invocados pelo usuário, produzem relatórios e **não alteram
código** — apontamento aceito vira tíquete no diário, passando pelo planejador. A separação evita o
padrão em que uma auditoria "corrige de passagem" e o repositório muda sem plano nem registro. A
pré-varredura obrigatória antes de qualquer auditor tem motivo econômico direto: a fase mecânica de
greps roda no modelo barato e grava um dossiê, e o modelo caro gasta contexto apenas na leitura
confirmatória.

**Onde o gerente intervém.** Ao adotar o kit num projeto, ele ajusta **somente** os "fatos estáveis"
dos arquivos de agente — os caminhos e as convenções daquele projeto. O índice `.claude/README.md` é
artefato **derivado** e não se edita à mão: regenerá-lo a partir do disco é a única forma legítima de
mudá-lo. Skills instaladas fora do repositório, de uso pessoal, **não** fazem parte do kit e não viajam
para o consumidor — regra que só existe fora do repositório não chega a consumidor nenhum e, por isso,
não conta como doutrina do framework.

## 12. Memória e telemetria

> Fonte da verdade: `GOVERNANCA.md` §4

**O que é.** Duas séries de registro persistente, com regras opostas sobre quem escreve.

**Memória.** Só vira memória o **fato durável não derivável** — algo que continua verdadeiro amanhã e
que não pode ser reobtido por um comando barato. Tudo o mais tem outra residência, decidida por um
teste de quatro perguntas aplicadas em ordem, em que a primeira resposta afirmativa decide: vale para
um projeto fora da família? → doutrina global do dono. É regra sempre-ativa do framework, que precisa
valer sem ninguém invocar nada? → `GOVERNANCA.md`. É procedimento reexecutável com gatilho declarado?
→ skill. É papel mais fatos estáveis de quem executa? → agente. Nenhuma das quatro: não é doutrina — é
estado de trabalho, e o lar é o diário de obras.

O ponto que muda a prática: **descobrir não é aprovar**. O agente **não grava memória direto**. Um
candidato vira uma linha numa fila append-only, e **só o dono promove** — a única exceção é a remoção
(ponteiro quebrado, memória obsoleta), que o agente faz na hora. A fila é apresentada ao dono no
passo 1 do procedimento de próxima tarefa, candidato a candidato.

Uma nota de residência que importa ao gerente: a governança das memórias do harness — inclusive a
fila de candidatos e a regra de que só o dono promove — mora **fora do kit**, na doutrina global do
dono, por decisão registrada. Ela passa na primeira pergunta do teste de residência (vale para
projeto fora da família) e, por isso, **não viaja** para o consumidor. O que este espelho descreve
acima é a prática vigente do hub; um projeto consumidor recebe a régua de residência e a doutrina de
telemetria, não a governança de memória em si.

Quando duas superfícies dizem coisas diferentes sobre o mesmo assunto, valem duas regras de
precedência: **específico vence geral** (dentro de um projeto da família, a doutrina versionada vence a
global; dentro de uma tarefa, o dossiê vence a skill, que vence o agente); e, no empate,
**versionado vence não-versionado**, porque um consumidor que recebe o kit **não recebe** o que está
fora do repositório. Colisão não se resolve com as duas cópias vivas: quem aplica a regra apaga a
cópia perdedora ou a reduz a ponteiro, no mesmo ato.

**Telemetria.** `docs/telemetria.tsv` é append-only e é a **fonte única** da série de consumo, com as
colunas `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s` e `fonte`. A coluna
`fonte` assume três valores e é o que torna a série auditável: `usage` (dado lido do bloco de uso da
notificação de conclusão), `contado` (execução inline, sem bloco a ler) e `nao_medido` (consumo perdido
com a sessão). Quem escreve a linha é **o orquestrador**, nos dois pontos de fechamento — a skill de
handover e o passo final do procedimento de próxima tarefa. O executor grava no diário o placeholder
literal `Consumo: (preenchido pelo orquestrador via notificação)` e **nunca** um número próprio; o
diário aponta para a série, não copia o valor.

**Por que foi adotado.** A separação entre descobrir e aprovar existe porque memória com dado fora de
escopo — status de sprint, lista volátil, regra já promovida a outro lugar — polui o recall e é paga em
toda sessão futura. Já a telemetria medida tem número: num caso registrado, o auto-relato do próprio
agente marcou **~90 mil tokens contra ~140 mil reais**, uma subestimativa de aproximadamente 35% (a
série mais ampla mostra desvios de 11% a 44%). Um agente é uma testemunha ruim do próprio consumo, e
uma série contaminada por auto-relato não sustenta a calibração dos tetos que o modelo econômico
depende. Duplicar o número em prosa no diário recriaria duas fontes que divergem à primeira edição.

**Onde o gerente intervém.** Ele é o **único** que promove memória: a fila é apresentada e ele decide
item a item. É ele quem lê a série para calibrar tetos — e a regra é que, quando a série medida
contradiz uma estimativa, manda a série. Registro qualitativo que não cabe em coluna (estouro de teto,
execução inline, ressalva sobre a medida) continua no bullet do diário, ao lado do ponteiro; o que
nunca se repete em dois lugares é o **número**.

## 13. Distribuição e versão

> Fonte da verdade: `GOVERNANCA.md` §9

**Versão vigente do framework: `2.0.0`.** O mesmo número vive em `VERSION` (raiz — o framework:
doutrina mais kit) e em `.claude/KIT_VERSION` (dentro do prefixo que a distribuição publica). Os dois
carregam **sempre** o mesmo valor: divergência entre eles é defeito, não estado válido, e é uma das
coisas que o verificador do kit checa.

**O que é.** Existe um **hub único** — este repositório — e os consumidores **materializam** o kit a
partir dele por `git subtree`, nunca por cópia manual. `.claude/kit/` é o subtree do branch de
distribuição; `sync-kit.ps1` aplica a versão publicada sobre a árvore local, respeitando os overrides
declarados em `kit-exclude.txt`. Um override é de **arquivo inteiro**, sem merge parcial: o caminho
listado fica sob controle do consumidor e o hub não o toca.

O versionamento é semântico, com significado declarado: **MAJOR** exige ação do consumidor (artefato
removido ou renomeado, doutrina invertida, contrato que muda de formato); **MINOR** adiciona artefato
ou guardrail compatível; **PATCH** corrige redação, sem mudança de comportamento. Toda tarefa que edite
o kit ou a doutrina bumpa os dois arquivos de versão **e** escreve a linha correspondente no
`CHANGELOG.md` — os três se movem juntos, nunca um sem os outros dois. A cada mudança canônica, o hub
publica uma tag `kit-v<versão>`.

A checagem de versão acontece na **criação de todo plano novo** — é o momento em que se decide trabalho
futuro, logo o momento certo de saber se a doutrina base está desatualizada. Ela usa uma única chamada
de rede, que não faz fetch nem toca a árvore de trabalho do consumidor, e tem quatro desfechos:
versões iguais → segue em silêncio, porque não vale o turno do dono confirmar o óbvio; divergência em
MINOR/PATCH → reporta local e remota e pergunta "atualizar agora ou postergar?", registrando a resposta
no próprio plano; divergência em **MAJOR** → reporta como **incompatível e para**, sem a pergunta de
atualização; sem rede → reporta "não verificado" e segue, porque falha de rede não bloqueia a tarefa
nem é tratada como se fosse "versões iguais".

O limite que atravessa tudo isso: **divergência é reportada, nunca aplicada por agente**. Nenhum agente
sincroniza o kit por conta própria em nenhuma circunstância — nem quando a divergência aparenta ser "só
um patch". Detectar e agir são dois atos distintos: um agente faz o primeiro, jamais o segundo, e não
existe threshold de severidade que justifique pular a separação.

Dois artefatos derivados completam o mecanismo. `docs/CONSUMIDORES.md` lista os projetos consumidores;
as colunas de versão instalada, último sync e modo são **escritas por script** a partir do carimbo que
cada consumidor grava a cada sync efetivo — só a coluna do nome do consumidor é mantida à mão. E o
passo de sync verifica a assinatura do commit de origem antes de aplicar: o que se distribui,
**executa**, e um artefato adulterado no hub viraria execução em todo consumidor.

**Por que foi adotado.** Cópia manual diverge no primeiro dia útil e ninguém sabe qual cópia está
certa; com hub único existe uma versão canônica e a divergência é **detectável**. O custo é real: o
consumidor precisa entender `git subtree`, manter a árvore limpa para sincronizar e aceitar que a pasta
do subtree não se edita à mão. A separação entre detectar e aplicar tem causa direta: atualizar o kit
no meio de uma tarefa muda a doutrina sob os pés do trabalho em curso. E a escolha do prefixo de
publicação para hospedar o número da versão foi deliberada — a versão viaja **dentro** do artefato que
ela versiona, em vez de ficar num arquivo solto que a distribuição não carrega.

**Onde o gerente intervém.** A atualização é **sempre** iniciada por ele: o agente reporta, ele decide
e comanda. Publicar commits e tags é ato dele, em momento próprio. Ele também é quem mantém o
`kit-exclude.txt` — e quem paga a consequência de um override: um caminho protegido **não recebe** o
que o hub adicionou ali, o que precisa ser incorporado manualmente se aquele projeto quiser a mesma
regra. Por fim, o critério de pronto de qualquer tarefa que edite o kit é dele conferir: versão que não
sobe quando o conteúdo muda deixa a checagem cega, e o guarda vira teatro.

## 14. Decisões e a evidência medida que as motivou

> Fonte da verdade: `GOVERNANCA.md` §3

Cada regra deste framework nasceu de um erro medido, não de uma preferência estética. Oito exemplos,
com o número que os produziu — a lista é ilustrativa, não exaustiva, e cada linha corresponde a um
episódio datado no histórico do repositório, não a um princípio abstrato adotado por analogia:

| Decisão | Evidência que a produziu |
|---|---|
| **Modelo por fase é vinculante** — a tabela não se inverte por preferência, e subir o modelo de um executor exige OK explícito registrado | Um executor rodando no modelo de planejamento consumiu **71 turnos e ~189 mil tokens de contexto numa única tarefa atômica** — cerca de 30% do limite de cinco horas, gasto numa tarefa só. |
| **`G-DEADCODE`: código morto testado é proibido; rota abandonada morre no mesmo commit** | Um episódio real num projeto consumidor deixou **~300 linhas de produção sem nenhum chamador**, vivas apenas porque dois arquivos de teste as exercitavam — dois módulos, de 174 e 127 linhas, de uma rota construída num plano e abandonada no seguinte. A suíte estava verde o tempo todo: foi exatamente a suíte verde que **mascarou** o problema, e o código passou por revisão humana assim mesmo. |
| **Decisão que escolhe mecanismo de plataforma exige sonda de viabilidade junto da recomendação, não depois** | Numa única iniciativa, **três premissas de plataforma caíram** por sondagem curta demais: o mecanismo escolhido para compartilhar arquivos entre repositórios (symlink de arquivo) exigia **privilégio elevado no Windows**; os projetos-filho **não eram repositórios git**, o que `git subtree` exige; e os filhos **já tinham cópia manual** dos documentos de doutrina. Cada uma custou retrabalho que uma sonda de um ou dois comandos teria evitado. |
| **Um plano que absorve fase de outro mapeia tarefa a tarefa, nunca fase a fase** | "A fase X foi absorvida pela fase Y" é afirmação numa granularidade mais grossa que o objeto afirmado. Medido: uma fase de quatro tarefas se espalhou por duas fases do plano sucessor e **uma tarefa não caiu em nenhuma das duas** — só apareceu quando um passo posterior tentou consumir o insumo e ele não existia. |
| **Telemetria vem da medição, nunca do auto-relato do agente** | Num caso registrado, o auto-relato do próprio agente marcou **~90 mil tokens contra ~140 mil reais** — subestimativa de aproximadamente 35%. |
| **Índice de agentes e skills é artefato derivado do disco, não editado à mão** | Na adoção do enforcement executável, a checagem de deriva encontrou o índice mantido manualmente listando **8 dos 9 agentes e 6 das 8 skills** existentes. Um índice que erra silenciosamente é pior que a ausência dele: ele é lido como verdade. |
| **Plano tem contador sequencial global, e não data no nome** | A nomenclatura por data colidiu de fato — **dois `P-0722` e quatro `P-0729`** —, deixando referências cruzadas ambíguas dentro dos próprios planos. O contador monotônico, nunca reusado, resolveu a ambiguidade sem renomear o que já existia. |
| **Teto de turnos graduado por classe, calibrado pela série medida** | O teto único anterior tratava naturezas diferentes como se custassem o mesmo. Ao calibrar a classe de redação de doutrina, a estimativa inicial de ≤25 turnos foi **contrariada pela série**: de sete tarefas medidas, cinco estouravam ≤25 e apenas duas estouravam ≤30. Quando série medida e estimativa divergem, manda a série. |

O padrão comum é o que separa este framework de uma lista de boas intenções: **nenhuma dessas regras
existe porque pareceu uma boa ideia.** Cada uma tem um número, uma data e um incidente atrás dela — e
quando um número novo contradiz a regra, é a regra que muda.

## 15. O que a V2 mudou

> Fonte da verdade: `CHANGELOG.md` §2.0.0

Esta seção fecha a iniciativa `PANTONIC-V2` e é **congelada como histórico**: ela descreve uma
transição, não um estado, e não é atualizada a cada versão nova.

**A origem.** Quatro estágios encadeados. O Estágio 1 avaliou **21 frameworks públicos** de agentes e
governança num esquema fixo de **16 dimensões** (D1..D16). O Estágio 2 confrontou o PantonicApp com
esse corpus: cinco dimensões saíram com veredito **MANTER**, cinco com **ADAPTAR**, cinco com
**ADOTAR**, uma com **REJEITAR**, e a comparação revelou **seis dimensões novas** (D17..D22) que o
esquema original não previa. Disso saíram 15 candidatos a mudança, ratificados um a um pelo dono em
2026-07-29: **12 `adotar`, 2 `adaptar`, 1 `adiar`, 0 `rejeitar`** — 14 ativos. Os Estágios 3 e 4
implementaram os 14 e fecharam a documentação.

### O que fica

Procedimento que já existia, foi confrontado com a prática pública e saiu confirmado — nada a mudar
por definição.

- **Identidade e escopo (D1).** Desktop-first, stack fixo, core comum, extensão só por plugin. O
  confronto não encontrou razão para afrouxar nenhuma das cinco premissas.
- **Ciclo de vida do trabalho (D3).** Plano fechado → tarefa atômica → contexto limpo → handover. O
  único delta apontado — um gate de prontidão explícito — já tinha dono, e virou `G-PLANREADY` e
  `G-EXECREADY`.
- **Papéis e modelo por fase (D4).** A separação planejador/executor/coletor, cada um no seu modelo,
  com a tabela vinculante, é prática confirmada pelo corpus.
- **Distribuição e versionamento do próprio framework (D10).** Hub único, `git subtree`, semver com
  significado declarado, atualização sempre iniciada pelo usuário. O único delta com valor virou o
  candidato de compatibilidade por MAJOR.
- **Interação com o humano (D16).** O agente para e pergunta ao dono nos pontos certos — decisão de
  arquitetura e de requisitos — em vez de operar sem supervisão.
- **TDD com TF e TR**, gate de conformance bloqueante e as regras de camada, ACL e MVVM: confirmados
  na forma em que já estavam, com o enforcement reforçado (abaixo).

### O que sai

Procedimento abandonado, e o motivo.

- **Piso de regressão como contagem ou percentual de testes.** Sai definitivamente, e percentual de
  cobertura fica **proibido** como piso, meta ou critério de pronto em qualquer ponto da doutrina.
  Motivo: piso percentual premia manter teste de código morto para não derrubar a métrica —
  exatamente o que `G-DEADCODE` proíbe.
- **Nomenclatura de plano por data (`P-<MMDD>`).** Sai porque colidiu de fato: dois `P-0722` e quatro
  `P-0729`. Os planos anteriores são grandfathered, mantendo o nome antigo.
- **Consumo auto-relatado pelo agente, em prosa, no diário.** Sai porque o auto-relato subestima
  (~90k contra ~140k reais num caso medido). O bullet do diário deixa de carregar o número.
- **Edição à mão do índice de agentes e skills.** Sai porque a deriva era mensurável: o índice listava
  8 de 9 agentes e 6 de 8 skills. O arquivo passa a ser derivado do disco.
- **Doutrina Pantonic morando na configuração global do dono.** Sai do global o que era só duplicata —
  onboarding, mapa de documentos, fatos estáveis de agente, modelo por fase, orçamento de turnos —
  porque um consumidor que recebe o kit não recebe o que está fora do repositório.
- **Publicação pública do hub (D2, veredito REJEITAR).** Não entra: importaria o bus factor 1 e a fila
  sem SLA medidos no corpus, sem nenhum benefício de doutrina.
- **Reversibilidade por snapshot paralelo do trabalho do agente (D20).** **Adiada**, não rejeitada: é
  o maior custo da lista (~40h no desenho de referência), risco alto, e colide com a própria premissa
  de custo por turno. Permanece registrada para reavaliação futura.
- **Oito propostas do corpus, descartadas com motivo escrito**: matriz formal de rastreabilidade,
  adapter multi-harness, marketplace público de artefatos, avaliação estatística por commit, meta de
  percentual de cobertura, multi-agente com message bus, auto-update no consumidor e modo sem
  aprovação. Duas delas viraram **limite** de outros candidatos: o descarte da meta percentual fixou a
  forma do piso comportamental, e o descarte do modo sem aprovação fixou a precedência de que
  enforcement vira código **antes** de qualquer conversa sobre automação sem supervisão.
- **Duas partes de candidatos adaptados ficaram de fora, explicitamente**: a varredura de conteúdo
  artefato por artefato na cadeia de distribuição (custo alto, corpus inteiro em aberto) e a análise
  automática de transcrições para alimentar memória (exigiria infraestrutura fora do escopo do hub).

### O que se modifica

Procedimento que existia e mudou de forma. O **antes → depois** de cada um.

| Procedimento | Antes | Depois |
|---|---|---|
| **Piso de regressão** | contagem/percentual de testes, conferida por leitura | lista versionada de comportamentos trancados em `tests/piso_comportamental.txt`, uma linha por comportamento, com ratchet executável que falha **nomeando** o que se perdeu |
| **Orçamento de contexto** | teto único de ~40 chamadas para qualquer tarefa | cinco classes com teto próprio (≤15, ≤40, ≤60, prescrito, ≤30), calibrado pela série medida e **registrado antes** de delegar |
| **Telemetria de consumo** | bullet `Consumo:` em prosa no diário, auto-relatado | série append-only `docs/telemetria.tsv` com oito colunas, escrita pelo orquestrador a partir do dado medido; o diário **aponta** para a série |
| **Enforcement do kit** | convenção escrita, índice mantido à mão | `kit_check.ps1` com quatro modos (validar, gerar, detectar deriva, derivar consumidores); o índice vira artefato derivado e a deriva vira falha |
| **Residência da doutrina** | implícita; regra Pantonic espalhada entre o global e o repo | tabela de quatro superfícies, duas regras de precedência e um teste de residência de quatro perguntas; o que pertencia ao kit foi **repatriado** para a doutrina versionada |
| **Checagem de versão do kit** | toda divergência tratada igual | MAJOR reportado como **incompatível**, e o procedimento **para** sem perguntar se atualiza; MINOR/PATCH mantém a pergunta ao dono |
| **Candidato a memória** | o agente gravava direto | fila append-only de candidatos; **só o dono promove**, item a item, no início do fluxo de próxima tarefa |
| **Guardrails obrigatórios** | 8 itens | **14 itens** — mais `G-DEADCODE`, `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY`, `G-EXECREADY` e a allowlist de subcomandos destrutivos, cada um com enforcement declarado |
| **Código morto** | nenhuma verificação; suíte verde bastava | check de alcançabilidade por AST (`dead_code.py`) no gate de fechamento, mais declaração dos chamadores de produção no handover |
| **Perda de contexto não planejada** | nada — a descoberta morria com a sessão | checkpoint intermediário disparado a **2/3 do teto da classe**: cinco linhas de ponteiro de estado, com teto de duas chamadas de ferramenta |
| **Dossiê de tarefa** | prosa descritiva | `caminho:linha` nos arquivos-alvo e o **comando de verificação colado do terminal**, não a intenção de verificar |
| **Publicação de plano** | plano podia ser registrado em aberto | `G-PLANREADY`: cinco condições verificadas ao registrar; trabalho que depende de insumo futuro vira **dois planos**, não um plano com vão |
| **Numeração de plano** | data (`P-<MMDD>`) | contador global monotônico (`P-NNNN`), nunca reusado, com o `_INBOX.md` como registro do contador |
| **Vida útil da doutrina** | só se acrescentava regra | porta de saída declarada: gatilho de revisão e deprecação, a única forma legítima de remover um guardrail |
| **Cadeia de distribuição** | sync aplicava sem verificar origem | commits assinados no branch de distribuição e verificação da assinatura no sync |
| **Registro de consumidores** | inexistente | `docs/CONSUMIDORES.md` com as colunas de versão instalada, último sync e modo **derivadas por script** do carimbo de cada consumidor |
| **Porta de entrada humana** | não havia; era preciso abrir vários artefatos | este `README.md` como espelho declarado, com fonte da verdade por seção e guarda executável de drift |

### Duas ressalvas sobre o que a iniciativa mediu

Nenhuma delas invalida o resultado acima; as duas mudam a força com que ele deve ser lido, e ficam
registradas para que a próxima rodada não as redescubra.

- **Documentação não é prática.** A avaliação mediu a **forma** do enforcement de cada framework
  público, não a conformidade que ele efetivamente obtém. Um projeto que declara "100% executável"
  pode estar validando trivialidades. Consequência direta: o candidato de enforcement executável foi
  recomendado porque conserta um defeito **já manifesto** neste repositório — não porque a forma
  executável seja boa por si.
- **Parte das lacunas é orçamento de coleta, não ausência de prática.** Onde uma conclusão dependia
  de uma célula vazia isolada, ela foi formulada como "o corpus não registra", e nunca como "o
  framework não tem". Nenhum dos 15 candidatos teve uma célula vazia isolada como fundamentação
  única.

**A ação que a `2.0.0` exige do consumidor.** O MAJOR não é placar de iniciativa: a superfície
consumida mudou de fato. O piso de regressão **muda de formato** — de contagem para lista versionada —,
o que exige criar `tests/piso_comportamental.txt` no lado do consumidor para o gate não falhar por
ausência de arquivo. Somam-se os seis guardrails novos que passam a valer e os artefatos novos do kit.
Um consumidor que ainda mantenha cópia manual de `.claude/` tem uma distância maior que o incremento de
versão sugere: a diferença relevante é entre a cópia antiga e o kit inteiro publicado até `2.0.0`. E se
o `kit-exclude.txt` daquele projeto protege um caminho onde o hub adicionou conteúdo novo, o sync
respeita o override e **não** propaga a novidade — incorporar é ato manual de quem mantém o override.

