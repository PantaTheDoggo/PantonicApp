# Laudo — DIARIO_DE_OBRAS · TK-93a

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
| criterio-de-pronto | parcial | O objetivo 1 fixa a árvore do <ref> como 'a árvore de trabalho inteira — rastreados e não rastreados não ignorados', e capturar_ref popula um índice temporário VAZIO com 'git add -A', que pula todo arquivo rastreado que casa com o .gitignore (git ls-files -ci): exercitado em repositório temporário com 'forcado.log' commitado por 'add -f' e intocado, o <ref> sai sem ele e o dossiê o lista em tocados como 'fora dos alvos e sem atribuição', estado 'A (commitado desde <ref>)', derrubando o veredito mecânico de escopo de 'conforme' para 'aberto' — regressão frente ao 'git stash create' que o Passo 4 aposentou, que carrega esses arquivos. Latente no PantonicApp (0 arquivos nessa classe), vivo no PantonicVideo (4, pantonicvideo_contracts.egg-info/*). Correção de uma linha: 'git read-tree HEAD' no índice temporário antes do 'add -A' (sem HEAD, índice vazio como hoje). O restante do critério tem contrapartida verificada: hunk do não rastreado editado sem truncar, só o que mudou em tocados, CRLF normalizado, estado '??', árvore/índice/lista de stash intactos (conferido por hash do .git/index), repositório sem commit sai sem pai, --plano/--tarefa seguem obrigatórios sem a flag, --atribuir coerente com o dossiê, e o Passo 4 com o texto do bloco novo (0 1 1). |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Duas classes que o card não fechou nem discriminou: (a) rastreado-e-ignorado — o card escreveu 'rastreados' no contrato da árvore, mas nenhuma Verificação nem TF o exercita, e o protótipo do consultor não o pegou (critério (vi) da §8: entregável que interage com o .gitignore sem ser confrontado com ele); (b) não rastreado binário ou não-UTF-8 presente no <ref> — o card manda comparar 'linha a linha com o fim de linha normalizado' e não diz o que fazer quando o texto não decodifica; a entrega DECIDIU tratá-lo como sempre mudado (_nao_rastreado_mudou_desde_ref devolve True quando _texto_do_disco dá None), de modo que um binário intocado desde a captura entra em tocados em toda evidência (exercitado: img.bin e latin.txt intocados saem em tocados). De quebra, coletar_estado_git rotula 'D (commitado desde <ref>)' o não rastreado capturado e depois apagado, que nunca foi commitado. Rota: item de replanejamento do TK-93 em docs/DIARIO_DE_OBRAS.md — card de retrabalho (TK-93b) com 'read-tree HEAD' no índice temporário, a regra fechada para o não rastreado sem texto (comparar bytes do blob contra os do disco) e dois TF, um por classe. |

## Lições aprendidas na tarefa

O instrumento que troca 'git stash create' por captura própria herda a obrigação de reproduzir o que o stash já fazia de graça: o stash parte do índice de HEAD, e um índice temporário vazio não parte. Exercício ponta a ponta em repositório com arquivo forçado ('add -f') e binário não rastreado revelou os dois furos que os TF de texto puro nunca tocam.
