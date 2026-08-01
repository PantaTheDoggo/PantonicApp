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
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking (T1..T19; 11/19) | in progress | `docs/plans/P-0729-v2-melhoria-candidatos.md` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T5) | blocked | `docs/plans/P-0729-v2-documentacao.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |
| TK-01 | Corrigir residência de `modelo-por-fase` em `GOVERNANCA.md` §3 e no bullet `V2M-T1` do `CHANGELOG.md` (ainda apontam `~/.claude/skills/`, superado por `DM-7`) | done *(absorvido pela `V2M-T3`)* | `docs/DIARIO_HISTORICO.md#tíquetes-avulsos--condensado-em-2026-08-01` |
| TK-02 | `.claude/sync-kit.ps1`: `Get-ExcludedKeys`/`Test-Excluded` quebram sem `kit-exclude.txt` presente (achado pré-existente, `V2K-T11`) | done | `## Tíquetes avulsos` |

---

## Tíquetes avulsos

- `TK-02` — **backlog.** Achado fora de escopo (`V2K-T11`, 2026-08-01, durante a montagem do
  sandbox de verificação): `.claude/sync-kit.ps1`, funções `Get-ExcludedKeys` e `Test-Excluded`.
  `Get-ExcludedKeys` devolve a `HashSet[string]` via `return $excluded` (sem `,` nem
  `-NoEnumerate`); o pipeline do PowerShell **enumera** a coleção antes de sair da função, então
  quando o conjunto está vazio (`kit-exclude.txt` ausente ou sem entradas válidas) o chamador
  recebe `$null`, e `Test-Excluded` quebra com "You cannot call a method on a null-valued
  expression" na primeira chamada de `.Contains()`. Reproduzido tanto na versão editada por esta
  tarefa quanto na versão **original** (pré-`V2K-T11`, via `git show HEAD:.claude/sync-kit.ps1`
  antes desta tarefa) — isola que é pré-existente, não introduzido aqui. **Impacto atual:** o hub
  não tem `.claude/kit-exclude.txt` nem em `.claude/` nem na raiz hoje — rodar
  `.claude/sync-kit.ps1` (com ou sem `-Check`) no estado atual do repo quebra antes de
  copiar/comparar qualquer artefato. Correção sugerida (não aplicada aqui — fora do escopo desta
  tarefa): trocar os dois `return $excluded` por `return ,$excluded` (ou
  `Write-Output $excluded -NoEnumerate`) para impedir o achatamento pelo pipeline.
  - **Promovido a tarefa da vez em 2026-08-01** (decisão do dono, aberta pela `proximo-passo` ao
    escolher a `V2K-T12`): corrigido **antes e sozinho**, em contexto próprio e com alvo único,
    porque a `V2K-T12` verifica executando o `sync-kit.ps1` e o exige funcional. Descartados o
    contorno de sandbox (repetir o `kit-exclude.txt` sintético da `V2K-T11`) e a correção
    embutida na `V2K-T12` (viraria segundo alvo no gate de delegação).
  - **Nota de estado:** só uma das duas funções tem `return $excluded` na forma achatada
    (`sync-kit.ps1:86` e `:101`, os dois `return` de `Get-ExcludedKeys`); `Test-Excluded`
    (`:104-111`) é a **vítima**, não a origem — não precisa de edição, quebra porque recebe
    `$null`. Verificação de pronto: rodar `.claude/sync-kit.ps1 -Check` num sandbox **sem**
    `kit-exclude.txt` e obter saída normal em vez de "You cannot call a method on a null-valued
    expression".
  - **Fechamento (2026-08-01, done):** trocados os dois `return $excluded` por `return ,$excluded`
    em `.claude/sync-kit.ps1:86` e `.claude/sync-kit.ps1:101` (vírgula de array-wrap, impede o
    achatamento do `HashSet[string]` pelo pipeline). `Test-Excluded` (`:104-111`) não foi tocado —
    era a vítima, não a origem. Verificação: sandbox montado em
    `.claude/kit/sync-kit.ps1` + `.claude/kit/skills/dummy/` + `.claude/kit/agents/dummy-agent.md`,
    **sem** `.claude/kit-exclude.txt`, rodando `sync-kit.ps1 -Check`. Saída real:
    > WARN: sync-kit - origin commit \<unresolved: no commit found for this kit path, git missing,
    > or not a git repo\> is not signature-verified (git verify-commit failed or unavailable).
    > Proceeding without signature verification. Re-run with -RequireSignature to enforce.
    > sync-kit -Check: 2 managed artifact(s) diverge from the kit:
    >   - skills/dummy
    >   - agents/dummy-agent
    >
    > EXITCODE=1
    Sem o erro "You cannot call a method on a null-valued expression" — o `-Check` reporta
    divergência normalmente (exit 1 é o comportamento esperado de divergência, não de crash).
    Consumo: 18 tool uses, ~61k tokens, Sonnet, ~6min09s.

---

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0`.

**Próxima tarefa da sprint:** `V2K-T12` — Registro de consumidores e versões instaladas
(`docs/CONSUMIDORES.md`, `C-09`), oitava tarefa do Bloco C — **[Sonnet]** —
`docs/plans/P-0729-v2-melhoria-candidatos.md` (§T12), **ficha reescrita fechada em 2026-08-01**
sob `DK-12`. A ficha original dizia "quem escreve é o `sync-kit.ps1`, no mesmo passo que aplica a
versão" — três fatos medidos na abertura desta rodada contradizem isso: o script roda de
`<child>/.claude/kit/` com raízes vindas de `$PSScriptRoot` (`sync-kit.ps1:7-14,74-75`) e não tem
handle da árvore do hub; ele **não tem** passo que aplique versão (zero referências a
`KIT_VERSION`; só `Copy-Item` em `:244,:336`); e **0/6 consumidores** têm `.claude/kit/` ou
`KIT_VERSION` (5/6 nem são repositórios git). Rota escolhida pelo dono: **carimbo no consumidor
(`SYNC_STATE`, escrito pelo `sync-kit.ps1`) + coletor no hub (`kit_check.ps1 -Mode consumers`)**.
**Contagem de write-clusters já derivada (não re-derivar): 8** — `sync-kit.ps1` 3, `kit_check.ps1`
3, `docs/CONSUMIDORES.md` 1, `GOVERNANCA.md` §10 1. Está **no limite** do gate de delegação;
avaliar partir em duas sub-tarefas (carimbo × registro+coletor+§10) antes de despachar. **Pré-
requisito resolvido em 2026-08-01:** o `TK-02` (achatamento de `Get-ExcludedKeys` em
`.claude/sync-kit.ps1`) foi corrigido antes e sozinho, porque a `V2K-T12` verifica executando o
script e o exige funcional — ver nota de fechamento em `## Tíquetes avulsos`.

