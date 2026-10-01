# RDO — P-0755 · RAF-T16

# Humano

Tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados" concluída em 2026-09-29.
O planejador passa a medir o antes do card dependente numa cópia com os cards anteriores já aplicados.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 27/51 tarefas concluídas; próxima: "O planejador discrimina o card que deixa o alvo igual pela invariância".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T16` — O planejador mede o antes do card dependente na cópia com os anteriores aplicados
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o planejador a medir o antes do card que depende de outro na cópia de ensaio com os anteriores aplicados, declarando em que árvore mediu.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('arvore=%d'%t.count('só o primeiro card de cada cadeia'))"` → `arvore=1` — antes `arvore=0`, depois `arvore=1`

**Pronto quando:** - planejador.árvore em que se mede o antes — ele mede na cópia de ensaio com os anteriores aplicados, só o primeiro de cada cadeia mede na árvore real, e o valor publicado diz em que árvore foi medido — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-27`; relatório `R-26` (auditoria reg. 13).
- **Depende de:** `RAF-T15`
- **Operação do modelo:** `OP-16` - OP-16: Quem executa ensina o planejador a medir o antes do card que depende de outro na cópia de ensaio com os anteriores aplicados, declarando em que árvore mediu. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; medida gravada do card — Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, Fase 5; nenhum código muda. O comportamento que a regra usa já existe: `card_check --root <árvore>` roda os comandos do card na árvore dada, e `--gravar` grava a medida na pasta do plano dessa árvore, com o mundo no nome (`RAF-T15`). A regra mora só na Fase 5 do planejador; nenhum outro arquivo a repete.
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, na `### Fase 5 — Registro e parada`, logo depois da linha `instrução explícita do dono.` (a última do parágrafo da Fase 5) e da linha vazia que a segue, e antes da linha que começa por `## Anatomia do card`, inserir o bloco abaixo seguido de uma linha vazia (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0). ```text **Árvore do `antes`** (`R-26` da auditoria final, `P-0755`): o `card_check --mundo antes` que condiciona o registro roda, para o card cujo `antes` depende de um antecessor, na cópia do ensaio com os antecessores aplicados (`card_check --root <cópia>`); só o primeiro card de cada cadeia mede o `antes` contra a árvore real. O valor publicado nomeia a árvore em que foi medido: `real` ou `cópia com <IDs> aplicados`. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no parágrafo existente da Fase 5 (a checagem de versão é da `RAF-T38`); não mexer no item 14 da Fase 4 (é da `RAF-T17` e da `RAF-T18`); não mexer na tabela de profundidade da Fase 4 (é da `RAF-T36`).
- **Contingências:** - se a linha `instrução explícita do dono.` seguida de linha vazia e da linha que começa por `## Anatomia do card` não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as dez linhas que antecedem `## Anatomia do card`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** a linha de invariância do card que deixa o alvo igual (`RAF-T17`); a medida gravada na rodada de replanejamento (`RAF-T18`).
- **Handover:** 2026-09-29 · para `RAF-T17` - **Entregue:** .claude/agents/pantonic-planner.md Fase 5: o antes do card dependente se mede na cópia com os cards anteriores aplicados (R-26) - **Contrato:** o planejador não mede o antes de card dependente na árvore crua - **Não refazer:** o trecho da Fase 5 - **Pendente:** nenhum

## Execução

**Consumo:** 9 tool uses, 49.8 k tokens, 142.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome" e vai pegar a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados".
Tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados" e vai executar: Quem executa ensina o planejador a medir o antes do card que depende de outro na cópia de ensaio com os anteriores aplicados, declarando em que árvore mediu.
Agente executor devolveu a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados": review — sem pendência.
Tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados" como done: registrar estado, RDO e telemetria.
