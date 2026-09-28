# Laudo — P-0753 · AF-T10

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
| criterio-de-pronto | parcial | Contrato 'a razao e a ultima linha do stderr' violado: os subprocessos (modelo.py, card_check.py, review_evidence.py) reconfiguram stderr para UTF-8 e despachar decodifica com a codificacao do locale (text=True sem encoding, cp1252 no Windows) - exercicio ponta a ponta na copia da fixture: 'despachar: recusado — card_check: card_check: FALHOU - 1 item(ns) da tarefa 'GAM-T2' nÃ£o fecham.'; e byte UTF-8 indefinido em cp1252 (ex.: 'Á' = C3 81 num literal de card ecoado) faz o leitor do subprocess falhar, stderr volta None e _ultima_linha_stderr(None) quebra com traceback em vez de exit 1. Correcao: encoding='utf-8', errors='replace' nos quatro subprocess.run (o de pytest --co tambem, por simetria). O resto do criterio tem contrapartida: gates na ordem, recusa sem escrita (estado.tsv e tarefa-corrente.json intocados), in-progress, json com os seis campos, saida DESPACHO/HANDOVER/card/ref=, redespacho reaproveitando ref. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Contratos/classes fixou 'a razao e a ultima linha do stderr' sem fixar a decodificacao do stderr dos irmaos (que escrevem UTF-8), e o TR so afere o prefixo 'despachar: recusado — card_check:' - nenhuma linha de Verificacao nem de Testes discrimina o texto da razao, e a mojibake passou verde. Rota: item de replanejamento do P-0753 na operacao do despacho (OP-10) - a correcao do encoding e um assert sobre o texto da razao ('não fecham') no TR, na auditoria final (diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste). |
| dossiê | Decisao que o card nao fechou (G-NOASK): 'Contratos/classes' manda '--plano <plano>' sem dizer se relativo ou absoluto; a entrega escolheu caminho absoluto (repo / pai.arquivo) porque card_check.verificar_tarefa usa Path(plano) sem juntar --root. Escolha correta e declarada em comentario no alvo; rota: item de replanejamento do P-0753 na operacao do despacho, para o card fixar a forma do argumento. |
| dossiê | docs/ACIONAMENTOS_CONSULTOR.tsv, escrito pelo consultor na triagem do blocked desta tarefa, sai no dossie de evidencia como fora dos alvos e sem atribuicao; reconciliado pela declaracao de desvio da orquestracao, escopo da entrega = os 3 alvos. Rota: sem acao - reincidencia do AE-4, ja roteado a auditoria final. |

## Lições aprendidas na tarefa

O defeito so apareceu rodando o verbo pela CLI numa copia da fixture: os tres testes chamam main() em processo e o TR confere so o prefixo da recusa, entao a decodificacao do stderr dos filhos nunca foi olhada. Verbo que orquestra irmaos por subprocess precisa de ao menos um aceite sobre o texto que atravessa a fronteira do processo.
