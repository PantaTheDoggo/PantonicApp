# P-0739 — O pickup vira instrumento: `backlog.py` decide a próxima tarefa, fecha a tarefa e mantém o kanban

**Data:** 2026-09-15 · **Origem:** diretiva do dono, 2026-09-15 ("mecanizar o próximo passo") ·
**Status:** `blocked` (2026-09-16, razão: revisão pedida pela orquestração — `AE-2`; sai de
`blocked` quando a `RP-2` fechar) · **Prefixo das tarefas no diário:** `BKL-T<n>` · **Prefixo das decisões:**
`DB-<n>` · **Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`DE-7`), nada a comparar.
**Ordem de execução:** BKL-T2 → BKL-T3 → BKL-T4 → BKL-T5 → BKL-T6 → BKL-T7 → BKL-T8 → BKL-T9 ·
**Rodadas de replanejamento:** `RP-1` (2026-09-16, sobre `AE-1`) · `RP-2` (**pendente** — sobre
`AE-2`, próxima tarefa do plano; ver `## Achados da execução`).

## Contexto

O fluxo "execute o próximo passo" é hoje um roteiro em prosa (`.claude/skills/proximo-passo/SKILL.md`,
201 linhas) que manda o agente **ler para descobrir**: drenar `docs/plans/_INBOX.md`, ler a diretiva e a
`Fila corrente` no cabeçalho do diário, apurar status no índice, grep pelo ID, ler a seção. A medida
está publicada em `docs/CUSTO_DO_PICKUP.md`: pickup típico de **77.457 chars** (`## 3`), rotas
`gerar-por-instrumento` / `ponteiro` / `condensar` ratificadas pelo dono em 2026-08-23 (`## 9`), e
a rodada de prosa do `P-0738` (Estágio C) **não** reduziu o custo — a `CTX-T10` mediu +34%
(`## 10`). O que falta não é mais prosa: é o instrumento que a `## 5` listou como rota e ninguém
implementou.

Três defeitos estruturais impedem que o pickup seja programático hoje (verificados nesta sessão):

1. **Status por tarefa não é legível por máquina.** Os cabeçalhos seguem a gramática `DP-C`
   (`### <ID> — <título> [<modelo> · classe <classe>]`) sem estado; o estado vive em prosa
   ("`TK-54a` é a próxima tarefa delegável", "3/12", bullets "`CTX-T9` — … — `done` em …").
2. **A célula `Status` do índice carrega narrativa.** Das 26 linhas do índice ativo, 9 têm estado
   seguido de parêntese narrativo, 1 usa `backlog` e 1 usa `**decidido em parte**` — valores fora do
   vocabulário fechado da residência única (skill `diario-de-obras`).
3. **Os ponteiros de fila são parágrafos.** `**Fila corrente:**` no cabeçalho tem 30 linhas de
   decisões acumuladas; `**Próxima tarefa:**` existe em 2 seções vivas (mais 39 históricas) e é
   reescrita à mão. O agente lê tudo isso para extrair um ID.

**Resultado esperado:** uma chamada (`python .claude/tools/backlog.py next`) devolve o dossiê da única
tarefa a tratar; uma chamada (`backlog.py status <ID> <estado>`) fecha a tarefa e reescreve todas as
projeções; a ambiguidade deixa de ser escolha do agente e vira **defeito nomeado** pelo instrumento.
Nada do diário, do inbox ou do histórico entra no contexto além do dossiê.

**Relação com planos vivos (Controle 1.2 verificado):** `P-0737` está `blocked` pela `TK-54` e sua
`AUT-T6` transpõe a *prosa* de `proximo-passo`/`handover` para `passagem-de-bastao`; este plano
entrega o *instrumento* que aquela skill vai chamar, sem tocar o `P-0737` (classificação: enabler,
não A nem B — registrado como apenso em `P-0737` `## 9` no ato do registro). `P-0736`/`P-0738` estão
`done`; suas rotas ratificadas são a autoridade deste plano.

## 1. Decisões (fechadas no ato; o executor não reabre)

