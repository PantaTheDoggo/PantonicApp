# P-0732 — Estágio 7: as portas do core e a camada de casos de uso

- **Origem:** 2026-08-07 — auditoria de aderência a CA+DDD na implementação de referência
  (`V2E-T10`), medida sobre `D:\workspaces\PantonicVideo`
- **Iniciativa:** `PANTONIC-V2` · **Estágio:** 7 · **Prefixo de tarefa:** `V2P-`
- **Depende de:** `docs/plans/P-0731-v2-extracao-modalidade.md`, fechado 21/21 — este plano nasce
  como a última tarefa dele (`V2E-T11`), com o escopo corrigido pela `DE-6`
- **Fecha em:** aceite do dono sobre o `README.md` (`T10`). **Sem bump, sem tag, sem instrução de
  migração por número:** a versão está congelada em `0.0.0` (`DE-7` do plano anterior) e todo
  registro de mudança vai para a seção `[Não lançado]` do `CHANGELOG.md`
- **Checagem de versão do kit:** modo hub — versão **congelada em `0.0.0`**, comparação local ×
  remoto **suspensa**, nada a comparar. O gatilho da porta de saída de guardrail
  (`GOVERNANCA.md` §7.1, regime da `DE-8`) está **armado** pelo fechamento do plano anterior: há uma
  rodada de revisão **pendente**, e ela é a `T7` deste plano — não fica como vão

## 0. O problema

O corpus promete, em dois lugares aprovados, que o core doutrina a metade não-domínio da
arquitetura:

> `ARQUITETURA_PANTONICA.md` §1 — "bootstrap, injeção de dependências, lifecycle, estado, sinais,
> egress de filesystem e execução assíncrona não são decisões de projeto — são um core herdado. É o
> que impede que cada aplicação reinvente a metade não-domínio da arquitetura, que é justamente onde
> a CA cala."

> `GOVERNANCA.md` §1, premissa 2 — "Infracore como doutrina das camadas de aplicação e
> infraestrutura."

A promessa não está cumprida em nenhuma das duas metades, e as duas falhas têm a mesma forma: **o
core é descrito pela implementação, não pelo contrato.**

**Infraestrutura.** O `ARQUITETURA_PANTONICA.md` §4 descreve oito *componentes* concretos do case de
referência (`SignalComponent`, `FilesystemComponent`, `LifecycleHarness`, `ui_shell`…) e o §5 lista
os *nomes* das portas correspondentes. Nome de porta não é contrato: não há operação, semântica,
invariante nem modo de falha escrito em lugar nenhum do hub. Um projeto de outra stack que queira
"herdar os conceitos e os contratos" precisa hoje ler o código da implementação de referência — que
é exatamente o que a regra de dependência entre as camadas proíbe. O próprio `GOVERNANCA.md` §2
admite o vão em texto: *"a abstração das portas do infracore (lifecycle, injeção, estado, sinais,
filesystem) é etapa própria e ainda não executada"*.

**Aplicação.** A auditoria mediu **zero artefatos de caso de uso** na implementação de referência: a
orquestração vive em ViewModels (5.216 linhas em 14 módulos) e numa fachada de serviço com 18
métodos e 6 razões para mudar. A doutrina diz "um plugin = um caso de uso", mas não diz **onde o
caso de uso mora dentro do plugin** — e, na ausência de residência, ele se aloja no adaptador de
apresentação, que é a camada da modalidade. O estágio anterior tirou a modalidade da doutrina; sem
esta correção, ela continua sendo o lugar onde o negócio mora no código.

As duas metades são o mesmo trabalho: **escrever o core como porta**, e não como o objeto que
alguém já construiu.

## 1. Decisões (fechadas no ato do planejamento)

