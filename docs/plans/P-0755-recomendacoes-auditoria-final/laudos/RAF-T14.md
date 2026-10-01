# Laudo — P-0755 · RAF-T14

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (arquivo nao rastreado, fora dos Arquivos-alvo, admitido no despacho como DRF-44); reconciliado no ato: nenhum achado novo da entrega; pytest 578 passed = piso 573 + 5 novos; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | dead_code vermelho pre-existente (docs/audits/sonda-2026-09-28/passos.py, DRF-44) segue admitido no despacho e nao carregado pelo dossie de evidencia: guardas sai parcial em toda tarefa do P-0755 enquanto o arquivo viver na arvore. Rota: a mesma do achado do laudo RAF-T13 (item de replanejamento, AE na secao 9 do P-0755) - linha de base admitida no review_evidence.py ou recorte de docs/audits/ no dead_code |
| dossiê | Passo 2 inalcancavel como escrito: manda conferir que 'os quatro TF falham e o TR passa', mas a secao Testes fixa para o TR test_tr_ref_do_despacho_de_outra_tarefa_falha a mensagem nova 'item 1: <ref> sem recorte do despacho para RX-T1', que so existe depois da regra 4; reproduzido pelo reviewer numa copia fora do repo com o card_check.py do ref 2d242634: 5 failed (4 TF + o TR, que falha com 'divergencia ... saida <ref>'). Executor que rodasse o Passo 2 fielmente pararia por duvida que o card nao previu (G-NOASK). Rota: item de replanejamento do P-0755 (AE na secao 9), registro para o criterio (ix) da secao 8 da rubrica - TR que confere mensagem nova nao e regressao que passa antes |
| doutrina | a checagem de vermelho do TDD (Passo 2) nao deixa rastro mecanico: o dossie de evidencia so admite a medida verde do executor, e o salto do Passo 2 nesta tarefa so e conhecido por relato do executor; a prova foi recuperada pelo reviewer por reproducao fora da arvore. Rota: tiquete indexado (AE na secao 9 do P-0755) - medida do mundo vermelho dos TF gravada antes da implementacao e colada no review_evidence.py, ou o passo sai dos cards como verificacao nao auditavel |

## Lições aprendidas na tarefa

Exercicio ponta a ponta (plano sintetico fora do repo, --root no repo, tarefa-corrente.json real de RAF-T14): git diff --exit-code <ref> --numstat na forma inline e na de bloco cercado com (invariancia) fica 'nao medida' em antes, sem exigir Medido antes, e em depois sai 0 para rdo.py (inalterado) e 1 para card_check.py (alterado) - a linha de invariancia discrimina; git show com <ref> troca pelo ref de 40 caracteres nos dois mundos; git -C, git sozinho e git stash sao recusados nomeando o segundo token; tarefa diferente da do tarefa-corrente.json falha nomeada em todo item com <ref>; --gravar registra o comando ja trocado. card_check sobre os 41 cards do P-0755 sai 0 em todos menos o proprio RAF-T14 no mundo antes (status review, antes exit 5 consumido - sai 0 em --mundo depois), mesmo padrao do RAF-T13. O TDD pulado pelo executor foi reposto por reproducao: os 4 TF falham no codigo do ref pelas razoes que os docstrings declaram.
