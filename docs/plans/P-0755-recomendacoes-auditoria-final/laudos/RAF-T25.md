# Laudo — P-0755 · RAF-T25

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, nao tocado desde 4774d67, admitido na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19..T24; a entrega so acrescenta prosa ao pantonic-planner.md, sem simbolo Python; pytest re-rodado 602 passed = piso 602 do despacho, exit 0; kit_check check-drift re-rodado exit 0; ratchet, validate e check-readme em exit 0 na evidencia |
| residuo | nao-se-aplica | nao-se-aplica: entrega de redacao sem artefato executavel (9 linhas de prosa no passo 4 da rodada de replanejamento) |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Buraco de coerencia da DRF-14 (nao da entrega): a regra entregue manda registrar o card da operacao nova em estado.tsv blocked, razao dependencia, nota 'aguarda o aceite da versao <k> no marco', mas nenhum instrumento nem doutrina o tira de blocked quando o marco aceita a versao - encerrar.py marco --aceita-versao so reescreve o campo Operacao do modelo (promover_versao) e move a linha do PLANO a ready; no ramo --recusa-versao o card da operacao eliminada fica blocked sem destino nomeado. Rota: item de replanejamento do P-0755 (AE-<n> na secao 9), card que fecha a transicao do card bloqueado no aceite e o destino dele na recusa. |

## Lições aprendidas na tarefa

Card de redacao com bloco cercado verbatim e verificacao por contagem de frase: a entrega bateu com o bloco prescrito (9 linhas, uma vazia e oito de prosa, no ponto das ancoras 561/565). A conferencia ponta a ponta das afirmacoes do trecho contra os instrumentos fechou para o que o trecho afirma (modelo.py emite '1A: V1 OP-<n> — operação sem tarefa'; convencao de lastro 'tarefas: <prefixo>-T<n>' existe na linha 214; promover_versao reescreve os cards) e expos o que o trecho nao afirma e o plano nao fechou: a saida de blocked do card no aceite. O card_check do card sai 1 em status review por construcao (compara o mundo antes, nova=0, contra o mundo depois); nao e sinal contra a entrega.
