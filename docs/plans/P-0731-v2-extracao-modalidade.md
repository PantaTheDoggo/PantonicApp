# P-0731 — Estágio 6: extração da camada de modalidade e o hub como núcleo universal

- **Origem:** 2026-08-06 — veredito da 2ª rodada de aceite do README (`V2I-T12`)
- **Iniciativa:** `PANTONIC-V2` · **Estágio:** 6 (corretivo) · **Prefixo de tarefa:** `V2E-`
- **Fecha em:** **congelamento do número em `0.0.0`** (`DE-7`) — o framework nunca foi lançado, a
  numeração não tem valor antes do lançamento, e o número só volta a andar quando o dono publicar
- **Substitui:** `docs/plans/P-0730-v2-identidade.md` (classificação **B**)
- **Checagem de versão do kit:** modo hub — `VERSION` `2.0.0` == `.claude/KIT_VERSION` `2.0.0` ==
  maior tag publicada `kit-v2.0.0`. Paridade OK, sem divergência; a "republicação pendente" anotada
  no `P-0730` está resolvida.

## 0. O problema real deste estágio

O `P-0730` corrigiu a identidade do framework de "desktop com stack fixo PySide6" para "agnóstico a
tecnologia e plataforma". A correção foi feita por **quarentena**: a `DR-2` criou o conceito de
**perfil** — o núcleo fica universal, e o que é específico de uma modalidade (desktop, container,
web) passa a viver num perfil declarado pelo projeto, com verificações que só quem declara paga.

A quarentena não resolve o problema; ela o move. O hub continua contendo o conhecimento do
consumidor, agora rotulado. E isso inverte a relação entre as camadas:

> Um framework de aplicação desktop contém **todo** o conhecimento do PantonicApp e o estende com
> MVVM, Qt, threading de UI e empacotamento. A dependência tem um sentido só: a camada de cima
> conhece a de baixo, e a de baixo **não sabe nada sobre quem a usa**.

Enquanto o hub descreve `desktop-pyside6` — inclusive como *default na ausência de declaração* — ele
sabe quem o usa. A `DR-2` cai. O perfil não é uma abstração do núcleo: é o nome que o núcleo dava
para o seu próprio vazamento.

## 1. Decisões (fechadas no ato do planejamento)

| id | Decisão | Origem |
|---|---|---|
| `DE-1` | O conceito de **perfil** sai do hub inteiro. Modalidade de aplicação não é dimensão do núcleo; é a camada acima. Nenhuma marcação `*[perfil ...]*`, nenhum arquivo `.claude/PERFIL`, nenhum default. | dono, 2026-08-06 |
| `DE-2` | O conhecimento desktop/PySide6/MVVM/Qt migra para `PantonicForDesktop/` — pasta no `.gitignore`, embrião do repositório próprio dessa ramificação. Não é tratada neste projeto; o dever aqui é **não perder o conhecimento**. | dono, 2026-08-06 |
| `DE-3` | O conhecimento de container recebe o mesmo tratamento em `PantonicForContainer/`. Dockerfile e 12-factor são tecnologia pela mesma régua que Qt é; manter um e extrair o outro reintroduz a assimetria que a `DE-1` elimina. | dono, 2026-08-06 |
| ~~`DE-4`~~ | ~~Fechamento em **`3.0.0`**. Remover o conceito de perfil e um guardrail quebra compatibilidade de doutrina com os consumidores — é MAJOR pela régua de semver do próprio framework.~~ **Revogada pela `DE-7`** (dono, 2026-08-07): o framework nunca foi lançado, logo não há compatibilidade publicada a quebrar e não há MAJOR a fechar. O diagnóstico permanece correto — as três quebras existem —, o que cai é o número que as carimbava. | dono, 2026-08-06 |
| `DE-5` | `dead_code.py` troca as duas constantes de Qt por um **ponto de extensão declarativo**: arquivo opcional `.claude/framework-virtuals.txt` do projeto, com as seções `[bases]` (nomes de classe-base cujo framework despacha métodos) e `[metodos]` (nomes de virtuais despachadas). Ausente ⇒ ambas vazias ⇒ zero conhecimento de framework no hub. | planejamento, 2026-08-06 |
| `DE-6` | Este plano toma o id `P-0731`. A abstração do infracore, que a `V2I-T15` reservava para esse id, passa a **`P-0732`** e tem o escopo corrigido pela `DE-1` (o binding Qt não vira "uma implementação de perfil entre outras" — sai do hub). | planejamento, 2026-08-06 |
| `DE-7` | **A versão congela em `0.0.0`; o que já foi numerado permanece como histórico pré-lançamento.** O número fica como artefato, parado em `0.0.0` até o dono decidir publicar: enquanto durar o congelamento não há bump, não há tag nova e a comparação local × remoto da checagem de versão fica **suspensa**. As entradas `1.0.0`..`2.0.0` do `CHANGELOG.md` e as **8 tags `kit-v*` já publicadas** (`kit-v1.0.0`, `1.0.1`, `1.1.0`, `1.2.0`, `1.3.0`, `1.4.0`, `1.5.0`, `2.0.0`) **não são apagadas nem reescritas** — passam a ser declaradas como histórico de desenvolvimento pré-lançamento, e a seção `[Não lançado]` do `CHANGELOG.md` vira a única seção viva, onde toda mudança canônica continua obrigatoriamente registrada. | dono (congelar em `0.0.0`), 2026-08-07 + planejamento (destino do que já foi numerado), 2026-08-07 |
| `DE-8` | **O gatilho da porta de saída de guardrail (`GOVERNANCA.md` §7.1) passa a pender do fechamento de um plano** — a linha do plano indo a `done` no índice de `docs/DIARIO_DE_OBRAS.md` —, não mais do fechamento de um MINOR do kit. Resolve o `TK-16`: com o número congelado nenhum MINOR fecha, e a única forma legítima de remover um guardrail deixaria de existir. Preserva a intenção original — revisão atrelada a **marco real de evolução**, nunca a calendário — apoiada num evento que já existe, já é registrado no índice do diário e teve historicamente a mesma cadência dos MINORs. Consequência interna à §7.1: escopo, janela da pergunta e período de transição passam a ser contados em **rodadas**, não em MINORs. | dono, 2026-08-07 |

**Trade-off da `DE-7`,** explícito porque a decisão tem custo real. *Alternativa rejeitada:* apagar
as 8 tags do remoto e reescrever o `CHANGELOG.md` como se a numeração nunca tivesse existido —
recusada por duas razões independentes: publicar e despublicar tag é ato do dono, nunca de agente
(`GOVERNANCA.md` §10, `README.md` §13), e registro de trabalho feito não se reescreve. *O que se
perde:* o número deixa de ser contrato de compatibilidade — ninguém pode mais dizer "estou na
`1.5.0`" e derivar o que tem; deriva entre hub e consumidor deixa de ser detectável por comparação
de versão e passa a depender de `kit_check.ps1 -Mode check-drift` rodado no consumidor; e o
`CHANGELOG.md` fica com uma seção viva permanente em vez de fatias fechadas por número. *O que se
ganha:* nada de histórico é apagado, nenhuma tag publicada precisa ser tocada, e `0.0.0` é
exatamente o que a régua semver reserva para desenvolvimento inicial — o artefato passa a dizer a
verdade sobre o estado do framework em vez de simular maturidade que ele não tem. *Por que o custo
é aceitável, medido:* `docs/CONSUMIDORES.md` registra **0/6 consumidores com `.claude/kit/`
instalado** — nenhuma instalação por subtree existe hoje, logo nenhum consumidor real depende da
numeração como contrato, e o custo é potencial enquanto o ganho é imediato.

**Trade-off da `DE-8`.** *Opções recusadas pelo dono:* **(a) cadência por contagem de tarefas
concluídas** — recusada porque contagem de tarefas mede volume, não marco: tarefas variam de peso,
o número seria arbitrário e exigiria um contador que não existe, enquanto a §7.1 exige o momento em
que **há material novo para julgar**; **(b) suspender a revisão até o lançamento** — recusada
porque é exatamente o apodrecimento que a §7.1 existe para impedir, e o congelamento não tem data
para acabar (é decisão do dono, sem prazo): durante ele o framework só adicionaria regra. *O que se
perde:* a cadência deixa de ter escala numérica objetiva — "idade de guardrail" passa a ser contada
em rodadas, o que só funciona se **cada rodada registrar o que avaliou**, disciplina de registro
maior do que a de hoje; e um plano longo espaça as rodadas mais do que um MINOR espaçava. *O que se
ganha:* a porta de saída volta a poder disparar sem depender de um número que não anda, e o evento
que a dispara já é registrado — nenhum artefato novo precisa existir.

