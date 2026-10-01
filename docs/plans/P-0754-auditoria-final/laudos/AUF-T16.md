# Laudo — P-0754 · AUF-T16

**Percentual:** 90%
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
| residuo | nao-se-aplica |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| criterio-de-pronto | parcial | Dois itens do Pronto quando com o resto identificado. (1) Recomendacoes: 35 registros inadequado/oportunidade na §3, e 6 sem nenhuma R-<nn> nem declaracao de inviabilidade - reg. 13 (card_check na arvore real da Fase 5), 14 (item 14 x operacao 'igual'), 17 (prefixo de decisao colidindo), 18 (next sem filtro despeja card de outro plano), 27 (curinga fnmatch, AE-103/AE-104) e 28 (escape octal, AE-99, achado roteado a este card). (2) Cobertura: o corpus do passo 3 do metodo nomeia .claude/checks/ e as skills diario-de-obras, passagem-de-bastao e guardrails-check, sem linha K na §2; K-09, K-22 e K-33 estao na §2 sem registro na §3. Medicao imprecisa: o reg. 41 diz que o planejador da SAIDA 1 do P-0755 falta na serie 'sem id do plano', mas a serie depois (p0754_artefatos/depois_docs_telemetria.tsv) o tem como P-0754-planejador 45.2k/3/121.4s (bate com registros.md: 45,2k/3 tools/122s) e mais uma linha P-0754-planejador 69.5k: atribuido ao plano real pelo id da primeira mensagem (telemetria_hook.py:338-339), nao ausente; o remedio da R-16 (id do _INBOX quando tarefa-corrente.json nao existe) mira a causa errada. Conferido e correto: §6 por papel (1.250,0k; serie 1.138,0k em 18 linhas), §8 real (101 turnos, 28.847k, P3 38/23, P9 13, P4 3,06k), descarte e arvore. |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | A Verificacao 5 so conta a frase e min(1, '### R-'), e as 1, 2 e 6 contam cabecalhos e linhas: nenhuma discrimina 'uma recomendacao por registro inadequado ou oportunidade' nem 'cada regra testavel tem teste'; os 6 registros sem R e o corpus sem linha K passaram verdes. Remedio: card de relatorio com cobertura enumerada verifica por comando (cada registro da §3 com avaliacao diferente de adequado citado em alguma 'Origem:' da §5; cada item do corpus do metodo com linha K). Rota: AE-<n> na §9 do P-0754, plano sucessor (DAU-20). |
| dossiê | A contingencia 2 manda registrar como AE-<n> na §9 do plano cada defeito em herdado ja fechado, mas o formato do relatorio (§3) nao tem marca de 'defeito em herdado fechado por este plano': plano.md segue sem alteracao desde o <ref> e o conjunto de AE fica a juizo de quem fecha (candidatos pela §3: reg. 23 e 24, AUF-T3/AUF-T4; reg. 36, AUF-T12; reg. 25 e 26 ja sao AE-105/AE-106). Rota: AE-<n> na §9 do P-0754, plano sucessor - a contingencia que escreve em residencia do fechamento nomeia a coluna ou a marca que a dispara. |
| dossiê | Decisao tomada pela entrega que o card nao fechou (G-NOASK): o loop ficticio despachou o executor com o card por arquivo em vez de colado (K-18, reg. 22), variante do Passo 4 do scrum-master que o metodo nao previa; declarada no relatorio e base da R-02. Rota: AE-<n> na §9 do P-0754, plano sucessor (card de sondagem que admite variante de procedimento a nomeia). |

## Lições aprendidas na tarefa

Os numeros do relatorio se re-derivam dos artefatos fora do repositorio: medir.py + passos.py sobre o transcript reproduzem exatamente o loop real (fim no handover da AUF-T15) e o ficticio a um turno de diferenca pelo marcador de fim; a soma por papel da §6 bate com as 22 linhas da serie depois. Terminologia: '20/20 aprovadas' (reg. 21, §4) inclui a AUF-T2, que fechou ressalva 91%. O card executado pela sessao principal nao tem linha na serie de telemetria (o hook so grava subagente); o custo dele so existe no transcript.
