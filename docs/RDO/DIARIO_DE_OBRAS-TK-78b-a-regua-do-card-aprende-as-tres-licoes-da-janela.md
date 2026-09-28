# RDO — DIARIO_DE_OBRAS · TK-78b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-78b` — A régua do card aprende as três lições da janela
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** fixar na definição do planejador que card de investigação mantém o rótulo `Pronto quando`, que card que edita a configuração do harness declara a contingência de permissão recusada, e que verificação por total de diff sobre arquivo com alteração alheia mede delta contra a base do despacho.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-24. 1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'por **o número ou fato que tem de existir ao final**').Count` — antes `1`, depois `0` 2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Pronto quando (o fato que tem de existir ao final)').Count` — antes `0`, depois `1` 3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'o dono cola o bloco literal do card').Count` — antes `0`, depois `1` 4. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'contra a base re-medida no despacho').Count` — antes `0`, depois `1` 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE` — antes e depois `0` 6. `python -m pytest -q` — total de `passed` ≥ o medido no despacho, `0 failed`

**Pronto quando:** as três regras estão escritas na definição do planejador — Verificações 1 a 4 —, e nenhum gate regrediu — Verificações 5 e 6.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Depende de:** `TK-78a`, `TK-78d`
- **Fundamento:** `AE-1`, `AE-2` (ii) e `AE-3` (i) do `P-0748`.
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md`, substitua o **Texto atual 1** pelo **Texto novo 1**. 2. Rode as Verificações.
- **Restrições desta tarefa:** - Substituição literal; o texto novo entra exatamente como está no bloco. - Não alterar a `description` do frontmatter (mudaria a região gerada de `.claude/README.md`). - Não tocar `.claude/tools/rdo.py` nem `review_evidence.py` — o rótulo se acerta na doutrina, não no parser. - Não reescrever card de plano nenhum para a forma nova. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui.
- **Não fazer:** não tocar os pacotes do `TK-72` nem `GOVERNANCA.md`.
- **Contingências:** - se o **Texto atual 1** não for encontrado **exatamente uma vez** → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina. A guarda é a suíte inteira, que inclui `tests/test_doutrina_unidade.py` (prende literais de `.claude/agents/pantonic-planner.md`).
- **Fora do escopo desta tarefa:** os pacotes do `TK-72`; ensinar ao parser um rótulo novo.

## Execução

**Consumo:** 10 tool uses, 52.0 k tokens, 117.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
