# Cenário do consultor — P-0753

Handover entre acionamentos do consultor deste plano (`pantonic-consultant`). Plano:
`docs/plans/P-0753-auditoria-estagio-1/plano.md`; estado: `estado.tsv` nesta pasta. Tem autoridade
sobre o plano para o que cobre.

## Estado da janela (2026-09-27)

- Marco 1: `go` do dono em 2026-09-27. Marco 2 pendente (`README.md` revisado, entrega, série de
  telemetria com os papéis gravados pelo hook).
- `AF-T1`..`AF-T7` `done` (aprovadas 100%; `AF-T5` depois do `DAF-37`, `AF-T6` do `DAF-38`, `AF-T7` do `DAF-39`);
  `AF-T8` `done` com ressalva 91%, sanada no `DAF-40`; `AF-T9` `done` 100% (`AE-11`, `AE-12`); `AF-T10`
  `done` com ressalva 91% (`AE-13`..`AE-15`), sanada no `DAF-42`; `AF-T11` `done` 100% (`AE-16`); `AF-T12`
  `done` com ressalva 91% (`AE-17`, `AE-18`), sanada no `DAF-43`; `AF-T13` `done` 100% (`AE-19`, sanado no
  `DAF-44`); `AF-T14`..`AF-T16` `done` 100%; `AF-T17` `done` com ressalva 91% (`AE-25`, sanado no `DAF-45`;
  `AE-23`, `AE-24` à auditoria final). Nenhum commit na janela (commit só no marco).
- Modelo: versão 3 vigente (sétimo ato do dono, 2026-09-27), versão 2 obsoleta; `AF-T19` `cancelled`,
  `DAF-46` revoga a `DAF-6` (batedor no Opus com `Bash`), segue pelo card corretivo `AF-T19a`.
- Diretiva do dono no cabeçalho de `docs/DIARIO_DE_OBRAS.md`: nenhum tíquete novo por ajuste; achado
  novo vai a `## 9` do plano como `AE-<n>` com rota "auditoria final".
- Árvore: `telemetria_hook.py` e `tests/test_telemetria_hook.py` já trazem WIP da `TK-88b` (filtro
  restrito a `pantonic-executor`, teste `test_tr_hook_so_executor_consome_estado`) — é a linha de
  base da `AF-T5`, não trabalho parcial dela.

## Decisões vivas deste consultor

- **DAF-37** (acionamento 1, `AF-T5`, `rota=resolve`): o passo 2 da `AF-T5` enumerava dois dos três
  testes que afirmam o apagamento de `tarefa-corrente.json`; entrou o terceiro,
  `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia` — `estado_rh`, `estado_rs`,
  `estado_vs` passam a `is True` (`estado_vh` fica `True`), e dois trechos da docstring mudam (literais
  no passo 2, conferidos: cada um ocorre 1 vez no arquivo). A contingência passou a "fora dos três que
  o passo 2 altera". Varredura feita: nenhum outro teste de `tests/` depende do apagamento
  (`test_progresso_hook.py` usa o estado do painel, não o do gancho; `test_encerrar.py` não cita
  `planejador`/`modelador`/`scout`/`outros`). Impedimento procedente — o executor parou pela
  contingência do card, com razão; não é recusa por improcedência.

- **DAF-38** (acionamento 2, `AF-T6`, `rota=resolve`): a contingência da `AF-T6` nomeava só
  `test_tf_ger_7_agente_de_volta_revisor`; `test_tf_ger_19_userpromptsubmit_sem_volta_pendente` e
  `test_tf_ger_25_show_no_meio_da_janela_nao_encerra` também afirmam a frase `M-7` antiga e entram na
  contingência com o literal `aprovado 100%, bloqueante nenhuma.'` → `..., recomendação não informada.'`
  (2 ocorrências, medido; numa cópia, `43 passed`). `tests/test_encerrar.py:107` traz a frase antiga como
  entrada de fixture e não cai. Trabalho parcial do executor **revertido** à ref `543229b` nos quatro
  alvos (o quarto gate, `card_check` mundo `antes`, o recusava com exit 1); `SKILL.md` do scrum-master
  mantido em CRLF como estava na árvore. Impedimento procedente. Padrão repetido (`DAF-37`, `DAF-38`):
  contingência que enumera testes afetados sem varredura — no próximo card do plano com contingência
  "outro teste cair", conferir a enumeração por `grep` antes do despacho.

