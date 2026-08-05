# P-0729 — V2 / Estágio 4: README espelho e fechamento da versão 2.0.0

**Iniciativa:** `PANTONIC-V2` — Estágio 4 de 4 (fechamento).
**Origem:** pedido do dono (2026-07-29): *"É necessário um README que seja um espelho dos documentos
atuais, de modo que um humano consiga ler um único arquivo, entender as premissas, filosofias e
escolhas do PantonicApp, e, principalmente, conseguir decidir sobre esse framework sem precisar ler
os demais artefatos."*

**Correção de premissa do dono (2026-08-05), vinculante — ver `## Revisão de rota`:** o verbo
"decidir" do pedido original foi lido no planejamento como *decidir se adota*, e o plano produziu um
documento de adoção. Não é isso. **Convencer nunca será preocupação deste projeto — assume-se que
quem lê já usa o framework.** O README é um **proxy das implementações** para o dono/gerente:
entender premissas, conceitos e procedimentos a ponto de **argumentar sobre as práticas** sem ler
skill, agente e hook um a um; e, nesta versão, enxergar **o que a V2 mudou** — o que fica, o que sai
e o que se modifica — para concluir a iniciativa com visibilidade.

**Planejador:** Opus (2026-07-29; revisão de rota em 2026-08-05). **Executor por tarefa:** T2
(redação do README) em **Opus** — é síntese de doutrina, a fase mais intelectual da iniciativa; as
demais em Sonnet; T5 com o dono.

**Estado:** `in progress` — 3/6 (`T1`, `T3` e `T4` fechadas em 2026-08-05; `T2` **reaberta** pela
revisão de rota; `T5` substituída; `T6` nova). Desbloqueado em 2026-08-05: a razão
registrada (*depende do Estágio 3 inteiro `done`* — `P-0729-v2-melhoria` = parte A, doutrina
herdada; `P-0729-v2-melhoria-candidatos` = parte B, autorada pelo Estágio 2 T6) deixou de valer com
3A 5/5 e 3B 20/20. O motivo do bloqueio continua válido como princípio: espelhar um framework que
ainda está mudando produz um espelho que nasce errado.

**Este plano também fecha a iniciativa:** T4 acumula a **distribuição aos consumidores** — a Fase 4
do `P-0722`, mapeada para cá em `P-0729-v2-melhoria` §1. A propagação acontece **uma vez**, no
fechamento, e não a cada estágio (DM-6).

**Idioma:** **PT-BR** (decisão do dono, 2026-07-29). Todo o corpus — doutrina, planos, skills,
agentes — é PT-BR; um README em inglês seria o único artefato traduzido e um canal permanente de
drift.

---

## 0. O problema real deste estágio

Um README "espelho" tem um modo de falha conhecido: nasce fiel e envelhece mentindo. E ele mente
com autoridade, porque é o **único** arquivo que o leitor vai ler — é essa a exigência do dono. Este
plano trata o espelho como um artefato com **fonte da verdade declarada por seção** e um **guarda
executável de drift**, não como um documento de boa vontade. Sem o guarda, o README é o pior
artefato do repositório em vez do melhor.

Segunda exigência, corrigida pelo dono em 2026-08-05: o leitor **já usa** o framework. O que ele não
tem é **memória da forma que cada acordo tomou**. Ele lembra do conceito ("próxima tarefa é uma fila")
e não da implementação (diretiva de priorização persistida + heurística de 4 níveis onde FIFO é o
**último** desempate) — e é sobre a implementação que ele precisa argumentar. O modo de falha
correspondente não é "README que só descreve virtudes"; é **README que descreve o conceito e não o
procedimento**, deixando o gerente discutir uma prática que o repositório não executa.

Terceira exigência, da mesma correção: a iniciativa V2 absorveu 14 candidatos ratificados vindos do
benchmarking de 21 frameworks públicos, e o dono **não tem visibilidade do resultado**. Concluir a
iniciativa exige ler, num só lugar, o que fica, o que sai e o que se modifica.

## 1. Esqueleto obrigatório do README (15 seções)

Ordem e conteúdo fixados aqui para que o T2 execute redação, não arquitetura. Meta de tamanho:
**750-900 linhas**. O teto antigo (400-550) servia ao documento de adoção; um espelho de procedimento
precisa de profundidade suficiente para o gerente **intervir**, não só reconhecer o nome do
procedimento. O risco que o teto antigo mitigava — "o leitor volta a precisar de um índice" — já tem
resposta melhor: o `docs/DOC_MAP.md` entregue pela `T1`.

