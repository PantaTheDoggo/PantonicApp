# Diário de Obras — PantonicApp (hub de governança Pantonic*)

**Diretiva de priorização:** Priorize a iniciativa `PANTONIC-V2` (consolidação do framework —
benchmarking → confronto → melhoria → documentação).

> Este diário é o kanban do backlog de **governança comum** dos projetos Pantonic*. Os planos
> completos vivem em `docs/plans/P-*.md`; aqui ficam o índice, o status e o ponteiro. Entrada de
> planos novos: `docs/plans/_INBOX.md` (append-only), drenado por quem abrir a skill
> `proximo-passo`.

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|
| SPRINT-PANTONICV2 | Consolidação do framework em V2 — 4 estágios encadeados | in progress | `## SPRINT-PANTONICV2` |
| P-0729-V2B | Estágio 1 — benchmarking de 21 frameworks públicos (T1..T9) | done | `docs/plans/P-0729-v2-benchmarking.md` |
| P-0729-V2C | Estágio 2 — confronto, diagnóstico e autoria do plano 3B (T1..T6) | done | `docs/plans/P-0729-v2-confronto.md` |
| P-0729-V2M | Estágio 3A — doutrina herdada do P-0722 (T1..T5 completos, 5/5) | done | `docs/plans/P-0729-v2-melhoria.md` |
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking (T1..T19, com `T12` partida em `T12a`/`T12b`; 20/20) | done | `docs/plans/P-0729-v2-melhoria-candidatos.md` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T4 entregues; `T5` reprovada, `T6` cancelada por absorção) | superseded | substituído por `docs/plans/P-0730-v2-identidade.md` |
| P-0730-V2I | Estágio 5 — identidade do framework: agnosticismo a stack/plataforma, CA+DDD, perfis e o README como contrato canônico (6/16) | in progress | `docs/plans/P-0730-v2-identidade.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |
| TK-01 | Corrigir residência de `modelo-por-fase` em `GOVERNANCA.md` §3 e no bullet `V2M-T1` do `CHANGELOG.md` (ainda apontam `~/.claude/skills/`, superado por `DM-7`) | done *(absorvido pela `V2M-T3`)* | `docs/DIARIO_HISTORICO.md#tíquetes-avulsos--condensado-em-2026-08-01` |
| TK-02 | `.claude/sync-kit.ps1`: `Get-ExcludedKeys`/`Test-Excluded` quebram sem `kit-exclude.txt` presente (achado pré-existente, `V2K-T11`) | done | docs/DIARIO_HISTORICO.md#tíquetes-avulsos--2ª-condensação-2026-08-01
| TK-05 | Skill `checar-versao-kit`: o gatilho de revisão de doutrina (`GOVERNANCA.md` §7.1) compara só o componente MINOR e fica cego ao atravessar um MAJOR (local `2.0.0` × última rodada `1.4.0` ⇒ "sem pendência" indevido) | backlog *(achado do planejamento do `P-0730`)* | `docs/plans/P-0730-v2-identidade.md` §7 |
| TK-06 | `docs/DOC_MAP.md` lista `GOVERNANCA.md` entre os "docs abaixo de 500 linhas (Read direto)", mas o arquivo já está em **644 linhas** — o mapa manda ler integralmente um doc que passou do limite e não tem entrada de âncoras. Drift pré-existente (já >500 antes da `V2I-T5`); corrigir criando a entrada de navegação da GOVERNANCA no DOC_MAP | backlog *(achado da `V2I-T5`)* | `docs/DOC_MAP.md:7-9` |
| TK-04 | `.claude/agents/pantonic-executor.md:20` hardcoda "orçamento esperado ~≤40 tool uses" — diverge de `DR-C`/`V2K-T16` (o kit, `GOVERNANCA.md` §3, já é a única autoridade numérica, tabela de tetos por classe; o global perdeu o número na `T17`) | backlog *(achado da `V2K-T17`)* | `.claude/agents/pantonic-executor.md:20` |

---

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0`.

**Próxima tarefa da sprint:** `V2I-T7` — [Opus], no **Estágio 5** (`P-0730-V2I`, 6/16). Dossiê em
`docs/plans/P-0730-v2-identidade.md` `### T7`.

**Estágio 5 aberto em 2026-08-05 — o Estágio 4 foi reprovado no aceite e está `superseded`.** A
`V2D-T5` cumpriu seu papel: a leitura do README pelo dono detectou que a identidade declarada do
framework está errada **na fonte da verdade** (`GOVERNANCA.md` §1: "desktop, stack fixo PySide6"),
não no espelho. O entendimento canônico é **agnóstico a tecnologia e plataforma**, atuando nos
níveis de **arquitetura** e de **projeto**, sobre **clean architecture + DDD**, estendidos pelo
**infracore** e por **plugins (um plugin = um caso de uso)**. `DR-7` eleva o **README a documento
canônico — o contrato entre o framework e o cliente**: um framework correto é rejeitado por um
README equivocado. 11 desvios medidos, 15 tarefas, fechamento em `2.1.0`.

**Revisão de rota em 2026-08-05 (decisão do dono).** A premissa do Estágio 4 estava errada desde o
planejamento: o README foi projetado como documento de **adoção** (as 6 perguntas da `T5` testavam
convencimento) quando o objetivo é ser um **proxy das implementações** para o gerente argumentar
sobre as práticas sem ler skill, agente e hook um a um — mais a visibilidade do que a V2 mudou (o que
fica, o que sai, o que se modifica). `T2` reaberta, `T5` substituída (utilidade + fidelidade), `T6`
nova (fecha a `2.0.1`), `DD-4` revogada. `T1`, `T3` e `T4` não foram afetadas. Fora de escopo por
decisão do dono: o `git push` e a migração do `PantonicVideo`.

A `V2D-T4` fechou em 2026-08-05: `VERSION`/`.claude/KIT_VERSION` em `2.0.0`, `CHANGELOG.md` §2.0.0
consolidando a iniciativa inteira com a justificativa do MAJOR e a nota de migração ao
`PantonicVideo`, `GOVERNANCA.md` §9 apontando o README como porta de entrada humana, guarda do T3
em exit 0 sobre o estado `2.0.0`, tag anotada `kit-v2.0.0` criada localmente (sem push). Divergência
do consumidor reportada, nenhuma alteração feita em `d:\workspaces\PantonicVideo` — ver
`## Achados da execução` de `docs/plans/P-0729-v2-documentacao.md`.

A `V2I-T1` fechou em 2026-08-05: commit único fechando o veredito do Estágio 4 (`V2D-T5`
reprovada, `V2D-T6` cancelada por absorção) e abrindo o Estágio 5 — README espelho, guarda de
drift, `DOC_MAP.md`, diário e telemetria, mais o plano novo `docs/plans/P-0730-v2-identidade.md`.
Detalhe do veredito em `## Achados da execução` §`T5/T6 — 2026-08-05` de
`docs/plans/P-0729-v2-documentacao.md`.

