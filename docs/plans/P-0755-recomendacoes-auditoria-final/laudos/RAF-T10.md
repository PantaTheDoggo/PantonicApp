# Laudo — P-0755 · RAF-T10

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo, achado pre-existente admitido pelo card e pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo, _extrair_caminho_status removido sem sobra; pytest --co 556 collected (554 do despacho + 2 novos); tests/test_review_evidence.py 90 passed; check-drift exit 0; demais guardas exit 0 no dossie |

## Achado de processo

| alvo | achado |
|---|---|
| modelo | OP-10 diz que o dossie de evidencia recebe inteiro o nome acentuado que o versionador lista, mas a entrega (fiel ao card) so cobre o git status -z: exercicio ponta a ponta com core.quotepath ligado e arquivo rastreado 'trilha acao.md' (com cedilha/til) editado depois do ref mostra, via git diff <ref> --name-only, o tocado como "trilha a\303\247\303\243o.md" (aspas e escape octal), atribuido alheio, e coletar_estado_git com duas chaves para o mesmo arquivo. Rota: dossie Ato de modelo de conflito devolvido com o laudo, ao pantonic-model-designer por quem conduz a sessao |
| dossiê | O Fora do escopo da RAF-T10 excluiu git diff <ref> --name-only/--name-status e pediu o julgamento da revisao: julgado defeito (mesma evidencia do achado de modelo: caminho rastreado acentuado chega com escape octal e duplica chave em coletar_estado_git). Rota: AE-<n> na secao 9 do P-0755, card corretivo com -z (ou core.quotepath=false por invocacao) nas duas leituras de git diff |
| dossiê | _CAMINHO_RE de review_evidence.py e ASCII-only: um arquivo acentuado declarado em Arquivos-alvo sai como Literal nao reconhecido como caminho, o tocado acentuado vira alheio e o dossie nao cola o trecho dele; o Pronto quando (chega com a sua diferenca, como qualquer outro) so vale em montar_trechos com alvos explicitos, que e o que a Verificacao 1 exercita. Rota: AE-<n> na secao 9 do P-0755 |
| dossiê | Prosa residual que o card nao mandou tocar: o docstring de coletar_arquivos_tocados ainda descreve o ramo do git status com nome entre aspas e escape octal, e a primeira linha do de coletar_estado_git cita o comando sem -z. Rota: AE-<n> na secao 9 do P-0755, junto do card corretivo do achado anterior |
| dossiê | Reincidencia na janela do P-0755 (apos RAF-T1..RAF-T9a): o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o despacho declara. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa


