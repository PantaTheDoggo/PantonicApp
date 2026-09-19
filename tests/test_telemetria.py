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


def test_tf_celula_vazia_aceita_quando_fonte_nao_e_usage(tmp_path):
    """TF da AUT-T5a: com `fonte` em {`contado`, `nao_medido`}, `tokens_k`/`duracao_s`/`tool_uses`
    vazios são aceitos — a célula vazia é a sentinela de métrica não medida."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(
        _args(tsv, fonte="contado", tokens_k="", duracao_s="")
    )

    assert exit_code == 0
    conteudo_final = tsv.read_bytes()
    nova_linha = conteudo_final[len(conteudo_anterior):]
    assert nova_linha == b"2026-08-08\tPantonicApp\tEXA-T7\tSonnet\t20\t\t\tcontado\n"


def test_tf_celula_vazia_aceita_com_fonte_nao_medido(tmp_path):
    """TF da AUT-T5a: `fonte=nao_medido` também aceita célula vazia nas três colunas numéricas."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(
        _args(tsv, fonte="nao_medido", tool_uses="", tokens_k="", duracao_s="")
    )

    assert exit_code == 0
    conteudo_final = tsv.read_bytes()
    nova_linha = conteudo_final[len(conteudo_anterior):]
    assert nova_linha == b"2026-08-08\tPantonicApp\tEXA-T7\tSonnet\t\t\t\tnao_medido\n"


def test_tf_append_tokens_k_decimal_grava_sem_conversao(tmp_path):
    """TF (`P-0740` `LM-T1`, `DM-11`): `--tokens_k` aceita o literal decimal de uma casa (ex.:
    `203.7`, a forma que o hook `SubagentStop` produz) e a linha apensada traz o mesmo literal na
    coluna `tokens_k`, sem conversão."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(_args(tsv, tokens_k="203.7"))

    assert exit_code == 0
    conteudo_final = tsv.read_bytes()
    nova_linha = conteudo_final[len(conteudo_anterior):]
    assert nova_linha == b"2026-08-08\tPantonicApp\tEXA-T7\tSonnet\t20\t203.7\t120\tusage\n"


def test_tf_append_tokens_k_nao_finito_recusa_sem_escrever(tmp_path, capsys):
    """TF (`P-0740` `LM-T1a`, `DM-15`): `--tokens_k nan` sai exit != 0 com
    `tokens_k: 'nan' não é finito` e o TSV de destino não chega a ser criado — a regra
    concorrente (medida na `RP-5`) saía exit 0 e gravava a linha com o literal `nan` na coluna de
    tokens."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"

    exit_code = telemetria.main(_args(tsv, tokens_k="nan"))

    assert exit_code != 0
    assert not tsv.exists()
    saida = capsys.readouterr()
    assert "telemetria: FALHOU - tokens_k: 'nan' não é finito" in saida.err


def test_tf_append_duracao_s_nao_finito_recusa(tmp_path, capsys):
    """TF (`DM-15`): `--duracao_s inf` sai exit != 0 com `duracao_s: 'inf' não é finito` — a
    regra concorrente saía exit 0 e gravava `inf`. `tokens_k` e `duracao_s` passam pelo mesmo
    validador (`_validar_numero_nao_negativo`); este teste tranca o segundo termo, o anterior
    tranca o primeiro."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(_args(tsv, duracao_s="inf"))

    assert exit_code != 0
    assert tsv.read_bytes() == conteudo_anterior
    saida = capsys.readouterr()
    assert "telemetria: FALHOU - duracao_s: 'inf' não é finito" in saida.err


def test_tr_celula_vazia_recusada_com_fonte_usage(tmp_path, capsys):
    """TR da AUT-T5a: com `fonte=usage` a célula vazia continua sendo falha ruidosa — o bloco de
    uso reportado sempre carrega os três campos, e vazio ali é medida perdida, não ausente."""
    telemetria = _load_telemetria()
    tsv = tmp_path / "telemetria.tsv"
    conteudo_anterior = (_HEADER + _LINHA_EXISTENTE).encode("utf-8")
    tsv.write_bytes(conteudo_anterior)

    exit_code = telemetria.main(_args(tsv, fonte="usage", tokens_k=""))

    assert exit_code != 0
    assert tsv.read_bytes() == conteudo_anterior
    saida = capsys.readouterr()
    assert "tokens_k" in saida.err
