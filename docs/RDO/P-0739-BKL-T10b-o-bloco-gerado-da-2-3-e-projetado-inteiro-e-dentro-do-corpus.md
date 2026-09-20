# RDO — P-0739 · BKL-T10b

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T10b` — O bloco gerado da §2.3 é projetado inteiro e dentro do corpus
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `_bloco_fila_corrente` passa a produzir o bloco da §2.3 **inteiro** — a linha `**Fila corrente:**` **mais** os bullets — e a enxergar o mesmo corpus que `check` e `next` enxergam, de modo que **todo verbo de escrita do instrumento possa correr contra o diário vivo sem destruir nem sujar o bloco**. Um ato, uma proposição.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog.py -Pattern 'if plano.id == linha_idx.id' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. É o literal da segunda cópia da regra de casamento, recortado da fonte; zerá-lo prova que a residência única do `_posicao_indice` passou a valer também aqui. 2. ``` pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'def test_tf_bloco_fila_','def test_tr_bloco_fila_' | Measure-Object).Count" ``` → **4**, um por teste do campo `Testes`. **Medido antes: 0**. O recorte casa só nome de teste que **este** card cria, e é invariante ao que outras entregas movem. 3. ``` python -m pytest tests/test_backlog.py -q -k bloco_fila ``` → **4** selecionados e **verdes**. **Medido antes: 0 selecionados** — referência datada de 2026-09-20, fora do literal: 56 testes no módulo, todos desselecionados. O par com o item 2 separa *teste escrito* de *teste que passa*. 4. ``` python -m pytest tests/ -q ``` → **verde**, com total **não menor** que o total re-medido no início deste despacho, e igual a ele **mais os quatro** testes do campo `Testes`. Referência datada de 2026-09-20, fora do literal: `tests/test_backlog.py` com 56 testes e a suíte inteira com 208.

