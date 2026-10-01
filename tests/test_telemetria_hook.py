"""EXA-T55 (`docs/plans/P-0734-execucao-autonoma.md` `### T55`) — TF/TR de
`.claude/tools/telemetria_hook.py`: o hook `SubagentStop` que fecha o vão deixado pela `EXA-T14`
(Sonda 5, `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`) — a identidade da tarefa não
vem mais de inferência sobre prosa, e sim do estado que o `scrum-master` grava no despacho
(`.claude/skills/scrum-master/SKILL.md`, Passo 4).

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_ocupacao.py` e
`tests/test_materializar.py`.

Superfície testável, separada do I/O de stdin do hook: `calcular_consumo` (pura, soma de
tokens/tool_uses/duração a partir das linhas do `agent_transcript_path`) e `processar` (núcleo do
hook, recebe payload e caminhos já resolvidos em vez de ler stdin/`sys.argv` — mesmo padrão de
`apply`/`check`/`drift` em `materializar.py`). `processar` chama o CLI real de `telemetria.py` via
subprocess (`--file` apontado para `tmp_path`), nunca reimplementa a validação de coluna (Cuidado
do dossiê `T55`). `main` ganhou cobertura por subprocesso na `TK-56a` (`DB-53`) — leitura de stdin
em UTF-8 explícito — restrita ao ramo `agent_type` fora do filtro do kit, o único seguro para
rodar contra os caminhos de produção reais que `main` resolve sozinho (`_estado_path_default`/
`_telemetria_cli_default`, sem injeção possível pela CLI)."""
from __future__ import annotations

import datetime
import importlib.util
import json
import os
import subprocess
import sys
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
    usage: dict | None,
    timestamp: str,
    n_tool_uses: int = 0,
    message_id: str | None = None,
    model: str | None = None,
) -> str:
    conteudo = [{"type": "text", "text": "ok"}]
    for i in range(n_tool_uses):
        conteudo.append({"type": "tool_use", "name": f"Ferramenta{i}", "input": {}})
    mensagem = {"usage": usage or {}, "content": conteudo}
    if message_id is not None:
        mensagem["id"] = message_id
    if model is not None:
        mensagem["model"] = model
    return json.dumps({"type": "assistant", "timestamp": timestamp, "message": mensagem})


def _linha_user(texto: str, timestamp: str = "2026-09-26T09:00:00+00:00") -> str:
    return json.dumps({"type": "user", "timestamp": timestamp, "message": {"role": "user", "content": texto}})


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


def _montar_raiz_isolada(base: Path, nome: str, fonte_hook: str) -> tuple[Path, Path, Path, Path]:
    """Raiz falsa em `base/nome` para relocar `_repo_root()` do hook (derivada de `__file__`):
    hook copiado em `.claude/tools/telemetria_hook.py`, CLI real copiado em
    `.claude/tools/telemetria.py`, estado válido em `.claude/estado/tarefa-corrente.json` e
    `docs/` — nunca toca `.claude/estado/` nem `docs/telemetria.tsv` reais. Devolve
    `(hook_path, estado_path, tsv_path, transcript_path)`; o transcript tem nome acentuado e é
    o canal por onde o payload acentuado chega ao observável (efeito colateral, já que o hook
    é silencioso por contrato)."""
    raiz = base / nome
    tools_dir = raiz / ".claude" / "tools"
    tools_dir.mkdir(parents=True)
    hook_path = tools_dir / "telemetria_hook.py"
    hook_path.write_text(fonte_hook, encoding="utf-8")
    (tools_dir / "telemetria.py").write_text(
        _TELEMETRIA_CLI_PATH.read_text(encoding="utf-8"), encoding="utf-8"
    )
    estado_path = raiz / ".claude" / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")
    (raiz / "docs").mkdir(parents=True)
    transcript_path = raiz / "análise.jsonl"
    transcript_path.write_text("", encoding="utf-8")
    tsv_path = raiz / "docs" / "telemetria.tsv"
    return hook_path, estado_path, tsv_path, transcript_path


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
    assert linhas[0] == _HEADER.rstrip("\n") + "\tagente"
    assert linhas[1] == "2026-08-19\tPantonicApp\tEXA-T55\tsonnet\t5\t1.0\t0.0\tusage\tagent-transcript"
    assert estado_path.exists()


