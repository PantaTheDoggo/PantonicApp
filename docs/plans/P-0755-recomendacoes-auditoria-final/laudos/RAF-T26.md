# Laudo — P-0755 · RAF-T26

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19..T25; a entrega so troca prosa em dois .md de agente, sem simbolo Python; pytest re-rodado 602 passed = piso 602 do despacho, exit 0; kit_check check-drift re-rodado exit 0; ratchet, validate e check-readme em exit 0 na evidencia |
| residuo | nao-se-aplica | nao-se-aplica: entrega de redacao sem artefato executavel (12 linhas no ato Emenda do modelador e uma frase estendida no passo 3 do consultor) |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Texto novo fixado pelo card diverge do comando que ele descreve (nao da entrega, que e verbatim): (a) diz que o modelador devolve 'a ## 1A e o registro acertados', mas o dossie de conflito que encerrar.py imprime (_dossie_emenda) manda 'Devolver: a secao ## 1 depois do ato e a linha nova do registro de versoes'; (b) enumera tres conflitos, e _checar_promocao tem um quarto que tambem imprime o dossie ('o plano nao tem a ## 1'). Rota: item de replanejamento do P-0755 (AE-<n> na secao 9), corretivo que alinha o campo Devolver do _dossie_emenda no ramo de conflito ao que a doutrina do modelador pede, ou a doutrina ao comando, e fecha a lista de conflitos. |

## Lições aprendidas na tarefa

Card de redacao com bloco cercado verbatim: a entrega bate byte a byte com o texto novo (12 linhas no modelador, contagem 1) e com o trecho novo do consultor (word-diff de uma unica troca), e as duas Verificacoes saem promocao=0-1 e validacao=1. O exercicio ponta a ponta das afirmacoes contra encerrar.py marco fechou para --aceita-versao, --consultor obrigatorio e de uma linha, escape de | na celula, frase 'Caiu pelo aceite' e reescrita do campo Operacao do modelo; e expos o que o card nao conferiu ao fixar o texto: o campo Devolver do dossie de conflito e o quarto caso de conflito.