**Régua única deste estágio,** aplicada a todo trecho candidato: *o hub pode afirmar isto sem saber
qual aplicação o consome?* Não ⇒ migra. A régua não distingue prosa de código executável.

## 2. Alcance medido (insumo das tarefas — nada inferido na execução)

Varredura de `perfil|PySide|MVVM|Qt|desktop` em 2026-08-06:

| Alvo | Ocorrências | Peso |
|---|---|---|
| `ARQUITETURA_PANTONICA.md` | 31 | §10 inteira ("MVVM e PySide6"), convenção de perfil no topo, árvore de diretórios, allowlist de imports, sequência de bootstrap, harness de teste, §12 |
| `GOVERNANCA.md` | 20 | §1.1 inteira (perfis), §7 item 3 (guardrail MVVM), §1, §3 |
| `README.md` | ~15 | glossário, §1, §2 (subseção "Perfis"), §10, §11, §15 |
| `.claude/skills/` | 6 skills | `guardrails-check`, `bootstrap-pantonic`, `integrar-poc`, `audit-sweep`, `redacao-doc`, `proximo-passo` |
| `.claude/agents/` | 2 agentes | `pantonic-auditor-arch` (verificação 11), `pantonic-executor` |
| `.claude/checks/dead_code.py` | 8 trechos | `_QT_VIRTUAL_METHODS` + heurística de classe Qt-derivada — **verificador executável, não prosa** |

Já executado fora de tarefa, na rodada de aceite: `PantonicForDesktop/` criada e ignorada,
`pantonic-auditor-pyside6.md` migrado, linha do agente removida do README, índice `.claude/README.md`
regenerado, inventário ancorado escrito em `PantonicForDesktop/README.md`. Guardas em exit 0.

## 3. Invariante de execução (vale para todas as tarefas)

1. **Migrar é um ato só.** Remover do hub sem preservar perde conhecimento; preservar sem remover
   deixa a inversão de dependência de pé. Toda remoção grava o trecho em
   `PantonicForDesktop/doutrina/` (ou `PantonicForContainer/doutrina/`) **no mesmo commit**.
2. **Toda tarefa fecha verde.** Uma tarefa que invalida uma linha do README corrige essa linha no
   próprio escopo — `check-readme.ps1` não fica vermelho entre tarefas. Isso não autoriza a
   varredura de prosa do README fora da `T6`: corrige-se o que a própria tarefa quebrou, nada mais.
3. **Verificação de fechamento de toda tarefa:** `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate`,
   `-Mode check-drift` e `pwsh -NoProfile -File .claude/checks/check-readme.ps1`, os três em exit 0.
   **A partir da `T5a`** a bateria ganha um quarto passo — `python -m pytest` na raiz do hub, também
   em exit 0 (decisão do dono, 2026-08-06, ao partir a `T5`: os verificadores executáveis que o hub
   distribui passam a ter prova comportamental trancada, em vez de nenhuma).

## 4. Tarefas

### T1 — `PantonicForContainer`: embrião e migração do auditor de container [Sonnet]
- **Objetivo:** `DE-3` — espelhar para container o que já foi feito para desktop.
- **Arquivos-alvo:** `PantonicForContainer/` (novo, com `README.md` e `.claude/agents/`);
  `.gitignore`; `.claude/agents/pantonic-auditor-container.md` (sai do índice do git);
  `README.md` §11 (linha do agente e a contagem "oito agentes" → sete); `.claude/README.md`
  (regenerado, nunca editado à mão).
- **Conteúdo do `README.md` da pasta nova:** mesma forma do `PantonicForDesktop/README.md` — por que
  a separação existe, o que já está lá, o que ainda falta migrar.
- **Verificação:** `git status --short` mostra a deleção do agente no índice e nenhum arquivo novo
  rastreado; a bateria do §3.
- **Pronto quando:** o kit tem sete agentes, todos universais, e o conhecimento de container está
  preservado fora do versionamento.

### T2 — `GOVERNANCA.md`: remover os perfis e o guardrail de MVVM [Opus]
- **Objetivo:** `DE-1` — tirar da fonte da verdade de governança a dimensão de modalidade.
- **Arquivos-alvo:** `GOVERNANCA.md` §1.1 (seção inteira), §1 (linha de modalidades cobertas), §3
  (linha da matriz de auditoria que cita "o perfil declarado acrescenta o seu auditor"), §7 item 3
  (guardrail MVVM) e a renumeração dos itens 4..15 → 3..14; `README.md` §10 (linha 3 da tabela e a
  contagem no texto de abertura, "Quinze regras" → "Quatorze"; as duas frases de rodapé que contam
  as formas de enforcement); `PantonicForDesktop/doutrina/` (texto extraído).
- **Cuidado de renumeração:** o guarda `check-readme.ps1` compara a contagem de linhas `| N |` da
  seção "Os guardrails" com os itens `^\d+\. \*\*` de `GOVERNANCA.md` §7 — as duas contagens caem
  para 14 juntas. Grep por referências cruzadas a "item <N>" (`.claude/`, `docs/`, `README.md`,
  `ARQUITETURA_PANTONICA.md`) **antes** de renumerar; os guardrails nomeados (`G-DEADCODE`,
  `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY`, `G-EXECREADY`, `G-README`) são referenciados por
  nome e não mudam.
- **Verificação:** bateria do §3; Grep por `perfil|PERFIL` em `GOVERNANCA.md` retorna vazio.
- **Pronto quando:** a governança não nomeia modalidade nenhuma e as duas contagens de guardrail
  batem em 14.

### T3 — `ARQUITETURA_PANTONICA.md`: remover a §10 e as marcações de perfil [Opus]
- **Objetivo:** `DE-1` na fonte da verdade de arquitetura — o alvo mais pesado do estágio.
- **Arquivos-alvo:** `ARQUITETURA_PANTONICA.md` — §10 inteira ("MVVM e PySide6"), a convenção de
  perfil do topo (linhas 12-18), a árvore de diretórios (`infracore/ui_shell/`, `view_model.py`), a
  tabela de camadas (PySide6 na allowlist de `infracore` e `plugins`), a superfície de entrada
  `ui_shell`, a sequência de bootstrap, a allowlist de imports por AST, o harness `pytest-qt` da
  estratégia de teste, e a §12 (shell Qt e primitivas de thread como não-núcleo);
  `PantonicForDesktop/doutrina/` (texto extraído, §10 na íntegra).
- **Ponto de atenção:** a §10 é referenciada de fora (o agente de execução e o auditor de
  arquitetura citam "ARQUITETURA_PANTONICA.md §10"). A renumeração das seções seguintes, se houver,
  exige a mesma varredura de referências cruzadas da `T2`. O que **permanece** é a camada de
  apresentação como conceito abstrato: o núcleo tem uma superfície de entrada, e nomear qual é ela
  é do projeto.
- **Verificação:** bateria do §3; Grep por `PySide|Qt|MVVM|perfil` em `ARQUITETURA_PANTONICA.md`
  retorna vazio.
- **Pronto quando:** o documento de arquitetura descreve camadas, domínio e extensão sem nomear
  framework de interface nenhum.

### T4 — Kit: skills e agentes sem perfil nem Qt [Sonnet]
- **Objetivo:** `DE-1` no pacote distribuído — é ele que chega aos consumidores.
- **Arquivos-alvo:** `.claude/skills/guardrails-check/SKILL.md` (descrição no frontmatter, item de
  dead code, checklist de ViewModel/Model); `.claude/skills/bootstrap-pantonic/SKILL.md` (pergunta
  de perfil, `.claude/PERFIL`, herança de View/ViewModel, critério de pronto);
  `.claude/skills/integrar-poc/SKILL.md` (dissecação da camada de UI, allowlist);
  `.claude/skills/audit-sweep/SKILL.md` (blocos `ARCH-mvvm` e `PYSIDE`, imports de PySide6 na
  varredura de pureza de domínio); `.claude/skills/redacao-doc/SKILL.md` (o exemplo ✓/✗ cita perfil
  — trocar por exemplo de mesma força sem tecnologia);
  `.claude/skills/proximo-passo/SKILL.md` (agrupamento "por perfil");
  `.claude/agents/pantonic-auditor-arch.md` (verificação 11 — fronteira MVVM — e a menção a Qt na
  verificação de pureza de domínio); `.claude/agents/pantonic-executor.md` (regra de MVVM);
  `.claude/README.md` (regenerado); `PantonicForDesktop/` (trechos extraídos).
- **Cuidado:** `pantonic-auditor-arch` verifica pureza de domínio citando "ORM, HTTP client, logging
  de infra, Qt" — a lista é universal **menos** o último item; remover só ele, não a verificação.
