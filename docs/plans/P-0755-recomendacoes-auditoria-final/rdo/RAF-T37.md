# RDO — P-0755 · RAF-T37

# Humano

Tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando" concluída em 2026-09-30.
O pedido do planejador ao modelador deixou de exigir caminho, linha e nome de comando.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 60/63 tarefas concluídas; próxima: "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T37` — O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa tira do pedido do planejador ao modelador a exigência de caminho, linha e nome de comando nas células descritivas do modelo.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('contrato=%d'%t.count('do modelador os recusa'))"` → `contrato=1` — antes `contrato=0`, depois `contrato=1`

**Pronto quando:** - planejador.pedido ao modelador — o roteiro diz que o pedido não exige caminho, linha nem nome de comando nas células descritivas, e que esses dados vão aos fatos do plano e ao card — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-24`; `F-28` (a Fase 3a não traz o pedido de caminho, o dossiê de autoria do plano fictício o pediu por conta própria e o modelador o recusou pela norma `TK-76`); relatório `R-22` (auditoria reg. 7).
- **Depende de:** `RAF-T36`
- **Operação do modelo:** `OP-37` - OP-37: Quem executa tira do pedido do planejador ao modelador a exigência de caminho, linha e nome de comando nas células descritivas do modelo. - precisa de: planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; modelador — Quem implementa troca a regra da promoção da versão aceita, que deixa de ser ato do modelador salvo no conflito.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, `### Fase 3a — Esqueleto e dossiê (SAÍDA 3)`, o parágrafo que começa por `Então **pare** e devolva, na linha de retorno, o dossiê` (os seis campos do dossiê `Ato de modelo` de `autoria`), campo `Restrição`; nenhum código muda. A norma `TK-76` mora na definição do modelador (`.claude/agents/pantonic-model-designer.md`: nas células descritivas não entram caminho de arquivo, número de linha, identificador de decisão, fato ou item, nome de instrumento nem remissão a outra seção), que este card não edita; o planejador passa a dizer, no próprio pedido, que não exige esses dados e onde eles moram. O contrato do objeto é: "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text `tarefas: <prefixo>-T<n>` para `OP-<n>`) e `Devolver` (a §1 inteira e a linha da versão 1). ``` Trecho novo: ```text `tarefas: <prefixo>-T<n>` para `OP-<n>`; e nunca caminho de arquivo, número de linha nem nome de instrumento nas células descritivas do modelo — a norma `TK-76` do modelador os recusa, e essas residências vão à seção 2 do plano e à `Camada e fronteira` do card, `R-22` da auditoria final, `P-0755`) e `Devolver` (a §1 inteira e a linha da versão 1). ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo e exige nele `SAÍDA 3` e `Fase 3b`, que o passo não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/agents/pantonic-model-designer.md` (a norma `TK-76` fica onde está); não mexer nos outros cinco campos do dossiê nem no esqueleto da Fase 3a; não mexer na tabela de profundidade (`RAF-T36`) nem na Fase 5 (`RAF-T38`).
- **Contingências:** - se o trecho antigo não existir verbatim, uma única vez, em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando o parágrafo que começa por `Então **pare** e devolva`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** a régua de profundidade (`RAF-T36`); a checagem de versão do kit (`RAF-T38`); a norma `TK-76` do modelador, que não muda.
- **Handover:** 2026-09-30 · para quem vier depois - **Entregue:** .claude/agents/pantonic-planner.md: o pedido do planejador ao modelador (dossiê de autoria) deixa de exigir caminho, linha e nome de comando - **Contrato:** o dossiê de autoria ao modelador fala do domínio, sem caminho, linha nem comando - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 10 tool uses, 50.2 k tokens, 123.8 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto" e vai pegar a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando".
Tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando" e vai executar: Quem executa tira do pedido do planejador ao modelador a exigência de caminho, linha e nome de comando nas células descritivas do modelo.
Agente executor devolveu a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando": review — sem pendência.
Tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando" como done: registrar estado, RDO e telemetria.
