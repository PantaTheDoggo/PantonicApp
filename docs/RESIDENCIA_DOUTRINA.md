# Residência da doutrina — o que desce do `~/.claude/CLAUDE.md` para o kit

**Tarefa:** `V2K-T16` (`P-0729-v2-melhoria-candidatos`, candidato `C-12`a) · **Data:** 2026-08-03 ·
**Régua:** `GOVERNANCA.md` §3.1 (escrita pela `V2K-T4`) · **Execução do texto:** `V2K-T17` — **nenhum
texto é movido por este documento**.

Este arquivo classifica **item a item** o conteúdo do `~/.claude/CLAUDE.md` (8 Regras, 169 linhas medidas em 2026-08-03)
e decide onde cada item deve morar — **36 itens**, nenhum sem classificação. A decisão do dono está registrada em §6 e é o insumo único da
`V2K-T17`: a `T17` executa esta tabela, sem acrescentar nem omitir item.

> **A régua mudou em 2026-08-15.** A classificação item a item das §§1-6 foi produzida sob a régua
> de quatro perguntas e permanece como registro do que foi decidido à época. O que a régua nova
> reclassifica está na **§8**, e é ela que vale para leitura de hoje.

## 1. Régua aplicada (resumo operacional)

Teste de residência de `GOVERNANCA.md` §3.1 — quatro perguntas na ordem, a primeira que der "sim"
decide:

| Sigla usada na tabela | Critério |
|---|---|
| **P1** | Vale para um projeto **não-Pantonic** do dono? → `~/.claude/CLAUDE.md` global |
| **P2** | É regra sempre-ativa **do framework**, que vale sem ninguém invocar nada? → `GOVERNANCA.md` |
| **P3** | É procedimento reexecutável com gatilho? → skill |
| **P4** | É papel + fatos estáveis de quem executa? → agente |
| **Prec-1** | Específico vence geral (dentro de projeto Pantonic, `GOVERNANCA.md` vence o global) |
| **Prec-2** | Empate → versionado vence não-versionado (o que está fora do repo não chega a consumidor — `BM-00§D15`) |
| **Dup** | "Colisão não se resolve com as duas cópias vivas" (§3.1, linha 134) |

Classificações possíveis: **`global`** (fica onde está), **`Pantonic`** (desce inteiro para o kit,
sai do global), **`dividir`** (parte fica, parte desce — sempre com a fronteira declarada).

## 2. Checagem de cruzamento com a `V2M-T3` (obrigatória)

A `V2M-T3` (2026-07-30) fez o movimento **inverso**: **subiu** G-PLANFIDELITY e G-EXECREADY do
`GOVERNANCA.md` §7 (itens 10 e 13) para o global (Regra 8), classificando-os como *"conduta
universal de executor, não doutrina específica de Pantonic"* — isto é, **P1 = sim**.

Subida e descida usam a mesma régua e **não se cruzam** desde que nada com P1 = sim desça. A tabela
de §4 respeita isso: nenhum item classificado `Pantonic` responde "sim" à P1.

A `V2M-T3` também fixou o **padrão de resolução de colisão** que este documento reusa espelhado:
a superfície que **perde** o texto normativo mantém *nome do item + uma frase de essência +
`Enforcement`*, e aponta para a que **ganha** — nunca vira ponteiro nu (`GOVERNANCA.md:311-315` e
`349-355`). Motivo: ponteiro nu quebra para quem não tem o arquivo do outro lado.

**Assimetria que a régua não resolve sozinha** (decisão `DR-A`, §5): há itens que são **universais**
(P1 = sim) **e** carga do framework (o agente do consumidor precisa deles sem ter o `~/.claude` do
dono). Para esses, P1 e Prec-2 apontam para lados opostos. O padrão da `V2M-T3` resolve: **texto
completo de um lado, condensado autossuficiente do outro** — nunca duas cópias plenas, nunca
ponteiro nu.

## 3. Achado que motiva a descida (`BM-00`)

O auto-retrato `BM-00` marcou dois blocos do CLAUDE.md global como **diferenciais do framework que
não viajam no kit**: o **orçamento/economia de contexto** (hoje Regra 3) e a **telemetria de
consumo** (hoje o bullet `Consumo:` da Regra 7). As citações originais do plano
(`~/.claude/CLAUDE.md:30,107`) são de 2026-07-29 e **envelheceram** — a `V2M-T3` inseriu a Regra 8
(150 → 165 linhas) e o arquivo está hoje em 169. Mapeamento atual verificado: linha 30 = heading da Regra 3;
o bloco de telemetria está hoje no fim da Regra 7 (linhas ~148-155).

