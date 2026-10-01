# Laudo — P-0755 · RAF-T31

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
| guardas | parcial | dead_code exit 1 com um unico achado, docs/audits/sonda-2026-09-28/passos.py (untracked, fora dos Arquivos-alvo), pre-existente e admitido pelo card (§8 risco 5); re-rodado na revisao: mesmo achado unico, nenhum novo; pytest 624 passed exit 0, check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Vermelho mecanico de guardas vem de docs/audits/sonda-2026-09-28/passos.py, pasta nao versionada fora da entrega, e a evidencia o reporta como 'nao conforme' sem carregar a admissao que o card faz (§8 risco 5); rota: AE na §9 do P-0755 para excluir a sonda do alcance do dead_code ou declarar a admissao na bateria, e o card que absorve a sonda |
| dossiê | Regra 4 do card manda o append com --agente ir direto a gravar_por_agente, sem checar_repetida (DFP-8); a docstring de append_row/checar_repetida segue dizendo que a recusa 'vale para todo escritor', o que deixou de ser verdade no caminho do hook; o card nao fechou se DFP-8 se aposenta (substituida pela chave de agente) ou se estende a gravar_por_agente; rota: AE na §9 do P-0755 com a decisao e o acerto da docstring |

## Lições aprendidas na tarefa

Exercicio ponta a ponta em raiz temporaria confirmou coerencia entre os dois verbos: executor sem estado com ID no despacho grava com projeto da raiz; executor sem ID nem estado nao grava; mesmo consultor em duas paradas fica em consultor-1 (substituido) e outro agente abre consultor-2; tiquete TK-12a casa; ID minusculo nao casa e cai em sem-id. A serie real ja foi migrada pela primeira parada pos-entrega: 1213 linhas, todas com 9 colunas.
