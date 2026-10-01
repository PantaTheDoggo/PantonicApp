# RDO — P-0755 · RAF-T24

# Humano

Tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada" concluída em 2026-09-29.
Quem conduz o loop passa a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 37/53 tarefas concluídas; próxima: "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T24` — Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('rodada=%d'%t.count('o loop despacha em seguida o '))"` → `rodada=1` — antes `rodada=0`, depois `rodada=1`

**Pronto quando:** - gerente do loop.rota do modelador com operação nova — o loop despacha o modelador e em seguida o planejador para a rodada, e a janela segue com as tarefas da versão vigente — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-1`, `DRF-14`; `F-19`, `F-21` (a rota `modelador` segue sem parar a janela, mas a emenda que cria operação sem card recusava o despacho seguinte); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T20`
- **Operação do modelo:** `OP-24` - OP-24: Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento. - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, Passo 8 (*Roteamento, bloco A*), bullet `- **Triagem:**`, trecho da `rota=modelador`; nenhum código muda. O comportamento que a doutrina descreve já está nos instrumentos: o `despachar` roda `modelo.py check --so-vigente` desde a `RAF-T20` (a `## 1A` não recusa o despacho), o `check` completo acusa a operação nova sem card como `1A: V1 OP-<n> — operação sem tarefa` e o `encerrar.py marco --aceita-versao` cobra a `## 1A` sem violação desde a `RAF-T23`. Quem escreve o card da operação nova é o planejador, na rodada (`RAF-T25`). A regra mora só neste trecho da skill; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Passos:** 1. No `### Passo 8 — Roteamento, bloco A`, no bullet que começa por `- **Triagem:**` (uma linha só no arquivo), trocar o trecho antigo pelo novo, sem quebra nova e sem refluxo: o trecho fica na mesma linha. Trecho antigo: ```text e com a recusa o caso volta ao consultor para resolver preservando o modelo; ``` Trecho novo: ```text e com a recusa o caso volta ao consultor para resolver preservando o modelo; quando, depois do modelador, `python .claude/tools/modelo.py check --plano <plano>` (sem `--so-vigente`) acusar `1A: V1 OP-<n> — operação sem tarefa`, a emenda criou operação nova, e o loop despacha em seguida o `pantonic-planner` para a rodada de replanejamento, que escreve o card dessa operação `blocked` até o aceite da versão no marco — a janela segue com as tarefas da versão vigente, porque o `despachar` julga só a `## 1` (`modelo.py check --so-vigente`) e a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao`, `R-04` da auditoria final, `P-0755`); ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas outras rotas do bullet `- **Triagem:**` nem na seção `### O que obriga parada e o que segue com registro`; não mexer nas regras `A3a`..`B1` das tabelas; não editar `.claude/agents/pantonic-planner.md` (o card da operação nova é da `RAF-T25`) nem `.claude/agents/pantonic-consultant.md`.
- **Contingências:** - se o trecho antigo não existir verbatim, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando o bullet `- **Triagem:**`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** o `--so-vigente` e o despacho que o usa (`RAF-T19`, `RAF-T20`); o card da operação nova, escrito pelo planejador (`RAF-T25`); a promoção no marco (`RAF-T23`).
- **Handover:** 2026-09-29 · para `RAF-T25` - **Entregue:** .claude/skills/scrum-master/SKILL.md: rota modelador com operação nova segue a janela e enfileira a rodada de replanejamento (R-04) - **Contrato:** quem conduz não para a janela quando o modelador cria operação nova; a rodada vira a próxima tarefa - **Não refazer:** o trecho da skill - **Pendente:** nenhum

## Execução

**Consumo:** 10 tool uses, 51.7 k tokens, 143.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Card de redacao com trecho antigo e novo em bloco cercado e verificacao por contagem de frase: a entrega bateu byte a byte com a substituicao prescrita (arquivo = original com o trecho trocado, mesma contagem de linhas), e a conferencia ponta a ponta das tres afirmacoes do trecho contra os instrumentos (modelo.py emite '1A: V1 OP-<n> — operação sem tarefa' so sem --so-vigente; backlog.py despachar chama check --so-vigente; encerrar.py marco --aceita-versao existe) fechou sem divergencia.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py" e vai pegar a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada".
Tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada" e vai executar: Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento.
Agente executor devolveu a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada": review — sem pendência.
Tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada" como done: registrar estado, RDO e telemetria.