**Depois dela:** `V2K-T13` — Compatibilidade por major entre kit e consumidor (`C-14`) — **[Sonnet]**
— `docs/plans/P-0729-v2-melhoria-candidatos.md` (§T13). Arquivos-alvo: `.claude/skills/
checar-versao-kit/SKILL.md`; `GOVERNANCA.md` §10 (uma linha). Divergência de **MAJOR** entre kit e
consumidor deixa de ser tratada como divergência comum: três casos distinguidos na saída da skill
— igual (silêncio) · MINOR/PATCH divergente (reportar, como hoje) · MAJOR divergente (reportar
como incompatível e parar). A regra do §10a é preservada: o agente reporta, nunca atualiza.
Verificação: no scratchpad, um `.claude/kit/KIT_VERSION` sintético com MAJOR diferente produz a
mensagem de incompatibilidade; com MINOR diferente, a mensagem antiga; igual, silêncio.

**Decisão do dono resolvida em 2026-08-01** (aberta pela `V2K-T9`, precedia a `V2K-T10`): a
primeira aplicação do gatilho mediu que a pergunta de `DK-5` não distingue *regra morta* de *regra
preventiva que ninguém violou*. Escolha do dono entre 4 opções: **isenção por enforcement
executável** — guardrail com check executável ativo **e nomeado** sai da pergunta, porque o check
verde é a evidência de vida; a pergunta vale só para regra advisória/procedimental. Aplicada no
mesmo ato (`GOVERNANCA.md` §7.1 + `DK-5a` no plano); ACL, egress G6 e namespace de estado ficam
**isentos** com os checks nomeados e verificados verdes no `PantonicVideo`. Rodada `1.4.0` fecha em
**0 marcações**, agora como resultado final e não retenção.

**Planejamento da campanha: feito em 2026-07-30 [Opus].** O plano nasceu **fechado** (gate de
publicação, `G-PLANREADY` item 5) com 6 decisões: **DL-1** achado comprovadamente vivo → tornar o
código honesto (nunca allowlist, nunca 4ª rodada; se exigir mudança de desenho, o executor PARA e
escala); **DL-2** apagar `tools/integration_agent/` (5 stubs `NotImplementedError`, sem o teste que
o `ARCHITECTURE.md` promete) + os docs que o descrevem, seguindo o precedente `D-FC09-1`;
**DL-3** apagar as 2 POCs já absorvidas em `integrations/poc/`; **DL-4** `SPRINT-BACKUP` parqueada
em `blocked` (gate T6 é do dono) e a campanha vira a iniciativa ativa do `PantonicVideo`, WIP=1
preservado; **DL-5** o piso de regressão cai por deleção **nominal** de teste (a campanha apaga
teste de propósito — é o alvo do `G-DEADCODE`), nunca em silêncio; **DL-6** os deltas por tarefa são
expectativa, não promessa (as 3 estimativas anteriores erraram para menos). Três sondas feitas no
planejamento mudaram o quadro antes de virar tarefa: `infracore/ui_shell/resources_rc.py` é gerado
**e nunca importado** (pipeline `.qrc` morto inteiro, não 2 símbolos); os 5 achados de
`tools/integration_agent` são stubs sem teste algum; e **não existe `.ui` nem `.qml` no repo** — as
15 properties de `view_model.py` não têm binding declarativo que as sustente.

A `V2M-T5` esgotou o que era decidível
dentro do PantonicApp: as três rodadas de ajuste do check rodaram (baseline do `PantonicVideo`
412 → 131 → 95 → **86**, 2026-07-30) e **não há 4ª rodada** (decisão do dono, definitiva). Como o
fecho da T5 é por **gate bloqueante** (`exit 0`, allowlist descartada), ela depende dessa campanha.
**Decisão do dono, 2026-07-30:** abrir a campanha **agora**, com a `PANTONIC-V2` parada até ela
concluir — a alternativa de liberar o Bloco C em paralelo (exceção à DK-1) e a de rever o gate de
fecho foram **descartadas**. Consequência aceita: os 86 achados entram no caminho crítico da
iniciativa e precisam ser triados um a um (órfão real × categoria de despacho ainda não nomeada),
em prazo desconhecido. A ordem DK-1 permanece **sem exceção**: Bloco A → Estágio 3A **inteiro** →
Bloco C → Estágio 4. Estágio 3A fechado (5/5).
**Destravada:** `V2M-T4` fechou em
2026-07-30 (contador sequencial de planos materializado, `_INBOX.md` com próximo id `P-0730`). O
**Bloco B abriu em 2026-07-30** com a `V2M-T1` (§7 em 13 guardrails + gate de publicação + os
três artefatos do kit + `1.4.0`) e seguiu com a `V2M-T2` em 2026-07-30 (skill `modelo-por-fase` no
kit — 9ª skill — + carve-out do falso positivo do hook global; sem bump, o Bloco B inteiro é a
release `1.4.0`, tag recriada sobre o commit novo). O **Bloco A fechou em 2026-07-30** (4/4:
`V2K-T1..T3` = enforcement do kit como código pendurado no gate; `V2K-T4` = régua de residência da
doutrina em `GOVERNANCA.md` §3.1, com os três casos em disputa resolvidos por escrito).
A ordem entre os dois planos do Estágio 3 é **normativa** (DK-1, §2
daquele plano) e não é escolha da `proximo-passo`: **Bloco A** = `V2K-T1..T4` (enforcement
executável do kit + régua de residência da doutrina) → **Bloco B** = Estágio 3A inteiro
(`V2M-T1..T5`, com `V2M-T3` depois de `V2K-T4`) → **Bloco C** = `V2K-T5..T19` → **Estágio 4**.
Motivo: `C-01` é precondição declarada (enforcement vira código antes de qualquer adição textual) e
`C-03` é a régua de residência de que a própria `V2M-T3` depende; o resto evita conflito de edição
em `GOVERNANCA.md` §3/§7.
O **Estágio 1 fechou em 2026-07-29** (9/9) e o **Estágio 2 fechou em 2026-07-29** (6/6) —
`V2C-T1` auto-retrato + `V2C-T2` matriz + `V2C-T3` consolidado + `V2C-T4` candidatos +
`V2C-T5` ratificação + `V2C-T6` autoria do plano 3B.

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

### Estágio 3B — `P-0729-v2-melhoria-candidatos` [in progress — 11/19 (Bloco A fechado, Bloco C em andamento), nascido fechado em 2026-07-29 pela `V2C-T6`]

19 tarefas, cada uma com o `C-NN` de origem. Ordem normativa em `docs/plans/P-0729-v2-melhoria-candidatos.md`
§2 — **Bloco A** (`T1..T4`) antes do Estágio 3A; **Bloco C** (`T5..T19`) depois dele.

