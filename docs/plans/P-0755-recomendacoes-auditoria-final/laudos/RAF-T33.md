# Laudo — P-0755 · RAF-T33

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
| guardas | parcial | dead_code exit 1 por docs/audits/sonda-2026-09-28/passos.py:13 (arquivo nao rastreado em docs/audits/, fora dos Arquivos-alvo e fora do alcance do card), anterior a tarefa (AE-192, DRF-44); reproduzido na revisao; demais guardas e a suite em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | O dossie de evidencia reporta dead_code vermelho sem marcar a causa como anterior a tarefa (docs/audits/sonda-2026-09-28/passos.py, fora dos alvos); cada revisao do P-0755 reconcilia o mesmo vermelho a mao. Rota: item de replanejamento do P-0755, junto ao AE-192 ja registrado - a evidencia deve atribuir o vermelho de guarda por arquivo, como faz com os tocados. |

## Lições aprendidas na tarefa


