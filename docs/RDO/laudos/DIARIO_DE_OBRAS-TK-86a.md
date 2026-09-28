# Laudo — DIARIO_DE_OBRAS · TK-86a

**Percentual:** 94%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | conforme |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | parcial |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| registro | parcial | a Medida do executor saiu 'ausente' no dossie de evidencia: a medida foi gravada como docs/RDO/evidencia/P-0751-TK-86a-medida.json (id do plano orquestrador P-0751) e nao como DIARIO_DE_OBRAS-TK-86a-medida.json, o nome que review_evidence.py procura para ticket do diario (precedente na mesma pasta: DIARIO_DE_OBRAS-TK-91a-medida.json); as seis Verificacoes foram re-medidas pelo reviewer (V1 exit 0 'check: OK'; V2 0; V3 2 passed; V4 114 passed; V5 428 passed exit 0; V6 0), mas a afirmacao de verde da execucao nao chegou pelo unico canal admitido |

## Achado de processo

| alvo | achado |
|---|---|
| doutrina | pantonic-executor.md item 5a e scrum-master Passo 5 fixam '<P-n> o id do plano (P-0752, nunca o caminho)', forma que nao cobre ticket residente em docs/DIARIO_DE_OBRAS.md, cujo id em review_evidence.py:787 e o stem 'DIARIO_DE_OBRAS'; a execucao escolheu P-0751 (plano orquestrador) e a medida ficou invisivel ao reviewer. Rota: ticket indexado no diario para emendar o item 5a e o Passo 5 com o id derivado como review_evidence.py o deriva (stem do plano legado/diario), de preferencia com o card_check.py --gravar calculando o destino sozinho |
| dossiê | dossie de evidencia sem o hunk da entrega: .claude/tools/encerrar.py e untracked ('??'), e o trecho colado e o cabecalho do arquivo truncado em 4000 caracteres, sem as linhas 680-683 do item 4; e o recorte --desde do redespacho (04a5ae0) marca backlog.py e tests/test_backlog.py 'sem alteracao', deixando os itens 1-3 fora da evidencia. O julgamento exigiu abrir o repositorio e o git diff HEAD. Rota: ticket indexado para review_evidence.py recortar arquivo untracked pelas ancoras de linha do card e para o despacho de retomada levar a ref do despacho original junto com a do redespacho |

## Lições aprendidas na tarefa

Retomada apos blocked com ref --desde do redespacho: a evidencia mecanica cobre so o delta da retomada (item 4), e os itens 1-3 da primeira execucao so aparecem contra HEAD. Em card com retomada, o despacho do reviewer precisa das duas refs.
