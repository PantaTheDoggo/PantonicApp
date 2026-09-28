# RDO — P-0747 · CON-T2b

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T2b` — Corretivo da OP-2: o agente nomeia a recusa do impedimento improcedente na rota resolve
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CON-T2` e da `CON-T2a` (`DCS-35`, `AE-22`, ato do dono de 2026-09-23): o bullet `rota=resolve` do item 2 da definição de conduta do consultor passa a nomear o desfecho **impedimento improcedente** — o executor parou sem razão e o card é executável como está — com as três amarras: a razão vai à coluna `motivo` da estatística; o card volta a `ready` com ao menos uma linha nova (a contingência ou o fato que responde à dúvida do executor), porque recusar sem tocar o card só reproduz a parada num executor frio; o redespacho não consome a retentativa.

**Arquivos-alvo:** - `.claude/agents/pantonic-consultant.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-23 pelo consultor (acionamento 10) na árvore real, com o bloco aplicado e revertido por hash, **como está depois da `CON-T8a`**; o executor mede o **antes** antes da primeira edição. 1. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'recusar o impedimento como improcedente').Count ~~~~ 2. antes `0` · depois `1` ~~~~ (Select-String -Path '.claude/agents/pantonic-consultant.md' -SimpleMatch -CaseSensitive -Pattern 'não consome a retentativa').Count ~~~~ 3. antes `0` · depois `0` ~~~~ python -c "import yaml; t=open('.claude/agents/pantonic-consultant.md',encoding='utf-8').read(); yaml.safe_load(t.split('---')[1])"; $LASTEXITCODE ~~~~ 4. antes `0` · depois `0` ~~~~ python .claude/tools/backlog.py check; $LASTEXITCODE ~~~~ 5. antes `0` · depois `0` ~~~~ python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md; $LASTEXITCODE ~~~~ 6. antes `0` · depois `0` ~~~~ pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE ~~~~ 7. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes — laudo da `CON-T8a`, mesma árvore — e `277 passed` depois, no ensaio de 2026-09-23 do acionamento 10) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.fronteira com o planejador` — fatia da `OP-2` (`F-4` item 24): o consultor fecha o técnico e o tático, e entre os desfechos da rota `resolve` está recusar o impedimento improcedente com as três amarras de `DCS-35` — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T8a`
- **Fundamento:** `DCS-4`, `DCS-35`; achado `AE-22`; ato do dono transcrito em `DCS-35`.
- **Operação do modelo:** `OP-2` - OP-2: O autor de papéis reescreve a definição de conduta do consultor sobre a norma nova: tira dela o estatuto provisório, faz qualquer das três razões de parada acioná-lo, dá a ele a rota que devolve, os deveres de validar a emenda do modelo no marco e de emiti-la quando a resolução muda o que o plano entrega, a linha de estatística que ele apensa a cada acionamento e a saída curta por edição mínima. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); parada de executor — nenhuma operação altera uma parada. O que se observa nela, antes e depois, é o caminho: quem a recebe, quem decide a rota e onde isso fica registrado. As paradas do `P-0745` e do `P-0746` (`F-8`) são o retrato do antes; o depois são as paradas da janela de execução deste plano, lidas no arquivo de estatística de `DCS-8` a partir do aceite da `OP-2`; planejador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 13, 19, 20 e 25 — é a fronteira do consultor e nada além: a rodada de replanejamento chega pela rota `planejador` da triagem, só quando emenda aceita cria ou remove operação ou quando a premissa cai inteira (`superseded`), e o corretivo `T<n>a` da mesma operação, com o id apensado à lista `tarefas:`, passa a ser também ato do consultor (`DCS-4`). O que `DCS-18` deixa com o planejamento continua com ele. Alterar outra conduta do planejador é colateral e se escala; modelador — não se transforma neste plano. O que os cards escrevem nas residências dele — `F-4` itens 26, 27 e 28 — é a fronteira do consultor e nada além: o consultor é nomeado como quem origina o dossiê de `emenda` e como quem apensa o id do corretivo à lista `tarefas:`; quem despacha continua sendo quem conduz a sessão (`I-2`). Os literais que a guarda executável prende no arquivo dele (`F-15`) ficam. O instrumento do modelo e seus testes não se tocam
- **Camada e fronteira:** definição de agente — `.claude/agents/pantonic-consultant.md`, só o bullet `rota=resolve` do item 2 (`:25`), do item 24 de `F-4`; sem código.
- **Domínio:** **impedimento improcedente** — desfecho da `rota=resolve` em que o consultor recusa a parada porque o card era executável como está (`DCS-35`). **Linha nova** — a contingência ou o fato que responde à dúvida do executor, gravada no card antes do redespacho; sem ela a recusa não é permitida. **Retentativa** — o redespacho por recusa não a consome.
- **Contratos/classes:** nenhuma assinatura de código; o front matter (`:1-6`) não muda, e a linha 3 da `Verificação` mede que ele continua a parsear (`AE-20`).
- **Passos:** 1. Em `.claude/agents/pantonic-consultant.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar a `description` (item 47, `OP-8`) nem as linhas de forma (item 44, `OP-4`). - Nenhum agente aciona outro: o redespacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não tocar a skill do loop: é da `CON-T3d` (`OP-3`). - Não tocar os bullets `rota=modelador` e `rota=planejador` (`:26-27`) nem a frase de abertura do item 2 (`:24`).
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`.
- **Fora do escopo desta tarefa:** a skill do loop (`CON-T3d`); a `## 1A` (modelador, dossiê de emenda de `DCS-35`). - `rota=resolve` — a questão é operacional, técnica ou tática: você a fecha sozinho, e o dono não valida (ato do dono de 2026-09-22: *"Eu não vou validar a decisão dele para questões técnicas e táticas."*). - `rota=resolve` — a questão é operacional, técnica ou tática: você a fecha sozinho, e o dono não valida (ato do dono de 2026-09-22: *"Eu não vou validar a decisão dele para questões técnicas e táticas."*). Um dos desfechos é **recusar o impedimento como improcedente** — o executor parou sem razão e o card é executável como está (`DCS-35` do `P-0747`), com três amarras: você declara a improcedência com a razão, que vai à coluna `motivo` da estatística; devolve o card a `ready` com **ao menos uma linha nova** — a contingência ou o fato que responde à dúvida do executor —, porque recusar sem tocar o card só reproduz a parada num executor frio; e o redespacho **não consome a retentativa**.

## Execução

**Consumo:** 11 tool uses, 60.1 k tokens, 67.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
