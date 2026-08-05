# P-0730 — Estágio 5: identidade do framework (agnosticismo, CA+DDD e o README como contrato)

**Data de origem:** 2026-08-05 · **Iniciativa:** `PANTONIC-V2` · **Estágio:** 5 (corretivo) ·
**Prefixo de tarefa:** `V2I-` · **Substitui:** `P-0729-v2-documentacao` (Estágio 4) — ver §6.

**Checagem de versão do kit (skill `checar-versao-kit`, 2026-08-05):** modo **hub**. Local
`VERSION` == `.claude/KIT_VERSION` == `2.0.0`, paridade OK. Maior tag publicada no remoto:
`kit-v1.3.0` ⇒ **republicação pendente** (`kit-v1.4.0`, `kit-v1.5.0` e `kit-v2.0.0` existem só
localmente — o `git push` ficou fora de escopo por decisão do dono na `V2D-T4`). Nada é atualizado
por este plano; a `T13` reavalia a publicação junto do bump `2.1.0`.
**Achado da própria checagem (vira `TK-05`, §7):** o gatilho de revisão de doutrina da skill compara
só o componente MINOR (`X.Y.Z` → `Y`). Com local `2.0.0` e última rodada registrada em `1.4.0`, a
comparação dá `0 > 4 = falso` e a revisão **pendente fica invisível** — a regra quebra ao atravessar
um MAJOR.

---

## 0. O problema real deste estágio

O Estágio 4 entregou um README fiel — e a fidelidade é justamente o que expôs o defeito. Ao ler o
espelho, o dono identificou que **a identidade declarada do framework está errada na fonte da
verdade**, não no espelho: `GOVERNANCA.md` §1 define o PantonicApp como framework para *"aplicações
desktop, stack fixo Python + PySide6"*, e o README §1/§2 apenas reproduziu isso com fidelidade.

O entendimento canônico, ditado pelo dono em 2026-08-05:

> O PantonicApp é **agnóstico a tecnologias e a plataformas**. Trabalha um nível acima da
> implementação, nos níveis de **arquitetura** e de **projeto**. Doutrina o desenvolvimento de
> aplicações de qualquer modalidade (desktop, container, web, servidor) com base em **clean
> architecture e domain driven design**, e dá um passo além ao doutrinar as camadas de aplicação e
> infraestrutura com os conceitos do **infracore** (hoje ainda vinculado ao PySide6; a abstração é a
> etapa seguinte) mais o conceito de **plugins, onde cada plugin responde por um caso de uso**. Na
> camada de projeto, concentra a doutrina histórica de engenharia **modulada para a programação
> agêntica** — porque a qualidade de um produto não se garante agindo sobre o produto, mas sobre o
> **processo** que o gera.

Dois fatos que delimitam o estrago e evitam pânico:

1. **A máquina operacional da V2 não depende da premissa errada.** Estágios 1–3B (25 tarefas:
   telemetria, tetos de turno, modelo por fase, diário, handover, `guardrails-check`, `sync-kit`,
   `dead_code`, residência da doutrina) pertencem à camada de projeto — que o entendimento canônico
   **confirma**, e amplia. Nada ali é retrabalho.
2. **O que falta nunca foi feito.** `DDD` aparece **uma única vez** em todo o corpus
   (`.claude/agents/pantonic-auditor-arch.md:22`, citando capítulo de skill externa). Escrever o
   DDD é trabalho novo, não correção.

O que este estágio corrige é a **camada de identidade/arquitetura** e o **status do README**.

## 1. Decisões (ratificadas pelo dono em 2026-08-05, fechadas no planejamento)

| id | Decisão | Valor ratificado |
|---|---|---|
| `DR-1` | Premissa de stack | PySide6/MVVM/desktop **deixam de ser premissa** e viram **perfil do case de referência** (`PantonicVideo`). O framework é agnóstico a tecnologia e plataforma. |
| `DR-2` | Tratamento do específico | **Perfis nomeados** — `desktop-pyside6`, `container`, `web/servidor` — com guardrails ligados por perfil. Um projeto declara seu perfil; o kit só cobra o que o perfil ativa. |
| `DR-3` | Eixo de justificação | **Qualidade → rota → custo** (hoje o README declara custo primeiro). O motor é qualidade **pelo processo**; custo é restrição operacional, não razão de ser. |
| `DR-4` | Cobertura de DDD | **Estender** `pantonic-auditor-arch` (não criar agente novo): CA e DDD auditam-se juntos. |
| `DR-5` | Abstração do infracore | **Estágio próprio, posterior.** Não entra aqui; nasce como plano `P-0731`, autorado já fechado pela `T15` deste plano (G-PLANREADY item 5 — nunca um plano com vão). |
| `DR-6` | Versão | A correção sai como **`2.1.0`** (doutrina muda ⇒ MINOR). A `V2D-T6` (`2.0.1` do espelho) é **cancelada por absorção** na `T13`. |
| `DR-7` | Status do README | O README é **documento canônico do projeto — o contrato entre o framework e o cliente**, não artefato acessório nem derivado. Um framework corretamente construído é rejeitado por um README desatualizado, confuso ou equivocado. Consequência: guardrail novo **G-README** (`T7`) e aceite do dono como **gate de release** (`T12` antes da `T13`). |
| `DR-8` | Forma do enforcement do G-README | **(2026-08-05, decisão do dono, revisa a `DR-7`.)** A revisão do README é **atividade de encerramento de sprint, autorada pelo planejador como tarefa nomeada** — **não** gate mecânico. Pendurar o aceite como bloqueio automático na skill `handover` foi **rejeitado**: gera artefato especializado e confuso no lugar de uma responsabilidade clara de papel. O `check-readme.ps1` **permanece**, rebaixado de critério de pronto a **instrumento do planejador** dentro dessa atividade (ele detecta drift estrutural; nunca julga sentido). Consequência: `T16` nova; §7 item 15 reescrito na mesma data. |

