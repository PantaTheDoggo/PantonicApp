# RDO — P-0739 · BKL-T3

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T3` — `next`: a seleção determinística
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** implementar §2.5 e §2.6 no verbo `next` de `.claude/tools/backlog.py`; exit 0/2/3.

**Arquivos-alvo:** - `.claude/tools/backlog.py` — o verbo `next` e as funções de seleção e de renderização. - `tests/test_backlog.py` — os TF/TR deste card. - `tests/fixtures/backlog/` — os arquivos de fixture que os TF deste card exigem.

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde, com os cinco testes novos deste card entre os coletados. 2. `python -m pytest tests/ -q` → verde.

**Pronto quando:** `python -m pytest tests/ -q` está verde; cada uma das cinco regras de §2.5 tem ao menos um teste em `tests/test_backlog.py`; e as duas formas da linha 2 de §2.6 (pai-plano e pai-tíquete) estão afirmadas literalmente por `test_tf_linha_do_pai_plano` e `test_tf_bug_antes_de_fifo`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `ready` · 2026-09-17 — reaberta pela rodada `RP-5` (`G-REPLAN`), que absorveu o `AE-6`: a linha de contexto do pai tem agora uma forma por tipo de pai (`DB-33`), com worked example para cada uma em §2.6, e as regras que o TF "bug antes de FIFO" exigia estão fechadas (`DB-34`, `DB-35`, `DB-36`). Esteve `blocked` razão `premissa` em 2026-09-17, devolvida pelo `pantonic-executor` sem nenhuma edição.
- **Depende de:** `BKL-T2`, `BKL-T2a`; decisões `DB-5`, `DB-6`, `DB-7`, `DB-33`, `DB-34`, `DB-35`, `DB-36`.
- **Restrições desta tarefa (copiadas inline):** - `next` é somente-leitura: nenhuma função deste card escreve em arquivo do repositório (`DB-5`). Escrita é verbo de `BKL-T4`. - Ambiguidade é defeito, não escolha: dois `in-progress`, item vivo sem linha `Status`, linha de índice fora da gramática e pai vivo sem linha no índice saem em **exit 3** nomeando o conserto (`DB-6`, `DB-33`) — o código nunca desempata por heurística. - Teto do dossiê: seção da tarefa verbatim até 8.000 chars / 120 linhas; além disso, truncada com ponteiro `arquivo:l1-l2` (`DB-7`). - As funções recebem `repo` e caminhos já resolvidos por parâmetro e nunca leem `sys.argv` (`DB-1`); o módulo é carregado nos testes por `importlib`, como em `tests/test_telemetria.py`. - `<done>/<total>` de qualquer pai sai da fórmula única da `DB-36`: `<total>` = filhos diretos com `Status` diferente de `cancelled`; `<done>` = destes, os com `Status` igual a `done`.
- **Não fazer:** não implementar `status`, `start`, `drain` nem `diretiva` (são `BKL-T4` e `BKL-T5`); não rodar o instrumento contra `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/` do repositório real — toda asserção é sobre a fixture; não editar `.claude/agents/`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*` nem `docs/RDO/*`.
- **Testes:** um TF por ramo — retomada de `in-progress`; diretiva restringe os candidatos; `Depende de` não `done` segura o candidato; plano `blocked` não contribui; `Ordem de execução` vence a ordem dos cabeçalhos; fila vazia → exit 2; dois `in-progress` → exit 3 com os dois IDs; rodapé lista os `blocked` e conta as linhas não marcadas de `<memory-dir>/_INBOX.md` (caminho injetado por parâmetro no teste). Mais os quatro que a `RP-5` fecha: - `test_tf_bug_antes_de_fifo` — a fixture tem um tíquete `TK-90` com `- **Tipo:** bug`, linha no índice e duas subtarefas `### TK-90a`/`### TK-90b` (`[Sonnet · classe mecanica]`, `Status` `ready`), mais uma tarefa de plano `ready` que venceria por FIFO e cujo plano-pai **não** está `in-progress`. Afirma: `next` devolve `TK-90a` (faixa (b) da §2.5 regra 4 pelo `Tipo` do tíquete-pai, `DB-35`) e a linha 2 da saída é exatamente `tíquete: TK-90 — <título> (0/2) · residência: <caminho do diário da fixture>:<l1>-<l2> · índice: <âncora>` (`DB-33`, worked example B de §2.6). - `test_tf_linha_do_pai_plano` — vencedor com plano-pai: a linha 2 começa pelo literal `plano: `, traz `P-NNNN`, o título da linha 1 do arquivo do plano, o par da `DB-36` e os campos `residência:` e `índice:` (worked example A de §2.6). - `test_tf_antecessora_omitida_no_primeiro_irmao` — vencedor que é o primeiro irmão na ordem interna do pai: a saída **não** contém a substring `antecessora:`; vencedor que não é o primeiro irmão: a linha 3 nomeia o irmão imediatamente anterior, com o estado dele, e escreve `sem notas` quando esse irmão não tem bloco `- **Notas de execução:**` (`DB-34`). - `test_tf_pai_sem_linha_de_indice_sai_exit_3` — tíquete-pai sem linha no índice da fixture → exit 3 e a mensagem contém `linha de índice ausente para TK-90` (`DB-6`, `DB-33`). - TR: `test_tr_saida_do_next_cabe_no_teto` — `len(saida) <= 8200` para o dossiê da fixture.
- **Contingências:** - se `tests/fixtures/backlog/` não existir no repositório → criar o diretório e os arquivos que os TF deste card exigem (mini-diário com índice, um plano, o tíquete `TK-90` com as duas subtarefas, inbox), nas formas de §2.1 a §2.4, e devolver na linha de retorno da entrega a frase `contingência 1 acionada: fixture de tests/fixtures/backlog/ criada neste card` (`DB-30`). - se a fixture já trouxer um tíquete com `- **Tipo:** bug` → reutilizar esse tíquete em vez de criar `TK-90`, ajustar os IDs das asserções acima ao dele e devolver na linha de retorno da entrega a frase `contingência 2 acionada: TF de bug escrito sobre o tíquete <ID> já existente` (`DB-30`). - se qualquer regra de §2.5 ou §2.6 admitir duas leituras para o mesmo dado da fixture → parar e sinalizar `blocked` razão `premissa`, citando a regra e as duas leituras (`DB-19`). - se um teste já existente de `tests/test_backlog.py` falhar por causa da renderização nova → seguir com o ajuste das asserções desse teste à forma de §2.6 e devolver na linha de retorno da entrega a frase `contingência 4 acionada: asserções de <nome do teste> ajustadas à §2.6` (`DB-30`).

