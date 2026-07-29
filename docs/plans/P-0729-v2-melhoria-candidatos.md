# P-0729 — V2 / Estágio 3B: mudanças adotadas do benchmarking (candidatos ratificados)

**Iniciativa:** `PANTONIC-V2` — Estágio 3 de 4, **parte B** (a parte A, herdada do `P-0722`, é
`docs/plans/P-0729-v2-melhoria.md`).
**Origem:** `docs/plans/P-0729-v2-confronto.md` §2 `T6` — este plano **é** o entregável daquela
tarefa. Insumo único e fechado: `docs/benchmark/CANDIDATOS.md` (`V2C-T4`), com a linha
`Decisão do dono` de cada ficha preenchida em `V2C-T5` (2026-07-29, 15/15).

**Planejador:** Opus (2026-07-29, inline no orquestrador da `proximo-passo`).
**Executor por tarefa:** declarado em cada tarefa. Redação de doutrina em Opus; mecânica (script,
skill, configuração, movimentação de texto já decidida) em Sonnet.

**Estado:** `backlog` — desbloqueado no instante em que o `V2C-T6` fecha, junto com o Estágio 3A.
**Plano fechado (G-PLANREADY, 5 condições):** todas as 19 tarefas têm objetivo, arquivos-alvo com
caminho exato, método, verificação executável e critério de pronto; nenhuma questão em aberto;
nenhum bloco a preencher; nenhuma referência para frente. O checklist de fechamento está no rodapé.

**Checagem de versão do kit:** modo **hub** (existe `.claude/KIT_VERSION` e não existe
`.claude/kit/`) — este repositório é o canônico. `VERSION` = `.claude/KIT_VERSION` = `1.2.0`,
paridade OK. Sem divergência a reportar.

---

## 1. Cobertura: de cada `C-NN` ratificado para a(s) tarefa(s)

Regra de rastreabilidade herdada do `T6`: **nenhuma tarefa sem `C-NN` de origem** e nenhum `C-NN`
`adotar`/`adaptar` sem tarefa. Ideia nova do executor não entra — vira candidato de uma rodada
futura.

| `C-NN` | Decisão do dono | Tarefa(s) | I÷E |
|---|---|---|---|
| `C-01` Checador/gerador executável do kit | adotar | **T1**, **T2**, **T3** | 1,0 (1º por precedência) |
| `C-03` Tabela de precedência e residência | adotar | **T4** | 3,0 |
| `C-02` Allowlist de subcomandos destrutivos | adotar | **T5** | 3,0 |
| `C-04` Teto de contexto graduado | adotar | **T6** | 3,0 |
| `C-05` Checkpoint de contexto não planejado | adotar | **T7** | 3,0 |
| `C-06` `file:line` + comando no dossiê | adotar | **T8** | 2,0 |
| `C-07` Gatilho de revisão/deprecação da doutrina | adotar | **T9** | 2,0 |
| `C-10` Inbox de memória (fila + promoção pelo dono) | adaptar | **T10** | 2,0 |
| `C-08` Commits assinados + verificação no sync | adaptar | **T11** | 2,0 |
| `C-09` Registro de consumidores e versões | adotar | **T12** | 2,0 |
| `C-14` Compatibilidade por major kit × consumidor | adotar | **T13** | 1,0 (agrupado, ver §2) |
| `C-11` Piso de regressão comportamental (ratchet) | adotar | **T14**, **T15** | 1,5 |
| `C-12` Repatriar doutrina Pantonic do CLAUDE.md global | adotar | **T16**, **T17** | 1,5 |
| `C-13` Telemetria em série append-only | adotar | **T18**, **T19** | 1,0 |
| `C-15` Reversibilidade (snapshot paralelo) | **adiar** | *nenhuma, por decisão* — §4 | 0,5 |

**19 tarefas**, exatamente o esforço somado ratificado em `CANDIDATOS.md:20`. Os quatro candidatos
com E>1 são os que a regra (a) do `T6` obriga a dividir por fase de modelo: `C-01` (validador ·
gerador · doutrina+integração), `C-11` (doutrina · receita), `C-12` (decisão de residência ·
movimentação), `C-13` (formato · escrita nos pontos de fechamento).

## 2. Ordem de execução e entrelaçamento com o Estágio 3A

Os dois planos do Estágio 3 editam os mesmos arquivos (`GOVERNANCA.md`, três skills do kit), então a
ordem entre eles não é preferência — é prevenção de conflito de edição e de retrabalho. Ordem
parcial, decidida aqui (**DK-1**):

| Bloco | Tarefas | Por quê nesta posição |
|---|---|---|
| **A** | 3B `T1` → `T2` → `T3` → `T4` | `C-01` é **precondição** declarada (`CANDIDATOS.md` §2 e descarte 8: enforcement vira código antes de qualquer outra adição textual); `C-03` é a régua de residência de que `T6`, `T10`, `T16` e a 3A `V2M-T3` dependem |
| **B** | 3A `V2M-T1` → `V2M-T2` → `V2M-T3` → `V2M-T4` → `V2M-T5` | `V2M-T1` escreve `GOVERNANCA.md` §7 (13 guardrails) e o gate de publicação; tudo em 3B que encosta em §7 ou em G-EXECREADY vem depois. `V2M-T3` (promoção ao CLAUDE.md global) só depois do 3B `T4`, que é a régua que decide o que sobe e o que desce |
| **C** | 3B `T5` → `T6` → … → `T19` | resto, por dependência e, sem dependência, por I÷E |
| **D** | Estágio 4 (`P-0729-v2-documentacao`) | README espelho, bump `2.0.0`, **distribuição única** aos consumidores (`V2D-T4`) — inclui a prova de aceitação do ratchet (`T15`) no `PantonicVideo` |

Dependências internas ao Bloco C, todas satisfeitas pela ordem numérica: `T6` depende de `T4` e de
`V2M-T1`; `T7` depende de `T6` (a fração de gatilho é fração do teto da classe); `T8` depende de
`V2M-T1` (estende G-EXECREADY); `T9` depende do **Estágio 3A inteiro** `done` (a política de saída
de regra se institui na mesma rodada que adiciona cinco); `T10` depende de `T4`; `T15` depende de
`T14`; `T17` depende da ratificação do dono em `T16`; `T19` depende de `T18`.

**Quebra deliberada da ordem I÷E, registrada:** `T13` (`C-14`, I÷E 1,0) sobe para logo depois de
`T11`/`T12` em vez de ir para o fim, porque toca os mesmos dois arquivos (`.claude/sync-kit.ps1`
não, mas `GOVERNANCA.md` §10 e a família de skills de versão sim) — foi exatamente o motivo pelo
qual o dono divergiu da recomendação `adiar` em `V2C-T5`: *"o delta é barato e toca os mesmos
arquivos-alvo de `C-08`/`C-09`"*. As três formam o bloco contíguo da cadeia de distribuição.

## 3. Tarefas

### T1 — Validador estrutural do kit [Sonnet] — *`C-01` (a)*
- **Objetivo:** um script do hub que falha quando um artefato de extensão do kit está
  estruturalmente inválido.
- **Arquivos-alvo:** `.claude/checks/kit_check.ps1` (**novo**; a pasta `.claude/checks/` não existe
  — hoje `.claude/` tem só `KIT_VERSION`, `README.md`, `sync-kit.ps1`, `agents/`, `skills/`,
  `worktrees/`).
- **Método:** um script, dois modos (`-Mode validate` nesta tarefa; `generate`/`check-drift` na
  `T2`). O modo `validate` exige, para cada `.claude/agents/*.md`, frontmatter com `name` e
  `description`, e — quando presente — `tools:` sintaticamente válido; para cada
  `.claude/skills/*/SKILL.md`, frontmatter com `name`+`description` e `name` idêntico ao nome do
  diretório; e `VERSION` == `.claude/KIT_VERSION`. **Limite de escopo (risco registrado na ficha do
  `C-01`):** o validador **não** interpreta semântica de doutrina — o defeito que `BM-14§D9`
  documenta é exatamente esse. Os campos exigidos são derivados do estado vigente: o validador
  **não pode reprovar o kit atual**; campo ausente hoje em algum artefato nasce opcional, com
  comentário no script.
- **Verificação:** `pwsh .claude/checks/kit_check.ps1 -Mode validate` sai `0` sobre os **9** agentes
  e **8** skills em disco; sobre um artefato sintético sem `description` (criado e removido no
  scratchpad) sai `≠0` com mensagem que nomeia o arquivo.
- **Pronto quando:** as duas execuções acima conferem; nenhum artefato do kit foi alterado além do
  script novo; `pantonic-auditor-container.md`, `checar-versao-kit` e `proximo-passo` **não** foram
  tocados (a correção do README é da `T2`).

### T2 — Gerador do `.claude/README.md` e detecção de deriva [Sonnet] — *`C-01` (b)*
- **Objetivo:** o índice do kit deixa de ser mantido à mão e passa a ser derivado do disco, com o
  check falhando quando o versionado divergir do regenerado.
- **Arquivos-alvo:** `.claude/checks/kit_check.ps1` (modos `-Mode generate` e `-Mode check-drift`);
  `.claude/README.md` (regenerado).
- **Defeito medido em 2026-07-29 — é o alvo da tarefa, não hipótese:** a tabela de agentes
  (`.claude/README.md:12-19`) lista **8** linhas contra **9** arquivos em `.claude/agents/` —
  falta `pantonic-auditor-container`; a tabela de skills (`.claude/README.md:39-44`) lista **6**
  contra **8** diretórios em `.claude/skills/` — faltam `checar-versao-kit` e `proximo-passo`. É a
  anti-prática 1 do `BM-00`, ainda viva: o índice mente em silêncio.
- **Método:** as colunas geradas saem do frontmatter (`model`/`description`); a prosa autoral entre
  as tabelas é preservada por marcadores de região (`<!-- kit:agents:begin -->` …
  `<!-- kit:agents:end -->`, idem `kit:skills`), para o gerador nunca sobrescrever texto escrito à
  mão. Padrão copiado de `BM-15§D9` (regenera e falha se diferir) e `BM-07§D8`
  (`skill:validate`) — **não** de `BM-14§D9` (bloqueio por casamento de string).
- **Verificação:** após `-Mode generate`, o README tem 9 linhas de agente e 8 de skill;
  `-Mode check-drift` sai `0`; com um agente sintético a mais em `.claude/agents/`, `check-drift`
  sai `≠0` (e o sintético é removido em seguida). **Não deletar** `.claude/README.md` em nenhum
  momento — regenerar por sobrescrita das regiões.
- **Pronto quando:** versionado == regenerado; a deriva sintética é detectada; as duas tabelas
  conferem com o disco.

### T3 — Doutrina do enforcement executável e integração no gate [**Opus**] — *`C-01` (c)*
- **Objetivo:** declarar na doutrina que o índice do kit é artefato **derivado** e pendurar o check
  no gate que já roda ao fim de toda tarefa.
- **Arquivos-alvo:** `GOVERNANCA.md` §9 (Kit agêntico reusável, linha 220+);
  `.claude/skills/guardrails-check/SKILL.md` (entrada nova); `CHANGELOG.md` (abrir a seção
  `## [Não lançado]`); `VERSION` + `.claude/KIT_VERSION` → **`1.3.0`** (fechamento do Bloco A) e tag
  anotada `kit-v1.3.0`, **sem push**.
- **Conteúdo:** em §9, três frases — (1) `.claude/README.md` é derivado do disco e **não se edita à
  mão**; (2) o comando canônico é `pwsh .claude/checks/kit_check.ps1 -Mode validate` e
  `-Mode check-drift`; (3) o enforcement do kit é **código**, e regra do kit que não puder ser
  verificada por esse script nasce com o motivo escrito de por que não pode.
- **Verificação:** `guardrails-check` invoca os dois modos e ambos saem `0` no baseline; `VERSION`
  e `.claude/KIT_VERSION` com o mesmo valor (`GOVERNANCA.md` §10); `git tag --list kit-v1.3.0`
  retorna a tag.
- **Pronto quando:** §9 tem as três frases com o comando exato; a entrada existe no
  `guardrails-check`; bump com paridade + tag criada; `CHANGELOG.md` com a seção
  `## [Não lançado]` contendo as três primeiras entradas (`T1`, `T2`, `T3`).