**Bloco A — enforcement executável e régua de residência**
- `V2K-T1` — Validador estrutural do kit (`.claude/checks/kit_check.ps1 -Mode validate`) — [Sonnet] — done *(`C-01`a)*
  - Resultado: `.claude/checks/kit_check.ps1` criado com `-Mode validate` (parâmetro já aceita `generate`/`check-drift`, não implementados — reservados p/ `V2K-T2`). Valida: frontmatter `name`+`description` de cada `.claude/agents/*.md` (`tools` opcional e só sintático, por causa de `pantonic-executor.md` sem essa linha); frontmatter `name`+`description` de cada `.claude/skills/*/SKILL.md` com `name` == diretório; paridade `VERSION` == `.claude/KIT_VERSION`. Execução real: exit 0, "kit_check: OK - 9 agente(s) e 8 skill(s) validados; VERSION == KIT_VERSION ('1.2.0')." Execução negativa (cópia sintética no scratchpad, agente sem `description`): exit 1, "Agente sem campo 'description' no frontmatter: ...\kit_copy_v2kt1\.claude\agents\synthetic-bad.md" — cópia removida após o teste.
  - Veredito: suítes — não aplicável (hub sem pytest/app Python); piso de regressão — sem mudança (nenhum teste existente tocado).
  - Consumo: 17 tool uses, ~55k tokens, Sonnet, ~36min (medido no `<usage>` da notificação; teto informado era 15 — estouro de 2, reportado pelo executor: 5 chamadas de exploração de frontmatter porque o dossiê citou `executor.md` em vez de `pantonic-executor.md`).
- `V2K-T2` — Gerador do `.claude/README.md` + detecção de deriva — [Sonnet] — done *(`C-01`b; defeito medido: 8/9 agentes, 6/8 skills)*
  - Resultado: `kit_check.ps1` ganhou `-Mode generate` e `-Mode check-drift` (dispatch real substituindo o stub `if ($Mode -ne 'validate') { exit 1 }` da `V2K-T1`); reutiliza `Get-Frontmatter`/`Get-FieldValue`. `.claude/README.md` ganhou marcadores `<!-- kit:agents:begin/end -->` e `<!-- kit:skills:begin/end -->`; `generate` reescreve só o conteúdo entre marcadores (ordem alfabética por nome de arquivo/diretório — determinística), prosa fora deles intacta; `generate`/`check-drift` falham com `throw` nomeando o marcador ausente/desbalanceado. Nuance do `pantonic-planner` (Fable só sob pedido explícito): opção (a) — coluna "Modelo" passa a derivar só do frontmatter (`Opus`); a ressalva foi movida para uma nota em prosa logo após `kit:agents:end`, fora da região gerada.
  - Achado durante a implementação (não hipótese, corrigido nesta mesma tarefa, sem tíquete): `[Parameter(Mandatory)][string[]]` sem `[AllowEmptyString()]` rejeita com erro enganoso ("Cannot bind argument ... because it is an empty string") qualquer array contendo uma linha em branco — afeta `$Content`/`$NewBody` de `Set-MarkedRegion` porque o README tem linhas em branco. Corrigido adicionando `[AllowEmptyString()]` aos dois parâmetros. Também trocado `Compare-Object -SyncWindow 0` (diff posicional, cascata de ruído após a linha inserida) por `Compare-Object` padrão (diff por conteúdo) em `check-drift`, para a mensagem nomear só a(s) linha(s) que realmente mudou(aram).
  - Verificação executada: (1) `-Mode validate` exit 0; (2) `-Mode generate` → README com 9 linhas de agente + 8 de skill, exit 0; (3) `-Mode check-drift` exit 0 (versionado == regenerado); (4) agente sintético `zzz-synthetic-drift-test.md` criado → `check-drift` exit 1 nomeando a linha divergente (`| \`zzz-synthetic-drift-test\` | Sonnet | ... |`) → sintético removido → `check-drift` exit 0 e `validate` exit 0 de novo.
  - Veredito: suítes — não aplicável (hub sem pytest/app Python); piso de regressão — sem mudança (item 1 da verificação é a regressão relevante da `V2K-T1`, permanece exit 0).
  - Consumo: 33 tool uses, ~101k tokens, Sonnet, ~407min de relógio (medido no `<usage>` da notificação; teto informado era 30 — estouro de 3, reportado pelo próprio executor: 3 scripts de diagnóstico até isolar a causa raiz do `[AllowEmptyString()]`. A duração de relógio inclui espera fora de execução e não é comparável à da `V2K-T1`).
- `V2K-T3` — Doutrina do enforcement em §9 + entrada no `guardrails-check` + bump `1.3.0` — [Opus] — done *(`C-01`c; fecha o Bloco A de enforcement executável)*
  - Resultado: `GOVERNANCA.md` §9 ganhou o parágrafo **"Enforcement do kit é executável"** com as três frases pedidas — (1) `.claude/README.md` é artefato **derivado** e não se edita à mão; (2) comando canônico `pwsh .claude/checks/kit_check.ps1 -Mode validate` / `-Mode check-drift`; (3) enforcement do kit é **código**, e regra não verificável pelo script nasce com o motivo escrito. No `.claude/skills/guardrails-check/SKILL.md`, os dois modos viraram o **item 5 do checklist executável** (bloqueante como o Tier 2, com `-Mode generate` como única correção legítima de deriva) e o bloco de veredito ganhou a linha `Kit:`. Bump `1.3.0` em `VERSION` e `.claude/KIT_VERSION` (paridade §10) e tag anotada `kit-v1.3.0` criada **sem push**.
  - Desvio autorizado pelo orquestrador: o plano falava em abrir `## [Não lançado]` no `CHANGELOG.md`, mas a mesma tarefa cria a tag — a seção foi aberta como `## 1.3.0 — 2026-07-30`, no estilo das seções `1.2.0`/`1.1.0`, com as três entradas (`V2K-T1`, `V2K-T2`, `V2K-T3`).
  - Verificação executada (outputs reais, **depois** do bump):
    - `pwsh .claude/checks/kit_check.ps1 -Mode validate` → `kit_check: OK - 9 agente(s) e 8 skill(s) validados; VERSION == KIT_VERSION ('1.3.0').` (exit `0`)
    - `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 8 skill(s)).` (exit `0`)
    - `git tag --list 'kit-v*'` → `kit-v1.0.0`, `kit-v1.0.1`, `kit-v1.1.0`, `kit-v1.2.0`, **`kit-v1.3.0`**.
  - ~~Atenção do dono: a tag `kit-v1.3.0` foi criada sobre o `HEAD` atual (`d6ffe0e`), que ainda **não** contém as mudanças do Bloco A.~~ **Resolvido em 2026-07-30** (decisão do dono no fecho da `V2K-T4`): Bloco A commitado em `7ec68d7`, tag `kit-v1.3.0` apagada e recriada sobre esse commit (nunca havia sido publicada, então sem `-f` e sem reescrita de tag remota), e `main` + `kit-v1.1.0`/`1.2.0`/`1.3.0` publicados em `origin` — antes disso o remoto estava 23 commits atrás e só tinha `kit-v1.0.0`/`1.0.1`. As tags `1.1.0` e `1.2.0` foram conferidas no mesmo ato e já apontavam para os commits corretos (`9f51055`, `80a97b4`).
  - Veredito: suítes — não aplicável (hub sem pytest/app Python); gate do kit — `validate` e `check-drift` exit `0`; piso de regressão — sem mudança (os dois modos do `kit_check` são a regressão relevante do Bloco A e permanecem verdes). Nenhum arquivo deletado; `.claude/README.md` e `.claude/checks/kit_check.ps1` não foram tocados (escopo de `T1`/`T2`).
  - Consumo: 18 tool uses, ~49k tokens, Opus, ~3min (medido no `<usage>` da notificação; teto informado era 22 — dentro do teto). O executor autorrelatou "8 tool uses" no handover: subestimativa de ~55% contra o medido — mais um caso do padrão que justifica a telemetria vir da notificação, nunca do auto-relato (Regra 7).