| § | Seção | O que precisa responder | Fonte da verdade |
|---|---|---|---|
| 1 | **O que é e o que ele governa** | Framework de governança + arquitetura para aplicações desktop Python/PySide6 construídas por agentes de IA. O que ele governa (custo, rota, qualidade) e o que ele deixa de fora. 3 parágrafos, sem jargão interno | `GOVERNANCA.md` §1 |
| 2 | **As cinco premissas de arquitetura** | Desktop-first; Python+PySide6+MVVM; obsessão por clean architecture; core comum reusável; extensão só por plugin. Cada uma com a consequência prática que ela impõe ao código | `GOVERNANCA.md` §1 |
| 3 | **O modelo econômico** | Por que o framework existe: custo ≈ Σ (contexto reenviado × peso do modelo). Orçamento de turnos, batching, cadência de testes, e o fato contraintuitivo de que **delegar a subagente é higiene de contexto, não economia de tokens** | `GOVERNANCA.md` §3 |
| 4 | **Modelo por fase** | A tabela vinculante (intelectual→Opus, execução→Sonnet, varredura→Haiku), o gate que a cobra no início de cada tarefa, e **o que o gerente faz quando o gate dispara** | `GOVERNANCA.md` §3 |
| 5 | **O fluxo plano → execução** | O coração do framework: toda iniciativa é antecedida por um **checklist em formato consolidado**, decomposto em **tarefas atômicas** que permitem ao executor operar incrementalmente, com **contexto limpo** e sem conhecer o projeto inteiro. Planejador e executor são papéis distintos, em modelos distintos, e o executor **não decide, não pergunta e não muda a rota** | `GOVERNANCA.md` §4 |
| 6 | **O procedimento `próxima tarefa`** | Como o ponto atual do projeto é identificado em contexto novo. A sequência real: drenar inboxes → ler a **diretiva de priorização persistida** → heurística de 4 níveis (`blocked` destravável → `in progress` → bug avulso → **FIFO como último desempate**) → gate de delegação → handover. E **como o gerente reordena**: escrevendo a diretiva no diário, que tem precedência total sobre a heurística | `.claude/skills/proximo-passo/SKILL.md` |
| 7 | **O diário de obras** | O kanban central: índice, status por item, âncora para o plano, tíquetes avulsos, e a condensação para `DIARIO_HISTORICO.md` quando o diário ativo cresce. Onde o gerente lê o estado sem abrir plano nenhum | `.claude/skills/diario-de-obras/SKILL.md` |
| 8 | **Planos: o que é um plano fechado** | O gate de publicação (`G-PLANREADY`): plano com questão pendente, bloco a preencher ou ramo não resolvido **não é publicado**, porque o executor pararia e forçaria retrabalho. Inbox append-only de planos, numeração monotônica, decisões `DP`/`DD` fechadas no planejamento, e o que torna um plano `superseded` em vez de "continuado" | `GOVERNANCA.md` §7 |
| 9 | **Handover e uma tarefa por contexto** | Por que uma tarefa por janela de contexto, o que o handover registra, e por que "decisão pendente é o próximo passo" — com o escopo do que conta como decisão do dono (**arquitetura e requisitos**; evento intrínseco do plano o agente executa) | `.claude/skills/handover/SKILL.md` |
| 10 | **Os guardrails** | Tabela: regra → como é enforceada (**teste executável** \| **gate de review** \| **instrução de agente**). A coluna do meio é o ponto alto do framework e precisa ser honesta sobre o que ainda é só texto | `GOVERNANCA.md` §7 |
| 11 | **Anatomia do kit** | Tabela dos agentes e das skills, uma linha cada: nome, modelo, quando dispara. Mais os checks executáveis em `.claude/checks/` | `.claude/README.md` |
| 12 | **Memória e telemetria** | O que vira memória (fato durável não derivável) e o que **não** vira; a fila `_INBOX.md` de candidatos, que o agente enfileira e **só o dono promove**; e a série medida `docs/telemetria.tsv` — consumo é **medido**, nunca auto-relatado pelo executor | `GOVERNANCA.md` §4 |
| 13 | **Distribuição e versão** | Hub único, `git subtree`, `sync-kit.ps1`, `kit-exclude.txt` (override de arquivo inteiro, sem merge parcial), semver do kit (MAJOR exige ação do consumidor) e o limite `§10a`: divergência é **reportada**, nunca aplicada por agente | `GOVERNANCA.md` §9 |
| 14 | **Decisões e a evidência medida que as motivou** | ADR compacto — cada decisão com o número que a produziu (o executor em Opus com 71 turnos; as ~300 linhas de código morto testado; a série de estouros de teto que virou a regra de dividir antes de delegar; o symlink que exigia privilégio no Windows). É o que separa este framework de uma lista de boas intenções | `GOVERNANCA.md` §3 |
| 15 | **O que a V2 mudou** | **A seção que fecha a iniciativa.** Origem: benchmarking de 21 frameworks públicos → 14 candidatos ratificados (12 `adotar`, 2 `adaptar`, 1 `adiar`). Três listas explícitas — **o que fica** (procedimento que já existia e foi confirmado), **o que sai** (procedimento abandonado e por quê), **o que se modifica** (procedimento que existia e mudou de forma, com o antes → depois). Autossuficiente: o dono conclui a iniciativa sem abrir `CANDIDATOS.md` nem o `CHANGELOG` | `CHANGELOG.md` §2.0.0 |

**Regras de redação:**

- Cada seção abre com a linha `> Fonte da verdade: <arquivo> §<seção>`, e o arquivo citado **existe
  no repositório** — o guarda da `T3` resolve o caminho a partir da raiz e falha em caminho externo
  (`~/.claude/...`). Doutrina que nasceu global já foi repatriada para `GOVERNANCA.md` na `V2K-T17`;
  citar o espelho interno, não o global.
- Nada de "veja o documento X para entender" no corpo — é exatamente o que o dono pediu para
  eliminar.
- **Procedimento se descreve pela forma implementada, não pelo conceito.** Onde a implementação for
  mais rica que o nome (o caso medido: `próxima tarefa` não é uma fila FIFO simples), o README
  descreve a implementação; simplificar aqui produz um gerente que argumenta sobre uma prática que o
  repositório não executa.
- Cada procedimento responde três coisas na mesma seção: **o que é**, **por que foi adotado** (a
  evidência ou o episódio que o produziu) e **onde o gerente intervém**. Seção sem o terceiro item
  não serve ao objetivo do documento.
- Zero convencimento. Não há "por que adotar", "devo adotar", "para quem não é". Assume-se que quem
  lê já usa o framework.

## 2. Tarefas

### T1 — `docs/DOC_MAP.md` do hub [Sonnet] — **done (2026-08-05)**, ver `## Achados da execução`
- **Objetivo (premissa caída):** o hub tem quatro documentos acima de 500 linhas (`P-0721` 619,
  `P-0725-hub-unico` 834, e os planos desta iniciativa) e nunca teve DOC_MAP — a Regra 4 do
  CLAUDE.md global o exige, e o §12 do README vai apontar para ele. **O mapa já existia** desde a
  `V2K-T6` (2026-07-30), posterior à redação deste plano; a tarefa foi fechada por verificação de
  cobertura/âncoras + atualização do delta desatualizado.
- **Arquivos-alvo:** `docs/DOC_MAP.md` (novo), via skill `doc-map`.
- **Pronto quando:** todo documento > 500 linhas do hub tem entrada com âncoras de seção e padrão de
  Grep de acesso; o mapa cabe em uma tela.

### T2 — Redigir o README espelho [**Opus**] — **in review** *(2ª rodada fechada em 2026-08-05; ver `## Achados da execução` §`T2 — 2026-08-05 (2ª rodada)`)*
> A primeira rodada fechou em 2026-08-05 (528 linhas, 13 seções) sob a premissa errada — ver
> `## Achados da execução` §T2 e `## Revisão de rota`. O artefato entregue **não é descartado**: seis
> seções sobrevivem com retrabalho de moldura, três saem e sete nascem.

- **Objetivo:** o entregável central da iniciativa, agora com o objetivo corrigido — **proxy das
  implementações** para o gerente argumentar sobre as práticas.
- **Arquivos-alvo:** `README.md` (raiz — existe, 528 linhas, será reescrito);
  `.claude/checks/check-readme.ps1` (ajuste obrigatório, ver abaixo).
