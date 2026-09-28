# RDO — P-0747 · CON-T6a

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T6a` — Corretivo da OP-6: a spec não prevalece sobre o bloco A
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CON-T6` (`AE-15`, `DCS-31`): o parágrafo *Consequência sobre a §2* da subseção *Ato do dono de 2026-09-22* (§3 da spec, `F-4` item 50) deixa de afirmar que a spec prevalece enquanto o bloco A não for reescrito — o bloco A foi reescrito pela `CON-T3` e pelos corretivos `CON-T3a`..`CON-T3c` — e vira registro histórico datado, apontando para a skill do loop e para `G-REPLAN`, onde a regra mora hoje.

**Arquivos-alvo:** - `docs/consultant-spec.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 6) na árvore real, com o bloco aplicado e revertido por cópia, **como está depois da `CON-T6`**; o executor mede o **antes** antes da primeira edição. 1. antes `1` · depois `0` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Enquanto o bloco A não for').Count ~~~~ 2. antes `1` · depois `0` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '**a spec prevalece**').Count ~~~~ 3. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'a spec prevaleceu por precedência do dono').Count ~~~~ 4. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Registro histórico: o bloco A foi reescrito pela').Count ~~~~ 5. antes `1` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Lastro medido, não fonte normativa').Count ~~~~ 6. antes `0` · depois `0` ~~~~ python .claude/tools/backlog.py check; $LASTEXITCODE ~~~~ 7. antes `0` · depois `0` ~~~~ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE ~~~~ 8. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T6`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 6) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.estatuto na doutrina` — fatia da `OP-6` (`F-4` item 50): a spec permanece lastro medido e não normativo, e nenhum parágrafo dela afirma prevalecer sobre a norma — Verificação 1 a 5

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T5a`
- **Fundamento:** `DCS-4`, `DCS-31`; achado `AE-15`; laudo da `CON-T6` (aprovado 100, `seguir`).
- **Operação do modelo:** `OP-6` - OP-6: O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** documento de lastro (`docs/consultant-spec.md`, só o parágrafo `:167-169`, item 50); sem código. `docs/DOC_MAP.md` não muda: a entrada da spec diz *"~480 linhas"* e o arquivo vai de 477 a 479 linhas.
- **Domínio:** **precedência da spec** — nenhuma: a spec é lastro medido, não fonte normativa (estatuto, `:3-5`); a frase que afirmava precedência sobre o bloco A é datada e apontada para onde a regra mora. Invariante: as quatro diretivas `DC-1`..`DC-4`, o parágrafo *Por que a lacuna existia* e os dois blocos de *Lastro* não mudam.
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:** 1. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não tocar `DC-1`..`DC-4`, o parágrafo *Por que a lacuna existia* nem os blocos de *Lastro* da subseção. - Não corrigir as três contagens defasadas da spec (`DCS-2`) e não tocar a §11 (item 46, `CON-T7`). - Não tocar `docs/DOC_MAP.md` (item 43, `CON-T6`, fechada).
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita lastro e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Fora do escopo desta tarefa:** a §11 da spec (item 46, `CON-T7`); o índice de documentos (item 43, `CON-T6`); o diário e a Regra 8 (`CON-T5a`, `OP-5`).

## Execução

**Consumo:** 11 tool uses, 57.5 k tokens, 63.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
