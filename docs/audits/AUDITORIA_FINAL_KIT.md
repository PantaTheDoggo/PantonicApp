# Auditoria final do kit — 2026-09-28

**Objeto:** o kit agêntico Pantonic* (`.claude/` + `GOVERNANCA.md` + `docs/`), na árvore de trabalho de 2026-09-28 (branch `plan/planner-modelo-escopo`, HEAD `2513964`, com o WIP não commitado do `P-0754` — as `AUF-T1`..`AUF-T15` entregues e aprovadas).
**Método:** o do estágio 1 (`docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md`): um plano fictício, `docs/plans/P-0755-sonda-auditoria-final/`, executado ponta a ponta contra o kit real pelo procedimento que o kit prescreve (planejador → batedor → modelador → decomposição → Marco 1 → loop do `scrum-master` → revisão → ato do dono no loop → consultor → emenda do modelo → rodada de replanejamento → Marco 2 com aceite de versão → fechamento), com um registro por cláusula exercitada. Somam-se as medidas do loop real das `AUF-T1`..`AUF-T15`, conduzido na mesma sessão, e o custo da sessão principal, lido do transcript (`message.usage` de cada resposta). O plano fictício foi descartado ao fim.
**Auditor:** a sessão principal, no papel que o dono nomeou (card `AUF-T16`, exceção à matriz de papéis válida só para ele).

## 0. O pedido, verbatim

Atos do dono de 2026-09-28, nesta ordem:

> "execute oplano de auditoria final"

> Escopo — **"Herdado + auditoria nova"**: *"Tudo o que foi herdado mais uma varredura nova do kit, que gera um relatório de auditoria, no formato usado na auditoria de encerramento do estágio 1 (P-0753)."*

> Condução — **"Quem conduz (Recomendado)"**: *"A auditoria é a última tarefa do plano, executada pela sessão principal, como no estágio 1. O loop para antes dela e só a abre quando você mandar. Isso abre uma exceção à matriz de papéis, válida só para essa tarefa. A tarefa passa pela revisão. A avaliação do scrum-master que você pediu é medida no loop real, com o custo real de orquestrar."*

> Marco 2 — "pode  iniciar a auditoria neste contexto"

Matéria herdada que esta auditoria recebe como item de avaliação: o `AE-95` do `P-0742` (*"pode existir potencial para ganhor mecanizado ações mecânicas do scrum-master ou otimizar as rotinas dele"*, com o `scrum-master` mantido no loop) e o `H-16` do `P-0754` (onde a rodada de replanejamento grava a medida dos cards que reescreve).

## 1. Modelo conceitual da auditoria

| objeto | o que é | propriedades | tipo |
|---|---|---|---|
| relatório final | este documento | cláusulas, registros, conclusão por dimensão, recomendações, custo, avaliação do gerente do loop | escopo |
| plano fictício | o `P-0755` que exercita as cláusulas | cláusulas cobertas, passagens, descarte | escopo |
| teste do kit | cada passagem do plano fictício ou do loop real por uma cláusula | cláusula, procedimento, resultado esperado | escopo |
| recomendação | tíquete derivado de um registro inadequado ou de oportunidade | causa, ação, verificação | escopo |
| cláusula do kit | cada mecanismo testável (skill, agente, instrumento, hook, regra) | forma prescrita | externo |
| execução do teste | a passagem real, medida | lacuna, erro, confiabilidade, custo evitável, qualidade, mecanização, fluxo | medição |
| gerente do loop | a rotina do `scrum-master` na sessão principal | passos P1..P10, turnos e tokens por passo | medição |

Fluxo: OP-1 enumerar as cláusulas → OP-2 autorar o plano fictício que as cobre → OP-3 executar cada teste e registrar a medição → OP-4 medir o gerente do loop por passo → OP-5 concluir por dimensão → OP-6 emitir as recomendações → OP-7 descartar o plano fictício.

## 2. Cláusulas do kit exercitadas

Uma linha por mecanismo testável; *teste* diz por qual passagem ele foi exercitado. `real` = loop real das `AUF-T1`..`AUF-T15`; `sonda` = sonda direta, sem passagem no plano fictício.

