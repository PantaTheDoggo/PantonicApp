# RDO — P-0751 · EBK-T1

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T1` — O `check` acusa tíquete vivo sem card
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo tíquete `## TK-<n>` cujo status não é `done`, `cancelled` nem `superseded` e que não tem nenhuma subtarefa `### TK-<n><letra>`; a skill `diario-de-obras` nomeia o código.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `.claude/skills/diario-de-obras/SKILL.md` - `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` e `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md` — só pela contingência abaixo

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde, com os testes acima. 2. `python .claude/tools/backlog.py check` na árvore → `check: OK — nenhuma violação.` 3. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'o acusa como').Count` — antes `0`, depois `1`. 4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos (referência medida na autoria: `360 passed`, 2026-09-25).

**Pronto quando:** o `check` acusa tíquete vivo sem card, com par em teste, e sai `OK` sobre a árvore.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-83a` do diário de obras, seção `## TK-83`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-1` - OP-1: O card que faz a conferência do diário acusar tíquete aberto sem card sai de pronto para concluído, e o backlog do plano começa a esvaziar. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.
- **Propriedades:** 1. O `C-15` sai uma vez por tíquete vivo sem subtarefa, nomeando o tíquete. 2. Tíquete terminal sem subtarefa não é acusado. 3. As menções `C-1..C-14` do módulo passam a `C-1..C-15`.
- **Medido na autoria (2026-09-25):** quatro fixtures têm tíquete vivo sem subtarefa — `candidato_a_fechamento` (`TK-4`), `contador_inbox` (`TK-1`), `corpus` (`TK-1`) e `vermelho` (`TK-2`); a fixture `verde` tem `TK-1` com `TK-1a`.
- **Testes (novos, em `tests/test_backlog.py`):** - TF par sobre cópia da fixture `verde`: como está → nenhum `C-15`; com a subtarefa `TK-1a` removida → um `C-15` que nomeia `TK-1`. - TF: a mesma cópia sem `TK-1a` e com `TK-1` em `cancelled` (seção e índice) → nenhum `C-15`.
- **Não fazer:** não mudar outro código de violação; não tocar `next`.
- **Contingências:** - se um teste existente ficar vermelho só por causa do `C-15` numa das quatro fixtures → acrescentar ao tíquete acusado dessa fixture uma subtarefa mínima `### TK-<n>a — Card de fixture [Sonnet · classe mecanica]` com o mesmo status do tíquete — **exceto na fixture `vermelho`**, cujo `TK-2` tem `backlog` de propósito (é o `C-3` do teste): ali a subtarefa é `### TK-2a — Card de fixture [Sonnet · classe mecanica]` com a linha de status na forma das demais da fixture, estado `ready`, data `2026-01-01`, apensa ao fim do arquivo depois de uma linha em branco, sem linha no índice (DEB-6); se, com isso, outra asserção do mesmo teste mudar de resultado → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - **Medido pelo consultor (2026-09-25, acionamento 1, numa cópia da árvore com um `C-15` mínimo no `check`):** sem subtarefa, só `test_tf_check_vermelho_dispara_cada_codigo_uma_vez` fica vermelho (`1 failed, 359 passed`) — nenhum teste das outras três fixtures cai, e elas não se tocam; com o `TK-2a` `ready` acima → `360 passed` e `backlog.py check` na cópia → `check: OK — nenhuma violação.`, exit 0. - se a Verificação 2 acusar `C-15` na árvore → parar e sinalizar `blocked` razão `premissa`, colando as violações.
- **Notas de execução:** - 2026-09-25 `ready` — consultor acionamento 1: contingencia reparada (DEB-6, AE-1)

## Execução

**Consumo:** 40 tool uses, 97.0 k tokens, 325.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
