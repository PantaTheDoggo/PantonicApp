#!/usr/bin/env python3
"""BKL-T11 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T11`) — hook `UserPromptSubmit`
que injeta a saída de `.claude/tools/backlog.py next` no prompt do dono quando ele pede o
próximo passo, para que o pickup pare de ser servido por leitura manual do diário e do inbox.

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — `backlog.py` é
carregado por caminho via `importlib.util.spec_from_file_location`, nunca por subprocesso: o
custo do hook é o de uma chamada de função, não o de um processo novo (restrição do card).

Superfície testável, separada do I/O de stdin do hook (`main`, mesmo desenho de
`telemetria_hook.py`): `processar` recebe o payload já parseado e devolve o objeto
`hookSpecificOutput` (ou `None` quando o gatilho não casa — stdout vazio, exit 0)."""
from __future__ import annotations

import importlib.util
import json
import sys
import unicodedata
from pathlib import Path

_GATILHO = "proximo passo"


def _norm(text: str) -> str:
    """lowercase + remove acentos (NFKD, descarta combinantes) — mesmo `_norm` do precedente
    `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, para casar `próximo passo` e
    `proximo passo` sem variantes."""
    text = text.lower()
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def _carregar_backlog():
    caminho = Path(__file__).resolve().parent / "backlog.py"
    spec = importlib.util.spec_from_file_location("backlog", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def _casa_gatilho(prompt) -> bool:
    return isinstance(prompt, str) and _GATILHO in _norm(prompt)


def _texto_next(modulo, repo: Path) -> str:
    """A saída de `next` tal como o CLI a produz sem flags: seleção + dossiê quando
    `exit_code == 0`, ou a mensagem do erro nomeado (E-1/E-2/E-3) quando não."""
    modelo = modulo.carregar(repo)
    selecao = modulo.selecionar_next(modelo)
    if selecao.exit_code == 0:
        inbox_planos = repo / "docs" / "plans" / "_INBOX.md"
        return modulo.renderizar_next(modelo, selecao, inbox_planos=inbox_planos)
    return selecao.mensagem or ""


def processar(payload: dict, repo: Path | None = None, backlog_module=None) -> dict | None:
    """Núcleo do hook. `repo`/`backlog_module` são injeção para teste (mesmo padrão de
    `telemetria_hook.processar`); em produção ambos ficam `None` e resolvem para o repo real
    a partir da localização do próprio `backlog.py`."""
    prompt = payload.get("prompt") if isinstance(payload, dict) else None
    if not _casa_gatilho(prompt):
        return None

    modulo = backlog_module or _carregar_backlog()
    alvo = repo if repo is not None else modulo.resolve_repo(None)
    try:
        contexto = _texto_next(modulo, alvo)
    except Exception as exc:  # o hook nunca bloqueia o prompt — qualquer falha vira contexto
        contexto = f"backlog_hook: falha ao rodar next: {exc}"

    return {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": contexto,
        }
    }


def main(repo: Path | None = None) -> int:
    try:
        try:
            raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        except AttributeError:
            raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except (ValueError, OSError):
        payload = {}

    resultado = processar(payload, repo=repo)
    if resultado is not None:
        print(json.dumps(resultado))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
