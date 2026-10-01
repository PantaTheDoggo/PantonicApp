# Laudo — P-0755 · RAF-T26a

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19..T26; a entrega so troca seis linhas de prosa num .md de agente, sem simbolo Python; pytest re-rodado 604 passed = piso 604 do despacho; kit_check check-drift re-rodado exit 0; ratchet, validate e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta feito contra o codigo, nao so contra o card: as quatro razoes que a frase nova enumera casam uma a uma com os quatro raise _conflito de _checar_promocao (encerrar.py:1084, 1088, 1095, 1102), e o 'devolve a ## 1 e a ## 1A acertadas, com o registro de versoes, para o comando rodar de novo' casa com o Devolver do ramo de conflito (encerrar.py:1077-1078); a frase da recusa, intocada, segue coerente com o Devolver da recusa (encerrar.py:1243-1244). Nenhum resto do texto antigo no .claude (grep 'acertad'). Verificacao 1 re-rodada conflito=0-1; arquivo em LF (0 CR); tests/test_doutrina_unidade.py 8 passed; recorte desde a ref so 6+/6- no alvo, com as seis primeiras linhas do paragrafo No marco intocadas.