def test_tr_processar_sem_tsv_path_grava_na_serie_do_repo_do_estado(tmp_path):
    """TR (`AE-5` do `P-0753`): sem `tsv_path`, a linha vai para `docs/telemetria.tsv` do
    repositório do estado (`estado_path.parents[2]`) — a mesma série de onde a contagem do
    consultor já lê —, nunca para a série padrão do CLI. Exercitar o hook com estado de fixture
    não escreve na série real; antes, a linha caía em `docs/telemetria.tsv` do kit."""
    hook = _load_hook()
    real = _ROOT / "docs" / "telemetria.tsv"
    antes_real = real.read_bytes() if real.is_file() else None

    repo = tmp_path / "repo"
    estado_path = repo / ".claude" / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido(tarefa="AE5-TR-SONDA")), encoding="utf-8")
    serie = repo / "docs" / "telemetria.tsv"
    serie.parent.mkdir(parents=True)
    serie.write_text(_HEADER, encoding="utf-8")
    transcript_path = tmp_path / "agent-transcript.jsonl"
    transcript_path.write_text(
        _linha_assistant({"input_tokens": 1000}, "2026-08-19T10:00:00+00:00", n_tool_uses=2),
        encoding="utf-8",
    )

    escreveu = hook.processar(
        _payload(agent_transcript_path=str(transcript_path)),
        estado_path=estado_path,
        telemetria_cli=_TELEMETRIA_CLI_PATH,
        data="2026-08-19",
    )

    assert escreveu is True
    assert serie.read_text(encoding="utf-8").splitlines()[1] == (
        "2026-08-19\tPantonicApp\tAE5-TR-SONDA\tsonnet\t2\t1.0\t0.0\tusage\tagent-transcript"
    )
    assert (real.read_bytes() if real.is_file() else None) == antes_real


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


