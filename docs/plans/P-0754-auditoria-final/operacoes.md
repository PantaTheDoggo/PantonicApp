# Operações — Auditoria final do kit: os herdados e o relatório de auditoria nova

Estado descrito: árvore de trabalho de 2026-09-28, branch `plan/planner-modelo-escopo`, HEAD `2513964`,
com as mudanças do plano ainda não commitadas. Todo número abaixo vem de comando rodado na redação
deste documento ou de registro citado com caminho.

## Abertura

**O problema:** vinte e um achados de planos e tíquetes anteriores estavam parados com a rota
"auditoria final" — a regra do diário em vigor proíbe abrir card ou tíquete por ajuste, e manda
todo achado novo para essa rota (`docs/DIARIO_DE_OBRAS.md:2`). O inventário mora na §2.1 do plano
(`docs/plans/P-0754-auditoria-final/plano.md:201-223`, linhas `H-1` a `H-21`) e se divide assim:

| grupo | herdados | quantos |
|---|---|---|
| defeito no gerador de evidência do revisor | `H-10`, `H-12`, `H-13`, `H-18`, `H-19`, `H-20` | 6 |
| defeito no painel de progresso e na frase final do fechamento | `H-14`, `H-15` | 2 |
| lacuna nas regras do agente planejador e na rubrica | `H-1` a `H-5`, `H-8`, `H-9` | 7 |
| conferidos, não pedem mudança no kit | `H-6`, `H-7`, `H-11`, `H-17` | 4 |
| matéria de avaliação, sem remédio conhecido | `H-16`, `H-21` | 2 |

Além deles, a última auditoria do kit (`docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md`)
media o kit antes de qualquer um desses itens fechar.

**A solução, em uma frase:** cada herdado vira código com teste, regra escrita na definição do
agente que a aplica, ou encerramento com a prova registrada na linha de origem; e uma auditoria
nova, feita executando de ponta a ponta um plano descartável contra o kit já corrigido, mede o
resultado e entrega 31 recomendações a um plano seguinte.

| termo | o que é |
|---|---|
| herdado (`H-<n>`) | achado de plano ou tíquete anterior deixado para a auditoria final; os 21 estão na §2.1 do plano, um por linha. Tíquete (`TK-<n>`) é tarefa avulsa, fora de plano, registrada no diário de obras (`docs/DIARIO_DE_OBRAS.md`, o quadro central de planos e tarefas do projeto) |
| fato `F-<n>`, decisão `DAU-<n>`, marco | linhas do próprio plano: a §2 lista os fatos medidos antes de escrever os cards, cada um com o comando que o mede; a §3, as decisões. Marco é o ponto em que o trabalho para até o dono dar o go — três neste plano (`plano.md:15-19`): o 1 aprova o modelo e as decisões, o 2 abre a auditoria nova, o 3 é o veredito final |
| card | a tarefa do plano (`AUF-T<n>`): objetivo, arquivos que ela pode alterar (campo **Arquivos-alvo**), passos, restrições, contingências e verificações numeradas, cada uma um comando com a saída esperada. O loop de execução — a skill `scrum-master`, conduzida pela **sessão principal** (a conversa do dono com o Claude Code, única que aciona outros agentes) — despacha o card a um agente executor e depois a um agente revisor, que grava um laudo com veredito (`aprovado` ou `ressalva`) e nota em %; o fechamento grava o RDO, o registro da tarefa. Os outros papéis: planejador (escreve os cards), modelador (escreve o modelo de domínio, a §1 do plano), batedor (leitura e busca baratas) e consultor (triagem de parada e de ressalva) |
| contingência | campo do card na forma "se acontecer X → faça Y"; a ação `seguir com <X>` continua a tarefa, a de parada devolve `blocked` |
| evidência | o documento que `.claude/tools/review_evidence.py` monta para o revisor julgar uma tarefa: os arquivos que mudaram, o trecho de diferença de cada arquivo-alvo e a atribuição de cada arquivo |
| recorte (`<ref>`) | commit solto, fora de qualquer branch, que `review_evidence.py --capturar-ref` grava no despacho da tarefa com a árvore de trabalho inteira; **tocado** é o arquivo que mudou desde ele |
| registro da condução | arquivo que quem conduz o loop escreve por ofício — diário, telemetria, planos, RDO, auditorias —, lista `_REGISTRO_ORQUESTRACAO` em `review_evidence.py:432-439`; não pesa no julgamento de escopo da tarefa |
| achado `AE-<n>` | defeito registrado em `## 9. Achados da execução` do plano (`plano.md:1046`) |
| plano fictício | plano descartável que a auditoria executa ponta a ponta para exercitar o kit, com cards `SA-T<n>`. O relatório o chama `P-0755` (pasta `docs/plans/P-0755-sonda-auditoria-final/`, removida); o id `P-0755` voltou a ser o próximo livre (`docs/plans/_INBOX.md:5`) e é o do plano sucessor, em autoria (`P-0755-recomendacoes-auditoria-final`) — são dois objetos distintos |
| cláusula `K-<nn>`, registro `<n>`, recomendação `R-<nn>` | as três listas do relatório da auditoria nova, `docs/audits/AUDITORIA_FINAL_KIT.md`: cláusula é um mecanismo testável do kit, com residência e teste (§2); registro é uma medição feita no plano fictício, numerada e avaliada `adequado`, `inadequado` ou `oportunidade` (§3); recomendação é a ação proposta ao plano seguinte (§5) |

## O arco

| estrato | pergunta que responde | tarefas |
|---|---|---|
| 1. A evidência do revisor | o revisor vê o que a entrega mudou, e só isso? | `AUF-T1`, `AUF-T2`, `AUF-T3`, `AUF-T4`, `AUF-T5`, `AUF-T6` |
| 2. O que quem conduz lê | o painel e a frase final dizem o que aconteceu sem decifrar? | `AUF-T7`, `AUF-T8` |
| 3. O card que sai do planejador | o card sai fechado nos pontos em que já falhou, e a rubrica cobra isso? | `AUF-T9`, `AUF-T10`, `AUF-T11`, `AUF-T12`, `AUF-T13` |
| 4. O fecho dos herdados | o que não pede mudança está encerrado com prova, e o guia de entrada descreve o kit resultante? | `AUF-T14`, `AUF-T15` |
| 5. A auditoria nova | como o kit se comporta de ponta a ponta com tudo isso, e o que ainda falta? | `AUF-T16` |

Os estratos 1 a 3 são independentes entre si. O 4 depende dos três: o guia de entrada descreve o que
eles mudaram. O 5 depende de todos: auditado antes, o kit mostraria defeitos que o plano já corrige
(decisão `DAU-2`). Dentro do estrato 1 as tarefas correm em série porque todas editam
`tests/test_review_evidence.py`; no 3, a rubrica (`AUF-T10`) cobra a regra que a `AUF-T9` escreve.

Contagem, por comando: `awk -F'\t' '$2=="tarefa"{print $3}' docs/plans/P-0754-auditoria-final/estado.tsv | sort | uniq -c`
→ `16 done`; `grep -c "^### AUF-T" plano.md` → `16`. Nenhuma tarefa `cancelled`. A linha do plano em
`estado.tsv` é `P-0754 ready`: o plano fecha só com o veredito do Marco 3 (ver pendências).