- **Ponto de partida — o que fazer com o README atual** (medido, não re-derivar):
  - **Aproveitar, remoldando:** §3 premissas → nova §2; §4 filosofia → dissolvida nas seções de
    procedimento (cada escolha vira o "por que foi adotado" da seção correspondente); §5 modelo
    econômico → nova §3; §7 anatomia → nova §11; §8 guardrails → nova §10; §11 decisões → nova §14.
  - **Descartar:** §2 "Para quem é / para quem não é", §10 "O que este framework não resolve",
    §13 "Devo adotar? (FAQ de decisão)" — os três são argumentação de adoção.
  - **Escrever do zero:** novas §1, §4, §5, §6, §7, §8, §9, §12, §15.
- **Ajuste obrigatório no guarda da `T3`** (senão a `T2` sai com o guarda vermelho): o
  `check-readme.ps1` localiza duas seções por **número hardcoded** — `'## 7. '` (Anatomia do kit) e
  `'## 8. '` (Os guardrails). No esqueleto novo elas são **§11** e **§10**. Trocar a busca por
  **título** em vez de número, nas duas checagens, e corrigir a linha 6 do bloco de ajuda, que ainda
  descreve "espelho de 13 seções escrito para que um humano decida sobre o framework".
- **Dois formatos que o guarda parseia e que a reescrita não pode quebrar** (medidos na `T3`, ver
  `## Achados da execução` §T3): (a) a linha de fonte usa **um** arquivo por seção, sempre entre
  crases — o guarda parseia por crase; (b) a tabela da seção **Os guardrails** conta linhas numeradas
  `| N |` e o guarda recorta a seção antes de contar, porque o sumário do topo usa a mesma forma —
  manter a tabela de guardrails numerada e dentro da própria seção.
- **Método:** seguir §1 seção a seção. Fontes lidas por Grep/âncora, não integralmente (o próprio
  framework proíbe leitura integral de doc grande). Onde a doutrina for ambígua ou tiver envelhecido,
  **não inventar consenso**: registrar como achado da execução no fim deste plano e escrever o que é
  verdade hoje. Para a §15, a fonte primária é `docs/benchmark/CANDIDATOS.md` (os 14 candidatos
  ratificados, com o veredito de cada um) cruzada com o `CHANGELOG.md` §2.0.0 — a seção precisa ficar
  **autossuficiente**, porque o dono não vai abrir nenhum dos dois.
- **Pronto quando:** as 15 seções existem na ordem de §1, cada uma com a linha de fonte da verdade
  apontando arquivo que existe no repositório; 750-900 linhas; toda seção de procedimento (§4 a §9,
  §12, §13) responde **o que é / por que foi adotado / onde o gerente intervém**; a §15 traz as três
  listas (fica / sai / modifica) com o antes → depois de cada item modificado; nenhuma remissão do
  tipo "leia o documento X para entender"; nenhuma seção de convencimento; e
  `pwsh -File .claude/checks/check-readme.ps1` sai **exit 0**.

### T3 — Guarda de drift do espelho [Sonnet]
- **Objetivo:** impedir que o README envelheça mentindo — o risco declarado em §0.
- **Arquivos-alvo:** `.claude/checks/check-readme.ps1` (novo); integração como modo do
  `.claude/sync-kit.ps1 -Check` ou entrada na skill `guardrails-check` (o que for menos intrusivo,
  decidido na execução com uma sonda de 1 comando); `VERSION`/`KIT_VERSION`/`CHANGELOG.md`.
- **O que o guarda verifica** (tudo mecânico, zero julgamento):
  1. Todo agente em `.claude/agents/*.md` aparece na tabela do §7; todo item da tabela existe.
  2. Toda skill em `.claude/skills/*/SKILL.md` aparece no §7; e vice-versa.
  3. A versão citada no §12 é igual a `VERSION` e a `.claude/KIT_VERSION`, e os dois coincidem.
  4. O número de guardrails do §8 é igual ao de `GOVERNANCA.md` §7.
  5. Toda seção do README tem a linha `> Fonte da verdade:` e o arquivo citado existe.
- **Verificação:** o guarda falha ao se adicionar um agente sem atualizar o README, e passa no
  estado corrente.
- **Pronto quando:** as duas verificações acima passam; sai `exit 1` em divergência e `0` limpo.

### T4 — Fechar a versão 2.0.0 e distribuir [Sonnet] — *acumula `P-0722` Fase 4*
- **Objetivo:** entregar o V2 que o dono pediu, com o significado correto de MAJOR, e **avisar o
  consumidor** — a distribuição da iniciativa inteira acontece aqui, uma vez só.
- **Arquivos-alvo:** `VERSION` e `.claude/KIT_VERSION` → `2.0.0`; `CHANGELOG.md` (seção `2.0.0`
  consolidando toda a iniciativa: benchmarking, guardrails novos, mudanças adotadas, README);
  `GOVERNANCA.md` §9 (uma linha apontando o README como porta de entrada humana do framework);
  `git tag kit-v2.0.0`.
- **Justificativa do MAJOR a registrar no CHANGELOG:** a superfície que o consumidor consome mudou
  (guardrails novos vinculantes + artefatos novos no kit + README canônico). Se ao chegar aqui
  **nenhuma** mudança exigir ação do consumidor, registrar isso e sair em `1.x` — semver que mente
  sobre compatibilidade custa mais do que a satisfação de escrever "2.0.0".
- **Nota de migração (para o `PantonicVideo`, único consumidor real hoje):** o que muda ao rodar
  `sync-kit.ps1`, em especial se algum override declarado em `kit-exclude.txt` colidir com artefato
  novo do kit, e quais guardrails novas passam a valer para os agentes daquele projeto.
- **Limite inviolável (`GOVERNANCA.md` §10a):** a divergência de versão do consumidor é
  **reportada**, nunca aplicada por agente. Detectar e agir são atos distintos; não existe threshold
  de severidade que justifique pular a separação. Esta tarefa não toca o repositório do consumidor.
- **Pronto quando:** os dois arquivos em `2.0.0` (ou a justificativa contrária escrita); CHANGELOG
  consolidado com a nota de migração; tag criada; o guarda do T3 passa; a divergência de versão do
  `PantonicVideo` está reportada ao dono, com nenhuma alteração feita naquele repositório.

