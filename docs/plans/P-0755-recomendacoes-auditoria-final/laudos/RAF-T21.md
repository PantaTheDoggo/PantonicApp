# Laudo — P-0755 · RAF-T21

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, nao rastreado, admitido no card e na nota do despacho como DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19/T19a; pytest 593 passed = piso 590 collected do despacho + os 3 testes novos, exit 0; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py) sem carregar a linha de base admitida no despacho; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | Parada nao prevista pelo card: a regra 2 original (um texto por numero, o ultimo vence) derrubava test_tf_check_invalido_lista_catorze_violacoes_na_ordem (EX2-T3 copia o primeiro de dois OP-3), e o primeiro despacho parou blocked premissa pela contingencia 1 - defeito de autoria (o ensaio nao rodou a regra contra a suite existente, criterio (xix)/(xii)(b) da rubrica §8). Rota: ja corrigida pela DRF-61 do consultor (regra 2 reescrita); sem acao nova, registrar como AE-<n> na secao 9 apontando para DRF-61. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta nesta revisao, em raiz temporaria fora do repositorio, com e sem --so-vigente: card que copia o texto novo da pendente para numero que existe na vigente sai 0 (DRF-37); card que copia texto da vigente com a pendente reescrita sai 0; texto que nao e nenhum sai V22 versao 1; OP-2 so-pendente com texto de OP-1 sai V22 versao 2; numero duplicado na vigente com copia do primeiro texto sai so V8/V11, sem V22 (DRF-61); tabulacao e espacos multiplos colapsam; OP-9 inexistente sai so V4. Forma da mensagem V22 casa com V4/V14 ('V<n> <ID> — ...'). Planos reais: P-0754 e P-0755 saem 0; os quatro encerrados saem 1 com exatamente 1/7/5/1 linhas V22, como o card mediu. show segue exit 0 e o --help publica V1..V22. OP-21 confere com a entrega: sem conflito de modelo. A parada do primeiro despacho custou um despacho inteiro mais uma passagem de consultor por um caso que o ensaio do card teria revelado rodando a regra contra a suite existente.
