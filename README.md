# PantonicApp — framework de governança e arquitetura para aplicações construídas por agentes de IA

**Versão do framework:** `0.0.0` · **Idioma do corpus:** PT-BR · **Licença de uso:** repositório público de referência.

Este arquivo é o **documento canônico do projeto**: o contrato entre o framework e quem o adota. Ele
é suficiente para decidir sobre o framework — adotar, adaptar ou recusar — sem abrir nenhum outro
arquivo do repositório.

A autoridade fica na **fonte da verdade** que cada seção declara na primeira linha: o arquivo
versionado onde a regra vive. O acordo vale na **forma que tomou no repositório**, e é para essa
forma que cada seção aponta.

Um guarda executável (`.claude/checks/check-readme.ps1`) falha quando este documento diverge do
disco. O alcance dele é **estrutural** — contagens, âncoras e fontes declaradas. O teste de sentido é
a leitura de quem adota (`G-README`, §10).

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
| 14 | Decisões estruturantes e seus trade-offs |

---

## Glossário — o vocabulário deste framework

> Fonte da verdade: `GOVERNANCA.md` §3.1 (residência e precedência da doutrina) — este glossário
> **define termos e aponta**; a regra de cada verbete mora na fonte citada nele, nunca aqui.

### Arquitetura — como o software é estruturado

- **Regra de dependência** — o único sentido em que um módulo pode importar outro:
  `infracore ← contracts ← services ← plugins`, e nunca o inverso. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §2 e `GOVERNANCA.md` §7, item 1 (§10 desta página).
- **Infracore** — a camada mais baixa: o core de runtime, definido por **dez portas** — sinais,
  estado, filesystem, log, registro de plugins, injeção, raiz de dados, lifecycle de plugin,
  superfície de entrada e execução assíncrona. Cada porta é um contrato com responsabilidade,
  operações, invariantes e modos de falha, e um projeto da família implementa as dez na linguagem e
  no toolkit que escolher. Onde a regra mora: `ARQUITETURA_PANTONICA.md` §4 e `GOVERNANCA.md` §1,
  premissa 2.
- **Core pantônico** — o conjunto do que é comum a todo projeto da família (infracore, contratos
  genéricos e os serviços de expressão), herdado por todo projeto, e a régua de quanto cada
  camada se especializa. O que se herda é o **contrato** de cada porta; a implementação de uma
  porta pertence à camada que declara a tecnologia. Onde a regra mora: `GOVERNANCA.md` §2 e
  `ARQUITETURA_PANTONICA.md` §1.
- **Contracts** — a camada onde vivem o domínio (entidades, VOs, agregados) e as **portas**
  (Protocols) pelas quais tudo o que é externo é declarado sem ser importado. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §5.
- **Serviços de expressão** — os serviços de core que são fachada fina sobre um componente do
  infracore (sinal, estado, filesystem, registro de plugins, log, injetor, execução assíncrona,
  caminhos), presentes em qualquer projeto da família. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §6, categoria 1.
- **ACL** (*anticorruption layer*) — a camada de serviços em que cada dependência externa
  pertence a exatamente um serviço, único módulo autorizado a importá-la. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §6 e `GOVERNANCA.md` §7, item 2.
- **Egress** — a saída única para o mundo: escrita em disco e operações de SO passam por um
  componente próprio. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §10 e `GOVERNANCA.md` §7, item 3.
- **Plugin** — a unidade de entrega funcional: um manifesto que declara o campo `use_case`, um caso
  de uso em módulo próprio e um teste funcional que o exercita pela superfície do caso de uso;
  comunica-se com os demais só por sinais e por um namespace de estado próprio. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §9 e §9.1, e `GOVERNANCA.md` §5.
- **Caso de uso** — um objetivo do usuário levado do início ao fim, com nome que o dono reconhece e
  efeito que ele consegue validar. É o artefato de aplicação do plugin: mora em
  `plugins/<nome>/use_case.py`, numa classe `<Nome>UseCase` com um método público de execução, e
  depende só de `contracts` — portas e domínio —, recebidas por injeção. Exatamente um por plugin.
  Onde a regra mora: `ARQUITETURA_PANTONICA.md` §1.1 e §9.1.
- **Linguagem ubíqua** — o vocabulário único do domínio, falado sem tradução por dono, planejamento,
  código e teste; sinônimo concorrente é defeito. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §1.1 e o PRD do projeto (§5 desta página).
- **Objeto de valor (VO)** — objeto de domínio sem identidade, definido inteiramente pelos seus
  atributos e imutável: mudar um campo é trocar o objeto. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §1.1.
- **Agregado** — o punhado de entidades e VOs tratado como uma unidade de consistência, com uma
  entidade eleita raiz, por onde todo acesso de fora passa. Onde a regra mora:
  `ARQUITETURA_PANTONICA.md` §1.1.

### Projeto — como o trabalho é organizado

- **Diário de obras** — `docs/DIARIO_DE_OBRAS.md`, o kanban central e a única fonte de verdade de
  status do projeto: diretiva, índice, uma seção por sprint ou tíquete e as notas de execução. Onde
  a regra mora: `.claude/skills/diario-de-obras/SKILL.md` (§7 desta página).
- **Tarefa atômica** — a unidade de execução, definida por uma propriedade: executável por um agente
  que não conhece o projeto, em contexto limpo, sem busca transversal. Onde
  a regra mora: `GOVERNANCA.md` §4.1 (§5 desta página).
- **Handover** — o procedimento fixo que encerra toda tarefa: gate verde, registro no diário,
  achados fora de escopo, decisões e a mensagem final de ponteiro mais deltas. Onde a regra mora:
  `.claude/skills/handover/SKILL.md` (§9 desta página).
- **Guardrail** — uma regra mínima obrigatória com forma de enforcement declarada (teste executável,
  gate de review, instrução de agente ou negação de permissão); o que não é verificável não é
  guardrail. Onde a regra mora: `GOVERNANCA.md` §7 (§10 desta página).
- **Piso de regressão** — a lista versionada de comportamentos trancados por teste
  (`tests/piso_comportamental.txt`), que nunca desce sem ato registrado do dono; não é percentual de
  cobertura. Onde a regra mora: `GOVERNANCA.md` §4.4 (§5 desta página).
- **Conformance** — a suíte de testes que verifica os guardrails estruturais do próprio código
  (camadas, ACL, padrão de apresentação) e cujo vermelho bloqueia qualquer `done`. Onde a
  regra mora: `GOVERNANCA.md` §7, item 5, e `ARQUITETURA_PANTONICA.md` §12.
- **Modelo por fase** — a correspondência vinculante entre fase do trabalho (planejamento, execução,
  coleta) e o modelo que a executa. Onde a regra mora: `GOVERNANCA.md` §3, com gatilho operacional
  em `.claude/skills/modelo-por-fase/SKILL.md` (§4 desta página).
- **Contexto** — a janela de trabalho de um agente, reenviada inteira a cada turno; "contexto limpo"
  é a janela iniciada do zero para um cenário novo. Um contexto sustenta um cenário coerente e acaba
  quando uma de duas condições cai: **coesão** — material de outro cenário, ou que contradiz o já
  ingerido, polui o contexto e obriga parada imediata — e **capacidade** — teto de trabalho de ~50%
  da janela, com encerramento planejado. Onde a regra mora: `GOVERNANCA.md` §4.3.
- **Orçamento de turnos** — o número de chamadas de ferramenta atribuído a uma tarefa **antes** da
  delegação, escolhido pela classe do trabalho e calibrado pela série medida. É **referência de
  dimensionamento**, nunca porteiro: cruzá-lo é alarme, não bloqueio. Onde a regra mora:
  `GOVERNANCA.md` §3 (§3 desta página).

### Metadados — como o próprio framework é distribuído

- **Kit** — o pacote versionado de agentes, skills e verificadores que viaja para todo projeto
  consumidor, em `.claude/`. Onde a regra mora: `GOVERNANCA.md` §9, com o índice derivado em
  `.claude/README.md` (§11 desta página).
