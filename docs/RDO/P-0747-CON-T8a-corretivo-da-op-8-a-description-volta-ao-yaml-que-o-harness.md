# RDO — P-0747 · CON-T8a

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T8a` — Corretivo da OP-8: a description volta ao YAML que o harness lê
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CON-T8` (`AE-20`, `DCS-33`): a `description` de `.claude/agents/pantonic-consultant.md` (`F-4` item 47) volta ao **Texto novo 3** da variante `adotada`, literal — `Efêmero - cada acionamento` onde entrou `Efêmero: cada acionamento` —, porque a sequência dois-pontos-espaço num valor sem aspas faz o parser YAML recusar o frontmatter inteiro, e o consultor é hoje o único dos dez agentes que o harness não lê. A região gerada `kit:agents` de `.claude/README.md` (item 41), regenerada a partir do valor defeituoso, se regenera de novo no mesmo ato. `README.md` não muda: o *"Efêmero: cada acionamento"* do Texto novo 2 é célula de tabela markdown, onde dois-pontos é legítimo.

**Arquivos-alvo:** - `.claude/agents/pantonic-consultant.md` - `.claude/README.md` (só pelo passo de regeneração)

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 8) na árvore real, **como está depois da `CON-T8`**, com o bloco aplicado e a região regenerada, ambos revertidos por cópia; o executor mede o **antes** antes da primeira edição. 1. antes: traceback e `1` · depois: `ok` e `0` — o parse YAML estrito do frontmatter ~~~~ python -c "import yaml; yaml.safe_load(open('.claude/agents/pantonic-consultant.md',encoding='utf-8').read().split('---')[1]); print('ok')"; $LASTEXITCODE ~~~~ 2. antes `1` · depois `0` ~~~~ (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero: cada acionamento').Count ~~~~ 3. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero - cada acionamento').Count ~~~~ 4. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/README.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero - cada acionamento').Count ~~~~ 5. antes `0` · com a `description` trocada e a região ainda não regenerada `1` · depois do passo 2 `0` ~~~~ (pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift | Select-String -SimpleMatch -Pattern 'README.md diverge do regenerado').Count ~~~~ 6. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE ~~~~ 7. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE ~~~~ 8. antes `1` · depois `1` — o Texto novo 2 da `CON-T8` fica ~~~~ (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'Efêmero: cada acionamento').Count ~~~~ 9. antes `0` · depois `0` ~~~~ python .claude/tools/backlog.py check; $LASTEXITCODE ~~~~ 10. antes `0` · depois `0` ~~~~ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE ~~~~ 11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — árvore real, acionamento 8 — e `277 passed` depois, com o bloco aplicado e a região regenerada) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.descrição pública da figura` — término da `OP-8` (`F-4` itens 41 e 47): a `description` do agente é o Texto novo 3 literal da variante `adotada`, o frontmatter passa no parser YAML estrito e a região gerada, regenerada no mesmo ato, o reproduz; `README.md` e *"O kit são dez agentes"* ficam iguais — Verificação 1 a 8

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T8`
- **Fundamento:** `DCS-4`, `DCS-20`, `DCS-33`; achado `AE-20`; laudo da `CON-T8` (ressalva 93, `seguir com ressalva`); `F-16`; `I-4`.
- **Operação do modelo:** `OP-8` - OP-8: O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** porta de entrada — a `description` do agente (item 47) e a região gerada `kit:agents` de `.claude/README.md` (item 41), esta só por instrumento (`I-4`). `README.md` fica como a `CON-T8` deixou.
- **Domínio:** **frontmatter legível** — o bloco YAML entre os dois `---` do agente é o que o harness lê para registrar o agente; um valor escalar sem aspas que contenha a sequência dois-pontos-espaço torna o bloco inválido para um parser estrito, e o arquivo deixa de ser agente. Invariante: o corpo do agente (itens 24 e 44, `CON-T2`, `CON-T2a`, `CON-T4`) não muda.
- **Contratos/classes:** frontmatter YAML do agente: a `description` é uma linha só, sem a sequência dois-pontos-espaço, e `yaml.safe_load` do bloco entre os `---` sai sem erro (linha 1 da `Verificação`).
- **Passos:** 1. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1** (é a linha 3 do arquivo, inteira). 2. Rode `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (exit `0` medido): ele reescreve a região `kit:agents` de `.claude/README.md` a partir da `description` corrigida.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação — o separador depois de *Efêmero* é hífen entre espaços. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não editar `.claude/README.md` à mão: só `kit_check.ps1 -Mode generate` (`I-4`). - Não tocar `README.md`: a linha 8 da `Verificação` mede que o Texto novo 2 da `CON-T8` fica. - Não tocar o corpo do agente (abaixo do segundo `---`) nem as linhas `name:`, `model:` e `tools:` do frontmatter.
- **Contingências:** - se o bloco **Texto atual 1** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo 1**, corrigir a cópia, rodar o passo 2 de novo e medir de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Fora do escopo desta tarefa:** `README.md` (`CON-T8`, fechada); o corpo do agente (`CON-T2`, `CON-T2a`, `CON-T4`, fechadas); `kit_check.ps1 -Mode validate` recusar frontmatter inválido (item (iii) do `AE-20`, tíquete de instrumento, fora deste plano).

## Execução

**Consumo:** 8 tool uses, 58.1 k tokens, 72.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
