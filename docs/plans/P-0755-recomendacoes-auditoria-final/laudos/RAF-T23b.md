# Laudo — P-0755 · RAF-T23b

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, nao rastreado, datado de 2026-09-28, admitido na restricao do card e na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19..RAF-T23a; nenhum simbolo do encerrar.py no relatorio; suite re-medida 604 collected = piso 602 do despacho + os 2 testes novos, pytest exit 0; ratchet, kit_check validate/check-drift e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Decisao que o card nao fechou (G-NOASK): a regra 1 de Contratos/classes pede o parametro devolver 'depois de restricao (um parametro por linha na assinatura)', o que tanto le 'o novo em linha propria' quanto 'todos os parametros um por linha'; a entrega escolheu a primeira leitura (devolver em linha propria, os seis anteriores intactos na mesma linha). Desvio de detalhe, reversivel, sem efeito em teste. Rota: AE-<n> na secao 9 do P-0755 para a autoria de cards fixar a forma da assinatura por bloco cercado, nao por parentetico. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta do verbo marco em repositorios temporarios (fixture PLANO_MARCO_PROMOCAO, fora da arvore): os quatro ramos de conflito de _checar_promocao (a ## 1A em outra versao, plano sem ## 1, registro sem vigente unico, registro sem a linha pendente) saem todos exit 1, plano byte a byte intacto, com o mesmo Devolver do conflito; a recusa sai exit 0 com o Devolver da recusa; a promocao valida sai exit 0 sem dossie. Isso fecha tambem a parte (b) do AE-180 do lado do comando: o quarto conflito ('o plano nao tem a ## 1') imprime o dossie com o Devolver novo. tests/test_encerrar.py 45 passed; Verificacao 2 re-rodada devolver=0-1.
