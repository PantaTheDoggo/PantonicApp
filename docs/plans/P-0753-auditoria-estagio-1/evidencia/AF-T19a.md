# Evidência de revisão — P-0753 AF-T19a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |  4 ++--
 .claude/agents/pantonic-scout.md                   | 13 ++++++++---
 .claude/global/agents/context-scout.md             | 15 ++++++++----
 .../global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md    |  2 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |  9 ++++----
 .claude/global/skills/context-prep/SKILL.md        |  8 +++----
 .claude/global/skills/onboard/SKILL.md             |  2 +-
 .claude/skills/audit-sweep/SKILL.md                |  2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |  2 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |  2 +-
 GOVERNANCA.md                                      |  2 +-
 README.md                                          |  4 ++--
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/cenario.md   | 27 ++++++++++++++++++----
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/plano.md     | 18 ++++++++-------
 docs/telemetria.tsv                                |  4 ++++
 18 files changed, 79 insertions(+), 40 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: da entrega; estado git: ` M`
- `.claude/agents/pantonic-scout.md` — atribuição: da entrega; estado git: ` M`
- `.claude/global/agents/context-scout.md` — atribuição: da entrega; estado git: ` M`
- `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: da entrega; estado git: ` M`
- `.claude/global/skills/context-prep/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/global/skills/onboard/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/audit-sweep/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/modelo-por-fase/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `README.md` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/cenario.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/plano.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `b3ba047cb323ed0e5ba6e3a40ffc1792f27b605a`
- Arquivos-alvo declarados: `.claude/agents/pantonic-scout.md`, `.claude/global/agents/context-scout.md`, `GOVERNANCA.md`, `README.md`, `.claude/README.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/skills/audit-sweep/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/global/skills/context-prep/SKILL.md`, `.claude/global/skills/onboard/SKILL.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-scout.md`, `.claude/global/agents/context-scout.md`, `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/global/skills/context-prep/SKILL.md`, `.claude/global/skills/onboard/SKILL.md`, `.claude/skills/audit-sweep/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `GOVERNANCA.md`, `README.md`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `docs/ACIONAMENTOS_CONSULTOR.tsv`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-scout.md`
```
diff --git a/.claude/agents/pantonic-scout.md b/.claude/agents/pantonic-scout.md
index d445e5b..49b8fc8 100644
--- a/.claude/agents/pantonic-scout.md
+++ b/.claude/agents/pantonic-scout.md
@@ -1,8 +1,8 @@
 ---
 name: pantonic-scout
-description: Agente de coleta Pantonic* (somente leitura, modelo barato). Usar para search, grep e leitura de codebase/documentos, devolvendo dossiês compactos que preservam o contexto dos agentes de planejamento e execução.
-model: haiku
-tools: Read, Glob, Grep
+description: Agente de coleta Pantonic* (não edita arquivo). Usar para search, grep, leitura de codebase/documentos e comando de consulta que a pergunta traz pronto, devolvendo dossiês compactos que preservam o contexto dos agentes de planejamento e execução.
+model: opus
+tools: Read, Glob, Grep, Bash
 ---
 
 Você é o **agente de coleta** de um projeto Pantonic* (GOVERNANCA.md §3). Recebe UMA pergunta
@@ -30,5 +30,12 @@ um modelo caro, então cada linha precisa pagar seu custo.
 
 - Nunca cole arquivos inteiros nem blocos longos de código.
 - Prefira Grep dirigido a leituras; Read sempre com offset/limit na faixa relevante.
+- **Comando de consulta:** pergunta que traz um comando exato você roda com `Bash`, verbatim, e
+  devolve o stdout literal e o exit code (≤ 40 linhas; passou disso, as 40 primeiras e o número de
+  linhas omitidas). Não roda comando que escreva, mova ou apague arquivo, nem `git` que altere a
+  árvore ou o histórico: pergunta assim não se roda e vai a *Lacunas*, com o comando.
+- **Contagem e filtro:** conte e filtre pela própria ferramenta (modo de contagem, glob, exclusão
+  de pasta, comando de consulta), nunca somando uma lista à mão; o número do dossiê é o que a
+  ferramenta imprimiu.
 - Não avalie, não recomende arquitetura, não proponha mudanças — colete e filtre.
 - Se a pergunta for aberta demais, responda o núcleo e liste em "Lacunas" o que ficou de fora.

```

