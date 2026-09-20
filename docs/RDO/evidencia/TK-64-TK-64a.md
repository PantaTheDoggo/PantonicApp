# Evidência de revisão — DIARIO_DE_OBRAS TK-64a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    1 +
 .../hooks/modelo_por_fase_userpromptsubmit.py      |    5 +-
 .claude/projecoes.json                             |   10 +
 .claude/skills/passagem-de-bastao/SKILL.md         |   35 +-
 .claude/skills/scrum-master/SKILL.md               |   23 +-
 .claude/tools/backlog.py                           |  289 ++-
 .claude/tools/ocupacao.py                          |   10 +-
 .claude/tools/rdo.py                               |    6 +-
 .claude/tools/telemetria_hook.py                   |   10 +-
 CHANGELOG.md                                       |   15 +-
 GOVERNANCA.md                                      |    2 +-
 README.md                                          |   33 +-
 docs/CUSTO_DO_PICKUP.md                            |   31 +
 docs/DIARIO_DE_OBRAS.md                            |  703 +++++-
 docs/DOC_MAP.md                                    |    2 +
 docs/RDO/INDEX.md                                  |   10 +
 docs/consultant-spec.md                            |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md   |    2 +-
 docs/plans/P-0737-loop-autonomo.md                 |    2 +-
 docs/plans/P-0738-contexto-esgotado.md             |    2 +-
 docs/plans/P-0739-backlog-instrumento.md           | 2526 +++++++++++++++++++-
 docs/plans/_INBOX.md                               |    2 +-
 docs/plans/_INBOX_HISTORICO.md                     |    1 +
 docs/telemetria.tsv                                |   48 +
 tests/test_backlog.py                              |  635 ++++-
 tests/test_materializar.py                         |   71 +
 tests/test_ocupacao.py                             |   66 +-
 tests/test_rdo.py                                  |   34 +
 tests/test_review_evidence.py                      |   37 +
 tests/test_telemetria_hook.py                      |  117 +-
 30 files changed, 4609 insertions(+), 185 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: da entrega; estado git: ` M`
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
- `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md` — atribuição: alheio; estado git: `??`
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
- `docs/RDO/evidencia/TK-62-TK-62a.md` — atribuição: alheio; estado git: `??`
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
- Arquivos-alvo declarados: `.claude/README.md`
- Arquivos tocados: `.claude/README.md`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/ocupacao.py`, `.claude/tools/rdo.py`, `.claude/tools/telemetria_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_materializar.py`, `tests/test_ocupacao.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`, `tests/test_telemetria_hook.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → `TK-56a`, `.claude/tools/backlog.py` → `TK-59a`, `.claude/tools/ocupacao.py` → `TK-56a`, `.claude/tools/rdo.py` → `TK-62a`, `.claude/tools/telemetria_hook.py` → `TK-56a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_backlog.py` → `TK-57a`, `tests/test_materializar.py` → `TK-56a`, `tests/test_ocupacao.py` → `TK-56a`, `tests/test_rdo.py` → `TK-62a`, `tests/test_review_evidence.py` → `TK-62a`, `tests/test_telemetria_hook.py` → `TK-56a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56a-os-tres-pontos-de-carga-passam-a-ler-stdin-em-utf-8-explicit.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-56b-os-dois-testes-sem-poder-discriminante-passam-a-observar-o-p.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-57a-o-teste-do-hook-fixa-o-ambiente-e-afirma-a-invariancia.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-62a-rdo-py-reconhece-tk-n-letra-como-id-de-tarefa.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-56-TK-56a.md`, `docs/RDO/evidencia/TK-56-TK-56b.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/evidencia/TK-62-TK-62a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 13 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/README.md`
```
diff --git a/.claude/README.md b/.claude/README.md
index cc88f76..1bf9e24 100644
--- a/.claude/README.md
+++ b/.claude/README.md
@@ -50,6 +50,7 @@ Skillstore mudar de lugar.
 | `bootstrap-pantonic` | Inicializa um novo projeto Pantonic* — os quatro artefatos (PRD, Architecture, Spec, Sprint Plan), a estrutura de docs ATIVO/HISTÓRICO e o esqueleto do core reusável. Usar ao criar um projeto novo da família Pantonic* ou ao auditar se um projeto existente segue o padrão. |
 | `checar-versao-kit` | Resolve a versão local do kit agêntico e, enquanto o framework estiver com a versão congelada em 0.0.0 (GOVERNANCA.md §10), reporta "congelada — nada a comparar" sem tocar a rede. Fora do congelamento, compara com a versão publicada no hub PantonicApp sem nunca atualizar sozinho, em três modos de resolução (consumidor, hub, não-instalado). Nos dois regimes arma o gatilho de revisão da doutrina (GOVERNANCA.md §7.1), que fica pendente quando existe plano fechado como done no índice do diário sem rodada de revisão registrada. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano"). |
 | `diario-de-obras` | Cria e mantém o diário de obras do projeto Pantonic* — kanban central em docs/DIARIO_DE_OBRAS.md com índice, status e arquivamento de planejamentos. Usar ao registrar um plano novo, abrir tíquete avulso, mudar status de tarefa ou condensar itens concluídos. |
+| `entrega-de-encerramento` | Produz o documento de encerramento de um plano Pantonic* — o modelo "as-is" que mapeia cada tarefa ao contexto que a motivou, ao artefato concreto que ela criou, a um exemplo real de funcionamento e ao que ela protege, mais o estado honesto do que ficou aberto. É o artefato pelo qual o dono valida o plano. Usar ao fechar qualquer plano, antes de pedir o veredito. |
 | `guardrails-check` | Verifica os guardrails de clean architecture de um projeto Pantonic* antes de marcar uma tarefa como concluída — regra de camadas, ACL, egress G6, namespace de estado, conformance e piso de regressão. Usar ao final de toda tarefa de execução ou em auditoria. |
 | `integrar-poc` | Integra uma POC validada pelo cliente como plugin de uma aplicação Pantonic*, dissecando-a nas camadas da clean architecture (pipeline de 5 passos). Usar quando uma POC standalone foi aprovada e deve virar plugin. |
 | `modelo-por-fase` | Gatilho operacional da regra "modelo por fase" (GOVERNANCA.md §3) — classifica a fase do trabalho (intelectual/execução/varredura), confere o modelo ativo contra a tabela vinculante e para para pedir o /model correto ao dono. Usar no início de qualquer tarefa/subagente, ao trocar de fase no meio de uma sessão, ou quando o hook global de nudge (UserPromptSubmit) disparar o aviso. |

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
