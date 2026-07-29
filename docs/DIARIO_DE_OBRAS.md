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
| P-0729-V2M | Estágio 3A — doutrina herdada do P-0722 (T1..T5) | backlog | `docs/plans/P-0729-v2-melhoria.md` |
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking (T1..T19) | in progress | `docs/plans/P-0729-v2-melhoria-candidatos.md` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T5) | blocked | `docs/plans/P-0729-v2-documentacao.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |

---

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0`.

**Próxima tarefa da sprint:** `V2K-T2` (`docs/plans/P-0729-v2-melhoria-candidatos.md`, §3 T2) —
**[Sonnet]**, gerador do `.claude/README.md` + detecção de deriva, segunda tarefa do **Bloco A**
(`V2K-T1` fechou `done` nesta sessão). A ordem entre os dois planos do Estágio 3 é **normativa** (DK-1, §2
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

### Estágio 1 — `P-0729-v2-benchmarking` [done — 9/9 tarefas, 2026-07-29]

- `V2B-T1` — Instituir o controle de versão do framework (`VERSION` + `KIT_VERSION` + `CHANGELOG`) — [Sonnet] — done
  - Resultado: `VERSION` e `.claude/KIT_VERSION` em `1.1.0` (paridade obrigatória); `CHANGELOG.md` criado na raiz; `GOVERNANCA.md` §10 ganhou parágrafo final com a regra de paridade e MAJOR/MINOR/PATCH; commit + tag anotada `kit-v1.1.0` (sem push).
  - Consumo: 13 tool uses, ~44k tokens, Sonnet, ~100s (medido no `<usage>` da notificação).
- `V2B-T2` — Agente `pantonic-benchmarker` + esquema D1..D16 — [Sonnet] — done
  - Resultado: agente `pantonic-benchmarker` (Haiku, sem Bash/Edit) e `docs/benchmark/_ESQUEMA.md` (D1..D16 + rodapé) criados; `.claude/README.md` atualizado; `VERSION`/`.claude/KIT_VERSION` em `1.2.0`; commit + tag `kit-v1.2.0` (sem push).
  - Consumo: 20 tool uses, ~57k tokens, Sonnet, ~128s (medido no `<usage>` da notificação; autoestimativa do executor dizia 13).
- `V2B-T3` — Curadoria e cache do corpus (25 candidatos → 20 confirmados) — [Sonnet] — done
  - Resultado: `docs/benchmark/_CORPUS.md` criado (26 linhas, **21 `confirmado`** numeradas BM-01..BM-21, cobrindo A=4/B=4/C=4/D=3/E=3/F=3) + `docs/benchmark/_trees/` com 21 árvores de arquivos cacheadas; 50 requisições GitHub API gastas, sem 403/429.
  - Desvio resolvido no mesmo turno: o executor achou a trilha F com só 2 candidatos na origem (piso de 3 da DV-3 inatingível) e propôs triar no `V2B-T8`; o orquestrador antecipou a decisão porque a numeração `BM-*` congela no `V2B-T4`. **Decisão do dono: ampliar o corpus de 20 para 21** — `snarktank/ai-dev-tasks` entra como `BM-21`. `DV-3` emendada; `V2B-T7` passa a 6 subagentes e `V2B-T8` valida 21/21.
  - Veredito — V2B-T3
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e `docs/plans/*`); nenhum teste/conformance relevante.
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 24 tool uses, ~79k tokens, Sonnet, ~357s (medido no `<usage>` da notificação).
- `V2B-T4` — Relatórios do lote 1 (repos 1-5) — [Haiku ×5] — done
  - Resultado: `docs/benchmark/BM-01..BM-05` emitidos (spec-kit 146 linhas, BMAD-METHOD 160, OpenSpec 115, SuperClaude 80, claude-code 102); 5/5 com D1..D16 completas e rodapé (3 transplantáveis / 3 anti-práticas / dimensões fora da grade); 58 buscas de conteúdo no total, nenhuma chamada a `api.github.com`.
  - Desvio 1 — **agente do kit não invocável na sessão em que nasce.** O registro de subagentes do CLI é carregado na inicialização do processo, então `pantonic-benchmarker` (criado no `V2B-T2`, mesmo processo) devolveu `Agent type not found`. Contornado com o tipo genérico + `model: haiku` + leitura da própria definição em disco (doutrina verbatim; restrição de ferramentas aplicada por instrução em vez de pelo harness). **RESOLVIDO — decisão do dono, 2026-07-29:** reiniciar o CLI. O contorno **não** vira doutrina; os lotes 2-4 (`V2B-T5..T7`) usam o agente real `pantonic-benchmarker`, com a restrição de ferramentas aplicada pelo harness. Confirmado em 2026-07-29 que `/clear` **não** basta (o registro é carregado na inicialização do processo, não da conversa) — é preciso fechar e reabrir o CLI.
  - Desvio 2 — **auto-relato de tamanho não é confiável.** Os 5 coletores reportaram contagens de linha que não bateram com `wc -l` (BM-05 reportou 157, tinha 253; BM-03 reportou 78, tinha 113). Três estouraram o teto de 160 (162/211/253) e foram condensados por `SendMessage` ao mesmo agente, sem gastar busca nova. **Regra para `V2B-T5..T7`: o teto de 160 é verificado pelo orquestrador em disco, nunca pelo relatório do coletor.**
  - Desvio 3 — **deriva dos títulos das dimensões** (o checklist do `V2B-T8` reprova dimensão renomeada): D10 truncado para "Distribuição e versionamento" em 4 dos 5, D14 truncado em 1, capitalização divergente em 2. Normalizado pelos títulos canônicos do `_ESQUEMA.md` via script determinístico (`scratchpad/normalize_dims.py`) — 32 títulos corrigidos, sem tocar conteúdo. Reaplicar o mesmo script ao fim de cada lote.
  - Desvio 4 — **guardrail 1 violado no BM-03**: "Contribuidores: 30+" sem URL e fora do cache do T3. Corrigido inline para `NÃO ENCONTRADO`, com a fonte dos metadados de D2 apontada para `_CORPUS.md`.
  - Veredito — V2B-T4
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 122 tool uses em 5 subagentes Haiku (incl. 3 retomadas de condensação), ~282k tokens Haiku, ~2,3k s de parede em paralelo (medido nos blocos `<usage>` das notificações); orquestrador ~20 tool uses em Opus.
- `V2B-T5` — Relatórios do lote 2 (repos 6-10) — [Haiku ×5] — done
  - Resultado: `docs/benchmark/BM-06..BM-10` emitidos (anthropics/skills 136 linhas, awesome-copilot 104, gemini-cli 141, awesome-cursorrules 118, cline 119); 5/5 com D1..D16 completas e rodapé, todos abaixo do teto de 160.
  - **Lote limpo — nenhum dos 4 desvios do `V2B-T4` reapareceu.** Os 5 subagentes rodaram com o agente **real** `pantonic-benchmarker` (CLI reiniciado antes do despacho, conforme Desvio 1 do `V2B-T4`) — confirmação prática de que a restrição de ferramentas pelo harness + doutrina no arquivo do agente elimina a deriva: (a) teto verificado em disco por `(Get-Content).Count` — 0 estouros, 0 condensações; (b) `_normalize_dims.py` rodado nos 5 — **0 títulos normalizados** (contra 32 no lote 1); (c) `D2 — Vitalidade` conferida contra `_CORPUS.md` — stars/`pushed_at`/licença batem nos 5, todos com `NÃO ENCONTRADO` em contribuidores e ponteiro de linha do corpus como fonte.
  - Commits: dois, um por tarefa (decisão do dono 2026-07-29) — `5e9f228` liquida o pendente herdado do lote 1 (`BM-01..BM-05` + `_normalize_dims.py`), seguido do commit do lote 2. Sem push.
  - Veredito — V2B-T5
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: **PARCIAL — só `BM-08` medido** (28 tool uses, ~40k tokens, Haiku, ~201 s, do `<usage>` da notificação). As notificações de `BM-06/07/09/10` foram consumidas na sessão anterior ao `/clear` e os `.output` das tarefas estão vazios — **NÃO MEDIDO**, sem autoestimativa disponível. Orçamento do lote 2 aparentemente ~⅓ do lote 1 (que gastou 122 tool uses/282k tokens com 3 retomadas de condensação); a comparação fica sem base medida. Orquestrador: ~14 tool uses em Opus.
  - **Lição de telemetria:** `/clear` entre o despacho e a conclusão dos subagentes **perde o `<usage>` dos que já haviam notificado**. Fechar o lote no mesmo contexto do despacho, ou aceitar telemetria parcial.
