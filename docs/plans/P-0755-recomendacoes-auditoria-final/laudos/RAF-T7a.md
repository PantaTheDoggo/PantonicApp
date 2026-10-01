# Laudo — P-0755 · RAF-T7a

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo e do alcance do card; achado pre-existente admitido pelo card e pela DRF-44, o mesmo dos laudos RAF-T1..RAF-T7); re-rodado na revisao: 1 achado, nenhum novo; pytest -q 549 passed exit 0 (549 collected = piso do despacho, sem teste novo, como o card exige); check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia apos RAF-T1..RAF-T7: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) declarada no proprio card; a revisao reconcilia a mao (passo 3a). Rota: DRF-44 ja aberta no P-0755; somar a reincidencia ao AE-<n> que ja aponta para ela na secao 9 |

## Lições aprendidas na tarefa

Reconciliacao por construcao: com _texto_do_disco devolvendo texto (bytes de hoje decodificam em UTF-8) e _texto_do_ref_ou_none devolvendo None (bytes do ref nao decodificam), os bytes nunca igualam - as duas comparacoes removidas eram de fato constantes, e o comportamento observavel nao muda. Verificacao 1 rodada nos dois mundos: 5 no ref 0ac4f75, 3 na arvore, exit 0. Os 5 testes quebra (inclusive test_tf_quebra_ref_binario_hoje_texto_compara_bytes, que atravessa coletar_arquivos_tocados e montar_trechos, isto e, os dois ramos editados) seguem verdes; tests/test_review_evidence.py intocado.
