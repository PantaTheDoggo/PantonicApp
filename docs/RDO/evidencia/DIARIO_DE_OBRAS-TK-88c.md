# Evidência de revisão — DIARIO_DE_OBRAS TK-88c

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   43 +-
 .claude/agents/pantonic-executor.md                |   11 +-
 .claude/agents/pantonic-fora-da-caixa.md           |    2 +-
 .claude/agents/pantonic-model-designer.md          |   81 +-
 .claude/agents/pantonic-planner.md                 |  217 +-
 .claude/agents/pantonic-reviewer.md                |   15 +-
 .claude/checks/kit_check.ps1                       |   39 +-
 .claude/global/CLAUDE.md                           |   67 +-
 .../hooks/modelo_por_fase_userpromptsubmit.py      |   13 +-
 .claude/projecoes.json                             |   47 +
 .claude/skills/bootstrap-pantonic/SKILL.md         |    6 +-
 .claude/skills/diario-de-obras/SKILL.md            |  156 +-
 .claude/skills/entrega-de-encerramento/SKILL.md    |    2 +-
 .claude/skills/modelo-por-fase/SKILL.md            |   26 +-
 .claude/skills/passagem-de-bastao/SKILL.md         |   54 +-
 .claude/skills/redacao-doc/SKILL.md                |    3 +-
 .claude/skills/scrum-master/SKILL.md               |  219 +-
 .claude/tools/backlog.py                           |  549 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  286 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  166 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  400 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3720 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  125 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  381 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  799 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  265 +-
 tests/test_telemetria_hook.py                      |   35 +
 56 files changed, 10331 insertions(+), 1081 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `tests/test_rdo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `14f8a4b08b1479048b99bc7d3642d1b1eb0e0be2`
- Arquivos-alvo declarados: `.claude/tools/progresso_hook.py`, `.claude/tools/rdo.py`, `.claude/skills/scrum-master/SKILL.md`, `tests/test_progresso_hook.py`, `tests/test_rdo.py`
- Literais não reconhecidos como caminho (13): `evento`, `PreToolUse`, `Bash`, `cmd_close`, `PLANO_PATH`, `M-2`, `M-5`, `M-10`, `M-13`, `M-18`, `docs/RDO/P-0752-FPU-*.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-*.md`, `docs/**/*.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/progresso_hook.py`, `.claude/tools/rdo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c-medida.json`, `docs/telemetria.tsv`, `tests/test_progresso_hook.py`, `tests/test_rdo.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, `docs/RDO/P-0752-FPU-T1-o-gate-do-card-le-a-forma-do-corpus-e-deixa-de-produzir-item.md`, `docs/RDO/P-0752-FPU-T1a-um-teste-tranca-o-marcador-de-item-so-no-inicio-de-linha-com.md`, `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, `docs/RDO/P-0752-FPU-T4-o-aviso-de-crenca-no-ato-de-gravar-plano-ou-diario.md`, `docs/RDO/P-0752-FPU-T4a-o-aviso-de-crenca-conta-uma-vez-o-literal-que-casa-dois-padr.md`, `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, `docs/RDO/P-0752-FPU-T5a-o-executor-o-revisor-e-o-loop-falam-do-arquivo-de-medida.md`, `docs/RDO/P-0752-FPU-T5b-a-medida-guarda-a-cauda-da-saida-onde-esta-o-sumario.md`, `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88c-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/progresso_hook.py`
```
"""Ganchos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` e `Stop` do `P-0748` (`OP-3`):
gera em `.claude/estado/progresso.txt` uma frase por evento de transição do loop, com o
título da tarefa no lugar da sigla. Falha aberta total: qualquer exceção em `main` é
silenciada e o script sempre sai `0`; nunca imprime. Captura de payload opcional (flag
`progresso-captura.on`).
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import shlex
import sys
import time
from pathlib import Path


def _carregar_caminhos():
    caminho = Path(__file__).resolve().parent / "caminhos.py"
    spec = importlib.util.spec_from_file_location("caminhos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar_caminhos()

KIT = Path(__file__).resolve().parents[1]
REPO = KIT.parent

PAPEIS = {
    "pantonic-executor": "executor",
    "pantonic-reviewer": "revisor",
    "pantonic-consultant": "consultor",
    "pantonic-model-designer": "modelador",
    "pantonic-planner": "planejador",
}

ESTADO_ARQ = "progresso-estado.json"
CAPTURA_FLAG = "progresso-captura.on"
CAPTURA_ARQ = "progresso-captura.jsonl"
CAPTURA_TETO_BYTES = 1_000_000

FRASES = {
    'M-0': 'Abrindo a janela do plano "<título do plano>".',
    'M-1': 'Tarefa "<título>". Passo: conferir os gates e preparar o despacho.',
    'M-2': 'Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
    'M-3': 'Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>',
    'M-3b': 'Agente executor recebe a tarefa "<título>" e vai executar o card.',
    'M-4': 'Agente executor devolveu a tarefa "<título>": review — <pendência>.',
    'M-4b': 'Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.',
    'M-5': 'Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.',
    'M-6': 'Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.',
    'M-7': 'Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.',
    'M-8': 'Agente consultor recebe a tarefa "<título>" e vai triar.',
    'M-9': 'Agente consultor devolveu a tarefa "<título>": rota <rota>.',
    'M-9b': 'Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.',
    'M-10': 'Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.',
    'M-10b': 'Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.',
    'M-11': 'Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".',
    'M-12': 'Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.',
    'M-12b': 'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.',
    'M-13': 'Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.',
    'M-14': 'Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.',
    'M-14b': 'Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.',
    'M-15': 'Agente planejador recebe a tarefa "<título>" e vai replanejar.',
    'M-16': 'Agente <papel> devolveu a tarefa "<título>": <primeira linha>.',
    'M-17': 'Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.',
    'M-18': 'Scrum master vai fechar o plano "<título do plano>": registrar estado, relatório de entrega e a linha do diário.',
}


def titulo_do_plano(caminho: str, raiz: Path) -> str:
    """Título da linha 1 do plano (`# P-<n> — <título>`) apontado por `--plano` de
    `encerrar.py plano`; vazio quando o arquivo não existe ou a linha não casa."""
    for base in (Path(caminho), raiz / caminho):
        try:
            primeira = base.read_text(encoding
```
[truncado em 4000 caracteres]

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index bd5785d..6cac10d 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -868,7 +868,7 @@ def cmd_close(args: argparse.Namespace) -> Path:
         "HUMANO": humano,
         "HISTORICO": historico,
         "PLANO_ID": plano_id,
-        "PLANO_PATH": str(args.plano),
+        "PLANO_PATH": str(args.plano).replace("\\", "/"),
         "TAREFA_ID": dossie.tarefa_id,
         "TITULO": dossie.titulo,
         "MODELO": dossie.modelo,

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 985a3cb..6daa0c4 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -367,28 +367,28 @@ ao gerente (`I-12`). Outras ferramentas, outros comandos e outros `subagent_type
 |---|---|---|---|
 | `M-0` | tarefa escolhida, primeira da sessão — `PostToolUse` · `Bash` · `command` contém `backlog.py next` · resposta contém `=== PRÓXIMA TAREFA: ` · estado sem `aberta` | `Abrindo a janela do plano "<título do plano>".` | `<título do plano>` ← `localizar_card(<ID>)`; vazio → linha omitida. Sai antes de `M-11` e de `M-1` |
 | `M-1` | tarefa escolhida — o mesmo evento de `M-0`, sempre | `Tarefa "<título>". Passo: conferir os gates e preparar o despacho.` | `<ID>`, `<título>` ← linha `=== PRÓXIMA TAREFA: <ID> — <título> [` da resposta. Estado ← `tarefa`, `titulo`, `objetivo`, `titulo_plano` (de `localizar_card`), `aberta` = true |
-| `M-2` | estado mudado para in-progress — `PreToolUse` · `Bash` · `command` casa `backlog\.py status (\S+) in-progress` | `Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<título>` ← estado se `<ID>` é a `tarefa` do estado, senão `localizar_card(<ID>)`. `status <ID> review` não gera linha |
+| `M-2` | estado mudado para in-progress — `PreToolUse` · `Bash` · numa invocação do comando encadeado (`_dividir_invocacoes`, fora de aspas) o programa é `backlog.py`, o verbo é `status` e o `<estado>` dos argumentos dessa invocação é `in-progress` (`TK-88c`: script e argumentos se leem na própria invocação, nunca no comando inteiro) | `Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.` | `<título>` ← estado se `<ID>` é a `tarefa` do estado, senão `localizar_card(<ID>)`. `status <ID> review` não gera linha |
 | `M-3` | agente despachado, executor — `PreToolUse` · `Agent` · `subagent_type` = `pantonic-executor` · objetivo não vazio | `Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>` | `<título>`, `<objetivo>` ← tarefa corrente (`DTG-33` (iv)) e `localizar_card`; `<objetivo>` já termina em ponto, ou em `…` se truncado |
 | `M-3b` | o mesmo evento de `M-3`, objetivo vazio | `Agente executor recebe a tarefa "<título>" e vai executar o card.` | `<título>` como em `M-3` |
 | `M-4` | agente de volta, executor — `PostToolUse` · `Agent` · `pantonic-executor`; se o agente entregou em hand-back (`handback` = `send` na resposta, e o `PostToolUse` só grava `pendentes[agentId]`), `UserPromptSubmit` com `prompt` começando por `<agent-message from="<agentId>">` de agente em `pendentes`, e a resposta é o trecho depois de `The report follows:` (`DTG-39`) · primeira linha não vazia da resposta casa `^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$` | `Agente executor devolveu a tarefa "<título>": review — <pendência>.` | `<pendência>` ← grupo 2; ausente → `sem pendência` |
 | `M-4b` | o mesmo evento, primeira linha casa `^(\S+) blocked motivo=(\S+)\s*(.*)$` | `Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.` | `<motivo>` ← grupo 2; `<razão>` ← grupo 3 |
-| `M-5` | evidência coletada — `PreToolUse` · `Bash` · `command` contém `review_evidence.py` e `--tarefa <ID>`, e não contém `--atribuir` | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa (\S+)` no comando; `<título>` ← estado ou `localizar_card` |
+| `M-5` | evidência coletada — `PreToolUse` · `Bash` · numa invocação do comando o programa é `review_evidence.py`, com `--tarefa <ID>` e sem `--atribuir` nos argumentos dessa mesma invocação (`TK-88c`) | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa` da própria invocação; `<título>` ← estado ou `localizar_card` 
```
[truncado em 4000 caracteres]

### `tests/test_progresso_hook.py`
```
"""TLG-T3 (`docs/plans/P-0748-tela-do-gerente.md` `### TLG-T3b`) — TFs de
`.claude/tools/progresso_hook.py`: ganchos `PreToolUse`/`PostToolUse`/`UserPromptSubmit`/`Stop`
que geram, a cada evento de transição do loop, a frase do repertório `FRASES` e a gravam em
`.claude/estado/progresso.txt`, uma por linha, na ordem em que o loop as atravessa.

Padrão de carga do módulo idêntico a `tests/test_modelo.py:35,53-54` (`.claude/` não é pacote
importável).
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_PROGRESSO_HOOK_PATH = _ROOT / ".claude" / "tools" / "progresso_hook.py"


def _load_progresso_hook():
    spec = importlib.util.spec_from_file_location("progresso_hook", _PROGRESSO_HOOK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


progresso_hook = _load_progresso_hook()


def P(**k):
    return {
        "session_id": "s1",
        "transcript_path": str(Path("t.jsonl")),
        **k,
    }


@pytest.fixture
def raiz(tmp_path):
    plans = tmp_path / "docs" / "plans"
    plans.mkdir(parents=True)
    (plans / "P-9999-teste.md").write_text(
        "# P-9999 — Plano de teste\n"
        "\n"
        "### TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
        "### TLG-T10 — Outro título [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer y.\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "DIARIO_DE_OBRAS.md").write_text(
        "# Diário de Obras — Teste\n"
        "## TK-99 — Tíquete de teste\n"
        "### TK-99a — Card do tíquete [Sonnet · classe mecanica]\n"
        "- **Objetivo:** Fazer z.\n",
        encoding="utf-8",
    )
    return tmp_path


@pytest.fixture
def estado(tmp_path):
    return tmp_path / "estado"


def progresso(estado):
    arq = estado / "progresso.txt"
    if not arq.exists():
        return []
    return arq.read_text(encoding="utf-8").splitlines()


def payload_next(resp_texto, session_id="s1", transcript_path=None):
    p = P(
        hook_event_name="PostToolUse",
        tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py next"},
        tool_response={"stdout": resp_texto},
        session_id=session_id,
    )
    if transcript_path is not None:
        p["transcript_path"] = transcript_path
    return p


def rodar(payload, estado, raiz):
    return progresso_hook.main(entrada=json.dumps(payload), estado=estado, raiz=raiz)


# --- TF-GER-1 -----------------------------------------------------------------------


def test_tf_ger_1_texto_da_resposta():
    f = progresso_hook.texto_da_resposta
    assert f("a\nb") == "a\nb"
    assert f({"stdout": "a\nb"}) == "a\nb"
    assert f({"content": [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]}) == "a\nb"
    assert f([{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]) == "a\nb"
    assert f(None) == ""
    assert f({"x": 1}) == '{"x": 1}'
    assert f({"content": []}) == ""
    assert f([]) == ""
    assert f({"content": [{"type": "image"}]}) == ""


# --- TF-GER-2 -------------------------------------------------------------------------


def test_tf_ger_2_tarefa_escolhida_primeira_da_sessao(estado, raiz):
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    assert rodar(payload, estado, raiz) == 0
    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
    ]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["tarefa"] == "TLG-T9"
    assert estado_loop["titulo"] == "Um título de teste"
    assert estado_loop["obj
```
[truncado em 4000 caracteres]

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index 25c8091..bcb1290 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -1284,6 +1284,24 @@ def test_tf_tk88_close_escreve_tres_secoes_e_preenche_humano_e_historico(tmp_pat
     assert "(nenhuma linha do painel para esta tarefa)" in conteudo2
 
 
+def test_tf_close_grava_plano_em_barra(tmp_path):
+    """TF do `TK-88c`: `cmd_close` com o caminho do plano em barra invertida grava a linha
+    `**Plano:**` sem barra invertida — venha o caminho como vier."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(
+        plano, "### T1 — Tarefa sintética [Sonnet · classe implementacao]", status="done",
+    )
+    plano_barra_invertida = str(plano).replace("/", "\\")
+
+    exit_code = rdo.main(_argv_close(tmp_path, tarefa="T1", **{"--plano": plano_barra_invertida}))
+
+    assert exit_code == 0
+    conteudo = next(p for p in tmp_path.glob("*.md") if p.name not in ("plano.md", "INDEX.md")).read_text(encoding="utf-8")
+    linha_plano = next(l for l in conteudo.splitlines() if l.startswith("**Plano:**"))
+    assert "\\" not in linha_plano
+
+
 # --- laudo --motivo e alvo `dossiê` (TK-85a) --------------------------------------------------
 
 

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-88c-medida.json; mundo: depois; gerado em: 2026-09-27T00:56:13+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_progresso_hook.py tests/test_rdo.py -q -k "propria_invocacao or plano_em_barra"` | 0 | true |
| 2 | `python -c "import re;from pathlib import Path;print(sum(len(re.findall('a tarefa '+chr(34)+'[A-Z][A-Za-z0-9-]*-revisao'+chr(34),p.read_text(encoding='utf-8'))) for p in Path('docs').rglob('*.md'))>0)"` | 0 | true |
| 3 | `python -c "from pathlib import Path;print(sum(1 for p in Path('docs').rglob('*.md') for l in p.read_text(encoding='utf-8').splitlines() if l.startswith(chr(42)*2+'Plano:') and chr(92) in l)>0)"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
