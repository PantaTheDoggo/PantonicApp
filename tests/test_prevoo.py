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


def test_tr_prevoo_citacao_em_crase_e_pontuada(tmp_path, capsys):
    """`DAF-45` (ressalva do laudo da `AF-T17`): o pedido real cita em crase e com pontuação de
    frase. Antes da normalização do token, este texto saía com a tabela vazia e exit 0 — o caso
    medido que motivou o card passava sem alarme. O ponto inicial de `.claude/` fica."""
    tools = tmp_path / ".claude" / "tools"
    tools.mkdir(parents=True)
    (tools / "caminhos.py").write_text("def outra_funcao():\n    pass\n", encoding="utf-8")
    (tools / "x.py").write_text('parser.add_argument("--desde")\n', encoding="utf-8")

    prevoo = _load_prevoo()
    codigo = prevoo.main([
        "use `ler_texto_utf8` de `.claude/tools/caminhos.py`, e rode com `--desde`.",
        "--root",
        str(tmp_path),
    ])
    saida = capsys.readouterr()

    assert codigo == 1
    assert saida.out.splitlines() == [
        "citado | existe | onde",
        ".claude/tools/caminhos.py | sim | .claude/tools/caminhos.py",
        "ler_texto_utf8 | não | —",
        "--desde | sim | .claude/tools/x.py:1",
    ]


def test_tr_prevoo_chamada_com_parenteses_fechados(tmp_path, capsys):
    """`DAF-45`: "nome seguido de `(`" vale com os parênteses fechados e com argumentos — antes,
    `funcao_inexistente()` e `outra_funcao(x).` não viravam item e o texto saía com exit 0."""
    tools = tmp_path / ".claude" / "tools"
    tools.mkdir(parents=True)
    (tools / "caminhos.py").write_text("def outra_funcao():\n    pass\n", encoding="utf-8")

    prevoo = _load_prevoo()
    codigo = prevoo.main([
        "chame funcao_inexistente() e outra_funcao(x).",
        "--root",
        str(tmp_path),
    ])
    saida = capsys.readouterr()

    assert codigo == 1
    assert saida.out.splitlines() == [
        "citado | existe | onde",
        "funcao_inexistente | não | —",
        "outra_funcao | sim | .claude/tools/caminhos.py:1",
    ]


def test_tr_prevoo_flag_com_pontuacao(tmp_path, capsys):
    """`DAF-45`: flag seguida de pontuação de frase é a mesma flag — antes, `--plano;` virava o
    citado `--plano;` com `não`."""
    tools = tmp_path / ".claude" / "tools"
    tools.mkdir(parents=True)
    (tools / "x.py").write_text('parser.add_argument("--plano")\n', encoding="utf-8")

    prevoo = _load_prevoo()
    codigo = prevoo.main(["com --plano;", "--root", str(tmp_path)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert saida.out.splitlines() == [
        "citado | existe | onde",
        "--plano | sim | .claude/tools/x.py:1",
    ]
