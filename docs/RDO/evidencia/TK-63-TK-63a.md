# Evidência de revisão — DIARIO_DE_OBRAS TK-63a

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
 docs/DIARIO_DE_OBRAS.md                            | 1010 +++++++-
 docs/DOC_MAP.md                                    |    2 +
 docs/RDO/INDEX.md                                  |   16 +
 docs/consultant-spec.md                            |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md   |    2 +-
 docs/plans/P-0737-loop-autonomo.md                 |    2 +-
 docs/plans/P-0738-contexto-esgotado.md             |    2 +-
 docs/plans/P-0739-backlog-instrumento.md           | 2526 +++++++++++++++++++-
 docs/plans/_INBOX.md                               |    2 +-
 docs/plans/_INBOX_HISTORICO.md                     |    1 +
 docs/telemetria.tsv                                |   68 +
 tests/test_backlog.py                              |  838 ++++++-
 tests/test_materializar.py                         |   71 +
 tests/test_ocupacao.py                             |   77 +-
 tests/test_rdo.py                                  |   34 +
 tests/test_review_evidence.py                      |   37 +
 tests/test_telemetria_hook.py                      |  117 +-
 30 files changed, 5350 insertions(+), 191 deletions(-)
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
- `docs/RDO/DIARIO_DE_OBRAS-TK-61a-o-rodape-de-next-imprime-candidato-a-fechamento.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/TK-61-TK-61a.md` — atribuição: alheio; estado git: `??`
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
- `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md` — atribuição: alheio; estado git: `??`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_materializar.py` — atribuição: alheio; estado git: ` M`
- `tests/test_ocupacao.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: alheio; estado git: ` M`
- `tests/test_telemetria_hook.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `tests/test_backlog.py`, `tests/test_ocupacao.py`
- Arquivos tocados: `.claude/README.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/ocupacao.py`, `.claude/tools/rdo.py`, `.claude/tools/telemetria_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-61a-o-rodape-de-next-imprime-candidato-a-fechamento.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-59-TK-59a.md`, `docs/RDO/evidencia/TK-60-TK-60a.md`, `docs/RDO/evidencia/TK-60-TK-60b.md`, `docs/RDO/evidencia/TK-60-TK-60c.md`, `docs/RDO/evidencia/TK-61-TK-61a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/evidencia/TK-64-TK-64a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md`, `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md`, `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_materializar.py`, `tests/test_ocupacao.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `TK-64a`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/ocupacao.py` → `TK-56a`, `.claude/tools/rdo.py` → `TK-62a`, `.claude/tools/telemetria_hook.py` → `TK-56a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_materializar.py` → `TK-56a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`, `tests/test_telemetria_hook.py` → `TK-56a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-59a-verificador-do-contador-de-id-do-inbox-contra-docs-plans.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60a-check-resolve-citacao-de-secao-e-emite-c-11.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60b-item-5-implementado-e-piso-devolvido-a-divida-real.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-60c-a-decomposicao-por-arquivo-do-piso-bate-com-o-total-que-ela.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-61a-o-rodape-de-next-imprime-candidato-a-fechamento.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-64a-regenerar-claude-readme-md-pelo-gerador-do-kit.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-59-TK-59a.md`, `docs/RDO/evidencia/TK-60-TK-60a.md`, `docs/RDO/evidencia/TK-60-TK-60b.md`, `docs/RDO/evidencia/TK-60-TK-60c.md`, `docs/RDO/evidencia/TK-61-TK-61a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/evidencia/TK-64-TK-64a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 19 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/citacao_secao/.claude/skills/diario-de-obras/SKILL.fixture.md`, `tests/fixtures/backlog/citacao_secao/docs/plans/P-0900-exemplo.md`, `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/P-0742-existe.md`, `tests/fixtures/backlog/contador_inbox/docs/plans/_INBOX.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index cdd5555..efe187a 100644
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
@@ -42,6 +52,31 @@ def _copiar_fixture(origem: Path, destino: Path) -> Path:
     return destino
 
 
