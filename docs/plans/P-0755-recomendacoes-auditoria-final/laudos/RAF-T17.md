# Laudo — P-0755 · RAF-T17

**Percentual:** 90%
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
| residuo | nao-se-aplica |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo e do alcance do card, admitido no despacho como DRF-44); reconciliado no ato: blob do arquivo na arvore (8ee3de5) igual ao do ref eeb6f20, e a entrega so insere 6 linhas de prosa em .claude/agents/pantonic-planner.md, sem simbolo; pytest 582 passed = piso 582 re-medido no despacho; ratchet, kit_check validate/check-drift e check-readme em exit 0 |
| residuo | nao-se-aplica | entrega de redacao: so prosa em .claude/agents/pantonic-planner.md, nenhum artefato executavel |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (apos os laudos RAF-T13a/T14/T15/T16): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa


