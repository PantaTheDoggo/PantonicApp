#!/usr/bin/env python3
"""UserPromptSubmit hook — modelo-por-fase (G-MODELPHASE).

Classifica a FASE do prompt do dono por heuristica de palavras-chave e emite um
nudge de modelo (systemMessage p/ o dono + additionalContext p/ o agente). NAO troca
o modelo — nenhum hook do Claude Code consegue trocar o modelo da conversa principal
(o schema de saida de hook nao tem esse campo); so o dono (`/model`) ou config estatica
o fazem. Este hook institucionaliza a REGRA DE DECISAO + o gate de parada + o anuncio
(Regra 5 / GOVERNANCA.md §3, plano PantonicApp/P-0722-governanca-guardrails-anti-saga).

Prioridade: intelectual > execucao > leitura. Sem sinal claro => silencio (nenhum
nudge), para nao poluir. Nunca quebra o fluxo: qualquer erro => saida vazia, exit 0.
Mantem o additionalContext curto (Regra 3 — economia de contexto): ele entra no
contexto a cada prompt que casar.
"""
from __future__ import annotations

import json
import sys
import unicodedata


def _norm(text: str) -> str:
    """lowercase + remove acentos, para casar 'audite'/'análise' sem variantes."""
    text = text.lower()
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


# Carve-out checado ANTES de qualquer grupo: frases de retomada de backlog/entrada de
# slash-command não contam como execucao mecanica, mesmo contendo "execut" (medido em
# 2026-07-30, V2M-T2 — "execute a proxima tarefa" e orquestracao+delegacao, fase
# intelectual, nao implementacao). Sem sinal claro de fase real => silencio, mesmo
# principio do restante do classificador.
_ORCHESTRATION_ENTRYPOINT = (
    "proximo passo", "proxima tarefa", "execute a proxima", "execute o proximo",
    "pegue o backlog", "continue o backlog", "siga o backlog", "puxe o backlog",
    "drene o backlog", "drenar o backlog",
)

# Ordem de prioridade importa: o primeiro grupo que casar decide a fase.
# Substrings normalizadas (sem acento, minusculas).
_INTELLECTUAL = (
    "planej", "plano", "arquitet", "audit", "avali", "especific", "retrospectiv",
    "parecer", "estrateg", "diagnostic", "trade-off", "tradeoff", "decis", "decid",
    "projet", "design", "analis", "spec", " prd", "abordagem", "proponha", "proposta",
    "revis", "concep", "modelagem", "por que", "porque", "trade off",
)
_EXECUTION = (
    "implement", "execut", "edit", "corrig", "escrev", "test", "rode", "roda ",
    "aplic", "fix", "bug", "refator", "ajust", "commit", "delet", "remov", "renomei",
    " mova", "mover", "adicion", "troqu", "troca", "substitu", "conserta", "conserte",
    "rodar", "instale", "compil", "build",
)
_READING = (
    "leia", " ler", "procur", "busc", "encontr", "grep", "liste", "lista", "mostr",
    "varr", "onde esta", "onde fica", "cade ", "inspecion", "resum", "levante",
    "verifique se existe", "quais arquivos",
)


def _classify(prompt: str) -> str | None:
    p = _norm(" " + prompt + " ")
    if any(k in p for k in _ORCHESTRATION_ENTRYPOINT):
        return None
    if any(k in p for k in _INTELLECTUAL):
        return "intellectual"
    if any(k in p for k in _EXECUTION):
        return "execution"
    if any(k in p for k in _READING):
        return "reading"
    return None


_NUDGE = {
    "intellectual": (
        "\U0001F7E1 Fase intelectual (planejar/arquitetar/auditar/decidir) — "
        "Opus e o modelo certo. Se voce estiver em Sonnet/Haiku, `/model opus`.",
        "Gate modelo-por-fase: este prompt e trabalho intelectual (Regra 7). "
        "Se o modelo ativo NAO for Opus, PARE e peca ao dono `/model opus` antes de "
        "prosseguir (anuncie a troca — Regra 5). Se ja estiver em Opus, ignore.",
    ),
    "execution": (
        "\U0001F7E1 Fase de execucao (implementar/editar/testar) — Sonnet basta. "
        "Rodar em Opus e desperdicio (Regra 7): considere `/model sonnet`.",
        "Gate modelo-por-fase: este prompt e execucao mecanica (Regra 7). Se o modelo "
        "ativo for Opus, recomende ao dono `/model sonnet` antes de implementar "
        "(anuncie — Regra 5), salvo tarefa de alto risco com racional registrado.",
    ),
    "reading": (
        "\U0001F7E1 Fase de leitura/varredura — Haiku basta, ou delegue ao "
        "context-scout. Considere `/model haiku`.",
        "Gate modelo-por-fase: este prompt e leitura/varredura (Regra 7). Prefira "
        "delegar ao subagente context-scout (Haiku) a ler tudo no modelo caro.",
    ),
}


def main() -> None:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except (ValueError, OSError):
        print("{}")
        return

    prompt = ""
    if isinstance(data, dict):
        prompt = data.get("prompt") or data.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        print("{}")
        return

    phase = _classify(prompt)
    if phase is None:
        print("{}")
        return

    system_msg, context_msg = _NUDGE[phase]
    print(json.dumps({
        "systemMessage": system_msg,
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context_msg,
        },
    }))


if __name__ == "__main__":
    main()
