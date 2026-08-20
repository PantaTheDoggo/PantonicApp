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

## SPRINT-PANTONICV2 — Consolidação do framework em V2

**Objetivo:** confrontar o framework PantonicApp com a prática pública registrada, corrigir o que
o confronto apontar, e entregar um `README.md` a partir do qual um humano decida sobre o framework
sem abrir nenhum outro arquivo — tudo sob controle de versão, fechando em `2.0.0` (objetivo
original, atingido no Estágio 4; com a `DE-7` de 2026-08-07 o fechamento da iniciativa passou a ser
o **congelamento do número em `0.0.0`** — `TK-14`, `V2E-T9a`..`T9d`).

**`V2E-T4` partida em três fatias (orquestrador, 2026-08-06):** o dossiê `### T4` do plano cobre 8
artefatos com **31 ocorrências** medidas de `perfil|PySide|MVVM|Qt` (`redacao-doc` 4,
`guardrails-check` 3, `proximo-passo` 1, `integrar-poc` 4, `bootstrap-pantonic` 10, `audit-sweep` 3,
`pantonic-auditor-arch` 4, `pantonic-executor` 2) ≈ **20 write-clusters**, muito além do teto de 8
do gate de delegação (`.claude/skills/proximo-passo/SKILL.md`, gate item 5). Corte por coerência de
vocabulário, cada fatia ≤ 8 clusters, todas fechando a bateria do §3 e regenerando o
`.claude/README.md`; o dossiê do plano permanece a autoridade de escopo e o somatório das três é
exatamente a `T4`:

- **`T4a` — cadeia de verificação de arquitetura:** `.claude/agents/pantonic-auditor-arch.md`,
  `.claude/agents/pantonic-executor.md`, `.claude/skills/guardrails-check/SKILL.md` (9 ocorrências).
  Os três carregam a *mesma* regra de fronteira MVVM e a mesma menção a Qt na pureza de domínio —
  uma decisão de vocabulário aplicada três vezes.
- **`T4b` — bootstrap e varredura mecânica:** `.claude/skills/bootstrap-pantonic/SKILL.md`,
  `.claude/skills/audit-sweep/SKILL.md` (13 ocorrências). Os dois removem o mecanismo de declaração
  de perfil (`.claude/PERFIL`; blocos `ARCH-mvvm` e `PYSIDE`).
- **`T4c` — skills de processo:** `.claude/skills/integrar-poc/SKILL.md`,
  `.claude/skills/redacao-doc/SKILL.md`, `.claude/skills/proximo-passo/SKILL.md` (9 ocorrências).

**`V2E-T5` partida em duas fatias (orquestrador + decisão do dono, 2026-08-06):** o gate
`G-PLANREADY` reprovou o dossiê original — ele prescrevia "`tests/` do hub (teste novo)" e
verificação por "suíte de testes do hub", e o hub **não tem suíte** (medido no pickup: nenhum
`tests/`, nenhum `test_*.py` rastreado, nenhuma configuração de pytest, `python -m pytest
--collect-only` em exit 5; as convenções `tests/` da `GOVERNANCA.md` §4.4 são das aplicações
consumidoras). Onde a prova comportamental mora é decisão de arquitetura de verificação, não do
executor. Decisão do dono: o hub ganha suíte própria, e a bateria de fechamento do §3 do plano
passa a ter um quarto passo (`python -m pytest`). O somatório das duas fatias é exatamente a `T5`:

- **`T5a` — suíte de testes do hub:** `pytest.ini` mínimo, `tests/fixtures/qt_project/` e
  `tests/test_dead_code.py` ancorando o comportamento **vigente** (o override de virtual em classe
  Qt-derivada não é acusado; o símbolo órfão do mesmo fixture é). Não toca `dead_code.py`.
- **`T5b` — a troca do mecanismo:** o dossiê original (`DE-5`) — `_QT_VIRTUAL_METHODS` e a
  heurística de classe Qt-derivada saem de `.claude/checks/dead_code.py` e viram
  `.claude/framework-virtuals.txt` opcional na raiz do projeto (seções `[bases]`/`[metodos]`, um
  nome por linha; arquivo ausente ⇒ nenhuma exceção concedida), mais
  `PantonicForDesktop/.claude/framework-virtuals.txt` com a tabela de Qt pronta para os
  consumidores desktop copiarem.

**`V2E-T9` partida em cinco fatias (planejador, 2026-08-07):** a reescrita do dossiê mediu ~23
blocos de edição contíguos (`VERSION` 1, `.claude/KIT_VERSION` 1, `CHANGELOG.md` 3, `README.md` 6,
`GOVERNANCA.md` §10 5, `GOVERNANCA.md` §7.1 6, `checar-versao-kit/SKILL.md` 6,
`docs/CONSUMIDORES.md` 1), quase o triplo do teto de 8 write-clusters do gate de delegação. O corte
é por **regime de dependência**, não por tamanho: nenhuma fronteira entre fatias pode deixar o
framework funcionalmente quebrado. O dossiê do plano permanece a autoridade de escopo e o somatório
das cinco é exatamente a `T9`:

