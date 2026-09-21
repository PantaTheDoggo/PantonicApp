"""EXA-T19 (`docs/plans/P-0734-execucao-autonoma.md` `### T19`) — o RDO deixa de ser aberto no
início e passa a ser **gerado no fechamento**: `python .claude/tools/rdo.py close --plano
<caminho.md> --tarefa <ID> --tool-uses <N> --tokens-k <N> --duracao-s <N> --veredito
<aprovado|ressalva> --percentual <N> --bloqueante <dimensão|nenhuma> --recomendacao "<uma linha>"
--pendencia-laudo "<uma linha|nenhuma>" [--pendencia "<uma linha>"] [--rdo-dir] [--template]
[--esquema-legado --modelo --classe]` localiza o cabeçalho da tarefa no `.md` do plano pela
gramática fixa da `DP-C` (`extrair_dossie`, reusada também por `review_evidence.py` — não remover),
**transcreve** — sem recalcular — o `pacote` do laudo (veredito/percentual/bloqueante/recomendação/
pendência-do-laudo) e o consumo medido, **calcula** o desdobramento pela tabela de dois ramos de
`calcular_desdobramento` e materializa o documento a partir de `.claude/tools/rdo_template.md`
numa única escrita atômica — o formato do RDO vive no template, não em nenhum prompt de agente.

O RDO é escrito por uma única transição (`review` → `done`, `DP-F`/`DP-E`): tarefa `cancelled` ou
`blocked` não produz RDO, então `close` não tem `--status` e não lê `status` de lugar nenhum. O
laudo é documento **consumido e descartado** pelo `scrum-master` (`DP-H`) — `close` não abre
arquivo de laudo nenhum e não conhece `--laudos-dir`; o template não pendura ponteiro para um
documento que já não existe.

Plano legado (cabeçalho sem colchete algum — a gramática fixa da `DX-15` é `### <ID> — <título>
[<modelo> · classe <classe>]`, com o segmento histórico ` · teto <N>` aceito e descartado sem
flag nenhuma): `--esquema-legado` com `--modelo`/`--classe` explícitos é o único caminho para
prosseguir (política de plano legado da `DP-C`, item 3) — o RDO registra `esquema=legado`.

`laudo` (EXA-T8b/T18, estendido pela `BKL-T2d` do `P-0739`): `python .claude/tools/rdo.py laudo --plano
<id> --tarefa <id> [--laudos-dir <dir>] --<dimensao> <nivel> ...` (as sete dimensões de
`docs/RUBRICA_DE_REVISAO.md` §4, na ordem canônica de §5) **calcula** percentual, veredito,
dimensão bloqueante e recomendação de domínio fechado (`seguir` | `seguir com ressalva` | `refazer`
| `escalar`) pela fórmula de §5 e pela tabela de recomendação da `T18` — nunca aceitos como
argumento (`DA-6`) — e grava documento próprio em `docs/RDO/laudos/<plano>-<tarefa>.md`, criando o
diretório se preciso. `--vermelho-mecanico <dimensao>` (repetível) declara o que a camada mecânica
já reportou vermelho; marcar `conforme` contra uma dimensão declarada vermelha é recusado (`DA-7`).
`--escalar "<uma linha>"` força `recomendacao=escalar` independentemente da tabela, e a linha
gravada é a pendência que a regra `B1` consome. `--achado-processo <alvo> "<uma linha>"`
(repetível; alvo em `dossie`, `doutrina`, `rubrica` ou `modelo`) grava a seção `## Achado de processo` e
**não** altera percentual, veredito, bloqueante nem recomendação — invariante 1 de
`docs/RUBRICA_DE_REVISAO.md` §6; `--escalar` fica reservado ao achado que invalida a rota (decisão
de arquitetura ou de requisito).

Escrita atômica (arquivo temporário no mesmo diretório de destino + `os.replace`) e falha ruidosa
(exit != 0, mensagem em stderr, nada escrito) no mesmo padrão de `.claude/tools/telemetria.py`."""
from __future__ import annotations

import argparse
import math
import os
import re
import sys
import tempfile
import unicodedata
from fractions import Fraction
from pathlib import Path

_MODELOS = {"Opus", "Sonnet", "Haiku"}

# Conjunto normativo de classes (`DP-C`) — usado nas mensagens de erro (`sorted(...)`) para nomear
# o domínio aceito. Os valores eram teto default por classe; a régua de teto agora é exclusiva do
# planejador em `GOVERNANCA.md` §3 — este módulo não os lê mais (`DX-15`, `CTX-T1d`).
_CLASSE_TETO_DEFAULT: dict[str, int | None] = {
    "mecanica": 15,
    "implementacao": 40,
    "comportamental": 60,
    "investigacao": None,
    "redacao": 30,
}