| id | Decisão | Origem |
|---|---|---|
| `DI-1` | Este plano é o **Estágio 7** da iniciativa `PANTONIC-V2`, prefixo `V2P-`. O escopo é o vão medido pela auditoria do estágio anterior: portas do core (infraestrutura) e residência do caso de uso (aplicação). A iniciativa permanece aberta enquanto houver estágio vivo; nenhum estágio novo é aberto por este plano. | planejamento, 2026-08-07 |
| `DI-2` | **O hub especifica contrato de porta, não implementação.** Nenhum código de `infracore` nasce aqui: o hub é doutrina + kit, não tem camada de produção, e um `infracore/` genérico no hub seria código sem chamador (golden rule 3 e `G-DEADCODE`). O que o hub entrega é o contrato que permite implementar a porta em qualquer stack, e a implementação de referência continua sendo citada como exemplo — nunca como norma. | planejamento, 2026-08-07 |
| `DI-3` | **A superfície de entrada da aplicação vira porta declarada**, com zero implementação no hub. É a porta que a camada de modalidade implementa do lado de fora; o binding de toolkit não volta ao hub sob nenhuma forma (`DE-1`/`DE-2` do plano anterior continuam valendo). Mesmo tratamento para a porta de execução assíncrona, hoje descrita com vocabulário de interface gráfica ("UI thread"). | planejamento, 2026-08-07 |
| `DI-4` | **Residência do caso de uso:** `plugins/<nome>/use_case.py`, uma classe `<Nome>UseCase` com um método público de execução, dependendo só de `contracts` (portas e domínio), recebida por injeção; `plugin.py` e o adaptador de apresentação apenas invocam; o `manifest.json` declara o campo `use_case`. **Nenhuma regra nova é criada** — é a forma que o corpus já exige ("um caso de uso = um plugin = um manifest = um TF") e que o kit já procura: o bloco `DDD-usecase` da skill `audit-sweep` varre `^class \w+UseCase` por diretório de plugin e trata 0 ou >1 como divergência de `D9`. O que faltava era a residência escrita. | planejamento, 2026-08-07 |
| `DI-5` | **Nenhum item novo em `GOVERNANCA.md` §7.** O plano não abre guardrail; ele dá **objeto verificável** às verificações 8 e 9 do `pantonic-auditor-arch`, que já existem e hoje são inauditáveis por falta de artefato. Doutrina que já está escrita não vira guardrail por ser finalmente cumprível. | planejamento, 2026-08-07 |
| `DI-6` | **Nenhum verificador executável novo no hub.** Um check de manifesto de plugin não tem alvo: o hub não tem `plugins/`, `docs/CONSUMIDORES.md` mede **0/6 consumidores com `.claude/kit/` instalado**, e a implementação de referência foi declinada pelo dono para investimento. Verificador sem alvo é o caso exato que `G-DEADCODE` e a golden rule 3 proíbem. O enforcement fica na cadeia de auditoria (`audit-sweep` → `pantonic-auditor-arch`) e no TF por caso de uso, que a doutrina já exige. **Gatilho registrado em §7:** o check entra por plano próprio quando existir um projeto que materialize o kit. | planejamento, 2026-08-07 |
| `DI-7` | A rodada de revisão de guardrails aberta pelo fechamento do plano anterior é **tarefa deste plano** (`T7`), com o rótulo `P-0731` no registro de rodadas. Sob o regime da `DE-8`, a rodada pendura-se no fechamento de um plano e a skill de checagem a reporta na criação do plano seguinte — este. Deixá-la para "algum plano futuro" a transformaria no vão que `G-PLANREADY` proíbe. | planejamento, 2026-08-07 |
| `DI-8` | **A numeração das seções do `ARQUITETURA_PANTONICA.md` não muda.** A camada de aplicação entra como `### 9.1` dentro da seção de plugins, e as portas reescrevem §4/§5 no lugar. Renumerar quebraria referência cruzada de documento fechado sem ganho (mesma régua que preservou os nomes de plano em `DP-G5`). | planejamento, 2026-08-07 |

**Trade-off da `DI-4`,** explícito porque tem custo real. O campo `use_case` nasce **obrigatório** no
manifesto, e o manifesto valida com `extra="forbid"`: um projeto com plugins já escritos paga uma
migração de um campo por plugin, e um manifesto sem o campo passa a ser inválido. *Alternativa
rejeitada:* campo opcional — recusada porque campo opcional não torna `D9` auditável, e a
inauditabilidade é exatamente o achado que este plano fecha. *Por que o custo é aceitável, medido:*
nenhuma instalação do kit existe hoje (0/6), a versão está congelada e não há compatibilidade
publicada a quebrar, e o registro da mudança vai para `[Não lançado]`, que é o que um adotante
futuro lê antes de migrar.

