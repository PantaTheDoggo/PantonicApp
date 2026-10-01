# Cenário — P-0755 · Aplicação das recomendações da auditoria final do kit

Handover do consultor entre acionamentos. Tem autoridade sobre o plano no que cobre; o que não
estiver aqui, o próximo acionamento não sabe. Teto: 15k tokens (matéria fechada vai à `## 9` do
plano, com ponteiro).

## 1. Estado do plano

- Plano `ready`; Marcos 1 a 4 go do dono (Marco 4: "Aceitar", v3 vigente). Etapas A, B e C
  fechadas. Etapa D aberta: `RAF-T27`, `RAF-T27a`, `RAF-T28`, `RAF-T29`, `RAF-T29a`, `RAF-T30`
  (passou por `blocked`, `DRF-68`), `RAF-T30a`, `RAF-T31`, `RAF-T31a`, `RAF-T31b` `done`; `RAF-T32`
  (passou por `blocked`, `DRF-71`), `RAF-T32a`, `RAF-T33`..`RAF-T35` `done`: etapa D fechada, Marco 5
  go (2026-09-30). Etapa E: `RAF-T36`..`RAF-T39` e `RAF-T22a` `done`; `RAF-T39a` (`DRF-75`) `ready`,
  `next`; `RAF-T40` depende dele e é a última; Marco 6 pendente.
- Modelo: versão 4 **vigente** (aceita no Marco 5; `modelo.py check` diz `versão 4`, 64 tarefas).
- Branch `plan/planner-modelo-escopo`, WIP não commitado de `P-0754`, roteiro e sonda na árvore.

## 2. Decisões vivas do consultor

- Fechadas, texto na §3 do plano (movidas no acionamento 25): `DRF-43`, `DRF-45`, `DRF-46`, `DRF-47`, `DRF-49`, `DRF-50`, `DRF-51`, `DRF-52`, `DRF-53`, `DRF-54`, `DRF-55`, `DRF-57`, `DRF-58`, `DRF-59`, `DRF-60`, `DRF-61`, `DRF-62`, `DRF-64`, `DRF-65`, `DRF-66`, `DRF-67`.
- **`DRF-44`** (acionamento 1, `AE-121`) — o vermelho do `dead_code.py` sobre
  `docs/audits/sonda-2026-09-28/passos.py:13` (`passo`, sem chamador) não ganha card nem tíquete:
  §7 mantém a sonda como registro, §8 item 5 prevê o gate vermelho, e a restrição dos cards de
  código já admite esse achado nominalmente. O revisor reconcilia pela linha do card.
- **`DRF-48`** (acionamento 5, `AE-132`/`AE-133`) — permissão negada sobre arquivo-alvo não se
  contorna por outra ferramenta nem canal: o executor faz o resto do card, sinaliza `blocked`
  razão `ferramenta` com caminho e texto exato da edição negada; quem conduz junta as negadas num
  comando PowerShell único ao dono no fim da sessão. §4 invariante 13 do plano + contingência
  inline em `RAF-T7`..`RAF-T40` (34 cards). A emenda da `GOVERNANCA.md` §7 fica com rota
  auditoria final (diretiva do §3). Sem drift. Triagem futura: card `blocked` por permissão negada
  é `rota=resolve` — a edição negada vai ao comando único e o card volta a `ready` depois que o
  dono o roda; não é improcedente nem estratégico.
- **`DRF-56`** (acionamento 12, `AE-158`) — §4 invariante 14: nenhum `git` que escreve (`stash`,
  `reset`, `checkout`, `restore`, `clean`, `add`, `commit`) roda na árvore na execução; prova do
  `antes` pela ordem dos Passos ou cópia fora do repo. Restrição de escopo dos 27 cards abertos
  (`RAF-T14`..`RAF-T40`) e da `RAF-T13a` nomeia a regra. Guarda mecânica (hook `PreToolUse`):
  rota auditoria final (diretiva do §3). Sem drift.
