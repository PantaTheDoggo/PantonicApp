# Evidência de revisão — DIARIO_DE_OBRAS TK-61a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    1 +
 .../hooks/modelo_por_fase_userpromptsubmit.py      |    5 +-
 .claude/projecoes.json                             |   10 +
 .claude/skills/passagem-de-bastao/SKILL.md         |   35 +-
 .claude/skills/scrum-master/SKILL.md               |   23 +-
 .claude/tools/backlog.py                           |  489 +++-
 .claude/tools/ocupacao.py                          |   10 +-
 .claude/tools/rdo.py                               |    6 +-
 .claude/tools/telemetria_hook.py                   |   10 +-
 CHANGELOG.md                                       |   15 +-
 GOVERNANCA.md                                      |    2 +-
 README.md                                          |   33 +-
 docs/CUSTO_DO_PICKUP.md                            |   31 +
 docs/DIARIO_DE_OBRAS.md                            |  978 +++++++-
 docs/DOC_MAP.md                                    |    2 +
 docs/RDO/INDEX.md                                  |   15 +
 docs/consultant-spec.md                            |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md   |    2 +-
 docs/plans/P-0737-loop-autonomo.md                 |    2 +-
 docs/plans/P-0738-contexto-esgotado.md             |    2 +-
 docs/plans/P-0739-backlog-instrumento.md           | 2526 +++++++++++++++++++-
 docs/plans/_INBOX.md                               |    2 +-
 docs/plans/_INBOX_HISTORICO.md                     |    1 +
 docs/telemetria.tsv                                |   64 +
 tests/test_backlog.py                              |  810 ++++++-
 tests/test_materializar.py                         |   71 +
 tests/test_ocupacao.py                             |   66 +-
 tests/test_rdo.py                                  |   34 +
 tests/test_review_evidence.py                      |   37 +
 tests/test_telemetria_hook.py                      |  117 +-
 30 files changed, 5274 insertions(+), 191 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: alheio; estado git: ` M`
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/ocupacao.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: alheio; estado git: ` M`
- `CHANGELOG.md` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/Entregas Aceitas/Entregas - P-0739.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T11.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T11a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T9a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-56-TK-56a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-56-TK-56b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-57-TK-57a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-59-TK-59a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-60-TK-60a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-60-TK-60b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-60-TK-60c.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-62-TK-62a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-64-TK-64a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0739-BKL-T12.md` — atribuição: alheio; estado git: `??`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0735-residencia-e-ponto-de-carga.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0737-loop-autonomo.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0738-contexto-esgotado.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0739-backlog-instrumento.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0742-loop-fora-do-llm.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_VIABILIDADE-agente-leitor.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md` — atribuição: da entrega; estado git: `??`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_materializar.py` — atribuição: alheio; estado git: ` M`
- `tests/test_ocupacao.py` — atribuição: alheio; estado git: ` M`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`, `tests/fixtures/backlog/`
- Arquivos tocados: `.claude/README.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/ocupacao.py`, `.claude/tools/rdo.py`, `.claude/tools/telemetria_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-59-TK-59a.md`, `docs/RDO/evidencia/TK-60-TK-60a.md`, `docs/RDO/evidencia/TK-60-TK-60b.md`, `docs/RDO/evidencia/TK-60-TK-60c.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/evidencia/TK-64-TK-64a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md`, `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md`, `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_materializar.py`, `tests/test_ocupacao.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `TK-64a`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/tools/ocupacao.py` → `TK-56a`, `.claude/tools/rdo.py` → `TK-62a`, `.claude/tools/telemetria_hook.py` → `TK-56a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_materializar.py` → `TK-56a`, `tests/test_ocupacao.py` → `TK-56a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`, `tests/test_telemetria_hook.py` → `TK-56a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-59-TK-59a.md`, `docs/RDO/evidencia/TK-60-TK-60a.md`, `docs/RDO/evidencia/TK-60-TK-60b.md`, `docs/RDO/evidencia/TK-60-TK-60c.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/evidencia/TK-64-TK-64a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 10 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 43e5327..04e4be1 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -1,8 +1,10 @@
 """BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — núcleo somente-leitura do
 instrumento de backlog: carrega o índice do diário, os planos vivos e o próprio diário; monta o
-grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-9`, vocabulário fechado
-definido no card) com `arquivo:linha`; `show` emite o dossiê verbatim de um item, truncado ao teto
-`DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).
+grafo item → tarefas; `check` acusa cada violação de gramática (`C-1..C-11`, vocabulário fechado
+definido no card) com `arquivo:linha`; `resolver_citacao_secao` (`TK-60a`) resolve uma citação
+`` `<arquivo>.md` §<N>[.<N>]* `` contra o arquivo citado, acusando `C-11` quando a seção não
+existe — vocabulário do instrumento fechado em `C-1..C-11`; `show` emite o dossiê verbatim de um item,
+truncado ao teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).
 
 Gramática implementada (residência canônica: skill `diario-de-obras`, seção "Gramática legível
 por máquina" — replicada aqui igual, `DB-17`/`DB-18`):
@@ -87,6 +89,7 @@ DIRETIVA_RE = re.compile(r"^\*\*Diretiva de priorização:\*\* (.*)$")
 NIVEL_1_OU_2_RE = re.compile(r"^#{1,2} ")
 
 INDICE_LINHA_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")
+INDICE_HEADING_RE = re.compile(r"^## Índice\s*$")
 
 _TETO_CHARS = 8000
 _TETO_LINHAS = 120
@@ -143,6 +146,7 @@ class Plano:
     prefixo: str | None = None
     ordem_execucao: list[str] = field(default_factory=list)
     tarefas: list[Item] = field(default_factory=list)
+    fora_do_corpus: bool = False
 
 
 @dataclass
@@ -289,8 +293,22 @@ def _scan_items(linhas: list[str], arquivo_rel: str) -> list[Item]:
 
 
 def _parse_indice(linhas: list[str], arquivo_rel: str) -> list[LinhaIndice]:
+    """Âncora do índice (§2.2, DB-43): a tabela que segue o cabeçalho `## Índice`, e só ela —
+    começa na primeira linha iniciada por `|` depois desse cabeçalho e termina na primeira linha
+    em branco. Nenhuma outra tabela markdown do diário produz linha de índice."""
     resultado: list[LinhaIndice] = []
-    for i, linha in enumerate(linhas, start=1):
+    inicio_secao = next((i for i, l in enumerate(linhas) if INDICE_HEADING_RE.match(l)), None)
+    if inicio_secao is None:
+        return resultado
+    inicio_tabela = next(
+        (i for i in range(inicio_secao + 1, len(linhas)) if linhas[i].startswith("|")), None
+    )
+    if inicio_tabela is None:
+        return resultado
+    for i in range(inicio_tabela, len(linhas)):
+        linha = linhas[i]
+        if linha.strip() == "":
+            break
         m = INDICE_LINHA_RE.match(linha)
         if not m:
             continue
@@ -301,7 +319,7 @@ def _parse_indice(linhas: list[str], arquivo_rel: str) -> list[LinhaIndice]:
             continue
         resultado.append(
             LinhaIndice(
-                id=id_, titulo=titulo, status_bruto=status_bruto, arquivo=arquivo_rel, linha=i, ancora=ancora
+                id=id_, titulo=titulo, status_bruto=status_bruto, arquivo=arquivo_rel, linha=i + 1, ancora=ancora
             )
         )
     return resultado
@@ -399,7 +417,7 @@ def carregar(repo: Path) -> Modelo:
     indice, tiquetes, diario_linhas = _parse_diario(diario_path, repo)
     diretiva_ids = _parse_diretiva(diario_linhas)
 
-    return Modelo(
+    modelo = Modelo(
         planos=planos,
         tiquetes=tiquetes,
         indice=indice,
@@ -408,9 +426,21 @@ def carregar(repo: Path) -> Modelo:
         diretiva_ids=diretiva_ids,
     )
 
+    # §2.0 (DB-43) — a autoridade sobre a vida de um plano é a célula de estado da linha dele no
+    # índice do diário, casada pela regra de sufixo de `_posicao_indice` (residência única do
+    # casamento). Núcleo em done/superse
```
[truncado em 4000 caracteres]

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index cdd5555..7044b68 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -13,18 +13,28 @@ from __future__ import annotations
 
 import hashlib
 import importlib.util
+import io
+import json
+import os
+import re
 import shutil
+import subprocess
 import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
 _BACKLOG_PATH = _ROOT / ".claude" / "tools" / "backlog.py"
+_HOOK_PATH = _ROOT / ".claude" / "tools" / "backlog_hook.py"
 _FIXTURES = Path(__file__).resolve().parent / "fixtures" / "backlog"
 _FIXTURE_VERDE = _FIXTURES / "verde"
 _FIXTURE_VERMELHO = _FIXTURES / "vermelho"
 _FIXTURE_NEXT_TK90 = _FIXTURES / "next_tk90"
 _FIXTURE_NEXT_TK90_SEM_INDICE = _FIXTURES / "next_tk90_sem_indice"
 _FIXTURE_INBOX_PLANOS = _FIXTURES / "inbox_planos" / "_INBOX.md"
+_FIXTURE_CORPUS = _FIXTURES / "corpus"
+_FIXTURE_CONTADOR_INBOX = _FIXTURES / "contador_inbox"
+_FIXTURE_CITACAO_SECAO = _FIXTURES / "citacao_secao"
+_FIXTURE_CANDIDATO_A_FECHAMENTO = _FIXTURES / "candidato_a_fechamento"
 
 
 def _load_backlog():
@@ -42,6 +52,13 @@ def _copiar_fixture(origem: Path, destino: Path) -> Path:
     return destino
 
 
+def _load_hook():
+    spec = importlib.util.spec_from_file_location("backlog_hook", _HOOK_PATH)
+    module = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(module)
+    return module
+
+
 def _hashes(repo: Path) -> dict[str, str]:
     return {
         str(caminho.relative_to(repo)): hashlib.sha256(caminho.read_bytes()).hexdigest()
@@ -50,6 +67,24 @@ def _hashes(repo: Path) -> dict[str, str]:
     }
 
 
+def _mudar_linha_unica(repo: Path, relpath: str, velha: str, nova: str) -> None:
+    """Troca uma linha por outra numa cópia de fixture em `tmp_path` — nunca na fixture do
+    repositório. `velha` tem de ser única no arquivo (mesmo padrão de `_indice_com_sufixo`)."""
+    caminho = repo / relpath
+    texto = caminho.read_text(encoding="utf-8")
+    assert texto.count(velha) == 1, f"linha não é única (ou ausente) em {relpath}: {velha!r}"
+    caminho.write_text(texto.replace(velha, nova, 1), encoding="utf-8")
+
+
+def _inserir_linhas_indice(repo: Path, linhas_novas: list[str]) -> None:
+    """Acrescenta linhas à tabela do índice da fixture `corpus`, logo depois da linha do
+    `TK-1` — sempre sobre a cópia em `tmp_path`, nunca na fixture do repositório."""
+    ancora = "| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |\n"
+    _mudar_linha_unica(
+        repo, "docs/DIARIO_DE_OBRAS.md", ancora.rstrip("\n"), ancora.rstrip("\n") + "\n" + "\n".join(linhas_novas)
+    )
+
+
 def _inserir_bloco_gerado(repo: Path) -> None:
     """Prepara a cópia da fixture para os TF de escrita da `BKL-T4`: a fixture
     `next_tk90` não carrega os marcadores `<!-- fila:gerada -->`/`<!-- /fila:gerada -->`
