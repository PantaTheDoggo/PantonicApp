"""LM-T10 (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T10`) — a escrita mecânica em
`.claude/agents/*.md`: `python .claude/tools/agentdef.py apply --arquivo <caminho> --de <texto>
--para <texto>`, com `--de`/`--para` repetíveis, lidos em pares, na ordem. Verbo único `apply`:
substitui, num arquivo de definição de agente, cada literal `--de` pelo `--para` correspondente,
só quando o literal ocorre exatamente uma vez no conteúdo atual do arquivo - tudo ou nada. O
instrumento não decide conteúdo algum além do que os pares declaram.

A validação dos itens 1 a 3 do contrato (alvo restrito a `.claude/agents/*.md` por glob não
recursivo, pares `--de`/`--para` completos, ocorrência única de cada `de`) mora em `_validar`,
função única chamada pelo verbo `apply` antes de qualquer escrita (`DM-22`, borda de residência
única) - o que garante que nenhum byte do arquivo muda quando um par falha (item 4, "tudo ou
nada"): `_validar` lê o conteúdo e confere os três itens contra ele; só depois de ela retornar com
sucesso é que `apply_verbo` aplica os pares (em memória) e escreve, uma única vez, com
`encoding='utf-8'` e `newline=''` (item 5: preserva o line ending original do arquivo)."""
from __future__ import annotations

import argparse
import re
import sys

_ALVO_RE = re.compile(r"^\.claude/agents/[^/]+\.md$")


class AgentDefError(Exception):
    """Mensagem já pronta para impressão; todo `apply` que levanta isto sai exit 1."""


def _validar(arquivo: str, des: list[str], paras: list[str]) -> tuple[list[tuple[str, str]], str]:
    """Itens 1 a 3 do contrato, nesta ordem, e só nesta função: alvo restrito a
    `.claude/agents/*.md` (glob não recursivo - um caminho aninhado sob `.claude/agents/` é
    recusado tanto quanto um arquivo fora dele), pares completos (`--de`/`--para` em número
    igual) e ocorrência única de cada `de` no conteúdo do arquivo. Levanta `AgentDefError` na
    primeira falha. Só lê o arquivo depois que os itens 1 e 2 fecham (o caminho já está
    confirmado dentro de `.claude/agents/`). Retorna `(pares, conteudo)` quando os três itens
    fecham - nenhuma escrita acontece aqui."""
    caminho_norm = arquivo.replace("\\", "/")
    if _ALVO_RE.match(caminho_norm) is None:
        raise AgentDefError(f"agentdef: alvo fora de '.claude/agents/*.md' {arquivo}")

    if len(des) != len(paras):
        raise AgentDefError("agentdef: --de e --para vem em pares")

    with open(arquivo, "r", encoding="utf-8", newline="") as f:
        conteudo = f.read()

    pares = list(zip(des, paras))
    for de, _para in pares:
        ocorrencias = conteudo.count(de)
        if ocorrencias == 0:
            raise AgentDefError(f"agentdef: literal nao encontrado {de}")
        if ocorrencias > 1:
            raise AgentDefError(f"agentdef: literal nao e unico {de}")

    return pares, conteudo


def apply_verbo(arquivo: str, des: list[str], paras: list[str]) -> tuple[int, str]:
    """Verbo único: `(exit_code, mensagem)`. Valida (`_validar`) antes de qualquer escrita;
    aplica todos os pares em memória e só então grava, uma única vez, preservando `utf-8` e o
    line ending original do arquivo (item 5)."""
    try:
        pares, conteudo = _validar(arquivo, des, paras)
    except AgentDefError as exc:
        return 1, str(exc)

    novo = conteudo
    for de, para in pares:
        novo = novo.replace(de, para, 1)

    with open(arquivo, "w", encoding="utf-8", newline="") as f:
        f.write(novo)

    saldo = len(novo.splitlines()) - len(conteudo.splitlines())
    return 0, f"agentdef: {arquivo} pares={len(pares)} saldo_linhas={saldo:+d}"


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura em literal acentuado - mesmo utilitário de
    `card_check.py`/`review_evidence.py` (`DM-11`, sem import cruzado entre módulos)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)

    parser = argparse.ArgumentParser(
        description=(
            "Escrita mecânica em .claude/agents/*.md: aplica literais --de/--para declarados, "
            "em pares, sobre um arquivo de definição de agente (LM-T10)."
        )
    )
    subparsers = parser.add_subparsers(dest="verbo", required=True)
    apply_parser = subparsers.add_parser("apply")
    apply_parser.add_argument("--arquivo", required=True)
    apply_parser.add_argument("--de", action="append", default=[], dest="de")
    apply_parser.add_argument("--para", action="append", default=[], dest="para")

    args = parser.parse_args(argv)

    exit_code, mensagem = apply_verbo(args.arquivo, args.de, args.para)
    if exit_code == 0:
        print(mensagem)
    else:
        print(mensagem, file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