- `V2B-T6` — Relatórios do lote 3 (repos 11-15) — [Haiku ×5] — done
  - Resultado: `docs/benchmark/BM-11..BM-15` emitidos (context-engineering-intro 71 linhas, agent-rules 137, awesome-claude-code 92, claude-code-hooks-mastery 125, wshobson/agents 90); 5/5 com D1..D16 completas e rodapé, todos abaixo do teto de 160.
  - **Desvio 1 (novo) — queda coletiva por limite de sessão da conta.** Os 5 subagentes morreram ao mesmo tempo com `You've hit your session limit`, não por falha própria: 2 já tinham gravado o arquivo (`BM-11`, `BM-12`), 3 pararam com a coleta feita e o relatório por escrever. **Nenhum foi re-delegado a frio** — os 5 foram retomados por `SendMessage` ao mesmo `agentId`, a partir do próprio transcript, com a instrução "feche com o que já coletou, sem busca nova". Custo da recuperação: 12 tool uses somados, **0 buscas de conteúdo novas**. **Regra: queda por limite de sessão é retomável — re-despacho a frio joga fora a coleta já paga.**
  - **Desvio 2 do `V2B-T4` reincidiu** (auto-relato de tamanho não confiável): `BM-14` relatou "~75 linhas" e tinha 125; `BM-15` relatou 154 e tinha 90; `BM-13` relatou "~130" e tinha 92. Dois estouros reais do teto (`BM-11` com 318, `BM-13` com 201) foram condensados por `SendMessage` ao mesmo agente, sem busca nova.
  - **Desvio 3 do `V2B-T4` reincidiu** (deriva dos títulos): 4 dos 5 truncaram `D10` para "Distribuição e versionamento"; `_normalize_dims.py` corrigiu os 4 (o lote 2 tinha normalizado 0).
  - **Desvio 4 do `V2B-T4` reincidiu** (`D2` sem fonte): `BM-14` gravou `D2 — Vitalidade` inteiro como `NÃO ENCONTRADO` com o dado disponível em cache; `BM-12` gravou os números sem ponteiro de fonte. Corrigidos inline pelo orquestrador contra `_CORPUS.md` (linhas 62 e 59). `D2` dos outros 3 confere com o corpus (stars/`pushed_at`/licença).
  - **Leitura dos 3 reincidentes:** o lote 2 limpo **não** provou que o agente resolveu o problema — provou que aquele lote teve sorte. Os pós-processamentos do orquestrador (contagem em disco, `_normalize_dims.py`, conferência de `D2`) são **permanentes**, não transitórios, e entram no `V2B-T8` como parte do QC.
  - Veredito — V2B-T6
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: **PARCIAL — só o trecho de retomada foi medido** (~190,5k tokens Haiku, 12 tool uses, ~6,5 min de parede somados, dos blocos `<usage>` das 5 notificações de conclusão). O trecho **pré-queda** — 8 a 12 buscas de conteúdo por coletor — está **NÃO MEDIDO**: notificação de falha não traz `<usage>`. Orquestrador: ~31 tool uses em Opus.
- `V2B-T7` — Relatórios do lote 4 (repos 16-21) — [Haiku ×6] — done
  - Resultado: `docs/benchmark/BM-16..BM-21` emitidos (guardrails-ai/guardrails 92 linhas, NVIDIA-NeMo/Guardrails 102, promptfoo/promptfoo 84, sdi2200262/agentic-project-management 100, Wirasm/prp 90, snarktank/ai-dev-tasks 158); 6/6 com D1..D16 completas e rodapé, todos abaixo do teto de 160 **após condensação**.
  - **Desvio 2 do `V2B-T4` reincidiu com força total**: 4 dos 6 estouraram o teto no auto-relato de tamanho **e** na primeira gravação em disco — `BM-16` (278 linhas), `BM-17` (292), `BM-20` (279, coletor relatou 154) e `BM-21` (165, coletor relatou ~155). Todos os 4 foram condensados por `SendMessage` ao mesmo `agentId`, sem busca nova. `BM-21` reincidiu **uma segunda vez** mesmo após condensação (relatou "exatamente 160", media 162 em disco) — aparado diretamente pelo orquestrador (removida uma nota de contexto temporal redundante com `D2`) para 158. **Regra reforçada: verificar em disco depois de toda condensação, não só na primeira gravação — o auto-relato erra na segunda tentativa também.**
  - **Desvio 3 do `V2B-T4` reincidiu**: `D10` truncado para "Distribuição e versionamento" em 5 dos 6; `D3` truncado em 1 (`BM-17`). `_normalize_dims.py` corrigiu os 6 (0 títulos incorretos restantes).
  - **Desvio 4 do `V2B-T4` reincidiu, com uma variante nova**: `BM-17` citou o `CHANGELOG.md` do próprio repositório como fonte de `D2` em vez de `_CORPUS.md` (corrigido inline, linha 65); `BM-21` apontou `_CORPUS.md:26` — **confundiu o índice da linha da tabela (coluna `#`) com o número real da linha do arquivo** (linha real: 69). Corrigido inline. **Variante nova para o `V2B-T8`: conferir que o ponteiro de fonte usa o número de linha do arquivo, não a coluna de índice da tabela.**
  - Veredito — V2B-T7
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 136 tool uses em 6 subagentes Haiku (incl. 4 retomadas de condensação), ~310k tokens Haiku, ~11,5k s de parede somados (medido nos blocos `<usage>` das 10 notificações); orquestrador ~28 tool uses em Sonnet.
- `V2B-T8` — Controle de qualidade e índice do corpus — [Sonnet] — done
  - Resultado: QC adversarial nos 21 relatórios contra o checklist de 7 itens do plano.
    `docs/benchmark/INDICE.md` criado com veredito por relatório, trilha, `owner/repo`, e a lista
    agregada de "Dimensões Fora da Grade" dos 21 (insumo do Estágio 2). **21/21 aprovados** após 5
    correções pontuais via Edit: 4× citação de fonte do `D2` sem linha real de `_CORPUS.md`
    (`BM-01` sem nenhuma fonte → linha 44; `BM-03` citava o rótulo `BM-03` em vez da linha real →
    linha 47; `BM-04` citava só "metadados T3" → linha 49; `BM-13` sem nenhuma fonte → linha 61) e
    1× menção a "Pantonic" no rodapé (`BM-16`: `Gerador: PANTONIC-V2 Estágio 1` → `Coletor de
    benchmarking, Estágio 1`). `BM-17` e `BM-21` (variante nova do `V2B-T7`) já conferiam
    corretamente contra a linha real de `_CORPUS.md` (65 e 69) — não reincidiram.
  - Achados de checklist limpos nos 21 sem correção: dimensões D1..D16 na ordem e título canônico
    exato; teto de 160 linhas (`BM-02` está exatamente em 160 — o `wc -l` real corrigiu um falso
    positivo do primeiro passe de checagem, que contava uma linha fantasma por causa do `\n` final
    do arquivo); rodapé com as 3 seções obrigatórias e 3 itens em cada lista; campo "Dimensões
    Fora da Grade" presente nos 21 (2 responderam "nenhuma": `BM-11`, `BM-16`); nenhuma URL de raiz
    de repositório (item 3) nos 21.
  - **Desvio registrado (tíquete no `INDICE.md`, não corrigido nesta tarefa):** boa parte das
    seções D3..D16 cita a fonte por caminho de arquivo relativo (ex.: `` **Fonte:** `package.json` ``)
    em vez da URL exata exigida por `_ESQUEMA.md` — padrão sistêmico em pelo menos `BM-07`, `BM-09`,
    `BM-10`, `BM-11`, `BM-14`, `BM-16`, `BM-17`, presente em várias sessões/lotes distintos.
    Corrigir os ~40+ pontos excede o orçamento desta tarefa e é busca transversal — recomendada
    tarefa dedicada (`V2B-T9` ou item do backlog geral) para normalizar as citações para URL
    completa.
  - Veredito — V2B-T8
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e
    `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 67 tool uses, ~159k tokens, Sonnet, ~13,5 min (medido no `<usage>` da notificação).
    **Teto estourado:** o dossiê fixou `~45 tool uses` com "PARE e reporte ao atingir o teto"; o
    executor foi a 67 (+49%) sem parar — quarto caso da série (UXROUND3 T3/T4/T5 no PantonicVideo,
    agora `V2B-T8`). Confirma a decisão do dono de 2026-07-16: **executores não param no teto — o
    teto é alarme, a divisão prévia em sub-tarefas é o controle.** Aqui o QC de 21 artefatos em 7
    itens de checklist era divisível por lote (T4..T7 já eram lotes de 5-6) e não foi dividido.

- `V2B-T9` — Normalizar as 29 citações de fonte para URL completa — [Sonnet] — done
  - Nasce do achado do `V2B-T8`. **Rota escolhida pelo dono (2026-07-29):** normalização completa
    das 29, e não a correção só das 6 vagas nem o aceite como limitação conhecida. Dimensionamento
    medido no fechamento (222 citações totais; 179 já com URL; 14 `_CORPUS.md` corretas por
    desenho; 23 caminhos reconstruíveis; 6 vagas) e dossiê fechado em
    `docs/plans/P-0729-v2-benchmarking.md` §5 `T9` — inclui o guardrail central: caminho ausente
    da árvore cacheada vira `NÃO ENCONTRADO`, nunca URL inventada.
  - **Correção de estado aplicada junto:** `P-0729-V2B` reverteu de `done` para `in progress` e
    `P-0729-V2C` voltou a `blocked`. O `V2B-T8` havia flipado o plano para `done` com este achado
    ainda sem rota triada — a regra da skill `diario-de-obras` ("a sprint só flipa para `done` com
    todos os achados triados") não admite.
  - Resultado: 29 citações convertidas via script determinístico
    (`_normalize_dims.py`-like, scratchpad) em `BM-02` (1), `BM-07` (2), `BM-09` (11), `BM-10` (2),
    `BM-11` (3), `BM-14` (1) e `BM-16` (9) para `https://raw.githubusercontent.com/<full_name>/HEAD/<caminho>`,
    `full_name` reaproveitado dos já-conformes de cada relatório (`bmad-code-org/BMAD-METHOD`,
    `github/awesome-copilot`, `PatrickJS/awesome-cursorrules`, `cline/cline`,
    `coleam00/context-engineering-intro`, `disler/claude-code-hooks-mastery`,
    `guardrails-ai/guardrails`); todo caminho verificado contra `docs/benchmark/_trees/*.txt` antes
    de virar URL. Citação com vários arquivos virou uma URL por arquivo (precedente `pyproject.toml,
    SECURITY_ADVISORY.md` do `BM-16`). Wildcard `docs/README.*.md` (`BM-07`) resolvido contra a
    árvore para os 6 arquivos reais (`agents/hooks/instructions/plugins/skills/workflows`), não uma
    URL inventada. `docs/benchmark/INDICE.md` — tíquete fechado com o resultado.
  - **6 referências vagas sem arquivo checável** viraram citação do artefato local
    `docs/benchmark/_trees/<slug>.txt` (3 mistas, com outro arquivo real no mesmo campo, mantêm ao
    menos uma URL; 3 puras — `BM-02` D5, `BM-11` D11, `BM-14` D11 — ficam só com o caminho da árvore,
    sem `http`, por desenho da decisão fechada). Consequência: `grep -h "Fonte:" docs/benchmark/BM-*.md
    | grep -v http | grep -vi "_CORPUS"` cai de 29 para **3** linhas, não 0 — resíduo esperado da
    regra "nunca inventar URL" aplicada a uma referência sem nenhum arquivo específico associado,
    não um defeito desta tarefa.
  - **Residual fora de escopo (não corrigido aqui, registrado no `INDICE.md`):** `BM-17`
    (D7/D11/D12) tem o mesmo padrão de caminho relativo mas não fazia parte da lista de 29
    citações/7 relatórios dimensionada no dossiê — fica como possível tíquete futuro.
  - Veredito — V2B-T9
    Suítes: não aplicável — tarefa não tocou código (só `docs/benchmark/*` e
    `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - **Defeito de dossiê (não de execução), para o Estágio 3:** o critério "Pronto quando" do `T9`
    (`grep ... → 0 linhas`) contradiz a decisão fechada nº 3 do próprio `T9` (referência vaga cita
    `_trees/<slug>.txt`, que não tem `http`). Plano fechado pode conter critério de aceite
    internamente inconsistente — o executor acertou ao seguir a decisão fechada e reportar, mas o
    gate `G-PLANREADY` deveria exigir que o "Pronto quando" seja derivado das decisões fechadas.
  - Consumo: 49 tool uses, ~117k tokens, Sonnet, ~9,0 min (medido no `<usage>` da notificação).
    **Teto estourado:** dossiê fixou 30 com "PARE ao atingir"; executor foi a 49 (+63%) — quinto
    caso da série (UXROUND3 T3/T4/T5, `V2B-T8`, agora `V2B-T9`). Aqui o teto foi mal dimensionado:
    a fase de reconhecimento (29 citações em 3 formatos distintos × 7 árvores) não cabe em 30 tool
    uses junto com a aplicação. Reforça a decisão de 2026-07-16: **o controle é a divisão prévia,
    não o número.**

### Estágio 2 — `P-0729-v2-confronto` [in progress — 3/6 tarefas, `V2C-T3` done em 2026-07-29]

- `V2C-T1` — Auto-retrato do PantonicApp no esquema do corpus (`BM-00`) — [Sonnet] — done
  - Resultado: `docs/benchmark/BM-00-pantonicapp.md` criado (156 linhas, D1..D16 completas, todas
    com `arquivo:linha`); 0 dimensões `NÃO ENCONTRADO` puras (D2/D13 têm campos parciais
    `NÃO ENCONTRADO` dentro de uma dimensão majoritariamente respondida); 2 dimensões com
    1 dimensão com trecho `PARCIAL — decidido, não escrito` (D9 — as 5 guardrails do `P-0722`,
    com ponteiro para o Estágio 3A; a skill `modelo-por-fase` aparece só como referência em
    D6/D9, sem marcação própria, pois a doutrina já existe em prosa e só a skill falta). Achado de
    escopo (README do kit desatualizado, falta `pantonic-auditor-container` na tabela) já
    virou anti-prática registrada no rodapé do próprio `BM-00`, não tíquete separado.
  - Veredito — V2C-T1
    Suítes: não aplicável — tarefa não toca código (só `docs/benchmark/*` e
    `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 28 tool uses, ~111k tokens, Sonnet, ~305s (medido no `<usage>` da notificação).
  - Verificado pelo orquestrador em disco: 156 linhas (teto 170) e os 16 títulos `## D1..D16`
    idênticos aos canônicos do `_ESQUEMA.md` — sem deriva de título (o desvio 3 do `V2B-T4` não
    se repetiu).
- `V2C-T2` — Matriz de cobertura dimensão × framework — [Sonnet] — done
  - Resultado: `docs/benchmark/MATRIZ_DIMENSOES.md` criado (matriz 16×22 = 352 células, nenhuma
    vazia — 182 `+`, 114 `~`, 56 `—`); lista (a) Lacuna de consenso **vazia** (só `D2` tem
    `BM-00`=`—`, e nenhum framework externo marca `+` em `D2`, todos `~`); lista (b) Diferencial
    ou excentricidade com **1 item** (`D6` — Contexto e custo, `BM-00`=`+` com 2 frameworks em
    `+`: `BM-04`, `BM-12`); lista (c) Candidatas a D17+ com **3 grupos** de 2 citações cada
    (orçamento/teto de contexto-turnos-custo: `BM-05`+`BM-20`; marketplace/registro canônico com
    lacuna de governança: `BM-07`+`BM-15`; precedência entre hooks/rules/skills/plugins:
    `BM-10`+`BM-14`).
  - Veredito — V2C-T2
    Suítes: não aplicável — tarefa não toca código (só `docs/benchmark/MATRIZ_DIMENSOES.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 32 tool uses, ~178k tokens, Sonnet, ~449s (medido no `<usage>` da notificação).
  - Verificado pelo orquestrador em disco: 83 linhas; linha `D2` da matriz é `BM-00`=`—` com os 21
    externos em `~` — a lista (a) vazia é resultado legítimo da rubrica, não célula esquecida (o
    campo "contribuidores" quase nunca é confirmado, então ninguém pontua `+` em `D2`). O `T3`
    deve ler a lista (a) vazia como "nenhuma lacuna de consenso pela régua mecânica", não como
    "nenhuma lacuna".
- `V2C-T3` — Relatório consolidado de forças, fraquezas e dimensões novas — [Opus] — done
  - Resultado: `docs/benchmark/RELATORIO_CONSOLIDADO.md` criado (808 linhas, 239 citações `BM-NN`;
    zero afirmação sobre externo sem `BM-NN`, zero afirmação sobre o Pantonic sem `arquivo:linha`
    via `BM-00`). **16 vereditos:** 5 `MANTER` (D1, D3, D4, D10, D16), 5 `ADOTAR` (D8, D9, D11,
    D13, D14), 5 `ADAPTAR` (D5, D6, D7, D12, D15), 1 `REJEITAR` (D2 — publicação pública do hub,
    com motivo escrito ancorado em `BM-09` anti-prática 2 e `BM-13` anti-prática 1). **6 dimensões
    novas propostas** (D17 precedência entre mecanismos de doutrina; D18 registro de consumidores e
    versões instaladas; D19 recuperação de sessão **não planejada**; D20 reversibilidade do
    trabalho do agente; D21 vida útil/deprecação da própria doutrina; D22 integridade da cadeia de
    suprimentos da doutrina) — 3 vêm da lista (c) do `MATRIZ_DIMENSOES.md`, 3 de leitura direta do
    corpus. **8 descartes justificados** (matriz formal de rastreabilidade, adapter multi-harness,
    marketplace público, Monte Carlo por commit, meta de % de cobertura, multi-agente com message
    bus, auto-update no consumidor, modo YOLO). **8 vieses do corpus** documentados.
    Juízos não óbvios: (1) os 5 `ADOTAR` consolidam em **3 peças de trabalho** para o `T4`, não 5 —
    D9+D11+D14 são um único checador/gerador do kit; (2) a recomendação nº 1 é converter a **forma**
    do enforcement (texto → código), explicitamente **não** criar guardrail nova — as 5 do `P-0722`
    já estão decididas e apontadas para o Estágio 3A, e o alvo inicial do checador é um defeito que
    já existe (drift do `.claude/README.md`, `BM-00§D4`); (3) achado de D15: dois diferenciais do
    framework (orçamento de contexto e telemetria de consumo) citam `CLAUDE.md` global do usuário —
    não viajam no kit por `git subtree`; (4) premissa do corpus contrariada: parte dos `—` da
    matriz é orçamento de coleta e não ausência real — `BM-08§D6` admite literalmente
    "existe (não buscado no orçamento)".
    Desvio de calibração: alvo do dossiê era ~400-550 linhas; entregue 808 (+47%) — densidade de
    citação exigida pelo guardrail duro (16 dimensões × 3 blocos + 6 D17+ + 8 descartes + 8 vieses,
    cada um com `BM-NN` colado). Não é gate de aceite; registrado para o `T4` dimensionar a leitura.
  - Veredito — V2C-T3
    Suítes: não aplicável — tarefa não toca código (só `docs/benchmark/RELATORIO_CONSOLIDADO.md` e
    `docs/DIARIO_DE_OBRAS.md`).
    Piso: sem mudança de piso.
    Checklist de review: não aplicável (sem import/camada/MVVM/UI thread tocados).
  - Consumo: 37 tool uses, ~183k tokens, Opus, ~698s (medido no `<usage>` da notificação).
  - Verificado pelo orquestrador em disco: 808 linhas; 236 linhas com citação `BM-NN`; 16 linhas
    `**Veredito — X.**` (5 `MANTER`, 5 `ADOTAR`, 5 `ADAPTAR`, 1 `REJEITAR` — a única `REJEITAR`,
    `D2`, traz *Motivo escrito*); §3 (D17..D22), §4 (8 descartes) e §5 (8 vieses) não-vazias.
- `V2C-T4` — Backlog priorizado de candidatos (`C-NN`) — [Opus] — done
  - Resultado: `docs/benchmark/CANDIDATOS.md` (471 linhas) — **15 candidatos** `C-01..C-15`, 100%
    rastreáveis a seção+linhas do consolidado. Conversão: 5 `ADOTAR` → 3 (D9+D11+D14 no `C-01`,
    conforme juízo do `T3`), 5 `ADAPTAR` → 1 cada, D17..D22 → 1 cada, D10 → `C-14`. Recomendações
    11/2/2 (`adotar`/`adaptar`/`adiar`); zero decisões tomadas — são do `T5`.
  - Deltas que o `T5`/`T6` precisam ver (detalhe nas próprias seções do arquivo): **override da
    ordem I÷E** no `C-01`, explicitado em `CANDIDATOS.md` §2 (é precondição, não melhor candidato);
    **tensão `C-11` × `G-DEADCODE`** registrada na ficha do `C-11` (piso comportamental, não
    percentual); `C-03` promovido por ser a régua de residência de que `C-04`/`C-10`/`C-12` e a
    `V2M-T3` dependem; resíduo de D2 (licença) **não** virou `C-NN` (§4, item 1).
  - Veredito — V2C-T4
    Suítes: não aplicável — tarefa não toca código (só `docs/benchmark/CANDIDATOS.md` e este diário).
    Piso: sem mudança de piso. Checklist de review: não aplicável.
    Pronto-quando verificado mecanicamente: 15/15 fichas com os 7 campos obrigatórios; IDs da
    tabela-índice idênticos e na mesma ordem das fichas; 6 blocos do `T5` cobrindo cada `C-NN` 1×.
  - Consumo: 28 tool uses (contados), tokens **NÃO MEDIDOS** — executada *inline* pelo orquestrador
    em Opus, sem subagente e portanto sem bloco `<usage>`; inline por volume (1 write-cluster).
- `V2C-T5` — Ratificação do dono (decisão por candidato) — [dono] — done
  - Resultado: **15/15 decididos** em 2026-07-29, gravados na linha `Decisão do dono` de cada ficha
    (fonte única) + bloco-resumo no cabeçalho do `CANDIDATOS.md`. `adotar` 12 · `adaptar` 2
    (`C-08`, `C-10`) · `adiar` 1 (`C-15`) · `rejeitar` 0. Esforço somado dos 14 ativos:
    **19 tarefas atômicas estimadas**.
  - Método: 6 blocos temáticos conforme `CANDIDATOS.md` §2, 1 round-trip por bloco (6 no total,
    não 15), recomendação do planejador visível em cada linha.
  - **Única divergência da recomendação: `C-14`** (recomendado `adiar`, decidido **`adotar`**) —
    o delta é barato e toca os mesmos arquivos-alvo de `C-08`/`C-09`, então o `V2C-T6` deve
    agrupá-los. Os 3 candidatos ≠ `adotar` têm linha de motivo registrada, como exige o dossiê.
  - Vínculos que o `V2C-T6` herda fechados: `C-11` só é redigível como piso **comportamental**
    (nunca percentual — trava a tensão com `G-DEADCODE`); `C-08` e `C-10` entram só na versão
    mínima descrita no motivo; `C-03` antes de `C-04`/`C-10`/`C-12` e da `V2M-T3`.
  - Tensão a resolver **no `V2C-T6`**, não aqui: a regra de decomposição (b) do dossiê do `T6` diz
    "todo `C-NN` `adotar`/`adaptar` gera **exatamente uma** tarefa", mas 4 candidatos foram
    estimados em 2-3 tarefas (`C-01` 3; `C-11`, `C-12`, `C-13` 2 cada) e a regra (a) obriga a
    dividir doutrina × mecânica. Prevalece (a) — a regra (b) deve ser lida como "≥1 tarefa, nenhuma
    sem `C-NN` de origem".
  - Consumo: 12 tool uses (contados), tokens **NÃO MEDIDOS** — executada *inline* pelo orquestrador
    em Opus (tarefa do dono, não delegável), sem subagente e portanto sem bloco `<usage>`.
- `V2C-T6` — Autorar `P-0729-v2-melhoria-candidatos.md` **já fechado** (Estágio 3B) — [Opus] — done
  - Resultado: `docs/plans/P-0729-v2-melhoria-candidatos.md` criado (**19 tarefas**, `V2K-T1..T19`),
    linha `[drenado]` no `_INBOX.md`, linha no índice deste diário e a seção do Estágio 3B abaixo.
    Cobertura: os 14 candidatos ratificados (12 `adotar` + 2 `adaptar`) têm tarefa; `C-15` (`adiar`)
    não gera nenhuma, com motivo em §4; nenhuma tarefa sem `C-NN` de origem. As 19 tarefas batem
    exatamente com o esforço somado ratificado em `CANDIDATOS.md:20`.
  - Tensão do dossiê resolvida como o `T5` mandou: prevalece a regra (a) (doutrina × mecânica são
    fases de modelo diferentes) e a (b) lê-se como "≥1 tarefa". A inflação que a leitura literal
    produziria (27 tarefas, uma linha de doutrina virando tarefa própria) foi evitada por **DK-3**:
    quando uma tarefa [Sonnet] encosta em uma linha de doutrina, **o texto é redigido no plano** e a
    tarefa apenas transcreve — 4 blocos de doutrina já vêm escritos verbatim (`T5`, `T8`, `T11`,
    `T18`).
  - 11 decisões novas fechadas no ato (`DK-1..DK-11`), incluindo a pergunta que a ficha do `C-01`
    deixava aberta (um script com dois checks ou dois scripts → **três** scripts, um ponto de
    invocação) e a ordem parcial normativa entre 3A e 3B.
  - Fatos re-derivados agora, não copiados do plano: `.claude/README.md` lista **8** agentes
    (`:12-19`) contra 9 em `.claude/agents/` e **6** skills (`:39-44`) contra 8 — a anti-prática 1
    do `BM-00` está **viva**, e é o alvo medido da `V2K-T2`; o único agente com `Bash` é o
    `pantonic-executor`, e por omissão de `tools:` (os outros 8 declaram lista explícita sem
    `Bash`), o que manda o controle do `C-02` para `.claude/settings.json` (inexistente hoje);
    `git config --get user.signingkey` **vazio**, o que fixa o ramo B da `V2K-T11`; `docs/telemetria.tsv`
    nasce com semente de **14** linhas `Consumo:`; o hub não tem `tests/` (confirma a anti-prática 2).
  - Veredito — V2C-T6
    Suítes: não aplicável — tarefa não toca código (só `docs/plans/*` e este diário).
    Piso: sem mudança de piso. Checklist de review: não aplicável.
    Pronto-quando verificado: o plano passa nas 5 condições de G-PLANREADY (checklist no rodapé do
    próprio plano); os dois pontos que exigem ato do dono (`V2K-T11` ramo B, `V2K-T16`) são tarefas
    com entregável e critério de parada, **não** questões em aberto.
  - Consumo: ~28 tool uses (contados), tokens **NÃO MEDIDOS** — executada *inline* pelo orquestrador
    em Opus (fase intelectual: autoria de plano), sem subagente e portanto sem bloco `<usage>`.

### Estágio 3A — `P-0729-v2-melhoria` [backlog — desbloqueado pelo Estágio 2 em 2026-07-29; executado como **Bloco B**, depois de `V2K-T1..T4`]

- `V2M-T1` — Redigir a doutrina nova em `GOVERNANCA.md` §7 — 5 guardrails + **gate de publicação** (G-PLANREADY item 5) — [Opus] — backlog *(herdado de `P-0722` Fase 1; abre o Bloco B)*
- `V2M-T2` — Skill global `modelo-por-fase` — [Sonnet] — backlog *(herdado de `P-0722` Fase 2)*
- `V2M-T3` — Promover G-PLANFIDELITY/G-EXECREADY ao CLAUDE.md global — [Sonnet] — backlog *(herdado de `P-0722` DP-G4; **depois de `V2K-T4`**, que é a régua de residência)*
- `V2M-T4` — Contador sequencial de planos (`P-NNNN`) — [Sonnet] — backlog *(herdado de `P-0722` DP-G5)*
- `V2M-T5` — Check executável de código morto testado (G-DEADCODE) — [Sonnet] — backlog *(herdado de `P-0722` Fase 3; script próprio, ver DK-7 do Estágio 3B)*

### Estágio 3B — `P-0729-v2-melhoria-candidatos` [in progress — 1/19, nascido fechado em 2026-07-29 pela `V2C-T6`]

19 tarefas, cada uma com o `C-NN` de origem. Ordem normativa em `docs/plans/P-0729-v2-melhoria-candidatos.md`
§2 — **Bloco A** (`T1..T4`) antes do Estágio 3A; **Bloco C** (`T5..T19`) depois dele.

**Bloco A — enforcement executável e régua de residência**
- `V2K-T1` — Validador estrutural do kit (`.claude/checks/kit_check.ps1 -Mode validate`) — [Sonnet] — done *(`C-01`a)*
  - Resultado: `.claude/checks/kit_check.ps1` criado com `-Mode validate` (parâmetro já aceita `generate`/`check-drift`, não implementados — reservados p/ `V2K-T2`). Valida: frontmatter `name`+`description` de cada `.claude/agents/*.md` (`tools` opcional e só sintático, por causa de `pantonic-executor.md` sem essa linha); frontmatter `name`+`description` de cada `.claude/skills/*/SKILL.md` com `name` == diretório; paridade `VERSION` == `.claude/KIT_VERSION`. Execução real: exit 0, "kit_check: OK - 9 agente(s) e 8 skill(s) validados; VERSION == KIT_VERSION ('1.2.0')." Execução negativa (cópia sintética no scratchpad, agente sem `description`): exit 1, "Agente sem campo 'description' no frontmatter: ...\kit_copy_v2kt1\.claude\agents\synthetic-bad.md" — cópia removida após o teste.
  - Veredito: suítes — não aplicável (hub sem pytest/app Python); piso de regressão — sem mudança (nenhum teste existente tocado).
  - Consumo: 17 tool uses, ~55k tokens, Sonnet, ~36min (medido no `<usage>` da notificação; teto informado era 15 — estouro de 2, reportado pelo executor: 5 chamadas de exploração de frontmatter porque o dossiê citou `executor.md` em vez de `pantonic-executor.md`).
- `V2K-T2` — Gerador do `.claude/README.md` + detecção de deriva — [Sonnet] — backlog *(`C-01`b; defeito medido: 8/9 agentes, 6/8 skills)*
- `V2K-T3` — Doutrina do enforcement em §9 + entrada no `guardrails-check` + bump `1.3.0` — [Opus] — backlog *(`C-01`c)*
- `V2K-T4` — Tabela de precedência e residência da doutrina (`GOVERNANCA.md` §3) — [Opus] — backlog *(`C-03`; destrava `T6`, `T10`, `T16` e `V2M-T3`)*

**Bloco C — o resto, por dependência e I÷E**
- `V2K-T5` — Allowlist de subcomandos destrutivos (`.claude/settings.json` + §7) — [Sonnet] — backlog *(`C-02`)*
- `V2K-T6` — Teto de contexto graduado por classe de tarefa — [Opus] — backlog *(`C-04`; depende de `T4` e `V2M-T1`)*
- `V2K-T7` — Checkpoint de perda de contexto não planejada — [Opus] — backlog *(`C-05`; depende de `T6`)*
- `V2K-T8` — `file:line` + comando de validação no dossiê — [Sonnet] — backlog *(`C-06`; depende de `V2M-T1`)*
- `V2K-T9` — Gatilho de revisão e deprecação da doutrina — [Opus] — backlog *(`C-07`; depende do Estágio 3A inteiro)*
- `V2K-T10` — Inbox de memória: fila + promoção pelo dono — [Opus] — backlog *(`C-10` adaptar; depende de `T4`)*
- `V2K-T11` — Commits assinados + verificação no sync (versão mínima) — [Sonnet] — backlog *(`C-08` adaptar; ramo B medido)*
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