| tarefa | título | status |
|---|---|---|
| `AUF-T1` | O arquivo criado depois do recorte chega ao revisor como diferença | done |
| `AUF-T2` | Um teste exercita o caminho com acento que o versionador devolve em código | done |
| `AUF-T3` | O alvo com curinga casa, e o alvo que não existia chega marcado como novo | done |
| `AUF-T4` | O que quem conduz escreve nos próprios registros conta como registro da condução | done |
| `AUF-T5` | O recorte parte de tudo o que já está versionado | done |
| `AUF-T6` | O arquivo novo que não é texto se julga pelo conteúdo bruto | done |
| `AUF-T7` | O painel mostra o título do tíquete em curso | done |
| `AUF-T8` | A frase final do fechamento serve a todos os comandos | done |
| `AUF-T9` | O planejador ensaia a contingência e a faz caber no card | done |
| `AUF-T10` | A rubrica cobra a contingência pela regra do planejador | done |
| `AUF-T11` | O teste de interrupção nomeia os três casos que passaram por ele | done |
| `AUF-T12` | A versão pendente do modelo reconfere a restrição que cita o estado do plano | done |
| `AUF-T13` | O planejador pergunta se o impedimento do papel é ajuste do kit | done |
| `AUF-T14` | Os quatro herdados sem mudança fecham com a prova | done |
| `AUF-T15` | O guia de entrada descreve o kit com os herdados fechados | done |
| `AUF-T16` | A auditoria nova do kit, medida num plano fictício de ponta a ponta | done |

**Como os exemplos das `AUF-T1` a `AUF-T8` foram colhidos.** Um script cria repositórios git
temporários, fora do repositório do kit, e chama as funções dos instrumentos em duas versões: a do
commit `2513964` (o kit antes do plano, extraída por `git show 2513964:<arquivo>`) e a da árvore de
hoje. A saída está copiada como saiu; o hash do recorte aparece trocado por `<ref>`. A `AUF-T7` roda
contra o diário real do repositório, só em leitura. Os 17 testes que o plano acrescentou ou ajustou
passam hoje: `python -m pytest tests/test_review_evidence.py tests/test_progresso_hook.py tests/test_encerrar.py -q -k "arquivo_novo_depois_do_recorte or arquivo_novo_sem_desde or caminho_acentuado or curinga or marcado_como_novo or marca_de_novo or escrita_da_conducao or fora_do_registro_segue or versionado or binario or tiquete or conclusao_da_tarefa or fechado_conta_como_o_indice"`
→ `17 passed, 143 deselected`; a suíte inteira, `python -m pytest -q` → `521 passed`. Nos testes, o
prefixo `test_tf_` marca o teste do comportamento novo e `test_tr_`, o de regressão (o comportamento
vizinho que tem de continuar igual).

## `AUF-T1` — O arquivo novo chega ao revisor como diferença

**Contexto que a motivou:** para o arquivo criado depois do recorte e ainda não versionado, a
evidência colava o conteúdo inteiro, sem as marcas `+` de linha nova: o revisor não distinguia um
arquivo novo de um arquivo que já existia (herdado `H-10`). O levantamento não sabia se uma mudança
anterior no recorte já tinha resolvido o caso; o ensaio do planejador — a aplicação dos cards numa
cópia do repositório, antes de publicá-los — mostrou que não: o teste novo
falha em `2513964` (fato `F-13`).

**O que é o artefato:** um ramo em `_diff_para_arquivo` (`.claude/tools/review_evidence.py:634-648`):
com recorte, o arquivo não versionado que o recorte não contém sai como diff unificado contra o
vazio. Dois testes em `tests/test_review_evidence.py`:
`test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca` e
`test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral`.

**Como funciona na prática:**

1. **O que dispara:** o passo 6 do loop (skill `scrum-master`) roda
   `review_evidence.py --plano <plano> --tarefa <ID>` com o recorte gravado no despacho.
2. **A entrada:** o recorte e a árvore de trabalho.
3. **O processamento:** para cada arquivo-alvo não versionado e ausente do recorte, lê o texto e
   monta `difflib.unified_diff([], linhas)`.
4. **A saída** — `novo.md` com `linha-1` e `linha-2`, criado depois do recorte;
   `montar_trechos(repo, ["novo.md"], 4000, desde=ref)`:

```text
2513964: 'linha-1\nlinha-2\n'
hoje:    '(arquivo novo — ausente em `<ref>`)\n--- novo.md@<ref>\n+++ novo.md\n@@ -0,0 +1,2 @@\n+linha-1\n+linha-2\n'
```

A primeira linha da saída de hoje, a marca de arquivo novo, é da `AUF-T3`.

**Protege contra:** arquivo novo lido pelo revisor como conteúdo sem sinal de novidade. O teste
falha se o ramo sair.

## `AUF-T2` — Um teste guarda o caminho com acento que o git devolve codificado

**Contexto que a motivou:** com `core.quotepath` ligado, o `git status` devolve nome com acento entre
aspas e com escape octal (`"a\303\247\303\243o.txt"`). Esse nome não existe no disco, e
`coletar_arquivos_tocados` tem um ramo que mesmo assim o põe entre os tocados. Nenhum teste
exercitava esse ramo (herdado `H-12`; `git grep -n -i octal 2513964 -- tests` → 0 linhas).

**O que é o artefato:** o teste
`test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente` em
`tests/test_review_evidence.py`. O instrumento não muda: o teste fixa o comportamento de hoje.

**Como funciona na prática:** o teste liga `core.quotepath` num repositório temporário, cria
`ação.txt` depois do recorte e confere que a lista de tocados é exatamente o nome codificado. O
mesmo cenário, rodado nas duas versões:

```text
2513964: tocados com acento: ['a\\303\\247\\303\\243o.txt', 'versionado.log']
hoje:    tocados com acento: ['a\\303\\247\\303\\243o.txt']
hoje:    trecho desse caminho: (sem diferença coletável — arquivo ausente na árvore de trabalho)
```

O `versionado.log` a mais na versão antiga é o defeito que a `AUF-T5` corrige. A terceira linha é o
limite que o teste deixa à vista: o arquivo entra na lista, mas o revisor recebe o aviso de arquivo
ausente no lugar do diff (achado `AE-99`, aberto — ver os defeitos). Hoje:
`grep -rn -i "octal" tests | wc -l` → `3`.

**Protege contra:** remoção silenciosa do ramo, que faria o arquivo com acento sumir da lista de
tocados sem o revisor saber que ele existe.

## `AUF-T3` — O alvo com curinga casa, e o arquivo novo chega marcado

**Contexto que a motivou:** o campo Arquivos-alvo aceitava pasta, expandida contra os tocados, mas
descartava o alvo escrito com `*` como texto que não é caminho: os arquivos criados dentro do
padrão caíam como "fora dos alvos" e o escopo da entrega saía aberto. O arquivo-alvo que não existia
antes chegava sem aviso de que era novo (herdado `H-13`).