**Pronto quando:** os quatro itens de `Verificação` dão o resultado descrito; os quatro testes do campo `Testes` exercem, cada um, **uma** das três metades e o invariante; a regeneração do bloco mora em **uma** função, chamada por `transacionar_status` e por `transacionar_diretiva`; e `docs/DIARIO_DE_OBRAS.md` real **não** foi tocado por esta tarefa.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-20 · autorado pelo `ESC-6` (`DB-48`), sobre a pendência do laudo da `BKL-T10` (`AE-27`); executa **antes** do `BKL-T10a` · despachado 2026-09-20 pelo `scrum-master` (não por `next`, cego pelo `AE-29`)
- **Esforço:** medium
- **Depende de:** `BKL-T10`. Decisões: `DB-48` (as três metades e a residência única do bloco), `DB-33` (um bullet por pai vivo, uma forma por tipo de pai), `DB-36` (fórmula do `<done>/<total>`), `DB-43` (corpus derivado do índice, e a regra de sufixo como residência única do casamento plano × linha de índice), `DB-2` (fonte única), `DB-1` (escrita atômica num ato). Fatos: §2.0, §2.3, §2.6 e §3 deste plano.
- **Passos:** 1. **Metade 1 — a linha `**Fila corrente:**` é parte do bloco gerado.** `_bloco_fila_corrente` (`.claude/tools/backlog.py:1029`) devolve hoje **só** os bullets, e o escritor substitui **tudo** entre os marcadores por esse retorno (`.claude/tools/backlog.py:1173`, `diario_linhas[ini + 1 : fim] = _bloco_fila_corrente(...)`). A função passa a devolver, como **primeiro** elemento, a linha `**Fila corrente:**` na forma fixa da §2.3 — `` `<ID>` `` — `<título>` (`<arquivo>:<l1>-<l2>`) · `fila: …` · `ready <n>` · `blocked <m>` · `in-progress <k>` —, composta com as funções que já existem (`selecionar_next`, `_residencia_plano`, `_residencia_tiquete`, `_listar_blocked`). Sem vencedor, a linha declara o motivo em vez de sumir. 2. **Metade 2 — o casamento de id de plano é o da residência única.** O laço de `_bloco_fila_corrente` casa `plano.id == linha_idx.id`, igualdade exata, e por isso **nenhum** plano jamais recebe bullet: o índice publica `P-0739-BKL` e o cabeçalho do arquivo declara `P-0739`. Passa a usar a regra de `_posicao_indice` (`.claude/tools/backlog.py:634`) — *id exato vence; na falta dele, a primeira linha cujo id seja `<id do plano>-<SUFIXO>`* —, sem reescrevê-la num segundo lugar (`DB-2`). 3. **Metade 3 — o bloco enxerga o corpus.** *Pai vivo* da §2.3 é pai **em corpus** (§2.0): plano cuja célula de índice tem núcleo terminal não produz bullet, e não entra nas contagens `ready`/`blocked`/`in-progress` da linha da metade 1. `check` e `_candidatos` ganharam esse filtro na `BKL-T10`; `_bloco_fila_corrente` **não** ganhou, e é a terceira metade da mesma divergência. Medida de 2026-09-20 em cópia, fora do literal: sem este passo, as metades 1 e 2 sozinhas emitem **15** bullets de plano, **14** deles de plano fora do corpus — cinco arquivos declarando o mesmo `P-0729`, e vários com `Status` ausente saindo como `` (`None`, 0/n) ``. Com o passo, o bloco sai com **2** bullets: `P-0739` e `TK-54`. 4. **Residência única do bloco (`DB-2`).** A regeneração do trecho entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->` vira **uma** função, chamada por `transacionar_status` e por `transacionar_diretiva`. Medido em 2026-09-20: `transacionar_diretiva` (`.claude/tools/backlog.py:1197`) **não** regenera o bloco hoje, contra a §2.3 (*"tudo entre os marcadores é reescrito a cada verbo de escrita"*) — divergência que hoje protege por acidente e amanhã diverge por desenho. Os dois marcadores continuam localizados por **igualdade exata de linha**, e o comportamento de marcador ausente ou de fechamento ausente **não muda**. 5. **Os testes.** Escrever em `tests/test_backlog.py` os três TF e o TR do campo `Testes`, todos sobre cópia de fixture em `tmp_path`.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):** - **Forma do bloco (§2.3):** primeira linha `**Fila corrente:**` na forma fixa; depois **um bullet por pai vivo**, na ordem das linhas do índice; o pai plano escreve o token `` `P-NNNN` `` e o pai tíquete escreve `` `TK-<n>` ``; pai sem filho elegível escreve `próxima —`. Tudo entre os marcadores é gerado, e humano não edita ali. - **Corpus (§2.0, `DB-43`):** a autoridade sobre a vida de um plano é a célula de estado da linha dele no índice; núcleo `done`/`superseded`/`cancelled` → fora do corpus, e o que está fora do corpus não vira bullet nem entra em contagem. - **Casamento plano × linha de índice (§2.2, `DB-43`):** residência única em `_posicao_indice`. Nenhum outro ponto do módulo reescreve essa regra — esta tarefa **remove** a segunda cópia dela, não acrescenta uma terceira. - **`<done>/<total>` (`DB-36`):** `<total>` = filhos diretos cujo `Status` não é `cancelled`; `<done>` = os que estão `done`. A fórmula **não muda** nesta tarefa. - **Escrita atômica (`DB-1`):** o verbo de escrita segue escrevendo num ato só, e segue sem tocar arquivo quando recusa (`DB-37`).
- **Não fazer:** - Não rodar `status`, `start` nem `diretiva` contra `docs/DIARIO_DE_OBRAS.md` real: os TF rodam sobre cópia de fixture em `tmp_path`. É a razão de ser desta tarefa, e vale **durante** ela. - Não editar `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md` nem a linha de diretiva. - Não mudar a §2.3, a §2.0 nem decisão nenhuma: a forma do bloco e a regra de corpus já estão fixadas, e esta tarefa faz o código alcançá-las. - Não implementar o verbo `drain` (`BKL-T10a`), o hook nem as skills (`BKL-T11`). - Não editar as seções `## 1`, `## 2` e `## 3` de `docs/plans/P-0739-backlog-instrumento.md`, nem card nenhum deste plano.
- **Contingências:** - se a composição da linha da metade 1 exigir dado que nenhuma função existente devolve → usar o que existe e declarar na linha de retorno o campo omitido, sem inventar função nova de coleta; - se um TF exigir fixture com plano cujo id se repete em dois arquivos → criá-la, porque é o caso real medido (`P-0729` em cinco arquivos) e é o que separa a metade 3 da metade 2; - se `transacionar_diretiva` não puder chamar a função única sem mudar a assinatura pública dela → manter a assinatura, extrair a regeneração para função interna e chamá-la dos dois pontos.
- **Fora do escopo desta tarefa:** o verbo `drain` — `BKL-T10a`, que executa **depois** desta; o hook, o ponto de carga e as skills — `BKL-T11`; a aferição e o `README.md` — `BKL-T12`. Fica fora também, e é ato de quem conduz o loop e não desta tarefa, a **atualização da linha de diretiva**, hoje priorizando `TK-54a`, que está `done` (`AE-28`).

## Execução

**Consumo:** 40 tool uses, 177.5 k tokens, 725.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: invariante opcional status+diretiva encadeados nao testado - passo 4 o torna redundante por construcao; reviewer concorda que basta hoje, com rota: o card BKL-T10a deve declarar que drain chama _regenerar_bloco_fila, ponto em que o teste encadeado deixa de ser redundante.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
