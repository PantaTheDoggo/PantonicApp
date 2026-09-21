"""`modelo.py` — os verbos `check` e `show` sobre a seção `## 1. Modelo conceitual` de um plano,
na superfície normativa da `### 16. Superfície do instrumento no terceiro estágio` de
`docs/plans/P-0743-modelo-de-dominio.md`.

Gramática lida (residência única: skill `diario-de-obras`, subseção "Modelo de domínio (seção do
plano)"): cabeçalho `**Estado do modelo:**`, tabela `### 1.1 Objetos` (coluna `propriedades`),
`### 1.2 Fluxo de operações` — pares de linhas `- **OP-<n>** — <texto>` e o sub-bullet com
`precisa de:`, `altera:` e `tarefas:`, com subtítulos `**A. …**` livres —, tabela
`### 1.3 Estado inicial e estado final` e tabela `### 1.4 Registro de versões`. A versão pendente,
quando existe, nasce como o bloco irmão `## 1A. Modelo conceitual — versão pendente de validação`,
com a mesma estrutura de `### 1.1` a `### 1.3`.

`check` julga a seção contra o vocabulário fechado de violações `V1`..`V20` (`### 16` do `P-0743`)
e `show` deriva a leitura do dono a partir do modelo real: ela abre pelo estágio atual, que é a
primeira operação ainda não concluída, derivada do status das tarefas e não gravada por nenhum
papel; com `--pendente` mostra o bloco `## 1A`, e com `--drift` mostra a diferença entre a versão
vigente e a pendente. Ambos carregam `backlog.py` por caminho
(`importlib.util.spec_from_file_location`) e chamam `backlog._parse_plano` para obter
`Plano.tarefas`; `backlog.py` não é reescrito (`I-1` do `P-0743`)."""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


def _default_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `—` — duplicado do
    mesmo utilitário de `card_check.py`/`review_evidence.py` (`DM-11`, sem import cruzado)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def _load_backlog(root: Path):
    caminho = root / ".claude" / "tools" / "backlog.py"
    spec = importlib.util.spec_from_file_location("backlog", caminho)
    modulo = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via
    # `sys.modules[cls.__module__]` — precisa estar registrado antes do exec_module (mesmo padrão
    # de `tests/test_backlog.py`).
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


# --------------------------------------------------------------------------- #
# Modelo de dados
# --------------------------------------------------------------------------- #


@dataclass
class Operacao:
    numero: int
    texto: str
    precisa_de: list[str] = field(default_factory=list)
    altera: list[str] = field(default_factory=list)
    tarefas: list[str] = field(default_factory=list)


@dataclass
class Objeto:
    nome: str
    contrato: str
    origem: str
    propriedades: list[str] = field(default_factory=list)


@dataclass
class Modelo:
    versao: int
    data: str
    objetos: list[Objeto] = field(default_factory=list)
    operacoes: list[Operacao] = field(default_factory=list)
    estado: list[tuple[str, str, str]] = field(default_factory=list)
    versoes: list[str] = field(default_factory=list)
    situacao: str = "vigente"
    tabela_objetos: list[str] = field(default_factory=list)
    subtitulos: dict[int, str] = field(default_factory=dict)
    cabecalho_presente: bool = True
    tabela_estado: list[str] = field(default_factory=list)
    tabela_versoes: list[str] = field(default_factory=list)


_HEADING_VIGENTE = "## 1. Modelo conceitual"
_HEADING_PENDENTE = "## 1A. Modelo conceitual — versão pendente de validação"

_MSG_AUSENTE = "modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')"

_MSG_FORMA_ANTERIOR_ORACOES = (
    "modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')"
)

_MSG_FORMA_ANTERIOR_SEM_ESTADO = "modelo: forma anterior — plano sem estado inicial e final"

_MSG_SEM_PENDENTE = "modelo: sem versão pendente"

_MSG_SEM_DRIFT = "sem drift"