**O que é o artefato:** cinco mudanças em `.claude/tools/review_evidence.py` — `_CAMINHO_RE` aceita
`*` (`:125`); função `_eh_alvo_curinga` (`:426-429`); `montar_trechos` casa o curinga contra os
tocados por `fnmatch.fnmatchcase`, com uma entrada por tocado que casa ou o texto
`(nenhum arquivo tocado casa com o curinga)` quando nenhum casa (`:686-706`); `confrontar_escopo`
dá por coberto o tocado que casa (`:547-558`); a marca `(arquivo novo — ausente em ...)` abre o
trecho do arquivo não versionado ausente da base — o recorte, ou `HEAD` sem recorte (`:647`,
`:664`). Quatro testes, nomes com `curinga`, `marcado_como_novo` e `marca_de_novo`.

**Como funciona na prática:** mesmo gatilho da `AUF-T1`. Cenário: depois do recorte, criam-se
`relatorios/a.md` e `relatorios/b.md`; o card declara o alvo `` `relatorios/*.md` ``:

```text
2513964: alvos extraídos: []
2513964: chaves dos trechos: ['relatorios/*.md']
2513964: fora_dos_alvos: ['relatorios/a.md', 'relatorios/b.md', 'versionado.log']
hoje:    alvos extraídos: ['relatorios/*.md']
hoje:    chaves dos trechos: ['relatorios/a.md', 'relatorios/b.md']
hoje:    fora_dos_alvos: []
```

A marca de arquivo novo sem recorte, no `novo.md` da `AUF-T1`:

```text
2513964: 'linha-1\nlinha-2\n'
hoje:    '(arquivo novo — ausente em `HEAD`)\nlinha-1\nlinha-2\n'
```

Limite: o `*` atravessa `/` — `fnmatch.fnmatchcase("relatorios/sub/x.md", "relatorios/*.md")` →
`True`, diferente do glob de shell (achado `AE-104`, aberto).

**Protege contra:** arquivo criado dentro de padrão declarado acusado como fora de escopo, e arquivo
novo julgado como alteração de arquivo existente.

## `AUF-T4` — O que a condução escreve conta como registro da condução

**Contexto que a motivou:** quem conduz o loop escreve no diário, na telemetria e nos planos durante
toda tarefa. Quando outro card ou tíquete do mesmo plano declarava um desses arquivos como alvo, a
evidência atribuía a escrita da condução a esse tíquete, que não a fez (herdado `H-18`).

**O que é o artefato:** a ordem de dois testes no laço de `confrontar_escopo`
(`.claude/tools/review_evidence.py:564-575`) e a docstring (`:531-534`), que enuncia a precedência:
coberto pelos alvos do card > registro da condução > alvo de outra tarefa do mesmo plano > ato do
dono fora do ciclo de tarefa > fora dos alvos sem atribuição. Dois testes, nomes com
`escrita_da_conducao` e `fora_do_registro_segue`.

**Como funciona na prática:** mesmo gatilho da `AUF-T1`; o resultado vai para a seção de escopo da
evidência. Exemplo:
`confrontar_escopo(["docs/DIARIO_DE_OBRAS.md"], ["src/b.py"], repo, {"docs/DIARIO_DE_OBRAS.md": "TK-1a"})`:

```text
2513964: registro_orquestracao: [] | de_outra_tarefa: {'docs/DIARIO_DE_OBRAS.md': 'TK-1a'}
hoje:    registro_orquestracao: ['docs/DIARIO_DE_OBRAS.md'] | de_outra_tarefa: {}
```

Limite: a lista por arquivo da evidência ainda rotula os mesmos arquivos `atribuição: alheio`,
enquanto o resumo os dá como registro da condução (achado `AE-115`, aberto).

**Protege contra:** evidência que acusa um tíquete de ter escrito o que a condução escreveu.

## `AUF-T5` — O recorte inclui o arquivo versionado que o `.gitignore` também cobre

**Contexto que a motivou:** o recorte era gravado num índice temporário vazio com `git add -A`, que
respeita o `.gitignore`. Arquivo versionado que o `.gitignore` também cobre ficava fora do recorte,
com efeito duplo: a mudança nele sumia da evidência, e ele aparecia como tocado em toda tarefa
(herdado `H-19`). O resumo de diferenças (`coletar_diff_stat`) gravava a árvore pelo mesmo molde e
tinha o mesmo defeito (fato `F-14`).

**O que é o artefato:** a função `_gravar_arvore_de_trabalho` (`.claude/tools/review_evidence.py:208-233`),
única residência da gravação da árvore: roda `git read-tree HEAD` no índice temporário antes do
`git add -A`. `capturar_ref` e `coletar_diff_stat` a chamam. Dois testes, nomes com `versionado`.

**Como funciona na prática:** dispara no passo 4 do loop (`review_evidence.py --capturar-ref`, no
despacho) e de novo no passo 6 (resumo de diferenças). Cenário: `versionado.log` versionado com
`git add -f` e listado no `.gitignore`, reescrito com `v2` antes do recorte:

```text
2513964: git show <ref>:versionado.log -> exit 128 ''
2513964: tocados logo depois do <ref>: ['versionado.log']
hoje:    git show <ref>:versionado.log -> exit 0 'v2\n'
hoje:    tocados logo depois do <ref>: []
```

A Verificação 2 do card, rodada hoje, conta definição, chamadas e `read-tree`: `[1-2-1]`.

**Protege contra:** arquivo versionado que some da evidência, ou que polui toda evidência como
tocado sem ter sido.

## `AUF-T6` — O arquivo que não é texto é comparado pelos bytes

**Contexto que a motivou:** o arquivo não versionado que já existia no recorte é julgado pelo
conteúdo. Quando ele não se lia como texto UTF-8, a função devolvia "mudou" sempre, e um binário
parado entrava nos tocados de toda tarefa (herdado `H-20`).

**O que é o artefato:** a função `_bytes_do_ref` (`.claude/tools/review_evidence.py:310-314`) e o ramo
de bytes de `_nao_rastreado_mudou_desde_ref` (`:323-329`). Dois testes, nomes com `binario`.

**Como funciona na prática:** mesmo gatilho da `AUF-T1`, na montagem da lista de tocados. Cenário:
`imagem.bin` com os bytes `FF FE 00 81`, gravado antes do recorte:

```text
2513964: binário não tocado depois do <ref>, tocados: ['imagem.bin', 'versionado.log']
2513964: binário regravado, tocados: ['imagem.bin', 'versionado.log']
hoje:    binário não tocado depois do <ref>, tocados: []
hoje:    binário regravado, tocados: ['imagem.bin']
```

Limite: o caso simétrico — binário no recorte, texto hoje — derruba a coleta. Rodado hoje, com
`m.dat` gravado com `FF FE 00 81` antes do recorte e reescrito com `ola`:
`AttributeError: 'NoneType' object has no attribute 'splitlines'` (achado `AE-106`, aberto).

**Protege contra:** binário intocado apresentado como mudança da entrega.

## `AUF-T7` — O painel mostra o título do tíquete

**Contexto que a motivou:** o painel de progresso (`.claude/estado/progresso.txt`) mostra o título
da tarefa em curso. A busca do título só reconhecia o cabeçalho de card de plano
(`### <id> — <título> [`); durante um tíquete do diário (`## TK-<n> — <título>`) o painel mostrava
o identificador cru (herdado `H-14`).

