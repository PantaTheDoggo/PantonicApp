# ARQUITETURA PANTONICA — Core reusável para aplicações Pantonic*

> **Audiência:** o **agente de planejamento** de um novo projeto Pantonic*. Este documento
> traduz a infraestrutura do **PantonicVideo** (`D:\workspaces\PantonicVideo`, case de sucesso e
> implementação de referência) num modelo de core reusável. Um novo projeto **replica o core
> descrito aqui** e diversifica apenas domínio e casos de uso, conforme
> [GOVERNANCA.md](GOVERNANCA.md) §2.
>
> Convenção de leitura: "**[REPLICAR]**" = copiar/portar do PantonicVideo com mudanças mínimas;
> "**[ESPECIALIZAR]**" = ponto onde cada aplicação escreve o seu próprio código.
>
> **Agnosticismo:** o núcleo descrito aqui é **agnóstico a stack e plataforma**. Onde um exemplo
> concreto aparece, ele ilustra o case de referência e nunca é exigência do framework.

---

## 1. Golden rules

Regras de ouro herdadas do PantonicVideo (ARCHITECTURE.md §1), válidas para qualquer Pantonic*:

1. **TDD ou defeito** — código sem teste que o motive é defeito.
2. **Quatro camadas unidirecionais** — `infracore ← contracts ← services ← plugins` (a seta
   significa "é importado por"); nunca no sentido inverso.
3. **Código enxuto** — nada além do necessário para a tarefa corrente.
4. **Coesão inegociável** — cada módulo com um propósito; responsabilidade acessória que corrói
   coesão é extraída (serviço simplificador, §6).
5. **Classes e funções finas.**
6. **Sem canais reversos** — o único acoplamento entre partes é **estado e sinais**; nunca
   referência direta entre plugins ou de camada alta para baixa.
7. **Executável muda a cada sprint** — todo sprint termina com algo demonstrável.
8. **Regressões trancam para sempre** — piso de testes nunca desce; teste com significado
   alterado intencionalmente é reescrito, não deletado.
9. **A camada de serviços é a ACL** — toda dependência externa entra na aplicação por
   exatamente um serviço.
10. **Sinais são só observação** — nada de polling; quem precisa reagir, assina.

Corolário — **Mirror Discipline**: todo tipo é autorado uma única vez na camada dona e
espelhado **verbatim** em `contracts/` quando precisa cruzar camadas.

### 1.1 Fundamentos — clean architecture + DDD

A base do framework são **dois fundamentos pares, não alternativas** ([GOVERNANCA.md](GOVERNANCA.md)
§1, premissa 1): a **clean architecture** dá as camadas e o sentido das dependências; o **DDD** dá o
conteúdo que essas camadas transportam. Uma aplicação que respeita a regra de dependência mas modela
o domínio como sacos de dados anêmicos **não** é Pantonic*; uma que modela bem o domínio e o deixa
importar infraestrutura, tampouco. Nada nesta seção depende de linguagem, framework ou plataforma.

**Vocabulário do domínio.** É com estes termos que o resto do documento fala de `contracts/domain` e
do código de negócio dos plugins:

| Elemento | O que é | Como se reconhece |
|---|---|---|
| **Linguagem ubíqua** | o vocabulário único do domínio, falado por dono, planejador, executor, código e teste — sem tradução entre eles | o nome que o cliente usa é o nome da classe, do campo, do sinal, do teste e do plugin; sinônimos concorrentes são defeito, não estilo |
| **Entidade** | objeto de domínio definido por **identidade própria e estável**, que sobrevive à mudança dos seus atributos | dois exemplares com todos os campos iguais ainda são coisas diferentes; a pergunta "é o mesmo?" se responde pelo id, não pelo conteúdo |
| **Objeto de valor (VO)** | objeto **sem identidade**, definido inteiramente pelos seus atributos; imutável e substituível | "é o mesmo?" se responde comparando os campos; mudar um campo é **trocar** o objeto, não editá-lo |
| **Agregado** | um punhado de entidades e VOs tratado como **uma unidade de consistência**, com uma entidade eleita **raiz** | o mundo de fora referencia **só a raiz**; nada de fora guarda referência a um membro interno |
| **Invariante** | a regra que precisa ser verdadeira **em toda transição** do agregado | se existe um instante observável em que ela é falsa, o agregado está mal desenhado — não é bug de chamador |
| **Serviço de domínio** | comportamento de domínio que **não pertence a nenhuma entidade sozinha** (envolve duas ou mais, ou uma política) | puro: decide sobre tipos de domínio, sem I/O, relógio, rede ou disco |
| **Caso de uso** | um objetivo do usuário levado do início ao fim: orquestra domínio e serviços para produzir um resultado observável | tem um nome que o dono reconhece e um efeito que ele consegue validar na tela ou na saída |
| **Contexto delimitado** | a fronteira dentro da qual um termo da linguagem ubíqua tem **um** significado | o mesmo nome com dois sentidos são dois contextos: cada um com seu modelo, ligados por tradução explícita — nunca um modelo "universal" costurando os dois |