### T4 — Tabela de precedência e residência da doutrina [**Opus**] — *`C-03`*
- **Objetivo:** declarar, em uma tabela, qual das quatro superfícies de doutrina vence quando duas
  colidem e que tipo de conteúdo mora em cada uma.
- **Arquivos-alvo:** `GOVERNANCA.md` §3 (Operações agênticas) — subseção nova ao final da seção,
  antes do §4. **Residência decidida (DK-2):** §3 e não §7, porque §7 são guardrails *de agente* e
  esta é a régua da própria doutrina; nenhum código.
- **Conteúdo:** as quatro superfícies — `~/.claude/CLAUDE.md` (global do dono) ·
  `GOVERNANCA.md`/`ARQUITETURA_PANTONICA.md` (versionados, viajam no kit) · skill · agente — com,
  para cada uma: que conteúdo mora, que conteúdo **não** mora, e quem vence no conflito. Duas regras
  explícitas: **específico vence geral**; **empate → versionado vence não-versionado** (um consumidor
  que recebe o kit por `git subtree` não recebe o que está fora do repo — o achado de `BM-00§D15`).
  Mais o **teste de residência** em quatro perguntas: vale para projeto não-Pantonic do dono? →
  global; é regra sempre-ativa do framework? → `GOVERNANCA.md`; é procedimento reexecutável com
  gatilho? → skill; é papel + fatos estáveis? → agente. A tabela **decide**; descrever a topologia
  atual sem decidi-la é o modo de falha registrado na ficha do `C-03`.
- **Verificação:** aplicar a tabela, no ato, aos três casos hoje em disputa e registrar o veredito
  de cada um na nota de execução: (1) orçamento de turnos por tarefa (`~/.claude/CLAUDE.md` Regra 7
  × `GOVERNANCA.md:67`), (2) telemetria de consumo medida (`BM-00§D12`), (3) governança de memória
  (`~/.claude/docs/GOVERNANCA_MEMORIAS.md`). Se a tabela não resolver os três sem ambiguidade, ela
  não está pronta.
- **Pronto quando:** a subseção existe em §3 com as quatro superfícies, as duas regras de
  precedência e o teste de residência; os três casos estão resolvidos por escrito; **nenhum texto
  foi movido** (mover é `T16`/`T17`).

### T5 — Allowlist de subcomandos destrutivos [Sonnet] — *`C-02`*
- **Objetivo:** negar, de forma declarativa, os subcomandos `git`/`gh` irreversíveis para os agentes
  que têm `Bash`.
- **Arquivos-alvo:** `.claude/settings.json` (**novo** — o hub não tem nenhum `settings*.json`
  hoje); `GOVERNANCA.md` §7 (guardrail nova, texto abaixo).
- **Fato medido em 2026-07-29:** o único agente do kit com `Bash` é o `pantonic-executor`, e por
  **omissão** — os outros 8 declaram `tools:` explícito sem `Bash`
  (`.claude/agents/pantonic-executor.md` não tem linha `tools:`). Por isso o controle vai em
  `settings.json` (`permissions.deny`, vale para todos) e não em frontmatter de agente: declarativo,
  sem parsing, o padrão de `BM-15§D13`.
- **Padrões a negar (fechados):** `Bash(git push --force*)`, `Bash(git push -f*)`,
  `Bash(git reset --hard*)`, `Bash(git branch -D*)`, `Bash(git clean -fdx*)`, `Bash(gh repo delete*)`.
- **Texto de doutrina a transcrever em §7 (redigido aqui — DK-3):**
  > **Comando destrutivo não é decisão de agente.** Reescrita de histórico, descarte de trabalho
  > não commitado e remoção de branch/repositório ficam negados em `.claude/settings.json`
  > (`permissions.deny`) para todo agente com `Bash`. O modo de falha correto é **ruidoso** —
  > comando negado, agente reporta ao dono — nunca silencioso. Ampliar a lista é rotina; encurtá-la
  > exige ato explícito do dono registrado no diário.
- **Verificação:** `Get-Content .claude/settings.json | ConvertFrom-Json` não lança;
  `git branch -D nao-existe-xyz` é **negado pela permissão** (o branch não existe, então a
  verificação é inócua se a negação falhar) e o retorno é registrado na nota de execução.
- **Pronto quando:** o JSON é válido e tem os 6 padrões; a tentativa acima é negada; §7 tem a
  guardrail transcrita **verbatim** do bloco acima.

### T6 — Teto de contexto graduado por classe de tarefa [**Opus**] — *`C-04`*
- **Objetivo:** substituir o teto único de ~40 tool uses por classes de tarefa com teto próprio.
- **Arquivos-alvo:** `GOVERNANCA.md` §3 — a linha **67** (`- **Orçamento de turnos por tarefa
  atômica**: ~≤40 tool uses esperado no agente de execução.`) é **substituída** pela tabela, não
  duplicada. Residência confirmada pela tabela da `T4`; zero código.
- **Classes e tetos (decididos aqui — DK-4, calibrados pela série medida do próprio diário, não por
  estimativa):** mecânica/pontual **≤15** · implementação padrão **≤40** · comportamental
  multi-camada (muda contrato ou fluxo; ciclo editar-rodar-depurar) **≤60, com teto numérico por
  ramo obrigatório no dossiê** · investigação/mapeamento **sem default: o teto é prescrito no
  dossiê junto do método de sondagem** · redação de doutrina/planejamento **≤25**.
- **Regra anti-desculpa (obrigatória no texto, é o efeito colateral registrado na ficha):** a classe
  é escolhida **no dossiê, antes de delegar**, e fica registrada; estourar o teto da classe é sinal
  de decomposição errada — **replanejar, não continuar**; classe generosa escolhida depois do
  estouro é falsificação da série.
- **Verificação:** aplicar as classes retroativamente às tarefas com linha `Consumo:` já registrada
  nos diários deste repo (`Select-String -Path docs\DIARIO_DE_OBRAS.md -Pattern 'Consumo:'` →
  14 ocorrências em 2026-07-29) e conferir que nenhuma classe fica com mais de 1/3 das suas tarefas
  estourando. Se ficar, o número está errado — e a série manda, não a estimativa.
- **Pronto quando:** a tabela está em §3; a linha 67 antiga não coexiste com ela; a aplicação
  retroativa está registrada na nota de execução; executada **depois** de `V2M-T1` (que edita §7) e
  da `T4`.