### `.claude/global/agents/context-scout.md`
```
diff --git a/.claude/global/agents/context-scout.md b/.claude/global/agents/context-scout.md
index c5cfb43..e189a90 100644
--- a/.claude/global/agents/context-scout.md
+++ b/.claude/global/agents/context-scout.md
@@ -1,11 +1,11 @@
 ---
 name: context-scout
-description: Batedor de contexto barato (Haiku). Recebe uma pergunta de exploração sobre o repositório e devolve um dossiê compacto (caminhos, linhas, assinaturas, mapa do que importa) sem colar arquivos inteiros. Usar para varreduras amplas de preparação de contexto antes da fase de análise/implementação no modelo principal. Somente leitura.
-tools: Read, Glob, Grep
-model: haiku
+description: Batedor de contexto. Recebe uma pergunta de exploração sobre o repositório e devolve um dossiê compacto (caminhos, linhas, assinaturas, mapa do que importa) sem colar arquivos inteiros. Usar para varreduras amplas de preparação de contexto antes da fase de análise/implementação no modelo principal. Não edita arquivo.
+tools: Read, Glob, Grep, Bash
+model: opus
 ---
 
-Você é um batedor de contexto: explora o repositório de forma barata e devolve um dossiê
+Você é um batedor de contexto: explora o repositório e devolve um dossiê
 compacto para um modelo mais caro trabalhar em cima. Você NÃO analisa, NÃO opina sobre design e
 NÃO propõe soluções — só localiza e cataloga.
 
@@ -16,6 +16,13 @@ NÃO propõe soluções — só localiza e cataloga.
 - Excluir sempre `build/`, `dist/`, `.venv/`, `__pycache__/`, `node_modules/`, `.git/`.
 - Se existir `docs/DOC_MAP.md`, usá-lo como índice antes de varrer `docs/`.
 - Pare quando a pergunta estiver respondida — não explore "por completude".
+- **Comando de consulta:** pergunta que traz um comando exato você roda com `Bash`, verbatim, e
+  devolve o stdout literal e o exit code (≤ 40 linhas; passou disso, as 40 primeiras e o número de
+  linhas omitidas). Não roda comando que escreva, mova ou apague arquivo, nem `git` que altere a
+  árvore ou o histórico: pergunta assim não se roda e vai a *Lacunas*, com o comando.
+- **Contagem e filtro:** conte e filtre pela própria ferramenta (modo de contagem, glob, exclusão
+  de pasta, comando de consulta), nunca somando uma lista à mão; o número do dossiê é o que a
+  ferramenta imprimiu.
 
 ## Formato do dossiê (sua resposta final)
 

```

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 9751733..5371d0b 100644
--- a/GOVERNANCA.md
+++ b/GOVERNANCA.md
@@ -94,7 +94,7 @@ adequado ao seu custo — a coluna *Modelo* é a tabela vinculante do **modelo p
 | **Execução** | Melhor custo-benefício (Sonnet) | **Executar a tarefa — responsabilidade única**: implementar **uma** tarefa do checklist por vez, em contexto limpo, sob TDD (§4.4), entregando-a **tecnicamente correta** — testes da área tocada, conformance e piso de regressão verdes — e **sinalizando** o resultado (`review`, ou `blocked` com razão tipada) | Não decide, não pergunta ao dono, **não fica com dúvida** — dúvida é sinal de parada, não objeto de deliberação —, não replaneja escopo e não substitui a rota aprovada (G-EXECREADY, G-PLANFIDELITY e G-NOASK, §7 itens 12, 9 e 18): plano não-pronto, obstáculo à rota ou dúvida → para, registra o fato, sinaliza `blocked` e encerra; a parada vai à triagem do consultor, nunca direta ao dono. **Não se ocupa de teto nem de orçamento** — nem de turnos, nem de contexto: estouro se registra no corpo da tarefa como insumo do planejador, nunca vira decisão sua. **Não revisa plano.** Não escreve no diário de obras, não registra o resultado da própria entrega e não afere a própria aceitação — o veredito é da revisão |
 | **Revisão** | O mais poderoso disponível (Opus) — as dimensões de maior peso do laudo são juízo puro, e reviewer no mesmo modelo de quem executou tende a ratificar; é o único gate entre a entrega e o `done` sem round-trip humano | Julgar a entrega de **uma** tarefa contra o dossiê dela e emitir o laudo, em contexto próprio e com a escrita restrita ao caminho do laudo — independência imposta pela lista de ferramentas. Onde a camada mecânica (guardas, conformance, piso, escopo) mediu vermelho, o laudo acompanha a medição; **não escreve no modelo de domínio** do plano (§3.2) — divergência entre a entrega e o texto de uma operação vira achado de alvo `modelo`, e a escrita é do modelador | Não corrige o que aponta, não replaneja e não fecha tarefa: o laudo é o veredito, e o encaminhamento do que ele aponta é da orquestração |
 | **Modelagem** | O mais poderoso disponível (Opus) — escrever o modelo de domínio de um plano é julgamento de domínio, e a consistência entre planos é o que um agente único compra | **Todo** ato sobre o modelo de domínio do plano (§3.2): escrever a seção na autoria, emendá-la quando uma decisão muda o que o plano entrega, resolver conflito entre o texto e a entrega e explicar o contexto do modelo a quem pergunta; devolve o ponteiro da seção, a linha do registro de versões que registra o ato, a saída do `check` e os achados fora da seção (`pantonic-model-designer`) | Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano; não é acionado por outro agente — recebe despacho de quem conduz a sessão |
