# RDO — P-0748 · TLG-T4a

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T4a` — A skill deixa de narrar: a transição chega ao painel pela função
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do loop liga cada transição à função: no instante em que o condutor escolhe a tarefa, muda o estado dela, despacha um agente, recebe o que ele devolveu, coleta a evidência ou fecha a tarefa, é a função que recebe o evento e leva a linha ao arquivo de progresso; o condutor deixa de escrever a linha como texto e deixa de precisar lembrar a forma dela, e o que chega ao dono é a transição narrada com o título da tarefa no lugar do identificador.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:50` — as nove linhas que começam por - **Narra:** (linhas 50, 62, 81, 111, 130, 154, 165, 182 e 225 em 2026-09-24, uma por passo 2 a 10, cada uma imediatamente antes da linha - **Ação:** do passo; localizar pelo texto) - `.claude/skills/scrum-master/SKILL.md:365` — o último bullet de ## Guardrails, a linha que começa por - Toda linha do repertório (seção *Repertório de mensagens ao gerente*) é escrita como texto do agente - `.claude/skills/passagem-de-bastao/SKILL.md:12` — a linha que contém que o gancho do kit grava no arquivo de progresso

**Verificação:** 1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` → antes `9` (depois de `TLG-T2b`; `10` em 2026-09-24, `F-26`), depois `0`. 2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "[gerente] " | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`. 3. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "gerada** pelo gancho" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 4. `(Select-String -SimpleMatch -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern "a partir dos eventos do loop" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`; e `arquivo de progresso` → antes `1`, depois `1`. 5. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "- **Ação:**" | Measure-Object).Count` → igual antes e depois (nenhuma linha de ação removida; medir antes e colar os dois valores na linha de retorno). 6. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.

**Pronto quando:** `stream de dados.o que as mensagens narram` — *ligado à tarefa e à intenção dos agentes: uma linha em linguagem humana por transição, gerada pela função no instante em que o loop a atravessa — e não escrita pelo condutor antes de agir —, e é ela que chega ao arquivo de progresso, sem saída de comando entre duas delas* — Verificação 1, 2, 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-30` (a função recebe o evento nos ganchos), `DTG-36` (`DTG-23` revogada, `I-2`/`I-5` reescritas; `DTG-15` — a `passagem-de-bastao` segue como colateral nomeado), `DTG-37` (roda depois de `TLG-T3b`: a função já gera as linhas), `DTG-28` (aceite por conteúdo), `F-26`, `F-27`, `I-2`, `I-5`, `I-11`.
- **Depende de:** `TLG-T3b`
- **Operação do modelo:** `OP-4` - OP-4: O mantenedor do loop liga cada transição à função: no instante em que o condutor escolhe a tarefa, muda o estado dela, despacha um agente, recebe o que ele devolveu, coleta a evidência ou fecha a tarefa, é a função que recebe o evento e leva a linha ao arquivo de progresso; o condutor deixa de escrever a linha como texto e deixa de precisar lembrar a forma dela, e o que chega ao dono é a transição narrada com o título da tarefa no lugar do identificador. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — skill `scrum-master` (remoção dos nove bullets `- **Narra:**` dos passos 2 a 10 e troca do último bullet de `## Guardrails`) e skill `passagem-de-bastao` (uma frase nas linhas 11-13). Nenhum agente, instrumento, teste, `README.md` ou configuração. A função que gera as linhas é o `progresso_hook.py` de `TLG-T3b`, já entregue; este card não o edita.
- **Domínio:** *ligar a transição à função* = a skill deixa de mandar o condutor escrever a linha e passa a dizer que a linha é gerada pelo gancho no evento (`I-2`, `I-5`); o condutor continua fazendo exatamente os mesmos atos (`backlog.py next`, `status`, despacho, `review_evidence.py`, `rdo.py close`) — são eles os eventos. *Marcador* = `[gerente] `, que deixa de existir na skill.
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** (a) na `scrum-master`, cada uma das nove linhas que começam por `- **Narra:**` é **removida inteira** (a linha `- **Ação:**` que a seguia fica onde está, sem linha em branco nova). (b) O último bullet de `## Guardrails` (a linha inteira que começa por `- Toda linha do repertório (seção *Repertório de mensagens ao gerente*) é escrita como texto do agente`) é substituído por esta linha, uma só: ``` - O gerente acompanha a execução num painel fora da extensão que mostra `.claude/estado/progresso.txt`; cada linha desse arquivo é **gerada** pelo gancho `.claude/tools/progresso_hook.py` (eventos `PreToolUse`, `PostToolUse` e `Stop`) a partir do evento da transição — `backlog.py next`, `backlog.py status`, o despacho e o retorno de cada agente, `review_evidence.py` e o encerramento —, com o título da tarefa no lugar da sigla (seção *Repertório de mensagens ao gerente*). O condutor **não escreve** linha de repertório, não usa marcador e não escreve no arquivo; nenhuma saída de ferramenta chega a ele (`P-0748`, `DTG-30`, `I-2`, `I-11`). ``` (c) Na `passagem-de-bastao`, o trecho `que o gancho do kit grava no arquivo de progresso` (nas linhas 11-13, hoje: *"o que chega ao dono chega pelas linhas do **repertório de mensagens ao gerente**, que o gancho do kit grava no arquivo de progresso, e pelo **relatório de encerramento**"*) passa a `que o gancho do kit gera a partir dos eventos do loop e grava no arquivo de progresso`; o resto da frase fica.
- **Passos:** 1. Na `scrum-master`, remover as nove linhas que começam por `- **Narra:**`. 2. Substituir o último bullet de `## Guardrails` pela linha de `Texto novo, literal` (b). 3. Na `passagem-de-bastao`, trocar o trecho de `Texto novo, literal` (c). 4. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `I-2` — a skill não manda o condutor escrever linha nenhuma do repertório; `I-11` — a skill não manda o loop escrever no arquivo; `DTG-36` — nenhum marcador, nenhum início de frase, nenhuma frase do repertório recopiada (a tabela de `TLG-T2b` fica intacta); `DTG-28` — nada de `numstat`: aceite por conteúdo. Na `scrum-master`, só as nove remoções e a troca de um bullet; na `passagem-de-bastao`, só a troca do trecho.
- **Não fazer:** não editar bullets `**Ação:**`, `**Gatilho:**`, `**Entrada:**`, `**Saída:**` nem nenhuma outra linha dos passos; não editar a seção `## Repertório de mensagens ao gerente` (é `TLG-T2b`); não remover outros bullets de `## Guardrails`; não editar agente, instrumento, `progresso_hook.py`, `projecoes.json`, testes ou `README.md` (é `TLG-T5`); não acrescentar instrução nova de narração.
- **Contingências:** 1. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` não for `9` antes da edição → parar e sinalizar `blocked` razão `dependencia` se for `10` (`TLG-T2b` não entregou o parágrafo), `premissa` para qualquer outro valor, devolvendo a saída de `grep -n "Narra:" .claude/skills/scrum-master/SKILL.md`; 2. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "[gerente] " | Measure-Object).Count` não for `1` antes da edição → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "gerente\]" .claude/skills/scrum-master/SKILL.md`; 3. se a `passagem-de-bastao` não contém `que o gancho do kit grava no arquivo de progresso` exatamente uma vez → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "arquivo de progresso" .claude/skills/passagem-de-bastao/SKILL.md`.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho.
- **Fora do escopo desta tarefa:** a descrição pública e o painel (`TLG-T5`); a leitura do painel pelo dono (Marco 3, aceite de marco e não de card, `I-6`).

## Execução

**Consumo:** 20 tool uses, 59.9 k tokens, 165.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: - **Ação:** antes=10 depois=10

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
