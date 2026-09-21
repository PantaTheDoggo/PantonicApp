# P-0744 — A especificação do agente de planejamento

**Data:** 2026-09-20 · **Origem:** diretiva do dono sobre o Marco 2 do `P-0741`
(`docs/plans/P-0741-modelo-conceitual.md`, `AE-18`), apontamento 3 · **Plano de origem:** `P-0741`
(classe B — continuação; e `P-0743` é o irmão de fronteira disjunta) · **Status:** `blocked` ·
2026-09-20 · depende de `P-0743` `done`: este plano é o **primeiro escrito na forma nova** do
modelo, e o instrumento que lê essa forma nasce na `DOM-T3` do `P-0743` (`D-11` daquele plano) ·
**Prefixo das tarefas no diário:** `PLS-T<n>` · **Prefixo das decisões:** `DPL-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10), nada a
comparar.
**Ordem de execução:** PLS-T1 → PLS-T2 → PLS-T3.
**Modelo de planejamento:** Opus 5 (rodada de replanejamento de 2026-09-20).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a `## 1. Modelo conceitual` deste plano, que é a forma nova aplicada | `go` = o plano sai de `blocked` para `ready` quando o `P-0743` fechar; `no-go` = `cancelled` |
| **Marco 2** | `docs/planner-spec.md` depois da `PLS-T2`, mais o `README.md` revisado (`PLS-T3`) | aceite registrado no diário (`GOVERNANCA.md` §4.5) |

**Tarefas:** 3 (`PLS-T1`..`PLS-T3`), fila única, sequencial.

> **Antes do `P-0743` fechar, `modelo.py check` sobre este plano sai `1`**, porque o instrumento
> vigente não conhece a forma nova. É o motivo do `blocked` no cabeçalho, e não um defeito deste
> plano: a `DOM-T3` do `P-0743` tem, na `Verificação`, o comando que exige exit `0` sobre este
> arquivo.

---

## 0. O problema, verbatim

Diretiva do dono, 2026-09-20, sobre a leitura do Marco 2 do `P-0741` (`AE-18`), apontamento 3, nas
palavras dele:

> **A `MC-T2` é responsabilidade herdada de outro papel.** O instrumento de conferência é
> atribuição do revisor e do planejador, não coisa intrínseca do modelo conceitual. Pede varredura
> dos artefatos já gerados atrás do que pertence a outros módulos — e cita como caso a
> operacionalização de tarefas a partir do plano, que é do agente de planejamento e deveria ter
> **spec própria**, a ser criada se não houver iniciativa de melhoramento desse agente.

A verificação foi feita em 2026-09-20: **não existe iniciativa de melhoramento do agente de
planejamento** — busca por "planner-spec" e "spec do planejador" em `docs/` e `.claude/` não
retornou ocorrência. O precedente de especificação de agente neste repositório é
`docs/consultant-spec.md`, com 440 linhas e onze seções. Logo, a spec se cria, e é este plano.

---

## 1. Modelo conceitual

> **Como ler esta seção (Marco 1).** Ela descreve, em objetos e operações encadeadas, o que este
> plano entrega. É a forma nova, aplicada pela primeira vez — a mesma que a `## 7` do `P-0743`
> mostra renderizada pelo instrumento, nos três momentos do plano.

**Estado do modelo:** versão 1 · 2026-09-20 · autor: planejador · 3 operações · última mudança: nenhuma

### 1.1 Objetos

| objeto | o que é | contrato | origem |
|---|---|---|---|
| registro medido da atuação do planejador | o conjunto fechado de rodadas de replanejamento e de achados de execução já escritos no repositório | uma ocorrência por linha, com o plano, a data, a classe do erro e a verificação que o teria evitado | externo |
| agregado da atuação | o resumo que volta da sondagem, dentro do teto de linhas | uma tabela por dimensão da especificação, com contagem e ocorrência de exemplo, sem nenhum dado bruto | OP-1 |
| especificação do planejador | o documento que descreve a figura do planejamento como o precedente do consultor descreve a dele | um documento próprio, uma seção por dimensão, toda afirmação ancorada em ocorrência do agregado | OP-2 |
| índice de documentos | a porta de entrada por onde todo documento grande do repositório é alcançado | uma entrada por documento, com tamanho, âncoras e a forma de acesso barata | externo |

