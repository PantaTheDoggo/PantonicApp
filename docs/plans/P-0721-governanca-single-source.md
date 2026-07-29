# P-0721 — Governança Pantonic* single-source: PantonicApp como repositório de referência

**Origem:** pedido do dono (2026-07-21). Dor declarada: toda alteração na governança comum obriga
a reajustar todos os filhos à mão. Meta: **PantonicApp = fonte única canônica** das decisões que
afetam todos os filhos; cada filho guarda **só o específico** + **ponteiros** para o comum.

**Planejador:** Opus (fase de arquitetura/planejamento, Regra 7). **Executor:** a definir por fase
(curadoria/arquitetura → Opus/dono; mecânica de migração → Sonnet).

**Estado:** **REVISADO 2026-07-25 (2ª rodada de arquitetura).** O mecanismo central mudou:
**DP-1 passou de A (junção/symlink em `~/.claude`) para D (distribuição git a partir do hub
remoto)**, por decisão do dono, depois que a Fase 2 original esbarrou num bloqueio de privilégio
no Windows (ver `## Achados da execução` → "Fase 2 original abortada"). DP-2..DP-5 seguem como
redigidas; **DP-6 cumprido** (o hub é repo git publicado em
`github.com/PantaTheDoggo/PantonicApp`); **DP-7 novo e aberto** (onde os artefatos herdados
aterrissam dentro do filho).

Fases renumeradas por essa troca: 0, 1a, 1b **done**; **Fase 2 (regularizar o hub como repo
remoto) done** — ela era a antiga Fase 5 e subiu para a frente porque, em DP-1=D, o hub versionado
é pré-requisito de toda distribuição. Curadoria de 0/1a/1b executada em Sonnet, não Opus/dono como
o texto original previa (precedente medido nas 3 rodadas: escopo suficientemente mecânico/bounded).

**DP-7 fechado pelo dono (2026-07-25) = D1** (subtree em `.claude/kit/` + materialização).
**DP-8 aberto** pela sondagem da mesma rodada: **5 dos 6 filhos não são repositórios git** — trava
a Fase 4, **não** a Fase 3.

