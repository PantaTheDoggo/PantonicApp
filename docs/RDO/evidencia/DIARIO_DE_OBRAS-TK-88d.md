# Evidência de revisão — DIARIO_DE_OBRAS TK-88d

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
 .claude/tools/backlog.py                           |  584 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  403 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  322 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  166 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  400 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3731 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  126 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 ++++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    8 +
 docs/telemetria.tsv                                |  382 ++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  819 +++++
 tests/test_card_check.py                           |  208 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  265 +-
 tests/test_telemetria_hook.py                      |   35 +
 56 files changed, 10426 insertions(+), 1090 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `bfad89d5f78c207b984775d9fb4df0d8f99a6b2d`
- Arquivos-alvo declarados: `.claude/tools/rdo.py`, `.claude/tools/backlog.py`, `.claude/tools/encerrar.py`, `tests/test_rdo.py`, `tests/test_backlog.py`, `tests/test_encerrar.py`
- Literais não reconhecidos como caminho (5): `cmd_close`, `transacionar_status`, `fechar_tarefa`, `fechar_plano`, `main`
- Arquivos tocados: `.claude/tools/backlog.py`, `.claude/tools/encerrar.py`, `.claude/tools/rdo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d-medida.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`, `tests/test_encerrar.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-88d-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 6cac10d..9b376ed 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -760,10 +760,15 @@ def _regenerar_indice(rdo_dir: Path) -> Path:
     return indice_path
 
 
-def cmd_close(args: argparse.Namespace) -> Path:
+def checar_close(args: argparse.Namespace, status_exigido: str = "done") -> Path:
+    """As checagens do `cmd_close`, sem escrita, devolvendo o destino do RDO (`TK-88d`): guarda
+    de domínio do consumo, plano/dossiê, status da tarefa (fonte de `_status_atual`, comparada a
+    `status_exigido` — `cmd_close` usa `"done"`; quem checa **antes** de escrever o `done`, como
+    `encerrar.py fechar_tarefa`, usa `"review"`), template e o destino do RDO (recusa se já
+    existe — tarefa já fechada). Nenhum arquivo é tocado."""
     # Guarda de domínio do consumo (`P-0740` `LM-T1a`, `DM-15` (iii); `--nao-medido` na `TK-88b`)
-    # — corre antes de qualquer outra checagem de `cmd_close`, `--plano` incluso: nada é lido nem
-    # escrito se o trio estiver fora do domínio, incompleto, ou junto de `--nao-medido`.
+    # — corre antes de qualquer outra checagem, `--plano` incluso: nada é lido nem escrito se o
+    # trio estiver fora do domínio, incompleto, ou junto de `--nao-medido`.
     trio = (args.tool_uses, args.tokens_k, args.duracao_s)
     tem_nao_medido = args.nao_medido is not None
     if tem_nao_medido and any(v is not None for v in trio):
@@ -773,16 +778,14 @@ def cmd_close(args: argparse.Namespace) -> Path:
     if not tem_nao_medido and not all(v is not None for v in trio):
         raise RdoValidationError("consumo: exige --tool-uses/--tokens-k/--duracao-s ou --nao-medido")
 
-    razao_nao_medido: str | None = None
-    tool_uses = tokens_k = duracao_s = None
     if tem_nao_medido:
         razao_nao_medido = args.nao_medido.strip()
         if not razao_nao_medido or _contar_linhas(args.nao_medido) > 1:
             raise RdoValidationError("nao_medido: razão é uma linha não vazia")
     else:
-        tool_uses = _validar_inteiro_nao_negativo("tool_uses", args.tool_uses)
-        tokens_k = _validar_numero_nao_negativo_finito("tokens_k", args.tokens_k)
-        duracao_s = _validar_numero_nao_negativo_finito("duracao_s", args.duracao_s)
+        _validar_inteiro_nao_negativo("tool_uses", args.tool_uses)
+        _validar_numero_nao_negativo_finito("tokens_k", args.tokens_k)
+        _validar_numero_nao_negativo_finito("duracao_s", args.duracao_s)
 
     plano_path = Path(args.plano)
     if not plano_path.is_file():
@@ -798,27 +801,56 @@ def cmd_close(args: argparse.Namespace) -> Path:
 
     pasta_plano = _caminhos.pasta_do_plano(plano_path)
     status_atual = _status_atual(plano_path, dossie.tarefa_id, dossie, pasta_plano)
-    if status_atual != "done":
+    if status_atual != status_exigido:
         raise RdoValidationError(
-            f"status: tarefa '{dossie.tarefa_id}' está '{status_atual or 'ausente'}', exigido 'done'"
+            f"status: tarefa '{dossie.tarefa_id}' está '{status_atual or 'ausente'}', exigido '{status_exigido}'"
         )
 
     template_path = args.template if args.template is not None else _default_template_path()
     if not template_path.is_file():
         raise RdoValidationError(f"template: arquivo não encontrado '{template_path}'")
-    template_texto = template_path.read_text(encoding="utf-8")
 
     plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem
     nome_arquivo = f"{plano_id}-{dossie.tarefa_id}-{_slugify(dossie.titulo)}.md"
 
     if args.rdo_dir is None and pasta_plano is not None:
         destino = _caminhos.destino_rdo(pasta_plano, dossie.tarefa_id)
-        rdo_dir = destino.parent
     else:
         rdo_dir = Path(args.rdo_dir) if args.rdo_dir is not None else _default_rdo_dir()
         destino = rdo_dir / nome_arquivo
     if destino.exists():
         raise RdoValidationError(f"rdo: '{destino}' já existe — tarefa já fechada")
+    return destino
+
+
+def cmd_c
```
[truncado em 4000 caracteres]

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 952b310..6744b40 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -1709,17 +1709,17 @@ def _regenerar_bloco_fila(modelo: Modelo, diario_linhas: list[str]) -> str | Non
     return None
 
 
