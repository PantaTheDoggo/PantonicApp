# Laudo — P-0755 · RAF-T32

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
| guardas | parcial | dead_code exit 1 com um unico achado, docs/audits/sonda-2026-09-28/passos.py:13 (nao rastreado, fora dos Arquivos-alvo, nao tocado pela entrega), pre-existente e admitido pela restricao do card (§8 risco 5, DRF-44); reconciliado re-rodando na revisao: mesmo achado unico; pytest 626 passed exit 0, check-drift exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia: a evidencia marca guardas nao conforme pelo dead_code da sonda nao rastreada docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado) que o card admite; a revisao reconcilia a mao (passo 3a). Rota: somar ao AE da §9 do P-0755 que ja aponta para DRF-44 |
| dossiê | O recorte do card deixa o modulo incoerente: a regra 3 troca a tarefa nos ramos PreToolUse e PostToolUse sincrono do Agent e proibe mexer no UserPromptSubmit, mas o retorno assincrono (PostToolUse com handback=send, frase de volta no UserPromptSubmit <agent-message>) segue com tarefa_corrente; exercitado na revisao: 'Agente consultor recebe a tarefa "Outro"' seguido de 'Agente consultor devolveu a tarefa "Um"'. Alem disso o ramo PostToolUse sincrono alterado nao tem teste exigido pelo card, e ID casado sem card (localizar_card devolve o proprio ID) mostra o ID em vez de cair na tarefa corrente, como a regra 2 manda. Rota: item de replanejamento na §9 do P-0755 (card irmao que guarde o titulo despachado em pendentes[agentId] e teste o PostToolUse) |

## Lições aprendidas na tarefa

Os dois testes do card so exercitam o PreToolUse; o defeito de coerencia (recebe uma tarefa, devolve outra no retorno assincrono) so aparece exercitando o ciclo recebe/devolve inteiro do mesmo agente.