## 4. Tabela item a item

Linhas referem-se ao `~/.claude/CLAUDE.md` no estado de 2026-08-03 (169 linhas, 8 Regras, 28
bullets — todos cobertos abaixo).

### Regra 1 — Nunca iniciar execução após aprovação de plano (3-16)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 1.1 | Regra inteira (parar após aprovação do plano; economia Opus→Sonnet) | `global` | **P1** — Plan Mode é recurso do harness, vale em qualquer projeto do dono | nenhuma |

*Nota:* `GOVERNANCA.md` §3 ("o agente de planejamento nunca executa") é regra de **papel de agente**,
não do gatilho de aprovação — não é a mesma proposição, não há colisão.

### Regra 2 — Integridade do contexto (17-49)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 2.1 | Integridade do contexto: coesão (poluição = parada fatal e imediata) e capacidade (dimensionamento pela operação do modelo, sem percentual — `P-0745` `DPN-3`) | `global` | **P1** — degradação de contexto é fato do harness, não do framework | nenhuma |

*Colisão já resolvida:* `GOVERNANCA.md` §7 item 7 e §4.3 já carregam a versão **do framework**
(handover, diário, contexto limpo) em forma condensada — é o padrão `DR-A`, sem duas cópias plenas.

### Regra 3 — Economia de contexto (30-50)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 3.1 | Motivo ("filtre na origem, não depois") | `dividir` | **P1** para o princípio; **Prec-2** para a carga do framework | frase-princípio desce condensada para `GOVERNANCA.md` §3 |
| 3.2 | Hook de filtro do `pytest`, log em `%TEMP%`, bypass `#nofilter` | `global` | **P1** — mecanismo do harness/máquina do dono; não viaja e não deve | nenhuma |
| 3.3 | `git status --short` / `git log --oneline`, nunca completos | `Pantonic` (cópia condensada) | **Prec-2** — agente de consumidor precisa disso sem o `~/.claude` | desce para `GOVERNANCA.md` §3, na lista de disciplina de coleta |
| 3.4 | Listagens: nunca recursivo sem excluir `build/`, `.venv/`, `node_modules/`… | `Pantonic` (cópia condensada) | **Prec-2** | idem 3.3 |
| 3.5 | Arquivos > 500 linhas: Grep + Read com `offset`/`limit` | `Pantonic` (cópia condensada) | **Prec-2**; reforça §7 item 8 ("docs grandes via índice") | idem 3.3 |
| 3.6 | Comandos verbosos não-teste → redirecionar para arquivo e ler só o fim | `Pantonic` (cópia condensada) | **Prec-2** | idem 3.3 |
| 3.7 | Varreduras amplas → subagente de coleta | `global` **e** já no kit | **Dup** — `GOVERNANCA.md` §3 já normatiza ("o agente de coleta existe para proteger o contexto dos agentes caros") | remover a duplicata do global; o kit já tem o texto |

**Fronteira declarada da Regra 3:** fica no global o que depende do harness/máquina do dono (3.2);
desce a disciplina de coleta que qualquer agente Pantonic precisa (3.3-3.6), como bullets compactos.
O global mantém a Regra 3 com o motivo e o hook, apontando para o kit no detalhe.

### Regra 4 — Onboarding econômico e bootstrap (51-68)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 4.1 | Usar a skill `onboard`; `DOC_MAP.md` como porta de entrada obrigatória | `global` | **P3** + **P1** — procedimento com gatilho, e as skills `onboard`/`doc-map` **não estão no kit** (são globais) | nenhuma; ver `DR-B` (§5) |
| 4.2 | CLAUDE.md de projeto ≤ 200 linhas, só regras que mudam comportamento | `Pantonic` | **Dup** — já está em `GOVERNANCA.md` §8 (linha 443), palavra por palavra | remover do global (kit já tem) |
| 4.3 | Docs separados ATIVO × HISTÓRICO desde o primeiro dia | `Pantonic` | **Dup** — `GOVERNANCA.md` §8 linha 442 | remover do global |
| 4.4 | `docs/DOC_MAP.md` obrigatório quando doc passar de 500 linhas | `Pantonic` | **Dup** — `GOVERNANCA.md` §8, tabela | remover do global (a menção à skill `doc-map` fica em 4.1) |
| 4.5 | `.claude/agents/*.md` nascem com bloco de "fatos estáveis" | `Pantonic` | **Dup** — `GOVERNANCA.md` §3.1, linha do agente na tabela ("papel + fatos estáveis que ele precisa saber a frio") | remover do global |
| 4.6 | `MEMORY.md`: hooks ≤ 120 chars, nunca conteúdo; `memory-diet` acima de ~40 linhas | `global` | **P1** + §3.1 "Ponteiro, não cópia" — governança de memória mora fora do kit por decisão explícita | nenhuma |

