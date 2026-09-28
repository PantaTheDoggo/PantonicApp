# P-0749 — Saneamento de artefatos: pasta por plano, máquina em TSV, humano mínimo

**Data:** 2026-09-24 · **Origem:** pedido do dono (§0) · **Status:** `done` · 2026-09-25 · **aceito pelo dono no fechamento**, verbatim: *"conclua o plano
atual 749"* (10/10 tarefas `done`; veredito sobre as trocas `M1`..`M6` incluso; validação em
`docs/OPERACOES_AS_IS_P-0749.md`). Antes: Marco 1 com `go` do dono (*"pode marcar como aceito"*) · **Prefixo das tarefas no diário:** `SAN-T<n>` · **Prefixo das decisões:**
`DSA-<n>` · **Forma:** legado (arquivo único, id de 4 dígitos — `DSA-15`).
**Ordem de execução:** SAN-T1 → SAN-T2 → SAN-T3 → SAN-T3a → SAN-T4 → SAN-T2a → SAN-T5 → SAN-T6 → SAN-T6a → SAN-T6b

## 0. O problema, verbatim

> Crie um novo plano de saneamento de arquivos.
> Aqui está um amontoado de artefatos. E artefatos muitos verbosos de planejamento e execução.
> Preciso de artefatos únicos "de máquina", que podem ser rastreados pelas funções de captura de texto sem leitura.
> Preciso de artefatos de planejamentos concisos, respeitando toda a disciplina já traçada hoje.
> Para cada plano, preciso que seja criada uma nova pasta e seja inserida ali os artefatos pertinentes.
> O código dos artefatos P-XXX devem ser numerados a partir do 0. Essa numeração 0748 para mim smente confunde.
> Faça esse plano visando enxugar o que temos de planejamento hoje, e melhoramento na geração de arquvios.
> Adicione também a regra que todo artefato "de humano" (o que não for "de máquina") deve ser os menores possíveis

Rodada respondida (2026-09-24): renumerar os existentes? *"Considerar este plano já como legado. Essa
diretiva deverá valer para os projetos que herdarem o kit"*. Enxugar ou mover os existentes? *"Mesma
resposta do anterior"*. Processo: *"Protocolo completo"*.

**Pronto quando:** o kit institui, para plano novo, pasta própria `P-<n>` com os artefatos dele,
estado de máquina em TSV de residência única, a regra do artefato de humano mínimo, e instrumentos
que leem e geram o layout novo sem mudar a leitura do legado do hub.

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-24 · autor: modelador · 6 operações · 9 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 | tipo |
|---|---|---|---|---|---|---|
| kit | as ferramentas que criam, guardam e leem um plano, e os textos que ensinam o kit a agentes e ao dono | reconhecimento do plano, número do plano, onde mora o estado, onde se gravam os registros da tarefa, o que a doutrina ensina, regra do artefato de humano, porta de entrada | Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje. | OP-1 | *"Faça esse plano visando enxugar o que temos de planejamento hoje, e melhoramento na geração de arquivos"* | escopo |
| plano novo | o próximo plano registrado depois desta entrega | forma com que nasce | Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou. | externo | *"Para cada plano, preciso que seja criada uma nova pasta"* | medição |
| acervo existente | os planos, relatos, laudos e entregas já gravados | forma e leitura | Quem implementa não o toca. Ele prova que nada do que existe se perdeu. | externo | *"Considerar este plano já como legado"* | medição |

### 1.2 Fluxo de operações

- **OP-1** — O mantenedor do kit reúne num lugar só a forma do número e do caminho de um plano, que passa a aceitar número a partir do zero e plano em pasta própria, ao lado da forma antiga; os ganchos do kit passam a consultar esse lugar.
  - `precisa de: acervo existente` · `altera: kit.reconhecimento do plano` · `tarefas: SAN-T1` · `lastro: Para cada plano, preciso que seja criada uma nova pasta; devem ser numerados a partir do 0`
- **OP-2** — O mantenedor do backlog faz o instrumento de backlog guardar o estado de plano e de tarefa numa tabela de máquina na pasta do plano, contar o próximo número a partir do zero em projeto novo e acusar plano novo com estado escrito no texto.
  - `precisa de: kit, acervo existente` · `altera: kit.onde mora o estado, kit.número do plano` · `tarefas: SAN-T2, SAN-T2a` · `lastro: artefatos únicos de máquina, que podem ser rastreados pelas funções de captura de texto sem leitura`
- **OP-3** — O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje.
  - `precisa de: kit, acervo existente` · `altera: kit.onde se gravam os registros da tarefa` · `tarefas: SAN-T3, SAN-T3a` · `lastro: melhoramento na geração de arquivos; seja inserida ali os artefatos pertinentes`
- **OP-4** — O redator da doutrina reescreve o que o kit ensina sobre plano: pasta própria com nomes fixos, estado na tabela que o planejador cria ao registrar o plano, e projeto novo nascendo com a contagem em zero.
  - `precisa de: kit, plano novo` · `altera: kit.o que a doutrina ensina, kit.número do plano` · `tarefas: SAN-T4` · `lastro: Para cada plano, preciso que seja criada uma nova pasta; Essa diretiva deverá valer para os projetos que herdarem o kit`
- **OP-5** — O redator da doutrina escreve, uma vez só, a regra de que todo artefato de humano é o menor possível, e os limites de tamanho que já existem passam a apontar para ela.
  - `precisa de: kit` · `altera: kit.regra do artefato de humano` · `tarefas: SAN-T5` · `lastro: todo artefato de humano deve ser os menores possíveis; artefatos de planejamentos concisos`
- **OP-6** — O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo.
  - `precisa de: kit, plano novo` · `altera: kit.porta de entrada` · `tarefas: SAN-T6, SAN-T6a, SAN-T6b` · `lastro: no prompt, a revisão da porta de entrada por último`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 |
|---|---|---|---|
| kit.reconhecimento do plano | só arquivo único com número de quatro dígitos; cada ferramenta guarda a sua cópia dessa forma | uma forma só, num lugar só, que aceita também pasta própria e número a partir do zero | *"uma nova pasta"*; *"numerados a partir do 0"* |
| kit.número do plano | quatro dígitos que parecem data | projeto novo começa em zero e soma um; aqui a contagem segue de onde está | *"Essa numeração 0748 para mim smente confunde"*; *"deverá valer para os projetos que herdarem o kit"* |
| kit.onde mora o estado | numa linha de status escrita no texto do plano | numa tabela de máquina na pasta do plano, achada por busca sem abrir arquivo | *"artefatos únicos de máquina"* |
| kit.onde se gravam os registros da tarefa | numa pasta comum, misturados aos de todos os planos | dentro da pasta do plano; tíquete e plano antigo seguem na pasta comum | *"seja inserida ali os artefatos pertinentes"* |
| kit.o que a doutrina ensina | plano em arquivo único, estado no texto, registros espalhados | pasta por plano, estado na tabela, contagem em zero no projeto novo | *"Para cada plano, preciso que seja criada uma nova pasta"* |
| kit.regra do artefato de humano | não existe; há só limites locais | uma regra única: texto para o dono é o menor possível e não repete o que já está em tabela de máquina | *"todo artefato de humano deve ser os menores possíveis"* |
| kit.porta de entrada | descreve plano em arquivo único | descreve pasta por plano, tabela de estado e a regra do texto mínimo | *"enxugar o que temos de planejamento hoje"* |
| plano novo.forma com que nasce | arquivo único, número de quatro dígitos, estado no texto | pasta própria com tudo dentro, estado na tabela. Nenhuma operação o altera: a diferença prova que o kit mudou | *"Para cada plano, preciso que seja criada uma nova pasta"* |
| acervo existente.forma e leitura | gravado e lido pelas ferramentas | o mesmo: nada movido nem reescrito, lido como antes | *"Considerar este plano já como legado"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-24 | vigente | modelador — autoria sobre o dossiê do planejador |

## 2. Fatos estabelecidos

Fonte de todos: dossiê do `pantonic-scout`, campanha Q1–Q9, 2026-09-24, salvo nota.

- **F-1** Tamanho medido (condutor): planos até 8465 linhas; diário 3967; `docs/RDO/` 153 arquivos.
- **F-2** Estado hoje: status de plano e de tarefa na linha `**Status:**` do plano; único escritor
  `backlog.py` `transacionar_status` (`STATUS_CAMPO_RE`). Fila no bloco `<!-- fila:gerada -->` do
  diário (`_regenerar_bloco_fila`); diretiva em `**Diretiva de priorização:**`; índice em `## Índice`
  (`INDICE_LINHA_RE`); contador literal `**Próximo id de plano: P-NNNN.**` no `_INBOX.md`, reescrito
  por `transacionar_drain` (`_CONTADOR_INBOX_RE`) e confrontado por `check` com o maior id em
  `docs/plans/P-*.md`.
- **F-3** Não há módulo compartilhado de caminhos: `backlog.py`, `rdo.py` (`_default_rdo_dir`,
  `_default_laudos_dir`, `_default_root`), `review_evidence.py` (lista estática), `progresso_hook.py`,
  `backlog_hook.py`, `telemetria.py` fixam os seus. Nada em `.claude/global/hooks`, `.claude/checks`,
  `sync-kit.ps1`.
- **F-4** Toda regex de id exige 4 dígitos: `backlog.py` `PLANO_HEADER_RE`, `_ID_PLANO_RE`,
  `_CAMINHO_PLANO_INBOX_RE`, `_ID_PLANO_INBOX_RE`, `_CONTADOR_INBOX_ID_RE`; `review_evidence.py` e
  `rdo.py` casam `^(P-\d{4})` no `stem` do plano. Hoje `review_evidence.py`, `rdo.py close` e
  `backlog.py check` recusam `P-0` e `docs/plans/P-0-x/plano.md` (stem `plano`).
- **F-5** Formas ligadas a plano (Q5): plano, `_CAMPANHA-*`/`_CENARIO-*`/`_VEREDITO-*`/
  `_VIABILIDADE-*`/`_CARD-*`, `OPERACOES_AS_IS*` (skill `entrega-de-encerramento`), RDO de tarefa e
  de tíquete, laudo, evidência (`rdo.py`, `review_evidence.py`), `Entregas Aceitas/*`, `audits/*`;
  máquina já existente: `docs/telemetria.tsv` (`telemetria_hook.py`), `docs/ACIONAMENTOS_CONSULTOR.tsv`.
- **F-6** Doutrina que cita a convenção antiga (medido pelo planejador, cada literal único no
  arquivo): `GOVERNANCA.md`, `pantonic-planner.md`, `pantonic-reviewer.md`,
  `pantonic-consultant.md`, skills `diario-de-obras`, `bootstrap-pantonic`, `scrum-master`,
  `entrega-de-encerramento`, e `README.md`. O Controle 1.1 não está em `.claude/global/CLAUDE.md`
  (residência); só na cópia `~/.claude/CLAUDE.md` (ponto de carga, `TK-68`). No hub não existe
  `kit/`: agentes e skills residem em `.claude/agents/` e `.claude/skills/`.
- **F-7** Não existe regra geral de tamanho de artefato de humano; só locais (handover ≤ 8 linhas,
  §4.2; célula do índice compacta, `diario-de-obras`). Teste de residência (§3.1): regra do kit
  reside em `GOVERNANCA.md`; ponto de carga nunca é residência.
- **F-8** `sync-kit.ps1` projeta só skills e agentes; `.claude/tools/` não chega ao herdeiro por
  ele. `bootstrap-pantonic` cria `_INBOX.md`, diário e `rdo_template.md`. Nenhum dos 6 consumidores
  tem o kit instalado; kit em 0.0.0.
- **F-9** Nenhum plano vivo na superfície. Tíquetes `ready` nela: `TK-65` (`backlog.py`), `TK-66` e
  `TK-74` (`review_evidence.py`) — os três priorizados pela diretiva vigente —, `TK-68`
  (`.claude/global/CLAUDE.md`), `TK-72` e `TK-73` (`GOVERNANCA.md`, `pantonic-planner.md`).
- **F-10** 145 ocorrências de caminho ou regex fixos em `tests/` (`test_backlog.py` 99,
  `test_rdo.py` 13, `test_progresso_hook.py` 12, demais ≤ 5).
- **F-11** `.claude/tools/` não é pacote: as ferramentas se carregam por caminho
  (`importlib.util.spec_from_file_location`). Dois helpers de teste copiam ferramenta para raiz
  temporária: `tests/test_backlog.py` `_montar_raiz_hook` (copia `backlog.py`) e
  `tests/test_review_evidence.py` (copia `rdo.py`). `rdo.py close` regenera `INDEX.md` no
  diretório de destino; `rdo.py laudo --plano` recebe o id, não o caminho (medido pelo planejador).
- **F-12** Referência de 2026-09-24: `python -m pytest tests -q` → `313 passed`;
  `pwsh .claude/checks/check-readme.ps1` → `OK`, exit 0.

## 3. Decisões