- **Hub** — o repositório único e canônico do kit e da doutrina, do qual todos os consumidores
  materializam a sua cópia; é este repositório. Onde a regra mora: `GOVERNANCA.md` §10 (§13 desta
  página).
- **Consumidor** — um projeto que instala o kit a partir do hub e é registrado como tal. Onde a
  regra mora: `GOVERNANCA.md` §10, com o registro em `docs/CONSUMIDORES.md`.
- **`sync-kit`** — o script (`.claude/sync-kit.ps1`) que aplica a versão publicada do kit sobre a
  árvore local do consumidor, respeitando os overrides declarados em `kit-exclude.txt`. Onde a regra
  mora: `GOVERNANCA.md` §10 (§13 desta página).
- **Drift** — a divergência entre o que um artefato derivado afirma e o que o disco realmente
  contém; é o que os verificadores executáveis detectam. Onde a regra mora: `GOVERNANCA.md` §9, com
  os guardas em `.claude/checks/`.
- **Espelho** — uma superfície que reapresenta doutrina cuja fonte da verdade é outra (este README é
  um), em forma condensada e autossuficiente, nunca como segunda cópia plena nem como ponteiro nu.
  Onde a regra mora: `GOVERNANCA.md` §3.1, com a classificação item a item em
  `docs/RESIDENCIA_DOUTRINA.md`.
- **Fonte da verdade** — o único lugar onde uma regra é normativa; toda superfície que a repete
  declara a sua na primeira linha, e colisão não se resolve com as duas cópias vivas. Onde a regra
  mora: `GOVERNANCA.md` §3.1, com o guarda estrutural em `.claude/checks/check-readme.ps1`.
- **`KIT_VERSION`** — o arquivo `.claude/KIT_VERSION`, que carrega o número da versão **dentro** do
  prefixo publicado, sempre igual ao `VERSION` da raiz. Onde a regra mora: `GOVERNANCA.md` §10 (§13
  desta página).
- **Tag `kit-vX.Y.Z`** — a marca que o hub publica a cada mudança canônica, fixando o ponto exato da
  história que os consumidores materializam; com a versão congelada, a criação de tag nova fica
  suspensa e as já existentes permanecem como histórico. Onde a regra mora: `GOVERNANCA.md` §10 (§13
  desta página).
- **Plano `P-NNNN`** — o planejamento consolidado de uma rota de trabalho, em formato de checklist,
  identificado por contador global monotônico e publicável só quando fechado. Onde a regra mora:
  `GOVERNANCA.md` §7, item 11 (`G-PLANREADY`), e `docs/plans/_INBOX.md` como registro do contador
  (§8 desta página).
- **Iniciativa** — o corpo de trabalho ao qual um ou mais planos servem; tem no máximo **um** plano
  vivo por vez, sempre o mais recente cuja premissa não foi contradita. Onde a regra mora:
  `.claude/skills/diario-de-obras/SKILL.md`, regra de convergência (§7 desta página).
- **Estágio** — a subdivisão de uma iniciativa longa, cada uma com o seu plano `P-NNNN`; é convenção
  de organização do diário, sem regra própria além da convergência de planos.
- **Sprint** — o recorte de trabalho com entregável ao fim, materializado como um plano; nenhuma
  sprint avança sem a validação do gerente/cliente registrada no diário. Onde a regra mora:
  `GOVERNANCA.md` §4.5.
- **Tíquete `TK-<seq>`** — o item avulso do diário, fora de qualquer sprint: bug, achado com ação
  futura ou correção pontual. Onde a regra mora: `.claude/skills/diario-de-obras/SKILL.md` (§7 desta
  página).
- **Agente** — um papel declarado em `.claude/agents/*.md`, com o modelo da sua fase e os fatos
  estáveis de que precisa a frio; não carrega estado volátil. Onde a regra mora: `GOVERNANCA.md`
  §3.1 (§11 desta página).
- **Skill** — um procedimento reexecutável com gatilho declarado, em `.claude/skills/<nome>/SKILL.md`;
  é onde mora o **como se faz**. Onde a regra mora: `GOVERNANCA.md` §3.1 (§11
  desta página).
- **Decisão `DR-` / `DP-`** — um *decision record* datado, ratificado pelo dono, que registra uma
  mudança comportamental intencional e o motivo dela; bifurcar rota exige um aprovado **antes** de a
  alternativa ser codada. Onde a regra mora: `GOVERNANCA.md` §3 (papéis) e
  `.claude/skills/handover/SKILL.md` (§9 e §14 desta página).

## 1. O que é e o que ele governa

> Fonte da verdade: `GOVERNANCA.md` §1

O PantonicApp é um framework de **governança e arquitetura** para aplicações construídas por agentes
de IA, e é **agnóstico a tecnologia e a plataforma**: atua **um nível acima da implementação**, e
linguagem, framework de interface, runtime e forma de entrega ficam com o projeto — a doutrina é a
mesma para todos. O core que ele entrega é um conjunto de **portas**: cada porta declara um
contrato de runtime, e o projeto consumidor a realiza na tecnologia que escolher.

Ele atua em **dois níveis**, e é a combinação dos dois que define a família:

| Nível | O que doutrina | Onde mora |
|---|---|---|
| **Arquitetura** | como o software é estruturado — camadas, sentido das dependências, domínio, portas de runtime, extensão | `ARQUITETURA_PANTONICA.md` |
| **Projeto** | como o software é produzido — backlog, sprints, papéis, guardrails, disciplina de contexto agêntico | `GOVERNANCA.md` §3 a §9 |

Os dois níveis viajam juntos para cada projeto consumidor como um kit versionado de agentes, skills e
scripts de verificação (§11).

A camada de projeto se justifica em três eixos, nesta ordem. **Qualidade** é o motor, e ela se
garante agindo sobre o **processo** que gera o produto: guardrails executáveis, TDD, piso de
regressão, contexto limpo e validação de cada sprint pelo dono são atos sobre o processo — e um
guardrail é uma coisa que **falha** sozinha, no instante em que a regra é violada. **Rota** vem em
segundo: quem decide arquitetura é o planejamento, no modelo caro e com o contexto de quem decidiu,
porque processo bom com rota errada entrega, com esmero, o produto errado. **Custo** é o terceiro, e
é **restrição de projeto**: um agente cobra por turno, reenviando o contexto inteiro a cada um, e o
orçamento de turnos, o modelo por fase e a disciplina de coleta existem para tornar a qualidade
**sustentável** (§3). Quando os três colidem, a ordem decide:
nenhuma economia justifica abrir mão de um guardrail, e nenhuma rota se muda para caber no orçamento.

O que ele deliberadamente deixa de fora também é parte do desenho. Ele não governa produto —
prioridade de negócio, escopo funcional e a decisão de fazer ou não fazer continuam sendo do dono. E
não governa a configuração de quem opera a máquina: diretórios adicionais, preferência de modelo,
linha de status e as permissões que ele concede pertencem a quem roda o harness — a exceção declarada
é a lista de negação que materializa o guardrail de subcomandos destrutivos (§10), canônica no kit. Conteúdo do framework que o harness só lê
de um caminho não-versionado permanece canônico no kit e chega a esse caminho por projeção — o que
fica **só** num ponto de carga não chega a consumidor nenhum.

## 2. As cinco premissas de arquitetura

> Fonte da verdade: `GOVERNANCA.md` §1

Cinco premissas valem para todo projeto da família. Elas são fixas — são o que define um projeto
como sendo "Pantonic" — e **nenhuma delas nomeia stack**: linguagem, framework de interface e
plataforma são escolha do projeto.

1. **Clean architecture + DDD como base.** Fundamentos pares: a CA dá as camadas e o sentido das
   dependências; o DDD dá o conteúdo do domínio — linguagem ubíqua, entidades, objetos de valor,
   agregados e suas invariantes. *Consequência:* a regra de dependência
   `infracore ← contracts ← services ← plugins` é analisada por AST nos imports, e o domínio é
   escrito na linguagem ubíqua fixada no PRD.