## 2. Alcance medido (insumo — nada inferido na execução)

Da auditoria de arquitetura da implementação de referência (relatórios em `docs/audits/` do
repositório `PantonicVideo`):

- `contracts/domain/` estende DDD plenamente — VOs `frozen`, invariante no construtor, comportamento
  na raiz do agregado. **Nada a corrigir na doutrina.**
- `infracore/` estende CA como *frameworks & drivers* e **por desenho não estende DDD** (allowlist de
  8 data classes). Conforme, não omissão — a doutrina precisa **dizer isso**, porque hoje o texto
  deixa o leitor esperar DDD onde ele não deve existir.
- `plugins/` estendem DDD na escrita (métodos do agregado) e **não na leitura**: 49 projeções
  `list[dict]` do agregado em 14 módulos; 5 de 15 plugins anotam a porta com `Protocol`.
- **A camada de casos de uso não tem artefato:** 0 classes `UseCase`; orquestração dispersa em 14
  ViewModels (5.216 linhas) e numa fachada de serviço (781 linhas, 18 métodos públicos).

Os três apontamentos de alta severidade emitidos pelo auditor foram **declinados pelo dono em
2026-08-07 quanto à ação na implementação de referência** — aquele projeto está quase finalizado e
não recebe investimento. O declínio recai sobre a ação lá, **não** sobre a medição: o achado
permanece válido como insumo da doutrina do hub, que é o que este plano escreve.

Resíduos de vocabulário de modalidade ainda no hub, medidos por Grep em 2026-08-07:
`ARQUITETURA_PANTONICA.md` §5 (linha do `TaskRunner`: "callbacks no UI thread"),
`.claude/skills/guardrails-check/SKILL.md:70` e `.claude/agents/pantonic-executor.md:15`.

## 3. Invariante de execução (vale para todas as tarefas)

1. **Contrato, nunca implementação.** Toda descrição de porta responde "o que qualquer implementação
   precisa garantir", e a implementação do case entra sempre nomeada como referência. Nenhum trecho
   pode nomear toolkit, plataforma ou modalidade como regra universal — a régua do estágio anterior
   (`DE-1`) continua valendo integralmente.
2. **Toda tarefa fecha verde.** Uma tarefa que invalide uma linha do `README.md` corrige essa linha
   no próprio escopo; o guarda não fica vermelho entre tarefas. Isso não autoriza varredura de prosa
   do README fora da `T8`.
3. **Redação.** `.claude/skills/redacao-doc/SKILL.md` é normativa em tudo que este plano manda
   escrever em documento publicado: nada de `V3` (id de plano, tarefa, estágio ou tíquete no corpo) e
   nada de `V7` (datação viva). O plano é registro e é isento; o que ele produz não é.
4. **Verificação de fechamento de toda tarefa** — os quatro em exit 0:
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate`,
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift`,
   `pwsh -NoProfile -File .claude/checks/check-readme.ps1`,
   `python -m pytest` na raiz do hub.

## 4. Tarefas

### T1 — `ARQUITETURA_PANTONICA.md` §4/§5: as oito portas de runtime do core [Opus]
- **Objetivo:** o core deixa de ser descrito por componentes concretos e passa a ser descrito por
  contrato de porta, com o componente do case como exemplo nomeado.
- **Arquivos-alvo:** `ARQUITETURA_PANTONICA.md` §4 (título e tabela de componentes, hoje ~linhas
  158-177), §5 (bloco "Portas genéricas (Protocols)…", hoje ~linhas 179-197), §2 (linha `infracore`
  da tabela de camadas, hoje ~linha 122).