### T5 — Teste de aceitação do espelho [dono] — **reprovada em 2026-08-05**
- **Objetivo:** verificar as duas exigências corrigidas — o README **serve** ao gerente e é
  **verdadeiro**. São testes distintos e ambos são necessários: um espelho fiel e inútil reprova
  tanto quanto um espelho útil e falso.
- **Método, parte A — utilidade (o dono lê só o `README.md`):** para **cada** procedimento descrito
  (§4 a §9, §12, §13), o dono consegue dizer, sem abrir outro arquivo: (1) **o que é**, (2) **por que
  foi adotado**, (3) **onde ele intervém como gerente**. E, ao fim da §15, consegue afirmar o que
  fica, o que sai e o que se modifica na V2 — o critério de conclusão da iniciativa.
- **Método, parte B — fidelidade (amostragem):** sorteiam-se **3** procedimentos descritos no README
  e confere-se a descrição contra o artefato real (a skill, o agente ou o hook correspondente).
  Divergência entre o que o README diz e o que o artefato faz é reprovação — é exatamente o modo de
  falha do §0.
- **Pronto quando:** parte A sem lacuna e parte B com 3/3 fiéis. Qualquer item faltante em A, ou
  qualquer divergência em B, **reabre a `T2`** com a lacuna nomeada — a reabertura é resultado
  esperado, não fracasso.

### T6 — Fechar a `2.0.1` do espelho [Sonnet] — **cancelada por absorção (DR-6)**
- **Objetivo:** manter tag e conteúdo coerentes depois da reescrita. A `kit-v2.0.0` foi criada em
  2026-08-05 sobre o README da premissa antiga; a `T2` o reescreve por inteiro.
- **Por que PATCH e não MINOR/MAJOR** (decisão `DD-7`, fechada): a reescrita não adiciona artefato
  nem guardrail ao kit e não exige nenhuma ação do consumidor — é correção de redação do espelho, que
  é a definição de PATCH em `GOVERNANCA.md` §10.
- **Arquivos-alvo:** `VERSION` e `.claude/KIT_VERSION` → `2.0.1`; `CHANGELOG.md` (seção `2.0.1`
  registrando a correção de premissa e o que mudou no README); `README.md` §13 (referências de
  versão); `git tag kit-v2.0.1`.
- **Não fazer:** `git push`, reescrita de história, alteração ou remoção da tag `kit-v2.0.0` — ela
  registra um estado real do repositório e permanece.
- **Pronto quando:** os dois arquivos em `2.0.1`; `CHANGELOG` com a seção nova; `check-readme.ps1`
  exit 0; tag `kit-v2.0.1` criada; nada pushado.

## 3. Riscos

- **README bonito e falso** — o modo de falha central (§0). Mitigação: T3 (guarda mecânico) + T5
  parte B (amostragem de fidelidade contra o artefato real).
- **README fiel e inútil** — risco novo, introduzido pela revisão de rota: descrever o procedimento
  com precisão e não dizer onde o gerente intervém. Mitigação: a regra "o que é / por que / onde
  intervenho" em §1 e a parte A do T5.
- **Espelho virar terceiro documento de doutrina**, divergindo de `GOVERNANCA.md` a cada edição.
  Mitigação: linha `> Fonte da verdade:` por seção; edição de doutrina acontece na fonte e desce
  para o README, nunca o contrário — regra a escrever no próprio §13.
- **A §15 envelhecer viva** — ela descreve uma transição, não um estado; mantida viva, vira um
  segundo changelog. Mitigação (`DD-8`): depois que o dono ratificar o fecho da iniciativa na `T5`,
  a §15 é congelada como histórico, não atualizada a cada versão.
- **Tamanho:** 15 seções com profundidade de procedimento passam de 900 linhas. Mitigação: teto
  declarado em §1; o que não couber é sinal de que pertence ao documento-fonte, não ao espelho.
- **Publicidade:** o repositório é público (`github.com/PantaTheDoggo/PantonicApp`) e o README passa
  a ser sua fachada. Mitigação: §11 cita evidências medidas do próprio projeto — nenhuma delas
  contém segredo, mas o T2 confere isso explicitamente antes de fechar.

## 4. Decisões (fechadas no planejamento)

| id | Decisão | Valor | Motivo |
|---|---|---|---|
| **DD-1** | Idioma | PT-BR | Decisão do dono; todo o corpus é PT-BR e um único artefato traduzido é canal permanente de drift |
| **DD-2** | Um arquivo, não um site | `README.md` na raiz | A exigência é "um humano lê um único arquivo"; qualquer split reintroduz o problema que o README resolve |
| **DD-3** | Espelho com fonte declarada | `> Fonte da verdade:` por seção + guarda executável | Espelho sem guarda envelhece mentindo, e mente com autoridade por ser o único arquivo lido |
| ~~**DD-4**~~ | ~~Aceitação por leitura cega, 6 perguntas de decisão~~ | **REVOGADA em 2026-08-05** | As 6 perguntas testavam convencimento ("devo adotar?"), e convencer nunca foi preocupação do projeto. Substituída por `DD-6` |
| **DD-5** | MAJOR condicionado | `2.0.0` se houver mudança que exija ação do consumidor; caso contrário `1.x` com justificativa | Meta do dono é o V2, mas semver é contrato com o consumidor, não placar da iniciativa. **Resolvida na `T4`:** `2.0.0`, pelo contrato novo do piso de regressão |
| **DD-6** | Objetivo do README e seu teste | **Proxy das implementações** para o gerente argumentar sobre as práticas; aceito por utilidade (o que é / por que / onde intervenho, por procedimento) **e** por fidelidade (amostragem de 3 contra o artefato real) | Correção de premissa do dono, 2026-08-05: quem lê já usa o framework. O que falta a ele não é motivo para adotar — é a **forma que cada acordo tomou** |
| **DD-7** | Versão da reescrita | `2.0.1` (PATCH), tag `kit-v2.0.1`, preservando `kit-v2.0.0` | Reescrita de espelho não adiciona artefato nem guardrail e não exige ação do consumidor — é redação, a definição de PATCH em `GOVERNANCA.md` §10 |
| **DD-8** | Ciclo de vida da §15 | Congelada como histórico após a ratificação do dono na `T5`; não atualizada a cada versão | Ela descreve uma transição, não um estado; mantida viva, duplica o `CHANGELOG` e envelhece dentro do espelho |

## Revisão de rota — 2026-08-05 (decision record)

**Quem decidiu:** o dono, no handover da `T4`, ao ler as 6 perguntas da `T5` original.
**Aprovada:** 2026-08-05, na mesma conversa, com a recomendação aceita integralmente.