### 1.2 Fluxo de operações

- **OP-1** — O investigador percorre o registro medido da atuação do planejador e devolve o agregado da atuação, dentro do teto de linhas.
  - `precisa de: registro medido da atuação do planejador` · `tarefas: PLS-T1`
- **OP-2** — O redator escreve a especificação do planejador sobre o agregado da atuação, uma seção por dimensão, sem nenhuma afirmação que o agregado não sustente.
  - `precisa de: agregado da atuação` · `tarefas: PLS-T2`
- **OP-3** — O mantenedor inscreve a especificação do planejador no índice de documentos e confere a documentação pública contra a árvore.
  - `precisa de: especificação do planejador, índice de documentos` · `tarefas: PLS-T3`

### 1.3 Mudanças do modelo

| id | data | autor | operações | o que mudou e por quê |
|---|---|---|---|---|
| — | — | — | — | modelo na versão de autoria; nenhuma mudança até aqui |

---

## 2. Fatos estabelecidos

- **F-1** — Não existe iniciativa de melhoramento do agente de planejamento: busca por
  `planner-spec`, `spec do planejador` e `spec do agente de planejamento` em `docs/` e `.claude/`
  não retornou ocorrência (2026-09-20). A condição que o dono pôs — "criar se não houver" — está
  satisfeita.
- **F-2** — `docs/consultant-spec.md` tem 440 linhas e onze seções, nesta ordem: a figura em uma
  página; (a) gatilho; (b) domínio de decisão; (c) fronteira com o planejador; (d) instrumento;
  (e) custo e teto; (f) encerramento; (g) fim de vida por limite; (h) estatística do próprio
  acionamento; o que a especificação não fecha; (i) custo por acionamento. Medido 2026-09-20.
- **F-3** — `docs/DOC_MAP.md` tem entrada para `docs/consultant-spec.md` na linha 157, com o
  tamanho aproximado e a forma de acesso barata por `Grep` de heading. Medido 2026-09-20.
- **F-4** — O registro medido da atuação do planejador já está escrito e é um corpus fechado:
  as entradas `RP-1`..`RP-7` citadas em `.claude/agents/pantonic-planner.md`, as seções
  `## Achados da execução` de `docs/plans/P-0739-backlog-instrumento.md`,
  `docs/plans/P-0740-loop-de-modulos.md` e `docs/plans/P-0741-modelo-conceitual.md`, e o
  documento `docs/Entregas Aceitas/Entregas - P-0743.md` (o as-is do `P-0741`+`P-0743`, promovido
  a entrega aceita em 2026-09-21; até então residia em `docs/OPERACOES_AS_IS.md`). Nenhuma
  sondagem fora desse corpus é necessária.
- **F-5** — `docs/telemetria.tsv` carrega o consumo medido por tarefa e por sessão, e é a fonte da
  dimensão de custo do precedente (`docs/consultant-spec.md` §6 e §11).
- **F-6** — `.claude/agents/pantonic-planner.md` tem 421 linhas e já carrega o **como** do papel;
  a residência do **escopo** do papel é a matriz de responsabilidades de `GOVERNANCA.md` §3, e só
  ela (`G-SCOPE`, §7 item 15). Uma especificação não pode reabrir nenhuma das duas.
- **F-7** — `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai
  `0` (medido 2026-09-20, antes deste plano existir).
- **F-8** — `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai `0` e começa por
  `check-readme: OK - 9 agente(s), 11 skill(s), 20 guardrail(s)` (medido 2026-09-20). Depois da
  `DOM-T4` do `P-0743` o numeral passa a `10 agente(s)`.

---

## 3. Decisões (fechadas neste ato; o executor não as reabre)