Consumo: ver docs/telemetria.tsv (linha `V2I-T1`)

A `V2I-T2` fechou em 2026-08-05 — **resultado negativo medido.** Varredura de contaminação do
benchmarking: `Grep -i "desktop|pyside|mvvm|\bqt\b"` (+ "não se aplica"/"aplicação local") nas
seções `## 2. Dimensão por dimensão` e `## 4. Descartes justificados` de
`docs/benchmark/RELATORIO_CONSOLIDADO.md`, e nas linhas `REJEITAR`/`adiar` de
`docs/benchmark/CANDIDATOS.md`. Nenhuma ocorrência satisfaz o critério de achado (rejeição/descarte
que **invoca** desktop/PySide6/MVVM/Qt como razão). Classificação das ocorrências: `D1 — Identidade
e escopo` (linhas 113-126) descreve a identidade desktop/PySide6/MVVM do Pantonic, mas o veredito é
**MANTER**, não descarte — irrelevante ao critério. O único `REJEITAR` de seção 2 (`D2 —
Vitalidade`, linha 130) é motivado por bus factor/SLA, sem menção a stack. A frase-guarda da seção 4
(linha 683, "conflito com as premissas Pantonic: desktop-first, custo por turno, ...") é a moldura
geral da seção; nenhum dos 8 descartes individuais (linhas 686-747) cita desktop/PySide6/MVVM/Qt
como motivo específico. Em `CANDIDATOS.md`, os dois `adiar` (`C-14`, depois revertido para `adotar`
pelo dono; `C-15`) têm motivo de custo/risco de infraestrutura, não de stack; o único `REJEITAR`
mencionado (`D2`, linha 439) repete o motivo de bus factor/SLA. Nenhum tíquete `TK-` aberto.
Nenhuma perda material identificada — a premissa errada não descartou candidato algum em silêncio.

Consumo: ver docs/telemetria.tsv (linha `V2I-T2`)

A `V2I-T3` fechou em 2026-08-05 — o entregável **é** o texto novo: `GOVERNANCA.md` §1 (identidade
agnóstica, dois níveis, 5 premissas sem stack), **§1.1 nova — Perfis** (`DR-2`) e §2 (régua por
altura preservada + ressalva medida de que o core é doutrina agnóstica com implementação ainda
ligada ao PySide6 → `P-0731`/`DR-5`). Três deltas que outras tarefas consomem: (a) **contrato de
declaração de perfil = `.claude/PERFIL`**, uma linha, artefato do projeto fora de `.claude/kit/`,
default `desktop-pyside6` na ausência — é o que a `V2I-T8` implementa no kit; (b) perfil
`web-servidor` declarado **sem verificação própria ainda** (G-PREMISE: vazio honesto, não vão);
(c) **edição adjacente ao alvo `10-37`** — §7 item 3 (MVVM estrito) passou a
`*[perfil desktop-pyside6]*`; era regra universal de stack que nenhuma tarefa do plano cobria e que
a §1.1 já contradizia, consequência mecânica da `DR-2`, não troca de rota.
Verificação: `Grep -i "desktop|pyside|mvvm|\bqt\b" GOVERNANCA.md` → 5 ocorrências, todas em
contexto de perfil; `pwsh .claude/checks/check-readme.ps1` → exit 0. Resíduo deixado de propósito:
`GOVERNANCA.md:348` (§6) — alvo declarado da `V2I-T10`.

Consumo: ver docs/telemetria.tsv (linha `V2I-T3`)

A `V2I-T4` fechou em 2026-08-05 — `ARQUITETURA_PANTONICA.md` deixa de exigir Qt como núcleo. O
documento ganhou uma **convenção de perfil** no cabeçalho (marcador *[perfil `desktop-pyside6`,
§1.1]*, declaração em `.claude/PERFIL`, ausência ⇒ `desktop-pyside6`, canônica em `GOVERNANCA.md`
§1.1) e toda exigência de stack foi reclassificada: §2 (allowlists de import de infracore/plugins e
a relação com MVVM), §3 (`ui_shell/`, `view_model.py`, ponte de logs do toolkit), §4 (linha
`ui_shell` e a shell na ordem de boot), §6 (QThreadPool/QRunnable como primitiva do perfil sob o
`task_runner`), §9 (allowlist AST de plugins), §10 **inteira** (marcador no próprio título), §11
(platformdirs vira default do perfil; a regra agnóstica passa a ser o ponto único de resolução),
§13 (pytest-qt) e §14 (shell Qt, View/ViewModel e primitivas de thread declarados fora do núcleo).
Ficaram intocados, por já serem agnósticos: golden rules (§1), as quatro camadas e a regra de
dependência, ACL, sinais/estado, plugins/manifests, contenção de falhas (§12) e a disciplina de
testes (§13).

Deltas que outras tarefas consomem: (a) a notação de marcação do corpus é a da `T3` — *[perfil
`desktop-pyside6`, §1.1]* — e o marcador `[PERFIL: desktop-pyside6]` previsto no dossiê original do
plano foi descartado para não deixar dois concorrentes (reconciliação registrada em
`docs/plans/P-0730-v2-identidade.md`, `## Achados da execução`); (b) dentro de árvore de diretórios
ou bloco de código, onde ênfase Markdown não renderiza, vale a variante sem itálico `[perfil
desktop-pyside6]` acompanhada de uma legenda logo abaixo do bloco; (c) nenhuma definição de perfil
foi duplicada — `GOVERNANCA.md` §1.1 permanece a única fonte, apenas referenciada.

Verificações: `Grep -i "pyside6|\bqt\b|mvvm|desktop|qthread|qobject"` em `ARQUITETURA_PANTONICA.md`
→ 23 ocorrências, **todas** dentro de trecho marcado por perfil, no próprio marcador/convenção de
leitura, ou em contexto explícito do case de referência; zero como regra universal.
`pwsh .claude\checks\check-readme.ps1` → `OK - 9 agente(s), 9 skill(s), 14 guardrail(s), versão
'2.0.0', 15 seção(ões) com Fonte da verdade válida`, exit 0.

Resíduos deixados de propósito: §12 mantém "UI thread" na linha do TaskRunner — é descrição do
comportamento no case de referência e reescrever a tabela de contenção está fora do escopo
declarado da `T4`; §14 continua intitulada "O que NÃO portar do PantonicVideo", com o recorte de
perfil adicionado como parágrafo em vez de retitulação. O documento marca o que é do perfil
desktop, mas **não** define o que os perfis `container`/`web-servidor` usam no lugar (superfície de
entrada, primitiva de concorrência, raiz de dados) — isso é matéria das tarefas seguintes do
estágio, não desta marcação.

Consumo: ver docs/telemetria.tsv (linha `V2I-T4`)

