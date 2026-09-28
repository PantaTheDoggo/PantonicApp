# RDO — P-0752 · FPU-T4a

# Humano

Tarefa "O aviso de crença conta uma vez o literal que casa dois padrões" concluída em 2026-09-26.
O aviso de número sem comando passa a contar uma vez só o número que casa mais de um padrão.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 11/15 tarefas concluídas; próxima: "As armadilhas de ferramenta medidas ganham um arquivo só".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T4a` — O aviso de crença conta uma vez o literal que casa dois padrões
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `contar_crencas` de `.claude/tools/crenca_hook.py`, os casamentos de todos os padrões numa linha viram trechos `(m.start(), m.end())`; trechos que se sobrepõem formam um grupo, e a linha soma um por grupo, não um por casamento (`AE-44`): o texto `antes`, crase, `397 passed`, crase, `, depois`, crase, `401 passed`, crase conta `2`, não `4`. Os descontos de hoje (linha de comando, bloco cercado, âncora com literal logo depois) não mudam; âncora descontada não entra nos trechos.

**Arquivos-alvo:** - `.claude/tools/crenca_hook.py:55` — `for padrao in _PADROES:` - `tests/test_crenca_hook.py`

**Verificação:** 1. `python -m pytest tests/test_crenca_hook.py -q -k sobrepostos` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python -c "import sys;sys.path.insert(0,'.claude/tools');import crenca_hook as c;q=chr(96);print(c.contar_crencas('antes '+q+'397 passed'+q+', depois '+q+'401 passed'+q))"` → `2` — antes `4`, depois `2`. 3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** card.números de aceite — cada literal sem comando conta uma vez no aviso — Verificações 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T4`
- **Operação do modelo:** `OP-4` - OP-4: Um gancho avisa, no ato de gravar plano ou diário, todo número de aceite que chega sem comando. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Fundamento:** DFP-5, DFP-19, `AE-44`.
- **Passos:** 1. No laço de `contar_crencas`, trocar o `total += 1` por casamento por uma lista de trechos da linha; depois do laço dos padrões, ordenar os trechos e somar um a `total` sempre que o início do trecho for maior ou igual ao maior fim já visto na linha. 2. Teste: TF `test_tf_literais_sobrepostos_contam_uma_vez` em `tests/test_crenca_hook.py` (via `_load_crenca_hook()`): `contar_crencas` do texto do Objetivo devolve `2`. Medido pelo consultor em protótipo (acionamento 7): hoje devolve `4`; com o Passo 1, `2`, os quatro testes existentes seguem verdes e `410 passed` em prosa segue contando `1`.
- **Não fazer:** não mudar os padrões nem os descontos; não bloquear (`decision: block`); não tocar `projecoes.json` nem `settings.json`.
- **Contingências:** - se um teste existente afirmar a contagem por casamento → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): passa a afirmar a contagem por grupo; registrar em `pendencia=`.
- **Handover:** 2026-09-26 · para `FPU-T7` - **Entregue:** contar_crencas (.claude/tools/crenca_hook.py:42) conta uma vez cada grupo de trechos sobrepostos dos padroes (_PADROES, :37); TF test_tf_literais_sobrepostos_contam_uma_vez em tests/test_crenca_hook.py:85 - **Contrato:** 'antes `397 passed`, depois `401 passed`' conta 2, nao 4; o aviso segue so avisando, nunca bloqueia - **Não refazer:** regra de contagem ja paga - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, veredito aprovado 100%

## Execução

**Consumo:** 12 tool uses, 56.5 k tokens, 155.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

A secao Escopo do dossie de evidencia listou 31 arquivos fora dos alvos e sem atribuicao; todos eram '??' anteriores ao despacho (caso conhecido AE-35 / TK-84a). A reconciliacao por mtime contra o commit de recorte cd90fc6 (11:37:45) mostrou que so os dois alvos (crenca_hook.py 11:38, test_crenca_hook.py 11:39) mudaram depois dele, mais o registro da orquestracao (medida, telemetria, diario, plano). Como os dois alvos sao '??' desde a FPU-T4, o 'diff' colado e o arquivo inteiro: o delta real da FPU-T4a (lista de trechos e soma por grupo em contar_crencas) so se le no laco, e nao num hunk. O exercicio ponta a ponta confirmou a contagem por grupo em dez casos (prosa, antes/depois com e sem passed, Medido antes, ancora com e sem literal, linha de comando, bloco cercado, duas linhas, casamentos disjuntos na mesma linha) e o gancho pela linha de comando com payload real: aviso '2', exit 0.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta" e vai pegar a tarefa "O aviso de crença conta uma vez o literal que casa dois padrões".
Tarefa "O aviso de crença conta uma vez o literal que casa dois padrões". Passo: conferir os gates e preparar o despacho.
Tarefa "O aviso de crença conta uma vez o literal que casa dois padrões": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O aviso de crença conta uma vez o literal que casa dois padrões" e vai executar: em `contar_crencas` de `.claude/tools/crenca_hook.py`, os casamentos de todos os padrões numa linha viram trechos `(m.start(), m.end())`; trechos que se sobrepõem formam um grupo, e a linha soma um por grupo, não um por casamento (`AE-44`)…
Agente executor devolveu a tarefa "O aviso de crença conta uma vez o literal que casa dois padrões": review — sem pendência.
Tarefa "O aviso de crença conta uma vez o literal que casa dois padrões": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O aviso de crença conta uma vez o literal que casa dois padrões" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O aviso de crença conta uma vez o literal que casa dois padrões": aprovado 100%, bloqueante nenhuma.
