# Laudo — P-0755 · RAF-T13a

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (arquivo nao rastreado, fora dos Arquivos-alvo, admitido no despacho como DRF-44); reconciliado: a entrega so troca texto de docstring e de help em card_check.py, nao cria nem remove simbolo, logo nao move o detector; pytest 573 passed = piso 573 re-medido no despacho; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia (AE-150, AE-152, AE-153, AE-154): o dead_code vermelho pre-existente de docs/audits/sonda-2026-09-28/passos.py (DRF-44) e admitido no despacho mas o dossie de evidencia nao carrega essa linha de base, e toda tarefa do P-0755 sai com guardas nao conforme mecanico e parcial reconciliado enquanto o arquivo viver na arvore. Rota: item de replanejamento do P-0755 (AE na secao 9) - linha de base admitida no review_evidence.py ou recorte de docs/audits/ no dead_code |

## Lições aprendidas na tarefa

Exercicio ponta a ponta em leitura: diff de card_check.py = exatamente as 5 linhas antigas trocadas pelas 6 novas do card (numstat 6/5), arquivo segue LF (0 CRLF antes e depois), ast valido; --help renderiza o texto novo de --mundo; card_check RAF-T13a sai 0 em --mundo depois e 1 em --mundo antes (divergencia nomeada 'docstring=1-0 help=1-0' contra 'docstring=0-1 help=0-1'), o que prova o card discriminante nos dois mundos; card_check RAF-T13 (done) segue 0. O texto novo diz 'depois o literal do esperado' no contexto da forma 8.1 do docstring, coerente com a regra 1 da RAF-T13; na forma inline com par o depois le o valor do par, e o docstring nao afirma o contrario.
