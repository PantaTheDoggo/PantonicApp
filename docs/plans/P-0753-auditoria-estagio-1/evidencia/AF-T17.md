# Evidência de revisão — P-0753 AF-T17

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                 |  10 +-
 .claude/tools/prevoo.py                            | 159 +++++++++++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T17-medida.json            |  43 ++++++
 docs/telemetria.tsv                                |   3 +
 tests/piso_comportamental.txt                      |   1 +
 tests/test_prevoo.py                               |  94 ++++++++++++
 8 files changed, 312 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/prevoo.py` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T17-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/piso_comportamental.txt` — atribuição: alheio; estado git: `??`
- `tests/test_prevoo.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `721720bfd8272eff6b2693c19ba49e083ea3e616`
- Arquivos-alvo declarados: `.claude/tools/prevoo.py`, `tests/test_prevoo.py`, `.claude/agents/pantonic-planner.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `.claude/tools/prevoo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T17-medida.json`, `docs/telemetria.tsv`, `tests/piso_comportamental.txt`, `tests/test_prevoo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T17-medida.json`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `tests/piso_comportamental.txt`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/prevoo.py`
```
"""AF-T17 (`docs/plans/P-0753-auditoria-estagio-1/plano.md` `### AF-T17`) — o pré-voo do pedido:
`python .claude/tools/prevoo.py "<texto>" [--root <caminho>]` confere, antes da campanha de
planejamento, se cada caminho, símbolo e flag citado no pedido do dono existe de fato na árvore —
premissa do pedido que não existe não deveria virar pergunta ao scout.

Extrai do texto, sem repetir e na ordem da primeira aparição dentro de cada categoria:

- **caminhos** — token terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml`
  ou `.toml`, ou terminado em `/`; existe quando `(<root> / <token>)` existe; `onde` é o próprio
  caminho.
- **símbolos** — nome seguido de `(`, ou identificador com `_` que não é caminho nem flag; existe
  quando algum `.py` sob `<root>` (fora de `.git` e `__pycache__`) tem a linha `def <nome>(` ou
  `class <nome>`; `onde` é `<arquivo>:<linha>` da primeira ocorrência, com `/`.
- **flags** — token que começa por `-` seguido de letra; existe quando algum `.py` sob
  `<root>/.claude` contém a flag entre aspas (`"<flag>"` ou `'<flag>'`); `onde` é
  `<arquivo>:<linha>` da primeira ocorrência, com `/`.

Só leitura: não escreve em arquivo nenhum, não chama rede. Carregado por
`importlib.util.spec_from_file_location` nos testes (`.claude/` não é pacote importável) — não
importa de `tests` nem de `caminhos` (`tests/conformance/test_camadas_do_kit.py`, AF-T15)."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_EXTENSOES_CAMINHO = (".py", ".md", ".ps1", ".json", ".tsv", ".txt", ".yml", ".yaml", ".toml")
_RE_IDENTIFICADOR = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir acento — mesmo padrão
    de `card_check.py`/`review_evidence.py`, sem import cruzado entre módulos."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def _e_caminho(token: str) -> bool:
    return token.endswith(_EXTENSOES_CAMINHO) or token.endswith("/")


def _e_flag(token: str) -> bool:
    sem_traco = token.lstrip("-")
    return token != sem_traco and bool(sem_traco) and sem_traco[0].isalpha()


def _simbolo_de(token: str) -> str | None:
    """Devolve o nome do símbolo citado por `token`, ou `None` se `token` não citar símbolo."""
    if _e_caminho(token) or _e_flag(token):
        return None
    if token.endswith("(") and _RE_IDENTIFICADOR.match(token[:-1]):
        return token[:-1]
    if "_" in token and _RE_IDENTIFICADOR.match(token):
        return token
    return None


def _extrair(texto: str) -> tuple[list[str], list[str], list[str]]:
    """Tokeniza `texto` por espaço em branco e separa em três listas — caminhos, símbolos,
    flags —, cada uma na ordem da primeira aparição e sem repetir."""
    caminhos: list[str] = []
    simbolos: list[str] = []
    flags: list[str] = []
    for token in texto.split():
        if _e_caminho(token):
            if token not in caminhos:
                caminhos.append(token)
            continue
        if _e_flag(token):
            if token not in flags:
                flags.append(token)
            continue
        simbolo = _simbolo_de(token)
        if simbolo is not None and simbolo not in simbolos:
            simbolos.append(simbolo)
    return caminhos, simbolos, flags


def _achar_simbolo(root: Path, nome: str) -> str | None:
    """Procura `def <nome>(` ou `class <nome>` em todo `.py` sob `root` (fora de `.git` e
    `__pycache__`); devolve `<arquivo>:<linha>` (com `/`) da primeira ocorrência, ou `None`."""
    padrao_def = f"def {nome}("
    padrao_class = re.compile(rf"class {re.escape(nome)}\b")
    for arquivo in sorted(root.rglob("*.py")):
        partes = arquivo.relative_to(root).parts
        if ".git" in partes or "__pycache__" in partes:
            continue
        try:
            linhas = arquivo.read_text(e
```
[truncado em 4000 caracteres]

### `tests/test_prevoo.py`
```
"""AF-T17 (`docs/plans/P-0753-auditoria-estagio-1/plano.md` `### AF-T17`) — TF/TR de
`.claude/tools/prevoo.py`: o pré-voo do pedido confere caminho, símbolo e flag citados no texto
do dono contra a árvore. Padrão de carga do módulo idêntico a `tests/test_card_check.py` (`.claude/`
não é pacote importável)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_PREVOO_PATH = _ROOT / ".claude" / "tools" / "prevoo.py"


