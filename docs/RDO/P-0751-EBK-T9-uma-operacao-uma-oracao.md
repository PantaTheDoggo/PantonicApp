# RDO — P-0751 · EBK-T9

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T9` — Uma operação, uma oração
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` §3.2 e a skill `diario-de-obras` passam a dizer que operação escrita com mais de uma oração é operação mal recortada, que cada oração vira operação própria, e que a guarda é o marco.

**Arquivos-alvo:** - `GOVERNANCA.md` - `.claude/skills/diario-de-obras/SKILL.md`

**Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25. 1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'Uma operação, uma oração.').Count` — antes `0`, depois `1` 2. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'Operação escrita com mais de uma oração').Count` — antes `0`, depois `1` 3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0` 4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** as duas contagens saem nos valores de depois.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-73a` do diário de obras, seção `## TK-73`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-9` - OP-9: O card que publica a regra de uma operação, uma oração sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Fundamento:** Pacote 1 do `TK-73`; medição da §5 da seção `## TK-73` do diário de obras.
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as Verificações.
- **Texto novo 2:** ~~~~ marco. Operação escrita com mais de uma oração é operação mal recortada: cada oração vira operação própria, e a guarda também é o marco. ~~~~
- **Não fazer:** não mudar `modelo.py` nem o `check`; não editar modelo de plano nenhum.
- **Contingências:** - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco (o **Texto atual 2** é a linha que termina o parágrafo *Objeto e propriedade, na decomposição*, que hoje é exatamente `marco.`).

## Execução

**Consumo:** 10 tool uses, 49.5 k tokens, 79.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