| id | decisão | razão |
|---|---|---|
| `DPL-1` | A especificação mora em `docs/planner-spec.md`, ao lado do precedente | `F-2`: `docs/consultant-spec.md` estabeleceu a convenção de nome e de lugar para spec de agente neste repositório |
| `DPL-2` | O esqueleto é o das **dez dimensões** da §4 deste plano, derivado do precedente e com uma dimensão nova — a operacionalização do plano em tarefas, que é o caso que o dono nomeou | o precedente cobre a figura ad-hoc do consultor; o planejador tem uma atribuição que o consultor não tem, e é justamente a que o dono apontou |
| `DPL-3` | Toda afirmação da especificação é ancorada em ocorrência do agregado; afirmação sem ocorrência não entra | o precedente é um documento **medido**; uma spec escrita de memória seria ficção, e ficção sobre o próprio papel é pior que a ausência dela |
| `DPL-4` | O levantamento é **tarefa de investigação** com corpus fechado e teto de agregado, não leitura do redator | o corpus tem milhares de linhas; ingeri-lo inteiro no contexto de quem redige é o desperdício que a doutrina de coleta proíbe |
| `DPL-5` | A especificação **não** reabre o escopo do papel nem o protocolo de conduta: aponta para a matriz de `GOVERNANCA.md` §3 e para `.claude/agents/pantonic-planner.md` | `F-6` e `G-SCOPE`; três residências para o mesmo assunto é a duplicação que a doutrina proíbe |
| `DPL-6` | O teto do agregado é **120 linhas** | o precedente tem 440 linhas e dez dimensões; 12 linhas de agregado por dimensão é o que sustenta uma seção sem trazer dado bruto |
| `DPL-7` | Este plano não toca nenhum arquivo de doutrina, de instrumento, de agente ou de skill | é a fronteira disjunta com o `P-0743` (§6), e é o que impede dois planos vivos disputando a mesma rota |

---

## 4. As dez dimensões da especificação (normativa; a `PLS-T2` as escreve)

> Esta seção é a **residência única** da lista de dimensões. A `PLS-T1` mede uma tabela por
> dimensão; a `PLS-T2` escreve uma seção por dimensão. Nenhuma outra seção deste plano reenuncia a
> lista.

| # | dimensão | a pergunta que a seção responde |
|---|---|---|
| 1 | A figura, em uma página | o que é o planejamento, em um parágrafo que quem nunca viu entende |
| 2 | Gatilho | o que aciona uma sessão de planejamento, e o que **não** aciona |
| 3 | Domínio de decisão | o que o planejador fecha por si, e o que sobe ao dono |
| 4 | Operacionalização do plano em tarefas | como um plano vira cards: qual é a unidade, o que entra num card, o que fica fora, e por que a régua de partição é o tema |
| 5 | Fronteira | onde o planejamento termina e começam o consultor, a orquestração e a revisão |
| 6 | Instrumento | que comandos o planejador roda, por que roda, e o que ele nunca mede por conta própria |
| 7 | Custo e teto | quanto custa uma sessão de planejamento, medido, e quando não abrir uma |
| 8 | A rodada de replanejamento | entrada, saída e posição na fila, com a série das rodadas já ocorridas |
| 9 | Estatística do próprio acionamento | quantas rodadas houve, quantas fecharam como decisão técnica e quantas subiram ao dono |
| 10 | O que esta especificação não fecha | as perguntas que o corpus medido não responde, nomeadas em vez de respondidas por adivinhação |

---

## 5. Invariantes de execução

- **I-1** — Nenhum card edita `.claude/tools/*`, `.claude/agents/*`, `.claude/skills/*`,
  `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`. É a fronteira com o `P-0743` (`DPL-7`).
- **I-2** — Piso de regressão é relação: o total de `python -m pytest tests -q` re-medido no
  despacho não reduz. Nenhuma tarefa deste plano acrescenta teste, porque nenhuma entrega código.
- **I-3** — Toda afirmação da especificação é ancorada em ocorrência do agregado (`DPL-3`).
- **I-4** — Nenhuma tarefa commita.
- **I-5** — Todo número de aceite deste plano é referência datada de 2026-09-20; quem despacha o
  re-deriva antes de delegar.
