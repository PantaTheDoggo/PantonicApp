"""EXA-T55 (`docs/plans/P-0734-execucao-autonoma.md` `### T55`) — TF/TR de
`.claude/tools/telemetria_hook.py`: o hook `SubagentStop` que fecha o vão deixado pela `EXA-T14`
(Sonda 5, `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`) — a identidade da tarefa não
vem mais de inferência sobre prosa, e sim do estado que o `scrum-master` grava no despacho
(`.claude/skills/scrum-master/SKILL.md`, Passo 4).

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_ocupacao.py` e
`tests/test_materializar.py`.

Superfície testável, separada do I/O de stdin do hook (`main`, não exercitado aqui — mesmo desenho
de `ocupacao.py`): `calcular_consumo` (pura, soma de tokens/tool_uses/duração a partir das linhas
do `agent_transcript_path`) e `processar` (núcleo do hook, recebe payload e caminhos já resolvidos
em vez de ler stdin/`sys.argv` — mesmo padrão de `apply`/`check`/`drift` em `materializar.py`).
`processar` chama o CLI real de `telemetria.py` via subprocess (`--file` apontado para `tmp_path`),
nunca reimplementa a validação de coluna (Cuidado do dossiê `T55`)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_HOOK_PATH = _ROOT / ".claude" / "tools" / "telemetria_hook.py"
_TELEMETRIA_CLI_PATH = _ROOT / ".claude" / "tools" / "telemetria.py"

_HEADER = "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"


def _load_hook():
    spec = importlib.util.spec_from_file_location("telemetria_hook", _HOOK_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _linha_assistant(
    usage: dict | None, timestamp: str, n_tool_uses: int = 0, message_id: str | None = None
) -> str:
    conteudo = [{"type": "text", "text": "ok"}]
    for i in range(n_tool_uses):
        conteudo.append({"type": "tool_use", "name": f"Ferramenta{i}", "input": {}})
    mensagem = {"usage": usage or {}, "content": conteudo}
    if message_id is not None:
        mensagem["id"] = message_id
    return json.dumps({"type": "assistant", "timestamp": timestamp, "message": mensagem})


def _estado_valido(**overrides) -> dict:
    valores = {
        "tarefa": "EXA-T55",
        "projeto": "PantonicApp",
        "modelo": "Sonnet",
        "plano": "docs/plans/P-0734-execucao-autonoma.md",
        "despachado_em": "2026-08-19T10:00:00+00:00",
    }
    valores.update(overrides)
    return valores


def _payload(**overrides) -> dict:
    valores = {
        "agent_type": "pantonic-executor",
        "agent_transcript_path": None,
    }
    valores.update(overrides)
    return valores


def test_tf_calcular_consumo_soma_tokens_e_conta_tool_uses_de_n_entradas_assistant():
    """TF: `tokens_k` = `usage` (input+cache_creation+cache_read+output)/1000 da **última**
    entrada assistant (LM-T2b — contingência 2 acionada: esta asserção afirmava a soma por
    `message.id`/sem id, que era a fórmula antiga; ajustada para a fórmula nova, caso mantido);
    `tool_uses` = contagem de blocos `tool_use` de todas as entradas; `duracao_s` = diferença
    entre o primeiro e o último timestamp."""
    hook = _load_hook()
    linhas = [
        _linha_assistant(
            {
                "input_tokens": 100,
                "cache_creation_input_tokens": 10,
                "cache_read_input_tokens": 5,
                "output_tokens": 20,
            },
            "2026-08-19T10:00:00+00:00",
            n_tool_uses=2,
        ),
        _linha_assistant(
            {
                "input_tokens": 200,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
                "output_tokens": 50,
            },
            "2026-08-19T10:01:30+00:00",
            n_tool_uses=1,
        ),
    ]

    tokens_k, tool_uses, duracao_s = hook.calcular_consumo(linhas)

    assert tokens_k == 250 / 1000
    assert tool_uses == 3
    assert duracao_s == 90.0


def test_tr_calcular_consumo_sem_entradas_assistant_e_zero_em_tudo():
    """TR: transcript sem nenhuma entrada assistant não lança exceção — devolve zeros."""
    hook = _load_hook()

    tokens_k, tool_uses, duracao_s = hook.calcular_consumo(
        [json.dumps({"type": "user", "timestamp": "2026-08-19T10:00:00+00:00"})]
    )

    assert tokens_k == 0.0
    assert tool_uses == 0
    assert duracao_s == 0.0


def _linhas_tres_mensagens_usage_crescente() -> list[str]:
    """Transcript sintético com três entradas `assistant` de `message.id` distintos e `usage`
    crescente (10k, 30k, 60k) — o transcript compartilhado pelos dois testes de LM-T2b que
    precisam do mesmo cenário."""
    return [
        _linha_assistant(
            {"input_tokens": 10000, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
            "2026-09-19T10:00:00+00:00",
            n_tool_uses=1,
            message_id="msg-1",
        ),
        _linha_assistant(
            {"input_tokens": 30000, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
            "2026-09-19T10:01:00+00:00",
            n_tool_uses=2,
            message_id="msg-2",
        ),
        _linha_assistant(
            {"input_tokens": 60000, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
            "2026-09-19T10:02:30+00:00",
            n_tool_uses=3,
            message_id="msg-3",
        ),
    ]


def test_tf_calcular_consumo_usa_a_ultima_mensagem_assistant():
    """TF (LM-T2b, calibração `ESC-3`): `tokens_k` é o `usage` da **última** entrada assistant
    com `usage`, não a soma das três. Concorrente: o código antigo (soma por `message.id`)
    devolvia 100.0 (10k+30k+60k)."""
    hook = _load_hook()

    tokens_k, _tool_uses, _duracao_s = hook.calcular_consumo(_linhas_tres_mensagens_usage_crescente())

    assert tokens_k == 60.0


def test_tr_calcular_consumo_mesma_mensagem_duas_entradas_nao_dobra():
    """TR (LM-T2b, o caso da calibração histórica do `T55`): duas entradas com o mesmo
    `message.id` e o mesmo `usage` — continua devolvendo o valor de uma, não o dobro.
    Concorrente: somar por entrada (o defeito que a dedupe por `message.id` corrigia) dobrava."""
    hook = _load_hook()
    usage = {
        "input_tokens": 10,
        "cache_creation_input_tokens": 8779,
        "cache_read_input_tokens": 0,
        "output_tokens": 74,
    }
    linhas = [
        _linha_assistant(usage, "2026-08-20T00:28:03.168Z", message_id="msg_calibracao"),
        _linha_assistant(usage, "2026-08-20T00:28:03.169Z", message_id="msg_calibracao"),
    ]

    tokens_k, tool_uses, _duracao_s = hook.calcular_consumo(linhas)

    assert tokens_k == 8863 / 1000
    assert tool_uses == 0


def test_tr_calcular_consumo_tool_uses_e_duracao_ficam_intocados():
    """TR (LM-T2b): no mesmo transcript de `test_tf_calcular_consumo_usa_a_ultima_mensagem_assistant`,
    `tool_uses` conta todos os blocos `tool_use` de todas as entradas (1+2+3=6) e `duracao_s`
    segue vindo do primeiro e do último timestamp (10:00:00 a 10:02:30 = 150s). Concorrente:
    aplicar "só a última mensagem" também a `tool_uses` derrubaria a contagem, que hoje está
    certa."""
    hook = _load_hook()

    _tokens_k, tool_uses, duracao_s = hook.calcular_consumo(_linhas_tres_mensagens_usage_crescente())

    assert tool_uses == 6
    assert duracao_s == 150.0


def test_tf_montar_args_append_normaliza_modelo_para_minusculo():
    """TF (LM-T2b, `AE-3`): `montar_args_append` normaliza `modelo` para minúsculas, evitando
    duas grafias do mesmo modelo na série. Concorrente: hoje devolve `Sonnet` sem normalizar."""
    hook = _load_hook()

    args = hook.montar_args_append(
        _estado_valido(modelo="Sonnet"), tokens_k=1.0, tool_uses=1, duracao_s=1.0, data="2026-09-19"
    )

    assert args[args.index("--modelo") + 1] == "sonnet"


def test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv(tmp_path):
    """TF: payload válido (agent_type de papel do kit + estado presente + transcript com
    usage) produz a linha esperada em `docs/telemetria.tsv` (via `--file` de teste) e consome
    (apaga) o estado.

    A grafia esperada do modelo é minúscula desde a `LM-T2b` (`AE-3`, `DM-33`): o payload
    entrega `Sonnet` e o hook normaliza — a asserção mede a normalização ponta a ponta, não a
    grafia de entrada."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")

    transcript_path = tmp_path / "agent-transcript.jsonl"
    transcript_path.write_text(
        "\n".join(
            [
                _linha_assistant(
                    {
                        "input_tokens": 1000,
                        "cache_creation_input_tokens": 0,
                        "cache_read_input_tokens": 0,
                        "output_tokens": 0,
                    },
                    "2026-08-19T10:00:00+00:00",
                    n_tool_uses=5,
                )
            ]
        ),
        encoding="utf-8",
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload,
        estado_path=estado_path,
        telemetria_cli=_TELEMETRIA_CLI_PATH,
        tsv_path=tsv_path,
        data="2026-08-19",
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[0] == _HEADER.rstrip("\n")
    assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage"
    assert not estado_path.exists()


def test_tr_processar_sem_estado_e_silencio_sem_escrita(tmp_path):
    """TR: ausência de `.claude/estado/tarefa-corrente.json` é o caso previsto de despacho fora
    do loop — o hook devolve False e não toca o TSV nem lança exceção."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado
    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_transcript_path=str(tmp_path / "nao-importa.jsonl"))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is False
    assert tsv_path.read_text(encoding="utf-8") == _HEADER


def test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado(tmp_path):
    """TR: `agent_type` que não é papel do kit (ex.: sessão principal do loop, sem agent_type,
    ou um subagente que não é `pantonic-*`) não escreve nem consome o estado — preserva o
    arquivo para o despacho real do executor consumir depois."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="context-scout", agent_transcript_path=str(tmp_path / "x.jsonl"))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is False
    assert tsv_path.read_text(encoding="utf-8") == _HEADER
    assert estado_path.exists()
