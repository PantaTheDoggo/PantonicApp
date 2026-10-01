# RDO — P-0754 · AUF-T9

# Humano

Tarefa "O planejador ensaia a contingência e a faz caber no card" concluída em 2026-09-28.
O planejador passa a ensaiar também o plano de contingência de cada tarefa e a declarar os arquivos que ele escreve.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 9/16 tarefas concluídas; próxima: "A rubrica cobra a contingência pela regra do planejador".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T9` — O planejador ensaia a contingência e a faz caber no card
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o planejador a tratar cada contingência do card como parte ensaiada dele, sem contrariar as restrições do card e com os arquivos que ela escreve declarados.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('A contingência não contradiz o card'),t.count('A contingência se ensaia')))"` → `[1-1]` — antes `[0-0]`, depois `[1-1]`

**Pronto quando:** - planejador.contingência do card — cada contingência é ensaiada como o resto do card, não contraria nenhuma restrição dele, e o arquivo que ela escreve aparece entre os alvos, marcado como condicional — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-8` (i) e (ii), `DAU-31`; `H-1`, `H-8` (§2.1); `F-12`.
- **Operação do modelo:** `OP-9` - OP-9: Quem executa ensina o planejador a tratar cada contingência do card como parte ensaiada dele, sem contrariar as restrições do card e com os arquivos que ela escreve declarados. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Passos:** 1. Na Fase 4, item 3 (o que começa por `3. **Léxico proibido no card**`), logo depois da linha que termina em `` (plano legado: na linha `**Status:**` do card) (2026-09-16, `RP-4`). `` e antes da linha que começa por `4. **Rastreabilidade**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo): ```text **A contingência não contradiz o card:** a ação `seguir com <X>` de uma contingência não contraria nenhuma `Restrição` do mesmo card, e todo arquivo que ela escreve entra nos `Arquivos-alvo`, no próprio bullet, seguido de `(condicional: contingência <n>)`, com `<n>` a posição do bullet em `Contingências` (2026-09-27, `AE-24` do `P-0753`). ``` 2. Na Fase 4, item 14 (o que começa por `14. **Ensaio dos cards em árvore temporária**`), logo depois da linha `   volta à autoria.` e antes da linha `### Fase 5 — Registro e parada`, inserir o bloco abaixo, mantendo a linha vazia que já separa o item 14 do cabeçalho da Fase 5 (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo): ```text **A contingência se ensaia:** cada contingência de ação `seguir com <X>` se aplica na cópia como passo do card, e as linhas de `Verificação` se re-rodam depois dela; linha cujo valor ela muda publica, na própria contingência, o valor medido com ela aplicada (2026-09-27, pendência 1 do `P-0753`). ``` 3. Rodar a Verificação.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outra frase dos itens 3 e 14; não mexer na tabela de dosagem da Fase 4 (`| 14 (ensaio em cópia) |`); não editar a Anatomia do card nem o `docs/RUBRICA_DE_REVISAO.md` (é da `AUF-T10`).
- **Contingências:** - se a linha âncora de um dos passos não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Fora do escopo desta tarefa:** o critério da rubrica (`AUF-T10`); mecanizar a regra no `card_check.py` (candidata a recomendação do relatório novo, `DAU-8`).
- **Handover:** 2026-09-28 · para `AUF-T10`, `AUF-T11` - **Entregue:** duas regras novas em .claude/agents/pantonic-planner.md: 'A contingência não contradiz o card' (Fase 4 item 3, :271) e 'A contingência se ensaia' (Fase 4 item 14, :443) - **Contrato:** a contingência não contraria Restrição do card, o arquivo que ela escreve entra nos Arquivos-alvo com '(condicional: contingência <n>)', e ela se ensaia na cópia como passo do card - **Não refazer:** as duas regras de contingência do planejador - **Pendente:** nenhum

## Execução

**Consumo:** 14 tool uses, 51.7 k tokens, 100.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "A frase final do fechamento serve a todos os comandos" e vai pegar a tarefa "O planejador ensaia a contingência e a faz caber no card".
Tarefa "O planejador ensaia a contingência e a faz caber no card". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O planejador ensaia a contingência e a faz caber no card" e vai executar: Quem executa ensina o planejador a tratar cada contingência do card como parte ensaiada dele, sem contrariar as restrições do card e com os arquivos que ela escreve declarados.
Agente executor devolveu a tarefa "O planejador ensaia a contingência e a faz caber no card": review — sem pendência.
Tarefa "O planejador ensaia a contingência e a faz caber no card": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O planejador ensaia a contingência e a faz caber no card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O planejador ensaia a contingência e a faz caber no card": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O planejador ensaia a contingência e a faz caber no card" como done: registrar estado, RDO e telemetria.
