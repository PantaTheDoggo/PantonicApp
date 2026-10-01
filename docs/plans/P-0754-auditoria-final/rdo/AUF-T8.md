# RDO — P-0754 · AUF-T8

# Humano

Tarefa "A frase final do fechamento serve a todos os comandos" concluída em 2026-09-28.
A frase final do comando de fechamento deixou de dizer 'tarefa fechado' e agora serve a todos os comandos.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 8/16 tarefas concluídas; próxima: "O planejador ensaia a contingência e a faz caber no card".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T8` — A frase final do fechamento serve a todos os comandos
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa troca a frase final do fechamento de tarefa por uma sem erro de concordância com o nome de nenhum comando.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py -q -k "conclusao_da_tarefa"` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('concluído; relatório em'),t.count('fechado; relatório em')))"` → `[1-0]` — antes `[0-1]`, depois `[1-0]`

**Pronto quando:** - fechamento de tarefa.mensagem de conclusão — a frase final diz que o comando foi concluído, correta para todos os comandos — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-16`, `DAU-27`; `H-15` (§2.1); `F-13`, `F-15`.
- **Operação do modelo:** `OP-8` - OP-8: Quem executa troca a frase final do fechamento de tarefa por uma sem erro de concordância com o nome de nenhum comando. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`; só a linha final de sucesso de `main` muda.
- **Contratos/classes:** a linha de sucesso de `main` em `.claude/tools/encerrar.py`, hoje `print(f"encerrar: OK - {args.comando} fechado; relatório em '{destino}'.")`, passa a ser, exata (as quebras são as do bloco: uma linha só; ela perde o recuo da cerca do bloco, e os quatro espaços que sobram entram no arquivo): ```python print(f"encerrar: OK - comando '{args.comando}' concluído; relatório em '{destino}'.") ```
- **Passos:** 1. Em `tests/test_encerrar.py`, no teste `test_tf_fechado_conta_como_o_indice`, trocar a asserção `assert "plano fechado" in capsys.readouterr().out` por `assert "encerrar: OK - comando 'plano' concluído;" in capsys.readouterr().out`, e, na docstring do mesmo teste, o trecho `` diz `plano fechado` `` por `` diz `comando 'plano' concluído` ``. 2. Acrescentar ao fim de `tests/test_encerrar.py` o TF da seção `Testes`, no molde de `test_tf_tarefa_fecha_num_ato_status_rdo_tres_secoes_e_achado` (`_montar_repo`, `_argv_tarefa`). 3. Trocar a linha de `Contratos/classes` em `.claude/tools/encerrar.py`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o 1 teste novo (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar as outras linhas `encerrar: OK - …` de `main` (handover, operações), a mensagem `marco:` nem o texto humano dos relatórios (`Plano "…" fechado em …`).
- **Contingências:** - se `tests/test_encerrar.py` tiver, além da asserção do passo 1, outra asserção sobre o texto `fechado; relatório` ou `<comando> fechado` → seguir trocando-a pelo texto novo, no mesmo molde do passo 1, e devolver `contingência 1 acionada: <nome do teste>`. - se um teste que já existia em `tests/test_encerrar.py` cair depois do passo 3 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_conclusao_da_tarefa_sem_erro_de_concordancia` — `encerrar.main(_argv_tarefa(repo, **{"--resumo": "A primeira coisa está entregue.", "--pendencia": "nomear a função"}))` sai 0, e o stdout contém `encerrar: OK - comando 'tarefa' concluído;` e não contém `tarefa fechado` (a regra antiga imprime `encerrar: OK - tarefa fechado;`). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o guia de entrada (`AUF-T15`), que não cita a frase.
- **Handover:** 2026-09-28 · para `AUF-T15` - **Entregue:** linha de sucesso de main em .claude/tools/encerrar.py:1293 passa a "encerrar: OK - comando '<comando>' concluído; relatório em '<destino>'."; asserção de test_tf_fechado_conta_como_o_indice atualizada e TF test_tf_conclusao_da_tarefa_sem_erro_de_concordancia no fim de tests/test_encerrar.py - **Contrato:** a frase final do fechamento serve a todos os comandos - **Não refazer:** a frase final de main - **Pendente:** nenhum

## Execução

**Consumo:** 31 tool uses, 63.8 k tokens, 168.6 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O painel mostra o título do tíquete em curso" e vai pegar a tarefa "A frase final do fechamento serve a todos os comandos".
Tarefa "A frase final do fechamento serve a todos os comandos". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A frase final do fechamento serve a todos os comandos" e vai executar: Quem executa troca a frase final do fechamento de tarefa por uma sem erro de concordância com o nome de nenhum comando.
Agente executor devolveu a tarefa "A frase final do fechamento serve a todos os comandos": review — sem pendência.
Tarefa "A frase final do fechamento serve a todos os comandos": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A frase final do fechamento serve a todos os comandos" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A frase final do fechamento serve a todos os comandos": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "A frase final do fechamento serve a todos os comandos" como done: registrar estado, RDO e telemetria.
