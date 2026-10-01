# Laudo — P-0755 · RAF-T9

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
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), arquivo nao rastreado fora dos alvos e nao tocado pela entrega, admitido nominalmente na restricao do card como pre-existente; pytest 554 passed (piso 552 + os 2 testes novos), ratchet_piso, kit_check validate/check-drift e check_readme em exit 0; reconciliado re-rodando dead_code, a Verificacao 1 e a suite |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia apos RAF-T1..RAF-T8a: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio card declara; a revisao reconcilia a mao (passo 3a). Rota: DRF-44 ja aberta no P-0755; somar a reincidencia ao AE-<n> que ja aponta para ela na secao 9 |
| dossiê | a restricao que congela as linhas existentes de tests/test_review_evidence.py deixou o docstring de test_tf_alvo_com_curinga_casa_os_tocados (linha 1459) dizendo que o curinga casa 'por fnmatch', mecanismo que esta entrega removeu; o card mandou trocar so o docstring de _eh_alvo_curinga. Rota: item de replanejamento na secao 9 do P-0755, a acertar pelo proximo card que ja edita tests/test_review_evidence.py (RAF-T11 ou sucessor) |

## Lições aprendidas na tarefa

Exercicio ponta a ponta em montagem descartavel: main() com alvo relatorios/*.md, relatorios/**/*.md e relatorios\*.md da atribuicao na lista de Arquivos tocados, fato de escopo e chaves de trecho coerentes entre si; 22 casos de borda da traducao (**/ no inicio, ** no fim, ?, [ e { literais) casam como o card especifica, e divergem do fnmatch exatamente onde o R-30 apontava.