- **I-6** — Card que muda uma enumeração fecha, no mesmo card, as frases da mesma seção que contam
  o conjunto.

---

## 6. Fronteira com o `P-0743` (disjunção declarada)

| plano | o que toca |
|---|---|
| `P-0743` | `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `tests/test_modelo.py`, `tests/fixtures/modelo/`, `.claude/agents/` (quatro arquivos), `README.md` §8.1 e §11, `.claude/README.md` |
| `P-0744` | `docs/planner-spec.md` (novo), `docs/DOC_MAP.md`, `README.md` — **só** na revisão final da `PLS-T3`, que é a tarefa que `G-README` dever 2 exige de toda sprint |

A interseção é **um** arquivo, o `README.md`, e ela é resolvida pela ordem: o `P-0744` está
`blocked` até o `P-0743` fechar, e a `PLS-T3` revisa o README já na forma que a `DOM-T6` deixou.
Nenhum outro arquivo aparece nas duas linhas.

---

## 7. Tarefas

### PLS-T1 — O agregado medido da atuação do planejador [Sonnet · esforço high · classe investigacao]
- **Status:** `ready` · 2026-09-20
- **Objetivo:** a seção `## 11. Agregado medido` deste plano preenchida com uma tabela por dimensão
  da §4, dentro de 120 linhas, sem nenhum dado bruto.
- **Fundamento:** `DPL-3`, `DPL-4`, `DPL-6`; fatos `F-4`, `F-5`. O corpus é fechado pela `F-4` e
  não se amplia.
- **Operação do modelo:** `OP-1`
  - OP-1: O investigador percorre o registro medido da atuação do planejador e devolve o agregado da atuação, dentro do teto de linhas.
  - precisa de: registro medido da atuação do planejador — uma ocorrência por linha, com o plano, a data, a classe do erro e a verificação que o teria evitado
- **Camada e fronteira:** nenhuma camada de produto é tocada. A tarefa lê e escreve **só** neste
  arquivo de plano.
- **Método de sondagem:**
  - **Corpus fechado, nesta ordem e só ele:** (1) `.claude/agents/pantonic-planner.md`, as entradas
    `RP-1`..`RP-7` e os casos `AE-*` e `DM-*` que elas citam; (2)
    `docs/plans/P-0739-backlog-instrumento.md`, seção `## Achados da execução`; (3)
    `docs/plans/P-0740-loop-de-modulos.md`, seção `## Achados da execução`; (4)
    `docs/plans/P-0741-modelo-conceitual.md`, seção `## Achados da execução`; (5)
    `docs/Entregas Aceitas/Entregas - P-0743.md`, inteiro; (6) `docs/consultant-spec.md`, §1 e §4, para a fronteira;
    (7) `docs/telemetria.tsv`, filtrado pelas linhas cujo papel é planejamento.
  - **Acesso barato:** cada seção `## Achados da execução` se alcança por
    `grep -n '^## Achados da execução' <plano>` seguido de leitura com `offset` e `limit` a partir
    da linha devolvida. Nenhum plano é lido inteiro.
  - **Métricas, por dimensão da §4:** número de ocorrências encontradas; a ocorrência mais antiga e
    a mais recente, com data; a classe de erro dominante, quando houver; e **uma** ocorrência de
    exemplo, citada por identificador e data, nunca transcrita.
  - **Métricas de custo (dimensão 7):** de `docs/telemetria.tsv`, o número de sessões de
    planejamento registradas, o consumo mediano e o máximo, e a data da primeira e da última.
  - **Métricas de acionamento (dimensão 9):** número de rodadas de replanejamento ocorridas;
    quantas fecharam como decisão técnica ou tática no próprio contexto; quantas subiram ao dono;
    quantas terminaram com o plano `superseded`.
  - **Formato do agregado que volta:** a seção `## 11. Agregado medido` deste arquivo, inserida
    imediatamente antes de `## Achados da execução` e depois de `## 10. Riscos`, com **dez**
    subseções `### <n>. <dimensão>` na ordem da §4, cada uma com uma tabela de no máximo oito
    linhas. **Teto: 120 linhas** para a seção inteira (`DPL-6`).
  - **Nenhum dado bruto entra no agregado:** nenhuma citação literal de achado, nenhum trecho de
    plano, nenhuma linha de telemetria copiada. Só contagem, data, identificador e classe.