# Chave: grafia normalizada (sem acento, minúscula) medida no corpus de planos -> slug normativo.
# `DP-C` fixa os cinco slugs; os planos anteriores à decisão (este incluído) escrevem a linha de
# `GOVERNANCA.md` §3 por extenso, em mais de uma grafia (achado registrado no próprio plano).
_CLASSE_ALIASES: dict[str, str] = {
    "mecanica": "mecanica",
    "mecanica / pontual": "mecanica",
    "implementacao": "implementacao",
    "implementacao padrao": "implementacao",
    "comportamental": "comportamental",
    "comportamental multi-camada": "comportamental",
    "investigacao": "investigacao",
    "investigacao / mapeamento": "investigacao",
    "redacao": "redacao",
    "redacao de doutrina / planejamento": "redacao",
    "redacao de doutrina": "redacao",
    "redacao/planejamento": "redacao",
}

_ID_HEADER_RE = re.compile(
    r"^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?|TK-[0-9]+[a-z]?)(?=[\s—])"
)
_ID_LAUDO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")  # identificador, nunca caminho
_HEADER_BRACKET_RE = re.compile(
    r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?|TK-[0-9]+[a-z]?) — (?P<titulo>.+?) "
    r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)?"
    r"(?: · esforço (?:low|medium|high|xhigh|max))?"
    r" · classe (?P<classe>.+?)"
    r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"
)
_HEADER_LEGADO_TITULO_FMT = r"^### {id} — (?P<titulo>.+)$"
_SECTION_BREAK_RE = re.compile(r"^#{2,3} ")
_CAMPO_RE = re.compile(r"^- \*\*(?P<label>.+?):\*\*\s?(?P<content>.*)$")

_CAMPOS_CANONICOS = {
    "objetivo",
    "arquivos-alvo",
    "entregavel",
    "verificacao",
    "pronto-quando",
    "dossie-fechado-por",
}


class RdoValidationError(ValueError):
    """Dossiê ou argumento inválido (mensagem já nomeia o campo/identificador)."""


def _validar_inteiro_nao_negativo(nome: str, valor: str) -> int:
    """Guarda de domínio de `tool_uses` (`P-0740` `LM-T1a`, `DM-15`). Mesmo vocabulário de recusa
    de `telemetria.py` (`_validar_inteiro_nao_negativo`), duplicado aqui — sem import cruzado
    entre os dois módulos (`DM-11`)."""
    try:
        numero = int(valor)
    except ValueError as exc:
        raise RdoValidationError(f"{nome}: '{valor}' não é inteiro") from exc
    if numero < 0:
        raise RdoValidationError(f"{nome}: '{valor}' é negativo")
    return numero


def _validar_numero_nao_negativo_finito(nome: str, valor: str) -> float:
    """Guarda de domínio de `tokens_k`/`duracao_s` (`P-0740` `LM-T1a`, `DM-15`) — os dois campos
    compartilham este validador. Mesmo vocabulário de recusa de `telemetria.py`
    (`_validar_numero_nao_negativo`), duplicado aqui — sem import cruzado entre os dois módulos
    (`DM-11`)."""
    try:
        numero = float(valor)
    except ValueError as exc:
        raise RdoValidationError(f"{nome}: '{valor}' não é numérico") from exc
    if not math.isfinite(numero):
        raise RdoValidationError(f"{nome}: '{valor}' não é finito")
    if numero < 0:
        raise RdoValidationError(f"{nome}: '{valor}' é negativo")
    return numero


class DossieTarefa:
    """Dossiê da tarefa extraído do plano pela gramática da `DP-C`. Classe simples (não
    `@dataclass`) de propósito: carregar este módulo por caminho via
    `importlib.util.spec_from_file_location` sem registrar em `sys.modules` quebra a resolução
    de anotações adiadas (`from __future__ import annotations`) que `dataclasses` faz na
    definição da classe — evitado ficando fora do mecanismo de dataclass."""

    def __init__(self, tarefa_id, titulo, modelo, classe, esquema, campos, extras):
        self.tarefa_id = tarefa_id
        self.titulo = titulo
        self.modelo = modelo
        self.classe = classe
        self.esquema = esquema  # "padrao" | "legado"
        self.campos = campos
        self.extras = extras


def _remover_acentos(texto: str) -> str:
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def _normalizar_classe(bruto: str) -> str | None:
    chave = re.sub(r"\s+", " ", _remover_acentos(bruto.strip().lower()))
    return _CLASSE_ALIASES.get(chave)


def _normalizar_rotulo(rotulo: str) -> str:
    """Gramática de campo da `DP-C`: recorta antes do primeiro ' — ', ',' ou '(', minusculiza,
    remove acentos e troca espaço por hífen."""
    texto = rotulo
    for sep in (" — ", ",", "("):
        idx = texto.find(sep)
        if idx != -1:
            texto = texto[:idx]
    texto = _remover_acentos(texto.strip().lower())
    return texto.replace(" ", "-")


def _slugify(titulo: str) -> str:
    texto = titulo.replace("`", "")
    texto = _remover_acentos(texto).lower()
    texto = re.sub(r"[^a-z0-9]+", "-", texto).strip("-")
    texto = re.sub(r"-+", "-", texto)
    return texto[:60].rstrip("-")


