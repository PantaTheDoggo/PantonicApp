"""Hook PreToolUse (Bash/PowerShell): economia de contexto para comandos verbosos.

Tabela de reescritas/bloqueios (CLAUDE.md Regra 3):
- `git status` sem forma curta      -> `git status --short`
- `git log` sem limitador/formato   -> `git log --oneline -20`
- builds verbosos (pyinstaller, pip install, npm install/ci/run build)
                                    -> saida canalizada por tail_filter.py
                                       (log completo em %TEMP%\\claude\\, so a
                                       cauda entra no contexto)
- listagens recursivas (ls -R, Get-ChildItem/gci/dir -Recurse, tree)
                                    -> deny com sugestao de Glob

Salvaguardas (mesmo modelo do pytest_pretooluse.py):
- Nao mexe em comando com pipe/redirecionamento proprio.
- Bypass explicito: "#nofilter" no fim do comando.
- Nao reescreve o que ja passa por um filtro (tail_filter/pytest_filter).
- A sintaxe gerada (`cmd 2>&1 | python filtro`) funciona igual em bash e pwsh.
"""
import json
import re
import sys

TAIL_PATH = "C:/Users/panta/.claude/hooks/tail_filter.py"

RECURSIVE_LIST_RE = re.compile(
    r"(?i)(?:\b(?:Get-ChildItem|gci|dir)\b[^|;\n]*-Recurse)"
    r"|(?:(?:^|[;&]\s*)ls\s+-[A-Za-z]*R)"
    r"|(?:(?:^|[;&]\s*)tree\b)"
)
GIT_STATUS_RE = re.compile(r"\bgit\s+status\b")
GIT_STATUS_OK_RE = re.compile(r"--short|--porcelain|\s-s\b|\s-z\b")
GIT_LOG_RE = re.compile(r"\bgit\s+log\b")
GIT_LOG_OK_RE = re.compile(
    r"--oneline|--pretty|--format|--stat|--patch|--max-count|--name-only"
    r"|--name-status|\s-p\b|\s-L\b|\s-n\s*\d|\s-\d+"
)
BUILD_RE = re.compile(
    r"(?i)pyinstaller"
    r"|pip3?(?:\.exe)?\s+install"
    r"|-m\s+pip\s+install"
    r"|npm\s+(?:install|ci)\b"
    r"|npm\s+run\s+build"
)


def passthrough() -> None:
    print("{}")
    sys.exit(0)


def respond(decision: dict) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    **decision,
                }
            }
        )
    )
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        passthrough()

    if data.get("tool_name") not in ("Bash", "PowerShell"):
        passthrough()

    cmd = (data.get("tool_input") or {}).get("command") or ""

    if "#nofilter" in cmd or "tail_filter" in cmd or "pytest_filter" in cmd:
        passthrough()

    if RECURSIVE_LIST_RE.search(cmd):
        respond(
            {
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    "Listagem recursiva bloqueada (economia de contexto): use a "
                    "ferramenta Glob com padrao especifico, excluindo build/, "
                    "dist/, .venv/, __pycache__/, node_modules/. Bypass "
                    "deliberado: terminar o comando com #nofilter."
                ),
            }
        )

    if any(ch in cmd for ch in "|<>"):
        passthrough()

    new_cmd = cmd
    if GIT_STATUS_RE.search(new_cmd) and not GIT_STATUS_OK_RE.search(new_cmd):
        new_cmd = GIT_STATUS_RE.sub("git status --short", new_cmd, count=1)
    if GIT_LOG_RE.search(new_cmd) and not GIT_LOG_OK_RE.search(new_cmd):
        new_cmd = GIT_LOG_RE.sub("git log --oneline -20", new_cmd, count=1)
    if BUILD_RE.search(new_cmd):
        new_cmd = f'{new_cmd} 2>&1 | python "{TAIL_PATH}" build_last_run.log 40'

    if new_cmd == cmd:
        passthrough()

    respond({"permissionDecision": "allow", "updatedInput": {"command": new_cmd}})


if __name__ == "__main__":
    main()
