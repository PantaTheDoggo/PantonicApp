# Laudo — P-0755 · RAF-T18

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo e do alcance do card, admitido no despacho como DRF-44); reconciliado no ato: blob do arquivo na arvore (8ee3de5) igual ao do ref 35a0684, e a entrega so insere 5 linhas de prosa em .claude/agents/pantonic-planner.md, sem simbolo; pytest 582 passed = piso 582 re-medido no despacho; ratchet, kit_check validate/check-drift e check-readme em exit 0 |
| residuo | nao-se-aplica | entrega sem artefato executavel: 5 linhas de doutrina no item 14 da Fase 4 do planejador |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (apos os laudos RAF-T13a/T14/T15/T16/T17): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa

Exercicio ponta a ponta da regra entregue, em copia temporaria fora do repositorio: card_check --root <copia> --mundo depois --gravar e --mundo antes --gravar gravaram P-0755-RAF-T18-medida-depois.json e -medida-antes.json lado a lado em <copia>/docs/plans/P-0755-.../evidencia/ (exit 0 nos dois mundos), e o mundo depois contra a arvore antes falha com divergencia rodada=1 x rodada=0 - a doutrina descreve um caminho que o instrumento da RAF-T15 executa como escrito. Nota: a copia de ensaio precisa carregar .claude/tools (card_check importa rdo.py da raiz passada em --root); a copia integral que o item 14 manda fazer ja cobre isso.
