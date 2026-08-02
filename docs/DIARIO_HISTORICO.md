# Diário Histórico — PantonicApp

> Arquivo append-only. Seções condensadas do docs/DIARIO_DE_OBRAS.md quando o diário ativo
> passa de ~500 linhas ou domina por itens done/cancelled/superseded. Nunca editar
> retroativamente — só apensar.

---

## Tíquetes avulsos — condensado em 2026-08-01

- `TK-01` — **done, absorvido pela `V2M-T3` (2026-07-30).** Achado fora de escopo (`V2M-T2`,
  2026-07-30): `GOVERNANCA.md` §3 (linha ~64) e o bullet da `V2M-T1` em `CHANGELOG.md` 1.4.0 ainda
  descreviam a skill `modelo-por-fase` como "global" em `~/.claude/skills/`. `DM-7` (mesmo dia,
  commit posterior a `V2M-T1`) rebaseia essa decisão: a skill nasceu no kit versionado
  (`.claude/skills/modelo-por-fase/`). Corrigido pelo dono no mesmo ato da `V2M-T3` (decisão
  2026-07-30, mesma superfície de doutrina) em vez de tarefa própria — grep de confirmação em
  ambos os arquivos registrado no fechamento da `V2M-T3`.


---

## SPRINT-PANTONICV2 — Estágios 1, 2 e 3A (concluídos, condensado em 2026-08-01)

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

### Estágio 3A — `P-0729-v2-melhoria` [in progress — 2/5, Bloco B aberto em 2026-07-30 depois de `V2K-T1..T4`]

- `V2M-T1` — Redigir a doutrina nova em `GOVERNANCA.md` §7 — 5 guardrails + **gate de publicação** (G-PLANREADY item 5) — [Opus] — done *(herdado de `P-0722` Fase 1; abre o Bloco B)*
  - Resultado: `GOVERNANCA.md` §7 passou de **8 para 13 guardrails** (386 linhas, era 325) — itens 9-13 = `G-DEADCODE`, `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY` (5 condições) e `G-EXECREADY`, cada um com regra + `*Enforcement:*` explícito, transcritos do `P-0722` §2 sem reabrir a discussão. O **item 5 de G-PLANREADY** (gate de publicação, decisão do dono 2026-07-29) entrou com as três partes: regra, consequência operacional (plano com vão divide-se em dois; o dependente nasce como última tarefa do plano que produz o insumo) e enforcement nas três superfícies.
  - Materialização nos artefatos do kit: `pantonic-executor.md` ganhou G-EXECREADY como **passo 1** do protocolo (recusa antes de qualquer edição; os passos antigos 1-5 viraram 2-6, e o passo 4 herdou a deleção da rota abandonada por G-DEADCODE); `proximo-passo/SKILL.md` ganhou o **gate G-PLANREADY** antes do gate de delegação; `diario-de-obras/SKILL.md` ganhou o gate de publicação dentro da operação "Registrar plano". `GOVERNANCA.md` §3 ganhou o bullet do **gatilho operacional do modelo por fase**, com a residência resolvida pela régua de §3.1 (regra = doutrina versionada; skill = gatilho; hook = enforcement).
  - Bump: `VERSION` e `.claude/KIT_VERSION` em **`1.4.0`** (paridade OK), seção `## 1.4.0 — 2026-07-30` no `CHANGELOG.md`, commit + tag anotada `kit-v1.4.0` sobre esse commit (sem push).
  - **Desvio de rótulo (numeração de versão):** o `P-0729-v2-melhoria-candidatos` §2 previa `1.4.0` no **fim do Bloco C**, mas o Bloco B entra no meio e §10 obriga bump em toda tarefa que edite `.claude/` ou a doutrina. O Bloco B ocupa o `1.4.0`; **o fechamento do Bloco C passa a ser `1.5.0`**. Rótulo do plano é estimativa, a regra de §10 é normativa.
  - Veredito — V2M-T1
    Suítes: não aplicável — hub sem código de aplicação (só doutrina + `.claude/`). Gate executável rodado: `kit_check.ps1 -Mode validate` → exit 0 ("9 agente(s) e 8 skill(s) validados; VERSION == KIT_VERSION ('1.4.0')") e `-Mode check-drift` → exit 0 (`.claude/README.md` sem deriva).
    Piso: sem mudança de piso.
    Checklist de review: sem import/camada/MVVM/UI thread tocados. G-DEADCODE não se aplica (nenhum símbolo novo). `GOVERNANCA.md` em 386 linhas — abaixo do gatilho de 500 do DOC_MAP.
  - Consumo: **NÃO MEDIDO** — execução inline no orquestrador (Opus), sem notificação de subagente e portanto sem bloco `<usage>`; contagem própria ~40 tool uses, marcada como autoestimativa.