**FECHADO 2026-07-28**, via `P-0725-governanca-hub-unico.md` Fase 5. A partir da Fase 3, este
plano foi absorvido pelo sucessor com mapeamento tarefa a tarefa (ver `P-0725` §5 "Relação com os
planos anteriores"): Fase 3 (T2→Fase 3, T3/T4→Fase 4 de `P-0725`), Fase 4 (migrar 6 filhos)
superseded (1 virou prova de aceitação, 1 legado, 1 abortado, 3 adiados), DP-8 encerrado (nenhum
projeto que ele travava seguiu em escopo). Registro final de DP-1..DP-8 (deste plano) e DP-9..DP-13
(do sucessor) consolidado em `P-0725` §Fase 5 / "Notas de execução". Nenhuma tarefa deste plano
segue em aberto.

---

## 0. Escopo — quem segue a governança comum (medido 2026-07-21)

| Papel | Projetos |
|---|---|
| **Canônico (hub)** | `PantonicApp` |
| **Filhos governados** (têm o kit `.claude/skills` + agentes `pantonic-*`) | `PantonicContainer`, `PantonicContainerForAWS`, `PantonicMonitor`, `PantonicPatom`, `PantonicScanlator`, `PantonicVideo` |
| **Fora de escopo** (não seguem o kit hoje) | `PantonicDrawing`, `PantonicYoutuber` (têm `.claude` mas sem kit), `PantonicForum`, `PantonicPDF` (sem `.claude`) |

Total governado: **7 repositórios** (1 hub + 6 filhos).

---

## 1. Diagnóstico (o que está duplicado vs. o que já é single-source)

**Já é single-source — só falta FORMALIZAR como ponteiro (não mexer no conteúdo):**
- **Regras globais 1-7** → `~/.claude/CLAUDE.md`, herdadas por toda sessão de todo projeto.
- **`GOVERNANCA.md`** (214 linhas, §1-9) + **`ARQUITETURA_PANTONICA.md`** → existem **só** em
  `PantonicApp/`; os filhos já os citam por caminho absoluto (nenhum filho tem cópia — confirmado:
  `find -iname GOVERNANCA*` só acha `PantonicApp/GOVERNANCA.md`).
- **`pantonic-scout`** já é declaradamente `~/.claude/agents/context-scout.md` + bloco de fatos
  estáveis do projeto (precedente de herança global existente, README do kit).

**Está DUPLICADO — é a dor a resolver:**
- **Kit executável (skills + agentes)**: 7 skills + ~7 agentes, **copiados** no `.claude/` de cada
  filho. A GOVERNANCA §9 e o `.claude/README.md` do kit **institucionalizam a cópia**: *"Todo
  projeto novo copia esse kit no bootstrap e ajusta apenas os fatos estáveis dos agentes."* Cada
  mudança de governança comum = N edições manuais.

**Matriz comum × específico (medida):**

| Artefato | Comum (deveria ser idêntico em todos) | Variante / específico do filho |
|---|---|---|
| **Skills (7)** | `audit-sweep`, `bootstrap-pantonic`, `diario-de-obras`, `guardrails-check`, `handover`, `integrar-poc`, `proximo-passo` | — |
| **Agentes comuns (6)** | `pantonic-planner`, `pantonic-executor`, `pantonic-scout`, `pantonic-auditor-arch`, `pantonic-auditor-cleancode`, `pantonic-fora-da-caixa` | — |
| **Slot de auditor de domínio (1)** | — (escolhe-se 1 dos dois) | `pantonic-auditor-pyside6` (Video/Monitor/Scanlator) **ou** `pantonic-auditor-container` (Container/ForAWS/Patom) |
| **Extras bespoke** | — | `PantonicVideo`: pipeline de integração próprio (`architect-auditor`, `integration-*`, `poc-inspector`, `service-inspector`, `domain-expert`, `clean-code`) — específico, fica local |

**Deriva já instalada (evidência da dor):**
- `PantonicVideo` tem **só 4 das 7 skills** (falta `audit-sweep`, `bootstrap-pantonic`,
  `integrar-poc`) e um conjunto de agentes bespoke — está **defasado** do canônico.
- **Deriva viva a reconciliar JÁ:** as edições de 2026-07-21 em
  `PantonicVideo/.claude/skills/{diario-de-obras,proximo-passo}` (regra A/B/C de planos derivados +
  status `superseded`) são **melhoria de governança COMUM presa num filho**. Se a centralização
  rodar antes de promovê-las ao canônico, ela **apaga a melhoria**. → Fase 0 é pré-requisito
  bloqueante.

**Achado estrutural (RESOLVIDO na Fase 2, 2026-07-25):** `PantonicApp` **não era um repositório
git** (`git rev-parse` → exit 128) e não tinha `docs/`. Para ser "o repositório referenciado" com
histórico/revisão/rollback de decisões de governança, precisava virar repo git → DP-6. Hoje é repo
git publicado em `github.com/PantaTheDoggo/PantonicApp` (branch `main`). Com DP-1=D essa condição
deixou de ser só desejável e virou **pré-requisito técnico**: é o remoto que os filhos consomem.

---

## 2. Decisões (owner-gated — cada uma com recomendação)

| id | pergunta | recomendação |
|---|---|---|
| **DP-1** ⟳ **REVISADO 2026-07-25** | **Mecanismo de "fonte única + herança"** (o coração) | **D — Distribuição git a partir do hub remoto** (escolha do dono na 2ª rodada; substitui A). O hub é repo git publicado (`github.com/PantaTheDoggo/PantonicApp`) e cada filho **consome o kit por um comando git rodado pelo dev** (`git subtree pull`), materializando **arquivos nativos versionados no próprio filho** — "atua como se fosse algo nativo do projeto". Mudança comum = **1 commit no hub + 1 comando por filho**, contra 6 edições manuais hoje. Ganhos sobre A: atravessa máquinas (não depende de link local), o filho é **autocontido** (clone numa máquina nova traz o kit sem exigir o hub em disco), e cada atualização fica no histórico do filho (revisável/reversível por commit). Custo: não é instantâneo — exige o comando de pull (aceito pelo dono). **A (REJEITADO — era o default):** junção/symlink `~/.claude` → hub. Junção de *diretório* funciona sem admin (**testado OK**), mas **symlink de *arquivo* exige privilégio de administrador** no Windows sem Developer Mode (**medido: "Administrator privilege required"**) — inviabiliza os 8 agentes, que são `.md` soltos num namespace plano; e nenhuma das duas variantes atravessa máquinas. **B (absorvido por D):** copy-deploy por script — D é exatamente B, com a fonte versionada e a cópia registrada no histórico do filho. **C (rejeitado):** cópia por filho + só drift-guard — não atinge single-source. **Escape hatch (vale p/ D):** filho que precise especializar uma skill comum mantém uma de mesmo nome **fora** do caminho gerenciado pelo subtree (o subtree é dono do seu diretório e sobrescreve o que estiver dentro dele). |
| **DP-2** | **Home do slot de auditor de domínio variante** (`pyside6` × `container`) | Manter **ambos no canônico** como variantes nomeadas do kit; o filho **declara qual usa** (ponteiro/fato estável), não recria o arquivo. Assim uma melhoria no corpo comum do auditor de arquitetura beneficia os dois sem duplicar. |
| **DP-3** | **Como os filhos referenciam os docs comuns** (`GOVERNANCA`/`ARQUITETURA_PANTONICA`) | **Ponteiro fino padronizado** `.claude/README.md` em cada filho (5/6 já têm um README — repurpose; `PantonicVideo` ganha um novo): cita o caminho canônico + a regra "não editar cópia; o comum vive no PantonicApp/`~/.claude`; só o específico mora aqui". Mantém a citação por caminho absoluto que já funciona. |
| **DP-4** | **Tratamento do outlier `PantonicVideo`** | (a) Reconciliar a deriva viva (promover as edições A/B/C + `superseded` ao canônico — Fase 0); (b) realinhar o subconjunto de skills ao kit comum (ganha as 3 que faltam por herança); (c) **classificar o pipeline de integração bespoke como específico** — fica local, fora do kit comum. |
| **DP-5** | **Guarda de deriva (drift-guard)** | Check leve de conformance que **falha se um artefato comum divergir do canônico** (hash/diff de `~/.claude` ou do filho contra `PantonicApp/.claude`). Complementa DP-1 como rede de segurança — detecta cópia manual acidental ou junção quebrada. |
| **DP-6** ✅ **CUMPRIDO (Fase 2, 2026-07-25)** | **`PantonicApp` deve virar repositório git?** | **Sim.** Fonte canônica de governança sem histórico/PR/rollback é frágil. Feito: `git init -b main`, `.gitignore`, `.gitattributes` (LF), commit inicial `6068884`, publicado em `github.com/PantaTheDoggo/PantonicApp`. Com DP-1=D deixou de ser "recomendado" e virou **pré-requisito bloqueante** — é o remoto que os filhos consomem. |
| **DP-7** ✅ **FECHADO 2026-07-25 = D1** (dono aceitou a recomendação) | **Onde os artefatos herdados aterrissam dentro do filho.** Tensão real: `.claude/skills/` e `.claude/agents/` são namespaces **planos** que precisam **misturar** comum (do hub) + específico (local), mas `git subtree` **é dono de um diretório inteiro** — ele não sabe mesclar dois donos no mesmo diretório. | **D1 (recomendado) — subtree em `.claude/kit/` + materialização.** O subtree aterrissa em `.claude/kit/` (versionado, nunca editado à mão) e um passo de sync copia para os namespaces planos `.claude/{skills,agents}/`. Custo: duas cópias dentro do filho — e é justamente aí que o **drift-guard (DP-5) ganha função real** (`kit/` × materializado; divergência = alguém editou a cópia). **D2 — um subtree por artefato:** 15 branches `git subtree split` no hub, cada artefato direto no caminho final; zero duplicação, mas 15 `subtree pull` por filho a cada atualização. **D3 — hub dono do `.claude/{skills,agents}` inteiro do filho:** inviável, `PantonicVideo` tem pipeline bespoke local que morreria. **Consequência operacional de D1:** a materialização sobrescreve o artefato de mesmo nome no filho, então o *escape hatch* de override (já decidido na Fase 0/1a para o bloco backend de `Container`/`ContainerForAWS`/`Patom`) **não pode ser implícito** — vira uma **lista de exclusão declarada** (`.claude/kit-exclude.txt`) que o sync respeita. "Override ESPECÍFICO **declarado**" passa a ser literal. |
| **DP-8** 🆕 **ABERTO — trava a Fase 4, não a Fase 3** | **Os 5 filhos não-`PantonicVideo` não são repositórios git** (medido 2026-07-25: `.claude/` presente, `.git/` ausente em `Scanlator`, `Monitor`, `Container`, `ContainerForAWS`, `Patom`). DP-1=D pressupõe filho-repo para `git subtree pull`. | **Recomendado: `git init` + remoto por filho**, mesmo racional do DP-6 — código de projeto sem controle de versão não tem rollback nem trilha, e sem isso a distribuição git simplesmente não alcança 5 dos 6 filhos. **Alternativa (fallback):** para filho que o dono queira manter fora do git, o kit chega por cópia a partir do clone local do hub (o `sync-kit.ps1` já faz isso — bastaria apontá-lo para o hub em vez de para `kit/`), abrindo mão de autocontenção e histórico naquele filho. **Decidir antes da Fase 4.** A Fase 3 valida o mecanismo em sandbox e **não** depende desta decisão. |

---

## 3. Arquitetura alvo (após DP-1 = D)

```
FONTE CANÔNICA (git remoto, revisável)        CADA FILHO (git próprio, arquivos nativos)
──────────────────────────────────────        ──────────────────────────────────────────
github.com/PantaTheDoggo/PantonicApp          <filho>/
  GOVERNANCA.md            ◄──── cita ──────    .claude/
  ARQUITETURA_PANTONICA.md ◄──── cita             README.md   → ponteiro p/ o hub (DP-3)
  .claude/                                        kit/        ◄─┐ git subtree pull
    skills/   ──── git subtree split ──────►        skills/     │ (comum; NUNCA editar aqui)
    agents/   ──── (branch `kit`)   ──────►         agents/    ─┘
                                                  skills/     → comum materializado + específico
                                                  agents/     → comum materializado + específico
                                               (materialização: passo de sync — DP-7=D1)

~/.claude/  → permanece SÓ com o genérico não-Pantonic (context-scout, lean-test, onboard, …).
              Nenhuma junção, nenhum symlink, nenhum privilégio de admin envolvido.
```

Uma decisão de governança comum passa a ser **1 commit no hub + `git subtree pull` por filho** —
nenhuma edição manual em filho nenhum. O filho continua **autocontido**: clonado numa máquina
nova, já traz o kit junto, sem exigir que o hub exista em disco.

---

## 4. Tarefas (fases)

> **Renumeração 2026-07-25 (2ª rodada):** com DP-1=D, o hub versionado deixou de ser o
> fechamento e virou o alicerce. A antiga **Fase 5** (`git init`/DP-6) subiu para **Fase 2**;
> a antiga Fase 2 (implementar o mecanismo) virou **Fase 3** e ganhou DP-7; as antigas Fases
> 3/4/5 viraram **4/5/6**.

### Fase 0 — Reconciliar a deriva viva [PRÉ-REQUISITO, destrava tudo] ✅ DONE (2026-07-25)
- **Objetivo:** promover ao canônico `PantonicApp/.claude/skills/{diario-de-obras,proximo-passo}` as
  melhorias de 2026-07-21 que hoje só existem em `PantonicVideo` (regra A/B/C de planos derivados,
  status `superseded`, guardrails do picker, guardrail anti-log-narrativo).
- **Pronto quando:** o canônico contém as regras; diff `PantonicVideo` × canônico nessas 2 skills =
  só o que for legitimamente específico (idealmente zero). Sem isso, qualquer centralização apaga a
  melhoria.

### Fase 1 — Congelar o canônico (curadoria) ✅ DONE (2026-07-25, dividida em 1a + 1b)
- **Objetivo:** auditar as 7 skills + 6 agentes comuns **entre os 6 filhos**, achar todo diff,
  decidir a versão de referência campo a campo, gravar no PantonicApp. Resolver naming do slot de
  auditor (DP-2).
- **Método:** `pantonic-scout`/`context-scout` (Haiku) produz o diff-matrix; curadoria no modelo
  caro só sobre os conflitos reais.
- **Pronto quando:** `PantonicApp/.claude/{skills,agents}` é a única verdade, sem perda de nenhuma
  melhoria dispersa nos filhos.

### Fase 2 — Regularizar o hub como repositório git remoto (DP-6) ✅ DONE (2026-07-25)
- **Objetivo:** o canônico deixa de ser uma pasta solta e vira repo git publicado — pré-requisito
  técnico de DP-1=D (é o remoto que os filhos consomem) e a rede de segurança que faltava para
  editar o canônico com rollback.
- **Feito:** `git init -b main`; `.gitignore` (settings locais de máquina, ruído de SO/editor);
  `.gitattributes` com `* text=auto eol=lf` (sem isso o diff hub×filho infla por CRLF e o
  drift-guard de DP-5 fica inutilizável — problema já medido na Fase 0); commit inicial `6068884`
  com os 23 arquivos canônicos; `remote add origin` + `push -u origin main`.
- **Pronto quando:** ✅ `git ls-remote origin` devolve `refs/heads/main`; working tree limpo;
  `main` rastreando `origin/main`.

### Fase 3 — Implementar e provar o mecanismo D1 em sandbox ← **PRÓXIMA TAREFA**

> **DOSSIÊ DE EXECUÇÃO — pronto para contexto novo.** Modelo: **Sonnet** (mecânica; Regra 7).
> Teto: **30 tool uses** — ao atingir, PARE e reporte em vez de continuar.
> Decisões já fechadas, **não reabrir**: DP-1=D, DP-7=D1.
> **Não depende de DP-8.** Nenhum filho real é tocado nesta fase.

**Por que sandbox e não um filho piloto:** a sondagem de 2026-07-25 mediu que os 5 filhos
candidatos a piloto **não são repositórios git** (DP-8) e que o único que é — `PantonicVideo` —
estava com **258 arquivos não commitados**, e `git subtree add` exige árvore limpa. Validar o
mecanismo num sandbox descartável separa "o desenho funciona" de "os filhos estão prontos", e não
gasta uma decisão do dono para começar.

**Proibições (raio de explosão):**
- **NÃO** rodar `git init` em nenhum filho (isso é DP-8, decisão do dono).
- **NÃO** tocar em `D:\workspaces\Pantonic*` além do hub — em especial, **não** commitar, stashar
  ou descartar nada da árvore suja do `PantonicVideo`.
- O sandbox vive no scratchpad da sessão, nunca em `D:\workspaces\`.

#### T1 — Hub: criar o materializador `.claude/sync-kit.ps1`
Script PowerShell, versionado no hub (viaja junto com o kit; no filho ele fica em
`.claude/kit/sync-kit.ps1`). Contrato:
- **Resolve caminhos por `$PSScriptRoot`**: o script está em `<filho>/.claude/kit/`; o destino é
  `Split-Path $PSScriptRoot -Parent` (= `<filho>/.claude/`). Sem caminho absoluto hardcoded.
- **Copia**, de `kit/` para o namespace plano: cada diretório `kit/skills/<nome>/` →
  `.claude/skills/<nome>/`; cada arquivo `kit/agents/<nome>.md` → `.claude/agents/<nome>.md`.
- **Lista de exclusão (o escape hatch declarado do DP-7):** lê `<filho>/.claude/kit-exclude.txt`
  se existir — um nome de artefato por linha, `#` = comentário. Nome casa com diretório de skill
  ou basename de agente sem `.md`. Artefato excluído é **pulado** (o override local sobrevive ao
  sync). Arquivo ausente = nenhuma exclusão.
- **Nunca apaga** nada cujo nome não venha do kit: artefato local que não existe no kit fica
  intocado. (Dentro de um diretório de skill gerenciado, o espelhamento é total — arquivo removido
  no hub some no filho.)
- **Idempotente:** rodar 2× seguidas produz o mesmo estado.
- **`-Check`:** só compara, não escreve; lista os artefatos gerenciados que divergem e sai com
  **exit 1** se houver divergência, 0 se limpo. (É a semente do drift-guard da Fase 5 e o critério
  de aceite desta fase.)
- Imprime resumo: N copiados, M pulados por exclusão.

#### T2 — Hub: publicar o branch `kit`
```
git subtree split --prefix=.claude -b kit
git push origin kit
```
O branch `kit` tem como **raiz** o conteúdo de `.claude/` (`skills/`, `agents/`, `README.md`,
`sync-kit.ps1`). Confirmar com `git ls-tree --name-only kit`.
*(`settings.json`/`settings.local.json` já estão no `.gitignore` do hub — não vazam para o kit.)*

#### T3 — Sandbox: provar `add` + materialização
No scratchpad: `git init` num sandbox limpo, simular um filho com **(a)** um agente local bespoke
não pertencente ao kit, **(b)** um `kit-exclude.txt` declarando 1 skill do kit como override
local, e **(c)** uma versão local divergente dessa skill excluída. Então:
```
git subtree add --prefix=.claude/kit <URL-do-hub> kit --squash
pwsh .claude/kit/sync-kit.ps1
```
**Aceite:** as skills/agentes do kit aparecem em `.claude/{skills,agents}`; o bespoke (a) segue
intocado; a skill excluída (c) **não** foi sobrescrita; `sync-kit.ps1 -Check` → exit 0.

#### T4 — Prova da tese (a razão de ser do plano)
Commitar **1 linha** numa skill comum **só no hub** → `git subtree split -b kit` + `push origin kit`
→ no sandbox `git subtree pull --prefix=.claude/kit <URL> kit --squash` + sync.
**Aceite:** a linha aparece no sandbox **sem nenhuma edição manual nele**; `-Check` → exit 0.
*(Reverter o commit-cobaia no hub ao final, ou usar uma linha de comentário inócua.)*

#### T5 — Registro
Apensar a `## Achados da execução` o resultado medido de T1-T4 (incluindo o comando exato de
`split`/`pull` que funcionou — a Fase 4 vai reusá-lo) e o placeholder literal
`Consumo: (preenchido pelo orquestrador via notificação)`. **Não** editar a célula de índice do
diário — o orquestrador escreve.

**Fora de escopo (não fazer aqui):** migrar filho real (Fase 4), estender `bootstrap-pantonic`
(Fase 4/5 — depende de DP-8), drift-guard como gate de conformance (Fase 5).

**Pronto quando:** T1-T5 com os aceites acima verdes; nenhum arquivo fora do hub e do scratchpad
modificado.

### Fase 4 — Migrar filho a filho  🔒 **BLOQUEADA por DP-8**
- **Pré-requisito:** DP-8 resolvido — os 5 filhos não-`PantonicVideo` **não são repos git** hoje,
  e `git subtree pull` exige que sejam. Além disso, `subtree add/pull` exige **árvore limpa**:
  `PantonicVideo` tinha 258 arquivos não commitados na medição de 2026-07-25 e precisa ser
  regularizado antes da sua vez.
- **Objetivo:** por filho (ordem: um de baixo risco primeiro, `PantonicVideo` por **último** por
  ser o mais divergente): substituir as cópias manuais de skills/agentes comuns pelo kit
  distribuído por git, deixar só o específico fora do caminho gerenciado, gravar o ponteiro
  `.claude/README.md` (DP-3). Declarar o slot de auditor de domínio.
- **Preservar (decisão do dono, Fase 0/1a):** o bloco backend de `Container`/`ContainerForAWS`/
  `Patom` (`guardrails-check`, `pantonic-auditor-arch`, `pantonic-fora-da-caixa`, `pantonic-scout`,
  `integrar-poc`) é **override ESPECÍFICO declarado**, não deriva — a migração **não** o sobrescreve.
  **Mecanicamente:** esses nomes entram no `.claude/kit-exclude.txt` do filho **antes** do primeiro
  sync. Sem isso a materialização os sobrescreve silenciosamente.
- **Pronto quando:** cada filho tem o comum vindo do hub + o específico local intacto; nenhuma
  regressão de invocação de skill/agente.

### Fase 5 — Guardrail + inversão da doutrina
- **Objetivo:** drift-guard (DP-5) — em DP-7=D1 ele compara `.claude/kit/` × o materializado, e o
  filho × o hub; **reescrever GOVERNANCA §9 e o `.claude/README.md` do kit** para inverter a
  doutrina de *"todo projeto copia o kit"* para *"o comum vem do hub por git; filho só carrega o
  específico; mudança comum = 1 commit no hub + pull nos filhos"*.
- **Pronto quando:** a doutrina escrita reflete o novo modelo; o guarda falha sob divergência
  simulada.

### Fase 6 — Fechamento
- **Objetivo:** o hub ganha diário de obras próprio como dono do backlog de governança comum;
  decision record cobrindo **DP-1..DP-8** (incluindo a troca A→D e o porquê medido); promover ao
  `GOVERNANCA.md` a lição de sondagem de viabilidade registrada nos achados (toda DP que escolhe
  mecanismo de plataforma traz a sonda junto da recomendação) — **duas premissas caíram nesta
  sprint** pelo mesmo motivo (symlink/admin e filho-não-é-repo), o que a qualifica como regra.
- **Pronto quando:** decision record escrito; o hub tem trilha auditável; este plano fecha.

---

## 5. Verificação end-to-end
1. Commitar 1 linha numa skill comum **só no hub**, `push`, e confirmar que um `subtree pull` em 2
   filhos distintos traz a mudança **sem nenhuma edição manual neles** (a prova da tese).
2. Invocar 1 skill comum e 1 agente comum em `PantonicVideo` e num filho "container" — ambos
   resolvem do kit distribuído.
3. Um filho consegue **sobrepor** uma skill comum declarando-a em `.claude/kit-exclude.txt`, e o
   `subtree pull` + sync seguintes **não** apagam o override.
4. Drift-guard (`sync-kit.ps1 -Check`) falha quando alguém edita à mão a cópia materializada em
   vez do hub.
5. `bootstrap-pantonic` num projeto-sandbox novo instala o kit por git (não por cópia manual).
6. **Autocontenção:** clonar um filho já migrado numa pasta limpa, **sem o hub em disco**, e
   confirmar que as skills/agentes comuns estão lá e são invocáveis.

## 6. Riscos
- **Filhos não são repos git** (5 de 6, medido) e `PantonicVideo` está com árvore suja — DP-1=D
  não alcança nenhum deles até DP-8 ser resolvido. **Este é o risco dominante do plano hoje.**
  Mitigação: Fase 3 valida em sandbox e não fica refém da decisão; Fase 4 declara o bloqueio.
- **Override local sobrescrito silenciosamente** pela materialização (D1). Mitigação: o
  `kit-exclude.txt` precede o primeiro sync do filho; `-Check` denuncia divergência.
- **Conflito de merge no `subtree pull`** se alguém editar a cópia materializada no filho em vez do
  hub. Mitigação: `.claude/kit/` declarado read-only por doutrina (Fase 5) + drift-guard (DP-5)
  pegando a edição indevida antes de virar conflito.
- **Duplicação interna em DP-7=D1** (`kit/` + materializado no mesmo filho): é o preço de namespace
  plano. Mitigação: materialização por comando idempotente, nunca à mão; drift-guard compara os dois.
- **Divergência de line-ending** entre hub (LF) e filhos com `core.autocrlf=true` reintroduzindo
  ruído de diff. Mitigado na Fase 2 pelo `.gitattributes` do hub; **os filhos precisam do mesmo**
  na Fase 4.
- **Perda de melhoria dispersa** se Fase 1 não achar todo diff antes de congelar. Mitigação: Fase 0
  explícita + diff-matrix completo em Fase 1 antes de qualquer remoção. *(Coberto — 0/1a/1b done.)*
- **Especialização legítima virar "deriva"**: distinguir override intencional (escape hatch,
  declarado) de cópia acidental (o que o drift-guard pega). Documentar a diferença.
- **~~Junção/symlink dependente do path do PantonicApp~~** — risco **extinto** pela troca para
  DP-1=D; nenhum link local no desenho novo.

## 7. Rollback
Cada fase é reversível. A partir da **Fase 2** (hub em git, `push` feito) o canônico tem rollback
por commit — foi exatamente por isso que ela subiu para antes da implementação do mecanismo. Nos
filhos, a Fase 4 é reversível por `git revert` do commit de `subtree add`, e o estado pré-plano
continua recuperável enquanto o canônico retém tudo (Fase 1 congelou sem perda).

## Achados da execução
(a preencher na execução)

### 2026-07-25 — Fase 0 concluída (Reconciliar a deriva viva)

**Emenda de escopo (autorizada pelo dono, 2026-07-25):** o texto original da Fase 0 nomeava só
`diario-de-obras` e `proximo-passo`. Medição no início da execução mostrou deriva viva também em
`handover` e `guardrails-check` (deriva PantonicVideo × canônico, em linhas de diff bruto medidas
com `diff | wc -l`: diario-de-obras 247, proximo-passo 287, handover 169, guardrails-check 128).
O dono estendeu o escopo da Fase 0 de 2 para as 4 skills na mesma execução.

**Promovido ao canônico, por skill:**
- `diario-de-obras`: status `superseded` (+ semântica dos 3 terminais); guardrail "célula do
  índice nunca recebe prosa de execução"; seção inteira "Planos derivados de uma investigação em
  curso" (regras A/B/C, regra de convergência, guardrail anti-log-narrativo); regra de tíquete
  nascido de achado vivendo em `## Achados da execução` do plano-pai.
- `proximo-passo`: delegar a agente mais especializado quando o domínio já tiver um (ex.
  `clean-code`, `architect-auditor`) em vez do executor genérico por padrão; regra ">8
  write-clusters → dividir em sub-tarefas antes de delegar" (evidência medida UXROUND3 T3
  56/35, T4 61/40, T5 112/50 viajou junto com a regra); guardrails novos — nunca escolher plano
  `superseded`, protocolo de convergência de iniciativa (rebase antes de escolher 2+ planos
  vivos), e plano `blocked` por decisão owner-gated (DP-*) não é delegável ao executor.