def _parsear_campos(linhas: list[str]) -> tuple[dict[str, str], list[list[str]]]:
    """Extrai os campos canônicos (`_CAMPOS_CANONICOS`) e os extras de um bloco de card.

    Regra de fim de campo (`AE-27` item 2, caso `LM-T2b`): um **bullet de topo** encerra o campo
    corrente, case ele `_CAMPO_RE` (campo canônico) ou não. Antes deste reparo, só um bullet que
    casasse `_CAMPO_RE` encerrava o campo — um bullet de prosa cujo rótulo não termina em `:**`
    (ex.: `- **A calibração medida no \\`ESC-3\\`... — residência única desta tabela.**`) não
    encerrava nada, e todas as linhas indentadas seguintes (uma tabela inteira, no caso medido)
    continuavam sendo anexadas ao campo canônico anterior. Linha indentada continua alimentando
    o campo corrente, como sempre — só o bullet de topo fecha.
    """
    campos: dict[str, str] = {}
    extras: list[list[str]] = []
    chave_atual: str | None = None
    em_extra = False

    for linha in linhas:
        m = _CAMPO_RE.match(linha)
        if m:
            rotulo = m.group("label").strip()
            conteudo = m.group("content").strip()
            chave = _normalizar_rotulo(rotulo)
            if chave in _CAMPOS_CANONICOS:
                campos[chave] = conteudo
                chave_atual = chave
                em_extra = False
            else:
                extras.append([rotulo, conteudo])
                chave_atual = None
                em_extra = True
            continue
        if not linha.strip():
            continue
        if linha[:1] in (" ", "\t"):
            texto = linha.strip()
            if em_extra and extras:
                extras[-1][1] = (extras[-1][1] + " " + texto).strip()
            elif chave_atual is not None:
                campos[chave_atual] = (campos[chave_atual] + " " + texto).strip()
            continue
        if linha.startswith("- "):
            # Bullet de topo que não casa `_CAMPO_RE` (rótulo sem ':**'): encerra o campo
            # corrente do mesmo jeito que um campo canônico encerraria (AE-27 item 2).
            chave_atual = None
            em_extra = False
            continue
        # linha sem indentação que não é campo novo nem bullet de topo: fora da gramática,
        # ignorada.

    return campos, extras


def extrair_dossie(
    plano_path: Path,
    tarefa_id: str,
    *,
    esquema_legado: bool,
    modelo_legado: str | None,
    classe_legado: str | None,
) -> DossieTarefa:
    linhas = plano_path.read_text(encoding="utf-8").splitlines()

    header_idx = None
    for i, linha in enumerate(linhas):
        m = _ID_HEADER_RE.match(linha)
        if m and m.group(1) == tarefa_id:
            header_idx = i
            break
    if header_idx is None:
        raise RdoValidationError(f"tarefa: '{tarefa_id}' não encontrada em '{plano_path}'")

    header_linha = linhas[header_idx]
    bracket = _HEADER_BRACKET_RE.match(header_linha)

    if bracket:
        titulo = bracket.group("titulo").strip()
        classe_raw = bracket.group("classe")
        classe = _normalizar_classe(classe_raw)
        if classe is None:
            raise RdoValidationError(
                f"classe: '{classe_raw}' fora do conjunto {sorted(_CLASSE_TETO_DEFAULT)} "
                f"(cabeçalho de '{tarefa_id}')"
            )
        modelo = bracket.group("modelo")
        esquema = "padrao"
    else:
        titulo_padrao = _HEADER_LEGADO_TITULO_FMT.format(id=re.escape(tarefa_id))
        titulo_m = re.match(titulo_padrao, header_linha)
        titulo = titulo_m.group("titulo").strip() if titulo_m else header_linha
        faltando = [
            nome
            for nome, valor in (
                ("--esquema-legado", esquema_legado),
                ("--modelo", modelo_legado),
                ("--classe", classe_legado),
            )
            if not valor
        ]
        if faltando:
            raise RdoValidationError(
                f"cabeçalho de '{tarefa_id}' não declara modelo/classe (plano legado) — "
                f"faltando: {', '.join(faltando)}"
            )
        if modelo_legado not in _MODELOS:
            raise RdoValidationError(f"modelo: '{modelo_legado}' fora do conjunto {sorted(_MODELOS)}")
        classe = _normalizar_classe(classe_legado)
        if classe is None:
            raise RdoValidationError(
                f"classe: '{classe_legado}' fora do conjunto {sorted(_CLASSE_TETO_DEFAULT)}"
            )
        modelo = modelo_legado
        esquema = "legado"

    fim_idx = len(linhas)
    for j in range(header_idx + 1, len(linhas)):
        if _SECTION_BREAK_RE.match(linhas[j]):
            fim_idx = j
            break
    campos, extras_brutos = _parsear_campos(linhas[header_idx + 1 : fim_idx])

    for obrigatorio in ("objetivo", "verificacao", "pronto-quando"):
        if not campos.get(obrigatorio, "").strip():
            raise RdoValidationError(f"campo obrigatório ausente em '{tarefa_id}': '{obrigatorio}'")

    tem_arquivos = bool(campos.get("arquivos-alvo", "").strip())
    tem_entregavel = bool(campos.get("entregavel", "").strip())
    if tem_arquivos == tem_entregavel:
        estado = "os dois" if tem_arquivos else "nenhum"
        raise RdoValidationError(
            f"'{tarefa_id}' precisa de exatamente um entre 'Arquivos-alvo' e 'Entregável' "
            f"(tem {estado})"
        )

    return DossieTarefa(
        tarefa_id=tarefa_id,
        titulo=titulo,
        modelo=modelo,
        classe=classe,
        esquema=esquema,
        campos=campos,
        extras=[(rotulo, conteudo) for rotulo, conteudo in extras_brutos],
    )