### Regra 5 — Destacar troca de modelo (69-83)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 5.1 | Banner `🟡 Troca de modelo` na primeira resposta após `/model` | `global` | **P1** — convenção de saída do dono, independe de framework | nenhuma |

### Regra 6 — Governança de memórias e artefatos `.claude` (84-110)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 6.1 | Motivo + ponteiro para `~/.claude/docs/GOVERNANCA_MEMORIAS.md` | `global` | **P1** — a régua já a resolve nominalmente: §3.1 "Ponteiro, não cópia" diz que a governança das memórias *"passa na pergunta 1"* e mora fora do kit | nenhuma |
| 6.2 | Lar canônico: derivável → não gravar; estado de trabalho → tracker; regra → CLAUDE.md; procedimento → skill; papel → agente; fato durável → memória | `dividir` | **Dup** parcial — os quatro ramos não-memória **são** o teste de residência §3.1 | global mantém só o ramo de memória (o que **não** vira memória) e cita a régua do kit em uma linha; ramos duplicados saem |
| 6.3 | Descobrir ≠ aprovar: agente enfileira em `_INBOX.md`, só o dono promove | `global` | **P1** + §3.1 "Ponteiro, não cópia" (cita explicitamente a fila) | nenhuma |
| 6.4 | Memória: 1 fato/arquivo, ≤ 30 linhas, `description` ≤ 120 chars, indexada | `global` | **P1** | nenhuma |
| 6.5 | Promover feedback a regra ⇒ apagar a memória de origem | `global` | **P1** | nenhuma |
| 6.6 | Fato de escopo global sobe do projeto para o CLAUDE.md global | `global` | **P1** | nenhuma |
| 6.7 | Listas voláteis têm uma única memória dona | `global` | **P1** | nenhuma |
| 6.8 | Agentes/skills não carregam estado volátil; agente = papel + fatos estáveis; skill = procedimento com gatilho | `Pantonic` | **Dup** — é a tabela de §3.1 (colunas "Não mora aqui" de skill e agente) | remover do global; kit já tem o texto |
| 6.9 | Raiz de sessão canônica = raiz do repo; `.claude` em subpasta é defeito | `global` | **P1** — higiene de sessão do harness, vale em qualquer repo | nenhuma |

### Regra 7 — Economia de turnos (111-155)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 7.1 | Motivo (custo ≈ Σ contexto × peso do modelo; caso medido 71 turnos/189k) | `dividir` | **Prec-1** — o caso medido já está em `GOVERNANCA.md` §3 (linhas 60-62) | global mantém 1 frase de motivo; o caso medido fica só no kit |
| 7.2 | Modelo por fase vale para o `model:` de subagente; Fable nunca automático | `Pantonic` | **Dup** — `GOVERNANCA.md` §3 (tabela + "modelo por fase é vinculante, não preferência" + Fable) | remover do global; kit tem o texto completo e a skill `modelo-por-fase` é o gatilho |
| 7.3 | Delegar é higiene de contexto, não economia de tokens (< ~15 turnos ⇒ inline) | `Pantonic` | **Dup** — `GOVERNANCA.md` §3, linhas 70-73, quase palavra por palavra | remover do global |
| 7.4 | Batching de chamadas independentes numa mensagem | `dividir` | **P1** para o princípio; **Prec-2** para o consumidor | fica no global; **desce cópia condensada** para §3 (hoje o kit não tem) |
| 7.5 | Cadência de testes: Tier 1 no máx. 2× por tarefa; tier superior só no fechamento | `dividir` | **P1** (skill `test-tiers` é global); **P2** para o framework (§4.4 TDD) | fica no global; desce 1 linha para `GOVERNANCA.md` §4.4 amarrando cadência ao TDD |
| 7.6 | Sem re-leitura de verificação após Edit/Write | `global` | **P1** — fato do harness (Edit/Write falham ruidosamente) | nenhuma |
| 7.7 | **Orçamento por tarefa atômica: "~≤40 tool uses esperado"** | `Pantonic` — **aposentado** | **Prec-1 + Prec-2** — o teto único e a tabela de tetos por classe que o substituiu foram aposentados em 2026-09-21 (`GOVERNANCA.md` §3, *Classe do card — natureza, não teto*; `P-0745` `DPN-3`): a unidade de trabalho é a operação do modelo e nenhum número dimensiona tarefa | global e kit dizem o mesmo: classe é natureza, não teto; o número histórico fica só em `RECOMENDACOES_CONSUMO_GLOBAL.md` como medida de 2026-07 |
| 7.8 | Plano interno antes da primeira edição | `global` | **P1** | nenhuma |
| 7.9 | Fechamento enxuto: um único registro canônico; relatório = ponteiro + deltas | `dividir` | **P1** para o princípio; **P2** para "o registro canônico é o diário" | fica no global sem citar diário; desce 1 linha para §4.2 |
| 7.10 | **Telemetria pela notificação, não pelo auto-relato** (linha `Consumo:`; orquestrador lê o `<usage>`; subestimativa medida ~35%) | `Pantonic` | **P2** — a linha `Consumo:` é escrita **no diário de obras**, artefato do framework; `BM-00` marcou como diferencial que não viaja | desce inteiro para `GOVERNANCA.md` §4.2 (ao lado do diário); global mantém 1 linha ("telemetria é medida, não auto-relatada") |

