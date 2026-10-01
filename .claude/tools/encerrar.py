"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — o fechamento de tarefa e o de plano deixam de
ser uma sequência de comandos e prosa escrita à mão e passam a ser **um comando cada**, que recebe
a informação da tarefa realizada, escreve os artefatos de fechamento que o kit já tinha e faz os
registros nos documentos de backlog no mesmo ato.

Lugar comum medido (2026-09-26, sobre os fechamentos de `P-0745`..`P-0751`): fechar uma tarefa
eram quatro comandos em turnos separados — `modelo.py check`, `backlog.py status <ID> done`,
`rdo.py close` com o pacote do laudo **redigitado** a partir do arquivo que `rdo.py laudo` já
tinha gravado, e `telemetria.py append` conferindo a linha do hook —, mais o achado `AE-<n>`
editado no plano; fechar um plano era inteiramente manual, porque o instrumento recusava
`ready → done` para plano (registrado no diário em 2026-09-25) e o parágrafo de fechamento, a
linha do índice e a triagem dos achados eram escritos à mão.

Três verbos, todos com as checagens **antes** de qualquer escrita. `tarefa` e `plano` **reportam**
resultado e histórico; `handover` **entrega** — é o que quem vem depois espera da tarefa, de forma
inequívoca, direta e objetiva, inteiramente de máquina, registrado **na própria tarefa**:

``python .claude/tools/encerrar.py handover --plano <caminho.md> --tarefa <ID> --entregue "<o que
existe, com caminho:linha>" --contrato "<com o que a sucessora conta>" [--nao-refazer "<o que já
está pago>"] [--pendente "<o que fica de propósito>"] [--para <ID|papel>]... [--repo] [--data]``

Escreve (ou substitui) o campo `- **Handover:** <data> · para \\`<ID>\\`...` com os sub-bullets
`Entregue`, `Contrato`, `Não refazer` e `Pendente` no card, antes de `- **Notas de execução:**`;
exige entrega na árvore (`in-progress`, `review`, `done` ou `blocked`). A nomenclatura é a
âncora da recuperação: `backlog.py next` (`handovers_para`) devolve, sob `=== HANDOVER DE <ID>`,
junto com a próxima tarefa, o handover de todo irmão que a nomeia em `para` e, na falta, o da
antecessora imediata — o orquestrador cola na delegação o que for pertinente. O `rdo.py close`
transcreve o campo no RDO como extra do card, e `show <ID>` o imprime verbatim.

Os outros dois:

``python .claude/tools/encerrar.py tarefa --plano <caminho.md> --tarefa <ID> [--resumo "<frase>"]
[--pendencia "<uma linha>"] [--achado "<texto>" "<rota>"]... [--laudo <caminho>]
[--tool-uses N --tokens-k K --duracao-s S [--modelo-agente <nome>]] [--progresso <caminho>]
[--rdo-dir <dir>] [--repo <raiz>] [--data AAAA-MM-DD]``

1. a tarefa está em `review` (única transição que produz RDO — skill `diario-de-obras`,
   *Máquina de transições*, gatilho 2); 2. o laudo existe (`<pasta>/laudos/<ID>.md` ou
   `docs/RDO/laudos/<plano>-<ID>.md`) e o pacote é **transcrito** dele — veredito, percentual,
   bloqueante, recomendação, pendência e lições —, nunca redigitado; `reprovado` é recusado
   (`GOVERNANCA.md` §4.2: não é desfecho de RDO); 3. o consumo vem da **fonte única**
   `docs/telemetria.tsv` (última linha da tarefa, gravada pelo hook `SubagentStop`) ou, quando o
   chamador traz o bloco `<usage>` em `--tool-uses/--tokens-k/--duracao-s`, é apensado à série no
   mesmo ato; sem nenhum dos dois o fechamento é recusado — número inventado não fecha tarefa;
   4. `modelo.py check` sai `0` ou `2` (exit `1` mantém a tarefa em `review`, `DMC-30`).
   Passadas as checagens, e nesta ordem: `backlog.transacionar_status(<ID>, done)` com a nota de
   fechamento (bullet do card, índice `done/total`, bloco `Fila corrente`, `estado.tsv`);
   `rdo.cmd_close` em processo, com as seções `# Humano` e `# Histórico` preenchidas — o humano em
   linguagem corrente, com o título da tarefa no lugar da sigla (`GOVERNANCA.md` §4.2, *Mensagem
   legível ao dono*), e o histórico com as linhas que o painel do gerente (`progresso_hook.py`)
   gerou para a tarefa; a linha de telemetria, se o consumo veio por argumento; e cada `--achado`
   como entrada `AE-<n>` com `**Rota:**` em `## Achados da execução` do plano — registro único do
   achado (`GOVERNANCA.md` §4.2, *Fechamento enxuto*). A seção `# Humano` é impressa na saída: ela
   **é** o handover ao dono, em ≤ 8 linhas.

``python .claude/tools/encerrar.py plano --plano <caminho.md> --veredito "<frase do dono, verbatim>"
[--operacoes <caminho>] [--resumo "<frase>"] [--saida <caminho>] [--progresso <caminho>]
[--rdo-dir <dir>] [--repo <raiz>] [--data AAAA-MM-DD]``

1. nenhuma tarefa aberta (`done`/`cancelled` apenas) e ao menos uma `done`; 2. toda tarefa `done`
   tem RDO (tarefa sem RDO não está fechada — skill `passagem-de-bastao`, *Proibições*); 3. todo
   `AE-<n>` de `## Achados da execução` traz `**Rota:**` (gate de triagem do fechamento de sprint);
   4. o documento de validação existe (`operacoes.md` na pasta ou `docs/OPERACOES_AS_IS_<id>.md`,
   skill `entrega-de-encerramento`) — ele é insumo do veredito, não consequência; 5. `modelo.py
   check` não sai `1`. Depois, nesta ordem: `transacionar_status(<plano>, done)` — permitido pela
   regra de plano do `backlog.py` (`TK-88`) —, o relatório de entrega em `entrega.md` (pasta) ou
   `docs/plans/_ENTREGA-<id>.md` (legado), nas mesmas três seções, e **uma** linha no cabeçalho do
   diário com o veredito verbatim e os dois ponteiros — o parágrafo que antes se escrevia à mão.

Este módulo **não** reimplementa nenhuma regra dos instrumentos que compõe: carrega `backlog.py`,
`rdo.py`, `telemetria.py` e `caminhos.py` por caminho e chama as funções deles. Superfície
testável: `fechar_tarefa`/`fechar_plano` recebem caminhos já resolvidos e nunca leem `sys.argv`
(`DB-1`); a saída é `EncerramentoError` (exit 1, nada escrito) ou o caminho do relatório.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
REPO = KIT.parent


def _carregar(nome: str):
    caminho = KIT / "tools" / f"{nome}.py"
    spec = importlib.util.spec_from_file_location(nome, caminho)
    modulo = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via `sys.modules`.
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar("caminhos")
_backlog = _carregar("backlog")
_rdo = _carregar("rdo")
_telemetria = _carregar("telemetria")
_modelo = _carregar("modelo")


class EncerramentoError(ValueError):
    """Checagem que recusa o fechamento — a mensagem nomeia o que falta; nada foi escrito."""


class ConflitoDePromocao(EncerramentoError):
    """`--aceita-versao` em conflito com o estado do plano (`RAF-T23`, `DRF-38`) — carrega o
    dossiê `Ato: emenda` para o modelador, no atributo `dossie`."""

    def __init__(self, mensagem: str, dossie: str) -> None:
        super().__init__(mensagem)
        self.dossie = dossie


ACHADOS_HEADING_RE = re.compile(r"^## .*Achados da execução")
AE_ID_RE = re.compile(r"\bAE-(\d+)\b")
ROTA_RE = re.compile(r"\*\*Rota:?\*\*|\bRota:")
_LAUDO_RES = {
    "percentual": re.compile(r"^\*\*Percentual:\*\* (\d+)%", re.M),
    "veredito": re.compile(r"^\*\*Veredito:\*\* (\S+)", re.M),
    "bloqueante": re.compile(r"^\*\*Dimensão bloqueante:\*\* (.+?)\s*$", re.M),
    "recomendacao": re.compile(r"^\*\*Recomendação:\*\* (.+?)\s*$", re.M),
    "pendencia": re.compile(r"^\*\*Pendência:\*\* (.+?)\s*$", re.M),
}
_RDO_RES = {
    "veredito": re.compile(r"^\*\*Veredito:\*\* (\S+)", re.M),
    "percentual": re.compile(r"^\*\*Percentual:\*\* (\d+)%", re.M),
    "desdobramento": re.compile(r"^\*\*Desdobramento:\*\* (.+?)\s*$", re.M),
}


# --------------------------------------------------------------------------- #
# Leitores — laudo, série de telemetria, painel do gerente, achados do plano
# --------------------------------------------------------------------------- #


def ler_laudo(caminho: Path) -> dict[str, str]:
    """Pacote do laudo transcrito do arquivo que `rdo.py laudo` gravou (`DA-6`: quem fecha lê,
    não recalcula). Campo ausente é recusa nomeada, nunca valor padrão."""
    if not caminho.is_file():
        raise EncerramentoError(
            f"laudo: arquivo não encontrado '{caminho}' — rode `rdo.py laudo` antes, ou aponte --laudo"
        )
    texto = caminho.read_text(encoding="utf-8")
    pacote: dict[str, str] = {}
    for campo, regex in _LAUDO_RES.items():
        m = regex.search(texto)
        if not m:
            raise EncerramentoError(f"laudo: campo '{campo}' ausente em '{caminho}'")
        pacote[campo] = m.group(1).strip()
    licoes = ""
    marca = "## Lições aprendidas na tarefa"
    if marca in texto:
        corpo = texto.split(marca, 1)[1]
        m_fim = re.search(r"^## ", corpo, re.M)
        licoes = (corpo[: m_fim.start()] if m_fim else corpo).strip()
    pacote["licoes"] = licoes
    return pacote


