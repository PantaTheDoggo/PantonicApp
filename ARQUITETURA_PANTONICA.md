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
> **Convenção de perfil:** o núcleo descrito aqui é **agnóstico a stack e plataforma**. Trechos
> marcados com *[perfil `desktop-pyside6`, §1.1]* valem **apenas** para projetos que declaram esse
> perfil — a seção canônica de perfis é [GOVERNANCA.md](GOVERNANCA.md) §1.1, e a declaração vive em
> `.claude/PERFIL` na raiz (ausência do arquivo ⇒ `desktop-pyside6`). Um projeto de outro perfil
> (`container`, `web-servidor`) lê esses trechos como ilustração do case de referência, nunca como
> exigência do framework. **Desambiguação de numeração:** o `§1.1` que aparece *dentro* do marcador
> de perfil aponta sempre para [GOVERNANCA.md](GOVERNANCA.md) §1.1 (Perfis); a §1.1 **deste**
> documento é a seção de fundamentos CA+DDD.

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

**Grau de aderência da implementação atual: NÃO AUDITADO.** Esta seção declara a **doutrina**. O
grau em que o infracore e os plugins da implementação de referência (`PantonicVideo`) de fato
estendem CA+DDD — quantos agregados têm invariante real, quantos plugins mapeiam um caso de uso
único, onde o domínio vazou para a infraestrutura — **ainda não foi medido**. A medição é a tarefa
`T14` de [docs/plans/P-0730-v2-identidade.md](docs/plans/P-0730-v2-identidade.md), com saída em
`docs/audits/AUDIT_ARCH_<AAAA-MM-DD>.md` no repositório da implementação de referência. Até esse
relatório existir, nenhum documento do corpus pode afirmar conformidade a CA+DDD como fato
consumado — asserção sem medida é exatamente o que G-PREMISE ([GOVERNANCA.md](GOVERNANCA.md) §7)
proíbe.

## 2. Modelo de camadas

```
infracore  ←  contracts  ←  services  ←  plugins
   (1)           (2)           (3)         (4)
```

| Camada | Conteúdo | Pode importar |
|---|---|---|
| **infracore** [REPLICAR] | Componentes de bootstrap, injetor, lifecycle + a superfície de entrada do perfil (UI shell *[perfil `desktop-pyside6`, §1.1]*) | stdlib, pydantic, platformdirs + allowlist de data-classes de contracts; mais o toolkit do perfil ativo (no `desktop-pyside6`: PySide6) |
| **contracts** [REPLICAR estrutura; ESPECIALIZAR domínio] | Protocols (portas), Pydantic BaseModels, Enums, entidades de domínio — **zero código de runtime** | pydantic, typing, uuid |
| **services** [REPLICAR expressão; ESPECIALIZAR domínio] | Implementações dos Protocols; ACL das dependências externas | contracts, infracore, a lib externa que encapsula |
| **plugins** [ESPECIALIZAR] | Funcionalidades de negócio; recebem serviços via injetor | contracts, stdlib restrito (allowlist definida por app; default do case: pathlib, typing) + o toolkit do perfil ativo (no `desktop-pyside6`: PySide6) |

Relação com os elementos de DDD (§1.1): **entidades, objetos de valor e agregados** vivem em
`contracts/domain` — dados e invariantes, zero runtime; **serviços de domínio** (puros) vivem no
código de negócio do plugin, ou viram serviço com porta quando dois plugins precisam deles;
**serviços de aplicação/ACL** vivem em `services/`, sempre atrás de um Protocol de `contracts/`; e
**cada caso de uso** é um plugin (§9). A regra de dependência é o que mantém o domínio puro: como
`contracts/` não importa `services/` nem `plugins/`, o domínio não tem como alcançar o mundo
externo — só ser alcançado por ele.

Relação com MVVM (§10) *[perfil `desktop-pyside6`, §1.1]*: View e ViewModel vivem em
shell/plugins; Model puro vive em contracts/domain e no código ad-hoc dos plugins. Projetos de
outro perfil não têm essa camada de apresentação — as quatro camadas e a regra de dependência
acima permanecem idênticas.

## 3. Estrutura de pastas canônica

