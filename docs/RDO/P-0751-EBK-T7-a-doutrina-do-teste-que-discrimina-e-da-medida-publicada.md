# RDO — P-0751 · EBK-T7

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T7` — A doutrina do teste que discrimina e da medida publicada
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` §4.4 passa a carregar as quatro regras do teste que discrimina, e a *Disciplina de instrumento* de §3 passa de cinco para oito regras, com as três da medida publicada. A regra corrigida da `DB-53` do `P-0739` ganha residência aqui, e o plano fechado não é editado.

**Arquivos-alvo:** - `GOVERNANCA.md`

**Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25. 1. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**Teste que discrimina.**').Count` — antes `0`, depois `1` 2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'cinco regras de método').Count` — antes `1`, depois `0` 3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'efeito dentro da').Count` — antes `0`, depois `1` 4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** as três contagens saem nos valores de depois.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-55g` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-7` - OP-7: O card que publica a doutrina do teste que discrimina e da medida publicada sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as Verificações.
- **Não fazer:** não editar `docs/plans/P-0739-backlog-instrumento.md`; não tocar outro parágrafo de §4.4.
- **Contingências:** - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco.

## Execução

**Consumo:** 10 tool uses, 50.7 k tokens, 83.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