| id | valor | razão |
|---|---|---|
| DSA-1 | Escopo é o kit: doutrina, skills, agentes, `.claude/tools/`, template de bootstrap | rodada, resposta 1 |
| DSA-2 | Nenhum artefato existente do hub é movido, renomeado, renumerado ou condensado | rodada, respostas 1 e 2 |
| DSA-3 | Id `P-<n>`, `n` inteiro decimal; projeto novo começa em `P-0` e soma 1; o hub segue o contador (`P-0750`…) | resposta 1; recomeçar no hub faria `P-0`..`P-9` casar por prefixo com `P-07xx` |
| DSA-4 | Plano novo nasce no layout da §3.1, no hub inclusive | pedido (pasta por plano); o hub é o primeiro corpus real do layout |
| DSA-5 | Estado de plano e de tarefa do layout novo mora só em `estado.tsv` (§3.2); `plano.md` não tem linha `**Status:**` | pedido (máquina única, rastreável por busca); F-2 |
| DSA-6 | `estado.tsv` nasce do planejador no registro (Fase 5); depois só `backlog.py transacionar_status` o escreve | F-2: escritor único já existe |
| DSA-7 | Instrumentos reconhecem o layout pela forma do caminho, sem chave de configuração; leitura do legado inalterada | DSA-2 exige ler o legado; F-4 |
| DSA-8 | Regex de id e caminhos de plano residem só em `.claude/tools/caminhos.py` (novo); `backlog.py`, `rdo.py`, `review_evidence.py`, `progresso_hook.py`, `backlog_hook.py` o carregam; `telemetria.py` fica (não lê plano) | F-3, F-4: oito cópias; residência única |
| DSA-9 | `rdo.py` e `review_evidence.py` gravam RDO, laudo e evidência de tarefa do layout novo na pasta do plano; legado e `TK-*` seguem em `docs/RDO/` | pedido (geração de arquivos); DSA-2 |
| DSA-10 | `docs/telemetria.tsv` e `docs/ACIONAMENTOS_CONSULTOR.tsv` ficam globais | já são máquina de residência única com id no conteúdo (F-5) |
| DSA-11 | A regra da §3.3 reside em `GOVERNANCA.md` §4.2, subseção nova; as regras locais de tamanho passam a citá-la | F-7; §4.2 já é a residência da fronteira de registro |
| DSA-12 | `backlog.py check` acusa, só em plano em pasta: `C-13` (card sem linha em `estado.tsv`, linha sem card, arquivo ausente ou fora do esquema) e `C-14` (linha `**Status:**` em `plano.md`) | guarda discriminante sem vermelho sobre legado |
| DSA-13 | A doutrina ativa é regularizada no mesmo plano pela tabela da §3.4 (G-SURFACE) | F-6 |
| DSA-14 | Template de bootstrap cria `_INBOX.md` com `**Próximo id de plano: P-0.**` e a pasta `docs/plans/` vazia | DSA-3; F-8 |
| DSA-15 | Este plano é legado: arquivo único, id `P-0749` | rodada, resposta 1 |
| DSA-16 | Card que edita `backlog.py` depende de `TK-65`; card que edita `review_evidence.py` depende de `TK-66`, `TK-74`; âncoras por nome de constante, não por linha | F-9: mesma região, diretiva os prioriza |
| DSA-17 | Plano em pasta não ganha `INDEX.md` de RDO: a pasta e o `estado.tsv` são o índice | regra da §3.3 (a); F-11 |
| DSA-18 | Função de `caminhos.py` nasce no card que lhe dá o primeiro chamador de produção: `formatar_id` na `SAN-T2`, `pasta_por_id` na `SAN-T3`; `pasta_do_plano` fica na `SAN-T1`, chamada por `backlog._parse_plano` | `AE-1`: G-DEADCODE recusa superfície sem chamador |
| DSA-19 | `caminhos.py` tem CLI (`main`: lista `<id><TAB><caminho>` dos planos) — é o entry point que o `dead_code.py` reconhece, como em `backlog.py` e `rdo.py`, também carregados por caminho; `I-6` fica | `AE-1`: módulo só carregado por caminho é inalcançável ao detector; medido `dead_code` exit 0 com a CLI |
| DSA-20 | A verificação de `I-2` compara, na mesma árvore e no mesmo instante, a cópia de referência de `backlog.py` + `caminhos.py` feita em `$env:TEMP` antes da primeira edição e o código editado; saída gravada em arquivo não serve de base | `AE-1` (b): `next` muda com a transição da própria tarefa |
| DSA-21 | "Flag explícita sempre vence" vale também para o `INDEX.md`: o `close` o regenera sempre que grava no destino legado — com `--rdo-dir` ou com plano legado —, e só o destino na pasta do plano dispensa índice; a CLI anuncia os dois destinos. Corretivo `SAN-T3a` (`OP-3`) roda antes da `SAN-T4` | `AE-3` (a), (b) e ressalva |
| DSA-22 | `C-10` só se aplica com plano presente: sem plano em `docs/plans/`, todo contador vale, `P-0` inclusive; com plano, regra e mensagem inalteradas. Corretivo `SAN-T2a` (`OP-2`) antes da `SAN-T5` | `AE-4`: o estado que `DSA-14` ensina acusava `C-10` falso |
| DSA-23 | O glossário do `README.md` diz o contador como o item 1 do `G-PLANREADY` e `GOVERNANCA.md` §7 item 11: "contador monotônico do repositório". Corretivo `SAN-T6a` (`OP-6`) depois da `SAN-T6`; o veredito do dono sobre `M5` sobe junto com `M1`..`M4` no relatório de encerramento e fica fora do *Pronto quando* | `AE-5` (b), com (a) já aplicado ao card |
| DSA-24 | O `README.md` inteiro deixa de chamar o contador de "global": a linha da §14 (*Decisões estruturantes*) passa a "contador sequencial do repositório", alinhada ao glossário (`M5`), ao item 1 do `G-PLANREADY` e a `GOVERNANCA.md` §7 item 11 — o kit é herdado e cada repositório conta do zero, "global" diria o contrário. Corretivo `SAN-T6b` (`OP-6`) depois da `SAN-T6a`; `M6` sob o mesmo veredito do dono de `M1`..`M5`, fora do *Pronto quando*. Descartada: manter a palavra na §14 — a porta de entrada voltaria a dizer o contador de dois jeitos, o defeito que `DSA-23` fechou | `AE-6` |

### 3.1 Layout da pasta de plano — residência normativa desta lista

`docs/plans/P-<n>-<slug>/` contém, com estes nomes:

- `plano.md` — §0..§9 e os cards (humano e gramática de card)
- `estado.tsv` — estado de máquina (§3.2)
- `rdo/<tarefa>.md`, `laudos/<tarefa>.md`, `evidencia/<tarefa>.md`
- `campanha.md`, `cenario.md`, `veredito.md`, `viabilidade.md` — quando existirem
- `operacoes.md` — o documento de encerramento (hoje `OPERACOES_AS_IS_P-*.md`)
- `entrega.md` — a entrega aceita (hoje `Entregas Aceitas/Entregas - P-*.md`)

### 3.2 `estado.tsv` — residência normativa do esquema

Separador TAB (escrito `<TAB>` aqui). Primeira linha `id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota`;
depois uma linha por item, estado corrente, reescrita no lugar. `id` = `P-<n>` na linha do plano
(a primeira) ou o id da tarefa; `tipo` ∈ {`plano`, `tarefa`}; `status` ∈ vocabulário de
`backlog.py` (`triage`, `ready`, `blocked`, `in-progress`, `review`, `done`, `cancelled`; plano
também `superseded`); `razao` ∈ {`-`, `dependencia`, `premissa`}; `data` `AAAA-MM-DD`; `nota` uma
linha sem TAB, ou `-`. Busca sem leitura: `rg "^<id>	" docs/plans/*/estado.tsv`.

### 3.3 Artefato de humano mínimo — residência normativa do texto da regra (destino: DSA-11)

- **Artefato de humano mínimo** — artefato **de máquina** é o que um instrumento ou um agente lê
  por gramática (TSV, card); artefato **de humano** é o que o dono lê (§0, §1 e §3 do plano,
  rodada de decisões, handover, diretiva e índice do diário, documento de encerramento). Todo
  artefato de humano é o menor possível: (a) não repete dado cuja residência é artefato de máquina
  — no máximo o ponteiro; (b) não narra o que o git, o RDO ou um TSV já registram; (c) frase que
  não serve a decisão ou validação do dono sai. O card segue `G-EXECREADY`: a autossuficiência do
  executor frio prevalece sobre (a)–(c). Os limites locais de tamanho (handover, célula do índice)
  são aplicações desta regra.

### 3.4 Reescrita da convenção na doutrina ativa — residência normativa da tabela

| forma antiga | forma nova |
|---|---|
| `docs/plans/P-NNNN-<slug>.md` e `docs/plans/P-<MMDD>-<slug>.md` | `docs/plans/P-<n>-<slug>/plano.md` |
| linha `**Status:**` do card ou do cabeçalho | linha do item em `docs/plans/P-<n>-<slug>/estado.tsv` |
| `docs/RDO/<plano>-<tarefa>-<slug>.md` | `docs/plans/P-<n>-<slug>/rdo/<tarefa>.md` |
| `docs/RDO/laudos/<plano>-<tarefa>.md` | `docs/plans/P-<n>-<slug>/laudos/<tarefa>.md` |
| `docs/RDO/evidencia/<plano>-<tarefa>.md` | `docs/plans/P-<n>-<slug>/evidencia/<tarefa>.md` |
| `docs/plans/_CAMPANHA-*`, `_CENARIO-*`, `_VEREDITO-*`, `_VIABILIDADE-*` | `campanha.md`, `cenario.md`, `veredito.md`, `viabilidade.md` na pasta do plano |
| `docs/OPERACOES_AS_IS_P-NNNN.md` | `docs/plans/P-<n>-<slug>/operacoes.md` |
| `docs/Entregas Aceitas/Entregas - P-NNNN.md` | `docs/plans/P-<n>-<slug>/entrega.md` |

A tabela se aplica aos arquivos de F-6 (a `SAN-T4` a instancia literal a literal; o `README.md` é
da `SAN-T6`). Menção que descreve o legado fica, marcada `legado`. Registros (`docs/plans/P-07*`,
`docs/RDO/`, diário) não se tocam.

## 4. Invariantes de execução

- **I-1** Nenhum card move, renomeia ou reescreve arquivo existente em `docs/plans/`, `docs/RDO/`,
  `docs/Entregas Aceitas/`, `docs/audits/`, `docs/OPERACOES_AS_IS*.md` (DSA-2).
- **I-2** A saída dos instrumentos sobre o legado do hub não muda; o piso de regressão é o total da
  suíte re-medido no despacho, que a entrega não reduz.
- **I-3** Regex de id de plano e caminho de plano não aparecem fora de `.claude/tools/caminhos.py`.
- **I-4** Doutrina se edita na residência; `~/.claude/` é ponto de carga e nenhum card o edita.
- **I-5** A regra da §3.3 entra uma vez, em `GOVERNANCA.md` §4.2; os demais lugares recebem ponteiro.
- **I-6** Nada se edita em `.claude/global/hooks/`, `.claude/checks/`, `sync-kit.ps1`.

## 5. Tarefas

Comum a todos os cards: raiz `D:\workspaces\PantonicApp`; comandos na forma da `docs/RUBRICA_DE_REVISAO.md` §8.1 (só `python` e `pwsh`); os valores
"antes" das verificações foram medidos pelo planejador em 2026-09-24; o piso da suíte é o total que
`python -m pytest tests -q` imprime no despacho (referência: `313 passed`), e a entrega o soma, nunca
o reduz.

### SAN-T1 — O id e o caminho do plano num lugar só [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor do kit reúne num lugar só a forma do número e do caminho de um plano, que passa a aceitar número a partir do zero e plano em pasta própria, ao lado da forma antiga; os ganchos do kit passam a consultar esse lugar.
- **Fundamento:** DSA-3, DSA-7, DSA-8, DSA-16, DSA-18, DSA-19, DSA-20; F-3, F-4, F-11; I-2, I-3; `AE-1`.
- **Estado da árvore no redespacho:** a entrega de 2026-09-25, reprovada em `AE-1` (fiel ao card anterior), está na árvore, não commitada: `caminhos.py` e `tests/test_caminhos.py` existem e os passos 3-9 já foram aplicados. Os passos descrevem o estado final: troca já feita segue sem refazer; `caminhos.py` se sobrescreve inteiro com o literal abaixo.
- **Depende de:** `TK-65`, `TK-66`, `TK-74`
- **Operação do modelo:** `OP-1`
  - OP-1: O mantenedor do kit reúne num lugar só a forma do número e do caminho de um plano, que passa a aceitar número a partir do zero e plano em pasta própria, ao lado da forma antiga; os ganchos do kit passam a consultar esse lugar.
  - precisa de: acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, só `.claude/tools/` e `tests/`. `.claude/tools/` não é pacote: toda ferramenta carrega `caminhos.py` por caminho, com o carregador abaixo. Nada em `docs/`.
- **Arquivos-alvo:**
  - `.claude/tools/caminhos.py`
  - `.claude/tools/backlog.py`
  - `.claude/tools/backlog_hook.py`
  - `.claude/tools/progresso_hook.py`
  - `.claude/tools/rdo.py`
  - `.claude/tools/review_evidence.py`
  - `tests/test_caminhos.py`
  - `tests/test_backlog.py`
  - `tests/test_review_evidence.py`
  - `tests/test_progresso_hook.py`
- **Texto novo, literal — `.claude/tools/caminhos.py` (arquivo novo, inteiro):**

  ```python
  """P-0749 SAN-T1 — residência única da forma do id e do caminho de plano (`DSA-8`).

  Duas formas convivem, reconhecidas pelo caminho, sem chave de configuração (`DSA-7`): plano
  legado `docs/plans/P-<dígitos>-<slug>.md` e plano em pasta `docs/plans/P-<n>-<slug>/plano.md`.
  Nenhuma outra ferramenta guarda cópia destas regex (`I-3`); cada uma carrega este módulo por
  caminho, via `importlib.util.spec_from_file_location`. Função entra aqui com o primeiro chamador
  de produção (`DSA-18`); `main` é a CLI de listagem e o entry point do módulo (`DSA-19`).
  """
  from __future__ import annotations

  import argparse
  import re
  from pathlib import Path

  PLANO_HEADER_RE = re.compile(r"^# (P-\d+) — (.+)$")
  ID_PLANO_RE = re.compile(r"^P-(\d+)$")
  CAMINHO_PLANO_INBOX_RE = re.compile(r"docs/plans/P-\d+-[^)\s`/]+(?:/plano)?\.md")
  ID_PLANO_INBOX_RE = re.compile(r"docs/plans/P-(\d+)-")
  CONTADOR_INBOX_RE = re.compile(r"\*\*Próximo id de plano: P-\d+\.\*\*")
  CONTADOR_INBOX_ID_RE = re.compile(r"\*\*Próximo id de plano: P-(\d+)\.\*\*")

  NOME_PLANO_PASTA = "plano.md"
  _ID_NO_NOME_RE = re.compile(r"^(P-\d+)")
  _PASTA_RE = re.compile(r"^P-\d+-")


  def planos_dir(raiz: Path) -> Path:
      return Path(raiz) / "docs" / "plans"


  def inbox_planos(raiz: Path) -> Path:
      return planos_dir(raiz) / "_INBOX.md"


  def e_layout_pasta(plano_path: Path) -> bool:
      p = Path(plano_path)
      return p.name == NOME_PLANO_PASTA and _PASTA_RE.match(p.parent.name) is not None


  def arquivos_de_plano(raiz: Path) -> list[Path]:
      base = planos_dir(raiz)
      legado = [p for p in base.glob("P-*.md") if p.is_file()]
      pasta = [p for p in base.glob("P-*/" + NOME_PLANO_PASTA) if p.is_file() and e_layout_pasta(p)]
      return sorted(legado + pasta)


  def id_do_plano(plano_path: Path) -> str | None:
      p = Path(plano_path)
      nome = p.parent.name if e_layout_pasta(p) else p.stem
      m = _ID_NO_NOME_RE.match(nome)
      return m.group(1) if m else None


  def pasta_do_plano(plano_path: Path) -> Path | None:
      p = Path(plano_path)
      return p.parent if e_layout_pasta(p) else None


  def main(argv: list[str] | None = None) -> int:
      """Lista os planos da raiz, um por linha: `<id><TAB><caminho relativo à raiz>`."""
      parser = argparse.ArgumentParser(description="Lista os planos, legado e em pasta.")
      parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
      args = parser.parse_args(argv)
      raiz = Path(args.root)
      for plano in arquivos_de_plano(raiz):
          print(f"{id_do_plano(plano) or '-'}\t{plano.relative_to(raiz).as_posix()}")
      return 0


  if __name__ == "__main__":
      raise SystemExit(main())
  ```

  Carregador, colado igual em cada uma das cinco ferramentas, logo depois do bloco de imports:

  ```python
  def _carregar_caminhos():
      caminho = Path(__file__).resolve().parent / "caminhos.py"
      spec = importlib.util.spec_from_file_location("caminhos", caminho)
      modulo = importlib.util.module_from_spec(spec)
      sys.modules[spec.name] = modulo
      spec.loader.exec_module(modulo)
      return modulo


  _caminhos = _carregar_caminhos()
  ```
- **Passos:**
  1. Antes de qualquer edição, copiar o código de referência para `$env:TEMP` (`DSA-20`) e anotar o total da suíte:

     ```
     pwsh -NoProfile -Command 'New-Item -ItemType Directory -Force "$env:TEMP/san-t1a-ref" | Out-Null; Copy-Item .claude/tools/backlog.py,.claude/tools/caminhos.py "$env:TEMP/san-t1a-ref/"; "copiado"'
     python -m pytest tests -q
     ```
  2. Criar ou sobrescrever `.claude/tools/caminhos.py` com o texto literal acima.
  3. Em `backlog.py`, `backlog_hook.py`, `progresso_hook.py`, `rdo.py` e `review_evidence.py`: acrescentar ao bloco de imports `import importlib.util` e `import sys` onde faltarem; colar o carregador depois do bloco de imports (em `backlog.py`, antes da linha que define `PLANO_HEADER_RE`).
  4. Em `backlog.py`, trocar a definição de seis constantes pela referência, mantendo o nome: `PLANO_HEADER_RE = _caminhos.PLANO_HEADER_RE`, `_CAMINHO_PLANO_INBOX_RE = _caminhos.CAMINHO_PLANO_INBOX_RE`, `_ID_PLANO_INBOX_RE = _caminhos.ID_PLANO_INBOX_RE`, `_CONTADOR_INBOX_RE = _caminhos.CONTADOR_INBOX_RE`, `_CONTADOR_INBOX_ID_RE = _caminhos.CONTADOR_INBOX_ID_RE`, `_ID_PLANO_RE = _caminhos.ID_PLANO_RE`.
  5. Em `backlog.py` `carregar`: a lista de planos passa a `[_parse_plano(caminho, repo) for caminho in _caminhos.arquivos_de_plano(repo)]`; apagar `planos_dir = repo / "docs" / "plans"` se ficar sem uso. Trocar as três expressões `repo / "docs" / "plans" / "_INBOX.md"` (ramos `check`, `next`, `drain` de `main`) por `_caminhos.inbox_planos(repo)`. Em `_parse_plano`, as duas linhas `plano_id = m0.group(1) if m0 else caminho.stem` e `titulo = m0.group(2) if m0 else caminho.stem` → `pasta = _caminhos.pasta_do_plano(caminho)`, `nome = pasta.name if pasta is not None else caminho.stem`, `plano_id = m0.group(1) if m0 else nome`, `titulo = m0.group(2) if m0 else nome` (legado segue no `stem`).
  6. Em `backlog_hook.py`: `repo / "docs" / "plans" / "_INBOX.md"` → `_caminhos.inbox_planos(repo)`.
  7. Em `progresso_hook.py` `localizar_card`: a linha `arquivos = [p for p in sorted((raiz / "docs" / "plans").glob("P-*.md")) if p.exists()]` → `arquivos = _caminhos.arquivos_de_plano(raiz)`; e a linha `if arq.name.startswith("P-"):` → `if _caminhos.id_do_plano(arq) is not None:` (com `plano.md` o nome não começa por `P-` e o título vinha do último `## `).
  8. Em `rdo.py` e `review_evidence.py`: as duas linhas `plano_id_match = re.match(r"^(P-\d{4})", plano_path.stem)` e `plano_id = plano_id_match.group(1) if plano_id_match else plano_path.stem` → `plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem`.
  9. Nos dois helpers que copiam ferramenta para raiz temporária, copiar também `caminhos.py`: em `tests/test_backlog.py` `_montar_raiz_hook`, depois de `shutil.copy2(_BACKLOG_PATH, tools_dir / "backlog.py")`, a linha `shutil.copy2(_BACKLOG_PATH.parent / "caminhos.py", tools_dir / "caminhos.py")`; em `tests/test_review_evidence.py`, depois de `shutil.copy2(_RDO_REAL_PATH, destino_rdo)`, a linha `shutil.copy2(_RDO_REAL_PATH.parent / "caminhos.py", destino_rdo.parent / "caminhos.py")`.
  10. Criar `tests/test_caminhos.py` com os TF 1, 2, 3, 5 e 16 de `Testes`, carregando o módulo por `importlib.util.spec_from_file_location` a partir de `Path(__file__).resolve().parents[1] / ".claude" / "tools" / "caminhos.py"`; se ele já existir, retirar `test_tf_san_4_*` e `test_tf_san_6_*` (vão à `SAN-T3` e à `SAN-T2`, `DSA-18`) e acrescentar o 16. O TF 17 vai em `tests/test_backlog.py`, o 18 em `tests/test_progresso_hook.py`.
  11. Rodar a Verificação 1 a 8.