| Id | Decisão | Conteúdo |
|---|---|---|
| **`DB-1`** | Um instrumento, stdlib, testável por caminho | `.claude/tools/backlog.py`: funções recebem `repo`/caminhos já resolvidos e nunca leem `sys.argv` (desenho de `uow.py`/`materializar.py`); escrita atômica (temp + `os.replace`, como `telemetria.py`); parser próprio de ID (`DB-14`), sem tocar `rdo.py` |
| **`DB-2`** | Fonte única do estado = linha de campo na residência do item | Todo item vivo (tarefa `###`, tíquete `## TK-`, plano `# P-`) tem `**Status:**` legível por máquina (§2). A célula `Status` do índice é **projeção** escrita no mesmo ato pelo instrumento; `check` prova a igualdade e falha se divergir |
| **`DB-3`** | Vocabulário fechado, sem exceção | Só os estados da residência única (`triage`, `ready`, `blocked`, `in-progress`, `review`, `done`, `cancelled`; `superseded` só para plano). `backlog` e `decidido em parte` não existem: a migração (`BKL-T6`) os converte com razão registrada |
| **`DB-4`** | O instrumento não decide o que exige juízo | Não destrava `blocked`, não flipa plano para `done`, não promove memória, não escolhe entre dois `in-progress`. Esses casos saem num **rodapé fixo** de uma linha cada, e o agente decide com o dono |
| **`DB-5`** | `next` é somente-leitura e idempotente | Por isso pode rodar em hook. Toda escrita é verbo explícito (`status`, `drain`, `diretiva`) |
| **`DB-6`** | Ambiguidade é defeito, não escolha | Dois `in-progress`, tarefa sem linha de status, linha de índice fora da gramática, plano vivo sem prefixo: `next` sai com **exit 3** e nomeia o conserto. O agente nunca "resolve por grep" — conserta o dado ou escala |
| **`DB-7`** | Teto do dossiê emitido | Seção da tarefa verbatim até **8.000 chars / 120 linhas**; além disso, truncado com ponteiro `arquivo:l1-l2`. Alvo do pickup ratificado: 40.000 chars (`CUSTO_DO_PICKUP.md` `## 6`); o dossiê é a maior fatia |
| **`DB-8`** | Hook `UserPromptSubmit`, registrado no canônico | `backlog_hook.py` casa o gatilho (`pr[oó]ximo passo` / `continue o backlog` / `retome o backlog`, case-insensitive) e injeta a saída de `next` como `additionalContext`. Entra em `.claude/projecoes.json` e chega a `settings.json` só por `materializar.py apply` (`P-0735`) |
| **`DB-9`** | Históricos são append-only e nunca lidos | `_INBOX_HISTORICO.md` e `DIARIO_HISTORICO.md` só recebem apenso de `drain`; o instrumento nunca os abre para ler |
| **`DB-10`** | Toda escrita imprime a lista de arquivos tocados | Permite a verificação `git status --short` de cada tarefa e a revisão do diff antes do commit |
| **`DB-11`** | Diretiva de priorização reescrita no registro | O pedido do dono de 2026-09-15 é instrução de prioridade: ao registrar o plano, a linha vira `**Diretiva de priorização:** Priorize \`P-0739\` — depois retoma \`TK-54\`.` O texto atual da diretiva (decisões sobre `TK-53`/`TK-54`) migra verbatim para a seção `## TK-54`. **Único ponto a confirmar na aprovação** |
| **`DB-12`** | `Próxima tarefa` de seção deixa de ser fonte | A projeção viva é o bloco gerado `Fila corrente` no cabeçalho (§2.5). As linhas `**Próxima tarefa:**` das seções vivas viram ponteiro fixo ("ver bloco *Fila corrente*"); as históricas ficam como estão |
| **`DB-13`** | Sem bump, sem tag, hub primeiro | `DE-7`/`DA-3`: linha em `CHANGELOG.md` sob `## [Não lançado]`; nenhum derivado tocado — propagação é ato posterior (memória `kit-pantonic-propagacao`) |
| **`DB-14`** | Gramática de ID do instrumento | `P-[0-9]{4}` (plano) · `TK-[0-9]+[a-z]?` (tíquete/subtarefa) · `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` (tarefa de plano, com ou sem prefixo). Achado pré-existente, **não corrigido aqui**: `rdo.py` `_ID_HEADER_RE` só aceita `T<n>` sem prefixo — por isso não há RDO de `CTX-*`. Vai para `## Achados da execução` |
| **`DB-15`** | Plano vivo recebe linhas de campo; plano fechado não se toca | Adicionar `- **Status:**` sob cabeçalhos de `P-0737` é metadado, autorizado por esta decisão; corpo do plano segue imutável. Planos `done`/`superseded` não recebem nada (o índice é a projeção final deles) |
| **`DB-16`** | Executor não escreve estado; `scrum-master` chama o verbo | Mantém `DP-G`: quem materializa status é a orquestração. O executor devolve a linha de retorno; o orquestrador roda `backlog.py status`. `rdo.py close` e `telemetria.py append` seguem separados e sequenciados pela skill, não chamados pelo instrumento |
| **`DB-17`** | Cabeçalho de tíquete e de subtarefa — forma normativa (`RP-1`) | Tíquete: `## TK-<n> — <título>`, nível 2, **sem** bracket (tíquete é fila de entrada: não tem modelo nem classe). Subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]` — a `DP-C` completa, idêntica à tarefa de plano, porque a subtarefa é executada como tarefa e `rdo.py`/`review_evidence.py` já leem essa forma. As duas subtarefas reais sem modelo (`TK-54a`, `TK-54b`, `[classe investigacao]`) recebem `Sonnet · ` na migração `BKL-T6` (f) — execução roda em Sonnet (`GOVERNANCA.md` §3). Ratifica a leitura A do `AE-1` para tíquete; a leitura B não descreve nada real |
| **`DB-18`** | Tabela normativa não usa `idem` nem remissão | Toda linha de tabela de gramática escreve a forma inteira; `idem`, `análogo`, `mesmo que acima` são defeito de autoria (léxico proibido do planejador). Cada linha da gramática cita ≥ 1 ocorrência real que a casa, e toda forma real fora da gramática está nomeada como item de migração — o inventário é o fato `F-1` (antes de §2) |
| **`DB-19`** | Forma fora da gramática é violação nomeada, nunca decisão | `check` classifica o que não casa em violações de vocabulário fechado (`C-1..C-9`, inline no card `BKL-T2`). O executor nunca escolhe entre leituras: se a gramática admitir duas leituras para a mesma linha real, o defeito é da gramática e o card volta ao planejador (`G-REPLAN`, `GOVERNANCA.md` §7 item 17) |
| **`DB-20`** | Bracket de tarefa: variantes reais toleradas (`RP-1`, `F-1`) | `<modelo>` pode vir seguido de ` + dono` (o aceite do dono é parte da tarefa: `BKL-T9`, `AUT-T10`) e o bracket pode terminar em ` · teto <n>` (sufixo legado dos 10 cards de `P-0737`; a doutrina atual não escreve teto no card). O parser aceita os dois e ignora o teto; nenhum vira violação e a `BKL-T6` não toca esses cabeçalhos (`DB-15`: corpo de plano é imutável) |

### Inventário do corpus (fato `F-1`, apurado na `RP-1` de 2026-09-16)

Formas reais de cabeçalho de item vivo, contadas por regex sobre `docs/DIARIO_DE_OBRAS.md`,
`docs/plans/P-0737-loop-autonomo.md` e este plano. A gramática de §2.1 é escrita **contra** esta
lista: toda forma casa exatamente uma linha da tabela ou está nomeada como item de migração.

| forma real | ocorrências | exemplo | destino na gramática |
|---|---|---|---|
| `### <PFX>-T<n> — <título> [<modelo> · classe <classe>]` (tarefa de plano, `DP-C` pura) | 8 de 19 | `docs/plans/P-0739-backlog-instrumento.md:153` | linha *tarefa de plano* (`DP-C`) |
| `### <PFX>-T<n> — <título> [<modelo> · classe <classe> · teto <n>]` (sufixo legado `teto`) | 10 de 19 | `docs/plans/P-0737-loop-autonomo.md:218` | linha *tarefa de plano*: sufixo tolerado e ignorado (`DB-20`); não migra (`DB-15`) |
| `### <PFX>-T<n> — <título> [<modelo> + dono · classe <classe>[ · teto <n>]]` (aceite do dono) | 2 de 19 | `docs/plans/P-0739-backlog-instrumento.md:333` | linha *tarefa de plano*: ` + dono` aceito (`DB-20`) |
| `## TK-<n> — <título>` (tíquete, nível 2, sem bracket) | 7 | `docs/DIARIO_DE_OBRAS.md:705` | linha *tíquete* (`DB-17`) |
| `### TK-<n><letra> — <título> [classe <classe>]` (subtarefa **sem** `<modelo>`) | 2 de 4 | `docs/DIARIO_DE_OBRAS.md:1233` | **migração `BKL-T6` (f)**: vira `[Sonnet · classe <classe>]` (`DB-17`) |