**Pureza da camada de domínio.** O domínio não conhece o mundo: nada de I/O, rede, disco, relógio,
processo, log ou toolkit de interface dentro dele. Quem quiser tempo, arquivo ou serviço externo
recebe isso **de fora**, por uma porta (Protocol) declarada em `contracts/` e implementada na camada
de serviços (§6, a ACL). Regra prática: o domínio precisa ser testável sem instalar nada além da
linguagem e das suas dependências de modelagem de dados.

**Onde cada coisa mora, e como classificar uma classe nova.** A ordem abaixo é a ordem das
perguntas — a primeira que responder "sim" decide:

1. Tem identidade própria que sobrevive à mudança dos atributos? → **entidade**, em
   `contracts/domain`.
2. É definida só pelos atributos, imutável? → **objeto de valor**, em `contracts/domain`.
3. Impõe uma invariante sobre um conjunto de entidades/VOs que mudam juntos? → **agregado**; a raiz
   é a entidade pela qual todo acesso passa, e a invariante é validada na própria construção do
   tipo, em `contracts/domain`.
4. É comportamento puro de domínio que não cabe numa entidade só? → **serviço de domínio**, no
   código de negócio do plugin (ou promovido a serviço com porta, se dois plugins precisarem dele).
5. Encapsula uma dependência **externa** (biblioteca, processo, rede, disco, relógio)? → **serviço**
   da camada `services/`, atrás de um Protocol em `contracts/` — é a ACL, e é a **única** porta de
   entrada dessa dependência (golden rule 9).
6. Leva um objetivo do usuário do início ao fim? → **caso de uso**, e portanto **um plugin** (§9).

Se nenhuma responder "sim", a classe provavelmente não tem lugar: ou é infraestrutura genérica
(infracore, §4) ou é código que ainda não tem motivo — golden rule 3.

**O passo pantônico: infracore e plugins estendem CA+DDD.** A CA clássica descreve quatro anéis e
deixa as camadas de aplicação e infraestrutura ao improviso de cada projeto; o DDD descreve o
conteúdo do domínio e não diz nada sobre como o software é montado. O framework fecha os dois vãos
com duas peças normativas:

- **Infracore doutrina as camadas de aplicação e infraestrutura** (§4): bootstrap, injeção de
  dependências, lifecycle, estado, sinais, egress de filesystem e execução assíncrona não são
  decisões de projeto — são um core herdado. É o que impede que cada aplicação reinvente a metade
  não-domínio da arquitetura, que é justamente onde a CA cala.
- **Cada plugin responde por exatamente um caso de uso** (§9;
  [GOVERNANCA.md](GOVERNANCA.md) §1 premissa 3 e §5). A camada de casos de uso do DDD/CA deixa de
  ser uma pasta e passa a ser uma **unidade de entrega verificável**: um caso de uso = um plugin =
  um manifest = um TF que o valida. Plugin sem caso de uso nomeável é decomposição errada; caso de
  uso espalhado por dois plugins é acoplamento disfarçado, e a comunicação entre plugins continua
  sendo só estado e sinais (golden rule 6).

**Grau de aderência da implementação atual: medido.** Esta seção declara a **doutrina**; o grau em
que a implementação de referência (`PantonicVideo`) de fato a estende é registrado nos relatórios
de auditoria de arquitetura em `docs/audits/` daquele repositório, não inferido. O domínio
(`contracts/domain/`) estende DDD plenamente — objetos de valor imutáveis, invariante no
construtor, comportamento na raiz do agregado. O infracore estende CA como *frameworks & drivers*
e, por desenho, **não** estende DDD — allowlist fechada de data classes é conformidade, não
omissão. Os plugins estendem DDD na escrita, nos métodos do agregado, e não na leitura, que ainda
projeta o agregado em estruturas primitivas. A camada de casos de uso não tinha artefato próprio
que a medição pudesse contar; a residência que fecha esse vão é a §9.1.

## 2. Modelo de camadas