| id | cláusula (mecanismo) | residência | teste |
|---|---|---|---|
| K-01 | gate modelo-por-fase (hook `UserPromptSubmit` + skill) | `.claude/global/hooks/`, skill `modelo-por-fase` | toda mensagem da sessão |
| K-02 | pré-voo do pedido (`prevoo.py`) | `.claude/tools/prevoo.py`, `pantonic-planner.md` Fase 0 | pedido do `P-0754` e do `P-0755` |
| K-03 | `pantonic-planner` Fase 0–1 (SAÍDA 1) e Fase 2–3a (SAÍDA 2/3) | `.claude/agents/pantonic-planner.md` | autoria do `P-0754` e do `P-0755` |
| K-04 | `pantonic-scout` com `Bash` (configuração ajustada pela `DAF-46`) | `.claude/agents/pantonic-scout.md` | 6 batedores no `P-0754`, 3 no `P-0755` |
| K-05 | verificação "impedimento de papel é configuração do kit?" (`AUF-T13`) | `pantonic-planner.md` Fase 1 | rodada de decisões do `P-0754` |
| K-06 | `pantonic-model-designer`: autoria, emenda (`## 1A`) e desfecho de marco | `.claude/agents/pantonic-model-designer.md` | 3 atos no `P-0755` |
| K-07 | `modelo.py check` / `show` / `show --drift` | `.claude/tools/modelo.py` | cada ato de modelo |
| K-08 | `pantonic-planner` Fase 3b–5: um card por operação, ensaio em cópia, `card_check`, registro | idem | decomposição do `P-0754` e do `P-0755` |
| K-09 | contingência ensaiada e declarada nos alvos (`AUF-T9`, rubrica (xix) `AUF-T10`) | `pantonic-planner.md`, `docs/RUBRICA_DE_REVISAO.md` | card `SA-T2`; card `AUF-T16` |
| K-10 | teste de interrupção com os três pontos nomeados (`AUF-T11`) | `pantonic-planner.md` Fase 4 item 8 | decomposição do `P-0755` |
| K-11 | versão pendente reconfere a restrição que cita o estado do plano (`AUF-T12`) | `pantonic-planner.md`, rodada de replanejamento | rodada `RP-1` do `P-0755` |
| K-12 | `card_check.py` (formas de Verificação, mundos, `--gravar`) | `.claude/tools/card_check.py` | todos os cards |
| K-13 | `backlog.py drain` / `diretiva` / `check` | `.claude/tools/backlog.py` | abertura das duas janelas |
| K-14 | `backlog.py next` (seleção, `=== HANDOVER DE`, achados roteados) | idem | Passo 2 de cada tarefa |
| K-15 | `backlog.py despachar` (gates 3 e 4, coleta, `in-progress`, `<ref>`) | idem, skill `scrum-master` Passo 3 | cada despacho |
| K-16 | `encerrar.py marco` (tabela de marcos, `estado.tsv`, `--aceita-versao`) | `.claude/tools/encerrar.py`, `GOVERNANCA.md` §3.2 (validação prévia do consultor) | Marcos 1 e 2 do `P-0754` e do `P-0755` |
| K-17 | `pantonic-executor` (linha de retorno, TDD, contingência) | `.claude/agents/pantonic-executor.md` | 20 execuções |
| K-18 | despacho do card por arquivo em vez de colado | variante medida nesta auditoria | 5 despachos do `P-0755` |
| K-19 | `review_evidence.py`: arquivo novo como diferença e marca de novo (`AUF-T1`, `AUF-T3`) | `.claude/tools/review_evidence.py` | `SA-T1` |
| K-20 | `review_evidence.py`: alvo com curinga (`AUF-T3`) | idem | `AUF-T3`; sonda |
| K-21 | `review_evidence.py`: registro da condução antes da tarefa dona (`AUF-T4`) | idem | todas as evidências das duas janelas |
| K-22 | `review_evidence.py`: recorte a partir de tudo o que é versionado (`AUF-T5`) | idem | `AUF-T5` e seguintes |
| K-23 | `review_evidence.py`: não texto julgado pelo conteúdo bruto (`AUF-T6`) | idem | `SA-T1` (`c.bin`) |
| K-24 | `review_evidence.py --atribuir` e `--out` | idem | sonda |
| K-25 | `pantonic-reviewer` + laudo calculado | `.claude/agents/pantonic-reviewer.md`, `rdo.py` | 20 revisões |
| K-26 | bloco A (A8 com erro inequívoco → consultor; A9) | skill `scrum-master` | `AUF-T2`; demais |
| K-27 | `encerrar.py handover` / `tarefa` (RDO, achados, telemetria, frase final `AUF-T8`) | `.claude/tools/encerrar.py` | 20 fechamentos |
| K-28 | dedupe dos achados do laudo no fechamento | idem | `AUF-T2` |
| K-29 | `pantonic-consultant` efêmero (cenário, `rota=`, `ACIONAMENTOS_CONSULTOR.tsv`) | `.claude/agents/pantonic-consultant.md` | `AUF-T2` (A8); ato do dono no `P-0755` |
| K-30 | rota `modelador` segue sem parar (Passo 8) | skill `scrum-master` | ato do dono no `P-0755` |
| K-31 | a rodada de replanejamento grava a medida dos cards que reescreve (`H-16`) | `pantonic-planner.md` "Rodada de replanejamento", `card_check.py --gravar`, `caminhos.destino_medida` | rodada `RP-1` do `P-0755` |
| K-32 | hook `SubagentStop` → `docs/telemetria.tsv` (todos os papéis) | `.claude/tools/telemetria_hook.py` | todas as instâncias |
| K-33 | hook de progresso → painel, título do tíquete (`AUF-T7`) | `.claude/tools/progresso_hook.py` | painel `.claude/estado/progresso.txt` na janela do `P-0755` |
| K-34 | hook `UserPromptSubmit` de próximo passo (`backlog_hook.py`) | `.claude/tools/backlog_hook.py` | toda a sessão |
| K-35 | hook de ocupação (aviso de janela) | `.claude/tools/ocupacao.py` | disparo às 17:42 |
| K-36 | entrega de encerramento (`operacoes.md`) + `encerrar.py plano` | skill `entrega-de-encerramento`, `encerrar.py` | fechamento do `P-0755` |
| K-37 | hook de filtro do pytest | `~/.claude/hooks/pytest_pretooluse.py` | batedor Q3 |
| K-38 | relatório de encerramento + skills `fatos-frescos` e `mensagem-ao-dono` | skill `scrum-master`, `docs/FALHAS_COMUNICACAO.tsv` | fim da janela do `P-0754` |
| K-39 | checks executáveis (`dead_code.py`, `ratchet_piso.py`, `frontmatter_yaml.py`, `kit_check.ps1`, `check-readme.ps1`) | `.claude/checks/` | 5 evidências do `P-0755`; sonda direta na árvore depois da limpeza |
| K-40 | bateria do gate de qualidade antes de `review` | skill `guardrails-check`, `review_evidence.py` (`BATERIA_GUARDAS`) | 5 evidências do `P-0755` |
| K-41 | registro do plano no diário (índice, diretiva, fila) | skill `diario-de-obras` | nascimento e fechamento do `P-0755` |
| K-42 | transição entre tarefas (drenar, apurar a fila, dossiê sob o gate, herança, fechamento, checkpoint) | skill `passagem-de-bastao`, pelos instrumentos das K-13 a K-15 e K-27 | 20 transições |
| K-43 | versão do kit conferida ao criar plano | skill `checar-versao-kit`, `pantonic-planner.md` | autoria do `P-0755` (reg. 15) |

## 3. Registros — um por teste

Dimensões: **L** lacuna · **E** erro de execução · **C** pouca confiabilidade · **$** custo evitável · **Q** qualidade da entrega · **M** mecanização · **F** fluxo. Avaliação: `adequado` · `inadequado` · `oportunidade`.

| # | cláusula | teste | medido | dimensões | avaliação |
|---|---|---|---|---|---|
| 1 | K-01 | hook de modelo-por-fase | disparou a cada mensagem, inclusive nas voltas de subagente; Opus ativo acima do exigido na orquestração: seguiu e anotou | — | adequado |
| 2 | K-02 | pré-voo sobre pedido de criação (`P-0755`) | exit 1 com `não` em todo arquivo que o pedido manda criar; `.txt` tomado por caminho; `c.bin` não citado. O planejador contornou (entregável ≠ premissa) e registrou | L, C (a regra "linha com `não` volta ao dono" devolveria o pedido sem motivo) | inadequado |
| 3 | K-03 | planejador Fase 0–1 do `P-0754` e do `P-0755` | duas SAÍDAS 1 corretas (7 e 8 perguntas fechadas); instância 1 do `P-0755` 69,96k tokens / 6 tool uses / 209 s até a SAÍDA 3 | Q | adequado |
| 4 | K-05 | "impedimento de papel é configuração?" | o planejador do `P-0754` aplicou antes da regra existir: "a limitação é da plataforma (subagente não despacha) e não da configuração" — levou à rodada de decisões certa | Q | adequado |
| 5 | K-04 | batedor com `Bash` | 9 batedores rodaram comando e devolveram stdout literal; o defeito `RP-1` do estágio 1 (campanha que pede comando a quem não roda) não reapareceu | Q | adequado |
| 6 | K-06/K-07 | modelador, autoria (`P-0754`: 16 operações; `P-0755`: 4) | seções conformes; `check` só com `V3` de lastro, como a norma prevê; 89,6k e 58,0k | Q | adequado |
| 7 | K-06 | modelador × orientação do planejador | o dossiê do planejador pediu "o caminho mora no contrato"; o modelador recusou pela norma `TK-76` (célula descritiva sem caminho) | C (planejador e modelador leem a mesma doutrina de jeitos opostos) | oportunidade |
| 8 | K-08 | planejador Fase 3b–5, `P-0754` | 16 cards, ensaio em cópia, `card_check` nos dois mundos, 505 → 521 testes no ensaio; 311,4k / 123 tool uses / 37 min | Q, $ | oportunidade |
| 9 | K-08/K-09 | planejador Fase 3b–5, `P-0755` | 4 cards; ensaio inclusive da contingência `seguir com` (regra nova da `AUF-T9` em uso); 145,4k / 28 / 12,6 min para 5 arquivos de produto | $ (planejamento = 352,2k de 1.250,0k ≈ 28% do custo de subagentes do plano) | oportunidade |
| 10 | K-12 | `card_check`, forma de bloco cercado | compara sempre com `Medido antes` e ignora `--mundo`: o `--mundo depois` que o item 14 da Fase 4 pede não mede nada na forma normativa da §8.1 da rubrica | L, C | inadequado |
| 11 | K-12 | `card_check`, forma inline | o par antes/depois recusa `,` e `;` no antes e `.` no depois; literais reais (`a.txt: 3`) ficam truncados — o planejador passou a escrever comandos que imprimem veredito de uma palavra | C, Q (literal esperado escondido dentro do comando) | inadequado |
| 12 | K-12 | `card_check`, comandos aceitos | só executa comando que começa por `python` ou `pwsh`; `git status` exige invólucro `python -c` | F | oportunidade |
| 13 | K-08/K-12 | `card_check` exit 0 contra a árvore real (Fase 5) | card cujo `antes` depende do antecessor só passa se o valor for igual nos dois mundos; o protocolo não diz em que árvore medir | L | oportunidade |
| 14 | K-08 | item 14 × operação de estado final "igual" | revisão do `README.md` sem texto novo não tem linha que discrimine; linhas "trava" sem exceção prevista | L | oportunidade |
| 15 | K-08/K-43 | "invocar `checar-versao-kit`" | o planejador é subagente e não tem `Skill`; registrou a versão pelo cabeçalho | L (instrução impossível no papel) | oportunidade |
| 16 | K-13 | `backlog.py diretiva` depois do plano criado | a diretiva antiga citava `` `AE-<n>` `` antes de ` — ` e o `next` filtrou a fila inteira (0 elegível com o `P-0754` `ready`) até a reescrita | C, F (a diretiva não é revista quando o plano que ela anuncia nasce) | inadequado |
| 17 | K-13 | diretiva × convenção do auditor | o prefixo `DSA-` fixado pelo auditor colidia com as `DSA-1..24` do `P-0749` (72 ocorrências); nenhum instrumento lê prefixo de decisão | L | oportunidade |
| 18 | K-14 | `next` injetado em contexto de planejamento | o `next` sem filtro despeja o card de outro plano (AUF-T16, 15 KB) | $ | oportunidade |
| 19 | K-15 | `despachar` | 20 despachos, recusa correta quando o modelo falhou (reg. 31); imprime card, handover e `ref=` | Q, M | adequado |
| 20 | K-15 | âncoras do gate de delegação (item 3) | re-derivadas à mão: 23 turnos da sessão principal no loop real (≈1,5 por tarefa) | M | oportunidade |
| 21 | K-17 | executores (15 reais + 5 fictícios) | 20/20 entregas aceitas (19 `aprovado`, 1 `ressalva`: `AUF-T2`, 91%); 3 devolveram prosa depois da linha (descartada); 1 apagou uma asserção de teste vizinho (`AE-97`), corrigida pelo consultor | Q, C | adequado |
| 22 | K-18 | despacho por arquivo (variante) | 5/5 executores leram o arquivo e devolveram a linha exata, sem prosa; saída da sessão principal no Passo 4: 3,06k por despacho no loop real → 0,72k na variante (−77%) | M, $ | oportunidade |
| 23 | K-19 | arquivo novo depois do `<ref>` | `a.txt`/`b.txt` saíram com `(arquivo novo — ausente em <ref>)` e linhas `+`; `c.bin` saiu só `(arquivo binário…)` sem a marca de novo | L (leve) | oportunidade |
| 24 | K-21 | registro da condução | resumo correto em todas as evidências ("Registro da orquestração: diário, `estado.tsv`, medida, telemetria"); a lista por arquivo rotula os mesmos como `atribuição: alheio` | C (dois rótulos para o mesmo fato) | oportunidade |
| 25 | K-23 | binário intocado | `c.bin` julgado por bytes; o caso simétrico (binário no `<ref>`, texto hoje) derruba `coletar_arquivos_tocados` com `AttributeError` (`AE-106`) | E | inadequado |
| 26 | K-24 | `--atribuir` sem `rdo.py` na raiz | traceback cru, exit 1, enquanto o dossiê sai com mensagem nomeada (`AE-105`); `--out` procura a medida ao lado do `--out` e a dá por `ausente` embora exista na pasta do plano | E, C | inadequado |
| 27 | K-20 | curinga | casa `relatorios/*.md` também em `relatorios/sub/x.md` (`fnmatch`, não glob de shell; `AE-104`) | C | oportunidade |
| 28 | K-19 | caminho com escape octal | o caminho que `coletar_arquivos_tocados` devolve chega a `montar_trechos` como ausente: não rastreado com acento chega sem diff (`AE-99`) | L | oportunidade |
| 29 | K-25 | revisores (15 reais + 5 fictícios) | duas linhas exatas em 20/20; achados reais de instrumento em 9 laudos; 40,9k–62,2k por revisão | Q | adequado |
| 30 | K-25 | Verificação por `-k` e piso por contagem | não discriminam enfraquecimento de teste vizinho no mesmo arquivo; a remoção do `AE-97` passou verde; a condução passou a medir `git diff <ref> --numstat` à mão (`AE-98`) | L, M | inadequado |
| 31 | K-30 | rota `modelador` × gate do despacho | o consultor devolveu `rota=modelador` (segue); a `## 1A` pendente sai `V1` por construção (lista `tarefas:` vazia para o planejador) e `despachar SA-T3` foi recusado: "modelo: FALHOU — 1 violação"; a janela parou por `B3` | E, F (a rota que manda seguir produz o estado que o Passo 3 recusa) | inadequado |
| 32 | K-29 | consultor, ato do dono no loop | classificou drift, gravou `DSN-13/14`, criou o cenário, pôs a fila; propôs "rodada de planejamento" para o card novo, rota que o loop não tem sem parar; 59,4k / 15 / 225 s | Q, F | oportunidade |
| 33 | K-29 | consultor, A8 com erro inequívoco (`AUF-T2`) | repôs a asserção apagada no ato, mediu `20 0` no numstat e 508 passed; 51,3k | Q | adequado |
| 34 | K-06/K-07 | emenda com operação inserida no meio | a nova virou `OP-4` e a revisão do README foi renumerada para `OP-5` (`V8` exige 1..k); `--drift` mostra "OP-4 alterada + OP-5 nova" e não mostra a propriedade nova do estado final (`modelo.py:482-509`) | L, C (o dono lê um drift enganoso no marco) | inadequado |
| 35 | K-31 | onde a rodada grava a medida (`H-16`) | não grava: `card_check --gravar` escreve uma medida por tarefa, um mundo, na pasta derivada de `--plano` (não de `--root`); um ensaio em cópia com o `--plano` real gravaria a medida da cópia na pasta real e a seguinte sobrescreveria; a única residência foi a prosa da §5 | L, M | inadequado |
| 36 | K-11 | versão pendente × cards | o planejador reconferiu as restrições (regra `AUF-T12` em uso); a regra não cobre o campo `Operação do modelo`: `SA-T5` e `SA-T4` citaram `OP-4` com textos diferentes e o `check` aprovou | L | inadequado |
| 37 | K-16/K-06 | Marco 2 com `--aceita-versao 2` | `encerrar.py marco` só imprime o dossiê de emenda; a promoção exige outro modelador (55,0k); depois dela a `SA-T4` citava a `OP-4` nova (a da pasta) com texto e `precisa de` da versão 1, e `check` saiu 0 — nenhuma regra compara o texto copiado | L, C, M | inadequado |
| 38 | K-16 | validação prévia do consultor no marco | `GOVERNANCA.md` §3.2 pede consultor antes do dono; `encerrar.py marco --aceita-versao` não a cobra (`encerrar.py:1000-1004`) | L | oportunidade |
| 39 | K-27/K-28 | dedupe dos achados do laudo | `AE-100`/`AE-101` repetem `AE-98`/`AE-99` que o consultor reescreveu; a dedupe compara texto literal (`AE-102`) | C | oportunidade |
| 40 | K-27 | frase final (`AUF-T8`) | 20 fechamentos com `encerrar: OK - comando 'tarefa' concluído;` | — | adequado |
| 41 | K-32 | telemetria de todos os papéis | o hook já grava planejador, batedor, modelador, revisor e consultor (defeito do estágio 1 fechado); série do `P-0755` = 1.138,0k em 18 linhas contra 1.250,0k medido: o planejador da SAÍDA 1 (69,96k) não falta: está na série atribuído ao plano errado, `P-0754-planejador` 45,2k/3/121,4s e `P-0754-planejador` 69,5k/9/632,2s, pelo primeiro id de plano da primeira mensagem (`telemetria_hook.py:338-339`), que citava o `P-0754`; faltam 2 batedores `sem-id-scout` (75,7k); `SA-T4` com duas linhas (33,7k e 34,3k); consultor gravado como `SA-T2-consultor-1` triando a `SA-T3` (`tarefa-corrente.json` da anterior) | C | inadequado |
| 42 | K-34 | hook de próximo passo | gatilho `proximo passo` (`backlog_hook.py:33`) casou nos relatórios de subagente que trazem "Próximo passo de quem conduz" e injetou 15,3 KB do `next` (card `AUF-T16`) 3 vezes | E, $ | inadequado |
| 43 | K-35 | hook de ocupação | disparou às 17:42, no despacho da `SA-T4`; a condução seguiu a tarefa corrente (esta auditoria), sem abrir nova, como a Regra 2 manda | — | adequado |
| 44 | K-36 | `operacoes.md` + `encerrar.py plano` | fechamento por um comando; `entrega.md` com consumo da série | Q | adequado |
| 45 | K-37 | filtro do pytest | `cd … && pytest …; echo "exit=$?"` anexa o pipe ao comando inteiro e o exit vira 1 (do filtro) | C | oportunidade |
| 46 | K-38 | relatório de encerramento × dono | a mensagem do Marco 2 pediu "a auditoria nova" sem dizer que era a que o dono já tinha pedido; ele perguntou "Você está pedindo mais uma auditoria?"; linha gravada em `docs/FALHAS_COMUNICACAO.tsv` | Q | inadequado |
| 47 | K-26 | laudos com recomendação `seguir` e achado de erro | `AE-106` (queda do instrumento) veio num laudo `aprovado 100 seguir`; A9 não escala; o erro só chegou a este relatório porque a diretiva roteia tudo à auditoria | F | oportunidade |
| 48 | K-10 | teste de interrupção em uso | os cards do `P-0755` fixaram forma de caminho, `strip()` e recusas; 0 parada de executor por dúvida em 20 execuções | Q | adequado |
| 49 | K-39 | sonda direta dos checks na árvore depois da limpeza (2026-09-28) | `dead_code.py`, `ratchet_piso.py`, `frontmatter_yaml.py`, `kit_check.ps1 -Mode validate` e `-Mode check-drift`, `check-readme.ps1`: exit 0 todos; `git status` inalterado | — | adequado |
| 50 | K-40 | gate de qualidade no plano fictício | as 5 evidências do `P-0755` trazem a bateria medida (`pytest`, `dead_code`, `ratchet_piso`, `kit_check` validate e check-drift, `check_readme`), 6/6 exit 0 em cada; o gate não depende do auto-relato do executor | Q, M | adequado |
| 51 | K-41 | `P-0755` no diário | o loop gravou índice, diretiva e fila (3 menções do `P-0755` no diário depois); a limpeza os restaurou; os defeitos de diretiva e prefixo estão nos reg. 16 e 17 | — | adequado |
| 52 | K-42 | passagem de bastão nas 20 transições | 0 retentativa e 20 fechamentos com a frase final (reg. 19, 40); os defeitos dos instrumentos que a skill usa estão nos reg. 16, 18, 20 e 39 | — | adequado |
| 53 | K-22 | recorte a partir do versionado depois da `AUF-T5` | 15 laudos seguintes (`AUF-T6`..`AUF-T15`, `SA-T1`..`SA-T5`) sem queixa de arquivo versionado fora do recorte; a prova positiva é o exercício ponta a ponta do laudo da `AUF-T5` (100%) | — | adequado |
| 54 | K-33 | título do tíquete no painel | toda linha de tarefa do `P-0755` traz o título do card (regra da `AUF-T7` em uso); planejador e modelador do plano fictício saem com o título da `AUF-T16`, a tarefa corrente, e o modelador do desfecho do Marco 2 com o da `SA-T4` — a mesma atribuição por `tarefa-corrente.json` do reg. 41 | C | oportunidade |

