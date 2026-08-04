"""Check executável de ratchet do piso comportamental — GOVERNANCA.md §4.4, item 2.

V2K-T15 (`docs/plans/P-0729-v2-melhoria-candidatos.md` §T15; a doutrina do formato e do
papel deste check foi escrita pela V2K-T14 em GOVERNANCA.md §4.4 — este script a
materializa, não a redefine. DK-7 do Estágio 3B fixa "dois scripts, não um": este cobre
o piso de comportamentos trancados da suíte pytest; `dead_code.py` cobre alcançabilidade
de símbolo Python — gates distintos, unificados só no ponto de invocação
`guardrails-check`).

Papel: falha (exit != 0) quando um comportamento já trancado no piso comportamental do
consumidor desapareceu da coleta real da suíte pytest — nomeando a frase do
comportamento perdido, não só o nodeid. Cobertura percentual não entra em nenhum ponto
(GOVERNANCA.md §4.4 é explícito: percentual não vale como piso, meta ou critério de
pronto em lugar nenhum).

Método:
  1. O consumidor versiona `tests/piso_comportamental.txt` (caminho default, relativo a
     `--root`; ajustável via `--piso`) — uma linha por comportamento trancado, no
     formato `<pytest nodeid> — <comportamento em uma frase>` (travessão em dash " — ",
     conforme GOVERNANCA.md §4.4). Linhas em branco e linhas iniciadas por `#` são
     ignoradas (comentário/organização do arquivo).
  2. Arquivo de piso ausente é o estado normal de um consumidor que ainda não adotou o
     piso comportamental — não é erro. O script imprime "nenhum piso declarado" e sai 0
     (mesmo aprendizado do TK-02: `Get-ExcludedKeys` quebrava sem `kit-exclude.txt`
     presente; script de gate nunca explode por insumo opcional ausente).
  3. Linha presente sem o separador " — " é erro de **formato** (não silêncio): o
     arquivo existe e está mal escrito, o que é diferente de não existir. Sai != 0
     nomeando a linha malformada.
  4. Com o arquivo bem formado, roda `pytest --collect-only -q` sob `--root` e extrai o
     conjunto de nodeids coletados (linhas com `::`, ignorando cabeçalho/rodapé/
     resumo). Cada nodeid do piso ausente desse conjunto é um comportamento perdido:
     sai != 0 nomeando `<nodeid> — <frase>` de cada um.
  5. Todo nodeid do piso presente na coleta = piso intacto: sai 0.

CLI: ``python .claude/checks/ratchet_piso.py [--root <caminho>] [--piso <rel-ao-root>]``.
Sem `--root`, resolve a raiz do repositório a partir do próprio script (mesmo desenho do
`dead_code.py` e do `-KitRoot` do `kit_check.ps1`) — permite provar contra uma fixture
sintética fora da árvore real sem nunca escrever nela. `--piso` é relativo a `--root`,
default `tests/piso_comportamental.txt`.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SEPARATOR = " — "


class PisoFormatError(Exception):
    """Linha do arquivo de piso sem o separador esperado."""


def parse_piso(piso_file: Path) -> list[tuple[int, str, str]]:
    """Retorna [(lineno, nodeid, comportamento), ...]; levanta PisoFormatError na
    primeira linha malformada (não silencia — arquivo presente e mal escrito é erro,
    diferente de arquivo ausente)."""
    entries: list[tuple[int, str, str]] = []
    text = piso_file.read_text(encoding="utf-8")
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if SEPARATOR not in line:
            raise PisoFormatError(
                f"{piso_file}:{lineno}: linha sem separador ' — ' esperado: {raw!r}"
            )
        nodeid, _, comportamento = line.partition(SEPARATOR)
        nodeid = nodeid.strip()
        comportamento = comportamento.strip()
        if not nodeid or not comportamento:
            raise PisoFormatError(
                f"{piso_file}:{lineno}: nodeid ou comportamento vazio: {raw!r}"
            )
        entries.append((lineno, nodeid, comportamento))
    return entries


def collect_nodeids(root: Path) -> set[str]:
    """Roda `pytest --collect-only -q` sob `root` e extrai os nodeids coletados.

    Saída de `--collect-only -q` é uma linha por item de teste contendo `::`, seguida
    de uma linha de resumo em branco/"N tests collected..." sem `::` — filtrar por
    `::` separa item de ruído sem depender do texto exato do resumo (varia por versão
    do pytest)."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    nodeids: set[str] = set()
    for line in result.stdout.splitlines():
        line = line.strip()
        if "::" in line:
            nodeids.add(line)
    return nodeids


def check(root: Path, piso_file: Path) -> tuple[list[str], bool]:
    """Retorna (achados, houve_piso). `houve_piso=False` significa arquivo ausente —
    chamador trata como OK explícito, não como "zero achados coincidentemente"."""
    if not piso_file.exists():
        return [], False

    entries = parse_piso(piso_file)  # PisoFormatError propaga — erro de formato, não achado
    collected = collect_nodeids(root)

    findings: list[str] = []
    for lineno, nodeid, comportamento in entries:
        if nodeid not in collected:
            findings.append(
                f"{piso_file}:{lineno}: {nodeid} — {comportamento} "
                "(comportamento perdido: nodeid nao aparece mais na colecao da suite)"
            )
    return findings, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ratchet do piso comportamental — GOVERNANCA.md §4.4, item 2."
    )
    default_root = Path(__file__).resolve().parent.parent.parent
    parser.add_argument("--root", type=Path, default=default_root, help="Raiz do projeto a checar.")
    parser.add_argument(
        "--piso",
        type=Path,
        default=Path("tests/piso_comportamental.txt"),
        help="Caminho do arquivo de piso, relativo a --root.",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    piso_file = (root / args.piso).resolve()

    try:
        findings, houve_piso = check(root, piso_file)
    except PisoFormatError as exc:
        print(f"ratchet_piso: FALHOU - arquivo de piso malformado: {exc}")
        return 1

    if not houve_piso:
        print(f"ratchet_piso: OK - nenhum piso declarado em '{piso_file}'.")
        return 0

    if not findings:
        print(f"ratchet_piso: OK - piso intacto sob '{root}' ({piso_file}).")
        return 0

    for line in findings:
        print(line)
    print(f"ratchet_piso: FALHOU - {len(findings)} comportamento(s) perdido(s) do piso.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