```
infracore  ←  contracts  ←  services  ←  plugins
   (1)           (2)           (3)         (4)
```

| Camada | Conteúdo | Pode importar |
|---|---|---|
| **infracore** [REPLICAR] | As dez portas de runtime do core (§4) e as primitivas que as realizam, inclusive a da superfície de entrada da aplicação (`ui_shell`) | stdlib, pydantic, platformdirs + allowlist de data-classes de contracts; mais o toolkit da camada de apresentação declarado pelo projeto |
| **contracts** [REPLICAR estrutura; ESPECIALIZAR domínio] | Protocols (portas), Pydantic BaseModels, Enums, entidades de domínio — **zero código de runtime** | pydantic, typing, uuid |
| **services** [REPLICAR expressão; ESPECIALIZAR domínio] | Implementações dos Protocols; ACL das dependências externas | contracts, infracore, a lib externa que encapsula |
| **plugins** [ESPECIALIZAR] | Funcionalidades de negócio; recebem serviços via injetor | contracts, stdlib restrito (allowlist definida por app; default do case: pathlib, typing) + o toolkit da camada de apresentação declarado pelo projeto |

Relação com os elementos de DDD (§1.1): **entidades, objetos de valor e agregados** vivem em
`contracts/domain` — dados e invariantes, zero runtime; **serviços de domínio** (puros) vivem no
código de negócio do plugin, ou viram serviço com porta quando dois plugins precisam deles;
**serviços de aplicação/ACL** vivem em `services/`, sempre atrás de um Protocol de `contracts/`; e
**cada caso de uso** é um plugin (§9). A regra de dependência é o que mantém o domínio puro: como
`contracts/` não importa `services/` nem `plugins/`, o domínio não tem como alcançar o mundo
externo — só ser alcançado por ele.

## 3. Estrutura de pastas canônica

```
<app>/
├── infracore/
│   ├── bootstrap_components/     # signal, app_state, filesystem, plugin_registry, logging
│   ├── injector_component/
│   ├── lifecycle/                # LifecycleHarness, excepthook, ponte de logs do toolkit
│   ├── manifest/                 # tipos autoritativos de manifest
│   ├── ui_shell/                 # superfície de entrada da aplicação + tokens de apresentação
│   └── app.py                    # bootstrap_application()
├── contracts/                    # pacote instalável próprio (versão SemVer independente)
│   └── src/contracts/
│       ├── domain/               # entidades e VOs [ESPECIALIZAR]
│       └── *.py                  # um Protocol por serviço + manifest + exceptions
├── services/<nome>/service.py    # descoberta por pasta; um Protocol por serviço
├── plugins/<nome>/               # manifest.json + plugin.py + use_case.py + adhoc/
│                                 # (+ adaptador de apresentação, se o projeto tiver um)
├── tests/                        # infracore | contracts | services | plugins | integration |
│                                 # functional (TF-*) | regression (TR-*) | conformance | boundary
└── tools/                        # harness de integração de POC etc.
```

## 4. Infracore — as dez portas de runtime do core [REPLICAR]

O core do runtime é definido por dez portas. Cada uma é um **contrato**: um projeto da família
implementa as dez na linguagem e no toolkit que escolher, e um plugin escrito contra a porta
funciona sobre qualquer implementação que honre o contrato. As primitivas que as realizam sobem na
ordem fixa de boot declarada na porta de injeção, e falha de construtor é **abort fatal** do boot;
cada uma carrega versão própria, para que um consumidor declare a versão mínima de que depende.

Duas das dez — a **superfície de entrada** e a **execução assíncrona** — são as portas em que o
mundo externo encosta no núcleo. O core as declara e nunca conhece a tecnologia que as realiza:
quem as implementa é a camada de modalidade do projeto, fora do core reusável.

O componente citado em cada porta como **implementação de referência** pertence ao case
`PantonicVideo` e vale como exemplo, nunca como requisito.

**Porta de sinais.**
- *Responsabilidade:* propagar mudança de valor a interessados desacoplados, sem que o produtor
  conheça o consumidor.
- *Operações:* criar um sinal com valor inicial; ler o valor corrente; publicar um valor novo;
  assinar, recebendo uma inscrição cancelável; cancelar a inscrição.
- *Invariantes:* o sinal cacheia o último valor, e quem assina depois de uma publicação lê o valor
  corrente sem esperar a próxima; publicar valor igual ao corrente não notifica; cancelar é
  idempotente e libera a referência ao assinante; a notificação corre na thread que publicou, então
  trabalho longo em assinante bloqueia o publicador.