def _load_prevoo():
    spec = importlib.util.spec_from_file_location("prevoo", _PREVOO_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def test_tf_prevoo_simbolo_ausente_diz_nao(tmp_path, capsys):
    """`ler_texto_utf8` não está definido em nenhum `.py` da árvore — só mencionado num `.md`
    (a regra concorrente, "existe se aparece em qualquer lugar", aceitaria essa menção; a correta
    só aceita `def <nome>(`/`class <nome>` num `.py`), então o pré-voo tem de dizer `não`."""
    tools = tmp_path / ".claude" / "tools"
    tools.mkdir(parents=True)
    (tools / "caminhos.py").write_text("def outra_funcao():\n    pass\n", encoding="utf-8")
    (tmp_path / "nota.md").write_text("ler_texto_utf8 é citado aqui, mas não definido.\n", encoding="utf-8")

    prevoo = _load_prevoo()
    codigo = prevoo.main([
        "reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py",
        "--root",
        str(tmp_path),
    ])
    saida = capsys.readouterr()

    assert codigo == 1
    assert saida.out.splitlines() == [
        "citado | existe | onde",
        ".claude/tools/caminhos.py | sim | .claude/tools/caminhos.py",
        "ler_texto_utf8 | não | —",
    ]


def test_tr_prevoo_simbolo_definido_diz_onde(tmp_path, capsys):
    """Com a função `ler_texto_utf8` definida na linha 3 do mesmo arquivo, o pré-voo acha o
    símbolo e devolve `<arquivo>:<linha>` — tranca contra a regressão de voltar a aceitar só a
    menção no `.md`. (A definição é montada por `.format` — não escrita como literal `def
    ler_texto_utf8(` neste arquivo de teste — para não virar, ela mesma, um achado de `prevoo.py`
    ao rodar `python .claude/tools/prevoo.py` de verdade contra este repositório.)"""
    nome = "ler_texto_utf8"
    tools = tmp_path / ".claude" / "tools"
    tools.mkdir(parents=True)
    (tools / "caminhos.py").write_text(
        '"""Modulo de exemplo."""\n# comentario\n{marcador} {nome}(caminho):\n    return caminho.read_text(encoding="utf-8")\n'.format(
            marcador="def", nome=nome
        ),
        encoding="utf-8",
    )
    (tmp_path / "nota.md").write_text(f"{nome} é citado aqui, mas não definido.\n", encoding="utf-8")

    prevoo = _load_prevoo()
    codigo = prevoo.main([
        "reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py",
        "--root",
        str(tmp_path),
    ])
    saida = capsys.readouterr()

    assert codigo == 0
    assert saida.out.splitlines() == [
        "citado | existe | onde",
        ".claude/tools/caminhos.py | sim | .claude/tools/caminhos.py",
        "ler_texto_utf8 | sim | .claude/tools/caminhos.py:3",
    ]


def test_tf_prevoo_flag_existente(tmp_path, capsys):
    """`--desde` citado no texto e presente entre aspas num `.py` sob `.claude` — o pré-voo acha
    a flag e devolve `<arquivo>:<linha>`."""
    tools = tmp_path / ".claude" / "tools"
    tools.mkdir(parents=True)
    (tools / "x.py").write_text('parser.add_argument("--desde")\n', encoding="utf-8")

    prevoo = _load_prevoo()
    codigo = prevoo.main(["rode com --desde", "--root", str(tmp_path)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert saida.out.splitlines() == [
        "citado | existe | onde",
        "--desde | sim | .claude/tools/x.py:1",
    ]

```

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index 4d328d7..acdeca0 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -76,9 +76,17 @@ Uma sessão de planejamento termina de **quatro** formas, e só quatro: campanha
 registrado (fase 5). **Nunca** termina com
 plano escrito e pergunta pendurada — plano com questão aberta é plano que não existe.
 
-### Fase 0 — Intake (sem ferramenta, 1 turno)
+### Fase 0 — Intake (uma ferramenta, o pré-voo; 1 turno)
 
 1. Transcreva o pedido do dono **verbatim** — ele abre o plano (`## 0. O problema, verbatim`).
+
+   **Pré-voo do pedido.** A `## 0` recebe a tabela `citado | existe | onde` que
+   `python .claude/tools/prevoo.py "<pedido>"` imprime para todo caminho, símbolo e flag do texto
+   do dono, colada por quem conduz a sessão; sem ela, rode o instrumento como primeiro ato e cole a
+   tabela. Linha com `não` volta ao dono antes da campanha, pela SAÍDA 2, com o citado e o `onde`
+   vazio: premissa do pedido que não existe na árvore não vira pergunta ao scout (caso medido,
+   2026-09-27: um nome de função citado no pedido e ausente da árvore custou uma instância inteira
+   do planejador, 41,4k tokens).
 2. Classifique: **artefato inicial** (PRD → Architecture → Spec → Sprint Plan, `GOVERNANCA.md`
    §6), **plano novo**, ou **rodada de replanejamento** (escalada `premissa`, ver abaixo).
 3. Confira se o alvo já tem plano vivo: `Grep` pelo slug/iniciativa em `docs/plans/_INBOX.md` e

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T17-medida.json; mundo: depois; gerado em: 2026-09-27T16:39:26+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/prevoo.py "reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py"` | 1 | true |
| 2 | `python -m pytest tests/test_prevoo.py -q` | 0 | true |
| 3 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('sem ferramenta, 1 turno'),t.count('prevoo.py'))"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