- **Restrições desta tarefa:**
  - Não ampliar o corpus. Fonte fora da lista de sete itens acima não entra, por mais pertinente
    que pareça.
  - Não editar nenhum arquivo além de `docs/plans/P-0744-spec-do-planejador.md` (`I-1`).
  - Não escrever prosa de recomendação: a tarefa mede, não conclui.
  - Não commitar (`I-4`).
- **Não fazer:**
  - Não abrir `docs/DIARIO_DE_OBRAS.md` nem `docs/DIARIO_HISTORICO.md`: o corpus é o da `F-4`, e o
    diário está fora dele por tamanho.
  - Não criar `docs/planner-spec.md`: é a `PLS-T2`.
  - Não transcrever nenhum achado: o agregado é contagem, não antologia.
- **Contingências:**
  1. Se uma dimensão da §4 não tiver nenhuma ocorrência no corpus → a subseção dela existe com a
     tabela vazia e a linha literal `sem ocorrência no corpus medido`. Dimensão sem ocorrência é
     insumo da dimensão 10, não motivo de parada.
  2. Se `docs/telemetria.tsv` não tiver nenhuma linha cujo papel seja planejamento → a subseção 7
     registra `sem linha de planejamento em docs/telemetria.tsv em <data>` e segue.
  3. Se o agregado passar de 120 linhas → cortar pela cauda das tabelas, mantendo a ocorrência mais
     antiga e a mais recente de cada dimensão, e registrar na linha de retorno
     `contingência 3 acionada: <dimensão> cortada de <n> para 8 linhas`.
  4. Se alguma das sete fontes do corpus não existir no caminho declarado → parar e sinalizar
     `blocked` razão `premissa`, com o caminho na linha de retorno.
- **Testes:** nenhum — a entrega é agregado em texto.
- **Verificação:**

  ```
  grep -c '^### ' docs/plans/P-0744-spec-do-planejador.md
  ```
  imprime `16` — as três subseções da §1, as dez do agregado e os três cards (hoje imprime `6`,
  medido 2026-09-20: três subseções da §1 e três cards).

  ```
  grep -n '^## 11. Agregado medido' docs/plans/P-0744-spec-do-planejador.md
  ```
  imprime uma linha (hoje não imprime nada).

  ```
  python -c "import pathlib;t=pathlib.Path('docs/plans/P-0744-spec-do-planejador.md').read_text(encoding='utf-8');s=t.split('## 11. Agregado medido')[1].split('\n## ')[0];print(len(s.splitlines()))"
  ```
  imprime um número menor ou igual a `120` (hoje o comando falha, porque a seção não existe).

  `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** a seção `## 11. Agregado medido` existe com as dez subseções na ordem da §4,
  cada uma com a tabela ou com a linha `sem ocorrência no corpus medido`, e a seção inteira tem no
  máximo 120 linhas — o número que tem de existir ao final é, por dimensão, a contagem de
  ocorrências e a data da mais antiga e da mais recente.
- **Fora do escopo desta tarefa:** a redação da especificação (`PLS-T2`) e o índice de documentos
  (`PLS-T3`).

### PLS-T2 — A especificação do agente de planejamento [Opus · esforço xhigh · classe redacao]
- **Status:** `ready` · 2026-09-20
- **Depende de:** `PLS-T1`
- **Objetivo:** `docs/planner-spec.md` escrito, com uma seção por dimensão da §4 e nenhuma
  afirmação que o agregado da `PLS-T1` não sustente.
- **Fundamento:** `DPL-1`, `DPL-2`, `DPL-3`, `DPL-5`; fatos `F-2`, `F-6`. A lista de dimensões tem
  residência única na §4 deste plano; este card a consome, não a reenuncia.
