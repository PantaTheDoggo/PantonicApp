# Operações as-is — P-0750, a mensagem ao dono se entende sozinha

Documento de validação do plano `docs/plans/P-0750-comunicacao-agente-humano.md`. Descreve o que o
kit faz hoje, depois das 6 tarefas do plano (`CAH-T1`, `CAH-T2`, `CAH-T3`, `CAH-T4`, `CAH-T5`,
`CAH-T4a`), todas `done`, nenhuma `cancelled`. Saídas citadas foram rodadas em 2026-09-25, na árvore
do hub.

## Por que o plano existiu

**O problema.** Mensagens de agente ao dono citavam siglas sem dizer o que nomeavam, e o dono
pagava em prompts para descobrir. Três casos medidos: em 2026-08-13 um handover citou `DP-F`,
`DP-I`, `DP-J` e `DP-L` sem expansão, e o dono deduziu "Decisão Pendente", errado (1 prompt); em
2026-09-19 um relatório de janela citou as regras de roteamento só pelo identificador, e o dono
pediu glossário citando `A10` e `B6`, que não existem (1 prompt); em 2026-09-24 o termo "evidência
mecânica" chegou vago. A causa do segundo caso estava escrita no kit: a skill `scrum-master`
mandava citar a regra que encerrou a janela "pelo identificador". O glossário do `README.md`
definia 3 famílias de sigla, de ~25 em uso, e nunca dizia o que `DR`/`DP` ou `RDO` significam.

**A solução, em uma frase.** A sigla deixa de chegar sozinha ao dono: vai o título entre aspas —
o mesmo padrão que o painel do gerente já usava —, com uma regra na doutrina, um procedimento em
skill e uma tabela onde a falha se registra.

**Vocabulário mínimo.**

| termo | o que é |
|---|---|
| dono | o humano que decide sobre o projeto e lê as mensagens dos agentes |
| sigla | identificador curto de um artefato: `CAH-T4` (tarefa), `TK-38` (tíquete), `P-0750` (plano), `DCH-2` (decisão) |
| título | o nome em palavras do artefato, na primeira linha do cabeçalho dele |
| painel do gerente | o arquivo `.claude/estado/progresso.txt`, que um gancho do kit escreve a cada passo da execução, já com o título no lugar da sigla |
| superfície agente↔agente | texto que um agente escreve para outro (dossiê de tarefa, linha de retorno, laudo); ali a sigla crua continua sendo o contrato |
| doutrina | `GOVERNANCA.md`, o arquivo de regras do kit |
| regulamento global | `.claude/global/CLAUDE.md`, as regras que o dono copia para `~/.claude/CLAUDE.md` e valem em todo projeto |

## O arco

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. a regra | o que toda mensagem ao dono tem de cumprir? | `CAH-T1` |
| 2. o insumo | onde se acha o que cada sigla nomeia, e onde se anota quando falha? | `CAH-T2`, `CAH-T3` |
| 3. o procedimento | como um agente aplica a regra antes de enviar? | `CAH-T4`, `CAH-T4a` |
| 4. as fontes do defeito | quais textos do kit mandavam citar sigla, e o que dizem agora? | `CAH-T5` |

Sem a regra, o procedimento não tem o que aplicar; sem glossário e tabela, o procedimento não tem
onde buscar o título nem onde registrar a falha; sem trocar os textos que mandavam citar sigla, o
kit continuaria ensinando o defeito.

## `CAH-T1` — A regra, na doutrina e no regulamento global

