# RDO — P-0752 · FPU-T4

# Humano

Tarefa "O aviso de crença no ato de gravar plano ou diário" concluída em 2026-09-26.
Um gancho novo avisa, na hora de gravar plano ou diário, quando um número de aceite entra no texto sem o comando que o mede.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 8/13 tarefas concluídas; próxima: "O dossiê de despacho carrega os achados roteados ao card".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T4` — O aviso de crença no ato de gravar plano ou diário
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `python .claude/tools/crenca_hook.py` (novo gancho `PreToolUse`, matcher `Write|Edit`) lê o payload em stdin e, quando o `file_path` está em `docs/plans/` ou é `docs/DIARIO_DE_OBRAS.md`, conta no conteúdo novo (`content` ou `new_string`) os literais numéricos de aceite sem comando e devolve `{"systemMessage": "<n> número(s) de aceite sem comando no texto novo: número sem comando é crença — medir antes de gravar"}`; zero → sem saída; qualquer exceção → exit 0 sem saída (DFP-5).

**Arquivos-alvo:** - `.claude/tools/crenca_hook.py` (novo) - `tests/test_crenca_hook.py` (novo) - `.claude/projecoes.json` — `alvos.projeto.chaves.hooks.PreToolUse`: acrescentar `{"matcher": "Write|Edit", "hooks": [{"type": "command", "command": "python {KIT_ROOT}/tools/crenca_hook.py"}]}` - `tests/test_materializar.py` (se houver teste que conta os ganchos projetados)

**Verificação:** 1. `python -m pytest tests/test_crenca_hook.py tests/test_materializar.py -q` → verde — antes `exit 4`, depois `exit 0` (antes o arquivo de teste não existe, erro de coleta; depois 24 testes, 4 novos sobre os 20 de `test_materializar.py`). 2. `python -c "from pathlib import Path;print(Path('.claude/projecoes.json').read_text(encoding='utf-8').count('crenca_hook.py'))"` → `1` — antes `0`, depois `1`. 3. `python .claude/tools/materializar.py check` → exit 0 — antes `exit 0`, depois `exit 0` (trava). 4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (a suíte ganha os 4 testes novos; `409 passed` no acionamento 6 do consultor).

**Pronto quando:** card.números de aceite — número gravado sem comando recebe aviso no ato de gravar — Verificação 1; régua executável.conferências — o gancho está projetado — Verificações 2 e 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-4` - OP-4: Um gancho avisa, no ato de gravar plano ou diário, todo número de aceite que chega sem comando. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Fundamento:** DFP-5, F-9, causa 1 de F-10.
- **Contratos/classes:** `contar_crencas(texto: str) -> int` — literal numérico de aceite é: `\b\d+ passed\b`, `antes \`?\d+\`?`, `depois \`?\d+\`?`, `Medido antes: \d+`, `` `[^`]+:\d+` `` (âncora de linha) — descontados os que estão na mesma linha de um comando (linha contém `` `python `` ou `` `pwsh `` ou está dentro de bloco cercado) ou de um literal logo após a âncora (DFP-4). `main(argv=None, entrada=None) -> int` no padrão de `progresso_hook.main`.
- **Passos:** 1. Escrever o gancho com `_forcar_utf8`, leitura de stdin, filtro de caminho, `contar_crencas` e a saída JSON em stdout. 2. Testes: TF `test_tf_numero_sem_comando_avisa` (conteúdo com `410 passed` em prosa → `systemMessage` com `1 número`); TF `test_tf_numero_na_linha_do_comando_nao_avisa` (`` 1. `python -m pytest -q` → verde — antes `397 passed` `` → sem saída); TF `test_tf_fora_de_docs_plans_nao_avisa` (`file_path` em `src/` → sem saída); TR `test_tr_payload_invalido_sai_zero` (stdin vazio → exit 0, sem saída). 3. Acrescentar a projeção em `projecoes.json`; `python .claude/tools/materializar.py check` sai 0.
- **Não fazer:** não bloquear (`decision: block`) em caso nenhum; não escrever em `settings.json` (I-1); não tocar `progresso_hook.py` nem `ocupacao.py`.
- **Contingências:** - se `materializar.py check` recusar o matcher `Write|Edit` → usar matcher `.*` e filtrar por `tool_name` dentro do gancho; registrar em `pendencia=`. - se `tests/test_materializar.py` fixar o número de ganchos `PreToolUse` em `2` → o teste que fixa o número é alvo da tarefa (`DM-33` do `P-0740`): passa a `3`, com a asserção de que o terceiro é o `crenca_hook.py`.
- **Handover:** 2026-09-26 · para `FPU-T6` - **Entregue:** gancho PreToolUse .claude/tools/crenca_hook.py (contar_crencas :42, _elegivel :63, main :68), projetado em .claude/projecoes.json (matcher Write|Edit, 3o PreToolUse); tests/test_crenca_hook.py (4 testes) - **Contrato:** Write/Edit em docs/plans/ ou docs/DIARIO_DE_OBRAS.md com numero de aceite sem comando recebe systemMessage de aviso, nunca bloqueio; excecao sai 0 sem saida; o gancho ja esta vivo no .claude/settings.json do projeto (o teste de apply real de test_materializar.py o materializou) - **Não refazer:** gancho e projecao ja pagos - **Pendente:** contagem por casamento de padrao infla o numero exibido (um literal casa dois padroes); I-1 inalcancavel enquanto test_materializar roda apply real
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, veredito aprovado 100%

## Execução

**Consumo:** 31 tool uses, 90.2 k tokens, 274.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "A medida guarda a cauda da saída, onde está o sumário" e vai pegar a tarefa "O aviso de crença no ato de gravar plano ou diário".
Tarefa "O aviso de crença no ato de gravar plano ou diário". Passo: conferir os gates e preparar o despacho.
Tarefa "O aviso de crença no ato de gravar plano ou diário": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O aviso de crença no ato de gravar plano ou diário" e vai executar: `python .claude/tools/crenca_hook.py` (novo gancho `PreToolUse`, matcher `Write|Edit`) lê o payload em stdin e, quando o `file_path` está em `docs/plans/` ou é `docs/DIARIO_DE_OBRAS.md`, conta no conteúdo novo (`content` ou `new_string`) o…
Agente executor devolveu a tarefa "O aviso de crença no ato de gravar plano ou diário": review — sem pendência.
Tarefa "O aviso de crença no ato de gravar plano ou diário": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O aviso de crença no ato de gravar plano ou diário" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O aviso de crença no ato de gravar plano ou diário": aprovado 100%, bloqueante nenhuma.