**Nota de fundamentação da `DR-7`:** o próprio corpus já se contradiz hoje. `GOVERNANCA.md` §9 diz
*"um humano decide sobre o framework lendo só esse arquivo"*, enquanto o README §preâmbulo diz *"não
existe para convencer ninguém a adotar o framework: quem lê já o usa"*. A `DR-7` resolve a colisão a
favor do §9 e a eleva a guardrail. Evidência de campo: o dono identificou os desvios de identidade
**pela leitura do README**, não pelos artefatos.

## 2. Desvios medidos (insumo das tarefas — nenhum inferido na execução)

| # | Canônico | Escrito hoje | Onde | Tarefa |
|---|---|---|---|---|
| D1 | Agnóstico a tecnologia/plataforma; desktop, container, web, servidor | "Desktop-first"; "Stack fixo Python+PySide6"; "não tenta ser genérico" | `GOVERNANCA.md:14-15`; `README.md:43-65` | `T3`, `T11` |
| D2 | Dois níveis: **arquitetura** e **projeto** | "duas metades: arquitetura e operação", com operação ancorada em custo | `README.md:44-49` | `T3`, `T6`, `T11` |
| D3 | Base = clean architecture **+ DDD** | CA onipresente; DDD com 1 ocorrência no corpus inteiro | todo o corpus | `T5`, `T9` |
| D4 | Infracore = doutrina das camadas de aplicação/infra, hoje presa ao PySide6 | infracore = componentes portados do PantonicVideo, com Qt embutido na regra universal | `ARQUITETURA_PANTONICA.md` §2/§4/§10 | `T4`, `T15` |
| D5 | **Um plugin = um caso de uso** | plugin = "incremento funcional atômico" (vínculo com UC inexistente) | `GOVERNANCA.md:271-275` | `T5` |
| D6 | Motor = qualidade pelo processo; custo é restrição | "o que ele governa são três coisas, nesta ordem: custo, rota, qualidade" | `README.md:51-58` | `T6`, `T11` |
| D7 | Cada sprint validada — validação **visual** do gerente/cliente antes de seguir | só golden rule 7 ("executável muda a cada sprint") + validação de cliente no fluxo de POC | `ARQUITETURA_PANTONICA.md:27`; `GOVERNANCA.md:279-282` | `T6` |
| D8 | Backlog derivado de metodologia ágil (Scrum); responsabilidades declaradas | diário/sprints sem filiação declarada; responsabilidades espalhadas por §3/§4/agentes/Regra 8 | `GOVERNANCA.md` §4 | `T6` |
| D9 | Auditoria de CA **+ DDD** | `pantonic-auditor-arch` cobre CA; DDD de raspão | `.claude/agents/` | `T9` |
| D10 | O grau em que infracore/plugins de fato estendem CA+DDD **ainda precisa ser auditado** | o corpus afirma conformidade como fato consumado | `ARQUITETURA_PANTONICA.md` §1/§9 | `T5` (declara), `T14` (mede) |
| D11 | README é contrato canônico com o cliente | README se autodeclara espelho para quem "já usa"; contradiz `GOVERNANCA.md:489` | `README.md:5-11` | `T7`, `T11` |

**Ponto cego confirmado do guarda atual:** `.claude/checks/check-readme.ps1` verifica roster de
agentes/skills, paridade de versão e contagem de guardrails — **nada semântico**. Espelho fiel de
fonte errada passa verde. É por isso que a `DR-7` põe o aceite do dono no caminho do release, em vez
de tentar automatizar fidelidade de sentido.

## 3. Tarefas

Uma tarefa por contexto (`GOVERNANCA.md` §4.3). Modelo declarado por tarefa (§3, modelo por fase).

### T1 — Fechar o Estágio 4 e commitar a árvore em curso [Sonnet]
- **Objetivo:** deixar o histórico limpo antes da correção: o espelho reprovado vira commit, e o
  Estágio 4 fecha com o veredito registrado.
- **Arquivos-alvo:** `README.md`, `.claude/checks/check-readme.ps1`, `docs/DIARIO_DE_OBRAS.md`,
  `docs/plans/P-0729-v2-documentacao.md`, `docs/telemetria.tsv` (todos já modificados na árvore);
  `docs/plans/P-0729-v2-documentacao.md` §`## Achados da execução` (apensar).
