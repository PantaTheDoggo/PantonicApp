"""TK-77a (`docs/DIARIO_DE_OBRAS.md` `### TK-77a`) — o `validate` recusa frontmatter de agente ou
skill que o YAML estrito recusa. Função pura `problemas(caminhos)`: para cada arquivo, recorta o
bloco entre a primeira linha `---` e a seguinte `---` (arquivo sem o bloco não é problema deste
script — o `validate` já o acusa via `Get-Frontmatter`), aplica `yaml.safe_load` e devolve
`"<caminho>: <primeira linha do erro>"` quando o parser levanta, ou `"<caminho>: frontmatter não
é mapeamento"` quando o resultado não é `dict`.

CLI: `python .claude/checks/frontmatter_yaml.py <arquivo>...` imprime um problema por linha e sai
`1` se houver algum, `0` se nenhum; sem PyYAML importável imprime `frontmatter_yaml: PyYAML
ausente` e sai `2`.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def _extrair_frontmatter(texto: str) -> str | None:
    """Bloco entre a primeira linha `---` e a linha `---` seguinte, sem os marcadores. `None`
    quando o arquivo não tem o bloco (início ausente ou não fechado) — não é problema deste
    script."""
    linhas = texto.splitlines()
    inicio = None
    for i, linha in enumerate(linhas):
        if linha.strip() == "---":
            inicio = i
            break
    if inicio is None:
        return None
    fim = None
    for i in range(inicio + 1, len(linhas)):
        if linhas[i].strip() == "---":
            fim = i
            break
    if fim is None:
        return None
    return "\n".join(linhas[inicio + 1 : fim])


def problemas(caminhos: list[Path]) -> list[str]:
    """Um problema por arquivo cujo frontmatter não é YAML válido para `yaml.safe_load` ou não
    carrega um mapeamento. Arquivo sem bloco de frontmatter não entra na lista."""
    resultado: list[str] = []
    for caminho in caminhos:
        texto = caminho.read_text(encoding="utf-8")
        bloco = _extrair_frontmatter(texto)
        if bloco is None:
            continue
        try:
            valor = yaml.safe_load(bloco)
        except yaml.YAMLError as exc:
            mensagem = str(exc)
            primeira_linha = mensagem.splitlines()[0] if mensagem else mensagem
            resultado.append(f"{caminho}: {primeira_linha}")
            continue
        if not isinstance(valor, dict):
            resultado.append(f"{caminho}: frontmatter não é mapeamento")
    return resultado


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir caminho/mensagem com
    acentos; mesma forma de `.claude/tools/review_evidence.py:156-161` (`_forcar_utf8`)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str]) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    if yaml is None:
        print("frontmatter_yaml: PyYAML ausente")
        return 2
    lista = problemas([Path(a) for a in argv])
    for linha in lista:
        print(linha)
    return 1 if lista else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