- **`T9a` — a doutrina do congelamento** [Opus]: `GOVERNANCA.md` **§10** (bloco "Congelamento
  pré-lançamento", mecanismo, resultados da checagem, critério de pronto, paridade). Só a §10.
- **`T9b` — o gatilho da porta de saída** [Opus]: `GOVERNANCA.md` **§7.1** — `DE-8`: a revisão
  deixa de pender do fechamento de um MINOR e passa a pender do fechamento de um plano; escopo,
  janela da pergunta e transição passam a ser contados em rodadas, e o registro das rodadas ganha
  formato novo com a rodada `1.4.0` como marco zero.
- **`T9c` — o mecanismo executável** [Sonnet]: `.claude/skills/checar-versao-kit/SKILL.md` carrega
  as duas doutrinas — curto-circuito de congelamento no passo 1 (pula a rede, não encerra) e
  gatilho de revisão reescrito para ler o índice do diário em vez da versão —, mais
  `docs/CONSUMIDORES.md` e a regeneração de `.claude/README.md`. Entra **antes** da `T9d` de
  propósito: com o número já em `0.0.0` e a skill sem o curto-circuito, a primeira criação de plano
  compararia `0.0.0` com a tag `kit-v2.0.0` e reportaria "incompatível e para".
- **`T9d` — o número e o registro** [Sonnet]: `VERSION`, `.claude/KIT_VERSION`, `README.md:3` e
  `README.md:829` em `0.0.0`, e o `CHANGELOG.md` com `[Não lançado]` promovida a única seção viva,
  no topo (hoje ela está **abaixo** da `## 2.0.0`, anomalia física medida).
- **`T9e` — o espelho** [Opus]: `README.md` §13, a entrada de glossário da tag `kit-vX.Y.Z` e o
  parágrafo do apodrecimento em §10 (L700-702), espelho da abertura da §7.1.

**Reescrita do dossiê da `V2E-T9` em 2026-08-07 (`done`, planejador):** o `TK-14` invalidou a `T9`
como escrita — sem lançamento não existe compatibilidade publicada a quebrar, logo não há `3.0.0` a
fechar. A `DE-4` foi **revogada** no plano (com o texto original preservado e tachado) e entrou a
**`DE-7`**, que fecha o ponto que o `TK-14` deixava pendente: o número congela em `0.0.0` até o
dono publicar, e **o que já foi numerado permanece** — as 8 tags `kit-v*` não são tocadas (publicar
e despublicar tag é ato do dono), as seções `1.0.0`..`2.0.0` do `CHANGELOG.md` não são reescritas
(registro de trabalho feito não se apaga), e as duas passam a ser declaradas histórico de
desenvolvimento pré-lançamento. Trade-off registrado no plano: perde-se o número como contrato de
compatibilidade e a deriva passa a depender de `kit_check.ps1 -Mode check-drift`; o custo é
aceitável porque medido — `docs/CONSUMIDORES.md` registra **0/6 consumidores com `.claude/kit/`
instalado**, então nenhum consumidor real depende hoje da numeração. Reconciliados no plano: §5
(ordem de execução), §6 (risco dos consumidores), §7 (`V2I-T13` → `T9`) e §8. Achado novo:
**`TK-16`** — com o número congelado, o gatilho da porta de saída de guardrail (§7.1) não dispararia
e nenhuma regra poderia sair.

**Reconciliação com a `DE-8`, na mesma tarefa (2026-08-07):** o dono decidiu o `TK-16` no mesmo dia
— o gatilho de revisão passa a pender do **fechamento de um plano** (`P-NNNN` → `done` no índice
deste diário). A decisão entrou como **`DE-8`**, com o trade-off e as duas opções recusadas
(cadência por contagem de tarefas; suspensão até o lançamento) registrados no plano, e mudou o
desenho da `T9`: a §7.1 deixa de ser uma linha de suspensão dentro da `T9a` e vira **fatia própria**
(`T9b`), porque a mudança é maior do que o gatilho — escopo, janela da pergunta, período de
transição e formato do registro das rodadas passam todos de MINOR para rodada. A `T9` foi de quatro
para **cinco** fatias, com a `T9a` reduzida à §10. Efeito colateral medido: **`TK-05` fecha por
remoção** — sem leitura de versão no gatilho, a comparação de MINOR que ficava cega ao atravessar um
MAJOR some do procedimento, e não há correção a escrever. Índice atualizado: `TK-14` → `done`,
`TK-05` → `done`, `TK-16` → `decidido`.
Consumo: ver docs/telemetria.tsv

**`V2E-T9a` em 2026-08-07 (`done`):** a `DE-7` escrita na fonte da verdade. Alvo único —
`GOVERNANCA.md` §10 "Versionamento e atualização do kit", 5 write-clusters, exatamente os 5 itens
do "Conteúdo prescrito" do dossiê; nenhum outro arquivo tocado (§7.1 é da `T9b`, §9 não é alvo,
`VERSION` segue `2.0.0` e é da `T9d`). Edições aplicadas **de baixo para cima**, ancoradas por
conteúdo. (1) Bloco novo **"Congelamento pré-lançamento"** abre a seção logo após o parágrafo de
abertura: a versão é `0.0.0` e não anda até o dono publicar, mais os cinco efeitos enquanto
congelada — sem bump (a exigência dos três artefatos reduz-se a um, a linha no `CHANGELOG.md` sob
`[Não lançado]`); sem tag nova (a branch `kit` segue distribuindo, o que suspende é a criação de
`kit-v<versão>`); checagem sem comparação e sem rede; tags `kit-v*` e seções numeradas do
`CHANGELOG.md` preservadas como histórico de desenvolvimento pré-lançamento; descongelar como ato
do dono, que fixa a primeira versão publicada e reativa o mecanismo completo. (2) **Mecanismo**: a
residência de `.claude/KIT_VERSION` e a razão dela ficaram intactas; a publicação da tag vale a
partir do lançamento e a chamada de rede declara-se suspensa sob congelamento. (3) **Resultados
possíveis da checagem**: o rótulo perdeu o numeral "três" (a lista já tinha quatro bullets) e ganhou
o quinto, primeiro na ordem — versão congelada `0.0.0` → reporta "congelada — nada a comparar" e
encerra, sem rede; os quatro existentes ficaram com o texto atual, agora declarados como o mecanismo
em vigor a partir do lançamento. (4) **Critério de pronto** nos dois regimes: congelada, a linha no
`CHANGELOG.md`; fora dela, o bump — a razão ("versão que não sobe deixa a checagem cega") ficou
atribuída ao regime numerado. (5) **Paridade** exigida sem exceção (os dois carregam `0.0.0` sob
congelamento), semver com significado declarado operante a partir do lançamento, e "os três se
movem juntos" com a ressalva do congelamento. Redação sob `redacao-doc` §6: a varredura V3/V7
(`\bT[0-9]+|V2[A-Z]-T|Estágio [0-9]|SPRINT-|P-0[0-9]{3}|TK-[0-9]|AAAA-MM-DD`) não retorna **nenhuma
linha ≥ L642** — o rótulo `(V2B-T1)` do parágrafo da paridade saiu junto, e duas negações de
contraste (V9, "não estado válido") caíram pelo teste do apagamento. Nenhuma frase da §10 afirma o
que a §7.1 faz. Achado fora de escopo registrado como **`TK-17`**: as demais seções da
`GOVERNANCA.md` concentram 25+ ocorrências V3/V7 no corpo publicado.

```
Veredito — V2E-T9a
Suítes: bateria do §3 do plano, os quatro em exit 0 — kit_check -Mode validate, kit_check
  -Mode check-drift, check-readme.ps1, python -m pytest (3 verdes). Tier 3 não se aplica:
  a tarefa não toca código (doc de doutrina, arquivo único).
Piso: ratchet_piso.py exit 0 — nenhum piso declarado (hub sem tests/piso_comportamental.txt).
Kit: kit_check -Mode validate e -Mode check-drift — exit 0; VERSION == KIT_VERSION ('2.0.0');
  .claude/README.md sem deriva (não foi tocado — a tarefa não mexe em agente nem skill).
Espelho: check-readme.ps1 exit 0 — 7 agentes, 10 skills, 14 guardrails, versão '2.0.0',
  14 seções com Fonte da verdade válida (string idêntica ao baseline de abertura).
Morto: dead_code.py exit 0 — 0 achados.
Checklist de review: n/a em todos os itens de código (nenhum import, camada, sinal, contrato,
  thread ou teste tocado); nenhum teste deletado ou alterado.
```

Consumo: ver docs/telemetria.tsv

**`V2E-T9b` em 2026-08-07 (`done`):** a `DE-8` escrita na fonte da verdade. Alvo único —
`GOVERNANCA.md` §7.1 "Revisão e deprecação de guardrails", 6 write-clusters, exatamente os 6 blocos
do "Conteúdo prescrito" do dossiê; nenhum outro arquivo tocado (a skill `checar-versao-kit` é da
`T9c`, o espelho do `README.md` é da `T9e`). A seção passa a descrever o regime de **rodadas** sem
citar número de versão em nenhum ponto normativo. (1) **Abertura**: a unidade de crescimento da
doutrina passa de MINOR para **rodada de trabalho**; o argumento do apodrecimento e a declaração de
"porta de saída única" ficaram intactos. (2) **Gatilho** reescrito em três parágrafos — o que
dispara é o **fechamento de um plano** (`P-NNNN` → `done` no índice deste diário), nunca calendário
e nunca número de versão, preservada a razão original (o gatilho pendura-se no momento em que há
material novo para julgar) e declarado que cada fechamento abre uma rodada; quem detecta é a skill
`checar-versao-kit`, na criação do plano seguinte, confrontando o índice do diário com o registro
das rodadas, sem executar a revisão (tarefa nomeada, registro próprio); e o parágrafo de **atraso
aceito por desenho**, espelhado da skill (L85-87) com "MINOR" → "plano fechado". Escrito "plano
(`P-NNNN`)" e não "estágio", que é um plano como outro qualquer e ainda não tem residência
normativa (`TK-08`). (3) **Escopo**: `≥2 MINORs de idade` → **`≥2 rodadas de idade`** (as que já
constavam de §7 na **penúltima** rodada registrada), razão idêntica, mais a **regra de partida**
explícita — enquanto o registro não tiver duas rodadas deste regime, a rodada `1.4.0` faz as vezes
de penúltima. (4) **Pergunta única**: a janela "nos últimos 2 MINORs" → "desde a penúltima rodada
registrada"; o restante da pergunta e a definição de **caso citável** com as duas exclusões ficaram
literalmente intactos. (5) **Resultado**: `OBSOLETA desde <versão>` → **`OBSOLETA desde <rodada>`**,
identificada a rodada pelo plano que a disparou (`P-NNNN`); transição de "um MINOR" → **uma rodada**
e remoção "no MINOR seguinte" → **na rodada seguinte**; remoção como tarefa nomeada e caso citável
desfazendo a marcação, inalterados. (6) **Registro das rodadas**: o rótulo `**Registro das
rodadas:**` virou parágrafo que declara o **formato da entrada** (`<P-NNNN> — <AAAA-MM-DD>`, plano
disparador, guardrails avaliadas, as fora por idade e o resultado item a item), e a entrada `1.4.0`
ganhou uma linha final de conversão declarando-a **marco zero** (contam os planos fechados a partir
de 2026-08-01; tudo anterior está coberto por ela) — o corpo histórico L577-592 **não foi
reescrito**.

Fronteiras respeitadas: a linha do heading `### 7.1` não foi tocada (é o marcador de fim da
contagem de guardrails em `check-readme.ps1:186-193`) e a contagem seguiu em **14**; o parágrafo
"Caso citável" ficou intacto. **Insumo do `TK-17` aplicado** — piso de proveniência **zero** no
texto normativo da seção: o rótulo do parágrafo de isenção perdeu `(decisão do dono, 2026-08-01,
calibragem medida na rodada 1.4.0)` (era o `V2`/`V7` de L546), e a varredura `redacao-doc` §6 sobre
o intervalo da seção não retorna nenhuma linha de `V3`/`V7` no texto normativo. Duas ocorrências
sobrevivem, ambas justificadas: a menção a "reporta ao dono" no Gatilho é **papel**, não
interlocutor (`redacao-doc` §3), e a data na linha de marco zero é o próprio conteúdo (define quais
planos contam) dentro da entrada de **registro**, classe isenta pelo §5 — cujo corpo histórico o
dossiê manda preservar. Índice atualizado: `TK-16` → `done`.

```
Veredito — V2E-T9b
Suítes: bateria do §3 do plano, os quatro em exit 0 — kit_check -Mode validate, kit_check
  -Mode check-drift, check-readme.ps1, python -m pytest (3 verdes). Tier 3 não se aplica:
  a tarefa não toca código (doc de doutrina, arquivo único).
Piso: ratchet_piso.py exit 0 — nenhum piso declarado (hub sem tests/piso_comportamental.txt).
Kit: kit_check -Mode validate e -Mode check-drift — exit 0; VERSION == KIT_VERSION ('2.0.0');
  .claude/README.md sem deriva (não foi tocado — a tarefa não mexe em agente nem skill).
Espelho: check-readme.ps1 exit 0 — 7 agentes, 10 skills, 14 guardrails, versão '2.0.0',
  14 seções com Fonte da verdade válida (string idêntica ao baseline de abertura).
Morto: dead_code.py exit 0 — 0 achados.
Checklist de review: n/a em todos os itens de código (nenhum import, camada, sinal, contrato,
  thread ou teste tocado); nenhum teste deletado ou alterado.
```

Consumo: ver docs/telemetria.tsv

**`V2E-T9c` em 2026-08-07 (`done`):** o mecanismo executável de `DE-7`/`DE-8`. Alvos:
`.claude/skills/checar-versao-kit/SKILL.md`, `docs/CONSUMIDORES.md` e `.claude/README.md`
(regenerado por comando, nunca editado à mão). Cinco write-clusters na skill, exatamente os cinco
itens do "Conteúdo prescrito" do dossiê. (1) **Congelamento (curto-circuito)** — parágrafo novo ao
fim do passo 1 ("Resolver a versão local"): versão `0.0.0` → reporta "versão congelada em 0.0.0 —
nada a comparar", pula os passos 2 e 3 (nenhuma chamada de rede) e segue direto para o gatilho de
revisão; a skill não encerra aqui. Numeração 1/2/3 preservada. (2) **"Quando roda"**: a segunda
checagem deixa de aproveitar a leitura de versão — as duas passam a compartilhar só o momento de
invocação; sob congelamento a primeira para no passo 1 e a segunda roda assim mesmo. (3) **"Os
resultados possíveis"**: bullet novo primeiro — versão congelada → "congelada — nada a comparar",
sem rede e sem pergunta ao dono, segue para o gatilho; os quatro bullets existentes intactos. (4)
**"Gatilho de revisão da doutrina"** reescrito para a `DE-8`: roda sempre, congelada ou não; passo 1
lê a última rodada registrada em `GOVERNANCA.md` §7.1 (Grep `Registro das rodadas`); passo 2 lê o
índice do diário e lista os `done` (Grep `| done |`); passo 3 — plano `done` desde o marco zero
(`2026-08-01`) fora de toda rodada registrada ⇒ pendente, reporta plano disparador, última rodada e
guardrails em escopo, sem executar a revisão aqui; passo 4 — nenhum plano fora das rodadas ⇒
silêncio. Parágrafo de atraso aceito por desenho mantido, "MINOR" → "plano". A comparação de
componente MINOR — e a cegueira ao atravessar MAJOR — saiu junto (`TK-05` fecha por remoção); a
distinção MAJOR × MINOR/PATCH da checagem de versão (passo 3 da seção 1) permanece intacta. (5)
`description` do frontmatter substituída literalmente pelo texto prescrito, sem `|`.
`docs/CONSUMIDORES.md`: nota acrescentada ao cabeçalho — sob congelamento a coluna `Versão
instalada` carrega `0.0.0` para todos e não distingue deriva; a deriva passa a ser detectada por
`kit_check.ps1 -Mode check-drift` no consumidor; tabela não tocada (é derivada). Índice do kit
regenerado (`kit_check.ps1 -Mode generate`) por causa da `description` nova; `.claude/README.md`
não editado à mão. O gatilho de revisão, lido isoladamente, não menciona versão em nenhum passo.

```
Veredito — V2E-T9c
Suítes: bateria do §3 do plano, os quatro em exit 0 — kit_check -Mode validate, kit_check
  -Mode check-drift, check-readme.ps1, python -m pytest (3 verdes). Tier 3 não se aplica:
  a tarefa não toca código (skill em Markdown + doc, sem import/camada/contrato tocado).
Piso: ratchet_piso.py exit 0 — nenhum piso declarado (hub sem tests/piso_comportamental.txt).
Kit: kit_check -Mode validate e -Mode check-drift — exit 0; VERSION == KIT_VERSION ('2.0.0');
  .claude/README.md regenerado e sem deriva (description da skill mudou, índice atualizado).
Espelho: check-readme.ps1 exit 0 — 7 agentes, 10 skills, 14 guardrails, versão '2.0.0',
  14 seções com Fonte da verdade válida.
Morto: dead_code.py exit 0 — 0 achados.
Checklist de review: n/a em todos os itens de código (nenhum import, camada, sinal, contrato,
  thread ou teste tocado); nenhum teste deletado ou alterado.
```

Consumo: ver docs/telemetria.tsv

**`V2E-T9d` em 2026-08-07 (`done`):** o congelamento vira fato observável — as quatro fontes do
número dizem `0.0.0`. `VERSION` e `.claude/KIT_VERSION`: `2.0.0` → `0.0.0`. `README.md:3`
(cabeçalho) e `README.md:829` (corpo, seção "Distribuição e versão"): valor entre crases trocado,
resto de cada linha intacto; `README.md:829` ganhou uma frase nova declarando o congelamento até
decisão de publicar, com ponteiro para `GOVERNANCA.md` §10 — o resto do §13 não foi tocado (é
escopo da `T9e`, próxima). `CHANGELOG.md`: preâmbulo (L1-9) ganhou um parágrafo novo — versão
congelada em `0.0.0` (`DE-7`), toda mudança canônica registrada sob `## [Não lançado]` enquanto
durar, seções numeradas abaixo permanecem como registro histórico das tags `kit-v1.0.0`..`kit-v2.0.0`
já publicadas, sem reescrita nem revogação. O bloco `## [Não lançado]` (antes vazio, L82-85) foi
removido do meio do arquivo e reinserido logo após o preâmbulo, antes de `## 2.0.0`, com o corpo
substituído por cinco entradas — perda do conceito de perfil no hub (`V2E-T1`..`T4c`), guardrail de
MVVM fora da lista (`V2E-T2`, 15 → 14), `dead_code.py` trocando constantes de Qt pelo
`framework-virtuals.txt` opcional (`V2E-T5b`), o próprio congelamento com reconciliação das
superfícies de versão (`V2E-T9a`, `T9c`..`T9e`) e o gatilho de revisão de guardrail passando de
"fechamento de MINOR" para "fechamento de plano" (`V2E-T9b`). Nenhuma seção numerada do
`CHANGELOG.md` foi alterada; nenhuma tag `kit-v*` foi tocada, publicada ou despublicada.

```
Veredito — V2E-T9d
Suítes: tarefa não toca código nem teste (VERSION, KIT_VERSION, README.md, CHANGELOG.md) — Tier 1/2
  não se aplicam; Tier 3 não recomendado (raio de explosão nulo em contracts/infracore).
Piso: ratchet_piso.py exit 0 — nenhum piso declarado (hub sem tests/piso_comportamental.txt).
Kit: kit_check -Mode validate e -Mode check-drift — exit 0; VERSION == KIT_VERSION ('0.0.0');
  .claude/README.md regenerado e sem deriva.
Espelho: check-readme.ps1 exit 0 — 7 agentes, 10 skills, 14 guardrails, versão '0.0.0',
  14 seções com Fonte da verdade válida.
Morto: dead_code.py exit 0 — 0 achados.
Checklist de review: n/a em todos os itens de código (nenhum import, camada, sinal, contrato,
  thread ou teste tocado); nenhum teste deletado ou alterado.
```

Consumo: ver docs/telemetria.tsv

**`V2E-T9e` em 2026-08-07 (`done`):** o espelho do `README.md` alcança as fontes reescritas pela
`T9a` (§9/§10) e pela `T9b` (§7.1); com esta fatia a `V2E-T9` fecha completa e o `DE-7`/`DE-8` estão
refletidos no contrato com o cliente. Nove itens do dossiê, oito deles no §13 e no glossário: a linha
`> Fonte da verdade:` do §13 passou a citar `GOVERNANCA.md` **§9 e §10** (espelhava as duas, declarava
uma); o parágrafo de semver manteve os significados de MAJOR/MINOR/PATCH e passou a declarar que bump,
movimento conjunto dos três artefatos e publicação de tag operam **a partir do lançamento**, enquanto
sob congelamento a mudança canônica só escreve a linha no `CHANGELOG.md` sob `[Não lançado]`; o
parágrafo da checagem de versão foi condensado — primeiro o desfecho vigente ("congelada — nada a
comparar", sem tocar a rede) e depois **uma** frase que continua nomeando os quatro desfechos
pós-lançamento (espelho condensado, nunca ponteiro nu); o parágrafo de `docs/CONSUMIDORES.md` ganhou a
cláusula de que, com todo consumidor em `0.0.0`, a coluna de versão instalada não distingue em dia de
defasado e a deriva se detecta por `kit_check.ps1 -Mode check-drift`; o **"Por quê"** ganhou a razão do
congelamento (número sem lançamento correspondente simula maturidade inexistente; `0.0.0` é o que a
régua semver reserva para desenvolvimento inicial); o **"Onde o gerente intervém"** ganhou
*descongelar é ato dele* — fixando a primeira versão publicada e reativando bump, tag e checagem — e o
critério de pronto bifurcado (linha no `CHANGELOG.md` sob congelamento, bump a partir do lançamento);
a entrada de glossário `Tag kit-vX.Y.Z` registra que a criação de tag nova fica suspensa e as
existentes permanecem como histórico. O nono item está fora do §13: o parágrafo do apodrecimento em
§10 do README trocou "a cada versão" por "a cada rodada de trabalho" e nomeou o gatilho pelo que a
§7.1 declara — o **fechamento de um plano**, no lugar de "gatilho periódico" —, mantendo intacta a
afirmação de que remover guardrail é ato registrado, com motivo, nunca erosão silenciosa. O parágrafo
"divergência é reportada, nunca aplicada por agente" não foi tocado (item 4 do dossiê, "não tocar"),
e as entradas de glossário `KIT_VERSION`, `sync-kit`, `Hub` e `Consumidor` também não — nenhuma
afirma número. Este parágrafo de §10 **não** tem guarda executável: `check-readme.ps1` não compara o
texto dele com a §7.1, então a fidelidade é responsabilidade desta fatia. Redação sob `redacao-doc`
§6: nenhuma data, tíquete, id de tarefa, versão anterior ou episódio motivador entrou no corpo
publicado; varredura de `V3`/`V7`/`V10` no `README.md` sem ocorrência nova.

```
Veredito — V2E-T9e
Suítes: tarefa não toca código nem teste (só README.md, prosa) — Tier 1/2 não se aplicam;
  Tier 3 não recomendado (raio de explosão nulo em contracts/infracore).
Piso: ratchet_piso.py exit 0 — nenhum piso declarado (hub sem tests/piso_comportamental.txt).
Kit: kit_check -Mode validate e -Mode check-drift — exit 0; VERSION == KIT_VERSION ('0.0.0');
  .claude/README.md regenerado e sem deriva.
Espelho: check-readme.ps1 exit 0 — 7 agentes, 10 skills, 14 guardrails, versão '0.0.0',
  14 seções com Fonte da verdade válida.
Morto: dead_code.py exit 0 — 0 achados.
Greps de fechamento da T9: padrão '2\.0\.0|3\.0\.0|kit-v3' em README.md, GOVERNANCA.md,
  .claude/skills/checar-versao-kit/SKILL.md e docs/CONSUMIDORES.md — 0 ocorrências (mantido);
  padrão 'MINOR' nos mesmos quatro — 5 ocorrências, todas de checagem de versão ou de definição
  de semver (GOVERNANCA.md:699 e :726, README.md:843 e :855, SKILL.md:66); nenhuma ligada a
  revisão de doutrina ou a idade de guardrail.
Checklist de review: n/a em todos os itens de código (nenhum import, camada, sinal, contrato,
  thread ou teste tocado); nenhum teste deletado ou alterado.
```

Consumo: ver docs/telemetria.tsv

**`V2E-T10` em 2026-08-07 (`done`):** auditoria de em que grau infracore e plugins estendem
CA+DDD hoje, no **Estágio 6** (`P-0731-V2E`, 20/21). Sweep mecânico fresco (`audit-sweep`, HEAD
`ea8f9e5`) + agente `pantonic-auditor-arch` (Opus) rodaram sobre `D:\workspaces\PantonicVideo`
(implementação de referência), **sem alterar código**. Saída:
`D:\workspaces\PantonicVideo\docs\audits\SWEEP_2026-08-07.md` e
`D:\workspaces\PantonicVideo\docs\audits\AUDIT_ARCH_2026-08-07.md`.

Resposta medida: `contracts/domain` estende DDD plenamente (VOs frozen, invariante no
construtor, comportamento na raiz do agregado). `infracore` estende CA como frameworks & drivers
e **por desenho não estende DDD** (allowlist §4.4 de 8 data classes — conforme, não omissão).
`plugins` estendem DDD na escrita (métodos do agregado) mas não na leitura (49 projeções
`list[dict]` em 14 módulos; só 5/15 anotam a porta com Protocol). **Ninguém estende a camada de
casos de uso** — 0 classes `UseCase`, orquestração dispersa em ViewModels (5.216 linhas/14) e em
`capcut_service` (781 linhas, 18 métodos) — esse é o vão que o `P-0732` (`T11`) precisa endereçar.

3 apontamentos de alta severidade no PantonicVideo (fora do escopo deste plano): erro tipado
inalcançável por plugins (`ProjectWriteOutsideError` preso em `services/`), ausência de artefato
de caso de uso, e rastreabilidade UC→código congelada na v1 (15 plugins, só 1 com UC mapeado).
O auditor recomendou `TK-ERRO-TIPADO`, `TK-USECASE-PILOTO` e `TK-UC-MANIFEST`. **Declinados pelo
dono em 2026-08-07, antes de qualquer registro** — o PantonicVideo está quase finalizado e não
receberá investimento em atualização do kit; nenhum tíquete foi aberto, nem lá nem aqui. O
declínio está anotado no próprio `AUDIT_ARCH_2026-08-07.md` para que auditoria futura não
reapresente os mesmos achados como novos. A decisão recai sobre a **ação**, não sobre a
**medição**: o achado permanece válido como insumo da `T11`.
4 dos 6 blocos do sweep anterior (2026-07-14) já não são desvio ou fecharam sozinhos
(PySide6/pydantic fora de `services/` são conformidade declarada; `pathlib.Path` em
`contracts/domain` é falso positivo; `FilesystemEvent` tem decision record `D-2.0.1`).

Consumo: ver docs/telemetria.tsv (linhas `V2E-T10-sweep-*` e `V2E-T10`)

**`V2E-T11` em 2026-08-07 (`done`):** autoria de `docs/plans/P-0732-v2-portas-do-core.md` —
**Estágio 7**, prefixo `V2P-` —, absorvendo a `V2I-T15` com o escopo corrigido pela `DE-6`.
**Fecha o `P-0731` em 21/21.** Nenhum código, skill, agente ou doutrina foi tocado: a entrega é o
plano mais os três registros (plano, `_INBOX.md` com o contador em `P-0733`, este diário).

O plano nasce **fechado** (G-PLANREADY): **10 tarefas** `V2P-T1..T10`, decisões `DI-1..DI-8`
resolvidas no ato do planejamento e **todas atribuídas a `planejamento`** — nenhuma questão
owner-gated pendente, nenhum bloco a preencher, nenhum ramo condicional. O insumo da `T10` acima
entrou por inteiro: o plano ataca as **duas metades do mesmo vão** — o core descrito pela
implementação e não pelo contrato (portas do infracore só existem como nomes) e a camada de casos
de uso sem artefato. Escopo: esquema fixo de cinco campos por porta para as 8 portas de runtime
(`T1`) mais superfície de entrada e execução assíncrona (`T2`, onde saem os últimos "UI thread" do
hub); residência do caso de uso em `plugins/<nome>/use_case.py` com campo `use_case` no manifesto
(`T3`); alinhamento da `GOVERNANCA.md` (`T4`); cadeia de auditoria e produção no kit (`T5`/`T6`);
rodada de guardrails (`T7`); espelho e registro (`T8`/`T9`); aceite do dono (`T10`).

Três limites que o planejamento fixou para não extrapolar: **nenhum código de `infracore` nasce no
hub** (`DI-2` — o hub é doutrina + kit e não tem camada de produção), **nenhum guardrail novo em
`GOVERNANCA.md` §7** (`DI-5` — o que faltava era objeto verificável para as verificações 8 e 9 que
já existem) e **nenhum verificador executável novo** (`DI-6` — verificador sem alvo é exatamente o
que `G-DEADCODE` proíbe, com `0/6` consumidores materializando o kit). A residência do caso de uso
(`DI-4`) não cria requisito: é a forma que o bloco `DDD-usecase` da skill `audit-sweep` já procura
(`^class \w+UseCase` por diretório de plugin, 0 ou >1 = divergência de `D9`) e que o corpus já
exige em "um caso de uso = um plugin = um manifest = um TF" — o que faltava era escrevê-la.

A **primeira rodada de revisão de guardrails do regime da `DE-8`** entrou como `V2P-T7`, rotulada
`P-0731` no registro de rodadas: o gatilho arma no fechamento de um plano e a skill o reporta na
criação do plano seguinte, que é este — deixá-la para "algum plano futuro" a transformaria no vão
que `G-PLANREADY` proíbe. E o encerramento é a revisão do `README.md` com veredito do dono
(`V2P-T10`, dever 2 de `G-README`), com `check-readme.ps1` como instrumento da atividade e nunca
como gate automático de pronto.

Consumo: ver docs/telemetria.tsv

**Sprint encerrada.** Os sete estágios estão terminais e o `P-0732` fechou 10/10 com o aceite do dono
ao `README.md` (`V2P-T10`). Os tíquetes avulsos que sobraram foram convertidos no
`P-0733-divida-do-hub`, plano único e fechado, que passa a ser o backlog vivo do hub — ver a seção
`## P-0733` deste diário.

**`V2E-T8` em 2026-08-07 (`done`):** 3ª rodada de aceite do `README.md` pelo dono. Veredito
**aprovado com ressalvas**, com a ressalva executada na mesma rodada. O corpo `§1..§14` passa nos
três testes do dossiê: descreve o framework governado, sem afirmação equivocada ou desatualizada, e
sustenta a decisão de adotar ou recusar. A ressalva tem duas partes. **(a)** Da §15 em diante o
documento abandona o estilo de doutrina e volta a narrar evento no passado — informação
transitória num espelho que deveria descrever só o estado corrente. **(b)** A própria premissa da
seção caiu: o framework nunca foi lançado em público, então não existe `V0`/`V1`/`V2` e o registro
de histórico de alterações é desnecessário (vira o `TK-14`, que atinge a `T9`).

Correção aplicada — **§15 inteira removida** (`README.md` L901-1021) mais a linha `| 15 | ... |` do
índice de seções: **1021 → 898 linhas** (−123, −12%). Nenhuma doutrina ficou órfã. O critério de
corte foi o do dono: relato de evento sai, doutrina canônica é incorporada ao corpo. Nada precisou
ser incorporado, porque a coluna "depois" das 17 linhas de "o que se modifica" e os 6 bullets de "o
que fica" descreviam o estado corrente, que já vive nos §1..§14 — verificado item a item, com a
âncora de cada um: piso comportamental e ratchet `README.md:387-392`; proibição de percentual de
cobertura como piso, meta ou critério de pronto `README.md:389-390`; cinco classes de orçamento
`README.md:286-302`; `docs/telemetria.tsv` como fonte única `README.md:804`; `kit_check.ps1` e os
quatro modos `README.md:744`; residência da doutrina `README.md:779-799`; checkpoint a 2/3 do teto
`README.md:636`; dossiê com `caminho:linha` e comando colado `README.md:371-372` e `README.md:609`;
`G-PLANREADY` e o desdobramento em dois planos `README.md:552-574`; contador `P-NNNN`
`README.md:554,574`; porta de saída de guardrail `README.md:701-703`; commits assinados e
`docs/CONSUMIDORES.md` derivado por script `README.md:862-866`; MAJOR reportado como incompatível
`README.md:853`; fila de candidatos a memória promovida só pelo dono `README.md:788,820`. O que era
relato de evento — a origem da avaliação (21 frameworks, 16 dimensões, os vereditos por dimensão),
os oito descartes com motivo, as duas ressalvas de método e a nota de migração da `2.0.0` — sai sem
destino novo: já reside em `docs/benchmark/CANDIDATOS.md`, nos planos `P-0729-*` e no
`CHANGELOG.md`. As referências ao número de versão que ficam são as duas que o guarda exige
(cabeçalho e "Versão vigente do framework", `README.md:3` e `README.md:829`) mais o mecanismo de
versionamento do §13, que é doutrina de distribuição e não histórico.

Medição da skill `redacao-doc` (§8): a varredura mecânica do §6 dá **o mesmo número antes e
depois** — `V1`, `V2`, `V4`, `V6`, `V7`, `V8` e `V10` em **0** ocorrências nos dois estados, e `V3`
em **4** linhas, todas genéricas e legítimas (`T1..Tn` como formato de plano `README.md:343,556`;
`S1-T3` e `TK-042` como exemplo de tabela `README.md:506-507`). Nenhuma exceção do §3 foi mantida.
O vício da §15 era **estrutural**, invisível à varredura, e a isenção do §5 da skill era o que o
autorizava — vira o `TK-15`. Bateria do §3 do plano, todos exit 0: `kit_check.ps1 -Mode validate`
(7 agentes, 10 skills, `VERSION == KIT_VERSION '2.0.0'`), `-Mode check-drift` (OK — `.claude/README.md`
== regenerado), `check-readme.ps1` (14 guardrails, **14** seções com Fonte da verdade válida, contra
15 antes) e `python -m pytest` (3 passed). Nenhuma referência cruzada quebrada (`§15` não era citado por nenhum ponto do corpo, e a
única citação de `§14` — `README.md:163` — segue válida porque não houve renumeração).
Consumo: ver docs/telemetria.tsv

**`V2E-T6` partida em duas fatias (orquestrador, 2026-08-07):** o dossiê `### T6` do plano é
fechado (nenhuma questão em aberto — o gate `G-PLANREADY` passa); a partição é **só de orçamento**.
Medidas no pickup: `perfil|PySide|MVVM|Qt|desktop` casa **24 linhas** do `README.md` distribuídas
em **11 regiões contíguas** ≈ 11 write-clusters, acima do teto de 8 do gate de delegação
(`.claude/skills/proximo-passo/SKILL.md`, gate item 5 — decisão do dono 2026-07-16). O dossiê do
plano permanece a autoridade de escopo e o somatório das duas fatias é exatamente a `T6`; ambas
fecham a bateria do §3 e preservam os invariantes estruturais (títulos `Anatomia do kit` e
`Os guardrails`, `> Fonte da verdade:` por seção numerada, numeração `## N.`, 10 skills na tabela,
`Quatorze` guardrails).

- **`T6a` — o mecanismo de perfil sai do contrato** (6 clusters): entrada `Perfil` do glossário
  (L80) e a menção a "padrão de apresentação do perfil" no bullet do `guardrails-check` (L102); §1,
  frase das modalidades cobertas (L175); §2, a linha de premissa sobre interface/plataforma (L211),
  a linha "mesmo perfil" da tabela de especialização (L244) e a subseção "Perfis: o que a
  modalidade acrescenta" inteira + o parágrafo do case de referência que autoriza citar Qt/MVVM/
  PySide6 como default do case (L252-268).
- **`T6b` — resíduos nas seções de operação e histórico** (5 clusters): §5, apresentação "que o
  perfil declarar" (L382); §11, linha do `guardrails-check` na tabela de skills (L759); §15, as três
  regiões que reclassificam stack fixo e desktop-first como perfil (L934, L950-951, L962-963). §10
  não tem ocorrência — nada a fazer lá.

**`V2P-T1` em 2026-08-07 (`done`):** primeira tarefa do Estágio 7 (`docs/plans/P-0732-v2-portas-do-core.md`) — o core do runtime deixa de ser uma tabela de componentes concretos e passa a ser
**oito portas com contrato explícito**. Alvo único, `ARQUITETURA_PANTONICA.md`, 3 write-clusters
mais 1 de reconciliação. §4 (título "Infracore — as oito portas de runtime do core [REPLICAR]"): a
tabela `Componente | Responsabilidade` de 8 linhas e o parágrafo solto "Ordem de boot" saíram; no
lugar, as 8 portas — sinais, estado, filesystem, log, registro de plugins, injeção, raiz de dados e
lifecycle de plugin — cada uma no esquema fixo de 5 campos do dossiê (responsabilidade / operações
em prosa, sem assinatura de linguagem / invariantes / modos de falha coerentes com a tabela de
contenção da §11 / implementação de referência em uma linha). A **ordem de boot** permaneceu na §4,
agora como invariante da porta de injeção, junto com a lazyness das factories; o preâmbulo declara
que o componente nomeado como implementação de referência é do case e vale como exemplo, nunca como
requisito. A linha `ui_shell` da tabela virou parágrafo terminal com o texto preservado — é alvo da
`T2` e não foi tocada. §5 (título "Contracts [REPLICAR estrutura; ESPECIALIZAR domínio]", alinhado
com a célula da tabela de camadas da §2): a enumeração das portas saiu de lá e a seção passou a
tratar só do pacote — instalável, SemVer própria, zero runtime, e as quatro classes de tipo que ele
reúne (portas como Protocols, mirror dos tipos de manifest, exceções de contrato,
`contracts/domain`); o parágrafo `**Domínio [ESPECIALIZAR]:**` ficou intacto. §2: a célula
`Conteúdo` da linha `infracore` passou a "As oito portas de runtime do core (§4) e as primitivas que
as realizam + a superfície de entrada da aplicação (`ui_shell`)", com a coluna `Pode importar`
intacta. Reconciliação de referência cruzada quebrada pela própria edição, no mesmo arquivo: §14,
itens 1 e 2 do checklist de bootstrap ("portas genéricas do §5" → "as portas do §4 declaradas como
Protocols"; "Componentes de bootstrap na ordem do §4" → "As primitivas que realizam as portas, na
ordem de boot do §4"). A numeração das seções não mudou (`DI-8`) e as marcações
`[REPLICAR]`/`[ESPECIALIZAR]` foram preservadas. `README.md` não precisou de correção: as entradas
do glossário que apontam para §4 e §5 descrevem infracore e contracts por capacidade, e continuam
verdadeiras. Aceite de modalidade medido: `Grep -iE "pyside|\bqt\b|mvvm|desktop"` em
`ARQUITETURA_PANTONICA.md` **0 → 0** — nenhuma ocorrência nova, e o resíduo "callbacks no UI thread"
do `TaskRunner` (§5) saiu junto com o bloco de portas genéricas, sem que a `T2` fosse invadida.
Redação: nenhum vício `V3` (id de plano/tarefa/estágio) nem `V7` (datação viva) no texto novo; as
negações que ficaram enunciam limite (egress único, plugin não alcança o registro de factories, a
porta de raiz de dados não escreve). Bateria de fechamento, os quatro em exit 0: `kit_check.ps1
-Mode validate` (7 agentes, 10 skills, `VERSION == KIT_VERSION '0.0.0'`), `-Mode check-drift` (OK),
`check-readme.ps1` (14 guardrails, 14 seções com Fonte da verdade) e `python -m pytest` (3 passed).
Sem achado fora de escopo. Restam `T2`..`T10` do plano.

Consumo: ver docs/telemetria.tsv

**`V2P-T2` em 2026-08-07 (`done`):** as duas portas em que a modalidade encosta no core passam a
ser declaradas como porta, sem vocabulário de interface gráfica. `ARQUITETURA_PANTONICA.md` §4 vai
de 8 para **10 portas**: a **superfície de entrada** (o parágrafo terminal que a `T1` havia deixado
intacto) e a **execução assíncrona** (que não existia como porta) entram no mesmo esquema de cinco
campos das outras oito. A superfície de entrada é descrita pelo que faz — expor o estado publicado
pelo núcleo, receber comando e encaminhá-lo ao caso de uso, expor os alertas da porta de log,
concentrar os tokens de apresentação quando a modalidade tiver apresentação, encerrar o lifecycle —
com o invariante de que o core não conhece a tecnologia que a realiza e a implementação pertence à
camada de modalidade, fora do hub. A execução assíncrona carrega a regra antiga com o vocabulário
novo: **trabalho pesado ou bloqueante nunca corre na thread que atende a superfície de entrada**, e
resultado e falha voltam no **contexto de origem da chamada** — não no do worker. Reconciliações no
mesmo arquivo: §2 (célula `Conteúdo` de `infracore`, "oito" → "dez"), §3 (comentário da linha
`ui_shell/`), §4 (preâmbulo, que agora nomeia as duas como as portas de contato com a modalidade, e
ordem de boot), §9 (condições de POC integrável), §11 (a linha "Task em worker" virou "Unidade
submetida à porta de execução assíncrona", com "a interface nunca congela" → "a superfície de
entrada nunca fica bloqueada") e §14 (item 4 do checklist de bootstrap, que era `MainWindow +
DockManager + AlertPanel + ShellViewModel`). Fora do documento canônico:
`.claude/skills/guardrails-check/SKILL.md` e `.claude/agents/pantonic-executor.md`, os dois últimos
pontos de "UI thread" do hub, mais `.claude/skills/bootstrap-pantonic/SKILL.md` (item 4 da mesma
sequência de bootstrap), encontrado na reconciliação. `TaskRunner` e `ui_shell` sobrevivem **só** no
campo *implementação de referência*, onde o preâmbulo da §4 já os declara como do case.
Verificação: `Grep -i "ui thread"` nos três artefatos-alvo → **vazio** (era 0/1/1);
`Grep -iE "MainWindow|DockManager|AlertPanel|ShellViewModel|QThread|pyside|\bqt\b|mvvm|desktop"` em
`ARQUITETURA_PANTONICA.md` → **0**, mantendo o piso da `T1`. `README.md` não precisou de correção —
o espelho não nomeia as portas individualmente. Redação: nenhum vício `V3` nem `V7` no texto novo.
Bateria de fechamento, os quatro em exit 0: `kit_check.ps1 -Mode validate` (7 agentes, 10 skills,
`VERSION == KIT_VERSION '0.0.0'`), `-Mode check-drift` (OK), `check-readme.ps1` (14 guardrails, 14
seções com Fonte da verdade) e `python -m pytest` (3 passed). **Execução interrompida por limite de
sessão da conta** com as edições já aplicadas e a bateria por rodar; o orquestrador mediu o estado
(`git status` + as varreduras de aceite), rodou a bateria e escreveu este registro — nada foi
re-executado a frio. Achado fora de escopo: `TK-20`. Restam `T3`..`T10` do plano.

Consumo: ver docs/telemetria.tsv

**`V2P-T3` em 2026-08-08 (`done`):** residência do caso de uso e segunda declaração de aderência
fechada com o medido. `ARQUITETURA_PANTONICA.md` (497 → 513 linhas): subseção nova `### 9.1 O
caso de uso dentro do plugin` em `## 9. Plugins e manifests` — mora em `plugins/<nome>/use_case.py`
numa classe `<Nome>UseCase` com um método público de execução, depende só de `contracts` (portas +
domínio) por injeção, `plugin.py`/adaptador de apresentação só invocam, exatamente um por plugin,
a POC de `adhoc/` não é o caso de uso (é orquestrada por ele) e o TF do plugin exercita o caso de
uso pela superfície dele. Manifest (§9) ganhou o campo obrigatório `use_case` (nome reconhecido
pelo dono, a mesma frase do PRD, único na base de plugins) e a validação no load ganhou o passo de
unicidade de `use_case`. §3 (árvore de pastas): a linha `plugins/<nome>/` passou a listar
`use_case.py`. §1 (golden rules): "Grau de aderência da implementação atual: NÃO AUDITADO"
substituído pelo estado medido — domínio conforme (DDD pleno), infracore conforme como *frameworks
& drivers* e sem DDD por desenho, plugins conformes na escrita e não na leitura, camada de
aplicação sem artefato até agora, endereçada pela residência de §9.1 — com evidência apontada para
os relatórios de auditoria de arquitetura em `docs/audits/` do repositório da implementação de
referência, sem id de plano/tarefa nem datação viva; a única ocorrência de id de plano do arquivo
(`T14` de `P-0730-v2-identidade.md`, em `ARQUITETURA_PANTONICA.md:107`) saiu por consequência da
mesma edição. `docs/DOC_MAP.md`: como o arquivo passou de 500 linhas (513), saiu da lista "abaixo
de 500 linhas" e ganhou entrada própria (`## ARQUITETURA_PANTONICA.md (raiz, ~513 linhas)`) com
âncoras de seção e padrão de Grep, no mesmo formato das entradas existentes. Verificação:
`Grep -iE "não auditado|nao auditado"` em `ARQUITETURA_PANTONICA.md` → vazio (era 1);
`Grep -E "P-07[0-9]{2}|V2[A-Z]-T"` no mesmo arquivo → vazio (era 1, `:107`); `wc -l` conferido
contra o gatilho de 500 do `DOC_MAP.md`. Bateria de fechamento, os quatro em exit 0:
`kit_check.ps1 -Mode validate` (7 agentes, 10 skills, `VERSION == KIT_VERSION '0.0.0'`),
`-Mode check-drift` (OK), `check-readme.ps1` (14 guardrails, 14 seções com Fonte da verdade) e
`python -m pytest` (3 passed). Tarefa de doutrina/prosa, sem TF/TR de código — a verificação é a
bateria de Grep do dossiê mais os quatro gates. Sem achado fora de escopo. Restam `T4`..`T10` do
plano.

**`V2P-T4` em 2026-08-08 (`done`):** a governança passa a dizer sobre o core o mesmo que a
arquitetura, sem duplicar o texto, e a segunda declaração de aderência não medida fecha. Quatro
pontos em `GOVERNANCA.md`. (1) §2: o bullet que declarava o core "doutrina agnóstica com
implementação de referência ainda ligada a uma stack concreta" e a abstração das portas como
"etapa própria e ainda não executada" foi **substituído** — o core é definido por **portas**, cada
porta é um **contrato**, o contrato é o que todo projeto herda (nunca o binding), e a
**implementação** pertence à camada que declara a tecnologia; as duas portas em que o mundo externo
encosta no núcleo (superfície de entrada e execução assíncrona) são realizadas pela camada de
modalidade, fora do core reusável; um plugin escrito contra a porta funciona sobre qualquer
implementação que honre o contrato. O texto afirma a regra e aponta para
`ARQUITETURA_PANTONICA.md` §4, onde os contratos moram porta a porta — vocabulário colado do §4/§9.1
escritos pela `T1`/`T3`, sem segunda cópia. (2) §2, tabela de graus de especialização: a linha de
infraestrutura deixou de dizer "Nenhuma — idêntico entre projetos da mesma stack" e passou a
distinguir os dois níveis — nenhuma na **porta** (contrato idêntico entre **todos** os projetos),
com a **implementação** idêntica só entre projetos da mesma stack. (3) §5: bullet novo nas
consequências operacionais — "O caso de uso é um artefato, não uma pasta", com residência própria
no plugin, dependência só de `contracts` e invocação pela apresentação, apontando para
`ARQUITETURA_PANTONICA.md` §9.1 como texto normativo; forma `DR-A` de
`docs/RESIDENCIA_DOUTRINA.md` (nome do item + frase de essência + ponteiro), nunca ponteiro nu nem
regra duplicada. (4) §5: "**Estado da aderência: não auditado.**" substituído por "**Grau de
aderência da implementação atual: medido.**", espelhando a forma que a `T3` usou em
`ARQUITETURA_PANTONICA.md:103` — plugins estendem DDD na escrita e não na leitura (49 projeções
`list[dict]` do agregado em 14 módulos; 5 de 15 plugins anotam a porta com `Protocol`) e a camada
de casos de uso sem artefato próprio no case (nenhuma classe de caso de uso; orquestração dispersa
em 14 adaptadores de apresentação, 5.216 linhas, e numa fachada de serviço de 781 linhas com 18
métodos públicos), com evidência nos relatórios de auditoria em `docs/audits/` do repositório da
implementação de referência e o vão fechado pela residência de §9.1. Nenhum id de plano, tarefa ou
tíquete e nenhuma datação viva entraram no corpo (`V3`/`V7` da skill `redacao-doc`); a evidência é
fato afirmado inline, e a implementação de referência aparece nomeada como referência, nunca como
regra. Verificação, os cinco em verde: `kit_check.ps1 -Mode validate` (7 agentes, 10 skills,
`VERSION == KIT_VERSION '0.0.0'`), `-Mode check-drift` (OK), `check-readme.ps1` (14 guardrails, 14
seções com Fonte da verdade), `python -m pytest` (3 passed) e
`Grep -iE "não auditado|nao auditado|ainda não executada"` em `GOVERNANCA.md` → vazio (era 2).
Nenhuma linha do `README.md` foi invalidada pela mudança (Grep pelas formulações antigas → vazio),
então o invariante 2 do plano não exigiu correção. Tarefa de doutrina/prosa, sem TF/TR de código.
`TK-17` (`P-0730` no preâmbulo de §7) não foi tocado, conforme o escopo. Sem achado novo fora de
escopo. Restam `T5`..`T10` do plano.

Consumo: ver docs/telemetria.tsv

Consumo: ver docs/telemetria.tsv

**`V2P-T5` em 2026-08-08 (`done`):** a cadeia de auditoria ganha objeto verificável — as
verificações 8 e 9 do `pantonic-auditor-arch` deixam de ser inauditáveis (`DI-5`). Dois pontos.
(1) `.claude/skills/audit-sweep/SKILL.md`, bloco `DDD-usecase` da tabela do passo 2: passou de
`^class \w+UseCase` agrupado por diretório para três coletas por plugin, na mesma célula de
tabela (forma preservada, como `DDD-pureza`/`DDD-vo` vizinhas) — existência de `use_case.py`,
`^class \w+UseCase` dentro dele e o campo `use_case` de `manifest.json`, com a regra de
divergência explícita (ausente, vazio ou repetido entre plugins). (2) `.claude/agents/pantonic-
auditor-arch.md`: verificação 9 ("Caso de uso por plugin") ganhou critério objetivo — um módulo
`use_case.py`, uma classe `^class \w+UseCase`, um campo `use_case` declarado no manifesto, nome
único entre plugins; verificação 8 ("Use cases finos") ganhou a regra de dependência — o módulo
depende só de `contracts`, e import de superfície de apresentação, serviço concreto ou lib externa
nele é desvio. Nenhum verificador executável novo (`DI-6`) e a régua de 12 verificações não ganhou
item novo — numeração 8/9 preservada, nenhuma linha renumerada. Tarefa de doutrina/prosa sobre
artefatos do kit, sem TF/TR de código (o objeto da tarefa é o critério que o auditor aplica, não um
check automatizado). Verificação, os quatro em exit 0: `kit_check.ps1 -Mode validate` (7 agentes,
10 skills, `VERSION == KIT_VERSION '0.0.0'`), `-Mode check-drift` (OK — `.claude/README.md` ==
regenerado), `check-readme.ps1` (14 guardrails, 14 seções com Fonte da verdade) e `python -m
pytest` (3 passed). Sem achado novo fora de escopo. `TK-17` não foi tocado, conforme o escopo.
Restam `T6`..`T10` do plano.

Consumo: ver docs/telemetria.tsv

**`V2P-T6` em 2026-08-08 (`done`):** o que a doutrina de `9.1` (`ARQUITETURA_PANTONICA.md`) passou
a exigir nasce por padrão em projeto novo e em POC integrada, fechando o vão entre regra e
produção. `.claude/skills/bootstrap-pantonic/SKILL.md`: fase 2 (Architecture) marca a residência do
caso de uso (`plugins/<nome>/use_case.py`, um `<Nome>UseCase` por plugin) como `[REPLICAR]`; fase 3
(Spec) passa a materializar o caso de uso como classe própria, com o campo `use_case` do manifesto
declarando o nome reconhecido pelo dono; fase 5 (árvore inicial) mostra `plugins/<nome>/` com
`manifest.json + plugin.py + use_case.py + adhoc/`. `.claude/skills/integrar-poc/SKILL.md`: o passo
3 (Dissecação) ganha o bullet **Caso de uso** como artefato de saída obrigatório da dissecção, ao
lado do inventário de dependências (passo 1) e do mapeamento para serviços (passo 2), com o bullet
`plugin.py` corrigido para rotear ao caso de uso em vez de direto a `adhoc`; o passo 4 (Manifest)
passa a gerar o campo `use_case`; a seção `## Saída` lista `use_case.py` entre os artefatos do
plugin. Nenhuma `description` de skill mudou, então `.claude/README.md` não precisou ser
regenerado (`kit_check.ps1 -Mode check-drift` confirma). Tarefa de doutrina/prosa sobre artefatos
do kit, sem TF/TR de código — o objeto é o que a skill produz por padrão, não um check automatizado.
Verificação, os quatro em exit 0: `kit_check.ps1 -Mode validate` (7 agentes, 10 skills, `VERSION ==
KIT_VERSION '0.0.0'`), `-Mode check-drift` (OK — `.claude/README.md` == regenerado),
`check-readme.ps1` (14 guardrails, 14 seções com Fonte da verdade) e `python -m pytest` (3 passed).
Sem achado novo fora de escopo; `TK-17` e `TK-20` não foram tocados, conforme o escopo. Restam
`T7`..`T10` do plano.

Consumo: ver `docs/telemetria.tsv`.

**`V2P-T7` em 2026-08-08 (`done`):** primeira rodada da porta de saída de guardrails
(`GOVERNANCA.md` §7.1) sob o regime da `DE-8`, disparada pelo fechamento do `P-0731`. Escopo: **13
dos 14** itens de §7 — `G-README` fora por idade —, identificados por nome/conteúdo porque a
numeração deslocou quando o guardrail de fronteira MVVM saiu na `V2E-T3a`. Coleta delegada a dois
`pantonic-scout` (hub e consumidor `PantonicVideo`); julgamento em Opus.

**Isentas por enforcement executável (6)** — check nomeado e **executado hoje** no consumidor
(`python -m pytest` sobre os quatro arquivos → **17 passed**, nenhum `skip`/`xfail`; o único
`pytest.skip` é guarda condicional de `plugins/` ausente, diretório que existe no consumidor):
item 1 regra de dependência → `tests/conformance/test_layer_imports.py`; item 2 ACL →
`tests/conformance/test_acl_no_external_in_plugins.py`; item 3 egress G6 →
`tests/conformance/test_filesystem_egress.py`; item 4 namespace de estado →
`tests/boundary/test_state_writer_namespacing.py`; item 5 gate de conformance → a própria suíte
bloqueante (as quatro acima no consumidor; no hub, `python -m pytest` como 4º passo da bateria de
fechamento de toda tarefa); item 13 allowlist de subcomandos destrutivos →
`.claude/settings.json` `permissions.deny`, 6 entradas ativas.

**Na pergunta (7) — todas com caso citável, 0 marcações:**
- **6 piso de regressão** → `V2E-T5a`: a suíte que ancorou o comportamento vigente do `dead_code.py`
  foi escrita **antes** da troca do mecanismo, e existiu só por causa do piso.
- **7 disciplina de contexto** → `TK-06`: o `DOC_MAP.md` mandando ler integralmente um doc de 644
  linhas virou achado registrado (a regra "doc grande via índice, nunca integral" agindo).
- **8 G-DEADCODE** → `DE-5` (a tabela de virtuais de Qt vira arquivo declarativo do projeto) e
  `DI-6` (recusa de criar verificador executável novo sem alvo — "verificador sem alvo é o que
  `G-DEADCODE` proíbe").
- **9 G-PLANFIDELITY** → `V2E-T5` (o executor parou diante de um dossiê que prescrevia suíte
  inexistente em vez de inventar rota) e `V2I-T3` (edição adjacente ao alvo classificada como
  consequência mecânica da decisão, não bifurcação).
- **10 G-PREMISE** → `V2I-T3` (perfil declarado "sem verificação própria ainda": vazio honesto, não
  vão) e `V2I-T4` (as duas declarações de aderência ficaram **NÃO AUDITADO** em vez de afirmar
  conformidade antes da medida).
- **11 G-PLANREADY** → `V2E-T5`: o gate **reprovou um dossiê já publicado** (prescrevia `tests/` do
  hub, que não existia) e forçou partição em duas fatias, com a decisão de arquitetura subindo ao
  dono.
- **12 G-EXECREADY** → o mesmo episódio pelo lado do executor: recusou performar e não decidiu no
  lugar de quem planeja ("onde a prova comportamental mora é decisão de arquitetura de verificação,
  não do executor").

**Registro:** entrada `P-0731 — 2026-08-08` no bloco *Registro das rodadas* de `GOVERNANCA.md` §7.1;
§7 **sem nenhuma** marcação `OBSOLETA desde`. Efeito na `T8`: o ramo condicional "§10 (contagem e
lista de guardrails, **se** a `T7` marcar algum item)" fica resolvido em **não** — a contagem de 14
permanece. **Achado novo: `TK-21`** — o ratchet do piso comportamental roda sem alvo em toda parte
(hub com suíte mas sem arquivo de piso declarado; `0/6` consumidores materializam `.claude/checks/`),
de modo que o único check do piso passa por vacuidade; não isentou o item 6 nesta rodada porque o
caso citável veio do registro, não do check.
Verificação, os quatro em exit 0: `kit_check.ps1 -Mode validate` (7 agentes, 10 skills,
`VERSION == KIT_VERSION '0.0.0'`), `-Mode check-drift` (OK), `check-readme.ps1` (14 guardrails —
contagem inalterada, 14 seções com Fonte da verdade) e `python -m pytest` (3 passed). Tarefa de
julgamento e registro: nenhum código, skill ou agente tocado; alvos exatamente os três do dossiê.
Restam `T8`..`T10` do plano.

Consumo: ver `docs/telemetria.tsv`.

**`V2P-T8` em 2026-08-08 (`done`):** o espelho segue a fonte — o `README.md` passa a descrever o core
por **portas** e o caso de uso com residência própria. Sete write-clusters (estimativa do dossiê: ~7;
teto de parada: 12), um único arquivo de conteúdo tocado.

- **Glossário:** `Infracore` passa a nomear as **dez portas** de runtime (sinais, estado, filesystem,
  log, registro de plugins, injeção, raiz de dados, lifecycle de plugin, superfície de entrada,
  execução assíncrona) e o esquema de contrato de cada uma — responsabilidade, operações,
  invariantes, modos de falha —, com a contagem citada como a fonte a declara (`ARQUITETURA_PANTONICA.md`
  §4). `Core pantônico` ganha a distinção contrato herdado × implementação da camada que declara a
  tecnologia. `Plugin` passa a citar o campo `use_case` do manifesto, o caso de uso em módulo próprio
  e o TF exercitado pela superfície do caso de uso, com ponteiro para §9.1. `Caso de uso` ganha
  residência (`plugins/<nome>/use_case.py`, classe `<Nome>UseCase`, método público de execução),
  dependência só de `contracts` por injeção e a regra "exatamente um por plugin".
- **§2:** a premissa 2 troca a lista de capacidades com "forma prescrita" pelas dez portas com
  responsabilidade, operações, invariantes e modos de falha prescritos, e declara que superfície de
  entrada e execução assíncrona são realizadas pela camada de modalidade, fora do core reusável. A
  linha de infraestrutura da tabela de graus de especialização passa a distinguir **porta** (contrato
  idêntico entre todos os projetos) de **implementação** (idêntica só entre projetos da mesma stack),
  espelhando `GOVERNANCA.md` §2.
- **§1:** o parágrafo de abertura passa a dizer que o core entregue é um conjunto de portas, cada uma
  um contrato de runtime realizado pelo consumidor na tecnologia que escolher; a linha "Arquitetura"
  da tabela de níveis ganha "portas de runtime".

O ramo condicional do dossiê ficou confirmado resolvido **em não**: §10 não foi tocada e a contagem
de guardrails permanece **14**.

Verificação: `check-readme.ps1` em exit 0 com o baseline literal preservado (7 agentes, 10 skills,
14 guardrails, versão '0.0.0', 14 seções com Fonte da verdade válida);
`Grep -iE "perfil|pyside|mvvm|\bqt\b|desktop"` no `README.md` → **0 ocorrências** (zero mantido);
bateria do §3 nos quatro em exit 0 (`kit_check.ps1 -Mode validate`, `-Mode check-drift`,
`check-readme.ps1`, `python -m pytest` — 3 passed). Varredura da `redacao-doc` §6 sobre as regiões
editadas: **0 ocorrências novas** de V1..V10; as ocorrências remanescentes de `T1..Tn`, `S1-T3` e
`TK-042` no `README.md` são o **esquema** do formato de sprint plan e do índice deste diário, e já
compunham o baseline. Nenhum achado fora de escopo, nenhum tíquete novo. Restam `T9`..`T10` do plano.

Consumo: ver docs/telemetria.tsv

**`V2P-T9` em 2026-08-08 (`done`):** registro canônico da mudança no único lugar vivo do histórico,
sob o congelamento em `0.0.0`. `CHANGELOG.md`, seção `## [Não lançado]`: cinco bullets novos
acrescentados após os cinco já existentes do Estágio 6 (que não foram tocados) — (1) o core descrito
por **dez portas de contrato** (as oito de runtime mais superfície de entrada e execução assíncrona),
com `GOVERNANCA.md`/`README.md` espelhando sem duplicar (`V2P-T1`, `T2`, `T4`, `T8`); (2) a
residência do caso de uso em `plugins/<nome>/use_case.py` e o campo obrigatório `use_case` do
manifesto, com a nota de migração — manifesto existente sem o campo não é reconhecido pela
validação de load até declará-lo, sem default silencioso (`V2P-T3`); (3) a cadeia de auditoria
(`audit-sweep` + `pantonic-auditor-arch`) com critério objetivo para caso de uso por plugin
(`V2P-T5`); (4) `bootstrap-pantonic`/`integrar-poc` produzindo a residência por padrão (`V2P-T6`);
(5) a primeira rodada da porta de saída de guardrails sob a `DE-8` (`V2P-T7`). Nenhum número de
versão novo, nenhuma seção numerada nova, nenhuma tag, nenhuma instrução de migração expressa por
número de versão — as seções `1.0.0`..`2.0.0` não foram reescritas. Verificação: bateria do §3, os
quatro em exit 0 (`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`,
`python -m pytest`); `Grep -E "3\.0\.0|kit-v3|bump"` no `CHANGELOG.md` → **1 ocorrência** no total
(a pré-existente da seção histórica `1.5.0`, não tocada) e **zero** dentro de `[Não lançado]`. Sem
achado fora de escopo. Restam `T10` do plano (dono).

Consumo: ver docs/telemetria.tsv

**`V2P-T10` em 2026-08-08 (`done`):** aceite do dono ao `README.md` — dever 2 de `G-README` e gate de
sentido do Estágio 7. Instrumento de paridade estrutural rodado na `V2P-T9`: `check-readme.ps1` em
exit 0, 14 guardrails e 14 seções com `> Fonte da verdade:` declarada. Veredito: **aprovado, sem
ressalva** — primeira rodada de aceite do documento canônico que passa sem reprovação nem correção na
mesma rodada. Fecha o `P-0732` (10/10) e, com ele, a `SPRINT-PANTONICV2`: os sete estágios estão
terminais (5 `done`, 2 `superseded`). O fechamento do plano **arma o gatilho da porta de saída de
guardrails** (`GOVERNANCA.md` §7.1, regime da `DE-8`), a ser reportado pela skill `checar-versao-kit`
na criação do próximo plano. O `TK-18` **permanece `blocked`**: sua condição registrada é o fim das
operações de construção, e `TK-22`, `TK-17`, `TK-15` e `TK-21` ainda editam fontes espelhadas pelo
`README.md`.

Consumo: n/a — tarefa do dono (veredito), sem execução de agente.

**`V2E-T7` em 2026-08-07 (`done`):** o dever 2 do `G-README` ganha residência de
**responsabilidade de papel**, em vez de existir só como prosa dentro do texto do guardrail.
`GOVERNANCA.md` §3, célula *Responde por* da linha **Planejamento** da matriz de
responsabilidades: o planejador passa a responder também pela revisão do README ao encerrar cada
sprint — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do
dono como aceite, e sprint planejada sem essa tarefa é plano incompleto; ponteiro para o texto
integral em §7 item 14. `.claude/agents/pantonic-planner.md`: item **4** de `## Suas
responsabilidades`, no padrão `DR-A` — condensado autossuficiente (a tarefa nomeada, rodar
`pwsh .claude/checks/check-readme.ps1`, o veredito do dono como único teste de sentido, o guarda
como instrumento e nunca gate de pronto) mais ponteiro para §3 e §7 item 14, sem cópia plena do
guardrail. Nada além dessas duas células/seções foi tocado: `README.md`, o texto do §7 item 14, a
numeração dos guardrails, a skill `handover` e `check-readme.ps1` ficam como estavam — nenhum gate
automático foi criado (`DR-8` preservado). O `description:` do frontmatter do agente não mudou,
então `.claude/README.md` não precisou ser regenerado. Critério de pronto re-derivado no
fechamento: `grep -in "revisão do README"` casa a linha do planejador na matriz da §3, o texto do
§7 item 14 e o item 4 do agente — o normativo está em **um só** lugar canônico e as demais
ocorrências são ponteiro ou o próprio guardrail. Bateria do §3 do plano, todos exit 0:
`kit_check.ps1 -Mode validate` (7 agentes, 10 skills, `VERSION == KIT_VERSION '2.0.0'`),
`-Mode check-drift` (OK), `check-readme.ps1` (14 guardrails, 15 seções com Fonte da verdade
válida) e `python -m pytest` (3 passed). Sem achado fora de escopo.
Consumo: ver docs/telemetria.tsv

**`V2E-T6b` em 2026-08-07 (`done`):** segunda e última fatia da `T6` (`DE-1`), que fica
**completa** — os resíduos de perfil e de tecnologia saem das seções de operação e de histórico do
`README.md`. Só `README.md` tocado, nos 5 clusters do dossiê. §5 (L356-357): o artefato Architecture
leva "o padrão de apresentação que o projeto escolher". §11 (L734): a célula do `guardrails-check`
na tabela de skills enumera "camadas, ACL, padrão de apresentação" — mesmo vocabulário que a `T6a`
deu ao verbete do glossário. §15 (histórica, segue congelada): o blockquote "Correção posterior"
(L908-911) diz que as premissas **de plataforma e de stack fixos** foram reclassificadas como
**escolha do projeto**, fora do núcleo (§2); o bullet **Identidade e escopo (D1)** (L924-926) nomeia
as duas como "plataforma e framework de interface fixos" que "saíram do núcleo e são escolha do
projeto"; o bullet do TDD (L937-938) trocou "MVVM *(do perfil `desktop-pyside6`)*" por "padrão de
apresentação". O fato da correção posterior fica; sai o vocabulário de perfil e o nome de
plataforma/framework. Critério de pronto re-derivado no fechamento:
`grep -inE "perfil|pyside|mvvm|qt|desktop" README.md` retorna **vazio** (0 linhas, exit 1), de 7
no pickup. Invariantes preservados: 16 linhas `> Fonte da verdade:`, numeração `## N.`, títulos
`Anatomia do kit` e `Os guardrails`, 10 skills na tabela, `Quatorze` guardrails. Nenhum vício
`V1..V8` da skill `redacao-doc` reintroduzido. Bateria do §3 do plano, todos exit 0: `kit_check.ps1
-Mode validate` (7 agentes, 10 skills, `VERSION == KIT_VERSION '2.0.0'`), `-Mode check-drift` (OK),
`check-readme.ps1` (14 guardrails, 15 seções com Fonte da verdade válida) e `python -m pytest`
(3 passed). Sem achado fora de escopo.
Consumo: ver docs/telemetria.tsv

**`V2E-T6a` em 2026-08-07 (`done`):** primeira das duas fatias da `T6` (`DE-1`) — o **mecanismo de
perfil** sai do contrato com o cliente: vocabulário, premissa, tabela e a subseção que o instituíam.
Só `README.md` tocado, nos 6 clusters do dossiê. Glossário: a entrada `Perfil` foi removida inteira,
e o bullet do `guardrails-check` (verbete "Conformance") passou a enumerar "camadas, ACL, padrão de
apresentação", sem qualificar o padrão por perfil. §1: a frase que listava as modalidades cobertas e
apontava o perfil como o que muda entre elas saiu; o parágrafo agora fecha em "linguagem, framework
de interface, runtime e forma de entrega ficam com o projeto — a doutrina é a mesma para todos",
afirmando a universalidade sem instituir modalidade como conceito. §2: a abertura perdeu "em
qualquer modalidade" e o trecho "pertencem ao *perfil*" virou "são escolha do projeto" — a premissa
continua sendo uma, então "As cinco premissas de arquitetura" e a enumeração `1..5` ficam intactas;
a célula da tabela de especialização virou "Nenhuma — idêntica entre projetos". Removida a subseção
`### Perfis: o que a modalidade acrescenta` inteira (texto de abertura, a tabela
`Perfil | Modalidade | O que ativa | Auditor` — que era o último ponteiro vivo para o agente
`pantonic-auditor-pyside6`, já ausente do disco —, o parágrafo do `.claude/PERFIL` e o default
`desktop-pyside6`) mais o parágrafo do case de referência que autorizava citar Qt, MVVM e PySide6
como default do case. O parágrafo do caminho de uma capacidade nova, que abria com "é igualmente
fixo, e esse é agnóstico" — leitura que só se sustentava por contraste com a subseção removida —,
passou a "também é fixo" e foi reflowado; §2 termina nele. Critério de pronto re-derivado no
fechamento: `grep -nEi "perfil|pyside|mvvm|qt|desktop" README.md` caiu de **24** para **7** linhas,
todas fora desta fatia (§5 L357; §11 L734; §15 L909, L925-926, L937-938) — zero ocorrência no
glossário, em §1 e em §2. Invariantes preservados: 16 linhas `> Fonte da verdade:`, numeração
`## N.`, títulos `Anatomia do kit` e `Os guardrails`, 10 skills na tabela, `Quatorze` guardrails.
Nenhum vício `V1..V8` da skill `redacao-doc` reintroduzido — as reescritas afirmam o estado, sem
narrativa de proveniência nem ID de processo. Bateria do §3 do plano, todos exit 0: `kit_check.ps1
-Mode validate` (7 agentes, 10 skills, `VERSION == KIT_VERSION '2.0.0'`), `-Mode check-drift` (OK),
`check-readme.ps1` (14 guardrails, 15 seções com Fonte da verdade válida) e `python -m pytest`
(3 passed). Sem achado fora de escopo. Falta a `T6b` para fechar a `V2E-T6`.
Consumo: ver docs/telemetria.tsv

**`V2E-T5b` em 2026-08-06 (`done`):** segunda e última fatia da `T5` (`DE-5`) — tira Qt do único
verificador executável que o conhecia, sem cegar os consumidores que dependem dele hoje.
`.claude/checks/dead_code.py`: removidas `_QT_VIRTUAL_METHODS` (tabela de 40 métodos) e a
heurística `_is_qt_derived` (casamento textual `^Q[A-Z]`, com `import re` que ficou sem outro uso e
saiu junto); no lugar, `_load_framework_virtuals(root)`/`_parse_framework_virtuals(text)` (novas)
leem `<root>/.claude/framework-virtuals.txt` opcional — seções `[bases]`/`[metodos]`, um nome por
linha, `#` comenta, arquivo ausente ⇒ conjuntos vazios ⇒ nenhuma exceção concedida — e
`_is_framework_derived(cls_name, class_bases, framework_bases, _seen=None)` (renomeada de
`_is_qt_derived`, agora por membership em `framework_bases` em vez de regex) substitui o
casamento estrutural. `check()` carrega `framework_bases`/`framework_methods` uma vez por chamada
(estado local, não de módulo) e usa no `method_auto` do mesmo jeito que antes. Docstring do módulo,
exemplo de `_base_terminal_names` (`QWidget`/`QtWidgets.QWidget` → `Base`/`pkg.Base`) e comentário
de herança reescritos sem nenhuma menção a Qt — `grep -ci "qt" .claude/checks/dead_code.py` caiu de
**16** para **0**. Migração de conteúdo (§3 item 1, "migrar é um ato só"): a tabela e a lista de
bases removidas do hub foram para `PantonicForDesktop/.claude/framework-virtuals.txt` (novo, fora
do versionamento — `PantonicForDesktop/` está no `.gitignore` — pronto para qualquer consumidor do
perfil `desktop-pyside6` copiar para a raiz do próprio projeto), não para `doutrina/`, por ser
conteúdo operacional, não prosa. Testes (`tests/test_dead_code.py`, suíte da `T5a` estendida):
`test_tf_qt_virtual_override_not_flagged` (mantido, mesma asserção) volta a passar por declaração —
`tests/fixtures/qt_project/.claude/framework-virtuals.txt` (novo) declara `QWidget`/`paint`, não
mais a tabela embutida; `test_tr_orphan_symbol_is_flagged` (mantido, inalterado) continua travando
o falso-verde de "não varreu nada"; `test_tr_undeclared_framework_virtual_is_flagged` (novo, TR da
`T5b`) usa `tests/fixtures/qt_project_undeclared/widget.py` (novo, mesma forma de classe/método,
**sem** `.claude/framework-virtuals.txt`) e confirma que `MyWidget.paint` aparece nos achados sem
declaração — prova que a exceção não é concedida "de graça". Decisão de escopo: o fixture original
não foi renomeado para algo agnóstico a Qt — o "considere renomear" do dossiê é condicional ao
critério de pronto do plano se estender a ele, e o critério de pronto (`Grep -i "qt"` sobre
`.claude/checks/dead_code.py` e "exceção continua concedível por declaração") não menciona os
fixtures; renomear seria escopo além do dossiê. Bateria de fechamento, todos exit 0: `python -m
pytest` (3 passed — os 2 herdados da `T5a` + o novo); `python .claude/checks/dead_code.py --root .`
(`dead_code: OK - 0 achado(s) sob '.'.`); `kit_check.ps1 -Mode validate` (OK — 7 agentes, 10 skills,
`VERSION == KIT_VERSION '2.0.0'`) e `-Mode check-drift` (OK); `check-readme.ps1` (OK — 14
guardrails, 15 seções com Fonte da verdade válida). Sem achado fora de escopo nesta fatia. Com esta
fatia, a `V2E-T5` fecha completa (`T5a` + `T5b`).
Consumo: ver `docs/telemetria.tsv`.

**`V2E-T5a` em 2026-08-06 (`done`):** primeira das duas fatias da `T5`, infraestrutura mínima da
suíte de testes do hub e âncora do comportamento **vigente** de `.claude/checks/dead_code.py`
quanto às virtuais de framework Qt, antes da troca de mecanismo da `T5b`. `pytest.ini` na raiz
(mínimo, `testpaths = tests`, sem `pyproject.toml`/`setup.py`/`__init__.py` — o hub não vira
pacote Python). `tests/fixtures/qt_project/widget.py` (novo fixture puro, sem importar PySide6):
`MyWidget(QWidget)` com override de `paint` sem chamador explícito, e `orphan_function()` órfã de
produção. `tests/test_dead_code.py` (novo): carrega `dead_code.py` por caminho
(`importlib.util.spec_from_file_location`, já que `.claude/checks/` tem ponto no nome e não é
pacote importável) e chama `check(Path(<fixture>))` — `test_tf_qt_virtual_override_not_flagged`
confirma que o override não aparece nos achados (comportamento vigente que a `T5b` vai passar a
produzir por outro mecanismo, `framework-virtuals.txt`); `test_tr_orphan_symbol_is_flagged`
confirma que `orphan_function` aparece, travando contra o falso-verde de "a varredura não achou
nada". Os dois testes passaram já na primeira rodada — `dead_code.py` não foi tocado (fora do
escopo desta fatia). Bateria de fechamento, quatro passos, todos exit 0: `python -m pytest` (2
passed); `python .claude/checks/dead_code.py --root .` (`dead_code: OK - 0 achado(s) sob '.'.`);
`kit_check.ps1 -Mode validate` (OK — 7 agentes, 10 skills, `VERSION == KIT_VERSION '2.0.0'`) e
`-Mode check-drift` (OK); `check-readme.ps1` (OK — 14 guardrails, 15 seções com Fonte da verdade
válida). Achado fora de escopo: carregar `dead_code.py` via `importlib` grava bytecode em
`.claude/checks/__pycache__/`, sem entrada correspondente no `.gitignore` — aparece como
untracked em todo `git status` após rodar a suíte; registrado como tíquete `TK-13` no índice
(diretório removido nesta sessão, mas volta a cada `pytest`; `.gitignore` fora dos arquivos-alvo
desta fatia, não tocado). Com esta fatia, falta só a `T5b` para fechar a `V2E-T5`.
Consumo: ver `docs/telemetria.tsv`.

**`V2E-T4c` em 2026-08-06 (`done`):** terceira e última das três fatias da `T4`, skills de
processo do pacote distribuído sem perfil nem Qt (`DE-1`). `.claude/skills/integrar-poc/SKILL.md`:
o bullet "UI" *[perfil `desktop-pyside6`, §1.1]* da dissecação da POC virou "Camada de
apresentação" — estrutura equivalente na camada declarada pelo projeto, com o exemplo concreto
(View no plugin + `view_model.py`) preservado como o **case de referência**, "QtCore-only"
trocado por "sem lógica de negócio, só coordenação"; a frase "Projeto de outro perfil usa a
camada de apresentação equivalente ao seu perfil" despersonalizada para "Cada projeto usa a
estrutura equivalente à sua própria camada de apresentação". Na allowlist de imports do plugin,
"mais `PySide6.*` *[perfil `desktop-pyside6`, §1.1]*" virou "mais o toolkit da camada de
apresentação declarado pelo projeto" (vocabulário reusado das fatias anteriores).
`.claude/skills/redacao-doc/SKILL.md`: o par ✗/✓ de exemplo da regra V7 ("O artefato Architecture
deixou de ser MVVM e passou a ser clean architecture + DDD") foi **removido e substituído**, não
despersonalizado — a ilustração dependia do nome da tecnologia — por um exemplo de mesma força
retórica sem tecnologia ("O guarda de conformance deixou de rodar em cada commit..."), verificado
contra a definição de V7 antes da troca; a linha da tabela "Papel ≠ interlocutor" ("O gerente
intervém aqui: escolher o perfil") teve só a instância trocada por "aprovar o plano" — mesmo
padrão abstrato (papel decidindo algo), informação preservada, sem arquivamento.
`.claude/skills/proximo-passo/SKILL.md`: "agrupado por perfil" virou "agrupado por tipo" — aqui
"perfil" já tinha sentido de tipo/natureza do item, não de modalidade, então despersonalizado sem
perda de instrução. Da fatia, só o exemplo V7 original é remoção efetiva (não sobrevive em forma
agnóstica em lugar nenhum) — preservado verbatim em
`PantonicForDesktop/doutrina/kit-verificacoes-mvvm-e-qt.md` (apendado ao arquivo criado pela
`T4a`); os outros 8 pontos foram despersonalizados ou tiveram a instância trocada in place, sem
perda de conteúdo acionável. `.claude/README.md` regenerado (`kit_check.ps1 -Mode generate`).
Verificações: Grep por `perfil|PySide|MVVM|Qt|desktop` (case-insensitive) nos três arquivos-alvo
retorna **vazio**; o mesmo Grep em `.claude/skills/` + `.claude/agents/` caiu de 9 para **1**
ocorrência — não para 0 como o dossiê previa, porque restou "pyside6" na `description` do
frontmatter de `.claude/skills/audit-sweep/SKILL.md` (fora dos três arquivos-alvo desta fatia,
residual da `T4b`); achado registrado como tíquete `TK-12` no índice, não corrigido nesta tarefa
(fora de escopo). `kit_check.ps1 -Mode validate` (OK — 7 agentes, 10 skills, `VERSION ==
KIT_VERSION '2.0.0'`), `-Mode check-drift` (OK) e `check-readme.ps1` (OK — 14 guardrails, 15
seções com Fonte da verdade válida), os três em exit 0; `git status --short` mostra só os três
arquivos-alvo e `.claude/README.md` regenerado como novas modificações desta tarefa (mais
`.claude/skills/redacao-doc/` já untracked de sessão anterior), nada novo sob `PantonicForDesktop/`
(pasta no `.gitignore`). Com esta fatia, a `V2E-T4` está completa (`T4a` + `T4b` + `T4c`).
Consumo: ver `docs/telemetria.tsv`.

**`V2E-T4b` em 2026-08-06 (`done`):** segunda das três fatias da `T4`, bootstrap e varredura
mecânica do pacote distribuído sem perfil nem Qt (`DE-1`). `.claude/skills/bootstrap-pantonic/SKILL.md`:
a fase 2 (Architecture) perdeu o parágrafo que perguntava e registrava o perfil em `.claude/PERFIL`
e a frase que condicionava a herança de ViewModel/View a esse perfil — o modelo conceitual agora é
só "clean architecture + DDD", sem cláusula de MVVM (despersonalizar sobraria tautológico, mesmo
critério da `T4a` para a verificação "Fronteira MVVM"); a árvore de diretórios da fase 5 perdeu a
linha `.claude/PERFIL`; a "Aceitação" perdeu o bullet que exigia a pergunta de perfil registrada.
`.claude/skills/audit-sweep/SKILL.md`: a bateria de varredura perdeu as linhas inteiras dos blocos
`ARCH-mvvm` e `PYSIDE` (só faziam sentido para um perfil declarado) e o bloco `DDD-pureza` perdeu
as duas alternativas de PySide6 da regex de imports de infraestrutura, mantendo o resto da lista
(sqlite3, requests, httpx, logging, pathlib) intacto. Os 7 trechos são remoção efetiva, não
despersonalização — nenhum sobrevive em forma agnóstica no arquivo — e estão preservados verbatim,
apendados em `PantonicForDesktop/doutrina/kit-verificacoes-mvvm-e-qt.md` (arquivo criado pela
`T4a`). `.claude/README.md` regenerado (`kit_check.ps1 -Mode generate`). Verificações: Grep por
`perfil|PySide|MVVM|Qt|desktop` nos dois arquivos-alvo retorna **vazio**; o mesmo Grep em
`.claude/skills/` + `.claude/agents/` caiu de 22 para **9** ocorrências (`integrar-poc` 4,
`redacao-doc` 4, `proximo-passo` 1 — todas da fatia `T4c`); `kit_check.ps1 -Mode validate` (OK — 7
agentes, 10 skills, `VERSION == KIT_VERSION '2.0.0'`), `-Mode check-drift` (OK) e
`check-readme.ps1` (OK — 14 guardrails, 15 seções com Fonte da verdade válida), os três em exit 0;
`git status --short` mostra só os dois arquivos-alvo e o `.claude/README.md` regenerado como novas
modificações, nada novo sob `PantonicForDesktop/` (pasta no `.gitignore`). Nenhum achado fora de
escopo.
Consumo: ver `docs/telemetria.tsv`.

**`V2E-T4a` em 2026-08-06 (`done`):** primeira das três fatias da `T4`, cadeia de verificação de
arquitetura do pacote distribuído sem perfil nem Qt (`DE-1`). `.claude/agents/pantonic-auditor-arch.md`:
o import de plugins na lista de fatos estáveis ("mais PySide6 *[perfil `desktop-pyside6`, §1.1]*")
virou "mais o toolkit da camada de apresentação declarado pelo projeto"; a verificação 2 (pureza de
domínio) perdeu só "Qt" da enumeração "ORM, HTTP client, logging de infra, Qt", verificação
preservada; a verificação 11 ("Fronteira MVVM") foi removida — despersonalizada, sobraria só "o
padrão de apresentação declarado pelo projeto tem fronteira", sem informação acionável para um
auditor agnóstico a modalidade — e a lista renumerada de quinze para quatorze itens (12→11, 13→12,
14→13, 15→14), com as referências cruzadas da seção "Método" atualizadas para os novos números.
`.claude/agents/pantonic-executor.md`: o bullet de MVVM na lista de fatos estáveis, removido pela
mesma razão. `.claude/skills/guardrails-check/SKILL.md`: a `description` do frontmatter perdeu a
menção a MVVM; o item 6 (código morto) trocou "override de virtual Qt *[perfil `desktop-pyside6`,
§1.1]*" por "override de virtual do toolkit da camada de apresentação declarado pelo projeto"
(despersonalizado, preservando a categoria); o item de checklist de review sobre ViewModel/Model
QtCore-only foi removido, mesma razão da verificação 11. Vocabulário reusado das fatias `T3`, nenhum
conceito novo. Os 3 trechos efetivamente removidos (não apenas despersonalizados) estão preservados
verbatim em `PantonicForDesktop/doutrina/kit-verificacoes-mvvm-e-qt.md` (arquivo novo, mesmo padrão
dos irmãos `arquitetura-mvvm-e-pyside6.md` e `governanca-perfis-e-mvvm.md`); os trechos
despersonalizados no lugar não foram arquivados (a informação continua presente, só sem nomear
toolkit). `.claude/README.md` regenerado (`kit_check.ps1 -Mode generate`). Verificações: Grep por
`perfil|Perfil|PERFIL|PySide|MVVM|Qt|desktop|Desktop` nos três arquivos-alvo retorna **vazio**; o
mesmo Grep em `.claude/skills/` + `.claude/agents/` caiu de 31 para **22** ocorrências (`audit-sweep`
3, `bootstrap-pantonic` 10, `integrar-poc` 4, `proximo-passo` 1, `redacao-doc` 4 — todas de fatias
posteriores); `kit_check.ps1 -Mode validate` (OK — 7 agentes, 10 skills, `VERSION == KIT_VERSION
'2.0.0'`), `-Mode check-drift` (OK) e `check-readme.ps1` (OK — 14 guardrails, 15 seções com Fonte da
verdade válida), os três em exit 0; `git status --short` sem nada novo rastreado sob
`PantonicForDesktop/` (pasta no `.gitignore`). Nenhum achado fora de escopo.
**Orçamento:** 33 tool uses contra o teto de 30 fixado no dossiê — o estouro veio da renumeração da
lista de verificações do `pantonic-auditor-arch.md` (15 → 14) e das referências cruzadas da seção
"Método", consequência mecânica da remoção da verificação 11 que não estava nas três regiões
listadas. Consumo: ver `docs/telemetria.tsv`.

**`V2E-T3c` em 2026-08-06 (`done`):** terceira e última fatia da `T3` (§6 em diante do
`ARQUITETURA_PANTONICA.md`), fechando a extração de modalidade do documento. Saíram os 7 pontos
medidos: a primitiva de concorrência do `task_runner` na categoria "Expressão" (§6), a frase "UI
thread" do bullet do TaskRunner nas condições de POC integrável (§9), o toolkit do perfil ativo na
allowlist de imports por AST da validação no load (§9), a qualificação do `platformdirs` como
"default do perfil `desktop-pyside6` *[§1.1]*" na raiz de dados (§10), a linha do TaskRunner na
tabela de contenção de falhas (§11) e o harness de UI da linha `Plugins` da tabela de testes
(§12). Reescrita, seguindo o vocabulário das fatias anteriores: "QThreadPool/QRunnable" virou
"primitiva de concorrência declarada pelo projeto"; a allowlist virou "o toolkit da camada de
apresentação declarado pelo projeto"; o `platformdirs` virou "default do case de referência"
(mantendo a regra agnóstica do ponto único de resolução que já estava na frase anterior); o
harness virou "harness de UI declarado pelo projeto". Os dois pontos de "UI thread" foram
**despersonalizados, não apagados** — o conceito permanece como "a thread que serve a superfície
de entrada" (§9) e "`on_failed(exc)` na thread da superfície de entrada; a interface nunca
congela" (§11), preservando a garantia de não-congelamento sem nomear toolkit. Os 6 trechos estão
preservados verbatim em `PantonicForDesktop/doutrina/arquitetura-mvvm-e-pyside6.md`, apendados na
seção "Marcações de perfil e menções a Qt/PySide6 removidas do corpo de ARQUITETURA_PANTONICA.md"
no mesmo padrão de subseções `### §N — <âncora>` da `T3b`. Nenhuma seção foi removida, logo nenhuma
renumeração; nenhuma linha do `README.md` foi quebrada. Verificações: Grep por
`PySide|Qt|MVVM|perfil|Perfil|PERFIL` em `ARQUITETURA_PANTONICA.md` retorna **vazio**; Grep por
`UI thread` no mesmo arquivo retorna **vazio**; `kit_check.ps1 -Mode validate` (OK — 7 agentes, 10
skills, `VERSION == KIT_VERSION '2.0.0'`), `-Mode check-drift` (OK — `.claude/README.md` ==
regenerado) e `check-readme.ps1` (OK — 15 seções com Fonte da verdade válida), os três em exit 0;
`git status --short` sem nada novo rastreado sob `PantonicForDesktop/`. Nenhum achado fora de
escopo.
Consumo: ver `docs/telemetria.tsv`

**`V2E-T3b` em 2026-08-06 (`done`):** primeira metade do split da sobra da `T3` (topo do
`ARQUITETURA_PANTONICA.md` até a §4), medida em ~12 write-clusters e partida por posição no
documento. Saíram: o blockquote "Convenção de perfil" do cabeçalho (com a máquina de perfil
inteira — marcador `*[perfil ...]*`, `.claude/PERFIL`, ponteiro para `GOVERNANCA.md` §1.1 e a
desambiguação de numeração), as marcações e allowlists de toolkit das linhas `infracore` e
`plugins` da tabela de camadas (§2), os comentários de perfil da árvore de diretórios (§3, em
`ui_shell/` e `plugins/<nome>/`), o parágrafo "As entradas marcadas `[perfil desktop-pyside6]`..."
abaixo da árvore (§3), a descrição Qt da linha `ui_shell` da tabela de superfícies de entrada (§4)
e a marcação de perfil da sequência de bootstrap (§4). Os oito trechos estão preservados verbatim
em `PantonicForDesktop/doutrina/arquitetura-mvvm-e-pyside6.md`, seção "Marcações de perfil e
menções a Qt/PySide6 removidas do corpo de ARQUITETURA_PANTONICA.md". Reescrita: o blockquote
virou uma frase única de agnosticismo ("o núcleo descrito aqui é agnóstico a stack e plataforma;
onde um exemplo concreto aparece, ele ilustra o case de referência e nunca é exigência do
framework"); "o toolkit do perfil ativo (no `desktop-pyside6`: PySide6)" virou "o toolkit da
camada de apresentação declarado pelo projeto" nas duas linhas da tabela de camadas; a camada de
apresentação **permaneceu como conceito abstrato** — `ui_shell` continua na tabela e na árvore
como superfície de entrada da aplicação, despersonalizada ("expõe o estado do núcleo ao mundo
externo e concentra os tokens de apresentação — tema/estilo, só aqui; o toolkit que a implementa é
declarado pelo projeto"), e o `view_model.py` da árvore de plugins virou "adaptador de
apresentação, se o projeto tiver um". Nenhuma referência cruzada externa apontava para os trechos
removidos, e nenhuma linha do `README.md` foi invalidada (a prosa de perfil que resta lá é escopo
da `T6`) — nada a corrigir fora do arquivo-alvo. Verificações: o Grep por
`PySide|Qt|MVVM|perfil|Perfil|PERFIL` no `ARQUITETURA_PANTONICA.md` retorna exatamente as **5**
linhas reservadas à `V2E-T3c` (208 primitiva de concorrência, 275-276 allowlist de imports por
AST, 288 default do `platformdirs`, 314 harness `pytest-qt`), nenhuma antes da §6; os três
comandos da bateria (`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`)
fecharam em exit 0; `git status --short` não mostra nada novo rastreado sob `PantonicForDesktop/`.
Split registrado pelo orquestrador **antes** da delegação: a sobra da `T3` mediu ~12
write-clusters contra o teto de 8, e o gate de delegação manda dividir em vez de confiar no teto —
a segunda metade (§6 em diante) é a `V2E-T3c`. Decisão de redação do executor **ratificada** pelo
orquestrador: manter o `view_model.py` da árvore como "adaptador de apresentação, se o projeto
tiver um" aplica a mesma regra dada para o `ui_shell` (despersonalizar a descrição, não apagar a
camada) e não reintroduz vocabulário de MVVM.
Consumo: ver `docs/telemetria.tsv`

**`V2E-T3a` em 2026-08-06 (`done`):** a `T3` original do plano ("remover a §10 e as
marcações de perfil de `ARQUITETURA_PANTONICA.md`") mediu ~18 write-clusters, acima do teto de 8,
e foi partida por orçamento em `V2E-T3a` (esta tarefa) e `V2E-T3b` (marcações `*[perfil ...]*` e
menções a PySide6/Qt/MVVM no corpo restante do documento — segue em `backlog`, não iniciada). A
`V2E-T3a` extraiu e removeu a §10 inteira ("MVVM e PySide6"), o parágrafo "Relação com MVVM (§10)"
da §2 e o parágrafo "Também não é núcleo..." da §14 (com a reescrita de prosa "medida no perfil
`desktop-pyside6`" → "medida no case de referência" na mesma região), preservando os três trechos
na íntegra em `PantonicForDesktop/doutrina/arquitetura-mvvm-e-pyside6.md`. As seções `§11..§15`
foram renumeradas para `§10..§14` e as referências internas às seções deslocadas foram corrigidas
(§12→§11 "contenção de falhas", §14→§13 "não portar"). As três referências cruzadas externas do
dossiê foram corrigidas (`README.md:65` §11→§10, `.claude/skills/guardrails-check/SKILL.md:9`
§13→§12, `.claude/skills/bootstrap-pantonic/SKILL.md:40` §15→§14); a varredura de rede encontrou
uma **quarta** referência não listada no dossiê — `README.md:103` (entrada "Conformance" do
glossário, §13→§12) — corrigida na mesma tarefa, autorizado pelo próprio dossiê ("se aparecer uma
quarta, corrija-a").

**Achado do executor, fechado pelo orquestrador na mesma rodada (`TK-11`):**
`ARQUITETURA_PANTONICA.md` §9 ("Condições de POC integrável"), bullet do TaskRunner, citava
"(§10)" apontando para a seção MVVM/Threading extraída por esta tarefa. A renumeração fez `§10`
existir de novo — agora "Operações de OS e IN/OUT", conteúdo não relacionado — então a referência
passou a apontar para um número **válido mas semanticamente errado**, não para um número
inexistente; o Grep por `§1[0-5]` não distingue os dois casos automaticamente, e por isso o
executor parou em vez de inventar destino, conforme o dossiê. Destino decidido: **remover o
ponteiro** (`sempre TaskRunner;`) — a doutrina extraída vive em pasta fora do versionamento
(`DE-2`) e não pode ser destino de referência do hub, e a regra se sustenta afirmada inline. A
frase "UI thread" do mesmo bullet permanece para a `V2E-T3b`. As três verificações do dossiê
(`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`) fecharam em exit 0, e
`git status --short` não mostra nada novo rastreado sob `PantonicForDesktop/`.
Consumo: ver `docs/telemetria.tsv`

**`V2E-T2` fechou em 2026-08-06 (`done`):** o conceito de perfil saiu da fonte da verdade de
governança. `GOVERNANCA.md` perdeu a §1.1 inteira ("Perfis"), a linha de modalidades cobertas do
§1, a cláusula do auditor por perfil na matriz de papéis (§3), a marcação de MVVM no artefato
*Architecture* (§6) e o item 3 do §7 (guardrail "MVVM estrito"); os itens 4..15 foram renumerados
para 3..14 e as 9 referências cruzadas internas a "item N" acompanharam (§3, §4.4, §8, §9) — o
"Registro das rodadas" do §7.1 ficou intacto por ser registro histórico point-in-time. `README.md`
(raiz) perdeu a linha 3 da tabela de guardrails do §10, "Quinze regras" → "Quatorze", "Sete regras
falham como teste executável" → "Seis", e as citações de item 4/6/12/14/15 viraram 3/5/11/13/14. O
texto removido está preservado na íntegra em
`PantonicForDesktop/doutrina/governanca-perfis-e-mvvm.md`, e o inventário de
`PantonicForDesktop/README.md` moveu as duas linhas de "o que ainda precisa migrar" para "o que já
está aqui". Verificação: Grep `perfil|PERFIL` em `GOVERNANCA.md` **vazio**; §7 com 14 itens
`1..14`; tabela do `README.md` §10 com 14 linhas; `check-readme.ps1` em exit 0 ("14 guardrail(s)").
Nota para a `T6`: a tabela de perfis do `README.md` §2 cita "MVVM estrito (§10, item 3)", referência
que a remoção deixou pendurada — não foi corrigida aqui porque o bloco inteiro é alvo declarado da
`T6`. Orçamento estourado: ~65 tool uses contra o teto de ~50, sem retrabalho — a tarefa tinha três
arquivos-alvo e 27 pontos de edição pontual (renumeração item a item), o que a coloca acima do
tamanho de uma tarefa atômica típica. Consumo: ver `docs/telemetria.tsv`.

**`V2E-T1` fechou em 2026-08-06:** `PantonicForContainer/` criado (README no molde de
`PantonicForDesktop/README.md`, `.claude/agents/` e `doutrina/`), `pantonic-auditor-container.md`
movido do hub via `git mv` e removido do índice; `.gitignore` ganhou a entrada da pasta;
`README.md` (raiz) perdeu a linha de `pantonic-auditor-container` na tabela de perfis e na tabela
de agentes, "oito agentes" → "sete agentes"; `.claude/README.md` regenerado
(`kit_check.ps1 -Mode generate`). As três verificações do §3 do plano fecharam em exit 0. Consumo:
ver `docs/telemetria.tsv`.

**Estágio 6 aberto em 2026-08-06 — o Estágio 5 foi reprovado na 2ª rodada de aceite e está
`superseded`.** A `V2I-T12` reprovou o README de novo, agora por **identidade**, não por
legibilidade: a correção de forma da `T11c` foi aceita, mas o documento ainda descreve o consumidor.
O veredito derruba a `DR-2` — perfil não é abstração do núcleo, é o nome que o núcleo dava para o
próprio vazamento. Um framework de aplicação desktop contém todo o conhecimento do PantonicApp e o
estende; a camada de baixo não sabe nada sobre quem a usa, e o hub que declara `desktop-pyside6`
como default sabe. **O conceito de perfil sai do hub inteiro**, o material desktop/PySide6/MVVM/Qt
migra para `PantonicForDesktop/` e o de container para `PantonicForContainer/` — ambas no
`.gitignore`, embriões dos repositórios próprios dessas ramificações. Inclui o único caso que não é
prosa: `dead_code.py` troca a tabela de virtuais de Qt por ponto de extensão declarativo do projeto.
11 tarefas, decisões `DE-1..DE-6` fechadas no ato, fechamento em **`3.0.0`** (MAJOR — remover o
conceito de perfil e o guardrail de MVVM quebra compatibilidade com os 5 consumidores). As 5 tarefas
não iniciadas do Estágio 5 foram absorvidas com escopo corrigido (§7 do plano novo).

**A `V2I-T12` reprovou o README em 2026-08-06 (1ª rodada de aceite).** O veredito não é factual — o
conteúdo técnico da `V2I-T11` está aceito — é de **legibilidade**: o documento narra a própria
gestação. O preâmbulo abre relatando conversas anteriores e um episódio de campo, e em seguida
anuncia que cada seção contará a evidência ou o episódio que produziu o procedimento; a leitura foi
interrompida ali. Conforme o dossiê da `T12` ("reprovação gera rodada nova da `T11`"), abre-se a
`V2I-T11c`; a `V2I-T13` segue bloqueada.

O vício foi diagnosticado como **modo de escrever**, não como defeito de um documento: vira a skill
de kit `redacao-doc` (tíquete `TK-09`, autorada na mesma rodada), que passa a ser o critério
normativo de todo doc publicado. Baseline medido no README de 1114 linhas — `V2-interlocutor` 43,
`V3-id-processo` 16, `V3-data` 3, `V4-anuncio` 2, `V1-proveniencia` 4, `V7-datacao` 3, `V8-divida`
2 — registrado no plano `### T11c` como referência de aceite. Revisão de escopo em
`docs/plans/P-0730-v2-identidade.md` §9; total do plano 17 → **18 tarefas**.

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

A `V2I-T7` fechou em 2026-08-05 — a `DR-7` virou **guardrail** antes de o README ser reescrito, para
que a `V2I-T11` já nasça sob a regra. `GOVERNANCA.md` §7 passa a ter **15 itens**: o item 15,
**G-README — o README é documento canônico, não artefato acessório**, declara o `README.md` da raiz
como o **contrato entre o framework e o cliente** e fixa três deveres (doutrina refletida no README
na mesma sprint; nenhum bump de versão sem aceite explícito do dono; o guarda executável cobre
estrutura, não sentido — o aceite do dono é o único teste de sentido, logo gate e não cortesia).
§8 passa a listar o `README.md` como documento canônico na tabela de documentação mínima (primeira
linha). §9 absorveu a resolução da colisão: o status do README é agora guardrail, e o parágrafo novo
"Colisão registrada, ainda aberta" declara que o preâmbulo vigente (`README.md:5-11`, *"não existe
para convencer ninguém a adotar o framework"*) contradiz o §9, que a `DR-7` resolveu a favor do §9, e
que a correção é dívida da `V2I-T11` — até lá, prevalece o §9.

Verificação: `pwsh .claude\checks\check-readme.ps1` → **exit 1**, um problema: *"Divergência no
número de guardrails: a seção 'Os guardrails' do README tem 14 linha(s) vs GOVERNANCA.md §7 com 15
item(ns)"*. **Reprovação prevista pelo dossiê da tarefa** (14 → 15) e deliberadamente não
"consertada" no README: `README.md` está fora dos Arquivos-alvo da `V2I-T7`, e a contagem é fechada
pela `V2I-T11`. Nenhum outro problema apontado pelo guarda.

Dívidas registradas em `docs/plans/P-0730-v2-identidade.md` `### T11` (sem ampliar o escopo dela):
(a) a contradição de `README.md:5-11`; (b) a contagem de guardrails do README §10. Nenhum arquivo
fora dos Arquivos-alvo foi tocado — em especial, a skill `handover` **não** foi editada: o gate de
aceite é texto do guardrail em `GOVERNANCA.md`, e materializá-lo na skill é trabalho de outra tarefa.

Consumo: ver docs/telemetria.tsv

**Revisão da `DR-7` no mesmo dia — `DR-8` (decisão do dono, 2026-08-05).** A pergunta do dono sobre
o que o `check-readme.ps1` de fato protege expôs que o item 15, como entregue pela `V2I-T7`,
prometia enforcement inexistente ("gate de aceite na skill `handover`"). Decisão: a revisão do
README é **atividade de encerramento de sprint, autorada pelo planejador como tarefa nomeada** — não
gate mecânico, que "gera artefatos confusos e muito especializados no diretório". O
`check-readme.ps1` **permanece**, rebaixado de critério de pronto a **instrumento do planejador**
(detecta drift estrutural; não julga sentido). Aplicado de imediato: `GOVERNANCA.md` §7 item 15
reescrito (deveres 2 e 3 + *Enforcement*), `DR-8` registrada em `P-0730-v2-identidade.md` §1,
**`T16` nova** (materializa o dever 2 na matriz de responsabilidades §3 + agente planejador, com a
skill `handover` e o script explicitamente fora de escopo), risco e ordem de execução atualizados
(`T16` entra entre `T11` e `T12`). Plano passa a 17 tarefas.

A `V2I-T8` fechou em 2026-08-05 — o kit para de cobrar MVVM/Qt de projeto que não é desktop
(`DR-2`). Cada cobrança incondicional nos 5 arquivos-alvo ganhou o marcador de perfil já
materializado pela `T3`/`T4` — *[perfil `desktop-pyside6`, §1.1]* — reusando `GOVERNANCA.md` §1.1
como fonte única, sem redefinir o perfil localmente:
- `.claude/skills/guardrails-check/SKILL.md`: `description` do frontmatter (:3, "MVVM"), item 6 do
  checklist executável (:43, categoria "override de virtual Qt" do `dead_code.py`) e o item do
  checklist de review (:69, "ViewModel continua QtCore-only?...") — 3 pontos marcados.
- `.claude/agents/pantonic-executor.md` (:14) — bullet "MVVM" dos Fatos estáveis marcado.
- `.claude/agents/pantonic-auditor-arch.md`: item 32-33 ("plugins importam só
  contracts/PySide6/stdlib") reescrito para isolar PySide6 como acréscimo do perfil; item 9 do
  checklist (:56, "Fronteira MVVM") marcado.
- `.claude/skills/audit-sweep/SKILL.md` (:30) — linha `ARCH-mvvm` da tabela de greps marcada; o
  bloco `PYSIDE` (:32) foi deixado intocado de propósito — é a bateria do `pantonic-auditor-pyside6`,
  auditor que o próprio perfil `desktop-pyside6` ativa (mesma lógica da cerca de escopo abaixo).
- `.claude/skills/integrar-poc/SKILL.md`: passo 3 "UI" (:29-30, View/`view_model.py`) marcado com
  frase adicional para o perfil equivalente de outro projeto; allowlist do manifest (:39, incluindo
  `PySide6.*`) reescrita para isolar o item do perfil.

`.claude/README.md` regenerado via `kit_check.ps1 -Mode generate` (a `description` do
`guardrails-check` mudou de texto). Verificação: `pwsh .claude/checks/kit_check.ps1 -Mode validate`
→ `kit_check: OK - 9 agente(s) e 9 skill(s) validados; VERSION == KIT_VERSION ('2.0.0').`;
`-Mode check-drift` → `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 9
skill(s)).` — ambos exit 0, igual à baseline do dossiê. Grep final `Qt|MVVM|PySide6|ViewModel` nos
5 arquivos-alvo → toda ocorrência agora convive com o marcador de perfil na mesma linha/bullet;
nenhuma cobrança incondicional sobrevive.

Cerca de escopo respeitada: `.claude/agents/pantonic-auditor-pyside6.md` não foi tocado (é o
auditor que o perfil ativa, cobrança lá é correta por desenho). `.claude/agents/pantonic-fora-da-
caixa.md:23` ("mas o `plugin.py`/ViewModel em volta, sim") foi avaliado e **não** julgado cobrança
incondicional — é escopo de redesenho do plugin.py/ViewModel existente, não uma exigência de
MVVM/Qt independente de perfil; nenhum tíquete aberto. `.claude/PERFIL` não foi criado no hub (não é
o alvo — o hub não é aplicação).
Veredito (`guardrails-check`): não aplicável na parte de código — mudança é doutrina/texto puro nos
5 arquivos do kit (skills/agents), sem símbolo de produção, sem suíte pytest a rodar, sem piso a
mover; camadas/ACL `n/a`; nenhum teste deletado; gate do kit (`kit_check.ps1`, itens 5 e 8 da
`guardrails-check`) é o gate aplicável aqui e passou nos dois modos.

Consumo: ver docs/telemetria.tsv (linha `V2I-T8`)

A `V2I-T9` fechou em 2026-08-05 — o `pantonic-auditor-arch` passa a auditar CA **e** DDD
(`DR-4`/`D9`), sem precisar de skill externa ao kit:
- `.claude/agents/pantonic-auditor-arch.md`: `description` do frontmatter passa a citar DDD; a
  tabela de capítulos (cap. 4) ganha "invariantes, VOs imutáveis, linguagem ubíqua"; o checklist
  de verificações vai de 12 para 15 itens — três novas: **4. Invariante de agregado** (regra que
  atravessa entidades do agregado só se aplica dentro da raiz), **9. Caso de uso por plugin**
  (`D9`/`GOVERNANCA.md` §5 — plugin mapeia exatamente um caso de uso) e **13. Linguagem ubíqua**
  (termos consistentes entre PRD e identificadores do código); item 2 (pureza de domínio)
  reforçado com o enquadramento mecânico "sem import de infraestrutura". O passo 1 do Método
  (fase mecânica) e o passo 3 (o que exige leitura) foram renumerados para os novos índices.
- `.claude/skills/audit-sweep/SKILL.md`: 3 blocos novos na bateria — `DDD-pureza` (imports de
  infra/framework dentro de `contracts/domain/`), `DDD-vo` (`@dataclass` sem `frozen=True` em
  `contracts/domain/`) e `DDD-usecase` (`class \w+UseCase` por diretório de `plugins/*/`,
  detecta plugin sem caso de uso ou com mais de um).
- **Escopo respeitado:** verificações agnósticas a stack, sem condicional de perfil (ao contrário
  da `T8`) — DDD vale para todo projeto Pantonic*, não só `desktop-pyside6`.

Dry-run dos 3 greps novos no hub (`PantonicApp` não tem `contracts/domain/` nem `plugins/` — é o
hub de governança, não uma aplicação): os três padrões rodaram sem erro de sintaxe/regex
(confirmado sem `lookaround`, incompatível com o ripgrep do ambiente) e retornaram vazio —
resultado esperado e aceitável (nota operacional da tarefa), não colapso.

Verificação: `pwsh .claude/checks/kit_check.ps1 -Mode generate` → `README.md regenerado: 9
agente(s), 9 skill(s)`; `-Mode check-drift` → `check-drift OK` — exit 0 nos dois modos
(`description` do `pantonic-auditor-arch` mudou, README derivado precisava regenerar).
`check-readme.ps1` **não** rodado de propósito — divergência de contagem de guardrails já
prevista e aceita até a `V2I-T11` (nota operacional da tarefa, herdada da `V2I-T7`).

Veredito (`guardrails-check`): não aplicável na parte de código — mudança é doutrina/texto puro em
2 arquivos do kit (agent + skill), sem símbolo de produção, sem suíte pytest a rodar (hub não tem
`tests/`), sem piso a mover; camadas/ACL `n/a`; nenhum teste deletado; gate do kit
(`kit_check.ps1`, item 5 da `guardrails-check`) é o gate aplicável aqui e passou nos dois modos —
mesmo raciocínio da `V2I-T8`.

Consumo: ver docs/telemetria.tsv (linha `V2I-T9`)

A `V2I-T10` fechou em 2026-08-05 — um projeto novo nasce sob a doutrina corrigida, sem presumir
desktop em momento algum:
- `GOVERNANCA.md` (§6, item 2, linha real 440 — o plano apontava `:297`, desatualizado por
  edições anteriores do Estágio 5): o artefato *Architecture* deixa de ser "MVVM + clean
  architecture" e passa a "clean architecture + DDD, com MVVM apenas no perfil `desktop-pyside6`
  (§1.1)".
- `.claude/skills/bootstrap-pantonic/SKILL.md`: a fase 2 (Architecture) ganhou o passo de
  perguntar e registrar o **perfil** do projeto (`GOVERNANCA.md` §1.1) em `.claude/PERFIL` antes
  de qualquer especialização de camada — perfil nomeado ou perfil novo descrito na doutrina, com
  `desktop-pyside6` como padrão só na ausência de resposta, mas o arquivo sempre escrito (nunca
  perfil implícito); o texto do modelo conceitual passou para clean architecture + DDD, com MVVM
  condicionado ao perfil declarado; a fase 5 (estrutura inicial) ganhou a entrada `.claude/PERFIL`
  na árvore; a seção de Aceitação ganhou o critério "perfil perguntado e registrado".
- `.claude/README.md` regenerado via `kit_check.ps1 -Mode generate` (conferência de rotina —
  `description` do `bootstrap-pantonic` não mudou, regeneração ficou idêntica à baseline).

Verificação: `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` → `check-drift OK - .claude/
README.md == regenerado (9 agente(s), 9 skill(s))` — exit 0, igual à baseline do dossiê; `-Mode
validate` → `VERSION == KIT_VERSION ('2.0.0')` também OK.

Veredito (`guardrails-check`): não aplicável na parte de código — mudança é doutrina/texto puro em
2 arquivos do kit (doc de governança + skill), sem símbolo de produção, sem suíte pytest a rodar
(hub não tem `tests/`), sem piso a mover; camadas/ACL `n/a`; nenhum teste deletado; gate do kit
(`kit_check.ps1`, item 5 da `guardrails-check`) é o gate aplicável aqui e passou nos dois modos —
mesmo raciocínio da `V2I-T8`/`V2I-T9`.

Fora de escopo respeitado: `MVVM + clean architecture` ainda aparece em `docs/DIARIO_DE_OBRAS.md`
(citações históricas de fechamentos anteriores) e em `docs/plans/P-0730-v2-identidade.md` (texto
do próprio dossiê da `T10`) — ambas citações de registro histórico, não doutrina viva; nenhum
tíquete aberto.

```
Veredito — V2I-T10
Suítes: n/a — mudança é doutrina/texto puro em 2 arquivos do kit (GOVERNANCA.md + skill), sem
  símbolo de produção, sem suíte pytest a rodar (hub não tem tests/)
Piso: ratchet_piso.py — OK, nenhum piso declarado
Kit: kit_check -Mode validate / -Mode check-drift — exit 0 nos dois modos (9 agente(s), 9 skill(s),
  VERSION == KIT_VERSION '2.0.0')
Espelho: check-readme.ps1 — n/a (projeto sem esse script; check ligado ao README público, fora do
  escopo desta tarefa, mesmo raciocínio da V2I-T9)
Checklist de review: ok (mudança textual, sem import/camada/ViewModel/sinal/mirror tocado)
dead_code.py: OK - 0 achado(s)
```

Consumo: ver docs/telemetria.tsv (linha `V2I-T10`)

A `V2I-T11` fechou em 2026-08-06 — o `README.md` volta a ser fiel, agora a uma fonte correta, e
assume a voz de contrato (`DR-7`, `D1`, `D2`, `D6`, `D11`):
- **Título e preâmbulo**: cai "aplicações desktop" do título; cai a frase *"não existe para
  convencer ninguém a adotar o framework: quem lê já o usa"* — o README passa a se declarar
  **documento canônico, o contrato entre o framework e quem o adota**, com a evidência de campo
  (os desvios do Estágio 5 vieram da leitura do README). A dívida (a) da `V2I-T7` está fechada: a
  contradição com `GOVERNANCA.md` §9 não existe mais.
- **§1**: identidade agnóstica a tecnologia e plataforma; modalidades desktop/container/web/
  servidor; tabela dos **dois níveis** (arquitetura ↔ `ARQUITETURA_PANTONICA.md`; projeto ↔
  `GOVERNANCA.md` §3-§9); eixo invertido para **qualidade → rota → custo** com a doutrina da
  qualidade como motor e custo declarado restrição, não razão de ser (`DR-3`, `D6`).
- **§2**: as cinco premissas trocadas pelas da fonte (CA+DDD, infracore, um plugin = um caso de
  uso, core comum, guardrails executáveis); régua de altura alinhada à `GOVERNANCA.md` §2; nova
  subseção `### Perfis: o que a modalidade acrescenta`, com os três perfis, `.claude/PERFIL`, o
  default `desktop-pyside6` e o `PantonicVideo` nomeado como **case de referência**.
- **§3**: reaberta declarando custo como o **terceiro** eixo — a frase "todo o resto do framework
  deriva de uma conta" saiu; o modelo econômico continua inteiro, agora como restrição.
- **§10**: 14 → **15 regras**, com a linha nova do `G-README` (gate de review, aceite do dono, o
  script cobrindo estrutura e não sentido) e o item 3 (MVVM) marcado `[perfil desktop-pyside6]`;
  distribuição por tipo de enforcement recontada (sete testes, seis review/instrução). Dívida (b)
  da `V2I-T7` fechada.
- **§11**: `pantonic-auditor-arch` agora "clean architecture **e DDD**"; auditores de perfil
  marcados; `guardrails-check` com MVVM qualificado.
- **§15** (congelada como histórico): nota de revisão no topo registrando que o veredito "MANTER"
  de `D1` foi derrubado no Estágio 5; bullet de `D1` e linha de MVVM requalificados; linha de
  guardrails 8 → **15**; "porta de entrada humana" passa de *espelho declarado* a **documento
  canônico**. Nada mais foi reescrito: a seção descreve a `2.0.0` na linguagem da época.
- **§5** (fora dos alvos, tocada por afirmar stack fixo): o artefato *Architecture* deixa de ser
  "MVVM mais clean architecture" e passa a CA+DDD com o padrão de apresentação do perfil.

Verificação: `pwsh .claude/checks/check-readme.ps1` → **exit 0** (`9 agente(s), 9 skill(s), 15
guardrail(s), versão '2.0.0', 15 seção(ões) com Fonte da verdade válida`). Varredura de "pronto
quando": `Grep -i "desktop|PySide|MVVM|\bQt\b"` no README devolve 13 ocorrências, todas dentro de
**perfil**, de **case de referência**, da lista de modalidades cobertas ou da nota histórica do
§15 que declara a queda da premissa — nenhuma afirmação de stack fixo sobreviveu.

Veredito (`guardrails-check`): não aplicável na parte de código — mudança é texto puro em 1 arquivo
(`README.md`), sem símbolo de produção, sem suíte pytest a rodar (hub não tem `tests/`), sem piso a
mover; camadas/ACL `n/a`; nenhum teste deletado. O gate aplicável é o `check-readme.ps1`, exit 0
acima — mesmo raciocínio da `V2I-T9`/`V2I-T10`, com o espelho agora **dentro** do escopo.

Escopo não ampliado: o **glossário** do framework permanece com a `V2I-T11b`, e a versão do README
segue em `2.0.0` — o bump para `2.1.0` (`DR-6`) é da `V2I-T13`. Nenhum achado exigindo doutrina
inexistente na fonte apareceu; nenhum tíquete aberto.

Consumo: ver docs/telemetria.tsv (linha `V2I-T11`)

A `V2I-T11b` fechou em 2026-08-06 — o `README.md` ganha o **glossário do framework**, para que o
contrato deixe de depender de vocabulário privado (`DR-7`):
- **Seção nova `## Glossário — o vocabulário deste framework`**, não numerada, inserida entre o
  preâmbulo (após o `---` que fecha a tabela de seções) e a `## 1.`. Não numerada de propósito:
  nada é renumerado e todo ponteiro externo do tipo `README §10`/`§12` segue válido.
- **Três eixos, 39 verbetes.** *Arquitetura* (13): regra de dependência, infracore, core pantônico,
  contracts, serviços de expressão, ACL, egress, plugin, caso de uso, linguagem ubíqua, objeto de
  valor, agregado, perfil. *Projeto* (9): diário de obras, tarefa atômica, handover, guardrail,
  piso de regressão, conformance, modelo por fase, contexto, orçamento de turnos. *Metadados* (17):
  kit, hub, consumidor, `sync-kit`, drift, espelho, fonte da verdade, `KIT_VERSION`, tag
  `kit-vX.Y.Z`, plano `P-NNNN`, iniciativa, estágio, sprint, tíquete `TK-`, agente, skill, decisão
  `DR-`/`DP-`.
- **Forma de cada verbete:** uma frase de definição + "Onde a regra mora: `<fonte>`". Nenhum
  verbete é a única fonte de uma regra (critério anti-duplicata; `docs/RESIDENCIA_DOUTRINA.md`,
  padrão `DR-A`) — o glossário define o termo e aponta, nunca normatiza.
- **Linha `> Fonte da verdade:`** presente, apontando `GOVERNANCA.md` §3.1 (residência e
  precedência da doutrina), que é a autoridade sobre "onde cada regra mora".

Verificação: `pwsh -NoProfile -File .claude/checks/check-readme.ps1` → **exit 0**
(`check-readme: OK - 9 agente(s), 9 skill(s), 15 guardrail(s), versão '2.0.0', 15 seção(ões) com
Fonte da verdade válida.`). Baseline idêntico ao de antes da tarefa — ver achado (a): o guarda
**não conta** seção não numerada.

Veredito (`guardrails-check`): não aplicável na parte de código — texto puro em 1 arquivo
(`README.md`), sem símbolo de produção, sem suíte pytest (hub não tem `tests/`), sem piso a mover;
camadas/ACL/MVVM `n/a`; nenhum teste deletado. Gate aplicável = `check-readme.ps1`, exit 0 acima.

Achados:
- **(a) O dossiê da `T11b` previa `15 → 16 seção(ões) com Fonte da verdade válida`; a previsão está
  errada e a medição mostra que continua 15.** Causa lida no código: `check-readme.ps1:58` só
  indexa headings que casam `^## (\d+)\. `, de modo que seção `##` **não numerada** fica invisível
  às cinco checagens. A consequência doutrinária é que a linha `> Fonte da verdade:` do glossário
  **não é verificada por guarda nenhum** — ela está lá por disciplina, não por enforcement. A rota
  do plano não muda (a própria `T11b` previu o caso: "obrigatória se o guarda a enxergar,
  inofensiva se não"), mas o vão de cobertura é real. Registrado como tíquete `TK-07`.
- **(b) "Estágio" não tem residência normativa.** O termo estrutura a iniciativa `PANTONIC-V2`
  inteira (Estágios 1 a 5) e não é definido em `GOVERNANCA.md` nem em skill alguma — só aparece em
  uso, no diário e nos planos. Pelo critério anti-duplicata, o verbete **não** criou a regra: ele
  descreve a convenção e aponta para onde o uso está registrado (`docs/DIARIO_DE_OBRAS.md` e
  `docs/DIARIO_HISTORICO.md`). Decidir se "estágio" vira conceito normativo (com regra de
  abertura/fechamento) ou permanece convenção é do dono — registrado como tíquete `TK-08`.

Consumo: ver docs/telemetria.tsv (linha `V2I-T11b`)

A `V2I-T11c` fechou em 2026-08-06 — o `README.md` deixa de narrar a própria gestação. O critério é a
skill `redacao-doc` (`.claude/skills/redacao-doc/SKILL.md`), não o gosto: o conteúdo técnico já
aceito na `V2I-T11` não foi corrigido nem ampliado em ponto nenhum. A tarefa correu em três passadas
sobre faixas disjuntas do arquivo:

- **Preâmbulo (linhas 1–37)** — refeito em passada anterior desta tarefa, pelo §7.2 da skill
  (preâmbulo se descarta e se reescreve, não se saneia por edição). Não tocado nesta passada, salvo
  a linha da `## 14.` na tabela `| § | Seção |`.
- **Passada B — `## Glossário` até o fim da `## 7.`** — faixa de **572 → 548 linhas** (−24);
  V2 18→16, V3-data 1→0, V4 1→0, V7 2→0, V3-id 3→3, V8 1→1. Trocou o rótulo de beat
  `**Por que foi adotado.**` por `**Por quê.**` nas §3–§7: o rótulo antigo é o contêiner do vício —
  a própria skill o define (§2, exemplo V4) como "a evidência ou o episódio que o produziu".
- **Passada C — `## 8.` até o fim do arquivo (§8–§15)** — faixa de **499 → 481 linhas** (−18), com
  toda seção encolhendo. Método do §7.3: cada seção reescrita a partir da afirmação que ela existe
  para fazer, não a partir do texto antigo.

O que mudou na faixa `## 8.`–`## 15.`:

- **Rótulo espelhado (C1).** `**Por que foi adotado.**` → `**Por quê.**` nas §8, §9, §11, §12 e §13.
  O arquivo passa a ter um único rótulo para o beat (10 ocorrências, 0 do antigo); `**O que é.**` e
  `**Onde o gerente intervém.**` inalterados.
- **§8.** O beat perde a colisão de nomenclatura contada com os identificadores reais dos planos; a
  razão fica atemporal ("nome derivado de data não é único").
- **§9.** Saem "o checkpoint nasceu do modo de falha oposto" (V1) e a enumeração "o que já foi
  decidido" (V2); "ou antes disso" → "ou antes" (V7).
- **§10.** Saem "a parte honesta desta seção", "o framework não esconde isso" e "quanto do framework
  sobrevive a um dia ruim" (V4/V5). A distribuição por tipo de enforcement e os limites declarados
  dos itens 14 e 15 permanecem, em dois parágrafos no lugar de três. Título `Os guardrails` intacto.
- **§11.** Título `Anatomia do kit` e a tabela de 10 skills intactos; o beat perde "invocados pelo
  usuário" e a moldura narrativa da pré-varredura, mantendo o motivo econômico.
- **§12.** Saem "por decisão registrada" e "o que este espelho descreve acima". O número do
  auto-relato deixa de ser um caso ("~90k contra ~140k reais num caso registrado") e vira a faixa
  medida (**11% a 44%**) — é ela que muda a decisão do leitor.
- **§13.** Sai "a escolha do prefixo de publicação ... foi deliberada"; a razão fica no presente.
- **§14 — reescrita (C2).** Título `Decisões e a evidência medida que as motivou` →
  **`Decisões estruturantes e seus trade-offs`**, com o número `## 14.` preservado (renumerar
  quebraria os ponteiros `§10`/`§12` do próprio texto e as âncoras do guarda); a linha
  correspondente da tabela `| § | Seção |` do preâmbulo foi atualizada — única edição acima da
  `## 8.`. A coluna `Evidência que a produziu` vira **`O que se paga por ela`**: as 8 linhas passam
  a declarar o que vale hoje e qual é o custo de segui-lo. Números medidos que mudam a decisão do
  leitor permanecem (71 turnos e ~189 mil tokens numa tarefa atômica no modelo errado; desvio de
  11–44% do auto-relato; teto ≤30 porque 5 de 7 tarefas medidas estouram ≤25); saem o episódio, a
  data, o ID de tarefa e quem decidiu. O fecho ("cada uma tem um número, uma data e um incidente
  atrás dela") vira uma linha.
- **§15 — seção histórica declarada (C3).** Pelo §5 da skill, **V7 é liberado** ali (o assunto *é* a
  mudança entre versões); V1–V5 continuam proibidos, e o toque foi leve. Sai o bloco
  `Revisão do Estágio 5 (2026-08-06)` — que trazia "a premissa errada só apareceu quando o dono leu
  este documento" (V2 + V3 + data) — substituído por uma nota de correção sem episódio; "A origem" e
  o bullet D1 perdem os estágios numerados; saem `DR-7` e os identificadores `P-0722`/`P-0729` da
  tabela e dos bullets. O conteúdo histórico (vereditos, contagens, tabela antes → depois) fica
  inteiro.

Contagem por vício no **arquivo inteiro** (varredura do §6 da skill):

| Vício | Baseline da `T11c` | Pós-B | Pós-C |
|---|---|---|---|
| V2 — interlocutor | 43 | 38 | **34** |
| V3 — ID de processo | 16 | 15 | **4** |
| V3 — data | 3 | 2 | **0** |
| V4 — anúncio de estrutura | 2 | 0 | **0** |
| V1 — proveniência | 4 | 1 | **0** |
| V7 — datação viva | 3 | 1 | **0** |
| V8 — dívida de processo | 2 | 2 | **2** |

Linhas do arquivo: **1114 → 1066** (−48 no total da tarefa: −7 no preâmbulo refeito, −24 na passada
B, −18 na passada C, +1 da linha nova na tabela de skills). O baseline do dossiê chegou a anotar 935
linhas por erro de medição do orquestrador (`Measure-Object -Line` não conta linha em branco); o
número correto, por contagem direta, é **1114**, e foi corrigido no dossiê e acima. Os deltas por
vício não são afetados — todos vieram do mesmo arquivo, medidos antes e depois com o mesmo padrão.

Exceções mantidas, pela régua do §3 da skill:

- **V2 = 34 — todas construção de papel, não de interlocutor.** Passam no teste "troque o nome do
  papel por *qualquer pessoa nesse papel*": "só o dono promove memória", "o executor não pergunta ao
  dono", "não vale o turno do dono confirmar o óbvio". Nenhuma é pessoa como narradora ou testemunha
  de episódio.
- **V3 = 4 — o *esquema* de identificador, não instância de processo.** `T1..Tn` (§6 e §8: a forma
  que uma tarefa de plano tem) e `S1-T3`/`TK-042` dentro do bloco que exibe a forma literal do índice
  do diário. Documentar o formato de um identificador não é citar um processo.
- **V8 = 2 — regra atemporal de residência.** As duas ocorrências são a mesma regra ("colisão não se
  resolve com as duas cópias vivas"), no glossário e na §12: enuncia como a precedência se aplica,
  sem processo pendente atrás.

Verificação: `pwsh -NoProfile -File .claude/checks/check-readme.ps1` → **exit 0**
(`check-readme: OK - 9 agente(s), 10 skill(s), 15 guardrail(s), versão '2.0.0', 15 seção(ões) com
Fonte da verdade válida.`). Invariantes estruturais conferidas: `## 8.` a `## 15.` sem seção criada,
removida ou renumerada; títulos `Anatomia do kit` e `Os guardrails` literais; `> Fonte da verdade:`
presente em todas as seções numeradas.

Veredito (`guardrails-check`): não aplicável na parte de código — texto puro em 1 arquivo
(`README.md`), sem símbolo de produção, sem suíte pytest (hub não tem `tests/`), sem piso a mover;
camadas/ACL/MVVM `n/a`; nenhum teste deletado. Gate aplicável = `check-readme.ps1`, exit 0 acima.

Achados: nenhum que exija ação futura. O `TK-07` (guarda cego a seção não numerada) segue aberto e
inalterado por esta tarefa.

Consumo: ver docs/telemetria.tsv (linha `V2I-T11c` — soma medida das duas passadas)

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