-| **Coleta** | O mais barato (Haiku ou equivalente) | Search, grep, leitura de codebase/documentos/prompts; filtra e devolve só o pertinente para o contexto dos agentes mais caros | Não edita, não conclui tarefa, não emite juízo sobre o que coletou |
+| **Coleta** | O mais poderoso disponível (Opus) — a coleta alimenta toda decisão seguinte, e erro de contagem ou de escopo nela passa em silêncio | Search, grep, leitura de codebase/documentos/prompts e comando de consulta que a pergunta traz pronto; filtra e devolve só o pertinente, protegendo o contexto de quem pediu. Read de âncora já conhecida ou Grep de string exata, quem precisa do dado faz direto | Não edita, não conclui tarefa, não emite juízo sobre o que coletou; não roda comando que escreva na árvore |
 | **Auditoria** | Melhor custo-benefício (Sonnet) | Medir aderência **sem alterar código**, em duas frentes permanentes: **clean architecture + DDD** (`pantonic-auditor-arch`) e **clean code** (`pantonic-auditor-cleancode`) | Não corrige o que aponta — cada apontamento vira item no diário de obras, priorizado pelo dono |
 | **Redesenho** | O mais poderoso disponível
```
[truncado em 4000 caracteres]

### `README.md`
```
diff --git a/README.md b/README.md
index 09838b8..dc8e347 100644
--- a/README.md
+++ b/README.md
@@ -356,7 +356,7 @@ ficam em `docs/CUSTO_DO_PICKUP.md`.
 |---|---|---|
 | Planejamento (intelectual) | O mais poderoso disponível — Opus | PRD, arquitetura, specs, decomposição do modelo em cards, um por operação |
 | Execução | Melhor custo-benefício — Sonnet | Implementar uma tarefa do checklist por vez, com TDD, em contexto limpo |
-| Coleta / varredura | O mais barato — Haiku | Search, grep, leitura de codebase e documentos; devolve dossiê compacto |
+| Coleta / varredura | O mais poderoso disponível — Opus, em subagente | Search, grep, leitura de codebase e documentos e comando de consulta; devolve dossiê compacto. Leitura pontual, quem precisa do dado faz direto |
 
 Duas ressalvas fazem parte da regra. Um modelo ainda mais caro que o de planejamento **nunca** é
 escolha automática: só entra sob solicitação explícita do dono, mesmo em planejamento. E subir o
@@ -862,7 +862,7 @@ duas falhas.
 | `pantonic-executor` | Sonnet | Implementar **um** card — uma operação do modelo — por contexto, com TDD e guardrails. Não replaneja escopo. |
 | `pantonic-reviewer` | Opus | Julgar a entrega de **uma** tarefa contra o dossiê dela, marcar as sete dimensões da rubrica e emitir o laudo pelo gerador. Não corrige o que aponta. |
 | `pantonic-consultant` | Opus | Ponto de triagem de **toda** parada de executor e de todo laudo com pendência substantiva: devolve a rota `resolve`, `modelador` ou `planejador`, fecha sozinho o técnico e o tático e leva ao dono só o drift do modelo. Efêmero: cada acionamento é uma instância nova que lê o cenário persistido do plano. Não implementa entrega, não julga e não commita. |