_OPERACAO_HEADER_RE = re.compile(r"^- \*\*OP-(\d+)\*\* — (.+)$")
_OPERACAO_LINHA_RE = re.compile(
    r"^  - `precisa de: ([^`]*)` · `altera: ([^`]*)` · `tarefas: ([^`]*)`$"
)
_SUBTITULO_RE = re.compile(r"^\*\*[A-Z]\. .+\*\*$")
_CAMPO_OPERACAO_RE = re.compile(r"^- \*\*Operação do modelo:\*\* (.+)$", re.MULTILINE)
_ID_OP_RE = re.compile(r"`(OP-\d+)`")
_CABECALHO_VALOR_RE = re.compile(r"\*\*Estado do modelo:\*\* versão (\d+) · (\d{4}-\d{2}-\d{2})")
_SITUACAO_RE = re.compile(r"situação: (vigente|pendente)")
_ORIGEM_OP_RE = re.compile(r"^OP-(\d+)$")

_STATUS_CONCLUSIVO = {"done", "cancelled"}
_STATUS_EM_CURSO = {"in-progress", "review"}


def _extrair_tabela(secao: list[str], heading: str) -> list[str]:
    idx = next((i for i, l in enumerate(secao) if l.startswith(heading)), None)
    if idx is None:
        return []
    linhas_tab: list[str] = []
    coletando = False
    for linha in secao[idx + 1 :]:
        if linha.startswith("|"):
            linhas_tab.append(linha)
            coletando = True
        elif coletando:
            break
        elif linha.strip() == "":
            continue
        else:
            break
    return linhas_tab


def _localizar_secao(linhas: list[str], heading: str) -> list[str] | None:
    inicio = next((i for i, l in enumerate(linhas) if l == heading), None)
    if inicio is None:
        return None
    fim = len(linhas)
    for i in range(inicio + 1, len(linhas)):
        if linhas[i].startswith("## "):
            fim = i
            break
    return linhas[inicio:fim]


def _tem_fluxo(secao: list[str]) -> bool:
    return any(l.startswith("### 1.2 Fluxo de operações") for l in secao)


def _tem_estado_final(secao: list[str]) -> bool:
    return any(l.startswith("### 1.3 Estado inicial e estado final") for l in secao)


def _parse_linha_tabela(linha: str) -> list[str]:
    return [p.strip() for p in linha.strip().strip("|").split("|")]


def _parse_objetos(tabela: list[str]) -> list[Objeto]:
    objetos: list[Objeto] = []
    for linha in tabela[2:]:
        campos = _parse_linha_tabela(linha)
        if len(campos) >= 5:
            propriedades = [p.strip() for p in campos[2].split(",") if p.strip()]
            objetos.append(
                Objeto(
                    nome=campos[0],
                    contrato=campos[3],
                    origem=campos[4],
                    propriedades=propriedades,
                )
            )
    return objetos


def _parse_estado(tabela: list[str]) -> list[tuple[str, str, str]]:
    estado: list[tuple[str, str, str]] = []
    for linha in tabela[2:]:
        campos = _parse_linha_tabela(linha)
        if len(campos) >= 3:
            estado.append((campos[0], campos[1], campos[2]))
    return estado


def _parse_versoes(tabela: list[str]) -> list[str]:
    return tabela[2:] if len(tabela) > 2 else []


