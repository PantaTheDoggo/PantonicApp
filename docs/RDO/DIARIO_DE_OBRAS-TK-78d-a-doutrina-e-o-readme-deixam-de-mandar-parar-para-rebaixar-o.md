# RDO — DIARIO_DE_OBRAS · TK-78d

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-78d` — A doutrina e o README deixam de mandar parar para rebaixar o modelo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** corretivo da `TK-78a` (`AE-1` abaixo): os dois trechos que os Textos 1-9 da `TK-78a` não cobriram — `GOVERNANCA.md` §3, bullet *Gatilho operacional do modelo por fase*, e `README.md` §4, frase do gatilho e parágrafo *Onde o gerente intervém* — passam a dizer o mesmo que a skill do loop, a `modelo-por-fase` e o hook já dizem: modelo ativo **acima** do indicado segue e anota a divergência em uma linha; **abaixo** do indicado para e pede ao dono o `/model` do modelo melhor.

**Arquivos-alvo:** - `GOVERNANCA.md` - `README.md`

**Verificação:** no PowerShell 7 (`pwsh`), na raiz do repositório; **antes** medido em 2026-09-24, **depois** medido pelo consultor sobre cópia com as três substituições aplicadas. 1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'e o modelo ativo, **para** e pede o `/model` correto ao dono').Count` — antes `1`, depois `0` 2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'exige, **para** e pede ao dono o `/model` do modelo melhor').Count` — antes `0`, depois `1` 3. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**nunca para para rebaixar o modelo**').Count` — antes `1`, depois `2` 4. `(Select-String -Path README.md -SimpleMatch 'confere contra o modelo ativo e **para** para pedir o `/model` correto').Count` — antes `1`, depois `0`; `(Select-String -Path README.md -SimpleMatch '**abaixo** do exigido **para** para pedir o `/model` do modelo melhor').Count` — antes `0`, depois `1` 5. `(Select-String -Path README.md -SimpleMatch 'Quando o gate dispara, ele para e pede uma').Count` — antes `1`, depois `0`; `(Select-String -Path README.md -SimpleMatch 'decidir sozinho e seguir').Count` — antes `1`, depois `0` 6. `(Select-String -Path README.md -SimpleMatch 'agente seguir sozinho num modelo mais fraco').Count` — antes `0`, depois `1`; `(Select-String -Path README.md -SimpleMatch 'orquestra, nunca interrompe o trabalho').Count` — antes `0`, depois `1` 7. Discriminante das cinco superfícies: `(Select-String -Path GOVERNANCA.md,README.md,.claude/skills/scrum-master/SKILL.md,.claude/skills/modelo-por-fase/SKILL.md,.claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch '`/model` correto').Count` — antes `2`, depois `0` 8. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE` — antes e depois `0` 9. `pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE` — antes e depois `0` 10. `python -m pytest -q` — total de `passed` ≥ o medido no despacho, `0 failed`

**Pronto quando:** nenhuma superfície do kit manda parar para rebaixar o modelo nem pede o `/model` "correto" em qualquer divergência, e `GOVERNANCA.md` e `README.md` dizem o mesmo que a skill do loop, a `modelo-por-fase` e o hook — acima do indicado segue e anota, abaixo do indicado para e pede o melhor — Verificações 1 a 7; nenhum gate regrediu — Verificações 8 a 10. Fechada esta tarefa, o `Pronto quando` da `TK-78a` fica verdadeiro.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Depende de:** `TK-78a`
- **Fundamento:** adendo do dono de 2026-09-24 (cabeçalho do `## TK-78`); `AE-1`; triagem do consultor de 2026-09-24 (`docs/plans/_CENARIO-TK-78.md`, `CT-1`).
- **Passos:** 1. Em `GOVERNANCA.md`, substitua o **Texto atual 1** pelo **Texto novo 1**. 2. Em `README.md`, substitua o **Texto atual 2** pelo **Texto novo 2** e o **Texto atual 3** pelo **Texto novo 3**. 3. Rode as Verificações.
- **Restrições desta tarefa:** - Toda edição é substituição literal de linhas inteiras; o texto novo entra exatamente como está no bloco. Os dois arquivos têm final de linha LF. - Não tocar as outras superfícies já conformes (`.claude/skills/scrum-master/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, o hook), nem a linha *Orquestração* da matriz de `GOVERNANCA.md` §3, nem o parágrafo *Por quê* do `README.md` §4. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (medido pelo consultor em 2026-09-24: `277 passed`).
- **Não fazer:** não mudar a tabela de modelo por fase; não editar `CHANGELOG.md` (registro histórico); não editar `C:\Users\panta\.claude\`.
- **Contingências:** - se um bloco **Texto atual** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se `kit_check.ps1 -Mode check-drift` ou `check-readme.ps1` sair diferente de `0` → parar e sinalizar `blocked` razão `ferramenta`, colando a última linha da saída - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e espelho; nenhum teste prende os literais trocados (medido em 2026-09-24). TR: a suíte inteira.
- **Fora do escopo desta tarefa:** as `systemMessage` do hook (`considere /model sonnet|haiku`), que sugerem ao dono sem mandar parar e que a `TK-78a` proibiu tocar; o `CHANGELOG.md`, que registra o gate de parada como história. detecta a fase da tarefa e o modelo ativo, **para** e pede o `/model` correto ao dono (fato detecta a fase da tarefa e o modelo ativo e, só quando o ativo está **abaixo** do que a fase exige, **para** e pede ao dono o `/model` do modelo melhor — acima do exigido segue e anota a divergência em uma linha, porque o contexto principal só orquestra e o modelo de cada tarefa viaja no despacho (linha *Orquestração* acima); o gate **nunca para para rebaixar o modelo** (fato

## Execução

**Consumo:** 11 tool uses, 53.2 k tokens, 138.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