- **`DRF-63`** (acionamento 18, `AE-178`) — o card da operação nova que a rodada registra `blocked`
  (nota `aguarda o aceite da versão <k> no marco`, `DRF-14`) ganha destino na doutrina de quem
  conduz, no trecho da `scrum-master` que a `RAF-T24` escreveu: aceite → `ready` por `backlog.py
  status`; recusa → o consultor o tira do plano com a linha do `estado.tsv` (`cancelled` não basta:
  o `V4` do `validar` não olha status, lido). Card `RAF-T24a` (`OP-24`; `tarefas:` §1 e §1A; §6 C e
  D); `RAF-T27` depende dele. Mecanizar no `encerrar.py marco` mudaria o estado final de
  `fechamento.promoção da versão aceita` (drift): não seguido. O gate de etapa à mão (`RAF-T7`,
  `RAF-T19`) é a `DRF-5` como escrita, não defeito. Sem drift. Triagem futura: na recusa de versão
  com card desses, este consultor tira o card e a linha dele.
- **`DRF-68`** (acionamento 23, `RAF-T30` `blocked` premissa, `AE-186`) — o `B1` segue chaveado no alvo
  `instrumento`, que vira o quinto alvo de achado de processo: `rdo.py` (`_ALVOS_ACHADO`, docstrings,
  `help`), `RUBRICA_DE_REVISAO.md` §6 e `pantonic-reviewer.md`, pelo card `RAF-T30a` (`OP-30`;
  `tarefas:` §1; §6 D); `RAF-T34` depende dele. Chavear num dos quatro alvos não: nenhum denuncia
  instrumento, e o TR da `RAF-T30` manda termo de falha em outro alvo calar. **Drift** (rubrica ganha
  propriedade): rota `modelador`, v4 pendente; recusada, o corretivo que tira o quinto alvo e a nova
  chave do `B1` voltam a este consultor. A asserção deslocada volta no redespacho da `RAF-T30` (Passo
  0, Verificação 3; V1/V2 com `antes` `exit 0`, o mundo do redespacho); consome a retentativa. Item 3
  do `AE-186` → §5 (rota auditoria final). Autoria futura: instrumento que lê a saída de outro prova o
  caminho com a saída real do produtor; card que acrescenta ao fim de teste nomeia a última linha.
- **`DRF-69`** (acionamento 24, `AE-190`) — a `DFP-8` do `P-0752` não se aposenta nem se estende a
  `gravar_por_agente`: fica no escritor sem agente (`append_row` e a pré-checagem do `encerrar.py
  tarefa`); no escritor por agente a rodada é a linha do agente, que a nova troca (idempotente), e
  estender a recusa descartaria a linha de outro agente com os mesmos números. Hook → fechamento
  segue coberto (`ultima_linha_da_tarefa` lê pelo cabeçalho). O erro é de texto: docstrings de
  `checar_repetida`, `append_row`, `gravar_por_agente` e do módulo (`só apende`, CLI sem
  `--agente`). Card `RAF-T31a` (`OP-31`, redação; `tarefas:` §1 e §1A; §6 D; fecha a etapa D).
  `RAF-T31` fica como executada. Sem drift. `AE-189` reincide a `DRF-44`. Autoria futura: a da
  `DRF-55`, que reincidiu (card que muda o caminho de escrita varre os docstrings que o afirmam).
- **`DRF-70`** (acionamento 25, `AE-191`) — a frase do primeiro parágrafo do docstring de
  `telemetria.py` (linhas 5-6, "só ganha uma linha no final") ganha a ressalva "sem `--agente`", e
  o `help` do `append` (linha 271) ganha "com --agente, troca a do mesmo agente" (achado na
  varredura do consultor, fora do laudo). `append_row` (diz só dele, verdade) e a `description`
  (nome do verbo) ficam. Card `RAF-T31b` (`OP-31`, redação; `tarefas:` §1 e §1A; §6 D; fecha a
  etapa D no lugar da `RAF-T31a`). `RAF-T31a` fica como executada. Sem drift. Defeito de autoria
  do próprio consultor no acionamento 24: a `DRF-69` varreu os parágrafos que o laudo nomeou, não
  o arquivo.