### T7 — Checkpoint intermediário para perda de contexto não planejada [**Opus**] — *`C-05`*
- **Objetivo:** um procedimento que preserve a descoberta já paga quando o contexto acaba **sem
  plano**, em vez de reexecutá-la no contexto seguinte.
- **Arquivos-alvo:** `.claude/skills/handover/SKILL.md` (seção nova "Checkpoint intermediário");
  `GOVERNANCA.md` §4.3 (Execução em contexto limpo, linha 118+) — uma linha de ponteiro. Nenhuma
  infraestrutura nova.
- **Conteúdo:** **gatilho** = o consumo cruza **2/3 do teto da classe** (`T6`), ou o executor
  conclui que vai estourar. **Entregável** = até 5 linhas no diário: o que já está descoberto e
  decidido · o que falta · arquivos tocados (com `caminho:linha`) · o próximo passo exato · o que
  **não** precisa ser refeito. **Teto do próprio checkpoint = 2 tool uses** (um `Grep` de âncora +
  um `Edit`): o checkpoint tem de custar menos que a descoberta que preserva — é o risco registrado
  na ficha do `C-05`.
- **Verificação:** aplicar o formato ao caso real já documentado na `proximo-passo` (queda de
  subagente sem bloco `<usage>`) e confirmar que o checkpoint resultante cabe nas 5 linhas.
- **Pronto quando:** a seção existe com gatilho, entregável e teto; §4.3 aponta para ela; o texto
  diz explicitamente que o checkpoint é ponteiro de estado, **não** relatório intermediário.

### T8 — `file:line` e comando de validação no dossiê da tarefa [Sonnet] — *`C-06`*
- **Objetivo:** os campos hoje em prosa do dossiê ("arquivos-alvo", "testes") passam a exigir
  ponteiro `caminho:linha` e o **comando** de validação, colado.
- **Arquivos-alvo:** `.claude/skills/diario-de-obras/SKILL.md` (template de tarefa atômica);
  `.claude/skills/handover/SKILL.md` (campo correspondente no fechamento);
  `GOVERNANCA.md` §4.2 (Diário de obras, linha 95+) — uma linha, texto abaixo.
- **Texto a transcrever em §4.2 (redigido aqui — DK-3):**
  > **Dossiê de tarefa aponta e verifica.** "Arquivos-alvo" carrega `caminho:linha`; "Verificação"
  > carrega o **comando**, copiado do terminal, não a intenção de verificar. `caminho:linha` é
  > ponteiro de leitura — envelhece e **não** se mantém; tratá-lo como contrato custa mais do que
  > entrega.
- **Método:** padrão operacional de `BM-20§D5` (cada passo com `file:line`, comando e artefato
  esperado). A matriz formal de rastreabilidade fica **fora** (descarte 1 do `CANDIDATOS.md`).
- **Verificação:** as 19 tarefas **deste plano** satisfazem o template novo — se não satisfizerem, o
  template está exigindo o que o planejador não consegue produzir e é o template que muda.
- **Pronto quando:** os dois templates têm os campos; §4.2 tem o texto acima; a verificação está
  registrada. Executada **depois** de `V2M-T1` (que escreve G-EXECREADY).

### T9 — Gatilho de revisão e deprecação da própria doutrina [**Opus**] — *`C-07`*
- **Objetivo:** instituir o caminho de **saída** de uma regra — hoje nenhuma regra jamais saiu do
  framework.
- **Arquivos-alvo:** `GOVERNANCA.md` §7 (política, ao final da seção);
  `.claude/skills/checar-versao-kit/SKILL.md` (gatilho).
- **Conteúdo e decisão do gatilho (DK-5):** o gatilho **pendura-se em algo que já roda** — o
  fechamento de uma versão MINOR do kit — e nunca em calendário (risco de cerimônia, registrado na
  ficha). Escopo de cada revisão: só as guardrails com **≥2 MINORs** de idade. Pergunta única:
  *"esta regra mudou algum comportamento nos últimos 2 MINORs? cite o caso."* Sem caso citável →
  marcação `OBSOLETA desde <versão>`, período de transição de **um MINOR**, remoção no seguinte.
- **Verificação:** aplicar a pergunta, no ato, às guardrails de §7 já existentes (13 após
  `V2M-T1`) e registrar o resultado. **Nenhuma removida agora é resultado aceitável; não registrar
  não é.**
- **Pronto quando:** a política está em §7 com gatilho, escopo, pergunta e prazo; a
  `checar-versao-kit` dispara a revisão no fechamento de MINOR; a primeira aplicação está
  registrada. Executada **depois do Estágio 3A inteiro** `done`.

### T10 — Inbox de memória: separar descobrir de aprovar [**Opus**] — *`C-10` (adaptar)*
- **Objetivo:** candidato a memória entra numa fila e só é promovido a memória por ato do dono.
- **Residência decidida (DK-6):** **global**, não no repo — memória por projeto existe em projeto
  não-Pantonic do dono, e o teste de residência da `T4` manda o que vale fora da família para o
  global. O repo recebe só um ponteiro.
- **Arquivos-alvo:** `~/.claude/docs/GOVERNANCA_MEMORIAS.md` (seção nova "Fila de candidatos");
  `~/.claude/CLAUDE.md` Regra 6 (uma linha apontando a seção);
  `.claude/skills/proximo-passo/SKILL.md` (passo 1 passa a drenar **dois** inboxes);
  `GOVERNANCA.md` §3 (uma linha de ponteiro).
- **Método:** candidato vira linha em `<memory-dir>/_INBOX.md` (append-only, mesma forma de
  `docs/plans/_INBOX.md`); **só o dono promove**; o agente nunca grava direto em memória — a única
  exceção é a que a Regra 6 já obriga (remover ponteiro quebrado na hora). Drenagem no mesmo ato em
  que a `proximo-passo` drena o inbox de planos — é a mitigação do risco registrado na ficha (fila
  sem hábito de drenagem acumula e o agente volta a gravar direto). **Fora do escopo:** a análise
  automática de transcrições de `BM-08§D7` (motivo da decisão `adaptar` do dono).