-def transacionar_status(
-    repo: Path,
+def checar_transicao(
     modelo: Modelo,
     id_: str,
     estado: str,
     razao: str | None = None,
-    nota: str | None = None,
-) -> ResultadoStatus:
-    """§2.7 + §3 — `status`/`start`: transição e escrita atômica das projeções, num ato
-    só. Nenhuma escrita ocorre antes de todas as checagens (E-2, E-3, tabela de §2.7,
-    `blocked` exige `--razao`) passarem."""
+) -> ResultadoStatus | None:
+    """As checagens de `transacionar_status` que não dependem do repositório (`TK-88d`): id,
+    E-2, posição de índice do pai, a tabela de §2.7 — com o ramo especial de plano `done` — ,
+    `blocked` exige `--razao` e o travessão na razão. `None` quando a transição pode passar;
+    quem chama ainda decide a escrita. As checagens de `estado.tsv` (dependem de `repo`)
+    continuam só em `transacionar_status`."""
     alvo = _localizar(modelo, id_)
     if alvo is None:
         return ResultadoStatus(1, f"id não encontrado: {id_}")
@@ -1767,6 +1767,27 @@ def transacionar_status(
         if any(irmao is not alvo and irmao.status == "in-progress" for irmao in irmaos):
             return ResultadoStatus(1, f"já há item in-progress no mesmo pai: {pai.id}")
 
+    return None
+
+
+def transacionar_status(
+    repo: Path,
+    modelo: Modelo,
+    id_: str,
+    estado: str,
+    razao: str | None = None,
+    nota: str | None = None,
+) -> ResultadoStatus:
+    """§2.7 + §3 — `status`/`start`: transição e escrita atômica das projeções, num ato
+    só. Nenhuma escrita ocorre antes de todas as checagens (`checar_transicao`, mais a
+    consistência de `estado.tsv`, que depende de `repo`) passarem."""
+    resultado = checar_transicao(modelo, id_, estado, razao)
+    if resultado is not None:
+        return resultado
+
+    alvo = _localizar(modelo, id_)
+    pai, tipo_pai = _pai_do_alvo(modelo, alvo)
+
     plano_pasta = alvo if isinstance(alvo, Plano) else next(
         (p for p in modelo.planos if alvo.tipo == "tarefa" and p.arquivo == alvo.arquivo), None
     )

```

### `.claude/tools/encerrar.py`
```
"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — o fechamento de tarefa e o de plano deixam de
ser uma sequência de comandos e prosa escrita à mão e passam a ser **um comando cada**, que recebe
a informação da tarefa realizada, escreve os artefatos de fechamento que o kit já tinha e faz os
registros nos documentos de backlog no mesmo ato.

Lugar comum medido (2026-09-26, sobre os fechamentos de `P-0745`..`P-0751`): fechar uma tarefa
eram quatro comandos em turnos separados — `modelo.py check`, `backlog.py status <ID> done`,
`rdo.py close` com o pacote do laudo **redigitado** a partir do arquivo que `rdo.py laudo` já
tinha gravado, e `telemetria.py append` conferindo a linha do hook —, mais o achado `AE-<n>`
editado no plano; fechar um plano era inteiramente manual, porque o instrumento recusava
`ready → done` para plano (registrado no diário em 2026-09-25) e o parágrafo de fechamento, a
linha do índice e a triagem dos achados eram escritos à mão.

Três verbos, todos com as checagens **antes** de qualquer escrita. `tarefa` e `plano` **reportam**
resultado e histórico; `handover` **entrega** — é o que quem vem depois espera da tarefa, de forma
inequívoca, direta e objetiva, inteiramente de máquina, registrado **na própria tarefa**:

``python .claude/tools/encerrar.py handover --plano <caminho.md> --tarefa <ID> --entregue "<o que
existe, com caminho:linha>" --contrato "<com o que a sucessora conta>" [--nao-refazer "<o que já
está pago>"] [--pendente "<o que fica de propósito>"] [--para <ID|papel>]... [--repo] [--data]``

Escreve (ou substitui) o campo `- **Handover:** <data> · para \\`<ID>\\`...` com os sub-bullets
`Entregue`, `Contrato`, `Não refazer` e `Pendente` no card, antes de `- **Notas de execução:**`;
exige entrega na árvore (`in-progress`, `review`, `done` ou `blocked`). A nomenclatura é a
âncora da recuperação: `backlog.py next` (`handovers_para`) devolve, sob `=== HANDOVER DE <ID>`,
junto com a próxima tarefa, o handover de todo irmão que a nomeia em `para` e, na falta, o da
antecessora imediata — o orquestrador cola na delegação o que for pertinente. O `rdo.py close`
transcreve o campo no RDO como extra do card, e `show <ID>` o imprime verbatim.

Os outros dois:

``python .claude/tools/encerrar.py tarefa --plano <caminho.md> --tarefa <ID> [--resumo "<frase>"]
[--pendencia "<uma linha>"] [--achado "<texto>" "<rota>"]... [--laudo <caminho>]
[--tool-uses N --tokens-k K --duracao-s S [--modelo-agente <nome>]] [--progresso <caminho>]
[--rdo-dir <dir>] [--repo <raiz>] [--data AAAA-MM-DD]``

1. a tarefa está em `review` (única transição que produz RDO — skill `diario-de-obras`,
   *Máquina de transições*, gatilho 2); 2. o laudo existe (`<pasta>/laudos/<ID>.md` ou
   `docs/RDO/laudos/<plano>-<ID>.md`) e o pacote é **transcrito** dele — veredito, percentual,
   bloqueante, recomendação, pendência e lições —, nunca redigitado; `reprovado` é recusado
   (`GOVERNANCA.md` §4.2: não é desfecho de RDO); 3. o consumo vem da **fonte única**
   `docs/telemetria.tsv` (última linha da tarefa, gravada pelo hook `SubagentStop`) ou, quando o
   chamador traz o bloco `<usage>` em `--tool-uses/--tokens-k/--duracao-s`, é apensado à série no
   mesmo ato; sem nenhum dos dois o fechamento é recusado — número inventado não fecha tarefa;
   4. `modelo.py check` sai `0` ou `2` (exit `1` mantém a tarefa em `review`, `DMC-30`).
   Passadas as checagens, e nesta ordem: `backlog.transacionar_status(<ID>, done)` com a nota de
   fechamento (bullet do card, índice `done/total`, bloco `Fila corrente`, `estado.tsv`);
   `rdo.cmd_close` em processo, com as seções `# Humano` e `# Histórico` preenchidas — o humano em
   linguagem corrente, com o título da tarefa no lugar da sigla (`GOVERNANCA.md` §4.2, *Mensagem
   legível ao dono*), e o histórico com as linhas que o painel do gerente (`progresso_hook.py`)
   gerou para a tarefa; a linha de telemetria, se o consumo veio por argumento; e cada `--achado`
   como entrada `AE-<n>` com `**Rota:**` em `## Achados
```
[truncado em 4000 caracteres]

### `tests/test_rdo.py`
```
(sem alteração desde `bfad89d5f78c207b984775d9fb4df0d8f99a6b2d`)
```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index 17cee9b..abf89e2 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -2680,6 +2680,26 @@ def test_tr_tk88_plano_com_tarefa_aberta_nao_fecha_e_tarefa_segue_a_tabela(tmp_p
     assert plano.read_text(encoding="utf-8") == antes
 
 
+def test_tf_checar_transicao_sem_escrita(tmp_path):
+    """TF (`TK-88d`): `checar_transicao` devolve, para o plano com tarefa aberta, o mesmo
+    resultado que `transacionar_status` produz — sem tocar arquivo (a função não recebe
+    `repo`); quem escreve continua sendo só `transacionar_status`."""
+    backlog = _load_backlog()
+    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
+    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
+    plano.write_text(plano.read_text(encoding="utf-8").replace("- **Status:** `done` · 2026-01-01", "- **Status:** `ready` · 2026-01-01"), encoding="utf-8")
+    antes = plano.read_text(encoding="utf-8")
+    modelo = backlog.carregar(repo)
+
+    resultado_checagem = backlog.checar_transicao(modelo, "P-0001", "done")
+    resultado_transacao = backlog.transacionar_status(repo, modelo, "P-0001", "done")
+
+    assert resultado_checagem is not None
+    assert resultado_checagem.exit_code == 1 and "ALF-T1" in resultado_checagem.mensagem
+    assert resultado_checagem.mensagem == resultado_transacao.mensagem
+    assert plano.read_text(encoding="utf-8") == antes
+
+
 # --- TK-88 — o next devolve o handover à sucessora -------------------------------------------
 
 

```

### `tests/test_encerrar.py`
```
"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — TF/TR de `.claude/tools/encerrar.py`, o
instrumento de fechamento de tarefa e de plano. Repositório sintético em `tmp_path` com diário,
plano legado, laudo, série de telemetria e painel do gerente; nenhum teste toca a árvore real.
Padrão de carga por caminho igual ao de `tests/test_backlog.py` (`.claude/` não é pacote)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_ENCERRAR_PATH = _ROOT / ".claude" / "tools" / "encerrar.py"


def _load_encerrar():
    spec = importlib.util.spec_from_file_location("encerrar", _ENCERRAR_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


encerrar = _load_encerrar()

TITULO_T1 = "Primeira tarefa do plano"
TITULO_T2 = "Segunda tarefa, cancelada"
TITULO_PLANO = "Plano alfa"

DIARIO = (
    "# Diário de Obras — Teste\n"
    "**Diretiva de priorização:** Priorize `P-0001`.\n"
    "\n"
    "<!-- fila:gerada -->\n"
    "**Fila corrente:** —\n"
    "<!-- /fila:gerada -->\n"
    "\n"
    "## Índice\n"
    "\n"
    "| ID | Título | Status | Âncora |\n"
    "|---|---|---|---|\n"
    "| P-0001 | Plano alfa | ready 0/1 | docs/plans/P-0001-alfa.md |\n"
)

PLANO = (
    f"# P-0001 — {TITULO_PLANO}\n"
    "\n"
    "**Status:** `ready` · **Prefixo das tarefas no diário:** `ALF-T<n>`\n"
    "\n"
    "## 5. Tarefas\n"
    "\n"
    f"### ALF-T1 — {TITULO_T1} [Sonnet · classe implementacao]\n"
    "- **Status:** `{status_t1}` · 2026-09-20\n"
    "- **Objetivo:** entregar a primeira coisa.\n"
    "- **Arquivos-alvo:** `a.py`.\n"
    "- **Verificação:** `pytest -q`.\n"
    "- **Pronto quando:** o teste passa.\n"
    "\n"
    f"### ALF-T2 — {TITULO_T2} [Sonnet · classe implementacao]\n"
    "- **Status:** `cancelled` · 2026-09-20 · absorvida\n"
    "- **Objetivo:** nada.\n"
    "- **Arquivos-alvo:** `b.py`.\n"
    "- **Verificação:** nenhuma.\n"
    "- **Pronto quando:** nunca.\n"
    "\n"
    "## 8. Achados da execução\n"
    "\n"
    "- **AE-1** (`ALF-T1`, laudo, 2026-09-21) — achado antigo. **Rota:** registrado, sem ação.\n"
)

LAUDO = (
    "# Laudo — P-0001 · ALF-T1\n"
    "\n"
    "**Percentual:** 91%\n"
    "**Veredito:** ressalva\n"
    "**Dimensão bloqueante:** nenhuma\n"
    "**Recomendação:** seguir com ressalva\n"
    "**Pendência:** o teste novo não cobre o ramo vazio\n"
    "\n"
    "## Lições aprendidas na tarefa\n"
    "\n"
    "Observação qualitativa do revisor.\n"
)

TELEMETRIA = (
    "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"
    "2026-09-25\trepo\tALF-T1\tsonnet\t21\t77.5\t300.2\tusage\n"
    "2026-09-25\trepo\tALF-T1-revisao\topus\t9\t40.0\t120.0\tusage\n"
)

PAINEL = (
    f'Abrindo a janela do plano "{TITULO_PLANO}".\n'
    f'Tarefa "{TITULO_T1}". Passo: conferir os gates e preparar o despacho.\n'
    'Tarefa "Outra coisa de outro plano". Passo: conferir os gates e preparar o despacho.\n'
    f'Agente revisor devolveu a tarefa "{TITULO_T1}": ressalva 91%, bloqueante nenhuma.\n'
)


def _montar_repo(tmp_path: Path, status_t1: str = "review") -> Path:
    repo = tmp_path / "repo"
    (repo / "docs" / "plans").mkdir(parents=True)
    (repo / "docs" / "RDO" / "laudos").mkdir(parents=True)
    (repo / ".claude" / "estado").mkdir(parents=True)
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text(DIARIO, encoding="utf-8")
    (repo / "docs" / "plans" / "P-0001-alfa.md").write_text(PLANO.format(status_t1=status_t1), encoding="utf-8")
    (repo / "docs" / "plans" / "_INBOX.md").write_text("**Próximo id de plano: P-0002.**\n", encoding="utf-8")
    (repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md").write_text(LAUDO, encoding="utf-8")
    (repo / "docs" / "telemetria.tsv").write_text(TELEMETRIA, encoding="utf-8")
    (repo / ".claude" / "estado" / "progresso.txt").write_text(PAINEL, encoding="utf-8")
    return repo

```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-88d-medida.json; mundo: depois; gerado em: 2026-09-27T01:25:58+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_backlog.py -q -k "checar_close or checar_transicao or fechado_conta"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print(t.count('tarefa já fechada'),t.count('não terminal(is)'))"` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
