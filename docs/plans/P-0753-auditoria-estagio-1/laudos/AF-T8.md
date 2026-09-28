# Laudo — P-0753 · AF-T8

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
| criterio-de-pronto | parcial | O predicado _plano_em_esboco (backlog.py:600-601) omite a cláusula 'plano em pasta cujo estado.tsv existe' do Domínio: plano legado (arquivo único) com **Status:** blocked, id igual ao contador e fora do _INBOX.md passa a ser silenciado no C-10 — reproduzido em cópia temporária da fixture contador_inbox com Status trocado para blocked: antes da entrega C-10 acusado, depois não; viola o contrato 'o resto do C-10 não muda (plano que não está em esboço segue acusado)'. Correção: exigir plano.estado_arquivo presente (plano em pasta) no predicado e um TR com plano legado blocked. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | A Verificação e o par TF/TR do AF-T8 só discriminam a transição 'linha de tarefa entra no estado.tsv'; nenhuma linha exercita a cláusula 'plano em pasta' do Domínio, e por isso a perda de C-10 para plano legado blocked passou verde. Rota: item de replanejamento do P-0753 — card corretivo que estreita o predicado ao plano em pasta e acrescenta TR com plano legado blocked, id = contador, fora do inbox (deve sair 1 com C-10). |

## Lições aprendidas na tarefa