2. **Infracore como doutrina das camadas de aplicação e infraestrutura.** É o passo pantônico **além**
   da CA+DDD: as camadas altas seguem o core descrito no documento de arquitetura.
   *Consequência:* o runtime é definido por dez portas — entre elas injeção, lifecycle, estado,
   sinais e egress de filesystem —, e cada uma tem responsabilidade, operações, invariantes e modos
   de falha prescritos e herdados, idênticos em cada projeto novo. As duas portas em que o mundo
   externo encosta no núcleo — a superfície de entrada e a execução assíncrona — são realizadas
   pela camada de modalidade do projeto, fora do core reusável.
3. **Um plugin = um caso de uso.** Toda evolução funcional entra como plugin, e cada plugin responde
   por exatamente um caso de uso. *Consequência:* plugins se comunicam apenas por sinais e por um
   namespace de estado próprio (`plugins.<nome>.*`), nunca por acoplamento direto, e toda dependência
   externa — biblioteca, SO, filesystem, rede — pertence a exatamente um serviço, que é o único
   autorizado a importá-la. Não existe "adicionar um jeitinho no core".
4. **Core comum reusável.** Nenhum projeto reinventa infraestrutura: o que é comum é herdado.
   *Consequência:* a especialização é máxima no domínio e nos casos de uso, e tende a zero
   conforme se sobe para serviços de expressão, ACL e infraestrutura — quanto mais alto o nível, mais
   os projetos se parecem entre si.
5. **Guardrails executáveis.** A obsessão por clean architecture e clean code é verificada por teste
   e por script, e **o que não é verificável não é guardrail** (§10).
   *Consequência:* um projeto que "valoriza qualidade" negocia sob pressão de entrega; um projeto com
   gate vermelho não consegue entregar violando a regra.

A quarta premissa tem uma régua explícita, que o planejamento usa para decidir onde uma classe nova
deve nascer:

| Altura na clean architecture | Grau de especialização |
|---|---|
| Domínio (entidades, objetos de valor, agregados) | Máxima — único por projeto |
| Casos de uso / serviços de domínio | Alta — único por projeto (um plugin = um caso de uso) |
| Serviços de expressão / ACL | Baixa — padrão do core |
| Infraestrutura (infracore, adaptador de apresentação) | Nenhuma na **porta** — o contrato é idêntico entre todos os projetos; a **implementação** só é idêntica entre projetos da mesma stack |

Quanto mais baixo, mais especializada a classe; quanto mais alto, mais os projetos da família se
parecem entre si. Uma classe muito especializada nascendo na infraestrutura sinaliza uma
responsabilidade colocada na camada errada.

O caminho de uma capacidade nova também é fixo: prova de conceito **fora** da aplicação, estresse até
o cliente validar, dissecação da POC nas camadas da arquitetura (o que é domínio, o que é caso de
uso, o que vira serviço/ACL, o que fica ad-hoc do plugin) e, só então, integração com teste funcional
do plugin mais a suíte de conformance e o piso de regressão completo. Nada é integrado antes da
validação do cliente.

## 3. O modelo econômico

> Fonte da verdade: `GOVERNANCA.md` §3

**O que é.** Custo é o **terceiro** eixo (§1): restrição de projeto. Nada aqui autoriza trocar
qualidade ou rota por economia. O que essa restrição governa deriva de uma conta:

> **custo total ≈ Σ, por turno, de (tamanho do contexto reenviado × peso do modelo)**

Três consequências operacionais saem dela.

**Número de turnos importa tanto quanto tamanho de contexto.** Um contexto de 100 mil tokens
reenviado em 40 turnos custa 40 reenvios. Governar o tamanho sem governar a contagem deixa a maior
alavanca solta. Daí três práticas obrigatórias: leituras e buscas independentes vão **na mesma
mensagem** (N leituras em 1 turno custam 1 reenvio; em N turnos, N); a suíte de testes roda no máximo
duas vezes por tarefa — depois de implementar e depois de corrigir —, nunca a cada micro-edição; e
nunca se relê um arquivo recém-editado "para conferir", porque a ferramenta de edição já falha
ruidosamente quando não aplica a mudança.

**Saída de ferramenta entra inteira no contexto.** Por isso a disciplina de coleta é normativa:
`git status --short` e `git log --oneline` no lugar dos completos; listagem de diretório
nunca recursiva sem excluir `build/`, `.venv/` e `node_modules/`; arquivo acima de 500 linhas acessado
por Grep mais Read com `offset`/`limit`, nunca integralmente; comando verboso não-teste redireciona a
saída para arquivo e lê só o fim.

**O contraintuitivo: delegar a um subagente é higiene de contexto.** O subagente parte frio e paga de
novo as instruções globais, a definição do próprio agente e as skills carregadas — em *todos* os seus
turnos. Ele protege o contexto do orquestrador, o que é valioso, e o consumo total permanece o
mesmo. Tarefa pequena, abaixo de uns quinze turnos estimados, sai mais barata
executada inline do que delegada.

**Orçamento de turnos por classe de tarefa.** Cada tarefa atômica recebe um número de referência
**antes** de ser delegada, escolhido pela classe do trabalho. Ele dimensiona e alimenta a série
medida; não recusa entrega, não roteia e não encerra tarefa nem janela:

| Classe de tarefa | Teto | Como reconhecer |
|---|---|---|
| Mecânica / pontual | ≤15 | um bloco de escrita, arquivos já conhecidos, sem contrato novo |
| Implementação padrão | ≤40 | vários blocos numa camada; contrato novo, verificação direta |
| Comportamental multi-camada | ≤60, com teto por ramo no dossiê | muda contrato ou fluxo; ciclo editar-rodar-depurar |
| Investigação / mapeamento | prescrito caso a caso, junto do método de sondagem | o entregável é descoberta |
| Redação de doutrina / planejamento | ≤30 | o custo é decisão |

A rodada de replanejamento — fechar uma decisão e reescrever, no mesmo contexto, os dossiês que ela
invalida — fica na última classe com teto **≤50**: a série dessas rodadas não cabe em ≤30, e
dividi-la entre contextos obrigaria a repagar a leitura da decisão em cada fatia.

**Por quê.** Um teto único para tudo trata naturezas diferentes como se custassem o mesmo. Os números
acima vêm de consumo medido: quando medida e estimativa divergem, manda a série. E o número é
**alarme, nunca bloqueio** — executores fecham tarefas muito acima dele sem parar, e quem executa
registra o consumo no fechamento em vez de interromper a entrega. Custo e consumo são informativos e
não têm valor em isolamento: só rendem insight analisados em conjunto, e um limite não
conscientemente delimitado que afete o fluxo é vício, não critério. O controle real é
**dividir a tarefa antes de delegar**, acima de oito regiões de escrita distintas. O registro
qualitativo por tarefa, quando existe, mora no card "Lições aprendidas na tarefa" do laudo de
revisão.

**Onde o gerente intervém.** Em dois pontos. Primeiro, na classe: ela é escolhida e registrada no
dossiê **antes** da delegação, e escolher uma classe mais generosa *depois* do estouro é falsificar a
série — se um estouro se repete numa mesma classe, o sinal é de decomposição errada, e a resposta é
replanejar. Segundo, na leitura da série: `docs/telemetria.tsv` é append-only,
para que uma regressão de consumo por tarefa seja visível sem depender da memória de ninguém.

## 4. Modelo por fase

> Fonte da verdade: `GOVERNANCA.md` §3

**O que é.** A cada fase do trabalho corresponde um modelo, e a tabela é **vinculante**:

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
da tarefa, confere contra o modelo ativo e **para** para pedir o `/model` correto. A correção fica com
o dono: um agente não troca o próprio modelo — só o dono, pelo comando, ou o harness, por hook. O
hook de aviso é canônico no kit e chega por projeção ao ponto de carga que o harness lê: ele não é
superfície de doutrina, e sim o enforcement de uma regra que já mora na doutrina versionada.