- `handover`: guardrail "nunca preencher a célula do índice" (mesmo mecanismo do
  `diario-de-obras`, aplicado ao ato de fechar); "Achado fora de escopo" passa a exigir entrada
  na seção `## Achados da execução` do plano-pai (não só tíquete solto) + linha de índice com
  âncora; novo "Gate de triagem no fechamento de sprint" (sprint só vira `done` com todo achado
  do plano triado); referência ao gate mínimo Tier 2 / Tier 3 condicional no passo 1; teto de
  ~15 linhas na mensagem final.
- `guardrails-check`: reestruturação do checklist executável em Tier 1/Tier 2/Tier 3 (alinhado
  às skills globais `lean-test`/`test-tiers`, já presentes no kit); regra "executor não roda
  Tier 3 por conta própria em raio de explosão alto — recomenda, dono/orquestrador decide";
  clarificador de MVVM (`QScreen`, `infracore/ui_shell/`) e nome do serviço
  (`task_runner_service`); nova seção "Padrão de código (limiares canônicos)" com os limiares
  numéricos automáticos (ruff C901/F401/F841/E501) e manuais (>7 métodos públicos, duplicação
  ≥6 linhas); template estruturado de "Veredito" com exigência de `path:line` por desvio.

**Residuais ESPECÍFICO (ficam só na cópia local do PantonicVideo, com justificativa):**
- Todos os 4 arquivos: parágrafo de atribuição "cópia local, adaptada, do kit... (caminho
  `D:\workspaces\PantonicApp\...`)" — autorreferência que só faz sentido numa cópia, não no
  próprio canônico.