def _render(template_texto: str, mapping: dict[str, str]) -> str:
    texto = template_texto
    for chave, valor in mapping.items():
        texto = texto.replace("{{" + chave + "}}", valor)
    return texto


def _default_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _default_rdo_dir() -> Path:
    return _default_root() / "docs" / "RDO"


def _default_template_path() -> Path:
    return Path(__file__).resolve().parent / "rdo_template.md"


def _default_laudos_dir() -> Path:
    return _default_rdo_dir() / "laudos"


# --- laudo (T8b/T18) — cópia fiel de `docs/RUBRICA_DE_REVISAO.md` §4/§5, nunca reinterpretada ---

# Ordem canônica (§5): usada para o cálculo, para a tabela gravada e para escolher a primeira
# bloqueante quando há mais de uma vermelha.
_DIMENSOES_ORDEM = (
    "criterio-de-pronto",
    "escopo",
    "testes",
    "guardas",
    "rota",
    "residuo",
    "registro",
)
_PESO: dict[str, int] = {
    "criterio-de-pronto": 3,
    "escopo": 2,
    "testes": 3,
    "guardas": 3,
    "rota": 2,
    "residuo": 2,
    "registro": 2,
}
_BLOQUEANTE_DIM: dict[str, bool] = {
    "criterio-de-pronto": True,
    "escopo": True,
    "testes": True,
    "guardas": True,
    "rota": True,
    "residuo": False,
    "registro": False,
}
_ADMITE_NAO_SE_APLICA: dict[str, bool] = {
    "criterio-de-pronto": False,
    "escopo": True,
    "testes": True,
    "guardas": False,
    "rota": False,
    "residuo": True,
    "registro": False,
}
_NIVEIS_VALIDOS = ("conforme", "parcial", "nao-conforme", "nao-se-aplica")
_VALOR_NIVEL: dict[str, Fraction] = {
    "conforme": Fraction(1),
    "parcial": Fraction(1, 2),
    "nao-conforme": Fraction(0),
}

_RECOMENDACOES_VALIDAS = ("seguir", "seguir com ressalva", "refazer", "escalar")


class LaudoResultado:
    """Saída fechada pelo domínio de `RUBRICA_DE_REVISAO.md` §1: `percentual` inteiro,
    `veredito` ∈ {aprovado, ressalva, reprovado}, `bloqueante` = nome de dimensão ou 'nenhuma'.
    `recomendacao` (EXA-T18) ∈ `_RECOMENDACOES_VALIDAS` — calculada, nunca aceita como argumento
    (mesma regra que `DA-6` impõe a percentual/veredito); `pendencia` é a linha de `--escalar`
    quando a recomendação é `escalar`, senão `nenhuma`. Classe simples (não `@dataclass`), mesmo
    motivo de `DossieTarefa`."""

    def __init__(
        self,
        percentual: int,
        veredito: str,
        bloqueante: str,
        niveis: dict[str, str],
        recomendacao: str,
        pendencia: str,
    ):
        self.percentual = percentual
        self.veredito = veredito
        self.bloqueante = bloqueante
        self.niveis = niveis
        self.recomendacao = recomendacao
        self.pendencia = pendencia


def _arredondar_meio_para_cima(fracao: Fraction) -> int:
    """Arredondamento de metade para cima (§5), sobre `Fraction` exata — nunca `round()` do
    Python, que arredonda meio-para-par e divergiria da rubrica em caso de empate."""
    piso = fracao.numerator // fracao.denominator
    resto = fracao - piso
    if resto * 2 >= 1:
        return piso + 1
    return piso


