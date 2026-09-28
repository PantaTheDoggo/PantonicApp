# RDO — DIARIO_DE_OBRAS · TK-88d

# Humano

Tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles" concluída em 2026-09-26.
O comando de fechamento passou a perguntar ao gerador de RDO e ao backlog se pode escrever antes de mudar qualquer coisa, e a linha de plano fechado conta as tarefas como o índice.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Tíquete "O encerramento de tarefa e de plano vira um comando, com relatório em três seções e handover no card": 4/4 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-88d` — O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `rdo.py` expõe a checagem do `close` sem escrita e `backlog.py` a regra de transição de `transacionar_status` sem escrita; `encerrar.py tarefa` e `encerrar.py plano` chamam as duas antes da primeira escrita e deixam de ter cópia própria delas (destino e existência do RDO; regra de plano `done`). Toda recusa que hoje só o `rdo.py close` faz sai antes do `done`, e a janela "status `done` sem RDO" fica só para falha de E/S. A linha `FECHADO` que o `encerrar.py plano` escreve no diário conta as tarefas como o índice (`_done_total`, que tira as `cancelled` do total), e o stdout do fechamento diz `tarefa fechada` e `plano fechado` (`CT-4` do `## TK-88`).

**Arquivos-alvo:** - `.claude/tools/rdo.py` — `cmd_close` - `.claude/tools/backlog.py` — `transacionar_status` - `.claude/tools/encerrar.py` — `fechar_tarefa`, `fechar_plano`, `main` - `tests/test_rdo.py`, `tests/test_backlog.py`, `tests/test_encerrar.py`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_backlog.py -q -k "checar_close or checar_transicao or fechado_conta"` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print(t.count('tarefa já fechada'),t.count('não terminal(is)'))"` → `0 0` — antes `1 1`, depois `0 0`. 3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (piso re-medido no despacho).

**Pronto quando:** a recusa do `rdo.py` sai antes do `done` (Verificação 1), o `encerrar.py` não guarda cópia das duas regras (Verificação 2) e a linha `FECHADO` diz o que o índice diz (Verificação 1).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `TK-88b`, `TK-88c`
- **Contratos/classes:** `rdo.checar_close(args, status_exigido: str = "done") -> Path` — as checagens do `cmd_close`, sem escrita, devolvendo o destino; `cmd_close` a chama com `"done"`. `backlog.checar_transicao(modelo, id_, estado, razao=None) -> ResultadoStatus | None` — `None` quando a transição pode; `transacionar_status` a chama antes de escrever. As mensagens de recusa não mudam.
- **Testes (novos):** TR `test_tr_checar_close_recusa_antes_do_done` (`test_encerrar.py`) — uma recusa que hoje só o `rdo.py close` faz (o executor escolhe qual e a nomeia no retorno) sai do `encerrar.py tarefa` com a tarefa ainda em `review` e sem RDO; TF `test_tf_checar_transicao_sem_escrita` (`test_backlog.py`) — mesmo resultado de `transacionar_status` para plano com tarefa aberta, arquivos intactos; TF `test_tf_fechado_conta_como_o_indice` (`test_encerrar.py`) — plano com uma `done` e uma `cancelled` → linha `FECHADO` com `1/1` e stdout `plano fechado`.
- **Não fazer:** não mudar mensagem de recusa de `rdo.py` nem de `backlog.py`; não mudar a ordem das escritas do `encerrar.py` (status → RDO → telemetria → achados); não tocar `progresso_hook.py`; não reescrever a linha `FECHADO` já publicada no diário.
- **Contingências:** - se alguma checagem do `close` depender do status já `done` por outra razão que não a própria exigência de status → parar e sinalizar `blocked` razão `premissa`, nomeando a checagem.
- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** rdo.checar_close (rdo.py) e backlog.checar_transicao (backlog.py) sem escrita; encerrar.py chama as duas antes da primeira escrita e não copia mais as regras; linha FECHADO conta por _done_total - **Contrato:** recusa do rdo.py close sai do encerrar.py tarefa antes do done; FECHADO diz o que o índice diz - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88d-o-fechamento-pergunta-ao-rdo-py-e-ao-backlog-py-se-pode-escr.md`, veredito ressalva 91%

## Execução

**Consumo:** 60 tool uses, 192.8 k tokens, 1367.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos" e vai pegar a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles".
Tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles" e vai executar: `rdo.py` expõe a checagem do `close` sem escrita e `backlog.py` a regra de transição de `transacionar_status` sem escrita; `encerrar.py tarefa` e `encerrar.py plano` chamam as duas antes da primeira escrita e deixam de ter cópia própria de…
Agente executor devolveu a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles": review — sem pendência.
Agente revisor recebe a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles": ressalva 91%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles" como done: registrar estado, RDO e telemetria.
