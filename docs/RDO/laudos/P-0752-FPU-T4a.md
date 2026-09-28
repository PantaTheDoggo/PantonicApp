# Laudo — P-0752 · FPU-T4a

**Percentual:** 100%
**Veredito:** aprovado
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | conforme |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Achado de processo

nenhum

## Lições aprendidas na tarefa

A secao Escopo do dossie de evidencia listou 31 arquivos fora dos alvos e sem atribuicao; todos eram '??' anteriores ao despacho (caso conhecido AE-35 / TK-84a). A reconciliacao por mtime contra o commit de recorte cd90fc6 (11:37:45) mostrou que so os dois alvos (crenca_hook.py 11:38, test_crenca_hook.py 11:39) mudaram depois dele, mais o registro da orquestracao (medida, telemetria, diario, plano). Como os dois alvos sao '??' desde a FPU-T4, o 'diff' colado e o arquivo inteiro: o delta real da FPU-T4a (lista de trechos e soma por grupo em contar_crencas) so se le no laco, e nao num hunk. O exercicio ponta a ponta confirmou a contagem por grupo em dez casos (prosa, antes/depois com e sem passed, Medido antes, ancora com e sem literal, linha de comando, bloco cercado, duas linhas, casamentos disjuntos na mesma linha) e o gancho pela linha de comando com payload real: aviso '2', exit 0.
