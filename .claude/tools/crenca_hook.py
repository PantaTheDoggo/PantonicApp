"""FPU-T4 (`docs/plans/P-0752-fato-no-ponto-de-uso.md` `### FPU-T4`) — gancho `PreToolUse`,
matcher `Write|Edit`: avisa, no ato de gravar plano ou diário, todo número de aceite que chega
sem comando ao lado (DFP-5). Só olha `docs/plans/**` e `docs/DIARIO_DE_OBRAS.md`; conta, no
conteúdo novo (`content` de `Write` ou `new_string` de `Edit`), os literais numéricos de aceite
sem comando na mesma linha e devolve `systemMessage` com a contagem — nunca bloqueia
(`decision: block` não é emitido em caso nenhum) e nunca falha ruidosamente: qualquer exceção
sai `0` sem imprimir nada, no mesmo padrão de falha aberta de `progresso_hook.py`.
"""
from __future__ import annotations

import json
import re
import sys


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `—` — duplicado do
    mesmo utilitário de `card_check.py`/`review_evidence.py` (`DM-11`, sem import cruzado entre
    módulos)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


# --- literais numéricos de aceite (DFP-5): cada padrão abaixo é um "número gravado sem comando
# é crença" candidato; descontado quando a linha em que ele ocorre é a linha de um comando
# (contém "`python " ou "`pwsh ") ou está dentro de bloco cercado, e — só para a âncora de linha
# — quando a âncora tem literal logo em seguida (DFP-4, mesma forma que `card_check._ANCORA_RE` /
# `_LITERAL_APOS_ANCORA_RE`).
_PADRAO_PASSED = re.compile(r"\b\d+ passed\b")
_PADRAO_ANTES = re.compile(r"antes `?\d+`?")
_PADRAO_DEPOIS = re.compile(r"depois `?\d+`?")
_PADRAO_MEDIDO = re.compile(r"Medido antes: \d+")
_PADRAO_ANCORA = re.compile(r"`[^`]+:\d+`")
_LITERAL_APOS_ANCORA_RE = re.compile(r"\s*(?:—|:)\s*`(?:\\`|[^`\\])+`")

_PADROES = (_PADRAO_PASSED, _PADRAO_ANTES, _PADRAO_DEPOIS, _PADRAO_MEDIDO, _PADRAO_ANCORA)

_FENCE_RE = re.compile(r"^\s*(```+|~~~+)")


def contar_crencas(texto: str) -> int:
    """Conta, no `texto` (conteúdo novo gravado), os literais numéricos de aceite sem comando —
    ver `_PADROES` e os descontos de linha-de-comando/bloco-cercado/literal-após-âncora acima."""
    dentro_de_bloco = False
    total = 0
    for linha in texto.splitlines():
        if _FENCE_RE.match(linha):
            dentro_de_bloco = not dentro_de_bloco
            continue
        if dentro_de_bloco:
            continue
        if "`python " in linha or "`pwsh " in linha:
            continue
        trechos = []
        for padrao in _PADROES:
            for m in padrao.finditer(linha):
                if padrao is _PADRAO_ANCORA and _LITERAL_APOS_ANCORA_RE.match(linha, m.end()):
                    continue
                trechos.append((m.start(), m.end()))
        trechos.sort()
        maior_fim = -1
        for inicio, fim in trechos:
            if inicio >= maior_fim:
                total += 1
            maior_fim = max(maior_fim, fim)
    return total


def _elegivel(file_path: str) -> bool:
    normalizado = str(file_path).replace("\\", "/")
    return "docs/plans/" in normalizado or normalizado.endswith("docs/DIARIO_DE_OBRAS.md")


def main(argv: list[str] | None = None, entrada: str | None = None) -> int:
    """Ponto de entrada do gancho `PreToolUse`. Falha aberta: qualquer exceção ⇒ exit 0
    silencioso, sem imprimir nada e sem bloquear a chamada de ferramenta que disparou o gancho."""
    try:
        _forcar_utf8(sys.stdout)
        raw = entrada if entrada is not None else sys.stdin.buffer.read().decode(
            "utf-8", errors="replace"
        )
        payload = json.loads(raw)
        if not isinstance(payload, dict):
            return 0

        ti_raw = payload.get("tool_input")
        ti = ti_raw if isinstance(ti_raw, dict) else {}
        file_path = ti.get("file_path")
        if not isinstance(file_path, str) or not _elegivel(file_path):
            return 0

        conteudo = ti.get("content")
        if not isinstance(conteudo, str):
            conteudo = ti.get("new_string")
        if not isinstance(conteudo, str):
            return 0

        n = contar_crencas(conteudo)
        if n:
            saida = {
                "systemMessage": (
                    f"{n} número(s) de aceite sem comando no texto novo: número sem comando é "
                    "crença — medir antes de gravar"
                )
            }
            print(json.dumps(saida, ensure_ascii=False))
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