- **Verificação:** bateria do §3; Grep por `perfil|PySide|MVVM|Qt` em `.claude/skills/` e
  `.claude/agents/` retorna vazio.
- **Pronto quando:** nenhum artefato distribuível nomeia modalidade ou framework de interface.

> **`T5` partida em `T5a`/`T5b` (orquestrador + decisão do dono, 2026-08-06).** O gate
> `G-PLANREADY` reprovou a `T5` original: o dossiê prescrevia "`tests/` do hub (teste novo)" e
> verificação por "suíte de testes do hub", mas o hub **não tem suíte** — medido no pickup:
> nenhum `tests/`, nenhum `test_*.py` rastreado, nenhum arquivo de configuração de pytest, e
> `python -m pytest --collect-only` em **exit 5 ("no tests collected")**; as convenções `tests/`
> da `GOVERNANCA.md` §4.4 são das aplicações consumidoras, não do hub. Onde a prova comportamental
> passa a morar é decisão de arquitetura de verificação, não do executor (Regra 8). O dono decidiu
> pela suíte própria: a `T5a` cria a infraestrutura e ancora o comportamento vigente, a `T5b` faz a
> troca do mecanismo com TF/TR de verdade. O somatório das duas é exatamente a `T5` original.

### T5a — suíte de testes do hub: infraestrutura mínima e âncora do comportamento vigente [Sonnet]
- **Objetivo:** dar ao hub o lugar onde a prova comportamental dos verificadores executáveis que ele
  distribui passa a morar, e trancar o comportamento **atual** de `dead_code.py` quanto às virtuais
  de framework — é esse teste que vira o TR da `T5b`.
- **Arquivos-alvo:**
  - `pytest.ini` na raiz (novo, mínimo: `[pytest]` com `testpaths = tests`). O hub não é um pacote
    Python e não vira um: nada de `pyproject.toml`, nada de `setup.py`, nada de `__init__.py`.
  - `tests/fixtures/qt_project/` (novo) — projeto-fixture mínimo em Python puro, **sem importar
    PySide6** (as classes Qt são só nomes de base no AST; o verificador nunca executa o código
    varrido): pelo menos um módulo com (a) uma classe cuja base casa `^Q[A-Z]` e um override de
    virtual canônica (ex.: `data`, `paint`) sem nenhum chamador explícito, e (b) uma função ou
    método de produção órfão que **deve** ser acusado, para o teste distinguir "não acusa" de "não
    varreu nada".
  - `tests/test_dead_code.py` (novo) — os testes.
- **Como o teste chama o verificador:** carregar `.claude/checks/dead_code.py` por caminho
  (`importlib.util.spec_from_file_location`) e chamar `check(Path(<fixture>))`, que devolve a lista
  de linhas de achado — asserção sobre a lista, não sobre stdout. `.claude/checks/` não é pacote
  importável e o diretório tem ponto no nome; `import` normal não resolve. A CLI (`main(argv) -> int`,
  exit 0 sem achado) fica fora do escopo do teste.
- **Testes (comportamento vigente, antes da `T5b`):** (1) o override da virtual na classe Qt-derivada
  do fixture **não** aparece nos achados; (2) o símbolo órfão do mesmo fixture **aparece**.
- **Cuidado:** `EXCLUDED_DIR_NAMES` de `dead_code.py` inclui `"tests"`, e o caminho é relativo à
  `--root` passada — o fixture varrido com `root=tests/fixtures/qt_project` é enxergado
  normalmente, e a varredura do hub inteiro (`--root .`) continua ignorando `tests/`. Nenhuma das
  duas coisas precisa mudar.
- **Fora do escopo:** `.claude/checks/dead_code.py` não é tocado nesta tarefa — a mudança de
  mecanismo é da `T5b`.
- **Verificação:** `python -m pytest` na raiz com os dois testes passando e nenhum `skip`/`xfail`;
  `python .claude/checks/dead_code.py --root .` continua em exit 0; bateria do §3 (já com o quarto
  passo).
- **Pronto quando:** o hub tem suíte própria executável por um comando, ela tranca o comportamento
  que a `T5b` vai mexer, e a bateria de fechamento do §3 roda os quatro passos em exit 0.

### T5b — `dead_code.py`: ponto de extensão para virtuais despachadas por framework [Sonnet]
- **Objetivo:** `DE-5` — tirar Qt do único verificador executável que o conhece, **sem** cegar os
  consumidores que dependem dele hoje.
- **Contexto:** `_QT_VIRTUAL_METHODS` existe porque `paint`, `columnCount`, `headerData` e
  companhia são invocadas pelo framework, nunca por chamada explícita em Python; sem a tabela, o
  verificador acusa código morto onde não há. A regra atual só dispara quando (a) a classe tem base
  Qt **e** (b) o nome bate na tabela — as duas metades são conhecimento de framework.
- **Arquivos-alvo:** `.claude/checks/dead_code.py` (constante `_QT_VIRTUAL_METHODS` e a heurística
  de classe Qt-derivada, incluindo a travessia de herança entre arquivos); `tests/test_dead_code.py`
  e `tests/fixtures/` (suíte criada pela `T5a`, estendida aqui);
  `PantonicForDesktop/.claude/framework-virtuals.txt` (a tabela de Qt, já no formato final,
  pronta para os consumidores desktop copiarem).
- **Forma:** `.claude/framework-virtuals.txt` opcional na raiz do projeto, seções `[bases]` e
  `[metodos]`, um nome por linha, `#` comenta. Arquivo ausente ⇒ listas vazias ⇒ nenhuma exceção
  concedida. O parser é do hub; o conteúdo é do projeto.
- **Testes:** TF — projeto com o arquivo declarando base e método não acusa código morto no override
  correspondente; TR — projeto **sem** o arquivo mantém o comportamento atual em todo o resto da
  suíte de dead code.
- **Verificação:** `python .claude/checks/dead_code.py --root .` em exit 0; `python -m pytest` verde
  (o teste da `T5a` que ancora "não acusa o override" continua passando **por outro mecanismo** —
  agora por declaração no `framework-virtuals.txt` do fixture, não pela tabela embutida); bateria
  do §3.
- **Pronto quando:** `Grep -i "qt" .claude/checks/dead_code.py` retorna vazio e a exceção continua
  concedível por declaração do projeto.

### T6 — README: varredura final de perfil e tecnologia [Opus]
- **Objetivo:** o contrato com o cliente descreve o núcleo universal e nada além.
- **Arquivos-alvo:** `README.md` — entrada "Perfil" do glossário; §1 (as modalidades cobertas e a
  frase sobre o que muda entre elas); §2 (subseção "Perfis: o que a modalidade acrescenta" inteira,
  a linha "mesmo perfil" da tabela de especialização, e o parágrafo do case de referência que
  autoriza citar Qt/MVVM/PySide6 como default do case); §10, §11 e §15 no que as tarefas anteriores
  não tiverem alcançado.
- **Critério normativo:** `.claude/skills/redacao-doc/SKILL.md` continua valendo — a remoção não
  pode reintroduzir os vícios `V1..V8` já zerados pela `V2I-T11c`.
- **Invariantes estruturais (o guarda ancora nelas — não renomear):** títulos `Anatomia do kit` e
  `Os guardrails`; a linha `> Fonte da verdade:` de toda seção numerada; a numeração `## N.`; a
  tabela de skills com as 10 skills do disco; a contagem de guardrails, agora **14**.
- **Verificação:** bateria do §3; Grep por `perfil|PySide|MVVM|Qt|desktop` no README retorna vazio.
- **Pronto quando:** o README não permite ao leitor inferir qual aplicação consome o framework.

### T7 — Dever 2 do G-README como responsabilidade do planejador [Opus]
- **Objetivo:** absorve a `V2I-T16`, cujo escopo a `DE-1` não altera. Dar residência de
  **responsabilidade de papel** ao dever que hoje só existe como texto.
- **Arquivos-alvo:** `GOVERNANCA.md` §3 (matriz de responsabilidades — linha canônica do
  planejador); `.claude/agents/pantonic-planner.md` (ponteiro para §3, sem duplicata plena — padrão
  `DR-A` de `docs/RESIDENCIA_DOUTRINA.md`).
- **Fora de escopo, explicitamente:** a skill `handover` não se toca (gate mecânico rejeitado pelo
  dono em 2026-08-05); `check-readme.ps1` não se apaga.
- **Conteúdo:** ao encerrar qualquer sprint, o planejador autora uma tarefa nomeada de revisão do
  README, cujo dossiê inclui rodar o guarda e colher o veredito do dono. Sprint sem essa tarefa é
  plano incompleto (G-PLANREADY).
