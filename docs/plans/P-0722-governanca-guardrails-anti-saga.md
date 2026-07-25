# P-0722 — Governança: guardrails de doutrina extraídos do episódio "saga de legendas"

**Origem:** pedido do dono (2026-07-22), após a auditoria do plugin `subtitle_swapper` do
PantonicVideo (sessão de 2026-07-22). Dor declarada: uma feature "relativamente simples" percorreu
um caminho tortuoso (P-0718 → P-0719 → P-0720 → P-0721, com sanitização de 6 planos contaminados em
2026-07-21), reintroduziu bugs que o pipeline padrão já resolvia, e deixou **~300 linhas de código
de produção morto porém testado** vivo apenas pela suíte verde. O dono classificou isso como *"red
flag inaceitável em projeto"* que precisa estar **no radar de todo agente que trabalha num
Pantonic\***.

**Planejador:** Opus (fase de doutrina/arquitetura de governança, Regra 7). **Executor:** por fase
(ratificação/redação de doutrina = Opus/dono; mecânica de check/skill = Sonnet).

**Estado:** DECISÕES FECHADAS — DP-G1..DP-G4 resolvidas pelo dono 2026-07-22 (§4), todas conforme a
recomendação. Não iniciado: nenhuma tarefa começa antes do "go" explícito do dono (Regra 1). O
protótipo do hook de modelo-por-fase já foi instalado a pedido do dono (ver §6).

**Relação com `P-0721-governanca-single-source` (SPRINT-GOVSINGLESOURCE):** concerns distintos e
complementares. **Aquele** plano é o *veículo de distribuição* (kit comum herdado do canônico, zero
cópia). **Este** define o *conteúdo de doutrina novo* (guardrails + skill). Uma vez ratificadas em
`GOVERNANCA.md`, estas guardrails são propagadas a todos os filhos pelo mecanismo do SGSS — não por
edição manual filho a filho. Ordem sugerida: ratificar aqui → escrever em `GOVERNANCA.md` → SGSS
distribui.

---

## 1. O que o episódio provou (evidência, não opinião)

| Sintoma medido no PantonicVideo | Guardrail ausente que o teria evitado |
|---|---|
| `dehydrate_subtitles.py` (174 l) + `seed_prototype.py` (127 l) = ~300 linhas de produção **sem nenhum chamador de produção**, vivas só por `test_dehydrate_subtitles_t2.py` / `test_seed_prototype.py`. A rota que elas implementam foi construída (P-0720) e abandonada (P-0721) **sem serem removidas**. | **G-DEADCODE** — proibição de código morto testado. |
| A rota aprovada pelo dono (*dehydrate → `script.json` → `commit_to_capcut`*) foi trocada, **dentro da execução**, por uma segunda arquitetura (shadow-draft em `subtitle_swap.py`) sem decision record aprovado pelo dono. | **G-PLANFIDELITY** — mudança de rota é decisão do dono, não do executor. |
| Justificativa do abandono: *"resolve_chain devolve `(None, None)` para os 466 segmentos"* (P-0721 T4) **contradiz diretamente** *"todo segmento resolve pela wrapper"* (P-0720 T0). Findings reverteram entre sprints sem reconciliação. O dono afirma que a informação **era obtível** — e o próprio repo prova (`synthesize_missing_words`/`speech_window` derivam o timing por palavra; `seed_donor_prototype` semeia a cadeia que faltava). | **G-PREMISE** — premissa que embasa abandono de rota exige prova revisável, não asserção. |
| `TK-CAPANIM-LIMIT` (animação termina antes do intervalo da legenda) reincidiu **duas vezes** (P-0719 "T4c", P-0721 "T4b-restyle"); ordem render-split × continuity errada (P-0719-renderlimit-continuity-order) — bugs que o `correct_segments` padrão já acerta por default, vazados por **re-derivar a orquestração** em vez de reusá-la. | Consequência de G-PLANFIDELITY (reimplementar em vez de reusar) — sem guardrail próprio. |
| Suspeita do dono: decisões arquiteturais tomadas em Sonnet (executor) em vez de Opus. | **G-MODELPHASE-SKILL** — operacionalizar a troca de modelo por fase (§3 é vinculante mas sem gatilho). |
| Decisões owner-gated **postergadas** para a execução acabam tomadas pelo executor em sequência, no **modelo mais barato** (fase intelectual vazando para a barata, contra Regra 7). E o próprio backlog gerou **dois planos `P-0722` no mesmo dia** (nomenclatura por data colide); num plano não-linear "o executor já ficou confuso sobre o que fazer". | **G-PLANREADY** (plano fechado, linear, nomenclatura sequencial, decisões tomadas) + **G-EXECREADY** (executor não pergunta/decide; recusa plano não-pronto). |