- **Operação do modelo:** `OP-2`
  - OP-2: O redator escreve a especificação do planejador sobre o agregado da atuação, uma seção por dimensão, sem nenhuma afirmação que o agregado não sustente.
  - precisa de: agregado da atuação — uma tabela por dimensão da especificação, com contagem e ocorrência de exemplo, sem nenhum dado bruto
- **Camada e fronteira:** documentação em `docs/`. Nenhum código, nenhum teste, nenhum arquivo do
  kit.
- **Domínio:** *planejador* é o papel declarado na matriz de responsabilidades de `GOVERNANCA.md`
  §3 — quem produz os artefatos iniciais, decide rota e decompõe em tarefas atômicas fechadas.
  *Rodada de replanejamento* é a forma da `G-REPLAN` (`GOVERNANCA.md` §7 item 17). Nenhum dos dois
  é redefinido por este documento: o invariante é que a especificação **descreve** a figura e
  **não** altera o escopo do papel (`DPL-5`).
- **Arquivos-alvo:**
  - `docs/planner-spec.md` (novo)
- **Passos:**
  1. Criar `docs/planner-spec.md` com o título `# Especificação do agente de planejamento` e um
     cabeçalho de duas linhas: a data, e a frase que declara a fonte — o agregado medido da
     `## 11. Agregado medido` de `docs/plans/P-0744-spec-do-planejador.md`.
  2. Escrever, na ordem da §4 deste plano, uma seção `## <n>. <dimensão>` por dimensão, cada uma
     respondendo a pergunta que a §4 associa a ela.
  3. Em cada seção, ancorar toda afirmação numérica ou factual na subseção correspondente do
     agregado, citando a dimensão e o número. Afirmação sem ancoragem não entra (`DPL-3`).
  4. Na seção 5 (Fronteira), escrever a fronteira com o consultor como o **espelho** da §4 de
     `docs/consultant-spec.md`, que já a declara do lado de lá; onde as duas divergirem, registrar
     a divergência na seção 10 em vez de escolher um lado.
  5. Na seção 10, listar as perguntas que o corpus medido não responde, uma por linha, cada uma com
     o que seria preciso medir para respondê-la.
  6. Abrir o documento com uma seção `## 0. O que esta especificação não é`, de três linhas: não é
     a residência do escopo do papel, que é a matriz de `GOVERNANCA.md` §3; não é a residência do
     protocolo de conduta, que é `.claude/agents/pantonic-planner.md`; é a descrição **medida** da
     figura, para quem precisa decidir quando acioná-la e quanto ela custa.
  7. Rodar as verificações abaixo.
- **Restrições desta tarefa:**
  - Nenhuma afirmação sem ancoragem no agregado (`I-3`). Onde o agregado disser
    `sem ocorrência no corpus medido`, a seção correspondente diz isso e nada mais.
  - Não reabrir o escopo do papel nem o protocolo de conduta (`DPL-5`): as duas residências são
    citadas, nunca reenunciadas.
  - Não editar nenhum arquivo do kit nem de doutrina (`I-1`).
  - Não commitar (`I-4`).
- **Não fazer:**
  - Não editar `.claude/agents/pantonic-planner.md`, por mais que a redação sugira melhorias: o
    que a redação descobrir sobre o protocolo vira linha da seção 10, não emenda do agente.
  - Não copiar texto de `docs/consultant-spec.md`: o precedente dá o esqueleto, não o conteúdo.
  - Não inventar número: número que o agregado não tem não existe neste documento.
  - Não escrever a entrada do índice de documentos: é a `PLS-T3`.
- **Contingências:**
  1. Se a seção `## 11. Agregado medido` deste plano não existir ou estiver vazia → parar e
     sinalizar `blocked` razão `dependencia`.
  2. Se uma dimensão tiver agregado vazio → a seção dela existe, com a frase
     `sem ocorrência no corpus medido em 2026-09-20` e o ponteiro para a linha correspondente da
     seção 10. A seção não é omitida.
  3. Se a fronteira do passo 4 divergir de `docs/consultant-spec.md` §4 → registrar a divergência
     na seção 10 e devolver, na linha de retorno, `contingência 3 acionada: divergência de
     fronteira com o consultor`.