def test_tf_hook_grava_revisor_com_papel(tmp_path):
    """TF (`DAF-15`/`DAF-25`): `agent_type` `pantonic-reviewer` grava a própria rodada — tarefa
    `<tarefa>-revisao` (a do estado corrente) e modelo normalizado do `message.model` do
    transcript — e o estado permanece no disco (a regra de hoje não gravaria nada, porque
    filtrava todo papel que não fosse o executor)."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")

    transcript_path = tmp_path / "reviewer-transcript.jsonl"
    transcript_path.write_text(
        _linha_assistant(
            {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
            "2026-09-26T10:00:00+00:00",
            n_tool_uses=1,
            model="claude-opus-4",
        ),
        encoding="utf-8",
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="pantonic-reviewer", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    colunas = linhas[1].split("\t")
    assert colunas[2] == "EXA-T55-revisao"
    assert colunas[3] == "opus"
    assert estado_path.exists()


def test_tf_hook_grava_consultor_numerado_por_papel(tmp_path):
    """TF: `pantonic-consultant` numera pela série já existente — com uma linha
    `EXA-T55-consultor-1` presente, a nova rodada grava `EXA-T55-consultor-2`."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")

    transcript_path = tmp_path / "consultor-transcript.jsonl"
    transcript_path.write_text(
        _linha_assistant(
            {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
            "2026-09-26T10:00:00+00:00",
            n_tool_uses=1,
        ),
        encoding="utf-8",
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(
        _HEADER + "2026-09-25\tPantonicApp\tEXA-T55-consultor-1\tsonnet\t1\t1.0\t1.0\tusage\n",
        encoding="utf-8",
    )

    payload = _payload(agent_type="pantonic-consultant", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[-1].split("\t")[2] == "EXA-T55-consultor-2"


def test_tf_hook_grava_planejador_pelo_id_do_plano_papel(tmp_path):
    """TF: `pantonic-planner` deriva o id do plano da primeira mensagem de usuário do
    transcript — `P-0753` de `docs/plans/P-0753-auditoria-estagio-1/plano.md` — e grava
    `P-0753-planejador`, mesmo sem estado no disco."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado

    transcript_path = tmp_path / "planejador-transcript.jsonl"
    transcript_path.write_text(
        "\n".join(
            [
                _linha_user(
                    "Planeje a decomposição de docs/plans/P-0753-auditoria-estagio-1/plano.md agora."
                ),
                _linha_assistant(
                    {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
                    "2026-09-26T10:00:00+00:00",
                    n_tool_uses=1,
                ),
            ]
        ),
        encoding="utf-8",
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="pantonic-planner", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[1].split("\t")[2] == "P-0753-planejador"


def test_tr_hook_sem_id_derivavel_grava_sem_id_papel(tmp_path):
    """TR: `pantonic-scout` cuja primeira mensagem de usuário não cita `P-<n>` nenhum grava a
    linha sob `sem-id-scout`, em vez de ficar em silêncio."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado

    transcript_path = tmp_path / "scout-transcript.jsonl"
    transcript_path.write_text(
        "\n".join(
            [
                _linha_user("Faça uma varredura geral no repositório."),
                _linha_assistant(
                    {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0},
                    "2026-09-26T10:00:00+00:00",
                    n_tool_uses=1,
                ),
            ]
        ),
        encoding="utf-8",
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="pantonic-scout", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[1].split("\t")[2] == "sem-id-scout"


def test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia(tmp_path):
    """TK-56b: repara a ressalva da `TK-56a` — o par negativo deixa de ser um stub (que só
    discriminava a si mesmo) e passa a ser o produto revertido, extraído do arquivo real. Mundo
    hostil: `env` mínimo + `PYTHONIOENCODING=cp1252` (o host sem a variável mede o host, não o
    hostil). Mundo seguro: `env` mínimo + `PYTHONUTF8=1`. O hook é silencioso por contrato —
    `stdout` é `b""` e `rc=0` em todas as combinações — então o canal discriminante é o efeito
    colateral, observado numa raiz relocada para `tmp_path` (relocar é obrigatório: sem isso
    `main` gravaria na `docs/telemetria.tsv` real). O payload acentuado viaja no
    nome do transcript apontado por `agent_transcript_path`. Medido em 2026-09-20: reparado
    escreve a mesma linha TSV nos dois mundos; revertido, no mundo hostil, decodifica o caminho
    acentuado errado — o transcript não é encontrado e o TSV não é criado."""
    fonte = _HOOK_PATH.read_text(encoding="utf-8")
    bloco_reparo = (
        "        try:\n"
        "            raw = sys.stdin.buffer.read().decode(\"utf-8\", errors=\"replace\")\n"
        "        except AttributeError:\n"
        "            raw = sys.stdin.read()\n"
    )
    assert bloco_reparo in fonte
    fonte_revertida = fonte.replace(bloco_reparo, "        raw = sys.stdin.read()\n")

    env_hostil = {
        "SYSTEMROOT": os.environ["SYSTEMROOT"],
        "PATH": os.environ["PATH"],
        "PYTHONIOENCODING": "cp1252",
    }
    env_seguro = {
        "SYSTEMROOT": os.environ["SYSTEMROOT"],
        "PATH": os.environ["PATH"],
        "PYTHONUTF8": "1",
    }
    hoje = datetime.date.today().isoformat()
    linha_esperada = (
        _HEADER.rstrip("\n") + "\tagente\n"
        + f"{hoje}\tPantonicApp\tEXA-T55\tsonnet\t0\t0.0\t0.0\tusage\tanálise"
    )

    def _rodar(nome: str, fonte_hook: str, env: dict):
        hook_path, estado_path, tsv_path, transcript_path = _montar_raiz_isolada(
            tmp_path, nome, fonte_hook
        )
        payload = json.dumps(
            _payload(agent_transcript_path=str(transcript_path)), ensure_ascii=False,
        ).encode("utf-8")
        resultado = subprocess.run(
            [sys.executable, str(hook_path)], input=payload, capture_output=True, env=env,
        )
        tsv_conteudo = tsv_path.read_text(encoding="utf-8") if tsv_path.exists() else None
        return resultado, estado_path.exists(), tsv_conteudo

    reparado_hostil, estado_rh, tsv_rh = _rodar("reparado_hostil", fonte, env_hostil)
    reparado_seguro, estado_rs, tsv_rs = _rodar("reparado_seguro", fonte, env_seguro)
    revertido_hostil, estado_vh, tsv_vh = _rodar("revertido_hostil", fonte_revertida, env_hostil)
    revertido_seguro, estado_vs, tsv_vs = _rodar("revertido_seguro", fonte_revertida, env_seguro)

    for resultado in (reparado_hostil, reparado_seguro, revertido_hostil, revertido_seguro):
        assert resultado.returncode == 0
        assert resultado.stdout == b""

    # (i) produto reparado dá a mesma saída (efeito colateral) nos dois mundos
    assert estado_rh is True
    assert estado_rs is True
    assert tsv_rh is not None and tsv_rh.strip("\n") == linha_esperada
    assert tsv_rs is not None and tsv_rs.strip("\n") == linha_esperada

    # (iii) o valor acentuado chega íntegro ao observável no mundo hostil
    assert tsv_rh == tsv_rs

    # (ii) produto revertido dá saídas diferentes entre os dois mundos
    assert estado_vh is True
    assert tsv_vh is None
    assert estado_vs is True
    assert tsv_vs is not None and tsv_vs.strip("\n") == linha_esperada


def _transcript_com_mensagem(caminho: Path, primeira_mensagem: str, input_tokens: int = 10) -> Path:
    """Transcript sintético de duas linhas — a primeira mensagem de usuário (`primeira_mensagem`)
    e uma resposta `assistant` mínima — para os testes de `_linha_de_despacho` e de atribuição
    por agente (`R-16`, `DRF-18` do `P-0755`, `RAF-T31`)."""
    caminho.write_text(
        "\n".join(
            [
                _linha_user(primeira_mensagem),
                _linha_assistant(
                    {
                        "input_tokens": input_tokens,
                        "cache_creation_input_tokens": 0,
                        "cache_read_input_tokens": 0,
                        "output_tokens": 0,
                    },
                    "2026-09-26T10:00:00+00:00",
                    n_tool_uses=1,
                    model="claude-opus-4",
                ),
            ]
        ),
        encoding="utf-8",
    )
    return caminho


def test_tf_linha_de_despacho_atribui_o_plano_antes_do_primeiro_id_citado(tmp_path):
    """TF (`R-16`, `DRF-18` do `P-0755`): a linha de abertura do despacho (`despacho: P-0755`)
    manda antes de qualquer `P-<n>` citado na prosa livre da mensagem. Concorrente (ler o
    primeiro `P-<n>` da mensagem inteira, ignorando a linha de despacho): gravaria
    `P-0700-planejador`, o `P-<n>` do texto de contexto, não o do despacho."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado

    transcript_path = _transcript_com_mensagem(
        tmp_path / "planejador-transcript.jsonl",
        "Contexto: veja o P-0700 antes.\ndespacho: P-0755\nPlaneje.",
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="pantonic-planner", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[-1].split("\t")[2] == "P-0755-planejador"


def test_tf_linha_de_despacho_atribui_a_tarefa_antes_do_estado(tmp_path):
    """TF (`R-16`, `DRF-18` do `P-0755`): revisor cuja primeira mensagem abre com
    `despacho: P-0755 RAF-T3` grava a tarefa do despacho, não a do estado corrente. Concorrente
    (ler só o estado): gravaria `EXA-T55-revisao`, a tarefa do despacho anterior ainda no disco."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")

    transcript_path = _transcript_com_mensagem(
        tmp_path / "revisor-transcript.jsonl", "despacho: P-0755 RAF-T3\nRevise."
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="pantonic-reviewer", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[-1].split("\t")[2] == "RAF-T3-revisao"


def test_tr_linha_de_despacho_ausente_segue_o_estado(tmp_path):
    """TR: revisor cuja primeira mensagem não abre com a linha de despacho segue o estado
    corrente, como antes da `RAF-T31` — a regra concorrente (exigir a linha) não gravaria
    nada."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"
    estado_path.parent.mkdir(parents=True)
    estado_path.write_text(json.dumps(_estado_valido()), encoding="utf-8")

    transcript_path = _transcript_com_mensagem(
        tmp_path / "revisor-transcript.jsonl", "Revise a entrega, por favor."
    )

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    payload = _payload(agent_type="pantonic-reviewer", agent_transcript_path=str(transcript_path))

    escreveu = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path
    )

    assert escreveu is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[-1].split("\t")[2] == "EXA-T55-revisao"


def test_tf_linhas_por_agente_substitui_a_do_mesmo_agente(tmp_path):
    """TF (`R-16`, `DRF-39` do `P-0755`): duas paradas do mesmo agente (`agent-a1b2`) gravam uma
    linha só na série — a segunda substitui a primeira, e a série ganha a coluna `agente`, vazia
    (`-`) nas linhas antigas que não a tinham. Concorrente (apensar sempre): a série ficaria com
    duas linhas do mesmo agente."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado

    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(
        _HEADER + "2026-09-20\tPantonicApp\tP-0700-scout\tsonnet\t5\t10.0\t20.0\tusage\n",
        encoding="utf-8",
    )

    transcript_path = tmp_path / "agent-a1b2.jsonl"
    payload = _payload(agent_type="pantonic-planner", agent_transcript_path=str(transcript_path))

    _transcript_com_mensagem(transcript_path, "Planeje o P-0755.", input_tokens=10)
    escreveu_1 = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path,
        data="2026-09-28",
    )

    _transcript_com_mensagem(transcript_path, "Planeje o P-0755.", input_tokens=3000)
    escreveu_2 = hook.processar(
        payload, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path,
        data="2026-09-28",
    )

    assert escreveu_1 is True
    assert escreveu_2 is True
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    assert linhas[0] == _HEADER.rstrip("\n") + "\tagente"
    assert linhas[1] == "2026-09-20\tPantonicApp\tP-0700-scout\tsonnet\t5\t10.0\t20.0\tusage\t-"
    assert len(linhas) == 3
    ultima = linhas[2].split("\t")
    assert ultima[2] == "P-0755-planejador"
    assert ultima[5] == "3.0"
    assert ultima[-1] == "agent-a1b2"


def test_tf_linhas_por_agente_outro_agente_apensa(tmp_path):
    """TF (`R-16` do `P-0755`): agentes diferentes apensam, cada um com a própria linha na
    série. Concorrente (agrupar por tarefa, não por agente): a segunda parada substituiria a
    linha da primeira."""
    hook = _load_hook()

    estado_path = tmp_path / "estado" / "tarefa-corrente.json"  # nunca criado
    tsv_path = tmp_path / "telemetria.tsv"
    tsv_path.write_text(_HEADER, encoding="utf-8")

    transcript_um = _transcript_com_mensagem(tmp_path / "agent-um.jsonl", "Planeje o P-0755.")
    payload_um = _payload(agent_type="pantonic-planner", agent_transcript_path=str(transcript_um))
    hook.processar(
        payload_um, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path,
        data="2026-09-28",
    )

    transcript_dois = _transcript_com_mensagem(tmp_path / "agent-dois.jsonl", "Planeje o P-0755.")
    payload_dois = _payload(agent_type="pantonic-planner", agent_transcript_path=str(transcript_dois))
    hook.processar(
        payload_dois, estado_path=estado_path, telemetria_cli=_TELEMETRIA_CLI_PATH, tsv_path=tsv_path,
        data="2026-09-28",
    )

    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    dados = linhas[1:]
    assert [linha.split("\t")[-1] for linha in dados] == ["agent-um", "agent-dois"]
