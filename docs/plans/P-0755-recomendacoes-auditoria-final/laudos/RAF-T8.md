# Laudo — P-0755 · RAF-T8

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
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), arquivo nao rastreado fora dos alvos e nao tocado pela entrega, admitido no despacho como pre-existente; pytest, ratchet_piso, kit_check validate/check-drift e check_readme em exit 0; suite 552 coletados = piso 549 + os 3 testes novos |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | RUBRICA_DE_REVISAO.md §3 (linhas 48-53) ainda descreve a secao '## Arquivos tocados' com dois rotulos, 'da entrega' ou 'alheio'; a entrega (fiel ao card) criou o terceiro, 'registro da orquestracao', e o card nao pos a frase da rubrica nos Arquivos-alvo (criterio (viii) da §8). Rota: AE-<n> na §9 do P-0755, para card que emende a frase da §3 da rubrica ao novo rotulo. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta pela CLI num repositorio descartavel (com e sem --desde, e --atribuir) confirmou coerencia do modulo: binario novo abre com a marca nos dois ramos, a lista por arquivo e o resumo '## Escopo' usam o mesmo nome para o registro da orquestracao, e o --atribuir segue com registro-da-orquestracao, como o card manda preservar. O ramo TK-93a (nao rastreado ja presente no ref, binario) segue sem marca, correto por nao ser arquivo novo.