- **Forma — esquema fixo, cinco campos por porta, nesta ordem:**
  1. **Responsabilidade** — uma frase.
  2. **Operações** — nomes e o que cada uma promete, em prosa; sem assinatura de linguagem.
  3. **Invariantes** — o que qualquer implementação garante (ex.: egress único, cache de valor,
     namespace de chave, ordem de boot).
  4. **Modos de falha** — o que acontece quando falha, coerente com a tabela de contenção (§11).
  5. **Implementação de referência** — uma linha, nomeando o componente do case.
- **Portas desta tarefa (8):** sinais, estado, filesystem, log, registro de plugins, injeção, raiz de
  dados (`paths`) e lifecycle de plugin (invocação segura de hooks). A **ordem de boot** permanece
  onde está, como invariante da porta de injeção.
- **Cuidado:** §5 deixa de repetir a lista de portas e passa a tratar só do pacote `contracts`
  (pacote instalável, versão própria, mirror dos tipos de manifest, `contracts/domain` como
  `[ESPECIALIZAR]`). As marcações `[REPLICAR]`/`[ESPECIALIZAR]` permanecem; a numeração não muda
  (`DI-8`).
- **Verificação:** bateria do §3; `Grep -iE "pyside|\bqt\b|mvvm|desktop"` em
  `ARQUITETURA_PANTONICA.md` sem ocorrência **nova** em relação ao baseline atual (as remanescentes
  são citação explícita do case de referência).
- **Pronto quando:** um projeto de outra stack consegue implementar as oito portas lendo apenas o §4
  — cada uma tem responsabilidade, operações, invariantes, modos de falha e um exemplo de referência,
  e nenhuma delas exige abrir o código da implementação de referência.

### T2 — A superfície de entrada e a execução assíncrona como portas [Opus]
- **Objetivo:** `DI-3` — as duas portas onde a modalidade encosta no core ficam descritas sem
  vocabulário de modalidade, e a implementação continua fora do hub.
- **Arquivos-alvo:** `ARQUITETURA_PANTONICA.md` §4 (entrada `ui_shell` da tabela), §5 (linha do
  `TaskRunner`, hoje ~linha 187: "callbacks no UI thread"), §11 (linha "Task em worker" da tabela de
  contenção), §14 (item 4 do checklist de bootstrap, hoje "UI shell mínima"), §3 (árvore de pastas,
  linha `ui_shell/`); `.claude/skills/guardrails-check/SKILL.md:70`;
  `.claude/agents/pantonic-executor.md:15`.
- **Conteúdo:**
  - **Superfície de entrada** — porta pela qual o mundo externo alcança o núcleo: expõe o estado do
    núcleo, recebe comandos, concentra os tokens de apresentação quando a modalidade tiver
    apresentação, e encerra o lifecycle. O core não conhece a tecnologia que a implementa; a
    implementação pertence à camada de modalidade, fora do hub.
  - **Execução assíncrona** — trabalho fora da thread que atende a superfície de entrada, com
    resultado e falha entregues de volta no **contexto de origem da chamada**. A expressão "UI
    thread" sai dos três artefatos; a regra "trabalho pesado nunca na thread que atende a superfície
    de entrada" continua afirmada nos três, com o vocabulário novo.
- **Cuidado:** a mudança é de vocabulário e de nível de descrição, não de regra; nada de ponteiro
  para `PantonicForDesktop/`, que está fora do versionamento e não pode ser destino de referência do
  hub.
- **Verificação:** `Grep -i "ui thread"` nos três arquivos → vazio; bateria do §3.
- **Pronto quando:** nenhum artefato do hub descreve concorrência ou superfície de entrada em termos
  de interface gráfica, e as duas portas têm o mesmo esquema de cinco campos da `T1`.

### T3 — `ARQUITETURA_PANTONICA.md`: a camada de casos de uso e a aderência medida [Opus]
- **Objetivo:** `DI-4` — dar residência e forma verificável ao artefato de aplicação, e trocar a
  declaração de aderência não medida pelo estado medido.
- **Arquivos-alvo:** `ARQUITETURA_PANTONICA.md` — subseção nova `### 9.1` dentro de §9; bloco
  **Manifest** de §9 (hoje ~linhas 270-273); bloco **Validação no load** de §9 (hoje ~linhas
  275-280); §3 (árvore de pastas, linha `plugins/<nome>/`); §1 (bloco "Grau de aderência da
  implementação atual: NÃO AUDITADO", hoje ~linhas 103-111); `docs/DOC_MAP.md` (só se o arquivo
  passar de 500 linhas ao fim desta tarefa — nesse caso, criar a entrada de âncoras).
