# Laudo — P-0755 · RAF-T15

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (arquivo nao rastreado, fora dos Arquivos-alvo, admitido na Restricao do card e no despacho como DRF-44); reconciliado no ato: nenhum achado novo da entrega; pytest 582 passed = piso 578 + 4 novos; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | reincidencia da DRF-44 (apos AE-121..AE-160): o dossie de evidencia marca guardas nao conforme pelo dead_code da sonda untracked docs/audits/sonda-2026-09-28/passos.py sem carregar a linha de base (1 achado admitido) que o card e o despacho declaram; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta no P-0755; registrar a reincidencia como AE-<n> na secao 9 apontando para ela |
| doutrina | reincidencia do AE-162 (DRF-57): o Passo 4 (checagem de vermelho do TDD), pedido no despacho como passo proprio, nao deixa rastro mecanico no dossie de evidencia; a prova foi reposta pelo reviewer por reproducao fora da arvore (codigo do ref 55117ff + testes da entrega: 5 failed = 3 TF + 2 reescritos, 1 passed = o TR, exatamente o que o Passo 4 manda). Rota: AE-162 com rota auditoria final (diretiva de 2026-09-26); registrar a reincidencia como AE-<n> na secao 9 apontando para ela |

## Lições aprendidas na tarefa

Exercicio ponta a ponta fora do repo (arvore real com plano em pasta e plano legado, --root numa copia com rdo.py/caminhos.py da entrega): card_check --gravar sem caminho grava na pasta do plano sob a copia com -antes/-depois no nome (mundo de --mundo ou derivado do status), plano legado cai em copia/docs/RDO/evidencia com -antes, --gravar com caminho segue inalterado, e a arvore real nao ganha pasta de evidencia; montar_documento le a de depois, na falta dela a de antes, e a medida sem mundo ao lado do --out vence a da raiz, como o contrato 3 manda; as 20 medidas sem mundo do P-0753 seguem resolvidas por destino_medida(..., None) (20 de 20). O proprio dossie desta revisao ja leu P-0755-RAF-T15-medida-depois.json pelo caminho novo. Nota fora do card: em plano em pasta sem estado.tsv o mundo derivado e antes mesmo com bullet Status done (rdo._status_atual le o estado.tsv da arvore do --plano, nao da --root) - comportamento anterior, nao tocado pela entrega.
