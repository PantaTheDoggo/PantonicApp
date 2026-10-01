# Laudo — P-0755 · RAF-T40

**Percentual:** 90%
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
| residuo | nao-se-aplica |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), pasta nao rastreada fora dos alvos e no fora-do-alcance do card, nao tocada pela entrega (mesma falha no estado previo ao diff, igual aos laudos de RAF-T39 e RAF-T39a); reconciliado re-rodando dead_code (exit 1, mesmo achado), pytest 630 passed (igual a referencia datada 630), check-readme exit 0 e check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (AE-195 do RAF-T34, repetida de RAF-T36 a RAF-T40): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; reconciliado pelo reviewer. Rota: item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo |

## Lições aprendidas na tarefa

Redacao verbatim: as dezesseis trocas e os dois itens novos entraram identicos, cada um no ponto ancorado, sem refluxo das linhas vizinhas (diff restrito aos trechos). Exercicio ponta a ponta: Verificacao 1 re-rodada (guia=11-16-0), check-readme OK, e cada afirmacao nova do guia conferida contra o kit (custo_sessao.py medir/passos, card_check.py (invariancia), modelo.py --so-vigente chamado pelo despachar, encerrar.py --consultor e a linha encerrar: B1, backlog.py C-18, prevoo.py status criar). A linha 'imprime o card' que o AE-126 apontou saiu com a troca 9. O unico vermelho segue sendo a sonda da auditoria, pela setima tarefa seguida.
