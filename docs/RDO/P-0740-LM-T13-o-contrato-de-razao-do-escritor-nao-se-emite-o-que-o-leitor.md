# RDO — P-0740 · LM-T13

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T13` — O contrato de razão do escritor: não se emite o que o leitor não relê
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — fechar a assimetria medida entre o **leitor** e o **escritor** de `razão` em `.claude/tools/backlog.py`. A `LM-T4c` deu ao leitor a fronteira estrita (`([^—]+?)`: razão não contém travessão) e a Restrição dela congelou o escritor, que segue interpolando `--razao` verbatim. O resultado é uma borda **não round-trippável**, medida ponta a ponta no `ESC-30` sobre cópia da fixture `verde`: `status ALF-T1 blocked --razao 'premissa — suja'` sai **exit 0** e grava `· premissa — suja — cauda viva`; a releitura do mesmo arquivo devolve `razao='premissa'` e `cauda='suja — cauda viva'` — o texto do operador migra de campo **em silêncio**.

**Arquivos-alvo:** - `.claude/tools/backlog.py` — a checagem nova em `transacionar_status`. - `tests/test_backlog.py` — os dois TF. - `CHANGELOG.md` — a linha do bloco não lançado.

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog.py -Pattern 'travessão' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1**: a checagem nova nomeia o caractere. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'test_tf_razao_com_travessao_recusada' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path tests/test_backlog.py -Pattern 'test_tf_razao_legitima_faz_round_trip' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog.py -Pattern '([^—]+?)' -SimpleMatch | Measure-Object).Count" ``` → **1**, **inalterado**: o leitor **não** é tocado por esta tarefa — quem muda é o escritor. **Medido antes: 1**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'o escritor de razão para de emitir o que o leitor não relê' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 6. ``` python -m pytest tests/test_backlog.py -q ``` → verde, com **dois testes a mais** que o total re-medido no despacho (`DM-23`). **Medido antes: exit 0** — veredito invariante (critério (xviii)); referência **datada**, e não aceite: `47 passed` em 2026-09-19. 7. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho. **Medido antes: exit 0** — veredito invariante; referência **datada**: `197 passed` em 2026-09-19.

**Pronto quando:** `--razao` com travessão sai **exit 1** sem tocar arquivo nenhum, a razão legítima faz round-trip com a cauda preservada, os dois TF existem, o leitor está intacto, a linha do `CHANGELOG.md` existe e as **sete** linhas de `Verificação` saem nos valores declarados.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-30` (2026-09-19), pendência do laudo da `LM-T4c` roteada pelo `B1`. Não depende de nada e nada depende dela.
- **Esforço:** low
- **Depende de:** nada.
- **Produto do módulo:** - **(a) A rota decidida é VALIDAR, não normalizar nem tolerar** (decisão do consultor, `ESC-30`). Normalizar mutaria em silêncio o texto que o operador escreveu — é a classe que o `TK-55` acumula. Tolerar deixaria uma borda lossy medida no instrumento que o próprio loop usa para materializar `A3a`, `A3b` e `A3c`. Validar é fail-closed, custa uma linha e devolve o erro a quem pode corrigi-lo. O campo `razão` é **motivo** (`dependencia`, `premissa`, `ferramenta`); prosa livre é matéria da **cauda** e da nota, que continuam aceitando travessão. - **(b) A checagem, em `transacionar_status`**, ao lado da que já recusa `blocked` sem `--razao` e **antes** de qualquer escrita (a função já declara que nenhum arquivo é tocado antes de todas as checagens passarem): `razao` contendo o caractere travessão (`—`, U+2014) devolve `ResultadoStatus(1, ...)` com mensagem que **nomeia o caractere e o motivo** — a fronteira do leitor —, contendo o literal `travessão`. Nenhuma outra transição muda de comportamento. - **(c) Os dois TF em `tests/test_backlog.py`**, sobre cópia da fixture `verde` em `tmp_path`, nunca contra o repositório: `test_tf_razao_com_travessao_recusada` (exit 1, mensagem citando o literal, e **árvore intacta** pela comparação de hashes que o arquivo já usa) e `test_tf_razao_legitima_faz_round_trip` (razão sem travessão escrita e **relida igual**, com a cauda preservada ao lado). - **(d) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal `o escritor de razão para de emitir o que o leitor não relê`.
- **Restrições desta tarefa:** o **leitor** não muda — `STATUS_BULLET_RE` fica literal, e é isso que a `Verificação` 4 tranca. A cauda e a nota continuam aceitando travessão: o contrato novo é só do campo `razão`. Nenhum outro verbo do instrumento ganha validação nesta tarefa. Nenhum card do plano é reescrito. `docs/plans/P-0739-backlog-instrumento.md` não é tocado (plano estacionado).
- **Não fazer:** não normalizar, substituir nem escapar o travessão — a rota decidida é recusar; não estender a recusa a outros caracteres (`·` round-trippa, medido no `ESC-30`); não tocar `card_check.py` nem `check-readme.ps1`; não commitar.
- **Contingências:** 1. se a recusa nova fizer qualquer teste existente ficar vermelho → **parar** e sinalizar `blocked` razão `premissa`, citando o teste: haveria um chamador legítimo emitindo travessão em `razão`, e isso muda a rota decidida neste card; 2. se `transacionar_status` já recusar travessão no despacho → parar e sinalizar `blocked` razão `premissa`: alguém fechou a borda antes, e o card ficou sem objeto.

## Execução

**Consumo:** 23 tool uses, 67.3 k tokens, 137.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Decisao de planejamento pendente no P-0740: a diretiva de commitar so no marco torna o recorte --desde do review_evidence.py nao discriminante por tarefa dentro do arquivo-alvo, e a revisao das tarefas restantes (a comecar pela LM-T14) segue dependendo de injecao manual de contexto que a RUBRICA_DE_REVISAO.md secao 3 (AE-13) declara dispensavel.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

1) A prova que decidiu a tarefa foi mutacional, nao de leitura: rodar a recusa pela CLI sobre copia da fixture verde e comparar os hashes antes/depois mostrou a arvore byte a byte intacta - o diff sozinho so mostra que o return vem antes da escrita, nao que nenhum caminho anterior ja tocou arquivo. 2) O risco vivo do card era sobre-recusa, e so o exercicio ponta a ponta o fecha: hifen, en-dash U+2013 e middot U+00B7 continuam passando com round-trip exato (razao relida igual, cauda preservada ao lado), e travessao em cauda e em --nota segue aceito - a recusa parou exatamente no U+2014 que o ESC-30 decidiu. 3) O piso do modulo fecha com a relacao do card sem nenhuma constante: 41 na autoria -> 45 com o AE-47 -> 47 com a LM-T4c -> 49 agora, isto e 47 mais os dois TF nomeados; suite total 197 -> 201, sem reducao. 4) Os dois TF novos sao os unicos testes do arquivo sem docstring, quebrando a convencao vizinha de nomear o caso medido e o concorrente - nao e defeito de aceite, mas custa ao proximo leitor do modulo.

## Fechamento

**Desdobramento:** aprovado