- **Conteúdo de `### 9.1` — O caso de uso dentro do plugin:**
  - o caso de uso é o artefato de aplicação do plugin e mora em `plugins/<nome>/use_case.py`, numa
    classe `<Nome>UseCase` com um método público de execução;
  - depende **só** de `contracts` — portas e domínio —, recebidas por injeção; não importa a
    superfície de apresentação, nem serviço concreto, nem lib externa;
  - `plugin.py` e o adaptador de apresentação **apenas invocam**: nenhuma regra de negócio neles;
  - **exatamente um por plugin**; dois é decomposição errada, zero é caso de uso diluído no
    adaptador;
  - a POC preservada em `adhoc/` **não é** o caso de uso: o caso de uso a orquestra, e a POC continua
    intocada;
  - o TF do plugin exercita o caso de uso pela superfície dele, não pela apresentação — é isso que
    torna o teste independente da modalidade.
- **Manifest:** campo **`use_case`** obrigatório, com o nome que o dono reconhece (a mesma frase que
  o PRD usa para o objetivo do usuário), único na base de plugins. Entra na validação de load junto
  com os demais campos.
- **Bloco §1:** substituir a declaração "NÃO AUDITADO" pelo estado medido do §2 deste plano —
  domínio conforme; `infracore` conforme como *frameworks & drivers*, **sem** DDD por desenho;
  plugins conformes na escrita e não na leitura; camada de aplicação sem artefato, endereçada pela
  residência de §9.1. Evidência apontada como "relatórios de auditoria de arquitetura em
  `docs/audits/` do repositório da implementação de referência" — **sem** id de plano/tarefa e **sem**
  datação viva (`V3`/`V7`).
- **Verificação:** bateria do §3; `Grep -iE "não auditado|nao auditado"` em
  `ARQUITETURA_PANTONICA.md` → vazio; `Grep -E "P-07[0-9]{2}|V2[A-Z]-T"` no mesmo arquivo → vazio;
  contagem de linhas do arquivo conferida contra o gatilho de 500 do `DOC_MAP.md`.
- **Pronto quando:** a doutrina diz onde o caso de uso mora, de que depende, quem o invoca, como se
  declara e como se testa; e nenhuma afirmação de aderência não medida sobrou no documento.

### T4 — `GOVERNANCA.md` §2 e §5: o core por contrato e a aderência medida [Opus]
- **Objetivo:** alinhar a fonte da verdade de governança ao que a arquitetura passou a declarar, e
  fechar a segunda declaração de aderência não medida.
- **Arquivos-alvo:** `GOVERNANCA.md` §2 (bloco "Core comum e diversificação por camada", hoje ~linhas
  45-62), §5 (bloco final "Estado da aderência: não auditado", hoje ~linhas 393-397, e o corpo do
  fluxo de extensão, ~linhas 357-377).
- **Conteúdo:**
  - §2 — o bullet que declara a abstração das portas como "etapa própria e ainda não executada" é
    substituído: o core é definido por **portas**, o que todo projeto herda é o **contrato**, e a
    implementação de uma porta pertence à camada que declara a tecnologia. Na tabela de graus de
    especialização, a linha de infraestrutura passa a distinguir **porta** (idêntica entre todos os
    projetos) de **implementação** (idêntica entre projetos da mesma stack).
  - §5 — acrescentar a residência do caso de uso como **ponteiro** para a arquitetura §9.1, sem
    duplicar a regra (padrão `DR-A` de `docs/RESIDENCIA_DOUTRINA.md`); e substituir "Estado da
    aderência: não auditado" pelo estado medido, com a mesma evidência e as mesmas restrições de
    redação da `T3`.
- **Cuidado:** a ocorrência remanescente de `P-0730` no preâmbulo de §7 **não é desta tarefa** — é
  dívida registrada como `TK-17`. O executor não a toca e não para por causa dela.
