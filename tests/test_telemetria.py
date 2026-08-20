"""T7 (`docs/plans/P-0734-execucao-autonoma.md` `### T7`) — TF/TR de
`.claude/tools/telemetria.py`, o script que substitui a edição manual de
`docs/telemetria.tsv`.

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado
por caminho via `importlib.util.spec_from_file_location`, mesmo padrão de
`tests/test_dead_code.py` para `.claude/checks/dead_code.py`.

Todas as asserções trabalham sobre `tmp_path` — nunca sobre `docs/telemetria.tsv` real (a série
histórica é insumo do produto, nunca alvo de escrita por este teste; ver "Cuidado" do dossiê
T7)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_TELEMETRIA_PATH = _ROOT / ".claude" / "tools" / "telemetria.py"

_HEADER = "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"
_LINHA_EXISTENTE = "2026-08-01\tPantonicApp\tV2B-T1\tSonnet\t13\t44\t100\tusage\n"


def _load_telemetria():
    spec = importlib.util.spec_from_file_location("telemetria", _TELEMETRIA_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _args(tsv_path, **overrides):
    valores = {
        "data": "2026-08-08",
        "projeto": "PantonicApp",
        "tarefa": "EXA-T7",
        "modelo": "Sonnet",
        "tool_uses": "20",
        "tokens_k": "50",
        "duracao_s": "120",
        "fonte": "usage",
    }
    valores.update(overrides)
    argv = ["append"]
    for chave, valor in valores.items():
        argv += [f"--{chave}", valor]
    argv += ["--file", str(tsv_path)]
    return argv


def test_tf_append_linha_valida_grava_e_preserva_conteudo_anterior(tmp_path):
    """TF da EXA-T7: uma chamada `append` com todas as colunas válidas devolve exit 0, a linha
    nova aparece ao final no formato TSV esperado, e o conteúdo anterior (header + linha
    existente) fica byte a byte intacto — cobre "linha válida" e "preservação byte a byte" do
    dossiê na mesma verificação."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(_args(tsv))

    assert exit_code == 0
    conteudo_final = tsv.read_bytes()
    assert conteudo_final.startswith(conteudo_anterior)
    nova_linha = conteudo_final[len(conteudo_anterior):]
    assert nova_linha == b"2026-08-08\tPantonicApp\tEXA-T7\tSonnet\t20\t50\t120\tusage\n"


def test_tr_fonte_invalida_falha_ruidosa_sem_escrever(tmp_path, capsys):
    """TR: `fonte` fora do conjunto normativo (`usage`/`contado`/`nao_medido`) devolve exit != 0,
    imprime o motivo em stderr e não escreve nada — trava contra o caso que a edição manual
    admitia em silêncio."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(_args(tsv, fonte="chutada"))

    assert exit_code != 0
    assert tsv.read_bytes() == conteudo_anterior
    saida = capsys.readouterr()
    assert "fonte" in saida.err


def test_tr_campo_numerico_nao_numerico_falha_ruidosa_sem_escrever(tmp_path, capsys):
    """TR: `tool_uses` não numérico devolve exit != 0, imprime o motivo em stderr e não escreve
    nada — mesma trava para os outros dois campos numéricos (`tokens_k`/`duracao_s`), validados
    pela mesma função em `telemetria.py`."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(_args(tsv, tool_uses="vinte"))

    assert exit_code != 0
    assert tsv.read_bytes() == conteudo_anterior
    saida = capsys.readouterr()
    assert "tool_uses" in saida.err
