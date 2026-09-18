# RDO — P-0739 · BKL-T3b

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T3b` — E-2 sobre o pai do candidato e o prefixo `- ` do contador de memória
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `.claude/tools/backlog.py`, a condição E-2 de `next` passa a recusar também o **pai** de candidato sem a linha `- **Status:**`, e o contador `fila de memória:` deixa de contar a régua markdown `---` — com um TF discriminante por defeito.

**Arquivos-alvo:** - `.claude/tools/backlog.py` — a função do verbo `next` que decide exit 3 e a função que conta o inbox de memória para o rodapé. - `tests/test_backlog.py` — os dois TF deste card.

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde. 2. `python -m pytest tests/test_backlog.py --collect-only -q` → a lista traz os nomes `test_tf_exit_3_pai_de_candidato_sem_linha_de_status` e `test_tf_contador_de_memoria_ignora_regua_e_marcadas`. 3. `python -m pytest --collect-only -q` → não menos de 130 testes coletados (piso medido em 2026-09-18, no fechamento da `BKL-T3a`: suíte `130 passed`, `tests/test_backlog.py` em 24). 4. `python -m pytest tests/ -q` → verde.

**Pronto quando:** os quatro comandos da `Verificação` dão o resultado descrito; na cópia da fixture no `tmp_path` sem a linha `- **Status:**` do tíquete `TK-90`, a seleção sai exit 3 com a substring `linha de status ausente para TK-90` aparecendo **uma única vez** na mensagem; e a saída de `next` sobre `tests/fixtures/backlog/next_tk90/` com o inbox de memória deste card contém `fila de memória: 2 candidato(s)`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `review` · entregue em 2026-09-18 (`pantonic-executor`), nenhuma contingência acionada · autorado pela `RP-7` a partir dos achados 1 e 2 do `AE-8` (`DB-40`, `DB-41`, `DB-42`); nenhuma entrega fechada reaberta (`DB-23`).
- **Depende de:** `BKL-T3a` (`done`, entregou as substrings de E-1/E-2 e os dois contadores do rodapé); decisões `DB-1`, `DB-5`, `DB-6`, `DB-37`, `DB-38`, `DB-40`, `DB-41`, `DB-42`; §2.5 item 6 (residência única das condições de exit 3) e o rodapé de §2.6.
- **Restrições desta tarefa (copiadas inline de §2.5 item 6 e do rodapé de §2.6):** - `next` segue somente-leitura: nenhuma função deste card escreve em arquivo do repositório (`DB-5`). Escrita é verbo da `BKL-T4`. - **E-2, forma completa** (`DB-37`, `DB-40`): a condição casa **item candidato ou pai de candidato** sem a linha `- **Status:**`; a mensagem traz uma ocorrência de `linha de status ausente para <ID>` por **ID distinto**, em ordem alfabética crescente do `<ID>`, separadas por `, `. Pai com dois filhos candidatos aparece **uma vez** na mensagem. - E-2 é avaliada **antes** de E-1 e de E-3, como já está entregue. O conjunto sobre o qual ela corre é a união do **item de cada candidato** com o **pai de cada candidato**; pai sem a linha nunca é tratado como pai `ready` (`DB-2`, `DB-3`). - As outras duas condições ficam como estão entregues e este card não as altera: **E-1** — dois ou mais itens candidatos com `Status` `in-progress`, mensagem com `dois ou mais itens in-progress: ` seguida dos IDs em ordem alfabética crescente, separados por `, `; **E-3** — pai de candidato elegível sem linha no índice do diário, mensagem com `linha de índice ausente para <ID>`. Nenhuma outra condição sai exit 3 em `next`. - Fronteira contra o instrumento vizinho (`DB-40`): a **ausência** da linha `- **Status:**` é violação `C-2` (tarefa, tíquete, subtarefa) ou `C-8` (plano vivo) do verbo `check`; em `next` ela é E-2, que recusa a seleção e **não** classifica a violação. Este card não toca o `check`. - Contador de fila de memória (`DB-41`): conta a linha cujo texto, depois de `strip()`, **começa com `- `** — hífen **e** espaço — e não traz `[promovido]` nem `[descartado`. Nenhuma outra exclusão entra no contador. O contador irmão `_contar_inbox_planos` (gramática de §2.4) não é tocado. - As funções recebem `repo` e os caminhos já resolvidos por parâmetro e nunca leem `sys.argv` (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`.
- **Passos:** 1. Em `.claude/tools/backlog.py`, na função `selecionar_next`, substituir a lista `sem_status` — hoje formada só pelos candidatos cujo `item.status` é `None` — por uma lista de **IDs distintos**, formada pelo `item.id` de cada candidato com `item.status is None` e pelo `pai.id` de cada candidato com `pai.status is None`, ordenada alfabeticamente por `sorted`, mantendo o bloco na posição em que já está (antes da contagem de `in-progress`). 2. No mesmo bloco, montar a mensagem juntando `linha de status ausente para <ID>` por ID dessa lista, separados por `, `, e devolver `SelecaoNext(3, None, <mensagem>)`. 3. Na função `_contar_inbox_memoria`, trocar o teste de prefixo `s.startswith("-")` por `s.startswith("- ")`, sem acrescentar nenhum outro filtro à função. 4. Em `tests/test_backlog.py`, acrescentar os dois TF da seção `Testes` abaixo. 5. Rodar os quatro comandos da seção `Verificação`, nesta ordem. pytest): ```markdown # Inbox de memória (fixture) - 2026-01-01 — a — feedback — candidato 1 — **origem:** x - 2026-01-02 — b — feedback — candidato 2 — **origem:** y [promovido] --- - 2026-01-03 — c — feedback — candidato 3 — **origem:** z ``` Pela gramática de `GOVERNANCA_MEMORIAS.md` §8 (prefixo `- `, hífen e espaço) o arquivo tem **2** candidatos; pela leitura sem o espaço (`-`) teria **3**, porque a régua `---` entraria — é essa diferença que dá poder discriminante ao TF (`DB-41`).
- **Testes:** - `test_tf_exit_3_pai_de_candidato_sem_linha_de_status` — copia `tests/fixtures/backlog/next_tk90/` para o `tmp_path` do pytest (o helper de cópia de fixture já usado nos testes deste arquivo) e, **na cópia**: (a) apaga de `docs/DIARIO_DE_OBRAS.md` a linha `- **Status:** \`ready\` · 2026-01-01` que vem logo abaixo do cabeçalho `## TK-90 — Relatório diário sai com data trocada`; (b) substitui em `docs/plans/P-0090-fifo.md` a linha `**Status:** \`ready\` · **Prefixo das tarefas no diário:** \`FFO-T<n>\`` pela linha `**Prefixo das tarefas no diário:** \`FFO-T<n>\``. Carrega o modelo da cópia, roda a seleção e afirma, sobre o resultado: `exit_code == 3`; `mensagem.count("linha de status ausente para TK-90") == 1`; `"linha de status ausente para P-0090" in mensagem`; e `mensagem.index("P-0090") < mensagem.index("TK-90")`. **Poder discriminante:** com a E-2 como entregue hoje (só o item), essa mesma cópia **não** sai exit 3 — os candidatos dos dois pais caem no filtro de elegibilidade `pai.status in ("ready", "in-progress")` e a seleção devolve exit 2 (`nada delegável`), sem nomear conserto nenhum; e, quando só o tíquete perde a linha, devolve exit 0 elegindo `FFO-T2`, que é o desvio medido na revisão da `BKL-T3a` (`AE-8`). - `test_tf_contador_de_memoria_ignora_regua_e_marcadas` — escreve no `tmp_path` do pytest um arquivo `_INBOX.md` com o texto literal da seção `Texto novo, literal`, roda a seleção sobre a fixture `tests/fixtures/backlog/next_tk90/` intacta (exit 0) e renderiza a saída de `next` passando esse arquivo como inbox de memória; afirma que a saída contém a substring `fila de memória: 2 candidato(s)` e **não** contém `fila de memória: 3 candidato(s)`. **Poder discriminante:** o valor 3 é exatamente o que a leitura sem o espaço no prefixo imprime sobre o mesmo corpus.
- **Não fazer:** não tocar `_contar_inbox_planos` nem a fixture `tests/fixtures/backlog/inbox_planos/_INBOX.md`; não acrescentar ao contador de memória filtro de indentação, de data ou de campo `**origem:**`; não criar condição de exit 3 em `next` além de E-1, E-2 e E-3; não alterar as mensagens de E-1 e E-3; não implementar `status`, `start`, `drain` nem `diretiva` (são `BKL-T4` e `BKL-T5`); não editar os arquivos de `tests/fixtures/backlog/next_tk90/` nem de `tests/fixtures/backlog/next_tk90_sem_indice/` — o teste que precisa de dado diferente copia a fixture para o `tmp_path` do pytest; não mexer no verbo `check` nem nos códigos `C-1..C-9`; não rodar o instrumento contra `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do repositório real; não editar `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem `docs/RDO/*`.
- **Contingências:** - se a linha a apagar abaixo de `## TK-90` ou a linha de cabeçalho de `docs/plans/P-0090-fifo.md` não tiver o texto literal transcrito no TF → aplicar a edição à linha que **começa** com `- **Status:**` logo abaixo do cabeçalho `## TK-90` e à linha do cabeçalho do plano que **contém** `**Status:**`, preservando o resto dessa linha, e devolver na linha de retorno da entrega a frase `contingência 1 acionada: linha de Status da fixture localizada por prefixo, não por literal` (`DB-30`). - se `tests/test_backlog.py` já tiver um teste com um dos dois nomes acima → acrescentar as asserções deste card ao corpo do teste existente, sem criar outro, e devolver na linha de retorno da entrega a frase `contingência 2 acionada: asserções acrescentadas a <nome do teste>` (`DB-30`). - se um teste já existente de `tests/test_backlog.py` falhar por causa da mensagem nova de E-2 ou do contador de memória corrigido → seguir com o ajuste das asserções desse teste às Restrições deste card e devolver na linha de retorno da entrega a frase `contingência 3 acionada: asserções de <nome do teste> ajustadas às Restrições da BKL-T3b` (`DB-30`). - se a tabela de §2.5 item 6 ou o rodapé de §2.6 admitir duas leituras para o mesmo dado da fixture → parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras (`DB-19`).
- **Fora do escopo desta tarefa:** aplicar E-2 e E-3 aos verbos `status` e `start` (é a `BKL-T4`); migrar os documentos vivos (é a `BKL-T6`).

## Execução

**Consumo:** 22 tool uses, 78 k tokens, 97 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Revisao feita contra arvore de trabalho com 7 tarefas do mesmo plano ainda nao commitadas: o recorte --desde 6d7433c traz 33 arquivos tocados para uma entrega de 2, e a separacao do que e desta tarefa saiu de mtime + leitura do card, nao do dossie. Enquanto o plano acumular entregas sem commit, o custo de revisao por tarefa cresce com o numero de tarefas anteriores em aberto.

## Fechamento

**Desdobramento:** aprovado