**O que é o artefato:** o padrão de tíquete em `localizar_card`
(`.claude/tools/progresso_hook.py:149`, `:157-159`), que devolve o título com objetivo e título de
plano vazios. Dois testes, nomes com `tiquete`, em `tests/test_progresso_hook.py`.

**Como funciona na prática:** o gancho `progresso_hook.py` roda nos eventos `PreToolUse`,
`PostToolUse` e `Stop` do harness, descobre a tarefa em curso e procura o título. Rodado contra o
diário real:

```text
2513964: localizar_card("TK-91") -> ('TK-91', '', '')
hoje:    localizar_card("TK-91") -> ('O modelador não tem o ato que promove ou elimina a versão pendente no marco', '', '')
```

O card de tíquete (`TK-84a`) sai igual nas duas versões, com o título do card.

**Protege contra:** painel com sigla no lugar do título. Limite: a tarefa em curso vem de
`.claude/estado/tarefa-corrente.json`; quando esse arquivo aponta tarefa velha, o título sai errado
(registro 54 do relatório; ver pendências).

## `AUF-T8` — A frase final do fechamento concorda com qualquer comando

**Contexto que a motivou:** a última linha de `encerrar.py` imprimia `<comando> fechado` para todos
os subcomandos; para `tarefa`, saía "tarefa fechado" (herdado `H-15`).

**O que é o artefato:** a linha de sucesso de `main` em `.claude/tools/encerrar.py:1293`, a asserção
ajustada de `test_tf_fechado_conta_como_o_indice` e o teste novo
`test_tf_conclusao_da_tarefa_sem_erro_de_concordancia`, em `tests/test_encerrar.py`.

**Como funciona na prática:** dispara ao fim de todo subcomando de `encerrar.py` que grava
relatório. Rodado num repositório temporário montado pelo auxiliar `_montar_repo` dos testes, com
`encerrar.py tarefa`:

```text
2513964: exit 0 -> encerrar: OK - tarefa fechado; relatório em '<repo>/docs/RDO/P-0001-ALF-T1-primeira-tarefa-do-plano.md'.
hoje:    exit 0 -> encerrar: OK - comando 'tarefa' concluído; relatório em '<repo>/docs/RDO/P-0001-ALF-T1-primeira-tarefa-do-plano.md'.
```

A Verificação 2 do card, rodada hoje, conta a frase nova e a velha no arquivo: `[1-0]`.

**Protege contra:** frase de conclusão com erro de concordância; o teste falha se ela voltar.

## `AUF-T9` — O planejador ensaia a contingência e a declara nos alvos

**Contexto que a motivou:** o planejador ensaia as verificações de cada card numa cópia do
repositório antes de publicá-lo, mas não ensaiava a contingência. No plano anterior, contingências
saíram contrariando a restrição do próprio card e escrevendo em arquivo que o card não declarava
(herdados `H-1` e `H-8`). `card_check.py`, o verificador de cards, emite 17 violações e nenhuma olha
o campo Contingências (fato `F-12`).

**O que é o artefato:** duas regras na definição do agente planejador,
`.claude/agents/pantonic-planner.md` — **A contingência não contradiz o card** (Fase 4, item 3,
`:276-279`): a ação `seguir com <X>` não contraria nenhuma Restrição do card, e todo arquivo que ela
escreve entra nos Arquivos-alvo seguido de `(condicional: contingência <n>)`; **A contingência se
ensaia** (Fase 4, item 14, `:455-458`): a contingência se aplica na cópia como passo do card, as
verificações se re-rodam e o valor que ela muda sai publicado nela.

**Como funciona na prática:** o planejador lê a própria definição ao ser despachado para decompor um
plano em cards; a regra vale no ato de escrever cada card. Exemplo real neste plano: o card
`AUF-T16` declara `docs/plans/P-0754-auditoria-final/plano.md` `(condicional: contingência 2)` nos
Arquivos-alvo (`plano.md:959`), porque a contingência 2 grava achados ali. No plano fictício, o
planejador ensaiou a contingência `seguir com` do card `SA-T2` (registro 9 do relatório). Contagem
das duas regras hoje: `[1-1]`.

**Protege contra:** contingência que manda o executor violar restrição do card ou escrever em arquivo
que a evidência acusaria como fora de escopo. Limite: a regra é lida e aplicada pelo planejador e
pelo revisor; nenhuma checagem mecânica a cobra (`card_check.py` segue sem olhar contingências).

## `AUF-T10` — A rubrica cobra a contingência pela mesma regra

**Contexto que a motivou:** a rubrica de criação de card — a régua de autoria aplicada antes do
despacho (`docs/RUBRICA_DE_REVISAO.md:288`) — não dizia nada sobre contingência (herdados `H-1`,
`H-8`).

**O que é o artefato:** o critério `(xix)` da tabela da §8 de `docs/RUBRICA_DE_REVISAO.md:312`: a
contingência foi aplicada no ensaio, as verificações re-rodadas depois dela, ela não contraria
nenhuma Restrição do card e todo arquivo que ela escreve está nos Arquivos-alvo com a marca
condicional.

**Como funciona na prática:** quem julga um card antes do despacho percorre os critérios `(i)` a
`(xix)`; card cuja contingência escreve em arquivo não declarado reprova no `(xix)`. Contagem hoje:
`[1-1]` (o texto do critério e a linha `| (xix) |`).

**Protege contra:** planejador e revisor com réguas diferentes para o mesmo campo. Limite: o `(xix)`
omite uma cláusula da regra do planejador — "linha cujo valor a contingência muda publica o valor
medido com ela aplicada"; card que ensaia sem publicar o valor passa (achado `AE-107`, aberto).

## `AUF-T11` — O teste de interrupção nomeia três pontos de parada

**Contexto que a motivou:** o item 8 da Fase 4 do planejador pergunta, em termos gerais, se o
executor teria de parar para decidir algo. Três casos passaram por essa pergunta no plano anterior
e pararam executores (herdados `H-2`, `H-3`, `H-4`).

**O que é o artefato:** um bloco no item 8 da Fase 4 de `.claude/agents/pantonic-planner.md:346-352`
com os três pontos, pelo nome: (a) **Objetivo condicional contra contrato incondicional** — o
Objetivo diz "se" enquanto os contratos mandam fazer sempre; (b) **caminho sem forma fixada** —
argumento de caminho sem dizer se é relativo à raiz ou absoluto; (c) **argumento sem limpeza nem
recusas fechadas** — texto sem a normalização antes do uso e sem a lista das entradas recusadas.

**Como funciona na prática:** o planejador confere os três pontos em todo card, no ato da
decomposição. Registro de uso: os cards do plano fictício fixaram forma de caminho, `strip()` e
recusas, e houve 0 parada de executor por dúvida em 20 execuções (registro 48 do relatório).
Contagem hoje: `[1-1-1]`.

**Protege contra:** card que obriga o executor a decidir forma de caminho, limpeza de argumento ou
qual dos dois textos contraditórios seguir.

## `AUF-T12` — A versão pendente do modelo reconfere as restrições dos cards

**Contexto que a motivou:** o modelo de domínio do plano (a §1, com objetos e operações) muda
durante a execução por emenda: o modelador grava a versão nova ao lado da vigente, numa seção
`## 1A` marcada pendente, que só passa a valer quando o dono a valida no marco seguinte (promoção de
versão). Enquanto isso, a rodada de replanejamento — a tarefa em que o planejador reescreve os cards
que a mudança afeta — acerta os cards. Uma restrição de card afirmava um estado do plano que a versão
pendente mudou, e ninguém a reconferiu (herdado `H-5`).

