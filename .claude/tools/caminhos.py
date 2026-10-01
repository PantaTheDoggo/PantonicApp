"""P-0749 SAN-T1 — residência única da forma do id e do caminho de plano (`DSA-8`).

Duas formas convivem, reconhecidas pelo caminho, sem chave de configuração (`DSA-7`): plano
legado `docs/plans/P-<dígitos>-<slug>.md` e plano em pasta `docs/plans/P-<n>-<slug>/plano.md`.
Nenhuma outra ferramenta guarda cópia destas regex (`I-3`); cada uma carrega este módulo por
caminho, via `importlib.util.spec_from_file_location`. Função entra aqui com o primeiro chamador
de produção (`DSA-18`); `main` é a CLI de listagem e o entry point do módulo (`DSA-19`).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PLANO_HEADER_RE = re.compile(r"^# (P-\d+) — (.+)$")
ID_PLANO_RE = re.compile(r"^P-(\d+)$")
CAMINHO_PLANO_INBOX_RE = re.compile(r"docs/plans/P-\d+-[^)\s`/]+(?:/plano)?\.md")
ID_PLANO_INBOX_RE = re.compile(r"docs/plans/P-(\d+)-")
CONTADOR_INBOX_RE = re.compile(r"\*\*Próximo id de plano: P-\d+\.\*\*")
CONTADOR_INBOX_ID_RE = re.compile(r"\*\*Próximo id de plano: P-(\d+)\.\*\*")

NOME_PLANO_PASTA = "plano.md"
_ID_NO_NOME_RE = re.compile(r"^(P-\d+)")
_PASTA_RE = re.compile(r"^P-\d+-")


def planos_dir(raiz: Path) -> Path:
    return Path(raiz) / "docs" / "plans"


def inbox_planos(raiz: Path) -> Path:
    return planos_dir(raiz) / "_INBOX.md"


def e_layout_pasta(plano_path: Path) -> bool:
    p = Path(plano_path)
    return p.name == NOME_PLANO_PASTA and _PASTA_RE.match(p.parent.name) is not None


def arquivos_de_plano(raiz: Path) -> list[Path]:
    base = planos_dir(raiz)
    legado = [p for p in base.glob("P-*.md") if p.is_file()]
    pasta = [p for p in base.glob("P-*/" + NOME_PLANO_PASTA) if p.is_file() and e_layout_pasta(p)]
    return sorted(legado + pasta)


def id_do_plano(plano_path: Path) -> str | None:
    p = Path(plano_path)
    nome = p.parent.name if e_layout_pasta(p) else p.stem
    m = _ID_NO_NOME_RE.match(nome)
    return m.group(1) if m else None


def pasta_do_plano(plano_path: Path) -> Path | None:
    p = Path(plano_path)
    return p.parent if e_layout_pasta(p) else None


NOME_ESTADO = "estado.tsv"
CABECALHO_ESTADO = "id\ttipo\tstatus\trazao\tdata\tnota"


def estado_tsv(plano_path: Path) -> Path:
    return Path(plano_path).parent / NOME_ESTADO


def formatar_id(numero: int, largura: int) -> str:
    return f"P-{numero:0{largura}d}"


def pasta_por_id(raiz: Path, plano_id: str) -> Path | None:
    achadas = [p.parent for p in planos_dir(raiz).glob(plano_id + "-*/" + NOME_PLANO_PASTA) if p.is_file()]
    return achadas[0] if len(achadas) == 1 else None


def destino_rdo(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "rdo" / f"{tarefa}.md"


def destino_laudo(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "laudos" / f"{tarefa}.md"


def destino_evidencia(pasta: Path, tarefa: str) -> Path:
    return Path(pasta) / "evidencia" / f"{tarefa}.md"


# Artefatos de fechamento de plano (`GOVERNANCA.md` §4.2, *Pasta do plano*; `TK-88`): o
# documento de validação (`operacoes.md`, skill `entrega-de-encerramento`) e a entrega aceita
# (`entrega.md`, escrita por `encerrar.py plano`). Plano legado: `docs/OPERACOES_AS_IS_<id>.md`
# e `docs/plans/_ENTREGA-<id>.md`, ao lado de `_CENARIO-<id>.md`.
def destino_operacoes(raiz: Path, plano_path: Path) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "operacoes.md"
    return Path(raiz) / "docs" / f"OPERACOES_AS_IS_{id_do_plano(plano_path)}.md"


def destino_entrega(raiz: Path, plano_path: Path) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "entrega.md"
    return planos_dir(raiz) / f"_ENTREGA-{id_do_plano(plano_path)}.md"


# Destino único da medida do executor (`TK-92a`, `RAF-T15`/`R-05`): plano em pasta grava/procura
# na pasta do plano dentro da raiz medida (`planos_dir(raiz) / <pasta> / "evidencia"`, não ao
# lado do `plano.md` real — a árvore de `plano_path` pode ser uma cópia); plano legado e tíquete
# do diário (ex.: `docs/DIARIO_DE_OBRAS.md`) caem em `<raiz>/docs/RDO/evidencia`, com
# `<id ou stem>` = `id_do_plano(plano_path) or Path(plano_path).stem` — a mesma regra que
# `review_evidence.py` já usava para o plano_id. `mundo` (`"antes"`/`"depois"`/`None`) vira
# sufixo `-<mundo>` no nome, vazio quando `None`.
def destino_medida(raiz: Path, plano_path: Path, tarefa: str, mundo: str | None = None) -> Path:
    plano_path = Path(plano_path)
    sufixo = f"-{mundo}" if mundo is not None else ""
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return (
            planos_dir(raiz)
            / pasta.name
            / "evidencia"
            / f"{id_do_plano(plano_path)}-{tarefa}-medida{sufixo}.json"
        )
    plano_id = id_do_plano(plano_path) or plano_path.stem
    return Path(raiz) / "docs" / "RDO" / "evidencia" / f"{plano_id}-{tarefa}-medida{sufixo}.json"


def destino_despacho(raiz: Path, plano_path: Path, tarefa: str) -> Path:
    pasta = pasta_do_plano(plano_path)
    if pasta is not None:
        return pasta / "despacho" / f"{tarefa}.md"
    return Path(raiz) / "docs" / "RDO" / "despacho" / f"{tarefa}.md"


def main(argv: list[str] | None = None) -> int:
    """Lista os planos da raiz, um por linha: `<id><TAB><caminho relativo à raiz>`."""
    parser = argparse.ArgumentParser(description="Lista os planos, legado e em pasta.")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    args = parser.parse_args(argv)
    raiz = Path(args.root)
    for plano in arquivos_de_plano(raiz):
        print(f"{id_do_plano(plano) or '-'}\t{plano.relative_to(raiz).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