- **Conteúdo do achado a registrar:** `V2D-T5` **reprovada** em 2026-08-05 — o teste de aceitação
  cumpriu seu papel e detectou desvio de identidade na **fonte da verdade** (`GOVERNANCA.md` §1),
  não no espelho; os 11 desvios estão em `P-0730` §2. `V2D-T6` **cancelada por absorção** (`DR-6`).
- **Verificação:** `git status --short` sem pendências; `git log --oneline -1`.
- **Pronto quando:** commit criado; `P-0729-V2D` marcado `superseded` no índice do diário com
  ponteiro `substituído por: docs/plans/P-0730-v2-identidade.md`; `V2D-T5`/`V2D-T6` com status final.

### T2 — Varredura de contaminação do benchmarking [Sonnet]
- **Objetivo:** medir se a premissa errada descartou candidato bom em silêncio. É o único lugar onde
  o desvio de identidade pode ter causado perda material, e roda **antes** da reescrita da doutrina
  para que qualquer achado seja absorvido por ela (G-PREMISE: spike antes de asserção).
- **Arquivos-alvo:** `docs/benchmark/RELATORIO_CONSOLIDADO.md` §`## 4. Descartes justificados` e
  §`## 2. Dimensão por dimensão`; `docs/benchmark/CANDIDATOS.md` (linhas `REJEITAR`/`adiar`).
- **Critério de achado:** rejeição/descarte cuja justificativa **invoca** desktop, PySide6, MVVM,
  Qt ou "não se aplica a aplicação local" como razão.
- **Verificação:** `Grep -i "desktop|pyside|mvvm|\bqt\b"` nas duas seções + leitura das linhas
  `REJEITAR` do `CANDIDATOS.md`.
- **Pronto quando:** cada ocorrência classificada como (a) irrelevante, (b) reexame necessário →
  vira `TK-` no diário. Sem achado, fecha com uma linha de resultado negativo — resultado negativo
  medido é entrega, não ausência de trabalho.

### T3 — `GOVERNANCA.md` §1/§2: identidade agnóstica e perfis [Opus]
- **Objetivo:** reescrever a identidade do framework na fonte da verdade (`D1`, `D2`, `DR-1`,
  `DR-2`).
- **Arquivos-alvo:** `GOVERNANCA.md:10-37` (§1 Identidade, §2 Core comum).
- **Conteúdo:** (a) framework agnóstico a tecnologia e plataforma, atuando em **dois níveis** —
  arquitetura e projeto; modalidades cobertas: desktop, container, web, servidor. (b) As premissas
  deixam de citar stack; passam a ser: CA+DDD como base, infracore como doutrina de aplicação/infra,
  plugin = caso de uso, core comum reusável, guardrails executáveis. (c) Seção de **perfis**
  (`DR-2`): o que é universal, o que um perfil ativa, e como um projeto declara o seu. (d) A régua
  de especialização por altura (§2) permanece — é agnóstica.
- **Verificação:** `Grep -i "desktop|pyside|mvvm" GOVERNANCA.md` → nenhuma ocorrência fora de
  contexto de **perfil** ou de **case de referência**.
- **Pronto quando:** §1/§2 reescritos; nenhuma premissa de stack sobrevive como regra universal.

### T4 — `ARQUITETURA_PANTONICA.md`: separar núcleo agnóstico do perfil desktop [Opus]
- **Objetivo:** marcar o que é Qt-específico como `[PERFIL: desktop-pyside6]` e deixar o núcleo
  agnóstico (`D4`, `DR-1`, `DR-2`). Continua o precedente já aceito pelo dono: detalhe do
  PantonicVideo é **default do case**, nunca regra universal.
- **Arquivos-alvo:** `ARQUITETURA_PANTONICA.md` §2 (allowlists de import da tabela de camadas),
  §4 (infracore), §10 (MVVM e PySide6, inteiro), §11 (partes de OS/IN-OUT), §14.
- **Fica agnóstico:** golden rules (§1), quatro camadas `infracore ← contracts ← services ←
  plugins`, ACL, sinais/estado, plugins/manifests, contenção de falhas, disciplina de testes.
- **Verificação:** `Grep "PERFIL: desktop-pyside6" ARQUITETURA_PANTONICA.md` cobre todas as
  ocorrências de `PySide6|Qt|MVVM` remanescentes; nenhuma fora de bloco marcado.
- **Pronto quando:** um leitor que constrói um serviço containerizado consegue seguir o documento
  inteiro sem encontrar exigência de Qt.

### T5 — DDD como fundamento par, plugin = caso de uso, e o grau ainda não auditado [Opus]
- **Objetivo:** escrever o que nunca existiu (`D3`, `D5`, `D10`).
- **Arquivos-alvo:** `ARQUITETURA_PANTONICA.md` §1/§2 (seção nova de DDD, antes do modelo de
  camadas); `GOVERNANCA.md` §5 (fluxo de extensão) e §6 item 1 (PRD/linguagem ubíqua).