- **Restrições desta tarefa:** I-2 — `check` e `next` do código editado imprimem, sobre o hub, o mesmo que a cópia de referência do passo 1 (`DSA-20`); I-3 — nenhuma regex de id ou glob de plano fora de `caminhos.py`; toda função de `caminhos.py` tem chamador de produção (`DSA-18`); `progresso_hook.py` continua sem imprimir e saindo sempre 0.
- **Não fazer:** não mudar a formatação `:04d` de `backlog.py` (é da `SAN-T2`); não mudar destino de RDO, laudo ou evidência (`SAN-T3`); não renomear constante de `backlog.py`; não editar fixture existente nem arquivo em `docs/`.
- **Contingências:**
  1. se uma das seis constantes de `backlog.py`, ou as duas linhas de `plano_id_match`, não existirem com esse nome (renomeadas por `TK-65`/`TK-66`/`TK-74`) → parar e sinalizar `blocked` razão `premissa`, devolvendo o nome ausente;
  2. se um teste falhar com erro de arquivo `caminhos.py` ausente numa raiz temporária → acrescentar ao helper que copia a ferramenta a cópia de `caminhos.py` para o mesmo diretório, na forma do passo 9, e seguir;
  3. se a Verificação 5 imprimir `DIFERE` → corrigir a entrega até imprimir `IGUAL`; persistindo por forma que só a regex de 4 dígitos casava → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha que diverge;
  4. se `dead_code.py` (Verificação 7) acusar símbolo fora de `caminhos.py` → é alheio à tarefa: registrar no retorno e seguir; símbolo de `caminhos.py` acusado → corrigir a entrega (nunca editar `.claude/checks/`, `I-6`).
- **Testes** (novos; entre parênteses, o que a regra concorrente daria — a fixture separa as duas):
  - `test_tf_san_1_id_aceita_zero_e_legado` — `ID_PLANO_RE` casa `P-0`, `P-12`, `P-0749`; não casa `P-` nem `P-12a` (`^P-(\d{4})$` recusa `P-0`).
  - `test_tf_san_2_id_do_plano_nas_duas_formas` — `id_do_plano` dá `P-0` para `docs/plans/P-0-gama/plano.md`, `P-12` para `docs/plans/P-12-x/plano.md`, `P-0749` para `docs/plans/P-0749-saneamento-artefatos.md`, `None` para `tmp/plano.md` (o stem dá `plano` na forma pasta).
  - `test_tf_san_3_arquivos_de_plano` — em `tmp_path` com `docs/plans/P-0749-a.md`, `docs/plans/P-0-b/plano.md`, `docs/plans/_INBOX.md`, pasta vazia `docs/plans/P-1-c/` e `docs/plans/P-2-d/outro.md`, devolve exatamente `[tmp_path/"docs/plans/P-0-b/plano.md", tmp_path/"docs/plans/P-0749-a.md"]` (o glob `P-*.md` devolve só o segundo).
  - `test_tf_san_5_linha_viva_do_inbox` — `CAMINHO_PLANO_INBOX_RE.search` sobre ``- `docs/plans/P-0-gama/plano.md` — nota`` dá `docs/plans/P-0-gama/plano.md`, e sobre ``- `docs/plans/P-0749-saneamento-artefatos.md` — nota`` dá `docs/plans/P-0749-saneamento-artefatos.md` (a regex antiga não casa a primeira).
  - `test_tf_san_16_cli_lista_os_planos` (`test_caminhos.py`) — com `docs/plans/P-0749-a.md` e `docs/plans/P-0-b/plano.md` em `tmp_path`, `caminhos.main(["--root", str(tmp_path)])` devolve 0 e o stdout (`capsys`) é exatamente `P-0\tdocs/plans/P-0-b/plano.md\nP-0749\tdocs/plans/P-0749-a.md\n` (o glob `P-*.md` dá só a segunda linha).
  - `test_tf_san_17_parse_plano_em_pasta_sem_cabecalho` (`test_backlog.py`) — `_parse_plano(tmp_path/"docs/plans/P-0-gama/plano.md", tmp_path)` sobre arquivo sem linha `# P-… — …` dá `id == "P-0-gama"` e `titulo == "P-0-gama"` (o `stem` dá `plano`; medido pelo consultor em 2026-09-25).
  - `test_tf_san_18_titulo_do_plano_em_pasta` (`test_progresso_hook.py`) — com `tmp_path/"docs/plans/P-0-gama/plano.md"` = `# P-0 — Plano gama`, linha vazia, `## 5. Tarefas`, linha vazia, `### GAM-T1 — Primeira [Sonnet · classe implementacao]`, `- **Objetivo:** fixture.`: `localizar_card("GAM-T1", tmp_path) == ("Primeira", "fixture.", "Plano gama")` (a regra `startswith("P-")` dá `"5. Tarefas"`; medido pelo consultor em 2026-09-25).
  - TR: a suíte existente inteira.
- **Verificação:**
  1. ```
     python -m pytest tests/test_caminhos.py -q
     ```
     → **5 passed**. **Medido antes: 6 passed** (2026-09-25, entrega de `AE-1`, com os TF 4 e 6).
  2. ```
     pwsh -NoProfile -Command '(@(foreach ($f in ".claude/tools/backlog.py",".claude/tools/rdo.py",".claude/tools/review_evidence.py") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "P-\d{4}","P-(\d{4})").Count })) -join " / "'
     ```
     → **0 / 0 / 0**. **Medido antes: 0 / 0 / 0** (2026-09-25, entrega de `AE-1`; 6 / 1 / 1 em 2026-09-24).
  3. ```
     pwsh -NoProfile -Command '(@(foreach ($f in ".claude/tools/backlog.py",".claude/tools/progresso_hook.py") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "_caminhos.arquivos_de_plano(").Count })) -join " / "'
     ```
     → **1 / 1**. **Medido antes: 1 / 1** (2026-09-25, entrega de `AE-1`; 0 / 0 em 2026-09-24).
  4. ```
     pwsh -NoProfile -Command '(@(foreach ($f in ".claude/tools/backlog.py",".claude/tools/backlog_hook.py",".claude/tools/progresso_hook.py",".claude/tools/rdo.py",".claude/tools/review_evidence.py") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "_carregar_caminhos()").Count })) -join " / "'
     ```
     → **2 / 2 / 2 / 2 / 2** (a definição e a chamada). **Medido antes: 2 / 2 / 2 / 2 / 2** (2026-09-25, entrega de `AE-1`; 0 / 0 / 0 / 0 / 0 em 2026-09-24).
  5. ```
     pwsh -NoProfile -Command '$r = "$env:TEMP/san-t1a-ref/backlog.py"; $a = @(python $r check --repo . 2>$null) + @(python $r next --repo .); $b = @(python .claude/tools/backlog.py check --repo . 2>$null) + @(python .claude/tools/backlog.py next --repo .); if (($a -join "|") -ne ($b -join "|")) { "DIFERE"; exit 1 } else { "IGUAL" }'
     ```
     → **IGUAL**. **Medido antes: IGUAL** (2026-09-25, logo depois do passo 1; e com o reparo aplicado numa cópia em `$env:TEMP`). A referência é a entrega de `AE-1`, cuja saída o revisor mediu igual à do ref do despacho.
  6. ```
     python -m pytest tests -q
     ```
     → **o total anotado no passo 1 + 1, nenhuma falha** (menos os TF 4 e 6, mais os TF 16, 17 e 18). **Medido antes: 339 passed** (2026-09-25, entrega de `AE-1`).
  7. ```
     python .claude/checks/dead_code.py
     ```
     → **exit 0**, `dead_code: OK - 0 achado(s)`. **Medido antes: exit 1**, 8 achados, todos em `caminhos.py` (2026-09-25); exit 0 com o reparo aplicado numa cópia.
  8. ```
     pwsh -NoProfile -Command '(@(foreach ($p in "def pasta_por_id(","def formatar_id(","__main__") { @(Select-String -LiteralPath .claude/tools/caminhos.py -SimpleMatch -Pattern $p).Count }) + @(@(Select-String -LiteralPath .claude/tools/progresso_hook.py -SimpleMatch -Pattern "arq.name.startswith(").Count) + @(@(Select-String -LiteralPath .claude/tools/backlog.py -SimpleMatch -Pattern "if m0 else caminho.stem").Count)) -join " / "'
     ```
     → **0 / 0 / 1 / 0 / 0**. **Medido antes: 1 / 1 / 0 / 1 / 2** (2026-09-25); 0 / 0 / 1 / 0 / 0 com o reparo aplicado numa cópia.
- **Pronto quando:**
  - kit.reconhecimento do plano — uma forma só, num lugar só, que aceita também pasta própria e número a partir do zero — Verificação 1, 2, 3, 4, 7, 8
- **Fora do escopo desta tarefa:** `estado.tsv`, `C-13`/`C-14` e a largura do contador (`SAN-T2`); destinos de RDO, laudo e evidência (`SAN-T3`); doutrina (`SAN-T4`).
- **Notas de execução:**
  - 2026-09-25 `blocked` — reprovado 68 bloqueante=guardas, recomendação escalar (A6a); caminhos.py carregado por caminho é inalcançável ao dead_code.py e o I-6 veda .claude/checks; nenhum card fecha a guarda. Ver AE-1.
  - 2026-09-25 `ready` — consultor (A1, contexto limpo): card reescrito sobre AE-1 (DSA-18..20), reparo medido em copia; redespacho sobre a arvore atual