-| `pantonic-scout` | Haiku | Buscas, greps e leitura de codebase e documentos; devolve dossiê compacto para preservar o contexto dos caros. |
+| `pantonic-scout` | Opus | Buscas, greps, leitura de codebase e documentos e comando de consulta; devolve dossiê compacto para preservar o contexto de quem pediu. |
 | `pantonic-auditor-arch` | Opus | Auditoria de clean architecture **e DDD**: checklist de desvios de camada e de modelagem de domínio, com ações de recuperação. Não altera código. |
 | `pantonic-auditor-cleancode` | Sonnet | Auditoria de clean code: code smells, coesão e acoplamento. Não altera código. |
 | `pantonic-fora-da-caixa` | Opus | Varrer procedimentos que ficaram complexos por acúmulo e propor o redesenho "como se recomeçasse hoje". |

```

### `.claude/README.md`
```
diff --git a/.claude/README.md b/.claude/README.md
index c883431..348fa8c 100644
--- a/.claude/README.md
+++ b/.claude/README.md
@@ -19,7 +19,7 @@ blocos de "fatos estáveis" dos agentes. Fundamentos: `GOVERNANCA.md` e
 | `pantonic-model-designer` | Opus | Modelador de domínio de plano Pantonic*. Dono único de todo ato sobre a seção Modelo conceitual de um plano - escreve na autoria, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto do modelo. Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano. |
 | `pantonic-planner` | Opus | Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor o modelo de domínio de um plano em cards fechados — um por operação do modelo, autossuficientes para um executor frio. Grava o esqueleto do plano, devolve o dossiê de autoria do modelo e só decompõe depois de a seção do modelo existir. Não implementa código, não sonda codebase por conta própria, não escreve a seção do modelo e não publica plano com questão aberta. |
 | `pantonic-reviewer` | Opus | Reviewer de entrega Pantonic*. Julga a entrega de UM MÓDULO contra o dossiê dele, exercita o módulo ponta a ponta (não só as partes), reconcilia o estado real da árvore com a evidência, marca as sete dimensões da rubrica e emite o laudo pelo gerador. Não edita código, não corrige o que aponta e não replaneja. |
-| `pantonic-scout` | Haiku | Agente de coleta Pantonic* (somente leitura, modelo barato). Usar para search, grep e leitura de codebase/documentos, devolvendo dossiês compactos que preservam o contexto dos agentes de planejamento e execução. |
+| `pantonic-scout` | Opus | Agente de coleta Pantonic* (não edita arquivo). Usar para search, grep, leitura de codebase/documentos e comando de consulta que a pergunta traz pronto, devolvendo dossiês compactos que preservam o contexto dos agentes de planejamento e execução. |
 <!-- kit:agents:end -->
 
 **Nota sobre o modelo do `pantonic-planner`:** o frontmatter só carrega `model: opus`; a
@@ -30,7 +30,7 @@ região gerada, para não se perder a cada `kit_check.ps1 -Mode generate`.
 Os auditores são invocados pelo usuário, produzem relatórios em `docs/audits/` e **não alteram
 código** — apontamentos aceitos viram tíquetes no diário de obras via `pantonic-planner`.
 **Antes de invocar qualquer auditor, rode a skill `audit-sweep`** (contexto principal): ela
-executa a fase mecânica (greps determinísticos) via `pantonic-scout` (Haiku) e grava
+executa a fase mecânica (greps determinísticos) via `pantonic-scout` e grava
 `docs/audits/SWEEP_<data>.md`; o auditor parte do sweep e gasta o modelo caro só na leitura
 confirmatória.
 

```

### `.claude/skills/modelo-por-fase/SKILL.md`
```
diff --git a/.claude/skills/modelo-por-fase/SKILL.md b/.claude/skills/modelo-por-fase/SKILL.md
index e070b57..b3f77b2 100644
--- a/.claude/skills/modelo-por-fase/SKILL.md
+++ b/.claude/skills/modelo-por-fase/SKILL.md
@@ -22,7 +22,7 @@ si.
 |---|---|---|
 | Intelectual (planejar/arquitetar/auditar/decidir/especificar) | Opus (Fable só sob pedido explícito do dono) | PRD, arquitetura, spec, decomposição, auditoria, parecer |
 | Execução (implementar/editar/testar/corrigir) | Sonnet | Um card do diário de obras — a materialização de uma operação do modelo —, TDD |
