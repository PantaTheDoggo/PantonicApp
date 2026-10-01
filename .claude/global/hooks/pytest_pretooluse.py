"""Hook PreToolUse (Bash/PowerShell): reescreve comandos pytest "puros" para
canalizar a saida pelo pytest_filter.py, reduzindo a ingestao de contexto.

Regras de seguranca:
- So reescreve comandos que invocam pytest SEM pipe simples ou redirecionamento
  proprio (se o agente ja filtra ou redireciona, respeita a intencao original).
  A recusa e do pipe simples (`|`) e do redirecionamento (`<`, `>`); o `||`
  nao conta como pipe, e um separador de comando, como `&&`.
- Nao reescreve --collect-only/--co (a listagem e o proprio resultado util).
- Bypass explicito: incluir "#nofilter" no fim do comando.
- A sintaxe gerada (`cmd 2>&1 | python filter`) funciona igual em bash e pwsh.
- Comando encadeado (`&&`, `||`, `;`, quebra de linha): so o segmento que
  invoca o pytest entra no bloco filtrado; o resto do comando fica como esta.
  O bloco grava um marcador com o exit code real do pytest
  (`__PYTEST_EXIT__=...`) antes do pipe, e o pytest_filter.py devolve esse
  exit code no lugar do exit code do proprio pipe.
"""
import json
import re
import sys

FILTER_PATH = "C:/Users/panta/.claude/hooks/pytest_filter.py"

PIPE_OU_REDIRECIONAMENTO_RE = re.compile(r"(?<!\|)\|(?!\|)|[<>]")

PYTEST_RE = re.compile(
    r"(?:^|[;&|\n]\s*)"                                 # inicio ou apos ; / & / | / quebra de linha
    r"(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?"           # opcional: python -m
    r"(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)"            # pytest / caminho/pytest
)

# Mesmo casamento de PYTEST_RE, mas ancorado no inicio do segmento (sem o
# prefixo de inicio-de-comando ou separador): usado para testar se o texto de
# UM segmento (ja dividido por dividir_segmentos) e uma invocacao do pytest.
SEGMENTO_PYTEST_RE = re.compile(
    r"^(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)"
)


def passthrough() -> None:
    print("{}")
    sys.exit(0)


def dividir_segmentos(cmd: str) -> list[str]:
    """Divide `cmd` alternando segmento e separador (`&&`, `||`, `;` ou
    quebra de linha), reconhecendo o separador so fora de aspas simples ou
    duplas. A primeira e a ultima parte sao sempre segmentos; `"".join(...)`
    do resultado reproduz `cmd`."""
    partes: list[str] = []
    atual: list[str] = []
    aspas: str | None = None
    i = 0
    n = len(cmd)
    while i < n:
        ch = cmd[i]
        if aspas is not None:
            atual.append(ch)
            if ch == aspas:
                aspas = None
            i += 1
            continue
        if ch in ("'", '"'):
            aspas = ch
            atual.append(ch)
            i += 1
            continue
        if cmd[i : i + 2] in ("&&", "||"):
            partes.append("".join(atual))
            partes.append(cmd[i : i + 2])
            atual = []
            i += 2
            continue
        if ch in (";", "\n"):
            partes.append("".join(atual))
            partes.append(ch)
            atual = []
            i += 1
            continue
        atual.append(ch)
        i += 1
    partes.append("".join(atual))
    return partes


def reescrever(cmd: str, ferramenta: str) -> str | None:
    """Reescreve so os segmentos de `cmd` que invocam o pytest, cada um no seu
    bloco (Bash ou PowerShell conforme `ferramenta`) que grava o exit code
    real em `__PYTEST_EXIT__` antes do pipe pelo pytest_filter.py. Segmento
    sem pytest fica como esta. Devolve `None` se nenhum segmento casar."""
    partes = dividir_segmentos(cmd)
    houve = False
    novas: list[str] = []
    for indice, parte in enumerate(partes):
        if indice % 2 == 1:
            novas.append(parte)
            continue
        texto = parte.strip()
        if not texto or not SEGMENTO_PYTEST_RE.match(texto):
            novas.append(parte)
            continue
        prefixo = parte[: len(parte) - len(parte.lstrip())]
        sufixo = parte[len(parte.rstrip()) :]
        if ferramenta == "PowerShell":
            bloco = (
                '& { %s; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "%s"'
                % (texto, FILTER_PATH)
            )
        else:
            bloco = (
                '{ %s; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s"'
                % (texto, FILTER_PATH)
            )
        novas.append(prefixo + bloco + sufixo)
        houve = True
    if not houve:
        return None
    return "".join(novas)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        passthrough()

    if data.get("tool_name") not in ("Bash", "PowerShell"):
        passthrough()

    cmd = (data.get("tool_input") or {}).get("command") or ""

    if PIPE_OU_REDIRECIONAMENTO_RE.search(cmd):
        passthrough()
    if "#nofilter" in cmd or "pytest_filter" in cmd:
        passthrough()
    if "--collect-only" in cmd or re.search(r"\s--co\b", cmd):
        passthrough()
    if not PYTEST_RE.search(cmd):
        passthrough()

    new_cmd = reescrever(cmd, data.get("tool_name"))
    if new_cmd is None:
        passthrough()
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
