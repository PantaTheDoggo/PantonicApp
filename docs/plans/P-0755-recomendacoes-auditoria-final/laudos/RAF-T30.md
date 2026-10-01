# Laudo — P-0755 · RAF-T30

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
| guardas | parcial | dead_code exit 1 com 1 achado, docs/audits/sonda-2026-09-28/passos.py:13, nao rastreado, fora dos Arquivos-alvo, preexistente e admitido pela Restricao do card; nenhum simbolo de encerrar.py no relatorio; reconciliado no ato: pytest 617 passed exit 0 (referencia datada 521 + os 5 novos respeitada), ratchet_piso, kit_check validate/check-drift e check_readme exit 0 na evidencia. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado preexistente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no card; a revisao reconcilia a mao a cada tarefa. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |

## Lições aprendidas na tarefa

Redespacho fechou o defeito do primeiro laudo: tests/test_encerrar.py so ganhou linhas depois da 1211 (git diff contra 9e5bf2e sem linha removida), a assercao 'linha nova do registro' voltou ao TF do marco e a Verificacao 3 sai marco=2 total=2. Exercicio ponta a ponta numa copia temporaria: tres achados numerados #1..#3 na ordem da tabela, B1 com EXCECAO em caixa alta sai antes da linha OK, e o --achado do comando segue sem Origem. O caminho real rdo.py laudo -> alvo instrumento -> B1 segue fechado ate a RAF-T30a (DRF-68), fora deste card.