- **Verificação:** bateria do §3; `Grep -iE "não auditado|nao auditado|ainda não executada"` em
  `GOVERNANCA.md` → vazio.
- **Pronto quando:** governança e arquitetura dizem a mesma coisa sobre o core, sem duplicar texto, e
  nenhuma das duas afirma aderência que não foi medida.

### T5 — Kit: a cadeia de auditoria ganha objeto verificável [Sonnet]
- **Objetivo:** `DI-5` — as verificações 8 e 9 do auditor deixam de ser inauditáveis.
- **Arquivos-alvo:** `.claude/skills/audit-sweep/SKILL.md` (bloco `DDD-usecase` da tabela do passo 2,
  hoje ~linha 33); `.claude/agents/pantonic-auditor-arch.md` (verificações 8 e 9, hoje ~linhas
  57-60).
- **Conteúdo:**
  - `DDD-usecase` passa a coletar três coisas por plugin: existência de `plugins/*/use_case.py`,
    `^class \w+UseCase` dentro dele, e o valor do campo `use_case` de `plugins/*/manifest.json`
    (ausente, vazio ou repetido entre plugins = divergência).
  - verificação 9 passa a ter critério objetivo: um módulo de caso de uso, uma classe, um campo
    declarado, nome único na base.
  - verificação 8 ganha a regra de dependência do caso de uso: o módulo não importa a superfície de
    apresentação, nem serviço concreto, nem lib externa — só `contracts`.
- **Fora de escopo:** nenhum verificador executável novo (`DI-6`); a régua de 12 verificações não
  ganha item novo.
- **Verificação:** bateria do §3 (o `kit_check.ps1 -Mode validate` cobre a contagem de agentes e
  skills).
- **Pronto quando:** a cadeia aplicada a um projeto sem artefato de caso de uso aponta o que falta,
  com localização exata; aplicada a um projeto conforme, não aponta nada.

### T6 — Kit: bootstrap e integração de POC produzem o caso de uso [Sonnet]
- **Objetivo:** o que a doutrina passou a exigir nasce por padrão em projeto novo e em POC
  integrada — regra sem produção correspondente vira aspiração.
- **Arquivos-alvo:** `.claude/skills/bootstrap-pantonic/SKILL.md` (fase 2 — o que é `[REPLICAR]`;
  fase 3 — Spec; fase 5 — árvore inicial; a ordem de implementação do core, hoje ~linhas 35-37);
  `.claude/skills/integrar-poc/SKILL.md` (o passo que disseca a POC nas camadas); `.claude/README.md`
  (regenerar se a descrição de alguma skill mudar).
- **Conteúdo:** a árvore inicial de um projeto novo mostra `plugins/<nome>/use_case.py` e o campo
  `use_case` do manifesto; o Spec passa a materializar o caso de uso como classe própria; a dissecção
  de POC declara o caso de uso como **artefato de saída obrigatório**, ao lado do inventário de
  dependências e do mapeamento para serviços.
- **Verificação:** bateria do §3.
- **Pronto quando:** um projeto criado pela skill nasce com a residência do caso de uso, e a
  integração de uma POC produz o caso de uso como artefato nomeado, não como consequência implícita.

### T7 — Rodada de revisão de guardrails aberta pelo plano anterior [Opus]
- **Objetivo:** `DI-7` — executar a porta de saída de `GOVERNANCA.md` §7.1 na primeira rodada do
  regime por fechamento de plano.
- **Arquivos-alvo:** `GOVERNANCA.md` §7.1, bloco **Registro das rodadas** (entrada nova, rótulo
  `P-0731 — <AAAA-MM-DD>`); `GOVERNANCA.md` §7 (marcação `OBSOLETA desde <rodada>` no item que ficar
  sem caso citável, **se** houver); `docs/DIARIO_DE_OBRAS.md` (resultado item a item).
- **Escopo da rodada:** as guardrails que já constavam de §7 na rodada anterior registrada
  (rotulada `1.4.0`) — na numeração de hoje, os itens **1 a 13**. O item **14 (G-README)** fica
  **fora por idade**. **Identificar cada guardrail pelo nome/conteúdo, nunca pelo número:** a
  numeração deslocou quando o guardrail de fronteira MVVM foi removido no estágio anterior.
