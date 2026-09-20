# Kit agêntico Pantonic* — agentes e skills reusáveis

Este diretório é o **kit padrão** de todo projeto Pantonic*. Ao criar um projeto novo, copie
`agents/` e `skills/` para o `.claude/` do projeto e ajuste apenas os caminhos citados nos
blocos de "fatos estáveis" dos agentes. Fundamentos: `GOVERNANCA.md` e
`ARQUITETURA_PANTONICA.md` na raiz da pasta PantonicApp.

## Agentes (`agents/`)

<!-- kit:agents:begin -->
| Agente | Modelo | Papel |
|---|---|---|
| `pantonic-auditor-arch` | Opus | Auditor de clean architecture e DDD Pantonic*. Invocado pelo usuário para ler a codebase e criar um checklist de desvios de clean architecture e DDD com ações de recuperação da qualidade arquitetural. Não altera código. |
| `pantonic-auditor-cleancode` | Sonnet | Auditor de clean code Pantonic*. Invocado pelo usuário para inspecionar a codebase e identificar code smells — principalmente desvios de coesão e acoplamento — produzindo checklist de apontamentos com ações de correção. Não altera código. |
| `pantonic-benchmarker` | Haiku | Agente coletor de benchmarking Pantonic* (somente leitura + escrita do próprio relatório, modelo barato). Usar para produzir, a partir de UM repositório público confirmado, um relatório de benchmarking no esquema fixo de 16 dimensões (D1..D16), sem juízo sobre o PantonicApp. |
| `pantonic-consultant` | Opus | Consultor de plano Pantonic*, instanciado UMA vez por execução de plano e mantido de standby com o cenário inteiro no contexto. Acionado a cada escalonamento para desbloquear impedimento de executor e reparar o modelo funcional do plano, sem que a rodada precise redescobrir o cenário do zero. Figura ad-hoc, provisória, criada por decisão do dono em 2026-09-18. |
| `pantonic-executor` | Sonnet | Agente de execução Pantonic*. Usar para implementar UM MÓDULO COESO do diário de obras por contexto — a disciplina inteira de um tema, não um fragmento —, com TDD (teste funcional + regressão) e guardrails de clean architecture. Não avalia, não decide, não trata ambiguidade — card que exija qualquer um dos três é devolvido como defeituoso. Não replaneja escopo e nunca busca a próxima tarefa. |
| `pantonic-fora-da-caixa` | Opus | Agente fora-da-caixa Pantonic*. Invocado pelo usuário para varrer a codebase, identificar procedimentos que ficaram complexos por acúmulo de correções e extensões, e propor redesenhos "como se recomeçasse do zero hoje" — mais simples, robustos e diretos. Não altera código. |
| `pantonic-planner` | Opus | Agente de planejamento Pantonic*. Usar para produzir PRD, Architecture, Spec e Sprint Plan, e para decompor qualquer procedimento complexo em checklists de tarefas atômicas fechadas, autossuficientes para um executor frio. Não implementa código, não sonda codebase por conta própria e não publica plano com questão aberta. |
| `pantonic-reviewer` | Opus | Reviewer de entrega Pantonic*. Julga a entrega de UM MÓDULO contra o dossiê dele, exercita o módulo ponta a ponta (não só as partes), reconcilia o estado real da árvore com a evidência, marca as sete dimensões da rubrica e emite o laudo pelo gerador. Não edita código, não corrige o que aponta e não replaneja. |
| `pantonic-scout` | Haiku | Agente de coleta Pantonic* (somente leitura, modelo barato). Usar para search, grep e leitura de codebase/documentos, devolvendo dossiês compactos que preservam o contexto dos agentes de planejamento e execução. |
<!-- kit:agents:end -->

**Nota sobre o modelo do `pantonic-planner`:** o frontmatter só carrega `model: opus`; a
ressalva de que Fable nunca é escolha automática — só entra sob solicitação explícita do dono,
mesmo em planejamento (`GOVERNANCA.md` §3) — fica registrada aqui em prosa, fora da
região gerada, para não se perder a cada `kit_check.ps1 -Mode generate`.

Os auditores são invocados pelo usuário, produzem relatórios em `docs/audits/` e **não alteram
código** — apontamentos aceitos viram tíquetes no diário de obras via `pantonic-planner`.
**Antes de invocar qualquer auditor, rode a skill `audit-sweep`** (contexto principal): ela
executa a fase mecânica (greps determinísticos) via `pantonic-scout` (Haiku) e grava
`docs/audits/SWEEP_<data>.md`; o auditor parte do sweep e gasta o modelo caro só na leitura
confirmatória.

**Manutenção dos scouts:** `pantonic-scout` = `context-scout` global (canônico em
`.claude/global/agents/context-scout.md`, projetado no ponto de carga
`~/.claude/agents/context-scout.md`) + bloco de fatos estáveis do projeto. Toda melhoria em
um deve ser replicada no outro — edite sempre os dois juntos.
Bases de conhecimento dos auditores: `D:\Skillstore\Ready\skill\python_clean_architecture_skill.md`
(arch) e `D:\Skillstore\Ready\skill\pyside_skill.md` (pyside6) — ajustar os caminhos se o
Skillstore mudar de lugar.

