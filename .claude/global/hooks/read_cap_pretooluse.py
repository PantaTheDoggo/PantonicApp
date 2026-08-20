"""Hook PreToolUse (Read): nega Read integral em arquivo de texto grande.

Aplica a regra "nunca Read integral em arquivo > 500 linhas" (CLAUDE.md Regra 3,
onboard/doc-map): se a chamada nao tem offset/limit e o arquivo passa do limiar,
nega com orientacao (Grep para localizar a faixa + Read com offset/limit; DOC_MAP
para docs). Leitura em blocos deliberada (com offset/limit) nunca e bloqueada —
esse e o bypass intencional.

Salvaguardas:
- So age em arquivos de texto (extensoes binarias/imagem/PDF passam direto).
- Arquivos pequenos em bytes (< 20 kB) passam mesmo com muitas linhas curtas:
  o custo real e de tokens, nao de linhas.
- Qualquer erro de leitura/parse -> passthrough (o Read reporta o erro natural).
"""
import json
import os
import sys

THRESHOLD_LINES = 500
THRESHOLD_BYTES = 20_000  # ~500 linhas de 40 chars; abaixo disso o custo e baixo

SKIP_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".ico", ".svg",
    ".pdf", ".ipynb",
    ".zip", ".7z", ".gz", ".tar", ".exe", ".dll", ".pyd", ".so",
    ".mp4", ".mp3", ".wav", ".woff", ".woff2", ".ttf", ".otf",
}


def passthrough() -> None:
    print("{}")
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        passthrough()

    if data.get("tool_name") != "Read":
        passthrough()

    tool_input = data.get("tool_input") or {}
    if (
        tool_input.get("offset") is not None
        or tool_input.get("limit") is not None
        or tool_input.get("pages")
    ):
        passthrough()

    path = tool_input.get("file_path") or ""
    if os.path.splitext(path)[1].lower() in SKIP_EXTS:
        passthrough()

    lines = 0
    try:
        if os.path.getsize(path) < THRESHOLD_BYTES:
            passthrough()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 16), b""):
                lines += chunk.count(b"\n")
                if lines > THRESHOLD_LINES:
                    break
    except OSError:
        passthrough()

    if lines <= THRESHOLD_LINES:
        passthrough()

    reason = (
        f"Read integral bloqueado (economia de contexto): '{path}' tem mais de "
        f"{THRESHOLD_LINES} linhas. Localize a faixa relevante com Grep e leia so "
        f"ela com Read offset/limit. Para docs, consulte docs/DOC_MAP.md primeiro. "
        f"Se a leitura integral for realmente necessaria, leia em blocos "
        f"deliberados com offset/limit."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