```
<app>/
├── infracore/
│   ├── bootstrap_components/     # signal, app_state, filesystem, plugin_registry, logging
│   ├── injector_component/
│   ├── lifecycle/                # LifecycleHarness, excepthook, ponte de logs do toolkit
│   ├── manifest/                 # tipos autoritativos de manifest
│   ├── ui_shell/                 # [perfil desktop-pyside6] MainWindow, DockManager, TitleBar,
│   │                             # AlertPanel, DesignSystem
│   └── app.py                    # bootstrap_application()
├── contracts/                    # pacote instalável próprio (versão SemVer independente)
│   └── src/contracts/
│       ├── domain/               # entidades e VOs [ESPECIALIZAR]
│       └── *.py                  # um Protocol por serviço + manifest + exceptions
├── services/<nome>/service.py    # descoberta por pasta; um Protocol por serviço
├── plugins/<nome>/               # manifest.json + plugin.py + adhoc/
│                                 # (+ view_model.py [perfil desktop-pyside6])
├── tests/                        # infracore | contracts | services | plugins | integration |
│                                 # functional (TF-*) | regression (TR-*) | conformance | boundary
└── tools/                        # harness do agente de integração etc.
```

As entradas marcadas `[perfil desktop-pyside6]` só existem nesse perfil (§1.1 de
[GOVERNANCA.md](GOVERNANCA.md)); o restante da árvore é comum a qualquer perfil.

## 4. Infracore — componentes de bootstrap [REPLICAR]

Primitivas de runtime construídas **antes** do injetor, em ordem fixa; falha de construtor é
**abort fatal** do boot. Versionadas por `__component_version__`.

| Componente | Responsabilidade |
|---|---|
| `SignalComponent` | Primitiva reativa `Signal[T]` (cacheia valor, notifica mudança) + `Subscription` |
| `AppStateComponent` | KV store em memória com write-through JSON (via FilesystemComponent) |
| `FilesystemComponent` | **Único ponto de escrita em disco (G6)**; locking por path; watch com callbacks |
| `LoggingComponent` | Log por plugin + log rotativo do infracore + lista de alertas em memória |
| `PluginRegistryComponent` | Descoberta, validação de manifest, scan de allowlist (AST), lifecycle de plugins |
| `InjectorComponent` | Injetor topológico: valida grafo/ciclos no boot (eager), materializa serviços no primeiro `resolve` (lazy) |
| `LifecycleHarness` | Invocação segura de hooks de plugin (try/except → alerta → marca `failed`) |
| `ui_shell` *[perfil `desktop-pyside6`, §1.1]* | Shell Qt: canvas central, docks laterais, menu, status bar, `ShellViewModel`, `DesignSystem` (tokens de tema — só aqui) |

**Ordem de boot:** `Injector → Signal → Filesystem → AppState → Logging → PluginRegistry` →
validação topológica dos serviços → descoberta/carga de plugins → shell *[perfil
`desktop-pyside6`, §1.1]*. Serviços são lazy
(factories rodam no primeiro resolve), o que não altera a tabela de contenção de falhas (§12).

## 5. Contracts [REPLICAR estrutura + portas genéricas]

Pacote Python próprio, instalável, com versão SemVer — é a moeda de compatibilidade dos plugins
(`contracts_min_version` no manifest).

**Portas genéricas (Protocols) que todo Pantonic* replica:**
`FilesystemService`, `AppStateService`, `SignalService`, `LoggingService`, `InjectorService`
(única superfície de injeção exposta a plugins), `PluginRegistryService`, `PathsService`
(raiz de dados do usuário por OS), `TaskRunner` (execução off-thread com callbacks no UI
thread), além de `PluginManifest`/`ServiceManifest` (mirror do infracore) e
`NamespaceViolationError`.

**Domínio [ESPECIALIZAR]:** `contracts/domain/` recebe as entidades e VOs do negócio de cada
aplicação — imutáveis, framework-free, Pydantic com `extra="forbid"` e invariantes no
construtor. Os VOs do PantonicVideo servem de molde apenas quanto à **expressão** (imutáveis,
`extra="forbid"`, invariantes no construtor — um VO simples como `Dimensions` ilustra o
padrão); os tipos em si (`Project`, `Timeline`, `ContentAsset`, `CropRect`, `subtitle.py`,
`serialization.py`, `capcut.py`) são domínio de vídeo — **não portar** (§14).

