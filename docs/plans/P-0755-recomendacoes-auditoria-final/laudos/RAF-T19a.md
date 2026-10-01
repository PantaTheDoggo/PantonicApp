# Laudo — P-0755 · RAF-T19a

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido no card e no despacho como DRF-44); reconciliado no ato: blob do arquivo na arvore 8ee3de5, o mesmo do laudo RAF-T19; pytest 588 collected = piso 586 do despacho + os 2 testes novos, exit 0; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (apos os laudos RAF-T13a..T19): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa

O card corretivo fecha o AE-169 com poder discriminante medido nesta revisao: numa copia temporaria fora do repositorio, trocar 'and not so_vigente' por 'and True' em validar (modelo.py:362) faz o TF novo sair 1 (1 failed, 5 passed no recorte so_vigente), e o TR tranca a regra concorrente. Verificacao 1 exit 0, tests/test_modelo.py 40 passed, modelo.py e fixtures sem diff desde o ref, nenhuma linha removida dos testes. OP-19 confere com a entrega: sem conflito de modelo novo.