- Todos os 4 arquivos: citações a `CLAUDE.md`/Regra N em vez de `GOVERNANCA.md` §N — o canônico
  já cita a si mesmo (`GOVERNANCA.md`); o PantonicVideo cita o próprio `CLAUDE.md` global/local
  que espelha a mesma regra.
- `handover`: "decisão do dono 2026-07-16" e "(precedente: triagem T4 de
  `P-0714-triagem-consolidada`)" — datas/IDs de plano específicos do histórico do PantonicVideo;
  a regra em si (rota obrigatória para achado fora de escopo; gate de triagem no fechamento de
  sprint) foi promovida, só a citação de precedente ficou de fora.
- `handover`: pointer "ver CLAUDE.md 'Test execution tiers'" — nome de seção específico do
  `CLAUDE.md` do PantonicVideo; o canônico aponta para a skill `guardrails-check` em vez disso.
- `guardrails-check`: bullet "Construção eager/ordem fixa dos components... tabela de contenção
  de falhas (`docs/ARCHITECTURE.md` §13.1)" — invariante de boot documentada só no
  `ARCHITECTURE.md` do PantonicVideo (lista concreta de components: Injector→Signal→
  Filesystem→AppState→Logging→PluginRegistry), não uma doutrina genérica do kit.
- `guardrails-check`: bullet GQ-10 sobre `Timeline`/`TimelineSegment` e os builders
  `screenwriter`/`language_swapper` — amarrado a contratos e plugins que só existem no
  PantonicVideo (`contracts/domain/timeline.py`, `plugins/screenwriter/...`).
