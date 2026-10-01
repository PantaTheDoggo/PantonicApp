# Laudo — P-0755 · RAF-T23a

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, nao rastreado, admitido na restricao do card e na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19/T19a/T21/T22/T23; nenhum simbolo do encerrar.py no relatorio; pytest re-rodado 602 passed = piso 601 do despacho + o 1 teste novo, exit 0; ratchet, kit_check validate/check-drift e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta do verbo marco em repositorios temporarios (fixture PLANO_MARCO_PROMOCAO, fora da arvore): com a regra nova, --recusa-versao com cabecalho '(rascunho)', --aceita-versao com espaco final no cabecalho e plano sem ## 1A saem todos exit 1 com 'marco: plano sem versao pendente (## 1A)' e o plano byte a byte igual; cabecalho exato segue exit 0 no aceite e na recusa. A pre-checagem, o _checar_promocao e o _dossie_emenda leem agora a ## 1A pela mesma igualdade com _modelo._HEADING_PENDENTE; grep de _MARCO_VERSAO_PENDENTE_RE em encerrar.py sai 0; tests/test_encerrar.py 43 passed.