- *Modos de falha:* construtor falho no boot é abort fatal (§11); publicação para sinal sem
  assinante é operação válida e silenciosa; inscrição já cancelada nunca é notificada.
- *Implementação de referência:* `SignalComponent` (`Signal[T]` + `Subscription`).

**Porta de estado.**
- *Responsabilidade:* guardar o estado observável da aplicação em pares chave-valor e mantê-lo
  entre execuções.
- *Operações:* ler uma chave, com valor default; escrever uma chave; observar uma chave, recebendo
  um sinal; remover uma chave; enumerar as chaves de um namespace.
- *Invariantes:* a chave é namespaced, e um plugin escreve exclusivamente em `plugins.<nome>.*`
  (golden rule 5); a leitura serve de um espelho em memória e a escrita é write-through; a
  persistência passa pela porta de filesystem, nunca por acesso direto a disco (G6); escrever uma
  chave observada publica pela porta de sinais; todo valor é serializável.
- *Modos de falha:* escrita fora do namespace do chamador é rejeitada com exceção dedicada
  (`NamespaceViolationError`), sem alterar o estado; falha ao persistir propaga como falha da porta
  de filesystem; construtor falho no boot é abort fatal (§11).
- *Implementação de referência:* `AppStateComponent` (KV em memória com write-through JSON).

**Porta de filesystem.**
- *Responsabilidade:* ser o **único ponto de escrita em disco** do processo (G6).
- *Operações:* ler um arquivo; escrever um arquivo; verificar existência; criar diretório; remover;
  observar um caminho, notificando o interessado quando ele muda; tomar lock sobre um caminho.
- *Invariantes:* nenhum outro módulo — infracore, serviço ou plugin — alcança a API de arquivos do
  hospedeiro; a escrita é atômica do ponto de vista do leitor, que nunca observa arquivo pela
  metade; operações concorrentes sobre o mesmo caminho são serializadas por lock de caminho; todo
  caminho é resolvido a partir de uma raiz entregue pela porta de raiz de dados.
- *Modos de falha:* erro de I/O propaga ao chamador com o caminho na mensagem, e a porta nunca
  silencia falha de escrita; construtor falho no boot é abort fatal (§11).
- *Implementação de referência:* `FilesystemComponent`.

**Porta de log.**
- *Responsabilidade:* registrar eventos de diagnóstico com atribuição de origem e expor ao operador
  os que exigem atenção.
- *Operações:* obter um canal nomeado por origem; registrar em níveis de severidade; levantar um
  alerta; listar os alertas correntes.
- *Invariantes:* cada plugin tem canal próprio, separado do canal do core; o registro em disco é
  rotativo e limitado em tamanho; o alerta fica disponível em memória para a superfície de entrada
  consultar, além de ir para o disco; a gravação passa pela porta de filesystem (G6).
- *Modos de falha:* falha ao gravar no destino degrada para memória e não propaga ao chamador —
  registrar diagnóstico nunca é caminho crítico; construtor falho no boot é abort fatal (§11).
- *Implementação de referência:* `LoggingComponent`.

**Porta de registro de plugins.**
- *Responsabilidade:* descobrir as extensões instaladas, validar cada manifesto e manter o estado
  de carga de cada uma.
- *Operações:* descobrir os plugins da raiz de plugins; validar o manifesto contra o tipo
  autoritativo; conferir por análise estática a allowlist de imports do código do plugin; carregar
  o plugin; consultar o estado e as dependências declaradas de cada um.
- *Invariantes:* um plugin só é carregado com manifesto válido e versão de contratos compatível
  (`contracts_min_version`); a conferência de allowlist é estática e corre **antes** de qualquer
  linha do plugin executar; o nome do manifesto é a identidade do plugin e é única no processo;
  plugin recusado não impede a carga dos demais.
- *Modos de falha:* manifesto inválido, allowlist violada ou versão incompatível marcam o plugin
  `failed`, geram alerta e o boot segue (§11); construtor falho no boot é abort fatal.
- *Implementação de referência:* `PluginRegistryComponent`.

**Porta de injeção.**
- *Responsabilidade:* entregar a cada consumidor a implementação da porta que ele declara, sem que
  ele conheça a implementação.
- *Operações:* registrar a factory de uma porta; validar o grafo de dependências; resolver uma
  porta; expor aos plugins a superfície de resolução.