- **Conteúdo:** (a) DDD como fundamento par da CA: linguagem ubíqua, entidades, objetos de valor,
  agregados e suas invariantes, pureza da camada de domínio, contexto delimitado. (b) A tese
  pantônica: **infracore e plugins estendem CA+DDD** — infracore doutrina as camadas de aplicação e
  infraestrutura; cada plugin responde por **um caso de uso**. (c) O grau em que a implementação
  atual honra essa tese é declarado **não auditado**, com ponteiro para a `T14` — asserção sem
  medida é exatamente o que G-PREMISE proíbe.
- **Verificação:** `Grep -i "\bDDD\b|agregado|linguagem ubíqua"` nos dois documentos.
- **Pronto quando:** um planejador consegue decidir se uma classe nova é entidade, VO, agregado,
  caso de uso ou serviço lendo só estes documentos; e a relação plugin↔caso de uso é normativa.

### T6 — Camada de projeto: filiação ágil, validação por sprint e responsabilidades [Opus]
- **Objetivo:** declarar a camada de projeto tal como o dono a definiu (`D6`, `D7`, `D8`, `DR-3`).
- **Arquivos-alvo:** `GOVERNANCA.md` §3 (preâmbulo — eixo de justificação), §4 (fluxo de
  desenvolvimento), §4.2 (diário), §5.
- **Conteúdo:** (a) **Eixo qualidade → rota → custo** (`DR-3`): a doutrina da qualidade — agir sobre
  o processo que gera o produto, não sobre o produto — passa a ser o motor declarado; custo é
  restrição de projeto. (b) **Filiação ágil**: backlog, sprints e tarefas derivam de metodologia
  ágil (Scrum), modulados para programação agêntica. (c) **Validação contínua**: uma sprint não
  avança sem **validação visual do gerente/cliente** sobre o entregável; é gate, não recomendação.
  (d) **Matriz de responsabilidades** num único lugar canônico: dono/gerente = última instância e
  fonte da doutrina de produto; planejador = produz plano/checklist e não executa; executor =
  executa exatamente o registrado, não decide nem pergunta; auditores = CA+DDD e clean code.
- **Verificação:** cada uma das quatro alíneas localizável por Grep de âncora própria.
- **Pronto quando:** a matriz de responsabilidades existe em um só lugar, sem duplicata plena
  (padrão `DR-A` de `docs/RESIDENCIA_DOUTRINA.md`).

### T7 — G-README: o README como documento canônico [Opus]
- **Objetivo:** materializar a `DR-7` (`D11`) **antes** de o README ser reescrito, para que ele já
  nasça sob a regra nova.
- **Arquivos-alvo:** `GOVERNANCA.md` §7 (guardrail novo, item **15**), §8 (documentação mínima —
  README entra na tabela como canônico), §9 (resolver a colisão com o preâmbulo do README).
