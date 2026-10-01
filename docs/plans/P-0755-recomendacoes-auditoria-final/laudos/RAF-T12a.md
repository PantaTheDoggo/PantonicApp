# Laudo — P-0755 · RAF-T12a

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo; achado pre-existente admitido pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo; suite inteira 566 passed (= piso do despacho), tests/test_review_evidence.py 100 passed, check-drift exit 0, Verificacao 1 testes=0-1 ancoras=0-1 docstring=1 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia na janela do P-0755 (RAF-T10..RAF-T12 e agora RAF-T12a): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa


