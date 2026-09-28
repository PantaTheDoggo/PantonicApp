# Laudo — DIARIO_DE_OBRAS · TK-88a

**Percentual:** 85%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** escalar
**Pendência:** Defeito desta entrega no painel do gerente, medido em uso real hoje: progresso_hook.py:291-299 pega o primeiro '--tarefa' da linha inteira e casa 'encerrar.py plano' em texto de argumento - 14 linhas M-10 com '<ID>-revisao' no lugar do titulo (telemetria.py append encadeado antes do encerrar), 13 M-11 herdando o id errado e copiadas para o '# Historico' de 12 RDO, e 2 M-18 'vai fechar o plano' do P-0752 sem fechamento; correcao imediata: card corretivo que amarra --tarefa/--plano a propria invocacao do encerrar.py, com TR dos dois casos, e que passa o '**Plano:**' do RDO pelo mesmo _rel do verbo plano (encerrar.py:454 grava barra invertida em 16 RDO). O fechamento desta propria tarefa sera recusado pelo encerrar.py: nao ha linha medida de TK-88a na serie (executada na sessao principal) - a triagem decide o desfecho do consumo antes.

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | parcial |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | parcial |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Evidencia gerada sem --desde (ref do despacho nao capturada: tarefa executada na sessao principal, fora do loop); o recorte mistura 54 arquivos do P-0752, do TK-91a e dos consertos do condutor, e o veredito de escopo saiu 'aberto'. Reconciliado por conteudo (grep TK-88/encerrar.py fora de docs/RDO: so os 15 alvos, mais fatos-frescos da FPU-T9 e o _CENARIO do consultor) e por mtime (alvos novos 05:20-06:01; rdo.py 08:47 e backlog.py 11:21 com hunks posteriores de outras tarefas). Rota: tiquete na triagem do consultor - tarefa executada fora do loop so entra em review com ref capturada, medida do executor (card_check --gravar) e linha de telemetria. |
| dossiê | G-NOASK: o card exigiu 'recusam sem escrever' e a ordem status -> RDO compondo instrumentos cujas checagens so rodam no ato de escrever (rdo.cmd_close exige status done) e proibiu reimplementar regra, sem dizer como conciliar. Decisao tomada pela entrega: duplicar pre-checagens (regra de plano done em encerrar.py:649-654 = backlog.py:1699-1705; destino e existencia do RDO em encerrar.py:400-406 = rdo.py:761-771) e aceitar a janela 'status done sem RDO' se cmd_close falhar depois (encerrar.py:466-469, com a mensagem de recuperacao). Rota: tiquete na triagem do consultor - checagem sem escrita exposta por rdo.py/backlog.py, ou a duplicacao declarada na doutrina. |
| doutrina | Nao ha caminho honesto para fechar tarefa executada sem SubagentStop: encerrar.py tarefa recusa sem linha medida (consumo_da_serie ignora fonte nao_medido) e a propria TK-88a nao tem linha na serie nem bloco <usage>. GOVERNANCA 4.2 diz 'numero inventado nao fecha tarefa' e nao diz o que fecha a tarefa sem medida. Rota: triagem do consultor - declarar o desfecho (nao_medido admitido no fechamento, ou execucao so por subagente) em GOVERNANCA 4.2 e no instrumento. |

## Lições aprendidas na tarefa

Motivo do parcial em testes: o card declara TF/TR para test_progresso_hook.py (M-10 pelo instrumento, M-18) e so ha o TF (test_tf_tk88_encerrar_tarefa_gera_m10_e_encerrar_plano_gera_m18), com o comando isolado; o TR que discriminaria comando encadeado e literal em argumento nao existe, e e exatamente onde o defeito escalado vive (reproduzido com progresso_hook.evento sobre 'telemetria.py append --tarefa FPU-T8-revisao ...; encerrar.py tarefa --tarefa FPU-T8' -> titulo 'FPU-T8-revisao'). Motivo do parcial em registro: Medida do executor ausente (verificacao nao registrada pela execucao; as notas do card e do TK-88 parafraseiam a entrega sem exit code) e nenhuma linha de TK-88a em docs/telemetria.tsv. Re-medido na revisao: Verificacao 1 exit 0 (230 passed), 2 'check: OK' exit 0, 3 exit 0 (420 passed >= 376 + novos). Exercicio ponta a ponta: 16 fechamentos reais de hoje (15 RDO do P-0752 e o do TK-91a) com as tres secoes, handover no card e handovers_para devolvendo FPU-T9/FPU-T9a para FPU-T10 e FPU-T4a para FPU-T7; em copia de fixture de plano em pasta, handover -> tarefa -> plano fecharam (estado.tsv done, rdo/GAM-T1.md, entrega.md, linha FECHADO no diario) e o plano recusou sem operacoes.md. Divergencias menores do modulo, para o mesmo card corretivo: a linha FECHADO conta 1/2 com cancelada enquanto o indice logo abaixo diz done 1/1; stdout 'tarefa fechado'.
