# RDO — P-0755 · RAF-T4

# Humano

Tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora" concluída em 2026-09-28.
Quem conduz o loop passa a repassar ao executor o recado pronto do despacho, sem copiar o card nem reconferir âncoras.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 6/42 tarefas concluídas; próxima: "O gatilho do próximo passo responde só ao dono".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T4` — Quem conduz repassa o texto pronto do despacho e não reconfere âncora
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('entrega=%d-%d'%(t.count('com o dossiê da tarefa e a instrução de devolver'),t.count('repassado como está — sem copiar o card nem o handover na conversa')))"` → `entrega=0-1` — antes `entrega=1-0`, depois `entrega=0-1` 2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('ancoras=%d-%d'%(t.count('re-derivadas no ato'),t.count('nenhum passo as reconfere à mão')))"` → `ancoras=0-1` — antes `ancoras=1-0`, depois `ancoras=0-1`

**Pronto quando:** - gerente do loop.entrega do despacho ao executor — quem conduz repassa ao executor o texto pronto do despacho, que aponta o arquivo do pacote: perto de mil tokens por tarefa, ou menos — Verificação 1 - gerente do loop.conferência das âncoras — nenhum passo manda reconferir: as âncoras chegam conferidas no pacote — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-7`, `DRF-8`, `DRF-45`; `F-6`, `F-8` (Passo 3 e Passo 4 da skill `scrum-master`); relatório `R-02`, `R-03`.
- **Depende de:** `RAF-T1a`, `RAF-T3`, `RAF-T3a`
- **Operação do modelo:** `OP-4` - OP-4: Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card. - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, rotina de quem conduz o loop; nenhum código muda. O comportamento que a doutrina descreve já está no `despachar` desde a `RAF-T3`: grava o pacote em `<pasta-do-plano>/despacho/<ID>.md` (card, handovers e âncoras conferidas) e imprime, entre a linha `=== DESPACHO:` e a linha `ref=<sha>`, o texto pronto ao executor (a linha `despacho: <P-id> <ID>`, o caminho do pacote e a gramática da linha de retorno). A regra muda só nos Passos 3 e 4; nenhum outro arquivo a repete.
- **Passos:** 1. No `### Passo 3 — Gates herdados`, no parágrafo que começa por `**Por comando** (`, trocar as duas linhas do texto antigo pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo). Texto antigo: ```text `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem ``` Texto novo: ```text `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>`, grava o pacote da tarefa em `<pasta-do-plano>/despacho/<ID>.md` (fora do versionamento: o card, os handovers e as âncoras conferidas contra a árvore de agora) e imprime só o texto pronto do despacho ao executor e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem ``` 2. No `### Passo 4 — Despacho do executor`, trocar as cinco linhas do texto antigo pelas sete do texto novo (mesma regra de quebra e recuo). Texto antigo: ```text Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na linha `ref=<sha>` da saída: este passo só invoca o executor. Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente), com o dossiê da tarefa e a instrução de devolver **uma única linha**, domínio fechado (`DP-G` ``` Texto novo: ```text Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado, o pacote em `<pasta-do-plano>/despacho/<ID>.md` e o `<ref>` na linha `ref=<sha>` da saída: este passo só invoca o executor. Invocar `pantonic-executor` com `model` **igual ao do cabeçalho** (vence o `model:` do agente), com o texto pronto que o `despachar` imprimiu entre a linha `=== DESPACHO:` e a linha `ref=<sha>`, repassado como está — sem copiar o card nem o handover na conversa —, que já traz a instrução de devolver **uma única linha**, domínio fechado (`DP-G` ``` 3. No mesmo Passo 4, trocar as três linhas do texto antigo pelas três do texto novo (mesma regra de quebra e recuo). Texto antigo: ```text O despacho cola, junto do dossiê, as **âncoras** (arquivo, linha e texto do ponto a editar) re-derivadas no ato e o **range de linhas do bullet de fechamento anterior** quando a tarefa fecha em plano em andamento. ``` Texto novo: ```text As **âncoras** (arquivo, linha e texto do ponto a editar) chegam conferidas no pacote do despacho; nenhum passo as reconfere à mão. Quando a tarefa fecha em plano em andamento, o despacho acrescenta ao texto pronto o **range de linhas do bullet de fechamento anterior**. ``` 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que os passos não tocam. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nos gates do Passo 3 nem no caminho à mão do card de tíquete; não mexer na gramática da linha de retorno (o bloco cercado com `<tarefa> review`); não mexer no bloco `- **Janela:**` do Passo 1 (`RAF-T1`); não editar `.claude/tools/backlog.py` (a mecânica é da `RAF-T3`).
- **Contingências:** - se o texto antigo de um dos passos 1 a 3 não existir verbatim em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** a mecânica do pacote e das âncoras (`RAF-T3`); a rota do modelador com operação nova (`RAF-T24`); o despacho do consultor com a linha do card em triagem (`RAF-T34`).
- **Handover:** 2026-09-28 · para quem vier depois - **Entregue:** Passos 3 e 4 da skill scrum-master (.claude/skills/scrum-master/SKILL.md) mandam repassar ao executor o texto pronto do despachar, com o pacote em <pasta do plano>/despacho/<ID>.md, sem copiar o card nem reconferir âncora - **Contrato:** quem conduz repassa o recado impresso pelo despachar; as âncoras vêm conferidas no pacote - **Não refazer:** as três trocas de prosa nos Passos 3 e 4 - **Pendente:** passagem-de-bastao Gate de delegação item 3 e o campo Entrada do Passo 4 ainda mandam re-derivar/copiar (em triagem do consultor)

## Execução

**Consumo:** 11 tool uses, 55.9 k tokens, 142.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu" e vai pegar a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora".
Tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora" e vai executar: Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card.
Agente executor devolveu a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora": review — sem pendência.
Tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora" como done: registrar estado, RDO e telemetria.