**Interação com `V2K-T18`/`T19`:** a `T18`/`T19` definem o **formato e o arquivo** da série
(`docs/telemetria.tsv`) e os pontos de escrita. O item 7.10 desce a **doutrina** (medir pela
notificação, nunca pelo auto-relato). A `T17` escreve a doutrina; a `T19` escreve o mecanismo — não
podem duplicar a mesma frase: se a `T17` rodar antes, a `T19` referencia o parágrafo já existente.

### Regra 8 — O executor não decide, não pergunta, não muda a rota (156-170)

| # | Item | Classe | Régua | Ação na `T17` |
|---|---|---|---|---|
| 8.1 | Regra inteira (G-PLANFIDELITY + G-EXECREADY condensados) | `global` | **P1** — classificação da `V2M-T3`, 2026-07-30; reafirmada aqui | **nenhuma** — a `T17` não pode desfazer o que a `V2M-T3` subiu |

## 5. Decisões que a régua não resolve sozinha

- **`DR-A` — item universal E carga do framework.** P1 manda ficar global; Prec-2 manda estar no kit
  (o consumidor por subtree não recebe o `~/.claude`). Proposta: **texto normativo no kit,
  condensado autossuficiente no global** (espelho do padrão `V2M-T3`), com a fronteira declarada
  item a item na §4. Nunca duas cópias plenas — "duplicata é a próxima divergência" (§3.1:135).
- **`DR-B` — skills globais citadas pela doutrina.** `onboard`, `doc-map`, `memory-diet`,
  `context-prep`, `lean-test` e `test-tiers` moram em `~/.claude/skills/` e **não estão nas 9 skills
  do kit**. Qualquer texto que desça citando-as nasce com ponteiro quebrado no consumidor. Proposta:
  a descida **não cita skill global** — cita só a regra; a promoção dessas skills ao kit, se
  desejada, é iniciativa própria, fora da `T17`.
- **`DR-C` — divergência viva do orçamento de turnos** (item 7.7): hoje existem dois números
  incompatíveis para a mesma pergunta. Enquanto não for resolvido, um subagente que carrega o
  CLAUDE.md global lê ≤40 para tarefa de redação de doutrina cujo número de kit é ≤30. Nenhum dos
  dois governa fluxo — os dois são referência informativa de dimensionamento (`GOVERNANCA.md` §3),
  e cruzá-los é alarme, nunca bloqueio —, de modo que a divergência degrada o dimensionamento antes
  de delegar, não a aceitação da entrega; resolvê-la é alinhar o global ao kit.

## 6. Ratificação do dono

**Status:** ratificada em 2026-08-03 (`AskUserQuestion`, 1 round-trip, 4 blocos).