- **Método:** coleta delegada ao `pantonic-scout` (um dossiê com os candidatos a caso citável no
  diário do hub, no `CHANGELOG.md` e no diário do consumidor `PantonicVideo`); julgamento em Opus.
  **Isenção por enforcement executável não é declarativa:** quem a invoca nomeia o check (caminho do
  teste ou comando do gate) e confirma que ele roda hoje.
- **Verificação:** bateria do §3; a entrada da rodada existe com resultado item a item.
- **Pronto quando:** a rodada está registrada. **Zero marcações é resultado legítimo; rodada não
  registrada não é.**

### T8 — `README.md`: o espelho segue a fonte [Opus]
- **Objetivo:** o contrato com o cliente descreve o core por portas e a camada de casos de uso com
  residência, sem contradizer nenhuma fonte.
- **Arquivos-alvo:** `README.md` — glossário (entradas "Infracore", "Core pantônico", "Caso de uso",
  "Plugin"); §2 (premissa 2 e a tabela de graus de especialização); §10 (contagem e lista de
  guardrails, **se** a `T7` marcar algum item); §1 no que a `T1`..`T4` tiverem alcançado.
- **Critério normativo:** `.claude/skills/redacao-doc/SKILL.md`; a varredura não pode reintroduzir os
  vícios já zerados.
- **Invariantes estruturais (o guarda ancora nelas — não renomear):** títulos `Anatomia do kit` e
  `Os guardrails`; a linha `> Fonte da verdade:` de toda seção; a numeração `## N.`; a tabela de
  skills com as skills do disco; a contagem de guardrails.
- **Verificação:** `pwsh -NoProfile -File .claude/checks/check-readme.ps1` em exit 0; bateria do §3;
  `Grep -iE "perfil|pyside|mvvm|\bqt\b|desktop"` no `README.md` → vazio (mantém o zero da rodada
  anterior).
- **Pronto quando:** o leitor entende, só pelo README, que o core é um conjunto de portas e que cada
  plugin carrega um caso de uso com residência própria — sem inferir qual aplicação consome o
  framework.

### T9 — `CHANGELOG.md` `[Não lançado]` e fechamento do registro [Sonnet]
- **Objetivo:** registrar a mudança canônica no único lugar vivo do histórico, sob congelamento.
- **Arquivos-alvo:** `CHANGELOG.md`, seção `[Não lançado]`; `docs/DIARIO_DE_OBRAS.md`.
- **Conteúdo:** um bloco consolidado, cobrindo as portas do core, a superfície de entrada e a
  execução assíncrona, a residência do caso de uso e o campo `use_case` do manifesto (com a nota de
  migração de manifesto existente), a cadeia de auditoria, o bootstrap/integração e a rodada de
  guardrails.
- **Proibido:** número de versão novo, seção numerada nova, tag, e qualquer instrução de migração
  expressa por número de versão (`DE-7`).
- **Verificação:** bateria do §3; `Grep -E "3\.0\.0|kit-v3|bump"` no `CHANGELOG.md` → vazio.
- **Pronto quando:** um adotante futuro lê `[Não lançado]` e sabe o que mudou e o que precisa migrar.

### T10 — Revisão do `README.md` e veredito do dono [dono]
- **Objetivo:** dever 2 de `G-README` — toda sprint encerra com a revisão do documento canônico, e o
  gate de sentido é do dono.