- *Invariantes:* o grafo é validado no boot (eager), antes de qualquer serviço existir; a
  materialização é lazy, com a factory rodando no primeiro `resolve` e o resultado reusado — uma
  instância por porta no processo; a porta de injeção é a **única** superfície de injeção exposta a
  plugin, que não alcança o registro de factories; a **ordem de boot** é fixa —
  `injeção → sinais → filesystem → estado → log → registro de plugins` → validação topológica dos
  serviços → descoberta e carga de plugins → superfície de entrada (`ui_shell`).
- *Modos de falha:* grafo com ciclo ou versão incompatível é rejeitado no boot, com as arestas
  reportadas; falha de factory no primeiro `resolve` propaga ao chamador e a aplicação segue, o que
  mantém a lazyness sem efeito sobre a tabela de contenção (§11); construtor falho no boot é abort
  fatal.
- *Implementação de referência:* `InjectorComponent`.

**Porta de raiz de dados.**
- *Responsabilidade:* resolver, para o sistema operacional hospedeiro, os diretórios do usuário em
  que a aplicação escreve.
- *Operações:* obter a raiz de dados, a de configuração, a de cache e a de registro da aplicação;
  derivar a subárvore de um plugin.
- *Invariantes:* a resolução segue a convenção do hospedeiro, e nenhum caminho de usuário é literal
  em código de serviço ou de plugin; a raiz de um plugin deriva da identidade dele e é disjunta da
  de qualquer outro; a porta resolve caminho e não cria nem escreve — criação e escrita são da
  porta de filesystem (G6); o valor resolvido é estável por toda a execução.
- *Modos de falha:* hospedeiro sem raiz resolvível falha na construção do serviço e propaga ao
  chamador; a porta nunca devolve caminho vazio nem relativo.
- *Implementação de referência:* serviço `paths`, ACL sobre `platformdirs`.

**Porta de lifecycle de plugin.**
- *Responsabilidade:* invocar os hooks de ciclo de vida das extensões sem que uma extensão
  defeituosa derrube o core.
- *Operações:* invocar o hook de carga, o de descarga e o de encerramento da aplicação; reportar o
  resultado de cada invocação.
- *Invariantes:* toda chamada a código de plugin feita pelo core passa por esta porta; exceção em
  hook é capturada, vira alerta pela porta de log e marca o plugin `failed`; plugin `failed` não
  recebe os hooks seguintes; a ordem de invocação respeita as dependências declaradas no manifesto;
  o hook de encerramento corre para todo plugin carregado, inclusive quando um anterior falhou.
- *Modos de falha:* hook que lança gera alerta, marca o plugin `failed` e a aplicação segue (§11);
  hook que não retorna bloqueia a thread chamadora — trabalho longo pertence à porta de execução
  assíncrona, nunca ao hook.
- *Implementação de referência:* `LifecycleHarness`.

**Porta de superfície de entrada.**
- *Responsabilidade:* ser o ponto pelo qual o mundo externo alcança o núcleo — expõe o estado do
  núcleo, recebe comandos e encerra o lifecycle da aplicação.
- *Operações:* apresentar ao mundo externo o estado publicado pelo núcleo; receber um comando
  externo e encaminhá-lo ao caso de uso correspondente; expor os alertas correntes da porta de log;
  disponibilizar os tokens de apresentação, quando a modalidade tiver apresentação; encerrar o
  lifecycle da aplicação.
- *Invariantes:* o core não conhece a tecnologia que realiza esta porta — nenhum módulo abaixo dela
  importa a biblioteca que a implementa, e a implementação pertence à camada de modalidade; é a
  última etapa da ordem de boot, então todo serviço e todo plugin já existem quando ela sobe; os
  tokens de apresentação (tema, estilo) ficam concentrados aqui e em nenhum outro lugar; a porta não
  carrega regra de domínio — traduz estado e comando, e delega.
- *Modos de falha:* falha ao construir a superfície de entrada é abort fatal do boot (§11), porque
  sem ela a aplicação não tem como ser operada; comando dirigido a plugin `failed` é recusado com
  alerta, sem derrubar a superfície; trabalho longo executado nesta porta bloqueia o atendimento —
  daí a porta de execução assíncrona.
- *Implementação de referência:* `ui_shell`, no toolkit que o projeto declarar.

**Porta de execução assíncrona.**
- *Responsabilidade:* executar trabalho fora da thread que atende a superfície de entrada e devolver
  resultado e falha no contexto de origem da chamada.
- *Operações:* submeter uma unidade de trabalho; registrar o que fazer com o resultado e o que fazer
  com a falha; cancelar uma unidade submetida; consultar o estado de execução de uma unidade.