**O que é o artefato:** a regra **Versão pendente reconfere a restrição que cita o estado do plano**,
no passo 4 da Rodada de replanejamento de `.claude/agents/pantonic-planner.md:544-547`: toda
Restrição de card que afirma estado do plano — seção que existe, versão vigente, operação presente —
se reconfere contra o plano gravado no mesmo ato, e a falsa se reescreve.

**Como funciona na prática:** dispara quando o modelador grava uma versão pendente e o planejador
entra na rodada de replanejamento. Registro de uso: no plano fictício, o planejador reconferiu as
restrições na rodada (registro 36 do relatório). Contagem hoje: `[1]`.

**Protege contra:** restrição de card que fica falsa depois de uma emenda do modelo. Limite: a regra
não cobre o campo **Operação do modelo** do card — dois cards do plano fictício citaram a mesma
operação com textos diferentes e a checagem do modelo aprovou (achado `AE-116`, aberto).

## `AUF-T13` — O planejador pergunta se o impedimento do papel é ajuste do kit

**Contexto que a motivou:** diante de "o papel X não consegue Y", o planejador aceitava o impedimento
como dado e contornava, mesmo quando a causa era configuração corrigível do kit (herdado `H-9`).

**O que é o artefato:** o bullet **Impedimento de papel é pergunta antes de ser dado**, na Fase 1 de
`.claude/agents/pantonic-planner.md:137-141`: a campanha de levantamento pergunta primeiro se o
impedimento é configuração do kit (frontmatter `tools:` do agente, `.claude/settings*.json`) ou
limite da plataforma; configuração se corrige como tarefa, só o limite se contorna, com a razão na §2
do plano.

**Como funciona na prática:** vale na Fase 1, quando o planejador organiza o levantamento. Exemplo
real neste plano: o fato `F-11` (`plano.md:248`) lista a configuração de cada papel, e o `F-3`
(`plano.md:240`) registra que "subagente não aciona outro agente" é limite da plataforma — o que
levou a auditoria a ser executada pela sessão principal (registro 4 do relatório). Contagem hoje:
`[1]`.

**Protege contra:** contorno caro de um impedimento que um ajuste de configuração resolve.

## `AUF-T14` — Quatro herdados encerrados sem mudança, com a prova

**Contexto que a motivou:** quatro herdados seguiam abertos embora, conferidos, não pedissem mudança:
dois com a premissa caída (`H-11`, `H-17`), um com a regra já existente (`H-7`) e um teto conhecido
do instrumento (`H-6`).

**O que é o artefato:** um sufixo `· **Desfecho (P-0754, AUF-T14, 2026-09-28):** …` no fim da linha
de origem de cada achado — `AE-21` e `AE-22` em `docs/plans/P-0753-auditoria-estagio-1/plano.md:1753-1754`,
`AE-51` em `docs/plans/P-0752-fato-no-ponto-de-uso.md:841`, `AE-89` em `docs/DIARIO_DE_OBRAS.md:6084`.

**Como funciona na prática:** quem busca o achado pelo id chega à linha e lê o desfecho nela.
Saída de `grep -n -o "· \*\*Desfecho (P-0754, AUF-T14, 2026-09-28):\*\* .*"` nos três arquivos:

```text
P-0753…/plano.md:1753: … encerrado sem mudança no kit — o teto de 4000 caracteres do trecho é conhecido do instrumento e sai marcado na evidência, como o laudo da `AF-T14` registrou.
P-0753…/plano.md:1754: … encerrado sem mudança no kit — a regra já existe: o ensaio dos cards em cópia, item 14 da Fase 4 de `.claude/agents/pantonic-planner.md`, e o critério (xii)(b) de `docs/RUBRICA_DE_REVISAO.md`.
P-0752-fato-no-ponto-de-uso.md:841: … encerrado sem mudança no kit — a premissa caiu: `docs/ACIONAMENTOS_CONSULTOR.tsv` é versionado desde o commit `2513964`, e `review_evidence.py` o trata como registro da condução.
DIARIO_DE_OBRAS.md:6084: … encerrado sem mudança no kit — a premissa caiu: o card de tarefa é isento do teto do `backlog.py show`, e os oito cards do `P-0742` saem inteiros, sem marca de truncado.
```

Verificação do card hoje: `[1-1-1-1]`; `python .claude/tools/backlog.py check` →
`check: OK — nenhuma violação.`

**Protege contra:** achado que parece aberto e volta a ser investigado.

## `AUF-T15` — O guia de entrada descreve o kit resultante

**Contexto que a motivou:** o `README.md` é o guia de quem chega ao kit, e toda etapa que muda o kit
termina com a revisão dele. Antes do plano, o guia não citava `review_evidence.py` (0 ocorrências em
`2513964`) e descrevia o painel só com título de card.

**O que é o artefato:** três passagens do `README.md`: a §6 (`:472`) diz que o painel mostra o título
do card de plano ou do tíquete do diário; a condição 4 da §8 (`:633-635`) diz que a contingência faz
parte do card; um bullet novo na §11 (`:929-934`) descreve `review_evidence.py`. As regras internas
do planejador e da rubrica (`AUF-T10` a `AUF-T13`) ficam fora do guia.

**Como funciona na prática:** o guarda `pwsh -NoProfile -File .claude/checks/check-readme.ps1` confere
a estrutura do guia contra o kit. Rodado hoje:

```text
check-readme: OK - 10 agente(s), 13 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: 'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.
check-readme exit=0
```

Contagem das três passagens: `[1-1-1]`; `grep -c review_evidence README.md` → `1`.

**Protege contra:** guia que descreve um kit anterior ao que está instalado.

## `AUF-T16` — A auditoria nova do kit

**Contexto que a motivou:** a auditoria anterior mediu o kit antes destes herdados fecharem. Duas
matérias do inventário pediam medida e não remédio: onde a rodada de replanejamento grava a medida
dos cards que reescreve (`H-16`) e quanto das ações do gerente do loop — a rotina `scrum-master` —
é mecânico e quanto custa (`H-21`), com o gerente mantido no loop.

**O que é o artefato:** o relatório `docs/audits/AUDITORIA_FINAL_KIT.md` (307 linhas, `wc -l`), no
formato da auditoria do estágio 1, com uma seção nova, a §8. Contagens rodadas hoje sobre o arquivo:

| conteúdo | onde | contagem |
|---|---|---|
| cláusulas (linhas `\| K-`) | §2 | 43 |
| registros de medição, pela última coluna da tabela | §3 | 54: 18 `adequado`, 15 `inadequado`, 21 `oportunidade` |
| conclusão por dimensão, com veredito geral | §4 | 8 dimensões |
| recomendações (cabeçalhos `### R-`) | §5 | 31, `R-01` a `R-31` |
| registros não `adequado` sem recomendação que os cite no campo `Origem:` | §3 × §5 | 0 de 36 |
| custo por papel do plano fictício e da sessão principal | §6 | — |
| o que foi descartado e o que ficou na árvore | §7 | — |
| uma linha por passo `P1` a `P10` do gerente do loop | §8 | 10 |

