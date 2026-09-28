# RDO — DIARIO_DE_OBRAS · TK-76a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-76a` — As tabelas do modelo em frases curtas para o dono
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** fixar, na norma e nas duas definições de conduta, que as três tabelas do modelo conceitual — objetos, texto das operações, estados — são escritas para o dono em frases curtas e ilustrativas, e que a especificidade que o executor precisa mora nas seções do plano escritas para a máquina.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md` - `GOVERNANCA.md` - `.claude/agents/pantonic-planner.md`

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-23. 1. `(Select-String -Path .claude/agents/pantonic-model-designer.md -SimpleMatch 'As tabelas do modelo se escrevem para o dono').Count` — antes `0`, depois `1` 2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'human-friendly').Count` — antes `0`, depois `1` 3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'escrito para o dono').Count` — antes `0`, depois `1` 4. `python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md` — antes e depois `modelo: OK — 8 operações, 5 objetos, 12 propriedades, 8 tarefas, versão 1`, exit `0` 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` — antes e depois exit `0` 6. `python -m pytest -q` — total de `passed` igual ao medido no despacho, `0 failed`

**Pronto quando:** a regra *tabelas do modelo human-friendly, especificidade nas seções machine-friendly* está escrita nas três residências — Verificações 1, 2 e 3 —, o `P-0747` segue intocado e verde — Verificação 4 —, e nenhum gate regrediu — Verificações 5 e 6.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Fundamento:** ato do dono de 2026-09-23 (acima); veredito `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` §3.4.
- **Passos:** 1. Em `.claude/agents/pantonic-model-designer.md`, insira o bloco **Texto novo 1** imediatamente antes da linha `## Os quatro atos`, separado por uma linha em branco antes e depois. 2. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**. 3. Em `.claude/agents/pantonic-planner.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**.
- **Restrições desta tarefa:** - Toda edição é substituição ou inserção literal: o texto novo entra exatamente como está no bloco. - Não tocar `docs/plans/P-0747-consultor-de-plano.md` nem nenhum outro plano (ato do dono). - Não tocar `.claude/tools/modelo.py`, seus testes nem suas fixtures. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (medido em 2026-09-23: `277 passed`, referência histórica).
- **Não fazer:** não alterar a `description` do frontmatter de nenhum agente (mudaria a região gerada de `.claude/README.md` e deixaria o check-drift vermelho); não reescrever as tabelas de plano nenhum para a forma nova.
- **Contingências:** - se um bloco **Texto atual** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se a linha `## Os quatro atos` não existir exatamente uma vez em `.claude/agents/pantonic-model-designer.md` → parar e sinalizar `blocked` razão `premissa` - se o valor **antes** de qualquer linha de `Verificação` diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina. A guarda é a suíte inteira, que inclui `tests/test_doutrina_unidade.py` (prende literais de `GOVERNANCA.md` e de `.claude/agents/pantonic-planner.md`).
- **Fora do escopo desta tarefa:** estender a `V12` às tabelas; reescrever modelo de plano existente; o restante do `TK-72` §7.

## Execução

**Consumo:** 18 tool uses, 52.3 k tokens, 79.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
