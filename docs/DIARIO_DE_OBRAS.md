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
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking (T1..T19, com `T12` partida em `T12a`/`T12b`; 19/20) | in progress | `docs/plans/P-0729-v2-melhoria-candidatos.md` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T5) | blocked | `docs/plans/P-0729-v2-documentacao.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |
| TK-01 | Corrigir residência de `modelo-por-fase` em `GOVERNANCA.md` §3 e no bullet `V2M-T1` do `CHANGELOG.md` (ainda apontam `~/.claude/skills/`, superado por `DM-7`) | done *(absorvido pela `V2M-T3`)* | `docs/DIARIO_HISTORICO.md#tíquetes-avulsos--condensado-em-2026-08-01` |
| TK-02 | `.claude/sync-kit.ps1`: `Get-ExcludedKeys`/`Test-Excluded` quebram sem `kit-exclude.txt` presente (achado pré-existente, `V2K-T11`) | done | docs/DIARIO_HISTORICO.md#tíquetes-avulsos--2ª-condensação-2026-08-01
| TK-04 | `.claude/agents/pantonic-executor.md:20` hardcoda "orçamento esperado ~≤40 tool uses" — diverge de `DR-C`/`V2K-T16` (o kit, `GOVERNANCA.md` §3, já é a única autoridade numérica, tabela de tetos por classe; o global perdeu o número na `T17`) | backlog *(achado da `V2K-T17`)* | `.claude/agents/pantonic-executor.md:20` |

---

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0`.

**Próxima tarefa da sprint:** `V2K-T19` — Escrita da série nos dois pontos de fechamento + bump
`1.4.0` — [Sonnet] *(`C-13`b)*. A `V2K-T18` fechou em 2026-08-04 (`docs/telemetria.tsv` criado com
39 linhas de semente re-derivadas) — bullets de fechamento abaixo.

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

### Estágio 3B — `P-0729-v2-melhoria-candidatos` [in progress — 18/20 (Bloco A fechado, Bloco C em andamento; `T12` partida em `T12a`/`T12b` ⇒ 20 tarefas), nascido fechado em 2026-07-29 pela `V2C-T6`]

19 tarefas, cada uma com o `C-NN` de origem. Ordem normativa em `docs/plans/P-0729-v2-melhoria-candidatos.md`
§2 — **Bloco A** (`T1..T4`) antes do Estágio 3A; **Bloco C** (`T5..T19`) depois dele.

**Bloco A (`T1..T4`) e Bloco C até `T12b`: `done`, 13/20.** Os bullets de fechamento (resultado,
verificação, veredito e `Consumo:` de cada tarefa) estão em `docs/DIARIO_HISTORICO.md`, seção
"Estágio 3B: contexto encerrado e tarefas `T1..T12b`". **`V2K-T13`, `V2K-T14`, `V2K-T15`,
`V2K-T16` e `V2K-T17`: `done`, 18/20** — bullets de fechamento abaixo, ainda não condensados
(diário a ~130 linhas, longe do gatilho de 500).

**Bloco C — em aberto:**
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
- `V2K-T19` — Escrita da série nos dois pontos de fechamento + bump `1.4.0` — [Sonnet] — backlog *(`C-13`b)*

### Estágio 4 — `P-0729-v2-documentacao` [blocked — depende do Estágio 3 inteiro done]

- `V2D-T1` — `docs/DOC_MAP.md` do hub — [Sonnet] — blocked
- `V2D-T2` — Redigir o `README.md` espelho (13 seções) — [Opus] — blocked
- `V2D-T3` — Guarda executável de drift do espelho — [Sonnet] — blocked
- `V2D-T4` — Fechar a versão `2.0.0` (CHANGELOG + tag) e **distribuir** — [Sonnet] — blocked *(acumula `P-0722` Fase 4)*
- `V2D-T5` — Teste de aceitação: 6 perguntas respondidas só pelo README — [dono] — blocked

**Notas de execução:** *(vazio — nenhuma tarefa iniciada)*
