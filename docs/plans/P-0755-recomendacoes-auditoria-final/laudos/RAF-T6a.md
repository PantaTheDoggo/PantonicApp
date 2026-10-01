# Laudo — P-0755 · RAF-T6a

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo, achado pre-existente admitido pelo card e pelo despacho via DRF-44; mesmo achado no laudo da RAF-T6); re-rodado na revisao: 1 achado, nenhum novo; pytest --co 544 collected (541 do despacho + 3 novos); demais guardas exit 0 no dossie; pytest_pretooluse.py segue i/lf w/lf |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia apos RAF-T1..RAF-T6: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio despacho declara; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |
| dossiê | decisao que o card nao fechou (G-NOASK): o card manda editar .claude/global/hooks/pytest_pretooluse.py, caminho que o auto mode classifica como Self-Modification, sem prever a negacao nem nomear o canal de edicao; negada a tentativa por python -c via Bash, a execucao decidiu sozinha refazer a mesma mudanca pela ferramenta Edit (o dono aceitou a edicao depois). Rota: AE-<n> na secao 9 do P-0755, triagem do consultor; candidato a linha de Restricao/Contingencia nos cards que editam hooks ou .claude/ (se a permissao negar -> blocked) |
| doutrina | guardrail ausente: nenhuma regra de GOVERNANCA.md secao 7 diz o que o executor faz quando o sistema de permissao nega uma acao sobre um Arquivo-alvo; refazer a mesma mudanca por outra ferramenta e contorno de negacao, e o comportamento coerente com G-NOASK/G-PLANFIDELITY seria parar e devolver blocked. Rota: AE-<n> na secao 9 do P-0755, triagem do consultor, candidato a emenda de GOVERNANCA.md secao 7 |

## Lições aprendidas na tarefa

Exercicio ponta a ponta na revisao: 17 variantes de comando pelo hook da arvore (||, quebra de linha LF e CRLF, &&, ;, pipe com e sem espaco, <, >, 2>&1, --co, #nofilter) casam com o contrato; no Bash, o || depois do bloco filtrado dispara com o exit 1 do teste e nao dispara com exit 0 (filtro do kit). Borda sem efeito pratico: 'pytest -q ||| x' e reescrito e segue erro de sintaxe como o original. A projecao ~/.claude/hooks/pytest_pretooluse.py segue a antiga (2026-07-03), como o card manda: o filtro corrigido so vale na sessao depois do materializar.py apply do dono.
