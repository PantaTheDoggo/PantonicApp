# Laudo — P-0754 · AUF-T2

**Percentual:** 91%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | parcial |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| testes | parcial | O TF novo existe e passa (Verificacao 1 exit 0; suite 508 passed), mas o diff apaga a ultima linha do teste de regressao da AUF-T1, 'assert "+linha-1" not in texto' em test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral (hunk @@ -1432,4 +1432,23 @@, linha '-' sem reposicao); o card mandava so acrescentar ao fim e nada reverter. A assercao removida continua verdadeira (reexecutada em leitura), logo a remocao nao tem causa: e perda de cobertura, e a correcao e repor a linha numa execucao seguinte (AE-<n> na secao 9). |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | A Verificacao do card (-k caminho_acentuado) e a restricao de suite por contagem (505/508 passed) nao discriminam o enfraquecimento de um teste vizinho no mesmo arquivo-alvo: a remocao de uma assercao da AUF-T1 passou verde por construcao. Rota: item de replanejamento na secao 9 do plano (AE-<n>) - card de acrescimo a arquivo de teste existente precisa de verificacao de que o diff do arquivo-alvo nao tem linha removida (ex.: git diff --numstat com delecoes = 0). |
| dossiê | Exercicio ponta a ponta (3b): o caminho com escape octal que coletar_arquivos_tocados devolve segue para montar_trechos como '(sem diferenca coletavel - arquivo ausente na arvore de trabalho)', isto e, arquivo nao versionado com acento de verdade chega ao revisor sem diff. Comportamento de hoje, fora do escopo do card por decisao do plano; rota: AE-<n> na secao 9 do plano, como o proprio card preve. |

## Lições aprendidas na tarefa


