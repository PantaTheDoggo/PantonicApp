# Laudo — P-0755 · RAF-T13

**Percentual:** 91%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | conforme |
| guardas | parcial |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (arquivo nao rastreado, fora dos Arquivos-alvo, admitido no despacho como DRF-44); reconciliado: nenhum achado novo da entrega; pytest 573 passed = piso 566 + 7 novos; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | dead_code vermelho pre-existente (docs/audits/sonda-2026-09-28/passos.py, DRF-44) admitido no despacho mas nao carregado pelo dossie de evidencia: toda tarefa do P-0755 sai com guardas parcial enquanto o arquivo viver na arvore. Rota: item de replanejamento do P-0755 (AE na secao 9) - linha de base admitida no review_evidence.py ou recorte de docs/audits/ no dead_code |
| dossiê | card_check.py fica com dois textos que contradizem a regra 1 (mundo depois na forma 8.1): o docstring do modulo, linhas 5-6 ('comparando a saida medida agora com o Medido antes declarado'), e o help de --mundo ('Mundo do card a comparar na forma inline (DFP-14)'); a regra 3 do card nomeou so o docstring de verificar_tarefa, e a entrega seguiu o card. Rota: item de replanejamento do P-0755 (AE na secao 9), acerto dos dois textos no mesmo arquivo |
| dossiê | G-NOASK: o card fixou antes 'x, y' e o valor impresso do test_tf_par_com_crase_antes_aceita_virgula, mas nao o esperado nem o depois do item; a entrega escolheu esperado 'esperado' e depois 'q' (sem efeito no mundo antes que o teste exercita). Rota: item de replanejamento do P-0755 (AE na secao 9), registro para o criterio (i) da secao 8 da rubrica |
| dossiê | a restricao 'card_check deste plano continua saindo 0 sobre RAF-T1..RAF-T18' e inalcancavel para o proprio RAF-T13 no mundo antes (status review): a entrega consome o antes (exit 5 -> exit 0) e o card_check do RAF-T13 sai 1 em antes e 0 em --mundo depois; os demais 18 cards saem 0. Rota: item de replanejamento do P-0755 (AE na secao 9) - a restricao exclui o proprio card ou fixa --mundo depois para ele |
| doutrina | o executor rodou git stash e git stash pop na arvore compartilhada, que carrega WIP nao commitado de varios planos, para provar o TDD; a conducao conferiu stash vazio e WIP intacto, e o Passo 2 do card ja dava a prova (TF vermelho antes da regra). Nenhuma guarda mecanica impede comando git que reverte a arvore inteira numa sessao de execucao, e a restricao 'nada fora deles se toca, se reverte' nao foi lida como cobrindo stash. Rota: tiquete indexado (AE na secao 9 do P-0755) - guarda PreToolUse que recusa git stash/reset/checkout --/restore na execucao |

## Lições aprendidas na tarefa

A prova de TDD reproduzida pelo reviewer numa copia fora do repositorio (card_check.py do ref e0043041 + os testes novos) deu 5 TF vermelhos e 2 TR verdes, exatamente como o Passo 2 pede: a prova nao precisa de git stash na arvore real. Exercicio ponta a ponta (plano sintetico fora do repo): forma 8.1 em --mundo depois com negrito 'exit 3' compara o codigo, crase com ponto/virgula/ponto-e-virgula casa inteiro, esperado sem literal falha nomeado, --gravar grava a medida; nenhum card real de docs/plans/ tem item 8.1 com esperado sem literal (327 itens, 0 reais), entao a regra nova nao quebra card ja escrito.
