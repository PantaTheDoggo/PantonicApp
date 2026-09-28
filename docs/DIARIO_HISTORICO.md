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

---

## P-0733 — Quitação da dívida de doutrina e de kit do hub

> **Índice (texto integral do campo Título, migrado da tabela ativa em 2026-08-23):** Quitação da dívida de doutrina e de kit do hub — os 12 tíquetes vivos do índice em 13 tarefas (`DHB-T1..T13`): doutrina decidida e não executada (`TK-15`, `TK-17`, `TK-21`, `TK-22`), resíduo de vocabulário do kit (`TK-04`, `TK-12`, `TK-20`), guarda e navegação desalinhadas (`TK-06`, `TK-07`, `TK-10`), a não-promoção de "estágio" (`TK-08`) e a revisão final do espelho (`TK-18`); `DH-1..DH-7` fechadas no ato (1/13)
>
> *(Âncora original do índice, preservada:* `docs/plans/P-0733-divida-do-hub.md` *)*

**Objetivo:** quitar os doze tíquetes que sobraram no índice quando a iniciativa anterior encerrou,
agrupados por dívida: doutrina decidida e não executada, resíduo de vocabulário do kit, e guarda e
navegação desalinhadas do que guardam. Fecha na revisão final do espelho, que era o único tíquete
postergado por decisão, e no aceite do dono sobre o `README.md`.

**Plano:** `docs/plans/P-0733-divida-do-hub.md` — 13 tarefas (`DHB-T1..T13`), ordem linear sem ramo
condicional, decisões `DH-1..DH-7` fechadas no ato do planejamento. Nenhuma questão owner-gated
pendente: `TK-07` e `TK-08` foram levadas ao dono e decididas antes da publicação.

**Tíquetes cobertos:** `TK-04`, `TK-06`, `TK-07`, `TK-08`, `TK-10`, `TK-12`, `TK-15`, `TK-17`,
`TK-18`, `TK-20`, `TK-21`, `TK-22`. Cada um fecha na tarefa que o executa; o `TK-08` fecha como
recusa registrada (não vira conceito normativo) e o `TK-18` deixa de ser `blocked` por posição na
ordem — ele é a penúltima tarefa, quando as fontes já pararam de mudar.

**Próxima tarefa:** nenhuma — **plano `cancelled` em 2026-08-22**, corte seco por decisão do dono
(`P-0737` `DU-1`). A dívida que ele quitava não é caminho para o objetivo herdado da
`EXECUCAO-AUTONOMA`; os tíquetes que ele cobria foram podados pelo critério de
`docs/plans/P-0737-loop-autonomo.md` §5, e os dois que sobrevivem ao critério (`TK-04`, `TK-18`)
entram absorvidos por aquele plano. A `DHB-T1` entregue permanece como registro; nenhuma tarefa nova
sai deste plano.

---

## P-0734 — Execução autônoma

> **Índice (texto integral do campo Título, migrado da tabela ativa em 2026-08-23):** Execução autônoma — o backlog deixa de custar um round-trip humano por tarefa: papel de orquestração (skill `scrum-master`), papel de revisão (agente `pantonic-reviewer`) e documental gerado por função (telemetria/RDO/evidência), com o registro canônico da tarefa migrando do diário para `docs/RDO/` (`EXA-T1..T17`; `DA-1..DA-10` fechadas no ato, três desenhos postergados viram `T2`/`T3`/`T4`; alcance = hub primeiro, medir, depois propagar; `DA-9` revogada pelo dono em 2026-08-08 e substituída pela `DA-11` — Regra 2 passa a governar integridade de contexto, com a `T6` partida em `T6a`/`T6b`, a `T8` em `T8a`/`T8b`/`T8c` e a `T9` em `T9a`/`T9b` por orçamento; **`DP-D` ratificada em 2026-08-10** — o pacote de retorno de 8 campos deixa de existir, o RDO passa a ser gerado no fechamento e a retentativa vira agente novo em contexto novo, com `T18`..`T21` novas; **`DP-E` ratificada em 2026-08-11** — o `status` é característica da tarefa e quem o gerencia é o `scrum-master`, o laudo perde o campo, *inspetor* é abolido em favor de `pantonic-reviewer`, e os sete estados enunciados pelo dono viram objeto de avaliação própria antes de virar norma, com `T22`..`T27` novas e `T19`/`T20`/`T21` marcadas pendentes de reescrita; **`DP-F` fechada pela `T22` e ratificada pelo dono em 2026-08-11** — os sete estados avaliados como suficientes, com `backlog`→`ready`, `in progress`→`in-progress` e `superseded` fora do vocabulário de tarefa; destrava `T23`..`T27` e a reescrita de `T19`/`T20`/`T21`; `T23` partida em `T23a`/`T23b` por orçamento; **`DP-G` ratificada pelo dono em 2026-08-11** — a fronteira de `status` separa **autoria** (executor é autor de `review` e `blocked`, e de mais nada) de **materialização** (só o `scrum-master` grava, em qualquer estado), o `blocked` do executor é canal único com **razão tipada** (`dependencia` reordena a fila e segue; `premissa` para e escala), e daí a `T21` partida em `T21a`/`T21b` por orçamento mais a `T28` nova de sanitização; `T19`/`T20`/`T21` reescritos na mesma rodada e a fila reordenada para que a conformidade suceda o loop; **`DP-H` fechada em 2026-08-11**, por derivação do insumo do dono (`§12`) e sem decisão nova — a fronteira **conceito do framework × desenvolvimento do framework** escopa cada orientação, a regra de recência vale só dentro dos planos de desenvolvimento e não entra em artefato publicado, dossiê de tarefa executada é orientação e se concilia enquanto o que narra o ocorrido permanece intocado, o laudo é consumido e **descartado** pelo `scrum-master` e o `pacote` existe **dentro do laudo** (não é objeto devolvido pelo executor), com `T29` (artefato **tarefa**), `T30` (**utilidade**) e `T31` (resíduo de `pacote de retorno`) novas, `T19`/`T20`/`T21a`/`T21b`/`T23a`/`T26` e os achados do `§9` reconciliados, `TK-31` fechado e a fila reaberta pela `T19`; **`DP-K` fechada em 2026-08-11**, por ratificação do dono dos três pontos que a `DP-H` devolveu — a ambiguidade no framework **escala ao dono** (desempate que estava declarado não decidido, agora com residência no `GOVERNANCA.md` §3.1), `reviewer` vira **termo único** e abole também a forma *revisor* no texto vivo, e os **quatro artefatos canônicos** ganham hierarquia (plano → tarefa → laudo → RDO: a tarefa é a comunicação **entre agentes** e a verdade da tarefa em execução, o laudo é **efêmero** e move para `done` ou devolve para `in-progress`, o RDO é a comunicação com o **dono** e pressupõe tarefa finalizada, e **nenhum substitui o outro**), com `T32` (desempate) e `T33` (`reviewer`) novas e `T29`/`T30`/`T21a`/`T21b`/`T31` reconciliadas) **`TK-32` aberto em 2026-08-11** — uso e teto passam a ser medida de agregado, com regime interino de teto não-bloqueante e a `T34` nova, que decide e para junto de `DP-I`/`DP-J`; **`DP-M` ratificada em 2026-08-11** — o laudo se padroniza por função e vira mínimo e suficiente (`--observacoes` sai), e no lugar de coibir papel a papel entra a golden rule de escopo de agente como guardrail 15 do `GOVERNANCA.md` §7, com espelho em lockstep; a matriz de responsabilidades passa a ser autoridade exaustiva, o que torna a auditoria de completude precondição, e as tarefas `T35`..`T39` novas materializam a decisão; **`DP-N` ratificada em 2026-08-12** — o executor **sinaliza `review` ou `blocked` e nada mais**: não marca `in-progress`, não escreve bullet, não invoca `handover` e não grava consumo, e o achado fora de escopo vira uma linha do sinal que o `scrum-master` indexa; a verificação **fica** com ele, como responsabilidade de entregar tecnicamente correto, não de aferir aceitação; o `reviewer` não muda (dossiê + evidência + diff já são a coleta descrita), o `TK-35` fecha na `T40` e a reorganização da passagem de bastão vira o `TK-36`, com `T40`/`T41` novas; **`DP-O` fechada em 2026-08-12** — a matriz de responsabilidades é o **limitador exaustivo** de todo agente e o texto que atribui ato não endossado (ou papel sequer citado) é **não-conformidade grave, que para e regulariza**, com a régua já publicada no guardrail 15 e a resposta na descoberta entrando nele, mais a varredura dos dois universos fechados do framework e a lacuna da matriz subindo ao dono, materializadas em `T42`/`T43`/`T44`; **`T34` cancelada por absorção em 2026-08-12** — a matéria de uso e teto se revê inteira em plano próprio, aberto depois deste, o desdobramento é o item 4 da `T17` e nenhuma `DP-L` se forma aqui, de modo que a ratificação em lote fica com `DP-I` e `DP-J`; **bloco da `DP-O` encerrado em 2026-08-12 pela `T44`** — kit executável e doutrina varridos contra a matriz, com as duas ocorrências de classe (c) apontando para a lacuna já encaminhada ao `TK-36`; **`T25` fechada em 2026-08-13** — o espelho e os índices passam a falar a lista final da `DP-F` e a apontar para a residência única; **`T45` aberta em 2026-08-13** como card prioritário do `TK-39` — o critério de aceitação do §19 deixa de ser contagem de acionamentos do gerente; **fechada em 2026-08-13** — a aceitação passa a classificar cada acionamento pela causa (causa do gerente é legítima e ilimitada; caminho feliz é defeito), com residência na doutrina (`GOVERNANCA.md` §4.3) e na skill que conduz o loop, e o achado da tabela de riscos do §6 aberto como `TK-40`; **`DP-P` ratificada em 2026-08-13** — a golden rule do dono vira o guardrail 16 (`G-SURFACE`: mudança de decisão estruturante regulariza a superfície de contato inteira, no ato) e a consolidação é executada de imediato em dois universos fechados, com `T46` (a régua), `T47` (o plano) e `T48` (os artefatos publicados) novas, todas fechadas no mesmo dia — o `TK-40` quitado dentro da `T47`, o `TK-42` aberto com o resíduo fora dos universos declarados, e **duas ocorrências de classe (c) subindo ao dono como `TK-41`**, que bloqueia a `T16` e a `T17`; **`DP-Q` fechada em 2026-08-13** pela decisão do dono sobre o `TK-41` — teto numérico não governa fluxo (caem o roteamento por estouro `A4`, os dois números do fim de janela `B2`, o proxy operante de capacidade, o gatilho de checkpoint por 2/3 do teto e a ramificação por consumo no gerador), custo e consumo passam a ser informação de agregado com residência do qualitativo no card "Lições aprendidas na tarefa", e a matéria de limites vai inteira para plano próprio; primeira aplicação real do `G-SURFACE`, com `T49`, `T50`, `T51a`, `T51b` e `T52` novas e todas fechadas no mesmo dia, e a `T13` repositionada à frente da `T29` por virar o único critério de capacidade; **`T13` fechada em 2026-08-15** com laudo `aprovado` 100% e recomendação `escalar`, que sobe o `TK-43` ao dono; **`DP-R` fechada em 2026-08-15** — o *quê* por decisão do dono (hook canônico ganha **residência versionada própria**, com materialização no `settings.json` local; recusado o proxy só-do-hub, porque a capacidade do `GOVERNANCA.md` §4.3 vincula todo Pantonic\* e viraria regra sem meio de cumprimento no consumidor) e as **derivações de planejamento** fechadas na rodada do mesmo dia, sem decisão nova de arquitetura: residência em `.claude/hooks/hooks.json` com o comando portável por `{KIT_ROOT}`, materializador idempotente `.claude/tools/hooks_sync.py` (`apply`/`check`/`drift`) que preserva `permissions.deny` e todo hook não-kit, `kit_check` cobrando o canônico no `-Mode validate` e a materialização no `-Mode check-drift` (inclusive hook de kit registrado direto no arquivo local, que é a regressão do próprio `TK-43`), `sync-kit.ps1` inalterado e nenhum derivado tocado (`DA-3`; `docs/CONSUMIDORES.md` registra 0/6 com `.claude/kit/`), com `T53`/`T54` novas entrando **em bloco** logo depois da `T13` e antes da `T29`, o dossiê da `T14` reescrito (a rota por `settings.json` caiu; a tarefa passa a depender da `T53`) e o campo *Arquivos-alvo* do `### T13` conciliado com nota datada (`scrum-master` e `GOVERNANCA.md` §4.3, tocadas por consequência obrigatória); questão adjacente **fechada pela `DL-7`** (decisão do plano `P-0735`: `permissions.deny` é canônico, vira chave declarada do alvo `projeto`, `permissions.allow` e demais subchaves de `permissions` intocadas) — o `permissions.deny` do guardrail 13 tinha o mesmo defeito de distribuição; **rebaseado pelo `P-0735` em 2026-08-15** — classificação **(A)** da convenção de planos derivados: a premissa da iniciativa continua de pé, mas a matéria de residência e distribuição passa a ser resolvida em forma geral no plano novo, e o plano de origem fica **suspenso em 49/60** até ele fechar; `T53` e `T54` **canceladas por absorção** (o desenho da `T53` sobrevive integral na `RPC-T2`/`RPC-T3` e só a residência particular `.claude/hooks/hooks.json` desaparece; o item da `T54` que mandava preservar o bullet do hook global do `modelo-por-fase` é **revogado** pela régua nova), e a dependência declarada da `T14` passa da `T53` para a `RPC-T2` (49/60)
>
> *(Âncora original do índice, preservada:* substituído por `docs/plans/P-0737-loop-autonomo.md` *)*

**Objetivo:** a execução do backlog deixa de custar um round-trip humano por tarefa atômica e passa
a ser um loop conduzido pelo próprio agente — papel de orquestração (skill `scrum-master`), papel de
revisão (agente `pantonic-reviewer`) e documental gerado por função, com o registro canônico da
tarefa migrando do diário para `docs/RDO/`.

**Plano:** `docs/plans/P-0734-execucao-autonoma.md` — **31 tarefas atômicas** (`EXA-T1..T27`, com
`T6`/`T8`/`T9` partidas em `a`/`b`/`c` por orçamento), ordem linear, decisões `DA-1..DA-10` fechadas
no ato; três desenhos postergados viram as tarefas `T2`, `T3` e `T4`. Cinco decision records
ratificados: `DP-A`..`DP-C` (2026-08-08), `DP-D` (2026-08-10, reconciliação do fluxo) e **`DP-E`
(2026-08-11, §10 — o `status` é da tarefa, não do laudo)**, que encomenda `T22`..`T27` e deixa
`T19`/`T20`/`T21` pendentes de reescrita. Alcance: hub primeiro, medir, depois propagar.

**Estado — `superseded` em 2026-08-22**, rebase de classificação (B) pelo `P-0737` (decisão do dono,
`DU-4`). As **52 de 61** entregues permanecem como registro e nada delas se refaz; as **8** tarefas
abertas restantes são absorvidas uma a uma pelo `P-0737` (mapa em
`docs/plans/P-0737-loop-autonomo.md` §4: `T29`→`AUT-T2`, `T30`→`AUT-T3`, `T19`→`AUT-T4`,
`T12`+`T23b`→`AUT-T6`, `T26`→`AUT-T8`, `T27`→`AUT-T8`+`AUT-T9`, `T17`→`AUT-T10`) e a `T16` (piloto) é
**cancelada por absorção** no plano recomendado do piloto. **Próxima tarefa:** nenhuma — fora do
backlog, nenhuma tarefa nova sai daqui; a iniciativa continua no `P-0737`.

- **`EXA-T1` — spike de plataforma — `done`.** Entregável em
  `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md`, quatro sondas com evidência colada.
  **Sonda 1 (aninhamento de subagentes): `derrubada`** — aninhamento funciona, observado até
  profundidade 3 (contexto principal → `pantonic-executor` → `general-purpose` → `context-scout`).
  **Sonda 2 (`model` da chamada vence o `model:` do arquivo do agente): `confirmada`** — arquivo do
  `pantonic-scout` fixa `haiku`, chamada passou `opus`, system prompt do subagente declarou
  `claude-opus-5`; a `DA-8` é implementável. **Sonda 3 (observabilidade de contexto): `parcial`** —
  o payload de `PreToolUse` expõe `transcript_path`, então o proxy por hook é viável; nenhum bloco
  de uso de tokens vem pronto no payload, e a variante do contador calibrado por telemetria não foi
  medida (`TK-23`). **Sonda 4 (arquivo escrito por um subagente, lido por outro): `confirmada`** —
  cenário original produzido, o transporte por arquivo da `T2` tem base.
  Executada em duas rodadas: a primeira mediu a Sonda 1 contra `context-scout`, um agente cujo
  toolset declarado não inclui `Agent`, e o resultado media a definição daquele agente em vez de um
  limite de plataforma — defeito do dossiê de delegação, não da execução. A rodada corretiva
  re-mediu as Sondas 1 e 4 e deixou nota de correção no topo do documento. Orçamento estourado por
  isso: 26 tool uses contra teto de 20 (19 + 7).
  Consumo: ver `docs/telemetria.tsv`.

**Reexame da `DA-1` — resolvido em 2026-08-08.** A `EXA-T1` derrubou a premissa em que a decisão se
apoiava (subagente não invocaria subagente). O dono reexaminou e **manteve o scrum-master como
skill no contexto principal**, com o argumento trocado de impossibilidade técnica para controle: o
loop autônomo precisa de um ponto onde o dono interrompe sem derrubar a sessão, e profundidade 3
observada numa única tentativa não sustenta mudar a arquitetura do orquestrador. Registrado no
`DA-1` e no §2 do plano; a `T2` está desbloqueada.

- **`EXA-T2` — decisão do transporte do pacote de retorno — `done`.** `DP-A` fechada como
  **transporte por arquivo** e ratificada pelo dono no ato: o executor grava o pacote no RDO e
  devolve 1 linha de confirmação; o reviewer lê o arquivo e devolve 2 linhas de veredito; o
  orquestrador nunca ingere o corpo. Medição que sustenta (29 handovers da série `V2E-*`/`V2P-*`):
  mediana 2 839 chars, p90 3 926, máximo 5 345 ⇒ ~1,6k tokens/tarefa sob (a) contra ~3,4k sob (b),
  que entra duas vezes no contexto — ~90 tarefas por janela contra ~38. Argumento decisivo além do
  número: a `DA-5` já obriga a escrita do RDO, então (b) soma uma cópia em vez de substituir.
  Entregável em `docs/plans/P-0734-execucao-autonoma.md` `## Dossiês fechados por decisão`: decision
  record, campos fixos do pacote (8 campos, teto total 44 linhas, teto por campo no template de
  `rdo.py`) e gramática fixa das 3 linhas de contexto. Dossiês dependentes: **`T10` fechado**
  integralmente; **`T8`** fecha a parte da `DP-A` e segue não delegável até `T4` e `T5`; **`T11`**
  idem até `T3`. Executada inline pelo orquestrador (decisão + ratificação não são delegáveis).
  Verificação: `kit_check -Mode validate` / `-Mode check-drift` / `check-readme.ps1` / `python -m
  pytest` — exit 0, 0, 0, 0 (`3 passed in 0.24s`). Nenhum achado fora de escopo.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T3` — decisão da política de autonomia, tetos e escalada — `done`.** `DP-B` fechada e
  ratificada pelo dono no ato: **1 retentativa** por tarefa reprovada, **10 tarefas** e **900 k
  tokens** por janela autônoma. Medição que sustenta (série de 99 tarefas em `docs/telemetria.tsv`):
  mediana 85 k tokens e 29 tool uses por tarefa, p90 159 k/52, cadência real de 10-20 tarefas por dia
  ⇒ 10 × mediana = 850 k, e o teto de consumo morde primeiro quando a janela pega tarefas mais
  pesadas que a mediana; 4 das 99 tarefas precisaram de 2ª rodada e a única que passou disso
  (`V2E-T9`) foi resolvida reescrevendo o dossiê, não repetindo a execução. Entregável em
  `docs/plans/P-0734-execucao-autonoma.md` `## Dossiês fechados por decisão`: decision record,
  domínio de saída do laudo (`veredito` ∈ {`aprovado`, `ressalva`, `reprovado`} + `bloqueante`) e
  **tabela de roteamento por precedência** — bloco A (`A1`..`A9`, o que fazer com a tarefa) e bloco B
  (`B1`..`B4`, continuar ou encerrar a janela), total sobre o produto cartesiano do domínio e sem
  nenhuma célula que peça juízo do orquestrador. Dossiês dependentes: **`T11` fechado** (não tem mais
  dossiê aberto, só precedência de ordem); adendo na `T10` com o domínio do veredito; restrição
  herdada na `T5` (a rubrica produz valores do domínio, não o amplia). Executada inline pelo
  orquestrador (decisão + ratificação não são delegáveis). Achado registrado no §"Achados da
  execução": o corpo do plano manda a `T3` fechar o dossiê da `T10`, mas a `T2` já a fechara — a
  dependência real era a `T11`. Verificação: `kit_check -Mode validate` / `-Mode check-drift` /
  `check-readme.ps1` / `python -m pytest`.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T4` — decisão do formato estruturado da tarefa no plano — `done`.** `DP-C` fechada como
  **convenção de linhas rotuladas extraída por expressão regular** (opção `b`) — ratificada, não
  inventada: a tarefa segue prosa no próprio `.md`, com gramática fixa de cabeçalho e conjunto fechado
  de valores para `classe` e `modelo`. Medição que sustenta (15 planos, 129 tarefas): **119/129 (92%)**
  dos cabeçalhos já casam a gramática, `Objetivo` e `Pronto quando` em 90%, `Arquivos-alvo` em 81%,
  `Verificação` em 72% — mas **130 rótulos distintos** depois de normalizados e duas grafias da mesma
  classe dentro de um único plano. Custo de migração zero, porque o esquema foi extraído do corpus, e
  resistência à deriva estrutural, porque não há dois lados para divergir (a mesma régua da `DP-A`).
  Entregável em `docs/plans/P-0734-execucao-autonoma.md` `## Dossiês fechados por decisão`: decision
  record, gramática de cabeçalho (`ID`, `modelo`, 5 slugs de `classe` mapeados 1:1 à tabela de tetos
  de `GOVERNANCA.md` §3, `teto` autossuficiente e travado no default da classe), gramática de campo
  com normalização de rótulo, esquema de 5 campos + `extras` livres, política de plano legado (leitura
  tolerante, autoria estrita) e instrução de autoria para a `T15`. Dois achados de desenho vindos da
  medição: a **alternância `Arquivos-alvo` × `Entregável`** (sem ela a fidelidade de escopo do laudo
  não tem âncora em tarefa de decisão) e a promoção de **`Dossiê fechado por` a campo reservado**, que
  torna mecânica a regra `B3` da `DP-B`. Dossiês dependentes: **`T8`** fecha a parte da `DP-C` e passa
  a depender só da `T5`; adendos na `T11` e insumo para a `T15`. Executada inline pelo orquestrador
  (decisão não é delegável; a `T4` é a única das três sem exigência de ratificação no dossiê).
  Achados no §"Achados da execução": `TK-24` (12 tarefas não iniciadas do `P-0733` fora do esquema) e
  a deriva de grafia de classe neste próprio plano. Verificação: `kit_check -Mode validate` /
  `-Mode check-drift` / `check-readme.ps1` / `python -m pytest` — exit 0, 0, 0, 0 (`3 passed in
  0.48s`); e o esquema aplicado à mão a `T5`/`T7`/`T9` extraiu cabeçalho e campos sem ambiguidade, com
  os quatro obrigatórios presentes e a alternância satisfeita nas três. **Estouro de teto: 34 tool
  uses contra 30 da classe `redacao`** — a varredura de 15 planos/129 tarefas (insumo medido exigido
  pelo dossiê) custou 6 chamadas de medição que uma tarefa de redação típica não tem; não é
  decomposição errada, é insumo de medição embutido numa classe de redação.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T5` — rubrica do laudo — `done`.** Entregável em `docs/RUBRICA_DE_REVISAO.md` (259 linhas,
  documento publicado): **sete dimensões** discretas (`criterio-de-pronto`, `escopo`, `testes`,
  `guardas`, `rota`, `residuo`, `registro`) — as de partida do dossiê, confirmadas, com os cinco
  campos exigidos (nome, pergunta, fonte da evidência, bloqueante, os quatro níveis). Pesos
  3/2/3/3/2/2/2 (total **17**, denominador mínimo **10**); `conforme`=1, `parcial`=0,5, `não
  conforme`=0, `não se aplica` fora de numerador **e** denominador; percentual = 100 × Σpeso×valor /
  Σpeso, metade para cima. Faixas: ≥95 `aprovado`, 70..94 `ressalva`, <70 `reprovado`. Cinco
  dimensões bloqueantes (`residuo` e `registro` não): `não conforme` em bloqueante ⇒ `reprovado` +
  `bloqueante` = a primeira em ordem canônica, qualquer que seja o percentual — `aprovado` com
  bloqueante preenchida é inalcançável por construção. Domínio de saída não ampliado. `DA-7`
  materializada na coluna de fonte: mecânica / juízo / mista, com trava explícita (vermelho mecânico
  proíbe `conforme` e o gerador recusa a marcação). **Via para achado de processo** com três alvos
  (`dossiê`, `doutrina`, `rubrica`) e três invariantes — achado de processo nunca rebaixa dimensão
  de entrega, exige rota, e defeito de dossiê que impede verificação marca `parcial` (nunca
  `conforme`); achado que invalida a rota sobe ao dono pela pendência do pacote. Propriedade
  derivada dos pesos: `aprovado` ⟺ todas as aplicáveis `conforme` (menor peso 2 sobre denominador
  máximo 17 ⇒ um `parcial` já custa 5,9 pontos). Verificação: bateria do §3, os quatro em exit 0 —
  `kit_check.ps1 -Mode validate` (0), `-Mode check-drift` (0), `check-readme.ps1` (0),
  `python -m pytest` (0); varredura da `redacao-doc` §6 com 1 correção V9 aplicada. Aplicação a mão
  a três tarefas fechadas do `P-0732` (`V2P-T3`, `V2P-T7`, `V2P-T9`): as três com `testes` e
  `residuo` em `não se aplica`, denominador 12, numerador 12 ⇒ **100%, `aprovado`,
  `bloqueante=nenhuma`** — coerente com o `done` sem ressalva que o histórico registra para as três.
  A aplicação corrigiu a dimensão `escopo`: o nível `conforme` passou a admitir o artefato cuja
  atualização a doutrina torna obrigatória como consequência mecânica da mudança nos alvos (caso do
  `DOC_MAP.md` na `V2P-T3`), que na formulação anterior cairia em `parcial` e rebaixaria a tarefa a
  `ressalva` contra o registro. Sem achado fora de escopo; nenhum arquivo da lista de fora de escopo
  tocado. Tarefa de redação de doutrina, sem TF/TR de código.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T6a` — doutrina de papéis e fronteira de registro — `done`.** Entregável em
  `GOVERNANCA.md`, duas regiões, sem nenhum outro arquivo tocado. **§3, matriz de
  responsabilidades:** de 5 para **7 linhas**, com `Orquestração` entre `Planejamento` e `Execução` e
  `Revisão` entre `Execução` e `Coleta` — a ordem da tabela passa a ser a do fluxo de uma tarefa.
  `Orquestração` responde por conduzir um plano (despachar com dossiê fechado, rotear o pacote de
  retorno nos três desfechos, registrar a telemetria medida, arquivar) e não implementa, não julga
  entrega nem decide arquitetura; `Revisão` julga **uma** entrega contra o dossiê dela e emite o
  laudo, com a escrita restrita ao caminho do laudo, e não corrige, não replaneja e não fecha tarefa.
  Coluna *Modelo* preenchida nas duas com Sonnet — **derivado, não decidido**: para a orquestração,
  `DA-8` (a célula transcreve a parada para pedir `/model`, já que o loop mora no contexto principal);
  para a revisão, paridade com `Auditoria`, o papel análogo que julga sem editar. **§4.2:** a `DA-5`
  entra como bullet novo "Fronteira de registro — três artefatos, nenhum repetindo o outro" (diário =
  kanban; RDO = registro canônico da tarefa, um arquivo por tarefa; `telemetria.tsv` = fonte única do
  número), e o bullet `Fechamento enxuto` perde a cláusula que fazia do diário o registro canônico,
  apontando agora para o RDO. Verificação: bateria do §3, os quatro em exit 0 — `kit_check.ps1 -Mode
  validate` (0), `-Mode check-drift` (0), `check-readme.ps1` (0), `python -m pytest` (0);
  `registro canônico` segue com 1 ocorrência e agora nomeia o RDO; `RDO` vai de 0 para 4 ocorrências,
  todas em §4.2; varredura da `redacao-doc` §6 sobre as regiões editadas sem achado (V3/V7/V10 zerados
  no texto novo — sem ID de processo, sem data, terceira pessoa; as negações que ficaram enunciam
  proibição, na coluna *Não faz*). Nenhum item novo em §7 (`DA-10` intacta), nenhuma menção a
  repositório derivado (`DA-3`), nada da `T6b` antecipado. O ramo condicional do dossiê foi resolvido
  pelo orquestrador antes do despacho: `docs/RESIDENCIA_DOUTRINA.md` fica fora (documento de tarefa
  concluída) e `README.md` também (espelho é escopo da `T17`). Tarefa de redação de doutrina, sem
  TF/TR de código; sem achado fora de escopo. Desvio de protocolo declarado: o status `in progress`
  não foi gravado no diário antes da execução — a linha **Próxima tarefa** já designava a tarefa e a
  gravação separada custaria um turno; o diário foi atualizado uma vez, no fechamento. A coluna
  *Modelo* das duas linhas novas, que o dossiê mandava preencher sem fixar valor, foi escalada pelo
  executor e **decidida pelo dono na mesma rodada** (`DA-12`): Orquestração em Sonnet (derivação
  confirmada) e Revisão **em Opus** (a derivação por paridade com Auditoria foi corrigida) — a célula
  da matriz foi ajustada pelo orquestrador, e a `T10` cria o `pantonic-reviewer` já com `model: opus`.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T6b` — doutrina de integridade do contexto — `done`.** Transcrição da `DA-11` nas cinco
  superfícies medidas, sem nenhuma outra tocada. `~/.claude/CLAUDE.md` **Regra 2** reescrita em texto
  íntegro (título passa a "Integridade do contexto"; L17-49): cenário coerente, as duas condições, os
  cinco sinais de poluição, a fronteira cenário × detalhe, a consequência para quem executa e para
  quem orquestra, e o checkpoint como forma de aplicar. `GOVERNANCA.md` §4.3 — o bullet "toda tarefa
  ocorre dentro de um contexto limpo" (régua de contagem) dá lugar à forma condensada `DR-A`: duas
  condições aninhadas, coesão fatal com os sinais e a fronteira cenário × detalhe, capacidade a ~50%
  com o proxy de tool uses por classe afirmado inline enquanto não houver proxy de ocupação, mais o
  bullet da consequência prática (executor inalterado; orquestrador encerra na troca de plano ou
  iniciativa, ou na capacidade); o bullet do checkpoint (2/3 do teto) ganha uma frase para o gatilho
  de poluição. `GOVERNANCA.md` §7 item 7 **reescrito**, nenhum item novo (`G-DEADCODE` intacto no
  item 8). `README.md` em duas linhas: verbete **Contexto** do glossário e linha 7 da tabela de
  guardrails do §10, que segue em **Instrução de agente**. `docs/RESIDENCIA_DOUTRINA.md` seção
  "Regra 2": título, faixa de linhas (17-49), item 2.1 e a nota de colisão, que apontava "§7 item 8"
  e agora aponta o item 7. Verificação: `.claude/checks/check-readme.ps1` em **exit 0** (7 agentes,
  10 skills, 14 guardrails, 14 seções com fonte da verdade válida); `Grep` por "tarefa por contexto"
  em `GOVERNANCA.md` e `README.md` deixa 6 ocorrências, todas legítimas — `GOVERNANCA.md` L221 e
  L519 e `README.md` L574 afirmam a forma operacional de quem executa, preservada pela `DA-11`; L313
  é o texto novo; `README.md` L27 e L613 são o título do §9, fora de escopo por dossiê. Varredura
  `redacao-doc` §6 sobre o texto novo publicado sem achado (sem ID de processo, sem data, terceira
  pessoa; as negações remanescentes enunciam limite). Tarefa de redação de doutrina, sem TF/TR de
  código. Achado fora de escopo indexado no `TK-25`. Teto da classe (30) respeitado.
  Consumo: ver `docs/telemetria.tsv`.

**Replanejamento de 2026-08-08 — a `DA-9` foi revogada pelo dono e a `T6` foi partida.** A releitura
"uma tarefa por contexto **de executor**" abria exceção por papel; o veredito do dono é que não há
exceção a abrir — conduzir um plano **é** uma tarefa, e o errado era a régua (contar tarefas), não o
alcance da regra. Entra a **`DA-11`**: a Regra 2 passa a governar **integridade de contexto**, sob
duas condições independentes — **coesão** (violação fatal e imediata: para-se ao primeiro sinal de
poluição) e **capacidade** (~50% da janela, encerramento planejado) —, com a fronteira cenário ×
detalhe limitando o gatilho fatal, "uma tarefa por contexto" preservada como forma operacional de
quem executa, e o limite do orquestrador **derivado** (a janela dele é o plano, não a tarefa).
Ratificada com o texto normativo à vista, de modo que a tarefa chega ao executor como transcrição.
A `T6` virou **`T6a`** (papéis e fronteira de registro) e **`T6b`** (integridade do contexto, cinco
superfícies) por volume medido — juntas estouravam o teto da classe. Total do plano: 17 → **18**.

- **`EXA-T7` — `telemetria.py`: a série deixa de ser editada à mão — `done`.** Cria
  `.claude/tools/telemetria.py` (subcomando `append`, um argumento nomeado por coluna do TSV —
  `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte` — mapeamento
  sempre por nome, nunca por posição) e `tests/test_telemetria.py`. Validação por coluna: `data`
  em `AAAA-MM-DD` (`datetime.date.fromisoformat`); `projeto`/`tarefa`/`modelo` não vazios e sem
  tab/newline (guarda contra corromper o TSV); `tool_uses` inteiro não negativo; `tokens_k`/
  `duracao_s` numéricos não negativos; `fonte` restrita a `usage`/`contado`/`nao_medido`. Coluna
  inválida ⇒ `TelemetriaValidationError`, `exit 1`, mensagem em stderr nomeando a coluna, nada
  escrito. Escrita atômica: conteúdo anterior lido em bytes + linha nova, gravados num arquivo
  temporário no mesmo diretório (`tempfile.mkstemp`), substituído via `os.replace` — nenhum leitor
  concorrente vê arquivo parcial, conteúdo anterior nunca tocado por conteúdo. `.claude/tools/` não
  existe antes desta tarefa (fato 2 do dossiê) e `kit_check.ps1 -Mode validate` só inventaria
  `agents/`/`skills/` (fato 1) — **`kit_check.ps1` não foi tocado**, confirmado em exit 0 depois.
  TF cobre linha válida + preservação byte a byte do conteúdo anterior na mesma asserção (`tmp_path`,
  nunca o `docs/telemetria.tsv` real); dois TR travam `fonte` inválida e campo numérico não numérico,
  ambos com exit != 0 e conteúdo anterior intacto — as 4 verificações do dossiê, sem excesso. Módulo
  carregado por caminho via `importlib.util.spec_from_file_location`/`exec_module` (`.claude/tools/`
  tem ponto no nome, não é pacote importável — mesmo padrão de `tests/test_dead_code.py`). Header
  real do TSV e as 105 linhas existentes conferidos antes de codar (fato 3) e não tocados. Achado
  fora de escopo indexado no `TK-26`: a série histórica usa célula vazia e `-` como sentinela de
  "não medido" sem convenção única, e o `append` novo não aceita nenhuma das duas — decisão
  deliberada de escopo mínimo, dossiê não pede sentinela. Sem ramo condicional a resolver, sem
  obstáculo à rota do dossiê. Teto da classe (40) respeitado.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T8a` — `rdo.py new`: o documento e o template — `done`.** Cria `.claude/tools/rdo.py`
  (subcomando `new`), `.claude/tools/rdo_template.md` e `tests/test_rdo.py`; cria o diretório
  `docs/RDO/` (`.gitkeep`, vazio até a primeira chamada). `new --plano <md> --tarefa <ID>
  [--rdo-dir <dir>]` localiza o cabeçalho da tarefa pela gramática da `DP-C`
  (`### <ID> — <título> [<modelo> · classe <classe> · teto <N>]`), extrai o dossiê (`Objetivo`,
  `Arquivos-alvo`/`Entregável` — alternância exigida —, `Verificação`, `Pronto quando`, `Dossiê
  fechado por`, demais rótulos em `extras` verbatim) e materializa o `.md` a partir do template,
  que carrega os oito campos fixos do pacote de retorno da `DP-A` com seus tetos (`tarefa`,
  `status`, `arquivos_tocados`, `desvios_do_dossie`, `verificacao`, `achados`, `orcamento`,
  `pendencia_para_o_dono`) — nenhum deles no prompt de agente algum. Achado durante a extração:
  os cabeçalhos deste próprio plano (`P-0734`) escrevem a `classe` por extenso, na grafia da
  linha de `GOVERNANCA.md` §3 (`implementação padrão`, `redação/planejamento`, `redação de
  doutrina`, `investigação`), não no slug da `DP-C` — o parser normaliza (remove acento,
  minusculiza) contra uma tabela de alias para os cinco slugs antes de validar o teto; sem isso
  nenhuma tarefa deste plano seria lida sob esquema `padrao`. Plano legado (cabeçalho sem
  `classe`/`teto`): `--esquema-legado` com `--modelo`/`--classe`/`--teto` explícitos, registrando
  `esquema=legado` no RDO, conforme a política da `DP-C`. Escrita atômica (`tempfile.mkstemp` no
  diretório de destino + `os.replace`) e falha ruidosa (`exit 1`, stderr nomeando o campo/
  identificador, nada escrito) no mesmo padrão de `.claude/tools/telemetria.py`; módulo carregado
  por caminho no teste (`.claude/tools/` não é pacote importável) — `DossieTarefa` é classe simples,
  não `@dataclass`, porque a resolução de anotações adiadas do `dataclasses` quebra sob
  `spec_from_file_location` sem registro em `sys.modules`. TF roda `new` sobre a `T7` (tarefa real,
  `done`, deste plano) e confere identidade, classe resolvida, dossiê extraído e os oito campos
  fixos no `.md`; TR roda `new` sobre identificador inexistente (`T999`) — `exit != 0`, nada
  escrito em `--rdo-dir`, identificador nomeado em stderr. `laudo`/`close` não implementados
  (fatias `T8b`/`T8c`); índice de `docs/RDO/` não gerado (`T8c`); `kit_check.ps1` não tocado.
  Sem achado fora de escopo. **Estouro de teto: 48 tool uses contra os 40 da classe** (medido na
  notificação; o auto-relato do executor dizia "teto respeitado" — a série é do orquestrador). A
  fatia já era o produto de uma partição por orçamento, e ainda assim estourou: o `new` carregou o
  parser do esquema da `DP-C` inteiro (normalização de classe, alternância de campo, ramo de plano
  legado), que é uma capacidade própria e não um acessório do subcomando.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T8b` — `rdo.py laudo`: o veredito é calculado — `done`.** Acrescenta o subcomando `laudo`
  a `.claude/tools/rdo.py`, atualiza o texto da seção `## Laudo` do template e leva
  `tests/test_rdo.py` a 7 testes. `laudo --rdo <caminho>` recebe um flag por dimensão
  (`--criterio-de-pronto`, `--escopo`, `--testes`, `--guardas`, `--rota`, `--residuo`,
  `--registro`, cada um com `choices` nos quatro níveis), `--vermelho-mecanico <dimensão>`
  repetível e `--observacoes`/`--recomendacoes` livres; `calcular_laudo()` **copia** de
  `docs/RUBRICA_DE_REVISAO.md` §5 os pesos (3,2,3,3,2,2,2), as quatro dimensões que não admitem
  `não se aplica`, as cinco bloqueantes, a fórmula e a dominância — nada reinterpretado. Os três
  invariantes do dossiê ficaram executáveis: `--percentual`/`--veredito` **não existem** como
  flags (`DA-6` — a recusa é o erro de argumento desconhecido do argparse), `conforme` em
  dimensão declarada vermelha pela camada mecânica é recusado nomeando a dimensão (`DA-7`) e
  `não se aplica` numa das quatro que não o admitem é recusado; nos dois casos nada é escrito.
  Decisão de implementação: o arredondamento de metade para cima é feito sobre `Fraction` exata,
  nunca `round()` — o arredondamento bancário do Python levaria 0,5 para o par e desalinharia a
  fronteira de 95/70 da rubrica. A seção `## Laudo` é localizada por regex de heading (não por
  offset) e reescrita sozinha, com o mesmo padrão atômico de `cmd_new`. TF reproduz o exemplo de
  85%/`ressalva` da rubrica; os TR cobrem a dominância (`escopo` não conforme e as demais
  conforme dão 88% — `ressalva` pela faixa, `reprovado`/`bloqueante=escopo` pela dominância), a
  recusa de percentual/veredito por argumento e as duas recusas acima, ambas conferindo que o
  arquivo ficou intacto. Verificação: `13 passed` na suíte total (piso 8 + 5 novos, reconferido
  pelo orquestrador após a notificação), `dead_code.py`, `ratchet_piso.py`, `kit_check.ps1`
  (`validate` e `check-drift`) e `check-readme.ps1` todos em exit 0; `tests/conformance/` não
  existe neste repo (hub de kit, sem camadas de aplicação) — não aplicável. `close` e o índice de
  `docs/RDO/` não implementados (`T8c`); `kit_check.ps1` não tocado. Sem achado fora de escopo e
  sem pendência para o dono. **Orçamento: 26 tool uses contra o teto 40** — dentro, contra os 48
  da `T8a`: a fatia que sobrou depois de o `new` ter absorvido o parser do esquema da `DP-C`
  coube com folga, o que confirma a partição por orçamento como controle, não como formalidade.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T8c` — `rdo.py close` e o índice gerado — `done`.** Acrescenta o subcomando `close` a
  `.claude/tools/rdo.py` e leva `tests/test_rdo.py` a 12 testes (suíte total `18 passed`, piso
  13 → 18). `close --rdo <caminho> --tarefa --status --arquivos-tocados --desvios-do-dossie
  --verificacao --achados --orcamento --pendencia-para-o-dono` grava os oito campos fixos do
  pacote de retorno (`DP-A`) na seção `## Execução` já aberta por `new` — **validando teto de
  linhas por campo** (tabela de `DP-A`: 1/1/15/8/6/8/1/4), campo ausente é `unrecognized
  arguments`/`required` do próprio argparse. Lê veredito/dimensão bloqueante já gravados por
  `laudo` na seção `## Laudo` (recusa nomeando `laudo` se ainda placeholder — `close` não
  delegável antes da `T8b`, e o CLI também impõe isso). `calcular_desdobramento()` **copia** a
  precedência do bloco A da `DP-B` (`docs/plans/P-0734-execucao-autonoma.md` `### DP-B`):
  `bloqueado` (`A3`) antes de `estouro` (`A4`, comparando `<gastos>` do próprio campo `orcamento`
  contra `<teto>`, independentemente do resto), `status=parcial` tratado como reprovação (`A5`),
  `reprovado`/`aprovado com ressalva`/`aprovado` (`A6`..`A9` — a distinção `A6`/`A7` de
  retentativa é contador do loop, fora da autoridade mecânica deste CLI, registrado como achado
  abaixo). Os cinco valores de saída são substrings literais das células "ação" da tabela — nada
  inventado. Grava `## Fechamento` (`**Desdobramento:** <valor>`) como marcador de idempotência:
  `close` sobre RDO já com essa seção falha ruidosamente nomeando o caminho, sem escrever nada.
  `_regenerar_indice()` varre `docs/RDO/*.md` (nunca `INDEX.md` a si mesmo, nunca `.gitkeep` —
  exclusão por construção do glob, não por exceção) e reescreve `docs/RDO/INDEX.md` por inteiro,
  atômico (`tempfile.mkstemp` + `os.replace`, mesmo padrão de `cmd_new`/`cmd_laudo`); `docs/RDO/`
  real permanece só com `.gitkeep` (179 bytes, intacto) — todos os RDOs de teste usam `tmp_path`.
  TF fecha um RDO-fixture pronto (laudo `aprovado`/`nenhuma`, sem estouro) com um segundo RDO
  ainda aberto e um `.gitkeep` no mesmo diretório, e confere que `INDEX.md` lista os dois `.md` e
  ignora o `.gitkeep`. TR cobrem: RDO inexistente (caminho nomeado em stderr, `INDEX.md` não
  criado), fechar RDO já fechado (conteúdo idêntico ao pós-primeiro-fechamento), campo além do
  teto (`desvios_do_dossie` com 9 linhas contra teto 8, nada escrito) e `close` sem laudo
  calculado (placeholder de `new` intacto, `laudo` nomeado em stderr, nada escrito). Verificação:
  suíte total `18 passed`; `dead_code.py`, `ratchet_piso.py` (sem piso declarado neste
  consumidor), `kit_check.ps1` (`-Mode validate` e `-Mode check-drift`) e `check-readme.ps1`
  todos exit 0; `tests/conformance/` não existe neste repo (hub de kit, sem camadas de aplicação)
  — não aplicável, mesma constatação da `T8b`. Achado fora de escopo, com rota: a distinção
  `A6`/`A7` (retentativa) e o roteamento `A1`/`A2`/`B1`..`B4` da `DP-B` seguem inteiramente fora
  deste CLI — são estado/decisão do loop, não do RDO; nenhuma ação aqui, já é o desenho esperado
  pela própria `DP-B` ("nenhuma célula pede juízo" é sobre o scrum-master, não sobre `rdo.py`) —
  cobertos quando a `T11` (skill `scrum-master`) for implementada, sem tíquete novo. Sem
  pendência para o dono. **Orçamento: 38 tool uses contra o teto 40** — dentro, mas com margem
  estreita; o auto-relato do executor dizia 31, e o número medido é o da notificação.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T9a` — `review_evidence.py`: diff, escopo e a forma do dossiê — `done`.** Partida da
  `T9` no despacho por orçamento (a `T9` original tinha cinco guardas a invocar mais fixture de
  repositório — mesmo motivo que partiu a `T8`). Cria `.claude/tools/review_evidence.py` e
  `tests/test_review_evidence.py`; nenhum outro arquivo tocado (`rdo.py` e `.claude/README.md`
  intactos, como o dossiê exigia). Reusa `extrair_dossie` de `rdo.py:186` carregado por caminho
  (mesmo padrão de `test_rdo.py`) para obter os arquivos-alvo declarados da tarefa; coleta
  `git diff --stat HEAD` (com fallback sem `HEAD` se o repositório ainda não tem commit) e a
  lista de arquivos tocados via `git status --porcelain=v1 --untracked-files=all`; confronta
  tocados × alvos para o veredito mecânico da dimensão `escopo`
  (`docs/RUBRICA_DE_REVISAO.md:63-77`) — `conforme` quando o tocado é subconjunto do alvo; caso
  contrário só o **fato** ("N arquivo(s) fora dos alvos: ..."), veredito deixado em aberto, nunca
  resolvido para `parcial` sozinho (esse insumo mora no pacote de retorno, que este script não
  recebe). Recorta o trecho de diff de cada arquivo-alvo com teto de caracteres configurável
  (default 4000; truncamento sempre marcado na saída). Seção `## Guardas` nasce nomeada e vazia,
  marcada "não coletado", para a `T9b` preencher sem reescrever o renderizador. Dois defeitos
  reais apareceram só ao escrever o TF com repositório `git` de fixture (sem precedente na
  suíte) e foram corrigidos antes do verde: (1) `git status --porcelain=v1` sem
  `--untracked-files=all` colapsa um diretório inteiramente novo em `dir/` em vez de listar os
  arquivos dentro dele — escondia exatamente o caso "arquivo fora do escopo dentro de pasta
  nova"; (2) carregar `rdo.py` por `importlib` grava `__pycache__/` ao lado do arquivo, que
  aparecia como "tocado" nos testes porque o repositório de fixture não tinha `.gitignore` — o
  hub real já ignora `__pycache__/` (`TK-13`), então o fixture passou a espelhar isso em vez de o
  script ganhar lógica de filtro. TF cobre escopo respeitado (arquivo novo untracked + arquivo
  modificado, ambos dentro dos alvos, vereditos `conforme`); TR cobrem escopo violado (arquivo
  fora dos alvos gera o fato sem "parcial"), truncamento pelo teto (corte marcado, nunca
  silencioso), extração de arquivos-alvo (crases sem `/` ignoradas, sufixo `:N`/`:N-M` de
  referência de linha removido) e o CLI (`review_evidence: OK`/`FALHOU` com exit 0/1). Limitação
  documentada no próprio módulo (não é achado fora de escopo, é comportamento aceito pelo
  dossiê): a extração de arquivos-alvo é textual pura (todo caminho entre crases no campo
  `Arquivos-alvo` é tratado como alvo) e não interpreta prosa negativa como "não editar `x.py`" —
  quem interpreta é o reviewer (`DA-7`). Verificação: suíte total `23 passed` (piso 18 → 23);
  `dead_code.py`, `ratchet_piso.py` (sem piso declarado, `TK-21`), `kit_check.ps1` (`-Mode
  validate` e `-Mode check-drift`) e `check-readme.ps1` todos exit 0; `tests/conformance/` e
  `tests/boundary/` não existem neste repo — não aplicável, mesma constatação da `T8b`/`T8c`.
  Sem achado fora de escopo novo e sem pendência para o dono. **Orçamento: 37 tool uses contra o
  teto 40** — dentro, e a partição da `T9` se justificou: a tarefa inteira teria estourado.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T9b` — `review_evidence.py`: a bateria de guardas — `done`.** Preenche a seção
  `## Guardas` que a `T9a` deixou nomeada e vazia (`.claude/tools/review_evidence.py`,
  `tests/test_review_evidence.py` — edita, não cria, nenhum outro arquivo tocado). Bateria de
  seis comandos lidos de `GOVERNANCA.md` §3 (via o precedente já fechado pela `T9a`, que a rodou
  e registrou no fechamento): `python -m pytest -q`, `python .claude/checks/dead_code.py`,
  `python .claude/checks/ratchet_piso.py`, `pwsh .claude/checks/kit_check.ps1 -Mode validate`,
  `pwsh .claude/checks/kit_check.ps1 -Mode check-drift`, `pwsh .claude/checks/check-readme.ps1`
  — `BATERIA_GUARDAS`, cada comando com `cwd=root`, exit code e stdout+stderr colados
  (`rodar_bateria_guardas`, injetável via `comandos_guardas` para não depender de
  `.claude/checks/*`/`pytest.ini` ausentes no repositório de fixture da suíte). Veredito mecânico
  travado (`DA-7`) das duas dimensões: `guardas` (`docs/RUBRICA_DE_REVISAO.md:94-106`, autoridade
  integral, sem faixa de juízo — qualquer comando fora de exit 0 resolve `não conforme`, nunca
  `parcial` sozinha) via `veredito_guardas`; `testes` (`:79-92`, evidência mecânica é o exit code
  do comando `pytest` da bateria) via `veredito_testes`. Seção renderizada
  (`_renderizar_guardas`) lista nome/comando/exit code de cada item, cola a saída truncada
  (teto configurável, corte sempre marcado) só quando o comando falha, e fecha com os dois
  vereditos — placeholder "não coletado" da `T9a` removido. TF cobre a bateria toda verde
  (unidade, sem subprocess) e o caminho end-to-end via `montar_documento` com bateria injetada;
  TR cobrem comando não-`pytest` vermelho travando só `guardas`, comando `pytest` vermelho
  travando as duas dimensões, e bateria sem comando `pytest` travando `testes` em `não conforme`
  por ausência de evidência (nunca silêncio) — quatro regressões novas contra a exigida mínima de
  uma. Os quatro testes pré-existentes da `T9a` foram ajustados para injetar
  `comandos_guardas`/sobrescrever `BATERIA_GUARDAS` (bateria real depende de infraestrutura
  ausente no repositório de fixture; sem isso os testes ficariam lentos e não-determinísticos) e
  para não mais afirmar o placeholder "não coletado", que deixou de existir por desenho desta
  tarefa. Verificação: suíte total `28 passed` (piso 23 → 28, +5 líquido: 10 testes em
  `test_review_evidence.py` contra 5 antes); os seis comandos da bateria rodados de fato contra o
  hub real, todos exit 0 (`pytest -q` 28 passed; `dead_code.py` 0 achados; `ratchet_piso.py` sem
  piso declarado, `TK-21`; `kit_check.ps1 -Mode validate` e `-Mode check-drift` OK; `check-readme.ps1`
  OK); `tests/conformance/` e `tests/boundary/` não existem neste repositório — não aplicável,
  mesma constatação da `T8b`/`T8c`/`T9a`. Sem achado fora de escopo novo e sem pendência para o
  dono. **Orçamento: ~35 tool uses contra o teto 40** (contagem do executor, não a medida —
  telemetria real fica com a notificação do orquestrador).
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T10` — agente `pantonic-reviewer` — `done`.** Cria `.claude/agents/pantonic-reviewer.md`
  (frontmatter `model: opus`, conforme a `DA-12`; `tools: Read, Glob, Grep, Bash` — a independência
  imposta pela lista, sem `Write`/`Edit`/`NotebookEdit`), regenera `.claude/README.md` por
  `kit_check.ps1 -Mode generate` (nenhuma edição manual da região entre marcadores) e acrescenta a
  linha do agente à tabela **Agentes** da seção "Anatomia do kit" do `README.md` da raiz. O terceiro
  alvo foi resolvido pelo orquestrador antes do despacho: a checagem 1 do `check-readme.ps1` exige
  paridade entre `.claude/agents/*.md` e aquela tabela, então a linha é consequência mecânica da
  criação do agente — não a revisão substantiva do espelho, que segue sendo a `T17` e não foi
  antecipada. Corpo do agente: papel apontando para a linha `Revisão` da matriz de `GOVERNANCA.md`
  §3 e para `docs/RUBRICA_DE_REVISAO.md` sem recopiar nenhum dos dois; fatos estáveis (ordem
  canônica das sete dimensões, as quatro grafias de nível aceitas pelo gerador, as que não admitem
  `não se aplica`, autoridade da camada mecânica, achado de processo com três alvos); protocolo em
  sete passos (dossiê → pacote de retorno → dossiê de evidência → marcação dimensão a dimensão →
  achados de processo → `rdo.py laudo` → retorno ao chamador); proibições fechando em "não julga
  mais de uma tarefa por contexto". Verificação: os seis comandos da bateria do §3 em exit 0 —
  `pytest -q` (`28 passed`, piso mantido; tarefa de doutrina, sem TF/TR de código), `dead_code.py`
  (0 achados), `ratchet_piso.py` (sem piso declarado, `TK-21`), `kit_check.ps1 -Mode validate` e
  `-Mode check-drift` (8 agentes, 10 skills), `check-readme.ps1` (8 agentes, 10 skills, 14
  guardrails, 14 seções). Varredura `redacao-doc` §6 sobre o arquivo novo sem achado, com 1 correção
  V9 aplicada; V10 mantido só na abertura ("Você é o revisor"), forma canônica dos outros sete
  arquivos de agente. **Desvio do dossiê, declarado:** a prosa que introduz a tabela
  (`README.md:726`) dizia "sete agentes" e passou a "oito" — mesma consequência mecânica da linha,
  no mesmo parágrafo, e o guarda não mede contagem em prosa. Achado fora de escopo indexado no
  `TK-27`. **Orçamento: 19 tool uses contra o teto 30** — dentro (o auto-relato dizia 11; o número
  medido é o da notificação).
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T11` — skill `scrum-master`: o loop — `done`, com o RDO impedido de fechar.** Cria
  `.claude/skills/scrum-master/SKILL.md` (255 linhas), regenera `.claude/README.md` por
  `kit_check.ps1 -Mode generate` (8 agentes, 11 skills) e acrescenta a linha da skill à tabela
  **Skills** de "Anatomia do kit" no `README.md` da raiz — terceiro alvo fora dos declarados, exigido
  pela checagem de paridade do `check-readme.ps1`, mesma consequência mecânica que a `T10` teve ao
  criar o agente. Os dez passos do fluxo saem com **gatilho, entrada, ação e saída** declarados um a
  um; `G-PLANREADY` e o gate de delegação apenas **apontados**, nunca recopiados (a deduplicação é a
  `T12`); `A1`..`A9` e `B1`..`B4` em forma operacional com `DP-A`/`DP-B` declaradas normativas;
  encerramento de janela só por teto numérico (10 tarefas / 900 k) e nunca por percepção; proibições
  explícitas — não implementa, não julga entrega, não decide arquitetura, **não abre o RDO**, não
  reescreve dossiê e não paraleliza. Verificação: os seis comandos da bateria do §3 em exit 0
  (`pytest -q` 28 passed, `dead_code.py`, `ratchet_piso.py`, `kit_check.ps1 -Mode validate` e
  `-Mode check-drift`, `check-readme.ps1` — este último vermelho na primeira passada, pela linha
  ausente na tabela de Skills, corrigido e reconferido). **Percurso a seco sobre a `DHB-T1`**
  (`P-0733`), 10/10 passos, nada executado: o passo 3 recusou a tarefa pelo **gate de delegação item
  5** (cabeçalho legado sem `classe`/`teto` ⇒ `B3`), exercitando o roteamento no primeiro alvo real.
  **Fechamento do RDO bloqueado por defeito medido em `rdo.py close`** — ver o bloco abaixo; o
  executor levantou e **não decidiu** (Regra 8), e os oito campos do pacote ficaram por gravar.
  Achados fora de escopo, com rota: `proximo-passo/SKILL.md` cita `G-PLANREADY` como item 12 quando é
  o **item 11** (rota `T12`); planos legados param em `B3` por falta de `classe`/`teto` (rota `T16`,
  e é o `TK-24`); a convenção `docs/RDO/evidencia/<plano>-<ID>.md` foi prescrita pela skill sem
  ratificação prévia (rota `T16`); o RDO não tem campo para percurso a seco (sem ação).
  **Orçamento: 32 tool uses contra o teto 30 — estourado**, por auto-relato: a execução caiu por
  limite semanal de API no meio e foi retomada por `SendMessage` ao mesmo agente, de modo que
  **PARCIAL — trecho pré-queda não medido**; só a retomada tem bloco `<usage>`.
  Consumo: ver `docs/telemetria.tsv` (linha `EXA-T11-retomada` — perna medida apenas).

**Defeito de contrato entre `DP-A` e a `T8c` — aberto, decisão do dono.** `rdo.py close`
(`.claude/tools/rdo.py:654`) faz três coisas num ato só: valida e grava os oito campos do pacote de
retorno na `## Execução` (`:697-708`, **único escritor** desses campos), **exige** a `## Laudo` já
calculada (`:678-683`) e grava o `## Fechamento`. Mas a `DP-A` põe o pacote como **entrada** da
revisão, e o laudo é **saída** dela: o pacote precisa do `close`, que precisa do laudo, que precisa
do pacote. Nenhuma tarefa fecha o ciclo — o `EXA-T11` é a primeira a percorrê-lo inteiro, porque o
loop não existia antes dela. Circularidade confirmada no código, não inferida do relato.

**A decisão foi levada ao dono em 2026-08-10 e a resposta redefine o fluxo — `P-0734` entra em
replanejamento.** Nenhuma das três opções (partir `close`, flag `--sem-laudo`, revisar a `DP-A`) foi
escolhida: o dono descreveu o processo de outra forma. Dois pontos foram **fechados na mesma rodada**
e saem da lista de divergências:

- **O scrum-master é skill** — terminologia do dono corrigida por ele próprio, depois de conferido
  que a skill entregue atende as oito responsabilidades descritas: selecionar a tarefa (passo 2),
  invocar o executor no modelo correto (passo 4), popular o contexto dele com o suficiente e
  necessário (passo 4), aguardar o retorno (passo 5), invocar o inspetor (passo 6), ler o laudo
  (passo 7), fechar a tarefa em RDO quando não há desdobramento (passo 9) e executar o desdobramento
  quando há — nova execução, correção ou escalada ao dono (blocos `A`/`B`). Nenhuma delas exige forma
  de agente; a `DA-1` permanece válida.
- **Residência e identidade do RDO** — "anexar na memória do projeto" significa a pasta própria e
  destacada, que já é `docs/RDO/`: um `.md` por tarefa, identificado pelo identificador dela, e um
  plano concluído tem tantos RDOs quantas tarefas executadas. O que existe já conforma (o nome
  carrega `<plano>-<tarefa>` com slug de título como sufixo). **Consequência medida da regra:**
  `docs/RDO/` tem **1** RDO para **15** tarefas fechadas do `P-0734` — `T1`..`T10` fecharam antes de o
  instrumento existir e têm o diário como registro canônico. O replanejamento decide se retroage ou
  se a regra vale daqui para a frente.

**Divergências de contrato que permanecem, todas com a `DP-A`/`DP-B`:** o executor devolve **"Done"**
e não a linha de 5 campos — e `status`, `tools` e `pendencia` são justamente o que as regras `A3`,
`A4` e `B1` consomem; o **pacote de retorno de 8 campos deixa de existir**; o **RDO é criado no fim**,
pelo scrum-master, e não aberto no início por `rdo.py new`; o inspetor recebe **o mesmo contexto do
executor**, não o pacote em arquivo; o **laudo carrega a recomendação**, em vez de o desdobramento
sair da tabela; e a retentativa é **agente novo em contexto novo**, não o re-despacho do mesmo
executor da regra `A6` — nesta última a descrição do dono é a mais coerente com a Regra 2, já que o
contexto de uma execução reprovada está poluído. A circularidade `close`↔`laudo` **desaparece** sob a
descrição do dono, porque o pacote de retorno deixa de existir — o defeito registrado acima é real,
mas o conserto certo depende de qual descrição é normativa.

**Replanejamento executado em 2026-08-10 (Opus, contexto novo).** O decision record está autorado
como **proposta** em `docs/plans/P-0734-execucao-autonoma.md` §9 (`DP-D`): as seis divergências
julgadas uma a uma, a realocação dos oito campos do pacote, a fronteira entre o que o loop sabe e o
que o juiz sabe, e o rebase do que sobrevive dos artefatos já construídos (`telemetria.py` e
`review_evidence.py` intactos; `rdo.py new` perde objeto; `rdo.py close`, `pantonic-reviewer` e
`scrum-master` editados, nenhum refeito). A circularidade `close` ↔ laudo desaparece com o pacote.

**`DP-D` ratificada pelo dono em 2026-08-10**, com o texto à vista, incluindo o desvio declarado no
`D1` (o executor devolve `Done` ou `Done pendencia=<uma linha>`, para que a regra `B1` não dependa de
o revisor inferir do diff uma pendência que o diff não contém). O ponto aberto foi fechado conforme a
recomendação: **o RDO não retroage** — `T1`..`T10` mantêm o diário como registro canônico.

Os quatro dossiês novos foram autorados **fechados** no mesmo ato (`G-PLANREADY` item 5). São quatro
e não três porque a `DP-C` só admite um modelo e uma classe por cabeçalho, e a fatia "revisor +
laudo" reunia código e doutrina. Duas decisões de desenho foram fechadas junto, para que nenhum
dossiê chegasse aberto ao executor: o **laudo ganha documento próprio**
(`docs/RDO/laudos/<plano>-<tarefa>.md`, com o RDO carregando campos e ponteiro, nunca a prosa) e
**`escalar` é marcado, não derivado** — as outras três recomendações saem do veredito calculado.

- **`EXA-T18` — `rdo.py laudo`: documento próprio e recomendação de domínio fechado — `done`.**
  `cmd_laudo` (`.claude/tools/rdo.py:501`, aprox.) deixa de depender de RDO aberto por `new`: grava
  em `docs/RDO/laudos/<plano>-<tarefa>.md` (`--plano`/`--tarefa`/`--laudos-dir`, default
  `docs/RDO/laudos`), criando o diretório se preciso, escrita atômica no mesmo padrão dos irmãos.
  `calcular_laudo` (`:457`, aprox.) passa a devolver também `recomendacao`/`pendencia`
  (`LaudoResultado`) pela tabela do dossiê — `aprovado`→`seguir`, `ressalva`→`seguir com ressalva`,
  `reprovado`→`refazer` — e `--escalar "<linha>"` força `recomendacao=escalar`
  **independentemente** da tabela, gravando a linha como `Pendência` (a que a regra `B1` consumirá).
  Domínio fechado nos quatro valores: nenhum flag `--recomendacao` existe — único canal é
  `--escalar` (mesma regra `DA-6` de percentual/veredito) — passar `--recomendacao`/`--percentual`/
  `--veredito` é `unrecognized arguments` (`SystemExit`), nada escrito. Removido o marcador morto
  `_LAUDO_MARCADOR_RE` (escrita na seção `## Laudo` de um RDO — rota abandonada por esta tarefa,
  `G-DEADCODE`); `rdo_template.md` `## Laudo` atualizado só na prosa, para apontar ao documento
  próprio e deixar explícito que vira campos+ponteiro na `T19` (não tocada aqui, por escopo).
  `cmd_new`/`cmd_close`/`_LAUDO_VEREDITO_RE`/`_LAUDO_BLOQUEANTE_RE` intocados, como o dossiê mandou
  (ficam temporariamente sem produtor até a `T19` rewire `close`; previsto no próprio dossiê, não é
  achado novo). Testes (`tests/test_rdo.py`): as 5 TF/TR antigas de `laudo` (interface `--rdo`)
  foram **reescritas**, não deletadas, para a interface nova — cobertura preservada (`DA-6`/`DA-7`,
  não-se-aplica, dominância de dimensão bloqueante) — mais teste novo das três derivações da tabela
  (parametrizado em um TF), da dominância de `--escalar` sobre `veredito=aprovado`, da recusa dos
  três argumentos de domínio fechado e do caminho de saída com diretório aninhado ainda
  inexistente. `test_rdo.py`: 13 testes (era 12). Achados fora de escopo: nenhum.
  Veredito — EXA-T18
  Suítes: Tier 1 (tests/test_rdo.py) — 13 passed; piso completo (`pytest -q`) — 29 passed (era 28;
    repositório ainda sem `tests/conformance/`/`tests/boundary/` — nada bloqueante a rodar ali)
  Piso: ratchet_piso.py — OK (sem piso declarado em tests/piso_comportamental.txt)
  Kit: kit_check.ps1 -Mode validate / -Mode check-drift — exit 0 (8 agentes, 11 skills, VERSION==KIT_VERSION '0.0.0')
  Espelho: check-readme.ps1 — exit 0 (8 agentes, 11 skills, 14 guardrails, 14 seções com Fonte da verdade)
  Checklist de review: ok — script CLI fora da árvore infracore/contracts/services/plugins (sem
    direção de camada a checar); sem dependência externa nova; sem trabalho pesado em thread de
    entrada; sem tipo cruzando camada; teste com significado alterado foi reescrito, não deletado;
    mudança comportamental amparada por decision record `DP-D` (§9), ratificada.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T19` — `rdo.py`: o RDO se gera no fechamento — `blocked`.** G-EXECREADY: o dossiê do
  `### T19` não é performável sem uma decisão de arquitetura que não é do executor. O texto manda
  `cmd_close` materializar o RDO "a partir do plano, do laudo, do consumo medido e do desdobramento
  calculado" e confirma, via `9.1`/`D2` da própria `DP-D`, que "a validação dos 8 campos do pacote
  sai" (pacote de retorno deixou de existir) — mas não diz de onde `close` passa a tirar o parâmetro
  `status` (`entregue`/`parcial`/`bloqueado`) que `calcular_desdobramento` (reusada sem mudança de
  assinatura declarada, `:589`) continua exigindo. A tabela `D5` (§9) reparte o bloco A entre "passa
  ao laudo" (`A5`/`A6`/`A8`/`A9`) e "permanece no loop" (`A1`/`A2`/`A4`/`A7`/`B1`-`B3`) e **omite
  `A3` (bloqueado)** das duas listas — ramo condicional não resolvido. Segunda lacuna: `D1` põe
  `pendencia_para_o_dono` em "retorno do executor (campo opcional) ou laudo", e o `### T19` não diz
  se `close` ganha um flag para esse canal opcional. Nenhuma decisão foi tomada nesta sessão
  (G-PLANFIDELITY/Regra 8 global) — o dossiê volta ao planejamento para fechar as duas lacunas antes
  de ser redelegado. Nenhum arquivo tocado (nenhuma edição em `rdo.py`/`rdo_template.md`/
  `tests/test_rdo.py`). Achado indexado no `TK-28`.
  Consumo: ver `docs/telemetria.tsv`.

- **Replanejamento do dossiê da `EXA-T19` — `done`** (rodada de planejamento, não é tarefa do plano).
  As duas lacunas do `TK-28` foram fechadas por derivação da `DP-D` já ratificada, sem decisão nova do
  dono; detalhe da rota no `TK-28`. Escopo do `### T19` **cresceu**: além do rewire do `close`, ele
  passa a criar `laudo --status` (item mínimo, com o limite do que pode ser tocado da `T18` declarado
  no campo *Cuidado*) e a fixar a CLI final do `close` — `--plano/--tarefa/--tool-uses/--tokens-k/
  --duracao-s` mais os quatro flags de esquema legado movidos verbatim do `new`, sem os quais a `T17`
  não fecharia —, a origem do teto para `A4` (`tool_uses > dossie.teto`, sempre do cabeçalho), a
  detecção de "já fechada" e a forma seção-a-seção do template novo; os testes vão de 4 para 9.
  Achados fora de escopo: `calcular_desdobramento` recebe `bloqueante` e **nunca o usa**
  (`.claude/tools/rdo.py:624-644`, parâmetro morto, mantido porque a assinatura não muda — merece
  tíquete próprio); ramo morto `"prescrito no dossiê"` em `cmd_new:368`, que morre junto com o
  `cmd_new` na própria `T19`; `docs/RDO/laudos/` ainda não existe (a `T18` entregou o escritor, nenhum
  laudo foi produzido); o dossiê da `T20` já dizia que o revisor declara o `status` e fica consistente
  sem edição. Consumo: ver `docs/telemetria.tsv`.

- **Replanejamento `DP-E` — o `status` é da tarefa, não do laudo — `done`** (rodada de planejamento,
  não é tarefa do plano). A captura do §10 virou decisão **ratificada pelo dono em 2026-08-11**.
  Acolhidos os enunciados 1, 2, 3 e 5: `status` é característica da tarefa, o `scrum-master` é o
  único que o escreve, o laudo é escrito só pelo revisor (o `scrum-master` lê e descarta o resto), e
  o loop ganha dois gatilhos de estado — um que invoca o revisor, outro em que o RDO é escrito
  (estrutura fixada; a grafia segue a lista final). **Enunciado 4 (os sete estados) não virou norma:**
  foi deslocado para tarefa própria, que primeiro **avalia** se a lista é suficiente, exagerada ou
  insuficiente. **Nome do papel resolvido:** `pantonic-reviewer` é canônico, a prosa diz *revisor* e
  o termo *inspetor* está abolido do vocabulário. **Revogado da `DP-D`:** a linha "`status` → laudo
  do revisor" do `D1`, a célula "`status` → laudo" do `D2` e a *Nota de derivação de 2026-08-11*
  inteira (com ela caem `laudo --status`, a partição do `A3` e a leitura do `status` pelo `close`).
  **Permanecem** `D3`, `D4`, `D6`, o resto de `D1`/`D2`, o `D5` (recomendação de domínio fechado e
  partição por origem da informação), os três tetos da `DP-B`, a não-retroação do RDO e os §9.1/§9.2
  — declarados item a item no §10.3. O canal `close --pendencia` sobrevive como encomenda, sem
  derivação nova. Encomendadas **seis tarefas** (`EXA-T22..T27`): a `T22` fecha a `DP-F` (lista final,
  máquina de transições, tabela de tradução, recorte) e **para** para ratificação do dono;
  `T23`..`T26` conformam famílias disjuntas de artefatos vivos; a `T27` conforma kanban e planos
  vivos e faz a varredura de fecho. `### T19`, `### T20` e `### T21` **não foram reescritos** —
  ficam marcados como *pendentes de reescrita* no §4, com o motivo registrado. Achado medido fora de
  escopo: as ocorrências de `parcial` em `.claude/tools/review_evidence.py` são **veredito de
  rubrica**, não `status` de tarefa — a contagem bruta de ocorrências superestima a conformidade, e
  os três vocabulários (status, veredito, homônimo) estão separados no §10.2.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T22` — avaliação da lista de estados e fechamento da linguagem ubíqua — `done`; `DP-F`
  ratificada pelo dono em 2026-08-11, sem reserva.** `### DP-F` escrita em `docs/plans/P-0734-execucao-autonoma.md`
  (L1401-1560), logo após a `DP-C`; nenhum outro arquivo tocado, nenhum artefato conformado.
  **Veredito global: a lista dos sete é suficiente** — `triage`, `ready`, `blocked`, `in-progress`,
  `review`, `done` e `cancelled` têm consequência operacional observável, nenhum é exagero, nenhuma
  transição observada ficou sem nome e nenhum estado novo entra; `triage` nomeia uma insuficiência
  real (linha de `_INBOX.md` ainda não `[drenado]` não é escolhível e é avaliada, não delegada). As
  duas correções são de **grafia** e de **alcance**: `backlog` deixa de ser status e passa a nomear só
  o conjunto elegível, e `superseded` fica **fora** do vocabulário de tarefa (é exclusivo de
  plano/iniciativa; tarefa obsoleta é `cancelled`). Alcance decidido: a lista governa **todo item do
  kanban**, porque a coluna `Status` do índice é uma só e o `proximo-passo` lê essa mesma coluna, com
  tabela de aplicabilidade por objeto e residência única em `.claude/skills/diario-de-obras/SKILL.md`.
  Máquina de transições fechada com `done`/`cancelled` terminais (retrabalho vira item novo) e só as
  duas transições da `DP-E` disparando ação — `in-progress`→`review` invoca o revisor,
  `review`→`done` escreve o RDO. Tabela de tradução sem termo órfão: `entregue` e `bloqueado` morrem,
  `parcial` morre **como status** e sobrevive como veredito de rubrica. Uma correção de recorte no
  item 7: `docs/RDO/P-0734-T11-skill-scrum-master-o-loop.md` sai dos arquivos-alvo da `T27` (RDO
  emitido é registro histórico) e vira sobrevivente justificado na varredura de fecho.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T23a` — residência única do vocabulário de status no `diario-de-obras` — `done`.** A `T23`
  publicada foi **partida em `T23a`/`T23b` pelo orquestrador**, por orçamento: a contagem de
  write-clusters da tarefa inteira ficou em ~15-16, acima da linha de 8 do item 5 do gate de
  delegação; o corte é por arquivo, sem alterar nada do dossiê original. Arquivo único
  `.claude/skills/diario-de-obras/SKILL.md`: o bullet **Status válidos** virou ponteiro de duas
  linhas para a seção nova **`## Status — residência única`**, que enuncia uma única vez a lista
  final dos sete estados, a máquina de transições com os três fechamentos e a tabela de alcance por
  objeto — mais o enunciado de que o `status` é escrito exclusivamente pelo `scrum-master`. No resto
  do arquivo, só as ocorrências de tipo (i) foram traduzidas (exemplo de índice, heurística da
  diretiva de priorização, operação "Registrar plano", gatilho (c) de condensação, regra de
  convergência); prosa e homônimos ficaram intactos por classificação. Aceite re-derivado:
  `in progress|in review` de **4 → 0**; `backlog` de **8 → 3**, as três sobreviventes como
  substantivo (o conjunto), nenhuma como status. Bateria do §3 rodada pelo orquestrador no fecho —
  os quatro em exit 0, suíte em 29 passed. Achado registrado no `## Achados da execução` do plano e
  aberto como `TK-30`. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T23b` — conformidade do `proximo-passo` com a residência única — `blocked`.** **Razão do
  bloqueio (2026-08-11, decisão do dono):** o entregável existe e foi verificado, mas **não há quem
  conclua a tarefa** — a transição `review` → `done` é escrita só pelo `scrum-master`, e a skill na
  forma reescrita só passa a existir depois de `T19`/`T20`/`T21`. O executor escreve `review` e
  `blocked` e nunca `done` (captura em `docs/plans/P-0734-execucao-autonoma.md` §11, insumo ainda não
  fechado como `DP-G`). Destrava quando o loop existir. Arquivo único
  `.claude/skills/proximo-passo/SKILL.md`, cinco write-clusters. A skill que **consome** o kanban
  ganhou um parágrafo de abertura (`:15-19`) declarando que ela não define estado nenhum e apontando
  para a residência (`diario-de-obras`, `## Status — residência única`) — ponteiro, sem recopiar
  lista, máquina nem tabela de alcance. Traduzidas só as ocorrências de tipo (i) da `DP-F`: heurística
  de priorização (`:36`, `:39`, `:41-42`, `:44`), retomada de sprint (`:52`), guardrail de convergência
  (`:172`) e guardrail de diário vazio (`:182`) — `in progress`→`in-progress`, `backlog` (status)→
  `ready`. Nenhuma regra de escolha mudou de efeito: mesma ordem da heurística, mesmos filtros, mesmas
  proibições. No guardrail de `superseded` (`:167-168`) entrou o item 4 da `DP-F`: `superseded` é
  vocabulário de **plano/iniciativa**, não existe tarefa `superseded`. Tipo (ii)/(iii) intactos por
  classificação — `PARCIAL` de rubrica, `bloqueado` em prosa, `<done>/<total>` de contagem e as cinco
  ocorrências de `backlog` como substantivo (título, description, retomada, "próxima tarefa do
  backlog", "fora do backlog"). Aceite re-derivado no fecho: `in progress|in review` de **6 → 0**
  (grep vazio); `backlog` de **9 → 5**, todas substantivo. Bateria do §3:
  `check-readme.ps1`, `dead_code.py`, `kit_check.ps1`, `ratchet_piso.py` em **exit 0** e
  `python -m pytest tests -q` em **29 passed** (piso mantido, 29 × 29). Nenhum achado fora de escopo.
  Consumo: ver `docs/telemetria.tsv`.

**Fila reordenada em 2026-08-11 (decisão do dono).** A ordem anterior mandava `T24`..`T27` antes da
reescrita de `T19`/`T20`/`T21`; como nenhuma tarefa pode ser concluída antes de o loop existir, as
tarefas de conformidade passam a **suceder** o loop.

- **Replanejamento `DP-G` — a fronteira de escrita do `status` — `done`; ratificada pelo dono em
  2026-08-11, sem reserva** (rodada de planejamento, não é tarefa do plano). A captura do §11 virou
  decisão. **Fronteira fechada em dois atos que o texto vigente tratava como um só:** *autoria*
  (quem determina o valor) é do executor para `review` e `blocked`, e do `scrum-master` para todo o
  resto; *materialização* (gravar onde o kanban registra) é **exclusivamente** do `scrum-master`,
  que transcreve os dois valores do executor sem discricionariedade. A leitura literal — executor
  grava o kanban — foi **recusada por medida**: não existe hoje campo material de `status` por tarefa
  de plano (o índice só tem linha para iniciativa, plano e tíquete; a tarefa vive no bullet de
  fechamento e na ordem do §5), criá-lo é artefato novo e poria dois escritores no mesmo arquivo.
  **`E2` fechada no candidato (a)** — o `blocked` do executor é canal único com **razão tipada**:
  `motivo=dependencia` faz o `scrum-master` reordenar a fila e **seguir**; `motivo=premissa` faz
  **parar** e escalar; na dúvida, `premissa`. O previsível continua carregado pela ordem do §5, e
  nenhum campo novo entra na `DP-C`. Recusados (b) — vocabulário de retorno disjunto do `status` — e
  (c) sozinho, que não cobre dependência **descoberta em execução**, o caso do enunciado 4.
  **Consequência nas tabelas:** `A3` parte em `A3a`/`A3b` pela razão tipada, e `A5` **cai** (`parcial`
  morreu como status; entrega incompleta é veredito do revisor). Gramática de retorno nova:
  `<tarefa> review [pendencia=…]` ou `<tarefa> blocked motivo=<dependencia|premissa> …`.
  **`E1` virou a `T28`** (sanitização das quatro superfícies que afirmam o absoluto: §10.2, `DP-F`
  itens 2 e 3, e a residência única). **Três dossiês reescritos:** a `T19` perde `laudo --status` e
  encolhe `calcular_desdobramento` para `(veredito, orcamento_estourado)` — derivado de a `DP-F`
  fixar o RDO numa transição só, o que torna `bloqueado`/`reprovado` inalcançáveis e fecha o `TK-29`;
  a `T20` perde a declaração de `status` pelo revisor; a `T21` foi **partida em `T21a`/`T21b`** por
  volume (~9 write-clusters). Fila final: `T28` → `T19` → `T20` → `T21a` → `T21b` → `T23b` →
  `T24`..`T27`. Bateria do §3 no fecho: `check-readme.ps1`, `dead_code.py`, `kit_check.ps1`,
  `ratchet_piso.py` em **exit 0** e `python -m pytest tests -q` em **29 passed** (piso mantido).
  Consumo: ver `docs/telemetria.tsv`.

- **Duas questões operacionais fechadas por delegação do dono, na mesma rodada — `done`.**
  (1) **Teto da rodada de replanejamento:** `GOVERNANCA.md` §3 passa a reconhecer o caso — fechar a
  decisão e reescrever no mesmo contexto os dossiês que ela invalida — com teto **≤50**, dentro da
  classe de redação/planejamento, sem classe nova (a `DP-C` mantém os cinco slugs). Calibrado pela
  série medida dessas rodadas (19, 21, 39, 43, 48), três das cinco acima de ≤30; dividi-las entre
  contextos obrigaria a repagar a leitura da decisão em cada fatia. Espelhado no `README.md`,
  inclusive no gatilho de checkpoint por dois terços, e registrado no `CHANGELOG.md`.
  (2) **`TK-26`:** o ponto aberto foi fechado — célula vazia aceita nas três colunas numéricas
  **sempre que `fonte` ≠ `usage`**; a execução em `telemetria.py` segue pendente de tarefa própria.
  Bateria do §3 no fecho: `check-readme.ps1`, `kit_check.ps1`, `dead_code.py` em **exit 0** e
  `pytest tests -q` em **29 passed**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T28` — sanitização do texto vigente contra a `DP-G` — `done`.** As quatro superfícies que
  afirmavam o absoluto passaram a separar **autoria** de **materialização**, cada uma com ponteiro
  para a `DP-G`: `§10.2` enunciado 2 e `DP-F` itens 2 e 3 no plano, e a residência única em
  `.claude/skills/diario-de-obras/SKILL.md`. **Cinco edições, não quatro:** a residência única
  carrega duas frases da mesma superfície — a linha *Escritor* e a abertura da máquina de transições,
  cópia normativa da frase que a edição 3 corrige no plano —, e sem a segunda a residência
  continuaria enunciando para o kit inteiro o absoluto que a `DP-G` derrubou. O aceite literal do
  dossiê (Grep vazio no plano) foi **escopado pelo orquestrador antes da delegação**: o plano cita o
  texto antigo por desenho na tabela da própria `DP-G`, no insumo `§11.2`/`§11.4` e no dossiê da
  `T28`, e os invariantes proíbem tocá-las — o critério passou a ser "nenhuma ocorrência
  **afirmativa** sobrevive". Tabelas de estados, de transições, de alcance por objeto e de tradução
  intocadas; `DP-G` na skill saiu de 0 para 2 ocorrências. Achado tiquetado, não corrigido: `TK-31`.
  Bateria do §3 no fecho: `check-readme.ps1`, `dead_code.py`, `kit_check.ps1`, `ratchet_piso.py` em
  **exit 0** e `python -m pytest tests -q` em **29 passed**. Orçamento **estourado**: 21 tool uses
  contra teto 15 da classe `redacao` — a fatia extra veio da edição 5 e da verificação escopada, que
  não estavam no volume medido quando a classe foi atribuída. Consumo: ver `docs/telemetria.tsv`.

- **Insumo do dono registrado — a fronteira conceito × desenvolvimento (`§12` do plano).** O
  levantamento de contradições aberto pelo fechamento da `T28` foi respondido com uma distinção que
  reclassifica os seis pontos: **conceito do framework** (o que ele é, reside nos artefatos
  publicados) × **desenvolvimento do framework** (como está sendo construído, reside no plano). A
  regra de recência — o último entendimento do autor é canônico e reescreve o que contradiz — é de
  **desenvolvimento** e **não** entra em artefato publicado; o critério de desempate do framework em
  si não foi decidido. O RDO fica fora da conciliação, por ter mecânica própria. Entendimentos
  canônicos confirmados: o **laudo** é emitido pelo reviewer, consumido e **descartado** pelo
  `scrum-master` (fonte de poluição de contexto), vivendo só como argumento do desdobramento; o
  **pacote** é o conjunto de informações obrigatórias **dentro do laudo**, suficientes para invocar o
  script de RDO sem falha; **`reviewer`** é o nome canônico. A definição do artefato **tarefa** —
  documento com vários autores (`scrum-master`, executor, reviewer), principal canal de comunicação
  entre as partes — sai de remendo e vira tarefa própria. Registrado como insumo, sem derivação:
  nenhuma tarefa foi autorada e nenhum dossiê reescrito nesta rodada.

- **Rodada de replanejamento — `DP-H` fechada e o `§12` consumido — `done`.** A fronteira conceito ×
  desenvolvimento virou decision record (`§13` do plano) por **derivação**, sem decisão nova: recência
  é regra de **desenvolvimento** e não entra em artefato publicado; dossiê de tarefa executada é
  **orientação** e se concilia, enquanto o que narra o ocorrido permanece intocado; o laudo é
  consumido e **descartado**; o `pacote` existe **dentro do laudo**, com suficiência declarada; o
  RDO fica fora. Consequência material nos dossiês: a `T19` perde a leitura do laudo — o `close`
  recebe os cinco campos do `pacote` por argumento, `--laudos-dir` sai da CLI e o template perde o
  ponteiro `{{LAUDO_PATH}}` —, a `T20` deixa de tratar `pacote` como objeto morto, a `T21a` ganha a
  extração do `pacote` e o **apagamento** do laudo no passo 9, a `T21b` para de repassar o caminho do
  laudo na reexecução, os achados do `§9` trocam *inspetor* por `reviewer` e param de enunciar "o
  critério não é recência", e a `T26` perde o absoluto de escritor único e passa a depender da
  `DP-I`. **Três cards novos:** `T29` (artefato **tarefa** → `DP-I`), `T30` (**utilidade** → `DP-J`)
  e `T31` (resíduo de `pacote de retorno` em `GOVERNANCA.md`, na rubrica e na residência única, que
  estava sem cobertura). `T29` e `T30` decidem e **param** para ratificação em lote — quinto
  round-trip do dono, e único ponto de parada dura da fila. `TK-31` fechado por conciliação no
  dossiê da `T23a`. Fila: `T19` → `T20` → `T31` → `T21a` → `T21b` → `T23b` → `T24` → `T25` → `T29` →
  `T30` → [ratificação] → `T26` → `T27`. Bateria do §3 **não executada** nesta rodada: o contexto de
  planejamento não dispõe de ferramenta de execução e o diff ficou restrito a `docs/` (plano e
  diário), sem tocar código, teste ou kit executável — a bateria volta no fecho da `T19`.
  Consumo: ver `docs/telemetria.tsv`.

- **Rodada de replanejamento — `DP-K` fechada: os quatro artefatos e o desempate do framework —
  `done`.** Os três pontos que a `DP-H` devolveu voltaram respondidos pelo dono e foram **registrados
  e derivados na mesma passagem** (`§14` do plano). **(1) Desempate do framework:** ambiguidade
  **escala ao dono** — o buraco que o `§12.1` e a `DP-H` declaravam explicitamente não decidido. É
  **conceito**, então ganha residência em artefato publicado: entra como **terceira regra de
  precedência** no `GOVERNANCA.md` **§3.1**, que já é a superfície que decide colisão de doutrina —
  sem seção nova, e sem que a recência (regra de desenvolvimento) vire desempate publicado. Nenhuma
  tarefa viva cobria a gravação: card **`T32`**. **(2) `reviewer` é termo único** e abole também a
  forma portuguesa *revisor*, que a `DP-H` deixara livre. Volume medido no texto vivo: **18
  ocorrências em 5 arquivos** — 11 no corpo do `SKILL.md` do `scrum-master`, que a `T21a` (7) e a
  `T21b` (4) **já reescrevem**, a custo marginal zero; as **6** restantes são linhas espelhadas
  (`description` da skill e do agente, com os espelhos em `README.md` e `.claude/README.md`) mais a
  prosa do agente e uma docstring de teste. A `T31` **não** absorveu: com 9 ocorrências em 3 arquivos
  sob teto 15, o volume medido estoura — card **`T33`**, depois da `T21b`. Registro (diário,
  histórico, RDO, telemetria) intocado; o *Revisor* do OpenSpec no benchmark é papel externo e fica.
  **(3) Hierarquia dos quatro artefatos canônicos:** plano (objetivo materializado, antecede todas as
  tarefas), tarefa (escopo localizado do plano, comunicação **entre os agentes**, verdade da tarefa em
  execução), laudo (revisão realizada, **efêmero**, move para `done` ou devolve para `in-progress`) e
  RDO (comunicação com o **dono**, verdade da entrega, pressupõe tarefa finalizada) — **nenhum
  substitui o outro**. Medido contra o texto vigente: a efemeridade **confirma** a `DP-F` e não abre
  aresta na máquina (o `review` → `blocked` da escalada não é contradito — é a mesma rota que o ponto
  1 acabou de ratificar), "em execução" lê-se *tarefa não terminal* e nenhuma grafia muda, a `DP-G`
  fica intocada (recomendar não é autorar `status`) e a `T19` é **compatível** — `close` sem leitura
  de laudo, template sem `{{LAUDO_PATH}}`. **Uma aresta real:** o laudo morre em **qualquer**
  desdobramento, e não só no fechamento — a `T21b` ganha o descarte nos ramos `A6`/`A7`/`B1` e a `T30`
  ganha o piso dos três ramos. A **`T29` foi reescrita**: sai o ramo de escalada obrigatória por
  residência (o dono já respondeu que a tarefa não substitui nada), entra a hierarquia como insumo
  fechado, e **três das cinco perguntas viram transcrição** — sobram duas a decidir (autores/escrita e
  conteúdo obrigatório, com o lugar material do `status`), que é onde a `DP-I` passa a parar. Fila:
  `T19` → `T20` → `T31` → `T32` → `T21a` → `T21b` → `T33` → `T23b` → `T24` → `T25` → `T29` → `T30` →
  [ratificação] → `T26` → `T27`. Bateria do §3 **não executada**: ato de planejamento, diff restrito a
  `docs/` (plano e diário), sem tocar código, teste ou kit executável — a bateria volta no fecho da
  `T19`. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T31` — conformidade: o resíduo de `pacote de retorno` nos artefatos publicados** (`done`).
  O objeto morto saiu do texto vigente dos três artefatos publicados. `GOVERNANCA.md` §3, linha
  *Orquestração* da matriz de responsabilidades: a orquestração passa a rotear **a linha de retorno
  do executor** e **o laudo do `reviewer`**, com o roteamento em si (aprovado segue, reprovado volta
  ao mesmo escopo, escalado sobe ao dono) inalterado. `docs/RUBRICA_DE_REVISAO.md`, 6 ocorrências:
  as fontes de evidência de `criterio-de-pronto`, `escopo`, `rota`, `residuo` e `registro` passam a
  citar **o dossiê de evidência e o diff**, onde a `D2` realocou arquivos tocados, desvios e
  verificação; e a pendência de arquitetura ou requisito sobe ao dono pelo `--escalar` do laudo.
  `.claude/skills/diario-de-obras/SKILL.md`, 2 ocorrências: o estado `review` e a transição
  `in-progress` → `review` passam a dizer que o executor devolve **a linha de retorno da `DP-G`**.
  Nenhuma regra mudou de efeito — só o objeto citado: pesos, faixas e dimensões da rubrica, lista de
  estados, máquina de transições e alcance por objeto ficaram intocados, e nada novo foi enunciado.
  Onde a leitura ficaria ambígua com dois "dossiês" na mesma frase, o da tarefa passou a aparecer
  qualificado (`dossiê da tarefa`). Tarefa de redação de doutrina, sem TF/TR de código; sem achado
  fora de escopo. Verificação: as 9 ocorrências foram substituídas por `Edit`s de âncora exata sobre
  o texto colado no dossiê, todos aceitos. O executor atingiu o teto rígido de 15 tool uses no
  fechamento e deixou a conferência pendente; ela foi **executada pelo orquestrador na mesma
  rodada**: Grep por `pacote` nos três arquivos com resultado **vazio** nos três (0 ocorrências —
  nenhum sobrevivente a justificar, nem na acepção da `DP-H` item 4), e bateria do §3 verde —
  `kit_check.ps1 -Mode validate` exit 0 (8 agentes, 11 skills, VERSION == KIT_VERSION `0.0.0`),
  `check-readme.ps1` exit 0 (14 guardrails, 14 seções com Fonte da verdade), `dead_code.py` exit 0
  (0 achados) e `python -m pytest -q` com 39 passed. Achado de calibração levantado pelo executor:
  a classe `redacao` com 9 pontos de edição em 3 arquivos não cabe em 15 tool uses somando coleta,
  registro no diário e verificação — piso realista ~18-20, ou a verificação sai do teto do
  executor. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T32` — doutrina: o desempate do framework escala ao dono** (`done` — materializado pelo
  orquestrador: este plano não executa o loop que projeta, §3 item 1, então `review` não tem
  reviewer a invocar e a bateria de fechamento abaixo é o que fecha). O buraco que o
  `§12.1` e a `DP-H` declararam não decidido — o critério de desempate do framework em si — ganhou
  residência publicada. `GOVERNANCA.md:198-204`, §3.1, bloco *Precedência, quando duas superfícies
  colidem*: entra a **regra 3 — "Sem desempate → escala ao dono"**, depois de *Empate → versionado
  vence não-versionado*. Enuncia que, exauridas as regras 1 e 2, a ambiguidade não se resolve
  embaixo (nenhum agente arbitra por palpite, antiguidade ou recência), que o desempate do framework
  é o dono, que a regra de recência governa o desenvolvimento do framework dentro dos planos e **não
  é critério de desempate de doutrina publicada** (`DP-H` item 2), e que escalar é parar e perguntar
  — a mesma rota que a Regra 8 do `~/.claude/CLAUDE.md` dá ao executor. Invariantes respeitados:
  nenhuma seção nova, teste de residência das quatro perguntas intocado, regras 1 e 2 intocadas,
  parágrafo *Colisão não se resolve com as duas cópias vivas…* no lugar (`GOVERNANCA.md:205-206`).
  Nada da mecânica do `P-0734` (laudo, RDO, `status`, `pacote`) entrou no texto, e as âncoras da
  `T31` e da `T26` não foram tocadas — um único `Edit`, um único bloco. Tarefa de redação de
  doutrina, sem TF/TR de código; sem achado fora de escopo. Verificação colada do terminal:
  `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')* (exit 0); `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14 guardrail(s), versão
  '0.0.0', 14 seção(ões) com Fonte da verdade válida* (exit 0); `dead_code.py` → *OK - 0 achado(s)*
  (exit 0); `python -m pytest -q tests` → **39 passed** (piso anterior 39, mantido). Grep de aceite
  em `GOVERNANCA.md`: o bloco de precedência tem **três** regras numeradas (linhas 191, 194, 198) e
  a regra 3 contém `escala ao dono`. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T21a` — skill `scrum-master`: os passos do loop — `done`.** Os passos foram alinhados
  ao fluxo ratificado e o loop deixou de parar no passo 9. `## Estado do loop`: além dos três
  contadores da `DP-B`, o loop passa a guardar a **fila corrente e a ordem dela**, porque `A3a` a
  reordena em execução — nada mais entra. **Passo 2** lê a fila corrente (reordenada, se `A3a` já
  agiu na janela) e não o §5 do plano. **Passo 3** ganha a materialização `ready` → `in-progress`
  antes de delegar (`DP-G` item 1, consequência 3). **Passo 4** instrui o executor a devolver uma
  das duas linhas do domínio fechado (`<tarefa> review [pendencia=…]` \| `<tarefa> blocked
  motivo=<dependencia|premissa> …`) e declara o desempate `premissa`; sai a instrução de `rdo.py
  new`. **Passo 5** (agora *Recepção do retorno do executor*) materializa o valor devolvido sem
  discricionariedade, tipifica **retorno inválido** → `A2` e ancora os `tools` no bloco `<usage>`.
  **Passo 6** (agora *Despacho do `reviewer`*) é o **gatilho 1** da `DP-E`, recebe o mesmo dossiê do
  executor + o dossiê de evidência, sem caminho de RDO, e `blocked` não passa por ele (`DP-G` item
  4). **Passo 9** é o **gatilho 2**: uma chamada de `rdo.py close` com o consumo medido e o
  **pacote** do laudo (`--veredito --percentual --bloqueante --recomendacao --pendencia-laudo`,
  `DP-H` item 4), laudo **apagado** depois de consumido (`DP-H` item 3), `cancelled`/`blocked` sem
  RDO (`DP-F` item 3, fechamento (c)); o bloco *Ponto aberto* saiu. Sete ocorrências de *revisor*
  nas seções tocadas viraram `reviewer` (`DP-K` §14.2 item 2); as cinco fora de escopo (`:3` da
  `T33`; tabelas e proibições da `T21b`) ficaram intactas. Passos 1, 7, 8 e 10 e as seções de
  tabelas/relatório/proibições/guardrails não foram tocados, salvo a troca de termo no gatilho do
  passo 7, que o dossiê enumera. Tarefa de redação, sem TF/TR de código; sem achado fora de escopo.
  Verificação colada do terminal: `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s)
  validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1 -Mode check-drift` → *OK -
  .claude/README.md == regenerado (8 agente(s), 11 skill(s))* (exit 0); `check-readme.ps1` → *OK - 8
  agente(s), 11 skill(s), 14 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade
  válida* (exit 0); `python -m pytest` → **39 passed in 5.40s** (piso anterior 39, mantido). Grep de
  aceite em `.claude/skills/scrum-master/SKILL.md`: `pacote de retorno` → **0 ocorrências**;
  `rdo.py new` → 0; `Ponto aberto` → 0. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T21b` — skill `scrum-master`: tabelas de roteamento e vocabulário — `done`.** As duas
  tabelas passaram a refletir o estado ratificado. **Bloco A:** `A3` foi **partida** pela razão
  tipada — `A3a` (`motivo=dependencia`) reordena a fila para que a bloqueada suceda a que a bloqueia,
  materializa `blocked` com a razão, **não** despacha o `reviewer`, **não** escreve RDO, **não**
  consome retentativa, **não** incrementa o contador de tarefas fechadas e **segue**; `A3b`
  (`motivo=premissa`) materializa `blocked` e **PARA**, escalada ao dono (`DP-G` item 4). `A5`
  **saiu** da tabela (a numeração salta de `A4` para `A6`): `parcial` morreu como `status` e entrega
  incompleta é veredito do `reviewer`. `A4` passou a ler os `tools` do bloco `<usage>`; `A6`, `A8` e
  `A9` passaram a ler a **recomendação** do laudo (`refazer` / `seguir com ressalva` / `seguir`) em
  vez de derivar o desdobramento do veredito, e `A6` passou a despachar um executor **novo em
  contexto novo** com o dossiê original mais as **diretivas atualizadas**, **nunca** o caminho do
  laudo (`DP-H` item 3, `D6` reconciliado). `A1`, `A2` e `A7` ficaram intactos, e a precedência "a
  primeira que casa vence" permanece. **Bloco B:** `B1` passou a ler `pendencia=` do retorno do
  executor ou `recomendacao=escalar` do laudo; `B2`..`B4` e os três tetos da `DP-B` intactos.
  **Descarte do laudo em qualquer ramo** (`DP-K` §14.4): parágrafo próprio abaixo da tabela A —
  extraída a recomendação, o laudo é apagado na reexecução (`A6`), no fechamento (`A7`..`A9`, passo
  9) e na escalada (`B1`); nenhuma linha de tabela guarda ponteiro para ele. O bloco *O que obriga
  parada* deixou de citar os campos do pacote morto e passou a citar os canais vivos. A fonte
  normativa da seção ganhou `DP-G` item 4 e `DP-K` §14.4 ao lado de `DP-A`/`DP-B`, para que
  "divergência resolve a favor da seção" aponte para o texto ratificado. **Vocabulário:** só
  ocorrência de tipo (i) foi traduzida — `status=bloqueado` → `status=blocked` nas linhas do `A3`;
  `parcial` sobreviveu apenas onde não é `status` (`:214`, marcador literal `PARCIAL — trecho
  pré-queda não medido` do `A1`) e `bloqueado` apenas em prosa corrente (`:269`); `revisor` →
  `reviewer` no corpo (linhas do `A3`/`A4`/`A5` e a proibição *Não julga entrega*), com a
  `description` do frontmatter (`:3`) **intocada**, que é da `T33`. O frontmatter não foi editado, o
  `## Relatório de encerramento` e o `## Guardrails` não tinham termo morto nem citação do pacote e
  ficaram inalterados, e os passos entregues pela `T21a` não foram reabertos. Tarefa de redação, sem
  TF/TR de código. **Percurso a seco** (nenhum comando executado), sobre a `EXA-T32`, já fechada:
  passo 2 toma a tarefa da fila → passo 3 materializa `ready` → `in-progress` → passo 4 despacha o
  executor com o dossiê e o modelo do cabeçalho → passo 5 recebe `EXA-T32 review` (sem `pendencia=`)
  e lê os `tools` do `<usage>` → passo 6 (gatilho 1) despacha o `reviewer` → passo 7 lê `aprovado …
  bloqueante=nenhuma` + `laudo=<caminho>` → passo 8, bloco A por precedência: `A1` não (há
  `<usage>`), `A2` não (linha válida), `A3a`/`A3b` não (`status=review`), `A4` não (dentro do teto),
  `A6` não (`recomendacao=seguir`, não `refazer`), `A7` não, `A8` não, **`A9` casa** → fecha o RDO
  como `aprovado` e segue → passo 9 escreve o RDO por uma chamada de `rdo.py close`, **apaga o
  laudo** e apenda a telemetria → passo 10, bloco B: `B1` não (sem `pendencia=` e sem `escalar`),
  `B2` não (contadores abaixo dos tetos), `B3` conforme os gates da próxima, **`B4` casa** → despacha
  a próxima. Nenhuma célula do percurso exigiu juízo sobre prosa. Achado fora de escopo tiquetado,
  não corrigido: **`TK-33`** (três referências órfãs em passos e proibições que nem a `T21a` nem a
  `T21b` podiam tocar). Verificação colada do terminal: `kit_check.ps1 -Mode validate` → *OK - 8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1
  -Mode check-drift` → *OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s))* (exit 0);
  `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14 guardrail(s), versão '0.0.0', 14 seção(ões)
  com Fonte da verdade válida* (exit 0); `python -m pytest` → **39 passed in 6.14s** (piso anterior
  39, mantido). Grep de aceite em `.claude/skills/scrum-master/SKILL.md`: `revisor`
  (case-insensitive) → **1 ocorrência**, `:3`, a `description` do frontmatter, que é da `T33`;
  `pacote de retorno` → **0**; `in progress|in review` → **0**; `backlog`/`entregue` como `status` →
  **0**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T33` — Conformidade: `reviewer` nas linhas espelhadas e no resíduo fora do loop —
  `done`.** `reviewer` passa a ser o **termo único** do papel no texto vivo do kit e nos artefatos
  publicados (`DP-K` §14.2 item 2). Sete ocorrências em cinco arquivos, todas substituição
  **palavra por palavra** (`revisor`/`Revisor` → `reviewer`/`Reviewer`), sem enunciar regra nova e
  sem tocar campo, tabela, peso ou passo: os dois pares espelhados mudaram **no mesmo ato** e com
  texto idêntico caractere a caractere — `.claude/skills/scrum-master/SKILL.md:3` ↔
  `.claude/README.md:57` (`description` da skill) e `.claude/agents/pantonic-reviewer.md:3` ↔
  `.claude/README.md:19` (`description` do agente) —, mais a prosa de abertura do agente (`:8`,
  "Você é o **reviewer**"), a paráfrase da tabela do espelho em `README.md:755` (não é cópia
  verbatim da `description`: trocada só a palavra, frase preservada) e a docstring de
  `tests/test_rdo.py:122` (**só a palavra**; nenhuma asserção, nenhum comportamento). `model:` e
  `tools:` do frontmatter do `pantonic-reviewer` ficaram intocados (`TK-27`). Registro histórico
  (`docs/DIARIO_HISTORICO.md`, `docs/RDO/`, `docs/telemetria.tsv`), `docs/plans/**` e o *Revisor*
  do OpenSpec em `docs/benchmark/BM-03-fission-ai-openspec.md:26` (papel de framework externo)
  ficaram como estavam. Dois desvios do dossiê verificados na entrada e sem efeito no escopo: o
  corpo do `SKILL.md` do `scrum-master` já estava limpo pela `T21a`/`T21b` (sobrava só o
  frontmatter) e a ocorrência de `tests/test_rdo.py` migrou de `:186` para `:122` na reescrita da
  `T19`. Tarefa de redação, sem TF/TR de código. Verificação colada do terminal:
  `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')* (exit 0); `kit_check.ps1 -Mode check-drift` → *OK - .claude/README.md == regenerado
  (8 agente(s), 11 skill(s))* (exit 0); `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida* (exit 0) — prova da
  paridade dos espelhos; `dead_code.py` → *OK - 0 achado(s)* (exit 0); `python -m pytest` →
  **39 passed in 8.57s** (piso anterior 39, mantido). Grep de aceite case-insensitive por `revisor`
  em `.claude/`, `README.md` e `tests/` → **0 ocorrências** nos três.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T35` — Auditoria: a matriz de responsabilidades como autoridade exaustiva — `done`.**
  Precondição da `T36` cumprida: a matriz de `GOVERNANCA.md` §3 foi medida papel vivo por papel
  vivo e fechada por **transcrição**. Universo medido: os **oito** agentes de `.claude/agents/`
  (o diretório inteiro) mais o `scrum-master`, único papel que vive numa skill. Seis agentes já
  estavam cobertos (`planner`→Planejamento, `executor`→Execução, `reviewer`→Revisão,
  `scout`→Coleta, `auditor-arch` e `auditor-cleancode` → a linha *Auditoria*, que nomeia os dois)
  e o `scrum-master` entrou pela linha *Orquestração* que já existia — papel em skill não vira
  linha nova. **Duas lacunas, ambas do tipo (a) transcrição, ambas fechadas:** `pantonic-fora-da-caixa`
  → linha **Redesenho** (Opus, do frontmatter) e `pantonic-benchmarker` → linha **Benchmarking**
  (Haiku, do frontmatter); as quatro células saíram do que o próprio prompt já publica (`## Por que
  você existe` e `## Método por alvo`; `## Guardrails do coletor` e o esquema `D1..D16`). **Nenhuma
  lacuna (b)** — nenhuma responsabilidade existia sem estar publicada, logo **nenhum tíquete novo** e
  nada a subir ao dono. Invariantes respeitados: nenhuma responsabilidade criada, nenhuma proibição
  nova na coluna *Não faz* das sete linhas preexistentes, nenhuma proibição podada (é a `T37`),
  guardrail 15 não escrito (é a `T36`), `README.md`, `.claude/**` e `docs/RDO/**` intocados. A
  medida completa, com veredito por arquivo, ficou em `docs/plans/P-0734-execucao-autonoma.md`
  `### 16.7`. Tarefa de auditoria/redação, sem TF/TR de código. Contagem da matriz re-derivada
  (Grep `^\|\s\*\*`, 11 matches no arquivo − 2 da tabela de residência do §1): **7 linhas antes,
  9 depois**. Verificação colada do terminal: `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e
  11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1 -Mode
  check-drift` → *OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s))* (exit 0);
  `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida* (exit 0) — 14 guardrails inalterados, prova de que o
  guardrail 15 não foi antecipado; `dead_code.py` → *OK - 0 achado(s)* (exit 0); `python -m pytest`
  → **39 passed in 3.90s** (piso anterior 39, mantido).
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T36` — Doutrina: guardrail 15 (`G-SCOPE`) e o espelho em lockstep — `done`.** A golden
  rule de escopo de agente passa a existir na doutrina publicada: `GOVERNANCA.md` §7 ganha o **item
  15** (`G-SCOPE` — o agente se atém estritamente às responsabilidades declaradas; o que não está
  escrito é proibido), inserido entre o item 14 e o parágrafo "Esses guardrails são materializados
  em cada projeto como:", com a **matriz de responsabilidades do §3 nomeada como autoridade
  exaustiva**, a proibição de prompt criar responsabilidade por conta própria, o critério que poda
  proibição redundante (só se justifica a que restringe o exercício da **própria** responsabilidade
  declarada) e o *Enforcement* em instrução de agente/skill + gate de review sobre prompt novo ou
  alterado. O bullet "**Papéis não são intercambiáveis**" do §3 passa a **apontar** para o §7 item
  15 sem reenunciar a regra. Espelho subiu **no mesmo ato**: `README.md` §10 ganha a linha `| 15 |`
  e o numeral de abertura vira "**Quinze** regras mínimas obrigatórias". Nenhum dos 14 itens
  vigentes foi reescrito; nenhuma regra nasceu no README; nenhum prompt de agente ou skill foi
  tocado (é a `T37`); `docs/RESIDENCIA_DOUTRINA.md` intocado; sem bump de `VERSION` nem de
  `.claude/KIT_VERSION` (congelamento do §10 em vigor). **Achado — prosa de contagem do README
  (`:710`) estava divergente da tabela:** o texto vigente dizia "**Seis** … **seis**", mas a
  recontagem das três famílias **sobre a tabela** dá, com 14 linhas, **7** por teste executável
  (1–6 e 8) e **7** por gate de review/instrução (7–8, 9–12, 14), o item 8 aparecendo nas duas por
  somar as formas, mais **1** por permissão (13). Com o item 15 (instrução + gate), a contagem
  escrita passou a **sete** por teste executável e **oito** por gate/instrução, com a ressalva do
  item dual explicitada ("e por isso aparece nas duas contagens") para a aritmética fechar em 15.
  O número recontado mandou; nenhuma doutrina nova entrou por isso, e o desvio se esgota aqui (sem
  tíquete). `CHANGELOG.md` recebeu **uma** linha sob `[Não lançado]`, no formato da seção.
  Tarefa de redação, sem TF/TR de código. Verificação colada do terminal: `check-readme.ps1` →
  *OK - 8 agente(s), 11 skill(s), **15 guardrail(s)**, versão '0.0.0', 14 seção(ões) com Fonte da
  verdade válida* (exit 0) — de **14 × 14** para **15 × 15**; `kit_check.ps1 -Mode validate` →
  *OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0);
  `kit_check.ps1 -Mode check-drift` → *OK - .claude/README.md == regenerado (8 agente(s),
  11 skill(s))* (exit 0); `dead_code.py` → *OK - 0 achado(s)* (exit 0); `python -m pytest` →
  **39 passed in 3.93s** (piso anterior 39, mantido). Greps de aceite: `^15\. \*\*` em
  `GOVERNANCA.md` → **1** (linha 585); `^\| 15 \|` em `README.md` → **1** (linha 709);
  `DP-M|P-0734|T36` em `GOVERNANCA.md` e `README.md` → **vazio** nos dois. Teto 30 respeitado
  (regime `TK-32`), sem estouro.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T37` — Conformidade: poda das proibições que a matriz passa a derivar — `done`.** Os dois
  prompts que mais repetiam fronteira de outro papel pararam de repeti-la: **nove** bullets saíram
  dos blocos `## Proibições`, todos derivados da matriz de `GOVERNANCA.md` §3 somada ao guardrail 15
  (`G-SCOPE`, publicado pela `T36`). **Nenhuma regra perdeu efeito** — o que saiu passou a valer por
  derivação. `.claude/skills/scrum-master/SKILL.md` foi de **6 para 2** bullets: saíram "Não
  implementa…" (linha *Execução* da matriz), "Não julga entrega…" (*Revisão*), "Não decide
  arquitetura nem requisito…" (*Planejamento* e *Dono/gerente*) e "Não reescreve dossiê…"
  (*Planejamento*); permaneceram "Não abre o RDO nem o laudo…" (**intocado — é objeto da `T39`**) e
  "Não despacha duas tarefas em paralelo…", fronteira interna do próprio loop.
  `.claude/agents/pantonic-reviewer.md` foi de **7 para 3**: saíram "A única escrita permitida é o
  laudo…", "Não corrige o que aponta…", "Não replaneja e não decide rota…", "Não declara `status` de
  tarefa…" (*Execução* e *Orquestração*, `DP-G`) e "Não julga mais de uma tarefa por contexto";
  permaneceram as três que restringem o exercício da **própria** responsabilidade ("Não marca
  `conforme` contra vermelho mecânico", "Não completa critério de pronto inverificável por conta
  própria" e "Não escreve percentual nem veredito"). Estado de entrada conferido contra o dossiê
  **antes da primeira edição**: os dois blocos batiam bullet a bullet, nenhum faltando, nada a
  reconciliar. Invariantes respeitados: nada novo enunciado nos dois arquivos, nenhum passo, tabela,
  campo, contador ou gatilho tocado, `## Guardrails` do `scrum-master` fora do escopo, nenhum
  ponteiro explicativo para o guardrail 15 acrescentado (prompt não recopia doutrina) e nenhum outro
  prompt do kit podado (`DP-M` §16.5). Tarefa de redação, sem TF/TR de código. Verificação colada do
  terminal: `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s) validados; VERSION ==
  KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1 -Mode check-drift` → *OK - .claude/README.md ==
  regenerado (8 agente(s), 11 skill(s))* (exit 0); `check-readme.ps1` → *OK - 8 agente(s), 11
  skill(s), 15 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida* (exit 0);
  `python -m pytest` → **39 passed in 2.51s** (piso anterior 39, mantido). Greps de aceite: o início
  de cada um dos **nove** bullets removidos → **vazio** nos dois arquivos; "Não abre o RDO" no
  `scrum-master` → **1** ocorrência (linha 275, a `T39` a remove). **Teto de 15 (classe `redacao`)
  cruzado** — fechamento em ~19 tool uses, sob o regime `TK-32` (teto é alarme, não bloqueio). Causa
  medida, sem tarefa mal decomposta: a poda em si custou 3 chamadas (2 leituras + 3 edits em 2
  turnos); o excedente veio de **localizar a bateria de verificação** — o dossiê aponta "os quatro
  checks do §3 item 6" e o §3 lido é o de `GOVERNANCA.md`, não o do plano, o que gastou quatro
  buscas até achar `docs/plans/P-0734-execucao-autonoma.md:120-124` — e de **localizar o ponto de
  inserção no diário** (mais quatro). Recomendação ao planejamento: dossiê de tarefa de redação que
  cita "§3 item 6" nomear o arquivo do §3 e colar os quatro comandos, como já fazem outros cards do
  mesmo plano.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T38` — Laudo mínimo: `--observacoes` sai do gerador — `done`.** `.claude/tools/rdo.py`
  perdeu as três referências ao campo: o argumento `--observacoes` (linha 701), a variável
  `observacoes` (linha 479) e a linha `**Observações:** {observacoes}` do corpo do laudo (linha
  491) — `cmd_laudo` fica só com os cinco campos calculados mais a tabela de níveis.
  `.claude/agents/pantonic-reviewer.md` perdeu `--observacoes "<texto>"` do bloco de comando do
  passo 6; a prosa vizinha (linhas 67-72) já não citava observações, conferido sem edição.
  Nenhuma asserção em `tests/` citava o campo, então não houve atualização de teste. Invariantes
  respeitados: `calcular_laudo` e o cálculo de percentual, veredito, bloqueante, recomendação e
  pendência intocados; nenhum outro flag saiu; destino do laudo e escrita atômica como estavam;
  `docs/RUBRICA_DE_REVISAO.md` e `## Proibições` não tocados. Verificação: os quatro checks do §3
  item 6 do plano (`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`,
  `python -m pytest`) em exit 0; `python -m pytest` → **39 passed**, piso mantido;
  `python .claude/checks/dead_code.py` → exit 0, 0 achados; Grep `observacoes|Observações`
  (case-insensitive) em `.claude/` → **vazio**. **Teto de 15 (classe `mecanica`) cruzado** — 20 tool
  uses medidos, sob o regime `TK-32` (teto é alarme, não bloqueio). Causa medida, sem tarefa mal
  decomposta: a edição custou 3 edits + 5 verificações; o excedente veio de localizar o ponto de
  inserção no diário e o formato do bullet anterior, mais uma leitura desnecessária do índice de
  tíquetes. Recomendação ao planejamento: dossiê de tarefa `mecanica` que fecha em plano em
  andamento colar o range de linhas do bullet de fechamento anterior, como já faz para os checks.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T39` — `TK-33`: passos 7 e 8, a acepção de `pacote` em `A2` e a proibição que a `DP-M`
  dispensa — `done`.** Uma passada só em `.claude/skills/scrum-master/SKILL.md`, quatro pontos.
  (1) Gatilho do **passo 8**: "passo 5 concluído (regras `A1`..`A5`)" passou a ler `A1`..`A4` —
  `A5` não existe e as regras avaliadas depois do passo 5 são `A1`, `A2`, `A3a`, `A3b` e `A4`.
  (2) **Passo 7** (*Leitura do veredito*) passou a colher também a **recomendação**, campo fechado
  do laudo (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), que `A6`, `A8`, `A9` e `B1` leem
  e que nenhum passo colhia; a saída do passo virou a tripla (`veredito`, `bloqueante`,
  `recomendação`) e a **Entrada** do passo 8 passou a recebê-la assim. O retorno de duas linhas do
  `reviewer` **não mudou** e nenhum campo novo foi criado (`DP-M` §16.4). (3) Regra `A2`: "pacote
  ausente ou inválido" passou a dizer **retorno** ausente ou inválido — `A2` julga o retorno do
  executor, e `pacote` nomeia os cinco campos do laudo (`DP-H`, item 4); só o termo mudou, condição
  e encaminhamento idênticos. (4) O bullet "Não abre o RDO nem o laudo…" saiu de `## Proibições`
  **sem fronteira substituta**: com `Observações` fora do gerador (`EXA-T38`) o laudo só tem campo
  fechado ou calculado, e os passos 7 e 9 o leem por desenho. Invariantes respeitados: nenhuma
  tabela de roteamento mudou de **efeito**; nenhum contador, teto ou gatilho novo; passo 9 intocado;
  nada acrescentado ao retorno do `reviewer`; os demais bullets de `## Proibições` como a `T37` os
  deixou; nenhum outro arquivo do kit editado. Verificação: os quatro checks do §3 item 6 do plano
  (`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`, `python -m pytest`) em
  exit 0, com **39 passed** (piso mantido); Grep `A5` no arquivo → **1** ocorrência, a que narra a
  queda de `A5` como fonte normativa (`:210`); Grep `pacote ausente` → **vazio**; Grep
  `Não abre o RDO` → **vazio**; Grep `recomenda` no bloco do passo 7 → **2** ocorrências (`:148`,
  `:151`). Teto de 15 (classe `redacao`) **não cruzado**: 13 tool uses medidos — o dossiê trouxe as
  âncoras re-derivadas e o range do bullet anterior, o que eliminou a busca de localização que
  custou o excedente da `T38`, e as quatro edições e os quatro checks couberam em três turnos.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T23b` — conformidade do `proximo-passo` com a residência única — `done`.** O entregável foi
  produzido e verificado em 2026-08-11 (bullet acima) e a tarefa ficou `blocked` por não haver quem a
  concluísse: a transição `review` → `done` é escrita só pelo `scrum-master`, que só passou a existir
  com `T19`, `T20`, `T21a` e `T21b`. As quatro estão `done`, então a razão registrada do bloqueio não
  se aplica mais — o desbloqueio é consequência mecânica do plano vigente, não decisão nova. Estado
  re-derivado no fecho sobre o arquivo **como ele está hoje** (tocado depois daquela rodada pela
  correção do `TK-34`, que acrescentou o dever de âncoras ao item 3 do gate de delegação): Grep
  `in progress|in review` em `.claude/skills/proximo-passo/SKILL.md` → **vazio**; Grep `backlog` →
  **5** ocorrências, todas substantivo (`description` do frontmatter, título, abertura, "próxima
  tarefa do backlog", "fora do backlog"); o parágrafo de vocabulário (`:15-19`) continua apontando
  para `diario-de-obras`, `## Status — residência única`, sem recopiar lista, máquina nem tabela de
  alcance; o item 4 da `DP-F` segue afirmado no guardrail de `superseded` (`:172-173`). Nenhuma
  regra de escolha mudou de efeito e **nenhuma edição de conteúdo foi necessária** — a conformidade
  entregue em 2026-08-11 sobreviveu intacta à edição do `TK-34`. Verificação: os quatro checks do §3
  item 6 de `docs/plans/P-0734-execucao-autonoma.md` (`kit_check.ps1 -Mode validate` → *8 agente(s) e
  11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` → *.claude/README.md
  == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da
  verdade válida*; `python -m pytest`) em **exit 0**, com **39 passed** (piso mantido, 39 × 39).
  Rodada de fechamento conduzida pelo orquestrador, sem delegação: o que restava da tarefa era
  materializar `status`, ato exclusivo do `scrum-master` pela `DP-G`. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T24` — conformidade do restante do kit executável — `done`.** Os seis arquivos do kit que
  ainda citavam vocabulário morto de `status` foram alinhados à tabela de tradução da `DP-F`, com
  classificação por tipo de ocorrência antes de qualquer substituição. **9 edições em 4 arquivos:**
  `.claude/skills/handover/SKILL.md` (`:17` `in progress`→`in-progress`; `:20-21` `in review`→
  `review` e `in progress`→`in-progress`; `:43` ciclo do sprint `backlog`↔`in progress`↔`done` →
  `ready`↔`in-progress`↔`done`; `:109` `in progress`→`in-progress`);
  `.claude/skills/guardrails-check/SKILL.md` (`:8` `in review`→`review`; `:111` `in progress`→
  `in-progress`); `.claude/skills/bootstrap-pantonic/SKILL.md` (`:59` sprint inicial em `backlog`→
  `ready`, aqui `backlog` é status, não substantivo); `.claude/agents/pantonic-executor.md` (`:49`
  `in progress`→`in-progress`; `:60` `in review`→`review`). No `handover` `:20-21`, a enumeração dos
  quatro estados **permaneceu enumeração** — é regra do próprio handover, não recópia da lista
  canônica — e ganhou uma única linha de ponteiro para `.claude/skills/diario-de-obras/SKILL.md`,
  `## Status — residência única`. **Dois arquivos com zero edições, como previsto:**
  `.claude/skills/modelo-por-fase/SKILL.md` (`:63`, `:66`, `:67` — 3 ocorrências de `backlog`, todas
  tipo substantivo, e em `:67` string literal da lista de exclusão do hook: `pegue o backlog`;
  traduzir quebraria o casamento) e `.claude/README.md` (`:55`, substantivo dentro da região gerada
  a partir do `description` do frontmatter da `proximo-passo` — região gerada não se edita à mão).
  Invariantes respeitados: nenhuma regra mudou de efeito, nenhuma lista de estados foi recopiada em
  nenhum dos seis arquivos, nenhum gate foi reenunciado e nenhum arquivo fora dos seis foi tocado.
  Verificação (bateria do §3 item 6 de `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**):
  `kit_check.ps1 -Mode validate` → *8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')*; `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` →
  **39 passed** (piso mantido, 39 × 39 — a tarefa não toca código). Grep `in progress|in review`
  (case-insensitive) nos seis alvos → **vazio**. Grep `backlog` nos seis → **4 sobreviventes**, todos
  legítimos: `modelo-por-fase` ×3 (substantivo/string literal do hook) e `.claude/README.md` ×1
  (substantivo em região gerada). **Achado (fora do escopo desta tarefa, que só troca termo e não
  muda conteúdo de regra):** `.claude/agents/pantonic-executor.md:60` manda o executor gravar `done`
  no diário, o que contraria a fronteira da `DP-G` — o executor é autor de `review` e `blocked` e de
  mais nada, quem materializa `done` é o `scrum-master`. Teto de 30 (classe `redacao`) **não
  cruzado**: 24 tool uses medidos — o dossiê trouxe as âncoras re-derivadas no ato, as contagens
  por arquivo corrigidas (`guardrails-check` e `pantonic-executor` tinham 2 cada, não 1) e a
  classificação dos dois arquivos de zero edição já decidida, de modo que o executor não pagou
  nem localização nem classificação. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T40` — alinhamento do executor: o prompt para de escrever e passa a sinalizar — `done`.**
  `.claude/agents/pantonic-executor.md` (arquivo único) passou a descrever o papel que a `DP-N`
  fixou. **Sete edições, uma por âncora:** a abertura ganhou a responsabilidade enunciada pelo dono
  — entregar código **funcional e conforme com as regras do projeto** (testes passando, golden rules
  cumpridas), com a aferição da aceitação declarada como ato do `reviewer`; o fato estável de
  economia de turnos trocou os dois "handover" por **sinal ao `scrum-master`**, sem tocar o número
  `~≤40` (é objeto do `TK-04`); o bullet do `Consumo:` **saiu inteiro**, porque quem não escreve no
  diário não grava placeholder nem número; o achado fora de escopo deixou de ser "tíquete indexado
  no diário" e virou **uma linha do sinal**, com a indexação atribuída ao `scrum-master`; o passo 2
  perdeu "marque `in-progress`" e ficou só em localizar a própria tarefa pelo índice; o passo 4
  passou a **sinalizar `blocked` com razão tipada** (`dependencia`/`premissa`, `DP-G`) e encerrar,
  com a declaração em prosa dos chamadores de produção removida — a alcançabilidade é medida por
  `.claude/checks/dead_code.py` e julgada na dimensão `guardas` do laudo, e `G-DEADCODE` continua
  valendo; o passo 5 virou **entrega tecnicamente correta** (suíte da área + conformance + piso) e o
  passo 6 deixou de invocar a skill `handover`, de atualizar o diário e de registrar o que foi
  feito: **sinaliza `review` e encerra**. Invariantes respeitados: nenhuma regra de execução mudou
  de efeito, o `frontmatter` não foi tocado (por isso `.claude/README.md` não precisou ser
  regenerado), nenhuma lista de estados entrou no arquivo e nada do `reviewer` ou do `scrum-master`
  foi reenunciado. Verificação (bateria do §3 item 6 de
  `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode validate` → *8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed** (piso mantido,
  39 × 39 — a tarefa não toca código). Greps de aceite: `handover` → **vazio** (era 5 ocorrências);
  `diário` → **4 sobreviventes**, todas legítimas e nenhuma instrução de escrita (`:3` frontmatter,
  `:8` abertura, `:36` higiene de busca, `:48` passo 2). Teto de 15 (classe `redacao`) **não
  cruzado**: 9 tool uses medidos — o dossiê trouxe as sete âncoras coladas do arquivo, as duas
  contagens de Grep medidas no ato e a lista nominal dos quatro sobreviventes esperados, de modo que
  o executor não pagou localização nem classificação. Rodada fechada pelo orquestrador: o executor
  não editou o diário, não invocou `handover` e não gravou consumo — antecipação deliberada do
  regime que a própria tarefa institui. Consumo: ver `docs/telemetria.tsv`.
- **`EXA-T41` — as superfícies que descrevem o executor — `done`.** As cinco superfícies nomeadas
  pelo dossiê pararam de atribuir escrita ao executor, sem que nenhum princípio mudasse — **só o
  portador do ato**. `GOVERNANCA.md:93` (matriz §3, linha *Execução*): a coluna *Responde por* passa
  a declarar a entrega tecnicamente correta e o **sinal** (`review`/`blocked`), a coluna *Não faz*
  recebe que ele não escreve no diário, não registra o resultado da própria entrega e não afere a
  própria aceitação, e a cláusula final trocou "registra `blocked` no diário" por **sinaliza**;
  `GOVERNANCA.md:301-302` (§4.2): o registro do consumo é de **quem orquestra**, a partir do dado
  medido da notificação, com o desvio de 11-44% preservado como razão afirmada inline. Espelho em
  lockstep no `README.md` (o parágrafo de telemetria e a célula da tabela de preços), mesma seção,
  mesma ordem e mesma quantidade de afirmações, sem doutrina nova. Kit:
  `.claude/skills/proximo-passo/SKILL.md` perdeu a alternativa do placeholder — resta a forma única
  "o executor não edita o diário; o orquestrador escreve o bullet inteiro", com o ponteiro
  `Consumo: ver docs/telemetria.tsv` escrito direto no bullet e preservadas as regras de Edit
  pós-`Agent` e de telemetria vencida no pickup; `.claude/skills/guardrails-check/SKILL.md:8` passou
  a "obrigatório antes de sinalizar `review`", com o frontmatter intacto (índice não regenerado).
  Verificação (bateria do §3 item 6 de `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**):
  `kit_check.ps1 -Mode validate` → *8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')*; `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` →
  **39 passed** (piso mantido, 39 × 39 — a tarefa não toca código). Greps de aceite: `handover` na
  linha 93 de `GOVERNANCA.md` → **vazio**; `executor grava` em `README.md` → **vazio** e em
  `GOVERNANCA.md` → **1 sobrevivente**. **Achado indexado pelo orquestrador:** o dossiê contava 2
  ocorrências de `executor grava` e existem 3 — a terceira (`GOVERNANCA.md:341`, checkpoint
  intermediário pela skill `handover`) está inteiramente dentro do recorte do `TK-36`, que ganhou a
  superfície na linha do índice; é a contradição declarada entre esta tarefa e aquele tíquete, não
  um desvio da entrega. Teto de 30 (classe `redacao`) **não cruzado**: 17 tool uses medidos — o
  dossiê trouxe as cinco âncoras coladas do arquivo e a contagem de cada grep de aceite. Rodada
  fechada pelo orquestrador: o executor sinalizou `review` e não tocou diário, `handover` nem
  telemetria. Consumo: ver `docs/telemetria.tsv`.
- **`EXA-T42` — a resposta na descoberta de não-conformidade de escopo — `done`.** O guardrail 15
  (`G-SCOPE`) deixou de falar só do prompt novo e passou a dizer o que se faz quando a violação é
  **encontrada em artefato existente**, sem que nenhum enunciado anterior mudasse. `GOVERNANCA.md`
  §7 item 15 ganhou duas cláusulas na sequência de "…redundante e sai": (1) **resposta na
  descoberta** — artefato do framework que atribui a um agente ato **não endossado** pela matriz, ou
  que carrega papel que ela **sequer cita**, é **não-conformidade grave**, que se para e regulariza
  em vez de enfileirar como dívida; (2) **a lacuna oposta não se resolve no ato** — ato **real e
  necessário** que a matriz não declara é falta **da matriz**, e criá-lo no prompt é exatamente a
  violação: registra-se e **sobe ao dono** (mesma regra da `DP-M`, §16.5). O *enforcement* ganhou a
  **varredura dos artefatos já existentes** ao lado do gate sobre prompt novo ou alterado. Espelho em
  lockstep na linha `| 15 |` de `README.md` §10, com as duas cláusulas condensadas na célula da regra
  e a varredura entrando como **qualificação do gate de review existente** — não como forma nova de
  enforcement —, de modo que o parágrafo de contagem (`README.md:711-713`, "**Sete**… **oito**… as
  três formas") permaneceu verdadeiro e intocado. Contagem preservada em **15 × 15**, sem guardrail
  novo e sem responsabilidade nova. Verificação (bateria do §3 item 6 de
  `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode validate` → *8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed** (piso mantido,
  39 × 39 — a tarefa não toca código). Teto de 15 (classe `redacao`) **não cruzado**: 7 tool uses
  medidos — o dossiê trouxe as duas âncoras coladas na íntegra, o texto vizinho de cada uma e o
  invariante de contagem, e o executor não pagou localização. Rodada fechada pelo orquestrador: o
  executor sinalizou `review` e não tocou diário, `handover` nem telemetria. Consumo: ver
  `docs/telemetria.tsv`.
- **`EXA-T43` — sanitização do kit executável contra a matriz — `done`.** Os **19** prompts do kit
  (8 agentes + 11 skills) foram varridos contra a matriz de responsabilidades (`GOVERNANCA.md` §3)
  pelo método prescrito — uma coleta programática pelos doze verbos atributivos, **307 ocorrências
  brutas**, e leitura dirigida só das regiões apontadas. As **36** ocorrências classificadas ficaram
  em `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md` §1, uma linha por ocorrência com arquivo,
  linha, papel, atribuição, veredito (a/b/c) e ação; a §2 nasce aberta, com cabeçalho e a nota de
  escopo da `T44`. **Doze edições, todas de classe (b)**: os dois auditores deixaram de mandar
  registrar tíquete "via `pantonic-planner`" e passaram a dizer o que a matriz declara (o
  apontamento vira item do diário, priorizado pelo dono); o `pantonic-planner` perdeu os dois
  bullets redundantes de "nunca faz", um dos quais ainda atribuía `handover` ao planejamento; a
  `guardrails-check` corrigiu quatro pontos (ponteiro para o papel inexistente
  `integration-executor`, "recomenda no handover" → sinal de retorno, "agente de refactor" →
  auditor de clean code, o bloco de veredito indo às *Notas de execução* do diário, e "registrar no
  diário" → "sinalizar `blocked` com a razão tipada"); a `diario-de-obras` perdeu duas atribuições
  de escrita no diário à Execução; a `proximo-passo` perdeu a cláusula que autorizava delegar
  execução a `clean-code`/`architect-auditor`, papéis que a matriz sequer cita; e duas
  `description` de frontmatter saíram do vocabulário morto (`audit-sweep`: frente "pyside6" →
  "DDD", o que **fecha o `TK-12`**; `integrar-poc`: "do agente integrador"), com `.claude/README.md`
  regerado por `-Mode generate`. `scrum-master`, `pantonic-reviewer` e `pantonic-executor` foram
  reconferidos e **saíram sem edição** — o que apareceu neles é (a) ou já resolvido pela `T37`/`T40`.
  Nenhuma responsabilidade nova, nenhuma proibição nova, `GOVERNANCA.md` intocado. **Um achado de
  classe (c)** — a skill `handover` atribui à Execução escrever o checkpoint de contexto nas *Notas
  de execução* do diário, ato real e necessário que a matriz não declara —, não editado por
  prescrição do item 15 e indexado como **`TK-37`**, que sobe ao dono. Verificação (bateria do §3
  item 6 de `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode
  validate` → *8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*;
  `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s),
  versão '0.0.0', 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed**
  (piso mantido, 39 × 39 — a tarefa não toca código). Teto de 40 (classe `redacao`) **atingido no
  limite**, 41 tool uses medidos: o volume vem do universo varrido (19 arquivos, 307 ocorrências,
  18 leituras dirigidas antes de 12 edições) e não de thrashing, e sob o regime interino do
  `TK-32` o teto é alarme — a tarefa fechou completa. Rodada fechada pelo orquestrador: o executor
  sinalizou `review` e não tocou diário, `handover` nem telemetria. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T44` — sanitização da doutrina, do espelho e dos índices contra a matriz — `done`.** Os
  **6** documentos do universo fechado (`GOVERNANCA.md` 839 linhas, `README.md` 933,
  `ARQUITETURA_PANTONICA.md` 513, `docs/RUBRICA_DE_REVISAO.md` 259, `docs/RESIDENCIA_DOUTRINA.md`
  188, `docs/DOC_MAP.md` 102) foram varridos contra a matriz de responsabilidades (`GOVERNANCA.md`
  §3) pelo método prescrito — uma coleta programática pelos doze verbos atributivos, **381
  ocorrências brutas**, mais uma varredura complementar por **papel que a matriz sequer cita**
  (segundo membro do `G-SCOPE`, que os verbos não pegam por construção) —, com leitura dirigida só
  das regiões apontadas e nenhum Read integral nos três docs acima de 500 linhas. As **38**
  ocorrências classificadas ficaram na §2 de `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md`
  (`#37`..`#74`, mesma tabela da §1): **32 (a)**, **4 (b)**, **1 (c)** e uma linha declarada fora do
  escopo (§9 do `README.md`, recorte do `TK-36`). **Quatro edições, todas de classe (b)**: o estouro
  de teto deixou de se reportar "no handover" e passou ao **sinal de retorno** (`GOVERNANCA.md:139`,
  mesma correção do `#13` da `T43`); "o agente atualiza o diário de obras e faz handover"
  (`:333-334`) passou a dizer que quem executa **sinaliza** (`review`/`blocked` com razão tipada) e
  encerra o próprio contexto, cabendo o registro do fechamento e a abertura da tarefa seguinte à
  orquestração; o espelho `README.md:402-403`, que mandava "marcar `blocked` no diário e fazer
  handover", passou a "sinaliza `blocked` com a razão tipada e escala" — a **fonte já dizia isso**,
  só o espelho divergia; e "agente de integração", papel que a matriz sequer cita, saiu das duas
  ocorrências de `ARQUITETURA_PANTONICA.md` (`:155`, `:393`) para "harness de integração de POC" e
  "Pipeline de integração da POC (5 passos)". Nenhuma responsabilidade nova, nenhuma proibição nova,
  **matriz intocada** (é a régua, `#37`), registros do que aconteceu à época preservados (rodadas da
  §7.1, `RESIDENCIA_DOUTRINA.md`) e contagens do espelho intactas (15 × 15 guardrails, 14 seções com
  Fonte da verdade). **Um achado de classe (c)** — `GOVERNANCA.md:340-344` atribui à Execução gravar
  o checkpoint intermediário ao cruzar 2/3 do teto: é a **fonte na doutrina** da mesma lacuna do
  `#27` da §1, não editada pela prescrição do item 15 e **sem tíquete novo**, porque o `TK-37` já a
  registra e a superfície já está no recorte do `TK-36`. Verificação (bateria do §3 item 6 de
  `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode validate` → *8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed** (piso mantido, 39 × 39
  — a tarefa não toca código). Consumo **18 tool uses** contra teto 40 da classe `redacao`, com
  folga: o método prescrito (uma coleta programática, depois leitura dirigida) é o que segurou o
  custo num universo de 381 ocorrências brutas. Rodada fechada pelo orquestrador: o executor
  sinalizou `review` e não tocou diário, `handover` nem telemetria. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T25` — conformidade: espelho e índices — `done`.** A porta de entrada do projeto deixou de
  ensinar vocabulário morto de `status`. `README.md`: 8 substituições de tipo (i) (`in progress` →
  `in-progress` em `:449`, `:454`, `:527`, `:626`, `:661`; `backlog` → `ready` em `:452`, `:528`;
  `in review` → `review` em `:681`) mais a reescrita do parágrafo dos estados válidos (`:533-540`),
  que agora espelha a lista final ratificada — `triage`, `ready`, `blocked`, `in-progress`,
  `review`, `done`, `cancelled` —, declara `done` e `cancelled` como os terminais de tarefa, tira
  `superseded` da lista e o enuncia como estado **exclusivo de plano e de iniciativa** (tarefa
  tornada obsoleta é `cancelled`), e **aponta** para `## Status — residência única` de
  `.claude/skills/diario-de-obras/SKILL.md` sem recopiar a máquina de transições nem o alcance por
  objeto. As 10 ocorrências de tipo (ii)/(iii) — `backlog` substantivo, `superseded` de plano,
  `bloqueado`/`parcial` em prosa — ficaram intactas, como o dossiê classificou. `CHANGELOG.md`:
  entrada nova no topo de `## [Não lançado]`, entradas históricas não reescritas. Os **dois índices
  não mudaram, com motivo medido**: `docs/DOC_MAP.md` só indexa doc acima de 500 linhas e a
  residência tem 232, de modo que indexá-la contradiria a regra do próprio mapa (o ponteiro já vive
  no `README.md` §7); `docs/RESIDENCIA_DOUTRINA.md` reconcilia as Regras 1-8 do `CLAUDE.md` global
  contra o kit e não tem entrada de residência de vocabulário — criar uma seria doutrina nascendo
  fora da residência. Desvio declarado no grep de aceite: `in progress` sobrevive **1** vez, em
  `CHANGELOG.md:22`, dentro da entrada que descreve a própria migração — registro histórico, que é
  onde o critério de pronto admite o termo. Verificação (bateria do §3 item 6, os quatro em **exit
  0**): `kit_check -Mode validate` → *8 agente(s) e 11 skill(s); VERSION == KIT_VERSION ('0.0.0')*;
  `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s),
  versão '0.0.0', 14 seção(ões) com Fonte da verdade válida* (as duas contagens preservadas);
  `python -m pytest` → **39 passed** (piso 39 × 39 — a tarefa não toca código). Consumo **24 tool
  uses** contra teto 30 da classe `redacao`. **Um achado fora de escopo**, indexado como segunda
  ocorrência do `TK-30` e sem tíquete novo: na residência única, `superseded` aparece na tabela
  `### Alcance por objeto` mas está ausente da `### Lista final` e da `### Máquina de transições` —
  o único estado terminal de plano não tem gatilho de entrada na fonte da verdade. Rodada fechada
  pelo orquestrador: o executor sinalizou `review` e não tocou diário, `handover` nem telemetria.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T45` — `TK-39`: o critério de aceitação deixa de ser contagem — `done`.** O §19 do
  `P-0734` parou de aprovar a entrega por número de acionamentos do gerente e passou a classificar
  cada acionamento **pela causa**. `docs/plans/P-0734-execucao-autonoma.md`: no **§19** saiu o
  bloco-andaime que anunciava esta própria tarefa, saiu a frase *"round-trip de despacho é
  reprovação"* e entrou o bloco **"A aceitação classifica cada acionamento pela causa"**, com os
  dois ramos — causa que é do gerente (dirimir ambiguidade, conflito de requisito ou de aceitação)
  é legítima e **ilimitada**, e o risco fatal declarado é o agente decidir aceitação sem estar
  inequivocamente seguro; acionamento em **caminho feliz ou natural** é ineficiência da entrega, e
  **uma só ocorrência** basta, sem franquia — mais o ponteiro para `GOVERNANCA.md` §4.3 e §3.1
  item 3. Na **`T16`** a medida "quantos round-trips o dono precisou dar" saiu da lista, entrou o
  registro **qualitativo, por ocorrência**, e a cláusula de aceitação com o "Pronto quando" passaram
  a classificar por causa. A **`T17`** não precisou de edição: o veredito já referenciava o §19 sem
  contagem. `GOVERNANCA.md` §4.3 recebeu o bullet **"Acionamento do dono — a causa decide"**, entre
  a sinalização de fechamento e a retomada sem tarefa nomeada, com o gancho para §3.1 item 3; a
  skill `scrum-master` recebeu, na seção "O que obriga parada e o que segue com registro", o bullet
  **"Parada defeituosa"** (despachar, criar contexto e distribuir handover são execução normal do
  loop) e o parágrafo "Parada legítima não tem teto", que separa escalada de ocupação de janela
  (`B2`). Verificação (bateria do §3 item 6, os quatro em **exit 0**): `kit_check -Mode validate` →
  *8 agente(s) e 11 skill(s); VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida* (as duas contagens preservadas, nenhum guardrail novo);
  `python -m pytest` → **39 passed** (piso 39 × 39 — a tarefa não toca código). Grep de aceite: as
  ocorrências remanescentes de `round-trip` são exatamente as declaradas fora do alvo — origem e
  custo, batching de decisão, ratificações ocorridas, tabela de riscos e dimensionamento de janela.
  `README.md` não tocado, por invariante do dossiê: a consolidação do espelho é da `T17`. Consumo
  **17 tool uses** contra teto 25 da classe `redacao` (âncora do §19 re-derivada pelo orquestrador
  antes da delegação: o dossiê apontava `:3652-3673`, vencido em ~57 linhas, e a seção estava em
  `:3709-3745`). **Um achado fora de escopo**, aberto como **`TK-40`**: a tabela de riscos do §6
  (`:2000`) ainda promete que a `T16` "mede quantos round-trips de fato desapareceram" — mitigação
  viva, incoerente com a `T16` reescrita, e fora do recorte que o dossiê declarou intocável. Rodada
  fechada pelo orquestrador: o executor sinalizou `review` e não tocou diário, `handover` nem
  telemetria. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T46` — doutrina: guardrail 16 (`G-SURFACE`) e o espelho em lockstep — `done`.** A golden
  rule enunciada pelo dono virou guardrail nomeado: **mudança de decisão estruturante regulariza a
  superfície de contato inteira, no ato**. O gatilho é a decisão que altera o que o trabalho *é* —
  objetivo-chave, requisito ou caso de uso —, e refinar redação, corrigir número ou trocar âncora
  **não** dispara a regra. `GOVERNANCA.md` §7 recebeu o item **16** entre o `G-SCOPE` e o parágrafo
  de materialização; o `README.md` §10 recebeu a linha 16 da tabela, mais duas correções de
  consistência na mesma seção que a linha nova tornaria falsas (a abertura, de *Quinze* para
  *Dezesseis*, e a contagem das formas de enforcement, de *oito* para *nove* dependentes de gate).
  *Enforcement* declarado: gate de planejamento — a rodada que fecha a decisão estruturante emite os
  cards de regularização no mesmo ato, e a fila não avança sem eles — somado ao gate de review.
  `check-readme.ps1` **não** foi tocado: ele conta guardrail dinamicamente, e o espelho fechou em
  **16 × 16** só por as duas listas crescerem juntas. Verificação (bateria do §3 item 6, os quatro em
  **exit 0**): `kit_check -Mode validate`; `-Mode check-drift`; `check-readme.ps1` → *16
  guardrail(s), 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed**.
  Consumo **12 tool uses** contra teto 25 da classe `redacao`. Achado fora de escopo roteado para a
  `T48`: o `CHANGELOG.md` registrava a subida 14 → 15 e não tinha a entrada do 15 → 16. Rodada
  fechada pelo orquestrador. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T47` — consolidação, universo 1: o plano `P-0734` — `done`.** **17 ocorrências
  classificadas: 9 de classe (a), 6 de classe (b) regularizadas e 2 de classe (c) que subiram ao
  dono.** Método prescrito cumprido — sonda programática via scratchpad sobre as 3.928 linhas
  (mapa de seções, índice dos 48 cards e frequência de todo `DP-*`/`DA-*`/`DE-*`), depois leitura
  dirigida; o Grep cru do índice de decisões estourou 35 KB numa chamada e foi descartado em favor
  da sonda. Recorte de vigência aplicado e declarado: **dossiê de tarefa já executada é história**
  (é a encomenda da época), de modo que só entraram em (b) os dossiês não executados, os §1-§3, as
  mitigações do §6, o §7/§8, o §19 e o bloco `## Dossiês fechados por decisão`. As seis edições:
  **b1** quita o `TK-40` (a mitigação de risco da consciência situacional passa a se apoiar no
  registro qualitativo por ocorrência classificado pela causa, com o RDO mantido como instrumento
  compensatório da `DA-5`, sem reintroduzir contagem); **b2** e **b3** marcam a revogação parcial da
  `DP-A` e da `DP-B` no topo de cada dossiê, com o corpo intocado, dizendo o que permanece e o que
  caiu; **b4** e **b5** dão ao §9 o ponteiro da revogação da `DP-D` pela `DP-E`, que morava ~270
  linhas adiante sem marca na âncora; **b6** conserta um invariante da `T27` que enumerava
  `DP-A..DP-F` como lista fechada sete rodadas atrás — executada assim, a `T27` reescreveria
  registro. Verificação (bateria do §3 item 6, os quatro em **exit 0**): `check-readme.ps1` → *16
  guardrail(s), 14 seção(ões)*; `python -m pytest` → **39 passed**. Consumo **28 tool uses** contra
  teto 40 da classe `redacao`. Rodada fechada pelo orquestrador. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T48` — consolidação, universo 2: os artefatos publicados — `done`.** **28 ocorrências
  classificadas: 12 de classe (a), 13 de classe (b) regularizadas e 3 de classe (c), todas
  herdadas — nenhuma nova.** Duas medições fecharam em zero e valem como invariante conferido:
  nenhuma ocorrência viva de *revisor*/*inspetor* (`DP-H`, termo único) e nenhuma de
  `--observacoes` (`DP-M`). As edições, por arquivo: `CHANGELOG.md` ganhou a entrada 15 → 16 na
  série das subidas de guardrail, sem bump (`DE-7`); `GOVERNANCA.md` §4.2 trocou a lista morta de
  `status` (`backlog`, `in progress`, `in review`) por ponteiro à residência única, e os itens 8 e 9
  do §7 perderam o handover morto das cláusulas de *Enforcement*; `README.md` acompanhou nas linhas
  8 e 9 do espelho e reescreveu o ciclo ponta a ponta do §11, que ainda publicava *"o handover
  fecha; o gerente limpa o contexto e invoca a próxima"* — exatamente o acionamento de caminho feliz
  que o §19 reprova; `.claude/README.md` corrigiu a mesma prosa de ciclo, fora da região gerada;
  a skill `scrum-master` trocou "a rota é escrita pela execução no RDO" pelo caminho vigente (chega
  pelo laudo ou pela linha de achado do sinal, e quem fecha transcreve); e `review_evidence.py`
  perdeu as três menções vivas ao objeto morto *pacote de retorno* — docstring do módulo, docstring
  de `confrontar_escopo` e a string do veredito impressa no documento que o `reviewer` lê —, com
  mudança textual e comportamento intocado. Eixo declarado: esta varredura mede contra os
  **objetivos vigentes**, não contra a matriz de responsabilidades, que já foi varrida em 2026-08-12
  pelas `T43`/`T44`. Verificação (bateria do §3 item 6, os quatro em **exit 0**), com
  `check-drift` verde depois da edição de skill: `check-readme.ps1` → *16 guardrail(s), 14
  seção(ões)*; `python -m pytest` → **39 passed**. Consumo **46 tool uses** contra teto 40 da classe
  `redacao` — estouro de 6, registrado sem interromper a entrega (regime interino do §3 item 5); o
  sinal é de universo amplo (9 famílias de artefato), não de método ruim. Dois achados fora do
  universo declarado, indexados como **`TK-42`**. Relatório único das duas metades:
  `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`. Rodada fechada pelo orquestrador. Consumo:
  ver `docs/telemetria.tsv`.

- **`EXA-T49` — a régua na doutrina: número arbitrário não governa fluxo — `done`.**
  `GOVERNANCA.md` §3: a tabela de tetos por classe permanece com todos os números, mas passa a ser
  declarada **referência informativa de dimensionamento, nunca gate** — não recusa entrega, não
  roteia, não encerra tarefa nem janela; caiu *"estourar o teto da classe é sinal de decomposição
  errada — replanejar, não continuar"* e entrou *"cruzar o número é alarme, nunca bloqueio"*. A
  residência do qualitativo foi nomeada ali: card **"Lições aprendidas na tarefa"** do laudo,
  preenchido quando houver o que observar; sem observação, o número isolado se desconsidera. §4.3:
  caiu a **cláusula-vício** — *"enquanto não houver proxy de ocupação disponível ao agente, o proxy
  operante é o teto de tool uses por classe"* —, e o encerramento passou a se apoiar em **coesão** e
  **capacidade**, com a medida de ocupação como instrumento e, enquanto ela não existir, a coesão e
  o fim do plano. Uma edição além das âncoras nomeadas, dentro da mesma régua: o gatilho de
  checkpoint intermediário deixou de ser *"2/3 do teto da classe"* e virou qualitativo — mantê-lo
  ressuscitaria o teto como operante logo abaixo da cláusula que o desautoriza. `README.md`
  espelhado nas 15 ocorrências varridas, com 9 preservadas por não atribuírem poder de porteiro. No
  plano, o §3 item 5 deixou de ser "regime interino" e virou o **regime deste plano**, e o topo do
  `### DP-B` recebeu marca de revogação parcial com corpo intocado. Verificação: os quatro em **exit
  0**, *16 guardrail(s), 14 seção(ões)*, **39 passed**; Grep de fecho com zero ocorrências de
  `proxy operante`, `2/3 do teto` e `replanejar, não continuar`. Consumo **38 tool uses**. Consumo:
  ver `docs/telemetria.tsv`.

- **`EXA-T50` — a regra no loop: `A4` e `B2` deixam de rotear por número — `done`.** Na skill
  `scrum-master`, a linha **`A4`** saiu da tabela do bloco A (mesmo precedente da queda de `A5` pela
  `DP-G`: sem renumeração, a lacuna fica), substituída por prosa que declara o consumo **alarme,
  nunca bloqueio** e o encaminha para a série e para o card de lições aprendidas. **`B2`** perdeu os
  dois números que o dono nomeou como vício — dez tarefas fechadas, 900 k tokens acumulados — e
  passou a medir as duas condições do §4.3, com a ressalva de que, enquanto não existir medida de
  ocupação, valem a coesão e o fim do plano. A lista "Obriga parada" perdeu os dois itens de teto e
  **manteve íntegras** as paradas de causa (`pendencia=`/`escalar`, `A3b`, `A7`, `B3`). A tabela de
  contadores trocou a coluna `teto` por `para que serve`, e a `description` do frontmatter, que
  dizia *"encerra a janela por teto numérico"*, passou a *"por coesão e ocupação de contexto"* — era
  o vício afirmado na própria superfície do alvo. Nove ocorrências de `teto` permaneceram, cada uma
  com motivo declarado, e nenhuma governa rota ou encerramento. Verificação: os quatro em **exit 0**,
  **39 passed**. Consumo **36 tool uses**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T51a` — sanitização, o instrumento: o gerador para de decidir por consumo — `done`.** Em
  `.claude/tools/rdo.py`, `calcular_desdobramento` perdeu o parâmetro `orcamento_estourado` e o ramo
  `if orcamento_estourado: return "estouro"`; a linha `orcamento_estourado = args.tool_uses >
  dossie.teto` saiu. Os campos `TETO`/`TOOL_USES`/`TOKENS_K`/`DURACAO_S` seguem medidos, transcritos
  e impressos — a medição é o que a decisão preserva. **Achado que encolheu a superfície:** as 21
  ocorrências de `teto` em `review_evidence.py` são todas `teto_chars`/`teto_diff_chars`,
  truncamento de string, e não consumo — o arquivo não precisou de edição, nem o `rdo_template.md`.
  O teste que provava o gate foi **reescrito**, não apagado: agora fecha um RDO real com
  `--tool-uses 41` contra teto 40 e prova que o desdobramento continua `aprovado`, que os números
  aparecem no documento e que a palavra `estouro` não aparece em lugar nenhum. Verificação: os
  quatro em **exit 0**, **39 passed**. Consumo **26 tool uses**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T51b` — sanitização, a descrição: prompts, índices e a marca da `DA-11` — `done`.** **27
  ocorrências classificadas: 18 de classe (b), 9 de classe (a), nenhuma (c) nova.** O
  `pantonic-executor` perdeu o *"orçamento esperado ~≤40 tool uses … sinalizar ao scrum-master"* (o
  número roteava); o `pantonic-reviewer` ganhou a proibição de pontuar, reprovar ou escalar por
  consumo, mais o card de lições aprendidas nomeado como residência **discricionária**; a
  `RUBRICA_DE_REVISAO.md` passou a medir **existência e procedência** do registro de consumo, nunca
  a grandeza; a `RESIDENCIA_DOUTRINA.md` trocou *"estourar = replanejar, não continuar"* por
  referência informativa. No plano, marca de revogação parcial na **`DA-11`** e no topo do card
  `T6b`, corpo intocado nos dois. Nove famílias de ocorrências de `teto` permaneceram com motivo
  declarado — teto de **retentativa** (parada de causa, íntegra por desenho), limite de **tamanho de
  campo**, e transcrição de medida. Terceiro bloco do relatório acrescentado sem tocar os dois
  existentes. Verificação: os quatro em **exit 0**, **39 passed**. Consumo **48 tool uses**.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T52` — fecho do bloco `DP-Q`: o gatilho residual e a residência não materializada —
  `done`.** Card emitido pelo orquestrador a partir de dois resíduos vivos que a `T51b` mediu — o
  `G-SURFACE` proíbe enfileirar como dívida o que a decisão estruturante atingiu. **Parte 1:** o
  gatilho de checkpoint do `handover` foi conferido contra o §4.3 já reescrito e está transcrito
  como sinal qualitativo, sem número; o teto de 2 tool uses do próprio checkpoint e o limite de 5
  linhas permanecem, por serem prescrição de esforço do artefato. **Parte 2:** o card **"Lições
  aprendidas na tarefa"** deixou de ser residência nomeada e não materializada — `rdo.py` ganhou
  `--licoes-aprendidas` opcional em `laudo` e em `close`, e o `rdo_template.md` ganhou a seção com
  `{{LICOES_APRENDIDAS}}` entre `## Laudo` e `## Fechamento`. **Discricionário por desenho:** vazio
  é estado legítimo, sem campo obrigatório e sem validação que reprove ausência — quatro testes
  novos provam as duas metades (preenchido e vazio, em `laudo` e em `close`). Fronteira respeitada:
  materializa a residência que a `DP-Q` item 3 fixou, e **não** decide o que o `scrum-master` colhe
  do laudo, que segue com a `T30`. Verificação: os quatro em **exit 0**; **piso subiu de 39 para
  43**. Consumo **52 tool uses**. Consumo: ver `docs/telemetria.tsv`.

**Bloco da `DP-Q` encerrado em 2026-08-13** (bullets de fechamento acima) — **número arbitrário
deixou de governar fluxo em todo o framework**. A decisão do dono fechou o `TK-41` pelo mesmo
princípio nos dois itens: teto de tarefa e teto de janela são a mesma questão do limite de
round-trips, números que ninguém deriva de nada e que só geram ruído, e ação baseada em ruído é
decisão equivocada. Caíram, nominalmente, o roteamento por estouro (`A4`), os dois números de fim de
janela (`B2`), a cláusula que elegia o teto de tool uses como proxy operante de capacidade, o
gatilho de checkpoint por 2/3 do teto e a ramificação por consumo no gerador de RDO. **O que ficou
intacto por desenho:** a medição — a série `docs/telemetria.tsv` continua alimentada sem exceção,
porque é o **agregado** que a decisão declara ter valor — e toda parada de **causa**, com escalada
por ambiguidade ou conflito de requisito e de aceitação seguindo **ilimitada**. A matéria de limites
**não foi doutrinada aqui**: ela se revê inteira no plano próprio já previsto (desdobramento da
`T17` item 4), e nenhum número novo entrou no lugar dos que caíram. Consequência declarada e aceita:
até a `T13` entregar a medida de ocupação, o encerramento de janela se apoia só em coesão e no fim
do plano — por isso a `T13` saiu do fim da fila e passou a suceder o bloco. **Próxima tarefa:**
**`EXA-T13`** — proxy de ocupação de contexto. Fila registrada: **`T13`** → `T29` → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T14` → `T15` → `T16` → `T17`
(dono).

**Bloco da `DP-P` encerrado em 2026-08-13** (bullets de fechamento acima) — **a golden rule do dono
virou guardrail e a superfície de contato foi regularizada nos dois universos**. A régua (`T46`) foi
publicada antes da varredura, o plano (`T47`) passou a enunciar o entendimento vigente uma vez só
com o texto derrubado marcado como derrubado, e os artefatos publicados (`T48`) deixaram de ensinar
o entendimento antigo — em particular o `README.md`, que descrevia como ciclo normal o gerente
limpar o contexto e invocar a próxima tarefa, que é o caso exemplar de ineficiência do §19. O
`TK-40` foi quitado dentro da `T47`. **Duas ocorrências de classe (c) pararam e subiram ao dono,
indexadas como `TK-41`** — a `DP-B` prescreve paradas (`A4`, estouro de teto; `B2`, fim de janela)
que o §19 pode classificar como acionamento em caminho feliz; nenhum dos dois textos foi tocado, e a
decisão muda o que a `T16` mede e o que a `T17` aprova. **Próxima tarefa:** a decisão do `TK-41` é o
próximo passo — enquanto ela não fecha, `T29` e `T30` seguem delegáveis (matéria disjunta), mas a
`T16` e a `T17` não. Fila registrada: [decisão do dono: `TK-41`] → **`T29`** → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T13` → `T14` → `T15` → `T16` →
`T17` (dono).

**`EXA-T45` fechada** (bullet de fechamento acima) — **a aceitação do plano deixou de ser um número
e passou a ser uma classificação por causa**. Com ela, o `TK-39` está quitado na superfície que
declarou (o §19, a `T16`, a `T17`, a doutrina em `GOVERNANCA.md` §4.3 e a skill que conduz o loop),
e a `T16` (piloto) e a `T17` (veredito) passam a aferir o critério certo. **Próxima tarefa:**
**`EXA-T29`** — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T29` (artefato `tarefa`:
definição, autores e canal). Em **contexto novo**. Fila registrada: **`T29`** → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T13` → `T14` → `T15` → `T16` →
`T17` (dono).

**`EXA-T25` fechada** (bullet de fechamento acima) — **o espelho e os índices falam a lista final e
apontam para a residência, sem recopiá-la**. Com ela, a conformidade de vocabulário da `DP-F` cobre
as duas skills do kanban (`T23a`/`T23b`), o restante do kit executável (`T24`) e agora a porta de
entrada; sobram a doutrina normativa (`T26`) e o kanban mais os planos vivos (`T27`), que a fila já
posiciona depois da ratificação em lote.

**Fila reordenada em 2026-08-13 por decisão do dono** — entra o card prioritário **`EXA-T45`**
(`TK-39`), à frente da `T29`: o §19 (critério de aceitação final) foi autorado no mesmo dia apoiado
em **contagem de round-trips**, e o dono derrubou a contagem como conceito de aceitação. Enquanto o
critério estiver escrito como número, a `T16` (piloto) e a `T17` (veredito) aferem a coisa errada, e
é a aceitação da entrega final que fica em risco — por isso o card para a fila em vez de entrar no
fim dela. **Próxima tarefa:** **`EXA-T45`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T45` (o critério de aceitação deixa de ser contagem e
passa a classificar cada acionamento do gerente **pela causa**). Em **contexto novo**. Fila
registrada: **`T45`** → `T29` → `T30` → [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` →
`T12` → `T13` → `T14` → `T15` → `T16` → `T17` (dono).

**`EXA-T44` fechada** (bullet de fechamento acima) — **doutrina, espelho e índices só atribuem o que
a matriz endossa; o que sobrou é lacuna declarada da matriz, não improviso**. Com ela encerra o bloco
de três cards da `DP-O` (`T42`..`T44`): a régua foi publicada, o kit executável e a doutrina foram
varridos contra ela, e as duas ocorrências de classe (c) apontam para a mesma lacuna, já encaminhada
ao `TK-36`. **Próxima tarefa:** **`EXA-T25`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T25` (conformidade de **espelho e índices**: o
vocabulário de `status` da `DP-F` no `README.md` e nos índices); destravada agora, e a ordem já foi
justificada no §5 — a `T44` precede a `T25` porque as duas passam pelo mesmo `README.md`, e inverter
faria a conformidade de vocabulário rodar sobre texto que a sanitização ainda ia reescrever. Em
**contexto novo**. Fila registrada: **`T25`** → `T29` → `T30` → [ratificação em lote: `DP-I` e
`DP-J`] → `T26` → `T27` → `T12` → `T13` → `T14` → `T15` → `T16` → `T17` (dono).

**`EXA-T43` fechada** (bullet de fechamento acima) — **nenhum prompt do kit atribui mais ato que a
matriz não endossa; o que não coube nela virou `TK-37`, não improviso**. **Próxima tarefa:**
**`EXA-T44`** — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T44` (sanitização da
**doutrina, do espelho e dos índices** contra a matriz: `GOVERNANCA.md`, `README.md`,
`ARQUITETURA_PANTONICA.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/RESIDENCIA_DOUTRINA.md`,
`docs/DOC_MAP.md`); destravada agora, por depender da `T43` `done`, e com metade das âncoras já no
relatório de conformidade, cuja §2 recebe as linhas novas. Em **contexto novo**. Fila registrada:
**`T44`** → `T25` → `T29` → `T30` → [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27`. **A `T34`
saiu da fila em 2026-08-12**, cancelada por absorção: a matéria de uso e teto se revê inteira, em
plano próprio, aberto depois deste, e o desdobramento é o item 4 da `T17`.

**`EXA-T42` fechada** (bullet de fechamento acima) — **o `G-SCOPE` agora responde também pelo que já
está escrito: não-conformidade encontrada para e regulariza, e lacuna da matriz sobe ao dono**. A
régua que a `T43` e a `T44` aplicam está publicada. **Próxima tarefa:** **`EXA-T43`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T43` (sanitização do **kit executável** contra a
matriz de responsabilidades); destravada agora, por depender da `T42` `done`, e precede a `T44`
porque a doutrina descreve o kit e o relatório dela já traz metade das âncoras da seguinte. Em
**contexto novo**. Fila registrada: **`T43`** → `T44` → `T25` → `T29` → `T30` → `T34` →
[ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T41` fechada** (bullet de fechamento acima) — **doutrina, espelho e a skill que delega não
mandam mais o executor escrever**. **Próxima tarefa:** **`EXA-T42`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T42` (o guardrail 15 passa a dizer o que se faz quando
a não-conformidade de escopo é encontrada em artefato existente); precede a `T43` e a `T44`, que
aplicam a régua. Em **contexto novo**. Fila registrada: **`T42`** → `T43` → `T44` → `T25` → `T29` →
`T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T40` fechada** (bullet de fechamento acima) — **o prompt do executor não manda escrever em
lugar nenhum: ele entrega tecnicamente correto e sinaliza `review` ou `blocked`**. O `TK-35` está
`done`. **Próxima tarefa:** **`EXA-T41`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T41` (as superfícies que descrevem o executor:
doutrina, espelho e a skill que delega param de mandar o executor escrever); destravada agora, por
depender da `T40` `done`. Em **contexto novo**. Fila registrada: **`T41`** → `T42` → `T43` → `T44` →
`T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T24` fechada** (bullet de fechamento acima) — **o kit executável não cita mais vocabulário
morto de `status`; o que sobrou de `backlog` é substantivo ou região gerada**. O achado dela abriu o
`TK-35` e, com ele, a rodada da **`DP-N`** (§17 do plano), ratificada pelo dono no mesmo dia: o
executor sinaliza e nada mais, a coleta do entregável é do `reviewer`, e a passagem de bastão vira
o `TK-36`. **Próxima tarefa:** **`EXA-T40`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T40` (o prompt do executor: sete pontos, arquivo
único). Em **contexto novo**. Fila registrada: **`T40`** → `T41` → `T42` → `T43` → `T44` → `T25` →
`T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T23b` fechada** (bullet de fechamento acima) — **a skill que consome o kanban fala a lista
final e aponta para a residência, sem reenunciá-la; o `blocked` da `DP-G` está quitado**. **Próxima
tarefa:** **`EXA-T24`** — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T24` (conformidade
do restante do kit executável: seis arquivos, contagem medida em 2026-08-11). Em **contexto novo**.
Fila registrada: **`T24`** → `T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`,
`DP-L`] → `T26` → `T27`.

**`EXA-T39` fechada** (bullet de fechamento acima) — **as três referências órfãs do `TK-33` estão
reconciliadas e a proibição que a `DP-M` dispensa saiu; o `TK-33` está `done`**. Com ela encerra o
bloco de cinco cards da `DP-M` (`T35`..`T39`). **Próxima tarefa:** **`EXA-T23b`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T23b`. Em **contexto novo**. Fila registrada:
**`T23b`** → `T24` → `T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`]
→ `T26` → `T27`.

**`EXA-T37` fechada** (bullet de fechamento acima) — **os dois blocos `## Proibições` só contêm
fronteira interna do próprio papel; nenhuma proibição do tipo "não faça o que é de outro papel"
sobrevive neles**.

**`EXA-T38` fechada** (bullet de fechamento acima) — **o gerador de laudo rejeita `--observacoes`;
o laudo emitido não tem prosa livre além da linha de pendência**. **Próxima tarefa:** **`EXA-T39`**
— dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T39`. Em **contexto novo**. Fila
registrada: **`T39`** → `T23b` → `T24` → `T25` → `T29` → `T30` → `T34` → [ratificação] → `T26` →
`T27`.

**`EXA-T36` fechada** (bullet de fechamento acima) — **a golden rule `G-SCOPE` existe na doutrina
publicada como guardrail 15, com o espelho em lockstep (15 × 15)**. **Próxima tarefa:** **`EXA-T37`**
— dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T37` (poda das proibições que a matriz
passa a derivar: 4 das 6 do `scrum-master`, 5 das 7 do `pantonic-reviewer`). Em **contexto novo**.
Fila registrada: **`T37` → `T38` → `T39`** → `T23b` → `T24` → `T25` → `T29` → `T30` → `T34` →
[ratificação] → `T26` → `T27` (fila da rodada de replanejamento da `DP-M`).

**`DP-M` ratificada pelo dono em 2026-08-11 — a golden rule de escopo de agente e o laudo mínimo.**
Enunciado do dono: o problema nunca foi proibir o `scrum-master` de ler o corpo do laudo — foi o
laudo ter corpo. O laudo se padroniza por função, como o RDO, e passa a ser **mínimo e suficiente**;
e no lugar de coibir papel a papel, vale uma **golden rule** para todo agente — *o agente se atém
estritamente às suas responsabilidades declaradas; o que não é escrito é proibido*. Escopo:
**conceito do framework**, não desenvolvimento dele (`DP-H`) — a regra entra em doutrina publicada,
e o plano carrega só as tarefas. Duas escolhas levadas ao dono e ratificadas: (1) a regra mora em
`GOVERNANCA.md` §7 como **guardrail 15**, com a §3 (matriz de responsabilidades) apontando para ela
— o espelho `README.md` §10 sobe para 15 linhas em lockstep, que é o que `check-readme.ps1` compara;
(2) `--observacoes` **sai** do gerador de laudo, assumido o risco de a marcação abaixo de `conforme`
ficar sem justificativa registrada.

Estado medido nesta rodada, que a rodada de replanejamento não precisa remedir: o laudo já é gerado
por função (`.claude/tools/rdo.py:481-492`), com 6 dos 8 campos fechados ou calculados; só
`Pendência` (uma linha, consumida por `B1`) e `Observações` (texto livre, sem limite, **sem
consumidor** — fora dos cinco campos do pacote) são prosa. `GOVERNANCA.md:104` já declara a matriz
como residência única do escopo de cada papel, mas **não existe** a cláusula de fechamento — nada diz
hoje que o não escrito é proibido. Sob a regra nova a matriz vira autoridade exaustiva, então
**auditar a matriz por completude é precondição**: sem isso todo agente nasce fora de conformidade.
A regra devolve linhas: 4 das 6 proibições do `scrum-master` (`:273`) e 5 das 7 do `pantonic-reviewer`
(`:83`) são do tipo "não faça o que é de outro papel" e passam a derivar da matriz. O `TK-33` item 3
(a proibição *"Não abre o RDO nem o laudo"* contra o passo 9) fica **decidido pela `DP-M`**: a
proibição some sem fronteira substituta, porque com `Observações` fora não sobra no laudo nada que o
`scrum-master` possa extrapolar lendo; os itens 1 e 2 continuam mecânicos.

**Rodada de replanejamento da `DP-M` — executada em 2026-08-11.** Autorada a seção `## 16` do
`docs/plans/P-0734-execucao-autonoma.md` (`16.1` enunciado, `16.2` as duas escolhas ratificadas,
`16.3` estado medido, `16.4` critério de sobrevivência de proibição + fechamento do `TK-33`, `16.5`
o que a `DP-M` não decide, `16.6` cards e fila; `16.7` reservada ao resultado que a `T35` escreve).
Cinco tarefas novas no §4: **`T35`** auditoria de completude da matriz de responsabilidades
[Opus · investigacao · 30], **`T36`** guardrail 15 (`G-SCOPE`) + espelho `README.md` §10 em lockstep
[Opus · redacao · 30], **`T37`** poda das proibições que a matriz passa a derivar
[Opus · redacao · 15], **`T38`** `--observacoes` sai do gerador de laudo [Sonnet · mecanica · 15] e
**`T39`** `TK-33` (passos 7 e 8, acepção de `pacote` em `A2`, proibição dispensada pela `DP-M`)
[Opus · redacao · 15]. Dois pontos fechados por derivação, sem decisão nova do dono: o **critério de
poda** (sobrevive só a proibição que restringe a própria responsabilidade) e o **`TK-33` item 2**
(a `recomendacao` é campo fechado do laudo e o passo 7 a colhe de lá — recusada a ampliação do
retorno do `reviewer`). Número de aceite re-derivado na rodada: `check-readme.ps1` compara
contagem (`| N |` do README × `^\d+\. \*\*` de `GOVERNANCA.md` §7), hoje **14 × 14** → **15 × 15**.
Fila reposicionada no §5 e linha do `TK-33` atualizada na tabela de tíquetes. A fila retoma pela
`T33`. Consumo: ver `docs/telemetria.tsv`.

**Regime interino de teto — decisão do dono, 2026-08-11 (`TK-32`); prorrogado em 2026-08-12.** O teto
do cabeçalho de cada tarefa é **alarme, nunca bloqueio**: nenhuma tarefa para, é impedida ou fica
incompleta por cruzar o número, e quem delega **não escreve cláusula de parada dura por teto** no
dossiê de delegação. A medição continua obrigatória em `docs/telemetria.tsv` — é a série que decide.
**A `DP-L` não se forma no `P-0734`:** a `EXA-T34` foi cancelada por absorção e a matéria de uso e
teto se revê inteira, em plano próprio, aberto depois deste (desdobramento na `T17`, item 4). O regime
vigora até aquela decisão. Materializado em `docs/plans/P-0734-execucao-autonoma.md` §3, item 5.

**Depois da `T20`:** `T31` → `T32` (desempate do framework no `GOVERNANCA.md` §3.1;
independente, não para) → `T21a` → `T21b` (o loop passa a existir) → `T33` (`reviewer` nas linhas
espelhadas) → `T23b` sai de `blocked` e é concluída → `T24` → `T25` → `T29` → `T30` → `T34` (uso e
teto como medida agregada; decide e para) → [ratificação em lote de `DP-I`, `DP-J` e `DP-L`, único
ponto de parada dura da fila] → `T26` → `T27`.

- **`EXA-T19` — `rdo.py`: o RDO se gera no fechamento — `done`.** `close` passa a materializar o
  RDO inteiro numa única chamada (CLI: `--plano --tarefa --tool-uses --tokens-k --duracao-s
  --veredito --percentual --bloqueante --recomendacao --pendencia-laudo [--pendencia] [--rdo-dir]
  [--template] [--esquema-legado --modelo --classe --teto]`), transcrevendo o `pacote` do laudo e o
  consumo medido por argumento — nenhuma leitura de arquivo de laudo sobrevive. Morrem `cmd_new`, o
  subparser `new`, `_CAMPOS_PACOTE_ORDEM`, `_TETO_CAMPO_PACOTE`, `_STATUS_VALIDOS`,
  `_FECHAMENTO_MARCADOR_RE`, `_EXECUCAO_CAMPO_VAZIO_RE`, `_ORCAMENTO_RE`, `_LAUDO_VEREDITO_RE` e
  `_LAUDO_BLOQUEANTE_RE` (sem consumidor vivo, confirmado por `dead_code.py` em exit 0).
  `calcular_desdobramento` encolhe para `(veredito, orcamento_estourado)`, dois ramos com
  precedência do estouro — fecha o `TK-29`. Template ganha `## Fechamento` e perde os oito bullets
  do pacote antigo e `{{LAUDO_PATH}}` (laudo é descartado pelo `scrum-master`, `DP-H`).
  `extrair_dossie` preservada (`review_evidence.py` reusa). RDOs de `T1`..`T10` e o RDO existente
  (`T11`) não tocados.
  Notas de execução:
  Arquivos: `.claude/tools/rdo.py` (reescrito), `.claude/tools/rdo_template.md` (reescrito),
    `tests/test_rdo.py` (reescrito: testes do `new` saem, 18 testes novos de `close` entram, os 6
    de `laudo` preservados intactos).
  Veredito — `EXA-T19`
  Suítes: `python -m pytest tests/test_rdo.py -q` — 23 passed; `python -m pytest -q` (suíte
    inteira) — 39 passed. `tests/conformance/` inexistente no hub (script CLI fora da árvore
    infracore/contracts/services/plugins, sem direção de camada a checar).
  Piso: `ratchet_piso.py` — OK (sem piso declarado em `tests/piso_comportamental.txt`).
  Kit: `kit_check.ps1 -Mode validate`/`-Mode check-drift` — exit 0 (8 agentes, 11 skills,
    VERSION==KIT_VERSION '0.0.0').
  Espelho: `check-readme.ps1` — exit 0 (8 agentes, 11 skills, 14 guardrails, 14 seções com Fonte
    da verdade).
  Código morto: `dead_code.py` — exit 0 (0 achados; confirma a lista de símbolos mortos acima).
  Checklist de review: ok — script CLI fora da árvore infracore/contracts/services/plugins; sem
    dependência externa nova; sem trabalho pesado em thread de entrada; sem tipo cruzando camada;
    teste com significado alterado foi reescrito, não deletado (suíte de `new` removida porque o
    comportamento morreu, não por conveniência); mudança comportamental amparada por `DP-H`/`T19`
    (ratificados) e `TK-29` (fecha aqui).
  Consumo: ver `docs/telemetria.tsv` (41 tool uses contra teto rígido 40 — estouro de 1).

- **`EXA-T20` — `pantonic-reviewer`: o revisor sem pacote — `done`.** As três entradas do
  julgamento passam a ser dossiê da tarefa + dossiê de evidência + diff, e `pacote de retorno`
  some do arquivo (0 ocorrências): o passo 2 do protocolo deixa de ler narrativa do executor e
  passa a ler a evidência mecânica; o passo 3 passa a ser o diff. O `pacote` sobrevive na acepção
  vigente — os cinco campos obrigatórios **dentro do laudo** (veredito, percentual, bloqueante,
  recomendação, pendência), com a suficiência declarada nos fatos estáveis, mais a cláusula de que
  o laudo é consumido e descartado (não é residência durável nem completa juízo por remissão). A
  saída ganha as duas linhas fixas de veredito (`<tarefa> <veredito> <percentual>
  bloqueante=<dimensão|nenhuma>` + `laudo=<caminho>`) e uma proibição nova: não declara `status` —
  nem autora, nem materializa, nem usa o vocabulário. O bloco de CLI, que documentava `--rdo` e
  `--recomendacoes` (nenhum dos dois existe no `rdo.py` vigente), passa à assinatura viva
  (`--plano --tarefa [--laudos-dir]`, sete flags de dimensão, `--vermelho-mecanico`,
  `--observacoes`, `--escalar`), com `--escalar` nomeado como o único canal de pendência do
  revisor e a recomendação declarada calculada.
  Notas de execução:
  Arquivos: `.claude/agents/pantonic-reviewer.md` (5 `Edit`s). `.claude/README.md` não regenerado —
    inventário de agentes inalterado (`check-drift` em exit 0 confirma).
  Conformidade de vocabulário (frente c): `entregue`/`bloqueado` — **0 ocorrências** antes e
    depois, nada a traduzir; `parcial` permanece nas duas ocorrências de tipo (ii) (níveis da
    rubrica, linhas 19 e 91); `pacote` remanescente em 1 linha (35), na acepção do conjunto
    obrigatório dentro do laudo.
  Veredito — `EXA-T20`
  Suítes: `python -m pytest` (raiz do hub) — 39 passed. Sem teste novo: o alvo é prompt de agente,
    sem superfície executável.
  Kit: `kit_check.ps1 -Mode validate`/`-Mode check-drift` — exit 0 (8 agentes, 11 skills,
    VERSION==KIT_VERSION '0.0.0').
  Espelho: `check-readme.ps1` — exit 0 (8 agentes, 11 skills, 14 guardrails, 14 seções com Fonte
    da verdade).
  Checklist de review: ok — `model: opus` e `tools:` intocados (escopo do `TK-27`); nenhum plano
    editado; nenhuma outra superfície tocada; redação sem narrativa de proveniência, sem citação de
    interlocutor e sem ID de processo no corpo do arquivo publicado.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T13` — proxy de ocupação de contexto — `done`.** A condição de **capacidade** do
  `GOVERNANCA.md` §4.3 deixou de ser critério sem instrumento. Rota fechada por derivação da `T1`
  Sonda 3 (variante (a), hook lendo o `transcript_path`); a variante (b) segue descartada e o
  `TK-23` fecha sem sonda nova. Entregável: `.claude/tools/ocupacao.py` (novo) com duas funções
  puras — `calcular_ocupacao` toma a última entrada de assistant com bloco `usage` do `.jsonl` e
  soma `input_tokens` + `cache_read_input_tokens` + `cache_creation_input_tokens`, com fallback
  `soma(len)/4` marcado como fonte estimada; `avaliar` compara com `JANELA_TOKENS` (default
  200 000, sobrescrevível por ambiente) contra o limiar **0,50**, que é o "~50% da janela" já
  doutrinado e não número novo. Falha aberta total (qualquer erro ⇒ exit 0 silencioso, jamais
  bloqueia chamada de ferramenta) e filtro por `agent_type` para não avisar dentro de subagente.
  Hook `PreToolUse` registrado em `.claude/settings.json` com o bloco `permissions.deny` original
  preservado. Três superfícies de doutrina passaram a nomear o instrumento que existe, em vez da
  ausência dele: `GOVERNANCA.md` bullet *Capacidade*, e no `scrum-master` o Passo 10, a regra `B2` e
  o parágrafo de encerramento de janela. **Ramo A vencedor no primeiro mecanismo tentado**, provado
  ao vivo com hook de sonda descartável e revertido: `hookSpecificOutput.additionalContext` chega
  injetado ao turno seguinte. Ramos B e C descartados por sucesso do A, não testados.
  **Confirmação que o executor não podia produzir:** o instrumento disparou no contexto principal do
  orquestrador durante o próprio fechamento desta tarefa, o que resolve a limitação que ele
  registrou como inferida — `agent_type` é de fato ausente no contexto principal, senão o hook teria
  ficado em silêncio. Verificação: `pytest -q` **43 → 52 passed** (+9 testes novos, mínimo era 6);
  `dead_code.py`, `kit_check -Mode validate`, `-Mode check-drift` e `check-readme.ps1` todos em exit
  0, com 8 agentes, 11 skills e **16 guardrails inalterados**. Achado fora de escopo em
  `.gitignore:3` — ver bloco abaixo. **Laudo emitido em 2026-08-15: `aprovado`, 100%,
  bloqueante `nenhuma`, recomendação `escalar`** — as sete dimensões `conforme`, a pendência é o
  `TK-43` e a entrega fecha em `done`. Registro canônico da tarefa em
  `docs/RDO/P-0734-T13-proxy-de-ocupacao-de-contexto.md`; o laudo foi consumido e descartado
  (`DP-K` §14.4). Dois achados de processo do laudo saem com rota: o **`TK-44`** (o dossiê de
  evidência não discrimina escopo com a iniciativa inteira sem commit) e um **item de
  replanejamento** — o campo *Arquivos-alvo* do `### T13` não nomeia
  `.claude/skills/scrum-master/SKILL.md` nem `GOVERNANCA.md` §4.3, embora o campo *Conteúdo* exija
  o comportamento do `scrum-master`; a entrega tocou as duas superfícies por consequência
  obrigatória (`G-SURFACE`), e o escopo foi julgado contra o *Conteúdo*, sem punir a execução pelo
  campo incompleto.
  Consumo: ver `docs/telemetria.tsv`.

**Achado da `EXA-T13` — `TK-43`: o hub distribui um kit cuja configuração de hook é ignorada pelo
git.** `.claude/settings.json` está em `.gitignore:3`, sob o comentário "Configuração local de
máquina — nunca canônica". A `T13` registrou ali o hook do proxy de ocupação porque o dossiê nomeia
esse arquivo como alvo, e o instrumento funciona na máquina do dono — mas nada dele viaja para
consumidor nenhum, e `kit_check` não o vê. A `T14` (telemetria sem turno de agente) tem o mesmo
alvo e herda o mesmo defeito. É questão de arquitetura de distribuição do kit, não de execução:
decidir se hook canônico ganha residência versionada própria com materialização no `settings.json`
local, ou se o proxy de ocupação é assumido como instrumento só-do-hub. Sobe ao dono.

**Janela encerrada por escalada em 2026-08-15** — a `T13` fechou `aprovado` 100%, e a recomendação
`escalar` do laudo dispara `B1`: a pendência sobe ao dono e o loop **PARA**, mesmo com veredito
aprovado. A janela também cruzou o teto de trabalho, com o aviso disparado pelo próprio instrumento
da `T13` (`B2`) — encerramento normal, não falha. **Próxima tarefa:** a **decisão do dono sobre o
`TK-43`** — **decidida no mesmo dia**: hook canônico ganha residência versionada própria, com
materialização no `settings.json` local. A decisão fecha o *quê* e deixa o *como* em aberto (onde
mora o hook versionado, como materializar sem sobrescrever configuração de máquina do consumidor, o
que `kit_check` passa a exigir), de modo que o próximo passo é uma **rodada de replanejamento** que
autora o dossiê da correção e reescreve o da `T14`, cuja rota o achado invalida — não a delegação de
uma tarefa existente (`G-PLANREADY`). Fila registrada: [replanejamento: `TK-43` + reescrita do
dossiê da `T14`] → `T29` → `T30` → [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` →
`T14` → `T15` → `T16` → `T17` (dono).

- **Rodada de replanejamento `DP-R` — `TK-43` + reescrita da `T14` — concluída em 2026-08-15.** A
  decisão do dono (hook canônico com residência versionada própria e materialização no
  `settings.json` local) ganhou residência no plano como **`DP-R`** (§22), com o bloco do dono
  separado das derivações de planejamento. Fechado, com verificação no repo: o hook canônico mora em
  `.claude/hooks/hooks.json` (chave única `hooks`, comando com placeholder `{KIT_ROOT}`); a
  materialização é do `.claude/tools/hooks_sync.py` (`apply`/`check`/`drift`), que resolve a raiz
  pelo próprio caminho, cobre as duas topologias (hub e consumidor com `.claude/kit/`), preserva
  byte a byte toda chave de topo que não seja `hooks` — inclusive o `permissions.deny` — e todo hook
  não-kit, e é idempotente; `kit_check` passa a exigir canônico válido em `-Mode validate` e
  materialização em dia em `-Mode check-drift`, com falha específica para hook de kit escrito direto
  no `settings.json` (regressão do próprio `TK-43`). `sync-kit.ps1` não muda e `DA-3` se mantém
  (0/6 consumidores com kit materializado). Dois cards novos, partidos por volume e por natureza:
  **`T53`** (residência + materializador + guarda, `[Sonnet · implementação padrão · teto 40]`, 9
  testes nomeados) e **`T54`** (superfície que diz onde hook mora e o que viaja, `[Opus · redacao ·
  teto 25]`). A **`T14`** teve o alvo trocado de `settings.json` para
  `.claude/hooks/hooks.json` + `.claude/tools/telemetria_hook.py`, ganhou dependência da `T53` e um
  invariante de residência, com a cláusula *resultado negativo é resultado* preservada e endurecida.
  A **`T13`** teve só o campo *Arquivos-alvo* conciliado (`+.claude/skills/scrum-master/SKILL.md`,
  `+GOVERNANCA.md` §4.3), com nota datada — bullet de fechamento, RDO, telemetria e histórico
  intocados (`DP-H`). Plano em **49/60**. Achado incidental prescrito dentro da `T54`: `README.md:741`
  diz "dez skills" onde disco e tabela têm onze. **Escalada ao dono, não decidida:** o
  `permissions.deny` do guardrail 13 tem o mesmo defeito de distribuição do `TK-43` — enforcement de
  regra publicada vivendo em arquivo que o git ignora —, e estender a ratificação de hook para
  permissões é requisito novo (registrado em `DP-R` §22.5, fora da `T53`/`T54`; nada da rodada
  depende da resposta). **Próxima tarefa:** **`EXA-T53`** — dossiê em
  `docs/plans/P-0734-execucao-autonoma.md` `### T53`. Fila: `T53` → `T54` → `T29` → `T30` →
  [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T14` → `T15` → `T16` → `T17`
  (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **Iniciativa suspensa em 2026-08-15, rebase (A) — `blocked` em 49/60.** A `T53`/`T54` foram
  **retidas pelo dono** e depois **canceladas por absorção**: elas resolviam o sub-caso do hook antes
  da regra geral, e o `TK-45` mediu que o mesmo defeito de residência tem **5 ocorrências**. A
  matéria inteira migrou para o `P-0735`; corpo das duas tarefas preservado como material absorvido,
  §5 e o dossiê da `T14` conciliados com nota datada (a dependência da `T14` passa da `T53` para a
  `RPC-T2`). O ponto escalado em `DP-R` §22.5 (`permissions.deny` do guardrail 13) **fechou sem
  requisito novo** — a invariante da régua nova o decide —, com o fecho anotado no próprio §22.5.
  Destrava no fechamento do `P-0735`.

- **`EXA-T14` — Telemetria sem turno de agente — `review` (2026-08-19).** Iniciativa retomada:
  `P-0735` fechou `done` (13/13) e a razão do bloqueio deixou de se aplicar; as dependências `T7` e
  `RPC-T2` estavam satisfeitas. **Ramo B (resultado negativo) realizado**, com evidência: sonda pelo
  método da Sonda 3 (hook descartável em `SubagentStop` via `.claude/settings.local.json`, disparo
  por invocação trivial de `context-scout`, reversão confirmada) mediu que o evento **existe** e que
  `agent_transcript_path` aponta para um `.jsonl` exclusivo do subagente com `message.usage` e
  `message.model` por entrada — mesma classe de fato que `transcript_path` na Sonda 3, e mesmo padrão
  de parse que `ocupacao.py` (`T13`) já usa; `tool_uses` seria contável por blocos `tool_use` e
  `duracao_s` pela diferença de `timestamp`. **O obstáculo não é o consumo, é a identidade da
  tarefa:** `tarefa` (coluna obrigatória de `telemetria.py append`) não é campo de schema do harness —
  existe só como texto livre no prompt do subagente, e inferi-la por regex sobre prosa arrisca não
  escrever nada ou gravar linha com `tarefa` errada. Conforme o ramo: **nenhuma** entrada em
  `.claude/projecoes.json`, **nenhum** `telemetria_hook.py` e **nenhum** teste novo (`G-DEADCODE`);
  evidência registrada como **Sonda 5** em `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md` (payload
  literal colado, veredito `parcial, insuficiente para a automação completa`) e o fluxo vigente da
  `T7` mantido. Bateria de fechamento 4/4 em exit 0, suíte **71 passed** (piso inalterado, coerente
  com o ramo). Único arquivo tocado: o documento de sondas. **Escalada ao dono, não decidida:** o
  plano enumerava dois ramos (viável / inviável) e o medido é um terceiro — o consumo está exposto e
  só falta um **contrato** que carregue a identidade da tarefa até o hook. Bifurcar a rota exige
  decision record aprovado antes (Regra 8); nada da fila depende da resposta. Plano em **50/60**.
  **Próxima tarefa:** a decisão acima; depois dela, `EXA-T15`. Fila: [decisão do dono sobre o
  contrato de identidade] → `T15` → `T16` → `T17` (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T15` — Enxugamento dos prompts absorvidos pelos instrumentos — `review` (2026-08-19).** O
  invariante 3 do §3 foi aferido nos seis artefatos declarados e a economia medida é **−1 linha
  líquida** (734 → 733): o único texto de formato coberto por instrumento que ainda vivia num prompt
  era a **enumeração das 8 colunas** do TSV em `handover/SKILL.md:32-35`, que saiu e virou ponteiro
  para `.claude/tools/telemetria.py append` (colunas, validação de tipo/domínio e escrita atômica são
  do script desde a `T7`); em `proximo-passo/SKILL.md:151-153` a mecânica do apenso, antes descrita em
  prosa sem citar instrumento, passou a apontar para o mesmo CLI, com a regra de qual `--fonte` usar
  por cenário preservada. **Três alvos fecharam com 0 linhas removidas** — `diario-de-obras/SKILL.md`,
  `pantonic-executor.md` e `pantonic-planner.md` —, confirmado por grep dedicado
  (`RDO|laudo|telemetria|colunas|dimens|campo|formato|schema`): não há ali gabarito que um CLI passou a
  garantir. As regiões MISTO (`handover:70-112`, `proximo-passo:126-149`, `diario-de-obras:44-51`)
  foram lidas e **preservadas pela regra de corte** — relatório ao dono, checkpoint e estrutura do
  diário são regra, não formato gerado por código, e o "Cuidado" do dossiê proíbe removê-las.
  `.claude/README.md` foi **regenerado por `kit_check.ps1 -Mode generate`** (nunca editado à mão) e
  reconciliou o índice com o disco: caem `pantonic-auditor-container` e `pantonic-auditor-pyside6` (já
  deletados), entra `pantonic-reviewer`, entram as skills `redacao-doc` e `scrum-master`, e quatro
  descrições desatualizadas sincronizam. Bateria do §3 item 6 inteira em exit 0 (8 agentes, 11 skills,
  20 entradas canônicas; 16 guardrails × 14 seções; `dead_code.py` com 0 achados) e suíte **71
  passed**, piso mantido — a tarefa não cria teste, por ser edição textual. **3 write-clusters** contra
  o teto de 8. **Teto de tool uses estourado:** 43 medidos contra 40 prescritos (+7,5%), sem mudança de
  rota nem de escopo — o excedente é da varredura de confirmação nos três alvos que fecharam em zero.
  Sem bump e sem tag (`DE-7`). Nenhum achado fora de escopo. Plano em **51/60**. **Próxima tarefa:** a
  decisão do dono sobre o contrato de identidade da `T14`, ainda em aberto; depois dela, `EXA-T16`.
  Fila: [decisão do dono sobre o contrato de identidade] → `T16` → `T17` (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **Decisão do dono, 2026-08-19 — contrato de identidade da `T14`: rota (a) aceita.** O `scrum-master`
  grava a tarefa corrente num ponto de estado conhecido do kit no ato do despacho, e o hook de
  `SubagentStop` lê a identidade de lá — sem inferência por regex sobre a prosa do prompt, que foi o
  defeito medido. Registro é **checkpoint**: o decision record no plano e o card da tarefa nova são a
  **rodada de replanejamento** seguinte. **Próxima tarefa:** essa rodada; depois dela, `EXA-T16`.

- **Checkpoint de janela, 2026-08-19 — pickup da rodada de replanejamento, encerrado por capacidade.**
  Janela cruzou o teto de ~50% (`GOVERNANCA.md` §4.3) no levantamento, antes de qualquer edição do
  plano; nada foi iniciado depois do sinal (Regra 2). Estado derivado, para não se repagar: a rodada é
  **inline pelo orquestrador em Opus** (precedente `EXA-DP*-replan` na série, nunca delegada — Regra
  8); próximos identificadores livres **`DP-S`** (seção `## 23`, molde no `## 22` do `DP-R`) e card
  **`T55`**; o `## 5` do plano e o dossiê `### T14` são as duas superfícies a conciliar, e o
  denominador do plano passa de 60 para 61. **Próxima tarefa:** a mesma rodada, em contexto novo.

- **Checkpoint de janela, 2026-08-19 (2ª) — levantamento da rodada `DP-S` completo, encerrado por capacidade.** Teto de ~50% cruzado no levantamento; nenhuma edição iniciada (Regra 2). **Insumos já pagos:** Sonda 5 em `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195` (payload traz `agent_id`/`agent_type`/`agent_transcript_path`, sem bloco de uso); `telemetria.py append` exige 8 flags; `.claude/projecoes.json` alvo `projeto` → `chaves.hooks` só tem `PreToolUse`→`ocupacao.py` com `{KIT_ROOT}`; `scrum-master/SKILL.md` "Estado do loop" `:20-38` e Passo 4 `:84-107`; `.gitignore:1-5`; no plano, §4 termina em `:2320` (último card `### T54`), §5 em `:2321-2334` (fila fecha em `T12 → T14 → T15 → T16 → T17`), molde da rodada em §22 `:4433-4534`, dossiê `### T14` em `:538-568`.
  **Desenho derivado, a transcrever (não repagar):** estado local de máquina `.claude/estado/tarefa-corrente.json` (gitignored) gravado pelo `scrum-master` no Passo 4; hook `SubagentStop` → `.claude/tools/telemetria_hook.py`, declarado no manifesto; filtro por `agent_type` + consumo do estado depois de escrever a linha (staleness limitada); sem estado ⇒ silêncio e exit 0, preservando o fluxo manual da `T7`; `tokens_k` somado do `agent_transcript_path` (`input+cache_creation+cache_read+output` por entrada `assistant`), calibrado contra o `<usage>` de um despacho aninhado trivial; ~6 write-clusters ⇒ **um** card `[Sonnet · implementação padrão · teto 40]`.
  **A escrever:** §23 `DP-S` + card `### T55` + `T55` na fila do §5 + nota datada no `### T14`; denominador 60 → **61** (plano em 51/61). **Próxima tarefa:** a mesma rodada, em contexto novo.

- **Rodada de replanejamento `DP-S` — contrato de identidade da telemetria — concluída em 2026-08-19.**
  A decisão do dono (o `scrum-master` grava a tarefa corrente num ponto de estado do kit no ato do
  despacho; o hook de `SubagentStop` lê a identidade de lá) ganhou residência no plano como **`DP-S`**
  (§23), com o bloco do dono separado das derivações de planejamento. Recusa registrada com a decisão:
  inferência por regex sobre a prosa do prompt — falha silenciosa que grava linha com `tarefa` errada,
  pior do que linha ausente, porque contamina a única fonte de número do framework. Derivações
  fechadas, todas de planejamento: o estado é **local de máquina** (`.claude/estado/tarefa-corrente.json`,
  no `.gitignore` — pela pergunta zero da régua, é fato de uma sessão numa máquina, não autoridade do
  framework); o autor é o **Passo 4** do `scrum-master`, sem contador novo na tabela do estado do loop;
  o hook é `SubagentStop` → `.claude/tools/telemetria_hook.py`, declarado em `.claude/projecoes.json`
  com `{KIT_ROOT}`, na mesma forma do `PreToolUse` → `ocupacao.py` já existente; filtro por
  `agent_type` e consumo do estado **depois** de escrever a linha, o que limita a staleness a uma
  janela; sem estado ⇒ silêncio e exit 0, preservando íntegro o fluxo manual da `T7`; números pelo
  `agent_transcript_path`, com calibração obrigatória contra o `<usage>` de um despacho aninhado
  trivial. **Um card**, `T55` `[Sonnet · implementação padrão · teto 40]`, 6 write-clusters contra o
  limite de 8 — sem razão de volume nem de natureza para partir. **Fila:** o card entra **depois da
  `T15` e antes da `T16`**, por duas razões declaradas: ele edita o Passo 4 do `scrum-master`, que é a
  superfície que a `T16` pilota (pilotar antes e mudar depois invalidaria a medida), e a automação
  existindo antes do piloto faz o próprio piloto se medir sozinho. A **`T14` não é reaberta** —
  fechou corretamente em ramo B — e recebeu só nota datada apontando para o §23. Denominador **60 →
  61**; plano em **51/61**. Sem guardrail novo (`DA-10`), sem bump e sem tag (`DE-7`). Nenhum ponto de
  parada e nada escalado ao dono. **Próxima tarefa:** **`EXA-T55`** — dossiê em
  `docs/plans/P-0734-execucao-autonoma.md` `### T55`. Fila: `T55` → `T16` → `T17` (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T55` — identidade da tarefa por estado do loop: a série se alimenta sozinha — 2026-08-19.**
  A linha de `docs/telemetria.tsv` deixa de custar turno: o Passo 4 do `scrum-master` (`:88-93`) grava
  `.claude/estado/tarefa-corrente.json` antes de invocar o executor, e o hook novo
  `.claude/tools/telemetria_hook.py` lê a identidade de lá no `SubagentStop`, traduzindo o payload em
  chamada a `telemetria.py append` com as 8 flags e `--fonte usage`. A declaração entra em
  `.claude/projecoes.json` (chave `SubagentStop`, comando em `{KIT_ROOT}`, mesma forma do `PreToolUse`
  → `ocupacao.py`); o `settings.json` local continua sendo produto de `materializar.py apply`, nunca
  alvo de edição. `.gitignore:10` recebe `.claude/estado/` como local de máquina. Sem estado ⇒ silêncio
  e exit 0, com o fluxo manual da `T7` intacto. **A calibração obrigatória produziu achado e ele entrou
  no produto:** contra um despacho aninhado real, o total de `tokens_k` dobrava — entradas `assistant`
  do transcript repetem a mesma `message` com `usage` idêntico —, e o hook passou a **deduplicar por
  `message.id`**, com teste de regressão dedicado. Verificação: os quatro guardas da bateria em exit 0,
  mais `materializar.py check` em exit 0; suíte de **71 → 77 passed**. **Teto estourado:** 49 tool uses
  contra os 40 da classe (+22%), sem replanejamento nem mudança de rota — a calibração empírica com
  transcript real foi o excedente. Sem guardrail novo (`DA-10`), sem bump e sem tag (`DE-7`). Nenhum
  achado fora de escopo e nada escalado ao dono. Plano em **52/61**. **Próxima tarefa:** **`EXA-T16`**
  — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T16` (piloto medido). Fila: `T16` → `T17`
  (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **Rodada de decisão — a `EXA-T16` não é delegável e seu combustível está travado — 2026-08-20.**
  O pickup da `T16` parou no gate `G-PLANREADY`, antes de qualquer delegação, por dois fatos. (1) A
  `DA-1` põe o `scrum-master` no **contexto principal**, de modo que a `T16` **não é delegável** a
  `pantonic-executor` — conduz-se de um contexto principal; a premissa técnica original caiu na `T1`
  (aninhamento funciona), mas a decisão foi reexaminada e mantida por controle. (2) O combustível que
  a `T16` declara — tarefas ainda abertas do `P-0733` — está medido como inválido: o percurso a seco
  da `T13` já viu a `DHB-T1` ser recusada em **`B3`** por cabeçalho legado sem `classe`/`teto`, e as
  tarefas abertas (`T2`..`T12`, mais a `T13` do dono) seguem com cabeçalho só `[Opus]`/`[Sonnet]`.
  Pilotar assim mediria apenas a recusa — sem execução, laudo, RDO ou comparação com a série, que é o
  entregável da tarefa. **Duas decisões do dono nesta rodada:** (a) o **`TK-24`** — retrofit dos 12
  cabeçalhos do `P-0733` para `[<modelo> · classe <slug> · teto <N>]` — é executado **antes** do
  piloto, em tarefa própria de planejamento; recusadas rodar o piloto sobre a recusa (não mede nada) e
  afrouxar o gate `B3` (mudaria a superfície sob teste às vésperas de medi-la, o que a `T55` já
  registrou como invalidante); (b) a convenção `docs/RDO/evidencia/<plano>-<ID>.md`, prescrita pela
  skill sem ratificação prévia, é **ratificada como está**, fechando o achado que estava roteado à
  `T16`. Nada executado nesta rodada: a janela cruzou o teto de ocupação (§4.3) antes do retrofit.
  Plano em **52/61**. **Próxima tarefa:** o retrofit do `TK-24` (ato de planejamento, Opus), e só
  depois a `EXA-T16`. Fila: `TK-24` → `T16` → `T17` (dono).

- **Checkpoint de janela — segundo pickup consecutivo encerrado por capacidade, sem execução —
  2026-08-21.** A janela cruzou o teto de ocupação (§4.3) durante o próprio pickup do `TK-24`, antes
  de qualquer edição — mesmo desfecho da rodada de 2026-08-20. Estado apurado e não perdido: fila
  `TK-24` → `T16` → `T17`; os 12 cabeçalhos a retrofitar são `### T2`..`### T13` de
  `docs/plans/P-0733-divida-do-hub.md` (linhas 130, 142, 157, 170, 188, 200, 209, 224, 235, 252, 268,
  283); gramática e conjunto fechado de slugs em `P-0734` `### DP-C` (`:2880-2905`); tabela de tetos
  em `GOVERNANCA.md` §3 (`:133-139`); o parser que recusa cabeçalho legado é
  `.claude/tools/rdo.py:79-80` e exige `<modelo>` ∈ `Opus|Sonnet|Haiku`. **Ponto que a execução
  encontra:** a `T13` do `P-0733` tem cabeçalho `[dono]`, valor fora do conjunto fechado da `DP-C` —
  a rota do cabeçalho de tarefa que não é delegada a agente ainda não está decidida. **Recorrência
  (2ª) do pickup que consome a janela antes de executar** — reportada ao dono nesta rodada.
  Consumo: ver `docs/telemetria.tsv`.

- **Checkpoint de janela — terceiro pickup consecutivo encerrado por capacidade, sem execução —
  2026-08-21.** `proximo-passo` drenou os dois inboxes (vazios), leu a diretiva de priorização
  (`P-0734` primeiro, `P-0733` depois) e confirmou a fila já apurada: `TK-24` → `T16` → `T17`. A
  janela cruzou o teto de ocupação (§4.3) no próprio levantamento de estado, antes de qualquer
  delegação. Nenhum fato novo: o estado é o mesmo do checkpoint de 2026-08-21 imediatamente
  acima. **Recorrência (3ª)** do pickup que consome a janela antes de executar — reportada ao
  dono nesta rodada.

- **Insumo do dono — a regra escalonada da decisão a jusante — 2026-08-21.** O pickup do `TK-24`
  levou ao dono a questão do cabeçalho de tarefa sem agente (a `### T13` do `P-0733` é `[dono]`,
  valor fora do conjunto fechado da `DP-C`, e o parser `.claude/tools/rdo.py:79-80` a recusa). O
  dono **não escolheu entre as opções apresentadas**: estabeleceu no lugar uma **regra escalonada de
  três níveis**, que é doutrina de autoria de plano e excede o `TK-24`. Registro do insumo, verbatim
  em substância, para a rodada de doutrina que o materializa:
  1. **Primeiro nível — a norma.** Na elaboração do plano, **todas as decisões pertinentes se
     resolvem no primeiro nível**. Elaborar plano já prevendo decisão do dono a jusante é
     **anomalia**: não é postergação, é **procrastinação**, e procrastinação é **vício inaceitável
     do projeto**.
  2. **Segundo nível — existe decisão, faltam elementos para tomá-la.** O plano **se reescopa**:
     começa e termina **antes** da decisão, as entregas são avaliadas, e **só então** se decide.
     Mesmo neste nível, **parar para decidir é procrastinação**.
  3. **Terceiro nível — parada genuinamente inesperada.** O executor **aciona o `scrum-master`** e
     **bloqueia** a execução do plano para resolução da questão. Mesmo a parada inesperada é
     **perda do projeto**, e deve haver **esforço para evitá-la**.
  **Superfície apurada, não editada:** a residência natural é `GOVERNANCA.md` §7 item 11
  (**G-PLANREADY**, `:576`), cujo item 5 já é o gate de publicação — a regra nova aprofunda e
  escalona o mesmo dever; o §7 tem 16 guardrails e o espelho `README.md` anda em lockstep por
  `G-SURFACE` (guardrail 16). O nível 3 toca a fronteira executor→`scrum-master`, já governada pela
  `DP-G` (razão tipada `dependencia`/`premissa`). **Consequência imediata sobre a fila:** pelo
  **nível 2**, o `TK-24` não se resolve perguntando — o `P-0733` se reescopa para começar e terminar
  antes da decisão do cabeçalho `[dono]`. Nada editado nesta rodada.

- **Checkpoint de janela — quarto pickup consecutivo encerrado por capacidade, sem execução —
  2026-08-21.** A janela cruzou o teto de ocupação (§4.3) no levantamento da superfície da doutrina,
  antes de qualquer edição de `GOVERNANCA.md`. Diferente das três anteriores, **esta rodada produziu
  fato novo** — o insumo do dono acima, gravado. **Recorrência (4ª)** do pickup que consome a janela
  antes de executar: quatro rodadas seguidas (2026-08-20, 2026-08-21 ×3) em que o custo de apurar o
  estado esgotou a janela antes da primeira delegação. O padrão deixou de ser acidente e é ele
  próprio um defeito de desenho do fluxo de pickup — escalado ao dono nesta rodada.

---

## P-0735 — Residência e ponto de carga

> **Índice (texto integral do campo Título, migrado da tabela ativa em 2026-08-23):** Residência e ponto de carga — o pacote materializa o que a doutrina invoca: a régua de residência deixa de responder *onde mora* com uma resposta só e separa **autoridade** de **ponto de carga** em três classes (canônico · ponto de carga · local de máquina), com **pergunta zero** antes das quatro e o `Prec-2` promovido a **invariante** (*nada canônico mora só num ponto de carga*). Constrói o manifesto único `.claude/projecoes.json` e o materializador `.claude/tools/materializar.py` (`apply`/`check`/`drift`, alvos `projeto` e `usuario`), promove ao kit os **13 artefatos** que hoje só existem em `~/.claude/` (4 hooks registrados, 6 skills, 1 agente, 2 docs de doutrina) mais o `CLAUDE.md` global, declara por exaustão o que é **local de máquina** e faz o `kit_check` cobrar o canônico (`-Mode validate`) e a materialização do alvo `projeto` (`-Mode check-drift`). **9 tarefas** (`RPC-T1..T9`), decisões `DL-1..DL-9` fechadas no ato, todas de planejamento. Absorve `TK-45`, `TK-43` e o `permissions.deny` do `DP-R` §22.5, destrava o `DR-B`, e **não** absorve o `TK-21` (rota já decidida na `DH-4`, executável no `P-0733` `T10`). Alcance: hub primeiro, medir, depois propagar (`DA-3` mantida, 0/6 consumidores), alvo `usuario` **opt-in**, `sync-kit.ps1` inalterado. Sem bump e sem tag (`DE-7`). **`DL-10` decidida pelo dono em 2026-08-17** sobre o `TK-47` (achado da `RPC-T4`): `apply` passa a ser byte-idempotente sob equivalência semântica — recusada a alternativa de aceitar a normalização e afrouxar o critério da `T5` —, com a `T10` nova autorada fechada e entrando entre a `T4` e a `T5`; **`TK-49` (achado da `T5`, decidido pelo dono no mesmo dia) vira a `T11`**, autorada fechada logo depois da `T5` — `{KIT_ROOT}` passa a resolver para caminho absoluto; a `T6` foi executada em 2026-08-17 fora de ordem, à frente da `T11`, e a `T11` fechou em 2026-08-18, restabelecendo a ordem do §5; a `T7` foi **partida em `T7a`/`T7b`/`T7c` por orçamento** no gate de delegação (14 write-clusters medidos contra o limite de 8 na primeira partição; 10 na re-derivação da fatia do kit executável, que forçou a segunda; sem mudança de rota ou escopo em nenhuma das duas) (13/13 — `T1`, `T2`, `T3`, `T4`, `T10`, `T5`, `T6`, `T11`, `T7a`, `T7b`, `T7c`, `T8`, com a `T7` inteira fechada; `T8` fecha `.gitignore`/`CHANGELOG.md`/`TK-43`/`TK-45`/`permissions.deny` (`DL-7`), bateria de fechamento em exit 0, suíte 71 passed; `T9` fecha o espelho com veredito **aprovado** do dono: `check-readme.ps1` em exit 0 e dois trechos de estado anterior corrigidos (§4, que descrevia o hook como fora do kit, contra `GOVERNANCA.md` §3, onde ele é canônico e projetado; §1 e §11, que listavam permissões em bloco como configuração do operador, contra a `DL-7`, que tornou `permissions.deny` chave canônica do alvo `projeto`), com o §11 mantido sem enumerar `.claude/tools/` por decisão do dono — os cinco instrumentos restantes são entregáveis do `P-0734` e entram quando aquela iniciativa fechar. Consumo: ver `docs/telemetria.tsv`)
>
> *(Âncora original do índice, preservada:* `docs/plans/P-0735-residencia-e-ponto-de-carga.md` *)*

- **Rodada de doutrina e autoria do plano — 2026-08-15.** Pedido do dono: *"vamos parar por algumas
  tarefas e resolver isso globalmente"*, com o alcance ratificado no mesmo ato — **o pacote passa a
  materializar também o `~/.claude`**. `GOVERNANCA.md` §3.1 deixou de responder *onde mora* com uma
  resposta só e passou a separar **autoridade** de **ponto de carga** em três classes (canônico ·
  ponto de carga · local de máquina), com **pergunta zero** antes das quatro, `Prec-2` promovido a
  **invariante** (*nada canônico mora só num ponto de carga*), a precedência 2 trocada para *canônico
  vence projeção* e a cláusula "e não viaja" do parágrafo de hook removida — era o sintoma registrado
  como lei. `docs/RESIDENCIA_DOUTRINA.md` ganhou §8 de conciliação datada, sem reescrever nenhuma
  linha das §§1-6 (`DP-H`): a classe `global` muda de residência sem mudar de alcance, `DR-A`
  sobrevive com motivo trocado, `DR-B` **destravado** depois de 12 dias parado como "iniciativa
  própria" nunca aberta. Plano `P-0735-RPC` autorado fechado, 9 tarefas (`RPC-T1..T9`), `DL-1..DL-9`
  todas de planejamento. Desenho: manifesto único `.claude/projecoes.json` (o `hooks_sync.py`/
  `hooks.json` da `T53` **não nasce** — vira chave do manifesto, `DL-2`); os 13 artefatos globais
  passam a canônicos em `.claude/global/`, **fora** de `.claude/skills/` e `.claude/agents/`, para não
  virarem skill ativa em todo projeto Pantonic nem colidir por nome com a própria projeção (`DL-6`,
  com o espelho intacto em 8 agentes e 11 skills); `check-drift` cobra só o alvo `projeto`, com o alvo
  `usuario` opt-in para não reprovar consumidor por projeção de máquina alheia (`DL-4`); `DA-3`
  mantida e `sync-kit.ps1` inalterado (`DL-8`). Ordem por valor validável, com `copiar → declarar →
  aplicar` tornando todo `apply` de promoção um **no-op verificável** — a máquina do dono não muda um
  byte e o `drift` verde é a prova de fidelidade. `TK-21` **não absorvido**, com motivo: rota já
  decidida (`DH-4`) e executável no `P-0733` `### T10`. **Próxima tarefa:** **`RPC-T1`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T1`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T1` — espelho: o `README.md` fala a régua das três classes — 2026-08-15.** As 7 edições do
  dossiê aplicadas em `README.md`, único arquivo tocado. §12: o teste de residência ganha a **pergunta
  zero** antes das quatro e a pergunta 1 passa a apontar doutrina global **canônica no kit, projetada
  em `~/.claude/CLAUDE.md`**; a afirmação de que a governança das memórias **não viaja** cai, e a
  precedência 2 troca "versionado vence não-versionado" por **canônico vence projeção**, com a nota de
  que projeção não se edita no destino. §11: a prosa de abertura passa de "dez" para **onze** skills
  (disco e tabela já tinham onze; o guarda compara tabela × disco e não lê o número em prosa) e nomeia
  a **declaração de projeções** entre o que viaja, mais um parágrafo novo com `.claude/projecoes.json`,
  `.claude/tools/materializar.py` e `.claude/global/`; a frase das "skills instaladas fora do
  repositório" vira a régua nova — o que fica fora do kit é **configuração de quem opera a máquina**.
  §2: a frase do "não viaja no pacote distribuído" concilia com a invariante — o que não chega ao
  consumidor é o que fica **só** num ponto de carga, e a resposta é projetar, não excluir do pacote.
  Tabelas de agentes e de skills intactas (`DL-6`), nenhuma seção numerada nova, nenhuma linha
  `> Fonte da verdade:` alterada, nenhum guardrail novo, `CHANGELOG.md` não tocado (registro é da
  `T8`). Verificação: `check-readme.ps1` exit 0 (8 agentes, 11 skills, 16 guardrails, versão `0.0.0`,
  14 seções com fonte válida) e Grep de `não viaja`/`não viajam` em zero ocorrências. Achado fora de
  escopo indexado como **`TK-46`**. **Próxima tarefa:** **`RPC-T2`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T2`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T2` — manifesto de projeções, materializador e o ponto de carga do projeto — 2026-08-17.**
  Três arquivos novos: `.claude/projecoes.json` (declaração canônica, chave única `alvos`, com o
  alvo `projeto` transcrevendo do `.claude/settings.json` real as duas chaves existentes — o
  `PreToolUse` do proxy de ocupação e as 6 entradas de `permissions.deny` do guardrail 13 — **sem
  alterar valor nenhum**, e o alvo `usuario` **declarado e vazio**, como o dossiê manda);
  `.claude/tools/materializar.py` (`apply`/`check`/`drift`, `--alvo projeto|usuario|todos` com
  default `projeto`, `--kit-root` e `--home`, ancoragem hub × consumidor decidida pelo nome do
  diretório-raiz — `kit` ⇒ destino no pai —, `{KIT_ROOT}` resolvendo para token POSIX `.claude` ou
  `.claude/kit` e `{HOME_CLAUDE}` para o `~/.claude` corrente); e `tests/test_materializar.py`, com
  os 12 casos do dossiê cobertos 1:1. O `.claude/settings.json` deixa de ser artefato editado à mão
  e passa a ser **produto** de `python .claude/tools/materializar.py apply`, com chave de topo não
  declarada, hook local não-kit e `permissions.allow` preservados por construção. Verificação
  específica do dossiê cumprida: a materialização foi desfeita à mão uma vez, o `drift` ficou
  vermelho (exit 1, dois problemas — hook canônico ausente e `permissions.deny` divergente) e o
  `apply` restaurou o arquivo, com `drift` de volta a exit 0. Bateria do §3 item 6 inteira em exit 0
  (`kit_check -Mode validate` — 8 agentes, 11 skills, paridade de versão —, `kit_check -Mode
  check-drift`, `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **64 testes passando**
  (piso de 52 + os 12 novos). Fora de escopo e não tocados, como o dossiê fixou: `CHANGELOG.md` e
  `.gitignore` (são da `T8`), `kit_check.ps1` (é da `T3`), `~/.claude` e o preenchimento do alvo
  `usuario` (são da `T4`..`T6`). Nenhum achado fora de escopo. **Próxima tarefa:** **`RPC-T3`** —
  dossiê em `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T3`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T3` — `kit_check` cobra o canônico e a materialização — 2026-08-17.** A régua deixa de
  depender de disciplina: `.claude/checks/kit_check.ps1` (único arquivo tocado, 65 linhas de delta)
  ganha dois blocos. No `-Mode validate`, **bloco 4** entre a paridade de versão e o agregador do
  modo, chamando `materializar.py check --alvo todos --kit-root <kitRoot>` e agregando a saída a
  `$errors`; a agregação é **condicionada a exit 1**, porque o contrato medido do materializador
  imprime uma linha de OK em exit 0 e agregá-la incondicionalmente reprovaria o modo para sempre —
  exit ≠ 0 e ≠ 1 vira "saída não interpretável" com a mensagem crua, de modo que nenhum dos dois
  modos passa em silêncio por não conseguir checar. A linha de OK passa a citar a contagem de
  entradas canônicas, derivada de `.claude/projecoes.json` por `ConvertFrom-Json` em tempo de
  execução (soma de entradas de hook por evento por alvo + itens de `arquivos`; valor corrente **1**)
  — nunca hardcodada. No `-Mode check-drift`, que **não tinha lista de erros** e saía no primeiro
  problema, entra `$driftErrors`: README regenerado e `materializar.py drift --alvo projeto` se
  agregam num relatório único antes de decidir o exit. Alvo `usuario` **fora** do `check-drift`
  (`DL-4`) — cobrar no guarda a projeção da máquina de quem executa quebraria consumidor que não
  optou por ela. Verificação específica do dossiê cumprida: com a chave `hooks` removida à mão do
  `.claude/settings.json`, `-Mode check-drift` ficou **vermelho** (exit 1, 2 problemas vindos do
  `drift`), e `materializar.py apply` restaurou o arquivo com os dois modos de volta a exit 0.
  Bateria do §3 item 6 inteira em exit 0 e suíte em **64 testes passando** (piso mantido — `tests/`
  não muda nesta tarefa, por desenho do dossiê). Fora de escopo e não tocados: `CHANGELOG.md` e
  `.gitignore` (são da `T8`), `.claude/projecoes.json`, `.claude/tools/materializar.py`, `README.md`,
  `.claude/README.md` e `~/.claude`. Nenhum achado fora de escopo. **Próxima tarefa:** **`RPC-T4`** —
  dossiê em `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T4`.
  Consumo: ver `docs/telemetria.tsv`.

- **`RPC-T4` — `.claude/global/`: a doutrina global vira canônica projetada — 2026-08-17.** Primeiro
  uso real do alvo `usuario`, com o conteúdo mais simples de provar: arquivos, sem hook. Os três
  documentos que só existiam no ponto de carga do dono passam a viajar no pacote —
  `.claude/global/CLAUDE.md` (156 linhas), `.claude/global/docs/GOVERNANCA_MEMORIAS.md` (161) e
  `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` (94) —, cada um conferido por **SHA256
  idêntico** ao original antes de qualquer outra edição, e o bloco `arquivos` do alvo `usuario` em
  `.claude/projecoes.json` deixa de ser `[]` para declarar os três pares `de`/`para`. A ordem
  obrigatória do dossiê foi cumprida (copiar → declarar → `apply`), e é ela que produz a prova: o
  `apply --alvo usuario` real foi **no-op** nos três alvos, com mtime inalterado (`CLAUDE.md`
  2026-08-08 18:25:20; `GOVERNANCA_MEMORIAS.md` 2026-08-01 18:58:22;
  `RECOMENDACOES_CONSUMO_GLOBAL.md` 2026-08-07 20:45:09) e `drift --alvo usuario` em exit 0. O teste
  novo (`tests/test_materializar.py`, TF `test_tf_drift_alvo_usuario_acusa_arquivo_ausente_e_fica_verde_apos_apply`)
  prova o ciclo contra fixture sintética com `--kit-root`/`--home` em `tmp_path`, conforme o §3 item
  3 — nunca contra o `~/.claude` real. Bateria do §3 item 6 inteira em exit 0 e suíte em **65 testes
  passando** (piso 64 → 65, sem perda). Fora de escopo e não tocados: `CHANGELOG.md` e `.gitignore`
  (são da `T8`), `.claude/tools/materializar.py` e `.claude/checks/kit_check.ps1` (`T2`/`T3`), os
  hooks e as skills globais (`T5`/`T6`). **Achado fora de escopo, indexado como `TK-47`:** o
  primeiro `apply --alvo usuario` real reescreveu `~/.claude/settings.json` por normalização de
  serialização JSON, com o conteúdo semanticamente preservado — comportamento pré-existente do
  materializador da `T2`, não introduzido aqui, mas que colide com o critério de verificação da
  `T5` ("difere do anterior **apenas** no caminho dos comandos"). **Decidido pelo dono no mesmo dia**
  (`DL-10`): `apply` passa a ser byte-idempotente sob equivalência semântica, e a `RPC-T10` nova foi
  autorada fechada entre a `T4` e a `T5`. **Próxima tarefa:** **`RPC-T10`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T10`.
  Consumo: ver `docs/telemetria.tsv`.

- **`RPC-T10` — `apply` não reescreve o que não mudou — 2026-08-17.** Quita o `TK-47` na origem:
  `write_settings` (`.claude/tools/materializar.py`) mantinha só a comparação de **texto** contra o
  `_dump` canônico, de modo que destino com formatação divergente era reescrito inteiro com o
  conteúdo semanticamente intacto. Entra o caminho **semântico** — `json.loads` do arquivo do
  destino comparado ao objeto a escrever; iguais ⇒ retorna `False` sem abrir o arquivo para escrita
  —, com `json.JSONDecodeError` caindo no comportamento anterior (destino ilegível ou ausente é
  escrito). `_dump` intocado: o formato de escrita **quando há mudança real** não estava em questão
  (`DL-10`), e `check`/`drift` não foram tocados porque ambos já comparam semanticamente — é por
  isso que a mudança não cria drift perpétuo. Dois testes novos em `tests/test_materializar.py`,
  ao lado do `test_tf_apply_e_idempotente`: TF — destino reescrito à mão com `indent=4` e ordem de
  chaves trocada sai do `apply` com **bytes idênticos**; regressão — destino a que falta a entrada
  de hook canônica **continua** sendo reescrito, no formato do `_dump`. Bateria do §3 item 6 inteira
  em exit 0 (`kit_check -Mode validate`, `kit_check -Mode check-drift`, `check-readme.ps1`,
  `dead_code.py` com 0 achados) e suíte em **67 testes passando** (piso 65 → 67, sem perda). Fora de
  escopo e não tocados, como o dossiê fixou: `CHANGELOG.md` e `.gitignore` (são da `T8`), `check` e
  `drift`, `_dump` e o `~/.claude` real — toda prova de comportamento novo em fixture `tmp_path` com
  `--kit-root`/`--home` (§3 item 3). Nenhum achado fora de escopo. Com isso a `T5` pode tratar
  qualquer diferença byte a byte no `settings.json` como sinal. **Próxima tarefa:** **`RPC-T5`** —
  dossiê em `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T5`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T5` — os hooks globais e seus módulos viram canônicos — 2026-08-17.** Fecha o `TK-43` na
  forma geral: os quatro hooks registrados em `~/.claude/settings.json` deixam de existir só na
  máquina do dono. `.claude/global/hooks/` recebe os seis arquivos — os quatro scripts de hook
  (`pytest_pretooluse.py`, `verbose_cmd_pretooluse.py`, `read_cap_pretooluse.py`,
  `modelo_por_fase_userpromptsubmit.py`) mais os helpers `pytest_filter.py` e `tail_filter.py` — e o
  alvo `usuario` de `.claude/projecoes.json` passa a declarar os quatro registros (matchers
  `Bash|PowerShell`, `Read` e `UserPromptSubmit`, `timeout: 15`, comando por `{HOME_CLAUDE}`) mais os
  seis pares `de`/`para`. `statusline.py` e a chave `statusLine` ficaram fora, por `DL-3`. Não existe
  `statusMessage` nas entradas vivas, de modo que a cláusula de transcrição do dossiê saiu vazia.
  **A execução foi encontrada já feita** por sessão anterior do mesmo dia, encerrada antes do
  fechamento (mtime dos artefatos 20:25-20:26, posterior à última linha de telemetria da `RPC-T10`,
  18:47), sem bullet e sem consumo medido — daí a tarefa ter sido **verificada, não reexecutada**:
  seis arquivos byte-idênticos aos de `~/.claude/hooks/` (`diff -q` em todos), declaração conferida
  contra a tabela do dossiê, `~/.claude/settings.json` vivo resolvendo exatamente os quatro comandos
  declarados com as chaves de topo preservadas (`model`, `effortLevel`, `switchModelsOnFlag`,
  `statusLine`, `permissions`), `materializar.py drift --alvo usuario` em exit 0, e o teste
  `test_tf_apply_alvo_usuario_preserva_chaves_de_topo_e_grava_hooks_declarados`
  (`tests/test_materializar.py:295`) provando as cinco chaves em fixture `tmp_path` com `--home`.
  Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode validate`, `kit_check -Mode check-drift`,
  `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **68 testes passando** (piso 67 → 68,
  sem perda). Dois dos quatro hooks se provaram vivos na própria sessão de verificação — o cap de
  Read barrou a leitura integral do diário e o de comando verboso barrou um `ls -R`. **Achado fora de
  escopo, indexado como `TK-49`:** o hook do alvo `projeto` é materializado com **caminho relativo**
  (`python .claude/tools/ocupacao.py`, de `{KIT_ROOT}/tools/ocupacao.py`), então basta o cwd de uma
  chamada de ferramenta sair da raiz do repositório para o hook falhar — e hook `PreToolUse` que
  falha **bloqueia toda ferramenta da sessão**, não só o comando. Medido ao vivo nesta sessão.
  **Decidido pelo dono no mesmo dia:** `{KIT_ROOT}` passa a ser resolvido para caminho absoluto na
  escrita do `settings.json`, em tarefa própria, para que nenhum consumidor herde o defeito.
  **Próxima tarefa:** **`RPC-T11`** (o `TK-49`) — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11`.
  Consumo: ver `docs/telemetria.tsv` (`nao_medido` — a sessão que executou a tarefa se perdeu).

- **`RPC-T6` — as seis skills e o agente `context-scout` — 2026-08-17.** Fecha o `DR-B`, aberto desde
  2026-08-03: os artefatos executáveis que a doutrina versionada invoca deixam de existir só no ponto
  de carga. `.claude/global/skills/` recebe as seis skills (`context-prep`, `doc-map`, `lean-test`,
  `memory-diet`, `onboard`, `test-tiers`) e `.claude/global/agents/` recebe o `context-scout.md`,
  todos cópia byte a byte conferida por `diff -q`; cada diretório de origem continha só o `SKILL.md`,
  de modo que a cláusula de arquivo auxiliar do dossiê saiu vazia. O alvo `usuario` de
  `.claude/projecoes.json` passa de 9 para **16** pares `de`/`para`. O `DL-6` foi respeitado e é
  verificável: nada foi escrito em `.claude/skills/` nem em `.claude/agents/` deste repositório, e as
  contagens do kit seguem em **8 agentes e 11 skills** nos dois guardas. Teste novo
  `test_tf_apply_alvo_usuario_cria_diretorio_intermediario_e_nao_toca_irmao`
  (`tests/test_materializar.py`), que prova o `apply` criando `skills/<nome>/` inexistente no destino
  sem tocar irmão não declarado — suíte de **68 para 69**, sem perda. Ordem do ato cumprida
  (copiar → declarar → `apply --alvo usuario` **no-op**, respondendo "ja atualizado" → `drift --alvo
  usuario` em exit 0). Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode validate`,
  `kit_check -Mode check-drift`, `check-readme.ps1` com os 16 guardrails inalterados, `dead_code.py`
  com 0 achados). Sem bump, sem tag e sem linha de `CHANGELOG.md`, e nenhum ponteiro de doutrina
  tocado — as duas coisas são escopo da `T7` e da `T8`. Nenhum achado fora de escopo.
  **Desvio de fila, registrado:** o bullet da `RPC-T5` declarava a **`RPC-T11`** como próxima, e esta
  sessão despachou a `T6` por ler o `(7/11)` do índice como se a `T11` estivesse fechada, sem
  verificar. A `T11` **continua aberta** — medido nesta sessão: `kit_root_placeholder()`
  (`.claude/tools/materializar.py:70-74`) ainda devolve caminho relativo e o `.claude/settings.json`
  vivo ainda grava `python .claude/tools/ocupacao.py`, que é o defeito do `TK-49`. Sem retrabalho: a
  `T6` só acrescenta pares de arquivo sob `{HOME_CLAUDE}` e não toca comando de hook, de modo que as
  duas tarefas são ortogonais. **Próxima tarefa:** **`RPC-T11`** (o `TK-49`) — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11`.
  Consumo: ver `docs/telemetria.tsv`.

- **`RPC-T11` — `{KIT_ROOT}` resolve para caminho absoluto — 2026-08-18.** Fecha o `TK-49` na origem:
  `kit_root_placeholder` (`.claude/tools/materializar.py`) passa a devolver `kit_root.as_posix()`, e o
  `command` gravado no `settings.json` do alvo `projeto` deixa de depender do cwd da chamada de
  ferramenta. Nome da função preservado; a docstring que afirmava "nunca o caminho físico absoluto"
  passa a afirmar o oposto, com a razão (o destino é local de máquina — `.gitignore:3` —, e o cwd não
  é garantido), e o parágrafo correspondente da docstring de módulo acompanha. A regra de topologia
  migrou para `_kit_marker_prefix(kit_root)`, privada, que devolve o marcador **relativo**
  (`.claude/kit` ou `.claude`) e passa a alimentar `is_kit_command`: sem ela a classificação por
  substring leria a entrada relativa já instalada como hook não-kit, a preservaria ao lado da nova e
  deixaria o hook defeituoso vivo. `_referenced_file`, `check`, `drift` e o alvo `usuario` intocados.
  Testes: quatro asserções migradas de literal para caminho derivado da fixture `tmp_path` — e **não
  seis**, como o dossiê previa: os dois setups em forma relativa (`hook_antigo.py`, `obsoleto.py`)
  continuam válidos justamente porque o marcador de classificação permaneceu relativo, o que os torna
  cobertura da compatibilidade retroativa e não dívida. Dois testes novos:
  `test_tf_apply_grava_command_absoluto_e_arquivo_referenciado_existe` e
  `test_tr_apply_substitui_entrada_de_kit_relativa_antiga_por_absoluta_unica` (regressão do `TK-49` —
  destino com a entrada relativa antiga sai do `apply` com **uma** entrada só, a absoluta). Suíte de
  **69 para 71**, sem perda. **Correção de número no dossiê:** ele partia de 68 → 70; o piso real era
  69, elevado pela `RPC-T6`, e o orquestrador re-derivou antes do despacho. **Correção de âncora:** o
  `obsoleto.py` estava em `:474`, não `:437`. **Ordem do ato, revista no despacho:**
  `test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply` (`tests/test_materializar.py`) chama
  `apply` contra o repositório real, de modo que rodar a suíte inteira já reescreve o `settings.json`
  vivo da sessão — a execução rodou primeiro `-k "not repositorio_real"` (18 verdes), depois provou à
  mão `python <abs>/.claude/tools/ocupacao.py` a partir de cwd fora da raiz (exit 0), e só então o
  `apply` real (`settings: atualizado`) e o `drift --alvo projeto` real (exit 0). Bateria do §3 item 6
  inteira em exit 0 (`kit_check -Mode validate`, `-Mode check-drift`, `check-readme.ps1`,
  `dead_code.py` com 0 achados). O `settings.json` resultante difere do anterior **apenas** no
  `command` do hook (`python D:/workspaces/PantonicApp/.claude/tools/ocupacao.py`). Sem bump, sem tag
  e sem linha de `CHANGELOG.md`. Nenhum achado fora de escopo. Com este fechamento a ordem do §5 está
  restabelecida. **Próxima tarefa:** **`RPC-T7`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T7a` — os ponteiros da doutrina publicada para artefato global — 2026-08-18.** Primeira das
  duas fatias da `T7`, **partida por orçamento no gate de delegação**: a varredura `~/.claude`
  re-derivada no despacho mediu **14 write-clusters** contra o limite de 8, e o dossiê foi cortado em
  `T7a` (doutrina publicada: `GOVERNANCA.md`, `README.md`, `.claude/README.md`) e `T7b` (kit
  executável: `.claude/skills/**`, `.claude/agents/**`). Sem mudança de rota, de escopo ou de
  proibições — o texto do `### T7` continua valendo para as duas. Nesta fatia, 6 write-clusters:
  `GOVERNANCA.md` `:113` (ponteiro da auditoria de consumo), `:175` (Regra 3), `:252-254` (governança
  das memórias, que citava só "canônica no kit", sem caminho) e `:402` (Regra 7) passam a nomear o
  canônico em `.claude/global/`; `README.md:824-825` e `.claude/README.md:35-38` (o `context-scout`,
  promovido na `T6`) idem, na forma canônico + ponto de carga da `GOVERNANCA.md:211`. Quatro
  ocorrências foram **classificadas e mantidas** por serem menção legítima ao ponto de carga —
  `:116` (o ponto de carga é o contraexemplo do argumento), `:197` (a linha que define a classe),
  `:201` (o enunciado do invariante) e `:211` (já na forma correta) —, e as sete remanescentes estão
  justificadas uma a uma no relatório da tarefa: nenhuma trata `~/.claude` como residência. Bateria
  do §3 item 6 inteira em exit 0 (`kit_check -Mode validate` e `-Mode check-drift`,
  `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **71 passed**, sem perda. Sem bump,
  sem tag e sem linha de `CHANGELOG.md` (a entrada única do plano é escopo da `T8`). Nenhum achado
  fora de escopo. **Próxima tarefa:** **`RPC-T7b`** — mesmo dossiê
  (`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7`), fatia do kit executável: âncoras
  vivas em `.claude/skills/scrum-master/SKILL.md:18,309`, `.claude/skills/proximo-passo/SKILL.md:10,49,145`
  (`:27` e `:31` são `~/.claude/projects/<slug>/memory/`, ponto de carga legítimo),
  `.claude/skills/handover/SKILL.md:8` e `.claude/skills/modelo-por-fase/SKILL.md:10,51` — a `:10`
  ainda declara o hook "fora deste repo", o que a `T5` derrubou; `.claude/agents/*.md` mediu 0
  ocorrências.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T7b` — os ponteiros da `proximo-passo` para artefato global — 2026-08-18.** Segunda das
  três fatias da `T7`. A varredura re-derivada no gate mediu **10 write-clusters** vivos contra o
  limite de 8, e a fatia do kit executável foi partida de novo, por orçamento e sem mudança de rota,
  escopo ou proibições: `T7b` = `.claude/skills/proximo-passo/SKILL.md` e `T7c` = `modelo-por-fase`,
  `handover` e `scrum-master`. A re-derivação também corrigiu duas afirmações do fechamento da
  `T7a`: a `:31` da `proximo-passo` **não** é ponto de carga de memória — é ponteiro para
  `~/.claude/docs/GOVERNANCA_MEMORIAS.md`, que tem canônico no kit —, e o item 3 do `### T7`
  (caminho canônico nas invocações de `context-prep`/`context-scout`) mora neste arquivo e não
  constava da lista. Nesta fatia, 5 write-clusters, todos textuais: `:10`, `:49` e `:145` passam a
  nomear `.claude/global/CLAUDE.md`; `:31` passa a `.claude/global/docs/GOVERNANCA_MEMORIAS.md`; e a
  **primeira** menção de `context-scout`/`context-prep` (`:70`) ganha os canônicos
  `.claude/global/agents/context-scout.md` e `.claude/global/skills/context-prep/SKILL.md` — as
  menções seguintes não repetem o caminho, porque o texto da skill é pago em todo turno de quem a
  invoca. Uma ocorrência **classificada e mantida**: `:27`, o `<memory-dir>`
  `~/.claude/projects/<slug>/memory/`, ponto de carga do harness sem canônico possível no kit.
  Nenhuma etapa do procedimento mudou. Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode
  validate` e `-Mode check-drift`, `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **71
  passed**, sem perda. Sem bump, sem tag e sem linha de `CHANGELOG.md` (escopo da `T8`). Nenhum
  achado fora de escopo. **Próxima tarefa:** **`RPC-T7c`** — mesmo dossiê
  (`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7`), últimos 5 clusters do kit
  executável: `.claude/skills/modelo-por-fase/SKILL.md:10` (ainda declara o hook "fora deste repo",
  o que a `T5` derrubou) e `:51`, `.claude/skills/handover/SKILL.md:8`,
  `.claude/skills/scrum-master/SKILL.md:18,309`; `.claude/agents/*.md` mediu 0 ocorrências.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T7c` — os ponteiros das três skills restantes do kit executável — 2026-08-18.** Terceira e
  última fatia da `T7`, que fecha a tarefa: com ela nenhuma superfície executável do kit trata
  `~/.claude` como residência de conteúdo do framework. Cinco write-clusters, todos textuais. O
  primeiro é o único com **fato derrubado**: `modelo-por-fase/SKILL.md:8-12` declarava o hook de
  enforcement como "fora deste repo, não versionado no kit", o que a `RPC-T5` desfez ao promover os
  quatro hooks globais a canônicos — passa a nomear
  `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` com `~/.claude/hooks/` citado como
  projeção. Os outros quatro (`modelo-por-fase:51`, `handover:8`, `scrum-master:18` e `:309`) trocam
  `~/.claude/CLAUDE.md` por `.claude/global/CLAUDE.md` na forma nua, seguindo a convenção que a
  `T7b` fixou e que foi conferida na fonte antes de editar: o ponto de carga só acompanha a
  **primeira** menção de cada arquivo, porque o texto de skill é pago em todo turno de quem a
  invoca. Nenhuma etapa de procedimento mudou. A varredura de fechamento do item 4 do `### T7`
  deixa **8 ocorrências vivas**, justificadas uma a uma: `modelo-por-fase:11` (a projeção que o
  cluster 1 produziu, resultado pretendido), `proximo-passo:27` (`<memory-dir>`, ponto de carga do
  harness sem canônico possível), `GOVERNANCA.md:116` (contraexemplo do argumento), `:197` (linha
  que define a classe), `:201` (enunciado do invariante), `:211`, `README.md:825` e
  `.claude/README.md:37` (as três já na forma canônico + projeção pela `T7a`, não reeditadas).
  Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode validate` — 8 agentes, 11 skills, 20
  entradas canônicas —, `-Mode check-drift`, `check-readme.ps1` com 16 guardrails × 14 seções,
  `dead_code.py` com 0 achados) e suíte em **71 passed**, piso mantido — a tarefa não cria teste,
  por ser edição textual de skill. Sem bump, sem tag e sem linha de `CHANGELOG.md` (escopo da `T8`).
  Nenhum achado fora de escopo. **Próxima tarefa:** **`RPC-T8`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T8`.
  Consumo: ver `docs/telemetria.tsv`.

---

## P-0736 — Custo do pickup

> **Índice (texto integral do campo Título, migrado da tabela ativa em 2026-08-23):** Custo do pickup — mede por fonte o que uma retomada ingere, ranqueia e lista rotas candidatas; termina antes da decisão da rota (nível 2). 5 tarefas `CPK-T1..T5`, 3 executadas; `T4`/`T5` **sem objeto** — o plano fecha como **lições aprendidas** (decisão do dono, 2026-08-22) e é insumo da rodada de consolidação da `EXECUCAO-AUTONOMA`
>
> *(Âncora original do índice, preservada:* `docs/plans/P-0736-custo-do-pickup.md` *)*

**Objetivo:** medir, por fonte lida num pickup típico, o que a retomada ingere antes da primeira
delegação; ranquear do maior ao menor e listar, para cada fonte, a rota candidata (condensar ·
substituir por ponteiro · gerar por instrumento · mover ao histórico). Autorado sob o **nível 2** da
regra escalonada de 2026-08-21: **termina antes da decisão da rota de correção** — nenhuma tarefa
daqui corrige o fluxo. A decisão e a implementação nascem no `P-0737`, depois da avaliação do dono.

**Plano:** `docs/plans/P-0736-custo-do-pickup.md` — 5 tarefas (`CPK-T1..T5`), decisões `DC-1..DC-9`
fechadas no ato. Relatório em `docs/CUSTO_DO_PICKUP.md`. Sem bump e sem tag (`DE-7`).

**Próxima tarefa da sprint:** nenhuma — **o plano fecha como lições aprendidas** (decisão do dono,
2026-08-22, no ato da `CPK-T4`). A `T4` como escrita (ratificar rota por fonte) e a `T5` ficam **sem
objeto**: o orçamento do `proximo-passo` está abolido como custo transitório. Sobrevive como insumo
da rodada de consolidação: o método (`DC-2` definição operacional · `DC-3` chars · `DC-4` sonda
programática) e três medidas válidas para **qualquer** contexto de orquestração — custo fixo de
entrada de 33.932 chars (43,8%) antes de tocar fonte do projeto; append-only lido integral para
drenar quase nada; seção terminal ocupando o kanban ativo. Medida nova colhida no mesmo ato:
`.claude/skills/scrum-master/SKILL.md` tem **21.660 chars**, maior que a maior fonte do pickup
medido — é ele o custo fixo do contexto que se quer fixo. A `T12` do `P-0734` fica **decidida pela
forma (b)** (`proximo-passo` descontinuada, responsabilidade herdada pelo `scrum-master` de contexto
fixo, que orquestra mecanicamente os contextos dos agentes que instancia); a decisão entra na rodada
em vez de ser aplicada isolada.

- **Fechamento do plano — 2026-08-22.** Célula do índice conciliada com o veredito: `in-progress`
  (3/5) → `done`, com `T4`/`T5` registradas como sem objeto. O relatório `docs/CUSTO_DO_PICKUP.md`
  (162 linhas, `## 1`..`## 6`) permanece como medida durável; a `## 7` prevista pela `DC-6` não
  existe porque a avaliação do dono substituiu a pergunta em vez de respondê-la. Nenhuma rota da
  `## 5` foi implementada — invariante 1 preservada até o fim.

**Notas de execução:**

- **Registro do plano — 2026-08-22.** Linha do `_INBOX.md` de 2026-08-21 drenada ao índice; o plano
  foi autorado nesta rodada (a linha do inbox precedeu o arquivo). Ancoragem medida no próprio
  pickup e levada ao §0 do plano: diário com 2.471 linhas / 307.541 chars, célula do `P-0734` no
  índice com 10.528 chars numa única linha, `_INBOX.md` com 22.213 chars lidos para drenar 1 linha.
  Consumo: ver `docs/telemetria.tsv`.
- **`CPK-T1` `done` — 2026-08-22.** Sonda programática descartável no scratchpad; `docs/CUSTO_DO_PICKUP.md`
  publicado com as `## 1`/`## 2` (71 linhas de 80). Orçamento medido do pickup típico: **98.313 chars
  ingeridos (~24.578 tokens)**. Maior gap arquivo × ingerido: o diário (299.643 × 5.859), cujas seções
  `P-0734` e `Índice` somam 265.365 de 296.977 chars. Recortes: `H5` com 3 de 6 seções sem status vivo,
  `H3` com 39 linhas `Próxima tarefa` (4.358 chars). Três achados de divergência doc × medida no
  `docs/DOC_MAP.md`, registrados sem conserto (invariante 1). Estouro de teto: 31 tool uses contra 20
  — tarefa-investigação com 15 fontes fixas e 5 recortes num único script. Consumo: ver
  `docs/telemetria.tsv`.
- **`CPK-T2` `done` — 2026-08-22.** Entrega encontrada **já materializada** no pickup seguinte, sem
  bullet nem linha de telemetria: a sessão que a executou encerrou antes do fechamento. Verificação
  refeita pelo orquestrador contra o dossiê e aprovada — `## 3` + `## 4` em 40 linhas de ≤50
  (`docs/CUSTO_DO_PICKUP.md:73-112`), 11 passos tabelados (`0a`..`0e`, `P1a`..`P1c`, `P2`, `P3a`,
  `P3b`), e a soma dos **10 obrigatórios** fecha exatamente no número único declarado: **77.457
  chars (~19.364 tokens)**. As cinco hipóteses com veredito numérico: `H1` confirmada (diário
  ingerido 5.859 de 299.643 chars), `H2` **parcial** (mecanismo confirmado, volume diverge — 212 de
  231 linhas sem marca `[drenado]`, não "zero ou uma"), `H3` **refutada** (o grep exato do roteiro
  devolve **1** match, não ~200 — o ponteiro é estável), `H4` confirmada (33.932 chars, 43,8% do
  total, antes de tocar qualquer fonte do projeto), `H5` confirmada (`P-0735` ocupa 27.300 chars,
  9,1%, no diário ativo). Dois achados fora de escopo, registrados sem conserto: (a) o relatório
  passou a carregar **dois totais com o mesmo rótulo** — 98.313 chars por fonte (`## 2`, `T1`) ×
  77.457 por passo obrigatório (`## 3`), delta de 20.856 —, e conciliá-los é insumo direto da `T3`,
  que propõe o orçamento-alvo sobre esse número; (b) `TK-50`, o instrumento da série não expressa o
  caso que a própria doutrina prescreve. Consumo: ver `docs/telemetria.tsv` (linha `nao_medido` —
  telemetria vencida, sem `<usage>` recuperável).
- **`CPK-T3` `done` — 2026-08-22.** Executada **inline pelo orquestrador** (classe `redacao`,
  designada Opus no dossiê; sem delegação). `## 5` + `## 6` em **49 linhas de ≤50**, relatório inteiro
  em **162 de ≤200**; as 23 fontes da `## 2` aparecem uma vez cada, com rota do conjunto fechado da
  `DC-7`. O achado (a) da `T2` — dois totais com o mesmo rótulo — foi **conciliado na própria `## 5`**:
  a coluna `ingerido` passa a ser o valor refinado da `## 3` (fatia efetiva), com as duas divergências
  declaradas (diário 5.859→311; `diario-de-obras/SKILL.md` 16.178→870), de modo que os % somam sobre
  os 77.457 e a base do alvo é única. Rotas propostas: `gerar-por-instrumento` para as duas maiores
  (`_INBOX.md` 27,8% e dossiê do plano corrente 25,7%), `condensar` para `proximo-passo/SKILL.md`
  (19,5%), `CLAUDE.md` global (12,3%) e o índice do diário, `ponteiro` para as memórias indexadas
  (11,0%), `manter` para as 15 restantes. Alvo proposto: **40.000 chars (10.000 tokens)** — 5% da
  janela, 10% do teto de trabalho —, redução exigida de **37.457 chars (−48,4%)**, que as duas maiores
  fontes entregam sozinhas (41.377 chars). Entrada do relatório publicada no `docs/DOC_MAP.md`.
  Achado registrado sem conserto (invariante 1): o passo `P3a` modela a apuração da fila em 150 chars
  por grep de âncora, mas o índice — 83.162 chars, célula máxima de 10.528 — é lido para status,
  âncora e denominador, então o orçamento medido é **piso, não teto**; este próprio pickup cruzou o
  teto de ocupação antes do fechamento. Consumo: ver `docs/telemetria.tsv`.

---

## Índice — hooks migrados em 2026-08-23

> Células da coluna *Título* do índice ativo que excederam 200 chars e cujo plano não
> tem seção `## <ID>` própria no diário (o detalhe vive em `docs/plans/`) — texto
> integral preservado aqui pela `CTX-T6a`.

### P-0730-V2I — Estágio 5

Estágio 5 — identidade do framework: agnosticismo a stack/plataforma, CA+DDD, perfis e o README como contrato canônico (`T1..T11c` entregues; `T12` reprovou por identidade e derrubou a `DR-2`; `T13..T16` absorvidas)

*(Âncora original do índice, preservada:* substituído por `docs/plans/P-0731-v2-extracao-modalidade.md` *)*

### P-0731-V2E — Estágio 6

Estágio 6 — extração da camada de modalidade: o conceito de perfil sai do hub, desktop e container viram ramificações próprias, fechamento pelo **congelamento da versão em `0.0.0`** (`DE-7`, 2026-08-07 — a `DE-4`/`3.0.0` foi revogada) (`V2E-T1..T11`, com `T3` partida em `T3a`/`T3b`/`T3c` e `T4` em `T4a`/`T4b`/`T4c` e `T6` em `T6a`/`T6b` por orçamento, `T5` em `T5a`/`T5b` por plano não-pronto e `T9` em `T9a`..`T9e` na reescrita do dossiê; 21/21)

*(Âncora original do índice, preservada:* `docs/plans/P-0731-v2-extracao-modalidade.md` *)*

### P-0732-V2P — Estágio 7

Estágio 7 — as portas do core e a camada de casos de uso: contrato de porta para as 8 portas de runtime + superfície de entrada e execução assíncrona, residência do caso de uso (`plugins/<nome>/use_case.py` + campo `use_case` no manifesto) e as duas declarações de aderência "não auditado" fechadas com o medido (`V2P-T1..T10`; `DI-1..DI-8` todas de planejamento; 10/10)

*(Âncora original do índice, preservada:* `docs/plans/P-0732-v2-portas-do-core.md` *)*

---

## Tíquetes avulsos — 3ª condensação (2026-08-23)

| ID | Título | Status | Âncora |
|---|---|---|---|
| TK-01 | Corrigir residência de `modelo-por-fase` em `GOVERNANCA.md` §3 e no bullet `V2M-T1` do `CHANGELOG.md` (ainda apontam `~/.claude/skills/`, superado por `DM-7`) | done *(absorvido pela `V2M-T3`)* | `docs/DIARIO_HISTORICO.md#tíquetes-avulsos--condensado-em-2026-08-01` |
| TK-02 | `.claude/sync-kit.ps1`: `Get-ExcludedKeys`/`Test-Excluded` quebram sem `kit-exclude.txt` presente (achado pré-existente, `V2K-T11`) | done | docs/DIARIO_HISTORICO.md#tíquetes-avulsos--2ª-condensação-2026-08-01 |
| TK-05 | Skill `checar-versao-kit`: o gatilho de revisão de doutrina (`GOVERNANCA.md` §7.1) compara só o componente MINOR e fica cego ao atravessar um MAJOR (local `2.0.0` × última rodada `1.4.0` ⇒ "sem pendência" indevido). **Resolvido por remoção do mecanismo** (`DE-8`, 2026-08-07): o gatilho de revisão deixa de pender de versão e passa a pender do fechamento de um plano, então a comparação de MINOR — e com ela a cegueira ao atravessar um MAJOR — sai do procedimento. Execução na `V2E-T9c`; a distinção MAJOR × MINOR/PATCH da checagem de **versão**, que é outra coisa, permanece intacta | done *(achado do planejamento do `P-0730`; fechado pela `DE-8`, execução na `V2E-T9c`)* | `docs/plans/P-0731-v2-extracao-modalidade.md` §8 |
| TK-06 | `docs/DOC_MAP.md` lista `GOVERNANCA.md` entre os "docs abaixo de 500 linhas (Read direto)", mas o arquivo já está em **644 linhas** — o mapa manda ler integralmente um doc que passou do limite e não tem entrada de âncoras. Drift pré-existente (já >500 antes da `V2I-T5`); corrigir criando a entrada de navegação da GOVERNANCA no DOC_MAP | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `docs/DOC_MAP.md:7-9` |
| TK-04 | `.claude/agents/pantonic-executor.md:20` hardcoda "orçamento esperado ~≤40 tool uses" — diverge de `DR-C`/`V2K-T16` (o kit, `GOVERNANCA.md` §3, já é a única autoridade numérica, tabela de tetos por classe; o global perdeu o número na `T17`) | cancelled *(absorvido pelo P-0737, fecha na AUT-T9)* | `.claude/agents/pantonic-executor.md:20` |
| TK-07 | `check-readme.ps1` só indexa seções que casam `^## (\d+)\. ` — seção `##` **não numerada** (o glossário da `V2I-T11b`) fica invisível às cinco checagens, inclusive à exigência de `> Fonte da verdade:`; decidir se o guarda passa a cobrir seção não numerada ou se a regra vale só para as numeradas | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `.claude/checks/check-readme.ps1:58` |
| TK-08 | "Estágio" (subdivisão de iniciativa) estrutura toda a `PANTONIC-V2` mas não tem residência normativa — não está em `GOVERNANCA.md` nem em skill; decidir se vira conceito com regra de abertura/fechamento ou permanece convenção do diário | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `docs/DIARIO_HISTORICO.md#sprint-pantonicv2--consolidação-do-framework-em-v2` (bullet `V2I-T11b`) |
| TK-10 | `docs/DIARIO_DE_OBRAS.md` em 937 linhas, muito além do gatilho de ~500 da operação "Condensar" — as seções dos estágios 1 a 4, todas terminais, deveriam estar em `docs/DIARIO_HISTORICO.md` | done *(fecha na `DHB-T1`: seção terminal migrada para o histórico, diário em 78 linhas)* | `docs/plans/P-0733-divida-do-hub.md` `### T1` |
| TK-09 | Skill de redação de documentação — todo doc publicado que a IA escreve vem contaminado por **narrativa de proveniência**: relato das conversas com o dono, episódio que motivou cada procedimento, ID de tarefa/estágio no corpo do texto. Vício de escrita, não defeito de um documento; precisa de critério reexecutável | done *(skill `redacao-doc` autorada em 2026-08-06; aplicação ao README é a `V2I-T11c`)* | `.claude/skills/redacao-doc/SKILL.md` |
| TK-11 | `ARQUITETURA_PANTONICA.md` §9 ("Condições de POC integrável"), bullet do TaskRunner, cita "(§10)" apontando para a seção MVVM/Threading que a `V2E-T3a` extraiu para a doutrina; a renumeração das seções seguintes fez `§10` existir de novo (agora "Operações de OS e IN/OUT", conteúdo não relacionado), então a referência aponta para um número válido mas semanticamente errado. Resolvido pelo orquestrador na mesma rodada: o ponteiro de seção foi removido (`sempre TaskRunner;`) — a doutrina extraída vive em pasta fora do versionamento e não pode ser destino de referência do hub, e a regra se sustenta afirmada inline. A frase "UI thread" do mesmo bullet é escopo da `V2E-T3b` | done *(achado da `V2E-T3a`, fechado em 2026-08-06)* | `ARQUITETURA_PANTONICA.md` §9, bullet TaskRunner |
| TK-12 | `.claude/skills/audit-sweep/SKILL.md`, `description` do frontmatter, ainda cita "pyside6" como um dos tipos de varredura ("arch, pyside6, cleancode, fora-da-caixa") — residual fora dos blocos `ARCH-mvvm`/`DDD-pureza`/`PYSIDE` que a `V2E-T4b` já havia extraído; a `V2E-T4c` mediu ao verificar o total do kit (Grep caiu de 9 para **1**, não para 0) e não o tocou por estar fora dos três arquivos-alvo daquela fatia | done *(fechado pela `EXA-T43` em 2026-08-12: a `description` passou a citar a frente **DDD** no lugar de "pyside6", como ocorrência de classe (b) da sanitização contra a matriz)* | `.claude/skills/audit-sweep/SKILL.md:3` |
| TK-13 | Carregar `.claude/checks/dead_code.py` por caminho via `importlib.util.spec_from_file_location`/`exec_module` (padrão exigido pela `T5a` porque `.claude/checks/` tem ponto no nome e não é pacote importável) grava bytecode em `.claude/checks/__pycache__/`; `.gitignore` não tem entrada para `__pycache__/`, então o diretório aparece como untracked em todo `git status` após rodar `python -m pytest` — adicionar o padrão ao `.gitignore` | done *(fechado pelo orquestrador na mesma rodada, 2026-08-06: `__pycache__/` + `*.pyc` no `.gitignore` — consequência mecânica da suíte recém-criada, edição de risco zero)* | `.gitignore` |
| TK-14 | O framework nunca foi lançado em público: não existe `V0`/`V1`/`V2`, e todo o trabalho até aqui é o desenvolvimento da **primeira** versão (veredito do dono na `V2E-T8`). A consequência para o `README.md` já foi aplicada (§15 removida), mas a premissa atinge a `T9` do `P-0731`, cujo dossiê manda escrever `CHANGELOG.md` §3.0.0 com instrução de migração: decidir se o registro de histórico de alterações se mantém como artefato de distribuição (5 consumidores materializam o kit por versão) ou se cai junto com a numeração de versões. **Decidido pelo dono em 2026-08-07:** o número de versão **fica** como artefato, congelado em **`0.0.0`** até que ele decida publicar — antes do lançamento a numeração não tem valor, e só passa a ter depois; o `CHANGELOG.md` permanece (ver `TK-15`). A `T9` deixa de fechar `3.0.0` e passa a fechar o congelamento. Superfícies a reconciliar, medidas: `VERSION` e `.claude/KIT_VERSION` (paridade checada por `kit_check.ps1 -Mode validate` e pela checagem 3 do `check-readme.ps1`); `README.md:3` e `README.md:829`, as duas linhas que o guarda exige; `README.md` §13, onde o bump obrigatório a cada mudança canônica, a tag `kit-v<versão>` (colide com número congelado) e os quatro desfechos da checagem de versão perdem função; `GOVERNANCA.md` §9, fonte da verdade do §13; a skill `checar-versao-kit`, que passa a reportar sempre "versões iguais" — e torna o `TK-05` sem objeto enquanto durar o congelamento; `docs/CONSUMIDORES.md` e os 5 consumidores, para quem a deriva deixa de ser detectável por versão e passa a depender de `-Mode check-drift`. Ponto que o replanejamento precisa fechar antes de a `T9` ser performável: o que acontece com o que já foi numerado — as entradas `§1.x`..`§2.0.0` do `CHANGELOG.md` e as tags `kit-v*` já publicadas — sob um número que volta a `0.0.0`. **Fechado em 2026-08-07 pela reescrita do dossiê da `T9`:** a `DE-4` (fechamento em `3.0.0`) foi revogada, entrou a `DE-7` — o número congela em `0.0.0` e o que já foi numerado **permanece** como histórico de desenvolvimento pré-lançamento (as 8 tags `kit-v*` não são tocadas, as seções `1.0.0`..`2.0.0` do `CHANGELOG.md` não são reescritas, e `[Não lançado]` vira a única seção viva) —, e a `T9` virou `T9a`..`T9d` | done *(achado da `V2E-T8`; consumido pela reescrita do dossiê, 2026-08-07)* | `docs/plans/P-0731-v2-extracao-modalidade.md` `### T9` |
| TK-15 | `.claude/skills/redacao-doc/SKILL.md` §5 abre a classe **"Seção histórica declarada"** — uma seção do doc publicado cujo assunto *é* a mudança entre versões, com o vício `V7` liberado. Essa isenção é o que manteve a §15 do `README.md` viva por três rodadas de redação: a varredura mecânica do §6 não acusa nada nela (medido na `V2E-T8`: 0 ocorrências de `V1`,`V2`,`V4`,`V6`,`V7`,`V8`,`V10` no README antes e depois do corte). Decidir se a classe sai da skill ou se ganha condição de existência explícita. **Decidido pelo dono em 2026-08-07:** a classe **sai**. O histórico ganha residência num documento de finalidade estrita, e esse documento é o **`CHANGELOG.md`** que já existe, isento das restrições de redação do agente. Doc publicado não é lugar de histórico, e as restrições de padronização de escrita valem nele **sem exceção** — o `README.md` inclusive. A skill perde a linha do meio da tabela do §5 (a classe passa a ter duas entradas: **publicado**, com `V1..V10` proibidos, e **registro**, isento) e o §4 continua apontando "o que mudou entre versões → `CHANGELOG.md`" | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `.claude/skills/redacao-doc/SKILL.md` §5 |
| TK-16 | A porta de saída de guardrail (`GOVERNANCA.md` §7.1) pendura o gatilho de revisão no **fechamento de um MINOR do kit**. Com a versão congelada em `0.0.0` (`DE-7`) nenhum MINOR fecha e o gatilho não dispara — a `V2E-T9a` declara a suspensão no próprio §7.1 —, de modo que enquanto durar o congelamento o framework **só adiciona regra** e nenhuma pode sair: exatamente o apodrecimento que a §7.1 existe para impedir. Escolher o gatilho substituto é decisão de doutrina do dono. **Decidido pelo dono em 2026-08-07 (`DE-8`):** o gatilho deixa de pender do fechamento de um MINOR e passa a pender do **fechamento de um plano** (`P-NNNN` → `done` no índice deste diário) — preserva a intenção original (revisão atrelada a marco real de evolução, nunca a calendário) sem depender de um número que deixou de andar, apoiada num evento que já existe, já é registrado no índice e teve historicamente a mesma cadência dos MINORs. Recusadas: cadência por contagem de tarefas concluídas (mede volume, não marco) e suspender a revisão até o lançamento (é o apodrecimento que a §7.1 existe para impedir, e o congelamento não tem prazo). Escopo, janela da pergunta e transição passam a ser contados em **rodadas**. Execução: `V2E-T9b` (doutrina §7.1), `V2E-T9c` (procedimento da skill) e `V2E-T9e` (espelho no README). **Fechado em 2026-08-07 pela `V2E-T9b`:** a §7.1 passou a pender do fechamento de plano, com escopo, janela da pergunta, transição e registro contados em rodadas — o gatilho volta a disparar sob número congelado, que é o objeto do tíquete; o espelho (`T9e`) e o mecanismo executável (`T9c`) seguem como fatias do `P-0731` | done *(achado da reescrita do dossiê da `V2E-T9`, 2026-08-07; decidido e executado no mesmo dia)* | `docs/plans/P-0731-v2-extracao-modalidade.md` §8 |
| TK-17 | `GOVERNANCA.md` é doc da classe **publicado** (`redacao-doc` §5), onde `V3` (id de processo) e `V7` (datação viva) são proibidos com piso de aceite zero, mas o corpo fora da §10 concentra 25+ ocorrências: datas explícitas em §3 (L106, L118, L137-144), ids de tarefa e plano em §7 (L459, L474-476, L498, L511, L520, L523), §7.1 (L546, L577, L585-592) e §9 (L619-624, L630). Parte é razão legítima enunciada como fato medido (`redacao-doc` §3 — a evidência que sustenta o limiar), parte é proveniência pura. A §10 foi saneada na `V2E-T9a` e serve de referência de forma. **Decidido pelo dono em 2026-08-07: limpar tudo** — nenhuma ocorrência de `V3`/`V7` sobrevive no arquivo, nem as que enunciam razão como fato medido; a regra que a medição sustentava é afirmada inline, sem ponteiro de proveniência (padrão do `TK-11`), e a medição continua registrada onde é histórico (plano, diário, `CHANGELOG.md`). Piso de aceite da varredura do §6 sobre o arquivo inteiro passa a **zero**; a §10 é a referência de forma. Recusada a alternativa de preservar caso a caso o fato medido: o critério por seção era o próprio custo a evitar. **Precondição decidida em 2026-08-08:** o bloco *Registro das rodadas* da §7.1 é registro por desenho — o rótulo `<P-NNNN> — <AAAA-MM-DD>` é o mecanismo, não proveniência — e esta limpeza o apagaria; ele sai da `GOVERNANCA.md` primeiro (`TK-22`), e só depois o piso zero de `V3`/`V7` vale para o arquivo inteiro **sem exceção**, como decidido. Sem essa ordem, a limpeza precisaria de uma isenção por bloco — exatamente o que o `TK-15` acabou de remover da skill | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `docs/plans/P-0731-v2-extracao-modalidade.md` `## Achados da execução` |
| TK-18 | **Revisão final do espelho do `README.md`.** O `check-readme.ps1` verifica que cada seção declara uma `> Fonte da verdade:` existente, mas não compara o **texto** do espelho com o da fonte — a fidelidade do conteúdo é responsabilidade de quem executa a tarefa, e um par fiel hoje pode divergir em silêncio numa edição futura. Medido na `V2E-T9e`: o parágrafo do apodrecimento em `README.md` §10 espelha `GOVERNANCA.md` §7.1 e foi conferido à mão, sem guarda executável; o dossiê daquela fatia já previa a ausência de guarda e atribuiu a conferência à execução. Escopo: varrer o espelho inteiro (as 14 seções com `Fonte da verdade` declarada) contra as fontes correspondentes, e decidir o que fica sob guarda executável e o que permanece sob conferência humana. Achado de mesma natureza descoberto durante a construção acumula neste tíquete em vez de abrir tíquete novo. **Decidido pelo dono em 2026-08-07:** é revisão **final** — executa só ao término das operações de construção, nunca no meio delas; revisar espelho enquanto as fontes ainda mudam é conferir duas vezes o mesmo texto | cancelled *(absorvido pelo P-0737, fecha na AUT-T10)* | `.claude/checks/check-readme.ps1`; `README.md` §10 |
| TK-19 | Teto de bullet do diário na skill `handover` (gatilho de condensação) estava em ~10 linhas e era estourado por 100% dos bullets da sprint (`V2E-*` em 20-30 linhas; `V2P-T1` em ~30) — regra nunca cumprida é regra errada, não prática errada. **Decidido pelo dono em 2026-08-07: ajustar o teto ao real**; recusadas "manter e cumprir" (desloca o detalhe de fechamento para fora do kanban sem impedir o crescimento) e "deixar como está" (teto nominal ignorado). O gatilho de ~500 linhas do diário inteiro permanece intacto e continua sendo o controle de tamanho, junto do `TK-10` | done *(achado da `V2P-T1`; fechado pelo orquestrador na mesma rodada — edição de 1 linha em skill)* | `.claude/skills/handover/SKILL.md:41` |
| TK-20 | `.claude/skills/integrar-poc/SKILL.md:23` nomeia a **implementação de referência como se fosse a regra** — "estado via `PathsService`; trabalho pesado via `TaskRunner`" —, resíduo da mesma classe que a `V2P-T2` removeu dos outros artefatos do kit, mas fora dos três arquivos-alvo daquele dossiê. Não tem "UI thread" (por isso escapou da varredura da `T2`); o desvio é citar nome de componente do case onde a doutrina deveria citar a porta (raiz de dados e execução assíncrona). Corrigir para o vocabulário de portas da `ARQUITETURA_PANTONICA.md` §4 | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `.claude/skills/integrar-poc/SKILL.md:23` |
| TK-21 | O ratchet do **piso comportamental** roda **sem alvo em toda parte**: no hub, `ratchet_piso.py` entra na bateria de fechamento de toda tarefa mas reporta sempre `exit 0 — nenhum piso declarado`, porque `tests/piso_comportamental.txt` nunca foi criado (nem depois de a `V2E-T5a` dar suíte ao hub); nos consumidores, `.claude/checks/` não existe (`0/6` materializam o kit — medido em `docs/CONSUMIDORES.md`, confirmado por `Test-Path` no `PantonicVideo`). O guardrail do piso (`GOVERNANCA.md` §7 item 6) foi **retido com caso citável de registro**, não pelo check — o check é vacuidade, e a §7.1 diz que check neutralizado não isenta. Decidir se o hub declara piso próprio para a suíte que já tem, se o ratchet passa a rodar contra o consumidor por `--root`, ou se o piso é reconhecido como regra procedimental sem enforcement executável. **Decidido pelo dono em 2026-08-08:** o ratchet passa a rodar **contra o consumidor**, por `--root` — é onde o piso tem objeto, porque o hub não tem código de produção. Recusadas: declarar piso próprio no hub (protegeria 3 asserções de um repositório sem produção — cobre o lugar errado) e reconhecer o piso como regra procedimental sem enforcement (deixaria o item 6 de §7 dependente de caso citável em toda rodada futura, marcável por ausência de atividade no consumidor e não por morte da regra). O que a execução precisa resolver, medido nesta rodada: `tests/piso_comportamental.txt` **não existe** no `PantonicVideo` (o piso comportamental do consumidor ainda precisa ser autorado, uma frase por comportamento), e falta fixar onde a invocação com `--root` mora — bateria de fechamento do hub, skill `guardrails-check` ou fechamento de tarefa do próprio consumidor | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `.claude/checks/ratchet_piso.py`; `GOVERNANCA.md` §7 item 6 |
| TK-24 | `P-0733` tem **12 tarefas não iniciadas** cujo cabeçalho (`[Opus]`/`[Sonnet]`) não carrega `classe` nem `teto`, e portanto fica fora do esquema fixado pela `DP-C`. Retrofit é **ato de planejamento**, não de execução — a classe é escolhida no dossiê antes de delegar (`GOVERNANCA.md` §3) —, e a `EXA-T4` não edita outro plano. Escopo: completar os 12 cabeçalhos para `### <ID> — <título> [<modelo> · classe <slug> · teto <N>]`, com `<slug>` no conjunto de cinco e `<N>` igual ao teto da classe. Não bloqueia nada: `rdo.py` (`EXA-T8`) nasce com o caminho de plano legado por desenho | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `docs/plans/P-0733-divida-do-hub.md`; `docs/plans/P-0734-execucao-autonoma.md` `### DP-C` |
| TK-22 | O bloco *Registro das rodadas* (`GOVERNANCA.md` §7.1) ganha **residência própria**, num documento de finalidade estrita isento das restrições de redação, e a §7.1 passa a apontar para ele. **Reuso do `CHANGELOG.md` verificado e recusado em 2026-08-08**, por três medidas: (1) `CHANGELOG.md:3` declara como objeto as **mudanças notáveis** do framework, e o resultado normal de uma rodada é **0 marcações** — não-mudança que a §7.1 exige registrar mesmo assim ("revisão sem registro não aconteceu"); registro cujo caso comum é "nada mudou" não cabe num changelog; (2) a chave de organização do `CHANGELOG.md` é a **versão** e a do registro é o **fechamento de plano** — sob o congelamento tudo cai em `[Não lançado]`, e quando o congelamento acabar essa seção vira uma versão numerada, fatiando o registro entre seções de versão de forma permanente, quando o mecanismo precisa de lista contígua onde "última" e "penúltima rodada" sejam localizáveis; (3) o registro é **lido por mecanismo** — `.claude/skills/checar-versao-kit/SKILL.md:83-84` faz Grep por `Registro das rodadas` em `GOVERNANCA.md` §7.1 e confronta a última rodada com o índice deste diário. O `CHANGELOG.md` continua ganhando entrada quando a rodada **produzir** mudança (guardrail marcado ou removido) — aí sim é mudança notável. Superfícies medidas para a execução: `GOVERNANCA.md` §7.1 (o bloco mais a prosa que diz "a lista abaixo", L558 e L600) e a skill `checar-versao-kit` (L83-84); `README.md` **não** referencia o bloco (L701 espelha só o parágrafo do apodrecimento) e `docs/DOC_MAP.md` ganha o doc novo. **Bloqueia o `TK-17`** | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `GOVERNANCA.md` §7.1; `.claude/skills/checar-versao-kit/SKILL.md:83-84` |
| TK-25 | `docs/RESIDENCIA_DOUTRINA.md:89` (seção **Regra 3**, item 3.5) aponta "§7 item 8 ('docs grandes via índice')" quando esse conteúdo é do **item 7** — o mesmo drift de numeração que a `EXA-T6b` corrigiu na nota da seção "Regra 2", mas em seção fora dos alvos daquele dossiê, por isso não corrigido junto. Escopo: trocar a referência para "§7 item 7" e conferir se as demais faixas de linha citadas pelo documento acompanharam as edições que já ocorreram em `~/.claude/CLAUDE.md` | cancelled *(podado pelo critério do P-0737 §5, 2026-08-22)* | `docs/plans/P-0734-execucao-autonoma.md` `## Achados da execução`; `docs/RESIDENCIA_DOUTRINA.md:89` |
| TK-26 | `docs/telemetria.tsv` usa duas formas distintas de sentinela para "métrica não medida" nas 3 linhas com `fonte=nao_medido` medidas na `EXA-T7`: célula vazia (`V2K-T17`, `V2K-T19`) e traço literal `-` (uma linha com `fonte=contado`, `V2I-T3`) — sem convenção fixa entre as duas. `.claude/tools/telemetria.py` (`EXA-T7`) exige número válido em `tool_uses`/`tokens_k`/`duracao_s` em toda chamada `append` e não aceita nenhuma das duas formas — decisão deliberada de escopo mínimo (dossiê da `T7` só cobre linha válida/`fonte` inválida/campo numérico não numérico/preservação byte a byte, nenhum teste de sentinela). Decidir a convenção única (célula vazia **ou** `-`, nunca as duas) e se `append` passa a aceitá-la é escopo de tarefa própria — sem isso, uma tarefa futura com `fonte=nao_medido` não tem como registrar consumo pelo script novo. **Decidido pelo dono em 2026-08-08:** a sentinela única é a **célula vazia**, e o `append` passa a aceitá-la nas três colunas numéricas **apenas** quando `fonte=nao_medido` — é a forma majoritária da série, é a que um leitor de TSV por `split('\t')` já trata como ausência, e o `-` obrigaria todo consumidor futuro do arquivo a conhecer uma regra extra. Recusadas: padronizar em `-` (sentinela visível, mas empurra a regra para todo leitor) e não aceitar sentinela alguma (manteria a edição manual do TSV justamente no caso que a `EXA-T7` existiu para eliminar). Escopo da execução: `telemetria.py` aceita célula vazia nas colunas numéricas; teste de regressão para aceitação e para recusa; **1** linha histórica com `-` (`docs/telemetria.tsv:50`, `V2I-T3`, `tokens_k` e `duracao_s`) normalizada para célula vazia — única exceção à regra "só apende", por ser correção de sentinela, não de número. **Medido na ratificação (2026-08-08, corrige a contagem do achado):** a célula vazia aparece em **14** linhas e o `-` em **1**; das 14, **11 têm `fonte=contado`** (`tool_uses` preenchido, `tokens_k`/`duracao_s` vazios) e só 3 têm `nao_medido` — de modo que restringir a aceitação de vazio a `fonte=nao_medido` impediria o script de reproduzir a forma dominante da própria série. **Ponto aberto fechado em 2026-08-11, por delegação do dono ao orquestrador** (questão operacional, não tática): a célula vazia é aceita nas três colunas numéricas **sempre que `fonte` ≠ `usage`**. `usage` significa que o número veio do bloco `<usage>`, que carrega os três — célula vazia ali é medida **perdida**, não medida ausente, e deve falhar ruidosamente; `contado` e `nao_medido` são exatamente os casos em que parte ou todo o número não existe. A regra reproduz a forma dominante da série (11 linhas `contado` com `tool_uses` preenchido e as outras duas vazias) sem forçá-la, e não exige que o consumidor do TSV conheça combinação nenhuma além de "vazio = ausente". **Evidência nova da mesma rodada:** a linha `EXA-DPG-replan` (`fonte=contado`) **não pôde ser apendada pelo script** e foi escrita à mão — o defeito já não é hipotético sobre `nao_medido`, é bloqueio medido no caminho comum | cancelled *(absorvido pelo P-0737, fecha na AUT-T5)* | `.claude/tools/telemetria.py`; `docs/telemetria.tsv:17,40,42,50` |
| TK-27 | A independência do `pantonic-reviewer` é **parcial na lista de ferramentas**: `Write`, `Edit` e `NotebookEdit` estão fora, mas `Bash` é necessário para invocar `rdo.py laudo` e, sem escopo, permite escrita arbitrária no repositório — o "por construção" do critério de pronto da `EXA-T10` fica sustentado pela ausência das ferramentas de edição mais a proibição em prosa, não pela impossibilidade técnica plena. Não resolvido na tarefa porque escopar o comando no campo `tools:` do frontmatter é sintaxe não documentada para agentes: se o harness ignorar o especificador, o reviewer perde `Bash` inteiro e não emite laudo nenhum. Escopo: (a) confirmar empiricamente se `tools:` aceita especificador de `Bash`, ou (b) impor o escopo por regra de permissão de projeto — a escolha entre as duas é do dono | cancelled *(absorvido pelo P-0737, fecha na AUT-T5)* | `.claude/agents/pantonic-reviewer.md` (frontmatter `tools:`) |
| TK-28 | `docs/plans/P-0734-execucao-autonoma.md` `### T19` não fecha a lacuna que a própria `DP-D` (§9) deixou aberta sobre a origem do parâmetro `status` de `calcular_desdobramento` depois que o pacote de 8 campos sai (`D2`, "pacote não existe"): `D5` separa o que "passa ao laudo" (`A5`/`A6`/`A8`/`A9`) do que "permanece no loop" (`A1`/`A2`/`A4`/`A7`/`B1`-`B3`) e **omite `A3` (bloqueado)` das duas listas**, sem dizer se `close` ainda recebe algum equivalente a `--status` ou se a assinatura de `calcular_desdobramento` (reusada sem mudança declarada, `:589`) muda. Segunda lacuna do mesmo dossiê: `D1` aponta `pendencia_para_o_dono` para "retorno do executor (campo opcional) ou laudo", mas o `### T19` não lista um flag para esse canal opcional nem instrui removê-lo. Replanejar o dossiê da `T19` (fechar as duas lacunas) antes de redelegar. **Fechado em 2026-08-11 pela rodada de replanejamento**, as duas lacunas por derivação de cláusula já ratificada, sem decisão nova do dono: (1) o `status` é materializado onde a `DP-D` já o alocou — `laudo --status` obrigatório com domínio fechado grava `**Status:**` no documento de laudo, e o `close` lê de lá; `calcular_desdobramento` **não** muda assinatura nem corpo (ponteiro corrigido de `:589` para `:624`); recusada a derivação do `status` a partir do veredito, que contraria `D1` e tornaria `bloqueado` inalcançável; (2) `A3` não estava em nenhuma das duas listas do `D5` porque é o único caso com **condição** e **ação** em lados diferentes — a condição foi ao laudo por `D1`, a ação é do loop como todo o bloco A —, registrado como nota de derivação datada no §9, subordinada à `DP-D` e sem tocar o texto ratificado; (3) `close` ganha `--pendencia`, opcional, uma linha, único argumento de conteúdo, com a composição do campo fixada em tabela de 4 linhas | done *(achado do bloqueio da `EXA-T19`; fechado pelo replanejamento de 2026-08-11)* | `docs/plans/P-0734-execucao-autonoma.md` `## Achados da execução`, `### T19`, `### DP-D` (§9, `D1`/`D2`/`D5`) |
| TK-30 | Três fatos normativos sobre `superseded` ficaram **sem residência** quando a `EXA-T23a` substituiu o bullet *Status válidos* de `.claude/skills/diario-de-obras/SKILL.md` pela residência única: que ele é **terminal**, que **condensa para o histórico** e que **sai do backlog** (não é escolhível). A `DP-F` não reenuncia nenhum dos três — ela só posiciona `superseded` como estado exclusivo de plano/iniciativa, e sua máquina de transições é de tarefa, sem nenhuma aresta para `superseded`. O executor agiu certo ao não inventar a regra (a residência única enuncia só o ratificado), então os três fatos ficaram órfãos. Escopo: decidir se a `DP-F` ganha as arestas e propriedades de `superseded` no vocabulário de plano/iniciativa, ou se isso é escopo da reescrita da `T27`; a decisão precede a edição. Enquanto pendente, a regra continua afirmada nos demais pontos do arquivo que citam `superseded` (planos derivados, convergência). **Segunda ocorrência medida pela `EXA-T25`** (2026-08-13), do lado de fora do arquivo: ao espelhar a lista final no `README.md` §7, mediu-se que `superseded` consta da `### Alcance por objeto` da residência única mas está **ausente da `### Lista final` e da `### Máquina de transições`** — o único estado terminal de plano não tem gatilho de entrada nem aresta na fonte da verdade, e por isso o espelho o enuncia sem poder apontar transição. Nenhum tíquete novo: é a mesma lacuna deste tíquete, medida por outra superfície, e a decisão continua sendo a que ele já pede — arestas na `DP-F` ou escopo da reescrita da `T27`. **Decidido pelo dono em 2026-08-13:** as arestas e propriedades de `superseded` no vocabulário de plano/iniciativa são **escopo da reescrita da `T27`**, e a `DP-F` não se reabre. As arestas são de **plano**, não de tarefa, e a `DP-F` foi ratificada como decisão de tarefa: reabri-la para acrescentar um vocabulário paralelo custaria uma ratificação a mais sem destravar nada, enquanto a `T27` já passa pelo mesmo texto. A decisão precede a edição, e agora precede | cancelled *(absorvido pelo P-0737, fecha na AUT-T8)* | `.claude/skills/diario-de-obras/SKILL.md` `## Status — residência única`; `docs/plans/P-0734-execucao-autonoma.md` `### DP-F` |
| TK-29 | `calcular_desdobramento(status, veredito, bloqueante, orcamento_estourado)` recebe `bloqueante` e **nunca o usa** no corpo (`.claude/tools/rdo.py:624-644`) — parâmetro morto na fronteira do `G-DEADCODE`. Medido no replanejamento da `EXA-T19` e **deliberadamente não corrigido lá**: aquele dossiê declara que a assinatura não muda, e mexer nela no meio do rewire do `close` misturaria duas mudanças. **Decidido em 2026-08-11 pela rodada da `DP-G`, por derivação:** o parâmetro **sai**, e com ele sai também o `status`. A `DP-F` fixou que o RDO nasce de **uma única transição** (`review` → `done`), então tarefa bloqueada ou reprovada nunca chega ao `close` e os ramos `bloqueado`/`reprovado` ficam inalcançáveis — ramo morto testado é o que o `G-DEADCODE` proíbe. A assinatura passa a `calcular_desdobramento(veredito, orcamento_estourado)`, com dois ramos e a precedência do estouro sobre o veredito. Recusada a leitura oposta (a dominância de dimensão bloqueante deveria estar no corpo): `DA-6` já garante que `bloqueante` ≠ `nenhuma` implica `veredito=reprovado`, de modo que a informação não se perde | done *(executado na `EXA-T19`, item (c) do dossiê: assinatura encolhida para `(veredito, orcamento_estourado)`, ramos `bloqueado`/`reprovado` removidos, `dead_code.py` exit 0)* | `docs/plans/P-0734-execucao-autonoma.md` `### T19`; `.claude/tools/rdo.py:624-644` |
| TK-31 | `docs/plans/P-0734-execucao-autonoma.md:678`, dentro do **dossiê da `T23a`** (tarefa já executada), instrui "Registrar que o `status` é escrito **exclusivamente pelo `scrum-master`**" — última ocorrência afirmativa do absoluto que a `DP-G` derrubou, e a única fora das quatro superfícies que a tabela do item 5 da `DP-G` mediu. Efeito prático nulo (o artefato que aquele dossiê governa, a residência única, já foi corrigido pela `EXA-T28`), mas o texto do dossiê ficou dessincronizado da decisão vigente. Não corrigido na `T28` por desenho: os invariantes daquela tarefa proíbem tocar superfície fora das quatro e reabrir tarefa, e reescrever dossiê de tarefa fechada para acompanhar decisão posterior invalida registro (`DP-G5`). Escopo: reconciliar. **Decidido pelo dono em 2026-08-11** (`§12` do plano): no desenvolvimento do framework o último entendimento é canônico e reescreve a orientação anterior que ele contradiz — dossiê de tarefa executada é orientação, não registro, e se concilia; o que narra o ocorrido (bullet de fechamento, RDO, telemetria, histórico) permanece intacto. **Executado na rodada de replanejamento da `DP-H` (2026-08-11):** o bullet do dossiê da `T23a` passou a enunciar a fronteira da `DP-G` — o `scrum-master` é o único que **materializa** o `status`, o executor é **autor** de `review` e `blocked` —, com a conciliação datada e apontada para a `DP-H`; o artefato que aquele dossiê governa já estava corrigido pela `T28`, e nenhum registro do ocorrido foi tocado | done *(fechado por conciliação na rodada da `DP-H`; achado da `EXA-T28`)* | `docs/plans/P-0734-execucao-autonoma.md` `### T23a` |
| TK-44 | O dossiê de evidência mecânica (`.claude/tools/review_evidence.py`) **não discrimina escopo** enquanto a iniciativa inteira está sem commit: na revisão da `EXA-T13` ele leu o alvo declarado `.claude/tools/` como caminho literal ("sem diferença coletável — arquivo ausente na árvore de trabalho") e listou como *tocados* os **59** arquivos de toda a árvore não commitada do `P-0734`, produzindo "59 arquivos fora dos alvos" sem relação com a tarefa julgada. A camada declarada **autoridade sobre escopo** fica sem poder discriminante, e o conjunto real de arquivos da tarefa teve de ser reconstruído pelo `reviewer` fora do dossiê. Escopo: decidir se a atribuição de diff a tarefa passa a se apoiar em outro recorte (commit por tarefa, marco por tarefa, ou diff contra um ponto de referência gravado no despacho) e se o alvo declarado como **diretório** vira caso tratado em vez de caminho literal | cancelled *(absorvido pelo P-0737, fecha na AUT-T5)* | `.claude/tools/review_evidence.py`; `docs/RDO/evidencia/P-0734-T13.md` |
| TK-33 | Três referências órfãs em `.claude/skills/scrum-master/SKILL.md`, todas em superfície que **nem a `T21a` nem a `T21b` podiam tocar** — os passos 1, 7, 8 e 10 foram explicitamente fencados pelo *Cuidado* da `T21a` e não estão nos arquivos-alvo da `T21b`, e a `T21b` declara `A1`/`A2`/`A7` inalterados: (1) `:153`, o gatilho do **passo 8**, cita "passo 5 concluído (regras `A1`..`A5`)" quando `A5` deixou de existir e as regras avaliadas depois do passo 5 passaram a ser `A1`, `A2`, `A3a`, `A3b` e `A4` — deveria ler `A1`..`A4`; (2) o **passo 7** (*Leitura do veredito*) extrai só `veredito`, `bloqueante` e o caminho do laudo, e **não extrai a `recomendacao`** que `A6`, `A8`, `A9` e `B1` agora leem — o campo é lido pelas tabelas sem que nenhum passo o colha; (3) a proibição *"Não abre o RDO nem o laudo"* contradiz o passo 9 entregue pela `T21a` (que extrai o `pacote` de cinco campos do laudo) e as regras `A6`/`B1` (que extraem a recomendação) — a fronteira entre "não abrir o corpo" e "extrair o pacote" precisa ser enunciada em vez de proibida. Resíduo correlato, deliberadamente preservado: `A2` ainda diz "pacote ausente ou inválido (campo faltando, teto de campo estourado)", vocabulário da era do pacote, porque o dossiê da `T21b` fixa "`A1`, `A2` e `A7` não mudam" e a `T31` cobre o resíduo de `pacote` em outros três arquivos. Escopo: reconciliar os três pontos (mais a acepção de `pacote` em `A2`) numa passada só sobre os passos 7 e 8 e a seção `## Proibições`. **Item 3 decidido pela `DP-M` (ratificada pelo dono em 2026-08-11):** não há fronteira a enunciar — a proibição **sai sem substituta**, porque com `Observações` fora do gerador (`EXA-T38`) o laudo só tem campo fechado ou calculado e não sobra nada a extrapolar; os passos 7 e 9 leem o laudo por desenho. **Item 2 fechado por derivação na mesma decisão:** a `recomendação` é campo fechado do laudo e é de lá que o passo 7 a colhe — o retorno de duas linhas do `reviewer` não muda e nenhum campo novo é criado. **Itens 1, 2 e 3, mais o resíduo de `A2`, passam a ser cobertos pela `EXA-T39`**, numa única passada no arquivo | done *(fechado pela `EXA-T39` em 2026-08-12, os três itens mais o resíduo de `A2`: (1) o gatilho do passo 8 passou a ler `A1`..`A4`; (2) o passo 7 passou a colher a `recomendação` do laudo e sua saída virou a tripla `veredito`/`bloqueante`/`recomendação`, que o passo 8 recebe, sem nada acrescentado ao retorno de duas linhas do `reviewer`; (3) o bullet "Não abre o RDO nem o laudo" saiu de `## Proibições` sem fronteira substituta, por `DP-M`; mais `A2` reenunciada como "retorno ausente ou inválido", só o termo, condição e encaminhamento idênticos; achado da `EXA-T21b`)* | `.claude/skills/scrum-master/SKILL.md:153` (passo 8), `### Passo 7`, `## Proibições`; `docs/plans/P-0734-execucao-autonoma.md` §16.4 e `### T39`; `### T21a` (*Cuidado*) e `### T21b` |
| TK-34 | O dossiê de delegação não colava as **âncoras** do ponto a editar nem o **range do bullet de fechamento anterior**, e o executor pagava a localização em tool uses. Série medida no bloco da `DP-M`: `EXA-T37` fechou em ~19/15 e `EXA-T38` em 20/15, os dois excedentes atribuídos por causa medida a localizar a bateria de verificação e o ponto de inserção no diário — não a trabalho; a `EXA-T39`, delegada com âncoras re-derivadas e o range do bullet anterior colados, fechou em **13/15**, sem cruzar o teto. Recorrência de 3 rodadas consecutivas com a correção já provada na terceira | done *(decidido pelo dono e executado pelo orquestrador na mesma rodada, 2026-08-12: o dever entrou no item 3 do gate de delegação da skill `proximo-passo` e no passo 4 da skill `scrum-master`; `kit_check` `-Mode validate` e `-Mode check-drift` em exit 0)* | `.claude/skills/proximo-passo/SKILL.md` (gate de delegação, item 3); `.claude/skills/scrum-master/SKILL.md` (`### Passo 4`) |
| TK-35 | `.claude/agents/pantonic-executor.md:60` manda o executor "atualize o diário (`review`/`done`)" — o executor **materializa `done`**, e a `DP-G` fixou que ele é **autor** de `review` e `blocked` e de mais nada, cabendo a materialização em qualquer estado só ao `scrum-master`. Não é vocabulário (a `EXA-T24` traduziu o termo e parou aí, por invariante), é **conteúdo de regra**, e nenhuma tarefa viva o cobre: a `T26` alcança `GOVERNANCA.md`/rubrica/arquitetura e a `T27` alcança kanban e planos vivos. O que a execução precisa fechar junto: **quem escreve o bullet de fechamento do diário** quando o executor deixa de escrevê-lo — hoje ele o escreve inteiro, incluindo o marcador `— done`, e as rodadas recentes já dividiam o ato (executor escreve o bullet, orquestrador escreve índice, `Próxima tarefa` e telemetria) | done *(achado da `EXA-T24`; fechado pela `DP-N` e executado na `EXA-T40`, 2026-08-12)* | `docs/plans/P-0734-execucao-autonoma.md` §17 e `### T40` |
| TK-36 | **Reorganizar a passagem de bastão.** As skills `handover` e `proximo-passo` viram **uma única skill nova**, que executa a transição de tarefas suavemente — inclusive a passagem do contexto que precise ser herdado de tarefa predecessora — e que tenha coerência com as responsabilidades do `scrum-master` **sem exigir responsabilidade nova**; se responsabilidade nova se mostrar necessária, **escalar ao dono** em vez de criá-la. Aberto por decisão do dono em 2026-08-12, ao ratificar a `DP-N`: com o executor fora da escrita, a passagem de bastão é atividade crítica e merece tíquete próprio para destrinchar colaterais, em vez de ser consequência silenciosa. Superfícies medidas que **pertencem a este tíquete** e por isso ficam fora da `T41`: `README.md` §9 inteiro (*Handover e uma tarefa por contexto*), `GOVERNANCA.md:333`/`:338`/`:341`/`:342` (§4) e `:240` (cerimônias), o *enforcement* dos itens 8 e 9 do §7 ("gate de review no handover"), e o corpo das duas skills. Entre a `T41` e este tíquete a doutrina do handover descreve um encerramento que o executor não faz mais — contradição declarada, com dono e prazo. **Anotação incorporada em 2026-08-12** (decisão do dono, ao receber o achado de classe (c) da `EXA-T43`, `TK-37`): **quem escreve o checkpoint de contexto** entra no escopo desta unificação e **não se decide antes dela**. `.claude/skills/handover/SKILL.md:96-100` atribui à **Execução** escrever até 5 linhas nas *Notas de execução* do diário ao cruzar 2/3 do teto — ato real e necessário (`~/.claude/CLAUDE.md` Regra 2) que a matriz de responsabilidades não declara para esse papel e que o domínio fechado do sinal do executor (`review`, ou `blocked` com razão tipada) não carrega. Resolver a lacuna no documento atual não tem sentido: ele está na iminência de se tornar obsoleto. A skill nova declara o portador; se isso exigir responsabilidade nova, **escala ao dono**, como este tíquete já prescreve. **Natureza da skill fixada pelo dono em 2026-08-13** (`P-0734` §19, critério de aceitação final): a skill unificada é **maquinário estrito do `scrum-master`**, na superfície **agente↔agente**, e é **transparente para o gerente do projeto** — ele não a invoca, não a lê e não a acompanha. Ela prima por **eficiência e qualidade da transição**, incluindo a herança de contexto entre tarefa predecessora e sucessora, e **não é skill de comunicação com humano**; essa superfície é do `TK-38`, e os dois eixos não se misturam | cancelled *(absorvido pelo P-0737, fecha na AUT-T6)* | `docs/plans/P-0734-execucao-autonoma.md` §17.3; `.claude/skills/handover/SKILL.md`; `.claude/skills/proximo-passo/SKILL.md` |
| TK-37 | **Lacuna da matriz — quem escreve o checkpoint de contexto.** `.claude/skills/handover/SKILL.md:96-100` atribui à **Execução** escrever até 5 linhas nas *Notas de execução* do diário quando o consumo cruza 2/3 do teto. O ato é **real e necessário** (`~/.claude/CLAUDE.md` Regra 2: cruzada a capacidade, grava-se checkpoint de ponteiro de estado antes do handover), mas a matriz de responsabilidades (`GOVERNANCA.md` §3) nega à Execução escrever no diário, e o domínio fechado do sinal do executor (`review`, ou `blocked` com razão tipada) **não carrega o conteúdo do checkpoint** — de modo que hoje o ato não tem portador declarado. Ocorrência de **classe (c)** da `EXA-T43`, não editada por prescrição do item 15 (`G-SCOPE`): criar a responsabilidade no prompt seria a própria violação, e a falta é **da matriz**. Decisão do dono, entre (i) a matriz declarar o portador — Execução ganha o ato, ou o checkpoint passa a caber na Orquestração, que já escreve no diário —, ou (ii) o sinal do executor ganhar um canal para o conteúdo do checkpoint. **Encaminhado pelo dono em 2026-08-12, sem decidir o mérito:** a lacuna **não se resolve aqui** — vira **anotação no `TK-36`**, a unificação de `handover` + `proximo-passo`, porque resolver uma questão para um documento na iminência de se tornar obsoleto não tem sentido. A skill nova é que declara o portador do checkpoint; se isso exigir responsabilidade que a matriz não tem, aquele tíquete escala ao dono, como já prescreve. Este tíquete permanece indexado como o **registro do achado** de classe (c), não como decisão aberta. **Segunda ocorrência da mesma lacuna, medida pela `EXA-T44`** (2026-08-12): `GOVERNANCA.md:340-344` é a **fonte na doutrina** do texto que a skill repete — atribui à Execução gravar o checkpoint intermediário ao cruzar 2/3 do teto —, registrada como `#46` do §2 do relatório e **não editada** pela mesma prescrição do item 15. Nenhum tíquete novo foi aberto: é a mesma lacuna em outra superfície, e essa superfície já está dentro do recorte do `TK-36`, que lista `GOVERNANCA.md:341`/`:342` entre as suas; as duas se resolvem no mesmo ato | cancelled *(absorvido pelo P-0737, fecha na AUT-T6)* | `.claude/skills/handover/SKILL.md:96-100`; `GOVERNANCA.md` §3 (matriz), §7 item 15 e `:340-344`; `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md` §1 (`#27`) e §2 (`#46`) |
| TK-39 | **O critério de aceitação não pode ser contagem de acionamentos do gerente.** Aberto por decisão do dono em 2026-08-13, corrigindo o §19 do `P-0734` autorado no mesmo dia. **Enunciado do dono:** um valor numérico de vezes que o gerente é acionado durante a execução de um plano **não tem sentido prático** — ou é sem valor, ou, virando controle, é **arbitrário**, porque não existe forma de derivar esse limite de coisa alguma. A responsabilidade do gerente **sempre** será dirimir ambiguidades e resolver conflitos, sobretudo de **requisitos** e de **aceitação**, e é **risco fatal** o agente decidir aspecto de aceitação sem estar **inequivocamente** seguro de que é a melhor solução — de modo que ele não pode ser limitado num aspecto-chave do projeto por métrica arbitrária. **Critério que entra no lugar:** é entrega **ineficiente** quando o framework solicita acionamento do gerente em **caminho feliz ou caminho natural**, sem pendência e sem demanda que seja dele. Exemplo dado pelo dono: parar para que ele limpe o contexto e invoque a tarefa seguinte — o plano corre sem problema e ele está mediando **execução normal**, que é exatamente a ineficiência que o framework existe para eliminar. A aceitação passa a classificar cada acionamento **pela causa**, nunca pelo número: causa que é do gerente é legítima e ilimitada; caminho feliz é defeito. Superfície: artefatos do framework (doutrina em `GOVERNANCA.md` §4.3, a skill que conduz o loop) mais o §19, a `T16` e a `T17` do `P-0734` | done *(decisão do dono, 2026-08-13; quitado pela `EXA-T45`, card prioritário à frente da `T29`)* | `docs/plans/P-0734-execucao-autonoma.md` `### T45` e §19; `GOVERNANCA.md` §4.3 (`:312-346`) e §3.1 (`:201`); `.claude/skills/scrum-master/SKILL.md` |
| TK-40 | **A tabela de riscos do `P-0734` ainda promete a medida que a `T16` deixou de fazer.** Achado fora de escopo da `EXA-T45`, indexado pelo orquestrador. A mitigação do risco *"o dono perder consciência situacional ao sumir o round-trip por tarefa"* (§6, `:2000`) diz que *"a `T16` mede quantos round-trips de fato desapareceram — se o custo for cegueira, o piloto mostra"*. É **mitigação viva**, não registro histórico: descreve o que uma tarefa ainda não executada vai fazer. Com a `T16` reescrita para **registrar cada acionamento pela causa**, sem contagem, a linha promete um instrumento que não existe mais, e o risco fica sem mitigação verificável. A `EXA-T45` não a corrigiu porque o dossiê declarou a tabela de riscos do §6 **fora do alvo, como história** — recorte correto para as ocorrências que narram ratificações já ocorridas, e errado para esta. **Escopo:** reescrever a mitigação para se apoiar no registro qualitativo por ocorrência (o RDO continua sendo o instrumento compensatório de `DA-5`), sem reintroduzir contagem. Edição de uma linha, sem decisão pendente | done *(achado medido na `EXA-T45`; quitado como ocorrência de classe (b) dentro da `EXA-T47`, 2026-08-13)* | `docs/plans/P-0734-execucao-autonoma.md` §6 e `### T16` |
| TK-41 | **A `DP-B` prescreve paradas que o §19 pode classificar como acionamento em caminho feliz.** Duas ocorrências de classe (c) medidas pela `EXA-T47` na consolidação do plano; nenhum dos textos envolvidos foi tocado, conforme o `G-EXECREADY`. **Decisão do dono, owner-gated.** A `DP-B` (política de autonomia, tetos e escalada, ratificada em 2026-08-08) manda o loop **parar** em duas situações, e o §19 (critério de aceitação, enunciado em 2026-08-13) diz que acionamento do gerente em caminho feliz ou natural é ineficiência da entrega, bastando **uma** ocorrência. **(1) Estouro de teto (`A4` × invariante 5 do §3 × §19):** a `A4` manda PARAR para replanejamento em todo estouro, o regime interino do §3 item 5 diz que teto é **alarme, nunca bloqueio**, e o §19 reprova parada de caminho feliz. Leitura 1 — a `A4` governa o loop depois da entrega e o invariante 5 só protege o executor, de modo que as duas convivem; leitura 2 — a `A4` é parada de caminho natural e o regime interino a esvaziou. Agrava que a matéria de uso e teto está desdobrada para plano próprio (`T17` item 4; a `DP-L` não se forma neste plano). **(2) Fim de janela (`B2` × §19):** a `B2` encerra a janela por teto e PARA, chamando isso de "encerramento normal", enquanto o §19 diz que o dono **inicia o plano e nada mais** e que a skill **cria os contextos novos** sozinha — sendo o dono invocar a continuação o caso exemplar de ineficiência. **Por que é do dono:** é conflito entre dois enunciados dele, sobre requisito e sobre aceitação, e a escolha muda o que a `T16` mede e o que a `T17` aprova. **Bloqueia `T16` e `T17`; não bloqueia `T29`/`T30`** (matéria disjunta) | done *(decidido pelo dono em 2026-08-13 — os dois itens pelo mesmo princípio: teto arbitrário não governa fluxo; materializado pela `DP-Q` (§21) e pelo bloco `EXA-T49`..`T52`)* | `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md` (classe (c), `c1`/`c2`); `docs/plans/P-0734-execucao-autonoma.md` `### DP-B`, §3 item 5 e §19; `.claude/skills/scrum-master/SKILL.md` (`A4`, `B2`) |
| TK-42 | **Resíduo de entendimento derrubado fora dos universos declarados da `DP-P`.** Dois achados da `EXA-T48`, ambos de forma classe (b) mas em artefatos que o dossiê não declarou no universo. **(1)** `tests/test_review_evidence.py`, docstring de `test_escopo_violado_gera_fato_sem_inventar_parcial`, ainda cita *"pacote de retorno"* — objeto morto desde a `DP-H`; a `T48` corrigiu as três menções vivas em `.claude/tools/review_evidence.py`, e o teste ficou de fora porque `tests/` não estava no universo. **(2)** `.claude/README.md`, nota dos auditores: *"apontamentos aceitos viram tíquetes no diário via `pantonic-planner`"* — resíduo do **eixo da matriz de responsabilidades**, não do eixo dos objetivos: a rodada de 2026-08-12 (`T43`/`T44`) corrigiu os arquivos de agente e o índice do kit ficou para trás. Edição textual nos dois casos, sem mudança de comportamento e sem decisão pendente | cancelled *(absorvido pelo P-0737, fecha na AUT-T9)* | `tests/test_review_evidence.py`; `.claude/README.md` (nota dos auditores) |
| TK-43 | **O hub distribui um kit cuja configuração de hook é ignorada pelo git.** `.claude/settings.json` está em `.gitignore:3`, sob o comentário "Configuração local de máquina — nunca canônica". A `EXA-T13` registrou ali o hook do proxy de ocupação porque o dossiê `### T13` nomeia esse arquivo como alvo, e o instrumento funciona na máquina do dono — mas nada dele viaja para consumidor nenhum, e `kit_check` não o vê. A `EXA-T14` (telemetria sem turno de agente) tem o mesmo alvo e herda o mesmo defeito. **Decisão do dono, owner-gated:** é arquitetura de distribuição do kit, não execução — ou hook canônico ganha residência versionada própria, com materialização no `settings.json` local, ou o proxy de ocupação é assumido como instrumento só-do-hub, e nesse caso a condição de capacidade do §4.3 não existe para consumidor. **Bloqueia `T14`; não bloqueia o laudo da `T13` nem `T29`/`T30`**. **Decidido pelo dono em 2026-08-15:** hook canônico **ganha residência versionada própria**, com materialização no `settings.json` local. O `GOVERNANCA.md` §4.3 afirma a capacidade como condição vinculante para todo Pantonic\*, não só para o hub: assumir o proxy como instrumento só-do-hub transformaria regra publicada em regra sem meio de cumprimento nos consumidores — o apodrecimento que a §7.1 existe para impedir. Recusada a alternativa (proxy só-do-hub) por esse motivo. **Replanejamento concluído em 2026-08-15, na `DP-R` (§22 do plano):** os três pontos que estavam em aberto ficaram fechados sem decisão nova de arquitetura — residência em `.claude/hooks/hooks.json` (comando portável por `{KIT_ROOT}`), materialização por `.claude/tools/hooks_sync.py apply`, idempotente e preservando `permissions.deny` e todo hook não-kit, e `kit_check` cobrando o canônico no `-Mode validate` e a materialização no `-Mode check-drift`. Execução atribuída a **`EXA-T53`** (residência, materializador, testes e guarda) e **`EXA-T54`** (a superfície publicada: `.gitignore`, `GOVERNANCA.md` §3.1, `README.md` §11 e §13, `CHANGELOG.md`), em bloco à frente da `T29`. A `T14` deixa de estar bloqueada por dossiê: o dela foi reescrito na mesma rodada e agora depende da `T53`. **Absorvido pelo `P-0735` em 2026-08-15**, junto da regra geral de que é sub-caso: `EXA-T53` e `EXA-T54` ficam **canceladas por absorção**, o desenho da `T53` sobrevive integral nas `RPC-T2`/`RPC-T3` (manifesto único, materializador `apply`/`check`/`drift`, preservação de `permissions.deny` e de hook não-kit, ancoragem hub × consumidor, guarda no `kit_check`) e só a residência particular `.claude/hooks/hooks.json` desaparece — declaração única em `.claude/projecoes.json`, porque duas declarações lado a lado seriam a duplicata que a régua proíbe. Os hooks globais, que a `T53` não alcançava, entram na `RPC-T5`; a dependência da `T14` passa para a `RPC-T2` | done *(decidido pelo dono em 2026-08-15; absorvido no mesmo dia pelo `P-0735`; fechado pelo `P-0735` — execução em `RPC-T2`/`RPC-T3`/`RPC-T5`)* | `.gitignore:3`; `.claude/settings.json`; `docs/plans/P-0734-execucao-autonoma.md` `### T53`, `### T54`, `### T14`, §22 (`DP-R`) |
| TK-45 | **Ambiguidade estrutural de residência: o framework depende de artefatos que não viajam nele.** 5ª ocorrência medida da mesma classe (`TK-01` skill `modelo-por-fase` apontada para o global; `DR-B` de `docs/RESIDENCIA_DOUTRINA.md` §5, que adiou a promoção de 6 skills globais como "iniciativa própria" nunca aberta; `TK-21` ratchet sem alvo em 0/6 consumidores; `TK-43` hook ignorado pelo git; `permissions.deny` do guardrail 13, escalado em `DP-R` §22.5). **Medido em 2026-08-15:** vivem fora do pacote, em `~/.claude/`, 4 hooks registrados no `settings.json` global (`pytest_pretooluse`, `verbose_cmd_pretooluse`, `read_cap_pretooluse`, `modelo_por_fase_userpromptsubmit`), 6 skills (`context-prep`, `doc-map`, `lean-test`, `memory-diet`, `onboard`, `test-tiers`), 1 agente (`context-scout`) e 2 docs de doutrina (`GOVERNANCA_MEMORIAS.md`, `RECOMENDACOES_CONSUMO_GLOBAL.md`) — nenhum chega a consumidor algum, e a doutrina versionada os invoca (a skill `proximo-passo` do kit cita `context-prep`/`context-scout`; o hook global é o enforcement do §3). **Raiz:** o teste de residência (`GOVERNANCA.md` §3.1) responde *onde mora* com uma resposta só, fundindo dois eixos independentes — **autoridade** (conteúdo do framework × da máquina do dono) e **ponto de carga** (onde o harness lê). Quando o ponto de carga imposto pelo harness é global ou não-versionado, a régua obriga a escolher entre residência correta e funcionamento, e o §3.1 registra o sintoma como se fosse lei ("hook não é quinta superfície (...) e não viaja"). Pelo próprio `Prec-2` ("regra que só existe no `~/.claude` do dono não é doutrina do framework"), os 13 artefatos acima não são doutrina — e a doutrina depende deles: contradição medida, e a causa direta de comportamento inconsistente entre projetos. **Decisão do dono, owner-gated:** alcance do pacote (o kit passa a materializar também o global, ou para na fronteira do projeto). Bloqueia `EXA-T53`/`EXA-T54`, que resolvem o sub-caso do hook. **Decidido pelo dono em 2026-08-15:** o pacote passa a materializar também o `~/.claude` — CLAUDE.md global e skills/agentes globais viram projeção de canônico versionado, com residência e ponto de carga separados e a materialização projetando uma na outra. **Executado no mesmo dia, na rodada de doutrina:** `GOVERNANCA.md` §3.1 reescrito para as três classes, a pergunta zero e o `Prec-2` como invariante (a afirmação de que hook não viaja saiu), e `docs/RESIDENCIA_DOUTRINA.md` ganhou a §8 de conciliação datada, que reclassifica o que a régua nova muda sem reescrever a classificação de 2026-08-03. **Execução do mecanismo atribuída ao `P-0735`** (`RPC-T1..T9`) | done *(decidido pelo dono em 2026-08-15; doutrina publicada no mesmo dia; mecanismo executado e fechado pelo `P-0735`)* | `GOVERNANCA.md` §3.1; `docs/RESIDENCIA_DOUTRINA.md` §8; `docs/plans/P-0735-residencia-e-ponto-de-carga.md` |
| TK-46 | `README.md:352-354` (§7, modelo por fase) afirma que *"o hook de aviso fica fora do kit, por ser mecanismo de enforcement de uma regra que já mora na doutrina versionada"* — contradiz `GOVERNANCA.md` §3.1, onde a **declaração do hook é canônica e versionada** e só o arquivo de configuração que o harness lê é ponto de carga. Mesma classe das 7 edições da `RPC-T1`, mas fora dos alvos daquele dossiê. Verificar se a varredura fechada da `RPC-T7` (item 4) alcança a frase: o Grep dela é por `~/\.claude` e esta frase não cita o caminho, então provavelmente **não** — nesse caso a correção entra como alvo explícito da `T7` | cancelled *(absorvido pelo P-0737, fecha na AUT-T10)* | `README.md:352-354`; `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7` |
| TK-47 | `materializar.py apply --alvo usuario` **reescreve o `settings.json` do destino mesmo quando não há drift semântico**: o primeiro `apply` real da `RPC-T4` mudou o mtime de `~/.claude/settings.json` por normalização de serialização JSON (indentação/ordem de chaves reemitidas pelo dump), com todo o conteúdo preservado (`model`, `effortLevel`, `switchModelsOnFlag`, `statusLine`, `permissions.allow`, `additionalDirectories` intactos). Comportamento pré-existente do materializador entregue na `RPC-T2`, não introduzido pela `T4`. **Por que importa agora:** o critério de verificação da `RPC-T5` exige que o `settings.json` resultante difira do anterior **apenas** no caminho dos comandos resolvido pelo placeholder, e manda a tarefa parar em qualquer outra diferença — com a normalização em vigor, a `T5` para por um efeito que não é do escopo dela. Decidir se `apply` passa a ser byte-idempotente quando não há mudança semântica (preservar a formatação existente) ou se a normalização é aceita e o critério da `T5` é reescrito para comparar semanticamente | done *(achado da `RPC-T4`; decidido pelo dono em 2026-08-17 — `apply` byte-idempotente sob equivalência semântica; quitado pela `RPC-T10` no mesmo dia: comparação semântica em `write_settings`, 2 testes novos, suíte 65 → 67)* | `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `DL-10` e `### T10`; `.claude/tools/materializar.py:220-231` |
| TK-49 | **O hook do alvo `projeto` é materializado com caminho relativo e derruba a sessão inteira.** `.claude/projecoes.json` declara `python {KIT_ROOT}/tools/ocupacao.py` e o materializador resolve `{KIT_ROOT}` para o caminho **relativo** `.claude`, de modo que o `settings.json` do projeto registra `python .claude/tools/ocupacao.py`. Basta o cwd de uma chamada de ferramenta sair da raiz do repositório para o hook falhar — e hook `PreToolUse` que falha **bloqueia toda ferramenta da sessão** (Bash, PowerShell, Glob, Read, ToolSearch), inclusive a chamada que restauraria o cwd: sessão irrecuperável, só sai abrindo outra. Medido ao vivo em 2026-08-17, durante a verificação da `RPC-T5`. O mesmo campo minado viaja para todo consumidor que materializar o alvo `projeto`. **Decidido pelo dono em 2026-08-17:** corrigir na origem — `{KIT_ROOT}` resolve para caminho absoluto na escrita do `settings.json`, com TF em fixture `tmp_path`; recusada a alternativa de tratar como limitação operacional ("não mude o cwd"), que deixaria o defeito nascer propagado nos consumidores. **Dossiê autorado fechado em 2026-08-17** como `RPC-T11` do `P-0735`, logo depois da `T5`: `kit_root_placeholder` passa a devolver `kit_root.as_posix()`, a classificação de entrada de kit (`is_kit_command`) migra para um marcador relativo próprio — sem isso o `apply` preservaria a entrada relativa já instalada ao lado da nova, deixando o hook defeituoso vivo —, e a premissa foi verificada no ato: `.claude/settings.json` é gitignorado (`.gitignore:3`), então a portabilidade que o desenho original perseguia não tinha objeto | done *(fechado pela `RPC-T11` em 2026-08-18: `{KIT_ROOT}` grava caminho absoluto, TR de substituição da entrada relativa antiga, `apply`/`drift` reais em exit 0)* | `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11` |
| TK-50 | **`.claude/tools/telemetria.py append` não expressa o caso `nao_medido`/`contado` que a própria doutrina prescreve.** `GOVERNANCA.md` §4.2 e a skill `proximo-passo` mandam apender uma linha com `fonte: nao_medido` quando a telemetria da tarefa venceu (sessão anterior encerrou sem fechar) e `fonte: contado` na execução inline sem `<usage>` — casos em que `tokens_k` e `duracao_s` **não existem**. O validador rejeita campo vazio (`tool_uses: '' não é inteiro`, `tokens_k: '' não é numérico`) e não aceita nada além de número, então a única saída pelo instrumento é inventar `0` — número falso numa série cujo propósito é consumo medido. A série já tem o precedente da forma correta, escrito fora do instrumento (`EXA-DPS-replan`, 2026-08-19: `tool_uses` preenchido, `tokens_k`/`duracao_s` em branco). Medido ao vivo no fechamento da `CPK-T2`, cuja linha teve de ser apendida por `Add-Content` para não gravar zeros falsos. Rota candidata: campos numéricos passam a aceitar vazio quando `fonte` ∈ {`nao_medido`, `contado`}, mantendo a exigência para `fonte: usage` | cancelled *(absorvido pelo P-0737, fecha na AUT-T5)* | `.claude/tools/telemetria.py`; `docs/telemetria.tsv` |

## P-0737 — Loop autônomo

> **Condensado em 2026-09-21.** Plano terminal (`superseded` em 2026-09-18 pelo
> `P-0740-loop-de-modulos`, `DM-1`). Seção migrada verbatim do `docs/DIARIO_DE_OBRAS.md`,
> onde ficou só a linha do índice com ponteiro para cá.


> **Índice (texto integral do campo Título, migrado da tabela ativa em 2026-08-23):** Loop autônomo — o plano que consolida a `EXECUCAO-AUTONOMA`: 10 tarefas (`AUT-T1..T10`), decisões `DU-1..DU-13`, absorve as 8 tarefas abertas do `P-0734` e 11 tíquetes, poda 10 e encaminha 2; `AUT-T5` partida em `T5a`/`T5b`/`T5c` por orçamento no gate de delegação (3/12). **`superseded` em 2026-09-18 pelo `P-0740-loop-de-modulos` (`DM-1`)** — as 3 fechadas ficam como registro e as 7 abertas foram absorvidas e entregues lá (`done 35/35`). Histórico: ficou `blocked` de 2026-08-22 a 2026-09-18 por custo fixo de contexto, razão que caiu com a correção do denominador de janela para 1M; nenhum defeito do plano foi apontado
>
> *(Âncora original do índice, preservada:* `docs/plans/P-0737-loop-autonomo.md` *)*

**Objetivo (herdado verbatim da diretiva do dono, 2026-08-22):** transformar o trabalho de
`proximo-passo` num agente autônomo, capaz de rodar sozinho todas as delegações e ajustes de modelo e
entregar ao cliente o entregável do plano, sem delegar ao humano tarefa rotineira e mecânica. O plano
existe para desfazer o drift medido — instrumento, papel e doutrina em volume, e o loop nunca rodando.

**Plano:** `docs/plans/P-0737-loop-autonomo.md` — **10 tarefas** (`AUT-T1..T10`), decisões
`DU-1..DU-13` fechadas no ato do planejamento (cinco do dono, oito de planejamento). Absorve as **8**
tarefas abertas do `P-0734` e **11** tíquetes; **10** tíquetes são podados e **2** encaminhados ao
plano de contexto recomendado; `TK-38` e `TK-48` seguem vivos, sem toque. Sem bump e sem tag
(`DE-7`). **Checagem de versão do kit:** modo hub — congelada em `0.0.0`, nada a comparar.

**Ordem de execução (§7 do plano, e não a numeração):** `AUT-T1` → `AUT-T5` → `AUT-T4` → `AUT-T2` →
`AUT-T3` → **[ratificação em lote do dono, `DU-12`]** → `AUT-T6` → `AUT-T7` → `AUT-T8` → `AUT-T9` →
`AUT-T10`.

**Próxima tarefa:** **nenhuma — plano encerrado como `superseded` em 2026-09-18** (`DM-1` do
`P-0740-loop-de-modulos`). Não há fila a retomar: as **7 tarefas abertas** (`AUT-T2`, `T3`, `T4`,
`T5c`, `T6`..`T10`) foram **absorvidas e entregues** pelo `P-0740`, que fechou `done 35/35` —
`AUT-T2`/`T6`/`T7`/`T8` pela `LM-T4` (aprovado 100%), `AUT-T3`, `AUT-T4` e `AUT-T5c` pelos módulos
correspondentes, e `AUT-T9`/`AUT-T10` pela `LM-T6`. A recomendação **(a)** do §8 — o piloto medido,
única prova de que o desenho entrega o que promete — foi cumprida pela `LM-T6` com troca de
**veículo** decidida pelo dono (o corpus passou a ser a execução do próprio `P-0740` sob o loop):
está publicada em `docs/plans/P-0740-loop-de-modulos.md` › `## 10`, com **Veredito do dono:
APROVADO (2026-09-19)**. As recomendações **(b)** e **(c)** do §8 são matéria exclusivamente de
custo e encerram por obsolescência sob a diretiva de priorização de 2026-09-21 (`DM-30`).

**Reconciliação de 2026-09-21 — o que esta seção dizia e por que foi corrigida.** O flip de
2026-09-18 foi aplicado na tabela do índice, mas não aqui: a seção seguiu declarando `blocked`,
mandando a fila retomar em `AUT-T5c` (tarefa já entregue por outro plano) e argumentando contra
destravar sobre a premissa do **custo bimodal de abertura de janela** — premissa que o `P-0740`
derrubou ao medir a janela real de 1M (`## 2` daquele plano). Esse texto morto alimentou um **ponto
aberto falso** na *Diretiva de priorização* do topo deste diário, que afirmava haver trabalho de
framework parado por um critério que não vale mais. Nenhum defeito do `P-0737` foi apontado em
momento algum, e nada do registro histórico abaixo é reaberto ou reescrito — o que segue são as
notas de execução das 3 tarefas que fecharam no próprio plano (`AUT-T1`, `AUT-T5a`, `AUT-T5b`).

- **Paralisação por decisão do dono — 2026-08-22.** Registrada no ato da análise crítica do pickup da
  `AUT-T5b`. Fato medido que a originou: a tarefa consumiu **três janelas de orquestração** — (A)
  pickup pago, teto cruzado no gate de delegação **sem delegar**; (B) pickup pago, delegação
  despachada e teto cruzado **antes do retorno**, deixando o ato de fechamento órfão; (C) pickup pago
  integralmente para verificar entrega já pronta e escrever 2 edits. O trabalho real coube num único
  subagente em background. Cada janela repagou os **77.457 chars (~19.364 tokens)** que a `CPK-T2`
  mediu como pickup típico, dos quais **43,8% são custo fixo de entrada**. Diagnóstico preliminar
  levado à linha do `_INBOX.md` **sem ratificar rota**: o gate de delegação orça o teto do executor e
  não o saldo do orquestrador; o custo fixo não amortiza entre tarefas; e a verificação foi feita à
  mão, no contexto mais caro, existindo `review_evidence.py` e `pantonic-reviewer` para isso. A
  **Diretiva** deste diário foi condensada de 20 para 15 linhas no mesmo ato — o conteúdo retirado
  (drift da `EXECUCAO-AUTONOMA`, reconciliação `P-0734`/`P-0733`, recomendações do §8) não foi
  apagado: vive na linha `P-0737-loop-autonomo` do `_INBOX.md` e nesta seção.

**`AUT-T5` partida em `T5a`/`T5b`/`T5c` por orçamento — 2026-08-22, no gate de delegação.** Medidos
~12-14 write-clusters contra o limite de 8, com duas das três frentes comportamentais (mudam
contrato de CLI e assinatura de renderização). **Sem mudança de rota ou de escopo**: a partição segue
as três frentes já publicadas no dossiê, que permanece intocado, e o corte é o mesmo precedente da
`RPC-T7` do `P-0735`. Fatias: **`T5a`** = frente (a), sentinela de métrica ausente
(`.claude/tools/telemetria.py`, `docs/telemetria.tsv:50`, `tests/test_telemetria.py`), classe
`implementacao`, Sonnet, teto 40; **`T5b`** = frente (b), escopo do dossiê de evidência
(`.claude/tools/review_evidence.py`, `tests/test_review_evidence.py` e a conciliação de
`.claude/skills/scrum-master/SKILL.md:143`, que o *Conteúdo* do dossiê manda tocar e o campo
*Arquivos-alvo* omitiu), classe `implementacao`, Sonnet, teto 40; **`T5c`** = frente (c), medição do
`TK-27` e o achado no §9 do plano, **tarefa-investigação** que mede e **para** para a ratificação em
lote da `DU-12`, teto 15. O denominador do plano passa de 10 para 12.

**Notas de execução:**

- **`AUT-T5b` — done, confirmado em contexto novo — 2026-08-22.** Achado no pickup: o trabalho já
  estava materializado no working tree (agente em background da rodada anterior concluiu antes do
  retorno chegar a esta sessão — contexto anterior encerrado por capacidade sem consumir a
  notificação). Verificado, não redelegado: diff de `review_evidence.py`/`test_review_evidence.py`/
  `scrum-master/SKILL.md:143` bate exatamente com as duas frentes do dossiê (alvo-diretório por
  prefixo, `--desde <ref>`); suíte **83 passed** (piso `AUT-T5a` era 80, +3 testes novos da `T5b`).
  Consumo: ver `docs/telemetria.tsv` (`nao_medido` — notificação da sessão anterior perdida no
  `<usage>`, mesmo padrão da `RPC-T11`).
- **Checkpoint de janela — `AUT-T5b` delegada, aguardando retorno — 2026-08-22.** Dossiê montado com
  design já resolvido (alvo-diretório por prefixo, `--desde <ref>` sem tocar `DP-S`/`tarefa-corrente.json`)
  e despachado ao `pantonic-executor` em background (agentId `adb71e11660fbf127`). Contexto encerrado
  por capacidade antes do retorno. **Próximo passo:** aguardar a notificação de conclusão, fechar o
  registro (bullet + `docs/telemetria.tsv`) e seguir a ordem do §7 (`AUT-T4` depois).

- **Checkpoint de janela — pickup da `AUT-T5b` encerrado por capacidade, sem delegação — 2026-08-22.**
  Janela cruzou o teto no gate de delegação, depois do levantamento das âncoras. **Âncoras
  re-derivadas nesta rodada, para o contexto novo não repagar:** `review_evidence.py` 413 linhas —
  comparação literal de escopo em `confrontar_escopo:129-138` (`t not in alvo_set`), fallback
  "arquivo ausente na árvore de trabalho" em `_diff_para_arquivo:141-151`, recorte da árvore inteira
  em `coletar_arquivos_tocados:111-126` (`git status --porcelain=v1 --untracked-files=all`), bloco
  `argparse` em `main:362-384` (sem `--desde`), seção `## Escopo` do render em `_renderizar:272-285`
  (onde entra a declaração de recorte), chamada em `montar_documento:336`;
  `tests/test_review_evidence.py` 277 linhas; conciliação da skill em
  `.claude/skills/scrum-master/SKILL.md:143-145` (comando) — o `.claude/estado/tarefa-corrente.json`
  do passo 4 (`:88-94`) **não** tem campo de ref de git, então de onde sai o `<ref>` do `--desde` é
  ponto a fechar no dossiê. Piso da suíte (80 passed, `AUT-T5a`) **não** re-medido — a suíte não
  chegou a rodar.

- **`AUT-T5a` — done em 2026-08-22.** A célula vazia passou a ser a sentinela única de métrica
  ausente: `_validar_inteiro_nao_negativo` e `_validar_numero_nao_negativo` ganharam `permite_vazio`,
  e `build_row` valida `fonte` primeiro para propagá-lo às três colunas numéricas — com
  `fonte = usage` o vazio continua falha ruidosa, porque ali a medida é perdida, não ausente. A
  única linha histórica com traço literal (`docs/telemetria.tsv` L50, `V2I-T3`) foi normalizada, com
  o Grep de reconferência medindo 1 match antes e 0 depois e o resto do arquivo preservado. Ordem TDD
  demonstrada por `git stash` do fix: os dois testes de aceitação falharam sem ele e passaram com
  ele; o de recusa por `fonte = usage` já passava. Bateria do §3 inteira em exit 0; suíte em **80
  passed** (piso era 77 — subiu). **Reconciliação de série feita pelo orquestrador no fechamento:** a
  prova ponta a ponta exigida pela *Verificação* apende uma linha real pelo instrumento, e essa
  linha nasce auto-relatada (`fonte = contado`), o que colidiria com a linha medida da mesma tarefa;
  a célula `tarefa` da linha de prova passou a `AUT-T5a-prova-instrumento` — correção de
  identificador, não de número — e a linha canônica da tarefa foi apendada do bloco `<usage>` com
  `fonte = usage`. Nenhum achado fora de escopo. Consumo: ver `docs/telemetria.tsv`.

- **Registro do plano — 2026-08-22.** Plano autorado em contexto novo, a partir do inventário e das
  decisões que a rodada de consolidação do mesmo dia deixou na linha `P-0737-loop-autonomo` do
  `docs/plans/_INBOX.md` (agora `[drenado]`). Reconciliação de planos derivados aplicada no mesmo
  ato: `P-0734` → `superseded` (classificação B), `P-0733` → `cancelled` (`DU-1`) — a iniciativa
  volta a ter **um** plano vivo. Nenhuma questão precisou subir ao dono na autoria: as duas que
  ameaçavam abrir ramo — o portador do checkpoint de contexto (`TK-37`) e a fronteira de ferramenta
  do `pantonic-reviewer` (`TK-27`) — foram fechadas, a primeira por derivação do já ratificado
  (`DU-8`) e a segunda como medição que **para** para a ratificação em lote (`DU-12`). O agente de
  planejamento caiu por **limite de sessão da API** depois de publicar o plano e antes de fechar o
  registro no diário; retomado pelo mesmo `agentId` com o delta, sem re-delegação a frio. Consumo:
  ver `docs/telemetria.tsv` — a fatia anterior à queda não traz bloco `<usage>` e está **PARCIAL,
  não medida**.
- **Acréscimo de escopo por decisão do dono — 2026-08-22.** Achado de fronteira levantado no
  fechamento da autoria: o `P-0737` nasceu com 574 linhas, acima do gatilho de 500 do
  `docs/DOC_MAP.md`, que hoje indexa três planos grandes e não este. O dono decidiu acrescentar a
  entrada ao dossiê da `AUT-T1` (frente **(e)**) em vez de abrir tíquete ou ignorar — a `T1` já
  edita o kanban, o custo marginal é zero, e plano desse porte fora do mapa reintroduz o custo de
  navegação que o `P-0736` mediu. Único ponto do plano publicado alterado depois da publicação;
  `Arquivos-alvo`, `Invariantes`, `Verificação` e `Pronto quando` da `AUT-T1` atualizados no mesmo
  ato. Teto da tarefa mantido em 20.
- **`AUT-T1` — done em 2026-08-22.** O kanban passou a dizer a verdade do dia: as 23 células de
  tíquete do índice receberam rota única — 10 `cancelled` por poda, 11 com a nota de absorção e a
  `AUT-T<n>` que as fecha, 2 encaminhadas ao plano de contexto recomendado —, e `TK-38`/`TK-48`
  ficaram intocados. O `TK-18` teve a razão do `blocked` amarrada à `AUT-T9`. O
  `P-0734-execucao-autonoma.md` ganhou a seção `## 24. Rebase pelo P-0737` como acréscimo no fim do
  arquivo, com a tabela das 8 absorvidas e a `T16` cancelada por absorção; nenhum dossiê, bullet ou
  decision record anterior foi tocado. A frente **(e)** indexou o plano no `docs/DOC_MAP.md` com o
  porte re-derivado no ato (**586 linhas**, e não as 574 que o dossiê supunha) e padrão de acesso
  `^### AUT-T5 ` conferido por execução. As 23 anotações foram aplicadas num único passo
  programático, com guarda de 6 campos por linha da tabela — 23 edições linha a linha estourariam o
  teto da classe `mecanica`. Bateria do §3 inteira em exit 0; suíte em **77 passed**. Nenhum achado
  fora de escopo. Consumo: ver `docs/telemetria.tsv`.

- **2026-08-23 (`CTX-T6a`, item 4):** os 11 tíquetes absorvidos por este plano fecham `cancelled` no índice (preservando o ponteiro `fecha na AUT-T<n>` de cada célula) e migram para `docs/DIARIO_HISTORICO.md`: `TK-04` (fecha na `AUT-T9`), `TK-18` (fecha na `AUT-T10`), `TK-26` (fecha na `AUT-T5`), `TK-27` (fecha na `AUT-T5`), `TK-30` (fecha na `AUT-T8`), `TK-44` (fecha na `AUT-T5`), `TK-36` (fecha na `AUT-T6`), `TK-37` (fecha na `AUT-T6`), `TK-42` (fecha na `AUT-T9`), `TK-46` (fecha na `AUT-T10`), `TK-50` (fecha na `AUT-T5`).