-| Varredura (search/grep/leitura ampla) | Haiku (ou subagente de coleta) | Levantar contexto antes de planejar/executar |
+| Varredura (search/grep/leitura ampla) | Opus, em subagente de coleta (`pantonic-scout` ou `context-scout`); leitura pontual, direto no modelo ativo | Levantar contexto antes de planejar/executar |
 
 ## Os três gatilhos
 

```

### `.claude/skills/audit-sweep/SKILL.md`
```
diff --git a/.claude/skills/audit-sweep/SKILL.md b/.claude/skills/audit-sweep/SKILL.md
index 1a19e9c..47d768c 100644
--- a/.claude/skills/audit-sweep/SKILL.md
+++ b/.claude/skills/audit-sweep/SKILL.md
@@ -8,7 +8,7 @@ description: Pré-varredura mecânica das auditorias Pantonic* — executa a bat
 Os auditores rodam em Opus/Sonnet e, como subagentes, não podem delegar a ninguém: cada match
 de grep mecânico entraria no contexto do modelo caro. A detecção mecânica é determinística —
 não precisa de inteligência. Esta skill roda a bateria no contexto principal (delegando ao
-`pantonic-scout`, Haiku, pelos critérios da skill context-prep) e grava o resultado num dossiê
+`pantonic-scout`, pelos critérios da skill context-prep) e grava o resultado num dossiê
 que os auditores consomem pronto, gastando o modelo caro só na leitura confirmatória e no
 julgamento.
 

```

### `.claude/skills/passagem-de-bastao/SKILL.md`
```
diff --git a/.claude/skills/passagem-de-bastao/SKILL.md b/.claude/skills/passagem-de-bastao/SKILL.md
index a53540e..4d8770a 100644
--- a/.claude/skills/passagem-de-bastao/SKILL.md
+++ b/.claude/skills/passagem-de-bastao/SKILL.md
@@ -71,7 +71,7 @@ turnos do executor.
 
 **Levantamento de contexto antes do dossiê** — regra de precedência, não gatilho condicional: toda
 coleta que não seja Read de âncora já conhecida (arquivo + range de linhas) ou Grep de string exata
-vai para o papel barato — `pantonic-scout` (agente Pantonic* do projeto) ou, fora dele,
+vai para o papel de coleta — `pantonic-scout` (agente Pantonic* do projeto) ou, fora dele,
 `context-scout` (`.claude/global/agents/context-scout.md`) via skill `context-prep`
 (`.claude/global/skills/context-prep/SKILL.md`) —, nunca para leitura direta do modelo principal.
 O orquestrador monta o prompt de delegação a partir só do dossiê compacto devolvido pelo scout.

```

### `.claude/global/skills/context-prep/SKILL.md`
```
diff --git a/.claude/global/skills/context-prep/SKILL.md b/.claude/global/skills/context-prep/SKILL.md
index 7c9692a..3f3a3db 100644
--- a/.claude/global/skills/context-prep/SKILL.md
+++ b/.claude/global/skills/context-prep/SKILL.md
@@ -1,13 +1,13 @@
 ---
 name: context-prep
-description: Fragmenta a carga inicial de contexto de uma tarefa — delega greps/varreduras exploratórias ao subagente context-scout (Haiku) e entrega ao modelo principal só um dossiê compacto. Usar no início de tarefas que exigem explorar o repositório antes da fase de análise/implementação, ou quando o usuário pedir "preparação de contexto barata".
+description: Fragmenta a carga inicial de contexto de uma tarefa — delega greps/varreduras exploratórias ao subagente context-scout e entrega ao modelo principal só um dossiê compacto, protegendo o contexto dele. Usar no início de tarefas que exigem explorar o repositório antes da fase de análise/implementação, ou quando o usuário pedir "preparação de contexto barata".
 ---
 
