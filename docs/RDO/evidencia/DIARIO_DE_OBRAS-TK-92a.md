# Evidência de revisão — DIARIO_DE_OBRAS TK-92a

## Diff (`git diff --stat`)
```
.claude/README.md                                  |    8 +-
 .claude/agents/pantonic-consultant.md              |   49 +-
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
 .claude/skills/scrum-master/SKILL.md               |  223 +-
 .claude/tools/backlog.py                           |  584 ++-
 .claude/tools/backlog_hook.py                      |   14 +-
 .claude/tools/card_check.py                        |  423 ++-
 .claude/tools/modelo.py                            |   39 +-
 .claude/tools/rdo.py                               |  322 +-
 .claude/tools/rdo_template.md                      |   12 +-
 .claude/tools/review_evidence.py                   |  170 +-
 .claude/tools/telemetria.py                        |   56 +-
 .claude/tools/telemetria_hook.py                   |   15 +-
 GOVERNANCA.md                                      |  413 ++-
 README.md                                          |  196 +-
 docs/CUSTO_DO_PICKUP.md                            |  171 +
 docs/DIARIO_DE_OBRAS.md                            | 3776 +++++++++++++++++++-
 docs/DIARIO_HISTORICO.md                           |  154 +
 docs/DOC_MAP.md                                    |  115 +-
 docs/RDO/INDEX.md                                  |  134 +
 docs/RESIDENCIA_DOUTRINA.md                        |    4 +-
 docs/RUBRICA_DE_REVISAO.md                         |   27 +-
 docs/consultant-spec.md                            |   75 +-
 docs/plans/P-0741-modelo-conceitual.md             |    8 +-
 docs/plans/P-0742-loop-fora-do-llm.md              |  976 ++++-
 docs/plans/P-0745-planejador-modelo-operacao.md    | 1584 +++++++-
 docs/plans/_INBOX.md                               |    3 +-
 docs/plans/_INBOX_HISTORICO.md                     |    9 +
 docs/telemetria.tsv                                |  409 +++
 .../backlog/vermelho/docs/DIARIO_DE_OBRAS.md       |    3 +
 tests/fixtures/modelo/fluxo-concluido.md           |   12 +-
 tests/fixtures/modelo/fluxo-pendente.md            |   20 +-
 tests/fixtures/modelo/fluxo-valido.md              |   12 +-
 tests/fixtures/modelo/plano-invalido-2.md          |   10 +-
 tests/fixtures/modelo/plano-invalido.md            |   12 +-
 tests/fixtures/modelo/plano-sem-cabecalho.md       |    8 +-
 tests/fixtures/modelo/plano-sem-estado.md          |    8 +-
 tests/test_backlog.py                              |  819 +++++
 tests/test_card_check.py                           |  235 ++
 tests/test_materializar.py                         |    2 +-
 tests/test_modelo.py                               |  143 +-
 tests/test_rdo.py                                  |  411 ++-
 tests/test_review_evidence.py                      |  286 +-
 tests/test_telemetria.py                           |   50 +
 tests/test_telemetria_hook.py                      |   35 +
 59 files changed, 11500 insertions(+), 1274 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-executor.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/caminhos.py` — atribuição: da entrega; estado git: `??`