def calcular_laudo(
    niveis: dict[str, str], vermelhos_mecanicos: set[str], escalar: str | None = None
) -> LaudoResultado:
    for dimensao in _DIMENSOES_ORDEM:
        if dimensao not in niveis:
            raise RdoValidationError(f"dimensão obrigatória ausente: '{dimensao}'")
        nivel = niveis[dimensao]
        if nivel not in _NIVEIS_VALIDOS:
            raise RdoValidationError(f"nível inválido para '{dimensao}': '{nivel}'")
        if nivel == "nao-se-aplica" and not _ADMITE_NAO_SE_APLICA[dimensao]:
            raise RdoValidationError(
                f"dimensão '{dimensao}' não admite nível 'nao-se-aplica' (RUBRICA_DE_REVISAO §5)"
            )
        if nivel == "conforme" and dimensao in vermelhos_mecanicos:
            raise RdoValidationError(
                f"dimensão '{dimensao}' marcada 'conforme' contra vermelho mecânico — recusado (DA-7)"
            )

    aplicaveis = [d for d in _DIMENSOES_ORDEM if niveis[d] != "nao-se-aplica"]
    numerador: Fraction = sum(
        (_PESO[d] * _VALOR_NIVEL[niveis[d]] for d in aplicaveis), Fraction(0)
    )
    denominador = sum(_PESO[d] for d in aplicaveis)
    percentual = _arredondar_meio_para_cima(Fraction(100) * numerador / denominador)

    vermelhas = [
        d for d in _DIMENSOES_ORDEM
        if d in aplicaveis and _BLOQUEANTE_DIM[d] and niveis[d] == "nao-conforme"
    ]
    if vermelhas:
        bloqueante = vermelhas[0]
        veredito = "reprovado"
    else:
        bloqueante = "nenhuma"
        if percentual >= 95:
            veredito = "aprovado"
        elif percentual >= 70:
            veredito = "ressalva"
        else:
            veredito = "reprovado"

    escalar_linha = escalar.strip() if escalar else None
    if escalar_linha:
        recomendacao = "escalar"
        pendencia = escalar_linha
    else:
        pendencia = "nenhuma"
        if veredito == "reprovado":
            recomendacao = "refazer"
        elif veredito == "ressalva":
            recomendacao = "seguir com ressalva"
        else:
            recomendacao = "seguir"

    return LaudoResultado(
        percentual=percentual,
        veredito=veredito,
        bloqueante=bloqueante,
        niveis=dict(niveis),
        recomendacao=recomendacao,
        pendencia=pendencia,
    )


_ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo"}


def _formatar_achados_processo(pares: list[list[str]] | None) -> str:
    """`docs/RUBRICA_DE_REVISAO.md` §6: campo próprio, quatro alvos. Invariante 1 — o achado não
    rebaixa dimensão de entrega e não muda recomendação; por isso nada disto passa por
    `calcular_laudo`. Sem achado, o corpo é `nenhum` (a seção existe sempre)."""
    if not pares:
        return "nenhum"
    linhas = ["| alvo | achado |", "|---|---|"]
    for alvo, texto in pares:
        linhas.append(f"| {_ALVOS_ACHADO[alvo]} | {texto.strip()} |")
    return "\n".join(linhas)


def cmd_laudo(args: argparse.Namespace) -> Path:
    """EXA-T18: laudo grava documento próprio em `docs/RDO/laudos/<plano>-<tarefa>.md` — não
    depende de RDO nenhum aberto, e o `close` (EXA-T19) não o lê: o `pacote` chega a `close` por
    argumento, de quem consumiu este documento."""
    for flag, valor in (("--plano", args.plano), ("--tarefa", args.tarefa)):
        if not _ID_LAUDO_RE.fullmatch(valor):
            raise RdoValidationError(
                f"{flag} é identificador (ex.: P-0734, T18), não caminho: {valor!r}. "
                "Laudo de sonda vai para --laudos-dir <scratchpad>."
            )
    for alvo, texto in (args.achado_processo or []):
        if alvo not in _ALVOS_ACHADO:
            raise RdoValidationError(
                f"--achado-processo: alvo '{alvo}' fora de {sorted(_ALVOS_ACHADO)} "
                "(RUBRICA_DE_REVISAO.md §6)"
            )
        if not texto.strip():
            raise RdoValidationError("--achado-processo: a linha do achado não pode ser vazia")
        if "|" in texto or "\n" in texto:
            raise RdoValidationError(
                "--achado-processo: uma linha, sem '|' — a tabela do laudo quebraria"
            )
    niveis = {d: getattr(args, d.replace("-", "_")) for d in _DIMENSOES_ORDEM}
    vermelhos = set(args.vermelho_mecanico or [])

    resultado = calcular_laudo(niveis, vermelhos, escalar=args.escalar)

    laudos_dir = Path(args.laudos_dir) if args.laudos_dir is not None else _default_laudos_dir()
    destino = laudos_dir / f"{args.plano}-{args.tarefa}.md"

    tabela_niveis = "\n".join(f"| {d} | {niveis[d]} |" for d in _DIMENSOES_ORDEM)

    # Card "Lições aprendidas na tarefa" (`DP-Q` §21 item 3 do `P-0734`): residência do registro
    # qualitativo, discricionário — o reviewer preenche só quando enxergar algo. Vazio é estado
    # legítimo, não defeito: sem `--licoes-aprendidas`, o card existe (heading) com corpo vazio,
    # nunca um placeholder forçado tipo "nenhuma".
    licoes_aprendidas = (args.licoes_aprendidas or "").strip()

    conteudo_final = (
        f"# Laudo — {args.plano} · {args.tarefa}\n\n"
        f"**Percentual:** {resultado.percentual}%\n"
        f"**Veredito:** {resultado.veredito}\n"
        f"**Dimensão bloqueante:** {resultado.bloqueante}\n"
        f"**Recomendação:** {resultado.recomendacao}\n"
        f"**Pendência:** {resultado.pendencia}\n\n"
        "| dimensão | nível |\n"
        "|---|---|\n"
        f"{tabela_niveis}\n\n"
        "## Achado de processo\n\n"
        f"{_formatar_achados_processo(args.achado_processo)}\n\n"
        "## Lições aprendidas na tarefa\n\n"
        f"{licoes_aprendidas}\n"
    )

    laudos_dir.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(laudos_dir), prefix=".rdo-laudo-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as tmp_file:
            tmp_file.write(conteudo_final)
        os.replace(tmp_path, destino)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise

    return destino