- **Verificação:** `<memory-dir>/_INBOX.md` existe no PantonicApp (pode nascer vazio, com
  cabeçalho); a `proximo-passo` cita a drenagem dos dois inboxes no passo 1; nenhum caminho do
  procedimento promove memória sem ato do dono — conferido por leitura do texto novo.
- **Pronto quando:** os quatro arquivos-alvo estão consistentes e a exceção do ponteiro quebrado
  está escrita. Executada **depois** da `T4`.

### T11 — Commits assinados no branch de distribuição, versão mínima [Sonnet] — *`C-08` (adaptar)*
- **Objetivo:** o consumidor verifica a origem do que vai executar antes de aplicar o kit.
- **Arquivos-alvo:** `.claude/sync-kit.ps1`; `GOVERNANCA.md` §10 (uma linha, texto abaixo).
- **Estado medido em 2026-07-29:** o branch `kit` existe localmente; `git config --get
  user.signingkey` está **vazio** — ou seja, o ramo vigente é o **B** abaixo. A tarefa reconfirma com
  o mesmo comando (1 verificação barata) antes de escolher o ramo.
- **Dois ramos, com critério de parada explícito:**
  - **Ramo A — chave configurada:** o `sync-kit.ps1` verifica a assinatura do commit de origem
    (`git verify-commit` / `git log --show-signature`) e **aborta** o sync com mensagem acionável se
    faltar. PARE ao ter os dois casos (assinado passa / não assinado aborta) verificados.
  - **Ramo B — chave ausente (estado atual):** implementar a mesma verificação em modo **aviso**
    (`WARN` + prossegue), com o modo bloqueante já escrito atrás de um parâmetro
    (`-RequireSignature`). PARE em seguida e **reporte ao dono** o passo de configuração da chave —
    credencial é do dono; o executor **não** cria nem configura chave de assinatura.
- **Texto a transcrever em §10 (redigido aqui — DK-3):**
  > **O que se distribui, executa.** Agentes e skills são instruções que rodam com as ferramentas
  > que o frontmatter concede; um artefato adulterado no hub vira execução em todo consumidor. O
  > passo de sync verifica a assinatura do commit de origem antes de aplicar. **Fora de escopo,
  > registrado:** varredura de conteúdo artefato por artefato — custo alto, e o corpus inteiro a
  > deixa em aberto.
- **Verificação:** no ramo vigente, um commit **não** assinado no branch `kit` produz o
  comportamento declarado (aborta no A, `WARN` no B) — testado sobre uma cópia do repo no
  scratchpad, **sem** apagar nem reescrever nada no repo real.
- **Pronto quando:** o script tem a verificação e o parâmetro; o caso sintético confere; §10 tem o
  texto acima; no ramo B, o passo do dono está reportado no handover.

### T12 — Registro de consumidores e versões instaladas [Sonnet] — *`C-09`*
- **Objetivo:** responder "quais consumidores ainda não receberam a guardrail X" sem abrir cada
  repositório.
- **Arquivos-alvo:** `docs/CONSUMIDORES.md` (**novo**); `.claude/sync-kit.ps1` (escrita
  automática); `GOVERNANCA.md` §10 (uma linha).
- **Método:** colunas — consumidor (caminho ou repo) · versão instalada · data do último sync ·
  modo (`subtree`/cópia). Quem escreve é o **`sync-kit.ps1`**, no mesmo passo que aplica a versão:
  registro mantido à mão recria o defeito do `.claude/README.md` (mente em silêncio), que é o
  risco escrito na ficha. **Semente:** o roster de consumidores é fato volátil com dona única (a
  memória `kit-pantonic-propagacao`); a tarefa semeia a partir dela e do disco e marca cada linha
  como `semeada — não verificada por sync` até o primeiro sync real sobrescrevê-la.
- **Verificação:** executar o `sync-kit.ps1` sobre uma cópia sandbox no scratchpad e conferir que a
  linha do consumidor foi escrita/atualizada com versão e data; **não deletar** nenhum artefato de
  saída existente.
- **Pronto quando:** o arquivo existe com as 4 colunas; o script escreve; §10 declara que o
  registro é derivado do sync; as linhas semeadas estão marcadas como tal.

### T13 — Compatibilidade por major entre kit e consumidor [Sonnet] — *`C-14`*
- **Objetivo:** divergência de **MAJOR** entre kit e consumidor deixa de ser tratada como
  divergência comum.
- **Arquivos-alvo:** `.claude/skills/checar-versao-kit/SKILL.md`; `GOVERNANCA.md` §10 (uma linha).
- **Método:** padrão de `BM-19§D10` (CLI v1.x consome só templates v1.x.x): consumidor com kit
  `M.x` consome doutrina `M.x`. Três casos distinguidos na saída da skill — igual (silêncio) ·
  MINOR/PATCH divergente (reportar, como hoje) · **MAJOR divergente (reportar como incompatível e
  parar)**. A regra do §10a é preservada intacta: o agente **reporta, nunca atualiza** — o update
  segue sendo decisão humana obrigatória, que é o ponto em que o Pantonic supera todo o corpus.
- **Verificação:** no scratchpad, um `.claude/kit/KIT_VERSION` sintético com MAJOR diferente produz
  a mensagem de incompatibilidade; com MINOR diferente, a mensagem antiga; igual, silêncio.
- **Pronto quando:** os três casos estão descritos na skill e distinguidos na saída; §10 declara a
  regra de major; nenhuma automação de update foi introduzida.

### T14 — Doutrina do piso de regressão comportamental [**Opus**] — *`C-11` (a)*
- **Objetivo:** fixar o piso de regressão como conjunto de **comportamentos trancados**, nunca como
  percentual de cobertura.
- **Arquivos-alvo:** `GOVERNANCA.md` §4.4 (TDD obrigatório, linha 130+).
- **Vínculo bloqueante herdado da ratificação (`V2C-T5`) e do descarte 5:** o piso é
  **comportamental**; percentual de cobertura como piso cria incentivo a manter teste de código
  morto para não derrubar a métrica — o que **contradiria** `G-DEADCODE`. Redigido como
  comportamental, **reforça** `G-DEADCODE`.
