# Laudo — P-0752 · FPU-T5a

**Percentual:** 100%
**Veredito:** aprovado
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | nao-se-aplica |
| guardas | conforme |
| rota | conforme |
| residuo | nao-se-aplica |
| registro | conforme |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | FPU-T5a (OP-5): o card fixou no Objetivo e nos Passos 1 e 3 o caminho literal docs/RDO/evidencia/<plano>-<ID>-medida.json para o executor gravar e o scrum-master nomear, mas review_evidence.py:777-781 (FPU-T5) le o JSON em <dir da evidencia> = pai do --out, que para plano em pasta e <pasta>/evidencia; plano em pasta sai com '## Medida do executor' = ausente mesmo com o executor cumprindo o texto ao pe da letra (o P-0752, legado, nao exercita o ramo). No mesmo comando o placeholder <plano> vale caminho em --plano e id (P-0752) no nome do JSON. Execucao fiel ao card: nao rebaixa entrega. Rota: item de replanejamento do P-0752 - card corretivo da OP-5 que troca o literal pelo destino derivado (legado: docs/RDO/evidencia; pasta: <pasta>/evidencia) e desambigua <plano> em executor, reviewer e scrum-master Passo 5. |

## Lições aprendidas na tarefa

A medida desta tarefa foi gravada pelo loop com o mesmo instrumento (card_check --mundo depois --gravar), porque a regra que manda o executor grava-la nasce desta entrega; o reviewer re-executou card_check --mundo depois (exit 0, 'tarefa FPU-T5a fecha'). Os 31 arquivos fora dos alvos sem atribuicao tem mtime anterior ao ref de despacho ae9db2b (10:27:12), e os tres alvos tem mtime 10:29 - escopo reconciliado por git diff e mtime (AE-35/AE-38). Primeira tarefa julgada com a secao '## Medida do executor' preenchida: o ramo legado da cadeia executor -> evidencia -> reviewer funcionou de ponta a ponta.
