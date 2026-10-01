# Laudo — P-0755 · RAF-T30a

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
| guardas | parcial | dead_code exit 1 com 1 achado, docs/audits/sonda-2026-09-28/passos.py:13, nao rastreado, fora dos Arquivos-alvo, preexistente e admitido pela Restricao do card; nenhum simbolo de rdo.py no relatorio; reconciliado no ato: pytest exit 0 na evidencia, test_rdo+test_encerrar+test_doutrina_unidade 128 passed (127 datado + 1 novo), ratchet_piso, kit_check validate/check-drift e check_readme exit 0. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado preexistente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no card; a revisao reconcilia a mao a cada tarefa. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |

## Lições aprendidas na tarefa