def _ler_tsv(caminho: Path) -> list[dict[str, str]]:
    if not caminho.is_file():
        return []
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    if not linhas:
        return []
    colunas = linhas[0].split("\t")
    registros = []
    for linha in linhas[1:]:
        if not linha.strip():
            continue
        valores = linha.split("\t")
        if len(valores) != len(colunas):
            continue
        registros.append(dict(zip(colunas, valores)))
    return registros


def consumo_da_serie(tsv: Path, tarefa_id: str) -> dict[str, str] | None:
    """Última linha medida da tarefa em `docs/telemetria.tsv` (fonte única do número,
    `GOVERNANCA.md` §4.2). `nao_medido` e célula vazia não contam como medida."""
    for registro in reversed(_ler_tsv(tsv)):
        if registro.get("tarefa") != tarefa_id or registro.get("fonte") == "nao_medido":
            continue
        if all(registro.get(c, "") != "" for c in ("tool_uses", "tokens_k", "duracao_s")):
            return registro
    return None


def linhas_do_painel(progresso: Path, titulos: list[str]) -> list[str]:
    """As frases que `progresso_hook.py` gerou para os títulos dados, na ordem do arquivo. O
    título entre aspas duplas é o mesmo que o gancho escreve (`I-12` do `P-0748`)."""
    if not progresso.is_file():
        return []
    chaves = [f'"{t}"' for t in titulos if t]
    return [
        linha
        for linha in progresso.read_text(encoding="utf-8", errors="replace").splitlines()
        if any(chave in linha for chave in chaves)
    ]


def _secao_achados(linhas: list[str]) -> tuple[int, int] | None:
    """Índices `[ini, fim)` do corpo da seção `## Achados da execução` (sem o heading), ou None."""
    ini = next((i for i, l in enumerate(linhas) if ACHADOS_HEADING_RE.match(l)), None)
    if ini is None:
        return None
    fim = next((j for j in range(ini + 1, len(linhas)) if re.match(r"^#{1,2} ", linhas[j])), len(linhas))
    return ini + 1, fim


def achados_do_plano(plano_path: Path) -> list[tuple[str, str]]:
    """Entradas `AE-<n>` da seção de achados: (id, texto da entrada inteira, incluindo as linhas
    de continuação até o próximo bullet de nível zero ou heading)."""
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    faixa = _secao_achados(linhas)
    if faixa is None:
        return []
    ini, fim = faixa
    entradas: list[tuple[str, str]] = []
    atual: list[str] | None = None
    for linha in linhas[ini:fim]:
        if linha.startswith("- "):
            if atual:
                entradas.append(("\n".join(atual)))
            atual = [linha]
        elif atual is not None:
            atual.append(linha)
    if atual:
        entradas.append("\n".join(atual))
    resultado = []
    for texto in entradas:
        m = AE_ID_RE.search(texto.splitlines()[0])
        if m:
            resultado.append((f"AE-{m.group(1)}", texto))
    return resultado


ACHADO_PROCESSO_HEADING = "## Achado de processo"
_ACHADO_INSTRUMENTO_RE = re.compile(r"achado de processo \(instrumento\):\s*(?P<resto>.+)", re.IGNORECASE)
_TERMOS_DE_FALHA = ("queda", "traceback", "exceção", "excecao", "exception", "error")
_ACHADO_LINHA_RE = re.compile(r"^\|\s*(?P<alvo>[^|]+?)\s*\|\s*(?P<achado>.+?)\s*\|\s*$")


def achados_do_laudo(texto_laudo: str) -> list[tuple[str, str]]:
    """`(texto, rota)` por linha de dado da tabela `| alvo | achado |` da seção `## Achado de
    processo` do laudo (`rdo.py laudo` grava a seção sempre — corpo `nenhum` ou seção ausente
    devolve lista vazia). `texto` = `achado de processo (<alvo>): ` + o trecho antes da primeira
    ocorrência de `Rota:`, com `strip()`; `rota` = o trecho depois, com `strip()`, ou `não
    declarada no laudo` quando falta `Rota:` ou o trecho sai vazio."""
    if ACHADO_PROCESSO_HEADING not in texto_laudo:
        return []
    corpo = texto_laudo.split(ACHADO_PROCESSO_HEADING, 1)[1]
    m_fim = re.search(r"^## ", corpo, re.M)
    corpo = corpo[: m_fim.start()] if m_fim else corpo
    resultado: list[tuple[str, str]] = []
    for linha in corpo.splitlines():
        linha = linha.strip()
        if not linha.startswith("|"):
            continue
        m = _ACHADO_LINHA_RE.match(linha)
        if not m:
            continue
        alvo = m.group("alvo").strip()
        achado = m.group("achado").strip()
        if alvo.lower() == "alvo" or set(achado) <= {"-"}:
            continue
        if "Rota:" in achado:
            antes, depois = achado.split("Rota:", 1)
            texto = antes.strip()
            rota = depois.strip() or "não declarada no laudo"
        else:
            texto = achado
            rota = "não declarada no laudo"
        resultado.append((f"achado de processo ({alvo}): {texto}", rota))
    return resultado


# --------------------------------------------------------------------------- #
# Escritores auxiliares
# --------------------------------------------------------------------------- #


def _escrever_atomico(caminho: Path, texto: str) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    tmp = caminho.with_name(caminho.name + ".tmp")
    tmp.write_text(texto, encoding="utf-8", newline="\n")
    os.replace(tmp, caminho)


def apensar_achado(plano_path: Path, tarefa_id: str, texto: str, rota: str, data: str,
                   tiquete_id: str | None = None, origem: str | None = None) -> str:
    """Registro único do achado (`GOVERNANCA.md` §4.2): uma entrada `AE-<n>` com `**Rota:**`, ao
    fim de `## Achados da execução` do plano (a seção nasce se não existir). No diário, o achado
    de um card de tíquete entra no corpo da seção `## TK-<n>` do tíquete-pai, antes do primeiro
    card. O número é `max(AE-<k> do arquivo) + 1`, nunca reutilizado."""
    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    numeros = [int(n) for n in AE_ID_RE.findall("\n".join(linhas))]
    ae_id = f"AE-{max(numeros, default=0) + 1}"
    entrada = f"- **{ae_id}** (`{tarefa_id}`, fechamento, {data}) — {texto} **Rota:** {rota}"
    # Origem do achado, para o fechamento pular o já registrado pela linha do laudo e o
    # consultor citar a origem ao reescrever (R-19, DRF-21 do P-0755).
    if origem is not None:
        entrada += f" **Origem:** `{origem}`"

    if tiquete_id is not None:
        ini = next((i for i, l in enumerate(linhas) if l.startswith(f"## {tiquete_id} ")), None)
        if ini is None:
            raise EncerramentoError(f"achado: seção `## {tiquete_id}` não encontrada em '{plano_path}'")
        pos = next(
            (j for j in range(ini + 1, len(linhas)) if re.match(r"^#{1,3} ", linhas[j])), len(linhas)
        )
        while pos > ini + 1 and linhas[pos - 1].strip() == "":
            pos -= 1
        linhas[pos:pos] = [entrada, ""]
    else:
        faixa = _secao_achados(linhas)
        if faixa is None:
            while linhas and linhas[-1].strip() == "":
                linhas.pop()
            linhas += ["", "## Achados da execução", "", entrada]
        else:
            _, fim = faixa
            pos = fim
            while pos > faixa[0] and linhas[pos - 1].strip() == "":
                pos -= 1
            linhas.insert(pos, entrada)
    _escrever_atomico(plano_path, "\n".join(linhas) + "\n")
    return ae_id


