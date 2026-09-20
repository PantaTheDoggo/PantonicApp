# Evidência de revisão — DIARIO_DE_OBRAS TK-58a

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
 docs/CUSTO_DO_PICKUP.md                            |   54 +
 docs/DIARIO_DE_OBRAS.md                            | 1042 +++++++-
 docs/DOC_MAP.md                                    |    5 +
 docs/RDO/INDEX.md                                  |   17 +
 docs/consultant-spec.md                            |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md   |    2 +-
 docs/plans/P-0737-loop-autonomo.md                 |    2 +-
 docs/plans/P-0738-contexto-esgotado.md             |    2 +-
 docs/plans/P-0739-backlog-instrumento.md           | 2526 +++++++++++++++++++-
 docs/plans/_INBOX.md                               |    2 +-
 docs/plans/_INBOX_HISTORICO.md                     |    1 +
 docs/telemetria.tsv                                |   70 +
 tests/test_backlog.py                              |  838 ++++++-
 tests/test_materializar.py                         |   71 +
 tests/test_ocupacao.py                             |   77 +-
 tests/test_rdo.py                                  |   34 +
 tests/test_review_evidence.py                      |   37 +
 tests/test_telemetria_hook.py                      |  117 +-
 30 files changed, 5411 insertions(+), 191 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` — atribuição: alheio; estado git: ` M`
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/ocupacao.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/telemetria_hook.py` — atribuição: alheio; estado git: ` M`
- `CHANGELOG.md` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: da entrega; estado git: ` M`
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
- `docs/RDO/DIARIO_DE_OBRAS-TK-61a-o-rodape-de-next-imprime-candidato-a-fechamento.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-63a-o-mundo-hostil-do-teste-de-executavel-e-construido-nao-herda.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/TK-61-TK-61a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-62-TK-62a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-63-TK-63a.md` — atribuição: alheio; estado git: `??`
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
- `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md` — atribuição: alheio; estado git: `??`
- `tests/test_backlog.py` — atribuição: alheio; estado git: ` M`
- `tests/test_materializar.py` — atribuição: alheio; estado git: ` M`
- `tests/test_ocupacao.py` — atribuição: alheio; estado git: ` M`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `docs/CUSTO_DO_PICKUP.md`
- Arquivos tocados: `.claude/README.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/ocupacao.py`, `.claude/tools/rdo.py`, `.claude/tools/telemetria_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-61a-o-rodape-de-next-imprime-candidato-a-fechamento.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-63a-o-mundo-hostil-do-teste-de-executavel-e-construido-nao-herda.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-59-TK-59a.md`, `docs/RDO/evidencia/TK-60-TK-60a.md`, `docs/RDO/evidencia/TK-60-TK-60b.md`, `docs/RDO/evidencia/TK-60-TK-60c.md`, `docs/RDO/evidencia/TK-61-TK-61a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/evidencia/TK-63-TK-63a.md`, `docs/RDO/evidencia/TK-64-TK-64a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md`, `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md`, `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_materializar.py`, `tests/test_ocupacao.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `TK-64a`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/ocupacao.py` → `TK-56a`, `.claude/tools/rdo.py` → `TK-62a`, `.claude/tools/telemetria_hook.py` → `TK-56a`, `README.md` → `TK-51a`, `tests/test_backlog.py` → `TK-57a`, `tests/test_materializar.py` → `TK-56a`, `tests/test_ocupacao.py` → `TK-56a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`, `tests/test_telemetria_hook.py` → `TK-56a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-61a-o-rodape-de-next-imprime-candidato-a-fechamento.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-63a-o-mundo-hostil-do-teste-de-executavel-e-construido-nao-herda.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-59-TK-59a.md`, `docs/RDO/evidencia/TK-60-TK-60a.md`, `docs/RDO/evidencia/TK-60-TK-60b.md`, `docs/RDO/evidencia/TK-60-TK-60c.md`, `docs/RDO/evidencia/TK-61-TK-61a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/evidencia/TK-63-TK-63a.md`, `docs/RDO/evidencia/TK-64-TK-64a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 19 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md`, `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md`, `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/CUSTO_DO_PICKUP.md`
```
diff --git a/docs/CUSTO_DO_PICKUP.md b/docs/CUSTO_DO_PICKUP.md
index 29ab321..3526d0d 100644
--- a/docs/CUSTO_DO_PICKUP.md
+++ b/docs/CUSTO_DO_PICKUP.md
@@ -431,3 +431,57 @@ Uma linha por fonte carregada. `chars` = `len(texto)` medido em disco por sonda
 **Notas de honestidade.** A linha de E3 fecha os três regimes por construção, porque é a diferença; o que este extrato afirma com medida é a participação de E1. · E1 é medido em 2026-09-18; os regimes 34.600 e 46.100 são de 2026-08-24, quando o `CLAUDE.md` global tinha 10.751 ch — a reconciliação nesses dois regimes é aproximada, e é por isso que ela sai como faixa. · As linhas 8, 9 e 10 são medidas por proxy em disco ou por comando, não por leitura do preâmbulo de uma janela principal.
 
 **Resultado.** O extrato fecha nos três regimes. E1 carregado sempre custa entre **4.467 e 7.445 tk** — de **12,9% a 21,5%** do regime de 34.600 e de **7,4% a 12,3%** do regime de 60.472 (2,2% a 3,7% de uma janela de 200k). O residual não atribuído fica entre **87,7% e 92,6%** do `usage_1` de 60.472, e é onde mora qualquer corte com efeito sobre a meta declarada. Distribuição das classificações fixadas: `economizável` 4 · `necessário` 3 · `dispensável` 1 · `—` 2 · `válido` 0. **Duas contingências acionadas na medição:** (4) a chave `additionalDirectories` não existe em `C:\Users\panta\.claude\settings.json` nem em `D:\workspaces\PantonicApp\.claude\settings.local.json` — a linha 9 sai `não medido`; e, fora da lista de contingências, a enumeração bruta encontrou **23 `SKILL.md` e 10 `agents/*.md`** porque `D:\workspaces\PantonicApp\.claude\global\{skills,agents}\` **espelha** `C:\Users\panta\.claude\{skills,agents}\` — 6 skills e 1 agente duplicados. Deduplicado dá 17 e 9, que é o inventário da rodada; sem deduplicar, a listagem de skills mediria 8.033 ch em vez de 5.984 e a de agentes 3.104 em vez de 2.740. Esta seção **não** decide o que fazer com o espelho: é fato de medição, entregue à ratificação.
+
+## 14 Pickup por instrumento: aferição (2026-09-20)
+
+Método `DC-4` aplicado ao pickup novo, em que o dossiê da próxima tarefa chega injetado por hook no
+ponto de carga em vez de ser montado por um roteiro de leituras. `chars` = `len(texto)` medido nesta
+data; a metade `usage_1` do método está medida e publicada na `## 15`.
+
+| # | fonte | chars | situação no pickup novo |
+|---|---|---|---|
+| 0a | `.claude/global/CLAUDE.md` | 10.376 | mantida (era 9.546 na `## 3`) |
+| 0b | `.claude/skills/proximo-passo/SKILL.md` | 0 | fonte inexistente (era 15.081) |
+| 0c | `memory/MEMORY.md` | 817 | mantida |
+| 0d | `memory/*.md` indexadas (n=5) | 8.488 | mantida |
+| H | saída do hook de pickup | 7.079 | substitui P1a-P3b (43.525 na `## 3`) |
+
+**Pickup por instrumento = 26.760 chars (~6.690 tokens)** — soma das cinco linhas. A saída do hook
+são 7.079 chars (7.080 bytes em UTF-8), dos quais 6.122 são o `additionalContext` que entra na
+janela e o restante é o envelope JSON. Prompt sem o gatilho devolve 0 chars com exit 0: o custo só é
+pago quando o pickup é pedido.
+
+**Contra os dois valores de referência:** −65,5% sobre os **77.457 chars** da `## 3` (50.697 chars a
+menos) e **66,9%** do alvo de **40.000 chars** da `## 6`, cumprido com 13.240 chars de folga. A
+redução tem duas origens: os seis passos de roteiro da `## 3` somavam 43.525 chars — 21.505 do inbox
+de planos e 19.872 do dossiê do plano lido inteiro — e viram uma injeção de 7.079; e a skill de
+roteiro que custava 15.081 chars deixou de existir.
+
+**Metade em `usage_1`: medida.** O `usage_1` correspondente foi medido em **2026-09-20** e está
+publicado na `## 15`, que fecha o par do `DC-4` e corrige o que esta seção afirmava sobre a
+observabilidade do número.
+
+## 15 Par completo do método DC-4: o pickup por instrumento em chars e em usage_1 (2026-09-20)
+
+Fecha a aferição da `## 14`. O `DC-4` soma uma metade em **chars** e uma metade em **`usage_1`** de
+sessão nova; as duas estão medidas.
+
+**Metade em chars — 26.760**, rep
```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
