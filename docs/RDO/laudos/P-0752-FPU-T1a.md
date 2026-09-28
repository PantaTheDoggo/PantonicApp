# Laudo — P-0752 · FPU-T1a

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

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Evidência de FPU-T1a lista 31 arquivos '??' sem atribuição (tocados alheios); reconciliado por mtime: todos anteriores ao despacho (1a1ec9d, 10:34:01-03) e a entrega só escreveu os dois alvos (10:35:33/10:35:39). Mesma causa do AE-35; rota: TK-84a (já aberto), sem ação nova. |

## Lições aprendidas na tarefa

Poder discriminante conferido em memória, sem escrever no repositório: com _parsear_itens trocado por uma versão que achata as linhas do campo e parte em qualquer 'N.' precedido de espaço, CX-T5 cai (ok=False, 'item 1/2: fora da forma da 8.1') e CX-T4 continua verde (ok=True, 1 item). Isso confirma o AE-34: o TF antigo não trancava o marcador só no início de linha, e o novo tranca. Fixture: CX-T1..CX-T4 idênticos ao retrato do FPU-T1; mudaram só o parágrafo de abertura (Quatro->Cinco, mais a frase do CX-T5) e o card CX-T5 novo. O TF passa _PLANO_CORPUS sem o str() do Passo 2; verificar_tarefa aceita Path, então é detalhe equivalente e não desvio.
