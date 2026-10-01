# Laudo — P-0754 · AUF-T6

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
| dossiê | Caso simetrico fora do cerco do card: nao rastreado que era binario em <ref> (FF FE 00 81) e hoje se le como texto ('ola') derruba coletar_arquivos_tocados com AttributeError ('NoneType' object has no attribute 'splitlines'), porque _texto_do_ref decodifica como UTF-8 e devolve None; defeito anterior (o review_evidence.py de 55123364 falha igual) e o card fechou o ramo texto como 'nao muda', entao a entrega esta fiel. Rota: a conducao registra como AE-<n> na secao 9 do P-0754 e o leva como item de replanejamento (o ramo texto tambem compara pelo conteudo bruto quando o <ref> nao decodifica). |

## Lições aprendidas na tarefa

O TF discrimina de verdade: rodado contra o review_evidence.py do recorte 55123364 (numa copia em pasta temporaria), o arquivo binario intocado sai ['imagem.bin']; contra a entrega, sai []. Tambem se exercitaram, alem dos dois testes, o binario apagado depois do recorte e o que passou de texto a binario: os dois entram nos tocados e no diff-stat, como devem. O teste final da AUF-T5 segue integro, com a assercao coletar_diff_stat dentro dele; o numstat e 15/2 e 33/0, so acrescimo ao fim do arquivo de testes; a suite fecha 518 passed.