- **Testes:** nenhum — a entrega é documento.
- **Verificação:**

  ```
  grep -c '^## ' docs/planner-spec.md
  ```
  imprime `11` — a seção `## 0` mais as dez dimensões (hoje o arquivo não existe).

  ```
  grep -c 'sem ocorrência no corpus medido' docs/planner-spec.md
  ```
  imprime um número menor ou igual ao número de dimensões com agregado vazio na `PLS-T1`.

  ```
  python -c "import pathlib;print(len(pathlib.Path('docs/planner-spec.md').read_text(encoding='utf-8').splitlines()))"
  ```
  imprime um número entre `150` e `500` — abaixo de 150 a spec não cobre dez dimensões, acima de
  500 ela passou o precedente de 440 linhas sem ter mais matéria medida que ele.

  `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** `docs/planner-spec.md` existe com as onze seções, cada dimensão da §4 tem
  exatamente uma seção, e nenhuma seção carrega número que não esteja no agregado da `PLS-T1`.
- **Fora do escopo desta tarefa:** o índice de documentos e a revisão do README (`PLS-T3`).

### PLS-T3 — O índice de documentos, e a revisão do README [Sonnet · esforço medium · classe implementacao]
- **Status:** `ready` · 2026-09-20
- **Depende de:** `PLS-T2`
- **Objetivo:** `docs/planner-spec.md` alcançável pelo índice de documentos, e o `README.md`
  revisado contra o estado da árvore ao fim deste plano.
- **Fundamento:** `DPL-1`; fatos `F-3`, `F-8`; invariante `I-6`. É a tarefa de revisão de README
  que `G-README` dever 2 exige de toda sprint.
- **Operação do modelo:** `OP-3`
  - OP-3: O mantenedor inscreve a especificação do planejador no índice de documentos e confere a documentação pública contra a árvore.
  - precisa de: especificação do planejador — um documento próprio, uma seção por dimensão, toda afirmação ancorada em ocorrência do agregado; índice de documentos — uma entrada por documento, com tamanho, âncoras e a forma de acesso barata
- **Camada e fronteira:** documentação. Nenhum código, nenhum arquivo do kit.
- **Arquivos-alvo:**
  - `docs/DOC_MAP.md:157` (entrada de `docs/consultant-spec.md`, que é o modelo da entrada nova)
  - `README.md` (só o que a revisão do passo 3 apontar)
- **Passos:**
  1. Acrescentar a `docs/DOC_MAP.md` uma entrada `## docs/planner-spec.md (~<n> linhas)` na mesma
     forma da entrada de `docs/consultant-spec.md` da linha 157: o resumo em uma linha, a lista de
     seções e a linha `**Acesso:**` com o `Grep` de heading.
  2. Preencher `<n>` com a contagem real de linhas de `docs/planner-spec.md`, obtida por
     `python -c "import pathlib;print(len(pathlib.Path('docs/planner-spec.md').read_text(encoding='utf-8').splitlines()))"`.
  3. Percorrer o `README.md` contra o estado da árvore ao fim deste plano e corrigir o que estiver
     defasado, rodando `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e fechando o que ele
     apontar.
  4. Devolver, na linha de retorno, a saída literal de `check-readme.ps1` — é o insumo do veredito
     do dono.
- **Restrições desta tarefa:**
  - Entrada do índice segue a forma da entrada vigente de `docs/consultant-spec.md`, incluindo a
    linha `**Acesso:**` (`F-3`). Não inventar forma nova.
  - Se o índice de documentos tiver uma frase que conte as entradas, ela se fecha neste mesmo card
    (`I-6`).
  - Não editar `.claude/README.md` nem regenerar região alguma.
  - Não commitar (`I-4`).
- **Não fazer:**
  - Não alterar `docs/planner-spec.md`: ele está fechado pela `PLS-T2`.
  - Não alterar a tabela **Agentes** nem a frase de contagem de `README.md` §11: elas são do
    `P-0743`.
- **Contingências:**
  1. Se `check-readme.ps1` sair diferente de `0` por item alheio a esta sprint → corrigir só o que
     a saída nomear e registrar na linha de retorno `contingência 1 acionada: <item>`.
  2. Se `docs/DOC_MAP.md` tiver frase que conta as entradas → atualizá-la no mesmo ato e registrar
     `contingência 2 acionada: frase de contagem do índice`.
- **Testes:** nenhum. O guarda executável é `check-readme.ps1`, e o veredito do dono é gate de
  fechamento, não critério desta entrega.
- **Verificação:**

  ```
  grep -c '^## docs/planner-spec.md' docs/DOC_MAP.md
  ```
  imprime `1` (hoje imprime `0`).

  ```
  grep -c 'Acesso:' docs/DOC_MAP.md
  ```
  imprime um número maior em uma unidade que o medido no despacho antes desta tarefa.

  ```
  pwsh -NoProfile -File .claude/checks/check-readme.ps1
  ```
  sai `0`.

  `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`.
- **Pronto quando:** `docs/DOC_MAP.md` tem a entrada de `docs/planner-spec.md` com o tamanho real,
  a lista de seções e a linha de acesso, e `check-readme.ps1` sai `0`.
- **Fora do escopo desta tarefa:** o veredito do dono sobre o README e sobre a especificação, que é
  gate de fechamento registrado pela orquestração (`GOVERNANCA.md` §4.5).

---

## 8. Ordem de execução

Fila única, sequencial.

```
PLS-T1 (agregado medido)
   └→ PLS-T2 (a especificação)
        └→ PLS-T3 (índice de documentos e revisão do README)