- `V2K-T4` — Tabela de precedência e residência da doutrina (`GOVERNANCA.md` §3) — [Opus] — done *(`C-03`; destrava `T6`, `T10`, `T16` e `V2M-T3`; **fecha o Bloco A**)*
  - Resultado: subseção nova **`### 3.1 Residência e precedência da doutrina`** no fim do `GOVERNANCA.md` §3 (antes do §4), conforme a residência decidida em DK-2 (§3, não §7). Contém: (a) tabela das **quatro superfícies** — CLAUDE.md global · `GOVERNANCA.md`/`ARQUITETURA_PANTONICA.md` · skill · agente — com colunas "mora aqui" / "não mora aqui" / "versionada"; (b) as **duas regras de precedência** (específico vence geral; empate → versionado vence não-versionado, com o achado `BM-00§D15` como motivo: o consumidor por `git subtree` não recebe o que está fora do repo); (c) o **teste de residência em quatro perguntas**, na ordem, com fallback explícito ("nenhuma das quatro → não é doutrina, é estado de trabalho → diário de obras"); (d) a regra de que colisão se resolve apagando/reduzindo a ponteiro a cópia perdedora **no mesmo ato**. Adição fora do pedido literal, decidida na redação: **hook não é uma quinta superfície** — é mecanismo de enforcement de regra que já mora em uma das quatro (fechava uma ambiguidade real, o hook de modelo-por-fase, que a tabela deixaria sem lar).
  - **Nenhum texto foi movido** (mover é `T16`/`T17`): a edição é puramente aditiva no `GOVERNANCA.md`; nem o CLAUDE.md global nem o `~/.claude/docs/GOVERNANCA_MEMORIAS.md` foram tocados.
  - Verificação — a tabela aplicada, no ato, aos três casos hoje em disputa:
    1. **Orçamento de turnos por tarefa** (`~/.claude/CLAUDE.md` Regra 7 × `GOVERNANCA.md:67`, hoje duplicado). Teste: P1 **não** (fala em tarefa atômica, agente de execução, diário de obras — objetos que um projeto não-Pantonic do dono não tem); P2 **sim** → **`GOVERNANCA.md`**. Colisão real (as duas superfícies dizem ~≤40) resolvida pela regra 1, específico vence geral. Consequência: a `T16` remove o bullet de orçamento da Regra 7 global (ou o reduz a ponteiro), e o **teto graduado do `C-04` (`V2K-T6`) nasce em `GOVERNANCA.md` §3, nunca no global**. Partição: os itens genéricos da mesma Regra 7 (batching de chamadas independentes, não reler arquivo editado para conferir) passam P1 e **ficam** no global — a regra desce por item, não por seção inteira.
    2. **Telemetria de consumo medida** (`BM-00§D12`, hoje em `~/.claude/CLAUDE.md:107`). Parte-se em duas: a **regra** ("a fonte é o bloco `<usage>` da notificação, nunca autorrelato; a linha é do orquestrador") falha P1 — só tem efeito onde existem handover e diário de obras — e passa P2 → **`GOVERNANCA.md`**; o **ato de escrever a linha ao fechar a tarefa** é procedimento com gatilho, passa P3 → **skills `handover` e `proximo-passo`**. O global perde as duas partes. Consequência: a `V2K-T13` (`C-13`) põe o arquivo de série + a escrita nas skills, e a regra da fonte na doutrina versionada.
    3. **Governança de memória** (`~/.claude/docs/GOVERNANCA_MEMORIAS.md`). Passa P1 na primeira pergunta — o próprio documento se declara "agnóstica a projeto" e trata de objetos do harness (`~/.claude/projects/<slug>/memory/`, `MEMORY.md`, pastas `.claude` aninhadas), não do framework → **permanece global, não entra no kit**. Não há colisão: a regra 2 (versionado vence) **não dispara**, porque não há empate de especificidade — nenhuma parte disputa a superfície do kit. O único delta Pantonic ("estado de trabalho/pendência → diário de obras, nunca memória") já está coberto pela última linha do teste de residência e **não precisa de cópia**. Consequência — **decidida pelo dono em 2026-07-30, conforme o veredito**: a `V2K-T10` (`C-10`, inbox de memória) é procedimento com gatilho **sobre superfície agnóstica** → P1 antes de P3 ⇒ ela nasce **fora do kit** (`~/.claude` global + skill global), e portanto **não** é distribuída aos consumidores pelo Estágio 4. Custo aceito explicitamente: consumidor em outra máquina ou de outro dono não herda a disciplina de memória — hoje nominal, já que todos os consumidores Pantonic compartilham o mesmo `~/.claude`. Coerente com o estado medido (as skills `memory-diet`, `context-prep`, `onboard`, `doc-map` já vivem fora das 8 skills do kit). Sem exceção aberta na régua na sua primeira aplicação.
    Os três se resolveram sem ambiguidade e sem empate residual — critério de "tabela pronta" do dossiê atendido.
  - Veredito: suítes — não aplicável (hub sem pytest/app Python; tarefa só de doutrina, nenhum código). Gate do kit — `pwsh .claude/checks/kit_check.ps1 -Mode validate` → `kit_check: OK - 9 agente(s) e 8 skill(s) validados; VERSION == KIT_VERSION ('1.3.0').` (exit `0`); `-Mode check-drift` → `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 8 skill(s)).` (exit `0`). Piso de regressão — sem mudança. Sem bump de versão (o `1.3.0` do Bloco A já foi feito na `V2K-T3`; o próximo é `1.4.0` no fim do Bloco C).
  - Consumo: 11 tool uses, ~66k tokens, Opus, ~6min — **execução inline no orquestrador** (tarefa de 1 write-cluster em 1 arquivo + nota; `GOVERNANCA.md` §3 "delegar protege contexto, não reduz consumo": < ~15 turnos estimados ⇒ inline). Não há `<usage>` de subagente; os números são do próprio contexto do orquestrador e estão marcados como tal.

