# RDO — DIARIO_DE_OBRAS · TK-78a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-78a` — O loop não para para rebaixar o modelo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** tirar da skill do loop, da skill `modelo-por-fase`, da matriz de `GOVERNANCA.md` §3 e do hook de nudge a instrução de parar para **rebaixar** o modelo: o contexto principal só orquestra, o modelo de cada tarefa viaja no despacho, e modelo ativo acima do indicado vira uma linha de nota, nunca parada. A única parada que sobra é a de subir: modelo ativo abaixo do que a fase exige para e pede ao dono o `/model` do melhor.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md` - `.claude/skills/modelo-por-fase/SKILL.md` - `GOVERNANCA.md` - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` - `README.md` - `.claude/README.md` (regenerado pelo gerador do kit, nunca à mão)

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-24. 1. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'PARA e pede `/model` ao dono').Count` — antes `1`, depois `0` 2. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'O loop nunca para para rebaixar o modelo').Count` — antes `0`, depois `1` 3. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch '--desde <data de abertura da janela>').Count` — antes `1`, depois `0` 4. `(Select-String -Path .claude/skills/modelo-por-fase/SKILL.md -SimpleMatch 'Gate de parada').Count` — antes `2`, depois `0`; `(Select-String -Path .claude/skills/modelo-por-fase/SKILL.md -SimpleMatch '## Gate de subida').Count` — antes `0`, depois `1` 5. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**para para pedir `/model`**').Count` — antes `1`, depois `0`; `(Select-String -Path GOVERNANCA.md -SimpleMatch '**nunca para para rebaixar o modelo**').Count` — antes `0`, depois `1` 6. `(Select-String -Path README.md -SimpleMatch 'e para para pedir o correto').Count` — antes `1`, depois `0` 7. `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'recomende ao dono `/model sonnet`').Count` — antes `1`, depois `0`; `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'NAO pare e NAO peca').Count` — antes `0`, depois `1`; `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'PARE e peca').Count` — antes e depois `1` 8. `python -m py_compile .claude/global/hooks/modelo_por_fase_userpromptsubmit.py; $LASTEXITCODE` — `0` 9. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE` — depois `0` 10. `python -m pytest -q` — total de `passed` ≥ o medido no despacho, `0 failed`

**Pronto quando:** nenhuma das quatro superfícies manda parar para rebaixar o modelo, e as quatro dizem a mesma coisa — acima do indicado segue no modelo ativo e anota a divergência, abaixo do indicado para e pede o `/model` do melhor, o modelo da tarefa viaja no despacho — Verificações 1 a 7; o relatório de encerramento chama `modelo.py show` na forma que a ferramenta aceita — Verificação 3; nenhum gate regrediu — Verificações 8 a 10.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-24
- **Fundamento:** ordem do dono de 2026-09-24 e adendo do dono na abertura da execução (acima); caso medido acima.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o **Texto atual 1** pelo **Texto novo 1** e o **Texto atual 2** pelo **Texto novo 2**. 2. Em `.claude/skills/modelo-por-fase/SKILL.md`, substitua os **Textos atuais 3, 4 e 5** pelos **Textos novos 3, 4 e 5**. 3. Em `GOVERNANCA.md`, substitua o **Texto atual 6** pelo **Texto novo 6**. 4. Em `README.md`, substitua o **Texto atual 7** pelo **Texto novo 7**. 5. Em `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, substitua o **Texto atual 9** pelo **Texto novo 9** (não há Texto 8: o nudge da fase intelectual fica intacto). 6. Rode `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (a `description` da `modelo-por-fase` muda a região gerada de `.claude/README.md`). 7. Rode as Verificações.
- **Restrições desta tarefa:** - Toda edição é substituição literal; o texto novo entra exatamente como está no bloco. Os arquivos `.md` da skill têm final de linha CRLF na cópia de trabalho: compare ignorando `\r` e preserve o final de linha existente. - Não editar nada fora do repositório: a projeção do hook para `~/.claude/hooks/` é ato do dono (Fora do escopo). - Não tocar a Regra 5 (anúncio de troca efetivada) nem a seção `## Convenção de anúncio` da `modelo-por-fase`. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (referência histórica: `277 passed`, 2026-09-24).
- **Não fazer:** não mudar a tabela de modelo por fase (quem roda em que modelo); não remover a skill `modelo-por-fase`; não tocar `_NUDGE["intellectual"]` nem as `systemMessage` do hook (a parada para subir é a que o adendo preserva); não editar `C:\Users\panta\.claude\`.
- **Contingências:** - se um bloco **Texto atual** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se `kit_check.ps1 -Mode generate` ou `-Mode check-drift` sair diferente de `0` → parar e sinalizar `blocked` razão `ferramenta`, colando a última linha da saída - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e texto de nudge. TR: a suíte inteira; `py_compile` do hook.
- **Fora do escopo desta tarefa:** projetar o hook no ponto de carga — ato do dono, depois do fechamento: `Copy-Item .claude/global/hooks/modelo_por_fase_userpromptsubmit.py $HOME/.claude/hooks/ -Force` (a cópia do kit é superconjunto da carregada: a única diferença medida em 2026-09-24 é a leitura de stdin em UTF-8, que o kit já tem); a Regra 7 do `~/.claude/CLAUDE.md` do dono.
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz `GOVERNANCA.md` §3). Modelo diferente do exigido: **PARA e pede `/model` ao dono**.
- **Saída:** modelo conferido, ou parada com o `/model` pedido.
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz `GOVERNANCA.md` §3). Modelo ativo **acima** do exigido: **segue** nele — o contexto principal só orquestra, e o modelo de cada tarefa viaja no despacho (passo 4) — e anota a divergência em uma linha do relatório de encerramento. O loop nunca para para rebaixar o modelo. Modelo ativo **abaixo** do exigido: **PARA e pede ao dono o `/model` do modelo melhor** — a única parada do gate.
- **Saída:** modelo conferido, com a divergência anotada quando houver, ou parada com o `/model` do modelo melhor pedido.

## Execução

**Consumo:** 26 tool uses, 67.7 k tokens, 157.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Pronto quando segue falso: GOVERNANCA.md §3 bullet 'Gatilho operacional do modelo por fase' e README.md §4 (dois trechos) ainda mandam parar em qualquer divergencia, inclusive para rebaixar; os blocos do card nao os cobriram. Rota: B1 -> consultor (AE-1 do TK-78).

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
