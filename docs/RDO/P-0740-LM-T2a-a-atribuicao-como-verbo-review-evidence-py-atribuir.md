# RDO — P-0740 · LM-T2a

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T2a` — A atribuição como verbo: `review_evidence.py --atribuir`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — tornar **rodável** a pergunta que o `B0` da `LM-T2` faz: *este arquivo é da entrega ou é alheio?* A resposta já existe em código (`confrontar_escopo`); o que não existe é o **verbo**. Nenhuma lógica de classificação nova se escreve aqui.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** (medida no `ESC-3` para o mundo de antes — `DM-12`) 1. `python -m pytest tests/test_review_evidence.py -q` → verde. Baseline **re-medida no `ESC-4`**, depois da `LM-T3`: `28 passed`; depois desta tarefa, `32 passed` (quatro testes). 2. `python -m pytest tests/ -q` → verde, piso ≥ **156** (re-medido no `ESC-4`: `156 passed`; o piso de 153 venceu com a `LM-T3`), mais os quatro testes novos. 3. Execução real, sobre este plano: `python .claude/tools/review_evidence.py --plano docs/plans/P-0740-loop-de-modulos.md --tarefa LM-T3 --desde 428246c --atribuir` → exit **0**, com uma linha `atribuicao: .claude/tools/review_evidence.py -> alvo-do-card` e a linha de resumo. **Antes (medido):** exit **2**, `review_evidence.py: error: unrecognized arguments: --atribuir`. 4. Regressão do caminho de dossiê: o mesmo comando **sem** `--atribuir` e com `--out` continua gerando o documento e saindo exit 0 (medido hoje: exit 0 para as onze tarefas do plano).

**Pronto quando:** `--atribuir` existe, imprime os cinco baldes na forma literal acima, sai 0 mesmo com arquivo sem atribuição, não monta dossiê e acerta o **alvo-diretório**; os quatro testes existem; e as quatro linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` — despachada em 2026-09-19 pelo `scrum-master`. Era `ready` — card novo do `ESC-3` (`DM-19`).
- **Esforço:** low
- **Depende de:** `DM-19`. Nenhuma tarefa anterior. **Exclusão mútua com a `LM-T3a`** sobre `.claude/tools/review_evidence.py` (a `LM-T3` já fechou): as duas editam o arquivo em regiões diferentes — aqui o `main`/CLI, lá `coletar_estado_git` — e não podem estar abertas ao mesmo tempo; qualquer ordem serve.
- **Fatos medidos no `ESC-3` (2026-09-18):** `confrontar_escopo` (`review_evidence.py:282-333`) já devolve os cinco baldes da `DB-25`/`DB-32` (`fora_dos_alvos`, `de_outra_tarefa`, `registro_orquestracao`, `ato_do_dono`, `veredito`) e **não** devolve a lista do primeiro balde — os arquivos cobertos pelos alvos saem do laço por `continue`. As funções que alimentam a pergunta também já existem: `coletar_arquivos_tocados`, `extrair_arquivos_alvo` e `mapear_alvos_de_outras_tarefas`. `python .claude/tools/review_evidence.py … --atribuir` sai hoje **exit 2** com `review_evidence.py: error: unrecognized arguments: --atribuir`. `tests/test_review_evidence.py` está em **25 passed**; a suíte inteira, em **153**.
- **Produto do módulo:** a flag `--atribuir` no CLI de `review_evidence.py`: com ela, o script **não** monta dossiê — imprime a classificação de cada arquivo tocado desde `--desde` e sai **exit 0**, mesmo havendo arquivo sem atribuição (o verbo **informa**, quem julga é o reviewer pela rubrica). comando, não o formato): ``` atribuicao: <caminho> -> alvo-do-card atribuicao: <caminho> -> alvo-de-outra-tarefa (<ID>) atribuicao: <caminho> -> registro-da-orquestracao atribuicao: <caminho> -> ato-do-dono atribuicao: <caminho> -> sem-atribuicao atribuicao: OK - <N> arquivo(s), <M> sem atribuicao. ``` Uma linha por arquivo, na ordem de `sorted()`, e a linha de resumo por último.
- **Restrições desta tarefa (o que garante "uma pergunta, uma implementação"):** o primeiro balde (`alvo-do-card`) é obtido por **diferença de conjuntos** sobre o que `confrontar_escopo` já devolveu — nunca por uma segunda checagem de cobertura. Nenhuma função de classificação nova; nenhuma cópia de `coberto()`; nenhum `import` de `review_evidence` em outro módulo. - `TF-atribuir-classifica-nos-cinco-baldes` — com a lista de tocados e os alvos injetados como os testes do módulo já fazem, a saída traz uma linha por arquivo com o balde certo, inclusive `alvo-do-card` para o arquivo coberto. *Concorrente:* hoje não há saída nenhuma — o argumento nem é reconhecido (exit 2). - `TF-atribuir-sai-0-mesmo-com-arquivo-sem-atribuicao` — exit **0** com pelo menos um `sem-atribuicao` na saída. *Concorrente:* uma implementação que devolvesse 1 (tratando o balde como falha) faria o `B0` do loop encerrar janela por informação, que é exatamente o defeito 4 da §3. - `TR-atribuir-nao-monta-dossie` — com `--atribuir`, nenhum documento é escrito e o caminho de `--out` não é criado. *Concorrente:* implementar a flag depois da montagem do documento gravaria o dossiê como efeito colateral. - `TF-atribuir-alvo-diretorio-casa-por-prefixo` (acrescentado pelo `ESC-4`, `DM-21` (ii)(a)) — card cujo `Arquivos-alvo` declara um **diretório** e arquivo tocado **dentro** dele sai `alvo-do-card`. *Concorrente:* é este o caso em que uma segunda implementação por caminho **exato** — a reimplementação plausível que a `Restrição` proíbe — devolveria `sem-atribuicao`. É o teste que dá poder discriminante à exigência de "uma pergunta, uma implementação", que sozinha não é verificável (`DM-21` (i)).
- **Não fazer:** não mudar `confrontar_escopo` nem nenhum dos cinco baldes (quem os altera é o `P-0739`, e a seção de arquivo vermelho do dossiê é a `LM-T3`); não tocar `.claude/skills/scrum-master/SKILL.md` (é a `LM-T2`); não criar módulo novo em `.claude/tools/`; não rodar `python .claude/tools/backlog.py check` como aceite (`AE-1`); não commitar.
- **Contingências:** 1. se `confrontar_escopo` não devolver as quatro chaves citadas acima com esses nomes exatos → parar e sinalizar `blocked` razão `premissa`, citando a assinatura encontrada; 2. se `python -m pytest tests/ -q` ficar vermelho **fora** de `tests/test_review_evidence.py` → seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.

## Execução

**Consumo:** 26 tool uses, 92.5 k tokens, 238.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Correcao do contrato de falha do verbo --atribuir exige ato de planejamento (emenda ao dossie da LM-T3a ou card corretivo novo); o reviewer nao amplia escopo de card aberto.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