## 4. Conclusão por dimensão

| dimensão | veredito | fundamento (registros da §3) |
|---|---|---|
| **Integração ponta a ponta** | **adequado** | as duas janelas atravessaram planejador → batedor → modelador → decomposição → marco → loop → revisão → consultor → emenda → rodada de replanejamento → promoção de versão → fechamento; 20/20 entregas aceitas (19 aprovadas, 1 ressalva), 0 retentativa, 0 pergunta ao dono no meio do loop (19, 21, 29, 44, 48) |
| **Lacunas (L)** | **inadequado em três pontos** | a rodada de replanejamento não tem onde gravar a medida (35); o número de operação não amarra card e versão do modelo — card cita operação de outro texto e `check` aprova (36, 37); o `--mundo depois` não mede nada na forma normativa (10) |
| **Erros de execução (E)** | **quatro defeitos de instrumento ou fluxo** | a rota `modelador` produz o estado que o despacho recusa (31); o hook de próximo passo casa em relatório de subagente (42); `review_evidence` cai no binário→texto e no `--atribuir` (25, 26) |
| **Confiabilidade (C)** | **tem oportunidade de melhoria** | telemetria e painel com atribuição errada, lacunas e duplicata (41, 54); `--drift` enganoso na inserção (34); literal esperado escondido em veredito de uma palavra (11); diretiva velha filtrando a fila (16); dedupe literal (39) |
| **Custo evitável ($)** | **inadequado** | o custo da sessão principal cresce com o tamanho do contexto que ela carrega: 285,6k reenviados por turno no loop real e 485,6k no fictício, porque planejamento, loop e auditoria correram numa janela só (§8); planejamento ≈ 28% do custo de subagentes do plano fictício para 5 arquivos (9); 15 KB injetados três vezes (42) |
| **Qualidade da entrega (Q)** | **adequado** | 19/20 aprovadas com 100% e 1 ressalva (`AUF-T2`, 91%); os revisores acharam 15 defeitos reais de instrumento; as regras novas das `AUF-T9`..`AUF-T13` foram usadas pelo planejador e pelo consultor na sonda (4, 9, 36, 48) |
| **Mecanização (M)** | **tem oportunidade de melhoria** | despacho por arquivo (22), âncoras do gate (20), numstat de linhas removidas (30), promoção de versão num comando (37), medida da rodada (35) |
| **Fluxo (F)** | **tem oportunidade de melhoria** | emenda que cria operação não tem rota ao planejador sem parar (31, 32); erro de instrumento em laudo `seguir` não escala (47); diretiva não acompanha o nascimento do plano (16) |

