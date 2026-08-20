# P-0733 — Quitação da dívida de doutrina e de kit do hub

- **Origem:** 2026-08-08 — encerramento da `SPRINT-PANTONICV2`: com os sete estágios terminais, o
  backlog vivo do hub passou a ser inteiramente tíquete avulso, e quatro deles estavam decididos há
  dias sem tarefa que os executasse
- **Iniciativa:** nenhuma — plano único, sem estágios · **Prefixo de tarefa:** `DHB-`
- **Depende de:** `docs/plans/P-0732-v2-portas-do-core.md`, fechado 10/10
- **Fecha em:** aceite do dono sobre o `README.md` (`T13`), dever 2 de `G-README`
- **Sem bump, sem tag, sem instrução de migração por número:** a versão está congelada em `0.0.0`
  (`DE-7`); todo registro de mudança vai para a seção `[Não lançado]` do `CHANGELOG.md`
- **Checagem de versão do kit:** modo hub — versão **congelada em `0.0.0`**, comparação local ×
  remoto **suspensa**, nada a comparar. O gatilho da porta de saída de guardrail
  (`GOVERNANCA.md` §7.1, regime da `DE-8`) está **armado** pelo fechamento do plano anterior: há uma
  rodada de revisão **pendente**, e ela é a `T2` deste plano — não fica como vão

## 0. O problema

Doze tíquetes avulsos estão vivos no índice do diário, e eles não são uma lista de defeitos soltos:
são três dívidas com forma própria.

A primeira é **doutrina decidida e não executada**. Quatro tíquetes (`TK-15`, `TK-17`, `TK-21`,
`TK-22`) têm veredito do dono registrado, com alternativas recusadas e superfícies medidas — falta
só quem execute. Decisão que não vira mudança apodrece igual a regra que ninguém cumpre, e o
intervalo entre decidir e executar é exatamente onde o contexto que sustentou a decisão se perde.

A segunda é **resíduo de vocabulário do kit**. Três artefatos (`pantonic-executor`, `audit-sweep`,
`integrar-poc`) ainda carregam um número de orçamento hardcoded, uma menção de toolkit e um par de
componentes da implementação de referência citados onde a doutrina deveria citar a porta. Todos
sobreviveram a varreduras anteriores por estarem fora do recorte de arquivo daquelas tarefas.

A terceira é **guarda e navegação desalinhadas do que guardam**. O `check-readme.ps1` não enxerga
seção não numerada; o `DOC_MAP.md` manda ler integralmente um documento que dobrou de tamanho; o
diário passou de 2.000 linhas contra um gatilho de condensação de ~500, e todo pickup futuro paga
esse tamanho.

O encerramento é a dívida que só existe depois das outras: a **revisão final do espelho**
(`TK-18`), postergada por decisão do dono justamente até que as fontes parassem de mudar.

## 1. Decisões (fechadas no ato do planejamento)

- **`DH-1` — Escopo travado nos doze tíquetes vivos.** O plano quita `TK-04`, `TK-06`, `TK-07`,
  `TK-08`, `TK-10`, `TK-12`, `TK-15`, `TK-17`, `TK-18`, `TK-20`, `TK-21` e `TK-22`. Achado novo
  durante a execução vira tíquete novo, nunca tarefa deste plano.
