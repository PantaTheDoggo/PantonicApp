# RDO — P-0752 · FPU-T7

# Humano

Tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" concluída em 2026-09-27.
O escritor da telemetria passou a recusar a linha repetida da mesma rodada, venha ela do gancho ou do fechamento.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 16/17 tarefas concluídas; próxima: "A tabela de acionamentos ganha a coluna de causa raiz".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T7` — O escritor da telemetria recusa a linha repetida da mesma rodada
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `python .claude/tools/telemetria.py append …` sai `3` com `linha repetida: <tarefa> já tem linha com modelo, tool_uses e tokens_k iguais (data <d>)` e não escreve, quando a última linha da mesma `tarefa` na série tem `modelo`, `tool_uses` e `tokens_k` iguais aos da linha nova (DFP-8); qualquer outra diferença apensa como hoje.

**Arquivos-alvo:** - `.claude/tools/telemetria.py` — `append_row` (linha 116) e `main` (141) - `tests/test_telemetria.py` - `.claude/tools/encerrar.py:435` — `destino_rdo = _rdo.checar_close(args_precheck, "review")` (a chamada nova entra logo depois do `try` que envolve esta linha; única edição do arquivo, DFP-24) - `tests/test_encerrar.py` — um teste novo, nenhum existente muda

**Verificação:** 1. `python -m pytest tests/test_telemetria.py -q` → verde — antes `9 passed`, depois `12 passed`. 2. `python -c "from pathlib import Path;print(Path('.claude/tools/telemetria.py').read_text(encoding='utf-8').count('repetida')>=1)"` → `True` — antes `False`, depois `True`. 3. `python -m pytest tests/test_telemetria_hook.py tests/test_encerrar.py -q` → verde — antes `exit 0`, depois `exit 0` (trava: o gancho e os testes existentes do fechamento não mudam). 4. `python -m pytest tests/test_encerrar.py -q -k trio_repetido` → `1 passed` — antes `exit 5`, depois `exit 0`. 5. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** série de telemetria.linhas por rodada — uma; o escritor recusa a segunda — Verificação 1.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-27
- **Depende de:** `TK-88a`
- **Operação do modelo:** `OP-7` - OP-7: O escritor da série de telemetria recusa a segunda linha da mesma rodada, e a conferência sai de quem chama. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; série de telemetria — Quem implementa põe a recusa da duplicata no escritor, nunca em quem chama.
- **Fundamento:** DFP-8, DFP-24, F-3, `AE-26` do `P-0745`.
- **Contratos/classes:** `ultima_linha_da_tarefa(path: Path, tarefa: str) -> dict[str, str] | None` — cabeçalho = primeira linha quando ela começa por `data	`; sem ela (arquivo criado pelo próprio `append_row`), as colunas de `_COLUMNS`; `eh_repetida(ultima: dict, nova: dict) -> bool` — `modelo`, `tool_uses` e `tokens_k` iguais como texto; `checar_repetida(path: Path, row: str) -> None` — lê a `row` pelas colunas de `_COLUMNS` e lança `TelemetriaRepetidaError(ValueError)` com a mensagem do Objetivo; `append_row(path, row)` e `build_row(args)` **mantêm a assinatura** e `append_row` chama `checar_repetida` antes de ler os bytes, e assim a recusa vale para todo escritor (DFP-24); `main` traduz em exit 3 e `telemetria: FALHOU - <mensagem>` em stderr; `encerrar.fechar_tarefa`, quando `linha_telemetria is not None`, chama `_telemetria.checar_repetida(tsv, linha_telemetria)` logo depois do bloco do `checar_close` e traduz `TelemetriaRepetidaError` em `EncerramentoError(f"telemetria: {exc}")` — recusa antes da primeira escrita (padrão do `TK-88d`).
- **Passos:** 1. Implementar as duas funções e a exceção; `append_row` conserva a escrita atômica. 2. Testes: TF `test_tf_append_repetido_recusa` (duas chamadas iguais em `tmp_path` → segunda exit 3, arquivo com uma linha); TF `test_tf_append_com_tokens_diferentes_apensa` (segunda chamada com `tokens_k` diferente → duas linhas); TR `test_tr_serie_existente_nao_reescrita` (bytes anteriores idênticos após a recusa). 3. `encerrar.py`: acrescentar a chamada do Contratos entre o `try` do `checar_close` e o laço de `pendencia`/`resumo`. Teste TR `test_tr_tarefa_trio_repetido_recusa_sem_escrever` em `tests/test_encerrar.py`: `_montar_repo(tmp_path)` (a série já traz `ALF-T1` `sonnet` `21` `77.5`) e `encerrar.main(_argv_tarefa(repo, **{"--tool-uses": "21", "--tokens-k": "77.5", "--duracao-s": "999.0", "--modelo-agente": "sonnet"}))` → exit 1, `linha repetida` no stderr, `_rdos(repo) == []`, plano igual a `PLANO.format(status_t1="review")` e série igual a `TELEMETRIA`.
- **Não fazer:** não tocar `telemetria_hook.py` (ele chama o CLI com `check=False` e ignora o exit 3); em `encerrar.py`, nada além da chamada do Passo 3 (I-4 emendada pela DFP-24); não mudar a assinatura de `build_row` nem de `append_row`; não alterar teste existente de `tests/test_encerrar.py`; não reescrever, reordenar ou deduplicar linhas existentes de `docs/telemetria.tsv`.
- **Contingências:** - se algum teste existente de `tests/test_encerrar.py` ou `tests/test_telemetria_hook.py` falhar depois do Passo 3 por apensar duas vezes a mesma linha de propósito → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (medido no protótipo da DFP-24: nenhum).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** telemetria.checar_repetida (.claude/tools/telemetria.py:149) chamada por append_row e por encerrar.fechar_tarefa antes da primeira escrita; exit 3 na linha repetida - **Contrato:** a série não aceita segunda linha da mesma tarefa com modelo, tool_uses e tokens_k iguais aos da última - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-27 `ready` — consultor DFP-24: recusa em checar_repetida, append_row e build_row sem mudar assinatura; encerrar.py so ganha a chamada de checagem (I-4 emendada) - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T7-o-escritor-da-telemetria-recusa-a-linha-repetida-da-mesma-ro.md`, veredito aprovado 100%