- **`DRF-71`** (acionamento 26, `RAF-T32` `blocked` premissa) — o card nomeava `processar` em
  `progresso_hook.py`, que não a define; os ramos `Agent` vivem em `evento` (linhas 334-497). Card
  trocado para `evento`, com as atribuições `tarefa_corrente` das linhas 447 e 471 nomeadas (a da
  486 é do `UserPromptSubmit`, excluído no `Não fazer`); `ready`, `card_check --mundo antes` OK,
  `next` = `RAF-T32`. Procedente, sem drift. Autoria futura: função citada se mede por `grep` no
  arquivo-alvo.
- **`DRF-72`** (acionamento 27, `AE-193`) — o retorno por hand-back (`PostToolUse` `handback` `send` →
  `UserPromptSubmit` `<agent-message>`) seguia com `tarefa_corrente`: corretivo `RAF-T32a` (`OP-32`;
  `tarefas:` §1 e §1A; §6 D; fecha a etapa D) grava o título despachado em `titulos_pendentes[agentId]`
  (chave nova; `pendentes` segue string) e testa o `PostToolUse` síncrono. ID sem card mostrando o ID
  não é defeito (cair na corrente nomearia tarefa não despachada). `AE-192` reincide a `DRF-44`. Sem
  drift. Autoria futura: card que troca a fonte de frase do painel cobre todo ramo que a emite; o
  `Não fazer` da `RAF-T32` (reforçado pela `DRF-71`) excluiu o ramo sem medir o que ele emite.
- **`DRF-73`** (acionamento 28, Marco 5, `AE-187`) — `_diff_fluxo` compara o par só pelo texto (o card
  da `RAF-T22` mandava "nenhuma linha" para mesmo texto e número): operação que muda `precisa de:`/`altera:`
  sai do drift, contra o estado final de `OP-22` ("mostra operação [...] alterada"). Corretivo `RAF-T22a`
  (`OP-22`; `tarefas:` §1 e §1A; §6 E, depende do gate `RAF-T36`; `RAF-T40` depende dele): linhas
  `[~] OP-<k> — precisa de: …` e `… altera: …`; `tarefas:` fora. Não bloqueia o Marco 5 (mensagem leva a
  `OP-30` à mão). Sem drift. Se a v4 for recusada, a `RAF-T22a` segue igual (não depende da v4).
- **`DRF-74`** (acionamento 28) — v4 validada; linha do `--consultor` verbatim na §3 do plano. `DRF-65`
  faltava na §3 (o cenário a dava por escrita): restaurada no mesmo acionamento.
- **`DRF-75`** (acionamento 29, `AE-204`) — a subseção `### Quando a janela para num marco` (`RAF-T39`)
  mandava a célula *o que o dono lê* inteira, contra o próprio exemplo (trecho antes dos dois-pontos) e
  com a célula do Marco 1 sendo um comando; o primeiro parágrafo do `## Relatório de encerramento` seguia
  dizendo que o relatório abre com o `show`. Entrega = nome da etapa (trecho antes dos dois-pontos); célula
  sem etapa ou plano sem tabela: título do plano. Remissão no primeiro parágrafo sem o nome literal da
  subseção (a V1 da `RAF-T39` conta `marco=1`). Corretivo `RAF-T39a` (`OP-39`; `tarefas:` §1; §6 E);
  `RAF-T40` depende dele; `DRF-41` aponta a `DRF-75`. A rota do laudo (a `RAF-T40` ou o Marco 6 fixarem)
  foi recusada: erro inequívoco não se adia, e o dono não valida questão técnica. Sem drift. `AE-203`
  reincide a `DRF-44`. Autoria futura: exemplo de card confere com a regra que ele ilustra, e subseção
  que abre exceção remete no parágrafo que afirma a regra geral.