## 6. Services — a camada ACL

**Doutrina ACL:** toda dependência externa (lib, API de OS, filesystem, env) pertence a
exatamente **um** serviço, cujo Protocol vive em `contracts/<s>.py`; `services/<s>/service.py`
é o **único** módulo que importa a dependência. Trocar a lib externa = trocar um serviço.

Quatro categorias:

1. **Expressão** [REPLICAR] — fachada fina sobre um componente do infracore: `signal`,
   `app_state`, `filesystem`, `plugin_registry`, `logging`, `injector`, mais `task_runner`
   (primitiva de concorrência do perfil — no `desktop-pyside6`: QThreadPool/QRunnable) e `paths`.
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
- **Pipeline do agente de integração (5 passos):** (1) inventário de dependências externas da
  POC; (2) mapeamento para serviços existentes ou proposta de serviço novo; (3) geração de
  `plugin.py`; (4) geração de `manifest.json`; (5) suíte de conformance.
- **Condições de POC integrável** — o que importa é *como* cada capacidade entra na
  aplicação, não *qual* capacidade é:
  - toda dependência externa da POC (rede, engine de ML, binário de sistema) é identificada
    no inventário do passo 1 e mapeada, na integração, para **exatamente um serviço ACL**
    (golden rule 9); nenhum código de plugin a importa diretamente;
  - trabalho pesado ou bloqueante nunca no UI thread — sempre TaskRunner (§10);
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
(SemVer), `contracts_min_version`, `author`, `description` (≤500 chars),
`entry_point` (`modulo:Classe`), `required_services` (`[{name, min_version}]`), `inputs`/
`outputs` (declarativos), `permissions`.

**Validação no load:** caret-match de contracts → disponibilidade/versão dos serviços →
allowlist de imports por AST (`contracts.*`, o toolkit do perfil ativo — no `desktop-pyside6`,
`PySide6.*` — + stdlib permitido, definido por
app — default do case de referência: `pathlib`, `typing`) → colisão de
nome (built-in vence). Qualquer falha → plugin `failed` com razão registrada; a aplicação
continua de pé.

## 10. MVVM e PySide6 [REPLICAR] *[perfil `desktop-pyside6`, §1.1]*

Seção **inteira** do perfil `desktop-pyside6` (§1.1 de [GOVERNANCA.md](GOVERNANCA.md)). Projetos
de outro perfil não a aplicam e nada aqui é exigido pelo núcleo; o que permanece universal é o
Model puro — entidades sem dependência de framework, já coberto por §5.

- **View** — widgets; vive na shell e nos plugins; sem lógica.
- **ViewModel** — `QObject` **QtCore-only** (proibido importar widgets); orquestra, expõe
  signals/slots; um `view_model.py` por plugin; egress de I/O passa pelo ViewModel → serviços.
- **Model** — puro (sem Qt): entidades em `contracts/domain/` e lógica validada em `adhoc/`.
- Geometria, `QScreen`, styling e tokens de tema (`DesignSystem`) pertencem **exclusivamente à
  shell/Views** — nunca a ViewModel ou Model.
- **Threading:** trabalho pesado nunca no UI thread — sempre via `TaskRunner.run(fn, ...,
  on_finished, on_failed, on_progress)`, que executa em worker e invoca callbacks no UI thread.
  Plugins não importam primitivas de thread do Qt diretamente.

## 11. Operações de OS e IN/OUT

- **Escrita em disco:** só o `FilesystemComponent` chama `open(...,'w')`, `Path.write_*`,
  `os.makedirs`, `shutil.*` (**G6**) — enforcement por teste AST de conformance. Exceção única:
  handlers do `logging` stdlib.
- **Raiz de dados:** um único serviço (`PathsService`) resolve `user_data_root`/subdirs; nenhum
  caminho absoluto hardcoded fora dele. A regra agnóstica é o **ponto único de resolução**; a
  resolução por convenção de OS via platformdirs é o default do perfil `desktop-pyside6` *[§1.1]*.
- **Watch de arquivos:** via `signal_for_path` (FilesystemComponent), nunca polling.
- **Integrações externas** (no PantonicVideo: CapCut): sempre um serviço ACL dedicado com
  Protocol em contracts — o padrão a seguir para qualquer sistema externo.