- `.claude/tools/card_check.py` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-92a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_caminhos.py` — atribuição: da entrega; estado git: `??`
- `tests/test_card_check.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `81a398bad593c2593997240fe53b796a89ddedc1`
- Arquivos-alvo declarados: `.claude/tools/caminhos.py`, `.claude/tools/review_evidence.py`, `.claude/tools/card_check.py`, `.claude/agents/pantonic-executor.md`, `.claude/skills/scrum-master/SKILL.md`, `tests/test_caminhos.py`, `tests/test_card_check.py`
- Arquivos tocados: `.claude/agents/pantonic-executor.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/caminhos.py`, `.claude/tools/card_check.py`, `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-92a-medida.json`, `docs/telemetria.tsv`, `tests/test_caminhos.py`, `tests/test_card_check.py`
- Atribuídos a outra tarefa do mesmo plano: `docs/DIARIO_DE_OBRAS.md` → `TK-54b`, `docs/telemetria.tsv` → `TK-88b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-92a-medida.json`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/caminhos.py`
```
"""P-0749 SAN-T1 — residência única da forma do id e do caminho de plano (`DSA-8`).

Duas formas convivem, reconhecidas pelo caminho, sem chave de configuração (`DSA-7`): plano
legado `docs/plans/P-<dígitos>-<slug>.md` e plano em pasta `docs/plans/P-<n>-<slug>/plano.md`.
Nenhuma outra ferramenta guarda cópia destas regex (`I-3`); cada uma carrega este módulo por
caminho, via `importlib.util.spec_from_file_location`. Função entra aqui com o primeiro chamador
de produção (`DSA-18`); `main` é a CLI de listagem e o entry point do módulo (`DSA-19`).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PLANO_HEADER_RE = re.compile(r"^# (P-\d+) — (.+)$")
ID_PLANO_RE = re.compile(r"^P-(\d+)$")
CAMINHO_PLANO_INBOX_RE = re.compile(r"docs/plans/P-\d+-[^)\s`/]+(?:/plano)?\.md")
ID_PLANO_INBOX_RE = re.compile(r"docs/plans/P-(\d+)-")
CONTADOR_INBOX_RE = re.compile(r"\*\*Próximo id de plano: P-\d+\.\*\*")
CONTADOR_INBOX_ID_RE = re.compile(r"\*\*Próximo id de plano: P-(\d+)\.\*\*")

NOME_PLANO_PASTA = "plano.md"
_ID_NO_NOME_RE = re.compile(r"^(P-\d+)")
_PASTA_RE = re.compile(r"^P-\d+-")


def planos_dir(raiz: Path) -> Path:
    return Path(raiz) / "docs" / "plans"


def inbox_planos(raiz: Path) -> Path:
    return planos_dir(raiz) / "_INBOX.md"


def e_layout_pasta(plano_path: Path) -> bool:
    p = Path(plano_path)
    return p.name == NOME_PLANO_PASTA and _PASTA_RE.match(p.parent.name) is not None


def arquivos_de_plano(raiz: Path) -> list[Path]:
    base = planos_dir(raiz)
    legado = [p for p in base.glob("P-*.md") if p.is_file()]
    pasta = [p for p in base.glob("P-*/" + NOME_PLANO_PASTA) if p.is_file() and e_layout_pasta(p)]
    return sorted(legado + pasta)


def id_do_plano(plano_path: Path) -> str | None:
    p = Path(plano_path)
    nome = p.parent.name if e_layout_pasta(p) else p.stem
    m = _ID_NO_NOME_RE.match(nome)
    return m.group(1) if m else None


def pasta_do_plano(plano_path: Path) -> Path | None:
    p = Path(plano_path)
    return p.parent if e_layout_pasta(p) else None


NOME_ESTADO = "estado.tsv"
CABECALHO_ESTADO = "id\ttipo\tstatus\trazao\tdata\tnota"


def estado_tsv(plano_path: Path) -> Path:
    return Path(plano_path).parent / NOME_ESTADO


def formatar_id(numero: int, largura: int) -> str:
    return f"P-{numero:0{largura}d}"


def pasta_por_id(raiz: Path, plano_id: str) -> Path | None:
    achadas = [p.parent for p in planos_dir(raiz).glob(plano_id + "-*/" + NOME_PLANO_PASTA) if p.is_file()]
    return achadas[0] if len(achadas) == 1 else None


def destino_rdo(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "rdo" / f"{tarefa}.md"


def destino_laudo(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "laudos" / f"{tarefa}.md"


def destino_evidencia(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "evidencia" / f"{tarefa}.md"


# Artefatos de fechamento de plano (`GOVERNANCA.md` §4.2, *Pasta do plano*; `TK-88`): o
# documento de validação (`operacoes.md`, skill `entrega-de-encerramento`) e a entrega aceita
# (`entrega.md`, escrita por `encerrar.py plano`). Plano legado: `docs/OPERACOES_AS_IS_<id>.md`
# e `docs/plans/_ENTREGA-<id>.md`, ao lado de `_CENARIO-<id>.md`.
def destino_operacoes(raiz: Path, plano_path: Path) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "operacoes.md"
    return Path(raiz) / "docs" / f"OPERACOES_AS_IS_{id_do_plano(plano_path)}.md"


def destino_entrega(raiz: Path, plano_path: Path) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "entrega.md"
    return planos_dir(raiz) / f"_ENTREGA-{id_do_plano(plano_path)}.md"


# Destino único da medida do executor (`TK-92a`): plano em pasta grava/procura ao lado do
# plano; plano legado e tíquete do diário (ex.: `docs/DIARIO_DE_OBRAS.md`) caem em
# `<raiz>/docs/RDO/evidencia`, com `<id ou stem>` = `id_do_plano(plano_path) or
# Path(plano_path).stem` — a mesma regra que `review_
```
[truncado em 4000 caracteres]

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index e57b69f..4b98a92 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -785,10 +785,10 @@ def montar_documento(
 
     plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem
 
-    dir_evidencia_efetivo = (
-        Path(dir_evidencia) if dir_evidencia is not None else Path(root) / "docs" / "RDO" / "evidencia"
-    )
-    caminho_medida = dir_evidencia_efetivo / f"{plano_id}-{dossie.tarefa_id}-medida.json"
+    if dir_evidencia is not None:
+        caminho_medida = Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"
+    else:
+        caminho_medida = _caminhos.destino_medida(root, plano_path, dossie.tarefa_id)
 
     return _renderizar(
         plano_id=plano_id,

```

### `.claude/tools/card_check.py`
```
diff --git a/.claude/tools/card_check.py b/.claude/tools/card_check.py
index 5b8b2bc..e363b76 100644
--- a/.claude/tools/card_check.py
+++ b/.claude/tools/card_check.py
@@ -60,6 +60,18 @@ def _load_rdo(root: Path):
     return modulo
 
 
+def _carregar_caminhos():
+    caminho = Path(__file__).resolve().parent / "caminhos.py"
+    spec = importlib.util.spec_from_file_location("caminhos", caminho)
+    modulo = importlib.util.module_from_spec(spec)
+    sys.modules[spec.name] = modulo
+    spec.loader.exec_module(modulo)
+    return modulo
+
+
+_caminhos = _carregar_caminhos()
+
+
 def _forcar_utf8(stream) -> None:
     """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `→` — duplicado do
     mesmo utilitário de `review_evidence.py` (`DM-11`, sem import cruzado entre módulos)."""
@@ -509,10 +521,13 @@ def main(argv: list[str] | None = None) -> int:
     )
     parser.add_argument(
         "--gravar",
+        nargs="?",
+        const=True,
         type=Path,
         default=None,
         help=(
-            "Grava a medida (FPU-T5, DFP-17) neste caminho .json — um registro por item de "
+            "Grava a medida (FPU-T5, DFP-17, TK-92a) — com caminho, neste .json; sem caminho, "
+            "em caminhos.destino_medida(--root, --plano, --tarefa) — um registro por item de "
             "Verificação, ok ou não; não muda exit, stdout nem stderr."
         ),
     )
@@ -525,6 +540,11 @@ def main(argv: list[str] | None = None) -> int:
         return 1
 
     if args.gravar is not None:
+        destino = (
+            _caminhos.destino_medida(args.root, args.plano, args.tarefa)
+            if args.gravar is True
+            else args.gravar
+        )
         dados = {
             "plano": medida["plano"],
             "tarefa": medida["tarefa"],
@@ -533,14 +553,14 @@ def main(argv: list[str] | None = None) -> int:
             "itens": medida["itens"],
         }
         conteudo = json.dumps(dados, ensure_ascii=False, indent=2)
-        args.gravar.parent.mkdir(parents=True, exist_ok=True)
+        destino.parent.mkdir(parents=True, exist_ok=True)
         fd, tmp_path = tempfile.mkstemp(
-            dir=str(args.gravar.parent), prefix=".card-check-", suffix=".tmp"
+            dir=str(destino.parent), prefix=".card-check-", suffix=".tmp"
         )
         try:
             with os.fdopen(fd, "w", encoding="utf-8") as tmp_file:
                 tmp_file.write(conteudo)
-            os.replace(tmp_path, args.gravar)
+            os.replace(tmp_path, destino)
         except Exception:
             Path(tmp_path).unlink(missing_ok=True)
             raise

```

### `.claude/agents/pantonic-executor.md`
```
diff --git a/.claude/agents/pantonic-executor.md b/.claude/agents/pantonic-executor.md
index e2c665b..3920e3c 100644
--- a/.claude/agents/pantonic-executor.md
+++ b/.claude/agents/pantonic-executor.md
@@ -124,7 +124,7 @@ aceitável. Se a resposta honesta é a segunda, você acabou de encontrar o sina
    `guardrails-check`). Piso nunca desce; teste com significado alterado é reescrito, não
    deletado. Teste que quebra por motivo que o card não previu não é para você consertar
    "do jeito que parece certo": é sinal do passo 4.
-5a. **Medida gravada**: rode `python .claude/tools/card_check.py --plano <plano> --tarefa <ID> --mundo depois --gravar <evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta — a pasta em que `review_evidence.py` procura a medida; exit 1 é entrega incompleta, não verde com ressalva.
+5a. **Medida gravada**: rode `python .claude/tools/card_check.py --plano <plano> --tarefa <ID> --mundo depois --gravar`, sem caminho — o destino é o de `caminhos.destino_medida`, o mesmo em que `review_evidence.py` procura a medida, em plano legado, plano em pasta e tíquete do diário; exit 1 é entrega incompleta, não verde com ressalva.
 6. **Encerramento**: sinalize `review` e encerre. A sua última mensagem é **só** a linha de retorno do despacho, sem nada antes nem depois: o loop lê a primeira linha não vazia e descarta o resto sem ler; o que precisa chegar a ele vai em `pendencia=`, numa linha. Você não avalia a própria entrega: `review`
    significa "testes verdes e card cumprido ao pé da letra", não "ficou bom".
 

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index a70e30f..920b0d5 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -116,7 +116,7 @@ Dez passos, nesta ordem.
   `dependencia|premissa|ferramenta`, ou prosa no lugar da linha: **retorno inválido**, regra `A2`. Linha válida seguida de prosa **não** é retorno inválido: vale a primeira linha não vazia — a mesma que o gancho do painel lê —, a prosa depois dela é descartada sem reenvio de formato, e o descarte se anota numa linha do relatório de encerramento.
 - **Saída:** `status` materializado (`review` ou `blocked`), o `motivo` quando `blocked`, a
   `pendencia` quando presente, e os `tools` gastos lidos do `<usage>`, e o arquivo de medida em
-  `<evidencia>/<P-n>-<ID>-medida.json` (`<P-n>` o id do plano; `<evidencia>` = `docs/RDO/evidencia` no legado, `<pasta>/evidencia` no plano em pasta), cuja ausência vai ao laudo como verificação não
+  o destino de `caminhos.destino_medida` (o `card_check.py --gravar` sem caminho grava ali e o `review_evidence.py` procura ali), cuja ausência vai ao laudo como verificação não
   feita.
 
 ### Passo 6 — Despacho do `reviewer`

```

### `tests/test_caminhos.py`
```
"""P-0749 SAN-T1 — TF de `.claude/tools/caminhos.py`, carregado por caminho (`.claude/` não é
pacote importável), mesmo padrão dos demais testes de ferramenta do kit."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_CAMINHOS_PATH = Path(__file__).resolve().parents[1] / ".claude" / "tools" / "caminhos.py"