- **Conteúdo:** o texto tem de responder a três perguntas, explicitamente: como o piso se mede (lista
  versionada de comportamentos trancados por TF+TR) · como se prova que não desceu (comando, ver
  `T15`) · o que fazer quando um comportamento é **intencionalmente** removido (ato explícito do
  dono registrado no diário — remover do piso é decisão, não efeito colateral).
- **Verificação:** as palavras "percentual" e "cobertura" aparecem em §4.4 **apenas** na forma
  negativa; há referência cruzada explícita a `G-DEADCODE` (§7, escrita em `V2M-T1`).
- **Pronto quando:** §4.4 responde às três perguntas; o vínculo com `G-DEADCODE` está escrito; o
  hub continua sem `tests/` (não há código a testar aqui — a adoção é do consumidor).

### T15 — Receita executável de ratchet do piso [Sonnet] — *`C-11` (b)*
- **Objetivo:** dar ao consumidor um comando que falha quando um comportamento sai do piso.
- **Arquivos-alvo:** `.claude/checks/ratchet_piso.py` (**novo** — referência que roda **no
  consumidor**, cujo runtime é Python); entrada em `.claude/skills/guardrails-check/SKILL.md`.
- **Método:** o consumidor versiona `tests/piso_comportamental.txt`, uma linha por comportamento
  trancado no formato `<pytest nodeid> — <comportamento em uma frase>`. O check compara essa lista
  com `pytest --collect-only -q` e **falha** quando um nodeid do piso desapareceu da coleta.
  Cobertura percentual não entra em nenhum ponto (`T14`).
- **Verificação:** dois casos sintéticos no scratchpad — baseline com a lista casando a coleta
  (passa) e uma linha do piso apontando para nodeid inexistente (falha, nomeando o comportamento
  perdido). A prova no consumidor real (`PantonicVideo`) pertence ao `V2D-T4`, não a esta tarefa.
- **Pronto quando:** o script e o formato do arquivo de piso existem; `guardrails-check` o invoca;
  os dois casos sintéticos conferem.
- **Decisão de forma (DK-7):** **dois scripts, não um** — este e o `dead_code.py` da `V2M-T5` têm
  alvos diferentes (código do consumidor × ambos rodam lá, mas gates distintos) e o `kit_check.ps1`
  da `T1` valida o **kit do hub**. Um único script acoplaria o gate do hub ao runtime Python do
  consumidor; os três são invocados pelo mesmo lugar (`guardrails-check`), que é onde a unificação
  tem valor.

### T16 — Decisão de residência item a item da doutrina global [**Opus** + ato do dono] — *`C-12` (a)*
- **Objetivo:** produzir, sob a régua da `T4`, a tabela item a item do que **desce** do
  `~/.claude/CLAUDE.md` para `GOVERNANCA.md` — e ratificá-la com o dono.
- **Arquivos-alvo:** `docs/RESIDENCIA_DOUTRINA.md` (**novo**). **Nenhum texto é movido aqui.**
- **Método:** inventariar as 7 Regras do `~/.claude/CLAUDE.md` e os blocos que o `BM-00` cita como
  diferenciais do framework que **não viajam no kit** (`~/.claude/CLAUDE.md:30,107` — orçamento de
  contexto e telemetria de consumo); classificar cada item em `global` / `Pantonic` / `dividir`,
  citando a linha da régua da `T4` que produziu a classificação; apresentar ao dono em **1
  round-trip** (blocos, não item a item — o método da `V2C-T5`). A decisão do dono é **obrigatória**
  (`RELATORIO_CONSOLIDADO.md:480`).
- **Verificação:** nenhum item do CLAUDE.md global fica sem classificação; toda classificação cita a
  regra que a produziu; a divergência com a `V2M-T3` (que **sobe** G-PLANFIDELITY/G-EXECREADY) é
  checada explicitamente — subida e descida usam a mesma régua e não podem se cruzar.
- **Pronto quando:** a tabela está 100% classificada e a ratificação do dono está registrada nela.

### T17 — Mover o texto e corrigir os ponteiros [Sonnet] — *`C-12` (b)*
- **Objetivo:** executar exatamente a tabela ratificada na `T16`, sem acrescentar nem omitir item.
- **Arquivos-alvo:** `~/.claude/CLAUDE.md` (remoção do que desceu); `GOVERNANCA.md` (recebimento, na
  seção que a régua indicar); os ponteiros que citam as regras movidas em `.claude/skills/*/SKILL.md`
  e `.claude/agents/*.md` (localizar com `Select-String -Pattern 'CLAUDE\.md|Regra \d'` **antes** de
  editar); `CHANGELOG.md`; `VERSION` + `.claude/KIT_VERSION`.
- **Guardrail de escopo (risco médio-alto registrado na ficha):** o arquivo está **fora do repo** e
  vale para projetos não-Pantonic do dono — erro aqui altera todas as sessões. Copiar
  `~/.claude/CLAUDE.md` para o scratchpad antes de editar; mover **só** o que a tabela marcou; não
  desfazer o que a `V2M-T3` subiu.
- **Verificação:** para cada item movido, um `Select-String` mostra **uma** residência e não duas
  (duplicação = divergência futura, o custo que `BM-01§D15` mede); nenhum ponteiro quebrado; o
  `~/.claude/CLAUDE.md` continua dentro do teto declarado de 200 linhas.
- **Pronto quando:** os greps de duplicidade voltam vazios; os ponteiros estão atualizados; o
  `CHANGELOG.md` registra o que passou a viajar no kit.

### T18 — Formato e arquivo da série de telemetria [Sonnet] — *`C-13` (a)*
- **Objetivo:** a série de consumo deixa de ser prosa no diário e passa a ser linha estruturada
  append-only, agregável sem leitura humana.
- **Arquivos-alvo:** `docs/telemetria.tsv` (**novo**, com cabeçalho); `GOVERNANCA.md` §4.2 (uma
  linha: a série é a fonte, o diário aponta).
- **Formato decidido (DK-8):** TSV append-only, colunas
  `data ⇥ projeto ⇥ tarefa ⇥ modelo ⇥ tool_uses ⇥ tokens_k ⇥ duracao_s ⇥ fonte`, com
  `fonte ∈ {usage, contado, nao_medido}`. A coluna `fonte` é obrigatória: distinguir **medido** de
  **autorrelatado** é o que nenhum dos 21 frameworks do corpus faz (`D12` é `+` em 3 de 21) e é
  precisamente o diferencial a preservar. TSV e não JSONL: agregável por
  `Import-Csv -Delimiter "\`t"` sem escrever parser.
