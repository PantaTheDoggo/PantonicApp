"""EXA-T13 (`docs/plans/P-0734-execucao-autonoma.md` `### T13`) — proxy de ocupação da janela de
contexto do loop autônomo — **aviso informativo à orquestração entre tarefas**, sob a diretriz de
dimensionamento de `GOVERNANCA.md` §3. Mede a ocupação e avisa; não prescreve parada a quem executa
uma tarefa. Complementar ao sinal de poluição de contexto, que já tinha instrumento (sinal do
executor).

Rota fechada na `EXA-T1` Sonda 3 (`docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md`): variante (a),
hook lendo `transcript_path`. A variante (b) — contador de tarefas calibrado por
`docs/telemetria.tsv` — está descartada por derivação: o dossiê só a admitia se a sonda tivesse
derrubado o hook, e ela não derrubou.

Mecanismo de entrega do aviso ao agente (percorrido nesta tarefa, evidência colada no RDO): um
hook `PreToolUse` que devolve `{"hookSpecificOutput": {"hookEventName": ..., "additionalContext":
"..."}}` no stdout tem esse texto injetado no contexto do agente logo após a chamada de ferramenta
que disparou o hook — confirmado por sonda direta nesta mesma execução, primeiro mecanismo
tentado. Não foi necessário recorrer a `UserPromptSubmit` nem a um arquivo consultado pelo
`scrum-master`.

**Numerador (ocupação):** a última entrada `type == "assistant"` do `.jsonl` do transcript que
tenha bloco `message.usage` dá `input_tokens + cache_read_input_tokens +
cache_creation_input_tokens`. Nenhuma entrada com `usage` ⇒ ramo de fallback: estimativa por
`soma(len(linha)) / 4` sobre todas as linhas do transcript, fonte `"estimado"`.

**Denominador:** `JANELA_TOKENS`, default 200000, sobrescrevível pela variável de ambiente
`PANTONIC_JANELA_TOKENS`. **Limiar:** 0.50 — o "~50% da janela" que a diretriz de dimensionamento
de `GOVERNANCA.md` §3 já doutrina, não um número novo. A reclassificação do instrumento como aviso
informativo não mexe no valor nem no comportamento: muda o estatuto do que ele emite.

**Filtro de contexto:** o payload de `PreToolUse` de uma sessão de subagente traz `agent_type`
preenchido (confirmado nesta tarefa e na Sonda 3 — ambas mediram `agent_type="pantonic-executor"`
dentro de uma sessão de executor). Como o campo nomeia o tipo do subagente ativo e a sessão
principal do loop não é, ela própria, um subagente, o filtro assume `agent_type` ausente/vazio
nessa sessão — leitura não remedida diretamente (nenhuma sonda deste projeto alcança a sessão do
`scrum-master` a partir de dentro de uma sessão de executor). `agent_type` truthy ⇒ silêncio, exit
0, sem imprimir nada.

**Falha aberta, obrigatória:** o script roda em toda chamada de ferramenta (registrado em
`.claude/settings.json`). Qualquer exceção — transcript ausente, JSON malformado, encoding — é
silenciada e o script sempre sai 0, nunca bloqueando nem atrasando a chamada que disparou o hook.

Superfície testável, separada do I/O do hook: `calcular_ocupacao(linhas) -> (tokens, fonte)` e
`avaliar(tokens, janela) -> (fracao, cruzou)`. `tests/test_ocupacao.py` exercita as duas; o hook
(`main`, leitura de stdin/arquivo) não é exercitado por teste — é a superfície de I/O que a
separação existe para isolar.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

JANELA_TOKENS_ENV = "PANTONIC_JANELA_TOKENS"
JANELA_TOKENS_DEFAULT = 200_000
JANELA_TOKENS = int(os.environ.get(JANELA_TOKENS_ENV) or JANELA_TOKENS_DEFAULT)

LIMIAR = 0.50  # GOVERNANCA.md §3 — "~50% da janela", não um número novo (DP-Q)

MENSAGEM_AVISO = (
    "Ocupação da janela de contexto cruzou o teto de trabalho (~50%, GOVERNANCA.md §4.3). "
    "Encerre a tarefa corrente, arquive o RDO, prepare o handover de janela e pare — não inicie "
    "tarefa nova neste contexto."
)


def calcular_ocupacao(linhas: list[str]) -> tuple[int, str]:
    """Ocupação a partir das linhas cruas do `.jsonl` do transcript (uma entrada por linha).

    Numerador: `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` da última
    entrada `type == "assistant"` com bloco `message.usage` não vazio. Sem nenhuma entrada assim,
    cai no ramo de fallback: `soma(len(linha)) // 4` sobre todas as linhas, fonte `"estimado"`.
    """
    ultimo_usage: dict | None = None
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
        usage = mensagem.get("usage") if isinstance(mensagem, dict) else None
        if isinstance(usage, dict) and usage:
            ultimo_usage = usage

    if ultimo_usage is not None:
        tokens = (
            int(ultimo_usage.get("input_tokens", 0) or 0)
            + int(ultimo_usage.get("cache_read_input_tokens", 0) or 0)
            + int(ultimo_usage.get("cache_creation_input_tokens", 0) or 0)
        )
        return tokens, "usage"

    estimado = sum(len(linha) for linha in linhas) // 4
    return estimado, "estimado"


def avaliar(tokens: int, janela: int) -> tuple[float, bool]:
    """Fração de ocupação e se cruzou o limiar de 50% (`LIMIAR`). `janela <= 0` é caso
    degenerado absorvido (fração 0.0, não cruza) em vez de propagar `ZeroDivisionError` —
    coerente com a postura de falha aberta de quem chama esta função."""
    if janela <= 0:
        return 0.0, False
    fracao = tokens / janela
    return fracao, fracao >= LIMIAR


def main(argv: list[str] | None = None) -> int:  # noqa: ARG001 — hook não recebe argv, lê stdin
    """Ponto de entrada do hook `PreToolUse`. Falha aberta: qualquer exceção ⇒ exit 0
    silencioso, sem imprimir nada e sem atrasar a chamada de ferramenta que disparou o hook."""
    try:
        payload = json.loads(sys.stdin.read())

        if payload.get("agent_type"):
            return 0

        transcript_path = payload.get("transcript_path")
        if not transcript_path:
            return 0

        texto = Path(transcript_path).read_text(encoding="utf-8", errors="ignore")
        linhas = texto.splitlines()

        tokens, _fonte = calcular_ocupacao(linhas)
        _fracao, cruzou = avaliar(tokens, JANELA_TOKENS)

        if cruzou:
            saida = {
                "hookSpecificOutput": {
                    "hookEventName": payload.get("hook_event_name", "PreToolUse"),
                    "additionalContext": MENSAGEM_AVISO,
                }
            }
            print(json.dumps(saida))
        return 0
    except Exception:  # noqa: BLE001 — falha aberta é obrigatória, nunca bloqueia a ferramenta
        return 0


if __name__ == "__main__":
    sys.exit(main())
