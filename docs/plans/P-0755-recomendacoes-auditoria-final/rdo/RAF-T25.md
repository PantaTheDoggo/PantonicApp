# RDO — P-0755 · RAF-T25

# Humano

Tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco" concluída em 2026-09-29.
O planejador passa a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o marco.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 38/53 tarefas concluídas; próxima: "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T25` — O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o planejador a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o aceite da versão no marco.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('nova=%d'%t.count('**Card da operação nova**'))"` → `nova=1` — antes `nova=0`, depois `nova=1`

**Pronto quando:** - planejador.card da operação nova — na rodada que segue a emenda, o planejador escreve esse card e o registra bloqueado até o aceite da versão no marco — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-1`, `DRF-14`; `F-21` (nada diz quem escreve o card da operação que a emenda cria no meio do loop); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T19`
- **Operação do modelo:** `OP-25` - OP-25: Quem executa ensina o planejador a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o aceite da versão no marco. - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, seção `## Rodada de replanejamento`, passo 4 (*Reescrever os cards*); nenhum código muda. O mecanismo que a regra usa já existe: o `modelo.py check` sem `--so-vigente` acusa a operação nova sem card como `1A: V1 OP-<n> — operação sem tarefa`; com `--so-vigente`, que o despacho usa, a `## 1A` não recusa nada, e o card que cita operação que só existe na `## 1A` não é `V4` (`RAF-T19`); a promoção do marco reescreve o campo `Operação do modelo` dos cards das listas `tarefas:` (`RAF-T23`). A regra mora só no passo 4 da rodada; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, na seção `## Rodada de replanejamento`, logo depois da última linha do parágrafo que começa por `   **Versão pendente reconfere a restrição que cita o estado do plano:**` e antes da linha que começa por `5. **Fechar o estado**`, inserir uma linha vazia e o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os três espaços que sobram no começo de cada linha entram no arquivo). ```text **Card da operação nova** (`R-04` da auditoria final, `P-0755`): na rodada que segue uma emenda que cria operação sem card — o `modelo.py check` sem `--so-vigente` acusa `1A: V1 OP-<n> — operação sem tarefa` —, o planejador escreve o card dessa operação, com o campo `Operação do modelo` copiado da `## 1A` e o id da convenção de lastro sobre o número da operação na `## 1A` (com sufixo `a`, `b`, … quando esse id já existe no plano); apensa o id à lista `tarefas:` da operação na `## 1A`; e registra o card em `estado.tsv` `blocked`, razão `dependencia`, nota `aguarda o aceite da versão <k> no marco`. A janela segue com as tarefas da vigente, e a promoção do marco reescreve o campo dos cards. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outro parágrafo do passo 4 nem os demais passos da rodada; não mexer no item 14 da Fase 4 (`RAF-T17`, `RAF-T18`) nem no bloco `**Árvore do` da Fase 5 (`RAF-T16`); não editar a skill `scrum-master` (a rota do modelador com operação nova é da `RAF-T24`).
- **Contingências:** - se o parágrafo que começa por `   **Versão pendente reconfere a restrição que cita o estado do plano:**`, seguido da linha que começa por `5. **Fechar o estado**`, não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando o passo 4 da rodada inteiro. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** a rota do modelador no loop (`RAF-T24`); a promoção que reescreve os cards (`RAF-T23`); a régua de profundidade e o pedido ao modelador (`RAF-T36`, `RAF-T37`).
- **Handover:** 2026-09-29 · para `RAF-T26` - **Entregue:** .claude/agents/pantonic-planner.md: na rodada que segue a emenda, o planejador escreve o card da operação nova nascido blocked até o marco (R-04) - **Contrato:** operação nova criada por emenda ganha card na rodada seguinte, bloqueado até o aceite do dono no marco - **Não refazer:** o trecho do planejador - **Pendente:** nenhum

## Execução

**Consumo:** 9 tool uses, 51.3 k tokens, 178.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Card de redacao com bloco cercado verbatim e verificacao por contagem de frase: a entrega bateu com o bloco prescrito (9 linhas, uma vazia e oito de prosa, no ponto das ancoras 561/565). A conferencia ponta a ponta das afirmacoes do trecho contra os instrumentos fechou para o que o trecho afirma (modelo.py emite '1A: V1 OP-<n> — operação sem tarefa'; convencao de lastro 'tarefas: <prefixo>-T<n>' existe na linha 214; promover_versao reescreve os cards) e expos o que o trecho nao afirma e o plano nao fechou: a saida de blocked do card no aceite. O card_check do card sai 1 em status review por construcao (compara o mundo antes, nova=0, contra o mundo depois); nao e sinal contra a entrega.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada" e vai pegar a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco".
Tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco" e vai executar: Quem executa ensina o planejador a escrever, na rodada que segue a emenda, o card da operação nova bloqueado até o aceite da versão no marco.
Agente executor devolveu a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco": review — sem pendência.
Tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco" como done: registrar estado, RDO e telemetria.