- `guardrails-check`: tags `GQ-04`/`GQ-02`/`SPRINT-GUARDQUALITY`/`D-GQ-02-1` e o caminho
  `tests/conformance/test_static_quality.py` na seção "Padrão de código" — os limiares
  numéricos em si foram promovidos (COMUM), mas os identificadores de sprint/arquivo de teste
  concreto do PantonicVideo ficaram de fora do canônico (generalizado para "gate de
  conformance" sem apontar um arquivo que pode não existir nos outros filhos).
- `guardrails-check`: exemplo "R10/R14 em `docs/plans/P-0706-redesign-fora-da-caixa.md`" e nome
  de arquivo `docs/AS-IS_DECISIONS.md` — plano e doc concretos do PantonicVideo; o canônico
  generalizou para "gate de fechamento previsto no próprio plano" / "doc AS-IS".
- Vários pontos de reflow de parágrafo sem mudança de conteúdo (quebra de linha diferente) —
  não são divergência de regra, artefato do merge cirúrgico por bloco.

**AMBÍGUOS — nenhum.** Nenhum bloco divergente exigiu decisão de doutrina do dono nesta rodada;
todos foram classificáveis por COMUM/ESPECÍFICO/SÓ-NO-CANÔNICO com confiança.

**SÓ-NO-CANÔNICO preservado (confirmado, não perdido):** `guardrails-check`, bullet "Sinais
usados só para observação (sem polling)? Payload é Pydantic `extra="forbid"`?" — existe no
canônico, ausente na cópia PantonicVideo; mantido intacto (não fazia parte da promoção).

**Nota:** a medição de linhas de diff feita durante a execução usou `diff --strip-trailing-cr`
(a cópia PantonicVideo tem terminadores CRLF, o canônico LF; `diff` puro infla a contagem por
tratar toda linha como diferente por causa do `\r`). Números finais residuais, mesmo comando:
diario-de-obras 25, proximo-passo 21, handover 29, guardrails-check 71 (linhas de diff
`--strip-trailing-cr`, não comparável 1:1 à tabela de medição inicial que usava `diff` puro).

Consumo (medido pelo orquestrador via notificação de conclusão): 35 tool uses, ~150k tokens,
Sonnet, ~182 min de wall-clock (duração de sessão do subagente, inclui espera — não é tempo de
trabalho contínuo). Dentro do teto de 35 fixado no dossiê.

### 2026-07-25 — Fase 1a concluída (curadoria das skills)

**Método:** os 14 diffs mapeados no dossiê (`diff --strip-trailing-cr <hub> <filho>` sobre um
representante por grupo de versões idênticas) foram lidos integralmente para as 6 skills em
escopo (`bootstrap-pantonic`, `diario-de-obras`, `guardrails-check`, `handover`, `integrar-poc`,
`proximo-passo`), sobre os 5 filhos não-PantonicVideo (`Container`, `ContainerForAWS`, `Monitor`,
`Patom`, `Scanlator`).

**Promovido ao canônico, por skill: nenhuma.** Resultado da curadoria: toda linha só-do-filho
(`>`) nos 14 diffs caiu em STALE ou ESPECÍFICO — nenhum bloco atendia ao critério COMUM (regra/
guardrail genérico ausente do canônico). Explicação de fundo: a Fase 0 já promoveu ao canônico,
a partir do `PantonicVideo` (o filho mais divergente/à frente em governança), praticamente todo o
ganho vivo em `diario-de-obras`/`proximo-passo`/`handover`/`guardrails-check`; os 5 filhos
restantes ainda não migraram essas mudanças para as próprias cópias (isso é Fase 3, não Fase 1a) —
por isso quase toda linha `>` nestes diffs é STALE: fraseado mais antigo de algo que o canônico já
superou (ex.: `diario-de-obras`/`handover`: status sem `superseded`, ausência do guardrail "célula
do índice nunca recebe prosa", ausência da seção "Planos derivados A/B/C", template de Veredito
resumido em vez do estruturado; `guardrails-check`: estrutura de teste pré-Tier1/2/3;
`proximo-passo`: ausência de "delegar a agente mais especializado", ausência do teto ">8
write-clusters", ausência da regra `superseded`/convergência de iniciativa). Nada disso é
melhoria nova — é o canônico já correndo à frente do que a Fase 3 vai empurrar para os filhos.

**Residual ESPECÍFICO por filho (fica só na cópia local, não sobe):**
- `bootstrap-pantonic` (Container, ContainerForAWS): passo do core estendido para 8 etapas com
  "runtime shell mínima (app factory + /health + /ready + graceful shutdown) + Dockerfile
  multi-stage + compose.yaml", "smoke de container (vira gate de release)" e listagem
  `Dockerfile  compose.yaml  .dockerignore` na árvore de pastas — arquitetura de serviço
  containerizado, não aplicável a filhos sem Docker.
- `guardrails-check` (Container): descrição do skill menciona "transporte estrito"/"12-factor"
  em vez de "MVVM"; checklist "Handlers continuam finos / Framework de transporte só em
  runtime_shell e `transport.py` / DTO de borda / Config via ConfigService / stdout estruturado /
  escrita só no data dir montado"; tier de teste extra "Smoke de container (`tests/container/`)"
  — todo esse bloco é o guardrail-check equivalente ao MVVM da hub, só que para arquitetura de
  serviço backend (transport.py/FastAPI/ConfigService); não é uma versão melhor do mesmo item, é
  o item análogo para outro arquétipo.
- `integrar-poc` (Container, ContainerForAWS, Patom): "Condições de integrabilidade" reescritas
  em torno de rede/banco/broker/engine mapeável a serviço ACL, GPU só se declarada no runtime da
  imagem, `ConfigService`, superfície de borda via `transport.py`/`APIRouter` sob
  `/plugins/<nome>`, allowlist de conformance com `fastapi.*` — todo o vocabulário é de serviço
  HTTP/container, paralelo ao vocabulário PySide6/ViewModel do canônico, não uma generalização
  dele.

**AMBÍGUOS (decisão de doutrina do dono, não decidido aqui):**
1. `proximo-passo` canônico, passo "Delegar execução" (linhas ~47-53): o texto nomeia o agente
   fixo `pantonic-executor` e a frase "guardrails de arquitetura (regra de camadas, MVVM, ACL) já
   vivem nos 'fatos estáveis' de `pantonic-executor.md`" — `ContainerForAWS`/`Monitor`/`Patom`
   (grupo >10) já usam fraseado genérico ("guardrails de arquitetura já vivem nos 'fatos
   estáveis' do arquivo do agente", sem citar MVVM nem o nome do arquivo). Isso é plausivelmente
   uma melhoria COMUM (o canônico deveria falar do executor de forma agnóstica de arquétipo), mas
   o nome do agente-alvo da delegação é explicitamente Fase 1b (agentes) — mexer nisso agora
   cruzaria o limite de escopo desta tarefa. Não promovido; fica para o dono decidir se entra em
   Fase 1a (fraseado da skill) ou só em Fase 1b (nome do agente).
2. `guardrails-check`: os bullets "Chamadas de rede novas têm timeout?" e "Config nova entra por
   ConfigService (env)?" (só em Container/Monitor, arquétipo backend) descrevem princípios que
   PODERIAM generalizar para qualquer Pantonic* com chamadas de rede/config externa — mas exigem
   reescrever o checklist canônico como condicional por arquétipo (UI/MVVM vs. serviço/transport)
   em vez de uma lista única. Doutrina não decidida: o canônico deve ganhar branches por
   arquétipo, ou continua sendo o "perfil UI" e cada arquétipo mantém seu próprio adendo
   ESPECÍFICO (como hoje)? Não promovido.

**Resolução dos AMBÍGUOS (dono, 2026-07-25, `AskUserQuestion` em lote):**
- **(1) `guardrails-check` → "continuar perfil-UI + adendos".** O canônico NÃO ganha ramos por
  arquétipo: mantém o checklist MVVM/PySide6 como perfil único, e o bloco backend
  (transport/`ConfigService`/smoke de container) de `Container`/`ContainerForAWS`/`Patom` passa a
  ser **override ESPECÍFICO declarado** (escape hatch da DP-1), não deriva. Consequência para a
  Fase 3: a migração desses 3 filhos preserva o override em vez de sobrescrevê-lo.
- **(2) `proximo-passo` (fraseado agnóstico de agente) → Fase 1b.** A generalização depende do
  naming do slot de executor/auditor no canônico (DP-2), objeto da Fase 1b; tratar junto para não
  decidir o mesmo naming duas vezes. A Fase 1a fecha sem essa promoção, por decisão, não por
  omissão.

**Achado fora de escopo — fechado (TK-SGSS-ARQUETIPO, ver `P-0725-governanca-tres-camadas.md`
§1.2):** `bootstrap-pantonic` hub referencia `ARQUITETURA_PANTONICA §15` no passo do core;
Container/ContainerForAWS referenciam `§16` no mesmo ponto. Medido em §1.2: **não é deriva** —
é especialização legítima (o Container insere um §12 próprio, que desloca a numeração
subsequente). Sem ação pendente.

**Medição final (re-rodada, `diff --strip-trailing-cr <hub> <filho> | grep -c '^>'`,
representante por grupo) — idêntica à inicial, porque nenhum merge foi aplicado ao canônico:**
bootstrap-pantonic: Container 11 · ContainerForAWS 11 · Monitor 2 · Scanlator 2.
diario-de-obras: Container 1 · Scanlator 3.
guardrails-check: Container 30 · Monitor 21.
handover: Container 7 · Scanlator 4.
integrar-poc: Container 15 · Monitor 0.
proximo-passo: Container 3 · ContainerForAWS 10 · Scanlator 9.

**Decomposição da Fase 1 (decisão do orquestrador, 2026-07-25):** a Fase 1 do plano descreve
"7 skills + 6 agentes" como uma tarefa só, mas a medição de escopo deu ~9 arquivos canônicos
candidatos a escrita — acima do teto de 8 write-clusters que obriga divisão antes de delegar.
Dividida em **Fase 1a (skills — esta)** e **Fase 1b (agentes + DP-2 + varredura reversa de
artefatos presentes num filho e ausentes do canônico, ex.: `pantonic-auditor-container.md`,
que DP-2 manda existir no hub e hoje não existe)**.

Consumo (medido pelo orquestrador via notificação de conclusão): 16 tool uses, ~94k tokens,
Sonnet, ~5,4 min. Teto do dossiê era 40 tool uses.

### 2026-07-25 — Fase 1b concluída (curadoria dos agentes + DP-2 + varredura reversa)

**Método:** medição direta (`diff --strip-trailing-cr <hub> <filho> | grep -c '^>'`) dos 6
agentes comuns (`pantonic-planner`, `pantonic-executor`, `pantonic-scout`, `pantonic-auditor-arch`,
`pantonic-auditor-cleancode`, `pantonic-fora-da-caixa`) contra os 5 filhos não-`PantonicVideo`,
mais o slot de auditor de domínio (`pantonic-auditor-pyside6`/`pantonic-auditor-container`, DP-2).
Executado inline pelo orquestrador (tarefa pequena, <15 turnos estimados — Regra 7) em vez de
delegado.

**Promovido ao canônico:** `pantonic-executor.md`, bullet "Economia de turnos" — hub e filhos
tinham cada um metade da cláusula de orçamento (hub só "não é punição"; os 5 filhos só "reportar
no handover, não só continuar"), nenhum lado com o texto completo do `CLAUDE.md` global Regra 7
de origem. Unificado no canônico: "estourar não é punição — sinal de decomposição errada; reportar
no handover, não só continuar".

**Varredura reversa (DP-2):** `pantonic-auditor-container.md` existe idêntico em `Container`/
`ContainerForAWS`/`Patom`, ausente do canônico — criado em `PantonicApp/.claude/agents/` (cópia
exata, DP-2 manda ambas as variantes viverem no hub). `pantonic-auditor-pyside6.md` já existia no
canônico e já era idêntico a `Monitor`/`Scanlator` — nada a fazer.

**Classificado ESPECÍFICO (não promovido) — aplicação do precedente Fase 0 AMBÍGUO #2:**
`pantonic-auditor-arch.md`, `pantonic-fora-da-caixa.md`, `pantonic-scout.md` divergem de forma
idêntica entre si nos 3 filhos-container (`Container`/`ContainerForAWS`/`Patom`, sempre o mesmo
texto): bullets reescritos de fronteira MVVM (ViewModel/`view_model.py`) para fronteira de
transporte (`transport.py`/handler fino). Mesma pergunta de doutrina já resolvida em Fase 0 para
`guardrails-check` ("canônico continua perfil-UI/MVVM; bloco backend é override ESPECÍFICO
declarado, não vira ramo no canônico") — aplicada aqui por analogia direta ao mesmo padrão
recorrente, não uma decisão de doutrina nova. Não promovido; residual fica só nas cópias locais
dos 3 filhos-container.

**AMBÍGUOS — nenhum novo** (a única pergunta de doutrina latente é a mesma já resolvida em Fase 0).

Consumo (medido pelo orquestrador via notificação de conclusão): execução inline, 23 tool uses
(9 diff/leitura + 2 escrita + 1 handover), Sonnet, sessão contínua. Teto informal ~15 turnos
(Regra 7, tarefa pequena) — dentro do orçamento.

### 2026-07-25 — Fase 2 ORIGINAL abortada (DP-1=A inviável) + troca para DP-1=D

**O que aconteceu:** ao iniciar a Fase 2 original (materializar junções/symlinks de `~/.claude`
para o hub), a sondagem de viabilidade **derrubou a premissa central de DP-1=A**:

| sonda | resultado |
|---|---|
| `New-Item -ItemType Junction` (diretório, C:→D:) | ✅ **OK sem elevação** — junção de diretório funciona |
| `New-Item -ItemType SymbolicLink` (arquivo, C:→D:) | ❌ **"Administrator privilege required"** |
| Developer Mode (`HKLM:\...\AppModelUnlock`) | ❌ **não habilitado** nesta máquina |

Consequência: os **7 skills** são pastas → junção resolveria; os **8 agentes** são `.md` soltos num
namespace plano → exigiriam symlink de arquivo (bloqueado) ou junção da pasta `agents/` inteira —
o que **sequestraria `~/.claude/agents/context-scout.md`**, um agente genérico não-Pantonic usado
pela skill global `context-prep`. Hard link foi descartado por não atravessar volumes (C: × D:).
DP-1=A entregaria, na melhor das hipóteses, metade do kit.

**Decisão do dono (2026-07-25):** abandonar a herança por link e adotar **DP-1=D — distribuição
git**: hub publicado como repo remoto, filhos consomem por `git subtree pull`, artefatos ficam
nativos e versionados dentro do filho ("clona só a parte que interessa e atua como se fosse do
projeto"). O plano inteiro foi revisado nesta rodada para o novo mecanismo: §3 (arquitetura alvo),
§4 (fases renumeradas), §5 (verificação), §6 (riscos), §7 (rollback), DP-1 reescrito, DP-6 marcado
cumprido, **DP-7 aberto**.

**Lição (candidata a subir para GOVERNANCA):** decisão de mecanismo owner-gated foi fechada
(DP-1=A, 2026-07-25) **sem uma sonda de viabilidade de 2 comandos**. A sonda que a derrubou custou
menos que a redação da própria decisão. Toda DP que escolhe um **mecanismo de plataforma**
(symlink, junção, permissão, path) deve trazer o resultado da sonda junto da recomendação, não
depois.

### 2026-07-25 — Fase 2 NOVA concluída (regularizar o hub como repo git remoto, DP-6)

**Feito:** `git init -b main` em `D:\workspaces\PantonicApp`; `.gitignore` (settings locais de
máquina — `.claude/settings*.json` —, ruído de SO/editor, `*.log`, `scratchpad/`); `.gitattributes`
com `* text=auto eol=lf`; commit inicial **`6068884`** com **23 arquivos** (2 docs de governança,
`Base.txt`, 3 docs de plano, 7 skills, 8 agentes, `.claude/README.md`, os 2 arquivos de config);
`remote add origin https://github.com/PantaTheDoggo/PantonicApp.git`; `push -u origin main`.

**Verificado:** `git ls-remote origin` → `60688845… refs/heads/main`; `git status --short --branch`
→ `## main...origin/main` (working tree limpo, sem divergência).

**Checagem pré-publicação:** varredura de credenciais (`api_key|secret|token=|sk-|ghp_|AKIA|
BEGIN .*PRIVATE`) antes do push — os 2 únicos hits eram a **palavra** "secret" no checklist do
`pantonic-auditor-container.md` (texto que fala *sobre* vazamento de segredo), nenhuma credencial.
Conteúdo publicado = documentação de governança/arquitetura + definições de skills e agentes.

**Por que `.gitattributes` entrou aqui e não na Fase 5:** a Fase 0 já tinha medido que a mistura
CRLF (filhos) × LF (hub) inflava o diff a ponto de exigir `--strip-trailing-cr` em toda medição.
Sem normalização no hub, o drift-guard de DP-5 nasceria comparando terminadores de linha em vez de
regras. Custo de 4 linhas agora, contra reescrever histórico depois.

Consumo: execução inline pelo orquestrador (Opus — fase de arquitetura/revisão de plano, Regra 7),
~45 tool uses na sessão contínua, cobrindo sondagem de viabilidade + 2 rodadas de decisão do dono +
Fase 2 + revisão integral do plano. **Auto-relato, não medido por `<usage>`** (execução inline não
gera notificação de subagente) — tratar como piso, não como medida.

### 2026-07-25 — DP-7 fechado (=D1) + DP-8 aberto pela sondagem de prontidão dos filhos

**DP-7 = D1** (subtree em `.claude/kit/` + materialização), aceito pelo dono conforme recomendação.
Consequência que virou requisito de implementação: como a materialização sobrescreve o artefato de
mesmo nome, o *escape hatch* de override — já decidido na Fase 0/1a para o bloco backend de
`Container`/`ContainerForAWS`/`Patom` — **não pode ser implícito**. Vira `.claude/kit-exclude.txt`,
lista declarada que o `sync-kit.ps1` respeita. "Override ESPECÍFICO **declarado**" passa a ser
literal, não retórico.

**Sondagem antes de redigir o dossiê da Fase 3 (aplicando a lição da rodada anterior):**

| sonda | resultado |
|---|---|
| `git subtree` disponível nesta instalação | ✅ existe (exit 129 = mensagem de uso) |
| `Scanlator`, `Monitor`, `Container`, `ContainerForAWS`, `Patom` são repos git? | ❌ **nenhum** — `.claude/` presente, `.git/` ausente nos 5 |
| `PantonicVideo` é repo git? | ✅ sim (`master`, remoto `origin`) — mas **258 arquivos sujos** |

**Segunda premissa derrubada nesta sprint.** DP-1=D pressupõe filho-repo para `git subtree pull`;
5 dos 6 filhos não são. E `subtree add/pull` exige árvore limpa, o que desqualifica o único filho
que é repo como piloto. → **DP-8 aberto** (fazer dos filhos repos git, ou fallback por cópia).

**Efeito no desenho das fases:** a Fase 3 foi redesenhada de "piloto num filho real" para
**"provar o mecanismo em sandbox descartável"**. Isso desacopla *o desenho funciona* de *os filhos
estão prontos*, e — o ponto prático — deixa a Fase 3 **executável imediatamente, sem gastar uma
decisão do dono**. DP-8 passa a travar só a Fase 4.

**Reforço da lição de sondagem (agora com 2 ocorrências na mesma sprint):** a primeira derrubou
DP-1=A (symlink exige admin); a segunda derrubou a premissa de piloto da Fase 3 (filho não é repo).
Ambas custaram ~2 comandos e teriam evitado, cada uma, uma fase inteira mal desenhada. Promover a
regra ao `GOVERNANCA.md` está agendado na Fase 6.