## 12. Contenção de falhas [REPLICAR]

Princípio: **o core nunca cai por causa de extensão.**

| Origem da falha | Efeito |
|---|---|
| Construtor de componente do infracore | Abort fatal do boot (com mensagem) |
| Grafo de serviços com ciclo/versão incompatível | Rejeição no boot, com arestas reportadas |
| Factory de serviço no primeiro resolve | Erro propagado ao chamador; app segue |
| Hook de plugin (`on_load` etc.) | Capturado pelo LifecycleHarness → alerta → plugin `failed` |
| Task em worker (TaskRunner) | `on_failed(exc)` no UI thread; UI nunca congela |

A tabela completa de contenção do case de referência está em
`PantonicVideo/docs/ARCHITECTURE.md` §13.1 — replicar o padrão, adaptando os amendments.

## 13. Testes [REPLICAR disciplina]

| Suíte | Diretório | Postura |
|---|---|---|
| Infracore | `tests/infracore/` | Componentes reais |
| Serviços | `tests/services/` | Componentes/serviços mockados |
| Plugins | `tests/plugins/` | Serviços mockados; mais o harness de UI do perfil (no `desktop-pyside6`: pytest-qt) |
| Integração | `tests/integration/` | Boot completo da aplicação |
| Funcionais | `test_tf_<id>.py` | Um por UC/RF do PRD (definidos no Sprint Plan) |
| Regressão | `test_tr_<task_id>.py` | Trancam invariantes; formam o piso |
| **Conformance** | `tests/conformance/` | **Gate arquitetural (AST):** regra de camadas, egress G6, allowlist de plugins |
| Boundary | `tests/boundary/` | Namespace de estado por plugin |

Disciplina de piso: a contagem de regressões verdes nunca diminui; o gate de conformance é
bloqueante para qualquer merge/`done` (ver guardrails em GOVERNANCA.md §7).

## 14. O que NÃO portar do PantonicVideo

Específicos do domínio de vídeo — servem apenas como exemplo de como especializar:

- `contracts/domain/subtitle.py`, `contracts/domain/serialization.py` (manifesto
  `pantonicvideo-project.json`), `contracts/capcut.py`;
- os tipos do agregado de projeto de vídeo (`Project`, `Timeline`, `ContentAsset`), os VOs do
  ImageService (`CropRect`, `Dimensions`) e a chave de estado `current_project` que os
  acompanha;
- serviços de domínio `project`, `image`, `subtitle` e o serviço/integração CapCut;
- os 4 plugins built-in (`project_launcher`, `project_folder`, `image_cropping`,
  `subtitle_text_tool`).

Também **não é núcleo** o que pertence ao perfil `desktop-pyside6` do case (§1.1 de
[GOVERNANCA.md](GOVERNANCA.md)): a shell Qt (`infracore/ui_shell/`), o par View/ViewModel de §10 e
as primitivas de thread do Qt sob o `TaskRunner`. Um projeto de perfil `container` ou
`web-servidor` substitui esses artefatos pelo equivalente do seu perfil e mantém intactos as
quatro camadas, a ACL, sinais/estado, plugins/manifests, contenção de falhas e a disciplina de
testes.

Estimativa do case (medida no perfil `desktop-pyside6`): ~90% do `infracore/` e ~80% dos
`contracts/` são reusáveis diretamente; o resto é o espaço [ESPECIALIZAR] que o PRD e o
Architecture de cada novo projeto preenchem.

## 15. Checklist de bootstrap de um novo core Pantonic*

Ordem sugerida para o Sprint Plan do projeto novo (cada item testável ao fim):

1. `contracts` como pacote instalável (portas genéricas do §5 + exceptions + manifest).
2. Componentes de bootstrap na ordem do §4, com testes de infracore reais.
3. Injetor + serviços de expressão (8 do §6.1) + testes de serviços.
4. UI shell mínima (MainWindow + DockManager + AlertPanel) + ShellViewModel.
5. PluginRegistry + lifecycle + um plugin "hello" de referência.
6. Suíte de conformance (camadas, G6, allowlist, namespace) — a partir daqui, gate bloqueante.
7. Serviços de domínio e plugins reais do PRD [ESPECIALIZAR].
