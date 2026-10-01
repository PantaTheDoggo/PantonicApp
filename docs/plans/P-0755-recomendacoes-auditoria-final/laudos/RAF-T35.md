# Laudo — P-0755 · RAF-T35

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
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), pasta nao rastreada de 2026-09-28, anterior ao ref 6ba2a60 (2026-09-30), fora dos alvos e no fora-do-alcance do card, nao tocada pela entrega (so pantonic-consultant.md mudou); reconciliado re-rodando dead_code (exit 1, mesmo achado), pytest 628 passed (acima da referencia datada 521) e check-drift exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (AE-195 do RAF-T34): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; o reviewer reconciliou re-rodando. Rota: item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo |
| dossiê | reincidencia do AE-196: o trecho de diff do alvo trunca em 4000 caracteres dentro da linha unica do item 3, e a substituicao so se confirma abrindo o repositorio (confirmada: trecho antigo 1 vez, linha nova igual a antiga com o trecho novo inserido, numstat 1/1). Rota: item de replanejamento do P-0755 ja aberto na secao 9 (AE-196) |

## Lições aprendidas na tarefa


