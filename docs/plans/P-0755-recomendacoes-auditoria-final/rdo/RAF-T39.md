# RDO — P-0755 · RAF-T39

# Humano

Tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou" concluída em 2026-09-30.
A mensagem de marco passou a abrir nomeando a entrega e o pedido do dono que a originou.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 62/63 tarefas concluídas; próxima: "O guia de entrada descreve o kit como ele fica depois das cinco etapas".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T39` — A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('marco=%d'%t.count('Quando a janela para num marco'))"` → `marco=1` — antes `marco=0`, depois `marco=1`

**Pronto quando:** - gerente do loop.abertura da mensagem de marco — a mensagem de marco abre nomeando a entrega e citando, com a data e poucas palavras do dono, o pedido que a originou — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-26`, `DRF-41`; `F-29` (o repertório de mensagens é gerado pelo gancho e não tem frase de marco; a forma do relatório de encerramento está na skill `scrum-master`); relatório `R-25` (auditoria reg. 46: a mensagem do Marco 2 do `P-0754` levou o dono a perguntar "Você está pedindo mais uma auditoria?").
- **Depende de:** `RAF-T36`
- **Operação do modelo:** `OP-39` - OP-39: Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** doutrina do kit — a skill `.claude/skills/scrum-master/SKILL.md`, seção `## Relatório de encerramento`, que o condutor escreve à mão ao parar a janela; nenhum código muda. O repertório de mensagens ao gerente (`## Repertório de mensagens ao gerente`, ids `M-0`..`M-18`) é gerado pelo gancho `.claude/tools/progresso_hook.py` e não muda. A parada de marco se reconhece pela nota da tarefa: a primeira tarefa de uma etapa nasce `blocked` com a nota `Marco <m>: aguarda o veredito do dono sobre a etapa <X>` (`DRF-5`). A regra mora só na subseção nova; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, logo antes da linha `### Quando a janela fecha o PLANO, e não só a janela`, inserir o bloco abaixo seguido de uma linha vazia (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0). ```text ### Quando a janela para num marco A janela para num marco quando a próxima tarefa do plano está `blocked` à espera do veredito do dono sobre um marco da tabela de marcos do cabeçalho do plano (nota `Marco <m>: …`). Nessa parada, a primeira linha do relatório, antes da saída do `modelo.py show`, nomeia a entrega e o pedido do dono que a originou, na forma `"<entrega>", que você pediu em <data> ("<trecho verbatim do pedido, até 15 palavras>")`: a entrega é a célula *o que o dono lê* da linha do marco na tabela de marcos (plano sem tabela de marcos: o título do plano), e o pedido é a data e um trecho verbatim do ato do dono na seção 0 do plano (`R-25` da auditoria final, `P-0755`). Exemplo, no Marco 2 do `P-0755`: `"etapa A, custo da orquestração", que você pediu em 2026-09-28 ("faça double check dos achados, e elabore um plano de atuação")`. Sem essa linha, o dono já leu uma mensagem de marco e perguntou se lhe pediam mais uma auditoria. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o passo não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no primeiro parágrafo nem na lista do `## Relatório de encerramento`; não acrescentar linha ao repertório de mensagens (é gerado pelo gancho); não editar `.claude/tools/progresso_hook.py`.
- **Contingências:** - se a linha `### Quando a janela fecha o PLANO, e não só a janela` não existir, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando a seção `## Relatório de encerramento` inteira. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** a linha do `README.md` sobre a parada de marco (`RAF-T40`); a medida de que a próxima mensagem de marco sai sem pergunta de esclarecimento, que é da condução no Marco 6.
- **Handover:** 2026-09-30 · para quem vier depois - **Entregue:** .claude/skills/scrum-master/SKILL.md: subseção nova '### Quando a janela para num marco', antes de '### Quando a janela fecha o PLANO': a mensagem de marco abre nomeando a entrega e o pedido do dono que a originou - **Contrato:** a mensagem de marco abre com a entrega e o pedido datado do dono - **Não refazer:** nada a declarar - **Pendente:** ambiguidade da célula do marco e remissão no primeiro parágrafo do Relatório de encerramento (achado do laudo, ao consultor)

## Execução

**Consumo:** 13 tool uses, 52.7 k tokens, 139.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Entrega de redacao verbatim: o texto do card entrou identico e no ponto ancorado; o unico vermelho da bateria e a sonda nao rastreada da auditoria, pela quinta tarefa seguida, o que so o fechamento da DRF-44 encerra.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho" e vai pegar a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou".
Tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou" e vai executar: Quem executa ensina o gerente do loop a abrir a mensagem de marco nomeando a entrega e o pedido do dono que a originou.
Agente executor devolveu a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou": review — sem pendência.
Tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou" como done: registrar estado, RDO e telemetria.
