"""Hook PreToolUse (Bash/PowerShell): reescreve comandos pytest "puros" para
canalizar a saida pelo pytest_filter.py, reduzindo a ingestao de contexto.

Regras de seguranca:
- So reescreve comandos que invocam pytest SEM pipe/redirecionamento proprio
  (se o agente ja filtra ou redireciona, respeita a intencao original).
- Nao reescreve --collect-only/--co (a listagem e o proprio resultado util).
- Bypass explicito: incluir "#nofilter" no fim do comando.
- A sintaxe gerada (`cmd 2>&1 | python filter`) funciona igual em bash e pwsh.
"""
import json
import re
import sys

FILTER_PATH = "C:/Users/panta/.claude/hooks/pytest_filter.py"

PYTEST_RE = re.compile(
    r"(?:^|[;&]\s*)"                                    # inicio ou apos ; / &&
    r"(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?"           # opcional: python -m
    r"(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)"            # pytest / caminho/pytest
)


def passthrough() -> None:
    print("{}")
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        passthrough()

    if data.get("tool_name") not in ("Bash", "PowerShell"):
        passthrough()

    cmd = (data.get("tool_input") or {}).get("command") or ""

    if any(ch in cmd for ch in "|<>"):
        passthrough()
    if "#nofilter" in cmd or "pytest_filter" in cmd:
        passthrough()
    if "--collect-only" in cmd or re.search(r"\s--co\b", cmd):
        passthrough()
    if not PYTEST_RE.search(cmd):
        passthrough()

    new_cmd = f'{cmd} 2>&1 | python "{FILTER_PATH}"'
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "allow",
                    "updatedInput": {"command": new_cmd},
                }
            }
        )
    )


if __name__ == "__main__":
    main()
