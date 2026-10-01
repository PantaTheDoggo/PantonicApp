# Laudo — P-0755 · RAF-T6

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
| guardas | parcial | dead_code sai 1 so por docs/audits/sonda-2026-09-28/passos.py:13 (untracked, fora dos Arquivos-alvo, achado pre-existente admitido pelo card e pelo despacho via DRF-44); re-rodado na revisao: o mesmo 1 achado, nenhum novo; pytest --co 541 collected (piso 536 do despacho + 5 novos); check-drift exit 0; demais guardas exit 0 no dossie |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia apos RAF-T1..RAF-T5: o dossie de evidencia segue marcando guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o proprio despacho declara; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |
| dossiê | contrato do card incoerente no separador duplo-pipe (OU logico): dividir_segmentos o reconhece como separador, mas o card manteve inalterada a condicao de passthrough de main() que recusa qualquer comando com o caractere pipe, entao comando encadeado por OU logico (ex.: pytest -q seguido de OU echo falhou) nunca chega a reescrever() e segue sem filtro (exit preservado, saida nao encurtada); exercitado na revisao: main() devolve {} para esse comando. A entrega seguiu o card fielmente. Rota: AE-<n> na secao 9 do P-0755, candidato a card que restrinja o guarda de pipe ao pipe simples |

## Lições aprendidas na tarefa


