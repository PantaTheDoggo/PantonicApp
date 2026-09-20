# RDO — P-0739 · BKL-T10a

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T10a` — `drain`: o inbox de planos sai do contexto
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o instrumento ganha o verbo `drain` — cada linha viva de `docs/plans/_INBOX.md` vira linha de índice do diário e sai do inbox **verbatim** para o histórico, e o contador de id é recalculado —, com os seis testes que o exercem. Um ato, uma proposição: **o inbox deixa de ser lido à mão no pickup**.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. ``` pwsh -NoProfile -Command "python .claude/tools/backlog.py drain --help *> $null; $LASTEXITCODE" ``` → **0**. **Medido antes: 2** — hoje o `argparse` recusa o subcomando. O valor é o exit code do comando, não um total de corpus: nenhuma outra entrega o desloca. 2. ``` pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'def test_tf_drain_','def test_tr_historico_do_inbox_so_cresce' | Measure-Object).Count" ``` → **6**, um por teste do campo `Testes`. **Medido antes: 0**. O recorte casa só nome de teste que **este** card cria: nenhum dos seis testes do `BKL-T10` traz `drain` no nome, e por isso o valor é invariante ao que a entrega anterior move. 3. ``` python -m pytest tests/test_backlog.py -q -k drain ``` → **5** selecionados e **verdes** — os cinco `test_tf_drain_*`. O TR `test_tr_historico_do_inbox_so_cresce` **não casa `-k drain`**, porque o nome dele não contém o literal; é exatamente por isso que o item 2 usa **dois** padrões separados, e os dois itens medem coisas diferentes de propósito: o 2 conta **seis** testes escritos, o 3 conta **cinco** testes de `drain` que passam. **Medido antes: 0 selecionados** — referência datada de 2026-09-19, fora do literal: 49 testes no módulo, todos desselecionados. O par com o item 2 separa *teste escrito* de *teste que passa*. (Número corrigido de **6** para **5** em 2026-09-20 pelo `scrum-master`, `AE-30`: contradição interna ao card, não defeito de execução — o bloco `Testes` é a especificação e a `Verificação` mede o que ela prescreve.) 4. ``` python -m pytest tests/ -q ``` → **verde**, com total **não menor** que o total re-medido no início deste despacho, e igual a ele **mais os seis** testes do campo `Testes`. Referência datada de 2026-09-19, antes do `BKL-T10`, fora do literal: `tests/test_backlog.py` com 49 testes e a suíte inteira com 201.