**Por quê.** A tabela protege os dois sentidos. Executar no modelo de planejamento custa numa escala
diferente: uma única tarefa atômica chega a **71 turnos e ~189 mil tokens de contexto**, perto de um
terço do limite de cinco horas. Decidir arquitetura no modelo barato é o mesmo defeito com o sinal
trocado, e é o que os guardrails `G-EXECREADY` e `G-PLANFIDELITY` fecham.

**Onde o gerente intervém.** Quando o gate dispara, ele para e pede uma ação humana: trocar o modelo
com `/model` e confirmar. Três respostas são legítimas — trocar (o caso normal), autorizar
explicitamente a exceção (que fica registrada, com motivo, no plano ou no diário), ou reclassificar a
fase se o gate errou a classificação. O que **não** é legítimo é o agente decidir sozinho e seguir:
uma exceção não registrada vira precedente silencioso e a tabela deixa de valer na prática.

## 5. O fluxo plano → execução

> Fonte da verdade: `GOVERNANCA.md` §4

**O que é.** Todo procedimento mais complexo é antecedido por um **planejamento consolidado**: um
plano em formato de checklist, com tarefas numeradas `T1..Tn` em
ordem de dependência, que decompõe a iniciativa em **tarefas atômicas**. Uma tarefa atômica é definida
por uma propriedade operacional: ela é executável por um agente que **não conhece o projeto**, num
contexto limpo, sem precisar fazer nenhuma busca transversal. O custo de contexto da exploração é
pago **uma vez**, no planejamento, com apoio do agente de coleta.

Num projeto novo, o planejamento produz **quatro artefatos**, nesta ordem, cada um consumindo o
anterior:

1. **PRD** — coleta os objetivos da aplicação e determina casos de uso, elementos de domínio,
   requisitos, estruturas de dados e a **linguagem ubíqua** com que as camadas de domínio e de casos
   de uso serão escritas.
2. **Architecture** — o modelo conceitual em clean architecture mais DDD, com o padrão de
   apresentação que o projeto escolher, **partindo do core comum**
   e especializando as camadas baixas. Fixa os limites de cada camada e mapeia **cada
   responsabilidade** a um caso de uso ou requisito do PRD; a rastreabilidade é parte do artefato.
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
  ponteiro de leitura, envelhece e fica assim: tratá-lo como contrato custa mais do que entrega.
- **Contratos/classes** envolvidos.
- **Testes** — o TF novo, o TR que tranca, e as suítes a rodar.
- **Verificação** — o **comando copiado do terminal**.
- **Pronto quando** — critério objetivo, verificável sem interpretação.

Planejador e executor são papéis distintos, em modelos distintos, com deveres opostos e simétricos. O
planejador nunca executa e é responsável por fechar todas as decisões antes de publicar (§8). O
executor nunca replaneja: ele **não decide, não pergunta ao dono e não muda a rota**. Se a tarefa se
mostrar mal decomposta, ou se surgir um obstáculo que ameace a arquitetura aprovada, ele para,
**sinaliza** `blocked` com a razão tipada e escala — não improvisa uma alternativa própria.

O desenvolvimento é TDD, com dois tipos de teste garantidos prioritariamente: **funcionais (TF)**,
derivados dos casos de uso e requisitos, definidos já no plano; e **de regressão (TR)**, que trancam o
comportamento contra colaterais. O conjunto de comportamentos trancados forma o **piso de regressão** —
uma lista versionada em `tests/piso_comportamental.txt`, uma linha por comportamento no formato
`<pytest nodeid> — <comportamento em uma frase>`. O piso **não é** percentual de cobertura, e
percentual não vale como piso, meta nem critério de pronto em nenhum ponto da doutrina. Provar que o
piso não desceu é por comando: o ratchet (`.claude/checks/ratchet_piso.py`) compara a
lista com a coleta real da suíte e falha **nomeando** o comportamento perdido.

**Por quê.** Dois trade-offs sustentam o desenho. Contexto acumulado é reenviado inteiro a cada turno
e mistura escopo entre tarefas não relacionadas, então a tarefa atômica em contexto limpo é o que
torna o custo previsível — o preço é que cada tarefa recomeça fria, e um plano ruim dói
imediatamente. E piso percentual premia manter teste de código morto para não derrubar a métrica, que
é exatamente o que o `G-DEADCODE` proíbe; escrito como comportamento, o piso **reforça** a proibição.

**Onde o gerente intervém.** Em três momentos. Na **aprovação do plano**, que é quando a rota é
escolhida — depois disso, mudar a arquitetura exige um decision record novo. No **desbloqueio**: uma
tarefa `blocked` carrega a razão registrada, e cabe ao gerente
decidir se a razão caiu (caso em que o desbloqueio é mecânico e o agente executa) ou se a rota precisa
ser revista. E na **remoção de um comportamento do piso**, que é ato do dono e nunca efeito colateral
de refactor: ele registra no diário qual comportamento, por quê e em que commit, e só então a linha sai
do arquivo, no mesmo commit que remove o teste. Teste cujo significado muda de propósito é
**reescrito**, junto com a linha do piso — nunca deletado.

## 6. O procedimento `próxima tarefa`

> Fonte da verdade: `.claude/skills/proximo-passo/SKILL.md`

**O que é.** O ponto de entrada canônico do fluxo "abro um contexto novo, digo *execute o próximo
passo do backlog* e recebo um relatório". A sequência tem cinco passos, e FIFO aparece só no fim do
segundo, como último desempate.

**Passo 1 — drenar os dois inboxes, antes de escolher qualquer coisa.** O inbox de planos
(`docs/plans/_INBOX.md`, append-only) tem suas linhas novas promovidas para o índice do diário; a fila
de candidatos a memória é apresentada ao dono, item a item, para promover ou descartar. Sem essa
drenagem, um plano registrado por outra sessão fica invisível e a fila de memória acumula até a
disciplina degradar.

**Passo 2 — ler a diretiva de priorização.** É uma linha fixa no topo de `docs/DIARIO_DE_OBRAS.md`,
logo abaixo do título. Se ela nomear uma iniciativa ou um bug, tem **precedência total** sobre a
heurística: pula direto para a próxima tarefa daquela âncora, mesmo que outra iniciativa esteja mais
antiga no índice. Só quando ela está vazia entra a heurística padrão, nesta ordem:

1. Itens `blocked` cuja razão registrada **já não se aplica** — destravar vem antes de começar.
2. Itens `in-progress`, com WIP de 1 iniciativa por vez — nunca se abre uma segunda enquanto a
   primeira está em andamento.
3. Tíquetes avulsos de bug.
4. Demais itens `ready`, por ordem de entrada no índice — **FIFO, o quarto critério**.

Se houver duas ou mais iniciativas `in-progress` com a diretiva vazia, o desempate é uma **pergunta
ao dono**, porque empate de WIP é prioridade que ninguém persistiu.

**Passo 3 — escolher uma única tarefa atômica.** Localizada por Grep pelo ID, lendo só a seção
correspondente. Para retomar uma sprint em andamento, o atalho é a linha `Próxima tarefa da sprint`.

**Passo 4 — gate de delegação.** Antes de despachar o executor, sete verificações, das quais estas
mudam o resultado com mais frequência: o alvo é único, sem cláusula "investigue X" (nem introduzida
pelo próprio orquestrador ao transcrever); números de aceite — piso, contagem de suíte, call sites —
são **re-derivados por um comando barato agora**, nunca copiados do plano, porque contagens envelhecem
dentro da própria sprint; string destinada a `assert` é citação colada do output, nunca paráfrase; e o
volume é contado em regiões de escrita, com **mais de oito regiões obrigando a dividir antes de
delegar**. O gate `G-PLANREADY` precede todas: tarefa de plano aberto é devolvida ao planejamento.

**Passo 5 — handover.** O relatório final traz a tarefa executada e o status, a iniciativa de origem,
o índice de conclusão do plano (`<done>/<total>`), a próxima tarefa sugerida **sem iniciá-la** e a
recomendação de limpar o contexto. E aplica a regra "decisão pendente é o próximo passo": se a
execução deixou algo para o dono decidir, o próximo passo sugerido é **a decisão**, apresentada com o
fato medido que a originou, o que cada opção implica, o que fica bloqueado sem resposta e uma
recomendação com motivo.

