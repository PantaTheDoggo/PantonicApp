# Laudo — P-0755 · RAF-T23

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, nao rastreado, admitido na restricao do card e na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19/T19a/T21/T22; nenhum simbolo novo do encerrar.py no relatorio; pytest re-rodado 601 passed = piso 596 do despacho + os 5 testes novos, exit 0; kit_check check-drift re-rodado exit 0; ratchet, kit_check validate e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Contrato de erro do marco com duas regras para o mesmo cabecalho: a pre-checagem de gravar_marco aceita a ## 1A por prefixo (_MARCO_VERSAO_PENDENTE_RE), e o _checar_promocao que o card prescreveu le a secao por igualdade exata (_modelo._HEADING_PENDENTE, via _localizar_secao); cabecalho com texto a mais passa a pre-checagem e derruba _checar_promocao em AttributeError (modelo_pendente None) em vez de EncerramentoError com exit 1. O card enumerou as razoes de conflito sem a 'plano sem ## 1A legivel'; a entrega seguiu o card. Rota: AE-<n> na secao 9 do P-0755, card corretivo que unifique a leitura do cabecalho ou acrescente a razao de conflito. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta contra o plano real em memoria (sem escrita): _checar_promocao aceita a versao 3, recusa a 2 com o conflito 'a ## 1A e a versao 3' e o dossie Ato: emenda, e recusa 'x' pelo numero; promover_versao reescreve 52 cards, deixa 1 obsoleta, 2 obsoleta com 'Caiu pelo aceite da versao 3' e 3 vigente, e a ## 1 nova valida sem violacao (versao 3, 40 operacoes). Caminhos de CLI fora dos testes (consultor multilinha, consultor so espacos, versao nao numerica) saem 1 com o plano byte a byte igual; --consultor com --recusa-versao e ignorado em silencio, coerente com 'recusa nao muda'.
