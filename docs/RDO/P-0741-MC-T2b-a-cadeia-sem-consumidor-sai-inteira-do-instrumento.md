# RDO — P-0741 · MC-T2b

**Plano:** `docs/plans/P-0741-modelo-conceitual.md`
**Tarefa:** `MC-T2b` — A cadeia sem consumidor sai inteira do instrumento
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** nenhum símbolo de `.claude/tools/modelo.py` fica sem leitor por causa da remoção do campo `linha`, e a saída dos dois verbos continua idêntica.

**Arquivos-alvo:** - `.claude/tools/modelo.py` — a assinatura de `_extrair_oracoes` e a chamada dela

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern 'def _extrair_oracoes(secao: list[str], offset: int)' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern '_extrair_oracoes(secao, inicio)' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 3. ``` python -m pytest tests -q -p no:cacheprovider ``` → **exit 0**. **Medido antes: exit 0**. Piso: total coletado não reduz (`I-2`). 4. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md ``` → **exit 0**. **Medido antes: exit 0**. (invariância: a limpeza não quebra o corpus real.) 5. ``` pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T2b --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count" ``` → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)

**Pronto quando:** as cinco linhas acima devolvem o esperado e a linha de retorno declara a cadeia fechada (passo 2).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Fundamento:** `AE-14` e a decisão `DMC-29` do `ESC-4`. A `MC-T2a` removeu o campo `linha` e, com ele, o único leitor de `offset`; o aceite deste card é **propriedade**, não lista de posições — é isso que impede a terceira casca.
- **Depende de:** `MC-T2a`
- **Oração do modelo:** `M-17` - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`; só `modelo.py`. Nenhum arquivo de teste muda de expectativa.
- **Contratos/classes:** `_extrair_oracoes(secao: list[str]) -> tuple[list[Oracao], dict[int, str]]` — um parâmetro a menos. Nenhuma outra assinatura do módulo muda.
- **Passos:** 1. Remover o parâmetro `offset` da assinatura de `_extrair_oracoes` (`.claude/tools/modelo.py:106` em 2026-09-20) e o argumento `inicio` da chamada (`:172` em 2026-09-20). A variável `inicio` **permanece**: ela ainda recorta a seção. 2. **Fechar a cadeia:** procurar no módulo inteiro todo parâmetro, atributo ou variável que tenha ficado sem leitor por essa remoção, e removê-lo também. A busca é do executor e o resultado vai na linha de retorno como `cadeia fechada: <o que saiu>` — se nada mais saiu, `cadeia fechada: nada além de offset e inicio`. 3. Rodar a suíte inteira e o `check` sobre o corpus real.
- **Restrições desta tarefa:** nenhuma assinatura pública muda além da de `_extrair_oracoes`; a saída dos dois verbos é byte a byte a de antes; nenhum arquivo de teste muda; `backlog.py`, `review_evidence.py` e `card_check.py` intocados (`I-3`).
- **Não fazer:** não renomear nada; não reorganizar funções; não acrescentar teste para o que foi removido — o que some não se testa.
- **Contingências:** 1. se remover `offset` exigir mudar `tests/test_modelo.py` → há consumidor em teste e a premissa da `DMC-29` caiu: parar e sinalizar `blocked` razão `premissa`. 2. se o passo 2 encontrar símbolo sem leitor que **não** vem da remoção do campo `linha` → deixar como está e registrar na linha de retorno: é achado, não escopo deste card.
- **Testes:** `TR`: `tests/test_modelo.py` e a suíte inteira seguem verdes, sem redução de total (`I-2`).
- **Fora do escopo desta tarefa:** qualquer outra limpeza de `modelo.py`; README e Marco 2 (`MC-T5`).

## Execução

**Consumo:** 16 tool uses, 57.7 k tokens, 138.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: cadeia fechada: nada alem de offset e inicio

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
