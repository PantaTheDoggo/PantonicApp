"""AF-T17 (`docs/plans/P-0753-auditoria-estagio-1/plano.md` `### AF-T17`) — o pré-voo do pedido:
`python .claude/tools/prevoo.py "<texto>" [--root <caminho>]` confere, antes da campanha de
planejamento, se cada caminho, símbolo e flag citado no pedido do dono existe de fato na árvore —
premissa do pedido que não existe não deveria virar pergunta ao scout.

Extrai do texto, sem repetir e na ordem da primeira aparição dentro de cada categoria. O texto
se parte em tokens por espaço em branco, e cada token se normaliza antes da classificação (`DAF-45`):
perde, à esquerda, crase, aspas, `*` e abre-parêntese/colchete/chave; à direita, crase, aspas, `*`,
pontuação de frase (`,` `.` `;` `:` `!` `?`) e fecha-parêntese/colchete/chave; flag perde o `=<valor>`.
Assim `` `ler_texto_utf8` ``, `` `.claude/tools/caminhos.py`, ``, `--plano;` e `nome()` citam o mesmo
que `ler_texto_utf8`, `.claude/tools/caminhos.py`, `--plano` e `nome(`.

- **caminhos** — token terminado em `/`; ou com `/` e o último segmento terminado numa extensão
  de 1 a 5 letras ou dígitos; ou, sem `/`, terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`,
  `.txt`, `.yml`, `.yaml` ou `.toml` e não começado por `.` (`R-17` e `DRF-19` do `P-0755`);
  existe (`sim`) quando `(<root> / <token>)` existe, e `onde` é o próprio caminho; o que não
  existe sai `criar` quando a mesma frase (texto entre `. ` ou quebra de linha) o traz depois de
  um verbo de criação (`crie`, `criar`, `grave`, `gravar`, `escreva`, `escrever`, `gere`, `gerar`,
  sem distinção de caixa), e `criar` não derruba o exit 0; o que não existe e o pedido não manda
  criar sai `não` e, como o símbolo e a flag ausentes, faz o exit ser 1.
- **símbolos** — nome seguido de `(` (com ou sem argumentos até o `)`), ou identificador com `_` que não é caminho nem flag; existe
  quando algum `.py` sob `<root>` (fora de `.git` e `__pycache__`) tem a linha `def <nome>(` ou
  `class <nome>`; `onde` é `<arquivo>:<linha>` da primeira ocorrência, com `/`.
- **flags** — token que começa por `-` seguido de letra; existe quando algum `.py` sob
  `<root>/.claude` contém a flag entre aspas (`"<flag>"` ou `'<flag>'`); `onde` é
  `<arquivo>:<linha>` da primeira ocorrência, com `/`.

Só leitura: não escreve em arquivo nenhum, não chama rede. Carregado por
`importlib.util.spec_from_file_location` nos testes (`.claude/` não é pacote importável) — não
importa de `tests` nem de `caminhos` (`tests/conformance/test_camadas_do_kit.py`, AF-T15)."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_EXTENSOES_CAMINHO = (".py", ".md", ".ps1", ".json", ".tsv", ".txt", ".yml", ".yaml", ".toml")
_RE_IDENTIFICADOR = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_ABRE = "`'\"*([{<"
_FECHA = "`'\"*,.;:!?)]}>"


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir acento — mesmo padrão
    de `card_check.py`/`review_evidence.py`, sem import cruzado entre módulos."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def _normalizar(token: str) -> str:
    """Tira de `token` o invólucro da citação — crase, aspas, ênfase, parênteses e pontuação de
    frase nas pontas — e, de flag, o `=<valor>` (`DAF-45`). O ponto inicial de `.claude/` fica: só
    se tira à esquerda o que abre citação ou agrupamento."""
    token = token.lstrip(_ABRE).rstrip(_FECHA)
    if _e_flag(token):
        token = token.split("=", 1)[0]
    return token


_RE_EXTENSAO_CURTA = re.compile(r"\.[A-Za-z0-9]{1,5}$")


def _e_caminho(token: str) -> bool:
    """`R-17` (auditoria reg. 2) e `DRF-19` do `P-0755`: extensão solta sem `/` não é caminho —
    verdadeiro quando `token` termina em `/`; ou quando tem `/` e o último segmento (depois da
    última `/`) casa `_RE_EXTENSAO_CURTA` (qualquer extensão curta, não só as nove conhecidas);
    ou quando não tem `/`, termina numa das nove `_EXTENSOES_CAMINHO` e não começa por `.`."""
    if token.endswith("/"):
        return True
    if "/" in token:
        ultimo_segmento = token.rsplit("/", 1)[1]
        return bool(_RE_EXTENSAO_CURTA.search(ultimo_segmento))
    return token.endswith(_EXTENSOES_CAMINHO) and not token.startswith(".")


def _e_flag(token: str) -> bool:
    sem_traco = token.lstrip("-")
    return token != sem_traco and bool(sem_traco) and sem_traco[0].isalpha()


def _simbolo_de(token: str) -> str | None:
    """Devolve o nome do símbolo citado por `token`, ou `None` se `token` não citar símbolo."""
    if _e_caminho(token) or _e_flag(token):
        return None
    if "(" in token:
        nome = token.split("(", 1)[0]
        return nome if _RE_IDENTIFICADOR.match(nome) else None
    if "_" in token and _RE_IDENTIFICADOR.match(token):
        return token
    return None


def _extrair(texto: str) -> tuple[list[str], list[str], list[str]]:
    """Tokeniza `texto` por espaço em branco, normaliza cada token (`_normalizar`) e separa em
    três listas — caminhos, símbolos, flags —, cada uma na ordem da primeira aparição e sem repetir."""
    caminhos: list[str] = []
    simbolos: list[str] = []
    flags: list[str] = []
    for bruto in texto.split():
        token = _normalizar(bruto)
        if not token:
            continue
        if _e_caminho(token):
            if token not in caminhos:
                caminhos.append(token)
            continue
        if _e_flag(token):
            if token not in flags:
                flags.append(token)
            continue
        simbolo = _simbolo_de(token)
        if simbolo is not None and simbolo not in simbolos:
            simbolos.append(simbolo)
    return caminhos, simbolos, flags


_VERBOS_DE_CRIACAO = {"crie", "criar", "grave", "gravar", "escreva", "escrever", "gere", "gerar"}
_RE_FIM_DE_FRASE = re.compile(r"\. |\n")


def _caminhos_a_criar(texto: str) -> set[str]:
    """Caminhos que o pedido manda criar: `texto` se divide em frases por `_RE_FIM_DE_FRASE`; em
    cada frase, os tokens (normalizados por `_normalizar`) depois do primeiro cujo `lower()` é um
    dos `_VERBOS_DE_CRIACAO` entram no conjunto devolvido quando são caminho por `_e_caminho`."""
    resultado: set[str] = set()
    for frase in _RE_FIM_DE_FRASE.split(texto):
        verbo_visto = False
        for bruto in frase.split():
            token = _normalizar(bruto)
            if not token:
                continue
            if not verbo_visto:
                if token.lower() in _VERBOS_DE_CRIACAO:
                    verbo_visto = True
                continue
            if _e_caminho(token):
                resultado.add(token)
    return resultado


def _achar_simbolo(root: Path, nome: str) -> str | None:
    """Procura `def <nome>(` ou `class <nome>` em todo `.py` sob `root` (fora de `.git` e
    `__pycache__`); devolve `<arquivo>:<linha>` (com `/`) da primeira ocorrência, ou `None`."""
    padrao_def = f"def {nome}("
    padrao_class = re.compile(rf"class {re.escape(nome)}\b")
    for arquivo in sorted(root.rglob("*.py")):
        partes = arquivo.relative_to(root).parts
        if ".git" in partes or "__pycache__" in partes:
            continue
        try:
            linhas = arquivo.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for numero, linha in enumerate(linhas, start=1):
            if padrao_def in linha or padrao_class.search(linha):
                return f"{arquivo.relative_to(root).as_posix()}:{numero}"
    return None


def _achar_flag(root: Path, flag: str) -> str | None:
    """Procura `flag` entre aspas em todo `.py` sob `root / .claude`; devolve `<arquivo>:<linha>`
    (com `/`) da primeira ocorrência, ou `None`."""
    pasta = root / ".claude"
    if not pasta.exists():
        return None
    alvo_dupla = f'"{flag}"'
    alvo_simples = f"'{flag}'"
    for arquivo in sorted(pasta.rglob("*.py")):
        try:
            linhas = arquivo.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for numero, linha in enumerate(linhas, start=1):
            if alvo_dupla in linha or alvo_simples in linha:
                return f"{arquivo.relative_to(root).as_posix()}:{numero}"
    return None


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    parser = argparse.ArgumentParser(prog="prevoo")
    parser.add_argument("texto")
    parser.add_argument("--root", default=None)
    args = parser.parse_args(argv)

    if args.root is not None:
        root = Path(args.root)
    else:
        root = Path(__file__).resolve().parent.parent.parent

    caminhos, simbolos, flags = _extrair(args.texto)

    linhas: list[tuple[str, str, str]] = [("citado", "existe", "onde")]
    tudo_existe = True

    a_criar = _caminhos_a_criar(args.texto)
    for caminho in caminhos:
        existe = (root / caminho).exists()
        if existe:
            linhas.append((caminho, "sim", caminho))
        elif caminho in a_criar:
            linhas.append((caminho, "criar", "—"))
        else:
            tudo_existe = False
            linhas.append((caminho, "não", "—"))

    for simbolo in simbolos:
        onde = _achar_simbolo(root, simbolo)
        tudo_existe = tudo_existe and onde is not None
        linhas.append((simbolo, "sim" if onde is not None else "não", onde or "—"))

    for flag in flags:
        onde = _achar_flag(root, flag)
        tudo_existe = tudo_existe and onde is not None
        linhas.append((flag, "sim" if onde is not None else "não", onde or "—"))

    for citado, existe, onde in linhas:
        print(f"{citado} | {existe} | {onde}")

    return 0 if tudo_existe else 1


if __name__ == "__main__":
    sys.exit(main())