def _extrair_operacoes(secao: list[str]) -> tuple[list[Operacao], dict[int, str]]:
    idx = next(
        (i for i, l in enumerate(secao) if l.startswith("### 1.2 Fluxo de operações")), None
    )
    if idx is None:
        return [], {}
    fim = len(secao)
    for i in range(idx + 1, len(secao)):
        if secao[i].startswith("### ") or secao[i].startswith("## "):
            fim = i
            break

    operacoes: list[Operacao] = []
    subtitulos: dict[int, str] = {}
    i = idx + 1
    while i < fim:
        linha = secao[i]
        if _SUBTITULO_RE.match(linha):
            subtitulos[len(operacoes)] = linha
            i += 1
            continue
        m = _OPERACAO_HEADER_RE.match(linha)
        if m and i + 1 < fim:
            m2 = _OPERACAO_LINHA_RE.match(secao[i + 1])
            if m2:
                numero, texto = int(m.group(1)), m.group(2)
                precisa_de = [p.strip() for p in m2.group(1).split(",") if p.strip()]
                altera = [a.strip() for a in m2.group(2).split(",") if a.strip()]
                tarefas = [t.strip() for t in m2.group(3).split(",") if t.strip()]
                operacoes.append(
                    Operacao(
                        numero=numero,
                        texto=texto,
                        precisa_de=precisa_de,
                        altera=altera,
                        tarefas=tarefas,
                    )
                )
                i += 2
                continue
        i += 1
    return operacoes, subtitulos


def extrair_modelo(linhas: list[str], heading: str) -> Modelo | None:
    secao = _localizar_secao(linhas, heading)
    if secao is None:
        return None

    cabecalho = next((l for l in secao if l.startswith("**Estado do modelo:**")), None)
    versao, data, situacao = 0, "?", "vigente"
    if cabecalho:
        mc = _CABECALHO_VALOR_RE.search(cabecalho)
        if mc:
            versao, data = int(mc.group(1)), mc.group(2)
        ms = _SITUACAO_RE.search(cabecalho)
        if ms:
            situacao = ms.group(1)

    tabela_objetos = _extrair_tabela(secao, "### 1.1 Objetos")
    objetos = _parse_objetos(tabela_objetos)
    operacoes, subtitulos = _extrair_operacoes(secao)

    tabela_estado = _extrair_tabela(secao, "### 1.3 Estado inicial e estado final")
    estado = _parse_estado(tabela_estado)

    tabela_versoes = _extrair_tabela(secao, "### 1.4 Registro de versões")
    versoes = _parse_versoes(tabela_versoes)

    return Modelo(
        versao=versao,
        data=data,
        objetos=objetos,
        operacoes=operacoes,
        estado=estado,
        versoes=versoes,
        situacao=situacao,
        tabela_objetos=tabela_objetos,
        subtitulos=subtitulos,
        cabecalho_presente=cabecalho is not None,
        tabela_estado=tabela_estado,
        tabela_versoes=tabela_versoes,
    )


def campo_operacoes(item_texto: str) -> list[str] | None:
    m = _CAMPO_OPERACAO_RE.search(item_texto)
    if not m:
        return None
    return _ID_OP_RE.findall(m.group(1))


def _tem_subbullets(item_texto: str, op_id: str) -> bool:
    linhas = item_texto.splitlines()
    prefixo_texto = f"  - {op_id}: "
    for i, linha in enumerate(linhas):
        if linha.startswith(prefixo_texto):
            return i + 1 < len(linhas) and linhas[i + 1].startswith("  - precisa de: ")
    return False


