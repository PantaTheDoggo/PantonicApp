"""EXA-T9a (`docs/plans/P-0734-execucao-autonoma.md` `### T9a`) — a metade `git` da evidência de
revisão: o reviewer recebe *o que mudou* e *se a execução saiu do escopo* já apurado, em vez de
varrer o repositório para descobrir. `python .claude/tools/review_evidence.py --plano <caminho.md>
--tarefa <ID> [--root <raiz>] [--max-diff-chars <N>] [--out <caminho>]` localiza o dossiê da
tarefa reusando `extrair_dossie` de `.claude/tools/rdo.py:186` (carregado por caminho via
`importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_rdo.py` — `.claude/` não é
pacote importável), coleta `git diff --stat` e a lista de arquivos tocados (`git status
--porcelain=v1`, que também enxerga arquivo novo ainda não rastreado), confronta arquivos tocados
contra os arquivos-alvo declarados no dossiê e recorta o trecho de diff de cada arquivo-alvo até
um teto de caracteres (truncamento sempre visível na saída, nunca silencioso).

Invariante (`DA-7`): a saída é fato com veredito mecânico, sem interpretação — a camada mecânica é
autoridade sobre o que ela mede, quem interpreta é o reviewer. A dimensão `escopo`
(`docs/RUBRICA_DE_REVISAO.md:63-77`) tem uma faixa `parcial` que depende de declaração de desvio
na entrega — insumo que este script não recebe. Por isso, quando há arquivo tocado fora
dos alvos, a saída relata o **fato** ("N arquivo(s) fora dos alvos: ...") e deixa o veredito em
aberto; nunca resolve sozinha para `parcial`.

Limitação conhecida e aceita da extração de arquivos-alvo: o campo `Arquivos-alvo`/`Entregável` do
dossiê é prosa livre: a extração é puramente textual (todo caminho entre crases é tratado como
alvo declarado), então uma frase como "não editar `x.py`" também cita `x.py` entre crases e o
script o inclui como se fosse alvo. Interpretar a negação é trabalho do reviewer, não deste
script — resolver isso aqui seria reinterpretar prosa, não medir fato (fora do escopo desta
fatia).

A seção `## Guardas` (`EXA-T9b`) invoca a bateria de seis comandos de `GOVERNANCA.md` §3 (a
mesma que fechou a `T9a`: `python -m pytest -q`, `dead_code.py`, `ratchet_piso.py`,
`kit_check.ps1 -Mode validate`, `kit_check.ps1 -Mode check-drift`, `check-readme.ps1`), cola exit
code e saída de cada um, e trava o veredito mecânico das dimensões `guardas`
(`docs/RUBRICA_DE_REVISAO.md:94-106` — autoridade integral, sem faixa de juízo: qualquer comando
fora de exit 0 resolve para `não conforme`, nunca para `parcial` sozinha) e `testes`
(`docs/RUBRICA_DE_REVISAO.md:79-92` — evidência mecânica é o exit code do comando `pytest` da
bateria). A bateria de produção (`BATERIA_GUARDAS`) é injetável (`comandos_guardas` em
`montar_documento`/`rodar_bateria_guardas`) para permitir teste determinístico sem depender da
infraestrutura real do hub num repositório de fixture."""
from __future__ import annotations

import argparse
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

_BACKTICK_RE = re.compile(r"`([^`]+)`")
_LINHA_REF_RE = re.compile(r":\d+(-\d+)?$")


class ReviewEvidenceValidationError(ValueError):
    """Dossiê, plano, tarefa ou repositório git inválido (mensagem já nomeia o problema)."""