- **Verificação:** Grep pela linha do planejador em `GOVERNANCA.md` §3 e pelo ponteiro no arquivo do
  agente; bateria do §3.
- **Pronto quando:** a responsabilidade está declarada em um só lugar canônico e nenhum gate
  automático foi criado.

### T8 — 3ª rodada de aceite do README pelo dono [dono]
- **Objetivo:** absorve a `V2I-T12`. O gate de sentido que nenhum script cobre.
- **Forma:** leitura corrida do README pelo dono, respondendo: (a) o texto descreve o framework que
  ele governa? (b) alguma afirmação está equivocada, confusa ou desatualizada? (c) um cliente
  decidiria adotar — ou rejeitar — com base nisto, e a decisão seria justa?
- **Histórico do gate:** 1ª rodada reprovou por legibilidade (narrativa de proveniência → skill
  `redacao-doc`); 2ª rodada reprovou por identidade (perfil e tecnologia no núcleo → este plano).
- **Verificação:** veredito registrado no diário; reprovação gera rodada nova de redação, não segue
  adiante.
- **Pronto quando:** aceite explícito do dono registrado. **Bloqueia a `T9`.**

### T9 — congelar a versão em `0.0.0` (partida em `T9a`..`T9e`)

Dossiê reescrito em 2026-08-07 pelo planejador. O dossiê original ("Fechar `3.0.0` e distribuir",
`CHANGELOG.md` §3.0.0, tag `kit-v3.0.0`) caiu junto com a `DE-4`: sem lançamento não há
compatibilidade publicada a quebrar nem MAJOR a fechar. O objeto da tarefa passa a ser o
**congelamento** (`DE-7`) — o número para em `0.0.0` e todas as superfícies que dependem dele são
reconciliadas. A reescrita achou uma superfície que o `TK-14` não listava: a porta de saída de
guardrail (`GOVERNANCA.md` §7.1) pendurava seu gatilho no fechamento de um MINOR e ficaria sem
disparo nenhum sob número congelado. O dono decidiu no mesmo dia (`DE-8`) — o gatilho passa a
pender do fechamento de um plano —, e a mudança entra aqui porque é a mesma superfície de
doutrina, no mesmo par de arquivos, na mesma janela.

**Por que cinco fatias.** O alcance medido em 2026-08-07 é de ~23 blocos de edição contíguos
(`VERSION` 1, `.claude/KIT_VERSION` 1, `CHANGELOG.md` 3, `README.md` 6, `GOVERNANCA.md` §10 5,
`GOVERNANCA.md` §7.1 6, `.claude/skills/checar-versao-kit/SKILL.md` 6, `docs/CONSUMIDORES.md` 1),
quase o triplo do teto de 8 write-clusters do gate de delegação
(`.claude/skills/proximo-passo/SKILL.md`, gate item 5). O corte é por **regime de dependência**, não
por tamanho: nenhuma fronteira entre fatias pode deixar o framework funcionalmente quebrado. Daí a
ordem `T9a` → `T9b` → `T9c` → `T9d` → `T9e` — as duas doutrinas afetadas pelo congelamento são
escritas primeiro (§10, o número; §7.1, o gatilho da porta de saída, que pendia do fechamento de
MINOR e passa a pender do fechamento de plano pela `DE-8`), o mecanismo executável passa a
operacionalizar as duas **antes** de o número mudar (senão a primeira criação de plano após o
congelamento compararia `0.0.0` com a tag `kit-v2.0.0`, divergência de MAJOR, e a skill reportaria
"incompatível e para"), o número muda, e o espelho segue a fonte. O somatório das cinco é
exatamente a `T9`.

**Fato medido, insumo comum às quatro (2026-08-07 — não re-derivar):** `VERSION` = `2.0.0` e
`.claude/KIT_VERSION` = `2.0.0` (paridade OK); 8 tags publicadas (`kit-v1.0.0`, `1.0.1`, `1.1.0`,
`1.2.0`, `1.3.0`, `1.4.0`, `1.5.0`, `2.0.0`); `CHANGELOG.md` em 213 linhas, com `## [Não lançado]`
na L82 — **abaixo** de `## 2.0.0` (L11), anomalia física a corrigir na `T9d`; `README.md` em 898
linhas, §13 na L825 e §14 na L881; `GOVERNANCA.md` em 702 linhas, §9 na L608 e §10 na L642;
`docs/CONSUMIDORES.md` registra 0/6 consumidores com `.claude/kit/` instalado.

**Âncoras de linha, regra de uso.** Todo número de linha citado nas quatro fatias foi medido em
2026-08-07, **antes** de qualquer edição da `T9`. Dentro de uma fatia, a primeira inserção desloca
todas as âncoras seguintes do mesmo arquivo: aplicar as edições **de baixo para cima** no arquivo,
ou localizar por âncora de conteúdo (a frase inicial do parágrafo, citada em cada item). Número de
linha aqui é ponteiro de navegação, nunca identidade do trecho.

**Bateria de fechamento das quatro fatias** (invariante 3 do §3, comandos colados):

```
pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate
pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
pwsh -NoProfile -File .claude/checks/check-readme.ps1
python -m pytest
```

### T9a — `GOVERNANCA.md` §10: a doutrina do congelamento [Opus]
- **Objetivo:** `DE-7` na fonte da verdade. A doutrina passa a autorizar e descrever o número
  congelado antes que qualquer artefato o carregue.
- **Arquivos-alvo:** `GOVERNANCA.md` — **só** a §10 "Versionamento e atualização do kit"
  (L642-702). A §7.1 é da `T9b`; nenhum outro arquivo entra.
- **Conteúdo prescrito:**
  1. **Bloco novo, primeiro do §10** (logo após o parágrafo de abertura L644-645), sob rótulo
     **"Congelamento pré-lançamento"**: o framework não foi lançado, a versão é `0.0.0` e não anda
     até o dono decidir publicar. Enquanto congelada — (i) **não há bump**: a regra "os três se
     movem juntos" reduz-se a **um**, a linha no `CHANGELOG.md`; (ii) o hub **não publica tag
     nova**; (iii) a checagem de versão **não compara e não toca a rede**; (iv) as tags `kit-v*` e
     as seções numeradas do `CHANGELOG.md` já existentes **permanecem** como histórico de
     desenvolvimento pré-lançamento, não são revogadas nem reescritas; (v) **descongelar é ato do
     dono**, e reativa o mecanismo completo descrito no resto da seção.
  2. **Parágrafo "Mecanismo"** (L657-664): a residência do `.claude/KIT_VERSION` e a razão dela
     ficam intactas; a frase da tag passa a valer **após o lançamento**, e a frase da chamada de
     rede declara-se suspensa enquanto congelada.
  3. **"Os três resultados possíveis da checagem"** (L666-677): o rótulo perde o numeral — a lista
     tem **quatro** bullets hoje, e ganha um quinto. O bullet novo entra **primeiro**: *versão
     congelada (`0.0.0`) → reporta "congelada — nada a comparar" e encerra, sem chamada de rede*.
     Os quatro existentes descrevem o mecanismo pós-lançamento e permanecem com o texto atual.
  4. **"Critério de pronto"** (L685-687): passa a valer nos dois regimes — congelada, o critério é
     a linha no `CHANGELOG.md` sob `[Não lançado]`; descongelada, volta a ser o bump. A razão
     ("versão que não sobe deixa a checagem cega") permanece, agora atribuída ao regime numerado.
  5. **"Paridade `VERSION` × `.claude/KIT_VERSION`"** (L689-696): a paridade continua exigida sem
     exceção (os dois carregam `0.0.0`); os significados de MAJOR/MINOR/PATCH continuam declarados,
     operantes a partir do lançamento; "os três se movem juntos" ganha a ressalva do congelamento.
- **Fronteiras:** §9 (L608-640) **não é alvo** — ela aponta para §10 sem afirmar número, e o
  ponteiro segue válido. §7.1 **não é alvo** desta fatia: com a `DE-8` o gatilho da porta de saída
  deixa de depender de versão, então ele não é consequência do congelamento e tem fatia própria
  (`T9b`). Nenhuma frase do §10 deve afirmar o que a §7.1 faz — no máximo apontá-la.
- **Restrição de redação:** `GOVERNANCA.md` é doutrina publicada — vale `redacao-doc` §6. Proibido
  citar data, tíquete, id de tarefa, episódio ou "o que mudou": a seção descreve o regime vigente,
  não a decisão que o instituiu (isso mora no `CHANGELOG.md` e no diário).
- **Verificação:** a bateria acima, os quatro em exit 0. `check-readme.ps1` deve seguir reportando
  **14 guardrails**.