- **`DH-2` — `TK-07`, veredito do dono: o guarda cobre toda seção `##`.** A exigência de
  `> Fonte da verdade:` deixa de valer só para as numeradas. Duas consequências medidas condicionam
  a correção: (a) o `README.md` tem duas linhas `^## ` **dentro de um bloco cercado** ```` ```markdown ````
  (exemplo da forma do diário) — indexá-las quebraria o guarda, então a varredura passa a ignorar
  região cercada; (b) o glossário **já declara** sua fonte da verdade, então nenhuma prosa nova é
  necessária e a contagem final do guarda vai de 14 para 15 seções.
- **`DH-3` — `TK-08`, veredito do dono: "estágio" permanece convenção.** O conceito não sobe para
  `GOVERNANCA.md` nem para skill. O tíquete fecha registrando a não-promoção: promover agora criaria
  regra sem objeto — a iniciativa que a justificava terminou e este plano não tem estágios. Quando
  abrir a próxima iniciativa longa, o conceito se escreve com uso real na mão.
- **`DH-4` — `TK-21`, residência da invocação do ratchet: a skill `guardrails-check`.** É a bateria
  de fechamento que roda no projeto que tem código de produção, e é lá que o piso tem objeto.
  Medido: `ratchet_piso.py` **já aceita `--root`** e já resolve a raiz do repositório invocador por
  padrão — nenhuma linha de código nova. O ratchet **sai** da bateria de fechamento do hub, onde
  reporta `nenhum piso declarado` em toda rodada: check que nunca tem objeto é a vacuidade que a
  §7.1 manda tirar. Recusadas: a bateria do hub apontando `--root` para um consumidor (o hub
  passaria a precisar conhecer o caminho de cada consumidor, e o fechamento de uma tarefa de
  doutrina nada tem a ver com o comportamento de um consumidor) e o fechamento de tarefa do
  consumidor fora do kit (é a mesma coisa que `guardrails-check`, só que sem residência).
- **`DH-5` — `TK-18`, a fidelidade do espelho permanece sob conferência humana.** Nenhum guarda de
  diff texto-a-texto nasce aqui: comparar espelho e fonte mecanicamente exige uma regra canônica de
  extração do trecho espelhado, que não existe e é projeto próprio; e verificador construído sem
  alvo é o que `G-DEADCODE` proíbe. O guarda executável continua sendo estrutural (presença da
  declaração de fonte por seção). Se a varredura achar uma seção mecanicamente comparável, isso vira
  tíquete — não tarefa deste plano.
- **`DH-6` — `TK-17` parte em duas fatias.** ~25 ocorrências em quatro seções de um arquivo de 779
  linhas passam de 8 write-clusters; o corte é por seção, e o somatório das duas é exatamente o
  tíquete.
- **`DH-7` — Sem número de versão novo e sem tag.** Congelamento `DE-7`; o registro da mudança é uma
  entrada consolidada em `[Não lançado]`, na `T11`.

## 2. Alcance medido (insumo — nada inferido na execução)

- `docs/DIARIO_DE_OBRAS.md`: **2.070 linhas** contra o gatilho de condensação de ~500;
  `docs/DIARIO_HISTORICO.md` já em **1.007 linhas**.
- `GOVERNANCA.md`: **779 linhas**. `docs/DOC_MAP.md` (102 linhas) ainda o lista entre os documentos
  "abaixo de 500 linhas (Read direto)", sem entrada de âncoras.
- `README.md`: **923 linhas**, 14 seções numeradas mais o glossário não numerado (`L36`, já com
  `> Fonte da verdade:` declarada em `L38-39`); as duas linhas `^## ` de `L517` e `L523` estão
  dentro do bloco cercado aberto em `L512`.
- `.claude/checks/check-readme.ps1`: o índice de seções é montado em `L56-59` pelo padrão
  `'^## (\d+)\. '`; é consumido pela busca da seção "Anatomia do kit" (`L77-78`), da seção "Os
  guardrails" (`L160-161`), pelo laço de `> Fonte da verdade:` (`L202-204`) e pela contagem final
  (`L230`).
- `.claude/checks/ratchet_piso.py`: `--root` declarado em `L125`, resolvido em `L134-135`, com raiz
  padrão derivada do próprio script em `L124`.
- `.claude/skills/redacao-doc/SKILL.md`: a classe a remover é a **linha do meio** da tabela do §5,
  em `L150`.
- `.claude/skills/checar-versao-kit/SKILL.md`: `L84` faz Grep por `Registro das rodadas`.
- `GOVERNANCA.md` `L600`: a prosa "Cada rodada entra na lista abaixo…" mais o bloco que ela abre.
- Alvos de resíduo: `.claude/agents/pantonic-executor.md:20`, `.claude/skills/audit-sweep/SKILL.md:3`,
  `.claude/skills/integrar-poc/SKILL.md:23`.

## 3. Invariante de execução (vale para todas as tarefas)

1. **Números de linha do §2 são insumo, não verdade permanente.** Toda tarefa reconfirma sua âncora
   por Grep antes de editar — as fatias anteriores deslocam as posteriores.