def _carregar_caminhos():
    spec = importlib.util.spec_from_file_location("caminhos", _CAMINHOS_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


caminhos = _carregar_caminhos()


def test_tf_san_1_id_aceita_zero_e_legado():
    assert caminhos.ID_PLANO_RE.match("P-0")
    assert caminhos.ID_PLANO_RE.match("P-12")
    assert caminhos.ID_PLANO_RE.match("P-0749")
    assert not caminhos.ID_PLANO_RE.match("P-")
    assert not caminhos.ID_PLANO_RE.match("P-12a")


def test_tf_san_2_id_do_plano_nas_duas_formas():
    assert caminhos.id_do_plano(Path("docs/plans/P-0-gama/plano.md")) == "P-0"
    assert caminhos.id_do_plano(Path("docs/plans/P-12-x/plano.md")) == "P-12"
    assert caminhos.id_do_plano(Path("docs/plans/P-0749-saneamento-artefatos.md")) == "P-0749"
    assert caminhos.id_do_plano(Path("tmp/plano.md")) is None


def test_tf_destino_medida_tres_residencias():
    """`TK-92a` — `destino_medida` cobre as três residências pela mesma função: tíquete do
    diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava ao lado
    do plano, em `<pasta>/evidencia`."""
    raiz = Path("/raiz")

    assert caminhos.destino_medida(
        raiz, Path("docs/DIARIO_DE_OBRAS.md"), "TK-1a"
    ) == raiz / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-TK-1a-medida.json"

    assert caminhos.destino_medida(
        raiz, Path("docs/plans/P-0001-x.md"), "T1"
    ) == raiz / "docs" / "RDO" / "evidencia" / "P-0001-T1-medida.json"

    assert caminhos.destino_medida(
        raiz, Path("docs/plans/P-0002-y/plano.md"), "T2"
    ) == Path("docs/plans/P-0002-y") / "evidencia" / "P-0002-T2-medida.json"


def test_tf_san_3_arquivos_de_plano(tmp_path):
    base = tmp_path / "docs" / "plans"
    base.mkdir(parents=True)
    (base / "P-0749-a.md").write_text("a", encoding="utf-8")
    (base / "P-0-b").mkdir()
    (base / "P-0-b" / "plano.md").write_text("b", encoding="utf-8")
    (base / "_INBOX.md").write_text("inbox", encoding="utf-8")
    (base / "P-1-c").mkdir()
    (base / "P-2-d").mkdir()
    (base / "P-2-d" / "outro.md").write_text("outro", encoding="utf-8")

    resultado = caminhos.arquivos_de_plano(tmp_path)

    assert resultado == [
        tmp_path / "docs" / "plans" / "P-0-b" / "plano.md",
        tmp_path / "docs" / "plans" / "P-0749-a.md",
    ]


def test_tf_san_5_linha_viva_do_inbox():
    m1 = caminhos.CAMINHO_PLANO_INBOX_RE.search("- `docs/plans/P-0-gama/plano.md` — nota")
    assert m1 and m1.group(0) == "docs/plans/P-0-gama/plano.md"

    m2 = caminhos.CAMINHO_PLANO_INBOX_RE.search(
        "- `docs/plans/P-0749-saneamento-artefatos.md` — nota"
    )
    assert m2 and m2.group(0) == "docs/plans/P-0749-saneamento-artefatos.md"


def test_tf_san_16_cli_lista_os_planos(tmp_path, capsys):
    base = tmp_path / "docs" / "plans"
    base.mkdir(parents=True)
    (base / "P-0749-a.md").write_text("a", encoding="utf-8")
    (base / "P-0-b").mkdir()
    (base / "P-0-b" / "plano.md").write_text("b", encoding="utf-8")

    codigo = caminhos.main(["--root", str(tmp_path)])

    assert codigo == 0
    saida = capsys.readouterr().out
    assert saida == "P-0\tdocs/plans/P-0-b/plano.md\nP-0749\tdocs/plans/P-0749-a.md\n"


def test_tf_san_4_pasta_por_id_sem_colisao_de_prefixo(tmp_path):
    base = tmp_path / "docs" / "plans"
    base.mkdir(parents=True)
    (base / "P-1-a").mkdir()
    (base / "P-1-a" / "plano.md").write_text("a", encoding="utf-8")
    (base / "P-12-b").mkdir()
    (base / "P-12-b" / "plano.md").write_text("b", encoding="utf-8")

    assert caminhos.pasta_por_id(tmp_path, "P-1") == base / "P-1-a"
    ass
```
[truncado em 4000 caracteres]

### `tests/test_card_check.py`
```
diff --git a/tests/test_card_check.py b/tests/test_card_check.py
index 0a37ac1..f9ae5df 100644
--- a/tests/test_card_check.py
+++ b/tests/test_card_check.py
@@ -8,6 +8,7 @@ from __future__ import annotations
 
 import importlib.util
 import json
+import shutil
 from pathlib import Path
 
 _ROOT = Path(__file__).resolve().parents[1]
@@ -343,3 +344,29 @@ def test_tf_gravar_guarda_a_cauda_da_saida(tmp_path, capsys):
     saida = dados["itens"][0]["saida"]
     assert saida.endswith("FIM")
     assert len(saida) == 400
+
+
+def test_tf_gravar_sem_caminho_grava_no_destino_derivado(tmp_path, capsys):
+    """`TK-92a` — `--gravar` sem caminho grava em `caminhos.destino_medida(--root, --plano,
+    --tarefa)`: com `plano-corpus.md` copiado como `docs/DIARIO_DE_OBRAS.md` numa raiz
+    temporária (que carrega uma cópia de `rdo.py`/`caminhos.py`, como `verificar_tarefa`
+    exige de qualquer `--root`), o destino é `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida.json`,
+    dentro da própria raiz temporária — nada é gravado no repositório."""
+    card_check = _load_card_check()
+    ferramentas = tmp_path / ".claude" / "tools"
+    ferramentas.mkdir(parents=True)
+    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
+    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
+    plano = tmp_path / "docs" / "DIARIO_DE_OBRAS.md"
+    plano.parent.mkdir(parents=True)
+    plano.write_text(_PLANO_CORPUS.read_text(encoding="utf-8"), encoding="utf-8")
+
+    codigo = card_check.main(
+        ["--plano", str(plano), "--tarefa", "CX-T1", "--root", str(tmp_path), "--gravar"]
+    )
+    capsys.readouterr()
+
+    assert codigo == 0
+    destino = tmp_path / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-CX-T1-medida.json"
+    dados = json.loads(destino.read_text(encoding="utf-8"))
+    assert dados["tarefa"] == "CX-T1"

```

## Medida do executor
- Arquivo: docs\RDO\evidencia\DIARIO_DE_OBRAS-TK-92a-medida.json; mundo: depois; gerado em: 2026-09-27T04:15:32+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import sys;sys.path.insert(0,'.claude/tools');import caminhos as c;from pathlib import Path;print(c.destino_medida(Path('.'),Path('docs/DIARIO_DE_OBRAS.md'),'TK-86a').as_posix())"` | 0 | true |
| 2 | `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('<P-n>-<ID>-medida.json') for f in fs))"` | 0 | true |
| 3 | `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('caminhos.destino_medida') for f in fs))"` | 0 | true |
| 4 | `python -m pytest tests/test_caminhos.py tests/test_card_check.py -q -k "destino_medida or gravar_sem_caminho"` | 0 | true |
| 5 | `python -m pytest -q` | 0 | true |
| 6 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
