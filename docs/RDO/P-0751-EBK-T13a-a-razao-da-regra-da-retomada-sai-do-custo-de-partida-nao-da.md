# RDO — P-0751 · EBK-T13a

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T13a` — A razão da regra da retomada sai do custo de partida, não da média
**Modelo:** Sonnet · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** refazer a comparação da `EBK-T13` separando o custo de partida do trabalho da rodada, publicá-la em `docs/CUSTO_DO_PICKUP.md` ao fim da seção *Retomada do planejador por mensagem* e aplicar a `GOVERNANCA.md` o texto que o resultado determina.

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md` - `GOVERNANCA.md`

**Verificação:** 1. `(Select-String -Path docs/CUSTO_DO_PICKUP.md -SimpleMatch 'Decomposição do custo de retomada').Count` — antes `0`, depois `1` 2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'mesmo supondo que ela recrie').Count` — antes `0`, depois `1` 3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'custou o mesmo ou mais').Count` — antes `1`, depois `0` 4. `(Select-String -Path GOVERNANCA.md -Pattern 'Rodada de replanejamento (retoma|abre instância fria)').Count` — antes `1`, depois `1` 5. `python -m pytest -q` → nenhuma falha; `passed` = o do despacho (nenhum teste lê os dois arquivos, medido por grep em `tests/`).

**Pronto quando:** `docs/CUSTO_DO_PICKUP.md` termina com a decomposição do passo 3 e o desfecho do passo 4, e `GOVERNANCA.md` carrega exatamente o texto que o desfecho determinou.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** corretivo da `EBK-T13`, pendência do laudo dela (`AE-5`, `DEB-12`), escrito pelo consultor no acionamento 7.
- **Operação do modelo:** `OP-13` - OP-13: O card que mede quanto custa retomar o planejador por mensagem sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Método de sondagem:** 1. **Corpus e segmentos:** os mesmos da `EBK-T13` (regra do `DEB-11`), com a sonda `%TEMP%\claude\estrutura_t13c.py`; nenhum texto de mensagem entra no contexto. 2. **Por segmento:** `n` = mensagens `assistant` de `message.id` distinto; contexto de uma mensagem = `input_tokens` + `cache_read_input_tokens` + `cache_creation_input_tokens` do `usage` dela. Base `b` = contexto da primeira mensagem da fria do mesmo agente; carregado `c` = contexto da primeira mensagem da retomada menos `b`; cache expirado = o `cache_creation_input_tokens` da primeira mensagem da retomada é maior ou igual a `c`. 3. **Partida, em dólares:** retomada = `c × (n × 0,5 + (5,75 se expirou, senão 0)) / 10^6`; fria mínima = `b × 5,75 / 10^6`; fria máxima = fria mínima + `c × 6,25 / 10^6` (a instância fria recria todo o contexto carregado). Por retomada: vence `retomada` se a partida dela é menor que a fria mínima, `fria` se é maior que a fria máxima, senão `indeterminado`. 4. **O que cada resultado dispara** (somas das seis retomadas): partida da retomada **maior** que a soma das frias máximas → o Texto novo 1 e o Texto novo 2 abaixo, como estão; **menor** que a soma das frias mínimas → a linha da regra sai do `GOVERNANCA.md` trocada pelo Texto novo A da `EBK-T13`, e o Texto novo 2 termina com "O **Texto novo A** substitui o B."; **entre as duas** → a linha da regra sai do `GOVERNANCA.md`, e o Texto novo 2 termina com "Não mensurável neste corpus; a regra sai do `GOVERNANCA.md`.".
- **Medido pelo consultor (2026-09-26, só chaves):** a tabela e as somas do Texto novo 2, com o primeiro desfecho do passo 4 (retomada $6,30 contra frias de $1,16 a $3,80); os "antes" da Verificação medidos na árvore, os "depois" numa cópia com os dois textos novos aplicados.
- **Não fazer:** não ler conteúdo de mensagem dos transcripts; não mudar a seção *Retomada do planejador por mensagem* acima do parágrafo **Resultado.**, nem ele; não mudar outra linha do `GOVERNANCA.md`.
- **Contingências:** - se a sonda der número diferente da tabela do Texto novo 2 em qualquer célula, ou outro desfecho do passo 4 → parar e sinalizar `blocked` razão `premissa`, citando a célula e os dois valores.

## Execução

**Consumo:** 13 tool uses, 62.1 k tokens, 150.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
