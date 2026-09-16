"""Unidade de trabalho (UoW) para autoria de artefato canônico.

Regra 9 da doutrina global: artefato canônico do harness não se edita em
incrementos in-place. A tarefa abre uma UoW, edita **cópias** fora da árvore do
repositório, apresenta o diff para revisão e materializa tudo num ato só.

Motivo, nos três custos que a edição in-place cobra:

1. Cada `Edit` em caminho protegido abre uma janela de aceite. N edições, N
   interrupções.
2. Ninguém vê a mudança inteira antes de ela valer — a revisão é fragmentada em
   pedaços que chegam um a um.
3. Tarefa interrompida deixa artefato meio-editado, e o estado parcial vira
   dívida de governança em outro lugar (o diário passa a carregar a receita do
   que falta).

O (3) é o caro. Cópia fora da árvore transforma "tarefa morta não deixa
resíduo" de acidente em propriedade: o original só é tocado no `close`.

Escopo — o que entra na UoW: tudo que a tarefa editaria por `Edit`/`Write`.
O que não entra: ledger escrito por ferramenta via Bash (`rdo.py`,
`telemetria.py`) e `.claude/settings.json` (ponto de carga, do `materializar.py`,
`GOVERNANCA.md` §3.1).

O portão é conversacional, não modal: `close` **recusa** rodar antes de um
`diff` ter sido emitido para a UoW corrente (marca `diff_em` no manifesto).
Como a cópia de volta roda por Bash, ela não abre janela nenhuma — a revisão do
diff é o único portão que resta, e por isso é obrigatória.

Residência da UoW: fora do repositório, em
``<tempdir>/claude/uow/<slug do repo>/``. Fora da árvore não suja `git status`,
e o slug derivado do caminho do repo (não da sessão) mantém a UoW viva se a
sessão cair no meio da tarefa.

`close` é **sem argumento** de propósito: os alvos vêm do manifesto, nunca da
linha de comando. Comando com argumento variável não é aprovável de uma vez —
é o que produziu as ~190 entradas de uma-vez-só na allow-list do dono.

Superfície testável: as funções `abrir`/`estado`/`diferenca`/`fechar` recebem
`raiz_uow`/`repo` já resolvidos e nunca leem `sys.argv` — mesmo desenho de
`materializar.py` (`--kit-root`/`--home`) e `dead_code.py` (`--root`), para que
o teste exercite tudo contra `tmp_path` sem jamais escrever no repositório real.

CLI: ``python .claude/tools/uow.py {open,status,diff,close,abort}
[--arquivos ...] [--tarefa ID] [--repo <caminho>] [--raiz-uow <caminho>]``
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

_MANIFESTO_BASENAME = "manifesto.json"
_COPIAS_DIRNAME = "copias"


class UoWInvalida(Exception):
    """Manifesto ausente, malformado, ou operação fora da ordem do ciclo."""


class DriftDoOriginal(Exception):
    """O original mudou depois do `open`: copiar de volta destruiria a mudança."""


# --------------------------------------------------------------------------- #
# Resolução de topologia
# --------------------------------------------------------------------------- #


def resolve_repo(repo_arg: str | None) -> Path:
    if repo_arg:
        return Path(repo_arg).resolve()
    return Path(__file__).resolve().parent.parent.parent


def _slug_do_repo(repo: Path) -> str:
    """Identidade estável da UoW: deriva do caminho do repo, não da sessão.

    Sessão que cai no meio da tarefa não deve levar a UoW junto; o caminho do
    repo é o que permanece.
    """
    bruto = str(repo).replace("\\", "/").strip("/")
    return "".join(c if c.isalnum() else "-" for c in bruto).strip("-").lower()


def resolve_raiz_uow(raiz_arg: str | None, repo: Path) -> Path:
    if raiz_arg:
        return Path(raiz_arg).resolve()
    return Path(tempfile.gettempdir()) / "claude" / "uow" / _slug_do_repo(repo)


def _agora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# --------------------------------------------------------------------------- #
# Manifesto
# --------------------------------------------------------------------------- #


def _caminho_manifesto(raiz_uow: Path) -> Path:
    return raiz_uow / _MANIFESTO_BASENAME


def carregar_manifesto(raiz_uow: Path) -> dict:
    alvo = _caminho_manifesto(raiz_uow)
    if not alvo.exists():
        raise UoWInvalida(
            f"nenhuma UoW aberta em {raiz_uow} — rode `uow.py open --arquivos ...` antes"
        )
    try:
        dados = json.loads(alvo.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise UoWInvalida(f"manifesto malformado em {alvo}: {erro}") from erro
    if not isinstance(dados, dict) or not isinstance(dados.get("arquivos"), list):
        raise UoWInvalida(f"manifesto sem a chave `arquivos` como lista: {alvo}")
    return dados


def gravar_manifesto(raiz_uow: Path, manifesto: dict) -> None:
    raiz_uow.mkdir(parents=True, exist_ok=True)
    _caminho_manifesto(raiz_uow).write_text(
        json.dumps(manifesto, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def _hash(caminho: Path) -> str:
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def _slug_arquivo(relativo: str) -> str:
    return relativo.replace("/", "__").replace("\\", "__")


# --------------------------------------------------------------------------- #
# open
# --------------------------------------------------------------------------- #


def abrir(raiz_uow: Path, repo: Path, arquivos: list[str], tarefa: str | None) -> dict:
    """Copia os originais para a UoW e registra o hash de origem de cada um.

    Idempotente por arquivo: reabrir com um alvo já presente **não** re-copia —
    isso destruiria a edição em curso na cópia. Alvo novo entra na UoW aberta,
    porque tarefa que descobre um arquivo no meio do caminho é normal; o que
    não pode é a descoberta passar despercebida na revisão, e o `diff` final a
    mostra.
    """
    try:
        manifesto = carregar_manifesto(raiz_uow)
    except UoWInvalida:
        manifesto = {
            "tarefa": tarefa,
            "aberta_em": _agora(),
            "diff_em": None,
            "arquivos": [],
        }
    if tarefa and not manifesto.get("tarefa"):
        manifesto["tarefa"] = tarefa

    (raiz_uow / _COPIAS_DIRNAME).mkdir(parents=True, exist_ok=True)
    ja_presentes = {entrada["caminho"] for entrada in manifesto["arquivos"]}

    for bruto in arquivos:
        origem = Path(bruto)
        if not origem.is_absolute():
            origem = (repo / bruto).resolve()
        else:
            origem = origem.resolve()
        try:
            relativo = origem.relative_to(repo).as_posix()
        except ValueError:
            raise UoWInvalida(
                f"alvo fora do repositório {repo}: {origem} — a UoW cobre artefato "
                "versionado do projeto"
            ) from None
        if relativo in ja_presentes:
            continue

        copia = raiz_uow / _COPIAS_DIRNAME / _slug_arquivo(relativo)
        if origem.exists():
            shutil.copy2(origem, copia)
            entrada = {
                "caminho": relativo,
                "novo": False,
                "hash_origem": _hash(origem),
                "copia": copia.name,
            }
        else:
            # Artefato que a tarefa vai criar: não há original para copiar, e o
            # `close` é quem o materializa pela primeira vez.
            copia.write_text("", encoding="utf-8")
            entrada = {
                "caminho": relativo,
                "novo": True,
                "hash_origem": None,
                "copia": copia.name,
            }
        manifesto["arquivos"].append(entrada)
        ja_presentes.add(relativo)

    gravar_manifesto(raiz_uow, manifesto)
    return manifesto


# --------------------------------------------------------------------------- #
# status / diff
# --------------------------------------------------------------------------- #


def _ler(caminho: Path) -> str:
    return caminho.read_text(encoding="utf-8") if caminho.exists() else ""


def estado(raiz_uow: Path, repo: Path) -> list[dict]:
    manifesto = carregar_manifesto(raiz_uow)
    linhas: list[dict] = []
    for entrada in manifesto["arquivos"]:
        original = repo / entrada["caminho"]
        copia = raiz_uow / _COPIAS_DIRNAME / entrada["copia"]
        texto_original = _ler(original)
        texto_copia = _ler(copia)
        linhas.append(
            {
                "caminho": entrada["caminho"],
                "novo": entrada["novo"],
                "mudou": texto_original != texto_copia,
                "chars_antes": len(texto_original),
                "chars_depois": len(texto_copia),
                "linhas_antes": len(texto_original.splitlines()),
                "linhas_depois": len(texto_copia.splitlines()),
                "drift": (
                    not entrada["novo"]
                    and original.exists()
                    and _hash(original) != entrada["hash_origem"]
                ),
            }
        )
    return linhas


def diferenca(raiz_uow: Path, repo: Path) -> str:
    """Diff unificado cópia × original, e **arma o portão** do `close`.

    Marcar `diff_em` aqui é o que torna a revisão obrigatória: como a cópia de
    volta roda por Bash e não abre janela de aceite, o diff apresentado na
    conversa é o único portão que resta antes de o artefato mudar.
    """
    manifesto = carregar_manifesto(raiz_uow)
    partes: list[str] = []
    for entrada in manifesto["arquivos"]:
        original = repo / entrada["caminho"]
        copia = raiz_uow / _COPIAS_DIRNAME / entrada["copia"]
        antes = _ler(original).splitlines(keepends=True)
        depois = _ler(copia).splitlines(keepends=True)
        if antes == depois:
            continue
        partes.extend(
            difflib.unified_diff(
                antes,
                depois,
                fromfile=f"a/{entrada['caminho']}",
                tofile=f"b/{entrada['caminho']}",
            )
        )
    manifesto["diff_em"] = _agora()
    gravar_manifesto(raiz_uow, manifesto)
    return "".join(partes)


# --------------------------------------------------------------------------- #
# close / abort
# --------------------------------------------------------------------------- #


def fechar(raiz_uow: Path, repo: Path) -> list[str]:
    """Materializa as cópias nos originais, num ato só.

    Duas recusas, ambas antes de qualquer escrita:

    - **Sem `diff` emitido** — o portão conversacional não foi aberto.
    - **Drift do original** — alguém tocou o arquivo depois do `open`, e copiar
      de volta apagaria essa mudança em silêncio.
    """
    manifesto = carregar_manifesto(raiz_uow)
    if not manifesto.get("diff_em"):
        raise UoWInvalida(
            "`close` sem `diff` emitido: a revisão é o portão desta UoW — "
            "rode `uow.py diff` e apresente a mudança antes de fechar"
        )

    driftados = [
        entrada["caminho"]
        for entrada in manifesto["arquivos"]
        if not entrada["novo"]
        and (repo / entrada["caminho"]).exists()
        and _hash(repo / entrada["caminho"]) != entrada["hash_origem"]
    ]
    if driftados:
        raise DriftDoOriginal(
            "original alterado depois do `open` — fechar destruiria a mudança:\n  "
            + "\n  ".join(driftados)
        )

    escritos: list[str] = []
    for entrada in manifesto["arquivos"]:
        original = repo / entrada["caminho"]
        copia = raiz_uow / _COPIAS_DIRNAME / entrada["copia"]
        if _ler(original) == _ler(copia):
            continue
        original.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(copia, original)
        escritos.append(entrada["caminho"])

    abortar(raiz_uow)
    return escritos


def abortar(raiz_uow: Path) -> None:
    """Descarta a UoW. O original nunca foi tocado, então não há o que reverter."""
    if raiz_uow.exists():
        shutil.rmtree(raiz_uow)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _formatar_estado(linhas: list[dict]) -> str:
    if not linhas:
        return "UoW aberta, nenhum arquivo."
    saida = []
    for linha in linhas:
        marca = "NOVO " if linha["novo"] else ("M    " if linha["mudou"] else "     ")
        delta = linha["chars_depois"] - linha["chars_antes"]
        sinal = f"{delta:+d}" if delta else "0"
        aviso = "  [DRIFT DO ORIGINAL]" if linha["drift"] else ""
        saida.append(
            f"{marca}{linha['caminho']}  "
            f"{linha['chars_antes']} → {linha['chars_depois']} chars ({sinal}), "
            f"{linha['linhas_antes']} → {linha['linhas_depois']} linhas{aviso}"
        )
    return "\n".join(saida)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="uow.py", description="Unidade de trabalho para autoria de artefato canônico."
    )
    parser.add_argument("comando", choices=["open", "status", "diff", "close", "abort"])
    parser.add_argument("--arquivos", nargs="+", default=[], help="alvos do `open`")
    parser.add_argument("--tarefa", default=None, help="identificador da tarefa")
    parser.add_argument("--repo", default=None)
    parser.add_argument("--raiz-uow", dest="raiz_uow", default=None)
    args = parser.parse_args(argv)

    # Console Windows entrega cp1252 por padrão e engasga no diff e nas setas do
    # status. A saída desta ferramenta é lida por humano e por agente: forçar
    # UTF-8 é condição de funcionamento, não cosmético.
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(encoding="utf-8")

    repo = resolve_repo(args.repo)
    raiz_uow = resolve_raiz_uow(args.raiz_uow, repo)

    try:
        if args.comando == "open":
            if not args.arquivos:
                parser.error("`open` exige --arquivos")
            manifesto = abrir(raiz_uow, repo, args.arquivos, args.tarefa)
            print(f"UoW aberta em {raiz_uow}")
            print(f"tarefa: {manifesto.get('tarefa') or '(não declarada)'}")
            for entrada in manifesto["arquivos"]:
                print(f"  {'novo' if entrada['novo'] else 'copiado'}: {entrada['caminho']}")
            print("\nEdite as cópias em:")
            print(f"  {raiz_uow / _COPIAS_DIRNAME}")
        elif args.comando == "status":
            print(_formatar_estado(estado(raiz_uow, repo)))
        elif args.comando == "diff":
            texto = diferenca(raiz_uow, repo)
            print(texto if texto else "(nenhuma mudança nas cópias)")
        elif args.comando == "close":
            escritos = fechar(raiz_uow, repo)
            if escritos:
                print("materializado:")
                for caminho in escritos:
                    print(f"  {caminho}")
            else:
                print("nada a materializar (cópias idênticas aos originais)")
        elif args.comando == "abort":
            abortar(raiz_uow)
            print(f"UoW descartada; nenhum original foi tocado ({raiz_uow})")
    except (UoWInvalida, DriftDoOriginal) as erro:
        print(f"erro: {erro}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
