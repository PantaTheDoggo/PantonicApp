# RDO — P-0751 · EBK-T5a

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T5a` — O `kit_check` não conta o sumário do `materializar` e detalha sob o problema
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** fechar o que o objetivo da `EBK-T5` prometeu e o card dela não prescreveu, em `.claude/checks/kit_check.ps1`: 1. nos dois ramos que chamam o `materializar.py` — `materializar check` no modo `validate` e `materializar drift` no modo `check-drift` —, a linha de sumário que o `materializar.py` imprime por último quando falha (começa por `materializar: FALHOU - `) não entra na lista de problemas e não é impressa; o número do cabeçalho passa a ser o número de defeitos; 2. no modo `check-drift`, as linhas de detalhe da divergência de README saem logo abaixo do item do README, indentadas com quatro espaços e sem o marcador `- ` (`    [versionado] <linha>` e `    [regenerado] <linha>`); o número de linhas de item (`  - `) da saída é igual ao número do cabeçalho.

**Arquivos-alvo:** - `.claude/checks/kit_check.ps1` - `tests/test_kit_check.py`

**Verificação:** 1. `python -m pytest tests/test_kit_check.py -q` → `4 passed`. 2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → exit `0`. 3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0`. 4. `python -m pytest -q` → nenhuma falha; `passed` = o do despacho mais 3.

**Pronto quando:** nos dois modos, o número do cabeçalho conta defeito e é igual ao número de itens da lista, provado pelos três testes, e os dois modos seguem exit `0` na árvore.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** corretivo da `EBK-T5`, achados (1) e (2) do laudo dela (`AE-2`, `DEB-9`), escrito pelo consultor no acionamento 4.
- **Operação do modelo:** `OP-5` - OP-5: O card que faz a conferência do kit contar um defeito por vez sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Caso medido (2026-09-26, consultor, cópia de `.claude/` e `VERSION` em diretório temporário):** `-Mode check-drift` → `check-drift FALHOU (13 problema(s))` para 12 defeitos, e o 13º item é `materializar drift: materializar: FALHOU - 12 problema(s) de drift.`; com a frase extra no README do teste existente, 14 no cabeçalho e 16 itens. `-Mode validate` com uma entrada a mais em `arquivos` de um alvo de `projecoes.json`, `de` apontando `nao/existe.md` → `kit_check: FALHOU (2 problema(s))` para 1 defeito.
- **Fatos para a execução (medidos):** o `materializar.py` imprime cada problema antes do sumário e só imprime o sumário quando há ao menos um problema, então descartar a linha de sumário nunca esvazia a lista de um ramo que saiu `1`. No `check-drift`, o item do README é sempre o primeiro da lista quando há divergência (entra antes do ramo do `materializar.py`). O protótipo do consultor (descartar a linha que casa `^materializar: FALHOU - ` no laço de cada ramo; guardar o detalhe sem prefixo e imprimi-lo com quatro espaços depois do primeiro item quando há divergência) deu, na mesma cópia: `validate` → `kit_check: FALHOU (1 problema(s))` com um item; `check-drift` com README divergente → `(13 problema(s))`, 13 itens e as duas linhas de detalhe logo abaixo do item do README; e, rodado com `-KitRoot .claude` sobre a árvore, os dois modos exit `0`.
- **Não fazer:** não mudar o `materializar.py`; não mudar o que o `kit_check` considera divergência; não tocar os modos `generate` e `consumers`; não mexer na codificação do console.
- **Contingências:** - se o teste existente `test_divergencia_de_readme_conta_um_problema_e_detalha_as_duas_linhas` cair com o reparo → parar e sinalizar `blocked` razão `premissa`, colando a saída do teste.

## Execução

**Consumo:** 22 tool uses, 76.2 k tokens, 200.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
