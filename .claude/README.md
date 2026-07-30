# Kit agêntico Pantonic* — agentes e skills reusáveis

Este diretório é o **kit padrão** de todo projeto Pantonic*. Ao criar um projeto novo, copie
`agents/` e `skills/` para o `.claude/` do projeto e ajuste apenas os caminhos citados nos
blocos de "fatos estáveis" dos agentes. Fundamentos: `GOVERNANCA.md` e
`ARQUITETURA_PANTONICA.md` na raiz da pasta PantonicApp.

## Agentes (`agents/`)

<!-- kit:agents:begin -->
| Agente | Modelo | Papel |
|---|---|---|
| `pantonic-auditor-arch` | Opus | Auditor de clean architecture Pantonic*. Invocado pelo usuário para ler a codebase e criar um checklist de desvios de clean architecture com ações de recuperação da qualidade arquitetural. Não altera código. |
| `pantonic-auditor-cleancode` | Sonnet | Auditor de clean code Pantonic*. Invocado pelo usuário para inspecionar a codebase e identificar code smells — principalmente desvios de coesão e acoplamento — produzindo checklist de apontamentos com ações de correção. Não altera código. |
| `pantonic-auditor-container` | Sonnet | Auditor de containerização Pantonic*. Invocado pelo usuário para inspecionar o empacotamento e o runtime do container — Dockerfile, 12-factor, concorrência/event loop, shutdown, observabilidade — e produzir checklist de desvios das melhores práticas com ações de correção. Não altera código. |
| `pantonic-auditor-pyside6` | Sonnet | Auditor de PySide6 Pantonic*. Invocado pelo usuário para inspecionar o uso do framework Qt na codebase — threading, signals/slots, ownership, layouts, model/view, performance — e produzir checklist de desvios das melhores práticas com ações de correção. Não altera código. |
| `pantonic-benchmarker` | Haiku | Agente coletor de benchmarking Pantonic* (somente leitura + escrita do próprio relatório, modelo barato). Usar para produzir, a partir de UM repositório público confirmado, um relatório de benchmarking no esquema fixo de 16 dimensões (D1..D16), sem juízo sobre o PantonicApp. |
| `pantonic-executor` | Sonnet | Agente de execução Pantonic*. Usar para implementar UMA tarefa atômica do diário de obras por contexto, com TDD (teste funcional + regressão) e guardrails de clean architecture. Não replaneja escopo. |
| `pantonic-fora-da-caixa` | Opus | Agente fora-da-caixa Pantonic*. Invocado pelo usuário para varrer a codebase, identificar procedimentos que ficaram complexos por acúmulo de correções e extensões, e propor redesenhos "como se recomeçasse do zero hoje" — mais simples, robustos e diretos. Não altera código. |
| `pantonic-planner` | Opus | Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor qualquer procedimento complexo em checklists de tarefas atômicas registrados no diário de obras. Não implementa código. |
| `pantonic-scout` | Haiku | Agente de coleta Pantonic* (somente leitura, modelo barato). Usar para search, grep e leitura de codebase/documentos, devolvendo dossiês compactos que preservam o contexto dos agentes de planejamento e execução. |
<!-- kit:agents:end -->

**Nota sobre o modelo do `pantonic-planner`:** o frontmatter só carrega `model: opus`; a
ressalva de que Fable nunca é escolha automática — só entra sob solicitação explícita do dono,
mesmo em planejamento (CLAUDE.md global, Regra 7) — fica registrada aqui em prosa, fora da
região gerada, para não se perder a cada `kit_check.ps1 -Mode generate`.

Os auditores são invocados pelo usuário, produzem relatórios em `docs/audits/` e **não alteram
código** — apontamentos aceitos viram tíquetes no diário de obras via `pantonic-planner`.
**Antes de invocar qualquer auditor, rode a skill `audit-sweep`** (contexto principal): ela
executa a fase mecânica (greps determinísticos) via `pantonic-scout` (Haiku) e grava
`docs/audits/SWEEP_<data>.md`; o auditor parte do sweep e gasta o modelo caro só na leitura
confirmatória.

**Manutenção dos scouts:** `pantonic-scout` = `context-scout` global
(`~/.claude/agents/context-scout.md`) + bloco de fatos estáveis do projeto. Toda melhoria em
um deve ser replicada no outro — edite sempre os dois juntos.
Bases de conhecimento dos auditores: `D:\Skillstore\Ready\skill\python_clean_architecture_skill.md`
(arch) e `D:\Skillstore\Ready\skill\pyside_skill.md` (pyside6) — ajustar os caminhos se o
Skillstore mudar de lugar.

## Skills (`skills/`)

<!-- kit:skills:begin -->
| Skill | Quando usar |
|---|---|
| `audit-sweep` | Pré-varredura mecânica das auditorias Pantonic* — executa a bateria determinística de greps (arch, pyside6, cleancode, fora-da-caixa) fora dos modelos caros e grava um dossiê compacto em docs/audits/SWEEP_<AAAA-MM-DD>.md. Usar SEMPRE antes de invocar qualquer pantonic-auditor-* ou o pantonic-fora-da-caixa. |
| `bootstrap-pantonic` | Inicializa um novo projeto Pantonic* — os quatro artefatos (PRD, Architecture, Spec, Sprint Plan), a estrutura de docs ATIVO/HISTÓRICO e o esqueleto do core reusável. Usar ao criar um projeto novo da família Pantonic* ou ao auditar se um projeto existente segue o padrão. |
| `checar-versao-kit` | Checa se a versão local do kit agêntico diverge da versão publicada no hub PantonicApp, sem nunca atualizar sozinho. Resolve a versão local em três modos — consumidor (.claude/kit/KIT_VERSION), hub (.claude/KIT_VERSION sem .claude/kit/) e não-instalado. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano"). |
| `diario-de-obras` | Cria e mantém o diário de obras do projeto Pantonic* — kanban central em docs/DIARIO_DE_OBRAS.md com índice, status e arquivamento de planejamentos. Usar ao registrar um plano novo, abrir tíquete avulso, mudar status de tarefa ou condensar itens concluídos. |
| `guardrails-check` | Verifica os guardrails de clean architecture de um projeto Pantonic* antes de marcar uma tarefa como concluída — regra de camadas, ACL, MVVM, egress G6, namespace de estado, conformance e piso de regressão. Usar ao final de toda tarefa de execução ou em auditoria. |
| `handover` | Encerra uma tarefa Pantonic* com handover limpo — atualiza o diário de obras, registra estado e prepara a troca de contexto. Usar ao concluir, bloquear ou interromper qualquer tarefa; nunca iniciar outra tarefa no mesmo contexto. |
| `integrar-poc` | Integra uma POC validada pelo cliente como plugin de uma aplicação Pantonic*, dissecando-a nas camadas da clean architecture (pipeline de 5 passos do agente integrador). Usar quando uma POC standalone foi aprovada e deve virar plugin. |
| `proximo-passo` | Ponto de entrada de contexto novo para "execute o próximo passo do backlog" — drena o inbox de planos, escolhe a próxima tarefa do diário de obras pela diretiva de priorização (ou heurística padrão), delega a execução e fecha com relatório fixo. Usar quando o usuário pedir para pegar/continuar o backlog sem nomear uma tarefa específica. |
<!-- kit:skills:end -->

## Ciclo típico

`bootstrap-pantonic` (planner) → tarefas no diário → para cada tarefa, em contexto limpo:
executor → `guardrails-check` → `handover` → usuário limpa contexto e invoca a próxima.
Novas funcionalidades entram por `integrar-poc`.