| Bloco | Pergunta | Decisão do dono |
|---|---|---|
| `DR-A` | Onde fica o texto normativo de item universal + carga do framework | **Texto no kit + condensado no global** (recomendação acatada) |
| `DR-C` (7.7) | Teto de turnos no CLAUDE.md global | **Remover o número, manter o princípio**; o kit é a autoridade |
| `BM-00` (3.1-3.6, 7.10) | Diferenciais que não viajam | **Descem os dois** — disciplina de coleta e telemetria |
| `DR-B` (4.1) | Skills globais citadas pela doutrina | **Não citar skill global na descida**; promoção ao kit fica fora da `T17` |

Com estas quatro respostas, a tabela da §4 está 100% classificada e é o insumo fechado da
`V2K-T17`. Nenhum item ficou sem classificação; toda linha cita a regra da régua que a produziu.

## 7. Achado fora do escopo (não tratado aqui)

`GOVERNANCA.md` §4.2 (linha 183) ainda descreve o nome de plano como `docs/plans/P-<MMDD>-<slug>.md`,
padrão que o **G-PLANREADY item 1** (§7, linha 325) substituiu por `P-NNNN` com contador global
monotônico — justamente porque `P-<MMDD>` colidiu (dois `P-0722` no mesmo dia). Correção de 1 linha,
sem relação com residência; sugerido como tíquete avulso `TK-03`.

## 8. Nota de conciliação — 2026-08-15 (régua nova)

**Nada acima é reescrito.** As §§1-6 registram uma classificação feita sob a régua vigente em
2026-08-03; esta seção declara o que a régua de 2026-08-15 (`GOVERNANCA.md` §3.1) reclassifica, e é
a leitura válida de hoje. Execução: `P-0735`.

**O que mudou na régua.** Ela deixa de responder *onde mora* com uma resposta só e passa a separar
dois eixos que antes coincidiam: **autoridade** (de quem é o conteúdo) e **ponto de carga** (de onde
o harness lê). Três classes — canônico, ponto de carga, local de máquina —, uma **pergunta zero**
antes das quatro (*conteúdo ou ponto de carga?*) e o `Prec-2` promovido de critério de desempate a
**invariante**: nada canônico mora só num ponto de carga.

**Reclassificação, item a item do que esta tabela afirma:**

| O que a §4 afirma | O que a régua nova reclassifica |
|---|---|
| A classe **`global`** significa "fica onde está, fora do pacote" | A classe `global` continua significando **doutrina global** — o alcance não muda. O que muda é a residência: o canônico passa a ser versionado no kit (`.claude/global/CLAUDE.md`) e `~/.claude/CLAUDE.md` vira **projeção**. Nenhuma linha da tabela troca de classe |
| **`Prec-2`** desempata "versionado vence não-versionado" quando duas superfícies empatam (itens 3.3-3.6, 7.4, 7.7) | O empate que o `Prec-2` resolvia deixa de poder existir: com o canônico sempre versionado, a precedência 2 passa a ser **canônico vence projeção**. As conclusões dos itens permanecem — mudou o caminho que as produz |
| **`DR-A`** — item universal **e** carga do framework resolve-se com texto normativo no kit e condensado autossuficiente no global | Permanece, com o motivo trocado: a razão do condensado deixa de ser "o consumidor não recebe o `~/.claude`" e passa a ser **alcance de ponto de carga** — a doutrina global é o que está ativo num projeto fora da família |
| **`DR-B`** — as 6 skills globais (`onboard`, `doc-map`, `memory-diet`, `context-prep`, `lean-test`, `test-tiers`) não estão no kit, e a promoção fica como "iniciativa própria" fora da `T17` | **Destravado.** A promoção acontece: as seis skills e o agente `context-scout` passam a ser canônicos no kit e projetados no ponto de carga do usuário. A restrição derivada ("a descida não cita skill global, porque nasceria com ponteiro quebrado no consumidor") **cai** — o ponteiro passa a ter destino |
| Item **3.2** — o hook de filtro do `pytest` "é mecanismo do harness/máquina do dono; não viaja e não deve" | Reclassificado. O **script** do hook e a **declaração** que o registra são canônicos e viajam; continuam locais de máquina apenas o caminho de log em `%TEMP%` e o bypass, que são propriedade da máquina que executa |
| **`DR-C`** — divergência do orçamento de turnos | Sem efeito da régua nova; o item já se resolveu pelo alinhamento do global ao kit |

**O que esta nota não faz.** Não reabre nenhuma decisão da §6, não revisa o **conteúdo** do
`~/.claude/CLAUDE.md` item a item e não muda a fronteira declarada de nenhuma Regra. A mudança de
residência preserva o texto: o canônico nasce byte a byte igual ao que hoje está no ponto de carga.