- Lições de autoria dos corretivos (texto integral nas linhas `DRF-` da §3 do plano): card que
  troca mecanismo ou comportamento de instrumento varre o arquivo inteiro pelas frases que afirmam
  o antigo — docstring do módulo e das funções, `help` do `argparse`, docstrings dos testes-alvo,
  frase que conta vocabulário fechado (`DRF-51`, `DRF-55`, `DRF-66`, `DRF-67`, `DRF-69`, `DRF-70`;
  reincidiu cinco vezes); correção de leitura do `git` varre todas as chamadas do arquivo
  (`DRF-52`); filtro de alvos reusa a expansão existente (`DRF-53`); critério de juízo confere a
  fonte da dimensão e cita doutrina por seção (`DRF-54`); teste ditado fixa antes, esperado e
  depois (`DRF-55`); TR que o Passo manda passar antes só confere saída que já existe (`DRF-57`);
  guarda condicional vem com o caso que a dispara (`DRF-59`); acréscimo ao `modelo.py` ensaia
  `test_modelo.py` inteiro (`DRF-61`); leitura nova de seção segue a regra das checagens do verbo
  (`DRF-62`); doutrina que descreve saída de instrumento confere cada frase contra o código (`DRF-64`).

## 3. Regras vigentes que pesam na triagem