- `V2M-T2` — Skill `modelo-por-fase` do kit — [Sonnet] — done *(herdado de `P-0722` Fase 2)*
  - Resultado: `.claude/skills/modelo-por-fase/SKILL.md` criada **no kit versionado**, não global
    (`DM-7` rebaseia `DP-G3`): três gatilhos (início de tarefa/subagente, troca de fase na mesma
    sessão, nudge do hook), gate de parada (`/model` explícito ao dono, nunca decisão/troca
    própria) e a convenção de anúncio da Regra 5 — ponteiro para `GOVERNANCA.md` §3/§3.1 em vez de
    recopiar a doutrina. Hook global (`~/.claude/hooks/modelo_por_fase_userpromptsubmit.py`)
    revisado: falso positivo medido (prompt de retomada de backlog — "execute a próxima tarefa" —
    classificado como execução mecânica quando o trabalho real era orquestração/delegação, fase
    intelectual) corrigido com lista de exclusão `_ORCHESTRATION_ENTRYPOINT` checada antes da
    classificação de execução; verificado com 4 casos manuais via subprocess (carve-out, execução,
    intelectual, leitura) — todos batendo a fase esperada.
    Achado fora de escopo indexado como `TK-01` (seção `## Tíquetes avulsos`): `GOVERNANCA.md` §3
    e o bullet `V2M-T1` do `CHANGELOG.md` ainda apontam a skill como global — resíduo do rebase
    `DM-7`, fora dos arquivos-alvo desta tarefa.
  - Bump: nenhum (paridade `1.4.0` mantida — Bloco B é uma única release); bullet novo apensado à
    seção `## 1.4.0 — 2026-07-30` já existente do `CHANGELOG.md`; tag anotada `kit-v1.4.0` apagada
    e recriada sobre o commit desta tarefa (nunca publicada — sem `-f`, sem push).
  - Veredito — V2M-T2
    Gate executável rodado: `kit_check.ps1 -Mode generate` → "9 agente(s), 9 skill(s)"; `-Mode
    check-drift` → exit 0 ("README.md == regenerado"); `-Mode validate` → exit 0 ("9 agente(s) e 9
    skill(s) validados; VERSION == KIT_VERSION ('1.4.0')"). Hook: 4 casos manuais (subprocess),
    todos OK — sem suíte pytest aplicável (hook fora da árvore de testes do repo).
    Piso: sem mudança de piso (hub sem suíte de aplicação).
    Checklist de review: sem import/camada/MVVM/UI thread tocados. G-DEADCODE não se aplica
    (nenhum símbolo deletado). Nenhum arquivo fora dos arquivos-alvo foi reescrito.
    Desvio de orçamento: ~23 tool uses contra teto de 22 — sinalizado, não escondido (a maior
    parte do excedente veio de uma falha de ambiente recuperável: `python3` ausente no shell,
    retry com `python` resolveu em 1 chamada extra).
  - Consumo: 25 tool uses, ~78k tokens, Sonnet, ~49min (medido no `<usage>` da notificação; teto informado era 22 — estouro de 3, coerente com o "~23" autorrelatado, mas o medido é o que entra na série).
- `V2M-T3` — Promover G-PLANFIDELITY/G-EXECREADY ao CLAUDE.md global — [Sonnet] — done *(herdado de `P-0722` DP-G4; **depois de `V2K-T4`**, que é a régua de residência; `TK-01` absorvido no mesmo ato)*
  - Resultado: `~/.claude/CLAUDE.md` ganhou a **Regra 8** — condensação de G-PLANFIDELITY (rota é
    do dono) e G-EXECREADY (executor não decide, não pergunta, recusa plano não-pronto) numa
    única regra (15 linhas), por serem conduta universal de executor e não doutrina específica de
    Pantonic. Arquivo passa de 150 para 165 linhas (medido: `wc -l` → 165) — abaixo do teto de
    200. `GOVERNANCA.md` itens
    10 e 13 (§7) reescritos como ponteiro para a Regra 8 (nome do item e *Enforcement* mantidos,
    corpo normativo não duplicado). `TK-01` absorvido: `GOVERNANCA.md` §3 (linha ~64) e o bullet
    `V2M-T1` do `CHANGELOG.md` 1.4.0 corrigidos — a skill `modelo-por-fase` passa a ser descrita
    como residente no kit versionado (`.claude/skills/modelo-por-fase/`), não `~/.claude/skills/`;
    o hook segue global. `CHANGELOG.md` 1.4.0 ganhou bullet próprio da `V2M-T3`.
  - Grep de confirmação (pronto-quando item 3): `Grep "modelo-por-fase" GOVERNANCA.md CHANGELOG.md`
    → única ocorrência restante de "global" associada à skill é a frase "o hook (global) é
    enforcement" / "hook global" — sobre o **hook**, não a skill; nenhuma menção residual da
    skill como global.
  - Memória de origem (Regra 6 do CLAUDE.md global): grep `executor.*rota|nao decide|plano
    incompleto|não decide|plano incompleto` em todos os `~/.claude/projects/*/memory/` → zero
    hits (complementa o grep prévio de `planfidelity|execready|...`, também zero). Nenhuma
    memória a remover.
  - Veredito — V2M-T3
    Não aplicável: mudança é só doutrina/texto (`~/.claude/CLAUDE.md`, `GOVERNANCA.md`,
    `CHANGELOG.md`) — sem código de aplicação, sem suíte pytest, sem gate `kit_check.ps1` (nenhum
    agente/skill tocado). G-DEADCODE não se aplica (nenhum símbolo novo). Escopo estrito: só os
    4 arquivos-alvo listados na delegação foram tocados; G-DEADCODE/G-PREMISE não tocados em
    `GOVERNANCA.md` (DP-G4 preservada); nenhum outro item de §7 renumerado ou reescrito.
    Piso: sem mudança de piso (nenhuma suíte de teste nesta tarefa).
  - Consumo: 29 tool uses, ~71k tokens, Sonnet, ~3h13min (medido pelo `<usage>` da notificação).
- `V2M-T4` — Contador sequencial de planos (`P-NNNN`) — [Sonnet] — done *(herdado de `P-0722` DP-G5)*
  - Resultado: `GOVERNANCA.md` §7 (`G-PLANREADY` item 1) já continha a regra completa desde a
    `V2M-T1` — confirmado por `Grep "P-NNNN" GOVERNANCA.md`, não reescrito. `docs/plans/_INBOX.md`
    ganhou o cabeçalho de registro do contador (`P-NNNN-<slug>.md`, data como campo do plano, não
    do nome do arquivo) com a linha literal **Próximo id de plano: P-0730** (maior id registrado
    era `P-0729`); grandfathering explícito dos planos `P-0721`..`P-0729` (mantêm o nome atual,
    não renomeados — DP-G5); cláusula obsoleta sobre o `DIARIO_DE_OBRAS.md` "a ser criado" trocada
    pelo ponteiro direto ao arquivo (já existe). Superfícies do kit alinhadas:
    `.claude/skills/diario-de-obras/SKILL.md` (linhas ~105 e ~153, `P-<MMDD>` → `P-NNNN`, e a
    operação "Drenar inbox de planos" ganhou a regra de alocação do id: maior registrado + 1,
    atualizando a linha de próximo id do `_INBOX.md` no mesmo ato) e
    `.claude/skills/bootstrap-pantonic/SKILL.md` (linha ~41, árvore de diretórios). `CHANGELOG.md`
    1.4.0 ganhou bullet próprio da `V2M-T4`. Nenhum arquivo em `docs/plans/` renomeado.
  - Verificação de aceite: (1) `Grep "P-<MMDD>"` em `.claude/` e `docs/plans/_INBOX.md` → zero
    ocorrências. (2) `kit_check.ps1 -Mode check-drift` → sem drift (nenhuma skill/agente
    adicionado ou removido). (3) `git status --short` → só `M`, nenhum `R`/rename.
  - Consumo: 24 tool uses, ~55k tokens, Sonnet, ~7min26s (medido pela notificação de conclusão;
    o autorrelato do executor dizia 14 tool uses — subestimativa de ~42%, mesmo padrão da Regra 7).
- `V2M-T5` — Check executável de código morto testado (G-DEADCODE) — [Sonnet] — done *(herdado de `P-0722` Fase 3; script próprio, ver DK-7 do Estágio 3B; continuação 2026-07-30: 3 rodadas de ajuste estrutural — a 3ª é a última, autorizada pelo dono — concluídas; destravado pela campanha de limpeza no `PantonicVideo`)* **Nota (2026-07-31, `PantonicVideo` T17):** baseline do `PantonicVideo` confirmado em `exit 0` (`python .claude/checks/dead_code.py --root D:\workspaces\PantonicVideo` via PowerShell, 0 achados) — `SPRINT-DEADCODE` fechada formalmente naquele repo (`docs/plans/P-0730-limpeza-codigo-morto.md` §8 T17), destravando o fechamento desta `V2M-T5`. Status não alterado nem fechamento executado aqui — tarefa deste hub, fora de escopo da nota.
  - **Fechamento formal (2026-08-01):** as duas verificações do "Pronto quando" reconfirmadas ao
    vivo via PowerShell nesta sessão — `python .claude/checks/dead_code.py` (root = PantonicApp) →
    `OK - 0 achado(s)`; `--root D:\workspaces\PantonicVideo` → `OK - 0 achado(s)`; fixture sintética
    recriada no scratchpad (`services/service.py` com `orphan_helper` referenciado só por
    `tests/test_service.py`, `main.py` como entry point de produção chamando só `used_helper`) →
    exit 1, exatamente 1 achado, fixture removida em seguida. Wireado como item 6, bloqueante, do
    "Checklist executável" de `.claude/skills/guardrails-check/SKILL.md`. Estágio 3A fechado 5/5.
  - Consumo: 41 tool uses, ~76k tokens, Sonnet, ~5min12s (medido pela notificação de conclusão;
    autorrelato do executor dizia ~31 tool uses — subestimativa de ~24%, mesmo padrão da Regra 7).
  - Método do check (inalterado desde a sessão anterior): alcançabilidade por AST a partir de
    entry points (`contracts/`, `__main__`/bootstrap, `entry_point` de `manifest.json`),
    propagação por grafo de import, casamento por nome simples para referência
    (`Name`/`Attribute`/decorator/anotação), auto-vivo para dunder e decorador Pydantic invisível
    ao AST.
  - **Rodada 1** (`integrations/poc/**` vira seed de alcançabilidade por construção de diretório,
    mesmo desenho de `contracts/` — POCs standalone sem bootstrap comum): família caiu de 30 para
    10 achados (delta −20; não −30 como hipotetizado — os 10 residuais são símbolos sem nenhuma
    referência textual mesmo com o módulo já enraizado).
  - **Rodada 2** (causa raiz corrigida em `_resolve_import_targets`): para
    `from .adhoc.X import Y` (import relativo, `node.level>0`) o código descartava `node.module`
    ("adhoc.X") e resolvia o alvo só para o pacote-pai — o submódulo nunca entrava em
    `reachable_modules`. Caso de controle confere: `ProjectRepository.read_metadata` e
    `ScriptStore.get_script` saíram da lista. Efeito real menor que a hipótese de −57: só
    `services/*/adhoc/**` usa import relativo (27 → 11, delta −16); `plugins/*/adhoc/**` sempre
    importou por caminho absoluto (confirmado em `plugins/screenwriter/view_model.py:42`,
    `from plugins.screenwriter.adhoc import ...`) — já estava alcançável antes da correção e
    ficou **inalterado em 30** (bug diferente do hipotetizado; a estimativa original juntou duas
    causas sob o mesmo rótulo `*/adhoc/*`).
  - **Baseline: 131 → 95** (`python .claude/checks/dead_code.py --root D:\workspaces\PantonicVideo`,
    medido agora). Residual **95 > teto de 30** desta continuação — parei conforme critério
    explícito, sem abrir 3ª rodada. Classificação por área:

    | achados | área | leitura |
    |---|---|---|
    | 30 | `plugins/*/adhoc/**` | não tocada pela rodada 2 (import absoluto); mistura de overrides Qt por despacho de framework (`paint`/`columnCount`/`headerData`/`mimeData`/`fixup`) com possíveis órfãos reais |
    | 17 | `infracore/ui_shell` | untouched pelas 2 rodadas; mesmo padrão de override Qt (`DockManager`, `TitleBar`, `MainWindow`) — candidato a nova categoria de despacho dinâmico, não a bug de propagação |
    | 15 | `plugins/*` (fora de `adhoc/`) | `view_model.py` de vários plugins — properties/métodos Qt-bindáveis sem uso textual encontrado (mesmo padrão do exemplo já verificado na sessão anterior, `AssetsManagerViewModel.results`) |
    | 11 | `services/*/adhoc/**` | residual pós-rodada 2 — módulo já alcançável, símbolo específico sem referência textual (órfão real ou uso só dinâmico) |
    | 10 | `integrations/poc/**` | residual pós-rodada 1 — módulo já enraizado, símbolo sem referência (órfão real na POC, ou duplicação não cruzada entre `dehydrator/` e `desidratar_subtitle/`) |
    | 7 | `infracore/*` (fora de `ui_shell`) | bootstrap/manifest/components — `_check_first_run`, `caret_match`, `ServiceManifest`, `unobserve_*`/`evict_idle_locks`/`_record_loaded` |
    | 5 | `tools/integration_agent/*.py:4 .run` | mesmo achado da sessão anterior, não investigado (fora do escopo das 2 rodadas aprovadas) |

  - Caso negativo sintético (fixture em scratchpad, `services/service.py` com `orphan_helper`
    referenciado só de `tests/`): reproduzido após as 2 rodadas — exit 1, 1 achado exato, sem
    regressão.
  - Sem gate `kit_check.ps1` rodado (nada de agente/skill mudou) e sem commit de fechamento
    formal (entrada em `guardrails-check/SKILL.md`, `CHANGELOG.md`, bump de versão, tag ficam
    todos para o fechamento). Detalhe completo das 2 rodadas em
    `docs/plans/P-0729-v2-melhoria.md` §"Achados da execução".
  - **Decisões do dono (2026-07-30), tomadas sobre o residual de 95:**
    1. **Rodada 3 autorizada, e é a ÚLTIMA.** Nomear "override de virtual Qt" como categoria de
       despacho dinâmico (auto-vivo) — mesma forma das regras que o script já tem para validator
       Pydantic e plugin registry, logo não é allowlist de conveniência. Motivo: é defeito
       sistemático **do check**, não do `PantonicVideo`; sem isso ele desfoca em todo projeto
       PySide6 da família. Alvo estimado ~62 dos 95 (`plugins/*/adhoc` 30 + `infracore/ui_shell`
       17 + `plugins/*` 15) — tratar 62 como **teto, não promessa**: as duas estimativas
       anteriores erraram para menos (−30→−20, −57→−16). Qualquer que seja o residual, **não há
       4ª rodada**.
    2. **Fecho por gate bloqueante, com limpeza antes.** O "Pronto quando" original da T5 fica
       **inalterado**: o check só é aceito com o baseline do `PantonicVideo` em `exit 0`. Zerar
       por allowlist está descartado (95 entradas negariam o próprio check). **Consequência
       registrada:** a limpeza dos achados reais remanescentes no `PantonicVideo` entra no
       caminho crítico da `PANTONIC-V2` e **não está planejada nem orçada** — precisa de entrada
       própria no backlog daquele projeto antes de a `V2M-T5` poder fechar. Risco declarado ao
       dono na tomada de decisão e por ele assumido.
  - **Rodada 3 (a última, executada 2026-07-30)** — nova categoria de despacho dinâmico "override
    de virtual Qt", mesma forma estrutural das regras de validator Pydantic e entry class de
    `manifest.json` (não allowlist de diretório/classe): um método `M` de classe `C` é
    `auto_alive` se `C` é Qt-derivada (alguma base direta ou transitiva casa `^Q[A-Z]`, resolvida
    globalmente sobre todas as `trees` do `--root`, por nome simples/atributo terminal — não por
    arquivo) **e** o nome simples de `M` está em `_QT_VIRTUAL_METHODS` (conjunto novo em
    `dead_code.py`, ao lado de `_INVISIBLE_DISPATCH_DECORATORS`: virtuais de model/view, delegate,
    validator, item gráfico e eventos de widget). Aplicado só no cálculo de `method_auto`
    (`dead_code.py`, dentro do laço de classe) — caminho de `function`/`class` intocado.
    **Delta medido:** 95 → 86 achados (`python .claude/checks/dead_code.py --root
    D:\workspaces\PantonicVideo`, exit 1) — os 9 casos de controle (`AssetsIndexModel.mimeData`,
    `RowImageTableModel.columnCount`/`headerData`, `TargetRectItem.paint`,
    `SubtitleTableModel.columnCount`/`headerData`, `ClipItem.paint`,
    `LenientDoubleSpinBox.fixup`, `PlacementSpanItem.paint`) confirmados fora da saída por grep,
    zero hits cada. Delta real (−9) ficou na ponta baixa da faixa esperada (~9 a ~15) — a
    estimativa-teto de ~62 do dono (explicitamente rotulada teto, não promessa) não se
    confirmou: `infracore/ui_shell` (17), `plugins/*` fora de `adhoc` (15), `services/*/adhoc`
    (11), `integrations/poc` (10), `infracore/*` (7) e `tools/*` (5) ficaram **inalterados** —
    só `plugins/*/adhoc` moveu (30 → 21), terceira vez que uma estimativa de rodada erra para
    menos (mesmo padrão de −30→−20 na rodada 1 e −57→−16 na rodada 2).
  - **Classificação do residual (86) por área**, medida agora, para a campanha de limpeza:

    | achados | área |
    |---|---|
    | 21 | `plugins/*/adhoc/**` |
    | 17 | `infracore/ui_shell` |
    | 15 | `plugins/*` (fora de `adhoc/`) |
    | 11 | `services/*/adhoc/**` |
    | 10 | `integrations/poc/**` |
    | 7 | `infracore/*` (fora de `ui_shell`) |
    | 5 | `tools/*` |

  - **Piso de regressão confirmado**: fixture sintética recriada no scratchpad
    (`services/service.py` com `orphan_helper` referenciado só de `tests/test_service.py`) →
    `dead_code.py` ainda dá exit 1 com exatamente 1 achado. `PantonicVideo` permaneceu somente
    leitura — nenhum arquivo daquele repositório tocado.
  - **Próximo passo:** não há 4ª rodada (decisão do dono é definitiva, qualquer que fosse o
    residual). Falta só a campanha de limpeza no `PantonicVideo` — sem entrada no backlog daquele
    projeto ainda — e, depois dela, o fechamento formal da T5 (gate bloqueante: baseline em
    exit 0, sem allowlist de 86 entradas).
  - **Decisão do dono, 2026-07-30 (fecho da rodada 3):** a premissa sob a qual o risco havia sido
    assumido mudou — o residual esperado era ~33 (95 − ~62 estimados) e o medido é **86**. Com o
    fato novo à mesa, o dono **reafirmou a rota**: abrir a campanha de limpeza no `PantonicVideo`
    **agora**, com a `PANTONIC-V2` parada até ela concluir. Descartadas explicitamente: (a)
    bloquear a `V2M-T5` por dependência externa e liberar o Bloco C em paralelo (seria exceção à
    DK-1); (b) rever o gate de fecho e aceitar baseline não-zero como dívida registrada (seria o
    próprio modo de falha que a `G-DEADCODE` existe para impedir). A próxima tarefa, portanto, é
    de **planejamento [Opus] no backlog do `PantonicVideo`**, não deste projeto.
  - Consumo: 31 tool uses, ~94k tokens, Sonnet, ~19min32s (medido pela notificação de conclusão;
    dentro do teto de 30 na prática — as 31 chamadas incluem o commit final). Acumulado da `V2M-T5`
    nas duas sessões anteriores: 81 tool uses, ~237k tokens, ~92min.
  - Consumo (rodada 3): 33 tool uses, ~77k tokens, Sonnet, ~62min (medido no `<usage>` da
    notificação; teto informado era 30 — estouro de 3, **não reportado** pelo executor, que
    autorrelatou "30 tool uses — dentro do teto" no handover: primeiro caso da série em que a
    subestimativa cai exatamente sobre a linha do teto e o converte em falso "dentro"). Acumulado
    da `V2M-T5` nas três sessões: 114 tool uses, ~314k tokens, ~154min.


---

## Tíquetes avulsos — 2ª condensação (2026-08-01)

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

## SPRINT-PANTONICV2 — Estágio 3B: contexto encerrado e tarefas `T1..T12b` (condensado em 2026-08-01)

> Movido do `docs/DIARIO_DE_OBRAS.md` na 2ª condensação (gate aberto pela `V2K-T12b`, resolvido
> pelo dono em 2026-08-01: condensar antes de delegar a `V2K-T13`). O Estágio 3B seguia
> `in progress` (13/20) no momento da condensação — o que veio para cá é o **contexto já
> encerrado**; as tarefas em aberto (`T13..T19`) permanecem no diário ativo.

### Contexto encerrado do preâmbulo de `## SPRINT-PANTONICV2`

O bloco abaixo é a ficha da `V2K-T12` inteira (`done`), preservada como contexto do `C-09`:

`V2K-T12` — Registro de consumidores e versões instaladas
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
3, `docs/CONSUMIDORES.md` 1, `GOVERNANCA.md` §10 1. **Pré-requisito resolvido em 2026-08-01:** o
`TK-02` (achatamento de `Get-ExcludedKeys` em `.claude/sync-kit.ps1`) foi corrigido antes e sozinho,
porque a `V2K-T12` verifica executando o script e o exige funcional — ver nota de fechamento em
`## Tíquetes avulsos`.

**Partida em duas no pickup de 2026-08-01** (a própria ficha mandava avaliar; 8 clusters
comportamentais é o teto do gate, e a série medida diz que executor não para no teto — T3 56/35,
T4 61/40, T5 112/50). Corte na fronteira produtor × consumidor do carimbo, detalhado em
`docs/plans/P-0729-v2-melhoria-candidatos.md` §T12:
- **`V2K-T12a`** — `sync-kit.ps1` escreve `<child>/.claude/kit/SYNC_STATE`;
  `docs/CONSUMIDORES.md` nasce semeado com 6 linhas. ~4 clusters. **`done` em 2026-08-01.**
- **`V2K-T12b`** (a tarefa da vez) — `kit_check.ps1 -Mode consumers` + `GOVERNANCA.md` §10.
  ~4 clusters; verifica contra o `SYNC_STATE` real da `T12a`.

**`DK-13` fechada no mesmo pickup** (era plano aberto pelo `G-PLANREADY`): a coluna `modo` do
carimbo deriva de `$originSha` — não-nulo ⇒ `subtree`, nulo ⇒ `copia`. O valor já é computado em
`sync-kit.ps1:166`; zero chamadas de git adicionais.

**Roster re-derivado no pickup** (gate de delegação item 3 — número de aceite não se copia do
plano): 6 consumidores, **0/6** com `.claude/kit/` ou qualquer `KIT_VERSION`; skills 7/7/7/7/0/4
(`ContainerForAWS`, `Container`, `Scanlator`, `Patom`, `Monitor`, `Video`); só o `PantonicVideo` é
repositório git. Confere com o medido na abertura da ficha.

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

### Tarefas `V2K-T1..T12b` (done) — bullets de fechamento

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
- `V2K-T12a` — Carimbo `SYNC_STATE` no consumidor + registro semeado (`docs/CONSUMIDORES.md`) — [Sonnet] — done *(`C-09`; partição de `T12` no pickup de 2026-08-01)*
  - Mudou: `.claude/sync-kit.ps1:365-388` — bloco novo após o `Write-Host` de resumo do sync
    efetivo (`:363`), inalcançável sob `-Check` porque os dois ramos `-Check` já saem antes
    (`exit 1` em `:357`, `exit 0` em `:360`). Lê `Join-Path $kitRoot 'KIT_VERSION'` trimado (`unknown` se ausente),
    monta `synced_at` UTC ISO 8601 (`(Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')`),
    deriva `mode` de `$originSha` (já calculado em `:166`, reusado — nenhuma chamada git nova):
    `subtree` se não-nulo, `copia` se nulo. Escreve as 3 linhas via `Set-Content -Encoding
    utf8NoBOM` em `Join-Path $kitRoot 'SYNC_STATE'`. `.DESCRIPTION` (`:45-50`) ganhou parágrafo
    documentando o carimbo. `docs/CONSUMIDORES.md` (novo) — cabeçalho de 4 colunas literal +
    parágrafo de proveniência + as 6 linhas semeadas do roster medido em 2026-08-01, coluna
    `Consumidor` com caminho absoluto de cada um dos 6 projetos em `D:\workspaces\`.
  - Verificação (sandbox no scratchpad, `.claude/kit/` com `sync-kit.ps1` editado + `KIT_VERSION`
    (`1.4.0`) + skill dummy + agent dummy, sem `kit-exclude.txt`, sem git):
    - Passo 1 (sem `-Check`):
      ```
      WARN: sync-kit - origin commit <unresolved: no commit found for this kit path, git missing, or not a git repo> is not signature-verified (git verify-commit failed or unavailable). Proceeding without signature verification. Re-run with -RequireSignature to enforce.
      sync-kit: 2 copied, 0 skipped by exclusion.
      ---SYNC_STATE---
      version=1.4.0
      synced_at=2026-08-01T22:38:45Z
      mode=copia
      ```
      (`mode=copia` porque o sandbox não é repositório git ⇒ `$originSha` nulo — esperado.)
    - Passo 2 (apagado o `SYNC_STATE` do sandbox, rodado com `-Check`):
      ```
      WARN: sync-kit - origin commit <unresolved: no commit found for this kit path, git missing, or not a git repo> is not signature-verified (git verify-commit failed or unavailable). Proceeding without signature verification. Re-run with -RequireSignature to enforce.
      sync-kit -Check: clean, 2 managed artifact(s) match the kit (0 excluded).
      exitcode=0
      ---SYNC_STATE exists?---
      False
      ```
      Confirma que `-Check` não recria o carimbo.
  - Veredito: as 3 chaves nascem no sync efetivo no formato prescrito; `-Check` não escreve;
    `docs/CONSUMIDORES.md` existe com cabeçalho e 6 linhas semeadas. Sem mudança de piso de
    regressão (hub sem suíte pytest/app Python, sem `tests/conformance/`; escopo é PowerShell +
    doc). Gates bloqueantes do kit rodados no repo real: `kit_check.ps1 -Mode validate` →
    `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION == KIT_VERSION ('1.4.0').` (exit
    `0`); `-Mode check-drift` → `kit_check: check-drift OK - .claude/README.md == regenerado (9
    agente(s), 9 skill(s)).` (exit `0`); `dead_code.py` →
    `dead_code: OK - 0 achado(s) sob 'D:\workspaces\PantonicApp'.` (exit `0`). Nada tocado em
    `.claude/checks/kit_check.ps1` nem `GOVERNANCA.md` (reservado à `V2K-T12b`).
  - Consumo: 38 tool uses, ~87k tokens, Sonnet, ~9min24s (medido no `<usage>` da notificação; teto
    informado era 25 — **estouro de 13**, o executor não parou no checkpoint. Causa auto-relatada:
    round-trips de verificação não orçados (guarda de listagem recursiva do PowerShell abortou a
    montagem do sandbox e exigiu refazer; 2 idas extras de Read/Grep para confirmar âncoras
    `file:line` antes de citá-las no diário) + o custo próprio das skills de fechamento
    (`guardrails-check`, `handover`, `diario-de-obras`). O alvo em si não teve thrashing: 2 Edits,
    de primeira. **Leitura para a calibragem de `DK-4`:** o teto de 25 foi fixado pelos ~4 clusters
    da partição, mas ignorou o piso fixo de fechamento — a partição corta o custo do alvo, não o
    overhead de sandbox + skills.)
- `V2K-T12b` — Coletor `kit_check.ps1 -Mode consumers` + `GOVERNANCA.md` §10 — [Sonnet] — done
  *(`C-09`; depende de `T12a`; fecha o `C-09` junto com `T12a`)*
  - Mudou: `.claude/checks/kit_check.ps1:28` (`consumers` adicionado ao `ValidateSet`);
    `.claude/checks/kit_check.ps1:282-341` (ramo `elseif ($Mode -eq 'consumers')` — lê
    `docs/CONSUMIDORES.md` a partir de `Split-Path -Parent $KitRoot`, localiza a tabela pelo
    cabeçalho exato, para cada linha de dado testa `<Consumidor>/.claude/kit/SYNC_STATE`: se
    existe, parseia `chave=valor` e reescreve as 3 colunas derivadas; se não existe, preserva a
    linha semeada como está; só escreve o arquivo se `$updated -gt 0`). `GOVERNANCA.md:476-480`
    (`§10`, item novo `(c)` na forma de `(a)`/`(b)`: declara `docs/CONSUMIDORES.md` derivado do
    carimbo `SYNC_STATE` via `kit_check.ps1 -Mode consumers`, coluna `Consumidor` única entrada
    manual). Nada tocado em `.claude/sync-kit.ps1`, `.claude/README.md`; `docs/CONSUMIDORES.md`
    não foi editado à mão — só como saída do modo novo rodando (ficou byte-idêntico no repo
    real, ver abaixo).
  - Verificação: sandbox no scratchpad (`t12b_sandbox/`, dois consumidores sintéticos —
    `consumerA` com `.claude/kit/SYNC_STATE` de 3 chaves, `consumerB` sem carimbo — e uma cópia
    de `docs/CONSUMIDORES.md` apontando para os dois). Rodando
    `kit_check.ps1 -Mode consumers -KitRoot <sandbox>/.claude`:
    ```
    kit_check: consumers OK - 1 atualizado(s) por carimbo, 1 permanece(m) semeado(s).
    ```
    exit `0`; a linha do `consumerA` passou a `| ...consumerA | 1.4.0 | 2026-08-01T22:38:45Z |
    copia |` (valores reais do carimbo); a linha do `consumerB` permaneceu
    `| ...consumerB | semeada — não verificada por sync | — | — |`; a prosa fora da tabela e o
    cabeçalho ficaram intactos. No repo real, `kit_check.ps1 -Mode consumers` (sem `-KitRoot`,
    resolve `.claude/` do hub):
    ```
    kit_check: consumers OK - 0 atualizado(s) por carimbo, 6 permanece(m) semeado(s).
    ```
    exit `0`, batendo com "0/6 consumidores têm `.claude/kit/` hoje"; `git status --short
    docs/CONSUMIDORES.md` veio vazio (byte-idêntico ao versionado — o coletor não tocou o
    arquivo por não achar carimbo em nenhum dos 6). Gates bloqueantes do kit no repo real:
    `-Mode validate` → `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION ==
    KIT_VERSION ('1.4.0').` (exit `0`); `-Mode check-drift` → `kit_check: check-drift OK -
    .claude/README.md == regenerado (9 agente(s), 9 skill(s)).` (exit `0`); `dead_code.py` →
    `dead_code: OK - 0 achado(s) sob 'D:\workspaces\PantonicApp'.` (exit `0`).
  - Veredito — `V2K-T12b`
    ```
    Veredito — V2K-T12b
    Suítes: n/a (hub sem suíte pytest/app Python; escopo é PowerShell + doc). Tocou apenas o
      kit e GOVERNANCA.md — não é contracts/infracore/serviço compartilhado, sem recomendação de
      passe completo.
    Piso: sem mudança de piso (hub não tem tests/conformance/ nem suíte de regressão)
    Kit: kit_check -Mode validate exit 0 / -Mode check-drift exit 0 / dead_code.py exit 0
    Checklist de review: camadas n/a (script PowerShell, não código em camada) | ACL n/a |
      MVVM n/a | UI thread n/a | sinais/Pydantic n/a | mirror discipline n/a | nenhum teste
      deletado às cegas: ok | decision record: ok (segue DK-12/DK-13 já registrada, sem
      bifurcar rota)
    ```
    `C-09` (`T12a` + `T12b`) entregue por inteiro: metade produtora carimba em cada consumidor,
    metade coletora deriva `docs/CONSUMIDORES.md` a partir do carimbo, hub nunca edita o registro
    à mão.
  - Consumo: 25 tool uses, ~79k tokens, Sonnet, ~17min09s (medido no `<usage>` da notificação; teto
    informado era 35 — **dentro do teto**, 10 de folga. Confirma a calibragem lida na `T12a`: teto
    que soma o alvo (~4 clusters) ao piso fixo de fechamento (sandbox + `guardrails-check` +
    `handover` + edição do diário) para no lugar certo, enquanto o teto derivado só dos clusters
    (25 na `T12a`) estourou em 13.)