@@ -145,6 +180,251 @@ def test_tf_check_verde_sem_violacoes(tmp_path):
     assert violacoes == []
 
 
+# --------------------------------------------------------------------------- #
+# TF/TR C-10 — contador do inbox (`docs/plans/_INBOX.md`) confrontado com o maior id
+# presente em `docs/plans/P-*.md`. Caso medido: contador em `P-0742` com
+# `docs/plans/P-0742-loop-fora-do-llm.md` já na árvore, sem nenhuma linha viva no inbox
+# apontando para `P-0742` — a fixture `contador_inbox` reproduz exatamente essa forma
+# (nenhum caminho `P-0742` mencionado no texto do inbox), para que a guarda C-10 só passe
+# se ler `docs/plans/P-*.md`, nunca os ids do próprio texto do inbox.
+# --------------------------------------------------------------------------- #
+
+
+def test_tf_c10_contador_do_inbox_aponta_para_id_ja_usado(tmp_path):
+    backlog = _load_backlog()
+    repo = _copiar_fixture(_FIXTURE_CONTADOR_INBOX, tmp_path / "repo")
+
+    modelo = backlog.carregar(repo)
+    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md")
+
+    c10 = [v for v in violacoes if v.codigo == "C-10"]
+    asse
```
[truncado em 4000 caracteres]

### `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`
```
# Diário de Obras (fixture candidato_a_fechamento — TK-61a)

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|
| TK-1 | Tiquete todos terminais | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |
| TK-2 | Tiquete com filho vivo | ready | docs/DIARIO_DE_OBRAS.md#tk-2 |
| TK-3 | Tiquete já terminal | done | docs/DIARIO_DE_OBRAS.md#tk-3 |
| TK-4 | Tiquete sem subtarefa | ready | docs/DIARIO_DE_OBRAS.md#tk-4 |