**O achado.** As 6 perguntas da `T5` — *"o que ele faz por mim que eu não teria de graça?"*, *"em que
tipo de projeto ele seria um erro?"*, *"devo adotar?"* — testavam **convencimento**. O dono:
*"Convencer nunca será uma preocupação do projeto. Assume-se que quem está lendo já está
utilizando."*

**A raiz.** Erro de leitura na fase de planejamento (2026-07-29), não da execução. O pedido original
dizia *"conseguir **decidir** sobre esse framework"*, e o planejamento leu "decidir **se adota**".
O §0 do plano registrou isso explicitamente — *"o leitor precisa decidir sobre o framework... saber
onde ele não serve, o que ele custa e o que ele deliberadamente recusa a fazer"* — e o esqueleto de
§1 derivou daí três seções de adoção (§2, §10, §13) e um teste de aceitação de adoção (`DD-4`).
A `T2` executou o esqueleto com fidelidade; o defeito é anterior a ela.

**O objetivo correto**, nas palavras do dono: *"um proxy das implementações nos artefatos, para o
dono/gerente do projeto conseguir entender as premissas, os conceitos e os procedimentos para que ele
tenha condição de argumentar sobre as práticas sem precisar ler todos os artefatos individualmente"*
— mais a visibilidade do resultado do benchmarking: *"o que fica, o que sai e o que modifica"*.

**A evidência que confirmou o diagnóstico.** Ao descrever de memória um procedimento maduro do
próprio projeto, o dono definiu `próxima tarefa` como *"uma pilha FIFO onde cada comando de próxima
tarefa vai coletar a primeira task e passar ao executor"*. A implementação é outra: **diretiva de
priorização persistida** na primeira linha do diário, com precedência total sobre uma heurística de
**4 níveis** (`blocked` destravável → `in progress` com WIP de 1 → bug avulso → FIFO). FIFO é o
**quarto** critério de desempate, não o mecanismo. Não é falha de memória do dono — é exatamente a
lacuna que o documento existe para cobrir, e a prova de que o espelho precisa descrever a
**implementação**, não o conceito.

**O que mudou neste plano:** §0 segundo parágrafo reescrito e terceiro acrescentado; §1 de 13 para 15
seções, com meta de tamanho de 400-550 → 750-900 linhas; `T2` **reaberta** com esqueleto novo e um
ajuste obrigatório no guarda da `T3` (que localiza `## 7. ` e `## 8. ` por número hardcoded — as duas
seções mudam de número); `T5` **substituída** (utilidade + fidelidade, no lugar das 6 perguntas);
`T6` **nova** (fecha a `2.0.1`); `DD-4` revogada; `DD-6`, `DD-7` e `DD-8` acrescentadas; risco novo
"README fiel e inútil" registrado em §3.

**O que NÃO mudou e não deve ser revisitado:** `DD-1` (PT-BR), `DD-2` (arquivo único), `DD-3`
(fonte da verdade por seção + guarda executável) e as tarefas `T1`, `T3`, `T4`, todas `done` e não
afetadas pela correção de premissa. A `2.0.0` e a tag `kit-v2.0.0` permanecem — registram um estado
real do repositório.

**Fora do escopo deste plano** (mesma decisão): o `git push` dos commits e das tags, e a migração do
`PantonicVideo` para o kit `2.0.0`.

## Achados da execução

### T5/T6 — 2026-08-05

**`V2D-T5` reprovada.** O teste de aceitação (utilidade + fidelidade, `DD-6`) cumpriu seu papel e
detectou desvio de identidade na **fonte da verdade** (`GOVERNANCA.md` §1), não no espelho: o
README está fiel ao que documenta, mas `GOVERNANCA.md` §1 declara o framework como "desktop, stack
fixo PySide6" quando o entendimento canônico é agnóstico a tecnologia/plataforma. Os 11 desvios
medidos estão em `docs/plans/P-0730-v2-identidade.md` §2.

**`V2D-T6` cancelada por absorção.** A correção de `2.0.1` (redação do espelho) é substituída pelo
escopo maior do Estágio 5, que fecha em `2.1.0` (`DR-6`, ver `docs/plans/P-0730-v2-identidade.md`).

### T4 — 2026-08-05

**Entregue:** `VERSION` e `.claude/KIT_VERSION` em `2.0.0`; `CHANGELOG.md` §2.0.0 consolidando os
quatro estágios (Estágio 1 benchmarking, Estágio 2 confronto, Estágio 3A doutrina herdada do
`P-0722`, Estágio 3B mudanças adotadas, Estágio 4 README/guarda), com a justificativa do MAJOR (o
piso de regressão muda de formato — contagem/percentual para lista versionada — e exige ação do
consumidor, além de guardrails vinculantes novas e artefatos novos do kit) e a nota de migração ao
`PantonicVideo`; `[Não lançado]` esvaziada (o único item, correção de escopo da `proximo-passo`
passo 5, absorvido em `2.0.0`); `GOVERNANCA.md` §9 com uma linha apontando `README.md` como porta
de entrada humana do framework.

**Ramo único (kit-exclude × artefato novo), resolvido — houve colisão:** a entrada
`skills/guardrails-check` do `kit-exclude.txt` do `PantonicVideo` (protege o perfil local daquele
projeto, `P-0721` Fase 1a) ocupa o mesmo caminho onde a `T3` deste estágio acabou de adicionar o
item 8 (guarda do espelho, linha `Espelho:` no veredito). Consequência registrada na nota de
migração do `CHANGELOG.md` §2.0.0: `sync-kit.ps1` vai respeitar o override e **não** propagar o
item 8 para aquele projeto. As outras duas entradas (`agents/pantonic-executor`,
`skills/integrar-poc`) não colidem com nenhum artefato novo da iniciativa.

**Divergência do consumidor, reportada ao dono (nenhuma ação aplicada, `GOVERNANCA.md` §10a):** o
`PantonicVideo` (`d:\workspaces\PantonicApp\..\PantonicVideo`) está em estado **pré-kit** — sem
`.claude/KIT_VERSION` (nem `.claude/kit/KIT_VERSION`), cópia manual de `.claude/`, não via
`git subtree`/`sync-kit.ps1`. A distância relevante para aquele projeto não é o incremento
`1.5.0` → `2.0.0`; é o kit inteiro publicado até `2.0.0` contra uma cópia manual desatualizada,
incluindo os 6 guardrails do Estágio 3A/3B e o contrato novo do piso de regressão
(`tests/piso_comportamental.txt`, ainda não criado lá). Repositório do consumidor **não tocado**
nesta tarefa — confirmado por `git -C d:/workspaces/PantonicVideo status --short` ao final, sem
nenhuma mudança atribuível a esta execução.

