# RDO — P-0739 · BKL-T3a

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T3a` — As três condições de exit 3 de `next` e o contador do rodapé
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `.claude/tools/backlog.py`, cada uma das três condições de exit 3 de `next` imprime a substring obrigatória de §2.5 item 6, e o campo `inbox de planos: <n> por drenar` do rodapé conta pela gramática de §2.4 — com um TF por condição sem TF e um TF discriminante para o contador.

**Arquivos-alvo:** - `.claude/tools/backlog.py` — a função do verbo `next` que decide exit 3 e a função que renderiza o rodapé de pendências mecânicas. - `tests/test_backlog.py` — os TF deste card. - `tests/fixtures/backlog/inbox_planos/_INBOX.md` (novo) — o inbox de planos com uma linha viva, uma drenada e uma sem caminho de plano.

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde. 2. `python -m pytest tests/test_backlog.py --collect-only -q` → a lista traz os nomes `test_tf_contador_do_inbox_de_planos_ignora_drenada_e_linha_sem_plano`, `test_tf_exit_3_dois_in_progress_nomeia_os_ids` e `test_tf_exit_3_item_sem_linha_de_status`. 3. `python -m pytest --collect-only -q` → não menos de 127 testes coletados (piso medido em 2026-09-18, com `tests/test_backlog.py` em 21). 4. `python -m pytest tests/ -q` → verde.

**Pronto quando:** os quatro comandos da `Verificação` dão o resultado descrito, e a saída de `next` sobre `tests/fixtures/backlog/next_tk90/` com o inbox deste card contém `inbox de planos: 1 por drenar`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `review` · entregue em 2026-09-18 pelo `pantonic-executor`, **nenhuma contingência acionada** (suíte `130 passed`, piso 127; `tests/test_backlog.py` `24`); a rodada de revisão não foi despachada na mesma janela (encerrada por `B2`, `GOVERNANCA.md` §4.3). Autorada pela `RP-6` a partir dos achados 1 e 3 do `AE-7` (`DB-39`); nenhuma entrega fechada é reaberta (`DB-23`).
- **Depende de:** `BKL-T3` (`done`, entregou o verbo `next`); decisões `DB-1`, `DB-5`, `DB-6`, `DB-37`, `DB-38`, `DB-39`; seções §2.4 (gramática do inbox de planos), §2.5 item 6 (lista única das condições de exit 3) e o rodapé de §2.6.
- **Restrições desta tarefa (copiadas inline de §2.5 item 6 e de §2.4):** - `next` segue somente-leitura: nenhuma função deste card escreve em arquivo do repositório (`DB-5`). Escrita é verbo da `BKL-T4`. - Condições de exit 3 de `next`, lista fechada de três (`DB-37`): - **E-1** — dois ou mais itens candidatos com `Status` `in-progress`: a mensagem contém `dois ou mais itens in-progress: ` seguida dos IDs, em ordem alfabética crescente, separados por `, `. - **E-2** — item candidato, ou pai de candidato, sem a linha `- **Status:**`: a mensagem contém `linha de status ausente para <ID>`, com `<ID>` sendo o item ou o pai sem a linha. - **E-3** — pai de candidato elegível sem linha no índice do diário: a mensagem contém `linha de índice ausente para <ID>`, com `<ID>` sendo o ID do pai. - Nenhuma outra condição sai exit 3 em `next`. Linha de índice que não casa a gramática de §2.2 é descartada na leitura e não existe para `next`; quando é a linha do pai de um candidato elegível, o caso cai em E-3. O lint dela é do verbo `check` (`C-4`, `C-9`) e plano vivo sem prefixo é `C-7` no `check` e exit 3 do `drain`, nunca exit 3 de `next`. - Contador do rodapé (`DB-38`): `inbox de planos: <n> por drenar` conta as linhas de `docs/plans/_INBOX.md` que começam com `- `, contêm um caminho que casa `docs/plans/P-[0-9]{4}-<slug>.md` e **não** começam com `- [drenado `; `fila de memória: <m> candidato(s)` conta as linhas do inbox de memória que começam com `- ` e não trazem `[promovido]` nem `[descartado`. São duas gramáticas, uma por arquivo: nenhuma das duas serve o outro arquivo. - As funções recebem `repo` e os dois caminhos de inbox já resolvidos por parâmetro e nunca leem `sys.argv` (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`.
- **Passos:** 1. Em `.claude/tools/backlog.py`, partir a função `_contar_pendentes_inbox` em duas — `_contar_inbox_planos(caminho)` e `_contar_inbox_memoria(caminho)` —, cada uma com a gramática da sua residência (Restrições acima), e ligar cada uma ao seu campo do rodapé: a primeira a `inbox de planos: <n> por drenar`, a segunda a `fila de memória: <m> candidato(s)`. 2. Criar `tests/fixtures/backlog/inbox_planos/_INBOX.md` com o texto literal abaixo, sem mais nenhuma linha. 3. Na função do verbo `next` que decide exit 3, escrever as mensagens de E-1 e de E-2 com as substrings obrigatórias da tabela de Restrições, mantendo a de E-3 como já está entregue. 4. Em `tests/test_backlog.py`, acrescentar os três TF da seção `Testes` abaixo. 5. Rodar os quatro comandos da seção `Verificação`, nesta ordem. ```markdown # Inbox de planos (fixture) **Próximo id de plano: P-0742.** - `docs/plans/P-0740-exemplo-vivo.md` — plano vivo, por drenar - [drenado 2026-09-18] `docs/plans/P-0741-exemplo-drenado.md` — já drenado - nota solta, sem caminho de plano ``` Pela gramática de §2.4 o arquivo tem **1** linha viva; pela gramática do inbox de memória teria **3** — é essa diferença que dá poder discriminante ao TF (`DB-38`).
- **Testes:** - `test_tf_contador_do_inbox_de_planos_ignora_drenada_e_linha_sem_plano` — roda `next` sobre a fixture `tests/fixtures/backlog/next_tk90/` com o caminho do inbox de planos apontado para `tests/fixtures/backlog/inbox_planos/_INBOX.md`; afirma que a saída contém a substring `inbox de planos: 1 por drenar` e **não** contém `inbox de planos: 3 por drenar`. - `test_tf_exit_3_dois_in_progress_nomeia_os_ids` — copia `tests/fixtures/backlog/next_tk90/` para o `tmp_path` do pytest com `shutil.copytree`, troca na cópia o token da linha `- **Status:**` de dois itens `ready` para `in-progress` e roda `next` sobre a cópia; afirma exit 3 e a substring `dois ou mais itens in-progress: ` seguida dos dois IDs em ordem alfabética crescente, separados por `, `. - `test_tf_exit_3_item_sem_linha_de_status` — copia `tests/fixtures/backlog/next_tk90/` para o `tmp_path` do pytest com `shutil.copytree`, apaga na cópia a linha `- **Status:**` do item que `next` devolve na fixture intacta e roda `next` sobre a cópia; afirma exit 3 e a substring `linha de status ausente para ` seguida do ID desse item. - E-3 já tem TF entregue pela `BKL-T3` (`test_tf_pai_sem_linha_de_indice_sai_exit_3`, fixture `tests/fixtures/backlog/next_tk90_sem_indice/`): este card **não** cria outro para ela.
- **Não fazer:** não implementar `status`, `start`, `drain` nem `diretiva` (são `BKL-T4` e `BKL-T5`); não editar os arquivos de `tests/fixtures/backlog/next_tk90/` nem de `tests/fixtures/backlog/next_tk90_sem_indice/` — o teste que precisa de dado diferente copia a fixture para o `tmp_path` do pytest; não criar condição de exit 3 em `next` além de E-1, E-2 e E-3; não mexer no verbo `check` nem nos códigos `C-1..C-9`; não rodar o instrumento contra `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do repositório real; não editar `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem `docs/RDO/*`.
- **Contingências:** - se não existir função com o nome `_contar_pendentes_inbox` em `.claude/tools/backlog.py` → seguir com a função que o verbo `next` usa hoje para produzir o campo `inbox de planos:` do rodapé, aplicando a ela o passo 1, e devolver na linha de retorno da entrega a frase `contingência 1 acionada: contador do rodapé reside em <nome real da função>` (`DB-30`). - se a função que renderiza o rodapé não receber o caminho do inbox de planos por parâmetro → acrescentar o parâmetro com valor default `repo / "docs" / "plans" / "_INBOX.md"` (`DB-1`) e devolver na linha de retorno da entrega a frase `contingência 2 acionada: parâmetro de caminho do inbox de planos acrescentado` (`DB-30`). - se `tests/test_backlog.py` já tiver um teste com um dos três nomes acima → acrescentar as asserções deste card ao corpo do teste existente, sem criar outro, e devolver na linha de retorno da entrega a frase `contingência 3 acionada: asserções acrescentadas a <nome do teste>` (`DB-30`). - se um teste já existente de `tests/test_backlog.py` falhar por causa da mensagem nova de E-1 ou de E-2 → seguir com o ajuste das asserções desse teste às substrings da tabela de Restrições e devolver na linha de retorno da entrega a frase `contingência 4 acionada: asserções de <nome do teste> ajustadas a §2.5 item 6` (`DB-30`). - se a tabela de §2.5 item 6 ou a gramática de §2.4 admitir duas leituras para o mesmo dado da fixture → parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras (`DB-19`).
- **Fora do escopo desta tarefa:** aplicar E-2 e E-3 aos verbos `status` e `start` (é a `BKL-T4`); migrar os documentos vivos (é a `BKL-T6`).

## Execução

**Consumo:** 27 tool uses, 86 k tokens, 248 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: A metade 'pai de candidato sem linha de Status' da E-2 e a gramatica do contador de fila de memoria seguem abertas em .claude/tools/backlog.py e exigem card novo do planejamento (DB-23 veda reabrir entrega fechada).

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Execucao de 27 turnos, sem contingencia: a entrega cobriu exatamente os tres TF pedidos e nada alem deles. Onde a Restricao do card tinha duas metades (E-2: item candidato OU pai de candidato) e a lista de TF cobria uma, o codigo pousou so na metade coberta — sinal de que, nesta classe de card, o poder discriminante da lista de TF, e nao a prosa da Restricao, e o que de fato dimensiona a entrega.

## Fechamento

**Desdobramento:** aprovado com ressalva
