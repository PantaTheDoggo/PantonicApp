# RDO — P-0747 · CON-T6

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T6` — A especificação vira lastro medido
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística.

**Arquivos-alvo:** - `docs/consultant-spec.md` - `docs/DOC_MAP.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição. 1. antes `1` · depois `0` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Promovê-lo a doutrina é').Count ~~~~ 2. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern 'Lastro medido, não fonte normativa.').Count ~~~~ 3. antes `1` · depois `0` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '**sem rota decidida aqui**').Count ~~~~ 4. antes `0` · depois `7` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '`P-0747` `DCS-').Count ~~~~ 5. antes `1` · depois `0` ~~~~ (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern '**Não é doutrina**').Count ~~~~ 6. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern '## docs/ACIONAMENTOS_CONSULTOR.tsv').Count ~~~~ 7. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern '## docs/plans/_CENARIO-<plano>.md').Count ~~~~ 8. antes `1` · depois `0` ~~~~ (Select-String -Path 'docs/DOC_MAP.md' -SimpleMatch -CaseSensitive -Pattern 'as cinco matérias sem rota decidida').Count ~~~~ 9. o total de `passed` não é menor que o medido no despacho e não há `failed` (referência histórica datada: `277 passed` antes e `277 passed` depois, no ensaio) ~~~~ python -m pytest -q ~~~~

**Pronto quando:** - `consultor.estatuto na doutrina` — papel de doutrina em duas residências — a linha na matriz de `GOVERNANCA.md` §3 e a definição de conduta sem estatuto provisório —; a spec permanece como lastro medido e não normativo, com o estatuto apontando para as duas e o índice de documentos dizendo o mesmo — Verificação 1, 2, 5 - `consultor.lacunas deixadas pela especificação` — as sete fechadas: cinco por norma — handover e forma pelo cenário persistido, estatística pela residência estruturada, autoria de card novo pela fronteira com o planejador, disciplina de saída por regra do agente — e duas por residência nomeada — não-acionamento no `TK-55`, poluição pela regra geral do agente —; cada item da §10 da spec aponta para o que o fecha — Verificação 3, 4, 6, 7, 8

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T5`
- **Fundamento:** `DCS-2`, `DCS-4`, `DCS-6`..`DCS-10`; fatos `F-4` itens 42 e 43, `F-9`.
- **Operação do modelo:** `OP-6` - OP-6: O redator da especificação a converte em lastro medido: o estatuto dela passa a apontar para a norma e para a definição de conduta, cada lacuna que ela deixava aberta ganha o ponteiro para a regra que a fecha ou para a residência que a recebe, e o índice de documentos deixa de descrevê-la como a única fonte da figura e passa a indexar o cenário e a estatística. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`)
- **Camada e fronteira:** documentação — `docs/consultant-spec.md` (estatuto e §10) e `docs/DOC_MAP.md`; sem código.
- **Domínio:** **lacunas** — as sete da §10 da spec (`F-9`), cada uma com o ponteiro para a regra ou residência que a fecha.
- **Contratos/classes:** nenhuma assinatura de código.
- **Passos:** 1. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 1** pelo bloco **Texto novo 1**. 2. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**. 3. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 3** pelo bloco **Texto novo 3**. 4. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 4** pelo bloco **Texto novo 4**. 5. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 5** pelo bloco **Texto novo 5**. 6. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 6** pelo bloco **Texto novo 6**. 7. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 7** pelo bloco **Texto novo 7**. 8. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 8** pelo bloco **Texto novo 8**. 9. Em `docs/consultant-spec.md`, substitua o bloco **Texto atual 9** pelo bloco **Texto novo 9**. 10. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 10** pelo bloco **Texto novo 10**. 11. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 11** pelo bloco **Texto novo 11**. 12. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 12** pelo bloco **Texto novo 12**. 13. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 13** pelo bloco **Texto novo 13**. 14. Em `docs/DOC_MAP.md`, substitua o bloco **Texto atual 14** pelo bloco **Texto novo 14**.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não tocar a §11 da spec (`:422` em diante): é o item 46, da `CON-T7`. - Não corrigir as três contagens defasadas da nota de leitura (`:12-30`) nem as tabelas das §§1-9 (`DCS-2`).
- **Contingências:** - se um bloco **Texto atual** deste card não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco - se o valor **antes** de qualquer linha de `Verificação`, medido antes da primeira edição, diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido - se o valor **depois** de uma linha de `Verificação` diferir do publicado → reler o bloco **Texto novo** correspondente, corrigir a cópia e rodar de novo; persistindo a diferença → parar e sinalizar `blocked` razão `premissa` - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e não código. A guarda é a suíte inteira, `python -m pytest -q`; quando o card toca arquivo preso por literal (`F-15`), também `tests/test_doutrina_unidade.py`.
- **Fora do escopo desta tarefa:** o veredito do piloto na §11 (`CON-T7`). a estrutura, não. a estrutura, não. → fechado: `docs/ACIONAMENTOS_CONSULTOR.tsv`, uma linha por acionamento (`P-0747` `DCS-8`). continua sem regra que o autorize ou o proíba. continua sem regra que o autorize ou o proíba. → fechado: o card corretivo `T<n>a` da mesma operação é do consultor, e operação nova vai ao modelador (`GOVERNANCA.md` §3, linha *Consultoria*; `P-0747` `DCS-4`). saída; nenhum critério de entrada foi exercido. saída; nenhum critério de entrada foi exercido. → residência nomeada: `TK-55`, decidido sobre a estatística de `docs/ACIONAMENTOS_CONSULTOR.tsv` (`P-0747` `DCS-10`). exercitado. exercitado. → residência nomeada: a regra geral, na seção *Coesão do seu contexto* de `.claude/agents/pantonic-consultant.md` (`P-0747` `DCS-10`). decide a forma **por piloto medido**, não por argumento. decide a forma **por piloto medido**, não por argumento. → fechado: efêmera com cenário persistido, em piloto medido na §11 (`P-0747` `DCS-6`, `DCS-7`). hoje é recomendação, não regra. hoje é recomendação, não regra. → fechado: regra do agente, item 4 de *O que você faz* (`P-0747` `DCS-9`).

## Execução

**Consumo:** 25 tool uses, 67.7 k tokens, 128.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
