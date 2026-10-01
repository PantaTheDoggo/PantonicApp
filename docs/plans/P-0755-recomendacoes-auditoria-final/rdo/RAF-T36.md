# RDO — P-0755 · RAF-T36

# Humano

Tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano" concluída em 2026-09-30.
O planejador passou a dispensar, em plano de até cinco operações, os itens da auto-auditoria que não mudam o resultado.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 58/63 tarefas concluídas; próxima: "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T36` — O planejador ganha a régua de profundidade pelo tamanho do plano
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa dá ao planejador uma régua de profundidade pelo tamanho do plano, que dispensa no plano de até cinco operações os itens que não mudam o resultado.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('regua=%d-%d'%(t.count('a razão é a própria classe'),t.count('até 5 operações, qualquer classe')))"` → `regua=0-1` — antes `regua=1-0`, depois `regua=0-1`

**Pronto quando:** - planejador.profundidade do planejamento — uma régua pelo tamanho do plano dispensa, no plano de até cinco operações, os itens que não mudam o resultado — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-2`, `DRF-23` (o conteúdo da régua); `F-6` (o planejamento custou 352,2k de 1.250,0k do gasto de subagentes do plano fictício); `F-28` (a tabela de profundidade da Fase 4); relatório `R-21` (auditoria reg. 8 e 9).
- **Depende de:** `RAF-T29`, `RAF-T29a`, `RAF-T34`, `RAF-T35`
- **Operação do modelo:** `OP-36` - OP-36: Quem executa dá ao planejador uma régua de profundidade pelo tamanho do plano, que dispensa no plano de até cinco operações os itens que não mudam o resultado. - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, abertura da `### Fase 4 — Auto-auditoria (antes de gravar, uma passada)`: o parágrafo que começa por `**Profundidade pela classe do plano.**` e a tabela de três linhas que o segue; nenhum código muda. Primeira tarefa da etapa E: nasce `blocked` até o `go` do Marco 5 (`DRF-5`). A régua mora só nessa tabela; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text **Profundidade pela classe do plano.** ``` Trecho novo: ```text **Profundidade pela classe e pelo tamanho do plano.** ``` 2. No mesmo parágrafo, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text tabela dispensa não se aplica, e a razão é a própria classe. ``` Trecho novo: ```text tabela dispensa não se aplica, e a razão é a classe ou o tamanho. Plano cuja seção 1.2 tem até cinco operações usa a última coluna, qualquer que seja a classe declarada (`R-21` da auditoria final, `P-0755`): nesse tamanho, o parser frio, a segunda leva e o ensaio sem arquivo compartilhado não mudam o resultado, e o ensaio da contingência só o muda quando ela escreve arquivo. ``` 3. Trocar a tabela que segue o parágrafo (cinco linhas) pela tabela nova (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0). Trecho antigo: ```text | itens | ferramentaria | doutrina | produto | |---|---|---|---| | 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam | | 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam | | 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica | ``` Trecho novo: ```text | itens | ferramentaria | doutrina | produto | até 5 operações, qualquer classe | |---|---|---|---|---| | 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam | aplicam | | 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam | só com gramática ou tabela normativa no plano | | 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica | só com arquivo compartilhado tocado por dois cards; o ensaio da contingência, só quando a contingência escreve arquivo | ``` 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo e recusa nele os literais `atômic`, `50%`, `~80 linhas`, `tabela de classes` e `tabela de tetos`, que o texto novo não tem. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever os itens 1 a 14 da Fase 4 nem o parágrafo **A contingência se ensaia** do item 14; não mexer na Fase 3a (`RAF-T37`) nem na Fase 5 (`RAF-T38`); não criar outra tabela nem repetir a régua em outro arquivo.
- **Contingências:** - se algum dos três trechos antigos não existir verbatim, uma única vez, em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas do parágrafo que começa por `**Profundidade pela` até o item 1 da Fase 4. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** o pedido do planejador ao modelador (`RAF-T37`); a checagem de versão do kit (`RAF-T38`); a medida do ganho da `R-21` sobre o custo de planejamento, que é da condução no relatório do Marco 6 (§7).
- **Handover:** 2026-09-30 · para quem vier depois - **Entregue:** .claude/agents/pantonic-planner.md, Fase 4 (Auto-auditoria): a profundidade passa a ser pela classe e pelo tamanho do plano, com a régua que dispensa no plano de até cinco operações os itens que não mudam o resultado - **Contrato:** o planejador lê a régua de profundidade pelo tamanho do plano na Fase 4 - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 16 tool uses, 53.6 k tokens, 136.7 s (fonte: `<usage>` do encerramento)

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

Tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano" e vai executar: Quem executa dá ao planejador uma régua de profundidade pelo tamanho do plano, que dispensa no plano de até cinco operações os itens que não mudam o resultado.
Agente executor devolveu a tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano": review — sem pendência.
Tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano" como done: registrar estado, RDO e telemetria.
