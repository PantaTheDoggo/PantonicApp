# Laudo — P-0753 · AF-T13

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

## Motivo das dimensões fora de conforme

nenhum

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | AF-T13: o contrato do --checar não tem poder discriminante para seção ausente — 'nao citados' conta o ID em crase em qualquer lugar do documento e a tabela do arco que o próprio esqueleto gera já cita toda tarefa, e 'sem os quatro blocos' só itera seções existentes; medido em cópia do P-0753: seção inteira de AF-T1 apagada, --checar sai 0 com 'nenhum'/'nenhum', enquanto o item 6 da skill promete 'toda seção de tarefa com os quatro blocos'. Rota: item de replanejamento do P-0753 — card que acrescente a linha 'sem seção: <ids>' (tarefa não cancelled sem '## `<ID>`') ao --checar, com TR que apaga a seção inteira. |

## Lições aprendidas na tarefa

Entrega fiel ao contrato do card, e o furo mora no contrato: a checagem de cobertura cruza o ID contra o documento inteiro, e o esqueleto gerado pelo mesmo verbo cita todo ID na tabela do arco — a checagem passa a ser verdadeira por construção. O exercício que o revela é apagar a seção inteira, não uma linha dela; o TF do card só apaga uma linha.