- **Forma, nesta ordem:**
  1. Rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1` — **paridade estrutural**
     (agentes, skills, versão, guardrails, `> Fonte da verdade:` por seção). O guarda é instrumento
     desta atividade, **nunca** gate automático de pronto.
  2. Leitura corrida do README pelo dono, respondendo: (a) o texto descreve o framework que ele
     governa? (b) alguma afirmação está equivocada, confusa ou desatualizada? (c) um cliente
     decidiria adotar — ou rejeitar — com base nisto, e a decisão seria justa?
- **Verificação:** veredito registrado no diário; reprovação gera rodada nova de redação, não segue
  adiante.
- **Pronto quando:** aceite explícito do dono registrado no diário. **Fecha o plano.**

## 5. Ordem de execução

`T1` → `T2` → `T3` → `T4` → `T5` → `T6` → `T7` → `T8` → `T9` → `T10` (dono).

Linear, sem ramo condicional. A infraestrutura vem antes da aplicação (`T1`/`T2` antes de `T3`)
porque a residência do caso de uso se define por **de que portas ele depende** — descrevê-la antes de
as portas existirem produziria retrabalho. A governança segue a arquitetura (`T4` depois de `T3`)
porque §5 vira ponteiro para §9.1, e ponteiro para seção inexistente é referência para frente. O kit
vem depois da doutrina (`T5`/`T6`) porque ferramenta que verifica regra não escrita mede ruído. A
rodada de guardrails (`T7`) precede o espelho (`T8`) porque pode alterar a contagem de guardrails do
`README.md`, que é um dos ancoradouros do guarda. O registro (`T9`) fecha antes do aceite (`T10`),
que é o gate de sentido e o encerramento.

`T1`, `T2`, `T3`, `T4`, `T7` e `T8` são Opus (doutrina e redação canônica); `T5`, `T6` e `T9` são
Sonnet; `T10` é do dono.

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Porta descrita em nível vago demais — "universal" virando genérico inútil | Esquema fixo de cinco campos por porta (`T1`), com o teste de aceitação declarado: outra stack implementa lendo só a seção, sem abrir o código do case |
| A descrição da superfície de entrada reintroduzir modalidade pela porta dos fundos | Grep de fechamento nos três artefatos + a régua do estágio anterior no invariante 1 do §3; a implementação continua fora do versionamento |
| Campo obrigatório no manifesto invalidar manifesto existente | Medido: 0/6 consumidores com kit instalado, versão congelada, nenhuma compatibilidade publicada a quebrar; nota de migração em `[Não lançado]` (`T9`) |
| Doutrina nova sem enforcement executável virar aspiração | O enforcement declarado é a cadeia de auditoria (`T5`) e o TF por caso de uso, que a doutrina já exige; o check executável tem gatilho registrado em §7, não fica esquecido |
| `ARQUITETURA_PANTONICA.md` passar de 500 linhas e virar doc sem porta de entrada | Passo explícito na `T3`: conferir a contagem e criar a entrada de âncoras no `docs/DOC_MAP.md` no mesmo ato |
| A rodada de guardrails errar o alvo por numeração deslocada | `T7` identifica guardrail por nome/conteúdo, nunca por número, e registra a rodada mesmo com zero marcações |
| Renumerar seções e quebrar referência cruzada silenciosamente | `DI-8`: nenhuma seção é renumerada; a camada de aplicação entra como `### 9.1` |

## 7. Fora de escopo (explícito)

- **Qualquer alteração no `PantonicVideo`.** O dono declinou investimento naquele projeto; os três
  apontamentos de alta severidade da auditoria não geram tíquete lá nem aqui. Este plano escreve
  doutrina do hub.
- **Verificador executável novo** (`DI-6`), com gatilho registrado: quando existir projeto que
  materialize o kit, o check de manifesto/caso de uso entra por plano próprio.
- **Guardrail novo em §7** (`DI-5`).
- **Bump, tag e instrução de migração por número de versão** (`DE-7` do plano anterior).
- **Tíquetes de backlog que não pertencem a este assunto** e continuam precisando de tarefa própria:
  `TK-15` (a classe "Seção histórica declarada" sai da skill `redacao-doc`), `TK-17` (`V3`/`V7` no
  restante da `GOVERNANCA.md`), `TK-10` (condensação do diário), `TK-04`, `TK-06`, `TK-07`, `TK-08`.

## 8. Achados abertos deste planejamento

- **`TK-18`** — `docs/DIARIO_DE_OBRAS.md` linha de índice da sprint descreve a iniciativa como "4
  estágios encadeados"; ela está no sétimo. Correção trivial, sem relação com este assunto — cabe na
  próxima condensação (`TK-10`).

## Achados da execução

*(preenchido pelos executores)*