**Veredito qualitativo geral: adequado na integração e na qualidade; inadequado em custo e em três lacunas de amarração entre modelo, card e medida; tem oportunidade de melhoria em confiabilidade, mecanização e fluxo.**

Comparado ao estágio 1: fecharam-se a telemetria só do executor, o painel cego com `-X utf8`, o batedor sem `Bash`, o achado do laudo não transcrito e o dossiê truncado no `next`. Os defeitos novos concentram-se onde o estágio 1 não chegou: emenda com operação nova, rodada de replanejamento e promoção de versão.

## 5. Recomendações — um tíquete por registro viável

As recomendações deste relatório não se aplicam no P-0754.

Forma: origem (registro da §3), ação fechada, verificação. Nenhuma foi aberta no diário (diretiva do dono de 2026-09-26); o plano sucessor as recebe.

### R-01 — O loop abre em contexto novo, separado do planejamento
- Origem: §8, reg. 9. Ação: a skill `scrum-master` passa a exigir que o loop de um plano recém-planejado abra em janela nova, com o plano gravado como único insumo; o planejamento encerra a janela no Marco 1. Verificação: custo por turno da sessão principal medido pelo transcript no próximo loop, contra 285,6k deste.

### R-02 — `despachar` grava o dossiê em arquivo e imprime o prompt pronto
- Origem: reg. 22, §8 P4. Ação: `backlog.py despachar <ID>` grava o card, o handover e as âncoras em `<pasta-do-plano>/despacho/<ID>.md` e imprime o texto do despacho ao executor (caminho, gramática da linha de retorno). Verificação: saída da sessão principal no Passo 4 ≤ 1k por tarefa.

