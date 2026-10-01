# Laudo — P-0755 · RAF-T29

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido na Restricao do card como unico achado, DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19..T28; os simbolos novos _numero_do_plano e _prefixo_decisoes_checks tem chamador (check) e o detector nao os acusa; pytest re-rodado 612 passed = 610 do RAF-T28 + os 2 testes novos, exit 0; backlog.py check na raiz sai 0 sem linha C-18; ratchet, validate, check-drift e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base que o proprio card admite; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Criterio (viii) da rubrica (AE-12): o card acrescenta C-18 ao vocabulario do check e nao fecha a frase que o conta - a docstring do modulo .claude/tools/backlog.py segue dizendo 'C-1..C-17' e 'vocabulario do instrumento fechado em C-1..C-17' (linhas 3 e 7) e o comentario de secao da linha 592 idem; a execucao seguiu o card a letra e nao decidiu editar. Rota: AE-<n> na secao 9 do P-0755, card de reparo que atualize as tres frases (e qualquer outra enumeracao do vocabulario do check fora do modulo) para C-1..C-18. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta em copias fora do repositorio confirmou a regra alem dos dois testes: tres planos com o mesmo prefixo acusam os dois nao-donos nomeando o de menor numero independente da ordem de arquivo; plano em pasta (plano.md) colide com plano plano; linha de bullet com o campo e ignorada; sobre a arvore real 15 de 35 planos declaram prefixo e nenhum repete. A assercao de exit 1 do TF nao discrimina sozinha - a fixture verde com os dois planos novos ja sai 1 por C-16/C-10 alheios -; quem discrimina e a assercao da linha C-18, que o teste tambem faz.
