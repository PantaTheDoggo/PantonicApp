# Laudo — P-0753 · AF-T12

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
| criterio-de-pronto | parcial | grava os tres lugares no caminho feliz (verificacoes 1 e 2 verdes, 4/4 testes, suite 482 = piso 478+4), mas falha em dois caminhos exercitados numa copia temporaria do P-0753: (a) a celula e reescrita por split no caractere pipe sem respeitar o pipe escapado que o proprio verbo emite, e gravar de novo um marco cuja frase anterior tinha pipe deixa pedaco do veredito velho na celula; (b) Marco 1 go cuja transicao o backlog recusa (ex.: linha de indice ausente) grava o plano e so depois sai exit 1 'marco: status: ...', o que viola a Restricao 'todas as checagens antes da primeira escrita' - backlog.checar_transicao (TK-88d) existe para a checagem previa |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | AF-T12: o card nao traz aceite de coerencia do modulo (rubrica §8 (iv) e (xvii)). Nenhuma verificacao exercita a forma que o verbo emite (pipe escapado na celula) numa segunda gravacao, nem a recusa da transicao de status depois das escritas (1) e (2); por isso os dois defeitos do motivo passaram com a verificacao verde. Rota: item de replanejamento do P-0753, card corretivo AF-T12a da OP-12, com um TR para cada caminho |
| dossiê | AF-T12: o card prescreve _backlog.transacionar_status como escrita (3), que faz checagens proprias, e exige ao mesmo tempo 'todas as checagens antes da primeira escrita' sem dizer como conciliar (ex.: chamar checar_transicao antes da escrita (1)). Tambem ficaram sem fechamento: a forma de <plano> no dossie (a entrega usou caminho relativo ao repo), o strip() da frase e duas recusas a mais (plano sem id no nome; plano fora do backlog). Rota: o mesmo AF-T12a fecha isso no card |

## Lições aprendidas na tarefa