- *Invariantes:* **trabalho pesado ou bloqueante nunca corre na thread que atende a superfície de
  entrada** — todo trabalho longo passa por esta porta; resultado e falha voltam no contexto de
  origem da chamada, e não no do worker, o que dispensa o chamador de sincronizar por conta própria;
  a unidade de trabalho não alcança a superfície de entrada diretamente, e se comunica pela porta de
  sinais ou pelo retorno; cancelar é idempotente.
- *Modos de falha:* exceção dentro da unidade de trabalho é capturada e entregue ao tratamento de
  falha registrado, no contexto de origem, e nunca escapa no worker (§11); unidade submetida sem
  tratamento de falha registrado gera alerta pela porta de log; unidade cancelada não entrega
  resultado nem falha.
- *Implementação de referência:* `TaskRunner`.

## 5. Contracts [REPLICAR estrutura; ESPECIALIZAR domínio]

Pacote instalável próprio, com versão SemVer independente da versão da aplicação — é a moeda de
compatibilidade dos plugins, que declaram no manifesto a versão mínima de que dependem
(`contracts_min_version`). Contém **zero código de runtime**: Protocols, modelos de dados, enums e
exceções.

O pacote reúne quatro classes de tipo:

- **As portas** (§4) declaradas como Protocols, um por serviço. É por eles que um plugin declara o
  que consome, sem alcançar nenhuma implementação.
- **Os tipos de manifesto** (`PluginManifest`, `ServiceManifest`), mirror dos tipos autoritativos
  do infracore: o infracore valida, e `contracts` publica o tipo para quem escreve o manifesto.
  Divergência entre os dois é defeito.
- **As exceções de contrato**, entre elas `NamespaceViolationError`, levantada pela porta de estado
  quando um plugin escreve fora do próprio namespace.
- **O domínio** da aplicação, em `contracts/domain/`.

**Domínio [ESPECIALIZAR]:** `contracts/domain/` recebe as entidades e VOs do negócio de cada
aplicação — imutáveis, framework-free, Pydantic com `extra="forbid"` e invariantes no
construtor. Os VOs do PantonicVideo servem de molde apenas quanto à **expressão** (imutáveis,
`extra="forbid"`, invariantes no construtor — um VO simples como `Dimensions` ilustra o
padrão); os tipos em si (`Project`, `Timeline`, `ContentAsset`, `CropRect`, `subtitle.py`,
`serialization.py`, `capcut.py`) são domínio de vídeo — **não portar** (§13).

## 6. Services — a camada ACL

**Doutrina ACL:** toda dependência externa (lib, API de OS, filesystem, env) pertence a
exatamente **um** serviço, cujo Protocol vive em `contracts/<s>.py`; `services/<s>/service.py`
é o **único** módulo que importa a dependência. Trocar a lib externa = trocar um serviço.

Quatro categorias:

1. **Expressão** [REPLICAR] — fachada fina sobre um componente do infracore: `signal`,
   `app_state`, `filesystem`, `plugin_registry`, `logging`, `injector`, mais `task_runner`
   (primitiva de concorrência declarada pelo projeto) e `paths`.
   Estes 8 formam o core de serviços de qualquer Pantonic*.
2. **Domínio** [ESPECIALIZAR] — capacidade própria do negócio, geralmente encapsulando uma lib
   externa (no PantonicVideo: `project`, `image`/Pillow, `subtitle`/SRT).
3. **Auxiliar** — lógica reusável entre plugins (criar quando surgir a necessidade).
4. **Simplificador** — extração de responsabilidade acessória que corrói coesão de outro módulo.

Serviços são descobertos por pasta, registrados no injetor e versionados por
`service_api_version` (caret-match na resolução).

## 7. Sinais [REPLICAR]

- Primitiva: `Signal[T]` (Protocol com `.value` cacheado + subscribe/unsubscribe via
  `Subscription`).
- Factories do `SignalService`: `signal_for_state(key)`, `signal_for_path(path)` →
  `Signal[FilesystemEvent]`, `signal_for_plugins()`, `signal_for_alerts()`. Serviços de domínio
  expõem os seus (`observe_*() → Signal[...]`).
- **Payload:** sempre Pydantic model em `contracts/` com `extra="forbid"`; eventos de domínio
  carregam `timestamp: datetime`.
- **Acoplamento entre plugins: só via state keys** (um publica, o outro observa via
  `state_observe`) — nunca assinatura direta de sinais de outro plugin.

## 8. Estado [REPLICAR]