A `V2I-T5` fechou em 2026-08-05 — o corpus passa a **ter DDD**, que antes tinha 1 ocorrência no
documento inteiro (`D3`). Três textos novos: (1) `ARQUITETURA_PANTONICA.md` **§1.1 Fundamentos —
clean architecture + DDD**, entre as golden rules e o modelo de camadas, com o glossário de 8
termos (linguagem ubíqua, entidade, VO, agregado, invariante, serviço de domínio, caso de uso,
contexto delimitado — cada um com "como se reconhece"), a regra de pureza da camada de domínio, uma
**escada de classificação de 6 perguntas** que decide se uma classe nova é entidade/VO/agregado/
serviço de domínio/serviço-ACL/caso de uso, e a tese pantônica (`D5`): infracore doutrina as camadas
de aplicação e infraestrutura que a CA deixa ao improviso, e **cada plugin responde por exatamente
um caso de uso** — um caso de uso = um plugin = um manifest = um TF. (2) `GOVERNANCA.md` §5 abre
com a regra normativa `um plugin = um caso de uso` e quatro consequências verificáveis na revisão
de um plugin novo (sem caso de uso nomeável não entra; caso de uso partido em dois plugins é
acoplamento disfarçado; dois casos de uso num plugin é atomicidade quebrada; comunicação só por
sinais e estado), e o passo 3 do fluxo de POC agora manda dissecar pela escada da §1.1. (3)
`GOVERNANCA.md` §6 item 1 põe no PRD a obrigação de nomear o contexto delimitado, listar
entidades/VOs/agregados com invariantes e fixar a linguagem ubíqua (termo novo na execução volta ao
PRD), com cada caso de uso listado como candidato a exatamente um plugin. Nenhuma linha nova nomeia
stack — o texto encaixa na identidade agnóstica da `T3`.

`D10` cumprido: o grau de aderência da implementação atual está declarado **NÃO AUDITADO** em dois
fechos — `ARQUITETURA_PANTONICA.md` §1.1 (infracore e plugins vs. CA+DDD) e `GOVERNANCA.md` §5
(plugins existentes vs. um caso de uso cada) —, ambos apontando para a `T14` e para
`docs/audits/AUDIT_ARCH_<AAAA-MM-DD>.md`, com a proibição explícita de o corpus afirmar conformidade
antes da medida (G-PREMISE).

Deltas que outras tarefas consomem: (a) `ARQUITETURA_PANTONICA.md` §1.1 é a **fonte única** do
vocabulário de domínio — `T9` (auditor de CA+DDD), `T11`/`T11b` (README e glossário) e `T6`
referenciam, nunca duplicam; (b) a escada de 6 perguntas é o critério auditável que a `T9` pode
transformar em checagem; (c) a `T14` precisa substituir **as duas** declarações de não-auditoria, e
não só uma; (d) numeração: a seção entrou como `### 1.1` para não renumerar `##2`..`##15` e as
referências cruzadas do corpus, e o cabeçalho ganhou uma linha de desambiguação — o `§1.1` dentro
do marcador de perfil continua apontando para `GOVERNANCA.md` §1.1 (Perfis). Justificativa completa
em `## Achados da execução` §`T5 — 2026-08-05` de `docs/plans/P-0730-v2-identidade.md`.

Verificações: `grep -c -i "\bDDD\b|agregado|linguagem ubíqua"` → `ARQUITETURA_PANTONICA.md:14`,
`GOVERNANCA.md:12` (antes: 1 ocorrência de DDD em todo o corpus); `pwsh
.claude\checks\check-readme.ps1` → `OK - 9 agente(s), 9 skill(s), 14 guardrail(s), versão '2.0.0',
15 seção(ões) com Fonte da verdade válida`, exit 0.

Resíduos deixados de propósito: `GOVERNANCA.md` §6 **item 2** ("MVVM + clean architecture") segue
intocado — alvo declarado da `V2I-T10`; §4 (backlog/sprints/responsabilidades) e o eixo
qualidade→rota→custo são da `V2I-T6`, não desta tarefa; `docs/DOC_MAP.md` não foi atualizado
(fora do alvo) — o drift medido virou o tíquete `TK-06` no índice.

Consumo: ver docs/telemetria.tsv (linha `V2I-T5`)

A `V2I-T6` fechou em 2026-08-05 — a **camada de projeto** passa a estar declarada como o dono a
definiu (`D6`, `D7`, `D8`, `DR-3`), toda em `GOVERNANCA.md`, com uma âncora greppável por alínea.
(a) **Eixo de justificação — qualidade → rota → custo** abre a §3: o motor declarado é a doutrina da
qualidade (agir sobre o **processo** que gera o produto, não sobre o produto — daí guardrails, TDD,
piso, contexto limpo e o gate de sprint), a rota vem depois (decidida no planejamento, fiel na
execução), e o custo é **restrição de projeto**, não razão de ser; modelo por fase e orçamento de
turnos tornam a qualidade sustentável, não a compram mais barata. A ordem é decisória: nenhuma
economia derruba guardrail, nenhuma rota muda para caber no orçamento — inverte o "custo, rota,
qualidade" que o README ainda declara (`D6`, alvo da `T11`). (b) **Filiação ágil** abre a §4:
backlog, sprints e tarefas **derivam de Scrum**, modulado para programação agêntica porque quem
consome o backlog é um agente com contexto finito — tabela de 6 correspondências (backlog→diário,
sprint→plano `P-NNNN`, história→tarefa atômica, time auto-organizado→papéis fixos,
cerimônias→atos escritos, DoD→critério de pronto + guardrails), mais as duas práticas que **não**
viajam (story points, substituídos pelo orçamento de turnos medido; auto-organização de escopo,
proibida pelo modelo por fase). (c) **§4.5 Validação por sprint — gate do gerente/cliente**
(subseção nova, aditiva): nenhuma sprint avança sem validação **visual** do entregável pelo
gerente/cliente; suíte verde não substitui (teste prova o que o agente entendeu, a validação prova
o que o dono quis); reprovação volta como rodada da mesma sprint, não vira tarefa de outra; sprint
sem entregável mostrável é decomposição errada. (d) **Matriz de responsabilidades** na abertura da
§3, **lugar canônico único**: cinco papéis (dono/gerente, planejamento, execução, coleta,
auditoria) com colunas *Responde por* e *Não faz* — absorveu a tabela de agentes que já vivia ali.

`DR-A` cumprido sem duplicata: o bullet da §3 que repetia em prosa a fronteira dos papéis virou
**ponteiro** para a matriz; §4 (tabela Scrum), §4.5 e §5 apontam para a §3; a **regra** do gate mora
na §4.5 e o **veredito** de cada sprint no diário (§4.2, bullet novo) — doutrina versionada de um
lado, estado de trabalho do outro. Decisões de redação (por que a matriz não virou `### 3.1`, por
que a validação entrou como `### 4.5`) em `## Achados da execução` §`T6 — 2026-08-05` do plano.

Deltas que outras tarefas consomem: (a) a `T11` reescreve o README sob o eixo `qualidade → rota →
custo` — a fonte da verdade já está invertida aqui; (b) a `T7`, ao criar o **G-README** (§7 item
15), precisa ligá-lo de volta à §4.5 — a §4.5 fecha dizendo que em sprint de doutrina o entregável
é o documento e a leitura do dono é a validação, **sem citar item de guardrail**, porque o item 15
ainda não existe (ponteiro proposital, não esquecimento); (c) qualquer agente/skill que descreva
papel passa a apontar para a matriz da §3, nunca a repetir.