## Execução

**Consumo:** 46 tool uses, 179 k tokens, 1021 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Motivo de rota=parcial (dois desvios de detalhe, ambos contidos em .claude/tools/backlog.py e reversiveis, nenhum com decision record): (1) o campo 'inbox de planos: <n> por drenar' da forma fixa de 2.6 foi computado por _contar_pendentes_inbox, que aplica a gramatica de marcacao do inbox de memoria (linha '-' sem [promovido]/[descartado]) tambem ao inbox de planos, cuja linha viva a secao 2.4 do proprio plano define de outro jeito ('comeca com - e contem docs/plans/P-NNNN-<slug>.md'; drenada = prefixo '- [drenado AAAA-MM-DD]') - a regra estava no dossie e nao foi seguida; (2) das quatro condicoes de exit 3 enumeradas em Restricoes, selecionar_next implementa tres (sem Status, dois in-progress, indice ausente) e nao tem checador para 'linha de indice fora da gramatica'. Atenuante apurado para (2): _parse_indice descarta linha que nao casa o regex, de modo que pai vivo com linha malformada cai em 'linha de indice ausente para <ID>' e sai exit 3 do mesmo jeito - o invariante da DB-6 (o codigo nunca desempata por heuristica) segue de pe, o que falha e a nomeacao do conserto. Nao rebaixado: Pronto quando esta integralmente satisfeito (13 TF/TR prescritos presentes e passando, as cinco regras de 2.5 cobertas, linha 2 pai-tiquete afirmada por igualdade literal e pai-plano campo a campo). Consumo (informacao, nunca nota): serie de telemetria BKL-T3 - 46 tool_uses / 179.3k tok / 1020s, precedida de BKL-T3-devolvida (23 tool_uses) quando o card voltou blocked razao premissa e foi reaberto pela RP-5; a segunda passada entregou 13 testes e duas fixtures novas em disco.

## Fechamento

**Desdobramento:** aprovado com ressalva