---

## 2. Guardrails propostos (a ratificar → `GOVERNANCA.md` §7)

### G-DEADCODE — Proibição de código morto testado
**Regra:** todo símbolo de produção (função/classe/módulo fora de `tests/`) precisa de **ao menos um
chamador de produção** alcançável a partir de um entry point real (plugin registrado, superfície de
serviço no contrato, bootstrap). Cobertura por teste **não** confere "vivo" — um símbolo testado sem
chamador de produção é o pior caso, porque a suíte verde o **mascara**. Ao abandonar uma rota, o
executor **deleta os módulos da rota abandonada no mesmo commit**, nunca os deixa como fantasmas
testados.
**Enforcement:** (a) check executável de "símbolo de produção órfão" (reachability por AST a partir
dos entry points, ou `vulture` com allowlist mínima) no kit de conformance comum; (b) o handover de
toda tarefa declara os **chamadores de produção** de cada símbolo novo (some no fechamento se não há
nenhum); (c) review de fechamento rejeita módulo novo sem chamador não-teste.

### G-PLANFIDELITY — Fidelidade à rota; mudança de arquitetura é do dono
**Regra:** um executor (tipicamente Sonnet) **não** substitui a arquitetura/rota aprovada por uma
alternativa sob pressão de um obstáculo técnico. Ao bater num obstáculo que ameaça a rota do plano,
**para**, registra o achado, e **escala para replanejamento** (Opus/dono) — não improvisa uma
segunda arquitetura na mesma execução. Bifurcar a rota exige decision record aprovado **antes** de
codar a alternativa.
**Enforcement:** checklist de review + o handover cita a rota do plano e confirma que nenhuma
bifurcação arquitetural ocorreu sem decision record. (Regra não testável por código → consta como
gate de review, conforme §7 rodapé de `GOVERNANCA.md`.)

### G-PREMISE — Premissa que embasa abandono exige prova, não asserção
**Regra:** se um agente afirma *"a informação X não existe / não é obtível"* e usa isso para
abandonar/bifurcar uma rota, a afirmação precisa de um **spike que a comprove**, revisável pelo dono,
**antes** do abandono. Um *finding* não pode **reverter** um finding anterior entre sprints sem
reconciliação explícita registrada. Corolário: se a solução do obstáculo foi encontrada na rota
alternativa, verifique **primeiro** se ela pode ser reinjetada na rota original — normalmente pode.
**Enforcement:** gate de review no fechamento da tarefa que abandona/bifurca; o decision record cita
o spike e reconcilia qualquer finding anterior contraditório.

### G-MODELPHASE-SKILL — Skill global que operacionaliza a troca de modelo por fase
`GOVERNANCA.md` §3 já torna modelo-por-fase **vinculante**, mas não há gatilho operacional — daí a
suspeita de decisões arquiteturais rodando em Sonnet. Criar skill **global** `modelo-por-fase`
(`~/.claude/skills/`):
- Detecta a fase da tarefa em curso e o modelo ativo.
- **Trabalho intelectual** (planejar, arquitetar, auditar, decidir/abandonar rota, spec) rodando em
  modelo ≠ Opus → **para e instrui o dono a `/model opus`** (ou delega a subagente Opus) antes de
  prosseguir.
- **Iniciar execução mecânica** (implementar/editar/testar) → recomenda fallback **Sonnet**.
- **Leitura/varredura ampla** → **Haiku** (delegar a `context-scout`).
- Casa com a Regra 5 (destacar troca de modelo) para o anúncio.

