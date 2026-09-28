# RDO — P-0747 · CON-T3c

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T3c` — Corretivo da OP-3: com estrategico= a rota planejador executa a sua ação, que já é a parada
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CON-T3b` (`AE-10` ii, `DCS-30`): a triagem do passo 8 e a lista *O que obriga parada* deixam de suspender a ação da rota "em qualquer rota" — a suspensão com `estrategico=` vale para `resolve` e `modelador`; com `rota=planejador` a ação da rota já é a parada e se executa como está (`DCS-28`): o plano é materializado `blocked`, a rodada de replanejamento enfileirada, e a frase vai junto ao relatório de encerramento.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 5) na árvore real, com os blocos aplicados e revertidos por hash, **como está depois da `CON-T4a`**; o executor mede o **antes** antes da primeira edição. A linha 4 é a coerência do módulo herdada da `CON-T3b`: as duas ocorrências ficam, qualificadas. 1. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'a ação da rota já é a parada').Count ~~~~ 2. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'se executa com ou sem `estrategico=`').Count ~~~~ 3. antes `0` · depois `2` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'nas rotas `resolve` e `modelador`').Count ~~~~ 4. antes `2` · depois `2` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'sem executar a ação da rota').Count ~~~~ 5. antes `5` · depois `5` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern '`planejador` e `estrategico=` **PARAM**').Count ~~~~ 6. antes `1` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'o modelador **não** é despachado').Count ~~~~ 7. antes `1` · depois `1` ~~~~ (Select-String -Path '.claude/skills/scrum-master/SKILL.md' -SimpleMatch -CaseSensitive -Pattern 'Consultor: **nenhuma** retomada').Count ~~~~ 8. antes `0` · depois `0` ~~~~ python .claude/tools/backlog.py check; $LASTEXITCODE ~~~~ 9. antes `0` · depois `0` ~~~~ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE ~~~~ 10. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE ~~~~ 11. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T4a`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 5) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.alcance da triagem das paradas` — fatia da `OP-3` (`F-4` itens 2 e 8): com `estrategico=` a suspensão da ação da rota vale para `resolve` e `modelador`, e a rota `planejador` executa a sua ação, que já é a parada — plano `blocked`, replanejamento enfileirado, frase no relatório — Verificação 1 a 6

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T4a`
- **Fundamento:** `DCS-3`, `DCS-4`, `DCS-28`, `DCS-30`; achado `AE-10` (ii); laudo da `CON-T3b` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do loop reescreve a condução das paradas: as duas fontes normativas da skill passam a citar as decisões deste plano, toda regra que roteia parada de executor ou laudo com pendência substantiva e o guardrail que manda a matéria ao planejador passam a levá-los ao consultor, o loop despacha a rota que ele devolve e, quando a rota é o modelador, despacha o modelador sem parar a janela e leva o pedido de validar o drift ao dono no marco. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** procedimento de orquestração — `.claude/skills/scrum-master/SKILL.md`, só a triagem do passo 8 e a lista *O que obriga parada* (`F-4` itens 2 e 8, já reescritos pela `CON-T3`, pela `CON-T3a` e pela `CON-T3b`); sem código.
- **Domínio:** **linha `estrategico=` com `rota=planejador`** — a ação da rota é a própria parada (`DCS-28`), e suspendê-la deixaria o plano sem `blocked` materializado e sem rodada de replanejamento enfileirada (`G-REPLAN`); nas rotas `resolve` e `modelador` nada muda em relação à `CON-T3b`. Invariante: sem `estrategico=`, `resolve` e `modelador` seguem e `planejador` para (`DCS-24`).
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**. 2. Em `.claude/skills/scrum-master/SKILL.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não tocar a `A1`, a seção `## Acionamento do consultor` nem a nota de telemetria do passo 9: são da `OP-4` (`CON-T4`, `CON-T4a`); a linha 7 da `Verificação` mede isso. - Não tocar as regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1`: elas remetem ao passo 8, que é o que muda; a linha 5 da `Verificação` mede isso.
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Fora do escopo desta tarefa:** a `A1`, a seção `## Acionamento do consultor` e a nota de telemetria do passo 9 (`OP-4`); o agente do consultor (item 24, `OP-2`), cuja frase *"em qualquer rota sem executar a ação da rota"* se lê com a `DCS-28` que cita (`AE-12`, inconclusivo).

## Execução

**Consumo:** 15 tool uses, 60.7 k tokens, 88.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
