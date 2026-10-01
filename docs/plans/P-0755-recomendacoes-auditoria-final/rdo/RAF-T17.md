# RDO — P-0755 · RAF-T17

# Humano

Tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância" concluída em 2026-09-29.
O planejador passa a discriminar pela invariância o card que deixa o alvo igual.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 28/51 tarefas concluídas; próxima: "A rodada de replanejamento grava a medida dos dois mundos".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T17` — O planejador discrimina o card que deixa o alvo igual pela invariância
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o planejador a discriminar o card cujo alvo deve ficar igual pela prova de que nada nele mudou desde o recorte do despacho.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('igual=%d'%t.count('**Operação de estado final igual**'))"` → `igual=1` — antes `igual=0`, depois `igual=1`

**Pronto quando:** - planejador.card que deixa o alvo igual — a linha que o discrimina é a prova de que o alvo não mudou desde o recorte, declarada como invariância e medida depois da entrega — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-28`, `DRF-36`; relatório `R-27` (auditoria reg. 14 e 35).
- **Depende de:** `RAF-T14`, `RAF-T16`
- **Operação do modelo:** `OP-17` - OP-17: Quem executa ensina o planejador a discriminar o card cujo alvo deve ficar igual pela prova de que nada nele mudou desde o recorte do despacho. - precisa de: planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, Fase 4, item 14; nenhum código muda. O mecanismo que a regra usa já existe desde a `RAF-T14`: o `card_check` roda `git diff` (subcomando de leitura), troca o literal `<ref>` do comando pelo recorte que o despacho gravou para a tarefa, e a linha marcada `(invariância)` não se mede no mundo `antes` e se mede no `depois`; a forma da linha é a da `DRF-36`. A regra mora só no item 14; nenhum outro arquivo a repete.
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, na Fase 4, item 14 (o que começa por `14. **Ensaio dos cards em árvore temporária**`), logo depois da linha `   volta à autoria.` e antes da linha que começa por `   **A contingência se ensaia:**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os três espaços que sobram no começo de cada linha entram no arquivo). ```text **Operação de estado final igual** (`R-27` da auditoria final, `P-0755`): o card cujo alvo deve ficar igual — revisão sem texto novo — não tem linha que dê valores diferentes antes e depois; a linha que o discrimina é a prova de que o alvo não mudou desde o recorte do despacho, `git diff --exit-code <ref> --numstat -- <alvo>` → `exit 0`, marcada `(invariância)`: o `card_check` não a mede no mundo `antes`, mede no `depois`, e ela falha quando o alvo muda. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outra frase do item 14; não mexer no bloco `**Árvore do` da Fase 5 (`RAF-T16`); não acrescentar a regra da rodada de replanejamento (é da `RAF-T18`); não editar `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:** - se a linha `   volta à autoria.` seguida da linha que começa por `   **A contingência se ensaia:**` não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando o item 14 inteiro. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** a mecânica da invariância no `card_check` (`RAF-T14`); a medida gravada na rodada (`RAF-T18`).
- **Handover:** 2026-09-29 · para `RAF-T18` - **Entregue:** .claude/agents/pantonic-planner.md item 14: card que deixa o alvo igual se discrimina pela Verificação de invariância (R-27) - **Contrato:** o item 14 do planejador trata o card que não muda o alvo pela invariância - **Não refazer:** o trecho do item 14 - **Pendente:** nenhum

## Execução

**Consumo:** 9 tool uses, 51.9 k tokens, 149.7 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O planejador mede o antes do card dependente na cópia com os anteriores aplicados" e vai pegar a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância".
Tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância" e vai executar: Quem executa ensina o planejador a discriminar o card cujo alvo deve ficar igual pela prova de que nada nele mudou desde o recorte do despacho.
Agente executor devolveu a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância": review — sem pendência.
Tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância" como done: registrar estado, RDO e telemetria.