**Bloco C — o resto, por dependência e I÷E**
- `V2K-T5` — Allowlist de subcomandos destrutivos (`.claude/settings.json` + §7) — [Sonnet] — done *(`C-02`)*
  - Resultado: `.claude/settings.json` criado (o hub não tinha nenhum `settings*.json`) com
    `permissions.deny` contendo os 6 padrões fechados no plano: `Bash(git push --force*)`,
    `Bash(git push -f*)`, `Bash(git reset --hard*)`, `Bash(git branch -D*)`,
    `Bash(git clean -fdx*)`, `Bash(gh repo delete*)`. `GOVERNANCA.md` §7 ganhou o item **14**
    ("Allowlist de subcomandos destrutivos"), inserido depois do item 13 (`G-EXECREADY`) e antes
    do parágrafo de fechamento "Esses guardrails são materializados...", com o texto de doutrina
    (DK-3) transcrito verbatim e um *Enforcement:* citando o `permissions.deny` e os 6 padrões.
  - Verificação executada: `Get-Content .claude/settings.json -Raw | ConvertFrom-Json` não lançou
    erro (JSON válido, os 6 padrões presentes). Tentativa real `git branch -D nao-existe-xyz` via
    Bash tool → **"Permission to use Bash with command git branch -D nao-existe-xyz has been
    denied."** — negado pelo permission system antes de qualquer tentativa de execução do git,
    confirmando que a allowlist intercepta.
  - Veredito: suítes/conformance — não aplicável (tarefa não toca código de produção, só
    `.claude/settings.json` e `GOVERNANCA.md`, padrão já usado em `V2B-T3`); piso de regressão —
    sem mudança.
  - Achados da execução: nenhum achado fora de escopo.
  - Consumo: 21 tool uses, ~65k tokens, Sonnet, ~6,6 min (medido no `<usage>` da notificação).
    Dentro do orçamento (~≤40 tool uses) — primeira tarefa da série recente sem estouro de teto.