```

`PLS-T2` depende de `PLS-T1` porque não escreve nada que o agregado não sustente (`DPL-3`);
`PLS-T3` depende de `PLS-T2` porque a entrada do índice carrega o tamanho real do documento.

---

## 9. Fora de escopo (explícito)

| o que fica de fora | por quê | onde mora |
|---|---|---|
| Qualquer emenda a `.claude/agents/pantonic-planner.md` | a spec **descreve**; emendar o protocolo é outro ato, e o que a redação descobrir vira linha da seção 10 da spec | tíquete novo, a abrir a partir da seção 10 |
| A forma nova do modelo, o instrumento e o modelador | é o `P-0743` | `docs/plans/P-0743-modelo-de-dominio.md` |
| Especificação dos demais agentes do kit | o dono nomeou um caso, o do planejamento | — |
| A varredura de responsabilidade herdada nos demais artefatos do `P-0741` | está fechada como decisão no `P-0743` §3 e §11, não como investigação aberta | `docs/plans/P-0743-modelo-de-dominio.md` |

---

## 10. Riscos

| risco | resposta pré-decidida |
|---|---|
| O corpus medido não sustenta uma ou mais das dez dimensões | contingência 1 da `PLS-T1` e contingência 2 da `PLS-T2`: a dimensão existe com a frase de ausência e vira linha da seção 10. A spec fica honesta e incompleta, que é melhor que completa e inventada |
| O agregado estoura 120 linhas | contingência 3 da `PLS-T1`: corta pela cauda, preserva a ocorrência mais antiga e a mais recente |
| O `P-0743` não fecha e este plano fica parado | é o desenho: o `blocked` do cabeçalho é explícito e o gate é o `done` do `P-0743` no índice do diário |
| A fronteira com o consultor diverge do que o precedente declara | contingência 3 da `PLS-T2`: registra a divergência, não escolhe lado. Escolher lado é decisão de doutrina, e doutrina não se muda por redação |
| A revisão do README colide com o que o `P-0743` deixou | a `PLS-T3` roda depois do `P-0743` fechado e está proibida de tocar a §11, que é daquele plano |

---

## Achados da execução

_(vazio; apensado por quem executa ou orquestra)_
