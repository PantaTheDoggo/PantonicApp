# RDO — P-0753 · AF-T20

# Humano

Tarefa "`uow.py` sai do kit" concluída em 2026-09-27.
O instrumento obsoleto uow.py sai do kit, como o dono decidiu.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 19/21 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T20` — `uow.py` sai do kit
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa retira do kit o instrumento de unidade de trabalho, que nada cita e nenhum teste cobre.

**Arquivos-alvo:** - `.claude/tools/uow.py` - `.claude/tools/backlog.py`

**Verificação:** 1. `python -c "from pathlib import Path;print(Path('.claude/tools/uow.py').exists())"` → `False` — antes `True`, depois `False` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;print(Path('.claude/tools/backlog.py').read_text(encoding='utf-8').count('uow.py'))"` → `0` — antes `1`, depois `0` (esperado, não ensaiado) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - instrumento de unidade de trabalho.presença no kit — fora do kit — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-5`, `DAF-7`, `DAF-36`, `F-7`, `F-33`. **Espera o veredito do dono no Marco 1** (card nasce `blocked` razão `dependencia`). Opções registradas: sair do kit, recomendada e escrita neste card; ou o arquivo do executor passa a citá-lo e o exit de erro vira 1. Veredito na segunda → rodada de replanejamento, card corretivo `AF-T20a` da `OP-20`.
- **Depende de:** `AF-T10`
- **Operação do modelo:** `OP-20` - OP-20: Quem executa retira do kit o instrumento de unidade de trabalho, que nada cita e nenhum teste cobre. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; escolha do dono no primeiro marco — Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela.
- **Camada e fronteira:** instrumentos do kit em `.claude/tools/`; nenhuma configuração do harness.
- **Passos:** 1. Apagar `.claude/tools/uow.py`. 2. Na docstring de `.claude/tools/backlog.py`, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo): ```text antigo: mesmo desenho de `uow.py`/`telemetria.py` novo: mesmo desenho de `telemetria.py` ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste de `uow.py` existe; o total não muda). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0; `python .claude/checks/dead_code.py` sai 0. - Só os `Arquivos-alvo` se editam ou se apagam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não editar `.claude/settings.json` (a linha de diretório adicional das cópias de `uow` fica para o dono, `F-33`); não apagar teste nenhum; não tocar `.claude/projecoes.json`.
- **Contingências:** - se `python -m pytest -q` ou `kit_check` citar `uow` numa falha → parar e sinalizar `blocked` razão `premissa`, colando a linha.
- **Testes:** nenhum teste novo; a suíte inteira como trava.
- **Fora do escopo desta tarefa:** a linha de `.claude/settings.json` com o diretório de cópias de `uow` (configuração de quem opera a máquina; ato do dono).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** .claude/tools/uow.py apagado; docstring de .claude/tools/backlog.py:38 cita só telemetria.py - **Contrato:** uow.py não existe mais no kit; nenhum instrumento nem teste o cita - **Não refazer:** nada a declarar - **Pendente:** linha de .claude/settings.json:19 com o diretório de cópias de uow — ato do dono, fora do card

## Execução

**Consumo:** 13 tool uses, 50.2 k tokens, 196.4 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O guia de entrada descreve o kit como ele fica" e vai pegar a tarefa "`uow.py` sai do kit".
Tarefa "`uow.py` sai do kit". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "`uow.py` sai do kit" e vai executar: Quem executa retira do kit o instrumento de unidade de trabalho, que nada cita e nenhum teste cobre.
Agente executor devolveu a tarefa "`uow.py` sai do kit": review — sem pendência.
Agente revisor recebe a tarefa "`uow.py` sai do kit" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "`uow.py` sai do kit": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "`uow.py` sai do kit" como done: registrar estado, RDO e telemetria.
