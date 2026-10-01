# Laudo — P-0755 · RAF-T19

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido no card e no despacho como DRF-44); reconciliado no ato: blob do arquivo na arvore (8ee3de5) igual ao do ref 5e35c55; pytest 586 passed = piso 582 re-medido no despacho + os 4 testes novos; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (apos os laudos RAF-T13a..T18): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base admitida no despacho (1 achado); cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |
| dossiê | a regra 3 do card (validar com so_vigente=True nao emite V20) nao tem teste que a discrimine: a fixture dos quatro testes traz a pendente em versao 2 = vigente 1 + 1, entao V20 nunca dispara, e remover a guarda 'not so_vigente' deixa os 4 testes verdes (criterio (ix) da rubrica §8). A entrega implementou a regra como escrita. Rota: AE-<n> na secao 9 do P-0755, com teste de pendente fora de sequencia sob --so-vigente num card corretivo ou na RAF-T20 |
| modelo | objeto 'conferencia do modelo' (origem OP-19, tabela 1.1 linha 81): o contrato diz 'sem mudar o que ela ja julga quando chamada como hoje', mas a regra 4 do card RAF-T19 (DRF-37), entregue como escrita, muda o check sem --so-vigente: em tests/fixtures/modelo/fluxo-pendente.md a linha 'V4 EX-T2 — operacao inexistente OP-2' deixa de sair (5 -> 4 violacoes, conferido contra o modelo.py do ref 5e35c55). Rota: dossie Ato de modelo de conflito devolvido com o laudo ao pantonic-model-designer |

## Lições aprendidas na tarefa

A linha de retorno do executor so saiu no formato fixo depois de um reenvio (a primeira resposta trouxe prosa antes da linha); a telemetria carrega tres linhas usage para a tarefa. Informativo, sem efeito na marcacao.
