# Laudo — P-0753 · AF-T17

**Percentual:** 91%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | parcial |
| escopo | conforme |
| testes | conforme |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| criterio-de-pronto | parcial | Exercicio ponta a ponta: o pre-voo silencia citacao em crase ou com pontuacao e chamada com parenteses fechados - 'use `ler_texto_utf8` de `.claude/tools/caminhos.py`, e rode com `--desde`.' e 'chame funcao_inexistente()' saem com tabela sem item e exit 0 (o ultimo contra o proprio contrato 'nome seguido de ('); 'com --plano;' vira citado '--plano;' com nao. O caso medido que motivou o card (funcao citada e ausente) passa sem alarme na forma de citacao que o kit usa; Verificacoes 1-3 verdes, 'cada caminho, nome e opcao citados' nao. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Contrato do AF-T17 nao define 'token': a entrega escolheu str.split() sem remover crase, virgula, ponto, ponto-e-virgula nem parenteses, e nenhuma linha de Testes/Verificacao traz citacao em crase ou pontuada (criterio (xvii)/(ix) da §8: o aceite nao exercita a forma que o pedido real usa). Rota: item de replanejamento do P-0753 - card de correcao do prevoo.py fixando a normalizacao do token e um TF com pedido em crase e com 'nome()'. |
| dossiê | Contrato diz 'na ordem da primeira aparicao', mas o TF do proprio card lista o caminho antes do simbolo que aparece primeiro no texto; a entrega decidiu 'ordem por categoria (caminhos, simbolos, flags)' e declarou no docstring. Decisao que o card nao fechou (G-NOASK). Rota: item de replanejamento do P-0753 - o mesmo card de correcao fixa a ordem por categoria no Contratos/classes. |
| dossiê | A contingencia do card manda apensar linha a tests/piso_comportamental.txt, arquivo fora dos Arquivos-alvo e contra a Restricao 'so os Arquivos-alvo se editam'; o dossie de evidencia marcou o arquivo como alheio sem atribuicao. A entrega apensou exatamente uma linha (o TR novo, forma '<nodeid> - <frase>'), escopo conforme. Rota: item de replanejamento do P-0753 - card com contingencia que escreve em arquivo o lista em Arquivos-alvo como condicional. |

## Lições aprendidas na tarefa

Os tres testes do card fixam o comportamento sobre texto ja limpo (tokens separados por espaco, sem crase); o defeito so aparece quando o instrumento recebe um pedido escrito como o dono escreve. Instrumento que le prosa pede, no card, um caso de aceite com a prosa real.
