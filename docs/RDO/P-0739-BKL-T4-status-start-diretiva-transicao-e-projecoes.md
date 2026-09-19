# RDO — P-0739 · BKL-T4

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T4` — `status`, `start`, `diretiva`: transição e projeções
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** §2.7 + escrita atômica de todas as projeções num ato (§3), com lista de arquivos tocados na saída (`DB-10`).

**Arquivos-alvo:** - `.claude/tools/backlog.py` — os verbos `status`, `start` e `diretiva` e a escrita das projeções. - `tests/test_backlog.py` — os TF/TR deste card.

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde. 2. `python -m pytest tests/test_backlog.py --collect-only -q` → a lista traz os nomes `test_tf_bloco_gerado_tem_bullet_por_pai` e `test_tf_status_recusa_pai_sem_linha_de_indice`. 3. `python -m pytest tests/ -q` → verde.

**Pronto quando:** os três comandos da `Verificação` dão o resultado descrito; na cópia da fixture no `tmp_path`, uma única chamada `status <ID> done` deixa a linha `Status` do item, a célula do índice, o par `<done>/<total>` do pai e o bloco `Fila corrente` coerentes entre si; e `status` sobre item cujo pai não tem linha no índice sai exit 3 sem alterar arquivo nenhum da cópia.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-15 · restrições, `Não fazer` e contingências autorados pela `RP-6` (2026-09-18) a partir do achado 1 do `AE-7`; `Depende de` e a forma da mensagem de E-2 emendados pela `RP-7` (2026-09-18, `DB-40`, `DB-42`).
- **Depende de:** `BKL-T3`, `BKL-T3a`, `BKL-T3b`; decisões `DB-33`, `DB-36` (forma do bullet por pai e contagem do par `<done>/<total>`, iguais às que a `BKL-T3` já implementou para `next`), `DB-37` (as condições `E-2` e `E-3` valem antes de escrever) e `DB-40` (E-2 casa o item alvo **e** o pai dele, com ID distinto uma vez e em ordem alfabética).
- **Restrições desta tarefa (copiadas inline):** - Escrita atômica, num ato só: temp + `os.replace` (`DB-1`). Transição fora da tabela de §2.7 → **exit 1** sem escrever nada; `blocked` exige `--razao`; `done` e `cancelled` são terminais; `superseded` só para plano. - Antes de qualquer escrita, `status` e `start` aplicam duas das três condições de exit 3 de §2.5 item 6 (`DB-37`), saindo **exit 3** com **nenhum arquivo tocado**: **E-2** — item alvo, ou pai dele, sem a linha `- **Status:**` → a mensagem contém `linha de status ausente para <ID>`; **E-3** — pai do item alvo sem linha no índice do diário → a mensagem contém `linha de índice ausente para <ID>`. A recusa de `start` por já haver outro item `in-progress` no mesmo pai **não** é exit 3: é recusa de transição, **exit 1**, sem escrever — o dado não é ambíguo. - Forma da mensagem de E-2 nestes dois verbos (`DB-40`, a mesma de `next`): uma ocorrência de `linha de status ausente para <ID>` por **ID distinto** sem a linha, em ordem alfabética crescente do `<ID>`, separadas por `, ` — item alvo e pai dele sem a linha produzem as duas ocorrências na mesma mensagem. A função de E-2 usada aqui é a que a `BKL-T3b` normaliza em `.claude/tools/backlog.py`: este card **reusa**, não reescreve a regra. - `--nota` apensa um sub-bullet datado `  - AAAA-MM-DD \`<estado>\` — <texto>` sob `- **Notas de execução:**` do item e **nunca** toca a célula `Status` do índice (`DB-30`). - Num ato, `status` escreve: a linha `Status` do item · o apenso da nota, se houver `--nota` · a célula do índice · o par `<done>/<total>` do pai pela fórmula da `DB-36` (`<total>` = filhos diretos com `Status` diferente de `cancelled`; `<done>` = destes, os com `Status` igual a `done`) · o bloco entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->`, com um bullet por pai vivo na forma de §2.3 (`DB-33`): token `` `P-NNNN` `` para pai plano, `` `TK-<n>` `` para pai tíquete, na ordem das linhas do índice. - As funções recebem `repo` e caminhos já resolvidos por parâmetro e nunca leem `sys.argv` (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`.
- **Testes:** TF cada transição válida escreve campo + célula + `<done>/<total>` + bloco gerado; TF `blocked` sem `--razao` recusa; TF transição inválida não escreve nada (hash antes = depois); TF `--nota` apensa sub-bullet datado e **nunca** toca a célula do índice (TR do guardrail anti-log-narrativo); TF `start` recusa com outro `in-progress` no mesmo plano; TF `diretiva` preserva o texto livre. Mais o que a `RP-5` fecha: - `test_tf_bloco_gerado_tem_bullet_por_pai` — fechar uma subtarefa do tíquete `TK-90` da fixture reescreve o bloco entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->` com um bullet `` - `TK-90` (`<estado>`, 1/2): próxima `TK-90b` `` **e** o bullet do plano vivo, nesta ordem, a das linhas do índice (`DB-33`, §2.3); e a célula do índice de `TK-90` passa a `1/2` (`DB-36`). E o que a `RP-6` fecha (`DB-37`): - `test_tf_status_recusa_pai_sem_linha_de_indice` — `status` sobre item cujo pai não tem linha no índice, na cópia de `tests/fixtures/backlog/next_tk90_sem_indice/` feita no `tmp_path` do pytest: afirma exit 3, a substring `linha de índice ausente para ` seguida do ID do pai, e que o hash de cada arquivo da cópia é o mesmo antes e depois da chamada.
- **Não fazer:** não implementar `drain` (é a `BKL-T5`) nem tocar o verbo `next` (são a `BKL-T3a` e a `BKL-T3b`); não editar os arquivos de `tests/fixtures/backlog/next_tk90/` nem de `tests/fixtures/backlog/next_tk90_sem_indice/` — o teste que escreve copia a fixture para o `tmp_path` do pytest; não rodar o instrumento contra `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do repositório real; não editar `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem `docs/RDO/*`.
- **Contingências:** - se nenhuma fixture de `tests/fixtures/backlog/` tiver um pai cujo par `<done>/<total>` mude com uma única chamada `status` → montar no `tmp_path` do pytest a cópia editada que o TF exige, sem alterar as fixtures do repositório, e devolver na linha de retorno da entrega a frase `contingência 1 acionada: cópia de fixture editada no tmp_path para o TF <nome>` (`DB-30`). - se um teste já existente de `tests/test_backlog.py` falhar por causa da escrita nova do bloco `Fila corrente` → seguir com o ajuste das asserções desse teste à forma de §2.3 e devolver na linha de retorno da entrega a frase `contingência 2 acionada: asserções de <nome do teste> ajustadas à §2.3` (`DB-30`). - se §2.3, §2.7 ou a tabela de §2.5 item 6 admitir duas leituras para o mesmo dado da fixture → parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras (`DB-19`).

## Execução

**Consumo:** 51 tool uses, 204 k tokens, 1027 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: suite acusou 1 falha em tests/test_ocupacao.py, fora dos Arquivos-alvo; era WIP da orquestracao (denominador 200k->1M), corrigida apos o retorno; arvore final 142 passed

## Laudo

**Veredito:** ressalva

**Percentual:** 85%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
