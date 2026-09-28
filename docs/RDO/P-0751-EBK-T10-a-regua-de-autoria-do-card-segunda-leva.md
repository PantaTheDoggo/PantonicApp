# RDO — P-0751 · EBK-T10

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T10` — A régua de autoria do card, segunda leva
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a Fase 4 do `pantonic-planner` ganha o item 13 com os dez critérios de autoria que faltam; o `pantonic-consultant` passa a aplicar os itens 11 a 13 a todo card que escreve; e `GOVERNANCA.md` §3.2 limita o contrato copiado no card ao que a operação dele usa.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md` - `.claude/agents/pantonic-consultant.md` - `GOVERNANCA.md`

**Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25. 1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Régua de autoria, segunda leva').Count` — antes `0`, depois `1` 2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Literal com cabeçalho markdown entra recuado').Count` — antes `0`, depois `1` 3. `(Select-String -Path .claude/agents/pantonic-consultant.md -SimpleMatch 'itens 11 a 13 da Fase 4').Count` — antes `0`, depois `1` 4. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'O contrato copiado se limita ao que').Count` — antes `0`, depois `1` 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit `0` 6. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** as quatro contagens saem nos valores de depois e o kit segue válido e sem drift.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-72a` do diário de obras, seção `## TK-72`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-10` - OP-10: O card que acrescenta a segunda leva da régua de autoria do card sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Fundamento:** pacotes 1, 2, 3, 5, 9, 11 e 12 do `TK-72`; itens nomeados do `TK-55` (escalonamentos 3 a 6 de 2026-09-20); caso do `TK-68a` (2026-09-25).
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número, no arquivo indicado; rodar as Verificações.
- **Texto novo 2:** ~~~~ no caso que a skill `diario-de-obras` determina em "Tíquete nasce executável". Todo card que você escreve passa pelos itens 11 a 13 da Fase 4 do `pantonic-planner` (`.claude/agents/pantonic-planner.md`). ~~~~
- **Não fazer:** não renumerar nem reescrever os itens 1 a 12 da Fase 4; não tocar `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:** - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco.

## Execução

**Consumo:** 12 tool uses, 55.8 k tokens, 105.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
