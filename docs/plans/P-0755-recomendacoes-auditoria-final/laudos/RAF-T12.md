# Laudo — P-0755 · RAF-T12

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo e do alcance do card; achado pre-existente admitido pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo; suite inteira 566 passed (= piso do despacho, nenhum teste novo), check-drift exit 0, Verificacao 1 rubrica=0-1 (antes, no ref, rubrica=1-0) |
| testes | nao-se-aplica | nao-se-aplica: card de classe redacao, 'nenhum teste novo'; a suite segue medida em guardas (566 passed, exit 0); nenhum arquivo de teste entre os alvos |
| residuo | nao-se-aplica | nao-se-aplica: entrega sem artefato executavel - so texto da rubrica |

## Achado de processo

| alvo | achado |
|---|---|
| rubrica | O criterio novo de testes/nao conforme (asserção removida sem ordem do card) exige juizo - confrontar cada linha de '## Linhas removidas dos testes' com o que o card manda -, mas o bullet Fonte da evidencia segue 'mecanica' e o veredito travado de review_evidence.py (veredito_testes) le so o exit do pytest: a dimensao virou de fonte mista sem a rubrica dizer qual parte e travada e qual e juizo (§3). Texto entregue verbatim pelo card; nao rebaixa a entrega. Rota: item de replanejamento na secao 9 do P-0755 (AE-<n>), a triar pelo consultor junto de RAF-T17 (linha de invariancia do card de revisao) |
| dossiê | Reincidencia na janela do P-0755 (RAF-T10, RAF-T10a, RAF-T11, RAF-T11a e agora RAF-T12): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa


