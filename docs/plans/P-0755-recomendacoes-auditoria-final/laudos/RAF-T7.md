# Laudo — P-0755 · RAF-T7

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo e fora do alcance do card; achado pre-existente admitido pelo card, pelo despacho e pela DRF-44; o mesmo dos laudos RAF-T1..RAF-T6a); re-rodado na revisao: 1 achado, nenhum novo; _texto_do_ref saiu por inteiro; pytest --co 549 collected (544 do despacho + 5 novos); demais guardas exit 0 no dossie |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia apos RAF-T1..RAF-T6a: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio despacho declara; cada revisao reconcilia a mao (passo 3a). Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |
| dossiê | Contratos/classes regra 3 do RAF-T7 manda, no ramo texto_ref None, devolver '(sem alteracao desde <ref>)' quando os bytes do ref igualam os do disco; esse ramo so e alcancado com texto_atual decodificado em UTF-8 e ref nao decodificavel, logo bytes iguais sao impossiveis e o ramo e inalcancavel por construcao (a entrega o implementou fielmente, sem teste que o exercite). Rota: AE-<n> na secao 9 do P-0755, para o card seguinte que tocar _diff_para_arquivo (RAF-T8) decidir se o ramo sai |

## Lições aprendidas na tarefa

Exercicio ponta a ponta na arvore real: --atribuir e o caminho padrao sem rdo.py devolvem a mesma linha 'review_evidence: FALHOU - rdo.py: modulo nao encontrado em <caminho>' com exit 1 (contrato de erro coerente entre os verbos); a geracao real com --out fora da pasta do plano (tmp) achou evidencia/P-0755-RAF-T7-medida.json e preencheu a Medida do executor em vez de 'ausente'.