**Como funciona na prática:**

1. **O que dispara:** a instrução do dono no Marco 2. A tarefa nasce `blocked` e o loop não a
   despacha; a sessão principal a abre por `python .claude/tools/backlog.py status AUF-T16 ready`
   e, no ato seguinte, `... in-progress`. A auditoria roda na sessão principal porque o plano
   fictício precisa acionar planejador, modelador, executor, revisor e consultor, e subagente não
   aciona outro agente (fato `F-3`, limite da plataforma); é a única exceção à regra de que todo
   card vai a um executor (decisão `DAU-3`).
2. **A entrada:** o kit com as `AUF-T1` a `AUF-T15` aplicadas e o relatório do estágio 1
   (`docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md`) como molde, seção por seção.
3. **O processamento:** (a) retrato da árvore — cópia, fora do repositório, da saída de
   `git status` e dos registros que o plano fictício vai escrever, para restaurá-los depois;
   (b) o plano fictício, com cinco cards, atravessa planejador, batedor, modelador, decomposição em
   cards, marco, loop, revisão, consultor, emenda do modelo, rodada de replanejamento, promoção de
   versão e fechamento, e cada passagem vira um registro; (c) o custo por papel sai do bloco
   `<usage>` — a contagem de tokens que o harness anexa à notificação de conclusão de cada
   subagente —, e o da sessão principal, do transcript; (d) limpeza: a pasta do plano fictício sai e
   os registros voltam ao retrato.
4. **A saída:** o relatório. As seis verificações do card, rodadas hoje:

| # | o que confere | saída |
|---|---|---|
| 1 | as nove seções, cada cabeçalho exato numa linha | `[9]` |
| 2 | as oito dimensões numa linha de tabela | `[8]` |
| 3 | uma linha começando por `\| P<n> \|` para cada passo 1 a 10 | `[10]` |
| 4 | a cláusula cujo texto contém `rodada de replanejamento grava a medida` (herdado `H-16`) | `[1]` |
| 5 | a frase `As recomendações deste relatório não se aplicam no P-0754` e ao menos um `### R-` | `[1-1]` |
| 6 | o nome da pasta do plano fictício citado no relatório | `[1]` |

A limpeza, conferida hoje: `ls docs/plans | grep -c sonda-auditoria-final` → `0`.

O veredito geral do relatório (`AUDITORIA_FINAL_KIT.md:159`): *"adequado na integração e na
qualidade; inadequado em custo e em três lacunas de amarração entre modelo, card e medida; tem
oportunidade de melhoria em confiabilidade, mecanização e fluxo."* As duas matérias herdadas:

- **`H-21`, o gerente do loop** (§8, `:290-307`). Dos dez passos, sete já estão em instrumento
  (`P1`, `P2`, `P3`, `P5`, `P7`, `P9`, `P10`); o que resta à mão é redação de prompt (`P4`, `P6`),
  re-derivação de âncora (`P3`) e texto de handover (`P9`), mecanizáveis pelas `R-02` e `R-03`. O
  custo, porém, está no tamanho do contexto que cada turno da sessão principal reenvia — 285,6k
  tokens por turno no loop real das `AUF-T1` a `AUF-T15` (101 turnos), 485,6k no plano fictício
  (29 turnos) —, e o remédio é a `R-01`: o loop abre em contexto novo, separado do planejamento.
- **`H-16`, a medida da rodada de replanejamento**: vira a cláusula `K-31` e a `R-05`. Hoje a
  rodada que reescreve cards não grava a medida deles em lugar nenhum; a `R-05` manda
  `card_check.py --gravar` gravar a medida de cada card reescrito sob a pasta do plano, num arquivo
  por estado medido (antes e depois da entrega).

A revisão deu `ressalva`, 90% (`laudos/AUF-T16.md`): seis registros sem recomendação e parte do
kit sem cláusula. O consultor corrigiu o relatório no ato (decisão `DAU-33`, `plano.md:292`),
acrescentando as `R-26` a `R-31` e as `K-39` a `K-43`; a contagem de hoje, 0 registro sem
recomendação, é depois dessa correção.

**Protege contra:** escolher o plano seguinte sem medida do kit como ele está. As recomendações não
se aplicam neste plano (`AUDITORIA_FINAL_KIT.md:165`); vão ao plano sucessor, em autoria.

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| A contingência não contradiz o card | contingência que viola restrição ou escreve fora dos alvos | `.claude/agents/pantonic-planner.md`, Fase 4, item 3 |
| A contingência se ensaia | contingência publicada sem ter sido exercitada | `pantonic-planner.md`, Fase 4, item 14 |
| Três pontos de parada nomeados | card que obriga o executor a decidir | `pantonic-planner.md`, Fase 4, item 8 |
| Versão pendente reconfere a restrição que cita o estado do plano | restrição de card falsa depois de emenda do modelo | `pantonic-planner.md`, Rodada de replanejamento, passo 4 |
| Impedimento de papel é pergunta antes de ser dado | contorno caro de impedimento que é só configuração | `pantonic-planner.md`, Fase 1 |
| Critério `(xix)` da rubrica de criação de card | réguas diferentes para planejador e revisor | `docs/RUBRICA_DE_REVISAO.md`, §8 |
| Precedência da atribuição de escopo na evidência | escrita da condução atribuída a tarefa alheia | docstring de `confrontar_escopo`, `.claude/tools/review_evidence.py` |

## Os ganhos, medidos

Antes = versão do commit `2513964`; depois = árvore de hoje. As linhas de comportamento vêm dos
exemplos rodados nas seções das tarefas.

| medida | antes | depois |
|---|---|---|
| trecho de arquivo novo criado depois do recorte | conteúdo integral, sem `+` | marca de arquivo novo e diff com `+linha-1`, `+linha-2` |
| alvo `relatorios/*.md` com dois arquivos criados | alvo descartado; 2 arquivos fora dos alvos | alvo lido; 1 trecho por arquivo; 0 fora dos alvos |
| escrita da condução no diário, declarada por outro tíquete | atribuída ao tíquete `TK-1a` | registro da condução |
| arquivo versionado e ignorado, alterado antes do recorte | ausente do recorte (`git show` exit 128) e tocado sem ter sido | presente no recorte (`v2`) e fora dos tocados |
| binário não versionado e intocado | entre os tocados | fora dos tocados; entra só quando os bytes mudam |
| título do painel durante o tíquete `TK-91` | `TK-91` | o título do tíquete |
| frase final de `encerrar.py tarefa` | `tarefa fechado` | `comando 'tarefa' concluído` |
| suíte de testes | `505 passed` (referência datada nos cards, HEAD `2513964`, `plano.md:340`) | `521 passed` |
| linhas de teste com `octal` | 0 | 3 |
| menções a `review_evidence` no `README.md` | 0 | 1 |
| destino dos 21 herdados | 21 abertos com rota "auditoria final" | 15 fechados por mudança no kit, 4 encerrados sem mudança com prova, 2 medidos no relatório (`K-31`/`R-05`, §8) |
| diferença da árvore contra `2513964` | — | `git diff --shortstat 2513964` → `17 files changed, 516 insertions(+), 49 deletions(-)`, na redação deste documento; o número cresce sozinho, porque `docs/telemetria.tsv` (52 das linhas) ganha uma linha a cada subagente concluído |