**Verificação (guardrails-check, itens tocados):** `check-readme.ps1` → `check-readme: OK - 9
agente(s), 9 skill(s), 14 guardrail(s), versão '2.0.0', 13 seção(ões) com Fonte da verdade válida`,
exit 0. `kit_check.ps1 -Mode validate` → `OK` (paridade `VERSION == KIT_VERSION`, `2.0.0`).
`kit_check.ps1 -Mode check-drift` → `OK`. `dead_code.py` → `OK - 0 achado(s)`. `ratchet_piso.py` →
`OK - nenhum piso declarado`.

**Sequência de commits e tag** (estado inicial já tinha os entregáveis T1-T3 pendentes de
commit): commit 1 = README/guarda/DOC_MAP/diário/telemetria (`V2D-T1..T3`); commit 2 = fechamento
`2.0.0` (`VERSION`, `KIT_VERSION`, `CHANGELOG`, `GOVERNANCA` §9, diário, este bloco); tag anotada
`kit-v2.0.0` sobre o commit 2, mesmo padrão de `kit-v1.5.0`. Nada pushado.

**Fora do escopo deste plano** (decisão do dono, 2026-08-05, no handover da `T4`): (a) o `git push`
dos commits `f1e4879`/`6e2154a` e da tag `kit-v2.0.0` — a publicação é ato do dono, em momento
próprio; (b) a migração do `PantonicVideo` para o kit `2.0.0`, incluindo a colisão medida em
`skills/guardrails-check`. A `T4` cumpriu o seu dever sobre (b) — **reportar** a divergência
(`GOVERNANCA.md` §10a) —, e a ação em si não pertence a este estágio. Nenhum dos dois bloqueia a
`T5` nem o fechamento do plano.

Consumo: ver `docs/telemetria.tsv` (teto de 35 estourado — 46 tool uses; ver §Riscos/handover).

### T3 — 2026-08-05

**Entregue:** `.claude/checks/check-readme.ps1` (novo), com `-Root` no mesmo desenho de
`-KitRoot` (`kit_check.ps1`) e `--root` (`dead_code.py`/`ratchet_piso.py`) — resolve a raiz a
partir do próprio caminho do script, parametrizável para provar contra fixture sintética sem
nunca escrever no repo real. As 5 checagens do §T3 implementadas literalmente: (1)/(2)
agentes/skills do README §7 batendo com `.claude/agents/`/`.claude/skills/` nos dois sentidos;
(3) versão do README (cabeçalho **e** §12 — os dois pontos, não só o §12) igual a `VERSION` e a
`.claude/KIT_VERSION`; (4) guardrails da tabela do README §8 (`| N |` recortado só na seção 8,
não a tabela-sumário do topo que também usa `| N |`) igual aos itens numerados de `GOVERNANCA.md`
§7; (5) toda seção `## ` com `> Fonte da verdade:` apontando para arquivo existente. Integração
decidida pelo orquestrador (não reaberta na execução): entrada condicional na skill
`guardrails-check` (item 8, mesmo molde do item 5) + linha `Espelho:` no template de Veredito —
`.claude/sync-kit.ps1 -Check` não tocado (concern diferente).

**Achado de implementação, resolvido inline (dentro do escopo da tarefa):** PowerShell rejeita
binding de um parâmetro `[string[]]` `Mandatory` quando o array contém um elemento `""` (linha em
branco do README) — mensagem "Cannot bind argument... because it is an empty string" mesmo com o
tipo sendo array, não escalar. `kit_check.ps1` já carregava a correção (`[AllowEmptyString()]` em
`Set-MarkedRegion -NewBody`); aplicada aqui à função interna `Get-SectionLines`.

**As duas provas do "pronto quando" (§T3), saída literal:**

Estado corrente (`pwsh .claude/checks/check-readme.ps1`):
```
check-readme: OK - 9 agente(s), 9 skill(s), 14 guardrail(s), versão '1.5.0', 13 seção(ões) com Fonte da verdade válida.
```
exit 0 — confirma os quatro números que a T2 previu (9/9/14/`1.5.0`).

