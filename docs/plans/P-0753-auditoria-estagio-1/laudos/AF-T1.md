# Laudo — P-0753 · AF-T1

**Percentual:** 100%
**Veredito:** aprovado
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | conforme |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

nenhum

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | AF-T1, secao Testes: o TR test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas (ref capturado e nada mudado) nao discrimina a guarda do contrato 'com tocados vazio o git diff nao roda sem caminho' - sem a guarda, git diff --stat <ref> <arvore> tambem sai vazio nesse cenario; o caso que diverge (arvore difere de <ref> com tocados vazio, ex.: nao rastreado ausente de um <ref> de git stash create com mtime anterior ao corte) ficou fora do card, criterio (ix) da RUBRICA §8. Implementacao honra a guarda por inspecao. Rota: tiquete indexado no diario, aberto por quem conduz a sessao. |

## Lições aprendidas na tarefa

O proprio dossie de evidencia desta tarefa ja saiu pelo codigo entregue: o bloco Diff lista os mesmos 6 arquivos de Arquivos tocados, os 2 nao rastreados inclusive, contra os 59 do caso medido. Exercicio ponta a ponta em repositorio temporario (trabalho alheio antes do <ref>, rastreado alterado e nao rastreado criado depois): Diff = tocados, sem-desde inalterado, indice real, lista de stash e status da arvore identicos antes e depois. Observacao sem rota: o --stat abrevia caminho longo com '.../' (visto no bloco desta tarefa), efeito da largura padrao do git que o card prescreveu.