- **Semente:** importar as linhas `Consumo:` já registradas em `docs/DIARIO_DE_OBRAS.md`
  (`Select-String -Pattern 'Consumo:'` → 14 ocorrências em 2026-07-29; re-derivar a contagem no
  momento da execução), cada uma com a `fonte` correta — a série **não** nasce vazia, e os 5
  estouros deixam de ser prosa repetida (anti-prática 3 do `BM-00`).
- **Verificação:** `Import-Csv docs\telemetria.tsv -Delimiter "\`t"` lê sem erro; a contagem de
  linhas de dado é igual à contagem de `Consumo:` importáveis; nenhuma linha com `fonte` vazia.
- **Pronto quando:** arquivo, cabeçalho e semente existem; §4.2 declara a série como fonte.

### T19 — Escrita da série nos dois pontos de fechamento [Sonnet] — *`C-13` (b)*
- **Objetivo:** a série passa a ser escrita por quem já redige a linha `Consumo:`, e o diário passa
  a apontar em vez de copiar.
- **Arquivos-alvo:** `.claude/skills/handover/SKILL.md:29` (a linha que hoje exige
  `Consumo: <N> tool uses, ~<X>k tokens, <modelo>, <duração>`);
  `.claude/skills/proximo-passo/SKILL.md` (passo 5, "Telemetria pós-notificação");
  `CHANGELOG.md`; `VERSION` + `.claude/KIT_VERSION` → **`1.4.0`** (fechamento do Bloco C) e tag
  anotada `kit-v1.4.0`, **sem push**.
- **Conteúdo:** os dois pontos passam a **apender uma linha** em `docs/telemetria.tsv` com a `fonte`
  correta; a linha do diário passa a ser **ponteiro** (`Consumo: ver docs/telemetria.tsv`), nunca
  cópia — duplicar a série recria o problema de duas fontes, que é o risco escrito na ficha do
  `C-13`. A regra de que a medida vem do bloco `<usage>` e nunca do autorrelato do subagente
  permanece **inalterada**.
- **Verificação:** o fechamento **desta** tarefa é feito pelo procedimento novo — a linha da `T19`
  entra na série e o diário só aponta. `VERSION` == `.claude/KIT_VERSION`;
  `git tag --list kit-v1.4.0` retorna a tag.
- **Pronto quando:** os dois pontos escrevem na série; o diário aponta; bump com paridade + tag;
  `CHANGELOG.md` fecha a seção `[Não lançado]` como `1.4.0`.

## 4. O que este plano deliberadamente não faz

Registrado para que a ausência seja legível como decisão.

1. **`C-15` (reversibilidade por snapshot paralelo) não gera tarefa** — `adiar` decidido pelo dono
   em 2026-07-29: maior custo da lista (4+ tarefas; ~40h no desenho de referência do `BM-10`), risco
   alto e colisão com a própria premissa de custo por turno (D6). Permanece em `CANDIDATOS.md` para
   reavaliação futura. Se o dono quiser tratá-lo, o caminho é uma **tarefa de investigação** com
   teto de sondagem — não uma tarefa de implementação, e não deste plano.
2. **Os escopos amputados dos dois `adaptar`** — de `C-08`, a varredura de conteúdo artefato por
   artefato (custo alto, o corpus inteiro a deixa em aberto); de `C-10`, a análise automática de
   transcrições de `BM-08§D7` (exigiria infraestrutura fora do escopo do hub). Ambos ficam
   declarados no texto que as tarefas `T11` e `T10` escrevem, para que a versão mínima não seja lida
   como a versão completa.
3. **Os 8 descartes justificados** do `RELATORIO_CONSOLIDADO.md` e o `REJEITAR` de D2 (publicação
   pública do hub) — motivo em `CANDIDATOS.md` §4. Dois deles são o **limite** deste plano: o
   descarte 5 restringe a forma da `T14` (piso comportamental, nunca percentual) e o descarte 8 fixa
   a precedência do Bloco A (enforcement vira código antes de qualquer adição textual).
4. **Nenhuma guardrail do `P-0722` é revogada ou reescrita aqui.** O Estágio 2 podia **acrescentar**,
   nunca revogar; a única tensão encontrada (`C-11` × `G-DEADCODE`) é resolvida por redação na
   `T14`, não por revisão da guardrail.
5. **Nenhuma distribuição aos consumidores.** Acontece uma vez, no fechamento da iniciativa
   (`P-0729-v2-documentacao` `V2D-T4`), junto do bump `2.0.0` e da nota de migração — `DM-6` do
   Estágio 3A.

## 5. Riscos

- **Doutrina crescer além do que se lê.** `GOVERNANCA.md` tem 268 linhas; o Estágio 3A a leva além
  de 300 e este plano acrescenta 6 blocos de texto (`T3`, `T4`, `T5`, `T6`, `T7`, `T9`, `T14`).
  Mitigação estrutural: a `T9` (`C-07`) é o **contrapeso** — institui a saída de regra na mesma
  rodada que mais adiciona, e sua primeira aplicação é obrigatória e registrada.
- **Enforcement executável validando trivialidade** (viés 2 do corpus: documentação não é prática).
  Mitigação: a `T2` nasce apontada para um defeito **medido e vivo** (8/9 agentes, 6/8 skills no
  índice), não para a forma pela forma; a `T1` tem limite de escopo escrito.
- **A tabela de residência (`T4`) descrever em vez de decidir.** Mitigação: a verificação exige
  resolver, no ato, os três casos hoje em disputa — uma tabela que não os resolva reprova.
- **Mexer em arquivo fora do repo (`T17`).** Altera todas as sessões do dono, inclusive de projetos
  não-Pantonic. Mitigação: `T16` separa decidir de mover, com ratificação do dono no meio; cópia de
  segurança antes de editar; greps de duplicidade como critério de pronto.
- **Bloquear o único caminho de distribuição (`T11`).** Verificação de assinatura mal configurada
  trava o sync. Mitigação: o ramo vigente medido é o de **aviso**, com o modo bloqueante atrás de
  parâmetro; configurar credencial é ato do dono, nunca do executor.