## Execução

**Consumo:** 27 tool uses, 114.3 k tokens, 377.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Comparação 'iguais como texto' é literal por contrato: tokens_k '10' e '10.0' não se reconhecem como a mesma rodada (exercitado em série temporária); vale enquanto o gancho for o único formatador do número.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "A rodada de replanejamento `RP-1` do `P-0742`: os oito cards passam no gate do card" e vai pegar a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada".
Tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" e vai executar: `python .claude/tools/telemetria.py append …` sai `3` com `linha repetida: <tarefa> já tem linha com modelo, tool_uses e tokens_k iguais (data <d>)` e não escreve, quando a última linha da mesma `tarefa` na série tem `modelo`, `tool_uses` …
Agente executor devolveu a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada": blocked — motivo premissa: defeito=decisao: contrato manda `append_row` "recebe também os valores parseados e lança `TelemetriaRepetidaError` antes de escrever", mas I-4 e a Verificação 3 mandam "não tocar... `encerrar.py`" e "trava: os chamadores não mudam", e `.claude/tools/encerrar.py:398,410,503` chama hoje `build_row(args_tsv)` esperando `str` e `append_row(tsv, linha_telemetria)` com 2 argumentos — mudar a assinatura de `append_row`/`build_row` para caber os valores parseados exige decidir, sem o card fixar, entre (a) 3º parâmetro opcional que pula a recusa quando omitido (encerrar.py nunca recusa duplicata) ou (b) derivar `valores` da própria `row` aplicando a recusa também às escritas de `encerrar.py`, que não trata `TelemetriaRepetidaError` e propagaria a exceção depois de status/RDO já commitados (linha 502-503); nenhuma edição foi feita..
Scrum master vai marcar a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" como blocked, sem RDO.
Agente consultor recebe a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" e vai triar.
Agente consultor devolveu a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada": rota resolve.
Agente executor recebe a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" e vai executar: `python .claude/tools/telemetria.py append …` sai `3` com `linha repetida: <tarefa> já tem linha com modelo, tool_uses e tokens_k iguais (data <d>)` e não escreve, quando a última linha da mesma `tarefa` na série tem `modelo`, `tool_uses` …
Agente executor devolveu a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada": review — sem pendência.
Agente revisor recebe a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" como done: registrar estado, RDO e telemetria.