+def _load_hook():
+    spec = importlib.util.spec_from_file_location("backlog_hook", _HOOK_PATH)
+    module = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(module)
+    return module
+
+
+def _montar_raiz_hook(base: Path, nome: str, fonte_hook: str) -> Path:
+    """Raiz falsa em `base/nome` para relocar o acoplamento por `__file__` de `backlog_hook.py`
+    (TK-63a — substitui o shim de `__file__` preservado, que a devolução anterior apontou como
+    acoplamento ao diário e aos planos reais). Copiada de `_FIXTURE_NEXT_TK90` — fornece
+    `docs/DIARIO_DE_OBRAS.md` e `docs/plans/_INBOX.md` para o `next` real ter o que ler — com
+    `.claude/tools/backlog_hook.py` (fonte injetada, para poder trocar pelo produto revertido) e
+    `.claude/tools/backlog.py` (cópia do arquivo real via `shutil.copy2`). Basta: `_carregar_backlog`
+    resolve `backlog.py` como irmão de `__file__`, e `resolve_repo(None)` (em `backlog.py`) resolve
+    a raiz a partir de onde o próprio `backlog.py` está — o acoplamento se fecha dentro da raiz
+    falsa. Mesma técnica do `telemetria_hook` na `TK-56b` (aprovada 100%)."""
+    raiz = _copiar_fixture(_FIXTURE_NEXT_TK90, base / nome)
+    tools_dir = raiz / ".claude" / "tools"
+    tools_dir.mkdir(parents=True)
+    (tools_dir / "backlog_hook.py").write_text(fonte_hook, encoding="utf-8")
+    shutil.copy2(_BACKLOG_PATH, tools_dir / "backlog.py")
+    return raiz
+
+
 def _hashes(repo: Path) -> dict[str, str]:
     return {
         str(caminho.relative_to(repo)): hashlib.sha256(caminho.read_bytes()).hexdigest()
@@ -50,6 +85,24 @@ def _hashes(repo: Path) -> dict[str, str]:
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
 
```
[truncado em 4000 caracteres]

### `tests/test_ocupacao.py`
```
diff --git a/tests/test_ocupacao.py b/tests/test_ocupacao.py
index 98e5219..e88a56f 100644
--- a/tests/test_ocupacao.py
+++ b/tests/test_ocupacao.py
@@ -1,7 +1,8 @@
 """EXA-T13 (`docs/plans/P-0734-execucao-autonoma.md` `### T13`) — TF/TR de
 `.claude/tools/ocupacao.py`: `calcular_ocupacao` (numerador, com ramo de fallback estimado) e
-`avaliar` (fração e cruzamento do limiar de 50%, `GOVERNANCA.md` §4.3). Por desenho da tarefa, o
-hook (`main`, I/O de stdin/transcript) não é exercitado aqui — só as duas funções puras.
+`avaliar` (fração e cruzamento do limiar de 50%, `GOVERNANCA.md` §4.3). O hook (`main`, I/O de
+stdin/transcript) ganhou cobertura por subprocesso na `TK-56a` (`DB-53`,
+`docs/plans/P-0739-backlog-instrumento.md:122`) — leitura de stdin em UTF-8 explícito.
 
 `.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
 caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_rdo.py` e
@@ -11,6 +12,9 @@ from __future__ import annotations
 
 import importlib.util
 import json
+import os
+import subprocess
+import sys
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
@@ -169,3 +173,72 @@ def test_tr_janela_tokens_aceita_sufixo_e_ignora_lixo(monkeypatch):
     for lixo in ("lixo", "", "-5", "0"):
         monkeypatch.setenv("PANTONIC_CONTEXT_TOKENS_MAX", lixo)
         assert _load_ocupacao().JANELA_TOKENS == 1_000_000
+
+
+def test_tf_hook_executavel_stdin_utf8_cruza_o_limiar_e_devolve_aviso(tmp_path):
+    """TK-56a (`DB-53`) reescrito pela TK-63a: `main` lê stdin em UTF-8 explícito, não na
+    codificação do host. `ocupacao.py` não tem acoplamento por `__file__` — a raiz falsa é uma
+    cópia simples em `tmp_path`, sem a estrutura de `.claude/tools/`. O mundo hostil deixa de ser
+    "host sem PYTHONUTF8" (mede o host) e passa a ser construído: `env` mínimo +
+    `PYTHONIOENCODING=cp1252` (hostil) e `env` mínimo + `PYTHONUTF8=1` (seguro) — mesma técnica do
+    `backlog_hook` (TK-63a) e do `telemetria_hook` (TK-56b). O par negativo é o produto revertido
+    (bloco de decode UTF-8 explícito trocado por `sys.stdin.read()` cru), não mais um stub. Três
+    asserções de relação, nenhuma de magnitude: (i) invariância do reparado entre os mundos; (ii)
+    divergência do revertido entre os mundos; (iii) não-vazio do reparado no mundo hostil. O
+    `hook_event_name` acentuado viaja intacto do payload até a saída (medido no reparado).
+    Reproduzido em 2026-09-20: reparado → 325 B idênticos em hostil e seguro; revertido → 337 B
+    no hostil (decodifica errado mas ainda cruza o limiar), 325 B no seguro."""
+    transcript = tmp_path / "transcript.jsonl"
+    transcript.write_text("linha de teste ação " * 50, encoding="utf-8")
+    payload = json.dumps(
+        {"hook_event_name": "PreToolUse-ação", "transcript_path": str(transcript)},
+        ensure_ascii=False,
+    ).encode("utf-8")
+
+    fonte = _OCUPACAO_PATH.read_text(encoding="utf-8")
+    bloco_reparo = (
+        "        try:\n"
+        "            raw = sys.stdin.buffer.read().decode(\"utf-8\", errors=\"replace\")\n"
+        "        except AttributeError:\n"
+        "            raw = sys.stdin.read()\n"
+    )
+    assert bloco_reparo in fonte
+    fonte_revertida = fonte.replace(bloco_reparo, "        raw = sys.stdin.read()\n")
+
+    env_hostil = {
+        "SYSTEMROOT": os.environ["SYSTEMROOT"],
+        "PATH": os.environ["PATH"],
+        "PANTONIC_CONTEXT_TOKENS_MAX": "1",
+        "PYTHONIOENCODING": "cp1252",
+    }
+    env_seguro = {
+        "SYSTEMROOT": os.environ["SYSTEMROOT"],
+        "PATH": os.environ["PATH"],
+        "PANTONIC_CONTEXT_TOKENS_MAX": "1",
+        "PYTHONUTF8": "1",
+    }
+
+    def _rodar(nome: str, fonte_ocupacao: str, env: dict):
+        caminho = tmp_path / f"{nome}.py"
+        caminho.write_text(fonte_ocupacao, encoding="utf-8")
+        return subprocess.run(
+            [sys.executable, str(caminho)], input=payload,
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