## Skills (`skills/`)

<!-- kit:skills:begin -->
| Skill | Quando usar |
|---|---|
| `audit-sweep` | Pré-varredura mecânica das auditorias Pantonic* — executa a bateria determinística de greps (arch, DDD, cleancode, fora-da-caixa) fora dos modelos caros e grava um dossiê compacto em docs/audits/SWEEP_<AAAA-MM-DD>.md. Usar SEMPRE antes de invocar qualquer pantonic-auditor-* ou o pantonic-fora-da-caixa. |
| `bootstrap-pantonic` | Inicializa um novo projeto Pantonic* — os quatro artefatos (PRD, Architecture, Spec, Sprint Plan), a estrutura de docs ATIVO/HISTÓRICO e o esqueleto do core reusável. Usar ao criar um projeto novo da família Pantonic* ou ao auditar se um projeto existente segue o padrão. |
| `checar-versao-kit` | Resolve a versão local do kit agêntico e, enquanto o framework estiver com a versão congelada em 0.0.0 (GOVERNANCA.md §10), reporta "congelada — nada a comparar" sem tocar a rede. Fora do congelamento, compara com a versão publicada no hub PantonicApp sem nunca atualizar sozinho, em três modos de resolução (consumidor, hub, não-instalado). Nos dois regimes arma o gatilho de revisão da doutrina (GOVERNANCA.md §7.1), que fica pendente quando existe plano fechado como done no índice do diário sem rodada de revisão registrada. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano"). |
| `diario-de-obras` | Cria e mantém o diário de obras do projeto Pantonic* — kanban central em docs/DIARIO_DE_OBRAS.md com índice, status e arquivamento de planejamentos. Usar ao registrar um plano novo, abrir tíquete avulso, mudar status de tarefa ou condensar itens concluídos. |
| `entrega-de-encerramento` | Produz o documento de encerramento de um plano Pantonic* — o modelo "as-is" que mapeia cada tarefa ao contexto que a motivou, ao artefato concreto que ela criou, a um exemplo real de funcionamento e ao que ela protege, mais o estado honesto do que ficou aberto. É o artefato pelo qual o dono valida o plano. Usar ao fechar qualquer plano, antes de pedir o veredito. |
| `guardrails-check` | Verifica os guardrails de clean architecture de um projeto Pantonic* antes de marcar uma tarefa como concluída — regra de camadas, ACL, egress G6, namespace de estado, conformance e piso de regressão. Usar ao final de toda tarefa de execução ou em auditoria. |
| `integrar-poc` | Integra uma POC validada pelo cliente como plugin de uma aplicação Pantonic*, dissecando-a nas camadas da clean architecture (pipeline de 5 passos). Usar quando uma POC standalone foi aprovada e deve virar plugin. |
| `modelo-por-fase` | Gatilho operacional da regra "modelo por fase" (GOVERNANCA.md §3) — classifica a fase do trabalho (intelectual/execução/varredura), confere o modelo ativo contra a tabela vinculante e para para pedir o /model correto ao dono. Usar no início de qualquer tarefa/subagente, ao trocar de fase no meio de uma sessão, ou quando o hook global de nudge (UserPromptSubmit) disparar o aviso. |
| `passagem-de-bastao` | Maquinário de transição entre tarefas de um plano Pantonic*, na superfície agente↔agente — drena os inboxes, apura a fila pela diretiva, monta o dossiê de delegação sob o gate, herda o contexto da tarefa anterior, fecha a tarefa no registro canônico e grava o checkpoint da janela. Usar como procedimento interno do scrum-master, nunca como ponto de entrada do gerente. |
| `redacao-doc` | Redação de documento publicado — elimina narrativa de proveniência ("historinhas"), citação de interlocutor e ID de processo do corpo de qualquer doc lido por quem não participou da conversa que o gerou. Usar ao autorar, reescrever ou revisar README, doc de arquitetura, doc de governança ou qualquer artefato destinado a leitor externo. |
| `scrum-master` | Conduz o loop de execução de um plano Pantonic* — despacha as tarefas do plano em sequência ao executor e ao reviewer, roteia pelo veredito calculado e encerra a janela por coesão e ocupação de contexto, sem round-trip com o dono a cada tarefa. Usar quando o pedido for tocar um plano inteiro em regime autônomo, e não uma tarefa avulsa. |
<!-- kit:skills:end -->

## Ciclo típico

`bootstrap-pantonic` (planner) → tarefas no diário → para cada tarefa, em contexto limpo:
executor → `guardrails-check` → sinal de retorno → `pantonic-reviewer` → quem orquestra materializa
o status, registra a tarefa e abre o contexto seguinte.
Novas funcionalidades entram por `integrar-poc`.
