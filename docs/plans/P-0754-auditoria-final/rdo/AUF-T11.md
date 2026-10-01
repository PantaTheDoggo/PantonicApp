# RDO — P-0754 · AUF-T11

# Humano

Tarefa "O teste de interrupção nomeia os três casos que passaram por ele" concluída em 2026-09-28.
O teste de interrupção do planejador passou a nomear três casos reais em que a tarefa deveria ter sido fechada antes de sair.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 11/16 tarefas concluídas; próxima: "A versão pendente do modelo reconfere a restrição que cita o estado do plano".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T11` — O teste de interrupção nomeia os três casos que passaram por ele
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa acrescenta ao teste de interrupção do planejador os três casos medidos em que o card deveria ter parado e não parou.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('Objetivo condicional contra contrato incondicional'),t.count('sem forma fixada'),t.count('argumento sem limpeza nem recusas fechadas')))"` → `[1-1-1]` — antes `[0-0-0]`, depois `[1-1-1]`

**Pronto quando:** - planejador.pontos de parada do teste de interrupção — os três casos entram no teste pelo nome, como pontos em que o card tem de ser fechado antes de sair — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-9`, `DAU-31`; `H-2`, `H-3`, `H-4` (§2.1).
- **Depende de:** `AUF-T9`
- **Operação do modelo:** `OP-11` - OP-11: Quem executa acrescenta ao teste de interrupção do planejador os três casos medidos em que o card deveria ter parado e não parou. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Passos:** 1. Na Fase 4, item 8 (o que começa por `8. **Teste de interrupção**`), logo depois da linha `   falha sua, não do executor.` e antes da linha que começa por `9. **Campo de card lido por máquina`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo): ```text Três pontos de parada medidos que o enunciado geral deixou passar, e que se conferem pelo nome em todo card: (a) **Objetivo condicional contra contrato incondicional** — o `Objetivo` diz "se" enquanto `Contratos/classes` ou `Passos` mandam fazer sempre (`AE-8` do `P-0753`); (b) **caminho sem forma fixada** — argumento ou campo de caminho sem dizer se é relativo à raiz do repositório ou absoluto (`AE-13` do `P-0753`); (c) **argumento sem limpeza nem recusas fechadas** — argumento de texto sem a normalização aplicada antes do uso (`strip()`, separador) e sem a lista fechada das entradas que ele recusa, cada uma com a mensagem (`AE-18` do `P-0753`). ``` 2. Rodar a Verificação.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever o enunciado geral do item 8; não editar outro item da Fase 4.
- **Contingências:** - se a linha âncora do passo 1 não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas do item 8.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Fora do escopo desta tarefa:** reabrir os cards `AF-T7`, `AF-T10` e `AF-T12` do `P-0753` (já `done`).
- **Handover:** 2026-09-28 · para `AUF-T12` - **Entregue:** três pontos de parada nomeados no item 8 (Teste de interrupção) da Fase 4 de .claude/agents/pantonic-planner.md:341 — Objetivo condicional contra contrato incondicional; caminho sem forma fixada; argumento sem limpeza nem recusas fechadas - **Contrato:** o teste de interrupção confere os três casos pelo nome em todo card - **Não refazer:** o bloco dos três pontos de parada - **Pendente:** nenhum

## Execução

**Consumo:** 8 tool uses, 47.7 k tokens, 96.9 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "A rubrica cobra a contingência pela regra do planejador" e vai pegar a tarefa "O teste de interrupção nomeia os três casos que passaram por ele".
Tarefa "O teste de interrupção nomeia os três casos que passaram por ele". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O teste de interrupção nomeia os três casos que passaram por ele" e vai executar: Quem executa acrescenta ao teste de interrupção do planejador os três casos medidos em que o card deveria ter parado e não parou.
Agente executor devolveu a tarefa "O teste de interrupção nomeia os três casos que passaram por ele": review — sem pendência.
Tarefa "O teste de interrupção nomeia os três casos que passaram por ele": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O teste de interrupção nomeia os três casos que passaram por ele" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O teste de interrupção nomeia os três casos que passaram por ele": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O teste de interrupção nomeia os três casos que passaram por ele" como done: registrar estado, RDO e telemetria.