def validar(modelo: Modelo, plano, modelo_pendente: Modelo | None = None) -> list[str]:
    violacoes_op: list[str] = []
    violacoes_objeto: list[str] = []
    violacoes_id: list[str] = []

    ids_tarefas = {t.id for t in plano.tarefas}
    nomes_objetos = {o.nome for o in modelo.objetos}
    numeros_operacoes = {op.numero for op in modelo.operacoes}
    origem_por_objeto = {o.nome: o.origem for o in modelo.objetos}
    propriedades_por_objeto = {o.nome: set(o.propriedades) for o in modelo.objetos}
    propriedades_com_estado = {chave for chave, _, _ in modelo.estado}

    if (
        not modelo.cabecalho_presente
        or not modelo.tabela_objetos
        or not modelo.tabela_estado
        or not modelo.tabela_versoes
    ):
        violacoes_op.append(
            "V13 secao — cabeçalho, objetos, estado ou registro de versões ausente"
        )

    situacoes_versoes = [
        _parse_linha_tabela(linha)[2] if len(_parse_linha_tabela(linha)) >= 3 else ""
        for linha in modelo.versoes
    ]
    if situacoes_versoes.count("vigente") != 1:
        violacoes_op.append("V19 secao — registro de versões sem vigente único")

    if modelo_pendente is not None and modelo_pendente.versao != modelo.versao + 1:
        violacoes_op.append("V20 secao — versão pendente fora de sequência")

    numeros_vistos: set[int] = set()
    for posicao, operacao in enumerate(modelo.operacoes, start=1):
        if not operacao.tarefas:
            violacoes_op.append(f"V1 OP-{operacao.numero} — operação sem tarefa")
        for tid in operacao.tarefas:
            if tid not in ids_tarefas:
                violacoes_op.append(f"V3 OP-{operacao.numero} — tarefa inexistente {tid}")
        for nome in operacao.precisa_de:
            if nome not in nomes_objetos:
                violacoes_op.append(f"V5 OP-{operacao.numero} — objeto inexistente {nome}")
        if operacao.numero != posicao:
            violacoes_op.append(f"V8 OP-{operacao.numero} — fora da sequência")
        if operacao.numero > 1:
            tem_origem_operacional = any(
                _ORIGEM_OP_RE.match(origem_por_objeto.get(nome, ""))
                for nome in operacao.precisa_de
            )
            if not tem_origem_operacional:
                violacoes_op.append(f"V9 OP-{operacao.numero} — operação desencadeada")
        for nome in operacao.precisa_de:
            mo = _ORIGEM_OP_RE.match(origem_por_objeto.get(nome, ""))
            if mo and int(mo.group(1)) >= operacao.numero:
                violacoes_op.append(f"V10 OP-{operacao.numero} — objeto produzido depois {nome}")
        if operacao.numero in numeros_vistos:
            violacoes_op.append(f"V11 OP-{operacao.numero} — identificador duplicado")
        numeros_vistos.add(operacao.numero)
        if "`" in operacao.texto or "/" in operacao.texto:
            violacoes_op.append(f"V12 OP-{operacao.numero} — literal técnico no texto")
        if not operacao.altera:
            violacoes_op.append(
                f"V18 OP-{operacao.numero} — operação que não altera propriedade"
            )
        for item in operacao.altera:
            nome_objeto, _, propriedade = item.rpartition(".")
            if propriedade not in propriedades_por_objeto.get(nome_objeto, set()):
                violacoes_op.append(f"V16 OP-{operacao.numero} — propriedade inexistente {item}")

    for objeto in modelo.objetos:
        if not objeto.propriedades:
            violacoes_objeto.append(f"V15 objeto — objeto sem propriedade {objeto.nome}")
        for propriedade in objeto.propriedades:
            chave = f"{objeto.nome}.{propriedade}"
            if chave not in propriedades_com_estado:
                violacoes_objeto.append(f"V17 objeto — propriedade sem estado {chave}")
        if objeto.origem == "externo":
            usado = any(objeto.nome in op.precisa_de for op in modelo.operacoes)
            if not usado:
                violacoes_objeto.append(f"V6 objeto — objeto externo sem uso {objeto.nome}")
        else:
            mo = _ORIGEM_OP_RE.match(objeto.origem)
            if mo is None or int(mo.group(1)) not in numeros_operacoes:
                violacoes_objeto.append(f"V7 objeto — origem inexistente {objeto.nome}")

    for item in plano.tarefas:
        ops_citadas = campo_operacoes(item.texto)
        if not ops_citadas:
            violacoes_id.append(f"V2 {item.id} — tarefa sem operação")
        for op_id in ops_citadas or []:
            mo = _ORIGEM_OP_RE.match(op_id)
            numero = int(mo.group(1)) if mo else None
            if numero not in numeros_operacoes:
                violacoes_id.append(f"V4 {item.id} — operação inexistente {op_id}")
            if not _tem_subbullets(item.texto, op_id):
                violacoes_id.append(f"V14 {item.id} — contrato ausente para {op_id}")

    return violacoes_op + violacoes_objeto + violacoes_id