- Interface: `state_get / state_set / state_delete / state_observe(key, cb)`.
- **Namespace:** chaves core pertencem ao infracore (ex.: `plugins.<nome>.enabled`); chaves
  de domínio compartilhadas entre plugins (no PantonicVideo: `current_project`) entram por
  whitelist explícita; fora isso, cada plugin só escreve em `plugins.<nome>.*`. Enforcement
  por AST em `tests/boundary/`.
- **Concorrência (v1):** last-write-wins; duas escritas na mesma chave em < 50 ms geram WARNING.
- **Persistência:** write-through em `<root>/state.json` via FilesystemComponent; arquivo
  corrompido no load → warning + rename `state.json.corrupt-<ts>`.

## 9. Plugins e manifests [REPLICAR doutrina]

**Doutrina (POC-first):**

- Plugin nasce de uma **POC standalone validada pelo cliente** (fluxo em GOVERNANCA.md §5).
- A POC original é preservada em `plugins/<nome>/adhoc/` — a plataforma **não refatora, não
  audita, não reescreve** a lógica validada.
- `plugin.py` é um orquestrador fino com 4 hooks de lifecycle: `on_load`, `on_enable`,
  `on_disable`, `on_unload`; roteia entre POC e plataforma via sinais/estado.
- **Pipeline de integração da POC (5 passos):** (1) inventário de dependências externas da
  POC; (2) mapeamento para serviços existentes ou proposta de serviço novo; (3) geração de
  `plugin.py`; (4) geração de `manifest.json`; (5) suíte de conformance.
- **Condições de POC integrável** — o que importa é *como* cada capacidade entra na
  aplicação, não *qual* capacidade é:
  - toda dependência externa da POC (rede, engine de ML, binário de sistema) é identificada
    no inventário do passo 1 e mapeada, na integração, para **exatamente um serviço ACL**
    (golden rule 9); nenhum código de plugin a importa diretamente;
  - trabalho pesado ou bloqueante nunca na thread que atende a superfície de entrada — sempre
    pela porta de execução assíncrona (§4);
  - a política de aceleração por hardware é decisão do PRD de cada app (no case de
    referência: GPU opcional, com fallback funcional em CPU; um domínio que exige GPU
    declara o requisito mínimo no PRD);
  - nenhum processo de longa duração órfão: se a POC exige um, ele passa a ser propriedade
    de um serviço com lifecycle gerenciado;
  - o núcleo lógico da POC é decomponível em funções puras determinísticas testáveis; o
    não-determinismo fica confinado às bordas (rede, hardware, engines externos — que devem
    expor algum controle de reprodutibilidade, ex.: seed em engines de ML);
  - sem estado persistido fora do user-data; licença compatível.

**Manifest (`manifest.json`, Pydantic `extra="forbid"`):** `name` (snake_case único), `version`
(SemVer), `contracts_min_version`, `author`, `description` (≤500 chars), `use_case` (nome do caso
de uso reconhecido pelo dono — a mesma frase que o PRD usa para o objetivo do usuário —, único na
base de plugins), `entry_point` (`modulo:Classe`), `required_services` (`[{name, min_version}]`),
`inputs`/`outputs` (declarativos), `permissions`.

**Validação no load:** caret-match de contracts → disponibilidade/versão dos serviços →
unicidade de `use_case` na base de plugins → allowlist de imports por AST (`contracts.*`, o
toolkit da camada de apresentação declarado pelo projeto + stdlib permitido, definido por
app — default do case de referência: `pathlib`, `typing`) → colisão de
nome (built-in vence). Qualquer falha → plugin `failed` com razão registrada; a aplicação
continua de pé.

### 9.1 O caso de uso dentro do plugin

- O **caso de uso é o artefato de aplicação** do plugin: mora em `plugins/<nome>/use_case.py`,
  numa classe `<Nome>UseCase` com um método público de execução.
- Depende **só** de `contracts` — portas e domínio —, recebidas por injeção; não importa a
  superfície de apresentação, nem serviço concreto, nem lib externa.
- `plugin.py` e o adaptador de apresentação **apenas invocam** o caso de uso: nenhuma regra de
  negócio mora neles.
- **Exatamente um caso de uso por plugin.** Dois é decomposição errada; zero é caso de uso
  diluído no adaptador.
- A POC preservada em `adhoc/` **não é** o caso de uso — o caso de uso a orquestra, e a POC
  continua intocada.
- O TF do plugin exercita o caso de uso pela superfície dele, não pela apresentação: é isso que
  torna o teste independente da modalidade.

## 10. Operações de OS e IN/OUT

