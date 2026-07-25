# ARQUITETURA PANTONICA — Core reusável para aplicações Pantonic*

> **Audiência:** o **agente de planejamento** de um novo projeto Pantonic*. Este documento
> traduz a infraestrutura do **PantonicVideo** (`D:\workspaces\PantonicVideo`, case de sucesso e
> implementação de referência) num modelo de core reusável. Um novo projeto **replica o core
> descrito aqui** e diversifica apenas domínio e casos de uso, conforme
> [GOVERNANCA.md](GOVERNANCA.md) §2.
>
> Convenção de leitura: "**[REPLICAR]**" = copiar/portar do PantonicVideo com mudanças mínimas;
> "**[ESPECIALIZAR]**" = ponto onde cada aplicação escreve o seu próprio código.

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

## 2. Modelo de camadas

```
infracore  ←  contracts  ←  services  ←  plugins
   (1)           (2)           (3)         (4)
```

| Camada | Conteúdo | Pode importar |
|---|---|---|
| **infracore** [REPLICAR] | Componentes de bootstrap, injetor, lifecycle, UI shell | stdlib, PySide6, pydantic, platformdirs + allowlist de data-classes de contracts |
| **contracts** [REPLICAR estrutura; ESPECIALIZAR domínio] | Protocols (portas), Pydantic BaseModels, Enums, entidades de domínio — **zero código de runtime** | pydantic, typing, uuid |
| **services** [REPLICAR expressão; ESPECIALIZAR domínio] | Implementações dos Protocols; ACL das dependências externas | contracts, infracore, a lib externa que encapsula |
| **plugins** [ESPECIALIZAR] | Funcionalidades de negócio; recebem serviços via injetor | contracts, PySide6, stdlib restrito (allowlist definida por app; default do case: pathlib, typing) |

Relação com MVVM (§10): View e ViewModel vivem em shell/plugins; Model puro vive em
contracts/domain e no código ad-hoc dos plugins.

## 3. Estrutura de pastas canônica

```
<app>/
├── infracore/
│   ├── bootstrap_components/     # signal, app_state, filesystem, plugin_registry, logging
│   ├── injector_component/
│   ├── lifecycle/                # LifecycleHarness, excepthook, ponte de logs Qt
│   ├── manifest/                 # tipos autoritativos de manifest
│   ├── ui_shell/                 # MainWindow, DockManager, TitleBar, AlertPanel, DesignSystem
│   └── app.py                    # bootstrap_application()
├── contracts/                    # pacote instalável próprio (versão SemVer independente)
│   └── src/contracts/
│       ├── domain/               # entidades e VOs [ESPECIALIZAR]
│       └── *.py                  # um Protocol por serviço + manifest + exceptions
├── services/<nome>/service.py    # descoberta por pasta; um Protocol por serviço
├── plugins/<nome>/               # manifest.json + plugin.py + view_model.py + adhoc/
├── tests/                        # infracore | contracts | services | plugins | integration |
│                                 # functional (TF-*) | regression (TR-*) | conformance | boundary
└── tools/                        # harness do agente de integração etc.
```

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
| `ui_shell` | Shell Qt: canvas central, docks laterais, menu, status bar, `ShellViewModel`, `DesignSystem` (tokens de tema — só aqui) |

**Ordem de boot:** `Injector → Signal → Filesystem → AppState → Logging → PluginRegistry` →
validação topológica dos serviços → descoberta/carga de plugins → shell. Serviços são lazy
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
   (QThreadPool/QRunnable) e `paths`. Estes 8 formam o core de serviços de qualquer Pantonic*.
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
allowlist de imports por AST (`contracts.*`, `PySide6.*` + stdlib permitido, definido por
app — default do case de referência: `pathlib`, `typing`) → colisão de
nome (built-in vence). Qualquer falha → plugin `failed` com razão registrada; a aplicação
continua de pé.

## 10. MVVM e PySide6 [REPLICAR]

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
- **Raiz de dados por OS:** `PathsService` (platformdirs) resolve `user_data_root`/subdirs;
  nenhum caminho absoluto hardcoded fora dele.
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
| Plugins | `tests/plugins/` | Serviços mockados; pytest-qt |
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

Estimativa do case: ~90% do `infracore/` e ~80% dos `contracts/` são reusáveis diretamente; o
resto é o espaço [ESPECIALIZAR] que o PRD e o Architecture de cada novo projeto preenchem.

## 15. Checklist de bootstrap de um novo core Pantonic*

Ordem sugerida para o Sprint Plan do projeto novo (cada item testável ao fim):

1. `contracts` como pacote instalável (portas genéricas do §5 + exceptions + manifest).
2. Componentes de bootstrap na ordem do §4, com testes de infracore reais.
3. Injetor + serviços de expressão (8 do §6.1) + testes de serviços.
4. UI shell mínima (MainWindow + DockManager + AlertPanel) + ShellViewModel.
5. PluginRegistry + lifecycle + um plugin "hello" de referência.
6. Suíte de conformance (camadas, G6, allowlist, namespace) — a partir daqui, gate bloqueante.
7. Serviços de domínio e plugins reais do PRD [ESPECIALIZAR].