- Diretiva do dono de 2026-09-26 (linha 2 do diário, "vigente até o fechamento da auditoria
  final"), item (2): nenhum card nem tíquete novo por ajuste; achado novo vira `AE-<n>` com rota
  "auditoria final". Leitura adotada: vale fora do plano (tíquete); o corretivo `T<n>a` de defeito
  que o próprio plano entregou é reparo do plano aprovado, não ajuste de backlog.
- Ato do dono de 2026-09-29, verbatim: "para todo comando que exija permissão e você fique
  bloqueado, monte um comando powershell para eu escreve tudo de uma vez. Não me dê pedaço por
  pedaço. O que você conseguir editar, edite. O que não conseguir, junte tudo em me passe no final
  o comando powershell que eu escrevo aqui no meu terminal". O dono aceitou a edição por `Edit` da
  `RAF-T6a`. A condução o pôs na fila de memória do dono
  (`permissao-negada-vira-comando-powershell-unico`).

## 4. Achados abertos

- Nenhum aberto. `AE-191` → `DRF-70`/`RAF-T31b`; `AE-193` → `DRF-72`/`RAF-T32a`; `AE-192` reincide a `DRF-44`; `AE-187` → `DRF-73`/`RAF-T22a`; `AE-204` → `DRF-75`/`RAF-T39a`; `AE-195`, `AE-197`, `AE-201`..`AE-203` reincidem a `DRF-44`. As absorções até o acionamento 24 estão na §9 do
  plano (bloco *Medidas fechadas do cenário*); reincidência da `DRF-44` segue sem ação nova.

## 5. Matéria inconclusiva

- Escopo do `dead_code.py`: se `.py` sob `docs/` (ou script sem guarda `__main__`) entra na
  varredura "de produção". Não fechado aqui; rota "auditoria final" pela diretiva de 2026-09-26.
  Quando a sonda for versionada com o `P-0754`, o hub fica com `dead_code` vermelho permanente —
  levar ao relatório de encerramento se a diretiva cair antes do fim do plano.
- Se a diretiva de 2026-09-26 ainda vale (o `P-0754` não fechou). Adotada a leitura do §3.

- Linhas de âncora achadas que não são ponto de edição (a primeira linha que contém um trecho
  qualquer) seguem no pacote: 501 linhas nos 41 cards. Fora do `AE-125`; não fechado.
- Pipe ou redirecionamento dentro de aspas (`echo "a|b"` num comando com pytest) segue recusado
  pelo hook: fora do `AE-130`; não fechado.
- Residência do ato do dono de 2026-09-29 no kit: guardrail da `GOVERNANCA.md` §7 para o
  executor (`AE-133`) e, para quem conduz, regra global ou memória (fila do dono). Rota auditoria
  final; levar ao relatório de encerramento se a diretiva de 2026-09-26 cair antes do fim do plano.
- `modelo.py check --plano` resume `versão 1` com a v2 pendente válida: o resumo nomeia a
  vigente; se deve citar a pendente não está fixado em card nenhum (ver `DRF-37`/`DRF-38`, tarefas
  de versão do modelo). Não fechado; não é erro inequívoco.
- `modelo.py show --drift` lista só o estado final (`_diff_estado` compara só o final): a mudança
  do estado inicial da v2 não aparece nele. A mensagem de marco ao dono carrega as duas colunas.
  Se o drift deve mostrar o inicial: não fixado em card; não é erro inequívoco (desenho do verbo).
- Guarda mecânica contra `git` que escreve na árvore durante a execução (`AE-158`, `DRF-56`): rota
  auditoria final; levar ao relatório de encerramento se a diretiva de 2026-09-26 cair antes.
- `AE-154` pede linha de base admitida no dossiê (ou recorte de `docs/audits/` no `dead_code`):
  mesma matéria do escopo do `dead_code` acima; toda tarefa sai `guardas parcial` e aciona o
  consultor enquanto a sonda viver na árvore. Não fechado; `DRF-44` segue.
- Quais caminhos o auto mode nega (medido só o hook `.claude/global/hooks/` por `python -c` via
  Bash; `Edit` passou com aceite do dono; skills e ferramentas de `.claude/` passaram na etapa A).
- `AE-162`: a checagem do vermelho do TDD (prova do `antes` da `DRF-56`) não deixa rastro
  mecânico; o dossiê só admite a medida verde, e o salto do Passo 2 na `RAF-T14` só se soube por
  relato do executor. Lacuna de doutrina e de instrumento (medida do mundo vermelho gravada e
  colada no `review_evidence.py`, ou o passo sai dos cards); rota auditoria final, levar ao
  relatório de encerramento se a diretiva de 2026-09-26 cair antes do fim do plano.
- Citação livre do contrato de objeto em `Camada e fronteira` ("O contrato do objeto é: …"): a
  promoção (`DRF-38` (d)) reescreve só o `Operação do modelo`; card aberto no marco que cite o
  contrato mudado fica com o texto antigo. Hoje nenhum (`RAF-T21`/`T22` executam antes do Marco
  4). Não fechado; não é erro inequívoco.

- `AE-186` item 3: a seção *Linhas removidas dos testes* do `review_evidence.py` é textual e não vê
  asserção que migra de uma função de teste para outra (o laudo pede comparação por função via `ast`
  e emenda à rubrica §4). Não é erro inequívoco (a seção diz o que mede); rota auditoria final, levar
  ao relatório de encerramento se a diretiva de 2026-09-26 cair antes do fim do plano.

- Saída de `blocked` pelo próprio `encerrar.py marco` (card `aguarda o aceite da versão <k>` no
  aceite, primeira tarefa da etapa no `go`, `DRF-5`): hoje à mão por quem conduz (`DRF-63`); a
  mecanização muda o modelo (`fechamento`), rota auditoria final; levar ao relatório de
  encerramento se a diretiva de 2026-09-26 cair antes do fim do plano.

## 6. Medidas deste cenário

- Medidas dos corretivos fechados (`RAF-T1a`..`RAF-T29a`, Marco 3, `DRF-61`): §9 do plano, bloco *Medidas fechadas do cenário*.
- O `card_check` do despacho confere `` `<caminho>.<ext>:<n>` `` em `Arquivos-alvo`/`Passos`
  (literal logo depois, na faixa): âncora com linha em fixture de teste vai em
  `Contratos/classes`, e card do consultor não põe `caminho:n` de arquivo inexistente em `Passos`.
- Armadilha do consultor: heredoc do Bash colapsa a barra invertida dupla em simples — script Python com literal de
  código-fonte usa string crua (`r'''...'''`). Armadilha anterior: escrever `\n` literal no card via heredoc Python gera quebra real, e o
  `rdo.py` corta o campo na linha que começa por `- **`. Conferir com `card_check` após gravar.
  Nova (acionamento 3): o comando Bash foi truncado no literal `'### RAF-T5 — '` dentro de heredoc
  (script cortado, nada gravado); a cauda do script foi escrita com `Write` e o marcador montado
  com `'—'`.
- A `scrum-master` está `i/lf w/crlf` com `.gitattributes` `eol=lf` (medido 2026-09-28): alguma
  tarefa da etapa A a regravou em CRLF; o `RAF-T4a` a devolve a LF. Card futuro que edite skill
  mede `cr=` antes e depois.
- Bash do consultor: comando com `pytest` passa pelo hook projetado; terminar com `#nofilter`.
- Fim de linha (2026-09-29): mais de cem arquivos rastreados `i/lf w/crlf` contra `eol=lf`
  (`review_evidence.py`, `test_review_evidence.py`, `modelo.py`, `prevoo.py` entre eles); o git
  normaliza no `add`. Não é defeito do P-0755; card que regrave arquivo inteiro deixa LF.
- `DRF-68` ensaiada em cópia (`%TEMP%` pasta `raf_t30a`; `ensaio.py` fases `copiar`, `teste`,
  `aplica`, `t30`; `verif.sh`, `card.md`, `drf68.txt`, `aplica_plano.py`): real `-k alvo_instrumento`
  `exit 5`; com o TF e sem a regra `1 failed`; depois `1 passed`; V2 `alvos=3-0-0 rdo=0-0-0` →
  `alvos=0-1-1 rdo=1-1-1`; três suítes na cópia (base × depois) com as mesmas 34 falhas de
  infraestrutura e um `passed` a mais; real `127 passed`. Os quatro alvos são LF (0 CR). A asserção
  `"linha nova do registro" not in saida` aparece duas vezes no arquivo (linhas 1189 e 1320): V3
  `marco=1 total=2` → `marco=2 total=2`. Depois de gravar: `card_check --mundo antes` OK em `RAF-T30`,
  `RAF-T30a`, `RAF-T34`; `backlog.py check` OK; `modelo.py check --plano` e `--so-vigente` OK (59
  tarefas, versão 3); `check-drift` 0; `backlog.py status RAF-T30 ready` gravou; `next` = `RAF-T30`.
- `DRF-69` ensaiada em cópia (`%TEMP%` pasta `raf_t31a`; `ensaio.py` fases `copiar` e `aplica`,
  `card.md`, `aplica_plano.py`): `telemetria.py` LF (0 CR); V1 real `docstring=1-1-1-0-0 linhas=305`,
  cópia `docstring=0-0-0-3-1 linhas=314`; linhas novas até 99 (as de 101 e 100 são anteriores),
  compila; `test_telemetria.py` + `test_telemetria_hook.py` `33 passed` na cópia. Depois de gravar:
  `card_check --mundo antes` OK em `RAF-T31a`; `backlog.py check` OK; `modelo.py check --plano` e
  `--so-vigente` OK (60 tarefas, versão 3); `check-drift` 0; `next` = `RAF-T31a`. Linha do
  `estado.tsv` inserida depois da `RAF-T31`.
- Armadilhas dos ensaios (colhidas das medidas movidas): a linha do `estado.tsv` do corretivo se
  apensa à mão (`backlog.py status` recusa id sem linha); `card_check` exige `--plano`/`--tarefa`
  nomeados e só lê `antes`/`depois` como `` `exit <n>` `` logo depois da palavra; `#nofilter`
  comenta o resto da linha no Bash (vai no fim); Verificação sem crase no `python -c` (PowerShell
  toma a crase por escape); `Path.write_text` no Windows grava CRLF (ler e gravar por bytes);
  cópia para `test_doutrina_unidade.py` precisa de `GOVERNANCA.md` e `README.md`; suítes vizinhas
  na cópia têm dezenas de falhas de infraestrutura (comparar base × depois).
- `DRF-70` ensaiada em cópia (`%TEMP%` pasta `raf_t31b`; `ensaio.py` fases `copiar` e `aplica`,
  `card.md`, `drf70.txt`, `aplica_plano.py`): V1 real `texto=1-0-0-0 linhas=314`, cópia
  `texto=0-1-1-1 linhas=317`; compila; `--help` mostra o texto novo; `test_telemetria.py` +
  `test_telemetria_hook.py` `33 passed` na cópia; `telemetria.py` LF (0 CR).
- `DRF-72` ensaiada em cópia (`%TEMP%` pasta `raf_t32a`; `testes_novos.py`, `aplica.py`, `card.md`,
  `drf72.txt`, `aplica_plano.py`): `-k retorno_do_despacho` real `exit 5`; com os testes `1 failed, 1
  passed`; depois `2 passed`; arquivo real `47 passed`, cópia `48 passed` + `test_tf_ger_18_residencia`
  (infraestrutura: lê a skill). Depois de gravar: `card_check --mundo antes` OK; `backlog.py check` OK;
  `modelo.py check --plano` e `--so-vigente` OK (62 tarefas, versão 3); `check-drift` 0; `next` = `RAF-T32a`.
- `DRF-73` ensaiada em cópia (`%TEMP%` pasta `raf_t22a`; `ensaio.py` fases `copiar`, `teste`, `aplica`;
  `testes_novos.py`, `card.md`, `aplica_plano.py`, `aplica_drf.py`): real `-k drift_contrato_da_operacao`
  `exit 5`; com os testes `1 failed, 1 passed`; depois `2 passed`; `test_modelo.py` real `46 passed`, cópia
  `48 passed`; `show --drift` do plano na cópia ganha `## Fluxo` com as duas linhas da `OP-30`. `modelo.py`
  é CRLF, `test_modelo.py` LF. Depois de gravar: `card_check --mundo antes` OK em `RAF-T22a` e `RAF-T40`;
  `backlog.py check` OK; `modelo.py check --plano` e `--so-vigente` OK (63 tarefas, versão 3);
  `check-drift` 0; `next` = nada delegável (gate `RAF-T36` `blocked`).
- `DRF-75` ensaiada em cópia (`%TEMP%` pasta `raf_t39a`; `ensaio.py`, `card.md`, `aplica_plano.py`): V1
  real `marco=1-0-0-1`, cópia `marco=1-1-1-0`; skill LF (0 CR). Depois de gravar: `card_check --mundo antes`
  OK em `RAF-T39a` e `RAF-T40`; `backlog.py check` OK; `modelo.py check --plano` e `--so-vigente` OK (64
  tarefas, versão 4); `check-drift` 0; `next` = `RAF-T39a`. Linha do `estado.tsv` inserida depois da `RAF-T39`.

## 7. Acionamentos

| # | data | card | gatilho | rota | decisão |
|---|---|---|---|---|---|
| 1 | 2026-09-28 | `RAF-T1` | 2 (laudo ressalva 88) | resolve | `DRF-43` (`RAF-T1a`), `DRF-44` |
| 2 | 2026-09-28 | `RAF-T3` | 2 (laudo ressalva 91) | resolve | `DRF-45` (`RAF-T3a`) |
| 3 | 2026-09-28 | `RAF-T4` | 2 (laudo ressalva 88) | resolve | `DRF-46` (`RAF-T4a`) |
| 4 | 2026-09-29 | `RAF-T6` | 2 (laudo ressalva 91) | resolve | `DRF-47` (`RAF-T6a`) |
| 5 | 2026-09-29 | `RAF-T6a` | 2 (laudo ressalva 91) | resolve | `DRF-48` (invariante 13) |
| 6 | 2026-09-29 | `RAF-T7` | 2 (laudo ressalva 91) | resolve | `DRF-49` (`RAF-T7a`) |
| 7 | 2026-09-29 | `RAF-T8` | 2 (laudo ressalva 91) | resolve | `DRF-50` (`RAF-T8a`) |
| 8 | 2026-09-29 | `RAF-T9` | 2 (laudo ressalva 91) | resolve | `DRF-51` (`RAF-T9a`) |
| 9 | 2026-09-29 | `RAF-T10` | 2 (laudo ressalva 91) | resolve | `DRF-52` (`RAF-T10a`) |
| 10 | 2026-09-29 | `RAF-T11` | 2 (laudo ressalva 91) | resolve | `DRF-53` (`RAF-T11a`) |
| 11 | 2026-09-29 | `RAF-T12` | 2 (laudo ressalva 88) | resolve | `DRF-54` (`RAF-T12a`) |
| 12 | 2026-09-29 | `RAF-T13` | 2 (laudo ressalva 91) | resolve | `DRF-55` (`RAF-T13a`), `DRF-56` (invariante 14) |
| 13 | 2026-09-29 | `RAF-T14` | 2 (laudo ressalva 91) | resolve | `DRF-57` (sem card) |
| 14 | 2026-09-29 | `RAF-T18` | 4 (Marco 3, validar v2) | resolve | `DRF-58` (v2 validada) |
| 15 | 2026-09-29 | `RAF-T19` | 2 (laudo ressalva 91) | resolve | `DRF-59` (`RAF-T19a`), `DRF-60` (v3 validada) |
| 16 | 2026-09-29 | `RAF-T21` | 1 (`blocked` premissa) | resolve | `DRF-61` (card reescrito, `ready`) |
| 17 | 2026-09-29 | `RAF-T23` | 2 (laudo ressalva 91) | resolve | `DRF-62` (`RAF-T23a`) |
| 18 | 2026-09-29 | `RAF-T25` | 2 (laudo ressalva 90) | resolve | `DRF-63` (`RAF-T24a`) |
| 19 | 2026-09-29 | `RAF-T26` | 2 (laudo ressalva 90) | resolve | `DRF-64` (`RAF-T23b`, `RAF-T26a`) |
| 20 | 2026-09-29 | `RAF-T19` | 4 (Marco 4, linha da v3) | resolve | `DRF-65` (v3 validada) |
| 21 | 2026-09-29 | `RAF-T27` | 2 (laudo ressalva 91) | resolve | `DRF-66` (`RAF-T27a`) |
| 22 | 2026-09-29 | `RAF-T29` | 2 (laudo ressalva 91) | resolve | `DRF-67` (`RAF-T29a`) |
| 23 | 2026-09-29 | `RAF-T30` | 1 (`blocked` premissa, laudo reprovado 74) | modelador | `DRF-68` (`RAF-T30a`, redespacho da `RAF-T30`, v4 pendente) |
| 24 | 2026-09-29 | `RAF-T31` | 2 (laudo ressalva 91) | resolve | `DRF-69` (`RAF-T31a`) |
| 25 | 2026-09-29 | `RAF-T31a` | 2 (laudo ressalva 91) | resolve | `DRF-70` (`RAF-T31b`); cenário compactado (matéria fechada → §9 do plano) |
| 26 | 2026-09-29 | `RAF-T32` | 1 (`blocked` premissa) | resolve | `DRF-71` (card reescrito, `ready`) |
| 27 | 2026-09-29 | `RAF-T32` | 2 (laudo ressalva 91) | resolve | `DRF-72` (`RAF-T32a`) |
| 28 | 2026-09-30 | `RAF-T30` | 4 (Marco 5, validar v4; `AE-187`) | resolve | `DRF-74` (v4 validada), `DRF-73` (`RAF-T22a`), `DRF-65` restaurada |
| 29 | 2026-09-30 | `RAF-T39` | 2 (laudo ressalva 88, `AE-204`) | resolve | `DRF-75` (`RAF-T39a`) |
