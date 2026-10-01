# Laudo — P-0755 · RAF-T10a

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo, achado pre-existente admitido pelo card e pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo; pytest --co 559 collected (556 do despacho + 3 novos); tests/test_review_evidence.py 93 passed; Verificacoes 1 e 2 exit 0 (diff=0-0-1-1-1); check-drift exit 0 e demais guardas exit 0 no dossie |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia na janela do P-0755 (RAF-T10 e agora RAF-T10a): o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa

Exercicio ponta a ponta na revisao (repo descartavel, core.quotepath ligado, main com --desde e --out e --atribuir): rastreado acentuado commitado depois do ref, renomeacao acentuada commitada, rastreado acentuado alterado so na arvore e nao rastreado acentuado chegam todos com um nome so, atribuidos da entrega, com trecho e resumo --stat sem escape octal; OP-10 e o estado final da propriedade na versao 2 pendente (§1A) conferem com a entrega. Observacao sem rota: o trecho de uma renomeacao sai como arquivo novo (diff por pathspec do caminho novo), comportamento anterior e igual ao do nome ASCII.