2. **Toda tarefa fecha verde.** Uma tarefa que invalide uma linha do `README.md` corrige essa linha
   no próprio escopo; o guarda não fica vermelho entre tarefas. Isso não autoriza varredura de prosa
   do README fora da `T12`.
3. **Redação.** `.claude/skills/redacao-doc/SKILL.md` é normativa em tudo que este plano manda
   escrever em documento publicado: nada de `V3` (id de plano, tarefa ou tíquete no corpo) e nada de
   `V7` (datação viva). O plano é registro e é isento; o que ele produz não é.
4. **Contrato, nunca implementação.** Nenhum trecho pode nomear toolkit, plataforma ou componente da
   implementação de referência como regra universal — a régua da `DE-1` continua valendo.
5. **Verificação de fechamento de toda tarefa** — os quatro em exit 0:
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate`,
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift`,
   `pwsh -NoProfile -File .claude/checks/check-readme.ps1`,
   `python -m pytest` na raiz do hub.

## 4. Tarefas

### T1 — Condensar o diário de obras (`TK-10`) [Sonnet]
- **Objetivo:** trazer o kanban de volta para perto do gatilho de ~500 linhas, para que todo pickup
  posterior custe menos.
- **Arquivos-alvo:** `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`.
- **Forma:** operação "Condensar" da skill `diario-de-obras`. Migram as seções de estágio terminais
  (Estágios 1 a 7 da iniciativa encerrada) e os blocos de tíquete já `done`; permanecem no diário o
  índice íntegro, a diretiva de priorização, os tíquetes não terminais e a seção deste plano.
- **Proibido:** apagar conteúdo (condensar é mover, com ponteiro), alterar status de qualquer item,
  reescrever a linha de índice de item terminal.
- **Verificação:** bateria do §3; `wc -l` no diário abaixo de ~500; todo ponteiro de âncora do
  índice resolve (Grep pela âncora citada em cada linha da tabela).
- **Pronto quando:** o diário cabe numa leitura de pickup e nada foi perdido — só mudou de arquivo.

### T2 — Segunda rodada da porta de saída de guardrails (`DE-8`) [Opus]
- **Objetivo:** consumir o gatilho armado pelo fechamento do `P-0732`, no regime que pendura a
  revisão no fechamento de plano.
- **Arquivos-alvo:** `GOVERNANCA.md` §7.1, bloco *Registro das rodadas* (entrada nova, rótulo
  `P-0732`); `docs/DIARIO_DE_OBRAS.md`.
- **Forma:** o procedimento da §7.1, item a item sobre os 14 guardrails da lista do §7, com o
  resultado de cada um registrado (marcado, retido com caso citável, ou removido). Guardrail retido
  sem caso citável é reportado como tal — não vira remoção automática.
- **Proibido:** remover guardrail sem o procedimento completo; contar a rodada por calendário.
- **Verificação:** bateria do §3; a entrada da rodada existe com resultado item a item.
- **Pronto quando:** o gatilho está desarmado e a lista do §7 reflete a rodada.

### T3 — Resíduos de vocabulário do kit (`TK-04`, `TK-12`, `TK-20`) [Sonnet]
- **Objetivo:** tirar dos três artefatos o que a doutrina já diz em outro lugar ou já proibiu.
- **Arquivos-alvo:** `.claude/agents/pantonic-executor.md` (`TK-04`),
  `.claude/skills/audit-sweep/SKILL.md` (`TK-12`), `.claude/skills/integrar-poc/SKILL.md` (`TK-20`),
  e `.claude/README.md` regenerado ao final.
- **Conteúdo:** (a) o orçamento numérico hardcoded no agente sai e passa a apontar para a tabela de
  tetos por classe de `GOVERNANCA.md` §3, única autoridade numérica; (b) a menção de toolkit no
  `description` do frontmatter da `audit-sweep` sai, alinhando com os blocos que já foram extraídos;
  (c) o par de componentes da implementação de referência na `integrar-poc` passa ao vocabulário de
  portas de `ARQUITETURA_PANTONICA.md` §4 (raiz de dados e execução assíncrona).
- **Proibido:** introduzir número de orçamento novo em qualquer artefato; renomear skill ou agente.
- **Verificação:** bateria do §3; `Grep -iE "pyside|\bqt\b|≤ *40 tool"` nos três arquivos → vazio;
  `Grep -E "PathsService|TaskRunner"` em `.claude/skills/integrar-poc/SKILL.md` → vazio.