### R-03 — `despachar` re-deriva as âncoras que o card cita
- Origem: reg. 20, §8 P3. Ação: para cada `arquivo:linha` e cada texto entre crases em `Passos`/`Contratos` que casa uma linha do arquivo-alvo, o verbo imprime `arquivo:linha` atual. Verificação: 0 turnos de grep de âncora por despacho.

### R-04 — A rota `modelador` não bloqueia o despacho da vigente
- Origem: reg. 31, 32. Ação: ou o `modelo.py check` do Passo 3 julga só a `## 1` (a `## 1A` vai ao gate do marco), ou a emenda que cria operação volta ao planejador no mesmo ciclo, antes de a janela seguir. Decisão do dono sobre a doutrina. Verificação: reproduzir o ato do dono do `P-0755`: `despachar SA-T3` sai 0.

### R-05 — A rodada de replanejamento grava a medida dos cards que reescreve
- Origem: reg. 35 (`H-16`). Ação: `card_check.py --gravar` passa a gravar sob a pasta do plano do `--root` (não do `--plano`), com o mundo no nome (`<ID>-medida-<mundo>.json`), e a rodada passa a exigir a gravação dos dois mundos de cada card reescrito. Verificação: rodada fictícia com card reescrito deixa dois arquivos de medida e o `review_evidence` os lê.

### R-06 — O card cita a operação pela versão do modelo
- Origem: reg. 36, 37. Ação: `modelo.py check` passa a comparar o texto copiado em `Operação do modelo` com o da operação vigente (nova violação), e a promoção de versão renumera os cards pela lista `tarefas:`. Verificação: `SA-T4` citando `OP-4` depois da promoção sai `check` 1.

### R-07 — `--drift` mostra inserção e propriedade nova
- Origem: reg. 34. Ação: `_diff_fluxo` casa operações por texto antes do número; `_diff_estado` lista propriedade só da pendente como `[+]`. Verificação: o drift do `P-0755` mostra `[+] OP-4` e `[=] OP-5 (era OP-4)`.

### R-08 — A promoção de versão é um comando
- Origem: reg. 37, 38. Ação: `encerrar.py marco --aceita-versao <n>` promove a `## 1A` (mecânico: troca de bloco e linhas do registro), cobra a linha de validação do consultor, e o modelador só é chamado se houver conflito. Verificação: Marco 2 do `P-0755` sem instância de modelador.

### R-09 — `card_check` mede o mundo `depois` também no bloco cercado
- Origem: reg. 10. Ação: na forma de bloco cercado, `--mundo depois` compara com o literal esperado, não com `Medido antes`. Verificação: card de bloco cercado com `depois` errado sai 1.

### R-10 — `card_check` aceita literal com pontuação
- Origem: reg. 11. Ação: o par antes/depois inline passa a ser delimitado por crase (`` antes `x`, depois `y` ``), sem proibir `,`, `;` e `.`. Verificação: literal `a.txt: 3` publicado e conferido.

### R-11 — `card_check` executa `git` de leitura
- Origem: reg. 12. Ação: lista de programas aceitos inclui `git` com subcomandos de leitura (`status`, `diff`, `show`, `ls-files`, `check-ignore`). Verificação: Verificação com `git status --porcelain` roda.

### R-12 — Arquivo de teste existente não perde linha
- Origem: reg. 30 (`AE-98`). Ação: `review_evidence.py` imprime, por arquivo-alvo de teste, as linhas removidas desde o `<ref>` e o revisor as julga; a rubrica ganha o critério. Verificação: a remoção do `AE-97` aparece na evidência.

### R-13 — `review_evidence` sem quedas
- Origem: reg. 25, 26 (`AE-105`, `AE-106`). Ação: o ramo texto compara bytes quando o `<ref>` não decodifica; `--atribuir` falha com mensagem nomeada; `--out` procura a medida também na pasta do plano. Verificação: os dois casos reproduzidos saem sem traceback.

### R-14 — Marca de arquivo novo também no binário e rótulo único
- Origem: reg. 23, 24. Ação: binário novo abre com a marca; a lista por arquivo usa `registro da orquestração` como o resumo. Verificação: evidência da `SA-T1` reproduzida.

### R-15 — Hook de próximo passo só no prompt do dono
- Origem: reg. 42. Ação: `backlog_hook.py` ignora prompt que começa por `<agent-message` ou por `[SYSTEM NOTIFICATION`. Verificação: relatório de subagente com "Próximo passo" não injeta nada.

### R-16 — Telemetria sem lacuna nem duplicata
- Origem: reg. 41, 54. Ação: o despacho de planejador, batedor e modelador declara o id do plano e da tarefa numa linha própria da primeira mensagem, que o hook de telemetria e o de progresso leem antes do primeiro id citado e de `tarefa-corrente.json`; o hook deduplica por `agentId`, ficando a última linha (acumulada); o consultor recebe o card do despacho, não o da tarefa corrente. Verificação: série do plano igual à soma dos `<usage>`, sem linha do plano fictício com id de outro plano, e painel com o título da tarefa despachada.

