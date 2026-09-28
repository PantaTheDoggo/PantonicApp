# RDO — P-0751 · EBK-T11

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T11` — O planejador publica o grep da superfície e ensaia os cards antes de gravar
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o `pantonic-planner` passa a ter dois usos para o `Bash` — o comando de aceite e o grep de verificação de superfície, publicado com padrão e contagem —, e a Fase 4 ganha o item 14, o ensaio dos cards numa cópia da árvore.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25 (itens 1 e 2) e depois do `EBK-T10` (item 3). 1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'serve a **dois** usos').Count` — antes `0`, depois `1` 2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'serve a **um** uso').Count` — antes `1`, depois `0` 3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Ensaio dos cards em árvore temporária').Count` — antes `0`, depois `1` 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0` 5. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** as três contagens saem nos valores de depois e o kit segue válido.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-72b` do diário de obras, seção `## TK-72`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-11` - OP-11: O card que faz o planejador publicar a busca da superfície e ensaiar os cards sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Depende de:** `EBK-T10`
- **Fundamento:** pacotes 6 e 7 do `TK-72`.
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as Verificações.
- **Não fazer:** não tocar `.claude/agents/pantonic-scout.md`; não renumerar itens da Fase 4.
- **Contingências:** - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco.

## Execução

**Consumo:** 11 tool uses, 50.4 k tokens, 96.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
