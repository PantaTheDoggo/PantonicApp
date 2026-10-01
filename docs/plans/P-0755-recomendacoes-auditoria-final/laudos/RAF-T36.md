# Laudo — P-0755 · RAF-T36

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
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), pasta nao rastreada ja presente antes do ref cbfc089, fora dos alvos e no fora-do-alcance do card, nao tocada pela entrega (so pantonic-planner.md mudou, 7/7 linhas desde o ref); reconciliado re-rodando dead_code (exit 1, mesmo achado), pytest 628 passed (acima da referencia datada 521) e check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (AE-195 do RAF-T34): o dossie de evidencia marca guardas vermelho pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar que a causa e anterior a tarefa e alheia aos alvos; o reviewer reconciliou re-rodando. Rota: item de replanejamento do P-0755 ja aberto na secao 9 (DRF-44), sem card novo |

## Lições aprendidas na tarefa


