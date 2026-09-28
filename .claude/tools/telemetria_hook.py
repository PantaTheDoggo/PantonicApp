"""EXA-T55 (`docs/plans/P-0734-execucao-autonoma.md` `### T55`) — hook `SubagentStop` que fecha
o vão que a `EXA-T14` mediu e deixou aberto (Sonda 5,
`docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`): o payload de `SubagentStop` expõe
consumo (via `agent_transcript_path`) mas não a identidade da tarefa do plano. `DP-S` (`P-0734`
`### 23`) decidiu que a identidade viaja por **contrato**, não por inferência sobre prosa: o
`scrum-master` grava `.claude/estado/tarefa-corrente.json` no ato do despacho
(`.claude/skills/scrum-master/SKILL.md`, Passo 4), e este hook lê de lá.

**Números** (mesmo padrão de parse que `.claude/tools/ocupacao.py`, `T13`, já usa — nenhum leitor
novo se inventa): `tokens_k` = soma de `input_tokens + cache_creation_input_tokens +
cache_read_input_tokens + output_tokens` da **última** entrada `assistant` com `usage` no
`.jsonl` apontado por `agent_transcript_path`, dividida por 1000 — não a soma de todas as
entradas (calibração `ESC-3`, 2026-09-18: seis de seis transcripts reais bateram a notificação
`<usage>`, o número verdadeiro, só com a última mensagem; a soma por `message.id` reproduzia
exatamente os valores errados que o hook vinha gravando, porque `cache_read_input_tokens` é o
contexto **inteiro** relido a cada turno — somá-lo turno a turno multiplica o total pelo número
de turnos); `tool_uses` = contagem de blocos `type == "tool_use"` no `message.content` de
**todas** as entradas `assistant` (esse campo não sofre o mesmo problema — cada bloco aparece em
exatamente uma entrada, nunca repetido); `duracao_s` = diferença, em segundos, entre o primeiro e
o último `timestamp` do transcript.

**Filtro** (`DP-S` `### 23.3` item 4; generalizado na `DAF-15`/`DAF-25`): o hook age para todo
`agent_type` iniciado por `pantonic-` — cada papel do kit grava a própria rodada, com o papel no
identificador da tarefa. Fora do filtro (`agent_type` que não começa por `pantonic-`, ou vazio),
ou sem `agent_transcript_path` legível, é silêncio: exit 0, sem escrever nada. O estado
`tarefa-corrente.json` **não se apaga mais** — ele vale até o despacho seguinte do executor, que
o sobrescreve; só o executor depende dele para a própria linha (sem estado, o executor fica em
silêncio, como antes).

**Papel da linha:** `pantonic-executor` grava `estado["tarefa"]`; `pantonic-reviewer` grava
`<tarefa>-revisao`; `pantonic-consultant` grava `<tarefa>-consultor-<n>` (`<n>` = 1 + linhas da
série cuja `tarefa` já começa por `<tarefa>-consultor-`); `pantonic-planner` grava
`<P-n>-planejador`; `pantonic-model-designer` grava `<P-n>-modelador`; `pantonic-scout` grava
`<P-n>-scout`; outro `pantonic-<nome>` grava `<P-n>-<nome>`. `<tarefa>` vem de `estado["tarefa"]`;
`<P-n>` vem da primeira ocorrência de `P-` seguido de dígitos no texto da primeira entrada
`type == "user"` do transcript. Sem o id que o papel pede, a linha grava `sem-id-<sufixo>` em vez
de ficar em silêncio.

**Cuidado:** este hook é **cliente** do CLI que a `T7` entregou
(`.claude/tools/telemetria.py append`) — chamado via subprocess, nunca reimplementa validação de
coluna aqui (isso recriaria o gabarito que a `T15` tirou dos prompts).

**Falha aberta total**, como o proxy da `T13`: qualquer exceção em `main` é silenciada e o script
sempre sai 0, sem nunca bloquear ou atrasar a chamada que disparou o hook.

Superfície testável, separada do I/O de stdin do hook: `calcular_consumo` (pura) e `processar`
(núcleo do hook, recebe payload e caminhos já resolvidos em vez de ler stdin/`sys.argv` — mesmo
desenho de `apply`/`check`/`drift` em `materializar.py`). `tests/test_telemetria_hook.py`
exercita as duas; `main` lê stdin em UTF-8 explícito (`TK-56a`, `DB-53`) e ganhou cobertura por
subprocesso no mesmo teste, restrita ao ramo `agent_type` fora do filtro do kit.
"""
from __future__ import annotations

import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

_AGENT_TYPE_EXECUTOR = "pantonic-executor"  # papel com regra própria de tarefa/modelo/projeto