- **Pronto quando:** nenhum dos três diz sobre o framework algo que só valia para o case.

### T4 — A classe "Seção histórica declarada" sai da `redacao-doc` (`TK-15`) [Opus]
- **Objetivo:** executar o veredito do dono — doc publicado não é lugar de histórico, e a isenção
  por tipo de seção era o que mantinha o vício vivo por rodadas.
- **Arquivos-alvo:** `.claude/skills/redacao-doc/SKILL.md` (tabela do §5).
- **Conteúdo:** a tabela do §5 passa a ter **duas** entradas — **publicado** (`V1..V10` proibidos) e
  **registro** (isento). O §4 continua apontando "o que mudou entre versões → `CHANGELOG.md`", que é
  a residência do histórico.
- **Proibido:** criar isenção substituta sob outro nome; tocar o §6 (varredura mecânica).
- **Verificação:** bateria do §3; a tabela do §5 tem duas linhas de dados; `Grep -i "histórica
  declarada"` no kit inteiro → vazio.
- **Pronto quando:** a skill não oferece mais nenhuma porta de saída para datação viva em documento
  publicado.

### T5 — Residência própria do bloco *Registro das rodadas* (`TK-22`) [Opus]
- **Objetivo:** tirar da `GOVERNANCA.md` um bloco que é registro por desenho, para que a limpeza da
  `T6`/`T7` possa valer para o arquivo inteiro sem exceção.
- **Arquivos-alvo:** `GOVERNANCA.md` §7.1 (o bloco e a prosa que o abre);
  `.claude/skills/checar-versao-kit/SKILL.md` (o Grep que lê o registro); `docs/DOC_MAP.md` (o
  documento novo entra no mapa); o arquivo de destino, novo.
- **Conteúdo:** o registro ganha documento de finalidade estrita, isento das restrições de redação, e
  a §7.1 passa a apontar para ele em vez de conter a lista. O mecanismo que lê o registro passa a ler
  no destino novo, preservando a forma do rótulo e a localização de "última" e "penúltima" rodada.
  Entram no destino as entradas já existentes, incluindo a que a `T2` acabou de gravar.
- **Proibido:** reusar o `CHANGELOG.md` (recusado por medida — o caso comum de uma rodada é
  0 marcações, e a chave de organização é a versão, não o fechamento de plano); mudar o formato do
  rótulo; deixar a §7.1 sem ponteiro.
- **Verificação:** bateria do §3; Grep pelo rótulo da última rodada resolve no destino novo;
  `Grep -n "Registro das rodadas" GOVERNANCA.md` → só o ponteiro, nunca a lista.
- **Pronto quando:** o mecanismo da skill continua achando a última rodada, e a `GOVERNANCA.md` não
  guarda mais registro.

### T6 — Limpeza `V3`/`V7` da `GOVERNANCA.md`, §3 e §7 (`TK-17`, fatia 1 de 2) [Opus]
- **Objetivo:** executar o veredito do dono na primeira metade: nenhuma ocorrência sobrevive, nem as
  que enunciam razão como fato medido.
- **Arquivos-alvo:** `GOVERNANCA.md` §3 e §7.
- **Conteúdo:** cada regra sustentada por medição passa a ser afirmada **inline**, sem ponteiro de
  proveniência (padrão já aplicado no `TK-11`); a medição continua registrada onde é histórico
  (plano, diário, `CHANGELOG.md`). A §10, saneada em rodada anterior, é a referência de forma.
- **Proibido:** enfraquecer a regra ao remover a proveniência — o limiar numérico permanece, só perde
  a citação de origem; tocar seção fora da fatia.
- **Verificação:** bateria do §3; varredura do §6 da `redacao-doc` sobre §3 e §7 → zero.
- **Pronto quando:** as duas seções afirmam o que valem sem contar de onde vieram.