- **Escrita em disco:** só o `FilesystemComponent` chama `open(...,'w')`, `Path.write_*`,
  `os.makedirs`, `shutil.*` (**G6**) — enforcement por teste AST de conformance. Exceção única:
  handlers do `logging` stdlib.
- **Raiz de dados:** um único serviço (`PathsService`) resolve `user_data_root`/subdirs; nenhum
  caminho absoluto hardcoded fora dele. A regra agnóstica é o **ponto único de resolução**; a
  resolução por convenção de OS via platformdirs é o default do case de referência.
- **Watch de arquivos:** via `signal_for_path` (FilesystemComponent), nunca polling.
- **Integrações externas** (no PantonicVideo: CapCut): sempre um serviço ACL dedicado com
  Protocol em contracts — o padrão a seguir para qualquer sistema externo.

## 11. Contenção de falhas [REPLICAR]

Princípio: **o core nunca cai por causa de extensão.**

| Origem da falha | Efeito |
|---|---|
| Construtor de componente do infracore | Abort fatal do boot (com mensagem) |
| Grafo de serviços com ciclo/versão incompatível | Rejeição no boot, com arestas reportadas |
| Factory de serviço no primeiro resolve | Erro propagado ao chamador; app segue |
| Hook de plugin (`on_load` etc.) | Capturado pelo LifecycleHarness → alerta → plugin `failed` |
| Unidade submetida à porta de execução assíncrona | Falha entregue ao tratamento registrado, no contexto de origem da chamada; a superfície de entrada nunca fica bloqueada |

A tabela completa de contenção do case de referência está em
`PantonicVideo/docs/ARCHITECTURE.md` §13.1 — replicar o padrão, adaptando os amendments.

## 12. Testes [REPLICAR disciplina]

| Suíte | Diretório | Postura |
|---|---|---|
| Infracore | `tests/infracore/` | Componentes reais |
| Serviços | `tests/services/` | Componentes/serviços mockados |
| Plugins | `tests/plugins/` | Serviços mockados; mais o harness de UI declarado pelo projeto |
| Integração | `tests/integration/` | Boot completo da aplicação |
| Funcionais | `test_tf_<id>.py` | Um por UC/RF do PRD (definidos no Sprint Plan) |
| Regressão | `test_tr_<task_id>.py` | Trancam invariantes; formam o piso |
| **Conformance** | `tests/conformance/` | **Gate arquitetural (AST):** regra de camadas, egress G6, allowlist de plugins |
| Boundary | `tests/boundary/` | Namespace de estado por plugin |

Disciplina de piso: a contagem de regressões verdes nunca diminui; o gate de conformance é
bloqueante para qualquer merge/`done` (ver guardrails em GOVERNANCA.md §7).

## 13. O que NÃO portar do PantonicVideo

Específicos do domínio de vídeo — servem apenas como exemplo de como especializar:

- `contracts/domain/subtitle.py`, `contracts/domain/serialization.py` (manifesto
  `pantonicvideo-project.json`), `contracts/capcut.py`;
- os tipos do agregado de projeto de vídeo (`Project`, `Timeline`, `ContentAsset`), os VOs do
  ImageService (`CropRect`, `Dimensions`) e a chave de estado `current_project` que os
  acompanha;
- serviços de domínio `project`, `image`, `subtitle` e o serviço/integração CapCut;
- os 4 plugins built-in (`project_launcher`, `project_folder`, `image_cropping`,
  `subtitle_text_tool`).

Estimativa do case (medida no case de referência): ~90% do `infracore/` e ~80% dos
`contracts/` são reusáveis diretamente; o resto é o espaço [ESPECIALIZAR] que o PRD e o
Architecture de cada novo projeto preenchem.

## 14. Checklist de bootstrap de um novo core Pantonic*

Ordem sugerida para o Sprint Plan do projeto novo (cada item testável ao fim):

1. `contracts` como pacote instalável (as portas do §4 declaradas como Protocols + exceptions +
   manifest).
2. As primitivas que realizam as portas, na ordem de boot do §4, com testes de infracore reais.
3. Injetor + serviços de expressão (8 do §6.1) + testes de serviços.
4. Superfície de entrada mínima (§4): o estado do núcleo exposto, um canal de comando e a lista de
   alertas, na tecnologia da modalidade escolhida.
5. PluginRegistry + lifecycle + um plugin "hello" de referência.
6. Suíte de conformance (camadas, G6, allowlist, namespace) — a partir daqui, gate bloqueante.
7. Serviços de domínio e plugins reais do PRD [ESPECIALIZAR].
