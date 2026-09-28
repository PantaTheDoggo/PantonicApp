# Laudo — DIARIO_DE_OBRAS · TK-88d

**Percentual:** 91%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | parcial |
| escopo | conforme |
| testes | conforme |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| criterio-de-pronto | parcial | O Objetivo (CT-4: stdout concordando em genero) pede 'tarefa fechada' e o encerrar.py:958 ainda imprime 'encerrar: OK - {args.comando} fechado', que sai 'tarefa fechado' (exercitado ponta a ponta em repo temporario); os tres itens do Pronto quando (recusa do checar_close antes do done, 0 0 na Verificacao 2, FECHADO 1/1) tem contrapartida e estao verdes. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | O item 'stdout diz tarefa fechada' do Objetivo nao entrou no Pronto quando nem em teste: o TF test_tf_fechado_conta_como_o_indice so afirma 'plano fechado', que ja era a saida antes da tarefa (verificacao sem poder discriminante, rubrica §8 (xvii)). Rota: corretivo de uma linha no encerrar.py:958 com teste que afirme 'tarefa fechada' no stdout de encerrar.py tarefa, aberto pela triagem do TK-88. |
| dossiê | Decisao que o card delegou a execucao (G-NOASK): qual recusa do rdo.py close o TR test_tr_checar_close_recusa_antes_do_done exercita; a execucao escolheu a colisao de destino ('ja existe - tarefa ja fechada'). Escolha coerente com o Objetivo; rota: registrado, sem acao nesta tarefa - a regra de autoria (rubrica §8 (i)) ja cobre o caso para cards futuros. |

## Lições aprendidas na tarefa