**Nota técnica honesta (define DP-G2):** o agente **não troca o próprio modelo** da conversa
principal — só o dono (via `/model`) ou o harness (via hook em `settings.json`) o fazem. Portanto a
skill, sozinha, institucionaliza a **regra de decisão + o gate de parada + a convenção de anúncio**;
a **automação real** da troca exige um hook complementar. A skill entrega valor imediato mesmo sem o
hook (força a parada e o pedido explícito de `/model`).

### G-PLANREADY — Um plano só é executável quando fechado, linear e sem decisão pendente (dever do planejador)
**Regra:** antes de um plano ser marcado "pronto para execução", ele satisfaz as quatro condições:
1. **Nomenclatura sequencial.** Arquivo `P-NNNN-<slug>.md`, onde `NNNN` é um **contador global
   monotônico** (não a data), zero-padded, **nunca reusado**; o próximo id = maior id registrado no
   `_INBOX.md` + 1. A data de origem vira campo do cabeçalho, não do nome. (Motivo: `P-<MMDD>` colide
   — houve dois `P-0722` no mesmo dia.)
2. **Tarefas `T1..Tn` sequenciais**, em ordem de dependência, cada uma com objetivo + "pronto quando"
   + modelo da fase. Uma tarefa por contexto.
3. **Todas as decisões tomadas no fechamento — nada postergado.** Nenhuma escolha owner-gated fica
   "a resolver na execução". **Motivo medido neste episódio:** decisão adiada acaba tomada pelo
   executor em sequência, no modelo mais barato (Sonnet) — a fase intelectual (Opus) vazando para a
   fase de execução, contra a Regra 7; deteriora o projeto sem ganho real.
4. **Linear.** Sem referência para frente, sem ramo condicional não resolvido, sem "TBD". Um executor
   lê de cima a baixo e sabe o que fazer sem inferir.
**Enforcement:** checklist de review de fechamento de plano (as 4 condições); o `_INBOX.md` (de cada
filho e do hub) é o registro do contador sequencial.

### G-EXECREADY — O executor não decide, não pergunta e recusa plano não-pronto (dever do executor)
**Regra:** o executor **nunca inicia o trabalho fazendo perguntas ao dono.** Se precisaria perguntar,
o plano está incompleto → **devolve ao planejamento (Opus)**; não improvisa nem decide. E o executor
**recusa performar** enquanto o plano não estiver pronto por G-PLANREADY (fechado, linear, `T1..Tn`,
decisões resolvidas) — kicka de volta, não começa. Complementa G-PLANFIDELITY (não muda rota) e o
modelo-por-fase (decidir = Opus; executar = Sonnet): a decisão nunca desce para o modelo barato.
**Enforcement:** instrução no arquivo do agente `pantonic-executor` (recusa plano não-pronto; nunca
pergunta/decide) e na skill `proximo-passo` (só delega tarefa de plano pronto por G-PLANREADY); gate
de review.

---

## 3. Tarefas (fases)

### Fase 1 — Ratificar a doutrina [Opus/dono]
Dono resolve os DPs. Redigir em `GOVERNANCA.md` §7 os guardrails novos — G-DEADCODE, G-PLANFIDELITY,
G-PREMISE, **G-PLANREADY**, **G-EXECREADY** (itens 9-13); adicionar em §3 o ponteiro para a skill
`modelo-por-fase`. Materializar G-EXECREADY também no arquivo do agente `pantonic-executor` (recusa
plano não-pronto; nunca pergunta/decide) e na skill `proximo-passo` (só delega tarefa de plano pronto
por G-PLANREADY). Formalizar em G-PLANREADY o contador sequencial de planos (o `_INBOX.md` é o
registro; próximo id = maior + 1). **Pronto quando:** `GOVERNANCA.md` contém os guardrails novos (sem
duplicar os 8 existentes); o agente executor e a `proximo-passo` citam G-EXECREADY.

### Fase 2 — Skill global `modelo-por-fase` [Sonnet]
Criar `~/.claude/skills/modelo-por-fase/SKILL.md` (regra de decisão + gate de parada + anúncio).
Avaliar hook complementar em `settings.json` para automação (DP-G2). **Pronto quando:** a skill
existe e dispara nos gatilhos de fase; o hook (se aprovado) troca o modelo automaticamente.