# --- close (EXA-T19) — o RDO nasce inteiro no fechamento, desdobramento calculado ---------------

_TITULO_RDO_RE = re.compile(r"^# RDO — (?P<plano>\S+) · (?P<tarefa>\S+)\s*$", re.MULTILINE)
_DESDOBRAMENTO_RE = re.compile(r"(?m)^\*\*Desdobramento:\*\* (?P<valor>.+?)\s*$")

_INDICE_NOME = "INDEX.md"


def _contar_linhas(valor: str) -> int:
    return valor.count("\n") + 1 if valor.strip() else 0


def calcular_desdobramento(veredito: str) -> str:
    """Tabela de dois ramos por veredito (`T19` item c, fecha o `TK-29`): o RDO só nasce na
    transição `review` → `done` (`DP-F`), então `bloqueado`/`reprovado` nunca chegam a `close` —
    ramo morto testado é o que o `G-DEADCODE` proíbe, por isso não existem aqui. O terceiro ramo
    que existia por estouro de consumo caiu pela `DP-Q` (§21 do plano `P-0734`): nenhum limite
    numérico governa fluxo — consumo é medido e registrado (`TOOL_USES` no documento), nunca
    decide o desdobramento."""
    if veredito == "ressalva":
        return "aprovado com ressalva"
    if veredito == "aprovado":
        return "aprovado"
    raise RdoValidationError(f"veredito inesperado: '{veredito}'")


def _status_rdo(conteudo: str) -> str:
    m = _DESDOBRAMENTO_RE.search(conteudo)
    return m.group("valor") if m else "aberto"