**Custo medido do plano**, pela série `docs/telemetria.tsv` — a tabela em que um gancho do harness
grava, a cada subagente concluído, a tarefa, o modelo e os tokens do bloco `<usage>`. Hoje há 35
linhas com id `P-0754-*` ou `AUF-T*`; 33 entram na tabela, a `AUF-T16` entra sem valor, e a linha
1071 (`P-0754-planejador`, 75,1k) fica fora: foi gravada depois do fechamento da `AUF-T16`, quando
nenhum card deste plano estava aberto, e é seguida de cinco linhas `P-0755-scout` — o planejador
deste plano é a linha 1036 (ver pendência 6).

| papel | linhas | tokens (k) |
|---|---|---|
| planejador (Opus) | 1 | 311,4 |
| modelador (Opus) | 1 | 89,6 |
| executores das `AUF-T1` a `AUF-T15` (Sonnet) | 15 | 885,8 |
| revisões das `AUF-T1` a `AUF-T15` (Opus) | 15 | 616,6 |
| consultor na `AUF-T2` (Opus) | 1 | 51,3 |
| `AUF-T16` (sessão principal) | 1 | `nao_medido` |
| **total medido** | **33** | **1.954,7** |

O custo da sessão principal e o do plano fictício estão no relatório, §6 (`AUDITORIA_FINAL_KIT.md:262-280`),
medidos pelo transcript: subagentes do plano fictício 1.250,0k; sessão principal no loop real das
`AUF-T1` a `AUF-T15`, 101 turnos e 28.847k de contexto reenviado.

## O padrão que a execução revelou

**Classe 1 — o cerco de um caso deixa o vizinho de fora.** No gerador de evidência, cada card
corrigiu exatamente o caso que o herdado nomeava, e o caso adjacente apareceu na revisão: arquivo
novo vazio (`AE-96`), caminho com escape octal sem diff (`AE-99`), `*` que atravessa `/` (`AE-104`),
binário no recorte e texto hoje (`AE-106`), binário novo sem a marca (`AE-114`), dois rótulos para o
mesmo arquivo (`AE-115`). Estado: um caso fechado sem guarda (`AE-96`), cinco abertos com
recomendação no relatório. Nenhuma regra do kit manda o card de correção listar os casos vizinhos.

**Classe 2 — verificação que conta presença não discrimina a propriedade.** A verificação por `-k`
e o piso de suíte por contagem passaram verdes com uma asserção de teste vizinho apagada (`AE-97`,
`AE-98`); as verificações da auditoria contaram cabeçalhos e linhas e não discriminaram "uma
recomendação por registro" (`AE-111`); o critério `(xix)` copiou a regra do planejador com uma
cláusula a menos (`AE-107`); a contingência 2 da auditoria não nomeava a marca que a dispara
(`AE-112`). Estado: os casos foram reparados no ato ou ficaram registrados; a classe segue sem guarda,
e a `R-12` cobre só o primeiro caso.

**Classe 3 — atribuição pelo estado corrente velho.** Telemetria e painel descobrem a tarefa pelo
primeiro id de plano da mensagem ou por `.claude/estado/tarefa-corrente.json`; quando esse estado
está velho, a medida e o título vão para a tarefa errada (registros 41 e 54 do relatório). A série
de hoje mostra o caso: duas linhas com id de tarefa do plano fictício descartado e, depois do
fechamento, uma linha de planejador com o id deste plano sem card dele aberto (pendência 6).
Estado: regra escrita na `R-16`, aplicação pendente.

## Defeitos da execução, com estado

Achados da §9 do plano. Duplicatas contadas uma vez: `AE-100` e `AE-101` repetem `AE-98` e
`AE-99`; `AE-117`, `AE-118` e `AE-119` repetem `AE-111`, `AE-112` e `AE-113`; `AE-103` é o registro
de fechamento do `AE-96`.

**Os defeitos de instrumento, reproduzidos hoje.** Um script cria repositórios git temporários fora
do kit e chama `.claude/tools/review_evidence.py` da árvore de hoje; o `AE-99` e o `AE-104` estão
rodados nas seções da `AUF-T2` e da `AUF-T3`. Cenários: `AE-96`, arquivo vazio criado depois do
recorte; `AE-114`, arquivo com os bytes `FF FE 00 81` criado depois do recorte; `AE-106`, o mesmo
arquivo gravado antes do recorte e reescrito com `ola`; `AE-115`, evidência montada com o diário
tocado e fora dos alvos; `AE-105`, repositório sem `.claude/tools/rdo.py`, com o verbo `--atribuir`
e, para comparar, o caminho do dossiê. Caminho temporário trocado por `<tmp>`:

```text
AE-96: '(arquivo novo — ausente em `<ref>`)\n\n'
AE-114: '(arquivo binário ou não-UTF-8 — trecho omitido)'
AE-106: AttributeError: 'NoneType' object has no attribute 'splitlines'
AE-115: - `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: (sem entrada em `git status`)
AE-115: - Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`
AE-105 --atribuir: exit 1 | ultima linha: ReviewEvidenceValidationError: rdo.py: módulo não encontrado em '<tmp>\.claude\tools\rdo.py' | linhas stderr: 10
AE-105 dossie:    exit 1 | review_evidence: FALHOU - rdo.py: módulo não encontrado em '<tmp>\.claude\tools\rdo.py' | linhas stderr: 1
```

O `AE-96` sai com a marca e sem bloco em branco solto, mas nenhum teste cobre o arquivo vazio. As
duas linhas do `AE-115` são do mesmo documento: a lista por arquivo diz `alheio`, o resumo de escopo
diz registro da condução. O `AE-105` é a mesma falta de arquivo tratada de dois jeitos: dez linhas
de traceback num verbo, uma linha nomeada no outro.

