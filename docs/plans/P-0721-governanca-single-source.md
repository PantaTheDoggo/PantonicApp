# P-0721 — Governança Pantonic* single-source: PantonicApp como repositório de referência

**Origem:** pedido do dono (2026-07-21). Dor declarada: toda alteração na governança comum obriga
a reajustar todos os filhos à mão. Meta: **PantonicApp = fonte única canônica** das decisões que
afetam todos os filhos; cada filho guarda **só o específico** + **ponteiros** para o comum.

**Planejador:** Opus (fase de arquitetura/planejamento, Regra 7). **Executor:** a definir por fase
(Fase 0-1 = curadoria/arquitetura → Opus/dono; Fases 2-4 = mecânica de migração → Sonnet).

**Estado:** DECISÕES FECHADAS — DP-1..DP-6 resolvidas pelo dono 2026-07-25 (todas conforme a
recomendação: DP-1=A junção/symlink, DP-2..DP-5 aceitas como redigidas, DP-6=Sim). Fase 0 done;
Fase 1 dividida em 1a (skills, done — zero promoções) e 1b (agentes + DP-2 + varredura reversa,
done — 1 promoção em `pantonic-executor.md` + `pantonic-auditor-container.md` criado no canônico).
Curadoria de Fase 0/1a/1b executada em Sonnet, não Opus/dono como o texto original previa (precedente
medido nas 3 rodadas: escopo suficientemente mecânico/bounded). Próxima tarefa: **Fase 2**
(materializar o mecanismo de herança DP-1=A).

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

**Achado estrutural:** `PantonicApp` **não é um repositório git hoje** (`git rev-parse` → exit 128)
e não tem `docs/`. Para ser "o repositório referenciado" com histórico/revisão/rollback de
decisões de governança, provavelmente deve virar um repo git. → DP-6.

---

## 2. Decisões (owner-gated — cada uma com recomendação)

| id | pergunta | recomendação |
|---|---|---|
| **DP-1** | **Mecanismo de "fonte única + herança"** (o coração) | **A — Herança global ancorada no canônico.** O kit comum (skills + agentes) é resolvido a partir de `~/.claude/{skills,agents}`, cujo conteúdo é **junção de diretório (Windows) / symlink (POSIX) apontando para os artefatos canônicos de `PantonicApp/.claude/`**. Editar no PantonicApp = vivo em todos instantaneamente; **zero cópia, zero propagação**. Junção no Windows (`mklink /J`) **não exige admin**. Filho guarda só o específico + ponteiro. **B (fallback robusto a mover repos):** script de deploy que COPIA `PantonicApp/.claude/{skills,agents}` → `~/.claude/` (rodado por um comando de sync/`bootstrap-pantonic`); custo = 1 comando após cada mudança, não 6 edições. **C (rejeitado como default):** manter cópia por filho + só um drift-guard — não atinge single-source. **Escape hatch (vale p/ A e B):** um filho que precise especializar uma skill comum a sobrepõe colocando uma de mesmo nome no seu `.claude/skills/` local (precedência de projeto). |
| **DP-2** | **Home do slot de auditor de domínio variante** (`pyside6` × `container`) | Manter **ambos no canônico** como variantes nomeadas do kit; o filho **declara qual usa** (ponteiro/fato estável), não recria o arquivo. Assim uma melhoria no corpo comum do auditor de arquitetura beneficia os dois sem duplicar. |
| **DP-3** | **Como os filhos referenciam os docs comuns** (`GOVERNANCA`/`ARQUITETURA_PANTONICA`) | **Ponteiro fino padronizado** `.claude/README.md` em cada filho (5/6 já têm um README — repurpose; `PantonicVideo` ganha um novo): cita o caminho canônico + a regra "não editar cópia; o comum vive no PantonicApp/`~/.claude`; só o específico mora aqui". Mantém a citação por caminho absoluto que já funciona. |
| **DP-4** | **Tratamento do outlier `PantonicVideo`** | (a) Reconciliar a deriva viva (promover as edições A/B/C + `superseded` ao canônico — Fase 0); (b) realinhar o subconjunto de skills ao kit comum (ganha as 3 que faltam por herança); (c) **classificar o pipeline de integração bespoke como específico** — fica local, fora do kit comum. |
| **DP-5** | **Guarda de deriva (drift-guard)** | Check leve de conformance que **falha se um artefato comum divergir do canônico** (hash/diff de `~/.claude` ou do filho contra `PantonicApp/.claude`). Complementa DP-1 como rede de segurança — detecta cópia manual acidental ou junção quebrada. |
| **DP-6** | **`PantonicApp` deve virar repositório git?** | **Sim (recomendado).** Fonte canônica de governança sem histórico/PR/rollback é frágil. `git init` + `.gitignore` mínimo; decisões de governança passam a ter trilha auditável. Alternativa: manter fora do git e confiar em backup — **rejeitada** para o papel de "repositório de referência". |

---

## 3. Arquitetura alvo (após DP-1 = A)

```
FONTE CANÔNICA (git, revisável)          RUNTIME (resolução de skills/agentes)
────────────────────────────            ─────────────────────────────────────
PantonicApp/                             ~/.claude/
  GOVERNANCA.md            ◄──── cita ─────  CLAUDE.md         (Regras globais 1-7)
  ARQUITETURA_PANTONICA.md ◄──── cita        skills/
  .claude/                                     diario-de-obras ─╮ junção/symlink
    skills/  ◄───────────── junção/symlink ────  proximo-passo   ├─► PantonicApp/.claude/skills/*
    agents/  ◄───────────── junção/symlink ────  handover ...   ─╯
                                               agents/  ─► PantonicApp/.claude/agents/*

CADA FILHO/.claude/                       (herda tudo acima de ~/.claude, sem cópia)
  README.md            → ponteiro: comum vive no PantonicApp; só específico aqui
  skills/              → APENAS específico do filho (se houver)
  agents/              → APENAS específico (slot de domínio declarado + bespoke)
```

