# Laudo — P-0755 · RAF-T39a

**Percentual:** 88%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | nao-se-aplica |
| guardas | parcial |
| rota | conforme |
| residuo | nao-se-aplica |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), pasta nao rastreada fora dos alvos e no fora-do-alcance do card, nao tocada pela entrega (mesma falha no estado previo ao diff, igual ao laudo da RAF-T39); reconciliado re-rodando dead_code (exit 1, mesmo achado), pytest 630 passed (igual a referencia datada 630) e check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (AE-195 do RAF-T34, repetida de RAF-T36 a RAF-T39): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; reconciliado pelo reviewer. Rota: item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo |

## Lições aprendidas na tarefa

Redacao verbatim: as duas trocas entraram identicas e no ponto ancorado, a remissao do primeiro paragrafo nao repete o nome da subsecao (contagem 1) e o exemplo do Marco 2 agora casa com a regra (trecho antes dos dois-pontos); o AE-204 do laudo da RAF-T39 fecha aqui. O unico vermelho segue sendo a sonda da auditoria, pela sexta tarefa seguida.
