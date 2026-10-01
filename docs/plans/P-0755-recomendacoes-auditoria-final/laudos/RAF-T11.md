# Laudo — P-0755 · RAF-T11

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo, achado pre-existente admitido pelo card e pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo; suite 562 passed (559 do despacho + 3 novos), Verificacao 1 exit 0 (3 passed), check-drift e demais guardas exit 0 no dossie |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia na janela do P-0755 (RAF-T10, RAF-T10a e agora RAF-T11): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o card e o despacho declaram. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |
| dossiê | Lacuna latente das regras 2 e 3 do card RAF-T11, entregues como escritas: (a) alvo com curinga que cobre arquivos de teste (ex.: tests/test_*.py) e pulado, e a secao diz '- nenhum arquivo de teste entre os alvos' - afirmacao falsa e remocao invisivel (hoje sem caso vivo: F-17, 0 alvos com * no corpus); (b) linha removida cujo conteudo comeca por '--' cai no filtro de '---' e some. Exercitado na revisao em repositorio descartavel. Rota: item de replanejamento na secao 9 do P-0755 (AE-<n>), a triar pelo consultor contra RAF-T12, que consome a secao |

## Lições aprendidas na tarefa

A secao nova se provou no proprio dossie desta entrega: tests/test_review_evidence.py saiu 'nenhuma linha removida', o que confirma mecanicamente a restricao de so acrescentar ao fim do arquivo - a restricao que antes exigia leitura do diff agora se le numa linha.