Verificações (âncora por alínea): `qualidade → rota → custo` → `GOVERNANCA.md:92`; `Filiação ágil`
→ `:229`; `### 4.5 Validação por sprint` → `:362` e `validação visual do gerente/cliente` → `:364`;
`Matriz de responsabilidades` → `:103` (canônica) + 4 ponteiros. `pwsh
.claude\checks\check-readme.ps1` → `OK - 9 agente(s), 9 skill(s), 14 guardrail(s), versão '2.0.0',
15 seção(ões) com Fonte da verdade válida`, exit 0 — §7 intocada, guarda no mesmo estado de antes.

Resíduos deixados de propósito: `GOVERNANCA.md` §6 item 2 ("MVVM + clean architecture") segue
intocado (`V2I-T10`); §7 não foi tocada (`V2I-T7`); o README continua declarando o eixo invertido
(`V2I-T11`).

Consumo: ver docs/telemetria.tsv (linha `V2I-T6`)

**Condensado em 2026-08-01 (2ª rodada).** O gate aberto pela `V2K-T12b` foi resolvido pelo dono
antes desta tarefa: o contexto encerrado da sprint — ficha da `V2K-T12`, decisões já resolvidas,
histórico dos Estágios 1/2/3A e os bullets de fechamento de `V2K-T1..T12b` — está em
`docs/DIARIO_HISTORICO.md`. Diário ativo: 569 → 98 linhas; histórico: 516 → 1007 linhas.

**Origem:** pedido do dono, 2026-07-29. **Planejamento:** Opus, 2026-07-29 (4 planos registrados no
mesmo ato, com a cadeia de dependência declarada).

**Encadeamento:** os estágios são sequenciais. Só o Estágio 1 nasce `backlog`; os demais são
`blocked` por dependência do anterior e **não são escolhíveis** pela `proximo-passo` até o
predecessor fechar — assim a iniciativa mantém **um único plano vivo** por vez (skill
`diario-de-obras`, "Planos derivados", caso C). Exceção registrada em `P-0729-v2-melhoria` DM-4:
o Estágio 3A inteiro vem do `P-0722` (decisões fechadas em 2026-07-22) e pode ser antecipado se o
dono quiser paralelismo.

**Gate de publicação (decisão do dono, 2026-07-29):** nenhum plano desta iniciativa é publicado em
aberto. O Estágio 3B — as mudanças que só o benchmarking podia revelar — **nasceu fechado em
2026-07-29**, autorado pela `V2C-T6` (última tarefa do Estágio 2) a partir do `CANDIDATOS.md` já
ratificado, e só então entrou no inbox e neste índice: 19 tarefas, 14 candidatos cobertos, nenhuma
questão pendente. O ciclo do gate está fechado na prática antes de virar doutrina em `V2M-T1`
(G-PLANREADY item 5).

### Estágio 3B — `P-0729-v2-melhoria-candidatos` [done — 20/20 (Blocos A e C fechados; `T12` partida em `T12a`/`T12b` ⇒ 20 tarefas), nascido fechado em 2026-07-29 pela `V2C-T6`]

19 tarefas, cada uma com o `C-NN` de origem. Ordem normativa em `docs/plans/P-0729-v2-melhoria-candidatos.md`
§2 — **Bloco A** (`T1..T4`) antes do Estágio 3A; **Bloco C** (`T5..T19`) depois dele.

**Bloco A (`T1..T4`) e Bloco C até `T12b`: `done`, 13/20.** Os bullets de fechamento (resultado,
verificação, veredito e `Consumo:` de cada tarefa) estão em `docs/DIARIO_HISTORICO.md`, seção
"Estágio 3B: contexto encerrado e tarefas `T1..T12b`". **`V2K-T13`, `V2K-T14`, `V2K-T15`,
`V2K-T16`, `V2K-T17`, `V2K-T18` e `V2K-T19`: `done`, 20/20 — Bloco C fechado** em 2026-08-04
com o bump `1.5.0` + tag `kit-v1.5.0`; bullets de fechamento abaixo, ainda não condensados
(diário a ~140 linhas, longe do gatilho de 500).

**Bloco C — fechado:**
- `V2K-T13` — Compatibilidade por major kit × consumidor — [Sonnet] — **done** *(`C-14`; contíguo
  a `T11`/`T12` por DK-11)*
  - Mudou: `.claude/skills/checar-versao-kit/SKILL.md` (passo 3 extrai o componente MAJOR de cada
    versão; seção "Os resultados possíveis" ganha os ramos "Divergentes em MINOR/PATCH" —
    comportamento antigo — e "Divergentes em MAJOR" — reporta como incompatível e para, sem a
    pergunta de atualizar/postergar); `GOVERNANCA.md:467-474` (§10, bullet "Divergentes" dividido
    nos mesmos dois ramos, regra `(a)` preservada intacta).
  - Verificação: `.claude/checks/kit_check.ps1 -Mode validate` → OK (9 agentes, 9 skills, VERSION
    == KIT_VERSION `1.4.0`); `-Mode check-drift` → OK. Walkthrough textual do procedimento da
    skill (skill é procedimento, não script) sobre três `KIT_VERSION` sintéticos no scratchpad,
    contra um remoto hipotético `kit-v2.1.0`: local `1.4.0` (MAJOR `1`≠`2`) → ramo "Divergentes em
    MAJOR", mensagem de incompatibilidade, para; local `2.0.0` (MAJOR igual, MINOR `0`≠`1`) →
    ramo "Divergentes em MINOR/PATCH", mensagem antiga (atualizar agora ou postergar); local
    `2.1.0` (igual) → silêncio. Nenhuma automação de update introduzida; §10(a) intacto.
  - Consumo: 18 tool uses, ~73k tokens, Sonnet, ~8m22s (medido pela notificação de conclusão).