- **Pronto quando:** lida do começo ao fim, a §10 responde sem ambiguidade "qual é a versão, o que
  se exige a cada mudança canônica e o que a checagem de versão faz" no regime congelado.
  `VERSION` continua `2.0.0` nesta fatia — a conformidade do artefato é da `T9d`.

### T9b — `GOVERNANCA.md` §7.1: o gatilho da porta de saída passa a pender do fechamento de plano [Opus]
- **Objetivo:** `DE-8`. A porta de saída de guardrail está pendurada no fechamento de um MINOR do
  kit; com o número congelado nenhum MINOR fecha e a única forma legítima de remover uma regra
  deixaria de existir. O gatilho passa a pender de um evento que já existe e já é registrado: o
  fechamento de um plano.
- **Arquivos-alvo:** `GOVERNANCA.md` — **só** a §7.1 "Revisão e deprecação de guardrails"
  (L531-592). Nenhum outro arquivo.
- **Conteúdo prescrito** (seis blocos, todos dentro de §7.1):
  1. **Abertura** (L533, "o custo de ler a doutrina cresce a cada MINOR"): a unidade de crescimento
     deixa de ser o MINOR e passa a ser a rodada de trabalho. O argumento do apodrecimento fica
     intacto — muda só a unidade.
  2. **"Gatilho"** (L537-541), reescrito. O que dispara: o **fechamento de um plano** — a linha do
     plano indo a `done` no índice de `docs/DIARIO_DE_OBRAS.md`. Nunca calendário, nunca número de
     versão. Escrever "plano (`P-NNNN`)", não "estágio": estágio é um plano como qualquer outro
     (cada estágio da iniciativa tem seu próprio `P-NNNN`) e, como conceito, ainda não tem
     residência normativa (`TK-08`) — a regra não pode depender dele. Razão a preservar do texto
     atual: o gatilho pendura-se no momento em que **há material novo para julgar**, e o
     fechamento de plano é esse momento. Quem detecta: a skill `checar-versao-kit`, na criação do
     plano seguinte (`T9c`), comparando o índice do diário com o registro das rodadas. Quem
     executa: ninguém ali — a revisão é tarefa nomeada, com registro próprio, como já hoje. O
     parágrafo de atraso aceito por desenho (L85-87 da skill, espelhado aqui) permanece válido com
     a troca de "MINOR" por "plano fechado".
  3. **"Escopo"** (L543-544): "≥2 MINORs de idade" passa a **≥2 rodadas de idade** — entra a
     guardrail que já constava de §7 na **penúltima** rodada registrada. A razão fica idêntica
     ("regra recém-adicionada não teve tempo de agir"). **Regra de partida, explícita:** enquanto
     não houver duas rodadas registradas no novo regime, a rodada `1.4.0` faz as vezes de
     penúltima — entram as guardrails que já constavam de §7 nela.
  4. **"Pergunta única"** (L559): a janela "nos últimos 2 MINORs" passa a ser a mesma do escopo —
     **desde a penúltima rodada registrada**. O texto da pergunta e a definição de caso citável
     (L561-567), com as duas exclusões, ficam **intactos**.
  5. **"Resultado"** (L569-573): "OBSOLETA desde `<versão>`" passa a "OBSOLETA desde `<rodada>`",
     e a rodada é identificada pelo plano que a disparou (`P-NNNN`); "permanece em vigor por **um
     MINOR** de transição e é removida no **MINOR seguinte**" passa a "por **uma rodada** de
     transição, removida na **rodada seguinte**". Nada mais muda: a remoção continua sendo tarefa
     nomeada, e um caso citável na transição continua desfazendo a marcação.
  6. **"Registro das rodadas"** (L575-592): (a) declarar o **formato da entrada** no novo regime —
     rótulo `<P-NNNN> — <AAAA-MM-DD>`, o plano cujo fechamento disparou a rodada, as guardrails
     avaliadas, as que ficaram fora por idade e o resultado; (b) acrescentar à entrada `1.4.0` uma
     linha de conversão declarando-a **marco zero** do novo regime: contam os planos fechados a
     partir de `2026-08-01`, e tudo anterior está coberto por ela. **Não reescrever** o corpo
     histórico da entrada `1.4.0` (L577-592) — é registro.
- **Fronteiras:** não tocar o parágrafo "Isenção por enforcement executável" (L546-555) nem o
  "Caso citável" (L561-567) — nenhum dos dois menciona versão. **Não tocar** a linha do heading
  `### 7.1 Revisão e deprecação de guardrails` (L531): `check-readme.ps1:186-193` usa esse texto
  exato como marcador de fim da contagem de guardrails de §7. Toda edição desta fatia é depois do
  marcador, então a contagem (14) não muda.
- **Restrição de redação:** doutrina publicada — `redacao-doc` §6. A seção descreve o regime
  vigente; proibido narrar que o gatilho "era" de MINOR, quem decidiu ou quando (isso mora no
  `CHANGELOG.md` e no diário).
- **Verificação:** a bateria acima, os quatro em exit 0. `check-readme.ps1` deve seguir reportando
  **14 guardrails** — se o número mudar, o marcador de fim foi quebrado.
- **Pronto quando:** a §7.1, lida sozinha, responde sem ambiguidade: o que dispara uma rodada, como
  se sabe que há uma pendente, quais guardrails entram, qual a janela da pergunta, o que acontece
  com a que não tem caso citável, e onde a rodada fica registrada — tudo sem citar número de
  versão. `TK-16` fecha com esta fatia.

### T9c — mecanismo executável: skill de checagem, consumidores e índice derivado [Sonnet]
- **Objetivo:** `DE-7` e `DE-8` no que executa. Duas mudanças independentes na mesma skill, porque
  ela é o carregador das duas doutrinas: o **curto-circuito do congelamento** (que entra antes de o
  número mudar — enquanto `VERSION` for `2.0.0` ele é inerte por construção, e passa a valer
  sozinho no instante da `T9d`) e a **troca do gatilho de revisão da doutrina**, que deixa de ler
  versão e passa a ler o índice do diário.
- **Arquivos-alvo:** `.claude/skills/checar-versao-kit/SKILL.md`; `docs/CONSUMIDORES.md`;
  `.claude/README.md` (**regenerado por comando, nunca editado à mão**).