def _default_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _load_rdo(root: Path):
    caminho = root / ".claude" / "tools" / "rdo.py"
    if not caminho.is_file():
        raise ReviewEvidenceValidationError(f"rdo.py: módulo não encontrado em '{caminho}'")
    spec = importlib.util.spec_from_file_location("rdo", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def extrair_arquivos_alvo(campos: dict) -> list[str]:
    """Extrai os caminhos declarados no campo `Arquivos-alvo`/`Entregável` do dossiê — extração
    textual mecânica (tudo entre crases que contém `/`), sem interpretar prosa negativa. Ver
    limitação conhecida no docstring do módulo."""
    texto = campos.get("arquivos-alvo") or campos.get("entregavel") or ""
    vistos: dict[str, None] = {}
    for match in _BACKTICK_RE.finditer(texto):
        candidato = match.group(1).strip()
        if "/" not in candidato and "\\" not in candidato:
            continue
        candidato = _LINHA_REF_RE.sub("", candidato)
        vistos.setdefault(candidato, None)
    return list(vistos.keys())


def _git(args: list[str], root: Path) -> str:
    try:
        resultado = subprocess.run(
            ["git", *args], cwd=str(root), capture_output=True, text=True, encoding="utf-8"
        )
    except FileNotFoundError as exc:
        raise ReviewEvidenceValidationError("git: executável não encontrado no PATH") from exc
    if resultado.returncode != 0:
        raise ReviewEvidenceValidationError(
            f"git {' '.join(args)}: exit {resultado.returncode} - {resultado.stderr.strip()}"
        )
    return resultado.stdout


def _diff(args_sem_head: list[str], root: Path) -> str:
    """`git diff HEAD ...`; sem commit ainda (repositório recém-criado), cai para `git diff ...`
    puro (índice vazio contra árvore de trabalho) em vez de falhar."""
    try:
        return _git(["diff", "HEAD", *args_sem_head], root)
    except ReviewEvidenceValidationError:
        return _git(["diff", *args_sem_head], root)


def coletar_diff_stat(root: Path) -> str:
    return _diff(["--stat"], root).strip()


def coletar_arquivos_tocados(root: Path) -> list[str]:
    """`git status --porcelain=v1 --untracked-files=all` — ao contrário de `git diff --stat`,
    também enxerga arquivo novo ainda não rastreado (o caso comum de uma tarefa que *cria*
    arquivo-alvo). `--untracked-files=all` é necessário: sem ele, um diretório inteiramente novo
    aparece colapsado como `dir/` em vez de listar cada arquivo dentro dele."""
    saida = _git(["status", "--porcelain=v1", "--untracked-files=all"], root)
    tocados: dict[str, None] = {}
    for linha in saida.splitlines():
        if not linha:
            continue
        caminho = linha[3:]
        if " -> " in caminho:
            caminho = caminho.split(" -> ", 1)[1]
        caminho = caminho.strip().strip('"')
        tocados.setdefault(caminho, None)
    return sorted(tocados.keys())


def confrontar_escopo(tocados: list[str], arquivos_alvo: list[str]) -> dict:
    """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`): `conforme`
    quando o conjunto tocado está contido no conjunto declarado; caso contrário, só o fato — a
    faixa `parcial` depende de um insumo (desvio declarado na entrega) que este script
    não recebe, então o veredito fica em aberto (`None`), nunca resolvido para `parcial`."""
    alvo_set = set(arquivos_alvo)
    fora = sorted(t for t in tocados if t not in alvo_set)
    if not fora:
        return {"fora_dos_alvos": [], "veredito": "conforme"}
    return {"fora_dos_alvos": fora, "veredito": None}


def _diff_para_arquivo(root: Path, caminho_rel: str) -> str:
    texto = _diff(["--", caminho_rel], root)
    if texto.strip():
        return texto
    caminho_abs = root / caminho_rel
    if caminho_abs.is_file():
        try:
            return caminho_abs.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return "(arquivo binário ou não-UTF-8 — trecho omitido)"
    return "(sem diferença coletável — arquivo ausente na árvore de trabalho)"


def montar_trechos(root: Path, arquivos_alvo: list[str], teto_chars: int) -> dict[str, dict]:
    """Trecho de diff (ou conteúdo integral, se o arquivo é novo e sem diff registrável) de cada
    arquivo-alvo, truncado em `teto_chars` — truncamento sempre marcado na saída (nunca
    silencioso)."""
    trechos: dict[str, dict] = {}
    for caminho in arquivos_alvo:
        texto = _diff_para_arquivo(root, caminho)
        truncado = len(texto) > teto_chars
        trechos[caminho] = {"texto": texto[:teto_chars] if truncado else texto, "truncado": truncado}
    return trechos


BATERIA_GUARDAS: list[tuple[str, list[str]]] = [
    ("pytest", ["python", "-m", "pytest", "-q"]),
    ("dead_code", ["python", ".claude/checks/dead_code.py"]),
    ("ratchet_piso", ["python", ".claude/checks/ratchet_piso.py"]),
    ("kit_check_validate", ["pwsh", ".claude/checks/kit_check.ps1", "-Mode", "validate"]),
    ("kit_check_check_drift", ["pwsh", ".claude/checks/kit_check.ps1", "-Mode", "check-drift"]),
    ("check_readme", ["pwsh", ".claude/checks/check-readme.ps1"]),
]


def _rodar_comando(nome: str, args: list[str], root: Path) -> dict:
    """Roda um comando da bateria com `cwd=root` e devolve exit code + saída colada (stdout e
    stderr concatenados) — fato mecânico, sem interpretação. Executável ausente no PATH (ex.:
    `pwsh` não instalado) não derruba a coleta: vira `exit_code=None` com a mensagem do erro na
    própria saída, nunca uma exceção que aborta a bateria inteira."""
    try:
        resultado = subprocess.run(
            args, cwd=str(root), capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
    except FileNotFoundError as exc:
        return {"nome": nome, "comando": " ".join(args), "exit_code": None, "saida": f"(executável não encontrado: {exc})"}
    saida = (resultado.stdout or "") + (resultado.stderr or "")
    return {"nome": nome, "comando": " ".join(args), "exit_code": resultado.returncode, "saida": saida.strip()}


def rodar_bateria_guardas(root: Path, comandos: list[tuple[str, list[str]]] | None = None) -> list[dict]:
    """Roda a bateria de guardas de `GOVERNANCA.md` §3 (seis comandos na bateria de produção) e
    devolve, na ordem, exit code + saída de cada um. `comandos` é injetável — a bateria real
    depende de infraestrutura do hub (`.claude/checks/*`, `pytest.ini`) ausente num repositório de
    fixture isolado; testes passam uma bateria fake curta em vez de rodar a real contra um root
    que não a tem."""
    alvo = comandos if comandos is not None else BATERIA_GUARDAS
    return [_rodar_comando(nome, args, root) for nome, args in alvo]


def veredito_guardas(resultados: list[dict]) -> str:
    """Veredito mecânico travado da dimensão `guardas` (`docs/RUBRICA_DE_REVISAO.md:94-106`) —
    autoridade integral, sem faixa de juízo (`DA-7`): qualquer comando fora de exit 0 trava em
    `não conforme`; só quando todos os comandos fecham em exit 0 resolve para `conforme`. Nunca
    resolve para `parcial` sozinha (a faixa `parcial` da rubrica depende de julgar se a causa é
    anterior à tarefa — insumo que este script não recebe)."""
    if resultados and all(r["exit_code"] == 0 for r in resultados):
        return "conforme"
    return "não conforme"


def veredito_testes(resultados: list[dict]) -> str:
    """Veredito mecânico travado da dimensão `testes` (`docs/RUBRICA_DE_REVISAO.md:79-92`) —
    evidência mecânica é o exit code do comando `pytest` da bateria: exit 0 trava `conforme`,
    exit não-zero ou comando `pytest` ausente da bateria trava `não conforme` (nunca silêncio)."""
    pytest_resultado = next((r for r in resultados if r["nome"] == "pytest"), None)
    if pytest_resultado is not None and pytest_resultado["exit_code"] == 0:
        return "conforme"
    return "não conforme"


def _renderizar_guardas(
    resultados: list[dict], veredito_guardas_valor: str, veredito_testes_valor: str, teto_saida_chars: int
) -> list[str]:
    linhas: list[str] = ["## Guardas (bateria de `GOVERNANCA.md` §3)"]
    for r in resultados:
        exit_txt = r["exit_code"] if r["exit_code"] is not None else "erro"
        linhas.append(f"- `{r['nome']}` (`{r['comando']}`): exit {exit_txt}")
        if r["exit_code"] != 0:
            saida = r["saida"] or "(sem saída capturada)"
            truncado = len(saida) > teto_saida_chars
            texto = saida[:teto_saida_chars] if truncado else saida
            linhas.append("  ```")
            linhas.extend(f"  {linha}" for linha in texto.splitlines() or [texto])
            linhas.append("  ```")
            if truncado:
                linhas.append(f"  [truncado em {teto_saida_chars} caracteres]")
    linhas.append(f"- Veredito mecânico (`guardas`): {veredito_guardas_valor}")
    linhas.append(f"- Veredito mecânico (`testes`): {veredito_testes_valor}")
    return linhas


def _renderizar(
    *,
    plano_id: str,
    tarefa_id: str,
    diff_stat: str,
    arquivos_tocados: list[str],
    arquivos_alvo: list[str],
    escopo: dict,
    trechos: dict[str, dict],
    teto_diff_chars: int,
    resultados_guardas: list[dict],
    veredito_guardas_valor: str,
    veredito_testes_valor: str,
    teto_guarda_chars: int,
) -> str:
    linhas: list[str] = []
    linhas.append(f"# Evidência de revisão — {plano_id} {tarefa_id}")
    linhas.append("")
    linhas.append("## Diff (`git diff --stat`)")
    linhas.append("```")
    linhas.append(diff_stat if diff_stat else "(sem diferenças)")
    linhas.append("```")
    linhas.append("")
    linhas.append("## Arquivos tocados")
    if arquivos_tocados:
        linhas.extend(f"- `{caminho}`" for caminho in arquivos_tocados)
    else:
        linhas.append("- nenhum arquivo tocado")
    linhas.append("")
    linhas.append("## Escopo")
    alvos_txt = ", ".join(f"`{c}`" for c in arquivos_alvo) if arquivos_alvo else "(nenhum declarado)"
    tocados_txt = ", ".join(f"`{c}`" for c in arquivos_tocados) if arquivos_tocados else "(nenhum)"
    linhas.append(f"- Arquivos-alvo declarados: {alvos_txt}")
    linhas.append(f"- Arquivos tocados: {tocados_txt}")
    if escopo["veredito"] == "conforme":
        linhas.append("- Veredito mecânico: conforme")
    else:
        fora_txt = ", ".join(f"`{c}`" for c in escopo["fora_dos_alvos"])
        linhas.append(f"- Fato: {len(escopo['fora_dos_alvos'])} arquivo(s) fora dos alvos: {fora_txt}")
        linhas.append(
            "- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, "
            "não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)"
        )
    linhas.append("")
    linhas.append(f"## Trechos de diff dos arquivos-alvo (teto {teto_diff_chars} caracteres)")
    if not trechos:
        linhas.append("- nenhum arquivo-alvo declarado")
    for caminho, info in trechos.items():
        linhas.append("")
        linhas.append(f"### `{caminho}`")
        linhas.append("```")
        linhas.append(info["texto"] if info["texto"] else "(vazio)")
        linhas.append("```")
        if info["truncado"]:
            linhas.append(f"[truncado em {teto_diff_chars} caracteres]")
    linhas.append("")
    linhas.extend(
        _renderizar_guardas(
            resultados_guardas, veredito_guardas_valor, veredito_testes_valor, teto_guarda_chars
        )
    )
    linhas.append("")
    return "\n".join(linhas)


def montar_documento(
    plano_path: Path,
    tarefa_id: str,
    root: Path,
    *,
    teto_diff_chars: int = 4000,
    comandos_guardas: list[tuple[str, list[str]]] | None = None,
    teto_guarda_chars: int = 2000,
) -> str:
    plano_path = Path(plano_path)
    if not plano_path.is_file():
        raise ReviewEvidenceValidationError(f"plano: arquivo não encontrado '{plano_path}'")

    rdo = _load_rdo(root)
    try:
        dossie = rdo.extrair_dossie(
            plano_path,
            tarefa_id,
            esquema_legado=False,
            modelo_legado=None,
            classe_legado=None,
            teto_legado=None,
        )
    except rdo.RdoValidationError as exc:
        raise ReviewEvidenceValidationError(str(exc)) from exc

    arquivos_alvo = extrair_arquivos_alvo(dossie.campos)
    diff_stat = coletar_diff_stat(root)
    tocados = coletar_arquivos_tocados(root)
    escopo = confrontar_escopo(tocados, arquivos_alvo)
    trechos = montar_trechos(root, arquivos_alvo, teto_diff_chars)
    resultados_guardas = rodar_bateria_guardas(root, comandos_guardas)
    veredito_guardas_valor = veredito_guardas(resultados_guardas)
    veredito_testes_valor = veredito_testes(resultados_guardas)

    plano_id_match = re.match(r"^(P-\d{4})", plano_path.stem)
    plano_id = plano_id_match.group(1) if plano_id_match else plano_path.stem

    return _renderizar(
        plano_id=plano_id,
        tarefa_id=dossie.tarefa_id,
        diff_stat=diff_stat,
        arquivos_tocados=tocados,
        arquivos_alvo=arquivos_alvo,
        escopo=escopo,
        trechos=trechos,
        teto_diff_chars=teto_diff_chars,
        resultados_guardas=resultados_guardas,
        veredito_guardas_valor=veredito_guardas_valor,
        veredito_testes_valor=veredito_testes_valor,
        teto_guarda_chars=teto_guarda_chars,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Evidência de revisão (metade git) — diff, arquivos tocados e confronto de escopo, "
            "mecânico e sem interpretação (EXA-T9a)."
        )
    )
    parser.add_argument("--plano", required=True, type=Path, help="Caminho do .md do plano.")
    parser.add_argument("--tarefa", required=True, help="Identificador da tarefa (ex.: T9a).")
    parser.add_argument(
        "--root", type=Path, default=_default_root(), help="Raiz do repositório (onde 'git' roda)."
    )
    parser.add_argument(
        "--max-diff-chars",
        type=int,
        default=4000,
        dest="max_diff_chars",
        help="Teto de caracteres por trecho de diff de arquivo-alvo (truncamento sempre visível).",
    )
    parser.add_argument(
        "--out", type=Path, default=None, help="Também grava o documento neste caminho (escrita atômica)."
    )
    args = parser.parse_args(argv)

    try:
        documento = montar_documento(
            args.plano, args.tarefa, args.root, teto_diff_chars=args.max_diff_chars
        )
    except ReviewEvidenceValidationError as exc:
        print(f"review_evidence: FALHOU - {exc}", file=sys.stderr)
        return 1

    print(documento)

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=str(args.out.parent), prefix=".review-evidence-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as tmp_file:
                tmp_file.write(documento)
            os.replace(tmp_path, args.out)
        except Exception:
            Path(tmp_path).unlink(missing_ok=True)
            raise

    destino_msg = f" (gravado em '{args.out}')" if args.out is not None else ""
    print(f"review_evidence: OK - dossiê de evidência gerado para '{args.tarefa}'{destino_msg}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