_SUFIXO_POR_AGENT_TYPE = {
    "pantonic-reviewer": "revisao",
    "pantonic-consultant": "consultor",
    "pantonic-planner": "planejador",
    "pantonic-model-designer": "modelador",
    "pantonic-scout": "scout",
}

_PAPEIS_POR_TAREFA_DO_ESTADO = {"pantonic-reviewer", "pantonic-consultant"}

_RE_ID_PLANO = re.compile(r"P-\d+")


def calcular_consumo(linhas: list[str]) -> tuple[float, int, float]:
    """`(tokens_k, tool_uses, duracao_s)` a partir das linhas cruas do `.jsonl` exclusivo do
    subagente (`agent_transcript_path`). Entrada malformada ou sem campo esperado é ignorada
    linha a linha (falha aberta na leitura), nunca propaga exceção.

    **`tokens_k` é o `usage` da última mensagem, não a soma de todas** (achado da calibração
    obrigatória do dossiê `ESC-3`, 2026-09-18, sobre seis transcripts reais de subagente
    confrontados com o `<usage>` real da notificação): a soma por `message.id` reproduzia
    exatamente os valores errados que o hook vinha gravando (fatores medidos de até ×20 sobre o
    valor real), porque `cache_read_input_tokens` é o contexto **inteiro** relido a cada turno —
    somá-lo turno a turno multiplica o total pelo número de turnos. A última entrada `assistant`
    com `usage` já carrega o total acumulado da conversa inteira do subagente; usar só ela deu,
    nos seis casos medidos, exatamente o número da notificação. `tool_uses` continua somando
    todos os blocos `tool_use` de todas as entradas — cada bloco de conteúdo aparece em
    exatamente uma entrada, nunca repetido, e essa contagem já bate com a notificação."""
    tokens_ultima_mensagem = 0
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
            tokens_ultima_mensagem = (
                int(usage.get("input_tokens", 0) or 0)
                + int(usage.get("cache_creation_input_tokens", 0) or 0)
                + int(usage.get("cache_read_input_tokens", 0) or 0)
                + int(usage.get("output_tokens", 0) or 0)
            )

        conteudo = mensagem.get("content")
        if isinstance(conteudo, list):
            tool_uses += sum(
                1 for bloco in conteudo if isinstance(bloco, dict) and bloco.get("type") == "tool_use"
            )

    duracao_s = _duracao_segundos(primeiro_ts, ultimo_ts)
    return tokens_ultima_mensagem / 1000, tool_uses, duracao_s


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


def _sufixo_do_papel(agent_type: str) -> str:
    """Sufixo de identificador do papel: os nomeados de `_SUFIXO_POR_AGENT_TYPE`, ou o nome
    depois de `pantonic-` para qualquer outro papel do kit."""
    return _SUFIXO_POR_AGENT_TYPE.get(agent_type, agent_type[len("pantonic-"):])


def _primeiro_texto_de_usuario(linhas: list[str]) -> str | None:
    """Texto (ou concatenação dos blocos `text`) da primeira entrada `type == "user"` do
    transcript, ou `None` quando não há nenhuma."""
    for linha in linhas:
        linha_strip = linha.strip()
        if not linha_strip:
            continue
        try:
            entrada = json.loads(linha_strip)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(entrada, dict) or entrada.get("type") != "user":
            continue
        mensagem = entrada.get("message")
        if not isinstance(mensagem, dict):
            continue
        conteudo = mensagem.get("content")
        if isinstance(conteudo, str):
            return conteudo
        if isinstance(conteudo, list):
            textos = [
                bloco.get("text", "")
                for bloco in conteudo
                if isinstance(bloco, dict) and bloco.get("type") == "text"
            ]
            return "\n".join(textos)
        return None
    return None


def _id_plano_da_primeira_mensagem(linhas: list[str]) -> str | None:
    """`<P-n>` — primeira ocorrência de `P-` seguido de dígitos no texto da primeira entrada
    `type == "user"` do transcript."""
    texto = _primeiro_texto_de_usuario(linhas)
    if not texto:
        return None
    encontrado = _RE_ID_PLANO.search(texto)
    return encontrado.group(0) if encontrado else None


def _ultimo_modelo_assistant(linhas: list[str]) -> str | None:
    """`message.model` da última entrada `assistant` do transcript que o carrega, ou `None`."""
    modelo: str | None = None
    for linha in linhas:
        linha_strip = linha.strip()
        if not linha_strip:
            continue
        try:
            entrada = json.loads(linha_strip)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(entrada, dict) or entrada.get("type") != "assistant":
            continue
        mensagem = entrada.get("message")
        if not isinstance(mensagem, dict):
            continue
        valor = mensagem.get("model")
        if valor:
            modelo = valor
    return modelo