| achado | o que é | estado | o que fecha |
|---|---|---|---|
| `AE-96` (`AE-103`) | arquivo novo vazio saía como bloco em branco | 🟡 caso fechado: hoje sai `'(arquivo novo — ausente em `<ref>`)\n\n'` (rodado); nenhum teste com arquivo vazio | — |
| `AE-97` | a entrega da `AUF-T2` apagou `assert "+linha-1" not in texto` de um teste vizinho | 🟡 reposta no ato (decisão `DAU-32`); `git diff 3be2450 --numstat -- tests/test_review_evidence.py` contra o recorte da `AUF-T2` deu `20 0` na hora (`cenario.md:25`) e dá `218 0` hoje — as tarefas seguintes só acrescentaram linhas; nada barra outra remoção igual | classe no `AE-98` |
| `AE-98` (`AE-100`) | verificação por `-k` e piso por contagem não veem linha de teste removida | 🔴 remédio escrito, não aplicado | `R-12`, pendência 2 |
| `AE-99` (`AE-101`) | arquivo com acento no nome chega ao revisor sem diff | 🔴 | `R-31`, pendência 2 |
| `AE-102` | o fechamento registra de novo achado já registrado com outro texto | 🔴 | `R-19`, pendência 2 |
| `AE-104` | `*` do alvo atravessa `/` | 🔴 | `R-30`, pendência 2 |
| `AE-105` | `review_evidence.py --atribuir` sem `rdo.py` sai com traceback cru (rodado acima) | 🔴 | `R-13`, pendência 2 |
| `AE-106` | binário no recorte e texto hoje derruba a coleta (`AttributeError`, rodado) | 🔴 | `R-13`, pendência 2 |
| `AE-107` | o critério `(xix)` omite "publica o valor medido com a contingência aplicada" | 🔴 remédio escrito no achado, sem `R` no relatório | pendência 3 |
| `AE-108` | card de inserção em lista não nomeou a linha em branco separadora; a escolha da entrega é compatível | 🟡 | pendência 3 |
| `AE-109` | a evidência atribui o diário inteiro à entrega quando só uma linha é dela | 🟡 limite conhecido (atribuição por arquivo, sem recorte por trecho), anotado na §3 da rubrica | — |
| `AE-110` | trecho de diff truncado em 4000 caracteres | 🟡 teto conhecido, sempre marcado na evidência; encerrado sem mudança (desfecho do `AE-21`, `AUF-T14`) | — |
| `AE-111` (`AE-117`) | verificações da auditoria não discriminam cobertura | 🟡 caso reparado (decisão `DAU-33`: `R-26` a `R-31` e `K-39` a `K-43` acrescentadas; 0 registro sem recomendação); classe sem guarda | pendência 3 |
| `AE-112` (`AE-118`) | contingência 2 da auditoria sem a marca que a dispara | 🟡 caso reparado com `AE-114` a `AE-116`; classe sem guarda | pendência 3 |
| `AE-113` (`AE-119`) | o loop fictício despachou o card por arquivo, variante que o card não previa | 🟡 variante declarada no relatório e base da `R-02`; nenhuma regra manda o card de sondagem nomear variantes | pendência 3 |
| `AE-114` | binário novo sai sem a marca de arquivo novo (rodado: `'(arquivo binário ou não-UTF-8 — trecho omitido)'`) | 🔴 | `R-14`, pendência 2 |
| `AE-115` | resumo e lista por arquivo dão dois rótulos ao registro da condução (rodado acima) | 🔴 | `R-14`, pendência 2 |
| `AE-116` | a reconferência da versão pendente não cobre o campo Operação do modelo | 🔴 | `R-06`, pendência 2 |
| sem `AE` | duas linhas da telemetria com id de tarefa do plano fictício descartado, e a linha 1071 com o id deste plano depois do fechamento | 🔴 | `R-16`, pendência 6 |

Somatório: 0 🟢, 8 🟡, 11 🔴. Nenhum defeito da execução ficou com guarda mecânica; os 🔴 dependem
do plano sucessor.

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| 1 | veredito do dono no Marco 3 | a tabela de marcos do plano (`plano.md:15-19`) tem o Marco 3 `pendente` (`:19`): o dono julga o relatório e a entrega | o dono lê este documento e o relatório; com o go, `encerrar.py plano` fecha o plano | sim: o fechamento do plano e as pendências 4 e 5 |
| 2 | as 31 recomendações do relatório | aplicar fica fora deste plano (decisão `DAU-1`) | o plano sucessor, em autoria, com id `P-0755` (pasta `docs/plans/P-0755-recomendacoes-auditoria-final/`) | não bloqueia este plano; os 🔴 da tabela de defeitos seguem abertos até ele |
| 3 | achados com rota "plano sucessor" sem recomendação no relatório: `AE-107`, `AE-108`, `AE-111`, `AE-112`, a parte de regra do `AE-113`; e a mecanização da regra de contingência no `card_check.py` (fora de escopo, `plano.md:1029`) | o relatório fecha a cobertura pela §3 dele, e esses achados moram só na §9 do plano | o plano sucessor lê a §9 deste plano além do relatório | não; sem isso eles se perdem |
| 4 | trabalho não commitado | commit é ato do dono. `git status --porcelain=v1` → 22 entradas (17 modificados, 5 não rastreados), entre elas o relatório e a pasta deste plano | commit pelo dono | sim: plano ou propagação que parta do HEAD não vê nada deste plano |
| 5 | diretivas do diário apontam este plano | `docs/DIARIO_DE_OBRAS.md:2` vale "até o fechamento da auditoria final", e a diretiva de priorização (`:4`) aponta o `P-0754` | reescrita das duas no fechamento do plano | sim: diretiva velha já filtrou a fila inteira uma vez (registro 16 do relatório) |
| 6 | resíduo do plano fictício fora do git | `.claude/estado/tarefa-corrente.json` aponta `SA-T4` do plano fictício; o arquivo é ignorado pelo git (`.gitignore:11`), e a conferência da limpeza, feita por `git status`, não o vê. A série de telemetria tem `SA-T4-revisao` (97,4k) e `SA-T4-consultor-1` (110,1k) entre a linha `AUF-T15-revisao` e a `AUF-T16`, e nenhuma linha `AUF-T16-revisao`. Depois do fechamento da `AUF-T16`, a linha 1071 saiu com id `P-0754-planejador` (75,1k) sem card deste plano aberto — o mesmo defeito, ativo | `R-16` para a classe; correção das duas linhas e do arquivo por quem conduz | distorce a medida de consumo deste plano e o título do painel |
| 7 | medidas não tomadas | a série não mede a sessão principal: a `AUF-T16` tem `nao_medido`, e o loop das `AUF-T1` a `AUF-T15` só tem medida no relatório, pelo transcript. As linhas de batedor e planejador do mesmo dia com id `sem-id-scout`, `P-1-scout`, `P-0742-scout`, `P-0752-scout`, `P-0753-scout` e `P-0753-planejador` (linhas 1025-1034) não têm atribuição verificável a este plano | coluna de papel e atribuição corrigida na telemetria (`R-16`) | não |
| 8 | fato de inventário que não se reproduz | a §2.1 do plano registra para o `H-1` `conting[eê]ncia = 0` em `pantonic-planner.md`; contando em Python, sem distinguir maiúscula, o arquivo de `2513964` tem 12 linhas com `contingência`. O `grep -E 'conting[eê]ncia'` do Git Bash devolve 0 mesmo no arquivo de hoje, que tem 17 linhas com a palavra (mesma contagem): a classe de caractere acentuada não casa. A conclusão do `H-1` segue verdadeira — as duas regras não existiam (verificação da `AUF-T9`, antes `[0-0]`) | nota no plano sucessor; contagem de texto acentuado feita fora do `grep` com classe | não |

**Resumo do estado.** O plano entregou as 16 tarefas (`16 done`): 14 aprovadas com 100% e duas com
ressalva sanada no ato — `AUF-T2` (91%) e `AUF-T16` (90%), vereditos em `estado.tsv`. Os 21 herdados
têm destino: 15 fechados por mudança no kit, com teste ou regra escrita; 4 encerrados sem mudança,
com a prova na linha de origem; 2 medidos no relatório. A suíte passa de 505 para 521 testes, e o
relatório novo deixa 31 recomendações. Ficam 8 pendências; o veredito do dono no Marco 3 fecha a
primeira, e o commit, a quarta. Efeito fora do projeto: nenhum ainda — as regras novas do
planejador e da rubrica só chegam a `~/.claude` e aos projetos derivados pela projeção
(`materializar.py apply`) e pela propagação, atos fora deste plano (`plano.md:1030-1031`).
