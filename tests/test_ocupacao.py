"""EXA-T13 (`docs/plans/P-0734-execucao-autonoma.md` `### T13`) — TF/TR de
`.claude/tools/ocupacao.py`: `calcular_ocupacao` (numerador, com ramo de fallback estimado) e
`avaliar` (fração e cruzamento do limiar de 50%, `GOVERNANCA.md` §4.3). Por desenho da tarefa, o
hook (`main`, I/O de stdin/transcript) não é exercitado aqui — só as duas funções puras.

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_rdo.py` e
`tests/test_telemetria.py`.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_OCUPACAO_PATH = _ROOT / ".claude" / "tools" / "ocupacao.py"


def _load_ocupacao():
    spec = importlib.util.spec_from_file_location("ocupacao", _OCUPACAO_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _linha_assistant(usage: dict | None) -> str:
    entrada = {"type": "assistant", "message": {"usage": usage} if usage is not None else {}}
    return json.dumps(entrada)


def test_tf_calcular_ocupacao_soma_os_tres_campos_da_ultima_entrada_com_usage():
    """TF: numerador = input_tokens + cache_read_input_tokens + cache_creation_input_tokens da
    última entrada assistant com bloco usage não vazio."""
    ocupacao = _load_ocupacao()
    linhas = [
        _linha_assistant(
            {"input_tokens": 100, "cache_read_input_tokens": 10, "cache_creation_input_tokens": 5}
        ),
        _linha_assistant(
            {"input_tokens": 200, "cache_read_input_tokens": 20, "cache_creation_input_tokens": 8}
        ),
    ]

    tokens, fonte = ocupacao.calcular_ocupacao(linhas)

    assert tokens == 228
    assert fonte == "usage"


def test_tr_calcular_ocupacao_usa_a_ultima_entrada_nao_a_primeira():
    """TR: com múltiplas entradas de usage, o numerador vem da ÚLTIMA, não da primeira nem de
    soma acumulada — tranca a semântica de 'ocupação atual', não 'consumo total da sessão'."""
    ocupacao = _load_ocupacao()
    linhas = [
        _linha_assistant(
            {"input_tokens": 900, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}
        ),
        _linha_assistant(
            {"input_tokens": 1, "cache_read_input_tokens": 1, "cache_creation_input_tokens": 1}
        ),
    ]

    tokens, fonte = ocupacao.calcular_ocupacao(linhas)

    assert tokens == 3
    assert fonte == "usage"


def test_tf_calcular_ocupacao_fallback_estimado_sem_nenhum_usage():
    """TF: nenhuma entrada com bloco usage ⇒ estimativa por soma(len(linha)) // 4, fonte
    'estimado' — ramo de fallback medido pela tarefa."""
    ocupacao = _load_ocupacao()
    linhas = ["a" * 40, "b" * 60]

    tokens, fonte = ocupacao.calcular_ocupacao(linhas)

    assert tokens == 100 // 4
    assert fonte == "estimado"


def test_tr_calcular_ocupacao_ignora_entrada_com_type_diferente_de_assistant():
    """TR: uma entrada 'user' com bloco parecido a usage não conta — só type=='assistant' é
    elegível como fonte do numerador; sem candidato, cai no fallback estimado."""
    ocupacao = _load_ocupacao()
    linhas = [json.dumps({"type": "user", "message": {"usage": {"input_tokens": 999}}})]

    tokens, fonte = ocupacao.calcular_ocupacao(linhas)

    assert fonte == "estimado"
    assert tokens != 999


def test_tr_calcular_ocupacao_ignora_linha_json_malformada_e_usa_a_seguinte_valida():
    """TR: uma linha corrompida no meio do transcript não derruba o cálculo — é ignorada, e a
    entrada válida seguinte ainda é considerada (falha aberta na leitura linha a linha)."""
    ocupacao = _load_ocupacao()
    linhas = [
        "{isso nao eh json",
        _linha_assistant(
            {"input_tokens": 50, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}
        ),
    ]

    tokens, fonte = ocupacao.calcular_ocupacao(linhas)

    assert tokens == 50
    assert fonte == "usage"


def test_tf_avaliar_fracao_e_cruzamento_do_limiar_de_50_por_cento():
    """TF: fração = tokens/janela; cruzou = fração >= 0.50 — o limiar já doutrinado em
    GOVERNANCA.md §4.3, não um número novo (DP-Q)."""
    ocupacao = _load_ocupacao()

    fracao, cruzou = ocupacao.avaliar(100_000, 200_000)

    assert fracao == 0.5
    assert cruzou is True


def test_tr_avaliar_nao_cruza_abaixo_do_limiar():
    """TR: um token abaixo do limiar não cruza — a comparação é >=, não >."""
    ocupacao = _load_ocupacao()

    fracao, cruzou = ocupacao.avaliar(99_999, 200_000)

    assert fracao < 0.5
    assert cruzou is False


def test_tr_avaliar_janela_zero_nao_cruza_e_nao_lanca_zerodivisionerror():
    """TR: janela<=0 é caso degenerado absorvido (fração 0.0, não cruza) em vez de propagar
    ZeroDivisionError — coerente com a postura de falha aberta do hook que chama esta função."""
    ocupacao = _load_ocupacao()

    fracao, cruzou = ocupacao.avaliar(500, 0)

    assert fracao == 0.0
    assert cruzou is False


def test_tr_janela_tokens_default_e_sobrescrita_por_variavel_de_ambiente(monkeypatch):
    """TR: JANELA_TOKENS nasce 1000000 por default — a janela real do Claude Opus 5, corrigida em
    2026-09-18 (o default anterior, 200000, errava por 5x e fazia o aviso disparar a ~10% da janela
    real). PANTONIC_CONTEXT_TOKENS_MAX é o nome canônico da sobrescrita; PANTONIC_JANELA_TOKENS
    segue honrado como nome legado."""
    ocupacao_default = _load_ocupacao()
    assert ocupacao_default.JANELA_TOKENS == 1_000_000

    monkeypatch.setenv("PANTONIC_CONTEXT_TOKENS_MAX", "50000")
    ocupacao_sobrescrito = _load_ocupacao()
    assert ocupacao_sobrescrito.JANELA_TOKENS == 50_000
    monkeypatch.delenv("PANTONIC_CONTEXT_TOKENS_MAX")

    monkeypatch.setenv("PANTONIC_JANELA_TOKENS", "50000")
    ocupacao_legado = _load_ocupacao()
    assert ocupacao_legado.JANELA_TOKENS == 50_000
    monkeypatch.delenv("PANTONIC_JANELA_TOKENS")


def test_tr_janela_tokens_aceita_sufixo_e_ignora_lixo(monkeypatch):
    """TR: o denominador aceita as formas que o dono escreve à mão ('1M', '200k') e nunca quebra o
    hook com valor inválido — lixo cai no default, porque o hook falha aberto."""
    for bruto, esperado in (("1M", 1_000_000), ("200k", 200_000), ("1000000", 1_000_000)):
        monkeypatch.setenv("PANTONIC_CONTEXT_TOKENS_MAX", bruto)
        assert _load_ocupacao().JANELA_TOKENS == esperado

    for lixo in ("lixo", "", "-5", "0"):
        monkeypatch.setenv("PANTONIC_CONTEXT_TOKENS_MAX", lixo)
        assert _load_ocupacao().JANELA_TOKENS == 1_000_000
