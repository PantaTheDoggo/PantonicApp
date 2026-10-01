# Laudo — P-0755 · RAF-T11a

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo e fora do alcance do card; achado pre-existente admitido pelo card e pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo; suite inteira 566 passed (562 do despacho + 4 novos), Verificacao 1 exit 0 (4 passed), tests/test_review_evidence.py 100 passed, check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia na janela do P-0755 (RAF-T10, RAF-T10a, RAF-T11 e agora RAF-T11a): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o card e o despacho declaram. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa

Exercicio ponta a ponta em repositorio descartavel (alvos tests\test_*.py com barra invertida, tests/**/test_*.py, alvo exato com barra invertida mais curinga, src/*.py, arquivo de teste apagado, nao rastreado presente no ref, nao rastreado novo cujo conteudo tem linha '@@' e linha '-'): cobertura, dedupe por forma normalizada e a linha '---sep--' saem como o card fixa; o arquivo novo com '@@' no conteudo sai 'nenhuma linha removida', porque a regra ancora no primeiro '@@' do diff e nao no conteudo. Alvo diretorio sem barra final ('tests') nao chega a expandir: o parser do plano o descarta como literal nao reconhecido, fato pre-existente e visivel no proprio dossie (Literais nao reconhecidos) - o card usa 'tests/'. A propria secao nova confirma a restricao de so acrescentar: tests/test_review_evidence.py saiu 'nenhuma linha removida'.
