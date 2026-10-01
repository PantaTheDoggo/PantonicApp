# Laudo — P-0755 · RAF-T22

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, nao rastreado, admitido na restricao do card e na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19/T19a/T21; pytest 596 passed = piso 593 collected do despacho + os 3 testes novos, exit 0; ratchet, kit_check validate/check-drift e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Decisoes da entrega que o card nao fechou (G-NOASK): (1) apagou o helper _op_por_numero de modelo.py, que ficou sem chamador ao reescrever _diff_fluxo - o card nao previu o orfao, e manter o helper faria o dead_code ganhar achado novo contra a restricao; (2) o estado inicial dos casos de teste saiu '-', valor que o card nao fixou (so os finais). Nenhuma das duas muda o mundo exercitado. Rota: AE-<n> na secao 9 do P-0755, sem acao (autoria futura: card que reescreve funcao nomeia o helper que ela deixa orfao), mesma classe do AE-156. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta nesta revisao, em memoria, sem escrever no repositorio: remocao (A,B,C -> A,C) sai [=] OP-2 (era OP-3) e [-] OP-2 — B; insercao com alteracao (A,B -> A2,N,B) sai [~] OP-1, [+] OP-2, [=] OP-3 (era OP-2), sem cascata; troca de ordem sai dois [=]; texto duplicado na vigente sobra como [-]; versoes iguais seguem saindo 'sem drift'; estado com chave so-pendente, so-vigente e alterada sai [+], [-] e [~] nessa ordem. Plano real: show --drift sobre P-0755 sai exit 0 com so a linha de contrato do objeto e a linha de estado da versao 3, como a DRF-60 mediu; check sai 0 (versao 2, 52 tarefas). Os tres testes de drift pre-existentes seguem verdes sem mudanca e nenhuma linha de teste saiu. OP-22 confere com a entrega: sem conflito de modelo.
