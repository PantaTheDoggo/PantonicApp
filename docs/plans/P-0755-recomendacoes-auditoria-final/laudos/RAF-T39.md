# Laudo — P-0755 · RAF-T39

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
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), pasta nao rastreada fora dos alvos e no fora-do-alcance do card, identica no snapshot do ref 4e56d2b (mesma falha no estado previo ao diff); reconciliado re-rodando dead_code (exit 1, mesmo achado), pytest 630 passed (acima da referencia datada 521) e check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (AE-195 do RAF-T34, repetida em RAF-T36..T38): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; reconciliado pelo reviewer. Rota: item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo |
| dossiê | o bloco que o card ditou manda a entrega ser 'a celula o que o dono le' da linha do marco, mas o exemplo do Marco 2 usa a celula aparada ('etapa A, custo da orquestracao', sem a lista R-01..R-24), e a celula do Marco 1 e um comando, nao o nome de uma entrega; alem disso o primeiro paragrafo do Relatorio de encerramento (intocavel pelo card) segue dizendo que o relatorio abre com o modelo.py show, sem remissao a excecao do marco. Rota: item de replanejamento do P-0755 na secao 9 (AE-<n> pela conducao), para a RAF-T40 ou o Marco 6 fixarem se a celula entra inteira ou so ate os dois-pontos |

## Lições aprendidas na tarefa

Entrega de redacao verbatim: o texto do card entrou identico e no ponto ancorado; o unico vermelho da bateria e a sonda nao rastreada da auditoria, pela quinta tarefa seguida, o que so o fechamento da DRF-44 encerra.