Cinco travas cercam a escolha: nunca mais de
uma tarefa por invocação; **nunca** tarefa de plano `superseded`, que é terminal — se ele parece a
próxima coisa a fazer, o erro está na leitura do estado; nunca tarefa de plano travado por decisão
do dono ainda não resolvida, caso em que os pontos
pendentes são apresentados e o procedimento para, sem iniciar implementação nem redescobrir o que o
plano já responde; nunca duas iniciativas com planos vivos disputando a mesma rota, caso em que se
rebaseia antes de escolher; e, se não houver item escolhível, isso é reportado explicitamente — não
se inventa trabalho nem se reabre item terminal.

Uma sexta trava é de método: busca que precisa do **texto** pede o texto; tarefa de sprint no diário
é um bullet dentro da seção da sprint; o padrão de busca é **colado do texto real**, nunca suposto,
porque uma aspa ou um pipe espúrio faz o padrão casar tudo ou nada; e deslocamento posicional dentro
de um arquivo se faz com `offset`/`limit` de leitura, já que o deslocamento da busca conta
ocorrências.

**Por quê.** A diretiva é persistida porque prioridade dita numa conversa não sobrevive à troca de
contexto: o contexto seguinte não a conhece, e escolheria outra coisa com toda a convicção. E escalar
evento intrínseco — pedir decisão sobre um desbloqueio que a própria heurística já manda executar —
devolve ao dono trabalho que o plano já resolveu, erro simétrico ao de decidir arquitetura sozinho.

**Onde o gerente intervém.** Reordenar prioridade é **escrever a diretiva no diário**: a linha no
topo de `docs/DIARIO_DE_OBRAS.md` é a única forma de prioridade que sobrevive à
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
| S1-T3 | <título curto> | in-progress | `## S1 — <sprint>` |
| TK-042 | <título curto> | ready | `## TK-042` |

## <um heading por sprint ou tíquete, em apêndice cronológico>
```

Os IDs são `S<n>-T<m>` para tarefa de sprint e `TK-<seq>` para tíquete avulso. Os status válidos são
sete: `triage` (registrado, ainda não avaliado), `ready` (aceito e elegível para execução), `blocked`
(que **exige** razão registrada), `in-progress` (em execução neste momento), `review` (o entregável
existe e aguarda aceite ou feedback de correção), `done` (entregável aceito) e `cancelled` (não será
executado, por qualquer motivo). `done` e `cancelled` são terminais: saem do backlog e não são
escolhíveis. `superseded` é estado exclusivo de plano e de iniciativa, e a tarefa que a realidade
tornou obsoleta é `cancelled`. A máquina de transições e o alcance de cada estado por objeto residem
na seção `## Status — residência única` de `.claude/skills/diario-de-obras/SKILL.md`.

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
O gatilho tem dono declarado: o fechamento de cada tarefa o dispara.

**Por quê.** O índice no topo existe para que localizar trabalho custe uma linha de leitura, em vez
da varredura de um documento inteiro. Daí a trava da célula: handovers sucessivos apensando parágrafos à
coluna "Título" a fazem crescer sem limite, e cada agente seguinte paga essa leitura em toda tarefa —
por isso ela fica limitada a status, uma ou duas frases e um ponteiro, com o detalhe de execução na
seção da tarefa ou do plano. A reconciliação obrigatória de planos derivados protege o mesmo custo:
dois planos vivos disputando a mesma rota fazem o procedimento "continuar" um plano já superado,
refazendo perguntas já respondidas.

**Onde o gerente intervém.** O diário é onde ele lê o estado do projeto **sem abrir plano nenhum** —
índice, status, diretiva. É também onde ele escreve: a diretiva de priorização, o registro de remoção
de um comportamento do piso, e a triagem de achados no fechamento de uma sprint. Esse último é um gate:
uma sprint não flipa para `done` enquanto houver achado na seção `## Achados da execução` do plano sem
rota decidida — cada um sai como tarefa em plano derivado, como decisão do dono, ou rejeitado com uma
linha de motivo.

## 8. Planos: o que é um plano fechado

> Fonte da verdade: `GOVERNANCA.md` §7

**O que é.** Um plano só é publicável quando está **fechado**. Isso é um guardrail nomeado —
`G-PLANREADY` — e é dever do **planejador**. Cinco condições:

1. **Nomenclatura sequencial.** `P-NNNN-<slug>.md`, com `NNNN` sendo um contador global monotônico,
   zero-padded e **nunca reusado**. O próximo id é o maior registrado no
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
trabalho depende de um insumo futuro, o plano **divide-se em dois**. O fechado agora, e o dependente,
autorado **já fechado** como a última tarefa do plano que produz o insumo. Um plano por nascer tem
dono: é uma tarefa nomeada de outro plano.

O enforcement é distribuído por três artefatos, para que a regra valha por mecanismo: a skill
`diario-de-obras`, na operação de registrar plano, verifica o gate **antes** de apensar; a skill
`proximo-passo` recusa delegar tarefa de plano que viole qualquer condição; e o agente executor recusa
performar (`G-EXECREADY`). O `_INBOX.md` é, ele próprio, o registro do contador sequencial.

Revisar um plano publicado é legítimo e esperado; publicar um plano incompleto é defeito. Quando a
premissa que sustentava um plano cai, ele vira `superseded`, com ponteiro para o substituto, e
nenhuma tarefa nova sai dele. O código já entregue permanece, e a rota morre — com os módulos da rota
abandonada deletados **no mesmo commit**.

Planos que antecipam várias rodadas de perguntas mantêm uma tabela única de decisões (id → valor → uma
linha de motivo), referenciada pelas seções.

**Por quê.** Um plano aberto é **escolhível** pelo procedimento de próxima tarefa e **para o executor
no meio**, quando o contexto de quem decidiu já não existe. Decisão adiada acaba tomada pelo executor,
no modelo mais barato: é a fase intelectual vazando para a fase de execução. E o contador monotônico
identifica de forma única — dois planos abertos no mesmo dia disputariam o mesmo nome derivado de
data. Nome anterior a essa regra permanece como está.

**Onde o gerente intervém.** No fechamento das decisões, antes da publicação: um plano devolvido ao
planejamento por estar aberto é o comportamento correto. E na revisão de rota: quando a
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
ou permanece `in-progress`, **nunca** `done`.

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
problema custe uma leitura.

**Nota-forward de obsolescência.** Quando a execução descobre que um plano ou uma auditoria envelheceu
de um jeito que afeta as tarefas **restantes** do mesmo plano — arquivo movido, contagem mudada,
escopo invalidado —, isso é registrado junto da sugestão de próxima tarefa. O plano histórico não se
edita; a nota no diário é o canal vivo.

**Mensagem final.** Até cerca de quinze linhas, **ponteiro mais deltas**, nunca repetindo o que já foi
escrito no diário: tarefa e status, o que validar e como, iniciativa de origem, índice de conclusão do
plano, próxima tarefa sugerida sem iniciá-la, e a recomendação explícita de limpar o contexto.

Existe uma variante para o caso em que a tarefa **não** acabou e o contexto vai acabar antes dela: o
**checkpoint intermediário**. Ele dispara quando o executor conclui que o contexto acaba antes da
tarefa. O entregável são **cinco linhas**: o que já está descoberto e decidido (inclusive as
rotas descartadas — descarte é achado), o que falta, os arquivos tocados, o **próximo passo exato** e o
que não precisa ser refeito. O teto do próprio checkpoint é de **duas chamadas de ferramenta** — uma
busca pela âncora e uma edição. Depois dele, a tarefa fica `in-progress` com o ponto de parada
anotado: nunca `done`, nunca `blocked`, porque não há impedimento externo — acabou o contexto.

