# RDO — P-0740 · LM-T2f

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T2f` — O teste órfão da dedupe por `message.id`
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — a suíte deixa de afirmar, por nome e por docstring, um mecanismo que a `LM-T2b` removeu.

**Arquivos-alvo:** - `tests/test_telemetria_hook.py`

**Verificação:** (`DM-12`/`DM-24`: toda baseline abaixo foi rodada pelo consultor no `ESC-12`, com `-CaseSensitive` onde a caixa discrimina, `AE-25`) 1. `python -m pytest tests/test_telemetria_hook.py -q` → **`9 passed`**. **Medido antes: `10 passed`**. 2. `python -m pytest tests/ -q` → **`174 passed`**. **Medido antes: `175 passed`**, e o valor depois foi medido **de fato**, com `python -m pytest tests/ -q --deselect "tests/test_telemetria_hook.py::test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas"` → `174 passed, 1 deselected`, e não por subtração. 3. ``` pwsh -NoProfile -Command "(Select-String -Path tests/test_telemetria_hook.py -Pattern 'deduplica_por_message_id' -SimpleMatch -CaseSensitive | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. O nome não aparece em nenhum outro arquivo do kit (medido: 1 ocorrência no repositório, esta).

**Pronto quando:** o módulo sai `9 passed`, a suíte sai `174 passed`, e `deduplica_por_message_id` não aparece mais no arquivo.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (2026-09-19) — card novo do `ESC-12` (2026-09-19), residência única do `AE-27` item 1. **Fora do caminho crítico**: não precede nem sucede tarefa nenhuma, e roda em qualquer janela.
- **Esforço:** low
- **Depende de:** `LM-T2b` (fechada — é a entrega dela que tornou o teste órfão). Nenhuma tarefa depende desta.
- **O defeito, medido no `ESC-12`:** `test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas` (`:107`) e `test_tr_calcular_consumo_mesma_mensagem_duas_entradas_nao_dobra` (`:181`) têm corpo **byte a byte idêntico** — mesmo `usage` (10/8779/0/74), mesmas duas entradas com `message_id="msg_calibracao"`, mesmas asserções (`tokens_k == 8863/1000`, `tool_uses == 0`). O primeiro nomeia e descreve a **dedupe por `message.id`**, mecanismo que a `LM-T2b` removeu; o segundo descreve o **mesmo caso** sob a fórmula nova, com a prosa correta. O caso **não** se perde: ele fica no segundo.
- **Passos:** 1. Apagar a função `test_tr_calcular_consumo_deduplica_por_message_id_uma_mensagem_duas_entradas` **inteira** — do `def` até a última asserção —, junto com as linhas em branco que a separavam da função seguinte, deixando as duas linhas em branco de separação entre as funções que ficarem vizinhas. Nada mais do arquivo muda: o teste que **fica** é o `:181`, e ele **não** se renomeia.
- **Testes:** nenhum teste novo — esta tarefa **remove** duplicata. É a única tarefa do plano autorizada a **reduzir** o total da suíte, e a redução é de exatamente **1** (`DM-23` continua valendo para todas as outras).
- **Restrições desta tarefa:** o teste `:181` fica **literal** — nome, docstring e corpo. Nenhum outro teste é tocado. Nenhum arquivo de `.claude/` é tocado.
- **Não fazer:** não "fundir" os dois testes; não renomear o que fica; não tocar `.claude/tools/telemetria_hook.py`; não commitar.
- **Contingências:** 1. se o corpo dos dois testes não for idêntico no ato do despacho (arquivo mexido desde a medida) → parar e sinalizar `blocked` razão `premissa`, citando a diferença encontrada.

## Execução

**Consumo:** 5 tool uses, 44.4 k tokens, 37.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Tarefa de remocao pura fechada em 5 tool_uses / 44.4 tk. O card de um so passo com o alvo nomeado por identificador exato (funcao a apagar, funcao que fica, literal a sumir) executa sem nenhum grau de liberdade: nao houve decisao do executor a julgar. O unico atrito foi a baseline absoluta envelhecida (174/175 no card contra 188 medidos), absorvido no despacho pela re-derivacao e nao pela execucao - evidencia a favor do piso-como-relacao dos criterios (x)/(xiii) da rubrica.

## Fechamento

**Desdobramento:** aprovado