**Pronto quando:** os quatro itens de `Verificação` dão o resultado descrito — item 3 em **5**, item 2 em **6**, e a diferença é o TR, por desenho; o verbo `drain` existe no `main` e é coberto pelos cinco TF e pelo TR; `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md` e `docs/DIARIO_DE_OBRAS.md` reais continuam **intocados**; e nenhum arquivo fora dos dois `Arquivos-alvo` foi modificado por esta tarefa.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-20
- **Esforço:** medium
- **Depende de:** `BKL-T10b`. Decisões: `DB-44` (esta partição), `DB-48` (o bloco gerado é projetado inteiro — o `drain` escreve no diário e herda o bloco reparado), `DB-38` (gramática de linha viva do inbox de planos), `DB-9` (o histórico só recebe apenso e nunca é lido), `DB-1` (escrita atômica, funções recebem caminhos resolvidos), `DB-37` (exit 3 não toca arquivo nenhum). Fatos: §2.2 (forma da linha de índice e da célula de estado), §2.4 e §3 deste plano.
- **Passos:** 1. Acrescentar o subcomando `drain [--data AAAA-MM-DD]` ao `main` (`.claude/tools/backlog.py:1168`), ao lado de `check`, `show`, `next`, `status`, `start` e `diretiva`. 2. Implementar `drain`: cada linha viva de `docs/plans/_INBOX.md` vira uma linha de índice do diário — estado lido do campo `**Status:**` do cabeçalho do plano, título da linha 1 do plano, âncora igual ao caminho do arquivo — e a linha do inbox é movida **verbatim**, prefixada de `- [drenado AAAA-MM-DD] `, para `docs/plans/_INBOX_HISTORICO.md`. 3. Recalcular o contador `**Próximo id de plano: P-NNNN.**` do inbox como `max(id visto) + 1`. 4. Sair **exit 3**, nomeando o arquivo e sem tocar arquivo nenhum, quando um plano referido por linha viva não tem `**Prefixo das tarefas no diário:**` ou não tem `**Status:**`; inbox sem linha viva é no-op com **exit 0**. 5. Escrever em `tests/test_backlog.py` os cinco TF e o TR do campo `Testes`, todos sobre cópia de fixture em `tmp_path`.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):** - **Linha viva do inbox de planos (`DB-38`):** começa com `- `, contém um caminho que casa `docs/plans/P-[0-9]{4}-<slug>.md` e **não** começa com `- [drenado `. A gramática de marcação do inbox de memória (`- ` sem `[promovido]` e sem `[descartado`) vale só para o inbox de memória e **nunca** se aplica a este arquivo. - **Histórico (`DB-9`):** `docs/plans/_INBOX_HISTORICO.md` só recebe apenso e **nunca é lido** pelo instrumento — nem para calcular o contador, nem para decidir se uma linha já foi drenada. - **Marca de drenada:** o prefixo é `- [drenado AAAA-MM-DD] ` e a linha drenada **nunca** é viva, mesmo trazendo o caminho de um plano. - **Célula de estado que `drain` escreve (§2.2):** só o token do vocabulário, opcionalmente seguido de `<done>/<total>`. O plano recém-drenado ainda não tem linha de índice, e por isso o campo `**Status:**` do cabeçalho dele é a única fonte possível do token — é o caso de *bootstrap*, e ele **não** contradiz a `DB-43`: a regra "o índice é a autoridade" pressupõe que exista linha de índice, e é esta que a cria. - **Escrita atômica (`DB-1`) e exit 3 sem escrita (`DB-37`):** `drain` escreve num ato só; quando recusa, não toca arquivo nenhum. - **Corpus (`DB-43`):** esta tarefa **não** mexe em corpus, em `check`, em `next`, em `_candidatos` nem em `_parse_indice` — o `BKL-T10` já os entregou, e eles são a base sobre a qual esta roda.
- **Não fazer:** - Não rodar `drain` contra o `docs/plans/_INBOX.md` real, nem contra o `docs/DIARIO_DE_OBRAS.md` real: os TF do verbo rodam sobre cópia de fixture em `tmp_path`. Medida de 2026-09-19, fora do literal: o inbox real tem **0** linhas vivas, de modo que o verbo seria inerte contra a árvore — o que **não** autoriza rodá-lo, porque a próxima linha apensada muda isso sem aviso. - Não editar `docs/DIARIO_DE_OBRAS.md`, nem `docs/plans/_INBOX.md`, nem `docs/plans/_INBOX_HISTORICO.md`, nem `docs/DIARIO_HISTORICO.md`. - Não reabrir nada do corpus (`BKL-T10`), do hook e das skills (`BKL-T11`) ou da aferição (`BKL-T12`). - Não editar as seções `## 1`, `## 2` e `## 3` de `docs/plans/P-0739-backlog-instrumento.md`, nem card nenhum deste plano.
- **Contingências:** - se o `BKL-T10` não tiver entregue a âncora de índice da §2.2 — `check` ainda lintando plano terminal — parar e sinalizar `blocked` razão `dependencia`, citando o `BKL-T10`; - se a fixture de inbox exigida por um TF não existir em `tests/fixtures/backlog/`, criá-la dentro da própria fixture do teste, em `tmp_path`, e seguir: fixture de teste é parte do teste, não entregável novo; - se `docs/plans/_INBOX.md` real tiver ganhado linha viva entre o despacho e a entrega, **não** drenar: registrar na linha de retorno e seguir, porque drenar a árvore real está fora do escopo deste card.
- **Fora do escopo desta tarefa:** o corpus do instrumento e a migração do diário — `BKL-T10`, entregue antes desta; o hook e as skills — `BKL-T11`; a aferição do pickup e o `README.md` — `BKL-T12`.

## Execução

**Consumo:** 21 tool uses, 103.9 k tokens, 204.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: contingencia 3 acionada: _INBOX.md real ganhou 1 linha viva (P-0741) entre o despacho e a entrega - drain real nao executado, verbo exercitado so sobre copia tmp_path; arvore identica ao estado pre-tarefa fora dos dois arquivos-alvo.
laudo: Quem roda o drain contra a arvore real: nenhum card do P-0739 possui o ato, e o inbox segue com a linha viva P-0741 (sessao paralela do dono) - o reviewer classifica como ato de orquestracao do scrum-master no fechamento do plano, mas o efeito de admitir P-0741 ao corpus vivo e composicao de backlog e pede decisao do planejamento.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