Fecham o procedimento uma trava e três proibições. A trava vale para **qualquer** agente: depois do
handover, se o usuário pedir a próxima tarefa no mesmo contexto, o agente não inicia — responde com o
ID e o título, repete a recomendação de limpar o contexto e aguarda; a trava só cai se o usuário, já
avisado, insistir explicitamente. As proibições: não iniciar outra tarefa no mesmo contexto, mesmo que
"pequena"; não marcar `done` com conformance vermelho ou piso abaixo do registrado; e não deixar o
diário desatualizado — se o handover não atualizou o diário, o handover não aconteceu.

**Por quê.** Contexto acumulado degrada a qualidade da resposta, mistura escopo entre tarefas não
relacionadas e é reenviado inteiro a cada turno — o mesmo material é pago repetidamente, com
qualidade decrescente. O checkpoint cobre o modo de falha oposto: sem ele, a descoberta já paga morre
com o contexto e o contexto seguinte a reexecuta do zero, pagando duas vezes pelo mesmo achado. Um
checkpoint que custa mais do que a descoberta que preserva vira relatório; daí o teto de duas
chamadas.

**Onde o gerente intervém.** Ele é o destinatário do handover e o dono do gatilho de limpeza: se a
recomendação de `/clear` for ignorada seguidamente, o efeito é acumular contexto e degradar tudo o que
vier depois. É também quem decide o destino de cada achado no fechamento da sprint, e quem valida o
que ficou `review`. Se o próprio gerente emendar instruções e fechar dois entregáveis distintos na
mesma janela sem passar por handover, o agente emite o aviso por conta própria — a disciplina fica
com o agente.

## 10. Os guardrails

> Fonte da verdade: `GOVERNANCA.md` §7

Dezesseis regras mínimas obrigatórias, válidas em todo projeto da família, sem exceção.
A coluna do meio distingue o que **falha por si** do que depende de
alguém ler um checklist.

| # | Regra | Como é enforceada |
|---|---|---|
| 1 | Regra de dependência inviolável: `infracore ← contracts ← services ← plugins`, nunca no inverso | **Teste executável** (conformance, análise AST de imports) |
| 2 | ACL: toda dependência externa pertence a exatamente um serviço; nenhum outro módulo a importa | **Teste executável** (conformance) |
| 3 | Egress único de filesystem: só o componente de filesystem escreve em disco | **Teste executável** (AST) |
| 4 | Namespace de estado: plugin só escreve em `plugins.<nome>.*`, salvo whitelist explícita | **Teste executável** (boundary) |
| 5 | Gate de conformance: nenhuma tarefa é `done` com conformance vermelho | **Teste executável** (bloqueante) |
| 6 | Piso de regressão nunca desce; remoção intencional exige registro de decisão | **Teste executável** (ratchet contra a lista versionada) |
| 7 | Disciplina de contexto: um contexto sustenta um cenário coerente — material de outro cenário ou contraditório o polui e obriga parada imediata; teto de trabalho de ~50% da janela; varredura ampla só via agente de coleta; doc grande via índice | **Instrução de agente** |
| 8 | `G-DEADCODE`: todo símbolo de produção precisa de ao menos um chamador de produção alcançável; rota abandonada morre no mesmo commit | **Teste executável** (alcançabilidade por AST) + **gate de review** no fechamento da tarefa |
| 9 | `G-PLANFIDELITY`: o executor não substitui a rota arquitetural aprovada por alternativa própria sob pressão técnica | **Gate de review** (a revisão confirma que não houve bifurcação sem decision record) |
| 10 | `G-PREMISE`: premissa que embasa abandono de rota exige spike que a comprove, não asserção | **Gate de review** no fechamento da tarefa que abandona ou bifurca |
| 11 | `G-PLANREADY`: plano só é publicável fechado — id sequencial, tarefas ordenadas, decisões todas tomadas, linear, sem vão | **Gate de review** (checklist de 5 condições, verificado ao registrar o plano) |
| 12 | `G-EXECREADY`: o executor não decide, não pergunta ao dono e recusa performar plano não-pronto | **Instrução de agente** + **gate de review** |
| 13 | Allowlist de subcomandos destrutivos: reescrita de histórico, descarte de trabalho não commitado e remoção de branch/repo ficam negados | **Enforcement de permissão** (lista de negação nas configurações, falha ruidosa) |
| 14 | `G-README`: o README é documento canônico — o contrato com o cliente; nenhuma mudança de doutrina fecha sem ele refletida na mesma sprint | **Gate de review** (atividade nomeada de revisão no encerramento da sprint, com aceite do dono; `check-readme.ps1` cobre drift estrutural) |
| 15 | `G-SCOPE`: o agente se atém estritamente às responsabilidades declaradas na matriz de papéis — o que não está escrito é proibido; artefato existente que atribui ato não endossado, ou papel que a matriz sequer cita, é não-conformidade grave que se para e regulariza, e ato real que falta na matriz sobe ao dono em vez de virar responsabilidade nova no prompt | **Instrução de agente** + **gate de review** (prompt novo ou alterado e varredura dos existentes) |
| 16 | `G-SURFACE`: mudança de decisão estruturante — objetivo-chave, requisito ou caso de uso — regulariza a superfície de contato inteira no ato, não só o artefato onde a decisão foi tomada; a rodada de planejamento que fecha a decisão emite os cards de regularização no mesmo ato e a fila não avança sem eles | **Gate de planejamento** (cards emitidos no mesmo ato, plano parado sem eles) + **gate de review** |

**Sete** regras falham como teste executável, **nove** dependem de gate de review ou de instrução de
agente — uma delas soma as duas formas, e por isso aparece nas duas contagens —, e uma é negada pelo
sistema de permissões. As três formas têm forças distintas: um teste falha sem ninguém presente, um
gate de review falha só se alguém executar o gate, e uma instrução de agente falha apenas se o
agente obedecer. Uma regra que só cabe como gate ou instrução carrega escrito o motivo.

Dois itens declaram o próprio limite. O item 13 falha de modo **ruidoso**: o comando é negado e o
agente reporta; ampliar a lista de negação é rotina, encurtá-la exige ato explícito do dono
registrado no diário. No item 14, o guarda executável cobre **drift estrutural**, e o aceite de
sentido é humano e nomeado no plano da sprint.

Um framework que só adiciona regra apodrece: o custo de ler a doutrina cresce a cada rodada de
trabalho e nenhuma regra jamais sai. A **única** forma legítima de remover um guardrail desta lista é
a revisão de doutrina disparada pelo **fechamento de um plano**, que exige a remoção como ato
registrado, com motivo — nunca erosão silenciosa.

## 11. Anatomia do kit

> Fonte da verdade: `.claude/README.md`

O kit são oito agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,
que viajam juntos para todo projeto consumidor. O índice abaixo é derivado do conteúdo real do diretório e verificado por script
nos dois sentidos — item listado aqui sem arquivo no disco, e arquivo no disco sem item aqui, são as
duas falhas.

**Agentes**

| Agente | Modelo | Quando dispara |
|---|---|---|
| `pantonic-planner` | Opus | Produzir os quatro artefatos iniciais ou decompor um procedimento complexo em tarefas atômicas. Não implementa. |
| `pantonic-executor` | Sonnet | Implementar **uma** tarefa atômica por contexto, com TDD e guardrails. Não replaneja escopo. |
| `pantonic-reviewer` | Opus | Julgar a entrega de **uma** tarefa contra o dossiê dela, marcar as sete dimensões da rubrica e emitir o laudo pelo gerador. Não corrige o que aponta. |
| `pantonic-scout` | Haiku | Buscas, greps e leitura de codebase e documentos; devolve dossiê compacto para preservar o contexto dos caros. |
| `pantonic-auditor-arch` | Opus | Auditoria de clean architecture **e DDD**: checklist de desvios de camada e de modelagem de domínio, com ações de recuperação. Não altera código. |
| `pantonic-auditor-cleancode` | Sonnet | Auditoria de clean code: code smells, coesão e acoplamento. Não altera código. |
| `pantonic-fora-da-caixa` | Opus | Varrer procedimentos que ficaram complexos por acúmulo e propor o redesenho "como se recomeçasse hoje". |
| `pantonic-benchmarker` | Haiku | Produzir, a partir de um repositório público confirmado, um relatório de benchmarking em esquema fixo de 16 dimensões. |

