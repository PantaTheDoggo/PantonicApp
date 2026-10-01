# RDO — P-0755 · RAF-T39a

# Humano

Tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela" concluída em 2026-09-30.
A abertura da mensagem de marco passou a nomear a etapa, e o relatório de encerramento remete a essa regra.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 63/64 tarefas concluídas; próxima: "O guia de entrada descreve o kit como ele fica depois das cinco etapas".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T39a` — A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa corrige a subseção de abertura de marco da skill `scrum-master` para que a entrega seja o nome da etapa na tabela de marcos, e faz o primeiro parágrafo do relatório de encerramento remeter à linha que vem antes da saída do `modelo.py show`.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('marco=%d-%d-%d-%d'%(t.count('Quando a janela para num marco'),t.count('logo depois da linha que nomeia a entrega'),t.count('o trecho antes dos dois-pontos'),t.count('a entrega é a célula')))"` → `marco=1-1-1-0` — antes `marco=1-0-0-1`, depois `marco=1-1-1-0`

**Pronto quando:** - gerente do loop.abertura da mensagem de marco — a mensagem de marco abre nomeando a etapa entregue, sem a lista de recomendações, e o parágrafo que manda o relatório abrir pela saída do `modelo.py show` remete a essa linha — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-75`, `DRF-41`; `AE-204` (laudo da `RAF-T39`, ressalva 88, achado 2): a subseção manda a entrega ser a célula *o que o dono lê* inteira, o exemplo do Marco 2 usa só o trecho antes dos dois-pontos e a célula do Marco 1 do `P-0755` é um comando; o primeiro parágrafo do `## Relatório de encerramento` segue dizendo que o relatório abre com a saída do `modelo.py show`.
- **Depende de:** `RAF-T39`
- **Operação do modelo:** `OP-39` - OP-39: Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** doutrina do kit — a skill `.claude/skills/scrum-master/SKILL.md`, seção `## Relatório de encerramento`: o primeiro parágrafo e a subseção `### Quando a janela para num marco`, que a `RAF-T39` escreveu; nenhum código muda. A regra segue morando só na subseção; o primeiro parágrafo ganha uma remissão, não a regra, e a remissão não repete o nome da subseção (a Verificação da `RAF-T39` conta uma ocorrência dele). O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, fazer as duas trocas abaixo, cada uma na mesma linha do trecho antigo, sem quebra nova e sem refluxo; cada trecho antigo existe uma única vez no arquivo. Troca 1, primeiro parágrafo do `## Relatório de encerramento`. Trecho antigo: ```text .claude/tools/modelo.py show --plano <plano>` — a ``` Trecho novo: ```text .claude/tools/modelo.py show --plano <plano>` (na parada de marco, logo depois da linha que nomeia a entrega, na subseção abaixo) — a ``` Troca 2, subseção da parada de marco. Trecho antigo: ```text a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos (plano sem tabela de marcos: o título do plano) ``` Trecho novo: ```text a entrega é o nome da etapa na célula *o que o dono lê* da linha do marco na tabela de marcos, o trecho antes dos dois-pontos, sem a lista que os segue (marco cuja célula não nomeia etapa, como o do modelo, que cita o comando `modelo.py show`, ou plano sem tabela de marcos: o título do plano) ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `630 passed`, 2026-09-30, laudo da `RAF-T39`). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer na lista do `## Relatório de encerramento` nem no primeiro parágrafo além da troca 1; não repetir a regra da subseção em outro trecho; não acrescentar linha ao repertório de mensagens (é gerado pelo gancho); não editar `.claude/tools/progresso_hook.py`.
- **Contingências:** - se um dos dois trechos antigos não existir, ou existir mais de uma vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando a seção `## Relatório de encerramento` inteira. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** o texto da `RAF-T39` (`done`), que fica como executado; a linha do `README.md` sobre a parada de marco (`RAF-T40`); a medida de que a próxima mensagem de marco sai sem pergunta de esclarecimento, que é da condução no Marco 6.
- **Handover:** 2026-09-30 · para `RAF-T40` - **Entregue:** .claude/skills/scrum-master/SKILL.md: a abertura de marco nomeia a etapa (trecho da célula antes dos dois-pontos; sem etapa, o título do plano) e o primeiro parágrafo do Relatório de encerramento remete à exceção do marco - **Contrato:** a mensagem de marco nomeia a etapa e o pedido datado do dono - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 11 tool uses, 51.6 k tokens, 128.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Redacao verbatim: as duas trocas entraram identicas e no ponto ancorado, a remissao do primeiro paragrafo nao repete o nome da subsecao (contagem 1) e o exemplo do Marco 2 agora casa com a regra (trecho antes dos dois-pontos); o AE-204 do laudo da RAF-T39 fecha aqui. O unico vermelho segue sendo a sonda da auditoria, pela sexta tarefa seguida.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou" e vai pegar a tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela".
Tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela" e vai executar: Quem executa corrige a subseção de abertura de marco da skill `scrum-master` para que a entrega seja o nome da etapa na tabela de marcos, e faz o primeiro parágrafo do relatório de encerramento remeter à linha que vem antes da saída do `mo…
Agente executor devolveu a tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela": review — sem pendência.
Tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A abertura de marco nomeia a etapa, e o primeiro parágrafo do relatório remete a ela" como done: registrar estado, RDO e telemetria.
