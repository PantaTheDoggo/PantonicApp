"""Filtro de saida do pytest para economia de contexto do agente.

Le a saida completa do pytest via stdin, grava o log integral em
%TEMP%/claude/pytest_last_run.log e imprime apenas o que importa para o agente:
secoes FAILURES/ERRORS, o short test summary e a linha de sumario final.

Exit code: 0 se a suite passou; 1 se houve falha/erro/saida irreconhecivel
(permite ao agente detectar falha mesmo com o pipe engolindo o exit code
original do pytest).
"""
import os
import re
import sys
import tempfile

MAX_LINES = 200
TAIL_ON_UNKNOWN = 40

HEADER_RE = re.compile(r"^=+ .+ =+$")
SECTION_RE = re.compile(r"^=+ (FAILURES|ERRORS|short test summary info) =+$")
SUMMARY_HINT_RE = re.compile(
    r"(passed|failed|error|no tests ran|skipped|xfailed|xpassed|deselected|warning)"
)
FAILURE_HINT_RE = re.compile(r"(\d+ (failed|errors?)\b|INTERNALERROR|no tests ran)")
# Em modo -q o sumario final vem sem as barras ==== (ex.: "3 failed, 10 passed in 1.2s").
PLAIN_SUMMARY_RE = re.compile(
    r"^(no tests ran|\d+ (passed|failed|errors?|skipped|xfailed|xpassed|deselected|warnings?)\b.*)"
    r" in \d+(\.\d+)?s"
)


def main() -> None:
    try:
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    lines = sys.stdin.read().splitlines()

    log_dir = os.path.join(tempfile.gettempdir(), "claude")
    log_path = os.path.join(log_dir, "pytest_last_run.log")
    try:
        os.makedirs(log_dir, exist_ok=True)
        with open(log_path, "w", encoding="utf-8", errors="replace") as f:
            f.write("\n".join(lines) + "\n")
    except OSError:
        log_path = "(falha ao gravar log completo)"

    # Linha de sumario final: ==== ... ==== com contagens, ou a forma "plana"
    # do modo -q ("3 failed, 10 passed in 1.2s").
    summary_idx = None
    for i in range(len(lines) - 1, -1, -1):
        ln = lines[i]
        if (HEADER_RE.match(ln) and SUMMARY_HINT_RE.search(ln)) or PLAIN_SUMMARY_RE.match(ln):
            summary_idx = i
            break

    # Mantem apenas as secoes de interesse (FAILURES / ERRORS / short summary).
    keep = []
    in_section = False
    for ln in lines:
        if HEADER_RE.match(ln):
            in_section = bool(SECTION_RE.match(ln))
        if in_section:
            keep.append(ln)
    if summary_idx is not None and (not keep or keep[-1] != lines[summary_idx]):
        keep.append(lines[summary_idx])

    if not keep:
        # Saida irreconhecivel (usage error, crash, INTERNALERROR): mostra o fim.
        keep = lines[-TAIL_ON_UNKNOWN:]

    truncated = False
    if len(keep) > MAX_LINES:
        head = keep[: MAX_LINES - TAIL_ON_UNKNOWN]
        tail = keep[-TAIL_ON_UNKNOWN:]
        omitted = len(keep) - len(head) - len(tail)
        keep = head + [f"... [{omitted} linhas omitidas pelo pytest_filter] ..."] + tail
        truncated = True

    print("\n".join(keep))
    note = f"\n[pytest_filter] log completo: {log_path}"
    if truncated:
        note += " (saida filtrada acima foi truncada; use Grep no log)"
    print(note)

    summary = lines[summary_idx] if summary_idx is not None else ""
    failed = summary == "" or bool(FAILURE_HINT_RE.search(summary))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