**Skills**

| Skill | Quando dispara |
|---|---|
| `bootstrap-pantonic` | Criar um projeto novo da família — os quatro artefatos, a estrutura de docs e o esqueleto do core. |
| `diario-de-obras` | Registrar plano novo, abrir tíquete avulso, mudar status ou condensar itens concluídos. |
| `proximo-passo` | Contexto novo pedindo "siga o backlog": drena os inboxes, aplica a diretiva, escolhe uma tarefa e delega. |
| `scrum-master` | Conduzir um plano inteiro em regime de loop: despacha executor e reviewer por tarefa, roteia pelo veredito calculado e encerra a janela pelo fim do plano ou pela condição de contexto. |
| `handover` | Fechar, bloquear ou interromper qualquer tarefa; atualiza o diário e prepara a troca de contexto. |
| `guardrails-check` | Antes de marcar qualquer tarefa como concluída: camadas, ACL, padrão de apresentação, egress, namespace de estado, conformance, piso, kit e README. |
| `integrar-poc` | Uma prova de conceito foi validada e precisa virar plugin, dissecada nas camadas da arquitetura. |
| `modelo-por-fase` | Início de tarefa ou troca de fase: confere o modelo ativo contra a tabela vinculante e para para pedir o correto. |
| `checar-versao-kit` | Criação de um plano novo: compara a versão local do kit com a publicada no hub — e nunca atualiza sozinha. |
| `audit-sweep` | Antes de invocar qualquer auditor: roda a fase mecânica de greps no modelo barato e grava o dossiê. |
| `redacao-doc` | Autoria, reescrita ou revisão de documento publicado: proíbe narrativa de proveniência, citação de interlocutor e ID de processo no corpo. |

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

A declaração canônica das projeções vive em `.claude/projecoes.json`: ela nomeia o conteúdo canônico
do kit e o ponto de carga que recebe cada cópia. `.claude/tools/materializar.py` é o comando que
aplica e verifica essas projeções, e `.claude/global/` é a residência canônica do conteúdo que se
projeta no ponto de carga do usuário.

O ciclo típico, ponta a ponta: `bootstrap-pantonic` produz os quatro artefatos iniciais e o esqueleto
do core; as tarefas entram no diário; para cada tarefa, em contexto limpo, o executor implementa, o
gate de guardrails verifica e a execução devolve o sinal; a revisão julga a entrega, e quem orquestra
materializa o status, registra a tarefa e abre o contexto seguinte.
Capacidade nova entra por `integrar-poc`, depois da validação do cliente.

**Por quê.** Os auditores produzem relatórios e **não alteram código**: apontamento aceito vira
tíquete no diário, passando pelo planejador. Sem essa separação, uma auditoria "corrige de passagem"
e o repositório muda sem plano nem registro. A pré-varredura obrigatória é econômica: a fase mecânica
de greps roda no modelo barato e grava um dossiê, e o modelo caro gasta contexto só na leitura
confirmatória.

**Onde o gerente intervém.** Ao adotar o kit num projeto, ele ajusta **somente** os "fatos estáveis"
dos arquivos de agente — os caminhos e as convenções daquele projeto. O índice `.claude/README.md` é
artefato **derivado** e não se edita à mão: regenerá-lo a partir do disco é a única forma legítima de
mudá-lo. Fora do kit fica a **configuração de quem opera a máquina** — diretórios
adicionais, preferência de modelo e esforço, linha de status e as permissões que ele concede —, que a
materialização preserva intacta; a lista de negação do guardrail de subcomandos destrutivos é a
exceção declarada, canônica no kit. Skill, hook ou doc de conteúdo do framework é canônico no kit e
chega ao ponto de carga do usuário por projeção.

## 12. Memória e telemetria

> Fonte da verdade: `GOVERNANCA.md` §4

**O que é.** Duas séries de registro persistente, com regras opostas sobre quem escreve.

**Memória.** Só vira memória o **fato durável não derivável** — algo que continua verdadeiro amanhã e
que não pode ser reobtido por um comando barato. Tudo o mais tem outra residência, decidida por um
teste de uma pergunta zero e quatro perguntas seguintes, aplicadas em ordem, em que a primeira
resposta afirmativa decide. **Zero:** é ponto de carga ou configuração de quem opera a máquina? →
então não mora ali: recebe, e o que resta decidir é qual canônico se projeta nele. **Um:** vale para
um projeto fora da família? → doutrina global, canônica em `.claude/global/CLAUDE.md` e projetada no
ponto de carga `~/.claude/CLAUDE.md`.
**Dois:** é regra sempre-ativa do framework, que precisa valer sem ninguém invocar nada? →
`GOVERNANCA.md`. **Três:** é procedimento reexecutável com gatilho declarado? → skill. **Quatro:** é
papel mais fatos estáveis de quem executa? → agente. Nenhuma das quatro: é estado de trabalho, e o
lar é o diário de obras.

O ponto que muda a prática: **descobrir e aprovar são atos separados**. O agente **não grava memória
direto**. Um
candidato vira uma linha numa fila append-only, e **só o dono promove** — a única exceção é a remoção
(ponteiro quebrado, memória obsoleta), que o agente faz na hora. A fila é apresentada ao dono no
passo 1 do procedimento de próxima tarefa, candidato a candidato.

A governança das memórias do harness — inclusive a fila de candidatos e a regra de que só o dono
promove — passa na primeira pergunta do teste de residência: é **doutrina global**, canônica no kit e
projetada no ponto de carga do usuário. Um projeto consumidor recebe essa governança junto com a
régua de residência e a doutrina de telemetria.

Quando duas superfícies dizem coisas diferentes sobre o mesmo assunto, valem duas regras de
precedência: **específico vence geral** (dentro de um projeto da família, o `GOVERNANCA.md` vence a
doutrina global; dentro de uma tarefa, o dossiê vence a skill, que vence o agente); e, no empate,
**canônico vence projeção**, porque divergência entre a projeção e a origem é defeito de
materialização, cujo remédio é rematerializar. Projeção nunca se edita no destino. Colisão entre duas
cópias vivas se resolve no mesmo ato: quem aplica a regra apaga a cópia perdedora ou a reduz a
ponteiro.

**Telemetria.** `docs/telemetria.tsv` é append-only e é a **fonte única** da série de consumo, com as
colunas `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s` e `fonte`. A coluna
`fonte` assume três valores e é o que torna a série auditável: `usage` (dado lido do bloco de uso da
notificação de conclusão), `contado` (execução inline, sem bloco a ler) e `nao_medido` (consumo perdido
com a sessão). Quem escreve a linha é **o orquestrador**, nos dois pontos de fechamento — a skill de
handover e o passo final do procedimento de próxima tarefa. O valor registrado sai do dado medido da
notificação e **nunca** de um número que o próprio agente medido informe; o diário aponta para a
série.

**Por quê.** Memória com dado fora de escopo — status de sprint, lista volátil, regra já promovida a
outro lugar — polui o recall e é paga em toda sessão futura; daí a separação entre descobrir e
aprovar. E um agente é testemunha ruim do próprio consumo: o auto-relato subestima o real em **11% a
44%** na série medida, margem que inviabiliza a calibração dos tetos de que o modelo econômico
depende.
Duplicar o número em prosa no diário criaria duas fontes que divergem à primeira edição.

**Onde o gerente intervém.** Ele é o **único** que promove memória: a fila é apresentada e ele decide
item a item. É ele quem lê a série para calibrar tetos — e a regra é que, quando a série medida
contradiz uma estimativa, manda a série. Registro qualitativo que não cabe em coluna (estouro de teto,
execução inline, ressalva sobre a medida) continua no bullet do diário, ao lado do ponteiro; o que
nunca se repete em dois lugares é o **número**.

## 13. Distribuição e versão

> Fonte da verdade: `GOVERNANCA.md` §9 e §10

