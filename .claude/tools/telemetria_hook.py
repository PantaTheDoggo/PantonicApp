"""EXA-T55 (`docs/plans/P-0734-execucao-autonoma.md` `### T55`) — hook `SubagentStop` que fecha
o vão que a `EXA-T14` mediu e deixou aberto (Sonda 5,
`docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`): o payload de `SubagentStop` expõe
consumo (via `agent_transcript_path`) mas não a identidade da tarefa do plano. `DP-S` (`P-0734`
`### 23`) decidiu que a identidade viaja por **contrato**, não por inferência sobre prosa: o
`scrum-master` grava `.claude/estado/tarefa-corrente.json` no ato do despacho
(`.claude/skills/scrum-master/SKILL.md`, Passo 4), e este hook lê de lá.

**Números** (mesmo padrão de parse que `.claude/tools/ocupacao.py`, `T13`, já usa — nenhum leitor
novo se inventa): `tokens_k` = soma de `input_tokens + cache_creation_input_tokens +
cache_read_input_tokens + output_tokens` das entradas `assistant` do `.jsonl` apontado por
`agent_transcript_path`, dividida por 1000; `tool_uses` = contagem de blocos `type == "tool_use"`
no `message.content` dessas mesmas entradas; `duracao_s` = diferença, em segundos, entre o
primeiro e o último `timestamp` do transcript.

**Filtro** (`DP-S` `### 23.3` item 4): o hook só age quando `agent_type` é papel do kit —
convenção de nome `pantonic-*`. Fora do filtro, ou sem estado gravado (despacho fora do loop),
é silêncio: exit 0, sem escrever nada e **sem consumir o estado** (ele fica para o despacho real
consumir depois). O estado só é apagado depois de a linha ser escrita com sucesso.

**Cuidado:** este hook é **cliente** do CLI que a `T7` entregou
(`.claude/tools/telemetria.py append`) — chamado via subprocess, nunca reimplementa validação de
coluna aqui (isso recriaria o gabarito que a `T15` tirou dos prompts).

**Falha aberta total**, como o proxy da `T13`: qualquer exceção em `main` é silenciada e o script
sempre sai 0, sem nunca bloquear ou atrasar a chamada que disparou o hook.

Superfície testável, separada do I/O de stdin do hook: `calcular_consumo` (pura) e `processar`
(núcleo do hook, recebe payload e caminhos já resolvidos em vez de ler stdin/`sys.argv` — mesmo
desenho de `apply`/`check`/`drift` em `materializar.py`). `tests/test_telemetria_hook.py`
exercita as duas; `main` (leitura de stdin, subprocess real) não é exercitado por teste — é a
superfície de I/O que a separação existe para isolar.
"""
from __future__ import annotations

import datetime
import json
import subprocess
import sys
from pathlib import Path

_AGENT_TYPE_PREFIX_KIT = "pantonic-"  # DP-S §23.3 item 4 — "agent_type é papel do kit"


def calcular_consumo(linhas: list[str]) -> tuple[float, int, float]:
    """`(tokens_k, tool_uses, duracao_s)` a partir das linhas cruas do `.jsonl` exclusivo do
    subagente (`agent_transcript_path`). Entrada malformada ou sem campo esperado é ignorada
    linha a linha (falha aberta na leitura), nunca propaga exceção.

    **Deduplicação por `message.id`** (achado da calibração obrigatória do dossiê `T55`, contra
    um despacho aninhado trivial real): uma única resposta da API vira **múltiplas** entradas
    `type == "assistant"` no transcript quando a mensagem tem mais de um bloco de conteúdo (ex.:
    `thinking` + `text`, ou `text` + `tool_use`) — cada entrada carrega o **mesmo**
    `message.usage`, não um incremento. Somar `usage` por entrada, sem dedupe, dobrava (ou mais)
    o total medido: `subagent_tokens` reportado pelo harness = 8863; soma ingênua por entrada =
    17726 (exatamente 2x, transcript com 2 entradas para a mesma mensagem). A correção soma
    `usage` **uma vez por `message.id`** — `tool_uses` não sofre o mesmo problema, porque cada
    bloco de conteúdo (incluindo `tool_use`) aparece em exatamente uma entrada, nunca repetido."""
    tokens_por_mensagem: dict[str, int] = {}
    tokens_sem_id = 0
    tool_uses = 0
    primeiro_ts: str | None = None
    ultimo_ts: str | None = None

    for linha in linhas:
        linha_strip = linha.strip()
        if not linha_strip:
            continue
        try:
            entrada = json.loads(linha_strip)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(entrada, dict):
            continue

        timestamp = entrada.get("timestamp")
        if isinstance(timestamp, str) and timestamp:
            if primeiro_ts is None:
                primeiro_ts = timestamp
            ultimo_ts = timestamp

        if entrada.get("type") != "assistant":
            continue
        mensagem = entrada.get("message")
        if not isinstance(mensagem, dict):
            continue

        usage = mensagem.get("usage")
        if isinstance(usage, dict) and usage:
            tokens_desta_entrada = (
                int(usage.get("input_tokens", 0) or 0)
                + int(usage.get("cache_creation_input_tokens", 0) or 0)
                + int(usage.get("cache_read_input_tokens", 0) or 0)
                + int(usage.get("output_tokens", 0) or 0)
            )
            message_id = mensagem.get("id")
            if isinstance(message_id, str) and message_id:
                tokens_por_mensagem[message_id] = tokens_desta_entrada
            else:
                # Sem `message.id` (formato antigo/inesperado): soma a entrada isolada em vez de
                # arriscar perder o número — pior caso vira dupla contagem rara, não ausência.
                tokens_sem_id += tokens_desta_entrada

        conteudo = mensagem.get("content")
        if isinstance(conteudo, list):
            tool_uses += sum(
                1 for bloco in conteudo if isinstance(bloco, dict) and bloco.get("type") == "tool_use"
            )

    tokens_total = sum(tokens_por_mensagem.values()) + tokens_sem_id
    duracao_s = _duracao_segundos(primeiro_ts, ultimo_ts)
    return tokens_total / 1000, tool_uses, duracao_s