- **Conteúdo do G-README:** o `README.md` do hub é o **contrato entre o framework e o cliente**.
  (1) Nenhuma mudança de doutrina fecha sem o README refletindo-a **na mesma sprint**. (2) Nenhum
  bump de versão fecha sem **aceite explícito do dono** sobre o README. (3) O guarda executável
  (`check-readme.ps1`) cobre estrutura, não sentido — o aceite do dono é o único teste de sentido, e
  por isso é gate, não cortesia. *Enforcement:* `check-readme.ps1` + gate de aceite na skill
  `handover` e no fechamento de versão.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` (a contagem de guardrails do README §10
  passa a divergir de §7 — divergência **esperada**, fechada pela `T11`).
- **Pronto quando:** §7 tem 15 itens; §8 lista o README; a contradição de `README.md:5-11` está
  registrada como dívida da `T11`.

### T8 — Propagar perfis no kit [Sonnet]
- **Objetivo:** parar de cobrar MVVM/Qt de projeto que não é desktop (`DR-2`).
- **Arquivos-alvo:** `.claude/skills/guardrails-check/SKILL.md:43,69`;
  `.claude/agents/pantonic-executor.md:14`; `.claude/agents/pantonic-auditor-arch.md:33,56`;
  `.claude/skills/audit-sweep/SKILL.md:30`; `.claude/skills/integrar-poc/SKILL.md:39`.
- **Conteúdo:** cada checagem Qt/MVVM passa a ser condicionada ao perfil declarado do projeto; na
  ausência de declaração, o perfil é `desktop-pyside6` (compatibilidade com os consumidores atuais).
- **Verificação:** `pwsh .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift`.
- **Pronto quando:** nenhuma cobrança de Qt/MVVM incondicional sobrevive no kit.

### T9 — DDD na auditoria de arquitetura [Sonnet]
- **Objetivo:** `DR-4`/`D9` — o auditor de arquitetura passa a auditar CA **e** DDD.
- **Arquivos-alvo:** `.claude/agents/pantonic-auditor-arch.md` (descrição, capítulos de referência,
  lista de verificações); `.claude/skills/audit-sweep/SKILL.md` (greps determinísticos de DDD).
- **Conteúdo:** verificações novas — pureza do domínio (domínio sem import de infraestrutura),
  invariante de agregado aplicada dentro do agregado, VO imutável, caso de uso por plugin, linguagem
  ubíqua consistente entre PRD e código.
- **Verificação:** `kit_check.ps1 -Mode check-drift` (o `.claude/README.md` é derivado); dry-run do
  `audit-sweep` no hub.
- **Pronto quando:** o auditor produz apontamento de DDD sem precisar de skill externa ao kit.

### T10 — `bootstrap-pantonic` e `.claude/README.md` [Sonnet]
- **Objetivo:** um projeto novo nasce sob a doutrina corrigida.
- **Arquivos-alvo:** `.claude/skills/bootstrap-pantonic/SKILL.md`; `GOVERNANCA.md:297` (artefato
  *Architecture*); `.claude/README.md` (**regenerado do disco**, nunca editado à mão).
- **Conteúdo:** o artefato *Architecture* deixa de ser "MVVM + clean architecture" e passa a
  "clean architecture + DDD, com MVVM apenas no perfil `desktop-pyside6`"; o bootstrap pergunta/
  registra o **perfil** do projeto.
- **Verificação:** `kit_check.ps1 -Mode check-drift` exit 0.
- **Pronto quando:** o bootstrap não presume desktop em momento algum.

### T11 — Reescrever o README sob o status canônico [Opus]
- **Objetivo:** o espelho volta a ser fiel — agora a uma fonte correta — e assume a voz de contrato
  (`DR-7`, `D1`, `D2`, `D6`, `D11`).
- **Arquivos-alvo:** `README.md` — título, preâmbulo (a frase *"não existe para convencer ninguém"*
  cai), §1, §2, §3 (eixo `DR-3`), §10 (contagem de guardrails: 15), §11, §15; demais seções só onde
  herdarem o eixo custo-primeiro.
- **Conteúdo:** identidade agnóstica e os dois níveis; CA+DDD como base e infracore+plugins como a
  extensão pantônica; perfis; a camada de projeto com a doutrina da qualidade como motor; o que está
  medido × o que está declarado não auditado (`T14`).
- **Dívidas registradas pela `V2I-T7` (2026-08-05), a fechar aqui — sem ampliar o escopo acima:**
  (a) **contradição de `README.md:5-11`** — o preâmbulo declara *"não existe para convencer ninguém
  a adotar o framework: quem lê já o usa"*, o oposto de `GOVERNANCA.md` §9 e do novo G-README (§7
  item 15); a `DR-7` resolveu a colisão a favor do §9, e o §9 passou a registrar a dívida
  explicitamente ("Colisão registrada, ainda aberta"); a frase já está nos Arquivos-alvo desta
  tarefa. (b) **contagem de guardrails** — o README §10 declara 14 e §7 passou a ter 15 desde a
  `V2I-T7`; a divergência era prevista e já está nos Arquivos-alvo (§10 → 15).
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` → exit 0.
- **Pronto quando:** exit 0 **e** nenhuma afirmação de stack fixo/desktop sobrevive fora de "perfil"
  ou "case de referência".

### T12 — Teste de aceitação do README pelo dono [dono]
- **Objetivo:** o gate de sentido que nenhum script cobre (`DR-7`). Substitui a `V2D-T5`.
- **Forma:** leitura corrida do README pelo dono, respondendo três perguntas: (a) o texto descreve o
  framework que ele governa? (b) alguma afirmação está equivocada, confusa ou desatualizada? (c) um
  cliente decidiria adotar — ou rejeitar — com base nisto, e a decisão seria justa?
- **Verificação:** veredito registrado no diário; reprovação gera rodada nova da `T11`, não segue
  adiante.
- **Pronto quando:** aceite explícito do dono registrado. **Bloqueia a `T13`.**

### T13 — Fechar `2.1.0` e distribuir [Sonnet]
- **Objetivo:** `DR-6` — publicar a doutrina corrigida.
- **Arquivos-alvo:** `VERSION`, `.claude/KIT_VERSION`, `CHANGELOG.md` (§2.1.0), tag `kit-v2.1.0`.
- **Conteúdo:** o CHANGELOG registra a correção de identidade como o que ela é — a premissa de stack
  caiu, o framework é agnóstico — e absorve o escopo da `V2D-T6` cancelada. Reavaliar com o dono a
  **republicação pendente** (`kit-v1.4.0`/`1.5.0`/`2.0.0` locais, remoto em `1.3.0`): publicar ou
  manter local é decisão do dono, nunca do agente (§10(a)).
- **Verificação:** `kit_check.ps1 -Mode validate` (paridade de versão) e `check-readme.ps1`, ambos
  exit 0.
- **Pronto quando:** `2.1.0` fechada, com a decisão de publicação registrada.

### T14 — Auditoria: em que grau infracore e plugins estendem CA+DDD hoje [Sonnet]
- **Objetivo:** medir o que a `T5` declarou não auditado (`D10`). Roda na **implementação de
  referência** (`D:\workspaces\PantonicVideo`), não no hub — o hub não tem código de aplicação.