**Versão vigente do framework: `0.0.0`.** O número está congelado até decisão de publicar (`GOVERNANCA.md` §10 "Versionamento e atualização do kit"). O mesmo número vive em `VERSION` (raiz — o framework:
doutrina mais kit) e em `.claude/KIT_VERSION` (dentro do prefixo que a distribuição publica). Os dois
carregam **sempre** o mesmo valor: divergência entre eles é defeito, e é uma das coisas que o
verificador do kit checa.

**O que é.** Existe um **hub único** — este repositório — e os consumidores **materializam** o kit a
partir dele por `git subtree`, nunca por cópia manual. `.claude/kit/` é o subtree do branch de
distribuição; `sync-kit.ps1` aplica a versão publicada sobre a árvore local, respeitando os overrides
declarados em `kit-exclude.txt`. Um override é de **arquivo inteiro**, sem merge parcial: o caminho
listado fica sob controle do consumidor e o hub não o toca.

O versionamento é semântico, com significado declarado: **MAJOR** exige ação do consumidor (artefato
removido ou renomeado, doutrina invertida, contrato que muda de formato); **MINOR** adiciona artefato
ou guardrail compatível; **PATCH** corrige redação, sem mudança de comportamento. A régua opera a
partir do lançamento: é de lá em diante que toda tarefa que edite o kit ou a doutrina bumpa os dois
arquivos de versão **e** escreve a linha correspondente no `CHANGELOG.md` — os três se movem juntos,
nunca um sem os outros dois — e que o hub publica uma tag `kit-v<versão>` a cada mudança canônica.
Sob congelamento a exigência reduz-se a um: a mudança canônica escreve a linha no `CHANGELOG.md` sob
`[Não lançado]`, e o número fica onde está.

A checagem de versão acontece na **criação de todo plano novo** — é o momento em que se decide trabalho
futuro, logo o momento certo de saber se a doutrina base está desatualizada. Com a versão congelada ela
tem um desfecho único: reporta "congelada — nada a comparar" e encerra, sem tocar a rede. A partir do
lançamento ela usa uma única chamada de rede, que não faz fetch nem toca a árvore de trabalho do
consumidor, e ganha quatro desfechos — versões iguais seguem em silêncio; divergência em MINOR/PATCH
reporta local e remota e pergunta "atualizar agora ou postergar?", registrando a resposta no próprio
plano; divergência em **MAJOR** reporta como **incompatível e para**, sem a pergunta de atualização;
falha de rede reporta "não verificado" e segue, sem bloquear a tarefa e sem ser tratada como se fosse
"versões iguais".

O limite que atravessa tudo isso: **divergência é reportada, nunca aplicada por agente**. Nenhum agente
sincroniza o kit por conta própria em nenhuma circunstância — nem quando a divergência aparenta ser "só
um patch". Detectar e agir são dois atos distintos: um agente faz o primeiro, jamais o segundo, e não
existe threshold de severidade que justifique pular a separação.

Dois artefatos derivados completam o mecanismo. `docs/CONSUMIDORES.md` lista os projetos consumidores;
as colunas de versão instalada, último sync e modo são **escritas por script** a partir do carimbo que
cada consumidor grava a cada sync efetivo — só a coluna do nome do consumidor é mantida à mão. Com o
número congelado, todo consumidor carrega o mesmo `0.0.0` e essa coluna não distingue quem está em dia
de quem está defasado; a deriva do kit detecta-se por `kit_check.ps1 -Mode check-drift`. E o passo de
sync verifica a assinatura do commit de origem antes de aplicar: o que se distribui, **executa**, e um
artefato adulterado no hub viraria execução em todo consumidor.

**Por quê.** Cópia manual diverge e ninguém sabe qual lado está certo; com hub único existe uma versão
canônica e a divergência é **detectável**. O custo é real: o consumidor precisa entender `git subtree`,
manter a árvore limpa para sincronizar e aceitar que a pasta do subtree não se edita à mão. Detectar e
aplicar são atos separados porque atualizar o kit no meio de uma tarefa muda a doutrina sob os pés do
trabalho em curso. E o número da versão mora no prefixo publicado para viajar **dentro** do artefato
que ele versiona. O congelamento em `0.0.0` tem a mesma raiz: um número que não corresponde a
lançamento nenhum simula maturidade que o framework não tem, e `0.0.0` é o que a régua semver reserva
para desenvolvimento inicial.

**Onde o gerente intervém.** A atualização é **sempre** iniciada por ele: o agente reporta, ele decide
e comanda. Publicar commits e tags é ato dele, em momento próprio, e descongelar a versão também — o
ato fixa a primeira versão publicada e reativa o mecanismo completo de bump, tag e checagem. Ele
também é quem mantém o
`kit-exclude.txt` — e quem paga a consequência de um override: um caminho protegido **não recebe** o
que o hub adicionou ali, o que precisa ser incorporado manualmente se aquele projeto quiser a mesma
regra. Por fim, o critério de pronto de qualquer tarefa que edite o kit é dele conferir: versão que não
sobe quando o conteúdo muda deixa a checagem cega, e o guarda vira teatro. Sob congelamento o critério
é a linha no `CHANGELOG.md` sob `[Não lançado]`; a partir do lançamento, o bump acompanhando a mudança.

## 14. Decisões estruturantes e seus trade-offs

> Fonte da verdade: `GOVERNANCA.md` §3

Oito regras estruturantes e o preço que cada uma cobra de quem a segue. A lista é ilustrativa.

| Decisão | O que se paga por ela |
|---|---|
| **Modelo por fase é vinculante** — a tabela não se inverte por preferência, e subir o modelo de um executor exige OK explícito registrado | Uma troca de modelo a cada troca de fase, e atrito deliberado quando alguém quer o modelo caro na fase barata. Em troca: um executor rodando no modelo de planejamento consome até **71 turnos e ~189 mil tokens de contexto numa única tarefa atômica** — cerca de 30% de um limite de cinco horas numa tarefa só. |
| **`G-DEADCODE`: código morto testado é proibido; rota abandonada morre no mesmo commit** | Declarar, no fechamento, o chamador de produção de cada símbolo novo, e deletar código que ainda passa nos testes. Suíte verde não detecta símbolo sem chamador: o teste **é** o chamador e mascara a ausência, inclusive sob revisão humana. |
| **Decisão que escolhe mecanismo de plataforma exige sonda de viabilidade junto da recomendação** | Um ou dois comandos antes de recomendar. Sem eles, a premissa cai já dentro da execução — privilégio de sistema que o mecanismo exige, pré-condição que o repositório não satisfaz, estado que já existia e ninguém checou — e o retrabalho é da decisão inteira. |
| **Um plano que absorve fase de outro mapeia tarefa a tarefa, nunca fase a fase** | Um mapeamento item a item para escrever e conferir. "A fase X foi absorvida pela fase Y" afirma numa granularidade mais grossa que o objeto afirmado: tarefa que não caiu em nenhuma fase sucessora só aparece quando um passo posterior tenta consumir o insumo e ele não existe. |
| **Telemetria vem da medição, nunca do auto-relato do agente** | Só o orquestrador escreve a série de consumo, sempre a partir do dado medido da notificação. O auto-relato subestima o real em **11% a 44%** na série medida. |
| **Índice de agentes e skills é artefato derivado do disco, não editado à mão** | Nenhuma edição manual do índice, nem trivial: mudança de conteúdo exige regeneração. Índice mantido à mão erra em silêncio e é lido como verdade — pior que a ausência dele. |
| **Plano tem contador sequencial global no nome** | Consultar o registro do contador antes de nomear um plano. Dois planos abertos no mesmo dia disputariam um nome derivado de data e deixariam ambíguas as referências cruzadas dentro dos próprios planos. |
| **Teto de turnos graduado por classe, calibrado pela série medida** | Cada classe exige calibração própria, e a série precisa ser mantida para que a calibração continue válida. Teto único trata naturezas diferentes como se custassem o mesmo. Quando a série contradiz a estimativa, manda a série: a classe de redação de doutrina fica em **≤30** turnos porque **cinco de sete** tarefas medidas estouram ≤25. |

Quando um número novo contradiz uma dessas regras, é a regra que muda.