Nenhum item vivo tem linha `**Status:**` hoje (defeito 1 do Contexto) — migração `BKL-T6` (c).

## 2. Gramática legível por máquina (normativa; `BKL-T1` a transcreve para a skill `diario-de-obras`)

### 2.1 Item e residência

| item | residência viva | cabeçalho | campos obrigatórios logo abaixo |
|---|---|---|---|
| plano | `docs/plans/P-NNNN-<slug>.md` | `# P-NNNN — <título>` (linha 1) | nas 20 primeiras linhas: `**Status:** \`<estado>\`` e `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; opcional `**Ordem de execução:** ID → ID → …` (1ª ocorrência vence; ausente = ordem dos cabeçalhos) |
| tarefa de plano | no plano (`### <ID> …`) | `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]` (`DP-C`; ` + dono` marca aceite do dono, ` · teto <n>` é sufixo legado tolerado e ignorado — `DB-20`) | 1º bullet: `- **Status:** \`<estado>\` · AAAA-MM-DD[ · <razão de 1 linha>]`; opcionais `- **Depende de:** \`ID\`[, \`ID\`]`, `- **Tipo:** bug`; `- **Notas de execução:**` com sub-bullets `  - AAAA-MM-DD \`<estado>\` — <texto>` apensados pelo instrumento |
| tíquete | `docs/DIARIO_DE_OBRAS.md` | `## TK-<n> — <título>` (nível 2, **sem** bracket — tíquete não tem modelo nem classe; `DB-17`) | mesmos campos da tarefa (`Status`, `Tipo`, `Notas de execução`) |
| subtarefa de tíquete | `docs/DIARIO_DE_OBRAS.md`, dentro da seção do tíquete-pai | `### TK-<n><letra> — <título> [<modelo> · classe <classe>]` (`DP-C` completa, igual à tarefa de plano; `DB-17`) | mesmos campos da tarefa |

Uma tarefa é *do* plano cujo prefixo casa com o dela; `TK-<n><letra>` é *do* tíquete `TK-<n>`.

### 2.2 Índice do diário

`| <ID> | <título curto> | <estado>[ <done>/<total>] | <âncora> |` — a célula `Status` contém **só**
o token do vocabulário, opcionalmente seguido de `<done>/<total>` para plano/tíquete com subtarefas.
Nada mais. Título e âncora seguem de autoria humana (o instrumento só cria a linha no `drain` e só
reescreve a célula `Status`).

### 2.3 Cabeçalho do diário (bloco gerado)

```markdown
**Diretiva de priorização:** [Priorize `<ID>`[, `<ID>`…]] [— <texto livre>]
<!-- fila:gerada -->
**Fila corrente:** `<ID>` — <título> (`<arquivo>:<l1>-<l2>`) · fila: <ID2>, <ID3> · ready <n> · blocked <m> · in-progress <k>
- `P-NNNN` (`<estado>`, <done>/<total>): próxima `<ID>`
<!-- /fila:gerada -->
```

O instrumento lê só os tokens `` `ID` `` antes de ` — ` na diretiva; o texto livre é para humanos.
Tudo entre os marcadores é reescrito a cada verbo de escrita; humano não edita ali.

### 2.4 Inbox de planos

Linha viva: começa com `- ` e contém um caminho `docs/plans/P-NNNN-<slug>.md` (o resto é livre).
Drenada: prefixada `- [drenado AAAA-MM-DD] ` e movida **verbatim** para `_INBOX_HISTORICO.md`.
Contador: `**Próximo id de plano: P-NNNN.**` — `drain` o recalcula como `max(id visto) + 1`.

### 2.5 Ordem total de seleção (`next`)

1. Diretiva com IDs → candidatos restritos a esses itens e suas tarefas; sem IDs → todos.
2. Exatamente um `in-progress` → é a resposta (retomada). Dois ou mais → exit 3 (`DB-6`).
3. Elegíveis: tarefas `ready` cujo plano/tíquete-pai está `ready` ou `in-progress`, com todo
   `Depende de` em `done`. Plano `blocked`/`superseded`/`done`/`cancelled` não contribui.
4. Ordem: (a) tarefas de plano `in-progress` (WIP de 1 iniciativa); (b) tíquetes `Tipo: bug`;
   (c) FIFO pela ordem das linhas do índice. Dentro de um plano: `Ordem de execução`, senão ordem
   dos cabeçalhos.
5. Resultado: uma tarefa (exit 0) ou "nada delegável" com contagens (exit 2). `blocked` e
   memórias por promover aparecem só no rodapé.

### 2.6 Saída de `next` (forma fixa)

```
=== PRÓXIMA TAREFA: <ID> — <título> [<modelo> · classe <classe>]
plano: P-NNNN — <título> (<done>/<total>) · residência: <arquivo>:<l1>-<l2> · índice: <âncora>
antecessora: <ID> (<estado>; notas em <arquivo>:<l1>-<l2>)
--- dossiê (verbatim, teto DB-7) ---
<seção da tarefa>
--- pendências mecânicas ---
inbox de planos: <n> por drenar · fila de memória: <m> candidato(s) · blocked: <ID> (<razão>), …
```

### 2.7 Máquina de transições

Tabela da residência única (skill `diario-de-obras`, "Máquina de transições") transcrita para
`_TRANSICOES: dict[tuple[str, str], ...]`; `blocked` exige `--razao`; `done`/`cancelled` são
terminais; `superseded` só para plano. Transição fora da tabela → exit 1 sem escrever nada.

## 3. Superfície do instrumento

```
python .claude/tools/backlog.py next      [--sem-dossie] [--repo]        # somente leitura, exit 0/2/3
python .claude/tools/backlog.py show <ID>                                 # dossiê de um item
python .claude/tools/backlog.py check     [--repo]                        # lint da gramática, exit 0/1
python .claude/tools/backlog.py status <ID> <estado> [--razao "…"] [--nota "…"]   # transição + projeções
python .claude/tools/backlog.py start <ID>                                # = status <ID> in-progress
python .claude/tools/backlog.py drain     [--data AAAA-MM-DD]             # inbox → índice + histórico
python .claude/tools/backlog.py diretiva "Priorize `P-0739` — …"          # reescreve a linha
```

