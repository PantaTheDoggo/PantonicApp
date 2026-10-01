"""RAF-T2 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T2`) — o medidor de
custo da sessão vira comando do kit: lê uma conversa gravada (transcript, uma linha JSON por
evento) e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.

Fundamento: `DRF-6`; `F-6` (285,6k por turno no loop real), `F-13` (os rascunhos de
`docs/audits/sonda-2026-09-28/{medir,passos}.py` quebram e fixam `AUF-T`). Os rascunhos são o
ponto de partida lido e ficam intocados — este módulo não importa deles nem os reescreve.

Dois subcomandos:

``python .claude/tools/custo_sessao.py medir <transcript> <saida>`` — grava em `<saida>` (TSV) uma
linha por turno `assistant` com `usage` não vazio: `timestamp`, `message.id`, o contexto reenviado
(`input_tokens + cache_read_input_tokens + cache_creation_input_tokens`, campo ausente conta 0),
`output_tokens` e as ferramentas do turno unidas por ` | `.

``python .claude/tools/custo_sessao.py passos <tsv> <regex_inicio> <regex_fim>`` — agrupa o TSV por
`message.id`, recorta a janela entre a primeira mensagem cujas ferramentas casam `regex_inicio` e
a última que casa `regex_fim`, e imprime o total da janela, o total por passo do loop
(`classificar_passo`) e o total por tarefa despachada (regex `despachar
([A-Z]+-T\\d+[a-z]?|TK-\\d+)`, de qualquer plano ou tíquete — não só `AUF-T`)."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_REGEX_BACKLOG_STATUS_REVIEW = re.compile(r"backlog\.py status \S+ review")
_REGEX_GREP_MECANICO = re.compile(r"grep -n|--co -q|wc -l")
_REGEX_TAREFA = re.compile(r"despachar ([A-Z]+-T\d+[a-z]?|TK-\d+)")


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir certos caracteres —
    duplicado do mesmo utilitário de `card_check.py`/`review_evidence.py`/`crenca_hook.py`
    (`DM-11`, sem import cruzado entre módulos)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def _ferramentas_do_turno(blocos: list) -> str:
    ferramentas: list[str] = []
    for bloco in blocos or []:
        tipo = bloco.get("type")
        if tipo == "tool_use":
            nome = bloco.get("name")
            entrada = bloco.get("input") or {}
            if nome == "Agent":
                subagent_type = entrada.get("subagent_type", "")
                descricao = entrada.get("description", "")
                ferramentas.append(f"Agent:{subagent_type}:{descricao}")
            elif nome in ("Bash", "PowerShell"):
                comando = re.sub(r"\s+", " ", str(entrada.get("command", "")))
                ferramentas.append("Bash:" + comando[:220])
            else:
                valor = entrada.get("file_path", entrada.get("pattern", ""))
                ferramentas.append(f"{nome}:" + str(valor)[:120])
        elif tipo == "text" and str(bloco.get("text", "")).strip():
            ferramentas.append("TEXT")
    return " | ".join(ferramentas)


def medir(transcript: Path, saida: Path) -> int:
    """Grava em `saida` uma linha do TSV por turno `assistant` com `usage` não vazio; devolve o
    número de linhas gravadas."""
    linhas: list[tuple[str, str, int, int, str]] = []
    for linha_bruta in transcript.read_text(encoding="utf-8").splitlines():
        try:
            evento = json.loads(linha_bruta)
        except (json.JSONDecodeError, ValueError):
            continue
        if evento.get("type") != "assistant":
            continue
        mensagem = evento.get("message") or {}
        uso = mensagem.get("usage") or {}
        if not uso:
            continue
        contexto = (
            uso.get("input_tokens", 0)
            + uso.get("cache_read_input_tokens", 0)
            + uso.get("cache_creation_input_tokens", 0)
        )
        saida_tokens = uso.get("output_tokens", 0)
        ferramentas = _ferramentas_do_turno(mensagem.get("content") or [])
        linhas.append((evento.get("timestamp", ""), mensagem.get("id", ""), contexto, saida_tokens, ferramentas))
    with saida.open("w", encoding="utf-8") as f:
        for ts, mid, contexto, saida_tokens, ferramentas in linhas:
            f.write(f"{ts}\t{mid}\t{contexto}\t{saida_tokens}\t{ferramentas}\n")
    return len(linhas)


def classificar_passo(ferramentas: str) -> str:
    """Devolve o passo do loop (`P1`..`P10`, `texto` ou `outro`) que `ferramentas` casa, na ordem
    fechada do contrato."""
    texto = ferramentas.replace("TEXT | ", "").replace(" | TEXT", "")
    if "pantonic-executor" in texto:
        return "P4"
    if "pantonic-reviewer" in texto:
        return "P6"
    if "pantonic-consultant" in texto:
        return "P8"
    if "encerrar.py" in texto:
        return "P9"
    if _REGEX_BACKLOG_STATUS_REVIEW.search(texto):
        return "P5"
    if "despachar" in texto:
        return "P3"
    if "backlog.py next" in texto:
        return "P2"
    if _REGEX_GREP_MECANICO.search(texto) and "laudo" not in texto:
        return "P3"
    if "laudos/" in texto or "Achado de processo" in texto:
        return "P7"
    if texto.strip() in ("", "TEXT"):
        return "texto"
    return "outro"


def _formatar_k(valor: int) -> str:
    return f"{valor / 1000:.1f}"


def passos(tsv: Path, regex_inicio: str, regex_fim: str) -> list[str]:
    """Reparte os turnos do `tsv` pela janela entre `regex_inicio` e `regex_fim`, por passo do
    loop e por tarefa despachada."""
    mensagens: dict = {}
    for linha_bruta in tsv.read_text(encoding="utf-8").splitlines():
        if not linha_bruta:
            continue
        campos = linha_bruta.split("\t")
        campos = campos + [""] * (5 - len(campos))
        ts, mid, contexto, saida_tokens, ferramentas = campos[:5]
        registro = mensagens.setdefault(
            mid, {"ts": ts, "ctx": int(contexto or 0), "out": int(saida_tokens or 0), "ferramentas": []}
        )
        if ferramentas:
            registro["ferramentas"].append(ferramentas)

    lista = list(mensagens.values())
    re_inicio = re.compile(regex_inicio)
    re_fim = re.compile(regex_fim)
    indices_inicio = [i for i, m in enumerate(lista) if re_inicio.search(" | ".join(m["ferramentas"]))]
    indices_fim = [i for i, m in enumerate(lista) if re_fim.search(" | ".join(m["ferramentas"]))]
    if not indices_inicio or not indices_fim or indices_fim[-1] < indices_inicio[0]:
        return ["janela: vazia", "por tarefa: n=0"]

    i0 = indices_inicio[0]
    i1 = indices_fim[-1]
    janela = lista[i0 : i1 + 1]

    agregado_por_passo: dict[str, list[int]] = {}
    agregado_por_tarefa: dict[str, list[int]] = {}
    ordem_tarefas: list[str] = []
    tarefa_corrente: str | None = None
    for msg in janela:
        texto = " | ".join(msg["ferramentas"])
        casamento_tarefa = _REGEX_TAREFA.search(texto)
        if casamento_tarefa:
            tarefa_corrente = casamento_tarefa.group(1)
            if tarefa_corrente not in agregado_por_tarefa:
                ordem_tarefas.append(tarefa_corrente)
        passo = classificar_passo(texto)
        acumulador_passo = agregado_por_passo.setdefault(passo, [0, 0, 0])
        acumulador_passo[0] += 1
        acumulador_passo[1] += msg["ctx"]
        acumulador_passo[2] += msg["out"]
        if tarefa_corrente is not None:
            acumulador_tarefa = agregado_por_tarefa.setdefault(tarefa_corrente, [0, 0, 0])
            acumulador_tarefa[0] += 1
            acumulador_tarefa[1] += msg["ctx"]
            acumulador_tarefa[2] += msg["out"]

    total_turnos = sum(v[0] for v in agregado_por_passo.values())
    total_ctx = sum(v[1] for v in agregado_por_passo.values())
    total_out = sum(v[2] for v in agregado_por_passo.values())
    resultado = [
        f"janela: {lista[i0]['ts']} -> {lista[i1]['ts']} turnos {total_turnos} "
        f"ctx_k {_formatar_k(total_ctx)} out_k {_formatar_k(total_out)}"
    ]
    for passo in sorted(agregado_por_passo):
        n, ctx, out = agregado_por_passo[passo]
        resultado.append(f"{passo} turnos={n} ctx_k={_formatar_k(ctx)} out_k={_formatar_k(out)}")

    if not agregado_por_tarefa:
        resultado.append("por tarefa: n=0")
    else:
        turnos_por_tarefa = [v[0] for v in agregado_por_tarefa.values()]
        ctx_por_tarefa = [v[1] for v in agregado_por_tarefa.values()]
        n_tarefas = len(agregado_por_tarefa)
        turnos_medio = sum(turnos_por_tarefa) / n_tarefas
        ctx_k_medio = (sum(ctx_por_tarefa) / n_tarefas) / 1000
        resultado.append(
            f"por tarefa: n={n_tarefas} turnos medio={turnos_medio:.1f} ctx_k medio={ctx_k_medio:.1f} "
            f"min_turnos={min(turnos_por_tarefa)} max_turnos={max(turnos_por_tarefa)}"
        )
        for tarefa in ordem_tarefas:
            n, ctx, out = agregado_por_tarefa[tarefa]
            resultado.append(f"{tarefa} turnos={n} ctx_k={_formatar_k(ctx)} out_k={_formatar_k(out)}")

    return resultado


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)

    parser = argparse.ArgumentParser(prog="custo_sessao")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    parser_medir = subparsers.add_parser("medir")
    parser_medir.add_argument("transcript")
    parser_medir.add_argument("saida")

    parser_passos = subparsers.add_parser("passos")
    parser_passos.add_argument("tsv")
    parser_passos.add_argument("regex_inicio")
    parser_passos.add_argument("regex_fim")

    args = parser.parse_args(argv)

    if args.comando == "medir":
        transcript = Path(args.transcript)
        if not transcript.is_file():
            print(f"custo_sessao: FALHOU - transcript não encontrado '{args.transcript}'", file=sys.stderr)
            return 1
        saida = Path(args.saida)
        n = medir(transcript, saida)
        print(f"{n} linhas")
        return 0

    tsv = Path(args.tsv)
    if not tsv.is_file():
        print(f"custo_sessao: FALHOU - tsv não encontrado '{args.tsv}'", file=sys.stderr)
        return 1
    for padrao in (args.regex_inicio, args.regex_fim):
        try:
            re.compile(padrao)
        except re.error as exc:
            print(f"custo_sessao: FALHOU - regex inválida '{padrao}': {exc}", file=sys.stderr)
            return 1
    for linha in passos(tsv, args.regex_inicio, args.regex_fim):
        print(linha)
    return 0


if __name__ == "__main__":
    sys.exit(main())
