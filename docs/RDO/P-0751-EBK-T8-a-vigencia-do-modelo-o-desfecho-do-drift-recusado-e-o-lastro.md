# RDO — P-0751 · EBK-T8

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T8` — A vigência do modelo, o desfecho do drift recusado e o lastro na descrição pública
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` §3.2 passa a dizer que o modelo só vigora depois de validado pelo dono — o rascunho carrega `situação: vigente` por forma, não por vigência — e o que acontece com o que foi entregue sob uma versão pendente recusada; `README.md` §8.1 passa a dizer ao leitor que todo elemento do modelo tem lastro no pedido.

**Arquivos-alvo:** - `GOVERNANCA.md` - `README.md`

**Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25. 1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'o modelo só vigora depois de validado pelo dono').Count` — antes `0`, depois `1` 2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'retroage ao ponto do drift').Count` — antes `0`, depois `1` 3. `(Select-String -Path README.md -SimpleMatch 'Todo elemento do modelo tem **lastro** no pedido').Count` — antes `0`, depois `1` 4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** as três contagens saem nos valores de depois e a suíte segue verde.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-70a` do diário de obras, seção `## TK-70`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-8` - OP-8: O card que diz quando o modelo passa a valer e o que acontece com a versão recusada sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Fundamento:** `DLS-3` e `DLS-4` do `P-0746`; `AE-21` daquele plano; confirmação medida em 2026-09-25, na seção `## TK-70` do diário de obras.
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as Verificações.
- **Não fazer:** não tocar `.claude/skills/scrum-master/SKILL.md` (o Pacote B já está lá); não editar modelo de plano nenhum; não editar a seção do `TK-69`.
- **Contingências:** - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco.

## Execução

**Consumo:** 11 tool uses, 50.7 k tokens, 74.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