def _normalizar_modelo_de_papel(bruto: str | None) -> str:
    """Normaliza `message.model` do transcript: contém `opus`/`sonnet`/`haiku` vira a palavra
    solta; outro texto vira ele mesmo em minúsculas; ausente vira `nao-informado`."""
    if not bruto:
        return "nao-informado"
    minusculo = bruto.lower()
    for nome in ("opus", "sonnet", "haiku"):
        if nome in minusculo:
            return nome
    return minusculo


def _contar_linhas_com_prefixo(tsv_path: Path, prefixo: str) -> int:
    """Número de linhas da série cuja coluna `tarefa` começa por `prefixo` — usado para numerar
    `<tarefa>-consultor-<n>`."""
    if not tsv_path.is_file():
        return 0
    linhas = tsv_path.read_text(encoding="utf-8").splitlines()
    if not linhas:
        return 0
    colunas = linhas[0].split("\t")
    try:
        indice_tarefa = colunas.index("tarefa")
    except ValueError:
        return 0
    total = 0
    for linha in linhas[1:]:
        if not linha.strip():
            continue
        valores = linha.split("\t")
        if len(valores) <= indice_tarefa:
            continue
        if valores[indice_tarefa].startswith(prefixo):
            total += 1
    return total


def _tsv_para_contagem(tsv_path: Path | None, estado_path: Path) -> Path:
    """Série do hook — lida para contar `<n>` do consultor e escrita por `processar`: `tsv_path`
    quando dado; senão `docs/telemetria.tsv` a partir de `estado_path.parents[2]`."""
    if tsv_path is not None:
        return tsv_path
    return estado_path.parents[2] / "docs" / "telemetria.tsv"


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
        "--modelo", str(estado.get("modelo", "")).strip().lower(),
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
    `sys.argv`. Devolve `True` quando escreveu, `False` em qualquer ramo de silêncio previsto
    (sem nenhum efeito colateral nesse caso). O estado nunca é apagado por este hook — só o
    despacho seguinte do executor o sobrescreve."""
    agent_type = payload.get("agent_type") or ""
    if not agent_type.startswith("pantonic-"):
        return False

    agent_transcript_path = payload.get("agent_transcript_path")
    if not agent_transcript_path:
        return False
    transcript = Path(agent_transcript_path)
    if not transcript.exists():
        return False

    estado = ler_estado(estado_path)
    linhas = transcript.read_text(encoding="utf-8", errors="ignore").splitlines()

    if agent_type == _AGENT_TYPE_EXECUTOR:
        if estado is None:
            return False
        tarefa = str(estado.get("tarefa", ""))
        modelo = str(estado.get("modelo", ""))
        projeto = str(estado.get("projeto", ""))
    else:
        sufixo = _sufixo_do_papel(agent_type)
        if agent_type in _PAPEIS_POR_TAREFA_DO_ESTADO:
            tarefa_base = estado.get("tarefa") if estado is not None else None
            if not tarefa_base:
                tarefa = f"sem-id-{sufixo}"
            elif agent_type == "pantonic-consultant":
                serie = _tsv_para_contagem(tsv_path, estado_path)
                n = 1 + _contar_linhas_com_prefixo(serie, f"{tarefa_base}-consultor-")
                tarefa = f"{tarefa_base}-consultor-{n}"
            else:
                tarefa = f"{tarefa_base}-{sufixo}"
        else:
            id_plano = _id_plano_da_primeira_mensagem(linhas)
            tarefa = f"{id_plano}-{sufixo}" if id_plano else f"sem-id-{sufixo}"
        modelo = _normalizar_modelo_de_papel(_ultimo_modelo_assistant(linhas))
        projeto = str(estado.get("projeto", "")) if estado is not None else estado_path.parents[2].name

    tokens_k, tool_uses, duracao_s = calcular_consumo(linhas)

    args = montar_args_append(
        {"projeto": projeto, "tarefa": tarefa, "modelo": modelo},
        tokens_k, tool_uses, duracao_s, data or datetime.date.today().isoformat(),
    )
    # `AE-5` do `P-0753`: o destino é sempre explícito e é a série de onde a contagem do
    # consultor lê (`_tsv_para_contagem`) — sem `tsv_path`, a do repositório do estado, nunca o
    # default do CLI, que é a série real do kit mesmo quando o estado é de fixture.
    args = args + ["--file", str(_tsv_para_contagem(tsv_path, estado_path))]

    comando = [sys.executable, str(telemetria_cli), *args]
    subprocess.run(comando, check=False, capture_output=True)

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
        try:
            raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        except AttributeError:
            raw = sys.stdin.read()
        payload = json.loads(raw)
        repo_root = _repo_root()
        processar(payload, _estado_path_default(repo_root), _telemetria_cli_default(repo_root))
        return 0
    except Exception:  # noqa: BLE001 — falha aberta é obrigatória, nunca bloqueia o hook
        return 0


if __name__ == "__main__":
    sys.exit(main())
