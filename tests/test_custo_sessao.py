"""RAF-T2 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T2`) — TF/TR de
`.claude/tools/custo_sessao.py`: o medidor de custo da sessão, que lê uma conversa gravada e
reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_ocupacao.py` e
`tests/test_telemetria.py`.

Todo transcript sintético desta suíte é escrito em `tmp_path`: uma linha `user`, os turnos
`assistant` do teste e uma linha que não é JSON (prova de que `medir` pula linha ilegível sem
quebrar)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_CUSTO_SESSAO_PATH = _ROOT / ".claude" / "tools" / "custo_sessao.py"


def _load_custo_sessao():
    spec = importlib.util.spec_from_file_location("custo_sessao", _CUSTO_SESSAO_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _linha_user() -> str:
    return json.dumps({"type": "user", "message": {"content": []}})


def _linha_assistant(ts: str, mid: str, usage: dict, content: list) -> str:
    return json.dumps(
        {
            "type": "assistant",
            "timestamp": ts,
            "message": {"id": mid, "usage": usage, "content": content},
        }
    )


def _escreve_transcript(tmp_path: Path, turnos_assistant: list[str]) -> Path:
    caminho = tmp_path / "transcript.jsonl"
    linhas = [_linha_user(), *turnos_assistant, "isto não é json {{{"]
    caminho.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    return caminho


def test_tf_medir_grava_uma_linha_por_turno_com_contexto_reenviado(tmp_path, capsys):
    """TF: uma linha do TSV por turno `assistant` com `usage` não vazio; o contexto reenviado é a
    soma dos três campos (a regra concorrente que somasse só `cache_read_input_tokens` daria
    1000 no primeiro turno, não 1210)."""
    custo_sessao = _load_custo_sessao()
    t1 = _linha_assistant(
        "t1",
        "m1",
        {
            "input_tokens": 10,
            "cache_read_input_tokens": 1000,
            "cache_creation_input_tokens": 200,
            "output_tokens": 30,
        },
        [{"type": "tool_use", "name": "Bash", "input": {"command": "python .claude/tools/backlog.py next"}}],
    )
    t2 = _linha_assistant(
        "t2",
        "m2",
        {
            "input_tokens": 5,
            "cache_read_input_tokens": 2000,
            "cache_creation_input_tokens": 0,
            "output_tokens": 40,
        },
        [{"type": "text", "text": "algo"}],
    )
    transcript = _escreve_transcript(tmp_path, [t1, t2])
    saida = tmp_path / "medido.tsv"

    codigo = custo_sessao.main(["medir", str(transcript), str(saida)])

    assert codigo == 0
    assert capsys.readouterr().out.strip() == "2 linhas"
    linhas = saida.read_text(encoding="utf-8").splitlines()
    assert linhas == [
        "t1\tm1\t1210\t30\tBash:python .claude/tools/backlog.py next",
        "t2\tm2\t2005\t40\tTEXT",
    ]


def test_tf_passos_reparte_por_passo_e_por_tarefa_de_qualquer_plano(tmp_path, capsys):
    """TF: os turnos se repartem por passo do loop (`classificar_passo`) e por tarefa despachada
    de QUALQUER plano ou tíquete — inclusive `TK-12`, que o rascunho preso a `AUF-T` não conta."""
    custo_sessao = _load_custo_sessao()
    turnos = [
        _linha_assistant(
            "t1",
            "m1",
            {"input_tokens": 1000, "output_tokens": 0},
            [{"type": "tool_use", "name": "Bash", "input": {"command": "despachar RAF-T3"}}],
        ),
        _linha_assistant(
            "t2",
            "m2",
            {"input_tokens": 2000, "output_tokens": 0},
            [{"type": "tool_use", "name": "Agent", "input": {"subagent_type": "pantonic-executor", "description": "RAF-T3"}}],
        ),
        _linha_assistant(
            "t3",
            "m3",
            {"input_tokens": 3000, "output_tokens": 0},
            [{"type": "tool_use", "name": "Bash", "input": {"command": "despachar TK-12"}}],
        ),
        _linha_assistant(
            "t4",
            "m4",
            {"input_tokens": 4000, "output_tokens": 0},
            [{"type": "tool_use", "name": "Agent", "input": {"subagent_type": "pantonic-reviewer", "description": "TK-12"}}],
        ),
    ]
    transcript = _escreve_transcript(tmp_path, turnos)
    tsv = tmp_path / "medido.tsv"
    assert custo_sessao.main(["medir", str(transcript), str(tsv)]) == 0
    capsys.readouterr()

    codigo = custo_sessao.main(["passos", str(tsv), "despachar", "pantonic-reviewer"])

    assert codigo == 0
    saida = capsys.readouterr().out.splitlines()
    assert saida == [
        "janela: t1 -> t4 turnos 4 ctx_k 10.0 out_k 0.0",
        "P3 turnos=2 ctx_k=4.0 out_k=0.0",
        "P4 turnos=1 ctx_k=2.0 out_k=0.0",
        "P6 turnos=1 ctx_k=4.0 out_k=0.0",
        "por tarefa: n=2 turnos medio=2.0 ctx_k medio=5.0 min_turnos=2 max_turnos=2",
        "RAF-T3 turnos=2 ctx_k=3.0 out_k=0.0",
        "TK-12 turnos=2 ctx_k=7.0 out_k=0.0",
    ]


def test_tr_passos_sem_despacho_informa_zero_e_sai_0(tmp_path, capsys):
    """TR: janela sem `despachar` informa `por tarefa: n=0` e sai 0 (o rascunho `passos.py` sai 1
    com `ZeroDivisionError`); regex de início que nada casa devolve `janela: vazia` exatamente,
    também exit 0."""
    custo_sessao = _load_custo_sessao()
    turnos = [
        _linha_assistant(
            "t1",
            "m1",
            {"input_tokens": 1000, "output_tokens": 0},
            [{"type": "tool_use", "name": "Agent", "input": {"subagent_type": "pantonic-executor", "description": "x"}}],
        ),
        _linha_assistant(
            "t2",
            "m2",
            {"input_tokens": 2000, "output_tokens": 0},
            [{"type": "tool_use", "name": "Agent", "input": {"subagent_type": "pantonic-reviewer", "description": "y"}}],
        ),
    ]
    transcript = _escreve_transcript(tmp_path, turnos)
    tsv = tmp_path / "medido.tsv"
    assert custo_sessao.main(["medir", str(transcript), str(tsv)]) == 0
    capsys.readouterr()

    codigo = custo_sessao.main(["passos", str(tsv), "pantonic-executor", "pantonic-reviewer"])

    assert codigo == 0
    saida = capsys.readouterr().out.splitlines()
    assert saida[-1] == "por tarefa: n=0"

    codigo2 = custo_sessao.main(["passos", str(tsv), "nada-casa-isto-aqui", "pantonic-reviewer"])

    assert codigo2 == 0
    assert capsys.readouterr().out.splitlines() == ["janela: vazia", "por tarefa: n=0"]


def test_tr_medir_e_passos_recusam_com_mensagem(tmp_path, capsys):
    """TR: `medir` com transcript inexistente sai 1 com a recusa no stderr; `passos` com regex que
    não compila sai 1 com a recusa no stderr (a regra concorrente sem recusa sairia com a exceção
    crua do `re`)."""
    custo_sessao = _load_custo_sessao()
    transcript_inexistente = tmp_path / "nao-existe.jsonl"
    saida = tmp_path / "medido.tsv"

    codigo = custo_sessao.main(["medir", str(transcript_inexistente), str(saida)])

    assert codigo == 1
    assert not saida.exists()
    err = capsys.readouterr().err
    assert "custo_sessao: FALHOU - transcript não encontrado" in err

    tsv = tmp_path / "vazio.tsv"
    tsv.write_text("", encoding="utf-8")

    codigo2 = custo_sessao.main(["passos", str(tsv), "(", "pantonic-reviewer"])

    assert codigo2 == 1
    err2 = capsys.readouterr().err
    assert "custo_sessao: FALHOU - regex inválida '('" in err2