- **Procedimento:** skill `audit-sweep` (pré-varredura mecânica) → agente `pantonic-auditor-arch`
  já estendido pela `T9`.
- **Saída:** `docs/audits/AUDIT_ARCH_<AAAA-MM-DD>.md` no PantonicVideo; **não altera código**.
- **Verificação:** o relatório existe e classifica cada desvio com ação de correção.
- **Pronto quando:** existe resposta medida para "o infracore e os plugins de fato estendem CA+DDD,
  e onde não estendem".

### T15 — Autorar `P-0731` (abstração do infracore) já fechado [Opus]
- **Objetivo:** `DR-5` + G-PLANREADY item 5 — o plano dependente nasce como a última tarefa do plano
  que produz seu insumo, nunca como vão.
- **Insumos:** achado da `T14` + doutrina de infracore agnóstico escrita nas `T4`/`T5`.
- **Arquivos-alvo:** `docs/plans/P-0731-<slug>.md` (novo); `docs/plans/_INBOX.md` (linha nova +
  contador → `P-0732`); `docs/DIARIO_DE_OBRAS.md` (índice).
- **Escopo do plano a autorar:** desacoplar o infracore do PySide6 — portas genéricas para
  lifecycle, injeção, estado, sinais e filesystem, com o binding Qt virando uma implementação do
  perfil `desktop-pyside6` entre outras.
- **Verificação:** o plano novo satisfaz as 5 condições de G-PLANREADY.
- **Pronto quando:** `P-0731` registrado e fechado, sem questão owner-gated pendente.

### T16 — Materializar o dever 2 do G-README como responsabilidade do planejador [Opus]
- **Objetivo:** `DR-8` — o dever 2 do G-README (§7 item 15) hoje só existe como texto. Dar-lhe
  residência **como responsabilidade de papel**, não como gate mecânico.
- **Origem:** achado da `V2I-T7` (o item 15 prometia enforcement inexistente) + decisão do dono de
  2026-08-05 rejeitando o gate automático na skill `handover`.
- **Arquivos-alvo (normativo):** `GOVERNANCA.md` §3 (matriz de responsabilidades — linha canônica do
  planejador); `.claude/agents/pantonic-planner.md` (instrução operacional, **ponteiro** para §3, sem
  duplicata plena — padrão `DR-A` de `docs/RESIDENCIA_DOUTRINA.md`).
- **Fora de escopo, explicitamente:** a skill `handover` **não se toca** — o gate mecânico foi
  rejeitado pelo dono; e `check-readme.ps1` **não se apaga** (decisão do dono: mantido como
  instrumento do planejador).
- **Conteúdo:** ao encerrar qualquer sprint, o planejador autora uma **tarefa nomeada de revisão do
  README** no plano da sprint, cujo dossiê inclui rodar `pwsh .claude/checks/check-readme.ps1` para a
  paridade estrutural e colher o **veredito do dono** sobre o sentido. Sprint sem essa tarefa é plano
  incompleto (G-PLANREADY).