def derivar_andamento(operacao: Operacao, status_por_id: dict[str, str | None]) -> str:
    status_tarefas = [status_por_id.get(tid) for tid in operacao.tarefas]
    if status_tarefas and all(s in _STATUS_CONCLUSIVO for s in status_tarefas):
        return "concluída"
    if any(s in _STATUS_EM_CURSO for s in status_tarefas):
        return "em curso"
    return "prevista"


def derivar_estagio(modelo: Modelo, status_por_id: dict[str, str | None]) -> str:
    for operacao in modelo.operacoes:
        if derivar_andamento(operacao, status_por_id) != "concluída":
            return f"OP-{operacao.numero} — {operacao.texto}"
    return "concluído"


# --------------------------------------------------------------------------- #
# Drift entre a versão vigente e a pendente
# --------------------------------------------------------------------------- #


def _obj_por_nome(modelo: Modelo) -> dict[str, Objeto]:
    return {o.nome: o for o in modelo.objetos}


def _op_por_numero(modelo: Modelo) -> dict[int, Operacao]:
    return {op.numero: op for op in modelo.operacoes}


def _estado_por_chave(modelo: Modelo) -> dict[str, tuple[str, str]]:
    return {chave: (inicial, final) for chave, inicial, final in modelo.estado}


def _diff_objetos(vigente: Modelo, pendente: Modelo) -> list[str]:
    objetos_vigente = _obj_por_nome(vigente)
    objetos_pendente = _obj_por_nome(pendente)
    linhas: list[str] = []
    for nome, objeto in objetos_pendente.items():
        if nome not in objetos_vigente:
            linhas.append(f"[+] {nome} — {', '.join(objeto.propriedades)}")
    for nome, objeto in objetos_vigente.items():
        if nome not in objetos_pendente:
            linhas.append(f"[-] {nome} — {', '.join(objeto.propriedades)}")
    for nome, objeto_v in objetos_vigente.items():
        objeto_p = objetos_pendente.get(nome)
        if objeto_p is not None and objeto_v.propriedades != objeto_p.propriedades:
            linhas.append(
                f"[~] {nome} — {', '.join(objeto_v.propriedades)} => "
                f"{', '.join(objeto_p.propriedades)}"
            )
    return linhas


def _diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]:
    ops_vigente = _op_por_numero(vigente)
    ops_pendente = _op_por_numero(pendente)
    linhas: list[str] = []
    for numero, operacao in ops_pendente.items():
        if numero not in ops_vigente:
            linhas.append(f"[+] OP-{numero} — {operacao.texto}")
    for numero, operacao in ops_vigente.items():
        if numero not in ops_pendente:
            linhas.append(f"[-] OP-{numero} — {operacao.texto}")
    for numero, operacao_v in ops_vigente.items():
        operacao_p = ops_pendente.get(numero)
        if operacao_p is not None and operacao_v.texto != operacao_p.texto:
            linhas.append(f"[~] OP-{numero} — {operacao_v.texto} => {operacao_p.texto}")
    return linhas


def _diff_estado(vigente: Modelo, pendente: Modelo) -> list[str]:
    estado_vigente = _estado_por_chave(vigente)
    estado_pendente = _estado_por_chave(pendente)
    linhas: list[str] = []
    for chave, (_, final_v) in estado_vigente.items():
        par_pendente = estado_pendente.get(chave)
        if par_pendente is not None:
            _, final_p = par_pendente
            if final_v != final_p:
                linhas.append(f"[~] {chave} — {final_v} => {final_p}")
    return linhas