**Contexto que a motivou:** a regra de ouro ("mensagem que obriga o dono a abrir outro documento ou
criar um prompt é ineficiente") vivia só na prosa de um tíquete; nenhum agente a lia.

**O que é o artefato:** o bullet *Mensagem legível ao dono* em `GOVERNANCA.md` §4.2 (linha 567),
logo depois de *Artefato de humano mínimo*; e a Regra 9 em `.claude/global/CLAUDE.md` (linha 168),
eco curto para projetos que não têm `GOVERNANCA.md`.

**Como funciona na prática:** é regra de conduta, lida por todo agente que carrega a doutrina ou o
regulamento global. Ela exige três coisas: (a) o que o dono precisa para decidir vem no corpo da
mensagem, e caminho de arquivo é só complemento; (b) nenhuma sigla chega sozinha — vai o título
entre aspas duplas, e a sigla só o acompanha entre parênteses quando o dono precisa digitá-la para
agir; (c) a glosa vai no idioma da conversa. Pergunta do dono do tipo "o que é isso?" passa a ser
falha medida, registrada antes da resposta. Exemplo da própria regra: `Próximo: o tíquete
"Comunicação entre agente e humano — skill própria e requisitos mínimos" (TK-38).`

**Protege contra:** o agente escrever ao dono no dialeto interno do plano.

## `CAH-T2` — O glossário diz o que cada família de sigla nomeia

**Contexto que a motivou:** o glossário definia só `P-NNNN`, `TK-` e `DR-`/`DP-`, sem dizer o que
as letras significam; `RDO` nunca era expandido.

**O que é o artefato:** no glossário do `README.md`, o bullet de decisão reescrito e o bullet novo
*Identificadores de trabalho* (linha 188).

**Como funciona na prática:** é consulta. O bullet de decisão agora diz com franqueza que as letras
depois do `D` não abreviam palavra e que o número só vale dentro do plano que o define. O bullet
novo lista cada família — tarefa `<PFX>-T<n>`, operação `OP-<n>`, fato/invariante/questão/risco
`F-`/`I-`/`Q-`/`R-`, achado `AE-<n>`, `RDO` (registro canônico de tarefa fechada, do *Relatório
Diário de Obra* da construção civil), testes `TF-`/`TR-`, guardrail `G-<NOME>`, regras de
roteamento `A<n>`/`B<n>` e frases do painel `M-<n>`.

**Protege contra:** o agente — ou o dono — não ter onde descobrir o que uma sigla nomeia.

## `CAH-T3` — A tabela de falhas de comunicação

**Contexto que a motivou:** as falhas medidas estavam espalhadas em prosa no diário e num plano; o
registro previsto antes tinha sido cancelado.

**O que é o artefato:** o arquivo `docs/FALHAS_COMUNICACAO.tsv`, uma linha por falha, colunas
separadas por TAB: `data`, `superficie`, `o_que_faltou`, `custo_prompts`, `correcao`, `fonte`.

**Como funciona na prática:** quem recebe do dono uma pergunta de esclarecimento acrescenta uma
linha antes de responder, sem reescrever as anteriores. Hoje tem as três falhas medidas; a primeira:

```
2026-08-13	handover	siglas DP-F, DP-I, DP-J e DP-L sem expansão; o dono inferiu "Decisão Pendente", errado	1	regra Mensagem legível ao dono	docs/DIARIO_DE_OBRAS.md ## TK-38
```

A tabela se lê em conjunto na revisão periódica da doutrina (`GOVERNANCA.md` §7.1).

**Protege contra:** a falha de comunicação sumir sem deixar medida.

## `CAH-T4` e `CAH-T4a` — A skill da mensagem ao dono

**Contexto que a motivou:** uma regra de conduta não diz *como* achar o título de cada sigla nem
como montar um pedido de decisão.

**O que é o artefato:** a skill `.claude/skills/mensagem-ao-dono/SKILL.md`, inscrita na tabela
*Skills* do `README.md` (linha 874); a frase de contagem da seção passou a "doze skills" (linha
840). O `.claude/README.md` foi regenerado pelo gerador do kit.

**Como funciona na prática:**
1. **O que dispara:** um agente vai enviar ao dono mensagem que cita sigla ou aponta arquivo, ou
   recebe do dono pergunta "o que é / onde está".
2. **A entrada:** o rascunho da mensagem.
3. **O processamento:** uma checagem de cinco itens (§1) e uma tabela de onde achar o título (§2).
   Para tarefa, tíquete e plano, o título é o texto da primeira linha de `backlog.py show <ID>`
   entre ` — ` e ` [`. Saída real de `python .claude/tools/backlog.py show CAH-T4`:
   `### CAH-T4 — A skill da mensagem ao dono [Sonnet · esforço medium · classe redacao]` → título
   *"A skill da mensagem ao dono"*. Sem ` [` na linha (tíquete e plano), vai até o fim.
4. **A saída:** a mensagem com títulos entre aspas; na falha, uma linha na tabela de `CAH-T3`.

O verificador `check-readme.ps1` confere a inscrição: `check-readme: OK - 10 agente(s), 12
skill(s), 20 guardrail(s), …`, exit 0.

A `CAH-T4a` é o corretivo de uma célula: o texto original mandava pegar "o texto depois de ` — `",
o que trazia junto a etiqueta `[Sonnet · esforço medium · classe redacao]`.

**Protege contra:** cada agente inventar a própria maneira de nomear as coisas ao dono.

## `CAH-T5` — Os textos que mandavam citar sigla passam a mandar o título

**Contexto que a motivou:** a skill `scrum-master` mandava citar, no relatório de janela, a regra
que encerrou a janela "pelo identificador" e cada tarefa "com identificador" — a causa direta do
caso de 2026-09-19.

**O que é o artefato:** quatro trocas de texto: `.claude/skills/scrum-master/SKILL.md` linhas 292 e
293 (relatório de encerramento), `.claude/agents/pantonic-planner.md` linha 164 (rodada de
decisões), `.claude/skills/redacao-doc/SKILL.md` linha 12 (fronteira).

**Como funciona na prática:** o relatório de janela agora cita o plano pelo título e a regra que
encerrou a janela pela condição em palavras, com o identificador entre parênteses; cada tarefa
fechada vai pelo título. A rodada de decisões do planejador cita objeto pelo título. A
`redacao-doc` declara que mensagem de conversa ao dono não é documento publicado e aponta para a
regra nova. A superfície agente↔agente (tabelas de roteamento, painel, dossiês) não mudou.

**Protege contra:** o próprio kit instruir o agente a escrever sigla crua ao dono.

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| mensagem legível ao dono | o dono decide sem abrir arquivo nem perguntar | `GOVERNANCA.md` §4.2; `.claude/global/CLAUDE.md` Regra 9 |
| procedimento da mensagem | checagem, busca do título, pedido de decisão, registro de falha | `.claude/skills/mensagem-ao-dono/SKILL.md` |
| falha medida vira linha | a comunicação ruim deixa rastro contável | `docs/FALHAS_COMUNICACAO.tsv` |

## Os ganhos, medidos

| medida | antes | depois |
|---|---|---|
| famílias de sigla explicadas no glossário | 3 bullets (`P-NNNN`, `TK-`, `DR-`/`DP-` sem expansão) | os 3, com as letras de decisão explicadas, + o bullet *Identificadores de trabalho* com 9 linhas de família |
| textos do kit que mandavam citar sigla ao dono | 2 linhas (`scrum-master` 292–293) | 0 |
| falhas de comunicação registradas em forma contável | 0 | 3 |
| suíte de testes | 353 passed | 353 passed |

Ainda não há medida de efeito: a prova de que a regra pegou é a próxima mensagem ao dono, e a
Regra 9 só vale fora deste repositório depois que o dono a copiar para `~/.claude/` (pendência 1).

Custo da execução (telemetria medida, `docs/telemetria.tsv`, linhas `CAH-*`): 987,5 mil tokens,
dos quais 373,7 mil nos executores (Sonnet) e 613,8 mil em revisores e consultor (Opus).

## O padrão que a execução revelou

Nenhum defeito veio da execução: as 6 entregas saíram iguais ao texto literal dos cards, todas
aprovadas com 100%. Todos os defeitos vieram da **autoria dos cards** — o texto que o card mandava
escrever ou conferir estava errado ou incompleto. Um comando de verificação não compilava, um total
de testes fixo envelheceu, uma âncora por número de linha se deslocou, uma frase de contagem ficou
fora do card, e um literal descrevia mal a saída de um instrumento.

## Defeitos da execução, com estado

| defeito | estado | o que fecha |
|---|---|---|
| comando da Verificação 1 da `CAH-T1` com parêntese a mais (`AE-1`) | 🟡 caso fechado, classe sem guarda | régua de autoria, pendência 2 |
| total da suíte como literal de aceite, envelhecido (`AE-2`) | 🟡 caso contornado no despacho; classe sem guarda | pendência 2 |
| âncora de edição por número de linha (`AE-4`) | 🟡 caso contornado no despacho | pendência 2 |
| frase "onze skills" fora do card da skill (`AE-6`) | 🟢 fechado com guarda: `check-readme.ps1` barra a divergência | — |
| título de tarefa com a etiqueta na skill (`AE-7`) | 🟡 caso fechado pela `CAH-T4a` | pendência 2 |
| evidência de revisão lista não rastreados antigos como "sem atribuição" (`AE-3`, 9 recorrências) | 🔴 conhecido, não corrigido | pendência 3 |
| retorno do executor com prosa depois da linha (`AE-4`, anexo) | 🔴 conhecido, não corrigido | pendência 4 |

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| 1 | copiar o regulamento global para `~/.claude/CLAUDE.md` | é ato do dono, fora do repositório | `materializar.py apply --alvo usuario` pelo dono (tíquete `TK-68`) | a Regra 9 não vale em outros projetos até lá |
| 2 | régua de autoria de card | fora do escopo deste plano | tíquete `TK-72` ("A régua de autoria de card do kit") | não |
| 3 | evidência de revisão sem separar não rastreados antigos | fora do escopo; instrumento `review_evidence.py` | tíquete `TK-55` | não; custa reconciliação manual a cada revisão |
| 4 | prosa depois da linha de retorno do executor | fora do escopo | tíquete `TK-79` | não |
| 5 | propagar a skill e a regra aos projetos derivados | a doutrina assenta primeiro no hub | tíquete `TK-81` | não |
| 6 | resolvedor sigla→título por função | registrado e não agido por decisão do plano | um plano futuro, se a busca manual se mostrar cara | não |

**Estado honesto.** O plano entregou a regra, o glossário, a tabela de falhas, a skill e a troca dos
textos que mandavam citar sigla — 6 de 6 tarefas, todas aprovadas com 100%. Ficaram 6 pendências,
nenhuma bloqueante dentro do projeto; a única com efeito **fora** dele é a 1: sem a cópia do
regulamento global, a Regra 9 só existe neste repositório. O efeito real da regra ainda não foi
medido. **Nada commitado.**
