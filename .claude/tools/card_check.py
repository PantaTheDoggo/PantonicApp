"""LM-T5b (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T5b`) — a régua de autoria que roda:
`python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` recorta o bloco `Verificação`
do card pela forma normativa de `docs/RUBRICA_DE_REVISAO.md` `### 8.1` (comando em bloco cercado,
linha `→` com o esperado, literal `**Medido antes: <valor>**`), exige os três elementos em cada
item e **roda** cada comando publicado, comparando a saída medida agora com o `Medido antes`
declarado — divergência é falha nomeada, porque significa que o card descreve um mundo que não é
o que está na árvore.

Reusa `rdo.extrair_dossie` (que por sua vez usa `rdo._parsear_campos_com_linhas`, `.claude/tools/rdo.py:187`,
para localizar o cabeçalho da tarefa e recortar o bloco de campos) — o parser de campos é
**importado, nunca reescrito**. Carregado por caminho via `importlib.util.spec_from_file_location`,
mesmo padrão de `review_evidence.py` (`.claude/` não é pacote importável).

Contrato de segurança: a decisão é **por token**, depois de `shlex.split` — só executa comando
cujo primeiro token esteja na lista fechada (`python`, `pwsh`) e recusa — reportado, nunca
executado — qualquer comando com um **token isolado** que seja operador de shell (`;`, `&&`,
`||`, `|`, `>`, `>>`, `<`, `<<`) ou comece por substituição de comando (`` ` ``, `$(`). O conteúdo
de um argumento citado não é varrido por metacaractere: a justificativa é o próprio modo de
execução — `subprocess.run` roda os tokens **sem `shell=True`**, então um `|` dentro de um
argumento citado é texto do argumento, nunca operador.

Só afere e reporta o bloco `Verificação`: não corrige card, não julga objetivo/passos/restrições e
não substitui o `pantonic-reviewer` — roda **antes** do despacho, não depois da entrega. `rdo.py`,
`backlog.py` e `review_evidence.py` ficam intocados."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


class CardCheckValidationError(ValueError):
    """Plano, tarefa ou dossiê inválidos (mensagem já nomeia o problema)."""


def _default_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _exigir_plano(plano_path: Path) -> None:
    if not plano_path.is_file():
        raise CardCheckValidationError(f"plano: arquivo não encontrado '{plano_path}'")


def _load_rdo(root: Path):
    caminho = root / ".claude" / "tools" / "rdo.py"
    if not caminho.is_file():
        raise CardCheckValidationError(f"rdo.py: módulo não encontrado em '{caminho}'")
    spec = importlib.util.spec_from_file_location("rdo", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _carregar_caminhos():
    caminho = Path(__file__).resolve().parent / "caminhos.py"
    spec = importlib.util.spec_from_file_location("caminhos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar_caminhos()


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `→` — duplicado do
    mesmo utilitário de `review_evidence.py` (`DM-11`, sem import cruzado entre módulos)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


# --- forma da `Verificação` (`docs/RUBRICA_DE_REVISAO.md` `### 8.1` e DFP-14, forma inline):
# recortada das linhas **brutas** do campo (`DossieTarefa.campos_linhas["verificacao"]`,
# `DFP-13`) — marcador de item só no início de uma linha bruta do markdown original (`DFP-3`).

# Marcador de início de item: "N." no início de uma linha bruta (aplicado linha a linha por
# `_parsear_itens`, e também sobre o texto de cada item já unido por espaço — nesse caso o
# marcador está sempre na posição 0).
_ITEM_MARKER_RE = re.compile(r"^\s*(?P<num>\d+)\.")
_ABERTURA_BLOCO_RE = re.compile(r"\s*```")
_MEDIDO_ANTES_RE = re.compile(r"\*\*Medido antes:\s*(?P<valor>[^*]+?)\*\*")
_SETA_RE = re.compile(r"→\s*(?P<esperado>.+?)(?=\*\*Medido antes:|$)")
# Forma inline (DFP-14): esperado vai até " — antes" (par opcional) ou o fim do item.
_SETA_INLINE_RE = re.compile(r"→\s*(?P<esperado>.+?)(?=\s—\s*antes\b|\Z)")
# Par `antes`/`depois` opcional da forma inline; o valor pode estar entre crases ou não.
_ANTES_DEPOIS_RE = re.compile(
    r"antes\s+`?(?P<antes>[^`,;]+)`?[,;]?\s*depois\s+`?(?P<depois>[^`.\n]+)`?"
)
# Primeiro trecho entre crases simples — usado tanto para extrair o comando da forma inline
# quanto para achar o literal dentro de um `esperado` sem par `antes`/`depois`.
_CRASE_RE = re.compile(r"`(?P<val>[^`]*)`")
_AFERICAO_MANUAL_RE = re.compile(r"\*\*Aferição:\s*manual\*\*")

_COMANDOS_PERMITIDOS = ("python", "pwsh")
_TOKENS_SHELL_RECUSADOS = frozenset({";", "&&", "||", "|", ">", ">>", "<", "<<"})
_EXIT_RE = re.compile(r"^exit\s+(-?\d+)$", re.IGNORECASE)


class ItemVerificacao:
    """Um item do bloco `Verificação`, na forma normativa da `### 8.1` (`forma="8.1"`) ou na
    forma inline da `DFP-14` (`forma="inline"`, com `antes`/`depois` em vez de `medido_antes`).
    Classe simples (não `@dataclass`), mesmo motivo de `DossieTarefa`/`LaudoResultado` em
    `rdo.py`: módulo carregado por caminho via `importlib` nos testes e nas ferramentas irmãs."""

    def __init__(
        self,
        indice: int,
        comando: str | None,
        esperado: str | None,
        medido_antes: str | None,
        afericao_manual: bool,
        forma: str = "8.1",
        antes: str | None = None,
        depois: str | None = None,
    ):
        self.indice = indice
        self.comando = comando
        self.esperado = esperado
        self.medido_antes = medido_antes
        self.afericao_manual = afericao_manual
        self.forma = forma
        self.antes = antes
        self.depois = depois


def _parsear_itens(linhas: list[str]) -> tuple[list[ItemVerificacao], list[str]]:
    """`(itens, falhas_forma)`. `linhas` são as linhas **brutas** do campo `verificacao`
    (`DossieTarefa.campos_linhas["verificacao"]`, `DFP-13`). Marcador de item é `_ITEM_MARKER_RE`
    (`^\\s*\\d+\\.`) no início de uma linha bruta (`DFP-3`) — não mais em qualquer ponto do texto
    achatado, onde uma quebra de linha virada espaço podia confundir prosa de continuação com item
    novo. Cada item vai da sua linha marcadora até a linha anterior à próxima marcadora (ou o fim
    do campo); as linhas do item são unidas por espaço, o mesmo tratamento que o texto achatado já
    dava, agora escopado por item.

    O resto da linha do marcador, logo após `N.`, decide a forma: abre bloco cercado (`` ``` ``,
    como `EX-T1`) é a forma normativa da `### 8.1` (tratamento inalterado — o primeiro `` ``` ``
    fechado é o comando, e o resto é vasculhado por `→`, `**Medido antes:**` e
    `**Aferição: manual**`); começa por uma crase simples é a forma inline (`DFP-14`: comando entre
    crases, `→` e o par `antes`/`depois` opcionais); qualquer outro resto (prosa, como `EX-T4`) vira
    `item N: fora da forma da 8.1` e **não** entra em `itens` — descartar em silêncio é o falso
    verde que esta função existe para fechar. Elemento ausente vira `None` — a nomeação da falha é
    responsabilidade de quem chama (`verificar_tarefa`)."""
    heads: list[int] = []
    for i, linha in enumerate(linhas):
        if _ITEM_MARKER_RE.match(linha):
            heads.append(i)

    itens: list[ItemVerificacao] = []
    falhas_forma: list[str] = []
    for pos, inicio in enumerate(heads):
        fim = heads[pos + 1] if pos + 1 < len(heads) else len(linhas)
        texto_item = " ".join(linha.strip() for linha in linhas[inicio:fim])
        m_num = _ITEM_MARKER_RE.match(texto_item)
        num = m_num.group("num")
        resto = texto_item[m_num.end() :].lstrip()

        if resto.startswith("```"):
            abertura = _ABERTURA_BLOCO_RE.match(texto_item, m_num.end())
            fim_abertura = abertura.end()
            bloco = texto_item[fim_abertura:]
            fechamento = bloco.find("```")
            if fechamento == -1:
                comando = None
                pos_resto = ""
            else:
                comando = bloco[:fechamento].strip() or None
                pos_resto = bloco[fechamento + 3 :]
            m_medido = _MEDIDO_ANTES_RE.search(pos_resto)
            medido_antes = m_medido.group("valor").strip() if m_medido else None
            m_seta = _SETA_RE.search(pos_resto)
            esperado = m_seta.group("esperado").strip() if m_seta else None
            afericao_manual = bool(_AFERICAO_MANUAL_RE.search(pos_resto))
            itens.append(
                ItemVerificacao(
                    len(itens) + 1, comando, esperado, medido_antes, afericao_manual, forma="8.1"
                )
            )
        elif resto.startswith("`"):
            m_cmd = _CRASE_RE.search(texto_item, m_num.end())
            comando = (m_cmd.group("val").strip() or None) if m_cmd else None
            pos_resto = texto_item[m_cmd.end() :] if m_cmd else texto_item[m_num.end() :]
            m_seta = _SETA_INLINE_RE.search(pos_resto)
            esperado = m_seta.group("esperado").strip() if m_seta else None
            m_par = _ANTES_DEPOIS_RE.search(pos_resto)
            antes = m_par.group("antes").strip() if m_par else None
            depois = m_par.group("depois").strip() if m_par else None
            afericao_manual = bool(_AFERICAO_MANUAL_RE.search(pos_resto))
            itens.append(
                ItemVerificacao(
                    len(itens) + 1,
                    comando,
                    esperado,
                    None,
                    afericao_manual,
                    forma="inline",
                    antes=antes,
                    depois=depois,
                )
            )
        else:
            falhas_forma.append(
                f'item {num}: fora da forma da 8.1 (bloco cercado não vem logo após "{num}.")'
            )

    return itens, falhas_forma


def _validar_comando(comando: str) -> str | None:
    """`None` quando o comando é seguro para execução; senão, a razão da recusa. A recusa é
    **reportada, nunca executada** — chamado sempre antes de `_rodar_comando`. A decisão é por
    **token**, depois de `shlex.split`: recusa só quando um token **isolado** é operador de shell
    ou substituição de comando; o conteúdo de um argumento citado (ex.: `pwsh -Command "(… |
    Measure-Object).Count"`) não é varrido por metacaractere, porque `_rodar_comando` executa sem
    `shell=True` — o token citado inteiro nunca é interpretado por um shell."""
    try:
        tokens = shlex.split(comando)
    except ValueError as exc:
        return f"comando ilegível: {exc}"
    for tok in tokens:
        if tok in _TOKENS_SHELL_RECUSADOS or tok.startswith("$(") or tok.startswith("`"):
            return (
                f"token de shell isolado recusado ('{tok}') - operador de shell ou substituição "
                "de comando fora de argumento citado"
            )
    if not tokens or tokens[0] not in _COMANDOS_PERMITIDOS:
        return f"primeiro token fora da lista fechada {_COMANDOS_PERMITIDOS}"
    return None


def _rodar_comando(comando: str, root: Path) -> tuple[int, str]:
    tokens = shlex.split(comando)
    resultado = subprocess.run(
        tokens,
        cwd=str(root),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return resultado.returncode, (resultado.stdout or "") + (resultado.stderr or "")


def _bate_com_medido(valor_declarado: str, returncode: int, saida: str) -> bool:
    """`Medido antes: exit N` compara com o código de saída; qualquer outro valor é conferido
    como substring literal da saída (stdout + stderr) do comando rodado agora."""
    valor = valor_declarado.strip()
    m = _EXIT_RE.match(valor)
    if m:
        return returncode == int(m.group(1))
    return valor in saida


# --- âncoras de arquivo:linha (FPU-T3, DFP-4/DFP-16): toda âncora `<caminho>:<linha>` (ou
# `<caminho>:<linha>-<fim>`) citada em `Arquivos-alvo` ou `Passos` leva o literal citado logo em
# seguida (separado por "—" ou ":", entre crases), e o literal precisa estar contido (após
# `strip()`) em alguma linha da faixa `linha..fim` do arquivo em `--root`.
_ANCORA_RE = re.compile(r"`(?P<caminho>[^`:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-(?P<fim>\d+))?`")
_LITERAL_APOS_ANCORA_RE = re.compile(r"\s*(?:—|:)\s*`(?P<lit>(?:\\`|[^`\\])+)`")


def conferir_ancoras(dossie, root: Path) -> list[str]:
    """`falhas` (uma linha por âncora que não fecha) — varre as linhas brutas de
    `dossie.campos_linhas["arquivos-alvo"]` e o conteúdo achatado de cada extra de `dossie.extras`
    cujo rótulo, por `rdo._normalizar_rotulo`, é `passos`. Cada ocorrência de `_ANCORA_RE` é
    conferida contra `_LITERAL_APOS_ANCORA_RE` casada logo após a âncora (`.match(texto, m.end())`):
    sem literal ali, a âncora só passa se o mesmo texto de âncora (`m.group(0)`) tiver literal em
    outra ocorrência do card (`âncora sem literal` senão); com literal, o arquivo `root / caminho`
    precisa existir (`alvo inexistente` senão) e o literal precisa estar contido, após `strip()`,
    em alguma linha da faixa `linha..fim` (`literal fora da linha` senão)."""
    rdo = _load_rdo(root)

    textos: list[str] = list((dossie.campos_linhas or {}).get("arquivos-alvo", []))
    for rotulo, conteudo in dossie.extras:
        if rdo._normalizar_rotulo(rotulo) == "passos":
            textos.append(conteudo)

    ocorrencias: list[tuple[re.Match, str | None]] = []
    ancoras_com_literal: set[str] = set()
    for texto in textos:
        for m in _ANCORA_RE.finditer(texto):
            m_lit = _LITERAL_APOS_ANCORA_RE.match(texto, m.end())
            literal = None
            if m_lit:
                literal = m_lit.group("lit").replace("\\`", "`").strip()
                ancoras_com_literal.add(m.group(0))
            ocorrencias.append((m, literal))

    falhas: list[str] = []
    for m, literal in ocorrencias:
        ancora_texto = m.group(0)
        caminho = m.group("caminho")
        linha_ini = int(m.group("linha"))
        linha_fim = int(m.group("fim")) if m.group("fim") else linha_ini

        if literal is None:
            if ancora_texto in ancoras_com_literal:
                continue
            falhas.append(f"âncora sem literal: {ancora_texto}")
            continue

        alvo = root / caminho
        if not alvo.is_file():
            falhas.append(f"alvo inexistente: {caminho}")
            continue

        linhas_alvo = alvo.read_text(encoding="utf-8").splitlines()
        faixa = linhas_alvo[linha_ini - 1 : linha_fim]
        if any(literal in linha.strip() for linha in faixa):
            continue
        linha_real = (
            linhas_alvo[linha_ini - 1].strip() if 0 < linha_ini <= len(linhas_alvo) else ""
        )
        falhas.append(
            f"literal fora da linha: esperado '{literal}' na linha {linha_ini} de '{caminho}', "
            f"linha real '{linha_real}'"
        )

    return falhas


def verificar_tarefa(
    plano: Path, tarefa_id: str, root: Path, mundo: str | None = None
) -> tuple[bool, list[str], dict]:
    """Verbo único da `LM-T5b`/`FPU-T1`/`FPU-T5`: `(ok, falhas, medida)` — `ok` é `True` só quando
    todo item do bloco `Verificação` da tarefa fecha na forma que usa (normativa da `### 8.1` ou
    inline da `DFP-14`) e o comando publicado, rodado agora, bate com o valor declarado para o
    mundo comparado. `falhas` tem uma linha por item que não fechou, nomeando o elemento ausente,
    o comando recusado ou o valor divergente. `medida` (`FPU-T5`, DFP-17) é
    `{"plano": ..., "tarefa": ..., "mundo": ..., "itens": [...]}` — um registro por item de
    `itens` (`_parsear_itens`), com `exit`/`saida`/`bate` preenchidos só quando o comando roda.

    `mundo` em `{"antes", "depois", None}` — só afeta a forma inline (a forma 8.1 sempre compara
    `Medido antes`, qualquer que seja o mundo). `None` deriva do bullet `- **Status:**` do card
    (`rdo._status_atual`): `done` → `depois`; qualquer outro (inclusive ausente) → `antes`. Status
    ausente imprime o aviso `status ausente: comparando antes`."""
    plano_path = Path(plano)
    _exigir_plano(plano_path)

    rdo = _load_rdo(root)
    try:
        dossie = rdo.extrair_dossie(
            plano_path,
            tarefa_id,
            esquema_legado=False,
            modelo_legado=None,
            classe_legado=None,
        )
    except rdo.RdoValidationError as exc:
        raise CardCheckValidationError(str(exc)) from exc

    if mundo is None:
        status = rdo._status_atual(
            plano_path, dossie.tarefa_id, dossie, _caminhos.pasta_do_plano(plano_path)
        )
        if status is None:
            print("status ausente: comparando antes")
            mundo = "antes"
        else:
            mundo = "depois" if status == "done" else "antes"

    linhas_verificacao = (dossie.campos_linhas or {}).get("verificacao", [])
    itens, falhas_forma = _parsear_itens(linhas_verificacao)
    falhas: list[str] = list(falhas_forma)
    if not itens and not falhas_forma:
        falhas.append("verificacao: nenhum item reconhecido (comando em bloco cercado ausente)")

    registros: list[dict] = []
    for item in itens:
        registro = {
            "indice": item.indice,
            "comando": item.comando,
            "exit": None,
            "saida": "",
            "bate": False,
        }
        registros.append(registro)
        if item.forma == "8.1":
            motivo_recusa = _validar_comando(item.comando) if item.comando else None
            comando_executavel = item.comando is not None and motivo_recusa is None

            if item.afericao_manual and comando_executavel:
                falhas.append(
                    f"item {item.indice}: marcador 'Aferição: manual' rejeitado - comando é "
                    "executável (o marcador só vale sobre comando recusado ou ausente)"
                )
                continue

            if item.comando is None and not item.afericao_manual:
                falhas.append(f"item {item.indice}: elemento ausente - comando em bloco cercado")
                continue

            if item.esperado is None:
                falhas.append(f"item {item.indice}: elemento ausente - → (valor esperado)")
            if item.medido_antes is None:
                falhas.append(f"item {item.indice}: elemento ausente - Medido antes")
            if item.esperado is None or item.medido_antes is None:
                continue

            if item.afericao_manual:
                # aceito por (d): comando ausente ou recusado por (c) — reportado como manual,
                # não executado; os elementos 2 e 3 já foram conferidos acima.
                continue

            if motivo_recusa is not None:
                falhas.append(f"item {item.indice}: comando recusado - {motivo_recusa}")
                continue

            returncode, saida = _rodar_comando(item.comando, root)
            bate = _bate_com_medido(item.medido_antes, returncode, saida)
            registro["exit"] = returncode
            registro["saida"] = saida.strip()[-400:]
            registro["bate"] = bate
            if not bate:
                falhas.append(
                    f"item {item.indice}: divergencia - Medido antes declara "
                    f"'{item.medido_antes}', execução mediu exit {returncode} saída "
                    f"'{saida.strip()[:200]}'"
                )
            continue

        # forma inline (DFP-14): sem as checagens de → / Medido antes da 8.1.
        motivo_recusa = (
            _validar_comando(item.comando)
            if item.comando is not None
            else "elemento ausente - comando entre crases"
        )
        comando_executavel = item.comando is not None and motivo_recusa is None

        if item.afericao_manual and comando_executavel:
            falhas.append(
                f"item {item.indice}: marcador 'Aferição: manual' rejeitado - comando é "
                "executável (o marcador só vale sobre comando recusado ou ausente)"
            )
            continue

        tem_par = item.antes is not None and item.depois is not None
        if mundo == "antes":
            if item.antes is None:
                falhas.append(f"item {item.indice}: sem valor antes")
                continue
            valor_do_mundo = item.antes
        else:
            if not tem_par:
                if item.esperado is None:
                    falhas.append(f"item {item.indice}: sem valor esperado")
                    continue
                m_lit = _CRASE_RE.search(item.esperado)
                if m_lit is None:
                    falhas.append(f"item {item.indice}: esperado sem literal")
                    continue
                valor_do_mundo = m_lit.group("val")
            else:
                valor_do_mundo = item.depois

        if item.afericao_manual:
            continue

        if motivo_recusa is not None:
            falhas.append(f"item {item.indice}: comando recusado - {motivo_recusa}")
            continue

        returncode, saida = _rodar_comando(item.comando, root)
        bate = _bate_com_medido(valor_do_mundo, returncode, saida)
        registro["exit"] = returncode
        registro["saida"] = saida.strip()[-400:]
        registro["bate"] = bate
        if not bate:
            falhas.append(
                f"item {item.indice}: divergencia - valor do mundo ({mundo}) declara "
                f"'{valor_do_mundo}', execução mediu exit {returncode} saída "
                f"'{saida.strip()[:200]}'"
            )

    if mundo == "antes":
        falhas.extend(conferir_ancoras(dossie, root))

    medida = {
        "plano": plano_path.as_posix(),
        "tarefa": dossie.tarefa_id,
        "mundo": mundo,
        "itens": registros,
    }
    return (not falhas, falhas, medida)


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    parser = argparse.ArgumentParser(
        description=(
            "Régua de autoria (LM-T5b): afere o bloco Verificação de um card contra a forma "
            "normativa de docs/RUBRICA_DE_REVISAO.md #8.1 e roda cada comando publicado contra "
            "a árvore de teste."
        )
    )
    parser.add_argument("--plano", required=True, type=Path, help="Caminho do .md do plano.")
    parser.add_argument("--tarefa", required=True, help="Identificador da tarefa (ex.: EX-T1).")
    parser.add_argument(
        "--root",
        type=Path,
        default=_default_root(),
        help="Raiz do repositório (onde os comandos publicados rodam).",
    )
    parser.add_argument(
        "--mundo",
        choices=["antes", "depois"],
        default=None,
        help=(
            "Mundo do card a comparar na forma inline (DFP-14); ausente deriva do bullet "
            "- **Status:** (done -> depois; demais -> antes)."
        ),
    )
    parser.add_argument(
        "--gravar",
        nargs="?",
        const=True,
        type=Path,
        default=None,
        help=(
            "Grava a medida (FPU-T5, DFP-17, TK-92a) — com caminho, neste .json; sem caminho, "
            "em caminhos.destino_medida(--root, --plano, --tarefa) — um registro por item de "
            "Verificação, ok ou não; não muda exit, stdout nem stderr."
        ),
    )
    args = parser.parse_args(argv)

    try:
        ok, falhas, medida = verificar_tarefa(args.plano, args.tarefa, args.root, mundo=args.mundo)
    except CardCheckValidationError as exc:
        print(f"card_check: FALHOU - {exc}", file=sys.stderr)
        return 1

    if args.gravar is not None:
        destino = (
            _caminhos.destino_medida(args.root, args.plano, args.tarefa)
            if args.gravar is True
            else args.gravar
        )
        dados = {
            "plano": medida["plano"],
            "tarefa": medida["tarefa"],
            "mundo": medida["mundo"],
            "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "itens": medida["itens"],
        }
        conteudo = json.dumps(dados, ensure_ascii=False, indent=2)
        destino.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(
            dir=str(destino.parent), prefix=".card-check-", suffix=".tmp"
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as tmp_file:
                tmp_file.write(conteudo)
            os.replace(tmp_path, destino)
        except Exception:
            Path(tmp_path).unlink(missing_ok=True)
            raise

    if not ok:
        for linha in falhas:
            print(linha, file=sys.stderr)
        print(
            f"card_check: FALHOU - {len(falhas)} item(ns) da tarefa '{args.tarefa}' não fecham.",
            file=sys.stderr,
        )
        return 1

    print(f"card_check: OK - tarefa '{args.tarefa}' fecha.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