- `V2K-T14` — Doutrina do piso de regressão **comportamental** (§4.4) — [Opus] — **done**
  *(`C-11`a; nunca percentual)*
  - Mudou: `GOVERNANCA.md:206-238` (§4.4) — o TR deixa de definir o piso como contagem ("o número
    de testes verdes nunca diminui", texto removido) e ganha o bloco "Piso de regressão —
    comportamentos trancados, nunca percentual" respondendo às três perguntas exigidas: mede-se por
    lista versionada `tests/piso_comportamental.txt` (`<pytest nodeid> — <comportamento em uma
    frase>`, unidade = a frase); prova-se por comando (`.claude/checks/ratchet_piso.py` via
    `guardrails-check`, materializado na `T15`); remover comportamento é **ato do dono registrado no
    diário**, no mesmo commit que remove o teste — nunca efeito colateral de refactor.
  - Verificação: `Grep "percentual|cobertura"` em §4.4 → só forma negativa ("não é percentual de
    cobertura", "não vale como piso, meta ou critério de pronto"); referência cruzada a
    `G-DEADCODE` (§7 item 9) escrita e argumentada (piso percentual premia teste de código morto);
    `Grep "número de testes verdes|testes verdes nunca"` no repo → 0 matches (nenhuma cópia obsoleta
    da definição antiga); `Glob "tests/**"` → 0 arquivos (hub segue sem `tests/`, como previsto).
  - Consumo: 15 tool uses, Opus, execução **inline** (tarefa de 1 write-cluster — Regra 7 não abre
    subagente abaixo de ~15 turnos); sem bloco `<usage>` a medir, não há autoestimativa de tokens.
- `V2K-T15` — Receita executável de ratchet do piso — [Sonnet] — **done** *(`C-11`b)*
  - Mudou: `.claude/checks/ratchet_piso.py` (**novo** — mesma forma do `dead_code.py`: `--root`
    com default do próprio projeto, `--piso` com default `tests/piso_comportamental.txt` relativo
    ao `--root`, exit 0 = OK, exit != 0 = falha nomeando o achado; arquivo de piso ausente é exit
    0 explícito "nenhum piso declarado" — TK-02 aplicado a insumo opcional; linha do piso sem o
    separador ` — ` é erro de formato, exit != 0, nunca silêncio); `.claude/skills/guardrails-check/SKILL.md`
    (item 4 alinhado ao piso comportamental — removida a linguagem de contagem/percentual
    obsoleta desde a `T14`; item 7 novo, bloqueante no mesmo padrão dos itens 5/6, invoca
    `ratchet_piso.py`; bloco "Veredito" com a linha `Piso:` no vocabulário comportamental).
  - Verificação: dois casos sintéticos em projeto-brinquedo no scratchpad
    (`tests/test_x.py` com 3 testes reais + `tests/piso_comportamental.txt`). Caso A (piso casando
    a coleta):
    ```
    ratchet_piso: OK - piso intacto sob '...\toy_project' (...\toy_project\tests\piso_comportamental.txt).
    EXIT=0
    ```
    Caso B (linha do piso apontando para nodeid inexistente):
    ```
    ...\toy_project\tests\piso_comportamental.txt:2: tests/test_x.py::test_divisao_por_zero — divisao por zero levanta excecao controlada (comportamento perdido: nodeid nao aparece mais na colecao da suite)
    ratchet_piso: FALHOU - 1 comportamento(s) perdido(s) do piso.
    EXIT=1
    ```
    A prova no consumidor real (`PantonicVideo`) pertence à `V2D-T4`, não a esta tarefa.
    Kit: `kit_check.ps1 -Mode validate` → OK (9 agentes, 9 skills, `VERSION == KIT_VERSION`
    `1.4.0`); `-Mode check-drift` → OK (sem deriva — o novo arquivo em `.claude/checks/` não
    entra no índice de agentes/skills). Piso do hub: `python .claude/checks/ratchet_piso.py`
    (sem `--root`) → `OK - nenhum piso declarado` (hub segue sem `tests/`, como previsto);
    `dead_code.py` → `OK - 0 achado(s)`.
  - Veredito (skill `guardrails-check`):
    ```
    Veredito — V2K-T15
    Suítes: n/a (hub sem tests/, como previsto; script novo é standalone, sem tests/conformance/ a rodar)
    Piso: ratchet_piso.py — OK - nenhum piso declarado (hub); dead_code.py — OK - 0 achado(s)
    Kit: kit_check.ps1 -Mode validate -> exit 0; -Mode check-drift -> exit 0 (sem deriva)
    Checklist de review: ok (uma linha por item)
      - camadas infracore<-contracts<-services<-plugins: n/a (script standalone, sem imports de camada)
      - ACL/dependência externa: n/a (só stdlib subprocess/argparse/pathlib)
      - MVVM/Qt/UI thread/sinais: n/a (não é código de aplicação)
      - mirror discipline: n/a (nenhum tipo cruzando camadas)
      - teste deletado às cegas: ok, nenhum teste deletado
      - decision record: ok, materializa GOVERNANCA.md §4.4 (V2K-T14), não introduz decisão nova
    ```
  - Consumo: 26 tool uses, ~87k tokens, Sonnet, ~1h56m (medido pela notificação de conclusão;
    duração é relógio de parede do subagente, não tempo de CPU).
- `V2K-T16` — Decisão de residência item a item + ratificação do dono — [Opus + dono] — **done**
  *(`C-12`a; executada **inline**, não delegada: tarefa owner-gated)*
  - Mudou: `docs/RESIDENCIA_DOUTRINA.md` (**novo**) — **36 itens** do `~/.claude/CLAUDE.md` (8
    Regras, 169 linhas medidas) classificados em `global` / `Pantonic` / `dividir`, cada linha
    citando a pergunta ou regra de precedência da régua `GOVERNANCA.md` §3.1 que a produziu.
    Nenhum texto foi movido (é o escopo da `T17`).
  - Ratificação do dono (2026-08-03, `AskUserQuestion`, **1 round-trip**, 4 blocos — método da
    `V2C-T5`): `DR-A` texto normativo no kit + condensado autossuficiente no global (espelho do
    padrão da `V2M-T3`, nunca ponteiro nu); `DR-C` remover do global o número "~≤40 tool uses" —
    o kit (§3, tetos por classe calibrados em 26 registros `Consumo:`) passa a ser a única
    autoridade numérica; `BM-00` descem os dois diferenciais medidos (disciplina concreta de
    coleta → §3; telemetria `Consumo:` medida pela notificação → §4.2); `DR-B` a descida não cita
    skill global (`onboard`, `doc-map`, `memory-diet`, `context-prep`, `lean-test`, `test-tiers`
    não estão nas 9 skills do kit — citá-las nasceria com ponteiro quebrado no consumidor).
  - Checagem de cruzamento com a `V2M-T3` (exigida pelo "pronto quando"): a `V2M-T3` **subiu**
    G-PLANFIDELITY/G-EXECREADY por P1 = sim; nenhum item classificado `Pantonic` aqui responde
    "sim" à P1 ⇒ subida e descida não se cruzam. O item 8.1 registra explicitamente que a `T17`
    **não** pode desfazer a Regra 8.
  - Contradição viva encontrada e endereçada (`DR-C`): global "~≤40 para toda tarefa atômica" ×
    kit "≤30 para redação de doutrina" — hoje um subagente carrega os dois números.
  - Verificação: `Select-String` conta 36 linhas de item na tabela e **0** sem citação da régua;
    `Get-Content` mede 169 linhas / 8 Regras / 28 bullets no global — todos cobertos (as citações
    `CLAUDE.md:30,107` do plano são de 2026-07-29 e envelheceram com a inserção da Regra 8; o
    documento registra o mapeamento atual). `kit_check.ps1 -Mode validate` → exit 0 (9 agentes,
    9 skills, `VERSION == KIT_VERSION 1.4.0`); `-Mode check-drift` → exit 0.
  - Veredito (`guardrails-check`): não aplicável na parte de código — mudança é doutrina/texto,
    sem símbolo de produção, sem suíte pytest (hub segue sem `tests/`), sem piso a mover; itens
    de camadas/ACL/MVVM `n/a`; nenhum teste deletado; decision record = as 4 ratificações acima.
  - Consumo: ~34 tool uses, Opus, execução inline (sem bloco `<usage>` a medir — não há
    autoestimativa de tokens). **Estourou** o teto da classe "redação de doutrina" (≤30): as 5
    edições de correção pós-verificação (contagem de linhas, item sem citação da régua) caberiam
    em um único ato se a verificação tivesse rodado antes da redação final — registrado como
    método a corrigir, não como reclassificação da tarefa.
- `V2K-T17` — Mover o texto e corrigir os ponteiros — [Sonnet] — **done** *(`C-12`b; insumo fechado
  `docs/RESIDENCIA_DOUTRINA.md` §4/§6, 36 itens)*
  - Mudou: `~/.claude/CLAUDE.md` (169→136 linhas; cópia de segurança no scratchpad antes de editar)
    — Regra 3: bullets 3.3-3.6 (git/listagens/arquivos grandes/comandos verbosos) e 3.7
    (varreduras amplas) removidos, substituídos por 1 bullet-ponteiro para `GOVERNANCA.md` §3;
    Regra 4: bullet (a)-(d) (CLAUDE.md ≤200, ATIVO/HISTÓRICO, DOC_MAP, fatos estáveis de agente)
    removido inteiro (dup de §8); Regra 6: item 6.2 reduzido ao ramo de memória + ponteiro para
    §3.1, item 6.8 removido (dup de §3.1); Regra 7: motivo (7.1) cortado ao princípio, caso medido
    só por ponteiro; itens 7.2/7.3 removidos (dup de §3); 7.7 perde o número "~≤40" (mantém só o
    princípio, cita a tabela de tetos do kit — `DR-C`); 7.9 perde a menção literal a "diário"; 7.10
    vira 1 linha, texto completo desce para `GOVERNANCA.md` §4.2. `GOVERNANCA.md` recebe: §3
    (antes de `### 3.1`) 3 bullets novos — economia de contexto (princípio), disciplina de coleta
    condensada, batching de chamadas independentes (`7.4`, item novo no kit); §4.2 (após "Dossiê de
    tarefa aponta e verifica") 2 bullets novos — fechamento enxuto e telemetria medida (bloco
    completo do `7.10`, inclusive o placeholder `Consumo:`); §4.4 (após TF/TR, antes do piso) 1
    parágrafo novo — cadência de testes (Tier 1 ≤2×/tarefa) amarrada ao TDD. `CHANGELOG.md` ganha
    `## [Não lançado]` (seção não existia) com 1 bullet descrevendo o que passou a viajar no kit.
    `.claude/README.md:26` — ponteiro "CLAUDE.md global, Regra 7" (regra do Fable) corrigido para
    "`GOVERNANCA.md` §3". `VERSION`/`.claude/KIT_VERSION` conferidos, ambos `1.4.0`, **não**
    alterados (`DK-9`: bump é só de `T3`/`T19`).
  - Verificação: `Grep` de cada padrão removido contra o global → 0 matches (nenhuma duplicata
    viva); `wc -l ~/.claude/CLAUDE.md` → 136 linhas (era 169; teto 200 preservado com folga);
    `Grep "CLAUDE\.md global, Regra 7"` no repo → só `.claude/agents/pantonic-executor.md:20`
    restante (cita a Regra 7 inteira — batching/cadência/sem-releitura, que ficam no global por
    classificação `nenhuma`/`dividir` — citação válida, não é a divergência corrigida).
  - Achado fora de escopo, não corrigido aqui (tíquete `TK-04` aberto no índice):
    `.claude/agents/pantonic-executor.md:20` ainda hardcoda "orçamento esperado ~≤40 tool uses"
    como teto único — o mesmo número que a `T16` (`DR-C`) mandou remover do global porque o kit
    (`GOVERNANCA.md` §3) já é a única autoridade, com tabela de tetos graduada por classe.
  - Veredito (`guardrails-check`): não aplicável na parte de código — mudança é doutrina/texto
    puro, sem símbolo de produção, sem suíte pytest, sem piso a mover; camadas/ACL/MVVM `n/a`;
    nenhum teste deletado; decision record = as 4 ratificações da `T16` (§6), executadas item a
    item, sem acréscimo nem omissão.
  - Consumo: NÃO MEDIDO — placeholder expirado (sessão que executou `T17` encerrada antes do
    preenchimento; retomada em contexto novo sem notificação disponível).
- `V2K-T18` — Formato e arquivo da série de telemetria (`docs/telemetria.tsv`) — [Sonnet] — **done** *(`C-13`a)*
  - Resultado: `docs/telemetria.tsv` (novo) — TSV append-only, colunas `data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte`
    (`fonte` ∈ `{usage, contado, nao_medido}`, DK-8). Semente re-derivada agora (não copiada do
    plano nem do `V2C-T6`): `Grep "^\s*- Consumo:"` deu **5** em `docs/DIARIO_DE_OBRAS.md` e **34**
    em `docs/DIARIO_HISTORICO.md` — **39** linhas de dado, contra os `14`/`26` citados em planos e
    diário anteriores (ambos vencidos pela 2ª condensação de 2026-08-01). Data de cada linha por
    `git blame --date=short` (2 chamadas, uma por arquivo) — 34 linhas do histórico caem no mesmo
    dia (`fa5ce0d2`/`ce551448`, 2026-08-01); as 5 do diário atual seguem não commitadas (blame
    "Not Committed Yet", data de hoje 2026-08-04). `GOVERNANCA.md` (fim da §4.2, após a frase do
    placeholder) ganhou 1 bullet novo — "Fonte estruturada da série" — declarando o TSV como fonte
    agregável sem substituir o bullet `Consumo:` em prosa (isso é escopo da `V2K-T19`).
  - Verificação: `Import-Csv docs\telemetria.tsv -Delimiter "` + "`t" + `"` → 39 linhas de dado, sem
    erro; `Where-Object { -not $_.fonte }` → vazio (nenhuma linha sem fonte). `kit_check.ps1` não
    rodado — nenhum arquivo de `.claude/` tocado nesta tarefa.
  - Fora de escopo respeitado: bullets `Consumo:` existentes no diário/histórico não foram
    reescritos como ponteiro (`V2K-T19`); `VERSION`/`.claude/KIT_VERSION`/tag não tocados.
  - Consumo: 34 tool uses, ~135k tokens, Sonnet, ~7min29s (medido pela notificação de conclusão).
- `V2K-T19` — Escrita da série nos dois pontos de fechamento + bump `1.5.0` — [Sonnet] — **done** *(`C-13`b)*
  - Mudou: `GOVERNANCA.md` §4.2 (2 bullets reescritos — telemetria aponta `docs/telemetria.tsv`,
    fonte única da série); `handover`/`proximo-passo` SKILL.md (linha `Consumo:` vira ponteiro);
    `docs/telemetria.tsv` (+1 linha, backfill `V2K-T18`); `CHANGELOG.md` (`[Não lançado]` fechado
    como `1.5.0`, bullets `T13..T19` + nota de versão); `VERSION`/`.claude/KIT_VERSION` → `1.5.0`.
  - Verificação (rodada pelo orquestrador, saída colada): `Import-Csv docs\telemetria.tsv` → **40**
    linhas (39 + backfill da `T18`); `kit_check.ps1 -Mode validate` → `OK - 9 agente(s) e 9
    skill(s) validados; VERSION == KIT_VERSION ('1.5.0')`, exit 0; `-Mode check-drift` → exit 0;
    `ratchet_piso.py` → `OK - nenhum piso declarado`; `dead_code.py` → `OK - 0 achado(s)`.
  - Ressalva de execução: o subagente delegado reportou parada sem edições, mas as edições estavam
    no working tree e conferem com o dossiê verbatim — revisadas hunk a hunk pelo orquestrador
    antes do commit; a medida `<usage>` daquele agente é piso, não o custo real da tarefa.
  - Consumo: ver `docs/telemetria.tsv`

### Estágio 4 — `P-0729-v2-documentacao` [superseded em 2026-08-05 — `T1..T4` entregues e de pé; `T5` reprovada, `T6` cancelada por absorção. Substituído por `docs/plans/P-0730-v2-identidade.md` (classificação B: a premissa que o sustentava caiu)]

- `V2D-T1` — `docs/DOC_MAP.md` do hub — [Opus, inline] — **done** *(premissa caída — o mapa já
  existia)*
  - Achado: o objetivo da tarefa afirmava "o hub nunca teve DOC_MAP". Falso desde a `V2K-T6`
    (commit `fa5ce0d`), que criou `docs/DOC_MAP.md`; a `ce55144` já o havia atualizado na 2ª
    condensação. O plano do Estágio 4 foi escrito em 2026-07-29, antes do Bloco C.
  - Verificação da premissa (sondas baratas, antes de qualquer edição): medição de linhas dos
    `*.md` do hub → exatamente 5 docs > 500 linhas (`DIARIO_HISTORICO` 970,
    `P-0725-hub-unico` 669, `RELATORIO_CONSOLIDADO` 636, `P-0729-v2-melhoria-candidatos` 526,
    `P-0721` 524), **todos com entrada no mapa** — cobertura completa, nenhum órfão; `Grep
    "^#{1,3} "` nos 5 arquivos → **todas** as âncoras listadas batem com cabeçalho real (nenhuma
    adivinhada); `docs/DOC_MAP.md` = 5262 bytes, dentro do teto de ~8000 da skill `doc-map`.
  - Mudou (só o delta de desatualização): `docs/DOC_MAP.md` — tamanhos das 5 entradas
    reancorados na medição de 2026-08-05 e marcados como ordem de grandeza datada, não âncora;
    `P-0729-v2-melhoria-candidatos` reclassificado de `in progress` para `done (20/20)` com
    "quando consultar" reescrito para uso post-mortem; linha de docs abaixo do limiar corrigida
    (`GOVERNANCA.md` está na **raiz**, não em `docs/`; `ARQUITETURA_PANTONICA.md`,
    `RESIDENCIA_DOUTRINA.md` e `benchmark/CANDIDATOS.md` nomeados).
  - Aceitação da skill `doc-map` item "CLAUDE.md do projeto referencia o DOC_MAP": satisfeita pela
    residência equivalente do hub — o hub não tem `CLAUDE.md` de projeto por desenho (doutrina
    repatriada na `V2K-T17`), e a obrigatoriedade está em `GOVERNANCA.md:470` (§8) + nos fatos
    estáveis de `pantonic-scout`/`pantonic-executor`/`pantonic-planner`.
  - Consumo: ver `docs/telemetria.tsv`
- `V2D-T2` — Redigir o `README.md` espelho — [Opus] — **in review** *(2ª rodada, 2026-08-05)*
  - **2ª rodada (2026-08-05):** `README.md` reescrito como **proxy das implementações** — **752
    linhas**, **15 seções**, cada uma com `> Fonte da verdade:` apontando arquivo existente;
    `check-readme.ps1` passa a localizar "Anatomia do kit" e "Os guardrails" **pelo título**, não
    pelo número. Verificação: `pwsh -File .claude/checks/check-readme.ps1` → `OK - 9 agente(s),
    9 skill(s), 14 guardrail(s), versão '2.0.0', 15 seção(ões)`, exit 0. Decisões de redação e
    ambiguidades: plano §`Achados da execução` → `T2 — 2026-08-05 (2ª rodada)`. Nada commitado.
  - Consumo: ver `docs/telemetria.tsv` (linha `V2D-T2r2`)
  - **1ª rodada (2026-08-05, premissa caída — documento de adoção):**
    Entregue: `README.md` na raiz (novo, **527 linhas**, dentro da faixa 400-550 do plano §1), as
    13 seções na ordem prescrita, cada uma abrindo com `> Fonte da verdade:` — os 12 arquivos
    citados no README existem (conferidos um a um por `test -e`).
  - Premissas re-sondadas antes de escrever (padrão herdado da `V2D-T1`): `README.md` **não**
    existia (premissa do plano vale); `VERSION` = `.claude/KIT_VERSION` = **`1.5.0`** — o §12 cita
    `1.5.0`, **não** `2.0.0`, porque o bump é da `V2D-T4` e a `DD-5` o condiciona a haver mudança
    que exija ação do consumidor; **9 agentes** + **9 skills**; **14 guardrails** em
    `GOVERNANCA.md` §7; **5 premissas** em §1.
  - Evidência medida do §11 (ADR) confirmada na fonte antes de escrever, sem cifra inventada:
    executor em Opus com **71 turnos / ~189k** (`GOVERNANCA.md` §3); **~300 linhas** de código
    morto testado = `dehydrate_subtitles.py` 174 l + `seed_prototype.py` 127 l
    (`P-0722-governanca-guardrails-anti-saga.md:41`); as **três** premissas de plataforma caídas,
    incluindo o symlink que exige privilégio elevado no Windows (`GOVERNANCA.md` §3); auto-relato
    ~90k contra ~140k reais (§4.2); recalibração ≤25 → ≤30 pela série (§3).
  - Aceite verificado por comando: 13 linhas `Fonte da verdade` = 13 headings `## `; zero remissão
    do tipo "veja/leia o documento X" no corpo (grep vazio); §10 e §13 com afirmações
    desfavoráveis reais (não-CI/CD, um único consumidor, não validado fora de desktop/Qt, scripts
    só exercitados no Windows) e **duas** perguntas do §13 cuja resposta é "não adote" (Q2 e Q6);
    §6 com diagrama `mermaid` + a `T15` real do `P-0729-v2-melhoria-candidatos` como exemplo de
    tarefa atômica; §12 com a regra anti-drift (doutrina edita-se na fonte e **desce** para o
    espelho).
  - Repositório é público: varredura explícita por segredo/credencial/caminho local sensível no
    README — **nada** (o caminho do Skillstore que aparece em `.claude/README.md` foi
    deliberadamente omitido do espelho).
  - Consumo: ver `docs/telemetria.tsv`
- `V2D-T3` — Guarda executável de drift do espelho — [Sonnet] — **done** *(2026-08-05)*
  - Entregue: `.claude/checks/check-readme.ps1` (novo, `-Root` com o mesmo desenho de
    `-KitRoot`/`--root` dos checks irmãos) com as 5 checagens mecânicas — agentes/skills do
    README §7 nos dois sentidos contra `.claude/agents/`/`.claude/skills/`; versão do README
    (cabeçalho e §12) igual a `VERSION` e a `.claude/KIT_VERSION`; guardrails da tabela do README
    §8 == itens numerados de `GOVERNANCA.md` §7; toda seção `## ` do README com
    `> Fonte da verdade:` apontando para arquivo existente. `.claude/skills/guardrails-check/SKILL.md`
    ganhou o item 8 (condicional, mesmo molde do item 5: "projeto que tem `check-readme.ps1`") e a
    linha `Espelho:` no template de Veredito.
  - Achado de implementação (resolvido inline, dentro do escopo): parâmetro `[string[]]`
    `Mandatory` em PowerShell rejeita array contendo elemento `""` (linha em branco do README) —
    o mesmo padrão que `kit_check.ps1 Set-MarkedRegion -NewBody` já resolvia com
    `[AllowEmptyString()]`; aplicado à função interna `Get-SectionLines`.
  - Verificação 1 — estado corrente, `pwsh .claude/checks/check-readme.ps1`:
    ```
    check-readme: OK - 9 agente(s), 9 skill(s), 14 guardrail(s), versão '1.5.0', 13 seção(ões) com Fonte da verdade válida.
    ```
    exit 0.
  - Verificação 2 — drift, fixture sintética no scratchpad (repo mínimo copiado, repo real nunca
    tocado): agente `pantonic-fake-agent.md` adicionado sem atualizar o README da fixture,
    `check-readme.ps1 -Root <fixture>`:
    ```
    check-readme: FALHOU (1 problema(s))
      - Agente 'pantonic-fake-agent' (.claude/agents/pantonic-fake-agent.md) não aparece na tabela de Agentes do README §7.
    ```
    exit 1.
  - Guardrails-check (itens 5-7, kit agêntico): `kit_check.ps1 -Mode validate` → `OK - 9 agente(s)
    e 9 skill(s) validados; VERSION == KIT_VERSION ('1.5.0')`; `-Mode check-drift` → `OK`;
    `dead_code.py` → `OK - 0 achado(s)`; `ratchet_piso.py` → `OK - nenhum piso declarado`. Todos
    exit 0.
  - Não commitado (árvore de trabalho já carregava mudanças não commitadas da `V2D-T2`); `README.md`,
    `VERSION`, `.claude/KIT_VERSION`, `CHANGELOG.md` não tocados — bump é da `V2D-T4`.
  - Consumo: ver `docs/telemetria.tsv` — **estouro de orçamento** (teto 30, medido 57 tool uses):
    causa declarada pelo executor é obstáculo técnico não previsto (gotcha do `[string[]] Mandatory`
    com elemento `""`, isolado por bisseção) + bloqueio de sandbox em `Copy-Item -Recurse` sobre
    `.claude/skills/*` ao montar a fixture, que forçou reconstrução diretório a diretório.
- `V2D-T4` — Fechar a versão `2.0.0` (CHANGELOG + tag) e **distribuir** — [Sonnet] — **done** *(2026-08-05; `git push` e migração do `PantonicVideo` fora de escopo por decisão do dono)*
- `V2D-T5` — Teste de aceitação do README pelo dono (utilidade + fidelidade) — [dono] — **reprovada** *(2026-08-05)*: a leitura do dono achou desvio de identidade na **fonte da verdade**, não no espelho — ver `P-0730` §0/§2
- `V2D-T6` — Fechar a `2.0.1` do espelho reescrito (`DD-7`) — [Sonnet] — **cancelled** *(absorvida pela `V2I-T13`, que fecha `2.1.0` — `DR-6`)*

**Notas de execução:** a `V2D-T1` expôs um efeito de plano longo — o Estágio 4 foi planejado em
2026-07-29 e afirma estados de repositório que os Estágios 3A/3B mudaram. Antes de delegar
`V2D-T2`/`V2D-T3`, verificar por sonda barata as afirmações de estado dos dossiês (ex.: "`README.md`
hoje inexistente", contagens de agentes/skills do §7, número de guardrails do §8) — o padrão é o
mesmo da `V2D-T1`, não um caso isolado.

### Estágio 5 — `P-0730-v2-identidade` [in progress — 3/16; aberto em 2026-08-05]

**Objetivo:** corrigir a identidade declarada do framework na fonte da verdade e elevar o README a
documento canônico. O PantonicApp é **agnóstico a tecnologia e plataforma**, atua nos níveis de
**arquitetura** e de **projeto**, sobre **clean architecture + DDD**, estendidos pelo **infracore**
(hoje ainda preso ao PySide6) e por **plugins — um plugin responde por um caso de uso**. PySide6/
MVVM/desktop passam a ser **perfil do case de referência**, não premissa (`DR-1`/`DR-2`).

**Dossiê completo (11 desvios medidos, decisões `DR-1..DR-7`, tarefas `V2I-T1..T15`, riscos e
reconciliação):** `docs/plans/P-0730-v2-identidade.md`. Sequência linear `T1→T15`; `T3..T7` e `T11`
são doutrina/redação canônica [Opus], `T8..T10` e `T13..T14` propagação e medida [Sonnet], `T12` é
o aceite do dono e **bloqueia** o fechamento da versão.

**Revisão de escopo em 2026-08-05 (decisão do dono):** tarefa nova **`V2I-T11b` — glossário do
framework no README**, posicionada **entre a `T11` e a `T12`** (escrita sobre o README já reescrito
e antes do aceite do dono, que é onde a inteligibilidade do vocabulário é julgada). Escopo em três
eixos: jargão de arquitetura, de projeto e **de metadados do framework** (`kit`, `hub`, `drift`,
`estágio` — eixo destacado pelo dono). Plano passa a **16 tarefas**; dossiê fechado e ordem de
execução vigente em `docs/plans/P-0730-v2-identidade.md` §8. `T1`..`T10` não foram afetadas.

**Fecha em `2.1.0`** (`DR-6`, absorve a `V2D-T6`). A abstração do infracore (`DR-5`) **não** entra
neste estágio: nasce como `P-0731`, autorado já fechado pela `V2I-T15`, com o achado da `V2I-T14`
como insumo. Achado do planejamento: `TK-05`.