- **Conteúdo prescrito:**
  1. **`SKILL.md`, fim do passo "### 1. Resolver a versão local"** (após a L37): parágrafo novo
     **"Congelamento (curto-circuito)"** — se a versão local resolvida for `0.0.0`, o framework
     está em desenvolvimento pré-lançamento (`GOVERNANCA.md` §10, bloco "Congelamento
     pré-lançamento"): reportar `versão congelada em 0.0.0 — nada a comparar`, **pular os passos 2
     e 3** (nenhuma chamada de rede acontece) e **seguir direto para o gatilho de revisão da
     doutrina**, que com a `DE-8` não depende de versão e roda igual nos dois regimes. A skill
     **não** encerra aqui. A numeração dos passos 1/2/3 **não muda** (evita quebrar as referências
     internas das L15, L25, L29-30, L47-48 e L75).
  2. **`SKILL.md`, L15-16** ("executa **duas** checagens independentes ... que aproveita a mesma
     leitura de versão"): a segunda checagem deixa de aproveitar a leitura de versão — as duas
     passam a compartilhar **só o momento de invocação**. Acrescentar que, sob congelamento, a
     primeira para no passo 1 e a segunda roda assim mesmo.
  3. **`SKILL.md`, "## Os resultados possíveis"** (L53-65): bullet novo **primeiro** — *versão
     congelada (`0.0.0`) → reporta "congelada — nada a comparar", sem rede e sem pergunta ao dono,
     e segue para o gatilho de revisão*. Os quatro bullets existentes ficam como estão.
  4. **`SKILL.md`, "## Gatilho de revisão da doutrina"** (L67-87), **reescrito** para o gatilho da
     `DE-8`. Roda sempre, congelada ou não. A doutrina continua morando em `GOVERNANCA.md` §7.1 —
     aqui fica só o procedimento:
     - **1.** Ler, em `GOVERNANCA.md` §7.1, a última rodada registrada e o plano que ela cobre
       (Grep por `Registro das rodadas`, sem ler a seção inteira — como já hoje).
     - **2.** Ler o índice de `docs/DIARIO_DE_OBRAS.md` e listar os planos com status `done`
       (Grep por `| done |` na tabela do índice).
     - **3.** Existe plano `done` fechado a partir do marco zero (`2026-08-01`) que não conste de
       nenhuma rodada registrada ⇒ revisão **pendente**. Reportar ao dono: o plano que disparou, a
       última rodada registrada e quantas guardrails de §7 entram em escopo (as que já constavam
       na penúltima rodada). **Não executar a revisão aqui** — é tarefa nomeada, com registro
       próprio no diário.
     - **4.** Nenhum plano `done` fora das rodadas registradas ⇒ segue em silêncio.
     - O parágrafo final de atraso aceito por desenho (L85-87) permanece, trocando "um MINOR pode
       fechar sem que nenhum plano novo seja criado logo depois" por "um plano pode fechar sem que
       outro seja criado logo depois".
     - **`TK-05` fecha por remoção:** a comparação de componente MINOR sai do gatilho junto com o
       resto do mecanismo antigo, e com ela a cegueira ao atravessar um MAJOR. Não há correção a
       fazer — o trecho defeituoso deixa de existir. A distinção MAJOR × MINOR/PATCH da **checagem
       de versão** (passo 3) é outra coisa e **permanece intacta**.
  5. **`SKILL.md`, `description` do frontmatter (L3)** — substituir por, literalmente:
     `Resolve a versão local do kit agêntico e, enquanto o framework estiver com a versão congelada em 0.0.0 (GOVERNANCA.md §10), reporta "congelada — nada a comparar" sem tocar a rede. Fora do congelamento, compara com a versão publicada no hub PantonicApp sem nunca atualizar sozinho, em três modos de resolução (consumidor, hub, não-instalado). Nos dois regimes arma o gatilho de revisão da doutrina (GOVERNANCA.md §7.1), que fica pendente quando existe plano fechado como done no índice do diário sem rodada de revisão registrada. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano").`
     **Restrição dura:** a `description` não pode conter o caractere `|` — ela vira célula de
     tabela em `.claude/README.md` (`kit_check.ps1:65-84`).
  6. **`docs/CONSUMIDORES.md`, nota do cabeçalho** (L11-13): acrescentar que, com a versão
     congelada, a coluna `Versão instalada` carrega o mesmo `0.0.0` para todos e **não distingue
     deriva** — a deriva entre hub e consumidor passa a ser detectada por
     `kit_check.ps1 -Mode check-drift` rodado no consumidor. Não tocar a tabela (é derivada por
     `-Mode consumers`).
  7. **Regenerar o índice do kit**, porque a `description` mudou:
     `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`
- **Fronteiras:** `.claude/skills/diario-de-obras/SKILL.md:89` (que invoca a checagem na criação de
  plano) **não é alvo** — o ponto de invocação não muda com a `DE-8`: o gatilho *dispara* no
  fechamento de um plano e é *detectado* na criação do plano seguinte, que é onde a skill já roda.
  O atraso entre os dois é o mesmo que a §7.1 já aceita por desenho. Também **não é alvo** a
  operação de fechamento de plano de nenhuma skill.
- **Verificação:** a bateria acima, os quatro em exit 0 — `-Mode check-drift` é o que prova a
  regeneração do item 7.
- **Pronto quando:** as duas leituras cabem no texto sem ramo ambíguo — com `VERSION` em `0.0.0` a
  skill reporta "congelada", não toca a rede e ainda assim avalia o gatilho de revisão; com
  `VERSION` em `2.0.0` a checagem de versão se comporta exatamente como hoje. E o gatilho de
  revisão, lido isoladamente, não menciona versão em nenhum passo.

### T9d — congelar o número e abrir o registro [Sonnet]
- **Objetivo:** `DE-7` nos artefatos. Depois desta fatia o congelamento é fato observável, e as
  quatro fontes do número dizem a mesma coisa.
- **Arquivos-alvo:** `VERSION`; `.claude/KIT_VERSION`; `README.md` (L3 e L829, **só as linhas do
  número**); `CHANGELOG.md` (preâmbulo L1-9 e bloco `## [Não lançado]` L82-85).
- **Conteúdo prescrito:**
  1. `VERSION` e `.claude/KIT_VERSION`: conteúdo passa a ser exatamente `0.0.0` (arquivo de uma
     linha, como hoje).
  2. `README.md:3`: `**Versão do framework:** ` + `` `0.0.0` `` — o resto da linha (idioma,
     licença) fica intacto. O guarda casa o padrão
     `\*\*Versão do framework:\*\*\s*` seguido do valor entre crases (`check-readme.ps1:138`).
  3. `README.md:829`: `**Versão vigente do framework: ` + `` `0.0.0` `` + `.**`
     (padrão `Versão vigente do framework:` + valor entre crases, `check-readme.ps1:141`), seguido
     de **uma** frase declarando que o número está congelado até a decisão de publicar, com
     ponteiro para `GOVERNANCA.md` §10. A varredura de prosa do §13 é da `T9e`; aqui entra só o que
     impede a primeira linha da seção de mentir.
  4. `CHANGELOG.md`, preâmbulo (L1-9): acrescentar duas afirmações — (a) a versão está congelada em
     `0.0.0` e, enquanto durar, **toda** mudança canônica é registrada sob `## [Não lançado]`, que
     é a única seção viva; (b) as seções numeradas abaixo (`1.0.0`..`2.0.0`) são o histórico de
     desenvolvimento pré-lançamento, correspondem às tags `kit-v1.0.0`..`kit-v2.0.0` já publicadas
     e **permanecem como registro** — não são reescritas nem revogadas.
  5. `CHANGELOG.md`, seção `## [Não lançado]`: **mover para o topo**, imediatamente após o preâmbulo
     e **antes** de `## 2.0.0` (L11) — remover o bloco das L82-85 (cujo corpo hoje é só
     `_(vazia — ...)_`) e reinseri-lo no topo com o corpo substituído pelo registro do Estágio 6.
     Nenhuma outra seção do arquivo é tocada.
  6. **Corpo da seção `[Não lançado]`** — herda o conteúdo que o dossiê original da `T9` mandava
     escrever, que a `DE-7` não revoga (o registro continua obrigatório; só o número deixa de
     andar). Quatro entradas, com o id da tarefa como as entradas já existentes do arquivo fazem:
     (a) o conceito de **perfil** deixa de existir no hub — nenhuma marcação `*[perfil ...]*`,
     nenhum `.claude/PERFIL`, nenhum default (`V2E-T1`..`T4c`), com o conteúdo desktop preservado
     em `PantonicForDesktop/` e o de container em `PantonicForContainer/`; (b) o guardrail de MVVM
     sai da lista de `GOVERNANCA.md` §7 — **15 → 14** (`V2E-T2`); (c) `.claude/checks/dead_code.py`
     troca as constantes de Qt pelo arquivo opcional `.claude/framework-virtuals.txt` do projeto —
     quem dependia das exceções de Qt passa a declará-las, e o modelo pronto para copiar está em
     `PantonicForDesktop/.claude/framework-virtuals.txt` (`V2E-T5b`); (d) a versão congela em
     `0.0.0` e as superfícies de versionamento são reconciliadas (`V2E-T9a`, `T9c`..`T9e`); (e) o
     gatilho de revisão da porta de saída de guardrail (`GOVERNANCA.md` §7.1) deixa de pender do
     fechamento de um MINOR e passa a pender do fechamento de um plano (`V2E-T9b`). O
     `CHANGELOG.md` é **registro**, isento das restrições de redação do agente (`redacao-doc` §5):
     citar id de tarefa e o que mudou é o formato correto aqui.
- **Fronteiras:** as 8 tags `kit-v*` **não são tocadas** — publicar e despublicar tag é ato do dono
  (`DE-7`); o executor não roda `git tag` nem `git push` nesta fatia.
- **Verificação:** a bateria acima, os quatro em exit 0. A checagem 3 do `check-readme.ps1` é o
  gate desta fatia: ela compara `VERSION`, `.claude/KIT_VERSION`, cabeçalho e corpo do README e
  falha se os quatro não coincidirem.
- **Pronto quando:** os quatro portadores do número dizem `0.0.0`; `## [Não lançado]` é a primeira
  seção do `CHANGELOG.md` e contém a entrada do congelamento; nenhuma seção numerada foi alterada.

### T9e — espelho: `README.md` §13, §10 e glossário [Opus]
- **Objetivo:** fechar o `DE-7` e o `DE-8` no contrato com o cliente. O espelho segue as fontes
  (`T9a`, `T9b`), nunca as precede.
- **Arquivos-alvo:** `README.md` — a linha `> Fonte da verdade:` (L827), o corpo do §13 (L840-879),
  a entrada de glossário da tag (L135-137) e o parágrafo do apodrecimento em §10 (L700-702).
- **Aviso de deslocamento:** os números de linha acima são os de **antes** da `T9d`, que acrescenta
  uma frase logo após a L829 — tudo o que vem depois desloca. Localizar por âncora de conteúdo, não
  por número absoluto: item 2 = parágrafo iniciado por "O versionamento é semântico"; item 3 =
  parágrafo iniciado por "A checagem de versão acontece"; item 4 = parágrafo iniciado por "O limite
  que atravessa tudo isso"; item 5 = parágrafo iniciado por "Dois artefatos derivados"; item 6 =
  parágrafo iniciado por "**Por quê.**"; item 7 = parágrafo iniciado por "**Onde o gerente
  intervém.**". As âncoras L700-702, L827 e L135-137 são anteriores à L829 e **não** deslocam.
- **Conteúdo prescrito:**
  1. **L827** — `> Fonte da verdade: ` + `` `GOVERNANCA.md` `` + ` §9 e §10`. Medido: §9 é "Kit
     agêntico reusável" (distribuição por subtree) e §10 é "Versionamento e atualização do kit"; a
     §13 espelha as duas e hoje cita só a §9. O guarda captura o primeiro trecho entre crases e
     testa só a existência do arquivo (`check-readme.ps1:207`), então a forma proposta passa.
  2. **L840-845** (semver, bump, tag): os significados de MAJOR/MINOR/PATCH permanecem declarados;
     o bump obrigatório e a publicação de tag passam a valer **a partir do lançamento**, e no
     regime vigente a mudança canônica escreve no `CHANGELOG.md` sem mover o número.
  3. **L847-854** (os quatro desfechos da checagem): condensar. Primeiro o desfecho vigente —
     congelada, a checagem tem **um** desfecho, "nada a comparar", sem chamada de rede —, e depois
     **uma** frase que nomeia os quatro desfechos pós-lançamento, sem reproduzir o parágrafo
     inteiro. Espelho é condensado e autossuficiente, nunca ponteiro nu (`README.md:125-126`): o
     texto continua nomeando os quatro, não os substitui por "ver §10".
  4. **L856-859** (divergência é reportada, nunca aplicada por agente): **não tocar** — não depende
     do número.
  5. **L861-865** (`docs/CONSUMIDORES.md` derivado e assinatura do commit): acrescentar a cláusula
     de que, com o número congelado, a coluna de versão instalada não distingue deriva e a detecção
     é por `kit_check.ps1 -Mode check-drift`.
  6. **L867-872** ("Por quê"): acrescentar a razão do congelamento — número que não corresponde a
     lançamento nenhum simula maturidade que o framework não tem; `0.0.0` é o que a régua semver
     reserva para desenvolvimento inicial. O resto do parágrafo permanece.
  7. **L874-879** ("Onde o gerente intervém"): o critério de pronto que ele confere passa a ser a
     linha no `CHANGELOG.md` enquanto congelado; **descongelar é ato dele**, como publicar commits
     e tags já é.
  8. **L135-137** (glossário, "Tag `kit-vX.Y.Z`"): acrescentar que, com a versão congelada, o hub
     não publica tag nova. As entradas de `KIT_VERSION` (L132-134), `sync-kit` (L119-121), `Hub`
     (L114-116) e `Consumidor` (L117-118) **não são alvo** — nenhuma afirma número.
  9. **L700-702** (§10 do README, parágrafo do apodrecimento): espelho da abertura da
     `GOVERNANCA.md` §7.1 que a `T9b` reescreve. Trocar a unidade de crescimento ("o custo de ler a
     doutrina cresce **a cada versão**") pela mesma unidade que a fonte passa a usar, e nomear o
     gatilho pelo que ele é agora — o fechamento de um plano — em vez de "gatilho periódico". A
     afirmação central (remover guardrail só por ato registrado, com motivo, nunca por erosão
     silenciosa) fica intacta. Este parágrafo **não** tem guarda executável: `check-readme.ps1` não
     compara o texto de §10 com a §7.1, então a fidelidade é responsabilidade desta fatia.
- **Restrição de redação:** `redacao-doc` §6 sem exceção — o §13 descreve o estado corrente.
  Proibido citar data, tíquete, id de tarefa, versão anterior ou o episódio que motivou o
  congelamento; esse relato mora no `CHANGELOG.md` e no diário.
- **Verificação:** a bateria acima, os quatro em exit 0, **mais** o Grep de fechamento da `T9`
  inteira — padrão `2\.0\.0|3\.0\.0|kit-v3` em `README.md`, `GOVERNANCA.md`,
  `.claude/skills/checar-versao-kit/SKILL.md` e `docs/CONSUMIDORES.md`: **zero ocorrências**
  esperadas (o `CHANGELOG.md` está fora do conjunto por desenho — é lá que a numeração histórica
  vive). **Segundo Grep**, fechamento da `DE-8`: padrão `MINOR` nos mesmos quatro arquivos — as
  únicas ocorrências legítimas restantes são as da **checagem de versão** (`GOVERNANCA.md` §10
  "Divergentes em MINOR/PATCH", `README.md` §13 e o bullet correspondente da skill); qualquer
  ocorrência ligada a **revisão de doutrina** ou a **idade de guardrail** é resíduo do gatilho
  antigo.
- **Pronto quando:** um humano que leia só o §13 sabe qual é a versão, por que ela não anda, o que
  se exige a cada mudança canônica e o que a checagem de versão faz — sem abrir a `GOVERNANCA.md`;
  e o parágrafo de §10 do README descreve o mesmo gatilho que a §7.1 da fonte. Com esta fatia a
  `V2E-T9` fecha completa (`T9a` + `T9b` + `T9c` + `T9d` + `T9e`).

### T10 — Auditoria: em que grau infracore e plugins estendem CA+DDD hoje [Sonnet]
- **Objetivo:** absorve a `V2I-T14` — medir o que a `V2I-T5` declarou não auditado.
- **Procedimento:** roda na implementação de referência (`D:\workspaces\PantonicVideo`), não no hub;
  skill `audit-sweep` (pré-varredura mecânica) → agente `pantonic-auditor-arch`.
- **Saída:** `docs/audits/AUDIT_ARCH_<AAAA-MM-DD>.md` no PantonicVideo; **não altera código**.
- **Pronto quando:** existe resposta medida para "o infracore e os plugins de fato estendem CA+DDD,
  e onde não estendem".

### T11 — Autorar `P-0732` (abstração do infracore) já fechado [Opus]
- **Objetivo:** absorve a `V2I-T15` com o escopo corrigido pela `DE-6`. O plano dependente nasce
  como a última tarefa do plano que produz seu insumo, nunca como vão (G-PLANREADY).
- **Insumos:** achado da `T10` + a doutrina de infracore agnóstico consolidada pelas `T2`/`T3`.
- **Arquivos-alvo:** `docs/plans/P-0732-<slug>.md` (novo); `docs/plans/_INBOX.md` (linha nova +
  contador → `P-0733`); `docs/DIARIO_DE_OBRAS.md` (índice).
- **Escopo do plano a autorar:** portas genéricas de lifecycle, injeção, estado, sinais e filesystem
  no infracore. O binding Qt **não** é uma das implementações a manter no hub — ele já saiu; o que
  se projeta é a porta que permite a `PantonicForDesktop` implementá-lo do lado de fora.
- **Pronto quando:** `P-0732` registrado e fechado, sem questão owner-gated pendente.

## 5. Ordem de execução

`T1` → `T2` → `T3` → `T4` → `T5a` → `T5b` → `T6` → `T7` → `T8` (dono) → `T9a` → `T9b` → `T9c` →
`T9d` → `T9e` → `T10` → `T11`.

Linear, sem ramo condicional. As remoções de doutrina (`T2`, `T3`) precedem a varredura do README
(`T6`) porque o README é espelho: varrer o espelho antes da fonte produz retrabalho. A `T7` entra
antes do aceite porque é o que dá à `T8` o caráter de tarefa de encerramento, e não de gate. Dentro
da `T9` a ordem é de dependência, não de tamanho: as duas doutrinas afetadas são escritas primeiro
(`T9a`, o número; `T9b`, o gatilho da porta de saída), o mecanismo executável passa a carregar as
duas enquanto o curto-circuito ainda é inerte (`T9c`), o número muda (`T9d`) e o espelho segue a
fonte (`T9e`) — inverter `T9c` e `T9d` deixaria a primeira criação de plano após o congelamento
comparando `0.0.0` com a tag `kit-v2.0.0` e reportando "incompatível e para".
`T2`, `T3`, `T6`, `T7`, `T9a`, `T9b`, `T9e` e `T11` são Opus (doutrina e redação canônica); `T1`,
`T4`, `T5a`, `T5b`, `T9c`, `T9d` e `T10` são Sonnet; `T8` é do dono.

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Perder conhecimento ao remover — o material desktop foi caro de produzir | Invariante 1 do §3: remoção e preservação no mesmo commit; `PantonicForDesktop/README.md` mantém o inventário ancorado do que falta |
| Quebrar os consumidores, que hoje herdam o kit com Qt dentro | Medido: **0/6 consumidores têm `.claude/kit/` instalado** (`docs/CONSUMIDORES.md`) — nenhum materializou o kit por subtree, logo não há instalação a quebrar. A `T5` entrega o arquivo de declaração pronto para copiar, e a `T9d` registra a mudança sob `[Não lançado]` no `CHANGELOG.md`, que é o que um consumidor futuro lê. Com a `DE-7` a migração deixa de ser instruída por número de versão |
| Renumerar guardrails e quebrar referência cruzada silenciosamente | `T2` grepa por "item \<N\>" antes de renumerar; os guardrails que outros documentos citam de fato são os **nomeados**, que não mudam |
| "Universal" virar vago — perder a precisão que torna as regras executáveis | O que sai é sempre **modalidade**, nunca **regra**: as 14 regras restantes continuam com forma de enforcement declarada, e `dead_code.py` fica mais preciso, não menos |
| A varredura declarar vitória por Grep vazio enquanto o conceito sobrevive com outro nome | Cada tarefa tem "pronto quando" semântico além do Grep; a `T8` é o gate de sentido |

## 7. Reconciliação com o Estágio 5 (obrigatória)

Classificação **(B)** da skill `diario-de-obras` — *"a premissa que o sustentava caiu; a rota agora é
outra"*. A premissa era a `DR-2` do `P-0730`: perfis nomeados como forma de conciliar núcleo
agnóstico com verificação específica. Ela caiu.

`P-0730-V2I` vai a **`superseded`**, com ponteiro `substituído por:
docs/plans/P-0731-v2-extracao-modalidade.md`. O trabalho entregue permanece e **não é revertido**:
as `V2I-T1..T11c` corrigiram a identidade do framework de "desktop com stack fixo" para "agnóstico",
e essa correção é a base sobre a qual este estágio opera — o que muda é o mecanismo, não o
diagnóstico. As cinco tarefas que ainda não haviam rodado são absorvidas com escopo corrigido:
`V2I-T12` → `T8`, `V2I-T13` → `T9` (o fechamento em `2.1.0` virou `3.0.0` e, com a `DE-7`, virou o
congelamento em `0.0.0`, partido em `T9a`..`T9e`), `V2I-T14` → `T10`, `V2I-T15` → `T11`
(`P-0731` vira `P-0732`), `V2I-T16` → `T7`. Nenhuma tarefa nova sai do Estágio 5.

Este plano passa a ser o **único plano vivo** da iniciativa `PANTONIC-V2`.

## 8. Achados abertos deste planejamento

- **`TK-10`** — `docs/DIARIO_DE_OBRAS.md` está em **937 linhas**, muito além do gatilho de ~500 da
  operação "Condensar" da skill `diario-de-obras`. As seções dos estágios 1 a 4, todas terminais,
  dominam o documento e deveriam estar em `docs/DIARIO_HISTORICO.md`. Sem relação com este estágio.
- **`TK-05`** (herdado) — a skill `checar-versao-kit` compara só o MINOR no gatilho de revisão de
  doutrina e fica cega ao atravessar um MAJOR. **Fecha na `T9c`, por remoção do mecanismo**: com a
  `DE-8` o gatilho deixa de ler versão, e o trecho defeituoso some junto com a comparação. Não há
  correção a escrever, e a distinção MAJOR × MINOR/PATCH da checagem de **versão** — outra coisa —
  permanece intacta.
- **`TK-16`** (aberto e fechado na mesma rodada de planejamento) — a porta de saída de guardrail
  (`GOVERNANCA.md` §7.1) pendurava o gatilho no **fechamento de um MINOR do kit**; com o número
  congelado nenhum MINOR fecha, e o framework passaria a só adicionar regra, sem nenhuma poder
  sair. **Decidido pelo dono em 2026-08-07 (`DE-8`):** o gatilho passa a pender do **fechamento de
  um plano**. Executado pela `T9b` (doutrina), `T9c` (procedimento) e `T9e` (espelho).

## Achados da execução

- **`TK-14` (achado da `T8`, bloqueia a `T9`)** — o aceite do dono trouxe uma premissa que o
  planejamento não tinha: o framework nunca foi lançado em público, logo não existe `V0`/`V1`/`V2` e
  todo o trabalho é a **primeira** versão. O `README.md` já foi corrigido (a §15, "O que a V2
  mudou", saiu inteira). O que fica em aberto é o dossiê da `T9`, que manda escrever `CHANGELOG.md`
  §3.0.0 com instrução de migração: decidir se o registro de histórico de alterações permanece como
  artefato de distribuição — os 5 consumidores materializam o kit por versão, e `VERSION`,
  `.claude/KIT_VERSION` e a tag `kit-v<versão>` seguem tendo função mesmo sem lançamento público —
  ou se cai junto com a numeração. **Decidido pelo dono em 2026-08-07:** o número **fica** como
  artefato e é congelado em **`0.0.0`** até a decisão de publicar — antes do lançamento a numeração
  não tem valor. O `CHANGELOG.md` permanece. **O dossiê da `T9` fica inválido como está** ("Fechar
  `3.0.0` e distribuir", `CHANGELOG.md` §3.0.0, tag `kit-v3.0.0`): a tarefa passa a ser o
  congelamento, e o §13 do `README.md`, a `GOVERNANCA.md` §9 e a skill `checar-versao-kit` entram no
  alcance. Reescrita do dossiê é ato do planejador — o executor não muda rota (`G-PLANFIDELITY`).
  **Fechado em 2026-08-07 pela reescrita:** a `DE-4` foi revogada, a `DE-7` entrou com o destino do
  que já foi numerado (tags e seções numeradas permanecem como histórico pré-lançamento), e a `T9`
  virou `T9a`..`T9e`. O ponto que o tíquete deixava pendente está fechado no plano, não no tíquete.
- **`TK-15` (achado da `T8`)** — a classe "Seção histórica declarada" do §5 da skill `redacao-doc`
  isenta de `V7` uma seção do doc publicado cujo assunto é a mudança entre versões. Foi essa isenção
  que manteve a §15 do README viva por três rodadas de redação, com a varredura mecânica do §6
  acusando zero. **Decidido pelo dono em 2026-08-07:** a classe **sai**. O histórico mora num
  documento de finalidade estrita — o `CHANGELOG.md` que já existe —, isento das restrições de
  redação; doc publicado não carrega histórico, e as restrições valem nele sem exceção. Tarefa
  própria, fora do alcance deste plano.
- **`TK-17` (achado da `T9a`)** — a `T9a` aplicou `redacao-doc` §6 à §10 da `GOVERNANCA.md` e a
  varredura mecânica saiu limpa **dentro** do alvo (zero ocorrências de `V3`/`V7` em L642+, incluído
  o rótulo `(V2B-T1)` do parágrafo da paridade, removido na fatia). A mesma varredura sobre o
  arquivo inteiro devolve **25+ ocorrências fora do alvo**: datas em §3 (L106, L118, L137-144), ids
  de tarefa/plano em §7 (L459, L474-476, L498, L511, L520, L523), §7.1 (L546, L577, L585-592) e §9
  (L619-624, L630). A `GOVERNANCA.md` é da classe **publicado** (`redacao-doc` §5), onde o piso de
  aceite de `V3` é zero — mas parte dessas linhas é razão legítima enunciada como fato medido
  (`redacao-doc` §3: a medição que sustenta o limiar), e distinguir uma da outra é decisão de
  doutrina, não de execução. Pertinência: o Estágio 6 é o estágio que aplica `redacao-doc` ao
  corpus, e a §10 saneada serve de referência de forma para o resto do arquivo. Fora do alcance
  desta fatia (alvo único) e do plano como escrito; precisa de tarefa própria com critério por
  seção decidido antes da varredura. **Decidido pelo dono em 2026-08-07: limpar tudo.** Nenhuma
  ocorrência de `V3`/`V7` sobrevive na `GOVERNANCA.md` — nem as que hoje enunciam razão como fato
  medido. A regra que uma medição sustentava passa a ser afirmada inline, sem o ponteiro de
  proveniência (mesmo padrão do `TK-11`); a medição em si continua registrada onde é histórico
  (plano de origem, diário, `CHANGELOG.md`), que é de onde ela nunca deveria ter saído. O piso de
  aceite da varredura mecânica do §6 sobre o arquivo inteiro passa a ser **zero**, e a §10 saneada
  é a referência de forma. Execução pendente de tarefa própria — não pertence a este plano.