def _duracao_segundos(primeiro: str | None, ultimo: str | None) -> float:
    if not primeiro or not ultimo:
        return 0.0
    try:
        t0 = datetime.datetime.fromisoformat(primeiro.replace("Z", "+00:00"))
        t1 = datetime.datetime.fromisoformat(ultimo.replace("Z", "+00:00"))
    except ValueError:
        return 0.0
    return max((t1 - t0).total_seconds(), 0.0)


def ler_estado(caminho: Path) -> dict | None:
    """Estado gravado pelo `scrum-master` no despacho, ou `None` quando ausente/ilegível — os
    dois casos tratados como silêncio previsto pela `processar`, nunca como erro."""
    if not caminho.exists():
        return None
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(dados, dict):
        return None
    return dados


def montar_args_append(
    estado: dict, tokens_k: float, tool_uses: int, duracao_s: float, data: str
) -> list[str]:
    """As 8 flags obrigatórias de `telemetria.py append` (`--fonte usage`, porque o número vem
    do transcript, não de contagem do orquestrador)."""
    return [
        "append",
        "--data", data,
        "--projeto", str(estado.get("projeto", "")),
        "--tarefa", str(estado.get("tarefa", "")),
        "--modelo", str(estado.get("modelo", "")),
        "--tool_uses", str(tool_uses),
        "--tokens_k", f"{tokens_k:.1f}",
        "--duracao_s", f"{duracao_s:.1f}",
        "--fonte", "usage",
    ]


def processar(
    payload: dict,
    estado_path: Path,
    telemetria_cli: Path,
    tsv_path: Path | None = None,
    data: str | None = None,
) -> bool:
    """Núcleo testável do hook — recebe payload e caminhos já resolvidos, nunca lê stdin nem
    `sys.argv`. Devolve `True` quando escreveu (e consumiu o estado), `False` em qualquer ramo de
    silêncio previsto (sem nenhum efeito colateral nesse caso)."""
    agent_type = payload.get("agent_type") or ""
    if not agent_type.startswith(_AGENT_TYPE_PREFIX_KIT):
        return False

    estado = ler_estado(estado_path)
    if estado is None:
        return False

    agent_transcript_path = payload.get("agent_transcript_path")
    if not agent_transcript_path:
        return False
    transcript = Path(agent_transcript_path)
    if not transcript.exists():
        return False

    linhas = transcript.read_text(encoding="utf-8", errors="ignore").splitlines()
    tokens_k, tool_uses, duracao_s = calcular_consumo(linhas)

    args = montar_args_append(
        estado, tokens_k, tool_uses, duracao_s, data or datetime.date.today().isoformat()
    )
    if tsv_path is not None:
        args = args + ["--file", str(tsv_path)]

    comando = [sys.executable, str(telemetria_cli), *args]
    subprocess.run(comando, check=False, capture_output=True)

    estado_path.unlink(missing_ok=True)
    return True


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _estado_path_default(repo_root: Path) -> Path:
    return repo_root / ".claude" / "estado" / "tarefa-corrente.json"


def _telemetria_cli_default(repo_root: Path) -> Path:
    return repo_root / ".claude" / "tools" / "telemetria.py"


def main(argv: list[str] | None = None) -> int:  # noqa: ARG001 — hook não recebe argv, lê stdin
    """Ponto de entrada do hook `SubagentStop`. Falha aberta: qualquer exceção ⇒ exit 0
    silencioso, sem imprimir nada e sem atrasar/bloquear o encerramento do subagente."""
    try:
        payload = json.loads(sys.stdin.read())
        repo_root = _repo_root()
        processar(payload, _estado_path_default(repo_root), _telemetria_cli_default(repo_root))
        return 0
    except Exception:  # noqa: BLE001 — falha aberta é obrigatória, nunca bloqueia o hook
        return 0


if __name__ == "__main__":
    sys.exit(main())
