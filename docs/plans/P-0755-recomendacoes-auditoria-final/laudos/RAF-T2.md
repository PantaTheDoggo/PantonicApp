# Laudo — P-0755 · RAF-T2

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (achado pre-existente medido no despacho, 1 achado(s), admitido pelo card via DRF-44); passos.py e medir.py identicos ao blob do ref 9eb2af0, fora dos Arquivos-alvo; custo_sessao.py nao ganhou achado (todas as funcoes alcancaveis de main); re-rodado na revisao: pytest 525 passed (521 do despacho + 4 novos), Verificacao 1 e 2 exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia (terceira na janela, apos laudos RAF-T1 e RAF-T1a): o dossie de evidencia do P-0755 marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base do despacho, e cada revisao reconcilia o mesmo vermelho a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na §9 apontando para ela |

## Lições aprendidas na tarefa