- **Verificação:** Grep pela linha do planejador em `GOVERNANCA.md` §3 e pelo ponteiro no arquivo do
  agente; `pwsh .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit 0.
- **Pronto quando:** a responsabilidade está declarada em um só lugar canônico, o agente planejador
  a referencia, e nenhum gate automático foi criado.

## 4. Riscos

| Risco | Mitigação |
|---|---|
| Reescrever identidade sem medir o que a premissa errada já descartou | `T2` roda **antes** da doutrina; achado vira tíquete |
| "Agnóstico" virar vago — perder a precisão que hoje torna as regras executáveis | Perfis nomeados (`DR-2`): o núcleo é agnóstico, o perfil é específico e continua verificável por teste |
| Afirmar aderência a CA+DDD sem medida (o defeito que G-PREMISE proíbe) | `T5` declara não auditado; `T14` mede; nenhuma das duas afirma sem a outra |
| Quebrar os 5 consumidores ao trocar guardrail incondicional por condicional | `T8` fixa `desktop-pyside6` como perfil default na ausência de declaração |
| README voltar a divergir em silêncio | G-README (`T7`) + revisão do README como tarefa de encerramento de sprint autorada pelo planejador (`DR-8`, `T16`); nesta sprint, a `T12` (aceite do dono) é essa tarefa e bloqueia a `T13` |

## 5. Ordem de execução

`T1` → `T2` → `T3` → `T4` → `T5` → `T6` → `T7` → `T8` → `T9` → `T10` → `T11` → `T12` (dono) →
`T13` → `T14` → `T15`. Linear, sem ramo condicional. `T3`..`T7` são doutrina (Opus, um contexto
cada); `T8`..`T10` e `T13`..`T14` são propagação/medida (Sonnet); `T11` é redação canônica (Opus);
`T12` é do dono.

**`T16` (aberta em 2026-08-05 pela `DR-8`)** entra **antes da `T12`** — o dever que ela materializa
é o que dá à `T12` o caráter de tarefa de encerramento, e não de gate. Ordem efetiva a partir da
`T8`: `T8` → `T9` → `T10` → `T11` → `T16` → `T12` (dono) → `T13` → `T14` → `T15`.

## 6. Reconciliação com o Estágio 4 (obrigatória)

Classificação **(B)** da skill `diario-de-obras` — *"plano que muda completamente o entendimento do
plano atual: a premissa que o sustentava caiu"*. `P-0729-v2-documentacao` (`P-0729-V2D`) vai a
**`superseded`**, com ponteiro `substituído por: docs/plans/P-0730-v2-identidade.md`. O trabalho
entregue permanece (`V2D-T1`..`T4` seguem válidos: DOC_MAP, guarda de drift, infraestrutura de
versão); a **rota** não. Nenhuma tarefa nova sai do Estágio 4. Este plano passa a ser o **único
plano vivo** da iniciativa `PANTONIC-V2`.

## 7. Achados abertos deste planejamento

- **`TK-05`** — a skill `checar-versao-kit` compara só o MINOR no gatilho de revisão de doutrina
  (`GOVERNANCA.md` §7.1) e fica cega ao atravessar um MAJOR: local `2.0.0` × última rodada `1.4.0`
  dá "sem pendência" quando a revisão está pendente. Correção de uma linha (comparar
  `MAJOR.MINOR`), sem relação com este estágio — registrado como tíquete avulso.

## Achados da execução

### T4 — 2026-08-05

**Reconciliação da notação de perfil (decisão do orquestrador).** O dossiê da `T4` neste plano foi
escrito antes de a `T3` existir e previa o marcador `[PERFIL: desktop-pyside6]`. A `T3`
materializou no corpus outra forma — *[perfil `desktop-pyside6`, §1.1]*, ver `GOVERNANCA.md` §7
item 3 — e é ela que vale daqui em diante, para não deixar dois marcadores concorrentes. É
consequência mecânica da `DR-2`, não bifurcação de rota. Em heading, o sufixo vai no próprio
título; inline, no item. Dentro de árvore de diretórios ou bloco de código, onde ênfase Markdown
não renderiza, usa-se a variante sem itálico `[perfil desktop-pyside6]` com uma legenda logo abaixo
do bloco. Aplicado em `ARQUITETURA_PANTONICA.md` pela `T4`; as tarefas seguintes que marcarem
perfil devem usar a mesma notação.

### T5 — 2026-08-05

**Numeração da seção nova de DDD (decisão de redação).** O dossiê pede a seção "antes do modelo de
camadas". Criá-la como `## 2` numerada obrigaria a renumerar `##2`..`##15` de
`ARQUITETURA_PANTONICA.md` e todas as referências cruzadas do corpus (`§4`, `§6`, `§9`, `§10`, `§14`
aparecem em GOVERNANCA, nos agentes e nas skills) — cascata fora do escopo declarado e sem relação
com `D3`. A seção entrou como **`### 1.1 Fundamentos — clean architecture + DDD`**, logo após as
golden rules e antes de `## 2. Modelo de camadas`: mesma posição de leitura, zero renumeração.
Efeito colateral tratado no mesmo passo: como o marcador de perfil da `T3` cita "§1.1" apontando
para `GOVERNANCA.md` §1.1, a convenção de perfil no cabeçalho do documento ganhou uma linha de
**desambiguação de numeração** (o `§1.1` do marcador é sempre o da GOVERNANCA; a §1.1 local é a de
CA+DDD).

**Item (c) declarado em dois lugares, de propósito.** A não-auditoria (`D10`) aparece no fecho da
`ARQUITETURA_PANTONICA.md` §1.1 (aderência do infracore e dos plugins a CA+DDD) e no fecho da
`GOVERNANCA.md` §5 (plugins existentes de fato mapearem um caso de uso cada). São as duas asserções
que o corpus fazia como fato consumado, em documentos que se leem separadamente; ambas apontam para
a `T14` e para `docs/audits/AUDIT_ARCH_<AAAA-MM-DD>.md`. Quando a `T14` entregar, **as duas**
precisam ser substituídas pelo resultado medido — não só uma.