- **DAF-39** (acionamento 3, `AF-T7`, `rota=resolve`): a fixture literal do passo 2 (`P-0-pasta/plano.md`)
  não tinha `Arquivos-alvo` nem `Entregável` e `rdo.extrair_dossie` recusava `CP-T1`/`CP-T2`; entrou em
  cada card o bullet `- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.` (forma de
  `plano-exemplo.md`). Ensaiado: produto novo `CP-T1`/`CP-T2` exit 0; código da ref `CP-T1` exit 1 — o TF
  discrimina; `test_card_check.py` inteiro com a troca `20 passed`. As quatro Verificações viraram medidas;
  piso `468` (+2 = `470`). Trabalho parcial **revertido** à ref `2f63d41` (`card_check.py`,
  `test_card_check.py`; `P-0-pasta/` apagada). Impedimento procedente. Terceiro defeito de autoria na
  janela (`DAF-37`..`DAF-39`), todos valor publicado sem ensaio: no próximo acionamento, antes de
  devolver, rodar numa cópia toda Verificação do card que ainda diga "esperado, não ensaiado".

- **DAF-40** (acionamento 4, `AF-T8` já `done`, gatilho 2, `rota=resolve`, regra `A8`): o predicado
  `_plano_em_esboco` (`backlog.py`) omitia a cláusula *plano em pasta* do `Domínio` e silenciava o `C-10`
  do plano legado `blocked` com id = contador. Corrigido no ato pelo consultor (instrumento do loop,
  nenhum card cobre; diretiva veda card novo): exige `plano.estado_arquivo is not None`; TR novo
  `test_tr_check_plano_legado_blocked_no_contador_segue_acusando_c10` (cai sem a cláusula, passa com
  ela). Suíte `473 passed` (piso dos próximos cards). Quarto defeito da mesma família: TR que só
  discrimina uma das cláusulas do `Domínio` — ao reparar card com predicado de várias cláusulas,
  conferir um TR por cláusula.

- **DAF-41** (acionamento 5, `AF-T10`, `rota=resolve`): o passo 2 dava só a `Verificação` de `GAM-T1`;
  `rdo.extrair_dossie` exige também `Pronto quando` e `Arquivos-alvo`/`Entregável`. Ensaiando a cadeia
  numa cópia, apareceu um segundo defeito: `card_check.py:54` carrega `rdo.py` (e este `caminhos.py`)
  de `<root>/.claude/tools/`, ausentes na fixture. O passo 2 agora monta a cópia em quatro tempos
  (fixture; `rdo.py`+`caminhos.py`; `plano.md` com `GAM-T1`/`GAM-T2` literais completos, `GAM-T2` com
  `antes` `z`; `git init`+commit), ensaiado: `modelo` 2, `card_check` 0/1, `pytest --co` 5,
  `--capturar-ref` 0. Piso `475` medido (`478`). Nada a reverter (alvos iguais à ref `9f6bf68`).
  Procedente. `AE-11` não entra (é do `show`, operação da `AF-T9`; diretiva veda card novo). Quinto
  defeito de autoria da janela: o ensaio da Verificação não basta — ensaiar também a **montagem do
  teste** (fixture + instrumentos que o gate carrega por caminho de `--root`) antes de devolver.

- **DAF-42** (acionamento 6, `AF-T10` já `done`, gatilho 2, `rota=resolve`, regra `A8`): os quatro
  `subprocess.run` de `despachar` (`backlog.py`) decodificavam o stderr dos irmãos (UTF-8) pela
  codificação do locale (cp1252): razão com mojibake, ou stderr `None` e traceback. Corrigido no ato
  (`encoding="utf-8", errors="replace"`) e o TR `test_tr_despachar_recusa_no_primeiro_gate_sem_escrever`
  ganhou `"não fecham" in erro` (vermelho medido antes do reparo, verde depois). Suíte `478 passed`
  (piso dos próximos cards). `AE-13` (forma do `--plano`) não é erro — entrega correta; segue auditoria
  final. Sexto defeito da janela: verbo que cruza fronteira de processo precisa de aceite sobre o
  texto que a atravessa — em card que chama irmão por `subprocess`, fixar `encoding` no contrato.