Uma decisão de governança comum passa a ser **1 edição no PantonicApp** — nenhuma propagação.

---

## 4. Tarefas (fases)

### Fase 0 — Reconciliar a deriva viva [PRÉ-REQUISITO, destrava tudo]
- **Objetivo:** promover ao canônico `PantonicApp/.claude/skills/{diario-de-obras,proximo-passo}` as
  melhorias de 2026-07-21 que hoje só existem em `PantonicVideo` (regra A/B/C de planos derivados,
  status `superseded`, guardrails do picker, guardrail anti-log-narrativo).
- **Pronto quando:** o canônico contém as regras; diff `PantonicVideo` × canônico nessas 2 skills =
  só o que for legitimamente específico (idealmente zero). Sem isso, qualquer centralização apaga a
  melhoria.

### Fase 1 — Congelar o canônico (curadoria)
- **Objetivo:** auditar as 7 skills + 6 agentes comuns **entre os 6 filhos**, achar todo diff,
  decidir a versão de referência campo a campo, gravar no PantonicApp. Resolver naming do slot de
  auditor (DP-2).
- **Método:** `pantonic-scout`/`context-scout` (Haiku) produz o diff-matrix; curadoria no modelo
  caro só sobre os conflitos reais.
- **Pronto quando:** `PantonicApp/.claude/{skills,agents}` é a única verdade, sem perda de nenhuma
  melhoria dispersa nos filhos.

### Fase 2 — Implementar o mecanismo (DP-1)
- **Objetivo:** materializar a herança escolhida — junções/symlinks `~/.claude/{skills,agents}` →
  `PantonicApp/.claude/` (A) **ou** script de deploy idempotente (B). Estender `bootstrap-pantonic`
  para instalar a herança em vez de copiar.
- **Pronto quando:** um projeto novo e um filho existente resolvem o kit comum sem cópia local;
  smoke test invocando 1 skill comum em 2 projetos distintos.

### Fase 3 — Migrar filho a filho
- **Objetivo:** por filho (ordem sugerida: um piloto de baixo risco primeiro, `PantonicVideo` por
  último por ser o mais divergente): remover as cópias de skills/agentes comuns, deixar só o
  específico, gravar o ponteiro `.claude/README.md` (DP-3). Declarar o slot de auditor de domínio.
- **Pronto quando:** cada filho tem `.claude/` só com específico + ponteiro; kit comum resolvido por
  herança; nenhuma regressão de invocação de skill.

### Fase 4 — Guardrail + inversão da doutrina
- **Objetivo:** drift-guard (DP-5); **reescrever GOVERNANCA §9 e o `.claude/README.md` do kit** para
  inverter a doutrina de *"todo projeto copia o kit"* para *"o comum é herdado do canônico; filho só
  carrega o específico; mudança comum = 1 edição no PantonicApp"*.
- **Pronto quando:** a doutrina escrita reflete o novo modelo; o guarda falha sob divergência
  simulada.

### Fase 5 — Fechamento
- **Objetivo:** `git init` no PantonicApp se DP-6=sim; PantonicApp ganha diário próprio como dono do
  backlog de governança comum; decision record cobrindo DP-1..DP-6.
- **Pronto quando:** decision record escrito; o hub tem trilha auditável; este plano fecha.

---

## 5. Verificação end-to-end
1. Editar 1 linha numa skill comum **só no PantonicApp** e confirmar que a mudança aparece em 2
   filhos distintos **sem nenhuma edição neles** (a prova da tese).
2. Invocar 1 skill comum e 1 agente comum em `PantonicVideo` e num filho "container" — ambos
   resolvem da herança.
3. Um filho consegue **sobrepor** uma skill comum com versão local de mesmo nome (escape hatch).
4. Drift-guard falha quando uma cópia manual diverge do canônico.
5. `bootstrap-pantonic` num projeto-sandbox novo instala herança (não cópia).

## 6. Riscos
- **Junção/symlink dependente do path do PantonicApp** (DP-1=A): mover o repo quebra a herança.
  Mitigação: path estável documentado, ou escolher B (copy-deploy) se o repo migra com frequência.
- **Herança global vaza skills Pantonic para projetos não-Pantonic** em `~/.claude`. Baixo risco:
  as `description` já se auto-escopam a "projeto Pantonic*"; o agente não as invoca fora de contexto.
- **Perda de melhoria dispersa** se Fase 1 não achar todo diff antes de congelar. Mitigação: Fase 0
  explícita + diff-matrix completo em Fase 1 antes de qualquer remoção.
- **Especialização legítima virar "deriva"**: distinguir override intencional (escape hatch,
  declarado) de cópia acidental (o que o drift-guard pega). Documentar a diferença.

## 7. Rollback
Cada fase é reversível: Fase 2-3 restauram as cópias dos filhos a partir do canônico congelado
(Fase 1); o estado pré-plano é recuperável enquanto o canônico retém tudo. Fazer o `git init` de
DP-6 **antes** da Fase 2 dá rollback por commit a partir daí.

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

**Achado fora de escopo (não fechado, só anotado):** `bootstrap-pantonic` hub referencia
`ARQUITETURA_PANTONICA §15` no passo do core; Container/ContainerForAWS referenciam `§16` no
mesmo ponto — divergência de numeração de seção que pode ser doc desatualizado em um dos lados
(ou simplesmente doc local diferente por filho); não investigado (fora do escopo desta tarefa,
que é só as 6 `SKILL.md`).

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