## TK-1 — Tiquete todos terminais
- **Status:** `ready` · 2026-01-01

### TK-1a — Subtarefa terminal done [Sonnet · classe mecanica]
- **Status:** `done` · 2026-01-01

### TK-1b — Subtarefa terminal cancelled [Sonnet · classe mecanica]
- **Status:** `cancelled` · 2026-01-01

## TK-2 — Tiquete com filho vivo
- **Status:** `ready` · 2026-01-01

### TK-2a — Subtarefa terminal done [Sonnet · classe mecanica]
- **Status:** `done` · 2026-01-01

### TK-2b — Subtarefa viva [Sonnet · classe mecanica]
- **Status:** `ready` · 2026-01-01

## TK-3 — Tiquete já terminal
- **Status:** `done` · 2026-01-01

### TK-3a — Subtarefa terminal done [Sonnet · classe mecanica]
- **Status:** `done` · 2026-01-01

## TK-4 — Tiquete sem subtarefa
- **Status:** `ready` · 2026-01-01

```

### `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md`
```
# diario-de-obras — kanban central do projeto (fixture)

Reprodução mínima do caso real medido no `TK-60`: nenhum heading numerado no arquivo, mas o
literal `2.5` aparece em prosa — a armadilha que um casamento por substring (em vez de heading)
deixaria passar como se a seção `2.5` existisse.

