# Laudo — P-0755 · RAF-T20

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
| guardas | parcial | dead_code exit 1 com um unico achado, docs/audits/sonda-2026-09-28/passos.py:13, arquivo fora dos alvos e nao tocado pela entrega; mesma falha do estado previo (DRF-44, admitida na nota do despacho); demais cinco guardas exit 0 e suite 590 passed, piso 588 + 2 novos |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar que ele e admitido e anterior ao diff; o revisor reconcilia a mao a cada laudo. Rota: DRF-44 na secao 9 do P-0755 (lacuna ja roteada), sem acao nova nesta tarefa. |

## Lições aprendidas na tarefa

Discriminacao conferida em copia descartavel: sem o --so-vigente em despachar, o TF cai com 'despachar: recusado - modelo: modelo: FALHOU - 1 violacao(oes)' e o TR segue verde; com a flag, 2 passed. O check completo segue so no fechamento (encerrar.py:325), coerente com o card.
