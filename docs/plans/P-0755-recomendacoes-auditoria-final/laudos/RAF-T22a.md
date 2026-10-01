# Laudo — P-0755 · RAF-T22a

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido na restricao do card, §8 risco 5); reconciliado no ato da revisao: mesmo achado unico, nenhum novo; pytest exit 0 (tests/test_modelo.py 48 passed = 46 datados + 2 novos); ratchet, kit_check validate/check-drift e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base que o proprio card admite; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | O card fixou a forma '[~] OP-<k> — precisa de: <vigente> => <pendente>' com listas unidas por ', ' e nao fechou a lista vazia: operacao cujo precisa de/altera sai de ou vai para vazio emite 'precisa de:  => z' (dois espacos, lado em branco), exercitado na revisao via montar_drift. A entrega aplicou a regra ao pe da letra, sem decisao propria. Rota: AE-<n> na secao 9 do P-0755, sem acao salvo se o dono quiser marcador de vazio (ex.: '—') num card futuro. |

## Lições aprendidas na tarefa

O exercicio ponta a ponta pelo verbo (show --drift sobre tests/fixtures/modelo/fluxo-pendente.md e fluxo-pendente-contrato.md) mostra que o parser alimenta a regra nova: as duas fixtures agora ganham linha de contrato no Fluxo ([~] OP-1 — altera: ... e [~] OP-3 — precisa de: ...), e os testes de CLI existentes seguem verdes porque aferem so os marcadores, nao essas linhas. Casos combinados (renumeracao + contrato, texto novo + contrato, ordem invertida da lista) conferidos em memoria e coerentes com a regra do card; o TF/TR do card cobrem so o par de texto e numero iguais.