def montar_drift(vigente: Modelo, pendente: Modelo) -> str:
    linhas_objetos = _diff_objetos(vigente, pendente)
    linhas_fluxo = _diff_fluxo(vigente, pendente)
    linhas_estado = _diff_estado(vigente, pendente)

    if not linhas_objetos and not linhas_fluxo and not linhas_estado:
        return _MSG_SEM_DRIFT

    linhas: list[str] = [
        f"vigente: versão {vigente.versao} · {vigente.data}   "
        f"pendente: versão {pendente.versao} · {pendente.data}"
    ]
    if linhas_objetos:
        linhas.append("")
        linhas.append("## Objetos")
        linhas.extend(linhas_objetos)
    if linhas_fluxo:
        linhas.append("")
        linhas.append("## Fluxo")
        linhas.extend(linhas_fluxo)
    if linhas_estado:
        linhas.append("")
        linhas.append("## Estado final")
        linhas.extend(linhas_estado)
    return "\n".join(linhas)


# --------------------------------------------------------------------------- #
# Verbos
# --------------------------------------------------------------------------- #


def _resolver_plano(args) -> Path:
    plano = Path(args.plano)
    if plano.is_absolute():
        return plano
    return Path(args.root) / plano


def _checar_forma(linhas: list[str]) -> tuple[list[str] | None, int | None, str | None]:
    """Aplica, nesta ordem, os três primeiros exits de `### 16`. Devolve `(secao, None, None)`
    quando o plano está na forma nova, ou `(None, exit, msg)` quando o chamador deve sair sem
    seguir adiante."""
    secao = _localizar_secao(linhas, _HEADING_VIGENTE)
    if secao is None:
        return None, 2, _MSG_AUSENTE
    if not _tem_fluxo(secao):
        return None, 2, _MSG_FORMA_ANTERIOR_ORACOES
    if not _tem_estado_final(secao):
        return None, 2, _MSG_FORMA_ANTERIOR_SEM_ESTADO
    return secao, None, None


def verbo_check(args: argparse.Namespace) -> int:
    root = Path(args.root)
    plano_path = _resolver_plano(args)
    linhas = plano_path.read_text(encoding="utf-8").splitlines()

    _, exit_code, msg = _checar_forma(linhas)
    if exit_code is not None:
        print(msg)
        return exit_code

    modelo = extrair_modelo(linhas, _HEADING_VIGENTE)
    secao_pendente = _localizar_secao(linhas, _HEADING_PENDENTE)
    modelo_pendente = (
        extrair_modelo(linhas, _HEADING_PENDENTE) if secao_pendente is not None else None
    )

    backlog = _load_backlog(root)
    plano = backlog._parse_plano(plano_path, root)
    violacoes = validar(modelo, plano, modelo_pendente)
    if violacoes:
        for linha in violacoes:
            print(linha, file=sys.stderr)
        print(f"modelo: FALHOU — {len(violacoes)} violação(ões)", file=sys.stderr)
        return 1

    total_propriedades = sum(len(o.propriedades) for o in modelo.objetos)
    print(
        f"modelo: OK — {len(modelo.operacoes)} operações, {len(modelo.objetos)} objetos, "
        f"{total_propriedades} propriedades, {len(plano.tarefas)} tarefas, versão {modelo.versao}"
    )
    return 0


_ROTULOS_ANDAMENTO = {
    "concluída": "concluída".ljust(9),
    "em curso": "em curso".ljust(9),
    "prevista": "prevista".ljust(9),
}


def _linha_operacao(operacao: Operacao, andamento: str) -> str:
    return f"[{_ROTULOS_ANDAMENTO[andamento]}] OP-{operacao.numero} — {operacao.texto}"