Drift (fixture sintética em scratchpad — repo mínimo copiado do real: `README.md`, `VERSION`,
`GOVERNANCA.md`, `.claude/KIT_VERSION`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`,
`docs/plans/P-0729-v2-documentacao.md`, `CHANGELOG.md`, `.claude/README.md` — repo real nunca
tocado; agente `pantonic-fake-agent.md` adicionado só na fixture, README da fixture não
atualizado; `check-readme.ps1 -Root <fixture>`):
```
check-readme: FALHOU (1 problema(s))
  - Agente 'pantonic-fake-agent' (.claude/agents/pantonic-fake-agent.md) não aparece na tabela de Agentes do README §7.
```
exit 1, nomeando exatamente o agente injetado — sem ruído de outras seções, porque a fixture
copiou todos os arquivos citados pelas 13 linhas `Fonte da verdade`.

**Guardrails-check (itens 5-7, kit agêntico):** `kit_check.ps1 -Mode validate` e `-Mode
check-drift` → `OK`, exit 0; `dead_code.py` → `OK - 0 achado(s)`; `ratchet_piso.py` → `OK -
nenhum piso declarado`.

### T1 — 2026-08-05 (fechada por verificação de premissa)

Este plano foi escrito em 2026-07-29, **antes** dos Blocos A/C do Estágio 3B, e afirma estados de
repositório que aquelas tarefas mudaram. A `V2K-T6` (commit `fa5ce0d`) criou `docs/DOC_MAP.md`; a
`ce55144` já o atualizou. A T1 virou, então, verificação + delta:

- **Cobertura completa, medida:** exatamente 5 docs do hub passam de 500 linhas
  (`DIARIO_HISTORICO` 970, `P-0725-hub-unico` 669, `RELATORIO_CONSOLIDADO` 636,
  `P-0729-v2-melhoria-candidatos` 526, `P-0721` 524) e os 5 têm entrada no mapa.
- **Âncoras válidas:** `Grep "^#{1,3} "` nos 5 arquivos confirma que toda âncora listada é
  cabeçalho real — nenhuma adivinhada (item de aceitação da skill `doc-map`).
- **Delta corrigido:** tamanhos reancorados e explicitamente datados (não são âncora);
  `P-0729-v2-melhoria-candidatos` de `in progress` para `done (20/20)`; `GOVERNANCA.md` corrigido
  para a raiz. `docs/DOC_MAP.md` = 5262 bytes (teto ~8000).
- **Consequência para T2/T3:** os dossiês deste plano afirmam outros estados de repositório
  (`README.md` inexistente, contagem de agentes/skills do §7, número de guardrails do §8). Cada um
  precisa de sonda barata **antes** da delegação — a premissa caída da T1 é padrão do plano, não
  acidente.

### T2 — 2026-08-05

**Entregue:** `README.md` na raiz, **527 linhas** (faixa 400-550 do §1), 13 seções na ordem
prescrita, cada uma abrindo com `> Fonte da verdade: <arquivo> §<seção>`.

**Estados re-medidos antes de escrever** (a advertência da T1 se confirmou de novo):

| Afirmação | Medido em 2026-08-05 |
|---|---|
| `README.md` na raiz inexistente | **verdadeira** — única premissa do plano que sobreviveu intacta |
| Versão a citar no §12 | **`1.5.0`** (`VERSION` = `.claude/KIT_VERSION`), **não** `2.0.0` |
| Agentes / skills do §7 | **9** e **9** (18 linhas na tabela) |
| Guardrails do §8 | **14** (`GOVERNANCA.md` §7, itens 1..14) |
| Premissas do §3 | **5** (`GOVERNANCA.md` §1) |

**Ambiguidades da doutrina, resolvidas escrevendo o que é verdade hoje (não inventando consenso):**

1. **Fonte da verdade do §5 (modelo econômico).** O §1 deste plano manda citar
   `~/.claude/CLAUDE.md` Regra 7 **e** `GOVERNANCA.md` §3. Escrito com fonte única
   `GOVERNANCA.md` §3, por dois motivos: (a) a `V2K-T17` já repatriou essa doutrina para o kit, e
   `GOVERNANCA.md` §3.1 diz que, em empate, **versionado vence não-versionado**; (b) um arquivo em
   `~/.claude/` não existe no consumidor e faria o guarda da T3 falhar ao checar existência do
   arquivo citado. Mesmo critério aplicado ao §11.
2. **Formato da linha de fonte.** Fixado em **um único arquivo por seção**, para que a checagem do
   guarda seja mecânica. As seções 2, 10 e 13 (cuja fonte no §1 era "este plano" / "todas as
   acima") apontam para `docs/plans/P-0729-v2-documentacao.md` §1 e §2.
3. **§7 e o que é "do kit".** Skills instaladas em `~/.claude/skills/` (`onboard`, `context-prep`,
   `doc-map`, `test-tiers`, `lean-test`, `memory-diet`) **não** entraram na tabela — o README diz
   em prosa que skills fora do repositório não viajam para o consumidor e por isso não contam como
   doutrina do framework (aplicação de `GOVERNANCA.md` §3.1).
4. **`.claude/README.md` cita um caminho local** (`D:\Skillstore\...`, bases dos auditores). Como o
   repositório é público, esse caminho foi **deliberadamente omitido** do espelho. Não é drift: é
   um dado de ambiente do dono, não doutrina.

**Evidência do §11 — as quatro do dossiê, todas confirmadas na fonte, nenhuma cifra inventada:**
executor em Opus com **71 turnos / ~189k** (`GOVERNANCA.md` §3); **~300 linhas** de código morto
testado = `dehydrate_subtitles.py` 174 l + `seed_prototype.py` 127 l
(`P-0722-governanca-guardrails-anti-saga.md:41`); as **três** premissas de plataforma caídas por
sonda curta, incluindo o **symlink com privilégio elevado no Windows** (`GOVERNANCA.md` §3 —
symlink e as outras duas são o mesmo achado, não itens separados, e o README os apresenta assim).
Somadas duas evidências já registradas na doutrina e igualmente medidas: auto-relato ~90k contra
~140k reais (§4.2) e a recalibração ≤25 → ≤30 pela série de 7 tarefas (§3). **Nenhuma lacuna** —
não houve afirmação que precisasse ir para o README sem cifra.

**Aceite verificado por comando, não por leitura:** 13 `Fonte da verdade` = 13 headings `## `; os
12 arquivos citados existem; grep de remissão proibida ("veja/leia o documento X") **vazio**; §6
com `mermaid` + a `T15` real do `P-0729-v2-melhoria-candidatos` como exemplo de tarefa atômica;
§12 com a regra anti-drift; §13 com **duas** perguntas cuja resposta é "não adote" (Q2 — projeto
pequeno/não-desktop/time com CI; Q6 — quem quer framework maduro, com o fato desfavorável de um
único consumidor real); §10 com oito limites honestos. Varredura de segredo/credencial/caminho
local no README: **nada**.

**O que a T3 precisa saber.** Os quatro números que o guarda deve comparar com o disco: **9**
agentes, **9** skills, **14** guardrails, versão **`1.5.0`**. Dois avisos de implementação: (a) as
linhas de fonte usam **um** arquivo por seção e o caminho vem sempre entre crases — parsear por
crase, não por espaço; (b) a contagem de guardrails do §8 é a de linhas de tabela numeradas `| N |`
dentro da seção 8 — o README tem **outra** tabela numerada `| N |` (o sumário de 13 seções, no
topo), então o guarda precisa recortar a seção antes de contar, sob pena de achar 27.

### T2 — 2026-08-05 (2ª rodada)

**Entregue:** `README.md` reescrito como **proxy das implementações** — **752 linhas** (faixa
750-900 do §1 revisado), **15 seções** na ordem da tabela de §1, cada uma abrindo com
`> Fonte da verdade: <arquivo> §<seção>` apontando arquivo existente no repositório. Fontes
efetivamente citadas: `GOVERNANCA.md` (§1, §2, §4, §5, §8, §10, §12, §13, §14), `.claude/README.md`
(§11), `CHANGELOG.md` (§15) e as três skills — `proximo-passo` (§6), `diario-de-obras` (§7),
`handover` (§9). Nenhuma seção aponta para `docs/plans/` nem para `~/.claude/`: o esqueleto novo não
tem seção cuja fonte seja "este plano", que era a saída da 1ª rodada para §2/§10/§13.

**Ajuste no guarda (`.claude/checks/check-readme.ps1`), conforme o dossiê:** as duas seções passam a
ser localizadas **pelo título** (`^## \d+\. Anatomia do kit` e `^## \d+\. Os guardrails`) em vez do
número hardcoded — variáveis renomeadas de `$sec7*`/`$sec8*` para `$secKit*`/`$secGuard*` e as
mensagens de erro correspondentes reescritas sem citar número de seção. Bloco de ajuda atualizado
(linha 6 e as descrições das 5 checagens), incluindo o rótulo de origem da versão, que era "§12" e
virou "corpo do README" — a linha `Versão vigente do framework:` migrou para a §13 do esqueleto
novo, e o guarda nunca dependeu do número, só do texto. **Lógica das checagens 3, 4 e 5 intocada**;
os padrões `^## 7\. Guardrails dos agentes` / `^### 7\.1` continuam apontando para `GOVERNANCA.md`,
como o dossiê exigia.

**Decisões de redação não triviais:**

1. **As duas seções antigas fora das listas do dossiê**, resolvidas como o dossiê antecipou: a §9
   "Como adotar em 10 minutos" foi **descartada** (regra "zero convencimento"; o esqueleto novo não
   tem seção de adoção) e a §12 "Versão, changelog e mapa dos documentos" foi absorvida pela nova
   §13 "Distribuição e versão". **A tabela "Quer saber X? O arquivo é Y" não sobreviveu**: sob a
   regra "nenhuma remissão do tipo 'leia o documento X'", uma tabela de 11 remissões é o próprio
   defeito que a regra proíbe. O `docs/DOC_MAP.md` continua sendo a porta de entrada dos docs
   grandes, mas isso é procedimento de agente, não conteúdo do espelho — daí não haver ponteiro para
   ele no corpo. Se o dono quiser o índice de "onde mora o quê" de volta, é decisão dele, não da
   execução.
2. **A §4 antiga ("filosofia em seis escolhas") foi dissolvida**, como mandava o dossiê: (a) virou o
   "por que foi adotado" da §4 nova; (b) o da §9; (c) o fecho da §10; (d) a premissa 5 da §2; (e) o
   "por que" da §5; (f) o "por que" da §13. Nenhuma escolha se perdeu, e o formato
   "escolha → rejeitado → por quê → custo" foi absorvido no texto corrido de cada seção em vez de
   virar uma seção própria de argumentação.
3. **Conteúdo de fonte que estava ausente do espelho anterior e entrou agora**, por ser procedimento
   e não argumento: os quatro artefatos iniciais (`GOVERNANCA.md` §6) na §5; a régua de
   especialização por altura de camada (§2 da doutrina) na §2; as travas do procedimento de próxima
   tarefa, inclusive a higiene de busca, na §6; a estrutura literal do diário na §7; os passos de
   decisões/lições e a nota-forward de obsolescência na §9; o ciclo típico do kit na §11.
4. **Meta de tamanho atingida por profundidade de fonte, não por retórica.** A 1ª passagem fechou em
   661 linhas; as ~90 linhas restantes vieram dos itens do ponto 3, todos com fonte, mais duas
   linhas novas no ADR da §14 (deriva medida do índice derivado — 8/9 agentes e 6/8 skills — e a
   colisão de nomenclatura `P-0722`/`P-0729`). Nenhum parágrafo foi escrito para preencher cota.

**Ambiguidades de doutrina encontradas (escrito o que é verdade hoje, sem inventar consenso):**

1. **Governança de memória é doutrina do dono, não do kit.** A §12 do esqueleto manda descrever "o
   que vira memória, o que não vira e a fila `_INBOX.md` que só o dono promove", com fonte
   `GOVERNANCA.md` §4. Só que `GOVERNANCA.md` §3.1 declara explicitamente que essa governança
   **mora fora do kit** (`~/.claude/docs/GOVERNANCA_MEMORIAS.md`), por passar na pergunta 1 do teste
   de residência — e por isso **não viaja** ao consumidor. Resolvido escrevendo a prática vigente do
   hub **e** declarando a residência no corpo da §12: um consumidor recebe a régua de residência e a
   doutrina de telemetria, não a governança de memória em si. Sem essa nota, o espelho prometeria ao
   consumidor uma prática que o kit não entrega.
2. **A §15 é histórico congelado, e a `DD-8` já decidiu isso** — mas o texto entregue precisou de uma
   marca explícita disso no próprio corpo da seção, senão o guarda de drift futuro (ou um leitor)
   trataria uma seção deliberadamente desatualizada como espelho envelhecido. Registrado na primeira
   linha da §15.
3. **Nomes das 5 dimensões `MANTER`** (D1, D3, D4, D10, D16) não estão no `CANDIDATOS.md`, que só as
   cita por número; vieram de `docs/benchmark/RELATORIO_CONSOLIDADO.md` (headings `### D<N> — <nome>
   — **VEREDITO**`). Não é ambiguidade de doutrina, é ponteiro faltando no insumo — anotado aqui
   porque a `T5` (fidelidade por amostragem) pode querer conferir a lista "o que fica" e não a
   encontraria no `CANDIDATOS.md`.

**Verificação (comando colado do terminal):**
`pwsh -File D:\workspaces\PantonicApp\.claude\checks\check-readme.ps1` →
`check-readme: OK - 9 agente(s), 9 skill(s), 14 guardrail(s), versão '2.0.0', 15 seção(ões) com
Fonte da verdade válida.`, **exit 0**. Contagem final:
`(Get-Content README.md | Measure-Object -Line).Lines` = **752**. Lista de headings `## ` conferida:
as 15 seções na ordem exata da tabela de §1 (os dois `## ` extras que a listagem mostra estão
**dentro** do bloco cercado ```markdown``` da §7, não casam `^## \d+\. ` e são inertes para o
guarda).

**O que a `T5`/`T6` precisam saber.** (a) O guarda deixou de depender de número de seção — reordenar
o esqueleto de novo não o quebra, desde que os títulos "Anatomia do kit" e "Os guardrails" fiquem
como estão e a linha `Versão vigente do framework:` continue existindo em algum lugar do corpo.
(b) A versão citada no README é **`2.0.0`** nos dois pontos (cabeçalho e §13), coerente com
`VERSION`/`.claude/KIT_VERSION` **atuais**; o bump para `2.0.1` da `DD-7` é da `T6` e vai precisar
mexer nos **dois** pontos do README, senão a checagem 3 fica vermelha. (c) Nada commitado nesta
tarefa.

Consumo: ver `docs/telemetria.tsv` (linha `V2D-T2r2`)