def _gate_modelo(plano_path: Path, repo: Path) -> tuple[int, str]:
    """`modelo.py check`: exit 1 é defeito do modelo e recusa o fechamento (`DMC-30`); 0 e 2
    (forma anterior, sem modelo) seguem."""
    proc = subprocess.run(
        [sys.executable, str(KIT / "tools" / "modelo.py"), "check", "--plano", str(plano_path), "--root", str(repo)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if proc.returncode == 1:
        raise EncerramentoError(f"modelo: `modelo.py check` exit 1 — {proc.stderr.strip() or proc.stdout.strip()}")
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def _rel(caminho: Path, repo: Path) -> str:
    try:
        return caminho.resolve().relative_to(repo.resolve()).as_posix()
    except ValueError:
        return caminho.as_posix()


def _veredito_em_palavras(veredito: str, percentual: str, pendencia_laudo: str) -> str:
    if veredito == "aprovado":
        return f"Revisão: aprovada sem ressalva ({percentual}%)."
    frase = f"Revisão: aprovada com ressalva ({percentual}%)"
    if pendencia_laudo and pendencia_laudo != "nenhuma":
        frase += f"; pendência do laudo: {pendencia_laudo}"
    return frase + "."


# --------------------------------------------------------------------------- #
# Verbo `tarefa`
# --------------------------------------------------------------------------- #


def fechar_tarefa(
    repo: Path,
    plano_path: Path,
    tarefa_id: str,
    *,
    data: str,
    resumo: str | None = None,
    pendencia: str | None = None,
    achados: list[tuple[str, str]] | None = None,
    laudo_path: Path | None = None,
    consumo: tuple[str, str, str] | None = None,
    nao_medido: str | None = None,
    modelo_agente: str | None = None,
    progresso: Path | None = None,
    rdo_dir: Path | None = None,
    telemetria_tsv: Path | None = None,
    template: Path | None = None,
    esquema_legado: bool = False,
    modelo_legado: str | None = None,
    classe_legado: str | None = None,
) -> tuple[Path, str]:
    """Fecha a tarefa: checa tudo, depois status → RDO → telemetria → achados. Devolve
    (caminho do RDO, seção humana)."""
    plano_path = Path(plano_path)
    if not plano_path.is_file():
        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")
    modelo = _backlog.carregar(repo)
    alvo = _backlog._localizar(modelo, tarefa_id)
    if alvo is None or isinstance(alvo, _backlog.Plano):
        raise EncerramentoError(f"tarefa: '{tarefa_id}' não é tarefa nem card conhecido do backlog")
    if _rel(repo / alvo.arquivo, repo) != _rel(plano_path, repo):
        raise EncerramentoError(
            f"tarefa: '{tarefa_id}' mora em '{alvo.arquivo}', não em '{_rel(plano_path, repo)}'"
        )
    if alvo.status != "review":
        raise EncerramentoError(
            f"status: tarefa '{tarefa_id}' está '{alvo.status or 'ausente'}', exigido 'review' "
            "(única transição que produz RDO)"
        )

    try:
        dossie = _rdo.extrair_dossie(
            plano_path, tarefa_id, esquema_legado=esquema_legado,
            modelo_legado=modelo_legado, classe_legado=classe_legado,
        )
    except _rdo.RdoValidationError as exc:
        raise EncerramentoError(f"dossiê: {exc}") from exc

    pasta = _caminhos.pasta_do_plano(plano_path)
    plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem
    if laudo_path is None:
        laudo_path = (
            _caminhos.destino_laudo(pasta, tarefa_id) if pasta is not None
            else repo / "docs" / "RDO" / "laudos" / f"{plano_id}-{tarefa_id}.md"
        )
    pacote = ler_laudo(Path(laudo_path))
    texto_laudo = Path(laudo_path).read_text(encoding="utf-8")
    if pacote["veredito"] not in ("aprovado", "ressalva"):
        raise EncerramentoError(
            f"laudo: veredito '{pacote['veredito']}' não é desfecho de RDO — materialize `blocked` "
            "razão premissa e leve à triagem (GOVERNANCA.md §4.2)"
        )

    tsv = Path(telemetria_tsv) if telemetria_tsv is not None else repo / "docs" / "telemetria.tsv"
    if consumo is not None and nao_medido is not None:
        raise EncerramentoError("consumo: --tool-uses/--tokens-k/--duracao-s e --nao-medido não vêm juntos")

    linha_telemetria: str | None = None
    razao_nao_medido: str | None = None
    if nao_medido is not None:
        razao_nao_medido = nao_medido.strip()
        if not razao_nao_medido or len(nao_medido.strip().splitlines()) > 1:
            raise EncerramentoError("consumo: nao-medido é uma linha não vazia")
        if consumo_da_serie(tsv, tarefa_id) is not None:
            raise EncerramentoError(
                f"consumo: '{tarefa_id}' já tem medida em '{_rel(tsv, repo)}' — medida existente não se descarta"
            )
        args_tsv = argparse.Namespace(
            data=data, projeto=repo.name, tarefa=tarefa_id,
            modelo=modelo_agente or dossie.modelo, tool_uses="", tokens_k="", duracao_s="",
            fonte="nao_medido",
        )
        try:
            linha_telemetria = _telemetria.build_row(args_tsv)
        except _telemetria.TelemetriaValidationError as exc:
            raise EncerramentoError(f"telemetria: {exc}") from exc
        tool_uses = tokens_k = duracao_s = None
    elif consumo is not None:
        tool_uses, tokens_k, duracao_s = consumo
        args_tsv = argparse.Namespace(
            data=data, projeto=repo.name, tarefa=tarefa_id,
            modelo=modelo_agente or dossie.modelo, tool_uses=tool_uses, tokens_k=tokens_k,
            duracao_s=duracao_s, fonte="usage",
        )
        try:
            linha_telemetria = _telemetria.build_row(args_tsv)
        except _telemetria.TelemetriaValidationError as exc:
            raise EncerramentoError(f"telemetria: {exc}") from exc
    else:
        registro = consumo_da_serie(tsv, tarefa_id)
        if registro is None:
            raise EncerramentoError(
                f"consumo: sem linha medida de '{tarefa_id}' em '{_rel(tsv, repo)}' e sem "
                "--tool-uses/--tokens-k/--duracao-s nem --nao-medido — número não medido não fecha tarefa"
            )
        tool_uses, tokens_k, duracao_s = registro["tool_uses"], registro["tokens_k"], registro["duracao_s"]

    # A checagem do destino do RDO (existência) e do template não é mais cópia própria: sai de
    # `rdo.checar_close`, chamada aqui com `status_exigido="review"` — a tarefa ainda não foi
    # fechada — para que essa recusa (hoje só do `rdo.py close`) saia antes do `done` (`TK-88d`).
    args_precheck = argparse.Namespace(
        plano=str(plano_path), tarefa=tarefa_id,
        tool_uses=str(tool_uses) if razao_nao_medido is None else None,
        tokens_k=str(tokens_k) if razao_nao_medido is None else None,
        duracao_s=str(duracao_s) if razao_nao_medido is None else None,
        nao_medido=razao_nao_medido,
        template=template, rdo_dir=str(rdo_dir) if rdo_dir is not None else None,
        esquema_legado=esquema_legado, modelo=modelo_legado, classe=classe_legado,
    )
    try:
        destino_rdo = _rdo.checar_close(args_precheck, "review")
    except _rdo.RdoValidationError as exc:
        raise EncerramentoError(f"rdo: {exc}") from exc
    if linha_telemetria is not None:
        try:
            _telemetria.checar_repetida(tsv, linha_telemetria)
        except _telemetria.TelemetriaRepetidaError as exc:
            raise EncerramentoError(f"telemetria: {exc}") from exc
    for rotulo, valor in (("pendencia", pendencia), ("resumo", resumo)):
        if valor is not None and len(valor.strip().splitlines()) > 1:
            raise EncerramentoError(f"{rotulo}: aceita no máximo uma linha")
    for texto, rota in achados or []:
        if not texto.strip() or not rota.strip():
            raise EncerramentoError("achado: texto e rota são obrigatórios e não vazios")

    _gate_modelo(plano_path, repo)

    # --- checagens concluídas; escritas a partir daqui --------------------------------
    pai, tipo_pai = _backlog._pai_do_alvo(modelo, alvo)
    rdo_rel = _rel(destino_rdo, repo)
    nota = f"fechada por `encerrar.py`: RDO `{rdo_rel}`, veredito {pacote['veredito']} {pacote['percentual']}%"
    resultado = _backlog.transacionar_status(repo, modelo, tarefa_id, "done", nota=nota)
    if resultado.exit_code != 0:
        raise EncerramentoError(f"status: {resultado.mensagem}")

    done, total = _backlog._done_total(pai.tarefas if tipo_pai == "plano" else pai.filhos)
    proxima_id = _backlog._proxima_do_pai(modelo, pai, tipo_pai)
    proxima = next(
        (f.titulo for f in (pai.tarefas if tipo_pai == "plano" else pai.filhos) if f.id == proxima_id), None
    )
    humano_linhas = [f'Tarefa "{dossie.titulo}" concluída em {data}.']
    if resumo:
        humano_linhas.append(resumo.strip())
    humano_linhas.append(_veredito_em_palavras(pacote["veredito"], pacote["percentual"], pacote["pendencia"]))
    humano_linhas.append(f"Pendência para o dono: {pendencia.strip() if pendencia else 'nenhuma'}.")
    humano_linhas.append(
        f'{"Plano" if tipo_pai == "plano" else "Tíquete"} "{pai.titulo}": {done}/{total} tarefas concluídas; '
        + (f'próxima: "{proxima}".' if proxima else "nenhuma tarefa pronta na fila dele.")
    )
    ids_achados: list[str] = []
    if _backlog.extrair_handover(alvo) is not None:
        humano_linhas.append("Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.")
    if achados:
        humano_linhas.append(
            f"Achado{'s' if len(achados) > 1 else ''} registrado{'s' if len(achados) > 1 else ''} no plano, "
            f"com rota: {len(achados)} (ver seção de achados da execução)."
        )

    progresso_path = Path(progresso) if progresso is not None else repo / ".claude" / "estado" / "progresso.txt"
    historico = linhas_do_painel(progresso_path, [dossie.titulo])

    args_close = argparse.Namespace(
        plano=str(plano_path), tarefa=tarefa_id,
        tool_uses=str(tool_uses) if razao_nao_medido is None else None,
        tokens_k=str(tokens_k) if razao_nao_medido is None else None,
        duracao_s=str(duracao_s) if razao_nao_medido is None else None,
        nao_medido=razao_nao_medido,
        veredito=pacote["veredito"], percentual=int(pacote["percentual"]),
        bloqueante=pacote["bloqueante"], recomendacao=pacote["recomendacao"],
        pendencia_laudo=pacote["pendencia"], pendencia=pendencia,
        licoes_aprendidas=pacote["licoes"] or None,
        humano="\n".join(humano_linhas),
        historico="\n".join(historico) if historico else None,
        rdo_dir=str(rdo_dir) if rdo_dir is not None else None,
        template=template, esquema_legado=esquema_legado,
        modelo=modelo_legado, classe=classe_legado,
    )
    try:
        destino = _rdo.cmd_close(args_close)
    except _rdo.RdoValidationError as exc:
        raise EncerramentoError(f"rdo: {exc} (status já materializado como done — corrija e rode `rdo.py close`)") from exc

    if linha_telemetria is not None:
        _telemetria.append_row(tsv, linha_telemetria)

    tiquete_id = pai.id if tipo_pai == "tiquete" else None
    for texto, rota in achados or []:
        ids_achados.append(apensar_achado(plano_path, tarefa_id, texto.strip(), rota.strip(), data, tiquete_id=tiquete_id))

    textos_gravados = {texto.strip() for texto, _ in achados or []}
    entradas_existentes = "\n".join(texto for _, texto in achados_do_plano(plano_path))
    achados_laudo = achados_do_laudo(texto_laudo)
    for n, (texto, rota) in enumerate(achados_laudo, start=1):
        origem = f"laudo:{tarefa_id}#{n}"
        if f"`{origem}`" in entradas_existentes or texto in entradas_existentes or texto in textos_gravados:
            continue
        ids_achados.append(
            apensar_achado(plano_path, tarefa_id, texto, rota, data, tiquete_id=tiquete_id, origem=origem)
        )
        textos_gravados.add(texto)

    humano = "\n".join(humano_linhas)
    if ids_achados:
        humano += f"\nAchados: {', '.join(ids_achados)}."
    humano += f"\nDetalhe: `{rdo_rel}`."
    for texto, _rota in achados_laudo:
        m = _ACHADO_INSTRUMENTO_RE.search(texto)
        if m and any(termo in m.group("resto").lower() for termo in _TERMOS_DE_FALHA):
            humano += f"\nencerrar: B1 — achado de instrumento com falha: {m.group('resto')}"
    return destino, humano


# --------------------------------------------------------------------------- #
# Verbo `handover`
# --------------------------------------------------------------------------- #

HANDOVER_STATUS_PERMITIDOS = ("in-progress", "review", "done", "blocked")


def montar_handover(
    data: str,
    entregue: str,
    contrato: str,
    nao_refazer: str | None = None,
    pendente: str | None = None,
    para: list[str] | None = None,
) -> str:
    """O campo `- **Handover:**` do card — inteiramente de máquina: rótulos fixos, uma linha por
    rótulo, destinatários entre crases. `Entregue` diz o que existe agora, com `caminho:linha`;
    `Contrato` diz com o que quem vem depois pode contar; `Não refazer` o que já está pago;
    `Pendente` o que fica de propósito para a sucessora."""
    for rotulo, valor in (("entregue", entregue), ("contrato", contrato), ("nao-refazer", nao_refazer), ("pendente", pendente)):
        if valor is not None and (not valor.strip() or len(valor.strip().splitlines()) > 1):
            raise EncerramentoError(f"handover: `{rotulo}` é uma linha não vazia")
    destinatarios = ", ".join(f"`{p.strip()}`" for p in (para or []) if p.strip())
    cabecalho = f"- **Handover:** {data} · para {destinatarios or 'quem vier depois'}"
    linhas = [
        cabecalho,
        f"  - **Entregue:** {entregue.strip()}",
        f"  - **Contrato:** {contrato.strip()}",
        f"  - **Não refazer:** {nao_refazer.strip() if nao_refazer else 'nada a declarar'}",
        f"  - **Pendente:** {pendente.strip() if pendente else 'nenhum'}",
    ]
    return "\n".join(linhas)


def escrever_handover(
    repo: Path,
    plano_path: Path,
    tarefa_id: str,
    *,
    data: str,
    entregue: str,
    contrato: str,
    nao_refazer: str | None = None,
    pendente: str | None = None,
    para: list[str] | None = None,
) -> str:
    """Registra o handover **na própria tarefa** (card do plano ou do diário), como campo
    `- **Handover:**` antes de `- **Notas de execução:**` — ou ao fim do card, sem notas. Campo
    já existente é **substituído** (o handover é o estado corrente, não um diário). Exige
    entrega na árvore: status em `in-progress`, `review`, `done` ou `blocked`. Devolve o texto."""
    plano_path = Path(plano_path)
    if not plano_path.is_file():
        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")
    modelo = _backlog.carregar(repo)
    alvo = _backlog._localizar(modelo, tarefa_id)
    if alvo is None or isinstance(alvo, _backlog.Plano):
        raise EncerramentoError(f"tarefa: '{tarefa_id}' não é tarefa nem card conhecido do backlog")
    if _rel(repo / alvo.arquivo, repo) != _rel(plano_path, repo):
        raise EncerramentoError(f"tarefa: '{tarefa_id}' mora em '{alvo.arquivo}', não em '{_rel(plano_path, repo)}'")
    if alvo.status not in HANDOVER_STATUS_PERMITIDOS:
        raise EncerramentoError(
            f"status: tarefa '{tarefa_id}' está '{alvo.status or 'ausente'}' — handover exige entrega na árvore "
            f"({', '.join(HANDOVER_STATUS_PERMITIDOS)})"
        )
    texto = montar_handover(data, entregue, contrato, nao_refazer, pendente, para)

    linhas = plano_path.read_text(encoding="utf-8").splitlines()
    ini, fim = alvo.linha_header - 1, alvo.linha_fim  # índices 0-based: [ini, fim)
    card = linhas[ini:fim]
    # Remove o campo anterior, se houver (bullet de topo + linhas indentadas que o seguem).
    k = next((i for i, l in enumerate(card) if _backlog.HANDOVER_BULLET_RE.match(l)), None)
    if k is not None:
        j = k + 1
        while j < len(card) and card[j][:1] in (" ", "\t") and card[j].strip():
            j += 1
        del card[k:j]
    pos = next((i for i, l in enumerate(card) if _backlog.NOTAS_BULLET_RE.match(l)), None)
    if pos is None:
        pos = len(card)
        while pos > 1 and card[pos - 1].strip() == "":
            pos -= 1
    card[pos:pos] = texto.splitlines()
    linhas[ini:fim] = card
    _escrever_atomico(plano_path, "\n".join(linhas) + "\n")
    return texto


# --------------------------------------------------------------------------- #
# Verbo `plano`
# --------------------------------------------------------------------------- #


def _rdo_da_tarefa(repo: Path, plano_path: Path, plano_id: str, tarefa_id: str, rdo_dir: Path | None) -> Path | None:
    pasta = _caminhos.pasta_do_plano(plano_path)
    if pasta is not None and rdo_dir is None:
        destino = _caminhos.destino_rdo(pasta, tarefa_id)
        return destino if destino.is_file() else None
    base = Path(rdo_dir) if rdo_dir is not None else repo / "docs" / "RDO"
    candidatos = sorted(base.glob(f"{plano_id}-{tarefa_id}-*.md"))
    return candidatos[0] if candidatos else None


def _consumo_do_plano(tsv: Path, plano_id: str, ids: list[str]) -> dict[str, dict[str, float]]:
    """Agregado por papel da série de telemetria: `<ID>` executor, `<ID>-revisao` revisor,
    `*-consultor-*` consultor, `<P-n>-planejador` planejador, `<P-n>-modelador` modelador,
    `<P-n>-scout` scout, o resto em `outros`. Célula vazia não soma."""
    grupos: dict[str, dict[str, float]] = {
        p: {"linhas": 0, "tool_uses": 0, "tokens_k": 0.0}
        for p in ("executor", "revisor", "consultor", "planejador", "modelador", "scout", "outros")
    }
    for registro in _ler_tsv(tsv):
        tarefa = registro.get("tarefa", "")
        base = tarefa.split("-revisao")[0].split("-consultor")[0]
        if base not in ids and not tarefa.startswith(plano_id + "-"):
            continue
        if tarefa in ids:
            papel = "executor"
        elif tarefa.endswith("-revisao"):
            papel = "revisor"
        elif "-consultor" in tarefa:
            papel = "consultor"
        elif tarefa.endswith("-planejador"):
            papel = "planejador"
        elif tarefa.endswith("-modelador"):
            papel = "modelador"
        elif tarefa.endswith("-scout"):
            papel = "scout"
        else:
            papel = "outros"
        g = grupos[papel]
        g["linhas"] += 1
        try:
            g["tool_uses"] += int(registro.get("tool_uses") or 0)
        except ValueError:
            pass
        try:
            g["tokens_k"] += float(registro.get("tokens_k") or 0)
        except ValueError:
            pass
    return grupos


def fechar_plano(
    repo: Path,
    plano_path: Path,
    *,
    veredito: str,
    data: str,
    resumo: str | None = None,
    operacoes: Path | None = None,
    saida: Path | None = None,
    progresso: Path | None = None,
    rdo_dir: Path | None = None,
    telemetria_tsv: Path | None = None,
) -> tuple[Path, str]:
    """Fecha o plano: checa tudo, depois status → relatório de entrega → linha do diário.
    Devolve (caminho do relatório, seção humana)."""
    plano_path = Path(plano_path)
    if not plano_path.is_file():
        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")
    if not veredito or not veredito.strip():
        raise EncerramentoError("veredito: a frase do dono é obrigatória, verbatim")
    plano_id = _caminhos.id_do_plano(plano_path)
    if plano_id is None:
        raise EncerramentoError(f"plano: '{plano_path}' não tem id de plano no nome (P-<n>)")
    modelo = _backlog.carregar(repo)
    plano = _backlog._localizar(modelo, plano_id)
    if not isinstance(plano, _backlog.Plano):
        raise EncerramentoError(f"plano: '{plano_id}' não está no backlog carregado de '{repo}'")
    if plano.status in ("done", "cancelled", "superseded"):
        raise EncerramentoError(f"status: plano '{plano_id}' já está '{plano.status}'")

    # A regra de plano `done` (tarefa não terminal recusa, plano sem nenhuma `done` recusa) não
    # é mais cópia própria: sai de `backlog.checar_transicao`, a mesma checagem que
    # `transacionar_status` faz antes de escrever (`TK-88d`).
    resultado_transicao = _backlog.checar_transicao(modelo, plano_id, "done")
    if resultado_transicao is not None:
        raise EncerramentoError(resultado_transicao.mensagem)
    concluidas = [t for t in plano.tarefas if t.status == "done"]

    rdos: dict[str, Path | None] = {t.id: _rdo_da_tarefa(repo, plano_path, plano_id, t.id, rdo_dir) for t in concluidas}
    sem_rdo = [tid for tid, p in rdos.items() if p is None]
    if sem_rdo:
        raise EncerramentoError(f"rdo: tarefa(s) done sem RDO: {', '.join(sem_rdo)} — tarefa sem RDO não está fechada")

    achados = achados_do_plano(plano_path)
    sem_rota = [ae for ae, texto in achados if not ROTA_RE.search(texto)]
    if sem_rota:
        raise EncerramentoError(f"achados: sem `**Rota:**`: {', '.join(sem_rota)} — plano não fecha com achado sem rota")

    operacoes_path = Path(operacoes) if operacoes is not None else _caminhos.destino_operacoes(repo, plano_path)
    if not operacoes_path.is_file():
        raise EncerramentoError(
            f"operacoes: documento de validação não encontrado '{_rel(operacoes_path, repo)}' — "
            "rode a skill `entrega-de-encerramento` antes, ou aponte --operacoes"
        )

    saida_path = Path(saida) if saida is not None else _caminhos.destino_entrega(repo, plano_path)
    if saida_path.exists():
        raise EncerramentoError(f"saida: '{_rel(saida_path, repo)}' já existe — plano já fechado")
    if resumo is not None and len(resumo.strip().splitlines()) > 1:
        raise EncerramentoError("resumo: aceita no máximo uma linha")

    exit_modelo, saida_modelo = _gate_modelo(plano_path, repo)
    piso_c11, violacoes = _backlog.ler_piso_c11(repo)
    violacoes += _backlog.check(
        modelo, inbox_planos=_caminhos.inbox_planos(repo), repo=repo, piso_c11=piso_c11, dossie=True,
    )

    # --- checagens concluídas; escritas a partir daqui --------------------------------
    resultado = _backlog.transacionar_status(repo, modelo, plano_id, "done")
    if resultado.exit_code != 0:
        raise EncerramentoError(f"status: {resultado.mensagem}")

    total = len(plano.tarefas)
    canceladas = total - len(concluidas)
    tsv = Path(telemetria_tsv) if telemetria_tsv is not None else repo / "docs" / "telemetria.tsv"
    consumo = _consumo_do_plano(tsv, plano_id, [t.id for t in plano.tarefas])
    tokens_total = sum(g["tokens_k"] for g in consumo.values())
    linhas_total = int(sum(g["linhas"] for g in consumo.values()))

    linhas_rdo = []
    aprovadas = ressalvas = 0
    for t in plano.tarefas:
        if t.status == "done":
            rdo_path = rdos[t.id]
            conteudo = rdo_path.read_text(encoding="utf-8") if rdo_path else ""
            campos = {k: (r.search(conteudo).group(1) if r.search(conteudo) else "?") for k, r in _RDO_RES.items()}
            aprovadas += campos["veredito"] == "aprovado"
            ressalvas += campos["veredito"] == "ressalva"
            linhas_rdo.append(
                f"| `{t.id}` | {t.titulo} | done | {campos['veredito']} | {campos['percentual']}% | "
                f"{campos['desdobramento']} | `{_rel(rdo_path, repo) if rdo_path else '—'}` |"
            )
        else:
            linhas_rdo.append(f"| `{t.id}` | {t.titulo} | {t.status} | — | — | — | — |")

    operacoes_rel = _rel(operacoes_path, repo)
    entrega_rel = _rel(saida_path, repo)
    modelo_palavras = "sem modelo (plano anterior à doutrina)" if exit_modelo == 2 else "modelo conferido sem violação"
    check_palavras = "sem violação" if not violacoes else f"{len(violacoes)} violação(ões)"

    humano_linhas = [f'Plano "{plano.titulo}" fechado em {data}, pelo aceite do dono: "{veredito.strip()}".']
    if resumo:
        humano_linhas.append(resumo.strip())
    humano_linhas.append(
        f"Tarefas: {len(concluidas)} concluídas de {total}"
        + (f", {canceladas} cancelada{'s' if canceladas > 1 else ''}" if canceladas else "")
        + f"; aprovadas sem ressalva: {aprovadas}; com ressalva: {ressalvas}."
    )
    humano_linhas.append(
        f"Achados da execução: {len(achados)}, todos com rota." if achados else "Achados da execução: nenhum."
    )
    humano_linhas.append(f"Documento de validação: `{operacoes_rel}`.")
    humano_linhas.append(f"Instrumentos no fechamento: {modelo_palavras}; gramática do diário: {check_palavras}.")
    humano_linhas.append(
        f"Consumo do plano na série de telemetria: {tokens_total:.1f} mil tokens em {linhas_total} linha(s)."
        if linhas_total else "Consumo do plano: nenhuma linha na série de telemetria."
    )
    humano = "\n".join(humano_linhas)

    consumo_tabela = "\n".join(
        f"| {papel} | {int(g['linhas'])} | {int(g['tool_uses'])} | {g['tokens_k']:.1f} |"
        for papel, g in consumo.items()
    )
    achados_texto = "\n".join(texto for _, texto in achados) if achados else "(nenhum)"
    violacoes_texto = "\n".join(f"- {v}" for v in violacoes[:50]) if violacoes else "(nenhuma)"
    if len(violacoes) > 50:
        violacoes_texto += f"\n- … e mais {len(violacoes) - 50}"

    titulos = [plano.titulo] + [t.titulo for t in plano.tarefas]
    progresso_path = Path(progresso) if progresso is not None else repo / ".claude" / "estado" / "progresso.txt"
    historico = linhas_do_painel(progresso_path, titulos)

    maquina = "\n".join([
        f"**Plano:** `{_rel(plano_path, repo)}` · **Id:** `{plano_id}` · **Fechado em:** {data}",
        f"**Veredito do dono (verbatim):** {veredito.strip()}",
        f"**Documento de validação:** `{operacoes_rel}`",
        f"**Gate do modelo:** `modelo.py check` exit {exit_modelo}" + (f" — {saida_modelo}" if saida_modelo else ""),
        f"**Gramática do backlog:** `backlog.py check` — {check_palavras}",
        "",
        "## Tarefas",
        "",
        "| tarefa | título | status | veredito | percentual | desdobramento | RDO |",
        "|---|---|---|---|---|---|---|",
        *linhas_rdo,
        "",
        "## Achados da execução (verbatim do plano)",
        "",
        achados_texto,
        "",
        f"## Consumo (`{_rel(tsv, repo)}`)",
        "",
        "| papel | linhas | tool uses | mil tokens |",
        "|---|---|---|---|",
        consumo_tabela,
        f"| **total** | {linhas_total} | {int(sum(g['tool_uses'] for g in consumo.values()))} | {tokens_total:.1f} |",
        "",
        "## Violações do `check` no fechamento",
        "",
        violacoes_texto,
    ])
    historico_texto = "\n".join(historico) if historico else "(nenhuma linha do painel para este plano)"
    documento = "\n".join([
        f"# Entrega — {plano_id} · {plano.titulo}",
        "",
        "# Humano",
        "",
        humano,
        "",
        "# Máquina",
        "",
        maquina,
        "",
        "# Histórico",
        "",
        historico_texto,
        "",
    ])
    _escrever_atomico(saida_path, documento)

    diario_path = repo / modelo.diario_arquivo
    diario_linhas = diario_path.read_text(encoding="utf-8").splitlines()
    # Conta como o índice conta (`_done_total`, `TK-88d`): tarefas `cancelled` saem do total.
    done_indice, total_indice = _backlog._done_total(plano.tarefas)
    linha_diario = (
        f"**`{plano_id}` — FECHADO `done` {done_indice}/{total_indice} em {data}, pelo aceite do dono** "
        f"(*\"{veredito.strip()}\"*). Entrega: `{entrega_rel}` · validação: `{operacoes_rel}`."
    )
    pos = next((i for i, l in enumerate(diario_linhas) if _backlog.DIRETIVA_RE.match(l)), 0)
    diario_linhas[pos + 1:pos + 1] = ["", linha_diario]
    _escrever_atomico(diario_path, "\n".join(diario_linhas) + "\n")

    return saida_path, humano + f"\nEntrega: `{entrega_rel}`."


# --------------------------------------------------------------------------- #
# marco — OP-12: o veredito do dono em todos os lugares onde o marco aparece
# --------------------------------------------------------------------------- #


_MARCO_SECAO0_RE = re.compile(r"^## 0\.")
_MARCO_HEADING_RE = re.compile(r"^## ")
_MARCO_COLUNA_RE = re.compile(r"(?<!\\)\|")
_SOMENTE_DIGITOS_RE = re.compile(r"^\d+$")


def _dossie_emenda(
    plano_path: Path, repo: Path, marco: int, frase: str, fato_novo: str, restricao: str,
    devolver: str,
) -> str:
    """O dossiê `Ato: emenda` para o modelador (`OP-12`/`RAF-T23`): motivo do marco, o fato que
    muda o modelo e a restrição que a emenda tem de respeitar. O `Devolver` difere entre a
    recusa da versão e o conflito na promoção (`RAF-T23b`)."""
    return "\n".join([
        f"Plano: {_rel(plano_path, repo)}",
        "Ato: emenda",
        f'Motivo: Marco {marco}, veredito do dono: "{frase}"',
        f"Fato novo: {fato_novo}",
        f"Restrição: {restricao}",
        f"Devolver: {devolver}",
    ])


def _faixa_do_campo_operacao(linhas: list[str], tarefa_id: str) -> tuple[int, int] | None:
    """O card vai do cabeçalho `### <ID> — ` até a linha antes do próximo `### ` ou `## `.
    Devolve `(linha do campo Operação do modelo, primeira linha depois dos sub-bullets)`, ou
    `None` sem card ou sem campo (`RAF-T23`)."""
    prefixo = f"### {tarefa_id} — "
    idx_card = next((i for i, l in enumerate(linhas) if l.startswith(prefixo)), None)
    if idx_card is None:
        return None
    fim_card = next(
        (
            i
            for i in range(idx_card + 1, len(linhas))
            if linhas[i].startswith("### ") or linhas[i].startswith("## ")
        ),
        len(linhas),
    )
    idx_campo = next(
        (
            i
            for i in range(idx_card + 1, fim_card)
            if linhas[i].startswith("- **Operação do modelo:**")
        ),
        None,
    )
    if idx_campo is None:
        return None
    fim_campo = idx_campo + 1
    while fim_campo < fim_card and linhas[fim_campo].startswith("  "):
        fim_campo += 1
    return idx_campo, fim_campo


def promover_versao(linhas: list[str], k: int, data: str) -> tuple[list[str], int]:
    """`DRF-38` (`RAF-T23`) — promove a versão pendente (`## 1A`) a vigente (`## 1`): no
    registro de versões, a linha `vigente` cai a `obsoleta` (com o motivo na célula `por`) e a
    linha da versão `k` sobe a `vigente`; a `## 1` vira o conteúdo da `## 1A` (cabeçalho
    `situação: vigente`) e a `## 1A` sai do plano; o campo `Operação do modelo` de cada card
    citado nas `tarefas:` da pendente é reescrito com as operações e contratos dela. Devolve as
    linhas e o número de cards distintos reescritos."""
    linhas = list(linhas)

    modelo_pendente = _modelo.extrair_modelo(linhas, _modelo._HEADING_PENDENTE)
    obj_por_nome = {o.nome: o for o in modelo_pendente.objetos}

    idx_h1 = linhas.index(_modelo._HEADING_VIGENTE)
    fim_h1 = next(
        (i for i in range(idx_h1 + 1, len(linhas)) if linhas[i].startswith("## ")), len(linhas)
    )
    idx_h1a = linhas.index(_modelo._HEADING_PENDENTE)
    fim_h1a = next(
        (i for i in range(idx_h1a + 1, len(linhas)) if linhas[i].startswith("## ")), len(linhas)
    )

    tabela_registro = _modelo._extrair_tabela(linhas[idx_h1:fim_h1], "### 1.4 Registro de versões")
    cabecalho_tab, separador_tab = tabela_registro[0], tabela_registro[1]
    linhas_dados: list[str] = []
    for linha_tab in tabela_registro[2:]:
        celulas = _modelo._parse_linha_tabela(linha_tab)
        if celulas[2] == "vigente":
            celulas[2] = "obsoleta"
            celulas[3] = f"{celulas[3]}; Caiu pelo aceite da versão {k} em {data}"
        elif celulas[0] == str(k) and celulas[2] == "pendente":
            celulas[2] = "vigente"
        linhas_dados.append("| " + " | ".join(celulas) + " |")

    conteudo_1a = linhas[idx_h1a + 1 : fim_h1a]
    idx_1_4_1a = next(
        (i for i, l in enumerate(conteudo_1a) if l.startswith("### 1.4")), len(conteudo_1a)
    )
    conteudo_1a = conteudo_1a[:idx_1_4_1a]
    while conteudo_1a and conteudo_1a[-1].strip() == "":
        conteudo_1a.pop()
    conteudo_1a = [
        l.replace("situação: pendente", "situação: vigente")
        if l.startswith("**Estado do modelo:**")
        else l
        for l in conteudo_1a
    ]

    novo_bloco = (
        [_modelo._HEADING_VIGENTE]
        + conteudo_1a
        + ["", "### 1.4 Registro de versões", "", cabecalho_tab, separador_tab]
        + linhas_dados
        + [""]
    )
    linhas[idx_h1:fim_h1a] = novo_bloco

    cards: dict[str, list] = {}
    for operacao in modelo_pendente.operacoes:
        for tid in operacao.tarefas:
            cards.setdefault(tid, []).append(operacao)

    cards_reescritos = 0
    for tid, operacoes in cards.items():
        campo_idx, fim_idx = _faixa_do_campo_operacao(linhas, tid)
        ids_op = ", ".join(f"`OP-{op.numero}`" for op in operacoes)
        novas = [f"- **Operação do modelo:** {ids_op}"]
        for op in operacoes:
            novas.append(f"  - OP-{op.numero}: {op.texto}")
            pares = "; ".join(f"{nome} — {obj_por_nome[nome].contrato}" for nome in op.precisa_de)
            novas.append(f"  - precisa de: {pares}")
        linhas[campo_idx:fim_idx] = novas
        cards_reescritos += 1

    return linhas, cards_reescritos


def _checar_promocao(
    linhas: list[str],
    plano: "_backlog.Plano",
    k: str,
    marco: int,
    frase: str,
    plano_path: Path,
    repo: Path,
) -> None:
    """Checagens da promoção da versão aceita (`DRF-38`, `RAF-T23`), todas antes de qualquer
    escrita: o número da versão, a `## 1A` ser a versão pedida, o registro de versões ter um
    único vigente e a linha pendente da versão, a versão pendente sem violação e todo card
    citado com o campo `Operação do modelo` já existente."""
    if not _SOMENTE_DIGITOS_RE.match(k):
        raise EncerramentoError(f"--aceita-versao exige o número da versão, recebeu '{k}'")

    fato_novo_base = f"o dono aceitou a versão {k} do modelo no Marco {marco}."
    restricao = (
        f"a versão {k} passa a vigente e a anterior a obsoleta; o conteúdo da obsoleta sai "
        "do plano e o registro de versões guarda a linha (GOVERNANCA.md §3.2)."
    )

    def _conflito(razao: str) -> ConflitoDePromocao:
        dossie = _dossie_emenda(
            plano_path, repo, marco, frase,
            f"{fato_novo_base} Conflito na promoção: {razao}.",
            restricao,
            "a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do "
            "marco rodar de novo.",
        )
        return ConflitoDePromocao(f"conflito na promoção da versão {k} — {razao}", dossie)

    modelo_vigente = _modelo.extrair_modelo(linhas, _modelo._HEADING_VIGENTE)
    if modelo_vigente is None:
        raise _conflito("o plano não tem a ## 1")

    modelo_pendente = _modelo.extrair_modelo(linhas, _modelo._HEADING_PENDENTE)
    if modelo_pendente.versao != int(k):
        raise _conflito(f"a ## 1A é a versão {modelo_pendente.versao}")

    linhas_registro = [
        _modelo._parse_linha_tabela(l) for l in modelo_vigente.versoes if l.strip()
    ]
    situacoes = [celulas[2] for celulas in linhas_registro if len(celulas) >= 3]
    if situacoes.count("vigente") != 1:
        raise _conflito("o registro de versões não tem uma única linha vigente")

    tem_pendente_k = any(
        len(celulas) >= 3 and celulas[0] == k and celulas[2] == "pendente"
        for celulas in linhas_registro
    )
    if not tem_pendente_k:
        raise _conflito(f"o registro de versões não tem a linha pendente da versão {k}")

    violacoes = [f"1A: {v}" for v in _modelo.validar(modelo_pendente, plano, pendente=True)]
    if violacoes:
        raise EncerramentoError(f"versão pendente com violação — {'; '.join(violacoes)}")

    for operacao in modelo_pendente.operacoes:
        for tid in operacao.tarefas:
            if _faixa_do_campo_operacao(linhas, tid) is None:
                raise EncerramentoError(
                    f"card '{tid}' da lista tarefas: da OP-{operacao.numero} sem o campo "
                    "Operação do modelo no plano"
                )


def gravar_marco(
    repo: Path,
    plano_path: Path,
    *,
    marco: int,
    resultado: str,
    veredito: str,
    data: str,
    aceita_versao: str | None = None,
    recusa_versao: str | None = None,
    consultor: str | None = None,
) -> str | None:
    """OP-12/OP-23 — grava o veredito do dono nos lugares do marco (`DAF-27`): a última célula da
    linha `| **Marco <n>** |` da tabela de marcos, o fim da seção `## 0.` e, só quando
    `--marco 1 --resultado go` encontra o plano em `blocked`, a transição para `ready`. Com
    `--aceita-versao`, exige `consultor` e promove a versão sozinho (`_checar_promocao`,
    `promover_versao`, `DRF-38`); com `--recusa-versao`, devolve o dossiê `Ato: emenda` para o
    modelador. Todas as checagens correm antes de qualquer escrita."""
    plano_path = Path(plano_path)
    if not plano_path.is_file():
        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")

    linhas = plano_path.read_text(encoding="utf-8").splitlines()

    padrao_marco = re.compile(rf"^\|\s*\*\*Marco {marco}\*\*\s*\|")
    idx_marco = next((i for i, l in enumerate(linhas) if padrao_marco.match(l)), None)
    if idx_marco is None:
        raise EncerramentoError(f"linha do Marco {marco} ausente na tabela de marcos")

    idx_secao0 = next((i for i, l in enumerate(linhas) if _MARCO_SECAO0_RE.match(l)), None)
    if idx_secao0 is None:
        raise EncerramentoError("seção ## 0 ausente")

    # A `## 1A` se reconhece pela mesma regra do `modelo.py` (igualdade exata com
    # `_HEADING_PENDENTE`), não por prefixo — `AE-176`, `RAF-T23a` do `P-0755`.
    if (aceita_versao is not None or recusa_versao is not None) and not any(
        l == _modelo._HEADING_PENDENTE for l in linhas
    ):
        raise EncerramentoError("plano sem versão pendente (## 1A)")

    idx_prox_heading = next(
        (i for i in range(idx_secao0 + 1, len(linhas)) if _MARCO_HEADING_RE.match(linhas[i])),
        len(linhas),
    )

    plano_id = _caminhos.id_do_plano(plano_path)
    if plano_id is None:
        raise EncerramentoError(f"plano: '{plano_path}' não tem id de plano no nome (P-<n>)")
    modelo = _backlog.carregar(repo)
    plano = _backlog._localizar(modelo, plano_id)
    if not isinstance(plano, _backlog.Plano):
        raise EncerramentoError(f"plano: '{plano_id}' não está no backlog carregado de '{repo}'")

    # A escrita (3) é `transacionar_status`, que checa antes de escrever — mas depois das
    # escritas (1) e (2). As checagens dela correm aqui, antes da primeira escrita (`DAF-43`),
    # por `checar_transicao` (`TK-88d`). A outra checagem dela — a linha do plano em
    # `estado.tsv` — não precisa de prévia: plano em pasta só lê `blocked` dessa linha.
    tira_de_blocked = marco == 1 and resultado == "go" and plano.status == "blocked"
    if tira_de_blocked:
        previa = _backlog.checar_transicao(modelo, plano_id, "ready")
        if previa is not None:
            raise EncerramentoError(f"status: {previa.mensagem}")

    if aceita_versao is not None:
        if consultor is None or not consultor.strip():
            raise EncerramentoError(
                "--aceita-versao exige --consultor com a linha de validação do consultor"
            )
        if len(consultor.strip().splitlines()) > 1:
            raise EncerramentoError("consultor: aceita no máximo uma linha")
        _checar_promocao(
            linhas, plano, aceita_versao.strip(), marco, veredito.strip(), plano_path, repo
        )

    # --- checagens concluídas; escritas a partir daqui -----------------------------------
    frase = veredito.strip()
    frase_celula = frase.replace("|", "\\|")
    # Colunas GFM: `\|` não separa coluna. O verbo emite `\|` e precisa reler o que emite
    # (`DAF-43`: o split ingênuo no `|` deixava resto do veredito velho na célula).
    partes = _MARCO_COLUNA_RE.split(linhas[idx_marco])
    if aceita_versao is not None:
        consultor_celula = consultor.strip().replace("|", "\\|")
        partes[-2] = f' {resultado} · {data} — "{frase_celula}" · consultor: "{consultor_celula}" '
    else:
        partes[-2] = f' {resultado} · {data} — "{frase_celula}" '
    linhas[idx_marco] = "|".join(partes)

    bloco_secao0 = [
        f"**Marco {marco}, {data} — veredito do dono ({resultado}):**",
        "",
        f"> {frase}",
        "",
    ]
    linhas[idx_prox_heading:idx_prox_heading] = bloco_secao0

    cards_reescritos = None
    if aceita_versao is not None:
        linhas, cards_reescritos = promover_versao(linhas, int(aceita_versao.strip()), data)

    _escrever_atomico(plano_path, "\n".join(linhas) + "\n")

    if tira_de_blocked:
        resultado_status = _backlog.transacionar_status(
            repo, modelo, plano_id, "ready", nota=f"Marco {marco} go em {data}"
        )
        if resultado_status.exit_code != 0:
            raise EncerramentoError(f"status: {resultado_status.mensagem}")

    if aceita_versao is not None:
        return (
            f"marco: versão {aceita_versao.strip()} promovida — "
            f"{cards_reescritos} card(s) com a operação reescrita"
        )

    if recusa_versao is None:
        return None

    k = recusa_versao
    fato_novo = f"o dono recusou a versão {k} do modelo no Marco {marco}."
    restricao = (
        f"a versão {k} é eliminada e a vigente permanece, sem marca; o que foi entregue sob "
        "a versão recusada se refaz por card corretivo da operação afetada (GOVERNANCA.md §3.2)."
    )

    return _dossie_emenda(
        plano_path, repo, marco, frase, fato_novo, restricao,
        "a seção ## 1 depois do ato, com o registro de versões sem a linha da versão "
        "recusada, e o plano sem a ## 1A.",
    )


# --------------------------------------------------------------------------- #
# operacoes — OP-13: o esqueleto do relatório de operações sai por comando
# --------------------------------------------------------------------------- #


BLOCOS_OPERACAO = [
    "**Contexto que a motivou:**",
    "**O que é o artefato:**",
    "**Como funciona na prática:**",
    "**Protege contra:**",
]
_SECAO_OPERACAO_ID_RE = re.compile(r"^## `([^`]+)` — .*$", re.M)
_HEADING2_RE = re.compile(r"^## ", re.M)


def esqueleto_operacoes(plano: "_backlog.Plano") -> str:
    """O esqueleto do relatório de operações (`OP-13`): uma seção por tarefa não `cancelled`, na
    ordem do plano, com os quatro blocos vazios que a skill `entrega-de-encerramento` preenche
    depois. A tabela do arco cita toda tarefa, inclusive `cancelled`."""
    linhas = [
        f"# Operações — {plano.titulo}",
        "",
        "## Abertura",
        "",
        "**O problema:**",
        "",
        "**A solução, em uma frase:**",
        "",
        "| termo | o que é |",
        "|---|---|",
        "",
        "## O arco",
        "",
        "| estrato | pergunta que responde | tarefas |",
        "|---|---|---|",
        "",
        "| tarefa | título | status |",
        "|---|---|---|",
    ]
    for t in plano.tarefas:
        linhas.append(f"| `{t.id}` | {t.titulo} | {t.status} |")
    linhas.append("")
    for t in plano.tarefas:
        if t.status == "cancelled":
            continue
        linhas.append(f"## `{t.id}` — {t.titulo}")
        linhas.append("")
        for bloco in BLOCOS_OPERACAO:
            linhas.append(bloco)
            linhas.append("")
    linhas += [
        "## O que vale além deste plano",
        "",
        "| regra | o que resolve | residência |",
        "|---|---|---|",
        "",
        "## Os ganhos, medidos",
        "",
        "| medida | antes | depois |",
        "|---|---|---|",
        "",
        "## O padrão que a execução revelou",
        "",
        "## Pendências abertas ao fim do plano",
        "",
        "| pendência | por que ficou aberta | o que a fecha | bloqueia algo? |",
        "|---|---|---|---|",
    ]
    return "\n".join(linhas) + "\n"


def escrever_esqueleto_operacoes(repo: Path, plano_path: Path) -> Path:
    """Grava o esqueleto em `caminhos.destino_operacoes`; arquivo já existente é recusa — nada
    escrito."""
    # `AE-29` do `P-0753`: o parser faz `relative_to(repo)`, que recusa caminho relativo —
    # `--plano` relativo (a forma da skill `entrega-de-encerramento`) se resolve antes.
    plano_path = Path(plano_path).resolve()
    if not plano_path.is_file():
        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")
    plano = _backlog._parse_plano(plano_path, Path(repo).resolve())
    destino = _caminhos.destino_operacoes(repo, plano_path)
    if destino.exists():
        raise EncerramentoError(f"operacoes: já existe {_rel(destino, repo)}")
    _escrever_atomico(destino, esqueleto_operacoes(plano))
    return destino


def checar_esqueleto_operacoes(
    repo: Path, plano_path: Path
) -> tuple[list[str], list[str], list[str]]:
    """Confere a cobertura do esqueleto já gravado: `nao_citados` (todo `<ID>` de card do plano
    que não aparece no documento como `` `<ID>` ``), `sem_secao` (toda tarefa não `cancelled` sem
    a seção `` ## `<ID>` — `` — `DAF-44`: a tabela do arco já cita todo ID, então só esta lista
    acusa seção apagada) e `sem_blocos` (toda seção `` `<ID>` `` sem uma das quatro linhas de
    bloco)."""
    plano_path = Path(plano_path).resolve()
    destino = _caminhos.destino_operacoes(repo, plano_path)
    if not destino.is_file():
        raise EncerramentoError(f"operacoes: arquivo ausente {_rel(destino, repo)}")
    plano = _backlog._parse_plano(plano_path, Path(repo).resolve())
    texto = destino.read_text(encoding="utf-8")

    nao_citados = [t.id for t in plano.tarefas if f"`{t.id}`" not in texto]

    com_secao = {m.group(1) for m in _SECAO_OPERACAO_ID_RE.finditer(texto)}
    sem_secao = [t.id for t in plano.tarefas if t.status != "cancelled" and t.id not in com_secao]

    todas_headings = [m.start() for m in _HEADING2_RE.finditer(texto)]
    sem_blocos = []
    for m in _SECAO_OPERACAO_ID_RE.finditer(texto):
        inicio = m.end()
        fim = next((h for h in todas_headings if h > m.start()), len(texto))
        corpo = texto[inicio:fim]
        if any(bloco not in corpo for bloco in BLOCOS_OPERACAO):
            sem_blocos.append(m.group(1))
    return nao_citados, sem_secao, sem_blocos


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _forcar_utf8(stream) -> None:
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    parser = argparse.ArgumentParser(
        prog="encerrar.py",
        description="Fechamento mecânico de tarefa e de plano: artefatos e registros de backlog num comando (TK-88).",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    comuns = argparse.ArgumentParser(add_help=False)
    comuns.add_argument("--plano", required=True, help="Caminho do .md do plano (ou do diário, para card de tíquete).")
    comuns.add_argument("--repo", default=None, help="Raiz do repositório (default: a do próprio kit).")
    comuns.add_argument("--data", default=None, help="AAAA-MM-DD (default: hoje).")
    comuns.add_argument("--resumo", default=None, help="Uma frase em linguagem corrente para a seção Humano.")
    comuns.add_argument("--progresso", default=None, help="Arquivo do painel (default: .claude/estado/progresso.txt).")
    comuns.add_argument("--rdo-dir", dest="rdo_dir", default=None, help="Diretório dos RDO (default: docs/RDO ou a pasta do plano).")
    comuns.add_argument("--telemetria", default=None, help="Caminho do TSV (default: docs/telemetria.tsv).")

    p_tarefa = sub.add_parser("tarefa", parents=[comuns], help="Fecha uma tarefa em review: status, RDO (3 seções), telemetria, achados.")
    p_tarefa.add_argument("--tarefa", required=True, help="Identificador da tarefa (ex.: EBK-T4, TK-88a).")
    p_tarefa.add_argument("--pendencia", default=None, help="Pendência autoral do executor, uma linha.")
    p_tarefa.add_argument("--achado", nargs=2, action="append", metavar=("TEXTO", "ROTA"), default=None,
                          help="Achado de execução (repetível): texto e rota; vira AE-<n> com **Rota:** no plano.")
    p_tarefa.add_argument("--laudo", default=None, help="Caminho do laudo (default: <pasta>/laudos/<ID>.md ou docs/RDO/laudos/<plano>-<ID>.md).")
    p_tarefa.add_argument("--tool-uses", dest="tool_uses", default=None, help="Do bloco <usage>; com os três, a linha vai para a série.")
    p_tarefa.add_argument("--tokens-k", dest="tokens_k", default=None)
    p_tarefa.add_argument("--duracao-s", dest="duracao_s", default=None)
    p_tarefa.add_argument(
        "--nao-medido", dest="nao_medido", default=None,
        help="Fecha sem consumo medido: razão de uma linha, no lugar do trio — recusa junto dele, "
        "vazia/multilinha, ou quando a série já mede a tarefa (TK-88b).",
    )
    p_tarefa.add_argument("--modelo-agente", dest="modelo_agente", default=None, help="Modelo da linha de telemetria (default: o do cabeçalho do card).")
    p_tarefa.add_argument("--template", type=Path, default=None, help="Template do RDO (default: rdo_template.md do kit).")
    p_tarefa.add_argument("--esquema-legado", action="store_true", help="Cabeçalho sem [modelo · classe] — exige --modelo/--classe.")
    p_tarefa.add_argument("--modelo", default=None)
    p_tarefa.add_argument("--classe", default=None)

    p_handover = sub.add_parser("handover", help="Registra no card o que quem vem depois espera da tarefa: campo `- **Handover:**`, de máquina, que o `next` devolve à sucessora.")
    p_handover.add_argument("--plano", required=True, help="Caminho do .md do plano (ou do diário, para card de tíquete).")
    p_handover.add_argument("--tarefa", required=True, help="Identificador da tarefa.")
    p_handover.add_argument("--entregue", required=True, help="O que existe agora, com caminho:linha. Uma linha.")
    p_handover.add_argument("--contrato", required=True, help="Com o que quem vem depois pode contar. Uma linha.")
    p_handover.add_argument("--nao-refazer", dest="nao_refazer", default=None, help="O que já está pago. Uma linha.")
    p_handover.add_argument("--pendente", default=None, help="O que fica de propósito para a sucessora. Uma linha.")
    p_handover.add_argument("--para", action="append", default=None, help="Destinatário (id de tarefa ou papel); repetível. Sem ele: quem vier depois.")
    p_handover.add_argument("--repo", default=None)
    p_handover.add_argument("--data", default=None)

    p_plano = sub.add_parser("plano", parents=[comuns], help="Fecha um plano sem tarefa aberta: status, relatório de entrega (3 seções), linha do diário.")
    p_plano.add_argument("--veredito", required=True, help="Frase do dono que aceita o plano, verbatim.")
    p_plano.add_argument("--operacoes", default=None, help="Documento de validação (default: operacoes.md da pasta ou docs/OPERACOES_AS_IS_<id>.md).")
    p_plano.add_argument("--saida", default=None, help="Relatório de entrega (default: entrega.md da pasta ou docs/plans/_ENTREGA-<id>.md).")

    p_marco = sub.add_parser("marco", parents=[comuns], help="Grava o veredito do dono num marco de validação: a célula da tabela, o fim da `## 0.` e, no Marco 1 `go`, a saída de `blocked`.")
    p_marco.add_argument("--marco", type=int, required=True, help="Número do marco (a linha `| **Marco <n>** |` da tabela de marcos).")
    p_marco.add_argument("--resultado", choices=["go", "no-go"], required=True, help="Veredito do dono sobre o marco.")
    p_marco.add_argument("--veredito", required=True, help="Frase do dono, verbatim.")
    p_marco_versao = p_marco.add_mutually_exclusive_group()
    p_marco_versao.add_argument("--aceita-versao", dest="aceita_versao", default=None, help="Versão pendente (## 1A) que o dono aceitou.")
    p_marco_versao.add_argument("--recusa-versao", dest="recusa_versao", default=None, help="Versão pendente (## 1A) que o dono recusou.")
    p_marco.add_argument("--consultor", default=None, help="Linha de validação do consultor, verbatim; obrigatória com --aceita-versao (R-08).")

    p_operacoes = sub.add_parser("operacoes", parents=[comuns], help="Gera (ou confere) o esqueleto do relatório de operações — uma seção por tarefa viva do plano.")
    p_operacoes.add_argument("--checar", action="store_true", help="Não escreve: confere a cobertura do esqueleto já gravado (todo card citado, toda tarefa viva com seção, toda seção com os quatro blocos).")

    args = parser.parse_args(argv)
    repo = _backlog.resolve_repo(args.repo)
    data = args.data or datetime.date.today().isoformat()
    try:
        datetime.date.fromisoformat(data)
    except ValueError:
        print(f"encerrar: FALHOU - data '{data}' não é AAAA-MM-DD", file=sys.stderr)
        return 1

    try:
        if args.comando == "handover":
            texto = escrever_handover(
                repo, Path(args.plano), args.tarefa, data=data, entregue=args.entregue,
                contrato=args.contrato, nao_refazer=args.nao_refazer, pendente=args.pendente, para=args.para,
            )
            print(texto)
            print(f"encerrar: OK - handover registrado no card '{args.tarefa}' em '{args.plano}'.")
            return 0
        if args.comando == "marco":
            dossie = gravar_marco(
                repo, Path(args.plano), marco=args.marco, resultado=args.resultado,
                veredito=args.veredito, data=data,
                aceita_versao=args.aceita_versao, recusa_versao=args.recusa_versao,
                consultor=args.consultor,
            )
            if dossie is not None:
                print(dossie)
            print(f"marco: Marco {args.marco} gravado — {args.resultado}")
            return 0
        if args.comando == "operacoes":
            if args.checar:
                nao_citados, sem_secao, sem_blocos = checar_esqueleto_operacoes(repo, Path(args.plano))
                print(f"nao citados: {', '.join(nao_citados) if nao_citados else 'nenhum'}")
                print(f"sem seção: {', '.join(sem_secao) if sem_secao else 'nenhum'}")
                print(f"sem os quatro blocos: {', '.join(sem_blocos) if sem_blocos else 'nenhum'}")
                return 0 if not nao_citados and not sem_secao and not sem_blocos else 1
            destino_operacoes = escrever_esqueleto_operacoes(repo, Path(args.plano))
            print(f"encerrar: OK - esqueleto de operações gravado em '{_rel(destino_operacoes, repo)}'.")
            return 0
        if args.comando == "tarefa":
            trio = (args.tool_uses, args.tokens_k, args.duracao_s)
            if any(v is not None for v in trio) and not all(v is not None for v in trio):
                raise EncerramentoError("consumo: --tool-uses, --tokens-k e --duracao-s vão juntos")
            destino, humano = fechar_tarefa(
                repo, Path(args.plano), args.tarefa, data=data, resumo=args.resumo,
                pendencia=args.pendencia, achados=[tuple(a) for a in args.achado] if args.achado else None,
                laudo_path=Path(args.laudo) if args.laudo else None,
                consumo=trio if all(v is not None for v in trio) else None,
                nao_medido=args.nao_medido,
                modelo_agente=args.modelo_agente,
                progresso=Path(args.progresso) if args.progresso else None,
                rdo_dir=Path(args.rdo_dir) if args.rdo_dir else None,
                telemetria_tsv=Path(args.telemetria) if args.telemetria else None,
                template=args.template, esquema_legado=args.esquema_legado,
                modelo_legado=args.modelo, classe_legado=args.classe,
            )
        else:
            destino, humano = fechar_plano(
                repo, Path(args.plano), veredito=args.veredito, data=data, resumo=args.resumo,
                operacoes=Path(args.operacoes) if args.operacoes else None,
                saida=Path(args.saida) if args.saida else None,
                progresso=Path(args.progresso) if args.progresso else None,
                rdo_dir=Path(args.rdo_dir) if args.rdo_dir else None,
                telemetria_tsv=Path(args.telemetria) if args.telemetria else None,
            )
    except EncerramentoError as exc:
        if args.comando == "marco":
            if isinstance(exc, ConflitoDePromocao):
                print(exc.dossie)
            print(f"marco: {exc}", file=sys.stderr)
        else:
            print(f"encerrar: FALHOU - {exc}", file=sys.stderr)
        return 1

    print(humano)
    print(f"encerrar: OK - comando '{args.comando}' concluído; relatório em '{destino}'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