### Fase 3 — Materializar G-DEADCODE como check executável [Sonnet]
Detector de símbolo de produção órfão no kit de conformance comum (a home do check é o canônico, via
SGSS). **Pronto quando:** o check falha sob um símbolo de produção sem chamador; passa no baseline
atual de cada filho (após limpeza — ver P-0722 do PantonicVideo, que zera o débito de ~300 linhas).

### Fase 4 — Distribuição [depende de SPRINT-GOVSINGLESOURCE]
As guardrails novas entram no canônico e são herdadas por todos os filhos pelo mecanismo do SGSS —
sem edição manual filho a filho. **Pronto quando:** os 6 filhos resolvem a doutrina nova por
herança; decision record fecha este plano.

---

## 4. Decisões (resolvidas 2026-07-22 — todas conforme a recomendação)

- **DP-G1 → Check automático + review** (as duas redes).
- **DP-G2 → Manter o hook nudge + criar a skill `modelo-por-fase`** (sem tentar automação impossível; o hook já está instalado, §6).
- **DP-G3 → Skill global em `~/.claude/skills`** (regra universal do dono).
- **DP-G4 → G-PLANFIDELITY vira Regra global do `~/.claude/CLAUDE.md` + doutrina em `GOVERNANCA.md`**; G-DEADCODE/G-PREMISE ficam em `GOVERNANCA.md`.
- **DP-G5 → Nomenclatura de plano = sequência global `P-NNNN`** (contador monotônico registrado no `_INBOX.md`, não a data) + tarefas `T1..Tn`. G-EXECREADY vai também para o `~/.claude/CLAUDE.md` global (conduta universal do executor), junto de G-PLANFIDELITY. Os dois `P-0722` atuais ficam **grandfathered**; o próximo plano do backlog é `P-0723`.

| id | pergunta | recomendação (= resolução) |
|---|---|---|
| **DP-G1** | G-DEADCODE: check automatizado (AST reachability / `vulture`) **e/ou** checklist de review? | **Ambos.** Check executável como rede primária + declaração de chamadores no handover como rede humana. |
| **DP-G2** | Skill `modelo-por-fase`: só regra+anúncio (implementável já) **ou** também hook de automação em `settings.json`? | **Regra+anúncio na Fase 2 agora** (valor imediato, força a parada); **hook como incremento** logo após, se o dono quiser a troca 100% automática. |
| **DP-G3** | Home da skill: **global** `~/.claude/skills` (vale para todo projeto, não só Pantonic) vs. kit Pantonic. | **Global.** Modelo-por-fase é regra universal do dono (Regras 1/7), não específica de Pantonic. |
| **DP-G4** | G-PLANFIDELITY/G-PREMISE viram texto de `GOVERNANCA.md` **e** promoção a Regra global do `~/.claude/CLAUDE.md`? | **Ambos** para G-PLANFIDELITY (é regra de conduta universal do executor, cabe no CLAUDE.md global); G-DEADCODE/G-PREMISE ficam em `GOVERNANCA.md` (doutrina Pantonic). |

## 5. Riscos
- **G-DEADCODE gerar falso-positivo** em símbolos legitimamente reservados (API pública de contrato
  ainda sem consumidor). Mitigação: allowlist explícita e mínima, revisada.
- **Skill de modelo sem hook** depender da disciplina do dono em rodar `/model`. Mitigação: DP-G2
  aprova o hook para fechar a lacuna.

## 6. Achados da execução
- **2026-07-22 — protótipo do nudge de modelo-por-fase já instalado** (a pedido do dono, antes da
  ratificação): hook global `UserPromptSubmit` em `~/.claude/settings.json` +
  `~/.claude/hooks/modelo_por_fase_userpromptsubmit.py`. Classifica a fase do prompt por
  heurística (intelectual→Opus / execução→Sonnet / leitura→Haiku; silêncio sem sinal) e emite
  `systemMessage` + `additionalContext` (gate + anúncio, Regra 5). **Confirma o DP-G2:** a troca
  automática é impossível — o schema de saída de hook não tem campo de modelo (só o `model:` de
  subavaliação `prompt`/`agent`); o hook nudga, o `/model` final é do dono. Pendências para a Fase 2
  formal: mover a classificação de heurística de palavra-chave para algo mais robusto se gerar ruído,
  e a skill `modelo-por-fase` que documenta a regra.