- **DAF-43** (acionamento 7, `AF-T12` já `done`, gatilho 2, `rota=resolve`, regra `A8`): dois defeitos do
  verbo `marco` (`encerrar.py`, `gravar_marco`), que gravará o veredito do Marco 2. (a) a célula se
  reescrevia por `split("|")`, cego ao `\|` que o próprio verbo emite: regravar marco cuja frase tinha
  `|` deixava resto do veredito velho — agora `_MARCO_COLUNA_RE` (`(?<!\\)\|`). (b) Marco 1 `go` com
  transição recusada gravava o plano e só depois saía exit 1 — agora `checar_transicao` (`TK-88d`) roda
  antes da escrita (1); a outra checagem de `transacionar_status` (linha do plano em `estado.tsv`) não
  precisa de prévia, porque plano em pasta só lê `blocked` dessa linha. Um TR por caminho, ambos
  vermelhos medidos antes do reparo. Suíte `484 passed` (piso dos próximos cards). Sem `AF-T12a`
  (diretiva). Sétimo defeito da janela: verbo que grava formato que ele mesmo relê precisa de TR de
  ida e volta (gravar duas vezes), e verbo que delega escrita a instrumento com checagens próprias
  precisa chamar a checagem prévia do instrumento antes da primeira escrita dele.

- **DAF-44** (acionamento 8, `AF-T13` já `done`, gatilho 2, `rota=resolve`, regra `A8`): o `--checar` de
  `encerrar.py operacoes` não acusava seção apagada inteira (a tabela do arco já cita todo ID; `sem os
  quatro blocos` só itera seções existentes). Corrigido no ato: lista `sem_secao` em
  `checar_esqueleto_operacoes` (retorno passa a trio), linha `sem seção: <ids>` entre as duas de hoje,
  exit 0 só com as três `nenhum`; skill `entrega-de-encerramento` item 6 e `--help` atualizados; TR
  `test_tr_esqueleto_de_operacoes_checar_secao_apagada` (vermelho medido antes, verde depois). Suíte
  `488 passed` (piso dos próximos cards). O acionamento 7 deixou o `DAF-43` fora da tabela de decisões do
  plano (só cenário e `AE-17`/`AE-18`): linha apensada agora. Oitavo defeito da janela: conferência de
  cobertura precisa de um TR por forma de ausência (ID sumido, seção sumida, bloco sumido) — citação
  em qualquer lugar não prova seção. E, para este consultor: decisão só existe quando está na tabela
  do plano — conferir a linha `| DAF-<n> |` antes de devolver; em célula de tabela, nada de `|` cru.

- **DAF-45** (acionamento 9, `AF-T17` já `done`, gatilho 2, `rota=resolve`, regra `A8`): o `prevoo.py` partia o
  texto por `str.split()` sem normalizar — citação em crase, com pontuação e `nome()` saíam sem item
  (exit 0), e `--plano;` virava citado com `não`. Corrigido no ato: `_normalizar` (tira crase, aspas, `*`,
  abre/fecha de agrupamento e pontuação de frase nas pontas, sem tocar o `.` inicial de `.claude/`;
  flag perde `=<valor>`) e símbolo = nome antes do primeiro `(`. Três TRs, um por forma de citação,
  vermelhos medidos antes (CLI no repositório) e verdes depois, apensados ao `piso_comportamental.txt`;
  nenhum traz `def <nome>(` literal. Suíte `498 passed` (piso dos próximos cards). Nono defeito da
  janela: instrumento que lê texto do dono precisa de aceite na forma em que o dono escreve (crase,
  pontuação, chamada) — em card que extrai token de prosa, fixar a normalização no contrato.