### T7 — Limpeza `V3`/`V7` da `GOVERNANCA.md`, §7.1 e §9 (`TK-17`, fatia 2 de 2) [Opus]
- **Objetivo:** fechar o tíquete com o piso de aceite zero valendo para o **arquivo inteiro**.
- **Arquivos-alvo:** `GOVERNANCA.md` §7.1 e §9.
- **Precondição:** a `T5` já tirou o bloco *Registro das rodadas* da §7.1 — sem isso, esta fatia
  precisaria de uma isenção por bloco, que é justamente o que a `T4` acabou de remover da skill.
- **Verificação:** bateria do §3; varredura do §6 da `redacao-doc` sobre o **arquivo inteiro** →
  zero, sem exceção declarada.
- **Pronto quando:** o piso zero vale para a `GOVERNANCA.md` sem nenhuma seção isenta.

### T8 — O guarda do README cobre seção não numerada (`TK-07`) [Sonnet]
- **Objetivo:** fechar o vão em que dava para acrescentar seção sem procedência ao documento
  canônico sem que nada acusasse.
- **Arquivos-alvo:** `.claude/checks/check-readme.ps1`.
- **Conteúdo:** o índice de seções passa a casar `^## ` genérico **ignorando região cercada** (as
  duas linhas do bloco ```` ```markdown ```` de exemplo do diário não são seções). As duas buscas por
  seção nomeada ("Anatomia do kit", "Os guardrails") **mantêm** o padrão numerado — elas dependem do
  número. O glossário já declara sua fonte, então nenhuma edição do `README.md` é necessária.
- **Proibido:** editar o `README.md` para acomodar o guarda; afrouxar qualquer uma das cinco
  checagens; indexar heading dentro de bloco cercado.
- **Verificação:** bateria do §3, com o `check-readme.ps1` reportando **15** seções (era 14) e
  exit 0. Sem teste `pytest` novo: o guarda é o próprio verificador, e envolvê-lo em teste de
  Python está fora de escopo.
- **Pronto quando:** acrescentar uma seção `##` sem `> Fonte da verdade:` faz o guarda falhar.

### T9 — Entrada de navegação da `GOVERNANCA.md` no `DOC_MAP` (`TK-06`) [Sonnet]
- **Objetivo:** o mapa deixa de mandar ler integralmente um documento que passou do limite.
- **Arquivos-alvo:** `docs/DOC_MAP.md`.
- **Ordem:** depois da `T5`, `T6` e `T7` — as âncoras da `GOVERNANCA.md` só param de se mover
  quando aquelas fatias fecharem.
- **Conteúdo:** operação da skill `doc-map` para o documento: âncoras de seção e padrão de Grep de
  acesso, e a saída da lista de "abaixo de 500 linhas (Read direto)".
- **Verificação:** bateria do §3; toda âncora citada na entrada nova resolve por Grep na
  `GOVERNANCA.md`.
- **Pronto quando:** um agente novo chega a uma seção da governança sem ler as 779 linhas.

### T10 — O ratchet do piso passa a rodar onde o piso tem objeto (`TK-21`) [Opus]
- **Objetivo:** executar a `DH-4` — o check sai de onde é vacuidade e ganha residência onde há
  código de produção.
- **Arquivos-alvo:** `.claude/skills/guardrails-check/SKILL.md` (residência da invocação);
  `GOVERNANCA.md` §7 item 6 (o guardrail do piso passa a dizer onde é verificado); a bateria de
  fechamento do hub, de onde o ratchet sai.
- **Proibido:** escrever código novo em `ratchet_piso.py` (`--root` já existe e a raiz padrão já é a
  do repositório invocador); autorar o piso de qualquer consumidor a partir daqui.
- **Fora de escopo, com hand-off:** o `tests/piso_comportamental.txt` do `PantonicVideo` não existe
  e precisa ser autorado — uma frase por comportamento trancado. É trabalho do repositório
  consumidor, com o contexto daquele código; a tarefa registra um tíquete de hand-off no índice
  deste diário e para aí.
- **Verificação:** bateria do §3; a bateria de fechamento do hub não invoca mais o ratchet;
  `guardrails-check` diz com que raiz o ratchet roda.
- **Pronto quando:** o item 6 do §7 aponta para um verificador que tem alvo, e o hub parou de rodar
  um check que sempre reporta ausência de piso.

### T11 — Registro: `TK-08`, `CHANGELOG.md` `[Não lançado]` e fechamento dos tíquetes [Sonnet]
- **Objetivo:** registrar a mudança canônica no único lugar vivo do histórico e fechar no índice os
  tíquetes que este plano quitou.
- **Arquivos-alvo:** `CHANGELOG.md` seção `[Não lançado]`; `docs/DIARIO_DE_OBRAS.md`.
- **Conteúdo:** (a) um bloco consolidado cobrindo a residência do registro de rodadas, a limpeza de
  redação da governança, a classe removida da `redacao-doc`, a cobertura do guarda do README, a
  residência do ratchet do piso e os resíduos de vocabulário do kit; (b) o fechamento do `TK-08`
  registrando a **não-promoção** de "estágio" a conceito normativo, com o motivo (`DH-3`); (c) o
  status final de cada tíquete quitado no índice.
- **Proibido:** número de versão novo, seção numerada nova, tag, instrução de migração expressa por
  número de versão (`DE-7`); reescrever qualquer seção numerada do `CHANGELOG.md`.
- **Verificação:** bateria do §3; `Grep -E "3\.0\.0|kit-v3|bump"` **dentro da seção
  `[Não lançado]`** → vazio (a ocorrência pré-existente na seção histórica `1.5.0` não é tocada, e a
  contagem no arquivo inteiro permanece 1).
- **Pronto quando:** um adotante futuro lê `[Não lançado]` e sabe o que mudou e o que precisa migrar.

### T12 — Revisão final do espelho (`TK-18`) [Opus]
- **Objetivo:** conferir o conteúdo do espelho contra as fontes, agora que as fontes pararam de
  mudar — que era a condição registrada do adiamento.
- **Arquivos-alvo:** `README.md` (correções de fidelidade); `docs/DIARIO_DE_OBRAS.md` (registro dos
  desvios encontrados).
- **Forma:** para cada seção com `> Fonte da verdade:` declarada, confrontar a afirmação do espelho
  com a da fonte e corrigir o espelho onde divergir. A fonte tem precedência: divergência se resolve
  mudando o `README.md`, nunca a doutrina.
- **Proibido:** construir guarda de diff texto-a-texto (`DH-5`); reabrir decisão de doutrina a
  pretexto de fidelidade — divergência que pareça erro **da fonte** vira tíquete e para.
- **Teto:** a varredura é por seção e tem 15 delas; ao atingir **40 tool uses**, o executor para e
  reporta o que já cobriu, com a lista do que falta.
- **Verificação:** bateria do §3; as 15 seções conferidas, com o resultado de cada uma registrado.
- **Pronto quando:** nenhuma seção do espelho afirma coisa diferente da sua fonte.

### T13 — Revisão do `README.md` e veredito do dono [dono]
- **Objetivo:** dever 2 de `G-README` — todo plano encerra com a revisão do documento canônico, e o
  gate de sentido é do dono.
- **Forma, nesta ordem:** (1) rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1` como
  instrumento de paridade estrutural, **nunca** como gate automático de pronto; (2) leitura corrida
  do dono, respondendo se o texto descreve o framework que ele governa, se há afirmação equivocada ou
  desatualizada, e se sustentaria uma decisão justa de adotar ou recusar.
- **Verificação:** veredito registrado no diário; reprovação gera rodada nova de redação, não segue
  adiante.
- **Pronto quando:** aceite explícito do dono registrado no diário. **Fecha o plano.**

## 5. Ordem de execução

`T1` → `T2` → `T3` → `T4` → `T5` → `T6` → `T7` → `T8` → `T9` → `T10` → `T11` → `T12` → `T13` (dono).

Linear, sem ramo condicional. A condensação vem primeiro porque todas as tarefas seguintes leem e
escrevem no diário, e todas pagam o tamanho dele. A rodada de guardrails (`T2`) vem antes da mudança
de residência do registro (`T5`) para que a entrada nova migre junto, em vez de ser gravada duas
vezes. A skill de redação (`T4`) precede a limpeza que ela normatiza (`T6`/`T7`) — aplicar a regra
antes de removê-la a exceção produziria retrabalho na mesma prosa. O `DOC_MAP` (`T9`) vem depois de
tudo que mexe na `GOVERNANCA.md`, porque âncora registrada em documento que ainda vai mudar nasce
podre. O espelho (`T12`) é o penúltimo por definição: ele existe para conferir o resultado das
onze anteriores, e o aceite (`T13`) é o gate de sentido e o encerramento.

`T2`, `T4`, `T5`, `T6`, `T7`, `T10` e `T12` são Opus (doutrina e redação canônica); `T1`, `T3`, `T8`,
`T9` e `T11` são Sonnet; `T13` é do dono.

## 6. Riscos

| Risco | Contenção |
|---|---|
| A condensação (`T1`) mover algo não terminal e sumir com trabalho vivo | Condensar é mover com ponteiro, nunca apagar; a verificação resolve toda âncora do índice por Grep |
| A limpeza `V3`/`V7` enfraquecer regra ao remover a proveniência | O invariante da fatia: o limiar permanece afirmado inline; só a citação de origem sai |
| O afrouxamento do padrão do guarda (`T8`) indexar heading de exemplo dentro de bloco cercado | A `DH-2` fixa a exclusão de região cercada como parte da correção, com as duas linhas já localizadas no §2 |
| A `T10` deixar o guardrail do piso sem verificador em lugar nenhum | O hand-off do piso do consumidor é registrado como tíquete no ato; o item 6 do §7 passa a dizer onde o check roda, e o ratchet já aceita a raiz por argumento |
| A `T12` virar reescrita do README a pretexto de fidelidade | Fonte tem precedência e a correção é sempre do espelho; divergência que pareça erro da fonte vira tíquete e para. Teto de 40 tool uses com parada e relatório |

## 7. Fora de escopo (explícito)

- **Autoria do `tests/piso_comportamental.txt` do `PantonicVideo`** — é do repositório consumidor,
  com o contexto daquele código (`DH-4`); sai daqui como tíquete de hand-off.
- **Guarda executável de fidelidade do espelho** — `DH-5`.
- **Promoção de "estágio" a conceito normativo** — `DH-3`; o tíquete fecha registrando a recusa.
- **Qualquer bump de versão, tag ou instrução de migração por número** — congelamento `DE-7`.
- **Tíquete aberto durante a execução** — vira tíquete novo no índice, nunca tarefa deste plano
  (`DH-1`).

## 8. Achados abertos deste planejamento

*(nenhum — as duas questões que existiam, `TK-07` e `TK-08`, foram levadas ao dono e fechadas antes
da publicação, conforme o gate `G-PLANREADY` item 5)*

## Notas de execução

### 2026-08-08 — DHB-T1 (`TK-10`) — **done**

Condensação via PowerShell (leitura/escrita de linhas, sem `Read` do conteúdo movido): apendadas as
linhas 80..2094 de `docs/DIARIO_DE_OBRAS.md` (seção `## SPRINT-PANTONICV2`, 2015 linhas) ao fim de
`docs/DIARIO_HISTORICO.md` (1007 → 3023 linhas); diário truncado para as linhas 1..78 (índice
íntegro, diretiva de priorização, tíquetes não terminais e a seção `## P-0733` preservados). Índice
repointado — só a célula Âncora, Título/Status intocados: linhas `SPRINT-PANTONICV2` e `TK-08` agora
apontam para `docs/DIARIO_HISTORICO.md#sprint-pantonicv2--consolidação-do-framework-em-v2`.

**Desvio medido:** o insumo do dossiê (diário 1914 linhas / histórico 970) estava desatualizado —
medição desta rodada achou 2094/1007 (o diário cresceu ~180 linhas entre o planejamento e a
execução). O ponto de corte (linha 80, heading `## SPRINT-PANTONICV2`) permaneceu correto; a
operação seguiu com os números reais em vez dos do dossiê.

Verificação: os quatro comandos do §3 item 5 em exit 0 (`kit_check.ps1 -Mode validate`,
`-Mode check-drift`, `check-readme.ps1`, `python -m pytest` — 3 passed); diário em 78 linhas;
âncoras `SPRINT-PANTONICV2` e `TK-08` resolvidas por Grep em `docs/DIARIO_HISTORICO.md`. Sem TF/TR
— tarefa é movimentação de documentação, nenhum código de produção tocado.

Consumo: ver docs/telemetria.tsv

---

## Achados da execução

*(preenchido pelos executores)*