### R-17 — Pré-voo separa premissa de entregável
- Origem: reg. 2. Ação: `prevoo.py` marca `criar` para caminho precedido de verbo de criação ("crie", "grave", "escreva") e não conta extensão solta como caminho. Verificação: o pedido do `P-0755` sai exit 0 com 6 linhas `criar`.

### R-18 — Diretiva de priorização acompanha o plano que ela anuncia
- Origem: reg. 16. Ação: `backlog.py drain` avisa quando a diretiva não cita nenhum id vivo e o plano drenado não está nela. Verificação: drain do `P-0754` com a diretiva antiga imprime o aviso.

### R-19 — Dedupe de achado por origem, não por texto
- Origem: reg. 39. Ação: o fechamento marca como já registrado o achado do laudo cuja linha de origem (`laudo:<n>`) já foi citada por um `AE-<n>`. Verificação: fechamento da `AUF-T2` reproduzido sem `AE-100`/`AE-101`.

### R-20 — Erro de instrumento em laudo `seguir` sobe ao consultor
- Origem: reg. 47. Ação: achado de processo com alvo `instrumento` e verbo de falha (queda, traceback, exceção) vira pendência substantiva (`B1`), qualquer que seja a recomendação. Verificação: laudo da `AUF-T6` reproduzido vai ao consultor.

### R-21 — Profundidade do planejamento pela classe do plano
- Origem: reg. 8, 9 (e reg. 11/15 do estágio 1). Ação: a Fase 4 ganha uma régua por classe e tamanho (plano de ≤ 5 operações de `produto` dispensa itens que não mudam o resultado). Decisão do dono sobre a doutrina. Verificação: custo de planejamento de um plano de 4 operações ≤ metade dos 352k deste.

### R-22 — Planejador e modelador leem a mesma norma de contrato
- Origem: reg. 7. Ação: a Fase 3a do planejador deixa de pedir caminho no contrato (a norma `TK-76` prevalece). Verificação: dossiê de autoria sem essa restrição.

### R-23 — Instruções impossíveis ao planejador subagente
- Origem: reg. 15. Ação: `checar-versao-kit` roda na condução antes do despacho do planejador, e o resultado vai no dossiê. Verificação: a definição do planejador não manda invocar skill.

### R-24 — Filtro do pytest não engole o exit de comando encadeado
- Origem: reg. 45. Ação: o hook só reescreve o segmento do pytest, não o comando inteiro. Verificação: `pytest -q x; echo $?` devolve o exit do pytest.

### R-25 — Mensagem de marco nomeia o que o dono já pediu
- Origem: reg. 46. Ação: o repertório de mensagens ao gerente ganha a forma de marco que cita o ato do dono de origem ("a auditoria que você pediu em …"). Verificação: próxima mensagem de marco sem pergunta de esclarecimento.

### R-26 — A Fase 5 nomeia a árvore em que o card mede o `antes`
- Origem: reg. 13. Ação: o protocolo da Fase 5 do `pantonic-planner` fixa que o card cujo `antes` depende de antecessor mede o `antes` na cópia do ensaio com os antecessores aplicados, e só o primeiro card de cada cadeia mede contra a árvore real; o registro da medida nomeia a árvore. Verificação: card dependente com `antes` diferente nos dois mundos passa a Fase 5 sem ajuste de valor.

### R-27 — O item 14 admite a operação de estado final igual
- Origem: reg. 14. Ação: o item 14 da Fase 4 ganha a forma da operação cujo estado final é "igual" (revisão sem texto novo): a linha discriminante é a invariância do alvo contra o `<ref>` (`git diff <ref> --numstat -- <alvo>` vazio), declarada como tal. Verificação: card de revisão sem texto novo passa o item 14 com uma linha que falha quando o alvo muda.

### R-28 — Prefixo de decisão único entre planos
- Origem: reg. 17. Ação: `backlog.py check` recusa plano cujo prefixo de decisão (`D<XX>-`) já é usado por outro plano de `docs/plans/`, nomeando o plano dono. Verificação: plano novo com `DSA-` ao lado do `P-0749` sai com exit 1 e o nome do `P-0749`.

### R-29 — `next` limitado ao plano corrente
- Origem: reg. 18. Ação: `backlog.py next` com plano corrente imprime o corpo só de card desse plano; card de outro plano sai numa linha com id e título. Verificação: `next` durante o planejamento do plano fictício não imprime o corpo da `AUF-T16`.

### R-30 — Curinga de alvo com a semântica do glob de shell
- Origem: reg. 27 (`AE-104`). Ação: em `review_evidence.py`, o `*` do alvo não atravessa `/` e `**` casa subpastas, no lugar de `fnmatch.fnmatchcase`. Verificação: `relatorios/*.md` não casa `relatorios/sub/x.md`, e `relatorios/**/*.md` casa.

### R-31 — Caminho com escape octal chega decodificado
- Origem: reg. 28 (`AE-99`). Ação: `coletar_arquivos_tocados` lê o `git status` com `-z` (ou decodifica o caminho entre aspas com escape octal) antes de entregá-lo a `montar_trechos`. Verificação: não rastreado com acento no nome sai com o diff, não como `arquivo ausente`.

## 6. Custo medido da execução do plano fictício

Origem de todo número: o bloco `<usage>` da notificação de conclusão de cada subagente nesta sessão (2026-09-28), somado por papel; a sessão principal, pelo transcript (`message.usage`, uma entrada por resposta). Nenhum valor de memória.

| papel | instâncias | tokens (k) | tool uses | duração (s) |
|---|---|---|---|---|
| planejador (Opus) | 3 (SAÍDA 1 + retomada, 3b–5, rodada `RP-1`) | 352,2 | 66 | 1.599 |
| batedor (Opus) | 3 | 142,0 | 47 | 458 |
| modelador (Opus) | 3 (autoria, emenda, promoção) | 197,2 | 36 | 434 |
| executor (Sonnet 3 / Haiku 2) | 5 | 229,4 | 57 | 292 |
| revisor (Opus) | 5 | 269,8 | 68 | 425 |
| consultor (Opus) | 1 | 59,4 | 15 | 225 |
| **total de subagentes** | **20** | **1.250,0** | **289** | **3.433 (≈ 57 min)** |