- **DAF-47** (acionamento 12, `AF-T19a`, `rota=resolve`): a contingência do passo 13 parava se o
  `generate` mudasse qualquer linha de `.claude/README.md` além da do `pantonic-scout`, e contradizia a
  restrição `check-drift` exit 0 — a árvore já trazia `pantonic-consultant`, `pantonic-planner`,
  `modelo-por-fase` fora de sincronia com o frontmatter e duas skills fora do git (`fatos-frescos`,
  `mensagem-ao-dono`, `??`, nenhum card do plano as cria). Nova contingência: só para fora das duas
  regiões geradas ou com `check-drift` ≠ 0. Trabalho do executor **mantido** (passos 1-13 conferidos
  por grep); card `ready` com linha de estado de partida e Verificações medidas (`True True True` ×2,
  `8`, `frontmatter_yaml` 0, `498 passed`, `check-drift` 0); `card_check --mundo depois` exit 0.
  Procedente. Décimo defeito de autoria: contingência sobre saída de gerador escrita sem rodar o
  gerador na árvore — medir o `generate` antes de publicar contingência sobre o diff dele.

## Fila

`AF-T19a` `ready` (redespacho do `DAF-47`: roda as Verificações e fecha); depois a ordem da `## 6` do
plano. Medido no `DAF-47`: `backlog.py check` exit 0, `modelo.py check --plano` exit 0, suíte
`498 passed`, `check-drift` exit 0. Versão 3 do modelo vigente (sétimo ato do dono).

## Achados abertos

- `AE-3` (`AF-T1`, TR que não discrimina a guarda de tocados vazio) — rota auditoria final.
- `AE-4`, `AE-5` (`AF-T5`, fechamento) — rota auditoria final (diretiva do dono).
- `AE-6` (`AF-T6`, reincidência do `AE-4`) — sem ação na janela; rota auditoria final.
- `AE-7` (conflito de `OP-7`) — modelador gravou a v2 pendente; decide o dono no Marco 2.
- `AE-8` (`AF-T7`, Objetivo condicional × leitura incondicional) — auditoria final, junto do `AE-7`.
- `AE-9` (reincidência do `AE-4`) — sem ação.
- `AE-10` fechado no `DAF-40`.
- `AE-11` (`AF-T9`, ponteiro do bloco de achados no `show`), `AE-12` (`AF-T9`, camada do TF de CLI) —
  auditoria final; o `AE-11` avaliado e recusado para a `AF-T10` no `DAF-41`.
- `AE-13` (`AF-T10`, forma do `--plano` não fixada no card) — auditoria final. `AE-14` fechado no `DAF-42`.
  `AE-15` — sem ação (reincidência do `AE-4`).
- `AE-16` (`AF-T11`, item 1 do consultor sem ressalva das leituras dos itens 3 e 5) — auditoria final.
- `AE-17` fechado no `DAF-43`. `AE-18`: conciliação das checagens fechada no `DAF-43`; forma de `<plano>`
  no dossiê, `strip()` e as duas recusas a mais — não é erro, auditoria final.
- `AE-19` fechado no `DAF-44`.
- `AE-23` (`AF-T17`, ordem por categoria), `AE-24` (`AF-T17`, contingência fora dos `Arquivos-alvo`) —
  auditoria final. `AE-25` fechado no `DAF-45`.

## Inconclusivo

- Quando a árvore saiu de sincronia com a região gerada do `.claude/README.md` não se reconstruiu: a
  Fila registrava `check-drift` exit 0 depois do `DAF-45`, e o executor da `AF-T19a` relata drift
  pré-existente. Não muda o `DAF-47` (as linhas ressincronizadas são cópia do frontmatter da árvore);
  as duas skills sem rastreio no git (`fatos-frescos`, `mensagem-ao-dono`) entram no commit do marco só
  por decisão de quem o faz.

- O desfecho do teste `stdin_utf8` sob o produto novo foi deduzido, não ensaiado (o produto da `AF-T5`
  ainda não existe): revertido hostil → transcript não encontrado → silêncio, estado vivo, TSV ausente;
  revertido seguro → linha gravada, estado vivo. O canal de estado deixa de discriminar; a série
  (`tsv_vh is None` contra a linha em `tsv_vs`) carrega a discriminação sozinha. Se o revisor julgar que
  o par negativo enfraqueceu, é ressalva do laudo, não reabertura do `DAF-37`.
