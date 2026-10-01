# Laudo — P-0755 · RAF-T27

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
| guardas | parcial | dead_code sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (fora dos Arquivos-alvo, admitido na Restricao do card como unico achado, DRF-44); reconciliado no ato: blob 8ee3de5, o mesmo dos laudos RAF-T19..T26a; os simbolos novos da entrega (_RE_EXTENSAO_CURTA, _VERBOS_DE_CRIACAO, _RE_FIM_DE_FRASE, _caminhos_a_criar) nao aparecem no detector; pytest re-rodado 608 passed = piso 604 do RAF-T26a + 4 testes novos, exit 0; ratchet, validate, check-drift e check-readme em exit 0 na evidencia |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base que o proprio card admite; cada revisao reconcilia a mao. Rota: DRF-44 ja aberta na secao 9 do P-0755; registrar a reincidencia como AE-<n> apontando para ela. |
| dossiê | O card RAF-T27 fixou as tres regras e nao mandou acertar a docstring do modulo .claude/tools/prevoo.py (linhas 13-15), que segue descrevendo caminho como 'token terminado em uma das nove extensoes ou em /' e so os valores sim/nao, sem a regra de extensao curta com '/', sem o nome solto que nao comeca por '.', e sem o valor 'criar' nem a regra de verbo na mesma frase; o card tambem nao declarou aceite de coerencia do modulo (RUBRICA 8, criterio iv). A entrega seguiu o card sem decidir por conta propria, e o comportamento esta certo; so a documentacao do cabecalho do instrumento ficou falsa. Rota: AE-<n> na secao 9 do P-0755 com card de acerto da docstring de prevoo.py. |

## Lições aprendidas na tarefa

Exercicio ponta a ponta pela CLI, na raiz real: 'Crie .claude/tools/novo.py ... leia .claude/tools/prevoo.py. Grave docs/y.md; ... README.md' deu novo.py e y.md como criar, prevoo.py e README.md como sim, simbolo e flag inalterados, exit 1 so pelo simbolo ausente - as tres colunas e a tabela de exit seguem coerentes. Discriminacao conferida contra o prevoo.py da ref 643d75d: os dois TF saem como o card diz (.txt | nao e exit 1; seis linhas nao, com .txt no lugar de c.bin, e exit 1), e o TR da mesma frase ja passava. Bordas fieis a letra das regras, sem defeito de entrega, que o planejador pode querer ver: quebra de linha entre o verbo e o caminho tira o caminho do conjunto (gerar\ndocs/z.md sai nao); ponto sem espaco nao fecha frase (docs/a.md.Leia vira caminho a criar); o conjunto nao guarda posicao, entao 'leia docs/c.md e crie docs/c.md' sai criar; URL com extensao no ultimo segmento (https://x.com/a.html) conta como caminho.