Produto: 3 amostras, um script de ~40 linhas, 5 testes, uma revisão sem texto. Razão fase intelectual : execução = 1.020,6 : 229,4 ≈ 4,4 : 1 (estágio 1: 5,4 : 1). A série `docs/telemetria.tsv` registrou 1.138,0k em 18 linhas (reg. 41).

**Sessão principal no loop fictício** (do despacho da `SA-T1` ao fechamento da `SA-T4`): 29 turnos, 14.081k tokens de contexto reenviados (485,6k por turno), 21,3k de saída.

**Loop real das `AUF-T1`..`AUF-T15`**, para comparação: subagentes 1.553,7k em 31 linhas da série (15 executores, 15 revisões, 1 consultor); sessão principal 101 turnos, 28.847k de contexto reenviado (285,6k por turno), 91,5k de saída.

## 7. O que ficou na árvore e o que foi descartado

**Descartado** (restaurado do retrato inicial tirado antes do primeiro ato da sonda, `%TEMP%\claude\auditoria\p0754_retrato\`): a pasta `docs/plans/P-0755-sonda-auditoria-final/` (plano, `estado.tsv`, cenário, evidências, medidas, laudos, RDO, `operacoes.md`, `entrega.md`), `scratch_sonda/` (três amostras e `contar.py`), `tests/test_sonda_auditoria_final.py`, e as escritas do plano fictício em `docs/DIARIO_DE_OBRAS.md` (diretiva, índice, fila), `docs/plans/_INBOX.md` (contador de volta a `P-0755`), `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv` (18 linhas), `docs/ACIONAMENTOS_CONSULTOR.tsv` (1 linha) e `docs/RDO/INDEX.md`. Cópia integral fora do repositório: `%TEMP%\claude\auditoria\p0754_artefatos\`. O ensaio do planejador em `%TEMP%\ensaio_p0755` ficou fora do repositório.

**Mantido:** este relatório e os registros do card `AUF-T16` no `P-0754`.

**Conferência depois da limpeza (2026-09-28):** `git status --porcelain=v1 --untracked-files=all` idêntico ao retrato inicial (80 linhas); `docs/plans/` sem pasta `*-sonda-auditoria-final`; `backlog.py check` OK; `pytest --co -q` = `521 tests collected`.

## 8. As ações mecânicas do gerente do loop

Custo por passo medido no transcript da sessão principal: turnos e contexto reenviado no loop real (15 tarefas) e no fictício (5 tarefas, 1 consultor, 2 atos de modelo, 1 rodada). "Mecânica" = a ação segue regra fechada sobre dados já disponíveis. Nenhum passo se remove, funde ou substitui: o `scrum-master` fica no loop.

| passo | ação | mecânica | instrumento que a cobre | custo medido no plano fictício | recomendação |
|---|---|---|---|---|---|
| P1 | gate de modelo da sessão | sim | hook `UserPromptSubmit` de modelo-por-fase | 0 turno próprio (injeção do hook em toda mensagem) | nenhuma |
| P2 | seleção da próxima tarefa | sim | `backlog.py next` | juntado ao P3 num turno por tarefa (real: 15 turnos) | R-02 (o `despachar` já seleciona; o `next` separado só serve ao painel) |
| P3 | gates herdados, `in-progress`, `<ref>`, âncoras | quase toda: `G-PLANREADY` e gate de delegação pedem leitura; âncoras são mecânicas | `backlog.py despachar` (gates 3 e 4, coleta, `in-progress`, `ref`) | 3 turnos em 5 tarefas; real: 38 turnos (23 só de âncoras) | R-03 |
| P4 | despacho do executor | sim, salvo o texto de aviso específico | nenhum (prompt escrito à mão) | 5 turnos, 0,72k de saída por despacho com o card por arquivo (real: 3,06k colado) | R-02 |
| P5 | recepção e materialização de `review` + `card_check --gravar` | sim | `backlog.py status`, `card_check.py --gravar` | juntado ao P6 num turno por tarefa | R-02 (um verbo `receber <ID> <linha>`) |
| P6 | evidência e despacho do revisor | evidência sim; julgamento é do revisor | `review_evidence.py` | 5 turnos de despacho + 5 de evidência | R-12 (numstat na evidência), R-02 (prompt do revisor gerado) |
| P7 | leitura do veredito | sim | linha fixa do revisor + laudo calculado | 0 turno próprio (a primeira linha basta) | nenhuma |
| P8 | roteamento do bloco A | sim, salvo a triagem do consultor | tabela da skill; consultor para escalas | 1 turno (consultor) | R-04, R-20 |
| P9 | handover e fechamento | fechamento sim; o texto do handover é redigido | `encerrar.py handover` + `encerrar.py tarefa` | 5 turnos (real: 13) | R-02 (handover pré-preenchido pela linha do executor e pelo numstat) |
| P10 | continuar ou encerrar (bloco B) | sim | `review_evidence --atribuir` (B0), hook de ocupação (B2) | 0 turno próprio (decidido na saída do P9) | nenhuma |

**O que a medida mostra sobre o `AE-95`.** As ações mecânicas já estão quase todas em instrumento (P1, P2, P3, P5, P7, P9, P10); o gerente gasta em média 5,8 turnos por tarefa no fictício e 6,7 no real, e o que resta à mão é redação de prompt (P4, P6), re-derivação de âncora (P3) e texto de handover (P9) — as três mecanizáveis por R-02 e R-03. **O custo, porém, não está no número de turnos: está no tamanho do contexto que cada turno reenvia** (285,6k no real, 485,6k no fictício), porque planejamento, loop e auditoria correram numa janela só. Cortar turnos ajuda linearmente; abrir o loop em contexto novo (R-01) corta o custo por turno pela metade ou mais, sem tirar o julgamento do `scrum-master` do loop.
