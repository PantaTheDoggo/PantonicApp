# RDO — P-0752 · FPU-T5b

# Humano

Tarefa "A medida guarda a cauda da saída, onde está o sumário" concluída em 2026-09-26.
O arquivo de medida passa a guardar o fim da saída de cada comando, onde está o resumo do resultado.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 7/13 tarefas concluídas; próxima: "O aviso de crença no ato de gravar plano ou diário".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T5b` — A medida guarda a cauda da saída, onde está o sumário
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `verificar_tarefa` de `.claude/tools/card_check.py`, o campo `saida` do registro de cada item passa de `saida.strip()[:400]` (cabeça) para `saida.strip()[-400:]` (cauda), nas duas formas (8.1 e inline): em item de pytest a cabeça é a barra de pontos e o sumário `N passed` fica fora do JSON (`AE-37`). O teto de 400 caracteres (DFP-6) não muda; a mensagem de `divergencia` (`[:200]`) não muda.

**Arquivos-alvo:** - `.claude/tools/card_check.py` - `tests/test_card_check.py`

**Verificação:** 1. `python -m pytest tests/test_card_check.py -q -k cauda_da_saida` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python -c "from pathlib import Path;print(Path('.claude/tools/card_check.py').read_text(encoding='utf-8').count('[:400]'))"` → `0` — antes `2`, depois `0`. 3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** retorno do executor.evidência de verificação — o JSON de medida guarda o sumário do comando — Verificação 1.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T5`
- **Operação do modelo:** `OP-5` - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Fundamento:** DFP-6, DFP-17, DFP-18, `AE-37`.
- **Passos:** 1. Trocar as duas atribuições `registro["saida"] = saida.strip()[:400]` por `saida.strip()[-400:]`. 2. Teste: TF `test_tf_gravar_guarda_a_cauda_da_saida(tmp_path, capsys)` — grava em `tmp_path` um plano mínimo com um card `ready` cuja Verificação é o item inline `` 1. `python -c "print('x'*500+'FIM')"` → `FIM` — antes `FIM`, depois `FIM` ``; roda `card_check.main` com `--root` = `_ROOT` e `--gravar`; o JSON tem `itens[0]["saida"]` terminando em `FIM` e com 400 caracteres. Medido pelo consultor em protótipo (acionamento 6): com o código de hoje o card fecha, a `saida` tem 400 caracteres e não termina em `FIM`.
- **Não fazer:** não mudar o teto de 400 nem a forma do JSON; não tocar `review_evidence.py`.
- **Contingências:** - se um teste existente afirmar a cabeça da `saida` → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): passa a afirmar a cauda; registrar em `pendencia=`.
- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** registro['saida'] = saida.strip()[-400:] nas duas formas (.claude/tools/card_check.py:408 e :462); TF test_tf_gravar_guarda_a_cauda_da_saida em tests/test_card_check.py:308 - **Contrato:** o JSON de medida guarda os ultimos 400 caracteres da saida (sumario do pytest incluso); forma do JSON e teto inalterados - **Não refazer:** cauda da saida ja paga - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, veredito aprovado 100%

## Execução

**Consumo:** 22 tool uses, 60.8 k tokens, 157.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O teste novo exercita só o ramo inline; o ramo da forma A (bloco cercado) foi exercitado na revisão num plano temporário fora do repositório — saída de 400 caracteres terminando em FIM, exit 0 — e a Verificação 2 (contagem de '[:400]' = 0) tranca as duas atribuições por inspeção. O JSON de medida do próprio executor já mostra o efeito: o item de suíte inteira guarda '411 passed in 34.18s' na cauda.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item" e vai pegar a tarefa "A medida guarda a cauda da saída, onde está o sumário".
Tarefa "A medida guarda a cauda da saída, onde está o sumário". Passo: conferir os gates e preparar o despacho.
Tarefa "A medida guarda a cauda da saída, onde está o sumário": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "A medida guarda a cauda da saída, onde está o sumário" e vai executar: em `verificar_tarefa` de `.claude/tools/card_check.py`, o campo `saida` do registro de cada item passa de `saida.strip()[:400]` (cabeça) para `saida.strip()[-400:]` (cauda), nas duas formas (8.1 e inline): em item de pytest a cabeça é a ba…
Agente executor devolveu a tarefa "A medida guarda a cauda da saída, onde está o sumário": review — sem pendência.
Tarefa "A medida guarda a cauda da saída, onde está o sumário": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A medida guarda a cauda da saída, onde está o sumário" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A medida guarda a cauda da saída, onde está o sumário": aprovado 100%, bloqueante nenhuma.
