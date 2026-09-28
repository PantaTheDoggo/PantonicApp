# RDO — P-0747 · CON-T7a

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T7a` — Corretivo da OP-7: o veredito declara o modelo das instâncias
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CON-T7` (`AE-19`, `DCS-32`): a subseção *Veredito do piloto da forma efêmera* da §11 da spec (`F-4` item 46) passa a declarar o modelo em que as três instâncias medidas rodaram (`claude-fable-5-1`, ato do dono `DCS-23`), que a coluna de custo é contagem de tokens precificada pela tabela Opus nos dois lados — preço-Opus-equivalente, não custo real — e que a sonda se reexecuta na primeira execução de plano com o consultor em Opus. O veredito `adotada`, a tabela e a frase do veredito não mudam.

**Arquivos-alvo:** - `docs/consultant-spec.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 7) na árvore real, com o bloco aplicado e revertido por cópia, **como está depois da `CON-T7`**; o executor mede o **antes** antes da primeira edição. 1. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Modelo das instâncias medidas:').Count ~~~~ 2. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'preço-Opus-equivalente, não custo real').Count ~~~~ 3. antes `1` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '| 3 | $2,8 | $2,4–$3,0 | 0 | 0 | adotada |').Count ~~~~ 4. antes `1` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'A forma efêmera fica adotada: a média ficou abaixo de $3,7, o piso medido da forma standby, com zero reprovações.').Count ~~~~ 5. antes `0` · depois `0` ~~~~ python .claude/tools/backlog.py check; $LASTEXITCODE ~~~~ 6. antes `0` · depois `0` ~~~~ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE ~~~~ 7. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — árvore real, acionamento 7 — e `277 passed` depois, com o bloco aplicado) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.forma da figura` — fatia da `OP-7` (`F-4` item 46): o veredito medido do piloto segue gravado na §11 da spec como `adotada`, e a subseção declara o modelo das instâncias e a unidade da comparação — Verificação 1 a 4

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T7`
- **Fundamento:** `DCS-4`, `DCS-7`, `DCS-23`, `DCS-32`; achado `AE-19`; laudo da `CON-T7` (aprovado 100, `escalar`).
- **Operação do modelo:** `OP-7` - OP-7: O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** documento de lastro (`docs/consultant-spec.md`, só o fim da subseção do veredito, item 46); sem código. `docs/DOC_MAP.md` não muda: a entrada da spec diz *"~480 linhas"* e o arquivo vai de 489 a 491 linhas.
- **Domínio:** **preço-Opus-equivalente** — custo obtido precificando os tokens medidos de uma instância pela tabela Opus da §11, qualquer que seja o modelo em que ela rodou; é a unidade da comparação entre formas, não o custo real da instância. Invariante: a tabela da subseção e a frase do veredito não mudam — a `CON-T8` lê a última linha da tabela.
- **Contratos/classes:** nenhuma assinatura de código; nenhuma linha de tabela muda.
- **Passos:** 1. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**. O arquivo termina em CRLF: a substituição literal preserva o final de linha do arquivo, e o parágrafo novo entra com o mesmo final de linha.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não tocar a tabela da subseção nem a frase do veredito; as linhas 3 e 4 da `Verificação` medem isso. - Não editar a §11 fora do fim do arquivo, nem as §§1-10. - Não corrigir as três contagens defasadas da spec (`DCS-2`) e não tocar `docs/DOC_MAP.md` (item 43, `CON-T6`, fechada).
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita lastro e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Fora do escopo desta tarefa:** a descrição pública da forma (`CON-T8`); a tabela e a frase do veredito (`CON-T7`, fechada).

## Execução

**Consumo:** 10 tool uses, 52.7 k tokens, 92.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
