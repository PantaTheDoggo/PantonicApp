# RDO — P-0752 · FPU-T1a

# Humano

Tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item" concluída em 2026-09-26.
Um teste passa a garantir que um número seguido de ponto no meio da prosa de uma verificação não vira item fantasma.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 6/13 tarefas concluídas; próxima: "A medida guarda a cauda da saída, onde está o sumário".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T1a` — Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a fixture `tests/fixtures/card_check/plano-corpus.md` ganha o card `CX-T5`, cuja Verificação tem dois itens e a linha de continuação do item 1 traz prosa com `1.` e `2.` fora do início de linha; um TF novo prova que `card_check.verificar_tarefa` reconhece exatamente dois itens e fecha. É o caso do fantasma do `AE-33` do `P-0740`, que o TF `test_tf_marcador_so_no_inicio_de_linha` (`CX-T4`, prosa noutro campo) não discrimina (`AE-34`). Só teste e fixture: o `card_check.py` já se comporta certo.

**Arquivos-alvo:** - `tests/fixtures/card_check/plano-corpus.md` - `tests/test_card_check.py`

**Verificação:** 1. `python -m pytest tests/test_card_check.py -q -k prosa_na_continuacao` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T5` → `card_check: OK` — antes `exit 1`, depois `exit 0` (antes `CX-T5` não encontrada). 3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** régua executável.conferências — o marcador de item só no início de linha está trancado por teste que falharia sobre o texto achatado — Verificações 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-1` - OP-1: O gate do card passa a ler a forma de Verificação que o corpus vivo usa, a rodar cada comando e a comparar o valor do mundo em que o card está. - precisa de: card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Fundamento:** DFP-3, DFP-18, `AE-34`.
- **Passos:** 1. Fixture: depois do `CX-T4`, o card `CX-T5` no mesmo nível de cabeçalho dos vizinhos, título `CX-T5 — Card inline com prosa N. na continuação do item de Verificação [Sonnet · classe mecanica]`, com `Status` `ready`, `Objetivo`, `Entregável` (`nenhum — fixture sintética, não é card vivo de plano.`), `Pronto quando` e esta Verificação, três linhas, as duas primeiras sendo o item 1 e sua continuação (cinco espaços de recuo): `  1. \`python -c "print('a')"\` → \`b\` — antes \`a\`, depois \`b\`; medido no` / `     acionamento 1. e conferido na revisão 2. da mesma janela` / `  2. \`python -c "print('c')"\` → \`d\` — antes \`c\`, depois \`d\``. No parágrafo de abertura da fixture, `Quatro cards sintéticos` → `Cinco cards sintéticos` e uma frase sobre o `CX-T5`. 2. Teste: TF `test_tf_prosa_na_continuacao_do_item_nao_vira_item` — `ok, falhas, medida = card_check.verificar_tarefa(str(_PLANO_CORPUS), "CX-T5", _ROOT)` → `ok is True`, `falhas == []`, `len(medida["itens"]) == 2`. Medido pelo consultor em protótipo (acionamento 6): o parser de hoje dá 2 itens e fecha; o texto achatado das mesmas linhas tem 4 marcadores `N.`.
- **Não fazer:** não tocar `.claude/tools/card_check.py` nem `rdo.py`; não mudar `CX-T1`..`CX-T4` nem os testes que os usam.
- **Contingências:** - se o TF novo falhar sobre o `card_check.py` de hoje → o comportamento regrediu depois do `FPU-T1`: parar e sinalizar `blocked` razão `premissa`, colando a falha.
- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** card CX-T5 em tests/fixtures/card_check/plano-corpus.md:50 (prosa 1./2. na continuacao do item 1 da Verificacao); TF test_tf_prosa_na_continuacao_do_item_nao_vira_item em tests/test_card_check.py:206 - **Contrato:** verificar_tarefa sobre CX-T5 -> ok True, falhas [], 2 itens; suite 410 passed - **Não refazer:** o fantasma do AE-33/P-0740 esta trancado por teste - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, veredito aprovado 100%

## Execução

**Consumo:** 18 tool uses, 71.5 k tokens, 185.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Poder discriminante conferido em memória, sem escrever no repositório: com _parsear_itens trocado por uma versão que achata as linhas do campo e parte em qualquer 'N.' precedido de espaço, CX-T5 cai (ok=False, 'item 1/2: fora da forma da 8.1') e CX-T4 continua verde (ok=True, 1 item). Isso confirma o AE-34: o TF antigo não trancava o marcador só no início de linha, e o novo tranca. Fixture: CX-T1..CX-T4 idênticos ao retrato do FPU-T1; mudaram só o parágrafo de abertura (Quatro->Cinco, mais a frase do CX-T5) e o card CX-T5 novo. O TF passa _PLANO_CORPUS sem o str() do Passo 2; verificar_tarefa aceita Path, então é detalhe equivalente e não desvio.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O executor, o revisor e o loop falam do arquivo de medida" e vai pegar a tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item".
Tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item". Passo: conferir os gates e preparar o despacho.
Tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item" e vai executar: a fixture `tests/fixtures/card_check/plano-corpus.md` ganha o card `CX-T5`, cuja Verificação tem dois itens e a linha de continuação do item 1 traz prosa com `1.` e `2.` fora do início de linha; um TF novo prova que `card_check.verificar_t…
Agente executor devolveu a tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item": review — sem pendência.
Tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Um teste tranca o marcador de item só no início de linha, com prosa `N.` na continuação do próprio item": aprovado 100%, bloqueante nenhuma.