**Fronteira com a `T6`.** A `T5` não tocou `GOVERNANCA.md` §4 (backlog/sprints) nem o eixo
qualidade→rota→custo: `D5` e `D10` param na §5 e na §6 item 1. O item 2 da §6 ("MVVM + clean
architecture", `GOVERNANCA.md` §6) segue intocado como resíduo declarado da `T10`.

### T6 — 2026-08-05

**Posição da matriz de responsabilidades (decisão de redação).** A matriz entrou na **abertura da
`GOVERNANCA.md` §3**, absorvendo a tabela de agentes que já vivia ali, e não como subseção nova:
`### 3.1` já é *Residência e precedência da doutrina*, citada por `GOVERNANCA.md:119` e pelos docs
de residência — criar uma `### 3.1` para a matriz obrigaria renumeração em cascata, proibida pelo
escopo. A âncora greppável é a linha em negrito **`Matriz de responsabilidades — lugar canônico.`**,
acima da tabela. A tabela ganhou duas colunas (*Papel*, *Não faz*) e duas linhas novas
(**dono/gerente** e **auditoria**), passando de três agentes para os cinco papéis do projeto.

**`DR-A` aplicado dentro da própria §3.** O bullet *"O agente de planejamento nunca executa; o
agente de execução nunca replaneja escopo…"* dizia, em prosa, o que a matriz agora diz em tabela —
virou **ponteiro** ("papéis não são intercambiáveis… a fronteira está na matriz acima"), não cópia.
Mesma disciplina nas demais residências: §4 (tabela Scrum), §4.5 e §5 **apontam** para a §3.

**Numeração da validação por sprint.** Entrou como **`### 4.5 Validação por sprint — gate do
gerente/cliente`**, sufixo aditivo depois da `4.4` — zero renumeração. A **regra** do gate mora na
§4.5; o **veredito** de cada sprint mora no diário (§4.2), que ganhou um bullet-ponteiro. Separação
deliberada: regra é doutrina versionada, veredito é estado de trabalho (teste de residência, §3.1).

**Recado para a `T7` (não é bifurcação, é ponteiro faltante).** A §4.5 fecha dizendo que, em sprint
de doutrina/documentação, o entregável mostrável é o documento e a leitura corrida pelo dono é a
validação — **sem citar item de guardrail**, porque o G-README (§7 item **15**) ainda não existe. A
`T7`, ao criar o item 15, deve ligá-lo de volta à §4.5: o aceite do README é a instância desse gate
aplicada ao contrato com o cliente, não um gate paralelo.

## 8. Revisão de escopo — `T11b` (decisão do dono, 2026-08-05)

Requisito novo do dono, pedido após o fechamento da `T3`: **o README precisa de uma seção
introdutória que defina todo o jargão do framework**. Escopo ratificado no ato: jargão de
**arquitetura**, de **projeto** e — o eixo que o dono destacou — de **metadados do próprio
framework** (o exemplo dado foi o termo *kit*).

Posição decidida: **entre a `T11` e a `T12`**. O glossário é escrito sobre o README já reescrito
(`T11`) e **antes do aceite do dono** (`T12`) — é justamente o gate onde a inteligibilidade do
vocabulário é julgada. Escrevê-lo antes da `T4` seria documentar jargão em pleno movimento:
`T4`–`T7` ainda introduzem *perfil*, *agregado*, *linguagem ubíqua*, *infracore agnóstico* e
*G-README*.

**Ordem de execução vigente (substitui a de §5):** `T1` → … → `T10` → `T11` → **`T11b`** → `T12`
(dono) → `T13` → `T14` → `T15`. Total do plano passa de 15 para **16 tarefas**.

### T11b — Glossário do framework no README [Opus]
- **Objetivo:** um gerente/cliente lê o README de ponta a ponta sem encontrar um termo que não
  consiga definir. Decorre da `DR-7` (README = contrato com o cliente): contrato com vocabulário
  privado não é contrato.
- **Arquivos-alvo:** `README.md` — **uma seção `##` nova, não numerada**, inserida entre o preâmbulo
  e a `## 1.`, titulada `## Glossário — o vocabulário deste framework`.
- **Por que não numerada (medido na `T3`, não presumir de novo):** `.claude/checks/check-readme.ps1`
  ancora as seções que valida pelo **título** (`Anatomia do kit`, `Os guardrails`), e a contagem de
  seções é derivada, não fixa. Seção nova não numerada não renumera nada e não quebra ponteiro
  externo (`README §10`, `§12` etc. seguem válidos). **A seção precisa carregar a linha
  `> Fonte da verdade:`** — obrigatória se o guarda a enxergar, inofensiva se não.
- **Conteúdo — três eixos, um bloco cada:**
  1. **Arquitetura:** infracore, core pantonico, contracts, serviços de expressão, ACL, egress,
     plugin, caso de uso, perfil, agregado, objeto de valor, linguagem ubíqua, regra de dependência.
  2. **Projeto:** diário de obras, tarefa atômica, handover, guardrail, piso de regressão,
     conformance, modelo por fase, contexto, orçamento de turnos.
  3. **Metadados do framework:** kit, hub, consumidor, `sync-kit`, drift, espelho, fonte da verdade,
     `KIT_VERSION`, tag `kit-vX.Y.Z`, plano `P-NNNN`, iniciativa, estágio, sprint, tíquete `TK-`,
     agente, skill, decisão `DR-`/`DP-`.
  Cada verbete: **uma frase de definição + ponteiro para onde a regra vive**. Definição sem
  ponteiro cria segunda residência da doutrina (`docs/RESIDENCIA_DOUTRINA.md`, padrão `DR-A`) —
  o glossário **define o termo, nunca a regra**.
- **Critério anti-duplicata:** nenhum verbete pode ser a única fonte de uma regra. Se ao escrever
  um verbete a regra não existir em lugar nenhum, isso é achado — vai para `## Achados da execução`,
  não vira doutrina nova criada no glossário.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` → exit 0; e todo termo em **negrito ou
  crase** no corpo do README que não seja nome de arquivo tem verbete (varredura do próprio autor).
- **Pronto quando:** os três eixos existem, cada verbete tem definição + ponteiro, e o guarda passa.