`status` escreve, num ato: linha `Status` do item · apenso em `Notas de execução` (se `--nota`) ·
célula do índice · `<done>/<total>` do pai · bloco `Fila corrente`. Plano cujas tarefas ficaram
todas terminais entra no rodapé como "candidato a fechamento" (`DB-4`).

## 4. Tarefas

Ordem linear `BKL-T1 → … → BKL-T9`; cada uma cabe num contexto de executor frio. Testes em
`tests/test_backlog.py` sobre fixtures em `tests/fixtures/backlog/` (mini-diário + 2 planos +
inbox), carregando o módulo por `importlib` como `tests/test_telemetria.py`; nunca contra o repo
real. Teto de linhas é instrumentação (`DU-14`), não comando.

### BKL-T1 — A gramática publicada na residência única [Sonnet · classe redacao]
- **Status:** `done` · 2026-09-16
- **Objetivo:** a skill `diario-de-obras` ganha a seção `## Gramática legível por máquina`
  (transcrição de §2.1–§2.4 e §2.7, sem reescrever), e as operações 2, 4 e 5 passam a apontar
  para os verbos de §3 como forma canônica (a prosa atual fica como descrição do efeito).
- **Arquivos-alvo:** `.claude/skills/diario-de-obras/SKILL.md` (via `uow.py`, artefato canônico).
- **Verificação:** `Grep "^## Gramática legível por máquina"` → 1 match; `git status --short` só
  esse arquivo.
- **Pronto quando:** a gramática existe num lugar só e o plano aponta para ela.
- **Notas de execução:**
  - 2026-09-16 `done` — seção `## Gramática legível por máquina` publicada em
  `.claude/skills/diario-de-obras/SKILL.md:125` (transcrição verbatim de §2.1–§2.4 e §2.7 acima);
  operações 2/4/5 de `SKILL.md` `## Operações` passam a apontar para os verbos `status`/
  `diretiva`/`drain` de §3 como forma canônica, prosa original preservada como descrição do
  efeito. Editado via `uow.py open/diff/close` (artefato canônico). Verificação: `Grep "^##
  Gramática legível por máquina" .claude/skills/diario-de-obras/SKILL.md` → 1 match; `git status
  --short` sem arquivo novo além do já sujo na sessão. Consumo: ver `docs/telemetria.tsv`.

### BKL-T2 — `backlog.py`: modelo, parser, `check` e `show` [Sonnet · classe implementacao]
- **Status:** `blocked` · 2026-09-16 · premissa
- **Depende de:** `BKL-T1`
- **Objetivo:** o núcleo somente-leitura — carregar índice, planos vivos e diário; construir o
  grafo item→tarefas; `check` acusa cada violação `C-1..C-9` com `arquivo:linha`; `show` emite o
  dossiê com teto `DB-7`.
- **Arquivos-alvo:** `.claude/tools/backlog.py` (novo); `tests/test_backlog.py` (novo);
  `tests/fixtures/backlog/` (novo: `DIARIO_DE_OBRAS.md` mínimo, 2 planos, `_INBOX.md`).
- **Gramática que o parser implementa** (inline por `DB-17`/`DB-18`; a residência é a skill
  `diario-de-obras`, seção "Gramática legível por máquina" — igual a esta lista):
  - plano: linha 1 `# P-NNNN — <título>`; nas 20 primeiras linhas `**Status:** \`<estado>\`` e
    `**Prefixo das tarefas no diário:** \`<PFX>-T<n>\``; opcional `**Ordem de execução:** ID → ID`.
  - tarefa de plano: `### <ID> — <título> [<modelo> · classe <classe>]`, `<ID>` =
    `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` (`DB-14`); bracket completo `[<modelo>[ + dono] · classe
    <classe>[ · teto <n>]]` — ` + dono` e ` · teto <n>` são aceitos e não são violação (`DB-20`).
  - tíquete: `## TK-<n> — <título>` (nível 2, **sem** bracket).
  - subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]`, dentro da
    seção do tíquete-pai.
  - campos (tarefa, subtarefa, tíquete): 1º bullet `- **Status:** \`<estado>\` · AAAA-MM-DD[ ·
    <razão>]`; opcionais `- **Depende de:**`, `- **Tipo:** bug`, `- **Notas de execução:**` com
    sub-bullets `  - AAAA-MM-DD \`<estado>\` — <texto>`.
  - índice: `| <ID> | <título> | <estado>[ <done>/<total>] | <âncora> |`.
  - `<modelo>` ∈ `Opus|Sonnet|Haiku`; `<classe>` ∈
    `mecanica|implementacao|comportamental|investigacao|redacao`; `<estado>` ∈ vocabulário `DB-3`.
- **Violações de `check`** (vocabulário fechado; cada uma sai como `<código> <arquivo>:<linha> —
  <texto>`): `C-1 cabecalho-fora-da-gramatica` (heading `##`/`###` cujo ID casa `DB-14` mas cuja
  forma não casa nenhuma linha acima — inclui bracket sem `<modelo> ·`) · `C-2 item-sem-status` ·
  `C-3 status-fora-do-vocabulario` · `C-4 celula-do-indice-com-prosa` · `C-5
  divergencia-indice-x-campo` · `C-6 dois-in-progress` (no mesmo plano ou tíquete) · `C-7
  plano-vivo-sem-prefixo` · `C-8 plano-vivo-sem-status` · `C-9 id-do-indice-sem-residencia`
  (linha do índice cujo ID não existe em plano vivo nem no diário; planos `done`/`superseded` do
  índice são isentos, `DB-15`).
- **Passos:** (1) `tests/fixtures/backlog/` com um caso verde (tudo conforme) e um caso vermelho
  que dispara `C-1..C-9` uma vez cada; (2) `backlog.py`: dataclasses `Plano`, `Item`,
  `LinhaIndice`, `Violacao`; funções `carregar(repo: Path) -> Modelo`, `check(modelo) ->
  list[Violacao]`, `show(modelo, id: str) -> str`; a CLI `check`/`show` só embrulha (`DB-1`);
  (3) testes abaixo; (4) rodar `check` no repo real e colar a lista na nota de execução.
