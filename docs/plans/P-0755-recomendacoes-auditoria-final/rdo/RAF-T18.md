# RDO — P-0755 · RAF-T18

# Humano

Tarefa "A rodada de replanejamento grava a medida dos dois mundos" concluída em 2026-09-29.
A rodada de replanejamento passa a gravar a medida dos dois mundos, antes e depois.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 29/51 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T18` — A rodada de replanejamento grava a medida dos dois mundos
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o planejador a gravar, na rodada de replanejamento, a medida de antes e a de depois de cada card que ela reescreve.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('rodada=%d'%t.count('**A rodada grava a medida**'))"` → `rodada=1` — antes `rodada=0`, depois `rodada=1`

**Pronto quando:** - planejador.medida gravada na rodada — a rodada grava a medida de antes na árvore real e a de depois na cópia de ensaio, para cada card que reescreve — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-28` (a mesma seção manda a rodada gravar os dois mundos), `DRF-30`; `F-21` (nenhum texto manda a rodada gravar medida); relatório `R-05` (auditoria reg. 35, `H-16`).
- **Depende de:** `RAF-T15`, `RAF-T17`
- **Operação do modelo:** `OP-18` - OP-18: Quem executa ensina o planejador a gravar, na rodada de replanejamento, a medida de antes e a de depois de cada card que ela reescreve. - precisa de: planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; medida gravada do card — Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo.
- **Camada e fronteira:** doutrina do kit — a definição do agente planejador, `.claude/agents/pantonic-planner.md`, Fase 4, item 14, no mesmo trecho da `RAF-T17`, logo depois dele; nenhum código muda. O mecanismo que a regra usa já existe desde a `RAF-T15`: `card_check --gravar` sem caminho grava em `<raiz>/docs/plans/<pasta do plano>/evidencia/<P-id>-<ID>-medida-<mundo>.json`, a pasta vem do `--root` e o mundo vai no nome. A regra mora só no item 14; nenhum outro arquivo a repete.
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, na Fase 4, item 14, logo depois da linha `   quando o alvo muda.` (a última do bloco `**Operação de estado final igual**` da `RAF-T17`) e antes da linha que começa por `   **A contingência se ensaia:**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card, e os três espaços que sobram no começo de cada linha entram no arquivo). ```text **A rodada grava a medida** (`R-05` da auditoria final, `P-0755`): a rodada de replanejamento grava, para cada card que reescreve, a medida de antes na árvore real (`card_check --mundo antes --gravar`) e a de depois na cópia do ensaio (`card_check --root <cópia> --mundo depois --gravar`), e copia o arquivo da cópia para a `evidencia/` do plano na árvore real: `-medida-antes.json` e `-medida-depois.json` convivem. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê este arquivo. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever o bloco `**Operação de estado final igual**` (`RAF-T17`) nem outra frase do item 14; não mexer na seção `## Rodada de replanejamento` do arquivo (a regra mora no item 14, `DRF-28`); não editar `.claude/agents/pantonic-consultant.md`.
- **Contingências:** - se a linha `   quando o alvo muda.` seguida da linha que começa por `   **A contingência se ensaia:**` não existir em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `dependencia`, nomeando a `RAF-T17`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** o nome e a pasta da medida (`RAF-T15`); a rodada que escreve o card da operação nova (`RAF-T25`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/agents/pantonic-planner.md item 14: a rodada de replanejamento grava a medida dos dois mundos, antes e depois (R-05 doutrina) - **Contrato:** rodada de replanejamento deixa medida gravada de antes e de depois de cada card que ela emite - **Não refazer:** o trecho do item 14 - **Pendente:** nenhum

## Execução

**Consumo:** 10 tool uses, 51.0 k tokens, 147.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta da regra entregue, em copia temporaria fora do repositorio: card_check --root <copia> --mundo depois --gravar e --mundo antes --gravar gravaram P-0755-RAF-T18-medida-depois.json e -medida-antes.json lado a lado em <copia>/docs/plans/P-0755-.../evidencia/ (exit 0 nos dois mundos), e o mundo depois contra a arvore antes falha com divergencia rodada=1 x rodada=0 - a doutrina descreve um caminho que o instrumento da RAF-T15 executa como escrito. Nota: a copia de ensaio precisa carregar .claude/tools (card_check importa rdo.py da raiz passada em --root); a copia integral que o item 14 manda fazer ja cobre isso.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O planejador discrimina o card que deixa o alvo igual pela invariância" e vai pegar a tarefa "A rodada de replanejamento grava a medida dos dois mundos".
Tarefa "A rodada de replanejamento grava a medida dos dois mundos". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A rodada de replanejamento grava a medida dos dois mundos" e vai executar: Quem executa ensina o planejador a gravar, na rodada de replanejamento, a medida de antes e a de depois de cada card que ela reescreve.
Agente executor devolveu a tarefa "A rodada de replanejamento grava a medida dos dois mundos": review — sem pendência.
Tarefa "A rodada de replanejamento grava a medida dos dois mundos": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A rodada de replanejamento grava a medida dos dois mundos" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A rodada de replanejamento grava a medida dos dois mundos": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A rodada de replanejamento grava a medida dos dois mundos" como done: registrar estado, RDO e telemetria.