def _regenerar_indice(rdo_dir: Path) -> Path:
    """Gerado por varredura do diretório (nunca redigido nem apendado às cegas) — ignora
    `INDEX.md` (a si mesmo) e qualquer arquivo que não seja `.md` (`.gitkeep` incluído, nunca
    tocado). Escrita atômica no mesmo padrão de `cmd_laudo`/`cmd_close`."""
    arquivos = sorted(p for p in rdo_dir.glob("*.md") if p.name != _INDICE_NOME)

    linhas_tabela = []
    for arquivo in arquivos:
        conteudo = arquivo.read_text(encoding="utf-8")
        titulo_m = _TITULO_RDO_RE.search(conteudo)
        plano = titulo_m.group("plano") if titulo_m else "?"
        tarefa = titulo_m.group("tarefa") if titulo_m else "?"
        status = _status_rdo(conteudo)
        linhas_tabela.append(f"| {arquivo.name} | {plano} | {tarefa} | {status} |")

    corpo_tabela = "\n".join(linhas_tabela) if linhas_tabela else "| (nenhum RDO ainda) | | | |"
    conteudo_indice = (
        "# Índice de RDO\n\n"
        "*(Gerado por `python .claude/tools/rdo.py close` — varredura do diretório, nunca "
        "edição manual.)*\n\n"
        "| arquivo | plano | tarefa | status |\n"
        "|---|---|---|---|\n"
        f"{corpo_tabela}\n"
    )

    indice_path = rdo_dir / _INDICE_NOME
    fd, tmp_path = tempfile.mkstemp(dir=str(rdo_dir), prefix=".rdo-indice-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as tmp_file:
            tmp_file.write(conteudo_indice)
        os.replace(tmp_path, indice_path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise
    return indice_path


def cmd_close(args: argparse.Namespace) -> Path:
    # Guarda de domínio do consumo (`P-0740` `LM-T1a`, `DM-15` (iii)) — corre antes de qualquer
    # outra checagem de `cmd_close`, `--plano` incluso: nada é lido nem escrito se um dos três
    # campos estiver fora do domínio.
    tool_uses = _validar_inteiro_nao_negativo("tool_uses", args.tool_uses)
    tokens_k = _validar_numero_nao_negativo_finito("tokens_k", args.tokens_k)
    duracao_s = _validar_numero_nao_negativo_finito("duracao_s", args.duracao_s)

    plano_path = Path(args.plano)
    if not plano_path.is_file():
        raise RdoValidationError(f"plano: arquivo não encontrado '{plano_path}'")

    dossie = extrair_dossie(
        plano_path,
        args.tarefa,
        esquema_legado=args.esquema_legado,
        modelo_legado=args.modelo,
        classe_legado=args.classe,
    )

    template_path = args.template if args.template is not None else _default_template_path()
    if not template_path.is_file():
        raise RdoValidationError(f"template: arquivo não encontrado '{template_path}'")
    template_texto = template_path.read_text(encoding="utf-8")

    plano_id_match = re.match(r"^(P-\d{4})", plano_path.stem)
    plano_id = plano_id_match.group(1) if plano_id_match else plano_path.stem
    nome_arquivo = f"{plano_id}-{dossie.tarefa_id}-{_slugify(dossie.titulo)}.md"

    rdo_dir = Path(args.rdo_dir) if args.rdo_dir is not None else _default_rdo_dir()
    destino = rdo_dir / nome_arquivo
    if destino.exists():
        raise RdoValidationError(f"rdo: '{destino}' já existe — tarefa já fechada")

    for nome_campo, valor in (
        ("recomendacao", args.recomendacao),
        ("pendencia_laudo", args.pendencia_laudo),
        ("pendencia", args.pendencia),
    ):
        if valor is not None and _contar_linhas(valor) > 1:
            raise RdoValidationError(f"{nome_campo}: aceita no máximo uma linha")

    # Consumo (`tool_uses`/`tokens_k`/`duracao_s`, validados no topo desta função) é medido e vai
    # para o documento via TOOL_USES/TOKENS_K/DURACAO_S no `mapping` abaixo — não decide o
    # desdobramento (`DP-Q`, §21 do `P-0734`).
    desdobramento = calcular_desdobramento(args.veredito)

    linhas_pendencia = []
    if args.pendencia:
        linhas_pendencia.append(f"executor: {args.pendencia}")
    if args.pendencia_laudo != "nenhuma":
        linhas_pendencia.append(f"laudo: {args.pendencia_laudo}")
    pendencia_final = "\n".join(linhas_pendencia) if linhas_pendencia else "nenhuma"

    arquivos_label = "Arquivos-alvo" if dossie.campos.get("arquivos-alvo", "").strip() else "Entregável"
    arquivos_conteudo = dossie.campos.get("arquivos-alvo") or dossie.campos.get("entregavel") or ""

    extras_bloco = (
        "\n".join(f"- **{rotulo}:** {conteudo}" for rotulo, conteudo in dossie.extras)
        if dossie.extras
        else "nenhum"
    )

    mapping = {
        "PLANO_ID": plano_id,
        "PLANO_PATH": str(args.plano),
        "TAREFA_ID": dossie.tarefa_id,
        "TITULO": dossie.titulo,
        "MODELO": dossie.modelo,
        "CLASSE": dossie.classe,
        "ESQUEMA": dossie.esquema,
        "OBJETIVO": dossie.campos["objetivo"],
        "ARQUIVOS_LABEL": arquivos_label,
        "ARQUIVOS_CONTEUDO": arquivos_conteudo,
        "VERIFICACAO": dossie.campos["verificacao"],
        "PRONTO_QUANDO": dossie.campos["pronto-quando"],
        "DOSSIE_FECHADO_POR": dossie.campos.get("dossie-fechado-por") or "nenhum",
        "EXTRAS": extras_bloco,
        "TOOL_USES": str(tool_uses),
        "TOKENS_K": f"{tokens_k:.1f}",
        "DURACAO_S": f"{duracao_s:.1f}",
        "PENDENCIA": pendencia_final,
        "VEREDITO": args.veredito,
        "PERCENTUAL": str(args.percentual),
        "BLOQUEANTE": args.bloqueante,
        "RECOMENDACAO": args.recomendacao,
        "LICOES_APRENDIDAS": (args.licoes_aprendidas or "").strip(),
        "DESDOBRAMENTO": desdobramento,
    }
    conteudo_final = _render(template_texto, mapping)

    rdo_dir.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(rdo_dir), prefix=".rdo-close-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as tmp_file:
            tmp_file.write(conteudo_final)
        os.replace(tmp_path, destino)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise

    _regenerar_indice(rdo_dir)

    return destino


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="RDO da tarefa gerado por função, no fechamento — não por redação (EXA-T19)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    laudo_parser = subparsers.add_parser(
        "laudo",
        help="Calcula o laudo e grava documento próprio em docs/RDO/laudos/<plano>-<tarefa>.md (T18).",
    )
    laudo_parser.add_argument("--plano", required=True, help="Identificador do plano (ex.: P-0734).")
    laudo_parser.add_argument("--tarefa", required=True, help="Identificador da tarefa (ex.: T18).")
    laudo_parser.add_argument(
        "--laudos-dir", default=None, help="Diretório de saída (default: docs/RDO/laudos)."
    )
    for _dimensao in _DIMENSOES_ORDEM:
        laudo_parser.add_argument(
            f"--{_dimensao}",
            required=True,
            choices=_NIVEIS_VALIDOS,
            help=f"Nível da dimensão '{_dimensao}' (RUBRICA_DE_REVISAO.md §4).",
        )
    laudo_parser.add_argument(
        "--vermelho-mecanico",
        action="append",
        choices=_DIMENSOES_ORDEM,
        default=None,
        help="Dimensão já reportada vermelha pela camada mecânica (repetível); aplica DA-7.",
    )
    laudo_parser.add_argument(
        "--escalar",
        default=None,
        help=(
            "Uma linha de pendência; se presente, a recomendação é 'escalar' independentemente "
            "da tabela de veredito (dominante)."
        ),
    )
    laudo_parser.add_argument(
        "--achado-processo",
        dest="achado_processo",
        nargs=2,
        action="append",
        metavar=("ALVO", "LINHA"),
        default=None,
        help=(
            "Achado de processo (repetivel): ALVO e dossie, doutrina, rubrica ou modelo, seguido de uma "
            "linha. Nao altera percentual, veredito, bloqueante nem recomendacao (RUBRICA §6)."
        ),
    )
    laudo_parser.add_argument(
        "--licoes-aprendidas",
        dest="licoes_aprendidas",
        default=None,
        help=(
            "Card 'Lições aprendidas na tarefa' (`DP-Q` §21 item 3, `GOVERNANCA.md` §3): "
            "discricionário — preencher só quando houver o que observar; ausência é legítima."
        ),
    )

    close_parser = subparsers.add_parser(
        "close",
        help="Gera o RDO inteiro no fechamento: dossiê do plano + pacote do laudo + consumo (T19).",
    )
    close_parser.add_argument("--plano", required=True, help="Caminho do .md do plano.")
    close_parser.add_argument("--tarefa", required=True, help="Identificador da tarefa (ex.: T19).")
    close_parser.add_argument(
        "--tool-uses", required=True, dest="tool_uses",
        help="Tool uses gastos, medidos (nunca auto-relatados). Validado em código (LM-T1a).",
    )
    close_parser.add_argument(
        "--tokens-k", required=True, dest="tokens_k",
        help="Milhares de tokens gastos, medidos. Validado em código (LM-T1a).",
    )
    close_parser.add_argument(
        "--duracao-s", required=True, dest="duracao_s",
        help="Duração em segundos, medida (aceita decimal). Validado em código (LM-T1a).",
    )
    close_parser.add_argument(
        "--veredito", required=True, choices=("aprovado", "ressalva"),
        help="Veredito do laudo, transcrito (DA-6) — domínio fechado pela premissa de escopo.",
    )
    close_parser.add_argument(
        "--percentual", required=True, type=int, choices=range(0, 101), metavar="{0..100}",
        help="Percentual do laudo, transcrito (DA-6).",
    )
    close_parser.add_argument(
        "--bloqueante", required=True,
        help="Dimensão bloqueante do laudo, transcrita, ou 'nenhuma'.",
    )
    close_parser.add_argument(
        "--recomendacao", required=True,
        help="Recomendação do laudo, transcrita, uma linha.",
    )
    close_parser.add_argument(
        "--pendencia-laudo", required=True, dest="pendencia_laudo",
        help="Pendência do laudo, transcrita, uma linha, ou 'nenhuma'.",
    )
    close_parser.add_argument(
        "--pendencia", default=None,
        help="Pendência autoral do executor, uma linha — único argumento de conteúdo do close.",
    )
    close_parser.add_argument(
        "--licoes-aprendidas",
        dest="licoes_aprendidas",
        default=None,
        help=(
            "Card 'Lições aprendidas na tarefa', transcrito do laudo sem recálculo (`DP-Q` §21 "
            "item 3) — discricionário, ausência é legítima."
        ),
    )
    close_parser.add_argument(
        "--rdo-dir", default=None, help="Diretório de saída (default: docs/RDO)."
    )
    close_parser.add_argument(
        "--template", type=Path, default=None, help="Template (default: rdo_template.md do script)."
    )
    close_parser.add_argument(
        "--esquema-legado",
        action="store_true",
        help="Cabeçalho sem [modelo · classe] — exige --modelo/--classe.",
    )
    close_parser.add_argument("--modelo", default=None, help="Só com --esquema-legado.")
    close_parser.add_argument("--classe", default=None, help="Só com --esquema-legado.")

    args = parser.parse_args(argv)

    if args.command == "laudo":
        try:
            destino = cmd_laudo(args)
        except RdoValidationError as exc:
            print(f"rdo: FALHOU - {exc}", file=sys.stderr)
            return 1
        print(f"rdo: OK - laudo gravado em '{destino}'.")
        return 0

    if args.command == "close":
        try:
            destino = cmd_close(args)
        except RdoValidationError as exc:
            print(f"rdo: FALHOU - {exc}", file=sys.stderr)
            return 1
        print(f"rdo: OK - RDO fechado em '{destino}'.")
        return 0

    parser.error(f"comando desconhecido: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
