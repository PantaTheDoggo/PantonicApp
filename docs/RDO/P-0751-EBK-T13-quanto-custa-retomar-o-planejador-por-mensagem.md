# RDO — P-0751 · EBK-T13

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T13` — Quanto custa retomar o planejador por mensagem
**Modelo:** Sonnet · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** medir, nos transcripts do `pantonic-planner` da sessão de planejamento do `P-0747`, o custo de cada retomada por mensagem e o de cada invocação fria do mesmo papel; publicar a medida em `docs/CUSTO_DO_PICKUP.md` e aplicar a `GOVERNANCA.md` a regra que o resultado determina.

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md` - `GOVERNANCA.md`

**Verificação:** 1. `(Select-String -Path docs/CUSTO_DO_PICKUP.md -SimpleMatch 'Retomada do planejador por mensagem × invocação fria').Count` — antes `0`, depois `1` 2. `(Select-String -Path GOVERNANCA.md -Pattern 'Rodada de replanejamento (retoma|abre instância fria)').Count` — antes `0`, depois `1` (ou `0`, com o desfecho "não mensurável" publicado) 3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** `docs/CUSTO_DO_PICKUP.md` tem uma seção nova, com o próximo número da sequência, titulada `Retomada do planejador por mensagem × invocação fria`, com a data, o corpus, a regra de enumeração dos segmentos, o agregado do passo 4 e o desfecho do passo 5; e `GOVERNANCA.md` carrega exatamente o texto que o desfecho determinou.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-72c` do diário de obras, seção `## TK-72`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-13` - OP-13: O card que mede quanto custa retomar o planejador por mensagem sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Fundamento:** pacote 8 do `TK-72`.
- **Método de sondagem:** 1. **Corpus fechado:** os arquivos `agent-*.meta.json` sob `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\*\subagents\` com `agentType` igual a `pantonic-planner` e cujo `.jsonl` irmão cita `P-0747` na primeira linha. 2. **Segmento:** cada trecho do `.jsonl` que começa numa mensagem do tipo `user` vinda de fora do agente (a invocação ou uma retomada por mensagem) e vai até a próxima. O primeiro segmento de cada agente é a **invocação fria**; os seguintes são **retomadas**. Regra de enumeração (`DEB-11`), só por chaves: abre segmento a linha 0 (a invocação) e toda entrada `type=user` com `message.content` do tipo texto e `origin.kind == "coordinator"` (a retomada por mensagem, que o transcript grava com `isMeta=true`). Entrada `isMeta=true` sem `origin` (a linha 1, injetada pelo harness na mesma invocação) não abre segmento e fica no segmento em curso; `promptId` não delimita segmento. Medido pelo consultor: 2 frias e 6 retomadas, nenhuma fria com custo zero. 3. **Métrica por segmento:** soma de `input_tokens`, `output_tokens`, `cache_read_input_tokens` e `cache_creation_input_tokens` das mensagens `assistant` com `message.id` distinto, e o custo com os preços da sonda `%TEMP%\claude\sonda_p0747.py` (5, 25, 0,5 e 6,25 dólares por milhão, na ordem); mais o intervalo, em minutos, desde o fim do segmento anterior. Adaptar a sonda trocando `pantonic-consultant` por `pantonic-planner`, o filtro por `P-0747` e somando por segmento. Nenhum texto de mensagem entra no contexto: só chaves, contagens e datas. 4. **Agregado que volta:** no máximo 20 linhas — por grupo (fria, retomada): `n`, média, mínimo e máximo do custo, e o intervalo de cada retomada; e, por segmento, o número de mensagens `assistant` de `message.id` distinto (o custo do segmento soma o trabalho feito nele, e a seção publicada mostra esse volume ao lado da média). 5. **O que cada resultado dispara:** média das retomadas **menor** que a das invocações frias → entra em `GOVERNANCA.md` o **Texto novo A**; **igual ou maior** → o **Texto novo B**; nenhuma retomada no corpus → nenhum dos dois, e a seção publica "não mensurável neste corpus".
- **Não fazer:** não ler conteúdo de mensagem dos transcripts; não medir outro papel; não mudar o `pantonic-planner`.
- **Contingências:** - se a sonda não existir no despacho → escrever a soma direto sobre o corpus do passo 1, com as mesmas chaves e preços. - se a regra do passo 2 der outro número que 2 frias e 6 retomadas, ou uma fria de custo zero → parar e sinalizar `blocked` razão `premissa`, citando a contagem.
- **Notas de execução:** - 2026-09-26 `ready` — consultor acionamento 6: DEB-11, segmento por origin.kind=coordinator; agregado com mensagens por segmento; Texto B sem a causa

## Execução

**Consumo:** 19 tool uses, 66.9 k tokens, 166.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: A regra 'Rodada de replanejamento abre instância fria do planejador', que o EBK-T13 pôs na GOVERNANCA.md §3 como o card mandava, se apoia numa comparação de médias sem normalizar pelo volume. Normalizada por mensagem, a comparação se inverte em 5 das 6 retomadas. A triagem do consultor decide se a regra fica ou se abre tíquete para medir de novo.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