### SAN-T2 — O estado sai do texto e vai para o estado.tsv [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor do backlog faz o instrumento de backlog guardar o estado de plano e de tarefa numa tabela de máquina na pasta do plano, contar o próximo número a partir do zero em projeto novo e acusar plano novo com estado escrito no texto.
- **Fundamento:** DSA-3, DSA-5, DSA-6, DSA-12, DSA-16, DSA-18, DSA-20; §3.2; F-2; I-2.
- **Depende de:** `SAN-T1`
- **Operação do modelo:** `OP-2`
  - OP-2: O mantenedor do backlog faz o instrumento de backlog guardar o estado de plano e de tarefa numa tabela de máquina na pasta do plano, contar o próximo número a partir do zero em projeto novo e acusar plano novo com estado escrito no texto.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/backlog.py`, `.claude/tools/caminhos.py` e `tests/`. Plano legado (arquivo único) segue com estado na linha `**Status:**`, sem mudança; só plano em pasta (`_caminhos.e_layout_pasta`) lê e escreve `estado.tsv`.
- **Domínio:** `estado.tsv` — separador TAB; primeira linha `id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota`; uma linha por item, estado corrente, reescrita no lugar; `id` = `P-<n>` na linha do plano ou id da tarefa; `tipo` ∈ {`plano`, `tarefa`}; `razao` ∈ {`-`, `dependencia`, `premissa`}; `data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`.
- **Arquivos-alvo:**
  - `.claude/tools/caminhos.py`
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `tests/test_caminhos.py`
  - `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md`
  - `tests/fixtures/backlog/pasta/docs/plans/_INBOX.md`
  - `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/plano.md`
  - `tests/fixtures/backlog/pasta/docs/plans/P-0-gama/estado.tsv`
- **Texto novo, literal:**
  - em `caminhos.py`, imediatamente antes de `def main(` (`DSA-18`: nasce com o chamador de `drain` e `check`):

    ```python
    NOME_ESTADO = "estado.tsv"
    CABECALHO_ESTADO = "id\ttipo\tstatus\trazao\tdata\tnota"


    def estado_tsv(plano_path: Path) -> Path:
        return Path(plano_path).parent / NOME_ESTADO


    def formatar_id(numero: int, largura: int) -> str:
        return f"P-{numero:0{largura}d}"
    ```
  - em `tests/test_caminhos.py`, o TF `test_tf_san_6_formatar_id_preserva_largura` — `formatar_id(750, 4) == "P-0750"`, `formatar_id(1, 1) == "P-1"`, `formatar_id(10, 1) == "P-10"` (`:04d` dá `P-0001`).
  - fim da `@dataclass class Plano`, depois de `fora_do_corpus: bool = False`:

    ```python
        estado_arquivo: str | None = None
        estado_ids: list[tuple[str, int]] = field(default_factory=list)
        estado_defeitos: list[tuple[int, str]] = field(default_factory=list)
        status_no_texto: int | None = None
    ```
  - função nova, imediatamente antes de `def _parse_plano`:

    ```python
    def _aplicar_estado_tsv(caminho: Path, repo: Path, plano: Plano, linhas_plano: list[str]) -> None:
        """P-0749 SAN-T2 (`DSA-5`): plano em pasta tem o estado em `estado.tsv`, nunca no texto."""
        plano.status, plano.status_linha = None, None
        plano.status_no_texto = next(
            (i for i, linha in enumerate(linhas_plano, start=1) if STATUS_CAMPO_RE.search(linha)), None
        )
        por_id = {t.id: t for t in plano.tarefas}
        for tarefa in plano.tarefas:
            tarefa.status = tarefa.status_linha = tarefa.status_razao = tarefa.status_cauda = None
        estado_path = _caminhos.estado_tsv(caminho)
        plano.estado_arquivo = estado_path.relative_to(repo).as_posix()
        if not estado_path.is_file():
            plano.estado_defeitos.append((1, "estado.tsv ausente"))
            return
        linhas = estado_path.read_text(encoding="utf-8").splitlines()
        if not linhas or linhas[0] != _caminhos.CABECALHO_ESTADO:
            plano.estado_defeitos.append((1, "cabeçalho fora do esquema"))
            return
        for n, linha in enumerate(linhas[1:], start=2):
            if not linha.strip():
                continue
            campos = linha.split("\t")
            if len(campos) != 6:
                plano.estado_defeitos.append((n, "linha fora do esquema"))
                continue
            id_, tipo, status, razao, _data, nota = campos
            if tipo == "plano" and id_ == plano.id:
                plano.status = status
            elif tipo == "tarefa":
                plano.estado_ids.append((id_, n))
                tarefa = por_id.get(id_)
                if tarefa is not None:
                    tarefa.status = status
                    tarefa.status_razao = None if razao == "-" else razao
                    tarefa.status_cauda = None if nota == "-" else nota
            else:
                plano.estado_defeitos.append((n, f"{id_}: tipo '{tipo}' fora do esquema"))
    ```
  - em `_parse_plano`, `return Plano(` passa a `plano = Plano(`, e depois do parêntese que fecha a chamada:

    ```python
        if _caminhos.e_layout_pasta(caminho):
            _aplicar_estado_tsv(caminho, repo, plano, linhas)
        return plano
    ```
  - em `check`, imediatamente antes da linha `        for tarefa in plano.tarefas:` que segue o bloco `C-3` cuja mensagem é `f"{plano.id}: status '{plano.status}' fora do vocabulário"`:

    ```python
            if plano.estado_arquivo is not None:
                for linha_n, mensagem in plano.estado_defeitos:
                    violacoes.append(Violacao("C-13", plano.estado_arquivo, linha_n, mensagem))
                ids_estado = {id_ for id_, _ in plano.estado_ids}
                ids_cards = {t.id for t in plano.tarefas}
                for tarefa in plano.tarefas:
                    if tarefa.id not in ids_estado:
                        violacoes.append(
                            Violacao("C-13", plano.arquivo, tarefa.linha_header, f"{tarefa.id} sem linha em estado.tsv")
                        )
                for id_, linha_n in plano.estado_ids:
                    if id_ not in ids_cards:
                        violacoes.append(
                            Violacao("C-13", plano.estado_arquivo, linha_n, f"{id_}: linha de estado.tsv sem card em plano.md")
                        )
                if plano.status_no_texto is not None:
                    violacoes.append(
                        Violacao("C-14", plano.arquivo, plano.status_no_texto, f"{plano.id}: linha **Status:** em plano de pasta")
                    )
    ```
  - em `transacionar_status`, imediatamente antes do comentário `# Checagens concluídas`:

    ```python
        plano_pasta = alvo if isinstance(alvo, Plano) else next(
            (p for p in modelo.planos if alvo.tipo == "tarefa" and p.arquivo == alvo.arquivo), None
        )
        estado_rel = plano_pasta.estado_arquivo if plano_pasta is not None else None
        if estado_rel is not None:
            if "\t" in (razao or "") or "\t" in (nota or ""):
                return ResultadoStatus(1, "razão ou nota contém TAB: estado.tsv usa TAB como separador")
            estado_path = repo / estado_rel
            estado_linhas = estado_path.read_text(encoding="utf-8").splitlines() if estado_path.is_file() else []
            idx_estado = next(
                (k for k, l in enumerate(estado_linhas) if k > 0 and l.split("\t")[0] == id_), None
            )
            if idx_estado is None:
                return ResultadoStatus(3, f"{id_} sem linha em {estado_rel}")
    ```
  - em `transacionar_status`, três trocas: (a) `plano_arquivo = alvo.arquivo if (isinstance(alvo, Plano) or alvo.tipo == "tarefa") else None` → `plano_arquivo = alvo.arquivo if (estado_rel is None and (isinstance(alvo, Plano) or alvo.tipo == "tarefa")) else None`; (b) a linha `    if isinstance(alvo, Plano):` que abre a escrita do status passa a `    if estado_rel is not None:` seguida, no recuo de 8 espaços, de `estado_linhas[idx_estado] = "\t".join([id_, "plano" if isinstance(alvo, Plano) else "tarefa", estado, razao or "-", hoje, nota if nota is not None else (getattr(alvo, "status_cauda", None) or "-")])`, e depois `    elif isinstance(alvo, Plano):` com o corpo antigo intacto; (c) `if nota is not None and isinstance(alvo, Item):` → `if nota is not None and isinstance(alvo, Item) and estado_rel is None:`. Depois do bloco `if plano_arquivo is not None:` da escrita final:

    ```python
        if estado_rel is not None:
            _escrever_atomico(repo / estado_rel, estado_linhas)
            arquivos_tocados.append(estado_rel)
    ```
  - em `transacionar_drain`, depois de `novo_id = max(ids_vistos) + 1`:

    ```python
        m_contador = _CONTADOR_INBOX_ID_RE.search(texto_inbox)
        largura = len(m_contador.group(1)) if m_contador else 1
    ```
    e `f"**Próximo id de plano: P-{novo_id:04d}.**"` → `f"**Próximo id de plano: {_caminhos.formatar_id(novo_id, largura)}.**"`.
  - em `check` (`C-10`): `f"contador aponta para P-{contador:04d}, já presente em docs/plans/"` → `f"contador aponta para {_caminhos.formatar_id(contador, len(m.group(1)))}, já presente em docs/plans/"`.
  - as três ocorrências de `C-1..C-12` (docstring do módulo e comentário de `check`) → `C-1..C-14`.
  - fixture `tests/fixtures/backlog/pasta/` (quatro arquivos, separados pelas linhas `===`; em `estado.tsv`, `<TAB>` é o caractere TAB):

    ```text
    === docs/DIARIO_DE_OBRAS.md
    # Diário de Obras (fixture pasta)

    ## Índice

    | ID | Título | Status | Âncora |
    |---|---|---|---|
    | P-0-GAM | Plano gama | ready | docs/plans/P-0-gama/plano.md |
    === docs/plans/_INBOX.md
    **Próximo id de plano: P-1.**
    === docs/plans/P-0-gama/plano.md
    # P-0 — Plano gama

    **Prefixo das tarefas no diário:** `GAM-T<n>`

    ### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]
    - **Objetivo:** fixture.

    ### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao]
    - **Objetivo:** fixture.
    === docs/plans/P-0-gama/estado.tsv
    id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota
    P-0<TAB>plano<TAB>ready<TAB>-<TAB>2026-01-01<TAB>-
    GAM-T1<TAB>tarefa<TAB>ready<TAB>-<TAB>2026-01-01<TAB>-
    GAM-T2<TAB>tarefa<TAB>ready<TAB>-<TAB>2026-01-01<TAB>-
    ```
- **Passos:**
  1. Antes de qualquer edição, copiar o código de referência para `$env:TEMP` (`DSA-20`) e anotar o total da suíte:

     ```
     pwsh -NoProfile -Command 'New-Item -ItemType Directory -Force "$env:TEMP/san-t2-ref" | Out-Null; Copy-Item .claude/tools/backlog.py,.claude/tools/caminhos.py "$env:TEMP/san-t2-ref/"; "copiado"'
     python -m pytest tests -q
     ```
  2. Aplicar, na ordem, os blocos de `Texto novo, literal` (o TF 6 em `tests/test_caminhos.py` é um deles).
  3. Criar a fixture `pasta` e os seis TF de `Testes` em `tests/test_backlog.py`, cada um sobre cópia da fixture em `tmp_path` com `_copiar_fixture`.
  4. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** I-2 — sobre plano legado, nenhuma saída muda (Verificação 4); o contador do hub segue com 4 dígitos (`P-0750`); `estado.tsv` só é escrito por `transacionar_status`.
- **Não fazer:** não mexer em `rdo.py`, `review_evidence.py` nem na doutrina; não criar `estado.tsv` em `docs/`; não acusar `C-13`/`C-14` em plano legado; não mudar a leitura do diário.
- **Contingências:**
  1. se `check` sobre a cópia intacta da fixture `pasta` acusar código de `C-1` a `C-12` → trocar a linha do índice da fixture pela forma da linha `P-0001` da fixture `verde` (id `P-0-GAM`, âncora `docs/plans/P-0-gama/plano.md`) e rodar de novo; persistindo → parar e sinalizar `blocked` razão `premissa`, devolvendo a violação;
  2. se a transição `ready` → `in-progress` ou `in-progress` → `blocked` não existir em `_TRANSICOES` → parar e sinalizar `blocked` razão `premissa`;
  3. se a Verificação 4 imprimir `DIFERE` → corrigir a entrega até imprimir `IGUAL`.
- **Testes** (novos, em `tests/test_backlog.py`; entre parênteses, o valor da regra concorrente):
  - `test_tf_san_7_pasta_check_verde` — `check(carregar(repo), inbox_planos=..., repo=repo)` sobre a fixture `pasta` devolve lista vazia (estado lido do card: `C-8` e `C-2`).
  - `test_tf_san_8_status_escreve_estado_tsv` — `transacionar_status(repo, carregar(repo), "GAM-T1", "in-progress")` sai 0; a linha 3 de `estado.tsv` fica `GAM-T1<TAB>tarefa<TAB>in-progress<TAB>-<TAB><hoje><TAB>-`; `plano.md` byte a byte igual; `arquivos` contém `docs/plans/P-0-gama/estado.tsv` e não `docs/plans/P-0-gama/plano.md`. Depois, `transacionar_status(..., "GAM-T1", "blocked", razao="premissa", nota="contingência 2 acionada: x")` deixa a linha `GAM-T1<TAB>tarefa<TAB>blocked<TAB>premissa<TAB><hoje><TAB>contingência 2 acionada: x` (a escrita no card muda `plano.md`).
  - `test_tf_san_9_c13_nos_tres_casos` — três casos, cada um em cópia própria: sem a linha `GAM-T2` → violação `C-13` com `GAM-T2 sem linha em estado.tsv`; com linha extra `GAM-T9<TAB>tarefa<TAB>ready<TAB>-<TAB>2026-01-01<TAB>-` → `C-13` com `GAM-T9: linha de estado.tsv sem card em plano.md`; sem o arquivo → `C-13` com `estado.tsv ausente` (sem guarda: nenhum `C-13`).
  - `test_tf_san_10_c14_status_no_texto` — com a linha ``**Status:** `ready` `` inserida como linha 3 de `plano.md` → `C-14` em `docs/plans/P-0-gama/plano.md:3` com `P-0: linha **Status:** em plano de pasta` (sem guarda: nada).
  - `test_tf_san_11_drain_preserva_largura` — sem a linha `P-0-GAM` do índice e com `_INBOX.md` = `**Próximo id de plano: P-0.**` + linha ``- `docs/plans/P-0-gama/plano.md` — gama``, `transacionar_drain` sai 0 e o inbox passa a conter `**Próximo id de plano: P-1.**` (`:04d` dá `P-0001`).
  - `test_tf_san_12_c10_preserva_largura` — com `_INBOX.md` = `**Próximo id de plano: P-0.**`, `check` acusa `C-10` com `contador aponta para P-0, já presente em docs/plans/` (`:04d` dá `P-0000`).
  - TR: `test_tf_check_verde_sem_violacoes` e os testes da fixture `contador_inbox` (4 dígitos), inalterados.
- **Verificação:**
  1. ```
     python -m pytest tests/test_backlog.py -q -k tf_san
     ```
     → **6 passed**. **Medido antes: exit 5** (nenhum teste selecionado).
  2. ```
     pwsh -NoProfile -Command '@(Select-String -LiteralPath .claude/tools/backlog.py -SimpleMatch -Pattern ":04d}").Count'
     ```
     → **0**. **Medido antes: 2**.
  3. ```
     pwsh -NoProfile -Command '(@(foreach ($p in "C-13","C-14","C-1..C-12") { @(Select-String -LiteralPath .claude/tools/backlog.py -SimpleMatch -Pattern $p).Count })) -join " / "'
     ```
     → **≥ 1 / ≥ 1 / 0**. **Medido antes: 0 / 0 / 3**.
  4. ```
     pwsh -NoProfile -Command '$r = "$env:TEMP/san-t2-ref/backlog.py"; $a = @(python $r check --repo . 2>$null) + @(python $r next --repo .); $b = @(python .claude/tools/backlog.py check --repo . 2>$null) + @(python .claude/tools/backlog.py next --repo .); if (($a -join "|") -ne ($b -join "|")) { "DIFERE"; exit 1 } else { "IGUAL" }'
     ```
     → **IGUAL**. **Medido antes: IGUAL** (2026-09-25, com a cópia em `san-t1a-ref`; mede-se depois do passo 1, sem a cópia sai `DIFERE`; a forma com arquivo gravado deu `DIFERE` falso, `AE-1` (b)).
  5. ```
     python -m pytest tests -q
     ```
     → **o total anotado no passo 1 + 7, nenhuma falha** (seis TF em `test_backlog.py` e o TF 6). **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).
  6. ```
     python .claude/checks/dead_code.py
     ```
     → **exit 0**. **Medido antes: exit 1** (2026-09-25, 8 achados em `caminhos.py`; exit 0 depois da `SAN-T1` redespachada).
- **Pronto quando:**
  - kit.onde mora o estado — numa tabela de máquina na pasta do plano, achada por busca sem abrir arquivo — Verificação 1, 3
  - kit.número do plano — projeto novo começa em zero e soma um; aqui a contagem segue de onde está — Verificação 1, 2, 4
- **Fora do escopo desta tarefa:** destinos de RDO, laudo e evidência (`SAN-T3`); doutrina do `estado.tsv` e do contador (`SAN-T4`).

### SAN-T3 — Relato, laudo e evidência nascem na pasta do plano [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje.
- **Fundamento:** DSA-9, DSA-16, DSA-17, DSA-18; §3.1; F-11; I-2.
- **Depende de:** `SAN-T2`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py`, `.claude/tools/caminhos.py` e três arquivos de teste. Flag explícita (`--rdo-dir`, `--laudos-dir`, `--out`) sempre vence; o destino novo vale só sem a flag e só para plano em pasta.
- **Arquivos-alvo:**
  - `.claude/tools/caminhos.py`
  - `.claude/tools/rdo.py`
  - `.claude/tools/review_evidence.py`
  - `tests/test_rdo.py`
  - `tests/test_review_evidence.py`
  - `tests/test_caminhos.py`
- **Texto novo, literal:**
  - em `caminhos.py`, imediatamente antes de `def main(` (`pasta_por_id` nasce com o chamador do `laudo`, `DSA-18`):

    ```python
    def pasta_por_id(raiz: Path, plano_id: str) -> Path | None:
        achadas = [p.parent for p in planos_dir(raiz).glob(plano_id + "-*/" + NOME_PLANO_PASTA) if p.is_file()]
        return achadas[0] if len(achadas) == 1 else None


    def destino_rdo(pasta: Path, tarefa: str) -> Path:
        return Path(pasta) / "rdo" / f"{tarefa}.md"


    def destino_laudo(pasta: Path, tarefa: str) -> Path:
        return Path(pasta) / "laudos" / f"{tarefa}.md"


    def destino_evidencia(pasta: Path, tarefa: str) -> Path:
        return Path(pasta) / "evidencia" / f"{tarefa}.md"
    ```
  - `rdo.py`, no `close`, as duas linhas `rdo_dir = Path(args.rdo_dir) if args.rdo_dir is not None else _default_rdo_dir()` e `destino = rdo_dir / nome_arquivo` →

    ```python
        pasta_plano = _caminhos.pasta_do_plano(plano_path)
        if args.rdo_dir is None and pasta_plano is not None:
            destino = _caminhos.destino_rdo(pasta_plano, dossie.tarefa_id)
            rdo_dir = destino.parent
        else:
            rdo_dir = Path(args.rdo_dir) if args.rdo_dir is not None else _default_rdo_dir()
            destino = rdo_dir / nome_arquivo
    ```
    e a linha `    _regenerar_indice(rdo_dir)` do `close` → `    if pasta_plano is None:` seguida de `        _regenerar_indice(rdo_dir)`.
  - `rdo.py`, no `laudo`, as duas linhas `laudos_dir = Path(args.laudos_dir) if args.laudos_dir is not None else _default_laudos_dir()` e `destino = laudos_dir / f"{args.plano}-{args.tarefa}.md"` →

    ```python
        pasta_plano = _caminhos.pasta_por_id(_default_root(), args.plano) if args.laudos_dir is None else None
        if pasta_plano is not None:
            destino = _caminhos.destino_laudo(pasta_plano, args.tarefa)
            laudos_dir = destino.parent
        else:
            laudos_dir = Path(args.laudos_dir) if args.laudos_dir is not None else _default_laudos_dir()
            destino = laudos_dir / f"{args.plano}-{args.tarefa}.md"
    ```
  - `review_evidence.py` `main`, imediatamente antes da linha única `    if args.out is not None:`:

    ```python
        if args.out is None:
            pasta_plano = _caminhos.pasta_do_plano(args.plano)
            if pasta_plano is not None:
                args.out = _caminhos.destino_evidencia(pasta_plano, args.tarefa)
    ```
  - em `tests/test_caminhos.py`, o TF `test_tf_san_4_pasta_por_id_sem_colisao_de_prefixo` — com `P-1-a/plano.md` e `P-12-b/plano.md`: `P-1` → pasta `P-1-a`, `P-12` → pasta `P-12-b`, `P-9` → `None` (glob por prefixo `P-1*` acha as duas).
- **Passos:**
  1. Rodar `python -m pytest tests -q`; anotar o total.
  2. Aplicar os blocos de `Texto novo, literal`.
  3. Escrever os três TF de `Testes`.
  4. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** I-2 — com flag explícita, e para plano legado ou tíquete, destino e `INDEX.md` como hoje; nenhum teste grava no `docs/` real (todo TF isola o destino legado em `tmp_path`).
- **Não fazer:** não mover RDO, laudo ou evidência existente; não mudar o nome do RDO legado; não tocar `backlog.py` nem a doutrina.
- **Contingências:**
  1. se uma das linhas a trocar não existir literal (renomeada por `TK-66`/`TK-74`) → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha;
  2. se `_regenerar_indice(rdo_dir)` aparecer mais de uma vez em `rdo.py` → aplicar a troca só à chamada dentro do `close` e seguir.
- **Testes** (novos; entre parênteses, o valor da regra concorrente):
  - `tests/test_rdo.py::test_tf_san_13_close_grava_rdo_na_pasta_do_plano` — com `monkeypatch.setattr(rdo, "_default_rdo_dir", lambda: tmp_path / "legado")`, plano sintético (`_escrever_plano_sintetico`, cabeçalho `### T1 — Tarefa sintética [Sonnet · classe implementacao]`) em `tmp_path/"docs/plans/P-0-gama/plano.md"` e o `argv` de `close` do teste que já usa `_escrever_plano_sintetico`, sem o par `--rdo-dir`: sai 0, existe `P-0-gama/rdo/T1.md`, não existe `P-0-gama/rdo/INDEX.md`, não existe `tmp_path/"legado"` (destino legado: `legado/P-0-T1-...md` e `INDEX.md`).
  - `tests/test_rdo.py::test_tf_san_14_laudo_na_pasta_e_no_legado` — com `monkeypatch.setattr(rdo, "_default_root", lambda: tmp_path)` e `tmp_path/"docs/plans/P-0-gama/plano.md"`: `_argv_laudo(tmp_path, plano="P-0", tarefa="GAM-T1")` sem o par `--laudos-dir` sai 0 e grava `P-0-gama/laudos/GAM-T1.md`, sem criar `tmp_path/"docs/RDO"`; o mesmo com `plano="P-0749"`, `tarefa="SAN-T1"` grava `tmp_path/"docs/RDO/laudos/P-0749-SAN-T1.md"` (regra concorrente: o primeiro caso vai para `docs/RDO/laudos/P-0-GAM-T1.md`).
  - `tests/test_review_evidence.py::test_tf_san_15_evidencia_na_pasta_do_plano` — montado como `test_cli_main_ok_e_falhou` (`_init_repo_com_baseline`, `BATERIA_GUARDAS = _BATERIA_FAKE_VERDE`, `src/a.py` alterado), com o plano escrito por `_escrever_plano` em `tmp_path/"docs/plans/P-0-gama/plano.md"`: `main` sem `--out` sai 0 e grava `P-0-gama/evidencia/T1.md`; com o plano em `tmp_path/"docs/plans/P-0749-legado.md"`, `main` sem `--out` sai 0 e o conteúdo de `tmp_path/"docs/plans"` fica só `P-0-gama` e `P-0749-legado.md` (regra concorrente: nenhum arquivo no primeiro caso).
- **Verificação:**
  1. ```
     python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q -k tf_san
     ```
     → **3 passed**. **Medido antes: exit 5** (nenhum teste selecionado).
  2. ```
     pwsh -NoProfile -Command 'if (Test-Path .claude/tools/caminhos.py) { @(Select-String -LiteralPath .claude/tools/caminhos.py -SimpleMatch -Pattern "def destino_").Count } else { "ausente" }'
     ```
     → **3**. **Medido antes: 0** (2026-09-25, `caminhos.py` da entrega de `AE-1`; ausente em 2026-09-24).
  3. ```
     python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q
     ```
     → **o total destes dois arquivos no despacho + 3, nenhuma falha**. **Medido antes: 104 passed** (2026-09-25; 95 em 2026-09-24).
  4. ```
     python -m pytest tests -q
     ```
     → **o total anotado no passo 1 + 4, nenhuma falha** (três TF e o TF 4). **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).
  5. ```
     python .claude/checks/dead_code.py
     ```
     → **exit 0**. **Medido antes: exit 1** (2026-09-25, 8 achados em `caminhos.py`; exit 0 depois da `SAN-T1` redespachada).
- **Pronto quando:**
  - kit.onde se gravam os registros da tarefa — dentro da pasta do plano; tíquete e plano antigo seguem na pasta comum — Verificação 1, 2, 3
- **Fora do escopo desta tarefa:** a doutrina que cita os destinos (`SAN-T4`).

### SAN-T3a — A flag vence também no índice, e a CLI anuncia os dois destinos [Sonnet · esforço medium · classe implementacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** Corretivo da `SAN-T3` (`AE-3`): com `--rdo-dir` sobre plano em pasta o `close` volta a regenerar o `INDEX.md` do diretório da flag; o texto de ajuda de `rdo.py` e `review_evidence.py` anuncia o destino na pasta do plano ao lado do legado; a regressão `TK-62a` amputada pelo TF 15 volta inteira.
- **Fundamento:** DSA-21, DSA-9; I-2; `AE-3`.
- **Depende de:** `SAN-T3`
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py` e dois arquivos de teste. Nenhuma mudança de destino além do `INDEX.md` com flag.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `.claude/tools/review_evidence.py`
  - `tests/test_rdo.py`
  - `tests/test_review_evidence.py`
- **Texto novo, literal** (cada texto antigo aparece uma vez no seu arquivo, medido em 2026-09-25):
  - `rdo.py`, no `close`: `    if pasta_plano is None:` (linha seguida de `        _regenerar_indice(rdo_dir)`) → `    if args.rdo_dir is not None or pasta_plano is None:`.
  - `rdo.py`: `        "--rdo-dir", default=None, help="Diretório de saída (default: docs/RDO)."` →

    ```python
            "--rdo-dir",
            default=None,
            help="Diretório de saída (default: <pasta-do-plano>/rdo/ para plano em pasta, sem INDEX.md; docs/RDO para plano legado ou tíquete).",
    ```
  - `rdo.py`: `        "--laudos-dir", default=None, help="Diretório de saída (default: docs/RDO/laudos)."` →

    ```python
            "--laudos-dir",
            default=None,
            help="Diretório de saída (default: <pasta-do-plano>/laudos/ para plano em pasta; docs/RDO/laudos para plano legado ou tíquete).",
    ```
  - `rdo.py`: `        help="Calcula o laudo e grava documento próprio em docs/RDO/laudos/<plano>-<tarefa>.md (T18).",` → `        help="Calcula o laudo e grava documento próprio em <pasta-do-plano>/laudos/<tarefa>.md (plano em pasta) ou docs/RDO/laudos/<plano>-<tarefa>.md (T18).",`
  - `rdo.py`, primeira linha da docstring de `cmd_laudo`, `    """EXA-T18: laudo grava documento próprio em `docs/RDO/laudos/<plano>-<tarefa>.md` — não` → as duas linhas

    ```python
        """EXA-T18/SAN-T3: laudo grava documento próprio em `<pasta-do-plano>/laudos/<tarefa>.md` (plano
        em pasta, sem `--laudos-dir`) ou em `docs/RDO/laudos/<plano>-<tarefa>.md` (plano legado) — não
    ```
  - `review_evidence.py`: `        "--out", type=Path, default=None, help="Também grava o documento neste caminho (escrita atômica)."` →

    ```python
            "--out",
            type=Path,
            default=None,
            help="Também grava o documento neste caminho (escrita atômica); sem ele, plano em pasta grava em <pasta-do-plano>/evidencia/<tarefa>.md.",
    ```
  - `tests/test_review_evidence.py`: as seis linhas de `    codigo_falho = review_evidence.main(` a `    assert "review_evidence: FALHOU" in saida_falha.err` (e a linha em branco que as precede) saem do fim de `test_tf_san_15_evidencia_na_pasta_do_plano`, que passa a terminar no `    ]` da comparação `sorted(...)`, e voltam ao fim de `test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica`, depois de `    assert "review_evidence: OK" in saida.out`, precedidas de uma linha em branco — a forma de `git show HEAD:tests/test_review_evidence.py`, linhas 218-228.
- **Passos:**
  1. Rodar `python -m pytest tests -q`; anotar o total.
  2. Aplicar os blocos de `Texto novo, literal`.
  3. Acrescentar ao fim de `tests/test_rdo.py` o TR de `Testes`.
  4. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** I-2 — sem flag, destino e índice como a `SAN-T3` entregou; nenhum teste grava no `docs/` real.
- **Não fazer:** não mudar a lógica de destino do `close`, do `laudo` nem do `review_evidence` (só a condição do índice); não tocar `caminhos.py`, `backlog.py` nem a doutrina (`SAN-T4`); não reescrever o TF 15 além de lhe tirar a cauda.
- **Contingências:**
  1. se um texto antigo não aparecer literal, ou aparecer mais de uma vez → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha.
- **Testes** (novo; entre parênteses, o valor da regra concorrente):
  - `tests/test_rdo.py::test_tr_san_19_close_com_rdo_dir_sobre_plano_em_pasta_vence_a_flag` — sem monkeypatch; plano sintético (`_escrever_plano_sintetico`, cabeçalho `### T1 — Tarefa sintética [Sonnet · classe implementacao]`) em `tmp_path/"docs/plans/P-0-gama/plano.md"` e o `argv` de `close` do `test_tf_san_13_close_grava_rdo_na_pasta_do_plano` acrescido de `"--rdo-dir", str(tmp_path / "flag")`: sai 0, existe `flag/INDEX.md`, `flag.glob("P-0-T1-*.md")` acha exatamente 1, não existe `P-0-gama/rdo` (regra concorrente: sem `INDEX.md` — medido, o TR falha no código da `SAN-T3`).
- **Verificação:**
  1. ```
     python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q -k "tf_san or tr_san"
     ```
     → **4 passed**. **Medido antes: 3 passed** (2026-09-25).
  2. ```
     python -c "import ast,pathlib;t=pathlib.Path('tests/test_review_evidence.py').read_text(encoding='utf-8');f={n.name:ast.get_source_segment(t,n) for n in ast.parse(t).body if isinstance(n,ast.FunctionDef)};print(int('codigo_falho' in f['test_tf_san_15_evidencia_na_pasta_do_plano']), int('codigo_falho' in f['test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica']))"
     ```
     → **`0 1`** (Git Bash). **Medido antes: `1 0`** (2026-09-25).
  3. ```
     pwsh -NoProfile -Command '@(Select-String -LiteralPath .claude/tools/rdo.py,.claude/tools/review_evidence.py -SimpleMatch -Pattern "<pasta-do-plano>").Count'
     ```
     → **5**. **Medido antes: 0** (2026-09-25).
  4. ```
     python .claude/tools/rdo.py close --help > /dev/null && python .claude/tools/rdo.py laudo --help > /dev/null && python .claude/tools/review_evidence.py --help > /dev/null
     ```
     → **exit 0**. **Medido antes: exit 0**.
  5. ```
     python -m pytest tests -q
     ```
     → **o total anotado no passo 1 + 1, nenhuma falha**. **Medido antes: 351 passed** (2026-09-25; 352 com o reparo aplicado numa cópia da árvore).
  6. ```
     python .claude/checks/dead_code.py
     ```
     → **exit 0**. **Medido antes: exit 0**.
- **Pronto quando:**
  - kit.onde se gravam os registros da tarefa — flag explícita vence também no índice, e a CLI anuncia a pasta do plano ao lado do destino legado — Verificação 1, 2, 3
- **Fora do escopo desta tarefa:** a doutrina que cita os destinos (`SAN-T4`); a evidência sem os não rastreados anteriores ao despacho (`AE-3` (c), fora do plano).

### SAN-T4 — A doutrina ensina a pasta, o estado.tsv e a contagem em zero [Sonnet · esforço medium · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O redator da doutrina reescreve o que o kit ensina sobre plano: pasta própria com nomes fixos, estado na tabela que o planejador cria ao registrar o plano, e projeto novo nascendo com a contagem em zero.
- **Fundamento:** DSA-3, DSA-4, DSA-6, DSA-13, DSA-14; §3.1, §3.2, §3.4; F-6; I-4.
- **Depende de:** `SAN-T3a`
- **Operação do modelo:** `OP-4`
  - OP-4: O redator da doutrina reescreve o que o kit ensina sobre plano: pasta própria com nomes fixos, estado na tabela que o planejador cria ao registrar o plano, e projeto novo nascendo com a contagem em zero.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** doutrina do kit, só residências (I-4: nada em `~/.claude/`). Cada texto antigo abaixo aparece uma vez no seu arquivo, salvo onde indicado (medido em 2026-09-24), e se troca com `Edit`.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
  - `.claude/agents/pantonic-planner.md`
  - `.claude/skills/bootstrap-pantonic/SKILL.md`
  - `.claude/agents/pantonic-reviewer.md`
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/agents/pantonic-consultant.md`
  - `.claude/skills/entrega-de-encerramento/SKILL.md`
- **Texto novo, literal** (antigo → novo; `↵` é quebra de linha e o recuo de continuação é o do bullet):

  ```text
  [G1] GOVERNANCA.md
  plano em `docs/plans/P-<MMDD>-<slug>.md` e apensa
  → plano em `docs/plans/P-<n>-<slug>/plano.md` e apensa

  [G2] GOVERNANCA.md
  na próxima sessão que o utilizar.
  → na próxima sessão que o utilizar.↵
  - **Pasta do plano** — plano novo nasce em `docs/plans/P-<n>-<slug>/`, com tudo o que é dele↵
    dentro: `plano.md` (seções e cards), `estado.tsv` (estado de máquina do plano e das tarefas;↵
    esquema na skill `diario-de-obras`), `rdo/<tarefa>.md`, `laudos/<tarefa>.md`,↵
    `evidencia/<tarefa>.md` e, quando existirem, `campanha.md`, `cenario.md`, `veredito.md`,↵
    `viabilidade.md`, `operacoes.md` (documento de encerramento) e `entrega.md` (entrega aceita).↵
    O planejador grava `estado.tsv` ao registrar o plano; depois só `backlog.py` o escreve. Plano↵
    legado (`docs/plans/P-NNNN-<slug>.md`, arquivo único) segue lido como está; nada dele se move.

  [G3] GOVERNANCA.md
  O **RDO** (`docs/RDO/<plano>-<tarefa>-<slug>.md`,
  → O **RDO** (`docs/plans/P-<n>-<slug>/rdo/<tarefa>.md`; plano legado e tíquete em `docs/RDO/`,

  [G4] GOVERNANCA.md
  e preserva a cauda.
  → e preserva a cauda. Tarefa de plano em pasta não tem este bullet: o estado dela é a linha dela em `estado.tsv`.

  [G5] GOVERNANCA.md (duas linhas)
     1. **Nomenclatura sequencial.** `P-NNNN-<slug>.md`, com `NNNN` contador global monotônico↵
        (não a data), zero-padded, **nunca reusado**; próximo id = maior registrado no `_INBOX.md` + 1.
  →    1. **Nomenclatura sequencial.** `P-<n>-<slug>/plano.md`, com `<n>` contador monotônico do↵
        repositório (não a data), começando em `0` no projeto novo, sem zeros à esquerda, **nunca↵
        reusado**; próximo id = maior registrado no `_INBOX.md` + 1. O hub segue o contador legado↵
        (`P-0750`…), na largura que ele já tem.

  [G6] GOVERNANCA.md (três ocorrências: Edit com replace_all)
  (`P-NNNN`)
  → (`P-<n>`)

  [G7] GOVERNANCA.md
  `<P-NNNN> — <AAAA-MM-DD>`
  → `P-<n> — <AAAA-MM-DD>`

  [D1] .claude/skills/diario-de-obras/SKILL.md
  | plano | `docs/plans/P-NNNN-<slug>.md` |
  → | plano em pasta | `docs/plans/P-<n>-<slug>/plano.md` | `# P-<n> — <título>` (linha 1) | nas 20 primeiras linhas: `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; **sem** linha `**Status:**` — o estado é a linha `plano` de `estado.tsv`, na mesma pasta |↵
  | plano legado | `docs/plans/P-NNNN-<slug>.md` |

  [D2] .claude/skills/diario-de-obras/SKILL.md (duas trocas na linha da tarefa de plano)
  | 1º bullet: `- **Status:**
  → | plano legado: 1º bullet `- **Status:**
  apensados pelo instrumento |
  → apensados pelo instrumento; plano em pasta: sem bullet de Status nem de Notas de execução — estado, razão e nota na linha da tarefa em `estado.tsv` |

  [D3] .claude/skills/diario-de-obras/SKILL.md
  - `P-NNNN` (`<estado>`
  → - `P-<n>` (`<estado>`

  [D4] .claude/skills/diario-de-obras/SKILL.md
  contém um caminho `docs/plans/P-NNNN-<slug>.md` (o resto é livre).
  → contém um caminho `docs/plans/P-<n>-<slug>/plano.md` ou, legado, `docs/plans/P-NNNN-<slug>.md` (o resto é livre).

  [D5] .claude/skills/diario-de-obras/SKILL.md
  Contador: `**Próximo id de plano: P-NNNN.**` — `drain` o recalcula como `max(id visto) + 1`.
  → Contador: `**Próximo id de plano: P-<n>.**` — `drain` o recalcula como `max(id visto) + 1`, na largura de dígitos que o contador já tem (projeto novo: `P-0`, `P-1`…; hub: `P-0750`…).

  [D6] .claude/skills/diario-de-obras/SKILL.md
  ### Modelo de domínio (seção do plano)
  → ### Estado do plano em pasta (`estado.tsv`)↵
  ↵
  `docs/plans/P-<n>-<slug>/estado.tsv`, separador TAB (escrito `<TAB>` aqui). Primeira linha↵
  `id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota`; depois uma linha por item, estado corrente,↵
  reescrita no lugar. `id` = `P-<n>` na linha do plano (a primeira) ou o id da tarefa; `tipo` ∈↵
  {`plano`, `tarefa`}; `status` no vocabulário acima; `razao` ∈ {`-`, `dependencia`, `premissa`};↵
  `data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo ao registrar↵
  o plano; depois só `backlog.py status` o reescreve. `check` acusa `C-13` (card sem linha, linha↵
  sem card, arquivo ausente ou fora do esquema) e `C-14` (linha `**Status:**` em `plano.md`).↵
  Busca sem leitura: `rg "^<id>\t" docs/plans/*/estado.tsv`.↵
  ↵
  ### Modelo de domínio (seção do plano)

  [D7] .claude/skills/diario-de-obras/SKILL.md
  para um `docs/plans/P-NNNN-<slug>.md` gravado
  → para um `docs/plans/P-<n>-<slug>/plano.md` gravado

  [D8] .claude/skills/diario-de-obras/SKILL.md
  grava seu plano completo em `docs/plans/P-NNNN-<slug>.md` e apensa
  → grava seu plano completo em `docs/plans/P-<n>-<slug>/plano.md` e apensa

  [P1] .claude/agents/pantonic-planner.md
  - Plano novo: `docs/plans/P-NNNN-<slug>.md` + uma linha em `docs/plans/_INBOX.md`; `NNNN` = id
  → - Plano novo: `docs/plans/P-<n>-<slug>/plano.md` + `estado.tsv` na mesma pasta + uma linha em `docs/plans/_INBOX.md`; `<n>` = id

  [P2] .claude/agents/pantonic-planner.md
  Grave `docs/plans/P-NNNN-<slug>.md` **sem a §1
  → Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1

  [P3] .claude/agents/pantonic-planner.md
  # P-NNNN — <título>
  → # P-<n> — <título>

  [P4] .claude/agents/pantonic-planner.md
  a materializa na linha `**Status:**` do card
  → a materializa na coluna `nota` da linha da tarefa em `estado.tsv` (plano legado: na linha `**Status:**` do card)

  [P5] .claude/agents/pantonic-planner.md
  apense a linha ao `_INBOX.md` e atualize
  → grave `estado.tsv` na pasta do plano (linha do plano e uma linha por card, esquema da skill `diario-de-obras`), apense a linha ao `_INBOX.md` e atualize

  [B1] .claude/skills/bootstrap-pantonic/SKILL.md
  docs/plans/      P-NNNN-<slug>.md (planos completos) + _INBOX.md (append-only, drenado
  → docs/plans/      P-<n>-<slug>/ (uma pasta por plano, P-0 primeiro) + _INBOX.md (append-only, drenado

  [B2] .claude/skills/bootstrap-pantonic/SKILL.md
  - `docs/plans/_INBOX.md` criado vazio.
  → - `docs/plans/_INBOX.md` criado com uma linha só: `**Próximo id de plano: P-0.**`.

  [R1] .claude/agents/pantonic-reviewer.md e .claude/skills/scrum-master/SKILL.md (uma em cada)
      --out docs/RDO/evidencia/<plano>-<ID>.md
  →     --out docs/RDO/evidencia/<plano>-<ID>.md   # só plano legado; plano em pasta: sem --out, grava docs/plans/P-<n>-<slug>/evidencia/<ID>.md

  [R2] .claude/agents/pantonic-reviewer.md
  em `docs/RDO/laudos/<plano>-<tarefa>.md`.
  → em `docs/plans/P-<n>-<slug>/laudos/<tarefa>.md` (plano legado: `docs/RDO/laudos/<plano>-<tarefa>.md`).

  [C1] .claude/agents/pantonic-consultant.md (duas ocorrências: replace_all) e .claude/skills/scrum-master/SKILL.md (uma)
  `docs/plans/_CENARIO-<plano>.md`
  → `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`)

  [N1] .claude/skills/entrega-de-encerramento/SKILL.md
  **Residência:** `docs/OPERACOES_AS_IS.md` quando
  → **Residência:** `docs/plans/P-<n>-<slug>/operacoes.md`, na pasta do plano. Plano legado: `docs/OPERACOES_AS_IS.md` quando
  ```
- **Passos:**
  1. Rodar a Verificação 1 e 2 e conferir os valores "antes".
  2. Aplicar as trocas `G1`..`N1`, na ordem, com `Edit`.
  3. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** I-4 — nenhum arquivo em `~/.claude/`; só as trocas listadas; menção que descreve o legado fica (é o que as trocas marcam `legado`).
- **Não fazer:** não editar `README.md` (`SAN-T6`) nem escrever a regra do artefato de humano (`SAN-T5`); não reescrever menção a plano histórico (`P-0747`, `P-0722`); não renumerar seção.
- **Contingências:**
  1. se um texto antigo não aparecer, ou aparecer mais vezes que o indicado, no arquivo da troca (editado por `TK-72`/`TK-73` no intervalo) → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca;
  2. se a Verificação 4 falhar num teste que confere texto de agente ou skill → parar e sinalizar `blocked` razão `premissa`, devolvendo o teste.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/agents/pantonic-planner.md",".claude/skills/bootstrap-pantonic/SKILL.md",".claude/agents/pantonic-consultant.md",".claude/skills/scrum-master/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "P-<MMDD>-<slug>","P-NNNN","a materializa na linha","criado vazio.","docs/RDO/<plano>-<tarefa>-<slug>.md","docs/plans/_CENARIO").Count })) -join " / "'
     ```
     → **1 / 0 / 0 / 0 / 0** (o `1` é a menção ao legado da troca `G2`). **Medido antes: 7 / 4 / 2 / 2 / 1**.
  2. ```
     pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/agents/pantonic-planner.md",".claude/agents/pantonic-reviewer.md",".claude/agents/pantonic-consultant.md",".claude/skills/diario-de-obras/SKILL.md",".claude/skills/bootstrap-pantonic/SKILL.md",".claude/skills/scrum-master/SKILL.md",".claude/skills/entrega-de-encerramento/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "P-<n>-<slug>/").Count })) -join " / "'
     ```
     → **4 / 2 / 2 / 2 / 5 / 1 / 2 / 1**. **Medido antes: 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0**.
  3. ```
     pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/agents/pantonic-planner.md",".claude/skills/diario-de-obras/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "estado.tsv").Count }) + @(@(Select-String -LiteralPath .claude/skills/bootstrap-pantonic/SKILL.md -SimpleMatch -Pattern "P-0.**").Count)) -join " / "'
     ```
     → **≥ 1 em cada um dos quatro**. **Medido antes: 0 / 0 / 0 / 0**.
  4. ```
     python -m pytest tests -q
     ```
     → **o total do despacho, nenhuma falha**. **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).
- **Pronto quando:**
  - kit.o que a doutrina ensina — pasta por plano, estado na tabela, contagem em zero no projeto novo — Verificação 1, 2, 3
  - kit.número do plano — projeto novo começa em zero e soma um; aqui a contagem segue de onde está — Verificação 3
- **Fora do escopo desta tarefa:** a regra do artefato de humano (`SAN-T5`); o `README.md` (`SAN-T6`); a cópia `~/.claude/CLAUDE.md` (Controle 1.1, `TK-68`).

### SAN-T2a — Projeto novo com contador em P-0 e nenhum plano passa no check [Sonnet · esforço low · classe implementacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** Corretivo da `SAN-T2` (`AE-4`): o estado de projeto novo que o bootstrap cria (`_INBOX.md` só com `**Próximo id de plano: P-0.**`, `docs/plans/` sem plano) deixa de acusar `C-10`; com plano presente, `C-10` segue como está.
- **Fundamento:** DSA-22, DSA-3, DSA-14; I-2; `AE-4`.
- **Depende de:** `SAN-T2`
- **Operação do modelo:** `OP-2`
  - OP-2: O mantenedor do backlog faz o instrumento de backlog guardar o estado de plano e de tarefa numa tabela de máquina na pasta do plano, contar o próximo número a partir do zero em projeto novo e acusar plano novo com estado escrito no texto.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/backlog.py` (só o bloco `C-10` de `check`) e `tests/test_backlog.py`.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Texto novo, literal** (o texto antigo aparece uma vez, medido em 2026-09-25):
  - `backlog.py`, em `check`, as duas linhas

    ```python
                maior = max(ids_planos) if ids_planos else 0
                if contador <= maior:
    ```
    →

    ```python
                # Sem plano presente (projeto novo, `DSA-14`), todo contador vale, `P-0` inclusive.
                if ids_planos and contador <= max(ids_planos):
    ```
- **Passos:**
  1. Antes de qualquer edição, copiar o código de referência para `$env:TEMP` (`DSA-20`) e anotar o total da suíte:

     ```
     pwsh -NoProfile -Command 'New-Item -ItemType Directory -Force "$env:TEMP/san-t2a-ref" | Out-Null; Copy-Item .claude/tools/backlog.py,.claude/tools/caminhos.py "$env:TEMP/san-t2a-ref/"; "copiado"'
     python -m pytest tests -q
     ```
  2. Aplicar o bloco de `Texto novo, literal`.
  3. Acrescentar ao fim de `tests/test_backlog.py` o TF de `Testes`.
  4. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** I-2 — com plano presente, `C-10` e a sua mensagem não mudam (`test_tf_san_12_c10_preserva_largura` e a fixture `contador_inbox` seguem verdes, inalterados).
- **Não fazer:** não tocar `transacionar_drain`, `caminhos.py`, a doutrina nem fixture existente; não criar fixture nova (o TF monta o estado em `tmp_path`).
- **Contingências:**
  1. se o texto antigo não aparecer literal, ou aparecer mais de uma vez → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha.
- **Testes** (novo; entre parênteses, o valor da regra concorrente):
  - `tests/test_backlog.py::test_tf_san_20_c10_projeto_novo_sem_plano` — `repo = _copiar_fixture(_FIXTURE_PASTA, tmp_path / "repo")`; `shutil.rmtree(repo / "docs" / "plans" / "P-0-gama")`; tirar de `docs/DIARIO_DE_OBRAS.md` a linha que começa por `| P-0-GAM ` (como no `test_tf_san_11_drain_preserva_largura`); `docs/plans/_INBOX.md` = `"**Próximo id de plano: P-0.**\n"`; `backlog.check(backlog.carregar(repo), inbox_planos=inbox_path, repo=repo) == []` (regra concorrente: uma violação `C-10` `contador aponta para P-0, já presente em docs/plans/` — medido, o TF falha no código da `SAN-T2`).
- **Verificação:**
  1. ```
     python -m pytest tests/test_backlog.py -q -k tf_san
     ```
     → **8 passed**. **Medido antes: 7 passed** (2026-09-25; conta TF de cards anteriores, `AE-2`).
  2. ```
     pwsh -NoProfile -Command '@(Select-String -LiteralPath .claude/tools/backlog.py -SimpleMatch -Pattern "if ids_planos and contador <= max(ids_planos):").Count'
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command '$r = "$env:TEMP/san-t2a-ref/backlog.py"; $a = @(python $r check --repo . 2>$null) + @(python $r next --repo .); $b = @(python .claude/tools/backlog.py check --repo . 2>$null) + @(python .claude/tools/backlog.py next --repo .); if (($a -join "|") -ne ($b -join "|")) { "DIFERE"; exit 1 } else { "IGUAL" }'
     ```
     → **IGUAL**. **Medido antes: IGUAL** (2026-09-25, reparo aplicado numa cópia; mede-se depois do passo 1).
  4. ```
     python -m pytest tests -q
     ```
     → **o total anotado no passo 1 + 1, nenhuma falha**. **Medido antes: 352 passed** (2026-09-25; 353 com o reparo numa cópia da árvore).
  5. ```
     python .claude/checks/dead_code.py
     ```
     → **exit 0**. **Medido antes: exit 0**.
- **Pronto quando:**
  - kit.número do plano — projeto novo começa em zero e soma um; aqui a contagem segue de onde está — Verificação 1, 2, 3
- **Fora do escopo desta tarefa:** a doutrina do bootstrap (`SAN-T4`, entregue); o `README.md` (`SAN-T6`).

### SAN-T5 — A regra do artefato de humano mínimo, uma vez só [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O redator da doutrina escreve, uma vez só, a regra de que todo artefato de humano é o menor possível, e os limites de tamanho que já existem passam a apontar para ela.
- **Fundamento:** DSA-11; §3.3; F-7; I-5.
- **Depende de:** `SAN-T4`
- **Operação do modelo:** `OP-5`
  - OP-5: O redator da doutrina escreve, uma vez só, a regra de que todo artefato de humano é o menor possível, e os limites de tamanho que já existem passam a apontar para ela.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.
- **Camada e fronteira:** doutrina do kit; a regra reside em `GOVERNANCA.md` §4.2, logo depois do bullet *Fechamento enxuto*, e em nenhum outro lugar; os dois limites locais recebem ponteiro.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
- **Texto novo, literal** (antigo → novo; `↵` é quebra de linha):

  ```text
  [H1] GOVERNANCA.md
  é o defeito que esta regra fecha.
  → é o defeito que esta regra fecha.↵
  - **Artefato de humano mínimo** — artefato **de máquina** é o que um instrumento ou um agente lê↵
    por gramática (TSV, card); artefato **de humano** é o que o dono lê (§0, §1 e §3 do plano,↵
    rodada de decisões, handover, diretiva e índice do diário, documento de encerramento). Todo↵
    artefato de humano é o menor possível: (a) não repete dado cuja residência é artefato de máquina↵
    — no máximo o ponteiro; (b) não narra o que o git, o RDO ou um TSV já registram; (c) frase que↵
    não serve a decisão ou validação do dono sai. O card segue `G-EXECREADY`: a autossuficiência do↵
    executor frio prevalece sobre (a)–(c). Os limites locais de tamanho (handover, célula do índice)↵
    são aplicações desta regra.

  [H2] GOVERNANCA.md
  e o handover ao dono cabe em ≤ 8 linhas com o ponteiro.
  → e o handover ao dono cabe em ≤ 8 linhas com o ponteiro (aplicação de *Artefato de humano mínimo*, abaixo).

  [H3] .claude/skills/diario-de-obras/SKILL.md
  fica travada em ≤ ~1-2 frases + status + ponteiro, ponto final;
  → fica travada em ≤ ~1-2 frases + status + ponteiro, ponto final (aplicação de *Artefato de humano mínimo*, `GOVERNANCA.md` §4.2);
  ```
- **Passos:**
  1. Rodar a Verificação 1 e 2 e conferir os valores "antes".
  2. Aplicar `H1`, `H2`, `H3` com `Edit`.
  3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-5 — o texto da regra entra uma vez; em outro lugar, só o ponteiro.
- **Não fazer:** não criar item novo em `GOVERNANCA.md` §7; não copiar a regra para agente, skill ou `README.md`; não alterar o número `≤ 8`.
- **Contingências:**
  1. se um texto antigo não aparecer exatamente uma vez no arquivo → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/skills/diario-de-obras/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "Artefato de humano mínimo").Count })) -join " / "'
     ```
     → **2 / 1**. **Medido antes: 0 / 0**.
  2. ```
     pwsh -NoProfile -Command '"total=" + @(Select-String -Path "GOVERNANCA.md","README.md",".claude/agents/*.md",".claude/skills/*/SKILL.md" -SimpleMatch -Pattern "não repete dado cuja residência é artefato de máquina").Count'
     ```
     → **total=1** (a linha da regra em `GOVERNANCA.md`). **Medido antes: total=0**.
  3. ```
     python -m pytest tests -q
     ```
     → **o total do despacho, nenhuma falha**. **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).
- **Pronto quando:**
  - kit.regra do artefato de humano — uma regra única: texto para o dono é o menor possível e não repete o que já está em tabela de máquina — Verificação 1, 2
- **Fora do escopo desta tarefa:** a menção no `README.md` (`SAN-T6`).

### SAN-T6 — A porta de entrada descreve a pasta, a tabela e o texto mínimo [Sonnet + dono · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo.
- **Fundamento:** DSA-3, DSA-4, DSA-5, DSA-11; G-README (a revisão do `README.md` fecha a sprint).
- **Depende de:** `SAN-T5`
- **Operação do modelo:** `OP-6`
  - OP-6: O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** só o `README.md`; ele aponta para a regra, não a copia (I-5).
- **Arquivos-alvo:**
  - `README.md`
- **Texto novo, literal** (antigo → novo; `↵` é quebra de linha):

  ```text
  [M1] README.md
  - **Plano `P-NNNN`** — o planejamento consolidado de uma rota de trabalho, em formato de checklist,
  → - **Plano `P-<n>`** — o planejamento consolidado de uma rota de trabalho, numa pasta própria (`docs/plans/P-<n>-<slug>/`: `plano.md`, `estado.tsv` e os registros das tarefas), em formato de checklist,

  [M2] README.md
  (§8 desta página).
  → (§8 desta página).↵
  - **Artefato de humano mínimo** — o que o dono lê (plano, handover, diário) é o menor possível e↵
    aponta para o dado de máquina em vez de repeti-lo. Onde a regra mora: `GOVERNANCA.md` §4.2.

  [M3] README.md
  cada uma com o seu plano `P-NNNN`;
  → cada uma com o seu plano `P-<n>`;

  [M4] README.md (duas linhas)
  1. **Nomenclatura sequencial.** `P-NNNN-<slug>.md`, com `NNNN` sendo um contador global monotônico,↵
     zero-padded e **nunca reusado**. O próximo id é o maior registrado no
  → 1. **Nomenclatura sequencial.** `P-<n>-<slug>/plano.md`, com `<n>` sendo um contador monotônico do↵
     repositório, começando em `0` no projeto novo, sem zeros à esquerda e **nunca reusado** (o hub↵
     segue o contador legado, `P-0750`…). O próximo id é o maior registrado no
  ```
- **Passos:**
  1. Rodar a Verificação 1 e 2 e conferir os valores "antes".
  2. Aplicar `M1`..`M4` com `Edit`.
  3. Rodar a Verificação 1 a 3.
  4. Devolver ao chamador as quatro trocas aplicadas, para o veredito do dono.
- **Restrições desta tarefa:** I-5 — o `README.md` aponta para a regra, não a copia; as contagens que o `README.md` anuncia (agentes, skills, guardrails) não mudam.
- **Não fazer:** não editar outra seção do `README.md`; não tocar `GOVERNANCA.md` nem a doutrina.
- **Contingências:**
  1. se um texto antigo não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca;
  2. se `check-readme.ps1` sair diferente de 0 → corrigir a troca que o quebrou; persistindo → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída.
- **Testes:** nenhum novo; guarda `check-readme.ps1`.
- **Verificação:**
  1. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0, com a linha que começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`**. **Medido antes: check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)**.
  2. ```
     pwsh -NoProfile -Command '(@(foreach ($p in "P-NNNN","P-<n>-<slug>/","Artefato de humano mínimo") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $p).Count })) -join " / "'
     ```
     → **0 / 2 / 1**. **Medido antes: 3 / 0 / 0**.
  3. ```
     python -m pytest tests -q
     ```
     → **o total do despacho, nenhuma falha**. **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).
  4. ```
     veredito do dono sobre as trocas M1..M4
     ```
     → **go**. **Medido antes: sem veredito**. **Aferição: manual**.
- **Pronto quando:**
  - kit.porta de entrada — descreve pasta por plano, tabela de estado e a regra do texto mínimo — Verificação 1, 2, 4
- **Fora do escopo desta tarefa:** qualquer outra seção do `README.md`.

### SAN-T6a — O glossário diz o contador como a regra o diz [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** Corretivo da `SAN-T6` (`AE-5` (b)): no glossário do `README.md`, o item *Plano `P-<n>`* deixa de chamar o contador de "global" e passa a dizê-lo como o item 1 do `G-PLANREADY` (`M4`) e `GOVERNANCA.md` §7 item 11: contador monotônico do repositório.
- **Fundamento:** DSA-23, DSA-3; I-5; `AE-5`.
- **Depende de:** `SAN-T6`
- **Operação do modelo:** `OP-6`
  - OP-6: O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** só o `README.md`, uma linha do glossário (a linha 159 em 2026-09-25).
- **Arquivos-alvo:**
  - `README.md`
- **Texto novo, literal** (antigo → novo; o texto antigo aparece uma vez, medido em 2026-09-25; **sem quebra de linha nova e sem refluxo do parágrafo**: a linha só fica 8 caracteres mais longa):

  ```text
  [M5] README.md
  identificado por contador global monotônico e
  → identificado por contador monotônico do repositório e
  ```
- **Passos:**
  1. Rodar a Verificação 1 e 2 e conferir os valores "antes".
  2. Aplicar `M5` com `Edit`.
  3. Rodar a Verificação 1 a 3.
  4. Devolver ao chamador a troca aplicada: o veredito do dono sobre `M5` sobe com o de `M1`..`M4` no relatório de encerramento (DSA-23) e não é critério desta revisão.
- **Restrições desta tarefa:** I-5; as contagens que o `README.md` anuncia não mudam.
- **Não fazer:** não refluir o parágrafo; não editar outra linha do `README.md`; não tocar `GOVERNANCA.md` nem a doutrina.
- **Contingências:**
  1. se o texto antigo não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo a contagem.
- **Testes:** nenhum novo; guarda `check-readme.ps1`.
- **Verificação:**
  1. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0, com a linha que começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`**. **Medido antes: exit 0, a mesma linha** (2026-09-25; e com `M5` aplicado numa cópia, `-Root` em `$env:TEMP`).
  2. ```
     pwsh -NoProfile -Command '(@(foreach ($p in "contador global monot","identificado por contador monotônico do repositório") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $p).Count })) -join " / "'
     ```
     → **0 / 1**. **Medido antes: 1 / 0** (2026-09-25; `0 / 1` com `M5` aplicado numa cópia).
  3. ```
     python -m pytest tests -q
     ```
     → **o total do despacho, nenhuma falha**. **Medido antes: 353 passed** (2026-09-25).
- **Pronto quando:**
  - kit.porta de entrada — descreve pasta por plano, tabela de estado e a regra do texto mínimo — Verificação 1, 2
- **Fora do escopo desta tarefa:** qualquer outra linha do `README.md`; a régua de autoria (`AE-5` (a) e (c), `TK-72`).

### SAN-T6b — As decisões estruturantes dizem o contador como a regra o diz [Sonnet · esforço low · classe redacao]
- **Status:** `done` · 2026-09-25
- **Objetivo:** Corretivo da `SAN-T6a` (`AE-6`): na tabela da §14 do `README.md` (*Decisões estruturantes*), a linha *Plano tem contador sequencial global no nome* deixa de chamar o contador de "global" e passa a dizê-lo como o glossário (`M5`) e `GOVERNANCA.md` §7 item 11: do repositório.
- **Fundamento:** DSA-24, DSA-23, DSA-3; I-5; `AE-6`.
- **Depende de:** `SAN-T6a`
- **Operação do modelo:** `OP-6`
  - OP-6: O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo.
  - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** só o `README.md`, a primeira célula de uma linha da tabela da §14 (a linha 1045 em 2026-09-25).
- **Arquivos-alvo:**
  - `README.md`
- **Texto novo, literal** (antigo → novo; o texto antigo aparece uma vez, medido em 2026-09-25; **sem quebra de linha nova**: a linha da tabela continua uma só, e a segunda célula não muda):

  ```text
  [M6] README.md
  | **Plano tem contador sequencial global no nome** |
  → | **Plano tem contador sequencial do repositório no nome** |
  ```
- **Passos:**
  1. Rodar a Verificação 1 e 2 e conferir os valores "antes".
  2. Aplicar `M6` com `Edit`.
  3. Rodar a Verificação 1 a 3.
  4. Devolver ao chamador a troca aplicada: o veredito do dono sobre `M6` sobe com o de `M1`..`M5` no relatório de encerramento (DSA-24) e não é critério desta revisão.
- **Restrições desta tarefa:** I-5; as contagens que o `README.md` anuncia não mudam.
- **Não fazer:** não editar outra linha nem a segunda célula; não tocar `GOVERNANCA.md` nem a doutrina.
- **Contingências:**
  1. se o texto antigo não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo a contagem.
- **Testes:** nenhum novo; guarda `check-readme.ps1`.
- **Verificação:**
  1. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0, com a linha que começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`**. **Medido antes: exit 0, a mesma linha** (2026-09-25; e com `M6` aplicado numa cópia da árvore, `-Root` em `$env:TEMP`).
  2. ```
     pwsh -NoProfile -Command '(@(foreach ($p in "contador sequencial global","contador global","Plano tem contador sequencial do repositório no nome") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $p).Count })) -join " / "'
     ```
     → **0 / 0 / 1**. **Medido antes: 1 / 0 / 0** (2026-09-25; `0 / 0 / 1` com `M6` aplicado numa cópia).
  3. ```
     python -m pytest tests -q
     ```
     → **o total do despacho, nenhuma falha**. **Medido antes: 353 passed** (2026-09-25).
- **Pronto quando:**
  - kit.porta de entrada — descreve pasta por plano, tabela de estado e a regra do texto mínimo — Verificação 1, 2
- **Fora do escopo desta tarefa:** qualquer outra linha do `README.md`; `contador sequencial` sem "global" (`README.md:624`, `GOVERNANCA.md:867`) fica — não contradiz a regra.

## 6. Ordem de execução

Linear: `SAN-T1` → `SAN-T2` → `SAN-T3` → `SAN-T3a` → `SAN-T4` → `SAN-T2a` → `SAN-T5` → `SAN-T6` → `SAN-T6a` → `SAN-T6b`. Externas: `SAN-T1` espera
`TK-65`, `TK-66`, `TK-74` (DSA-16). Nada roda em paralelo: T1..T3 editam `caminhos.py` em sequência,
e T4..T6 editam a doutrina que cita o que T1..T3 entregam.

## 7. Fora de escopo (explícito)

- Renumerar, mover ou condensar legado do hub, inclusive o cabeçalho do diário (DSA-2).
- Estado de tíquete `TK-*`: segue no diário e em `docs/RDO/`.
- Distribuir `.claude/tools/` ao herdeiro (F-8): mora no mecanismo de propagação, sem plano vivo.
- O Controle 1.1 (`P-<MMDD>`) vive só em `~/.claude/CLAUDE.md`, ponto de carga sem residência no
  kit (F-6): é matéria do `TK-68`.

## 8. Riscos

- **R-1** `TK-65`/`TK-66`/`TK-74` renomeiam a constante âncora → card sinaliza `blocked` `premissa`.
- **R-2** Teste existente falha por mudança na leitura do legado → defeito da entrega (I-2); fixture
  legada não se edita.
- **R-3** `TK-72`/`TK-73` editam o mesmo trecho de `GOVERNANCA.md` ou `pantonic-planner.md` no
  intervalo → edição por âncora textual; âncora ausente → `blocked` `dependencia`.

## 9. Achados da execução

- **`AE-1`** (2026-09-25, laudo da `SAN-T1`, reprovado 68, bloqueante `guardas`, recomendação `escalar` — regra `A6a`) — **Pendência:** guardas vermelho estrutural e herdado pela `SAN-T2`/`SAN-T3`: `caminhos.py`, carregado por `spec_from_file_location` como o card manda, é inalcançável para o `dead_code.py` (sem import nem `__main__`), e o `I-6` veda `.claude/checks` — decidir entre emendar o `I-6`/estender o detector a módulo carregado por caminho, ou reescrever o carregamento; nenhum card do plano fecha a guarda. `dead_code.py` sai exit 1 com 8 símbolos de `caminhos.py`: 5 têm chamador real (`arquivos_de_plano`, `id_do_plano`, `inbox_planos`, `planos_dir`, `e_layout_pasta`) e caem por o módulo ser carregado por caminho; 3 (`pasta_do_plano`, `pasta_por_id`, `formatar_id`) só ganham consumidor na `SAN-T2`/`SAN-T3`. **Achados anexos do mesmo laudo:** (a) critério de pronto parcial — `progresso_hook.localizar_card` decide o título do plano por `arq.name.startswith('P-')`; com plano em pasta (`plano.md`) cai no ramo do diário e toma o último `## ` como título (medido numa cópia temporária com `docs/plans/P-0-gama/plano.md`); `backlog._parse_plano` mantém o fallback `caminho.stem` (`plano` na forma pasta) — duas derivações de plano fora de `caminhos.py` que o passo 7 não cobriu e nenhuma Verificação exercita na forma pasta; rota do revisor: corretivo `SAN-T1a` ou absorção explícita na `SAN-T3`. (b) a Verificação 5 não é invariante: a linha de base de `next` foi gravada com a própria `SAN-T1` como próxima tarefa e, depois da transição para `review`, imprime `DIFERE` com a entrega correta; reconciliado pelo revisor rodando o `backlog.py` do ref do despacho e o atual na mesma árvore (check e next idênticos, `I-2` cumprido); rota: a Verificação deve comparar código antigo × novo na mesma árvore. (c) evidência: os 12 arquivos "fora dos alvos e sem atribuição" são não rastreados anteriores ao despacho — `git stash create` não guarda não rastreados, e `progresso_hook.py` (alvo, não rastreado) vem inteiro em vez de diff; rota do revisor: tíquete em `review_evidence.py` (família `TK-78c`). Entrega fiel ao literal do card: Verificações 1-4 e 6 conferem (6 passed; 0/0/0; 1/1; 2/2/2/2/2; 339 passed = 333 + 6). **Absorvido (consultor, acionamento 1 — reexecução `A1` em contexto limpo, 2026-09-25; reparo medido numa cópia da árvore: Verificações 1-8 da `SAN-T1` conferem, 340 passed, `dead_code` exit 0, TF 17 e 18 falham no código sem o reparo):** defeito do card, não da entrega. Guarda → `DSA-18` (as três funções sem chamador nascem com ele: `pasta_do_plano` passa a ser chamada por `_parse_plano` na `SAN-T1`, `formatar_id` vai à `SAN-T2`, `pasta_por_id` à `SAN-T3`) e `DSA-19` (CLI `main` em `caminhos.py`; `I-6` intacto); (a) → passos 5 e 7 e TF 17-18 da `SAN-T1`; (b) → `DSA-20`, Verificação 5 da `SAN-T1` e 4 da `SAN-T2`; (c) → fora do plano: recorrência do caso já apontado no `TK-55` (`AE-4`/`AE-5`/`AE-11` do `P-0748`). `SAN-T1` reescrito e devolvido a `ready` para redespacho sobre a árvore atual.
- **`AE-2`** (2026-09-25, pendência do executor da `SAN-T2`, aprovado 100, recomendação `seguir` — regra `B0`) — **Pendência:** a Verificação 1 da `SAN-T2` (`-k tf_san`) sai **7 passed**, não 6: `test_tf_san_17_parse_plano_em_pasta_sem_cabecalho` (TF da `SAN-T1`) também casa o filtro; os seis TF novos (`san_7`..`san_12`) passam. **Atribuição medida:** o teste já existia em `tests/test_backlog.py` no ref do despacho (`git show <ref>:tests/test_backlog.py`), portanto não é entrega da `SAN-T2`; o defeito é o número esperado no texto do card (`docs/plans/`, fora dos alvos). Não rebaixa a entrega. Rota: `sem ação` sobre a entrega; filtros `-k tf_san` das próximas tarefas contam os TF anteriores.
- **`AE-3`** (2026-09-25, laudo da `SAN-T3`, ressalva 91, bloqueante `nenhuma`, recomendação `seguir com ressalva` — regra `A8`; RDO fechado como aprovado com ressalva) — **Ressalva (testes=parcial):** o TF `test_tf_san_15_evidencia_na_pasta_do_plano` foi inserido no meio de `test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica` (`tests/test_review_evidence.py:227`), amputando a metade final: a regressão `TK-62a` (`DB-17`/`DB-22`) que tranca a recusa de `--tarefa TK-62` na CLI deixou de existir — o trecho `codigo_falho`/`TK-62` passou a rodar contra o plano do `_escrever_plano` (só `### T1`), onde falha por ausência e não por gramática; correção medida pelo revisor: devolver as linhas 260-265 ao fim do teste `TK-62a` e fechar o TF 15 na linha 258. **Achados de processo:** (a) o literal do `close` (`if pasta_plano is None: _regenerar_indice`) contradiz `I-2` e a *Camada e fronteira* ("flag explícita sempre vence"): com `--rdo-dir` sobre plano em pasta o RDO vai ao diretório da flag com nome legado e o `INDEX.md` não é regenerado (reproduzido em raiz temporária); condição correta `args.rdo_dir is None and pasta_plano is not None`; (b) o texto de ajuda dos mesmos alvos segue anunciando só o destino legado — `rdo.py` `--rdo-dir`, `--laudos-dir`, help do subcomando `laudo` e docstring de `cmd_laudo`, `review_evidence.py` `--out`; a `SAN-T4` cobre doutrina, não a CLI. Rota do revisor para (a), (b) e a ressalva: corretivo `SAN-T3a` do `P-0749`, com TR do caso flag+pasta. (c) evidência: 11 não rastreados anteriores ao despacho listados sem atribuição — reconciliado como WIP alheio; rota: fora do plano, extensão do `TK-78c` (mesma família de `AE-1` (c)). **Absorvido (consultor, acionamento 2, 2026-09-25; reparo medido numa cópia da árvore: 352 passed, `dead_code` exit 0, TR 19 falha no código da `SAN-T3`):** ressalva, (a) e (b) → `DSA-21` e corretivo `SAN-T3a` (`OP-3`), antes da `SAN-T4` (que passa a depender dele); (c) → fora do plano, sem card: terceira recorrência do caso do `TK-55`/`TK-78c`, e o próximo laudo trará o mesmo ruído.
- **`AE-4`** (2026-09-25, laudo da `SAN-T4`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo:** `DSA-14`/troca `B2` × `backlog.py` `C-10`: o estado de projeto novo que a doutrina agora ensina (`_INBOX.md` só com `**Próximo id de plano: P-0.**` e `docs/plans/` vazia) faz `backlog.py check` sair 1 com `C-10` falso (`contador aponta para P-0, já presente em docs/plans/` sem plano nenhum), porque `check` usa `maior=0` quando não há plano (`backlog.py:749`, `contador <= maior`); reproduzido pelo revisor em repo temporário. A entrega escreveu o literal do card e `backlog.py` está fora dos alvos; a Verificação 3 da `SAN-T4` só conta texto e não exercita o mundo que o bootstrap cria. Rota do revisor: corretivo de `backlog.py` `C-10` no `P-0749` (sem plano presente, contador `P-0` é válido), com teste no estado de bootstrap, antes do fechamento do plano. **Absorvido (consultor, acionamento 3, 2026-09-25; reparo medido numa cópia da árvore: `check` exit 0 no estado de bootstrap, 353 passed, `dead_code` exit 0, `I-2` `IGUAL`, TF 20 falha no código da `SAN-T2`):** defeito da `SAN-T2` (`OP-2`, *"projeto novo começa em zero"*), não da `SAN-T4` → `DSA-22` e corretivo `SAN-T2a`, antes da `SAN-T5`.
- **`AE-5`** (2026-09-25, laudo da `SAN-T6`, ressalva 88, bloqueante `nenhuma`, recomendação `seguir com ressalva` — regra `A8`; RDO fechado como aprovado com ressalva) — **Ressalva (criterio-de-pronto=parcial):** o *Pronto quando* da `SAN-T6` amarra o aceite à Verificação 4 (veredito do dono sobre `M1`..`M4`, aferição manual), inverificável no ato da revisão; V1 exit 0 com `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`, V2 `0 / 2 / 1`, V3 353 passed, re-rodados pelo revisor. O veredito vai ao dono no relatório de encerramento da janela. **Achados de processo:** (a) a régua de card de revisão do `README.md` deveria separar o veredito do dono como gate do fechamento, fora do *Pronto quando* julgado na revisão; (b) `M1` trocou só a primeira linha do item *Plano `P-<n>`* do glossário e deixou, na linha seguinte do mesmo item, `identificado por contador global monotônico` — o `README.md` descreve o contador de dois jeitos (glossário "global" × item 1 do `G-PLANREADY`, `M4`, e `GOVERNANCA.md` §7 item 11, `SAN-T4`: "contador monotônico do repositório, começando em 0"); entrega fiel ao literal, resíduo do card; rota do revisor: corretivo `SAN-T6a` (`OP-6`) com troca literal no glossário, submetido ao mesmo veredito do dono; (c) `M1` publicou o texto novo como linha única de ~200 colunas sem dizer se o parágrafo se reflui; a entrega refluiu as linhas 2-4 do mesmo item (palavras idênticas, markdown renderizado idêntico) — detalhe reversível sem desvio; rota: troca literal de redação declara a quebra de linha do texto novo, como `M4` já faz. **Absorvido (consultor, acionamento 4, 2026-09-25; `M5` medido numa cópia com `check-readme -Root`: exit 0, contagens `0 / 1`):** ressalva → sem card: o veredito do dono sobre `M1`..`M4` é gate do marco e sobe no relatório de encerramento; (b) → `DSA-23` e corretivo `SAN-T6a` (`OP-6`), depois da `SAN-T6`, com `M5` sob o mesmo veredito; (a) e (c) → fora do plano, régua de autoria: `TK-72` §9, Pacotes 11 e 12 — já aplicados ao card `SAN-T6a` (veredito fora do *Pronto quando*; quebra de linha declarada).
- **`AE-6`** (2026-09-25, laudo da `SAN-T6a`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo:** `AE-5` (b)/`DSA-23` mediu o resíduo de "global" só pelo padrão `contador global monot` e deixou de fora `README.md:1045` (§14, *Decisões estruturantes*), cuja linha de tabela `Plano tem contador sequencial global no nome` segue chamando o contador de global, contra o glossário (`README.md:159`), `README.md:603` e `GOVERNANCA.md:841`, que agora dizem "contador monotônico do repositório". Fora do escopo da `SAN-T6a` por declaração do card; a entrega não responde por ela. Rota do revisor: corretivo da `OP-6` (`SAN-T6b`) com o literal de `README.md:1045` e medida por padrão que cubra `contador sequencial global`, ou decisão registrada no plano de manter a palavra na §14. **Absorvido (consultor, acionamento 5, 2026-09-25; `M6` medido numa cópia da árvore com `check-readme -Root`: exit 0, contagens `0 / 0 / 1`; a varredura do loop, `global` × `contador|P-NNNN|P-<n>|id de plano`, acha só esta linha):** resíduo do `DSA-23`, não da entrega → `DSA-24` e corretivo `SAN-T6b` (`OP-6`), depois da `SAN-T6a`, com `M6` sob o mesmo veredito do dono.
- **`AE-7`** (2026-09-25, laudo da `SAN-T6b`, aprovado 100, bloqueante `nenhuma`, recomendação `seguir` — regra `A9`; RDO fechado como aprovado) — **Achado de processo (autoria):** a Verificação 3 da `SAN-T6b` (e a da `SAN-T6a`) publica no literal *Medido antes* o total da suíte (`353 passed`), número de corpus que outra entrega desloca, contra o critério (xviii) da RUBRICA §8 (`AE-49`); o valor esperado já está em relação ("o total do despacho, nenhuma falha"), e o literal devia levar o veredito (exit 0), com o total como referência datada na prosa. Sem efeito na entrega (suíte re-medida 353 passed). Rota do revisor: registro neste plano, **sem corretivo** — a regra (xviii) já existe; a falha é de aplicação na autoria (família da régua de autoria do `TK-72`).