## Estrutura do documento

Corpo cresce de ~2.5k para ~5k chars por handovers sucessivos apensando parágrafos.

## Índice

Texto de exemplo, sem seção numerada nenhuma.

```

### `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md`
```
# P-0900 — Exemplo

**Status:** `ready`
**Prefixo das tarefas no diário:** `EX-T<n>`

## 2. Gramática legível por máquina

### 2.0 Corpus

Texto de exemplo.

### 2.5 Ordem total de seleção (`next`)

Seção realmente presente, numerada — caso positivo do par presença-ausência.

```

### `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`
```
# Diário de Obras (fixture contador_inbox)

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|
| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |

## TK-1 — Tiquete base
- **Status:** `ready` · 2026-01-01

```

### `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md`
```
# P-0742 — Existe

**Status:** `done` · **Prefixo das tarefas no diário:** `EXI-T<n>`

```

### `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md`
```
# Inbox de planos (fixture contador_inbox)

**Próximo id de plano: P-0742.**

- nota solta, sem caminho de plano

```

### `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`
```
# Diário de Obras (fixture corpus — BKL-T10)

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|
| P-0900 | Plano legado | ready | docs/plans/P-0900-legado.md |
| P-0777-XYZ | Plano gama | done | docs/plans/P-0777-gama.md |
| TK-1 | Tiquete base | ready | docs/DIARIO_DE_OBRAS.md#tk-1 |

## TK-1 — Tiquete base
- **Status:** `ready` · 2026-01-01

Tabela ilustrativa dentro da prosa do tíquete, fora da seção `## Índice` — não é lida como
índice (mesmo tendo 4 colunas e um núcleo fora do vocabulário):

| ID | Nota | Status | Âncora |
|---|---|---|---|
| X-1 | Nota decoy | totalmente-fora-do-vocabulario | docs/DIARIO_DE_OBRAS.md#x-1 |

```

### `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`
```
# P-0777 — Plano gama

**Status:** `ready` · **Prefixo das tarefas no diário:** `GAM-T<n>`

### GAM-T1 — Única [Sonnet · classe implementacao]
- **Status:** `done` · 2026-01-03

```

### `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
```
# P-0900 — Plano legado

Corpo sem os campos de cabeçalho esperados (sem Status, sem Prefixo) — típico de plano fechado
antigo que a DB-15 proíbe emendar.

### LEG-T1 — Única [Sonnet · classe implementacao]
- **Status:** `ready` · 2026-01-01

```

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