- **Testes:** TF parser (3 formas de ID de `DB-14`; campo `Status` com e sem razão; heading `###`
  legado sem bracket → `C-1`); TF `check` vermelho uma vez por código `C-1..C-9`; TF `check` verde
  na fixture conforme; TF `show` trunca em 8.000 chars / 120 linhas com ponteiro `arquivo:l1-l2`;
  TR `carregar` nunca abre `*_HISTORICO.md` (monkeypatch em `Path.open`/`open` que falha se o
  caminho casar `_HISTORICO`).
- **Contingências:** se o repo real tiver forma que não casa nenhuma linha da gramática → `C-1`
  com `arquivo:linha`, nunca bloqueio (`DB-19`); se a gramática admitir duas leituras para a
  mesma linha real → parar e sinalizar `blocked motivo=premissa defeito=ambiguidade` citando a
  linha e as duas leituras (`G-REPLAN`).
- **Não fazer:** não editar diário, planos, inbox ou histórico (esta tarefa é somente-leitura);
  não tocar `rdo.py`; não decidir migração (é a `BKL-T6`); não ler `docs/DIARIO_DE_OBRAS.md` além
  do que o parser lê por código.
- **Verificação:** `python -m pytest tests/test_backlog.py -q` verde; `python .claude/tools/backlog.py check` no repo real → exit 1 e a lista colada na nota (esperada: `C-1` em `TK-54a`/`TK-54b`, `C-2` nos itens vivos sem `Status`, `C-4` nas células narrativas do índice, `C-3` em `backlog`/`decidido em parte`), insumo da `BKL-T6`.
- **Pronto quando:** `check` e `show` funcionam sobre a fixture e a lista de defeitos reais está na nota.
- **Notas de execução:**
  - 2026-09-16 `blocked` — nenhum arquivo criado; contradição na tabela §2.1 (`idem` na coluna
    "cabeçalho" do tíquete), achado `AE-1`.
  - 2026-09-16 `ready` — `RP-1`: gramática de tíquete/subtarefa fechada (`DB-17`), violações
    `C-1..C-9` inline, contingência de forma desconhecida (`DB-19`).
  - 2026-09-16 `review` — entregues `.claude/tools/backlog.py` (584 linhas: dataclasses `Plano`,
    `Item`, `LinhaIndice`, `Violacao`, `Modelo`; `carregar`/`check`/`show`; CLI fina por `DB-1`),
    `tests/test_backlog.py` (8 TF/TR, verdes) e `tests/fixtures/backlog/{verde,vermelho}/`.
    Nenhum artefato de registro tocado (tarefa somente-leitura sobre diário/planos/inbox).
    **Defeitos reais do repo** (`python .claude/tools/backlog.py check` → exit 1, 274 violações,
    re-derivado pelo orquestrador): `C-1`=153 · `C-2`=79 · `C-7`=15 · `C-8`=14 · `C-4`=8 ·
    `C-9`=3 · `C-3`=2; `C-5` e `C-6` não ocorrem hoje — quase nenhum item vivo tem campo
    `Status`, então não há divergência índice×campo nem dois `in-progress` detectáveis. Confirma
    a expectativa do card (`C-1` em `TK-54a`/`TK-54b`; `C-3` em `backlog` e `decidido em parte`)
    e é o insumo da `BKL-T6`. Achado fora de escopo, não corrigido:
    `check-readme.ps1` acusa divergência pré-existente README × `GOVERNANCA.md` §7 (16 linhas × 17
    itens), sem relação com os alvos desta tarefa. Consumo: ver `docs/telemetria.tsv`.
  - 2026-09-16 `blocked` — razão `premissa`, achado `AE-2`: a rodada de revisão não roda porque o
    `review_evidence.py` não localiza ID prefixado (`rdo.py:79-81`). **O entregável não é
    descartado** — o bloqueio é da revisão. Decisão do dono no pickup: anotar e escalar. Próxima
    tarefa do plano é a `RP-2` (`pantonic-planner`), não a `BKL-T3`.

### BKL-T3 — `next`: a seleção determinística [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T2`
- **Objetivo:** implementar §2.5/§2.6; exit 0/2/3.
- **Arquivos-alvo:** `.claude/tools/backlog.py`; `tests/test_backlog.py`.
- **Testes:** TF por ramo: retomada de `in-progress`; diretiva restringe; `Depende de` segura;
  plano `blocked` não contribui; bug antes de FIFO; `Ordem de execução` vence ordem de cabeçalho;
  fila vazia → exit 2; dois `in-progress` → exit 3 com os IDs; rodapé lista `blocked` e conta
  linhas não marcadas de `<memory-dir>/_INBOX.md` (caminho injetado por parâmetro no teste).
- **Verificação:** pytest verde; saída do `next` na fixture ≤ 8.200 chars.
- **Pronto quando:** toda regra de §2.5 tem um teste e a saída tem a forma de §2.6.

### BKL-T4 — `status`, `start`, `diretiva`: transição e projeções [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T3`
- **Objetivo:** §2.7 + escrita atômica de todas as projeções num ato (§3), com lista de arquivos
  tocados na saída (`DB-10`).
- **Arquivos-alvo:** `.claude/tools/backlog.py`; `tests/test_backlog.py`.
- **Testes:** TF cada transição válida escreve campo + célula + `<done>/<total>` + bloco gerado;
  TF `blocked` sem `--razao` recusa; TF transição inválida não escreve nada (hash antes = depois);
  TF `--nota` apensa sub-bullet datado e **nunca** toca a célula do índice (TR do guardrail
  anti-log-narrativo); TF `start` recusa com outro `in-progress` no mesmo plano; TF `diretiva`
  preserva o texto livre.
- **Verificação:** pytest verde.
- **Pronto quando:** fechar uma tarefa é uma chamada e `check` fica verde depois dela.

### BKL-T5 — `drain`: o inbox sai do contexto [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T4`
- **Objetivo:** §2.4 — cada linha viva vira linha de índice (`status` do plano lido do cabeçalho
  dele, título da linha 1, âncora = caminho) e é movida verbatim com marca ao histórico; contador
  recalculado; plano sem `Prefixo` ou sem `Status` → exit 3 nomeando o arquivo.
