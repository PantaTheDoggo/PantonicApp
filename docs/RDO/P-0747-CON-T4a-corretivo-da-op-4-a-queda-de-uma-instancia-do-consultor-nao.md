# RDO — P-0747 · CON-T4a

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T4a` — Corretivo da OP-4: a queda de uma instância do consultor não se retoma
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CON-T4` (`AE-8`, `DCS-29`): a `A1` deixa de ser genérica — executor e `reviewer` se retomam por `SendMessage`; uma instância do consultor que cai se descarta, a telemetria dela registra `PARCIAL — trecho pré-queda não medido`, e o loop despacha uma instância nova com as mesmas três entradas, sobre o cenário como a caída o deixou; segunda queda no mesmo acionamento **PARA** —, e a seção *Acionamento do consultor* passa a dizer o mesmo. Uma regra para a queda, não duas.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T3b`**; o executor mede o **antes** antes da primeira edição. 1. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Consultor: **nenhuma** retomada').Count ~~~~ 2. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'a instância que cai se descarta').Count ~~~~ 3. antes `1` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'uma retomada por `SendMessage` ao mesmo `agentId`').Count ~~~~ 4. antes `1` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o consultor nunca é retomado').Count ~~~~ 5. antes `1` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '## Acionamento do consultor').Count ~~~~ 6. antes `2` · depois `2` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'sem executar a ação da rota').Count ~~~~ 7. antes `0` · depois `0` ~~~~ python .claude/tools/backlog.py check; $LASTEXITCODE ~~~~ 8. antes `0` · depois `0` ~~~~ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE ~~~~ 9. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE ~~~~ 10. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio de 2026-09-23 com os três corretivos aplicados) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.forma da figura` — fatia da `OP-4` (seção `## Acionamento do consultor` e a `A1` que a contradizia): a queda de uma instância do consultor tem uma regra só — descarte e despacho de instância nova sobre o cenário, nunca retomada por `SendMessage` — Verificação 1 a 5

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T3b`
- **Fundamento:** `DCS-4`, `DCS-6`, `DCS-19`, `DCS-29`; achado `AE-8`; laudo da `CON-T4` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-4` - OP-4: O mantenedor do loop instala a forma efêmera do consultor com o cenário persistido, numa seção própria da skill e não num passo novo: cada acionamento nasce uma instância que lê o cenário do plano e o card em causa, decide, reescreve o cenário com edição mínima e se encerra; o cenário passa a ser o próprio handover, a retomada da instância de prontidão sai da nota de telemetria, o reprovisionamento por limite deixa de existir, e as linhas do corpo do agente e da regra do loop que o descrevem instanciado uma vez por plano passam a descrevê-lo efêmero. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só a linha `A1` do bloco A e uma frase da seção `## Acionamento do consultor` (residência da `OP-4`); sem código.
- **Domínio:** **queda de instância** — notificação sem bloco `<usage>`; para o consultor, descarte e despacho novo em vez de retomada, porque o cenário é o handover (`DCS-6`, `DCS-29`).
- **Contratos/classes:** nenhuma assinatura de código; a linha `A1` mantém as três colunas `| # | condição | ação |`.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**. 2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não tocar o passo 8 nem a lista *O que obriga parada*: são da `CON-T3b`; a linha 6 da `Verificação` mede isso. - Não tocar a nota de telemetria do passo 9 (*"o consultor nunca é retomado"*): já diz o certo; a linha 4 da `Verificação` mede isso. - Não criar passo novo nem seção nova (`DCS-19`).
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Fora do escopo desta tarefa:** o passo 8 e a lista de parada (`CON-T3b`); o agente do consultor (`CON-T2a`).

## Execução

**Consumo:** 12 tool uses, 57.9 k tokens, 75.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
