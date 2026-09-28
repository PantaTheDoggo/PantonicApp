# RDO — P-0747 · CON-T8

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T8` — A porta de entrada e a descrição do agente
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente.

**Arquivos-alvo:** - `README.md` - `.claude/agents/pantonic-consultant.md` - `.claude/README.md` (só pelo passo de regeneração)

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição. 1. antes `1` · depois `0` ~~~~ (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'roteada ao planejador').Count ~~~~ 2. antes `1` · depois `0` ~~~~ (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado uma vez, mantido de standby').Count ~~~~ 3. antes `0` · depois `1` ~~~~ (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'Ponto de triagem de **toda** parada de executor').Count ~~~~ 4. antes `1` · depois `1` ~~~~ (Select-String -Path 'README.md' -SimpleMatch -CaseSensitive -Pattern 'O kit são dez agentes').Count ~~~~ 5. antes `1` · depois `0` ~~~~ (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado UMA vez').Count ~~~~ 6. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'description: Consultor de plano Pantonic*, papel de doutrina').Count ~~~~ 7. antes `1` · depois `0` ~~~~ (Select-String -Path '.claude/README.md' -SimpleMatch -CaseSensitive -Pattern 'instanciado UMA vez').Count ~~~~ 8. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/README.md' -SimpleMatch -CaseSensitive -Pattern 'papel de doutrina (GOVERNANCA.md §3, linha Consultoria)').Count ~~~~ 9. antes `0` · com a `description` trocada e a região ainda não regenerada `1` · depois do passo de regeneração `0` ~~~~ (pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift | Select-String -SimpleMatch -Pattern 'README.md diverge do regenerado').Count ~~~~ 10. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE ~~~~ 11. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE ~~~~ 12. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio) ~~~~ python -m pytest -q ~~~~ 13. Veredito do dono sobre o `README.md` revisado (G-README dever 2): `go`, pedido pela orquestração no relatório de encerramento.

**Pronto quando:** - `consultor.descrição pública da figura` — a porta de entrada, a `description` do agente e a região gerada, regenerada no mesmo ato, descrevem o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente; *"O kit são dez agentes"* fica igual — Verificação 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T7a`
- **Fundamento:** `DCS-15`, `DCS-17`, `DCS-20`; fatos `F-4` itens 39, 40, 41 e 47, `F-5`, `F-16`; G-README dever 2 (a tarefa de revisão do `README.md` que fecha a sprint).
- **Operação do modelo:** `OP-8` - OP-8: O mantenedor leva a figura nova à porta de entrada do repositório: a tabela de guardrails deixa de rotear o escalonamento ao planejador, a linha do consultor na tabela de agentes deixa de anunciá-lo instanciado uma vez e mantido de prontidão, e a descrição curta do agente é reescrita no mesmo ato em que o índice gerado do kit é regenerado, os quatro passando a descrever o papel de doutrina, a triagem de toda parada e a forma que o veredito do piloto deixou vigente. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** porta de entrada — `README.md`, a `description` do agente e a região gerada `kit:agents` de `.claude/README.md`, esta só por instrumento (`I-4`).
- **Domínio:** **veredito do piloto** — `adotada`, `recusada` ou `amostra insuficiente`, lido na última linha da tabela da subseção *Veredito do piloto da forma efêmera* da §11 de `docs/consultant-spec.md`, gravada pela `CON-T7`.
- **Contratos/classes:** frontmatter YAML do agente: a `description` é uma linha só, sem a sequência dois-pontos-espaço.
- **Passos:** 1. Em `README.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**. 2. Em `README.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**. 3. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**. 4. Rode `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (exit `0` no ensaio): ele reescreve a região `kit:agents` de `.claude/README.md` a partir da `description` nova.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não editar `.claude/README.md` à mão: só `kit_check.ps1 -Mode generate` (`I-4`). - Não alterar *"O kit são dez agentes"* (`DCS-15`); a linha 4 da `Verificação` mede isso. - Não corrigir a duplicação `` `scrum-master`/`scrum-master` `` na coluna da direita da linha 17 da tabela de guardrails: fora do escopo.
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário - se a subseção *Veredito do piloto da forma efêmera* não existir na §11 de `docs/consultant-spec.md` → parar e sinalizar `blocked` razão `dependencia`, citando `CON-T7`; se ela existir sem o parágrafo *Modelo das instâncias medidas* → o mesmo, citando `CON-T7a`
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Fora do escopo desta tarefa:** nenhuma outra linha do `README.md`.

## Execução

**Consumo:** 19 tool uses, 67.0 k tokens, 104.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 93%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
