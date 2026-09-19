"""LM-T10 (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T10`) — TF/TR de
`.claude/tools/agentdef.py`: a aplicação mecânica de literais `--de`/`--para` declarados sobre um
arquivo de `.claude/agents/*.md`, verbo único `apply`. Cada teste opera sobre um
`.claude/agents/agente.md` fabricado sob `tmp_path`, com `monkeypatch.chdir` apontando para lá -
o alvo restrito do contrato é checado sobre o caminho relativo literal `.claude/agents/...`, igual
aos exemplos publicados na `Verificação` do card. Padrão de carga do módulo idêntico a
`tests/test_card_check.py` (`.claude/` não é pacote importável)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_AGENTDEF_PATH = _ROOT / ".claude" / "tools" / "agentdef.py"


def _load_agentdef():
    spec = importlib.util.spec_from_file_location("agentdef", _AGENTDEF_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _preparar_agente(tmp_path, monkeypatch, conteudo=None, *, conteudo_bytes=None):
    """Cria `.claude/agents/agente.md` sob `tmp_path` e faz o cwd apontar para `tmp_path` - o
    apply roda com `--arquivo .claude/agents/agente.md`, caminho relativo, igual ao uso real."""
    diretorio = tmp_path / ".claude" / "agents"
    diretorio.mkdir(parents=True)
    caminho = diretorio / "agente.md"
    if conteudo_bytes is not None:
        caminho.write_bytes(conteudo_bytes)
    else:
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            f.write(conteudo)
    monkeypatch.chdir(tmp_path)
    return caminho


def test_apply_aplica_par_unico(tmp_path, monkeypatch, capsys):
    """Par único, literal presente exatamente uma vez: `apply` substitui, sai 0 e o arquivo passa
    a conter o `para`, não mais o `de`."""
    agentdef = _load_agentdef()
    _preparar_agente(tmp_path, monkeypatch, "linha um\nnao mede nada\nlinha tres\n")

    codigo = agentdef.main(
        ["apply", "--arquivo", ".claude/agents/agente.md", "--de", "nao mede nada", "--para", "mede tudo"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert (tmp_path / ".claude" / "agents" / "agente.md").read_text(encoding="utf-8") == (
        "linha um\nmede tudo\nlinha tres\n"
    )
    assert "agentdef:" in saida.out


def test_apply_recusa_alvo_fora_de_agents(tmp_path, monkeypatch, capsys):
    """Dois casos: `README.md` (fora de `.claude/agents/`) e um caminho aninhado sob
    `.claude/agents/` (`.claude/agents/sub/x.md`) - o glob não recursivo recusa os dois, o que
    separa o glob não recursivo do recursivo."""
    agentdef = _load_agentdef()
    monkeypatch.chdir(tmp_path)

    codigo_readme = agentdef.main(["apply", "--arquivo", "README.md", "--de", "a", "--para", "b"])
    saida_readme = capsys.readouterr()

    codigo_aninhado = agentdef.main(
        ["apply", "--arquivo", ".claude/agents/sub/x.md", "--de", "a", "--para", "b"]
    )
    saida_aninhado = capsys.readouterr()

    assert codigo_readme == 1
    assert "agentdef: alvo fora de '.claude/agents/*.md'" in saida_readme.err
    assert codigo_aninhado == 1
    assert "agentdef: alvo fora de '.claude/agents/*.md'" in saida_aninhado.err


def test_apply_recusa_literal_ausente(tmp_path, monkeypatch, capsys):
    """`de` com zero ocorrências no conteúdo atual: exit 1, `literal nao encontrado`."""
    agentdef = _load_agentdef()
    _preparar_agente(tmp_path, monkeypatch, "conteudo sem o literal buscado\n")

    codigo = agentdef.main(
        ["apply", "--arquivo", ".claude/agents/agente.md", "--de", "inexistente", "--para", "x"]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "agentdef: literal nao encontrado" in saida.err


def test_apply_recusa_literal_nao_unico(tmp_path, monkeypatch, capsys):
    """`de` com mais de uma ocorrência no conteúdo atual: exit 1, `literal nao e unico`."""
    agentdef = _load_agentdef()
    _preparar_agente(tmp_path, monkeypatch, "duplicado aqui\nduplicado aqui de novo\n")

    codigo = agentdef.main(
        ["apply", "--arquivo", ".claude/agents/agente.md", "--de", "duplicado aqui", "--para", "x"]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "agentdef: literal nao e unico" in saida.err


def test_apply_nao_escreve_quando_um_par_falha(tmp_path, monkeypatch, capsys):
    """Dois pares no mesmo `apply`: o primeiro validaria sozinho, o segundo não (literal
    ausente) - a implementação certa valida os dois antes de escrever qualquer byte; uma que
    aplicasse par a par enquanto valida passaria nos outros testes e falharia neste. Compara os
    bytes do arquivo antes e depois."""
    agentdef = _load_agentdef()
    caminho = _preparar_agente(tmp_path, monkeypatch, "primeiro literal\nsegundo nao existe aqui\n")
    bytes_antes = caminho.read_bytes()

    codigo = agentdef.main(
        [
            "apply",
            "--arquivo",
            ".claude/agents/agente.md",
            "--de",
            "primeiro literal",
            "--para",
            "x",
            "--de",
            "literal que nao existe",
            "--para",
            "y",
        ]
    )
    saida = capsys.readouterr()
    bytes_depois = caminho.read_bytes()

    assert codigo == 1
    assert "agentdef: literal nao encontrado" in saida.err
    assert bytes_depois == bytes_antes


def test_apply_preserva_crlf(tmp_path, monkeypatch, capsys):
    """Fixture gravada com CRLF; leitura em modo texto padrão converteria para LF e o teste
    cairia - o contrato exige `newline=''` na leitura e na escrita (item 5)."""
    agentdef = _load_agentdef()
    caminho = _preparar_agente(
        tmp_path,
        monkeypatch,
        conteudo_bytes=b"linha um\r\nnao mede nada\r\nlinha tres\r\n",
    )

    codigo = agentdef.main(
        ["apply", "--arquivo", ".claude/agents/agente.md", "--de", "nao mede nada", "--para", "mede tudo"]
    )
    capsys.readouterr()
    bytes_depois = caminho.read_bytes()

    assert codigo == 0
    assert bytes_depois == b"linha um\r\nmede tudo\r\nlinha tres\r\n"