- **Arquivos-alvo:** `.claude/tools/backlog.py`; `tests/test_backlog.py`.
- **Testes:** TF linha drenada aparece idêntica (menos o prefixo) no histórico e some do inbox; TF
  inbox vazio é no-op com exit 0; TF plano malformado não drena nada; TR o histórico só cresce.
- **Verificação:** pytest verde.
- **Pronto quando:** `next` reporta `inbox de planos: 0` depois de um `drain` na fixture.

### BKL-T6 — Migração dos documentos vivos até `check` verde [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T5`
- **Objetivo:** aplicar §2 ao estado real: (a) cabeçalho do diário → diretiva de `DB-11` + bloco
  gerado, com o parágrafo atual da `Fila corrente` movido verbatim para `## TK-54`/`## TK-53`
  conforme o assunto; (b) 26 células do índice → token puro, narrativa movida para a seção do item
  como bullet datado (`backlog`/`decidido em parte` → `cancelled` com razão "absorvido pelo
  P-0738", conforme já diz a própria célula); (c) linha `Status` sob cada item vivo: `TK-38`,
  `TK-48`, `TK-54`, `TK-54a`, `TK-54b`, e `AUT-T1..T10` em `P-0737` (`DB-15`), com data de origem;
  (d) `Próxima tarefa` das seções `P-0737`/`P-0738` → ponteiro fixo (`DB-12`); (e) `Ordem de
  execução` copiada do §7 do `P-0737` para o cabeçalho dele; (f) cabeçalhos `### TK-54a`/
  `### TK-54b` recebem `Sonnet · ` antes de `classe` (`DB-17`); os cards `BKL-T1..T9` já têm
  linha `Status` (aposta pela `RP-1`).
- **Arquivos-alvo:** `docs/DIARIO_DE_OBRAS.md`; `docs/plans/P-0737-loop-autonomo.md`.
- **Proibido:** apagar texto (mover, nunca remover); tocar `DIARIO_HISTORICO.md`; tocar planos
  `done`/`superseded`.
- **Verificação:** `python .claude/tools/backlog.py check` exit 0; `python .claude/tools/backlog.py next` devolve `BKL-T7` (efeito da diretiva `DB-11`, não `TK-54a`); `git status --short` só os dois arquivos.
- **Pronto quando:** `check` verde e `next` responde a próxima tarefa deste plano.

### BKL-T7 — O hook e o ponto de carga [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T6`
- **Objetivo:** `backlog_hook.py` (`DB-8`): lê o JSON do `UserPromptSubmit` em stdin, casa o
  gatilho, roda `next` por importação e devolve `{"hookSpecificOutput": {"hookEventName":
  "UserPromptSubmit", "additionalContext": <saída>}}`; sem gatilho, sai em silêncio; exit ≠ 0 do
  `next` vira texto de contexto (nunca bloqueia o prompt). Registro em `.claude/projecoes.json`
  (alvo `projeto`) e `python .claude/tools/materializar.py apply` + `drift` verde.
- **Arquivos-alvo:** `.claude/tools/backlog_hook.py` (novo); `.claude/projecoes.json`;
  `tests/test_backlog.py` (TF gatilho/não-gatilho, TF exit 3 vira contexto).
- **Verificação:** pytest verde; `materializar.py drift` exit 0; `tests/test_materializar.py`
  verde (fixture do projecoes pode exigir ajuste — se exigir, é nota, não bloqueio).
- **Pronto quando:** digitar "execute o próximo passo" numa sessão nova traz o dossiê sem nenhuma
  chamada de ferramenta.

### BKL-T8 — As skills passam a invocar o instrumento [Sonnet · classe redacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T7`
- **Objetivo:** `proximo-passo` passos 1–3 e 5 → "rode `backlog.py next` / `status`" (a heurística
  em prosa vira ponteiro para §2.5 na skill `diario-de-obras`); `handover` §2 → `status` + nota;
  `scrum-master` passos 2 e 9 → `next`/`status`; `GOVERNANCA.md` §4 bullet "Retomada sem tarefa
  nomeada" → uma frase apontando o instrumento; `CHANGELOG.md` linha sob `## [Não lançado]`;
  apenso em `P-0737` `## 9` ("`AUT-T6` embrulha `backlog.py` em vez de transpor a heurística").
- **Arquivos-alvo:** as 3 skills (via `uow.py`), `GOVERNANCA.md`, `CHANGELOG.md`,
  `docs/plans/P-0737-loop-autonomo.md` (só apenso). **`README.md` fica para a `BKL-T9`.**
- **Verificação:** `Grep 'Grep "Próxima tarefa' .claude/skills/` vazio; `Grep backlog.py
  .claude/skills/` ≥ 3 arquivos; `pwsh .claude/checks/check-readme.ps1` inalterado.
- **Pronto quando:** nenhuma skill manda o agente ler diário/inbox para achar ou fechar tarefa.

### BKL-T9 — Aferição e revisão do `README.md` com veredito do dono [Opus + dono · classe redacao]
- **Status:** `ready` · 2026-09-15
- **Depende de:** `BKL-T8`
- **Objetivo:** (a) medir o pickup novo pelo método de `CUSTO_DO_PICKUP.md` `DC-4` (chars da
  saída do hook numa sessão nova + 1º `usage`) e publicar `## 15` (≤ 30 linhas) contra os 77.457
  chars da `## 3` e o alvo de 40.000 da `## 6`; (b) `README.md`: seção de ferramentas ganha
  `backlog.py`/hook, §9 do fluxo descreve o pickup por instrumento; `docs/DOC_MAP.md` entrada da
  `## 15`; `pwsh .claude/checks/check-readme.ps1` exit 0; veredito do dono.
- **Pronto quando:** o dono aceita o espelho e a `## 15` tem número.

## 5. Verificação de ponta a ponta

1. `python -m pytest tests/ -q` verde (suíte inteira: `rdo`, `telemetria`, `materializar`,
   `backlog`).
2. `python .claude/tools/backlog.py check` exit 0 no repo real.
3. Sessão nova, prompt "execute o próximo passo": o dossiê chega pelo hook; nenhum `Read` de
   `DIARIO_DE_OBRAS.md`/`_INBOX.md` no transcript.
4. `backlog.py status <ID> review --nota "…"` → `git diff` mostra só campo, célula, bloco gerado e
   nota; `check` continua verde.
5. `## 15` de `docs/CUSTO_DO_PICKUP.md` com chars medidos abaixo de 40.000.

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Migração (`BKL-T6`) perder narrativa do índice | `DB-10` + regra "mover, nunca remover" + diff revisado antes do commit |
| Hook roda `next` num repo com `check` vermelho e injeta erro a cada prompt | Gatilho estreito (`DB-8`); erro vira 1 linha de contexto com o conserto nomeado |
| `AUT-T6` (P-0737) e `BKL-T8` editarem as mesmas skills | `BKL-T8` é transitório e menor; apenso em `P-0737` `## 9` avisa a `AUT-T6` |
| Parser de `rdo.py` continuar sem aceitar prefixo | Achado registrado (`DB-14`), fora de escopo; tíquete só se o dono pedir |

## 7. Registro (após aprovação, Controle 1.1 — não é execução)

Copiar este plano para `docs/plans/P-0739-backlog-instrumento.md`; apensar linha em
`docs/plans/_INBOX.md` e atualizar `Próximo id: P-0740`; reescrever a diretiva (`DB-11`) movendo o
texto atual para `## TK-54`; apenso em `P-0737` `## 9`. Depois, parar (Regra 1).

## Achados da execução

### AE-1 — `BKL-T2` blocked: tabela §2.1 não descreve cabeçalho de tíquete/subtarefa sem ambiguidade

**2026-09-16, achado do executor (`pantonic-executor`), devolvido sem decisão (Regra 8).**

A linha `tíquete` da tabela §2.1 acima (idêntica em `.claude/skills/diario-de-obras/SKILL.md:135-137`)
tem a coluna "cabeçalho" preenchida só com `idem`:

```
| tíquete | `docs/DIARIO_DE_OBRAS.md`, `## TK-<n> — <título>` | idem | mesmos campos da tarefa (`Status`, `Tipo`, `Notas de execução`) |
```

`idem` remete, por convenção de tabela, ao valor da linha `tarefa` logo acima — heading nível 3
com bracket (`### <ID> — <título> [<modelo> · classe <classe>]`, `DP-C`). Mas a própria coluna
"residência viva" desta mesma linha já mostra o cabeçalho completo e diferente: heading nível 2,
sem bracket (`## TK-<n> — <título>`). As duas leituras da tabela produzem parsers e vereditos de
`check` diferentes:

- **Leitura A** — cabeçalho de tíquete é `## TK-<n> — <título>` (nível 2, sem bracket), como a
  própria célula "residência viva" mostra.
- **Leitura B** — `idem` clona o valor inteiro da célula "cabeçalho" da linha `tarefa`: nível 3,
  com bracket `[<modelo> · classe <classe>]`.

**Confronto com o estado real do diário** (nenhuma das duas bate integralmente):

```
docs/DIARIO_DE_OBRAS.md:705   ## TK-23 — A variante (b) do proxy de ocupação de contexto        (nível 2, sem bracket → bate com A)
docs/DIARIO_DE_OBRAS.md:721   ## TK-38 — Comunicação entre agente e humano — ...                (nível 2, sem bracket → bate com A)
docs/DIARIO_DE_OBRAS.md:729   ## TK-54 — Extrato do custo de abertura de uma janela principal   (nível 2, sem bracket → bate com A)
docs/DIARIO_DE_OBRAS.md:1170  ### TK-54a — O extrato [classe investigacao]                       (nível 3, bracket sem "<modelo> ·" → não bate com A nem B)
docs/DIARIO_DE_OBRAS.md:1233  ### TK-54b — A fonte da bimodalidade [classe investigacao]         (nível 3, bracket sem "<modelo> ·" → não bate com A nem B)
```

Tíquete-pai bate com a leitura A; subtarefa não bate com nenhuma leitura nem com o `DP-C` citado
(falta `<modelo>` no bracket). A tabela §2.1, como publicada, não descreve nenhum estado do mundo
de forma inequívoca — três formas coexistem no repo real (`[Sonnet · classe implementacao]` nas
tarefas de plano, `## TK-n` sem bracket nos tíquetes, `[classe investigacao]` nas subtarefas) e a
tabela não nomeia qual é a normativa para tíquete/subtarefa.

**Por que bloqueia `BKL-T2` especificamente:** a tarefa exige que `check` acuse violações de §2 e
que a lista de defeitos reais vá para `BKL-T6` como insumo. Um parser escrito sobre uma aposta do
executor entre A/B produziria uma lista de defeitos construída sobre leitura não autorizada — a
mesma classe de decisão que a Regra 8 reserva ao dono/planejamento.

**Pendência para a próxima rodada de planejamento:** decidir a forma normativa do cabeçalho de
tíquete e de subtarefa (opções: ratificar leitura A, ratificar leitura B, ou redigir uma terceira
forma que descreva o real e ajustar tabela + migração `BKL-T6` de acordo) e corrigir a célula
"cabeçalho" da linha `tíquete` em §2.1 (aqui e em `SKILL.md:135-137`) para não depender de `idem`
ambíguo. Sem essa decisão, `BKL-T2` não pode ser retomada.

**Escopo não tocado pelo executor:** `.claude/tools/backlog.py`, `tests/test_backlog.py`,
`tests/fixtures/backlog/` seguem inexistentes; nenhum outro arquivo foi criado ou editado.

**Desfecho (`RP-1`, 2026-09-16):** absorvido. Decisões `DB-17`..`DB-19`; tabela §2.1 corrigida aqui e na
skill `diario-de-obras`; card `BKL-T2` reescrito com a gramática e as violações inline; `BKL-T2`
volta a `ready` e é a próxima tarefa (diretiva e `Fila corrente` do diário).

### RP-1 — Rodada de replanejamento sobre `AE-1` (2026-09-16, classe replanejamento)

**Classificação:** técnica — a forma do cabeçalho é gramática do instrumento, não objetivo,
prioridade nem escopo; decidida pelo planejador (`DB-17`..`DB-19`), sem rodada de decisões ao dono.
O dono pediu a rodada, a análise crítica da causa e a governança do gatilho.

**Análise crítica — por que o plano nasceu com o defeito:**

1. **Gramática autorada sem inventário do corpus.** A §2.1 saiu da `DP-C` e da memória do
   planejador, não de um dossiê com as formas reais do diário. O plano não tem `## 1. Fatos
   estabelecidos` (esqueleto obrigatório do agente): a tabela não tinha contra o que ser testada,
   e as três formas reais (tarefa de plano com `[<modelo> · classe]`, tíquete `##` sem bracket,
   subtarefa `###` com `[classe …]` sem modelo) nunca foram confrontadas com as linhas dela. O
   inventário `F-1` que agora precede §2 é o que faltava.
2. **`idem` é ponteiro dentro de tabela.** A auto-auditoria do planejador proíbe restrição por
   ponteiro no card e tem léxico proibido, mas a lista não cobria remissão em tabela normativa
   (`idem`, `análogo`) e a auditoria é feita card a card: a §2, que os cards citam por ponteiro,
   não passou por nenhuma passada.
3. **Card com restrição por ponteiro.** `BKL-T2` dizia "acusa cada violação de §2" em vez de
   enumerar as violações inline; o executor frio precisou abrir a §2 e foi ele quem achou a
   contradição — no momento mais caro (contexto de execução aberto, nada produzido).
4. **Sem contingência para forma desconhecida.** O card não dizia o que fazer com forma real fora
   da gramática. Com `DB-19`, só ambiguidade *da gramática* bloqueia; dado que não casa vira
   violação nomeada.
5. **Registro do plano incompleto.** O plano foi aprovado e o inbox recebeu a linha, mas o índice
   do diário não ganhou a linha `P-0739` e a `BKL-T1` rodou sem drenar o inbox — o kanban não
   sabia que o plano existia. Corrigido nesta rodada (linha drenada, índice atualizado).
6. **Custo.** Um contexto de executor Sonnet sem produto, mais esta rodada. A pergunta ao scout
   que evitaria tudo ("liste todas as formas de cabeçalho `## TK-` e `### TK-` do diário, com
   linha e contagem") custaria um dossiê de ≤ 10 linhas na fase 1.

**Lição para o planejador** (aplicada em `.claude/agents/pantonic-planner.md`): fase 1 exige
inventário do corpus para plano de parser/lint/migração/gramática; fase 4 ganha o teste do parser
frio (toda linha da gramática com exemplo real, toda forma real com destino) e `idem`/`análogo`
entram no léxico proibido, inclusive em célula de tabela.

**Governança** (aplicada em `GOVERNANCA.md` §7 item 17, `G-REPLAN`): bloqueio por `premissa` abre a
rodada de replanejamento como próxima tarefa do plano, roteada ao planejador; `scrum-master`
`A3b`, `proximo-passo` e `diario-de-obras` alinhados; `CHANGELOG.md` sob `## [Não lançado]`.

**Saída:** `DB-17`..`DB-20`; `F-1`; §2.1 corrigida aqui e na skill; `BKL-T2` reescrita, `ready`, no
topo da fila (diretiva + `Fila corrente` do diário); cards `BKL-T1..T9` com linha `Status`;
`P-0739` `in-progress` (1/9) no índice; `AE-1` absorvido. Consumo: `docs/telemetria.tsv`
(`BKL-RP1`, contado).

### AE-2 — `BKL-T2` blocked: o dossiê de evidência não pode ser gerado para ID prefixado

**2026-09-16, achado do orquestrador no pickup, devolvido sem decisão (Regra 8). Decisão do dono
no mesmo ato: anotar como bloqueio do card e escalar ao planejador na janela seguinte.**

A entrega da `BKL-T2` existe e está verde, mas a **rodada de revisão** que a `Fila corrente` exigia
antes da `BKL-T3` não roda — o `review_evidence.py` não localiza a tarefa:

```
$ python .claude/tools/review_evidence.py --plano docs/plans/P-0739-backlog-instrumento.md \
    --tarefa BKL-T2 --desde HEAD --out docs/RDO/evidencia/P-0739-BKL-T2.md
review_evidence: FALHOU - tarefa: 'BKL-T2' não encontrada em 'docs\plans\P-0739-backlog-instrumento.md'
```

**Causa medida:** o `review_evidence.py` reusa `extrair_dossie` de `.claude/tools/rdo.py:186`, que
casa o heading por `_ID_HEADER_RE = ^### (T[0-9]+[a-z]?)(?=[\s—])` (`rdo.py:79`) e por
`_HEADER_BRACKET_RE` (`rdo.py:80-84`) — as duas **sem** o prefixo opcional que a `DB-14` tornou
normativo (`(?:[A-Z0-9]+-)?T[0-9]+[a-z]?`). São os dois únicos pontos: `grep -n 'T\[0-9\]'` não casa
mais nada em `rdo.py` e não casa nada em `review_evidence.py`.

**O que ainda funciona:** `rdo.py laudo --plano P-0739 --tarefa BKL-T2` aceita o ID prefixado — o
gerador do laudo não passa por `extrair_dossie`. O bloqueio é só no dossiê de evidência, que o
protocolo do `pantonic-reviewer` nomeia como uma das "três entradas de julgamento, e só elas" e que
é a autoridade mecânica sobre as dimensões `guardas` e `testes`.

**Alcance:** os três planos vivos usam prefixo — `AUT-*` (`P-0737`, 10 tarefas), `CTX-*` (`P-0738`,
17) e `BKL-*` (`P-0739`, 9). Nenhuma tarefa deles é revisável pelo instrumento hoje. O precedente
que a própria `DB-14` registra ("por isso não há RDO de `CTX-*`") era fechar sem RDO — desfecho que
nunca foi decidido em lugar nenhum, só herdado.

**Por que não foi corrigido no pickup:** a §6 deste plano gateia a correção no dono ("Achado
registrado (`DB-14`), fora de escopo; tíquete só se o dono pedir") e a rota de um plano é do dono
(Regra 8). Consultado no ato, o dono optou por anotar o bloqueio e escalar.

**Rota:** `RP-2` — rodada de replanejamento sobre este achado, delegada ao `pantonic-planner` na
próxima janela (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). É a **próxima tarefa do plano**: a
`BKL-T3` não é despachada enquanto a rodada não fechar. Matéria a decidir: se o gate de revisão
vale para plano com ID prefixado e, valendo, por qual rota (corrigir as 2 regexes de `rdo.py` mais
regressão em `tests/test_rdo.py`, ou outra).

**Não descartar:** a entrega da `BKL-T2` está no repositório e verde (`.claude/tools/backlog.py`,
`tests/test_backlog.py`, `tests/fixtures/backlog/{verde,vermelho}/`) — o bloqueio é da revisão, não
do entregável. Pelo fechamento (c) da máquina de transições, `blocked` por escalada não dispara RDO.