def _montar_show(modelo: Modelo, plano, status_por_id: dict[str, str | None]) -> str:
    linhas_saida: list[str] = []
    linhas_saida.append(f"# Modelo de domínio — {plano.id} — {plano.titulo}")

    estagio = derivar_estagio(modelo, status_por_id)
    linhas_saida.append(
        f"Estado do modelo: versão {modelo.versao} · {modelo.data} · "
        f"situação: {modelo.situacao} · {len(modelo.operacoes)} operações · "
        f"estágio atual: {estagio}"
    )
    linhas_saida.append("")

    linhas_saida.append("## Objetos")
    linhas_saida.extend(modelo.tabela_objetos)
    linhas_saida.append("")

    linhas_saida.append("## Fluxo")
    for i, operacao in enumerate(modelo.operacoes):
        if i in modelo.subtitulos:
            linhas_saida.append("")
            linhas_saida.append(modelo.subtitulos[i])
        andamento = derivar_andamento(operacao, status_por_id)
        linhas_saida.append(_linha_operacao(operacao, andamento))
        linhas_saida.append(" " * 12 + f"precisa de: {', '.join(operacao.precisa_de)}")
        linhas_saida.append(" " * 12 + f"altera: {', '.join(operacao.altera)}")
    linhas_saida.append("")

    linhas_saida.append("## Estado")
    linhas_saida.extend(modelo.tabela_estado)

    return "\n".join(linhas_saida)


def verbo_show(args: argparse.Namespace) -> int:
    root = Path(args.root)
    plano_path = _resolver_plano(args)
    linhas = plano_path.read_text(encoding="utf-8").splitlines()

    _, exit_code, msg = _checar_forma(linhas)
    if exit_code is not None:
        print(msg)
        return exit_code

    modelo = extrair_modelo(linhas, _HEADING_VIGENTE)
    secao_pendente = _localizar_secao(linhas, _HEADING_PENDENTE)

    backlog = _load_backlog(root)
    plano = backlog._parse_plano(plano_path, root)
    status_por_id = {t.id: t.status for t in plano.tarefas}

    if args.drift:
        if secao_pendente is None:
            print(_MSG_SEM_PENDENTE)
            return 2
        modelo_pendente = extrair_modelo(linhas, _HEADING_PENDENTE)
        corpo = montar_drift(modelo, modelo_pendente)
        if corpo == _MSG_SEM_DRIFT:
            print(_MSG_SEM_DRIFT)
            return 0
        print(f"# Drift do modelo — {plano.id} — {plano.titulo}")
        print(corpo)
        return 0

    if args.pendente:
        if secao_pendente is None:
            print(_MSG_SEM_PENDENTE)
            return 2
        modelo_mostrado = extrair_modelo(linhas, _HEADING_PENDENTE)
    else:
        modelo_mostrado = modelo

    print(_montar_show(modelo_mostrado, plano, status_por_id))
    return 0


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    parser = argparse.ArgumentParser(
        description=(
            "modelo.py (P-0743): check julga a seção '## 1. Modelo conceitual' de um plano "
            "contra o vocabulário de violações V1..V20 (### 16); show deriva a leitura do dono "
            "a partir do modelo real, abrindo pelo estágio atual, com --pendente para o bloco "
            "'## 1A' e --drift para a diferença entre a versão vigente e a pendente."
        )
    )
    sub = parser.add_subparsers(dest="verbo", required=True)

    p_check = sub.add_parser("check")
    p_check.add_argument("--plano", required=True, help="Caminho do .md do plano.")
    p_check.add_argument("--root", default=_default_root(), help="Raiz do repositório.")
    p_check.set_defaults(func=verbo_check)

    p_show = sub.add_parser("show")
    p_show.add_argument("--plano", required=True, help="Caminho do .md do plano.")
    grupo = p_show.add_mutually_exclusive_group()
    grupo.add_argument(
        "--pendente",
        action="store_true",
        help="Mostra o bloco '## 1A' (versão pendente de validação) em vez da vigente.",
    )
    grupo.add_argument(
        "--drift",
        action="store_true",
        help="Mostra a diferença entre a versão vigente e a pendente.",
    )
    p_show.add_argument("--root", default=_default_root(), help="Raiz do repositório.")
    p_show.set_defaults(func=verbo_show)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