- **Duas fontes de telemetria (`T18`/`T19`).** Mitigação: a linha do diário vira **ponteiro** no
  mesmo passe em que a série começa a ser escrita — as duas tarefas são adjacentes de propósito.
- **Conflito de edição com o Estágio 3A.** Cinco tarefas deste plano editam `GOVERNANCA.md` §3/§7,
  que a `V2M-T1` reescreve. Mitigação: a ordem parcial de §2 é normativa, não sugestão — Bloco B
  inteiro antes do Bloco C, exceto o que §2 nomeia.

## 6. Decisões (fechadas no planejamento)

| id | Decisão | Valor | Motivo |
|---|---|---|---|
| **DK-1** | Ordem entre 3A e 3B | Blocos A (3B `T1`-`T4`) → B (3A inteiro) → C (3B `T5`-`T19`) → D (Estágio 4) | `C-01` é precondição declarada e `C-03` é a régua de que a própria `V2M-T3` depende; o resto evita conflito de edição em `GOVERNANCA.md` §3/§7 |
| **DK-2** | Residência da tabela de precedência (`C-03`) | `GOVERNANCA.md` **§3**, não §7 | §7 são guardrails *de agente*; esta é a régua da própria doutrina |
| **DK-3** | Doutrina em tarefa mecânica | Quando uma tarefa [Sonnet] encosta em uma linha de doutrina, **o texto é redigido neste plano** e a tarefa apenas o transcreve verbatim | Honra a regra (a) do `V2C-T6` (doutrina e mecânica são fases de modelo diferentes) sem inflar 14 candidatos em 27 tarefas; é o mesmo padrão com que o Estágio 3A absorveu o `P-0722` |
| **DK-4** | Classes e tetos de contexto (`C-04`) | 15 / 40 / 60 / prescrito / 25, com a classe escolhida **antes** de delegar | Calibrado pela série medida do próprio diário (14 linhas `Consumo:`), não por estimativa; a verificação retroativa da `T6` pode corrigir os números, e aí manda a série |
| **DK-5** | Gatilho de deprecação (`C-07`) | Fechamento de versão **MINOR** do kit; escopo = guardrails com ≥2 MINORs; transição de 1 MINOR | Pendurar em algo que já roda, nunca em calendário — o risco de cerimônia está escrito na ficha |
| **DK-6** | Residência do inbox de memória (`C-10`) | **Global** (`~/.claude/docs/GOVERNANCA_MEMORIAS.md`); o repo recebe ponteiro; fila em `<memory-dir>/_INBOX.md` | Memória por projeto existe em projeto não-Pantonic do dono — o teste de residência da `T4` manda para o global |
| **DK-7** | `kit_check.ps1` × `ratchet_piso.py` × `dead_code.py` (`V2M-T5`) | **Três scripts**, um único ponto de invocação (`guardrails-check`) | Alvos e runtimes diferentes (kit do hub em PowerShell × código do consumidor em Python); unificar acoplaria o gate do hub ao runtime do consumidor. Fecha a pergunta deixada aberta na ficha do `C-01` |
| **DK-8** | Formato da série de telemetria (`C-13`) | TSV append-only com coluna obrigatória `fonte ∈ {usage, contado, nao_medido}`; semente das 14 linhas já registradas | TSV agrega com `Import-Csv` sem parser; a coluna `fonte` preserva a distinção medido×autorrelato, que nenhum framework do corpus faz |
| **DK-9** | Bump de versão | **Dois** bumps MINOR: `1.3.0` no fim do Bloco A (`T3`) e `1.4.0` no fim do Bloco C (`T19`); as demais tarefas apendam ao `## [Não lançado]` do `CHANGELOG.md` | 19 tags para uma iniciativa que fecha em `2.0.0` no Estágio 4 seria ruído; a rastreabilidade fica no `[Não lançado]` |
| **DK-10** | `C-04` esperar a série de `C-13`? | **Não** — `T6` vem antes de `T18` | A série histórica já existe medida no diário (14 linhas, 5 estouros); esperar a série nova custaria dezenas de tarefas para calibrar o que o dado atual já calibra |
| **DK-11** | Posição de `C-14` na ordem I÷E | Sobe para `T13`, contíguo a `C-08`/`C-09` | Motivo dado pelo próprio dono ao divergir da recomendação `adiar` em `V2C-T5`: custo marginal menor na mesma rodada, arquivos-alvo compartilhados |

---

## Checklist de fechamento (G-PLANREADY, 5 condições)

1. **Nomenclatura** — `P-0729-v2-melhoria-candidatos.md`, o nome que o `V2C-T6` e o índice do diário
   já reservaram para o Estágio 3B (`P-0729-V2K`). Contador `P-NNNN` fica *grandfathered* até a
   `V2M-T4` instituí-lo.
2. **`T1..T19` sequenciais** — sem lacuna e sem letra: as subdivisões dos quatro candidatos com E>1
   são tarefas numeradas, não itens `a`/`b` dentro de uma tarefa.
3. **Todas as decisões tomadas** — 11 decisões `DK-*` registradas; as 15 decisões do dono vêm
   ratificadas de `V2C-T5`; os dois pontos que exigem ato do dono (`T11` ramo B: chave de
   assinatura; `T16`: tabela de residência) são **tarefas com entregável e critério de pronto**, não
   questões em aberto — o executor sabe exatamente onde parar e o que reportar.
4. **Linear, sem referência para frente** — toda dependência de uma tarefa aponta para tarefa de
   número menor, para o Estágio 3A (Bloco B) ou para o Estágio 4; §2 declara a ordem parcial.
5. **Nenhum bloco em aberto** — nenhuma tarefa cujo conteúdo dependa de artefato inexistente:
   os 5 arquivos novos (`kit_check.ps1`, `ratchet_piso.py`, `docs/CONSUMIDORES.md`,
   `docs/telemetria.tsv`, `docs/RESIDENCIA_DOUTRINA.md`) são criados pelas próprias tarefas que os
   consomem, na ordem declarada.

**`V2C-T6` — Estágio 2 de `PANTONIC-V2`, última tarefa. 19 tarefas, 14 candidatos ratificados
cobertos, 1 adiado com motivo, nenhuma tarefa sem `C-NN` de origem.**