- `V2K-T6` — Teto de contexto graduado por classe de tarefa — [Opus] — done *(`C-04`; destrava `T7`)*
  - Resultado: em `GOVERNANCA.md` §3, o bullet **"Orçamento de turnos por tarefa atômica"** (teto
    único ~≤40) foi **substituído** — não duplicado — pela tabela de 5 classes com teto próprio:
    mecânica/pontual **≤15** · implementação padrão **≤40** · comportamental multi-camada **≤60**
    (com teto numérico por ramo obrigatório no dossiê) · investigação/mapeamento **sem default**
    (teto prescrito no dossiê junto do método de sondagem) · redação de doutrina/planejamento
    **≤30**. A regra anti-desculpa entrou verbatim: classe escolhida **no dossiê, antes de
    delegar**; estourar = replanejar, não continuar; classe generosa escolhida depois do estouro é
    falsificação da série.
  - **Correção da série sobre a estimativa (autorizada por DK-4, "a verificação retroativa da `T6`
    pode corrigir os números, e aí manda a série"):** a classe de redação de doutrina nasceria em
    **≤25** e foi para **≤30**. Em ≤25 ela estourava em **5 das 7** tarefas medidas (71%), muito
    acima do critério de aceite de ⅓; em ≤30, **2 das 7** (29%). Nenhuma outra classe mudou.
  - **Números re-derivados no pickup (o plano estava vencido nos dois):** a linha a substituir é a
    **74**, não a 67 (`GOVERNANCA.md` cresceu com `V2M-T1` e `V2K-T5`); e a série tem **26**
    registros `Consumo:` (5 em `DIARIO_DE_OBRAS.md` + 21 em `DIARIO_HISTORICO.md`), não as 14 de
    2026-07-29 — a condensação de 2026-08-01 moveu o grosso da série para o histórico.
  - Verificação — aplicação retroativa das 5 classes às tarefas com `Consumo:` medido:
    - **Mecânica ≤15** — `V2B-T1` 13, `V2C-T5` 12. **0/2 estouros.**
    - **Implementação padrão ≤40** — `V2B-T2` 20, `V2B-T3` 24, `V2B-T8` **67**✗, `V2B-T9` **49**✗,
      `V2C-T2` 32, `V2M-T2` 25, `V2M-T3` 29, `V2M-T4` 24, `V2K-T1` 17, `V2K-T2` 33, `V2K-T5` 21.
      **2/11 (18%)** — dentro de ⅓.
    - **Comportamental multi-camada ≤60** — só `V2M-T5`: rodadas de 41, 31 e 33 tool uses,
      **0 estouros por rodada**. Achado registrado abaixo.
    - **Investigação/mapeamento** — `V2B-T4..T7` (coletores Haiku): banda medida **23-28 tool uses
      por coletor**. Sem default por desenho, então não há estouro possível; a banda fica como
      referência para prescrever o teto no dossiê.
    - **Redação de doutrina/planejamento ≤30** — `V2K-T4` 11, `V2K-T3` 18, `V2C-T1` 28, `V2C-T4` 28,
      `V2C-T6` ~28, `V2C-T3` **37**✗, `V2M-T1` ~**40**✗ (autoestimativa). **2/7 (29%)** — dentro
      de ⅓ **só** com o teto corrigido para 30.
  - Achado da verificação (não vira texto de doutrina nesta tarefa; insumo para a `T7`): a
    `V2M-T5` cabia no teto **por rodada** e ainda assim somou **~145 tool uses em 4 rodadas**. O
    teto por ramo funciona como alarme local, mas o **acumulado** da tarefa é o sinal de
    decomposição errada e hoje não tem gatilho — é exatamente a lacuna que o checkpoint da `T7`
    (gatilho em 2/3 do teto da classe) endereça.
  - Veredito: suítes/conformance — não aplicável (tarefa só de doutrina, zero código). Gate do kit
    — `-Mode validate` → `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION ==
    KIT_VERSION ('1.4.0').` (exit `0`); `-Mode check-drift` → `kit_check: check-drift OK -
    .claude/README.md == regenerado (9 agente(s), 9 skill(s)).` (exit `0`). Linha antiga do teto
    único: `Select-String -Pattern '~≤40 tool uses esperado no agente'` → **0 ocorrências**
    (substituída, não duplicada — critério de pronto). Piso de regressão — sem mudança. Sem bump
    (o `1.4.0` já saiu no Bloco B; o próximo é definido pela `V2K-T19`).
  - Consumo: ~24 tool uses (contados), tokens **NÃO MEDIDOS** — **execução inline no orquestrador**
    (Opus), sem notificação de subagente e portanto sem bloco `<usage>`; a contagem é autoestimativa
    e está marcada como tal. Dentro do teto de **≤30** da classe "redação de doutrina" que esta
    própria tarefa institui — a classe foi registrada antes de começar, não depois.
- `V2K-T7` — Checkpoint de perda de contexto não planejada — [Opus] — **done** (2026-08-01) *(`C-05`)*
  - Seção nova "Checkpoint intermediário" em `.claude/skills/handover/SKILL.md:76-112`, entre o
    Fluxo de fechamento e a Trava de contexto: gatilho = 2/3 do teto da classe (§3), com os quatro
    limiares já resolvidos em números (10 / 27 / 40 / 20; investigação = 2/3 do teto prescrito) para
    não exigir aritmética do executor sob pressão de contexto; entregável = 5 linhas de ponteiro;
    teto próprio de **2 tool uses** (1 `Grep` de âncora + 1 `Edit`); estado resultante `in progress`,
    nunca `done`/`blocked`. O texto abre e fecha dizendo que é **ponteiro de estado, não relatório
    intermediário** (critério de pronto). Ponteiro em `GOVERNANCA.md:193-196` (§4.3).
  - Verificação (a do dossiê): o formato aplicado ao caso real da `proximo-passo` — queda de
    subagente sem bloco `<usage>` — cabe nas 5 linhas e ficou no próprio texto como exemplo.
  - Piso de regressão — sem mudança (tarefa só de doutrina, sem código). Sem bump.
  - Consumo: ~14 tool uses (contados), tokens **NÃO MEDIDOS** — **execução inline no orquestrador**
    (Opus), sem notificação de subagente e portanto sem bloco `<usage>`; contagem é autoestimativa
    e está marcada como tal. Classe "redação de doutrina" (**≤30**), registrada antes de começar.
- `V2K-T8` — `file:line` + comando de validação no dossiê — [Sonnet] — **done** (2026-08-01) *(`C-06`)*
  - `.claude/skills/diario-de-obras/SKILL.md:55-70` — "Arquivos-alvo" agora pede `caminho:linha`
    (com `§seção`/`(novo)` como formas mais fracas); campo novo "Verificação" (comando colado do
    terminal). `.claude/skills/handover/SKILL.md:22-25` — mesma exigência no fechamento, sem
    tocar Consumo/checkpoint. `GOVERNANCA.md` §4.2 (~linha 181) recebeu o texto DK-3 verbatim.
  - Verificação auto-referente (**Ramo B**): as 19 tarefas do próprio plano **não** satisfazem
    `caminho:linha` estrito — usam âncora de seção/`linha X+`/`(novo)` (forma do ponteiro, caso
    previsto) → template ajustado, tarefas não reescritas.
  - **Ratificado pelo dono em 2026-08-01:** o afrouxamento fica como está — `caminho:linha` é
    preferência, `§seção`/`(novo)` são formas aceitas, e o requisito estrito do `C-06` é o
    **comando colado** no campo "Verificação". Motivo: 0/19 tarefas de um planejador Opus
    produziram a forma estrita, e a própria doutrina DK-3 diz que `caminho:linha` envelhece e não
    se mantém. Reabrir a exigência exige tíquete avulso, não revisão da `V2K-T8`.
  - Gate: `pwsh .claude/checks/kit_check.ps1 -Mode validate` → `kit_check: OK - 9 agente(s) e
    9 skill(s) validados; VERSION == KIT_VERSION ('1.4.0').` (exit 0); `-Mode check-drift` →
    `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 9 skill(s)).`
    (exit 0). Suítes — não aplicável; piso de regressão — sem mudança. Sem bump.
  - Consumo: 18 tool uses, ~99k tokens, Sonnet, ~6,6 min (medido no `<usage>` da notificação).
    Classe "redação de doutrina" (**≤30**), declarada no dossiê antes de delegar — dentro do teto,
    checkpoint de 20 não chegou a disparar. Autorrelato do executor: 19 tool uses (medido 18) —
    primeira divergência da série **para mais**; as anteriores subestimavam.
- `V2K-T9` — Gatilho de revisão e deprecação da doutrina — [Opus] — **done** (2026-08-01) *(`C-07`; instituída a porta de saída de um guardrail — nenhuma regra jamais havia saído do framework)*
  - Resultado: `GOVERNANCA.md` ganhou a subseção **`### 7.1 Revisão e deprecação de guardrails`** ao fim do §7, com os quatro elementos de `DK-5`: **gatilho** (fechamento de MINOR do kit, nunca calendário), **escopo** (guardrails com ≥2 MINORs de idade, i.e. introduzidas em MINOR ≤ corrente − 2), **pergunta única** (*"esta regra mudou algum comportamento nos últimos 2 MINORs? cite o caso"*) e **prazo** (sem caso → `OBSOLETA desde <versão>` → 1 MINOR de transição → remoção no seguinte, desfeita por qualquer caso citável surgido na transição). Mais a lista **"Registro das rodadas"**, que é o estado que o gatilho lê.
  - Definições acrescentadas na redação (detalhe interno de `DK-5`, não mudança de rota): **caso citável** = ocorrência *registrada* na janela (diário do hub **ou de um consumidor**, `CHANGELOG.md`, nota de fechamento, decision record) em que a regra bloqueou, forçou correção ou embasou decisão; com duas exclusões que são o modo de falha da pergunta — **suíte verde não é caso** e **lembrança sem registro não é caso**. Sem fixar a base de evidência a pergunta era inaplicável: o hub não tem código de produção, então avaliar guardrail de arquitetura só pelo registro dele responde "não" por construção.
  - Gatilho na skill `.claude/skills/checar-versao-kit/SKILL.md`: seção nova **"Gatilho de revisão da doutrina (§7.1)"** — a skill já resolve a versão local, então compara o MINOR corrente com o da última rodada registrada em §7.1 e, se avançou, **reporta a revisão como pendente sem executá-la** (a revisão é tarefa nomeada, com registro próprio). Corrigido no mesmo ato o "esse é o **único** gatilho" da seção "Quando roda", que a adição tornava falso: o gatilho de *invocação* continua único (criação de plano); o que passa a haver são duas checagens dentro dele. Atraso aceito por desenho (um MINOR pode fechar sem plano novo logo depois) — troca pontualidade por custo zero de cerimônia. `description` do frontmatter atualizada e `.claude/README.md` **regenerado** (`-Mode generate`, a única correção legítima de deriva).
  - **Primeira aplicação, executada no ato** (a verificação exigida pelo dossiê) — 14 guardrails, janela `1.3.0`+`1.4.0`:
    - **Fora de escopo por idade (6):** itens **9-13** (`G-DEADCODE`, `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY`, `G-EXECREADY`) nasceram em `1.4.0` — idade 0; item **14** (allowlist destrutiva, `V2K-T5`) ainda não foi lançada. A régua dos ≥2 MINORs as exclui corretamente.
    - **Em escopo com caso citável (5):** **1 (regra de dependência)** — `P-0730` do `PantonicVideo` (2026-07-30) usa a direção das camadas como critério de parada (`DL-1`: se tornar o símbolo honesto exigir mover responsabilidade entre camadas, o executor PARA e escala) e ordena a campanha núcleo→bordas por causa dela (§ linhas 76 e 157-158); **3 (MVVM)** — sonda do planejamento de 2026-07-30 mediu 15 properties de ViewModel sem binding declarativo (não há `.ui` nem `.qml` no repo), achado que só existe porque a regra prescreve a camada; **6 (gate de conformance)** — o fecho da `V2M-T5` ficou **bloqueado** até o baseline do consumidor sair `exit 0` (`CHANGELOG.md` 1.4.0); **7 (piso de regressão)** — `DL-5` (2026-07-30): o piso cai por deleção **nominal** de teste, nunca em silêncio; **8 (disciplina de contexto)** — `V2K-T6` (teto graduado) e `V2K-T7` (checkpoint) existem por causa dela, e a `V2K-T4` decidiu execução inline citando §3.
    - **Em escopo sem caso citável (3):** **2 (ACL)**, **4 (egress único de filesystem, G6)** e **5 (namespace de estado)**.
    - **Resultado: 0 marcações.** Os três sem caso ficam **retidos sem marcação**, pendentes de decisão do dono — ver ponto de decisão abaixo. Registrado em `GOVERNANCA.md` §7.1, lista "Registro das rodadas".
  - **Ponto de decisão para o dono (defeito de calibragem medido na primeira aplicação):** a pergunta de `DK-5` **não distingue "regra morta" de "regra preventiva que ninguém violou"**. Guardrail enforçado por teste automático só gera caso citável quando alguém o **viola**; funcionando perfeitamente, ele fica silencioso e a pergunta o condena. Foi exatamente o que aconteceu com ACL, egress G6 e namespace de estado — três regras de arquitetura que a aplicação literal marcaria `OBSOLETA desde 1.4.0` e removeria em `1.6.0`. Agravante medido: os dois MINORs da janela (`1.3.0` e `1.4.0`) fecharam **no mesmo dia** (2026-07-30), então "2 MINORs" hoje valem ~2 dias de relógio, não um período de observação. Não alterei `DK-5` (a rota é do dono — `G-PLANFIDELITY`); retive e escalei.
  - **Decisão do dono (2026-08-01), aplicada no ato pelo orquestrador:** entre 4 opções (isenção por
    enforcement / segunda pergunta contrafactual / piso temporal na janela / manter literal), o dono
    escolheu **isenção por enforcement executável**, sem combinar as demais. Materializada em três
    lugares: (1) `GOVERNANCA.md` §7.1 ganhou o parágrafo **"Isenção por enforcement executável"**
    entre "Escopo" e a pergunta — guardrail verificada por check executável ativo não entra na
    pergunta; a pergunta passa a valer só para regra **advisória/procedimental**; a isenção **não é
    declarativa** (quem invoca **nomeia o check** e confirma que roda; `skip`/`xfail`/allowlist total
    **não** isenta, e check morto é achado próprio); (2) `DK-5` no plano ganhou a emenda `DK-5a`;
    (3) o registro da rodada `1.4.0` foi fechado — ACL, egress G6 e namespace de estado passam de
    *retidos* a **isentos**, com os checks nomeados no consumidor `PantonicVideo`
    (`tests/conformance/test_acl_no_external_in_plugins.py`,
    `tests/conformance/test_filesystem_egress.py`,
    `tests/boundary/test_state_writer_namespacing.py`) e **verificados verdes em 2026-08-01: 11
    passed**, sem `skip`/`xfail` efetivo. Resultado final da rodada: **0 marcações**. Sem bump
    (o `1.5.0` fecha o Bloco C); `CHANGELOG.md` não tocado, mesmo tratamento das `V2K-T6..T9`.
    Gate do kit reconferido após a edição: `validate` e `check-drift` ambos `exit 0`.
    Consumo (aplicação da decisão, execução inline no orquestrador): ~22 tool uses, Opus, tokens
    **não medidos** (sem `<usage>` de subagente) — não entra na série como dado medido.
  - Veredito: suítes/conformance — não aplicável (tarefa só de doutrina + skill, nenhum código de produção no hub). Gate do kit — `validate` → `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION == KIT_VERSION ('1.4.0').` (exit 0); `check-drift` → falhou primeiro (exit 1, 2 linhas divergentes, pela `description` nova), corrigido com `-Mode generate` e reconferido → `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 9 skill(s)).` (exit 0). Piso de regressão — sem mudança. Sem bump (o `1.5.0` fecha o Bloco C). Nenhum arquivo deletado.
  - Consumo: 30 tool uses, ~120k tokens (estimado), Opus, ~12 min — **execução inline no
    orquestrador**, mesmo critério da `V2K-T4` (2 write-clusters em 2 arquivos + registro; `<15`
    turnos estimados ⇒ inline, `GOVERNANCA.md` §3 "delegar protege contexto, não reduz consumo").
    Não há `<usage>` de subagente: a contagem de tool uses é exata (do próprio contexto), a de
    tokens é **estimativa do orquestrador** e está marcada como tal — não entra na série como dado
    medido. Classe "redação de doutrina" (**≤30**): exatamente no teto, sem estouro; 5 das 30
    chamadas foram a varredura de evidência no consumidor (`PantonicVideo`), que não estava
    prevista no dossiê e sem a qual a pergunta de `DK-5` era inrespondível para os itens 1-5.
- `V2K-T10` — Inbox de memória: fila + promoção pelo dono — [Opus] — **done** (2026-08-01) *(`C-10` adaptar; `T4` já cumprida)*
  - **Residência decidida (dono, 2026-07-30, pela régua do `GOVERNANCA.md` §3.1):** **fora do kit** — a fila e a promoção vão para `~/.claude/docs/GOVERNANCA_MEMORIAS.md` + skill global, não para `GOVERNANCA.md` nem para as skills versionadas. Não entra na distribuição do Estágio 4.
  - Resultado — quatro alvos + a fila materializada:
    1. `~/.claude/docs/GOVERNANCA_MEMORIAS.md` ganhou a **§8 "Fila de candidatos a memória"**: a regra ("descobrir e aprovar são atos de donos diferentes"; o agente não escreve em `<memory-dir>/*.md` nem no `MEMORY.md` por conta própria), a **única exceção** — que é de **remoção**, nunca de escrita (ponteiro quebrado/memória obsoleta, como a Regra 6 global já obriga) —, a forma da linha, o ciclo de marcação e a residência com o `DK-6` citado.
    2. `~/.claude/CLAUDE.md` Regra 6: bullet novo "**Descobrir ≠ aprovar**" apontando a §8 (140 linhas, teto 200 preservado).
    3. `.claude/skills/proximo-passo/SKILL.md` passo 1 virou **"Drenar os dois inboxes"** (1 = planos, 2 = fila de memória via `AskUserQuestion`, com "fila vazia ou toda marcada: seguir sem ruído" para não gerar cerimônia).
    4. `GOVERNANCA.md` §3.1: **ponteiro puro** de 3 linhas, sem doutrina copiada.
    5. `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\memory\_INBOX.md` criado (cabeçalho + regramento + `<!-- nenhum candidato enfileirado -->`).
  - Correção feita na própria execução: a primeira redação do ponteiro em `GOVERNANCA.md` tinha ~7 linhas e **repetia** a doutrina da §8 — colisão que o §3.1 manda resolver reduzindo a cópia perdedora a ponteiro **no mesmo ato**. Reduzida antes do fecho.
  - Verificação (os três critérios do dossiê): (a) `<memory-dir>/_INBOX.md` existe no PantonicApp — sim, nasceu vazio com cabeçalho; (b) a `proximo-passo` cita a drenagem dos **dois** inboxes no passo 1 — sim; (c) nenhum caminho do procedimento promove memória sem ato do dono — conferido por leitura: os três textos novos (§8, Regra 6, passo 1) dizem "só o dono promove", e a única exceção escrita é de remoção.
  - Veredito: suítes — não aplicável (hub sem pytest/app Python; tarefa só de doutrina/procedimento). Gate do kit — `-Mode validate` → `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION == KIT_VERSION ('1.4.0').` (exit `0`); `-Mode check-drift` → `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 9 skill(s)).` (exit `0`). Piso de regressão — sem mudança. Sem bump (o `1.4.0` do Bloco C só fecha no fim do bloco).
  - Consumo: 35 tool uses, ~95k tokens, Opus, ~13min — **execução inline no orquestrador** (5 write-clusters pequenos, arquivos conhecidos; delegar pagaria cold start sem reduzir consumo — mesmo critério da `V2K-T4`). Números do próprio contexto do orquestrador, **não** de `<usage>` de subagente, e marcados como tal. **Estouro de 5 sobre a classe "redação de doutrina" (≤30)**: a execução inline absorve no mesmo contador os turnos de *pickup* (drenar inbox, ler diretiva, localizar a tarefa) que numa delegação ficariam fora do teto do executor — a série mede coisas diferentes quando a tarefa é inline, e a classe do `C-04` foi calibrada sobre execuções delegadas.
- `V2K-T11` — Commits assinados + verificação no sync (versão mínima) — [Sonnet] — **done** (2026-08-01) *(`C-08` adaptar; ramo B medido)*
  - Ramo confirmado pelo orquestrador antes da execução: `git config --get user.signingkey` vazio
    ⇒ **ramo B** (verificação em modo aviso). Executor não criou nem configurou chave de
    assinatura — credencial é do dono.
  - Resultado — dois alvos:
    1. `.claude/sync-kit.ps1`: origem resolvida por
       `git -C <kitRoot> log -1 --format=%H -- .` (funciona tanto no hub, `.claude/`, quanto no
       consumidor, `.claude/kit/`); verificação por `git -C <kitRoot> verify-commit <sha>` via
       helper `Invoke-GitCommand`, que captura o exit code explicitamente em vez de deixar
       `$ErrorActionPreference = 'Stop'` derrubar o script numa chamada git que falha. Casos
       degenerados (git ausente, diretório não é repo, nenhum commit toca o caminho) tratados
       como "não verificável" = mesmo tratamento do "não assinado". A verificação roda **antes**
       de qualquer cópia/comparação, inclusive sob `-Check` (decisão documentada no bloco de
       ajuda: é só leitura). Modo padrão imprime `WARN: sync-kit - origin commit <sha> ...` e
       prossegue; `-RequireSignature` (novo `[switch]`) aborta com mensagem acionável
       (`git config user.signingkey <key-id> && git config commit.gpgsign true, then re-commit`)
       e `exit 1`. Bloco de ajuda ganhou `.PARAMETER RequireSignature` e nota em `.DESCRIPTION`/
       `.PARAMETER Check` sobre o novo comportamento.
    2. `GOVERNANCA.md` §10: parágrafo verbatim do plano acrescentado ao fim da seção ("O que se
       distribui, executa...").
  - Verificação executada: sandbox sintético no scratchpad (`git init` +
    `.claude/kit/sync-kit.ps1` + 1 skill + 1 agent + commit **não assinado**, `--no-gpg-sign`).
    Caso 1 (padrão):
    `WARN: sync-kit - origin commit aff25ab80d3312d19d7406aad673001ca4187813 is not
    signature-verified (git verify-commit failed or unavailable). Proceeding without signature
    verification. Re-run with -RequireSignature to enforce.` seguido de
    `sync-kit: 1 copied, 1 skipped by exclusion.`, `exit 0`. Caso 2 (`-RequireSignature`):
    `sync-kit: ABORT - origin commit aff25ab80d3312d19d7406aad673001ca4187813 is not
    signature-verified. Configure commit signing (git config user.signingkey <key-id> && git
    config commit.gpgsign true, then re-commit) or omit -RequireSignature to proceed with a
    warning.`, `exit 1`. Sandbox removido após a prova; nada foi apagado/reescrito no repo real
    além dos dois arquivos-alvo.
  - Achado fora de escopo durante a montagem do sandbox, indexado como `TK-02` (seção
    `## Tíquetes avulsos`, mesma sessão): `Get-ExcludedKeys`/`Test-Excluded` quebram quando
    `kit-exclude.txt` está ausente ou vazio — reproduzido também na versão **original**
    (pré-`V2K-T11`) do script e presente hoje no próprio hub (`.claude/kit-exclude.txt` não
    existe). O caso 1 só chegou a `exit 0` porque o sandbox recebeu um `kit-exclude.txt` com 1
    entrada para contornar esse defeito pré-existente — não corrigido aqui, fora do escopo desta
    tarefa.
  - Gate do kit no repo real: `-Mode validate` →
    `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION == KIT_VERSION ('1.4.0').` (exit
    `0`); `-Mode check-drift` →
    `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 9 skill(s)).`
    (exit `0`).
  - Veredito: os dois ramos de comportamento provados no sandbox com output real; texto de §10
    conferido verbatim contra o plano; gates do kit verdes. Piso de regressão — sem mudança (hub
    sem suíte pytest/app Python). Sem bump de `VERSION`/`KIT_VERSION` — não pedido pelo plano
    desta tarefa e os gates já fecham verdes sem ele.
  - Consumo: 47 tool uses, ~104k tokens, Sonnet, ~100min (medido no `<usage>` da notificação; teto
    informado era 40, classe "implementação padrão" — **estouro de 7**. Causa registrada: o defeito
    pré-existente do `kit-exclude.txt` (`TK-02`) só apareceu como crash dentro do sandbox e consumiu
    turnos de diagnóstico até ser isolado como anterior à tarefa — custo de descoberta, não de
    retrabalho do alvo.)
- `V2K-T12` — Registro de consumidores e versões (`docs/CONSUMIDORES.md`) — [Sonnet] — backlog *(`C-09`)*
- `V2K-T13` — Compatibilidade por major kit × consumidor — [Sonnet] — backlog *(`C-14`; contíguo a `T11`/`T12` por DK-11)*
- `V2K-T14` — Doutrina do piso de regressão **comportamental** (§4.4) — [Opus] — backlog *(`C-11`a; nunca percentual)*
- `V2K-T15` — Receita executável de ratchet do piso — [Sonnet] — backlog *(`C-11`b)*
- `V2K-T16` — Decisão de residência item a item + ratificação do dono — [Opus + dono] — backlog *(`C-12`a; depende de `T4`)*
- `V2K-T17` — Mover o texto e corrigir os ponteiros — [Sonnet] — backlog *(`C-12`b; depende da ratificação em `T16`)*
- `V2K-T18` — Formato e arquivo da série de telemetria (`docs/telemetria.tsv`) — [Sonnet] — backlog *(`C-13`a)*
- `V2K-T19` — Escrita da série nos dois pontos de fechamento + bump `1.4.0` — [Sonnet] — backlog *(`C-13`b)*

### Estágio 4 — `P-0729-v2-documentacao` [blocked — depende do Estágio 3 inteiro done]

- `V2D-T1` — `docs/DOC_MAP.md` do hub — [Sonnet] — blocked
- `V2D-T2` — Redigir o `README.md` espelho (13 seções) — [Opus] — blocked
- `V2D-T3` — Guarda executável de drift do espelho — [Sonnet] — blocked
- `V2D-T4` — Fechar a versão `2.0.0` (CHANGELOG + tag) e **distribuir** — [Sonnet] — blocked *(acumula `P-0722` Fase 4)*
- `V2D-T5` — Teste de aceitação: 6 perguntas respondidas só pelo README — [dono] — blocked

**Notas de execução:** *(vazio — nenhuma tarefa iniciada)*
