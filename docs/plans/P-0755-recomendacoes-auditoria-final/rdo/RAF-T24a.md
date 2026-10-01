# RDO — P-0755 · RAF-T24a

# Humano

Tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado" concluída em 2026-09-29.
Quem conduz passa a dar destino, no marco, ao card da operação nova que a rodada deixou bloqueado.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 39/54 tarefas concluídas; próxima: "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T24a` — Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa completa, no trecho da rota `modelador` com operação nova da skill `scrum-master`, o destino do card que a rodada registrou `blocked` até o marco: `ready` no aceite da versão, fora do plano na recusa.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;b=Path('.claude/skills/scrum-master/SKILL.md').read_bytes();t=b.decode('utf-8');print('destino=%d-%d cr=%d'%(t.count('quem conduz dá destino a esse card'),t.count('tira o card do plano junto com a linha dele'),b.count(bytes([13]))))"` → `destino=1-1 cr=0` — antes `destino=0-0 cr=0`, depois `destino=1-1 cr=0`

**Pronto quando:** - gerente do loop.rota do modelador com operação nova — o loop despacha o modelador e em seguida o planejador para a rodada, e a janela segue com as tarefas da versão vigente — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-63`, `DRF-14`; `AE-178` (laudo da `RAF-T25`: a regra entregue registra o card da operação nova `blocked`, razão `dependencia`, nota `aguarda o aceite da versão <k> no marco`, e nenhum instrumento nem doutrina o tira de `blocked` no aceite; na recusa, o card fica sem destino nomeado); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T24`
- **Operação do modelo:** `OP-24` - OP-24: Quem executa ensina o gerente do loop a seguir a janela quando o modelador cria operação nova, enfileirando a rodada de replanejamento. - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, Passo 8 (*Roteamento, bloco A*), bullet `- **Triagem:**`, o trecho da `rota=modelador` com operação nova que a `RAF-T24` escreveu; nenhum código muda. O comportamento que a doutrina descreve já está nos instrumentos: `encerrar.py marco --aceita-versao <k>` promove a `## 1A` e reescreve o campo `Operação do modelo` dos cards, sem tocar o `estado.tsv` das tarefas (`gravar_marco` só transita a linha do plano, no Marco 1 `go`); `backlog.py status <ID> ready` tira de `blocked` uma tarefa (medido na condução, Marcos 2 e 3, `RAF-T7` e `RAF-T19`); o `modelo.py check`, com ou sem `--so-vigente`, acusa `V4` o card que cita operação que não está na vigente nem na pendente, sem olhar o status do card (`validar`, lido no código), e por isso o card da operação recusada não fica no plano nem como `cancelled`. A regra mora só neste trecho da skill; o parágrafo `**Card da operação nova**` do planejador (`RAF-T25`) não a repete. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Passos:** 1. No `### Passo 8 — Roteamento, bloco A`, no bullet que começa por `- **Triagem:**` (uma linha só no arquivo), trocar o trecho antigo pelo novo, sem quebra nova e sem refluxo: o trecho fica na mesma linha. Trecho antigo: ```text e a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao`, `R-04` da auditoria final, `P-0755`); ``` Trecho novo: ```text e a `## 1A` é cobrada no marco (`encerrar.py marco --aceita-versao`, `R-04` da auditoria final, `P-0755`); gravado o marco, quem conduz dá destino a esse card, que o `encerrar.py marco` não tira de `blocked`: com `--aceita-versao <k>`, todo card `blocked` com a nota `aguarda o aceite da versão <k> no marco` passa a `ready` (`python .claude/tools/backlog.py status <ID> ready`); com `--recusa-versao <k>`, o consultor, a quem o caso volta, tira o card do plano junto com a linha dele no `estado.tsv`, porque a operação que ele materializa saiu com a versão recusada e o `modelo.py check` o acusaria `V4` (`AE-178` do `P-0755`); ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - A skill fica em LF: nenhum retorno de carro (CR) no arquivo ao fim (`cr=0` na Verificação 1). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas outras rotas do bullet `- **Triagem:**` nem no resto do trecho da `RAF-T24`; não mexer na seção `### O que obriga parada e o que segue com registro` nem nas regras `A3a`..`B1` das tabelas; não editar `.claude/agents/pantonic-planner.md` nem `.claude/tools/encerrar.py`.
- **Contingências:** - se o trecho antigo não existir verbatim, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando o bullet `- **Triagem:**`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** o trecho da rota do modelador com operação nova (`RAF-T24`, feito); o card da operação nova, escrito pelo planejador (`RAF-T25`, feito); a promoção no marco (`RAF-T23`); a saída automática de `blocked` pelo `encerrar.py marco`, na aceitação e no gate de etapa (`DRF-63`, rota auditoria final).
- **Handover:** 2026-09-29 · para `RAF-T27` - **Entregue:** .claude/skills/scrum-master/SKILL.md Passo 8, Triagem: no aceite da versão k, todo card blocked com a nota 'aguarda o aceite da versão <k> no marco' vai a ready; na recusa, o caso volta ao consultor, que tira o card do plano e do estado.tsv - **Contrato:** o card da operação nova tem destino nomeado no aceite e na recusa do marco - **Não refazer:** a troca do trecho da skill - **Pendente:** nenhum

## Execução

**Consumo:** 10 tool uses, 51.9 k tokens, 246.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Troca verbatim conferida por reconstrucao: o arquivo do ref com o trecho antigo substituido pelo novo e byte a byte igual a arvore (445 linhas nos dois, trecho antigo 1 ocorrencia, CR 0). Exercicio ponta a ponta da regra contra os instrumentos que ela cita: backlog.py admite a transicao blocked->ready; encerrar.py marco tem --aceita-versao e --recusa-versao; o validar do modelo.py emite V4 para operacao fora da vigente e da pendente sem olhar status do card - as tres afirmacoes da doutrina casam com o codigo. O ramo de recusa manda o consultor tirar a linha do estado.tsv sem verbo de instrumento para isso (backlog.py nao tem remocao); decisao do card (DRF-63), fora do julgamento desta entrega.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O planejador escreve, na rodada que segue a emenda, o card da operação nova bloqueado até o marco" e vai pegar a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado".
Tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado" e vai executar: Quem executa completa, no trecho da rota `modelador` com operação nova da skill `scrum-master`, o destino do card que a rodada registrou `blocked` até o marco: `ready` no aceite da versão, fora do plano na recusa.
Agente executor devolveu a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado": review — sem pendência.
Tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado" como done: registrar estado, RDO e telemetria.