-# context-prep — exploração no Haiku, inteligência no modelo principal
+# context-prep — exploração em subagente, inteligência no modelo principal
 
 A saída de greps e leituras exploratórias entra no contexto do modelo que as executa e é
 cobrada na tarifa dele (e recobrada via cache a cada turno seguinte). Esta skill move essa
-fase para o subagente [[context-scout]] (`model: haiku`), preservando o contexto e o custo do
+fase para o subagente [[context-scout]], preservando o contexto do
 modelo principal para a fase intelectual. Complementa [[onboard]] (que cobre docs/planejamento);
 esta cobre a exploração de código específica da tarefa.
 
@@ -27,7 +27,7 @@ esta cobre a exploração de código específica da tarefa.
 
 1. Formule **uma pergunta de exploração fechada** por spawn (não "explore o projeto"), incluindo
    o objetivo da tarefa para o scout priorizar.
-2. Spawn: `Agent` com `subagent_type: context-scout` (o agente já fixa `model: haiku`).
+2. Spawn: `Agent` com `subagent_type: context-scout` (o agente já fixa o modelo).
    Perguntas independentes → múltiplos spawns em paralelo na mesma mensagem.
    **Todo prompt de spawn deve repetir o cap e o formato do dossiê** — encerre o prompt com:
    "Responda com um dossiê de ≤ 40 linhas: resposta direta, arquivos relevantes

```

### `.claude/global/skills/onboard/SKILL.md`
```
diff --git a/.claude/global/skills/onboard/SKILL.md b/.claude/global/skills/onboard/SKILL.md
index 0e5429e..8b94ffb 100644
--- a/.claude/global/skills/onboard/SKILL.md
+++ b/.claude/global/skills/onboard/SKILL.md
@@ -33,7 +33,7 @@ sobre leituras integrais — a mesma lógica de progressive disclosure usada por
    Read integral é proibido nessa faixa de tamanho.
 
 6. **Varreduras amplas.** Quando só a conclusão importa (muitos arquivos, busca exploratória sem
-   alvo certo) — delegar ao subagente `context-scout` (roda em Haiku; critérios de corte na skill
+   alvo certo) — delegar ao subagente `context-scout` (critérios de corte na skill
    [[context-prep]]) em vez de ler tudo no contexto principal.
 
 ## Aceitação

```

### `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
```
diff --git a/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py b/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
index 9a003a8..dac76a9 100644
--- a/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
+++ b/.claude/global/hooks/modelo_por_fase_userpromptsubmit.py
@@ -91,10 +91,11 @@ _NUDGE = {
         "`/model sonnet` se o ativo for Haiku.",
     ),
     "reading": (
-        "\U0001F7E1 Fase de leitura/varredura — Haiku basta, ou delegue ao "
-        "context-scout. Considere `/model haiku`.",
-        "Gate modelo-por-fase: este prompt e leitura/varredura (Regra 7). Prefira "
-        "delegar ao subagente context-scout (Haiku) a ler tudo no modelo caro.",
+        "\U0001F7E1 Fase de leitura/varredura — leitura pontual, faça direto; "
+        "varredura ampla, delegue ao context-scout.",
+        "Gate modelo-por-fase: este prompt e leitura/varredura (Regra 7). Leitura "
+        "pontual (ancora conhecida, grep exato): faca direto. Varredura ampla: delegue "
+        "ao subagente context-scout, para proteger o contexto.",
     ),
 }
 

```

### `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`
```
diff --git a/.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md b/.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md
index 8116b08..42eb359 100644
--- a/.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md
+++ b/.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md
@@ -38,7 +38,7 @@ de preferência (`feedback_opus_default`), contradizendo frontalmente o racional
 - Planejamento, auditoria, arquitetura → modelo caro (Opus) se o dono quiser.
 - Execução (implementar, testar, editar) → modelo de execução (Sonnet), salvo tarefa
   individualmente marcada como de alto risco.
-- Exploração/varredura → modelo barato (Haiku, ex.: context-scout).
+- Exploração/varredura ampla → subagente de coleta (context-scout, Opus), para proteger o contexto; leitura pontual, direto no modelo ativo.
 
 Toda exceção é explícita no arquivo do agente **com o racional de custo confrontado com a
 Regra 1**, nunca herdada de uma preferência genérica.

```

## Medida do executor
- ausente: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T19a-medida.json não existe

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
