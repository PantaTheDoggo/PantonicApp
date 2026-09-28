"""Ganchos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` e `Stop` do `P-0748` (`OP-3`):
gera em `.claude/estado/progresso.txt` uma frase por evento de transição do loop, com o
título da tarefa no lugar da sigla. Falha aberta total: qualquer exceção em `main` é
silenciada e o script sempre sai `0`; nunca imprime. Captura de payload opcional (flag
`progresso-captura.on`).
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import shlex
import sys
import time
from pathlib import Path


def _carregar_caminhos():
    caminho = Path(__file__).resolve().parent / "caminhos.py"
    spec = importlib.util.spec_from_file_location("caminhos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar_caminhos()

KIT = Path(__file__).resolve().parents[1]
REPO = KIT.parent

PAPEIS = {
    "pantonic-executor": "executor",
    "pantonic-reviewer": "revisor",
    "pantonic-consultant": "consultor",
    "pantonic-model-designer": "modelador",
    "pantonic-planner": "planejador",
}

ESTADO_ARQ = "progresso-estado.json"
CAPTURA_FLAG = "progresso-captura.on"
CAPTURA_ARQ = "progresso-captura.jsonl"
CAPTURA_TETO_BYTES = 1_000_000

FRASES = {
    'M-0': 'Abrindo a janela do plano "<título do plano>".',
    'M-1': 'Tarefa "<título>". Passo: conferir os gates e preparar o despacho.',
    'M-2': 'Tarefa "<título>": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
    'M-3': 'Agente executor recebe a tarefa "<título>" e vai executar: <objetivo>',
    'M-3b': 'Agente executor recebe a tarefa "<título>" e vai executar o card.',
    'M-4': 'Agente executor devolveu a tarefa "<título>": review — <pendência>.',
    'M-4b': 'Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.',
    'M-5': 'Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.',
    'M-6': 'Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.',
    'M-7': 'Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>, recomendação <recomendação>.',
    'M-8': 'Agente consultor recebe a tarefa "<título>" e vai triar.',
    'M-9': 'Agente consultor devolveu a tarefa "<título>": rota <rota>.',
    'M-9b': 'Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.',
    'M-10': 'Scrum master vai fechar a tarefa "<título>" como done: registrar estado, RDO e telemetria.',
    'M-10b': 'Scrum master vai marcar a tarefa "<título>" como <estado>, sem RDO.',
    'M-11': 'Scrum master concluiu a tarefa "<título fechada>" e vai pegar a tarefa "<título>".',
    'M-12': 'Scrum master concluiu a tarefa "<título fechada>"; nada delegável na fila. Encerrando a janela com o relatório.',
    'M-12b': 'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.',
    'M-13': 'Tarefa "<título>": vou medir a que arquivo a pendência é atribuível.',
    'M-14': 'Agente modelador recebe a tarefa "<título>" e vai fazer <ato> no modelo.',
    'M-14b': 'Agente modelador recebe a tarefa "<título>" e vai atualizar o modelo.',
    'M-15': 'Agente planejador recebe a tarefa "<título>" e vai replanejar.',
    'M-16': 'Agente <papel> devolveu a tarefa "<título>": <primeira linha>.',
    'M-17': 'Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.',
    'M-18': 'Scrum master vai fechar o plano "<título do plano>": registrar estado, relatório de entrega e a linha do diário.',
}


def titulo_do_plano(caminho: str, raiz: Path) -> str:
    """Título da linha 1 do plano (`# P-<n> — <título>`) apontado por `--plano` de
    `encerrar.py plano`; vazio quando o arquivo não existe ou a linha não casa."""
    for base in (Path(caminho), raiz / caminho):
        try:
            primeira = base.read_text(encoding="utf-8", errors="replace").splitlines()[0]
        except (OSError, IndexError):
            continue
        m = _caminhos.PLANO_HEADER_RE.match(primeira)
        if m:
            return m.group(2).strip()
    return ""


def capturar(payload: dict, estado: Path) -> None:
    try:
        if not (estado / CAPTURA_FLAG).exists():
            return
        arq = estado / CAPTURA_ARQ
        if arq.exists() and arq.stat().st_size > CAPTURA_TETO_BYTES:
            return
        ti = payload.get("tool_input")
        resp = payload.get("tool_response")
        registro = {
            "evento": payload.get("hook_event_name"),
            "tool": payload.get("tool_name"),
            "input_chaves": sorted(ti.keys()) if isinstance(ti, dict) else type(ti).__name__,
            "command": str(ti.get("command", ""))[:120] if isinstance(ti, dict) else "",
            "subagent_type": ti.get("subagent_type") if isinstance(ti, dict) else None,
            "response_tipo": type(resp).__name__,
            "response_chaves": sorted(resp.keys()) if isinstance(resp, dict) else None,
            "response": json.dumps(resp, ensure_ascii=False, default=str)[:2000],
        }
        with arq.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(registro, ensure_ascii=False) + "\n")
    except Exception:
        return


def texto_da_resposta(resp) -> str:
    if resp is None:
        return ""
    if isinstance(resp, str):
        return resp
    if isinstance(resp, dict):
        for chave in ("stdout", "output", "text", "result", "response"):
            valor = resp.get(chave)
            if isinstance(valor, str):
                return valor
        content = resp.get("content")
        if isinstance(content, list):
            partes = [
                str(bloco.get("text", ""))
                for bloco in content
                if isinstance(bloco, dict) and bloco.get("type") == "text"
            ]
            return "\n".join(partes)
        return json.dumps(resp, ensure_ascii=False, default=str)
    if isinstance(resp, list):
        partes = [
            str(bloco.get("text", ""))
            for bloco in resp
            if isinstance(bloco, dict) and bloco.get("type") == "text"
        ]
        return "\n".join(partes)
    return str(resp)


def localizar_card(id_tarefa: str, raiz: Path) -> tuple[str, str, str]:
    arquivos = _caminhos.arquivos_de_plano(raiz)
    diario = raiz / "docs" / "DIARIO_DE_OBRAS.md"
    if diario.exists():
        arquivos.append(diario)
    padrao = re.compile(r"^### " + re.escape(id_tarefa) + r" — (.+?) \[")
    padrao_rotulo = re.compile(r"^#+\s*(?:\S+\s+—\s+)?(.*)$")
    for arq in arquivos:
        try:
            linhas = arq.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for i, linha in enumerate(linhas):
            m = padrao.match(linha)
            if not m:
                continue
            titulo = m.group(1).strip()
            objetivo = ""
            for seguinte in linhas[i + 1:]:
                if seguinte.startswith("### "):
                    break
                if seguinte.startswith("- **Objetivo:**"):
                    objetivo = seguinte[len("- **Objetivo:**"):].strip()
                    if len(objetivo) > 240:
                        objetivo = objetivo[:239] + "…"
                    break
            if _caminhos.id_do_plano(arq) is not None:
                linha_plano = linhas[0] if linhas else ""
            else:
                linha_plano = ""
                for anterior in linhas[:i]:
                    if anterior.startswith("## "):
                        linha_plano = anterior
            mr = padrao_rotulo.match(linha_plano)
            titulo_plano = mr.group(1).strip() if mr else ""
            return (titulo, objetivo, titulo_plano)
    return (id_tarefa, "", "")


def frase(id_frase: str, lacunas: dict[str, str]) -> str:
    s = FRASES[id_frase]
    for k, v in lacunas.items():
        s = s.replace(k, v)
    return s


def tarefa_corrente(estado_loop: dict, estado: Path, raiz: Path) -> tuple[str, str, str]:
    if estado_loop.get("tarefa"):
        return (estado_loop.get("tarefa"), estado_loop.get("titulo", ""), estado_loop.get("objetivo", ""))
    try:
        dados = json.loads((estado / "tarefa-corrente.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        dados = None
    tid = dados.get("tarefa") if isinstance(dados, dict) else None
    if isinstance(tid, str) and tid:
        titulo, objetivo, _ = localizar_card(tid, raiz)
        estado_loop["tarefa"] = tid
        estado_loop["titulo"] = titulo
        estado_loop["objetivo"] = objetivo
        return (tid, titulo, objetivo)
    return ("", "(tarefa não identificada)", "")


def de_volta(sub: str, texto: str, titulo: str) -> list[str]:
    papel = PAPEIS[sub]
    l1 = ""
    for linha in texto.splitlines():
        l = linha.strip()
        if l:
            l1 = l
            break

    if sub == "pantonic-executor":
        m = re.match(r"^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$", l1)
        if m:
            pendencia = (m.group(2) or "").strip()
            return [frase("M-4", {"<título>": titulo, "<pendência>": pendencia or "sem pendência"})]
        m = re.match(r"^(\S+) blocked motivo=(\S+)\s*(.*)$", l1)
        if m:
            return [frase("M-4b", {"<título>": titulo, "<motivo>": m.group(2), "<razão>": m.group(3)})]
    elif sub == "pantonic-reviewer":
        m = re.match(r"^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$", l1)
        if m:
            return [frase("M-7", {
                "<título>": titulo,
                "<veredito>": m.group(2),
                "<percentual>": m.group(3),
                "<bloqueante>": m.group(4),
                "<recomendação>": (m.group(5) or "").strip() or "não informada",
            })]
    elif sub == "pantonic-consultant":
        mr = re.search(r"^\s*rota=(\S+)", texto, re.M)
        me = re.search(r"^\s*estrategico=(.*)$", texto, re.M)
        if mr and me:
            return [frase("M-9b", {"<título>": titulo, "<rota>": mr.group(1), "<frase>": me.group(1).strip()})]
        if mr:
            return [frase("M-9", {"<título>": titulo, "<rota>": mr.group(1)})]

    primeira_linha = l1[:160] + "…" if len(l1) > 160 else (l1 or "(sem texto)")
    return [frase("M-16", {"<título>": titulo, "<papel>": papel, "<primeira linha>": primeira_linha})]


_SEPARADORES_2 = ("&&", "||")
_INTERPRETE_RE = re.compile(r"^(python3?|py)(\.exe)?$", re.IGNORECASE)


def _dividir_invocacoes(cmd: str) -> list[str]:
    """Separa `cmd` em invocações por `&&`, `||`, `;`, `|` e quebra de linha, fora de aspas
    simples ou duplas (`TK-88c`: cada invocação se lê por si, um comando encadeado não
    empresta argumento de uma invocação para outra)."""
    partes: list[str] = []
    atual: list[str] = []
    aspas = ""
    i = 0
    n = len(cmd)
    while i < n:
        c = cmd[i]
        if aspas:
            atual.append(c)
            if c == aspas:
                aspas = ""
            i += 1
            continue
        if c in ("'", '"'):
            aspas = c
            atual.append(c)
            i += 1
            continue
        if cmd[i:i + 2] in _SEPARADORES_2:
            partes.append("".join(atual))
            atual = []
            i += 2
            continue
        if c in (";", "|", "\n"):
            partes.append("".join(atual))
            atual = []
            i += 1
            continue
        atual.append(c)
        i += 1
    partes.append("".join(atual))
    return [p.strip() for p in partes if p.strip()]


def _tokens_da_invocacao(invocacao: str) -> list[str]:
    try:
        return shlex.split(invocacao, posix=True)
    except ValueError:
        return invocacao.split()


def _programa(tokens: list[str]) -> tuple[str, list[str]] | None:
    """Quando `tokens` é `python`/`python3`/`py` (com ou sem caminho e opções) seguido do
    caminho de um script, devolve `(nome_do_script, tokens_seguintes)`; senão `None` — o
    script citado num argumento (mensagem de commit, `--resumo`) não é o programa da
    invocação e não casa aqui."""
    if not tokens:
        return None
    nome_interprete = tokens[0].replace("\\", "/").rsplit("/", 1)[-1]
    if not _INTERPRETE_RE.match(nome_interprete):
        return None
    i = 1
    while i < len(tokens) and tokens[i].startswith("-"):
        opcao = tokens[i]
        if opcao == "-m":
            if i + 1 >= len(tokens):
                return None
            return (tokens[i + 1], tokens[i + 2:])
        if opcao == "-c":
            return None
        if opcao in ("-X", "-W"):
            i += 2
            continue
        i += 1
    if i >= len(tokens):
        return None
    nome_script = tokens[i].replace("\\", "/").rsplit("/", 1)[-1]
    return (nome_script, tokens[i + 1:])


def _valor_opcao(tokens: list[str], opcao: str) -> str | None:
    for i, t in enumerate(tokens):
        if t == opcao and i + 1 < len(tokens):
            return tokens[i + 1]
    return None


def evento(payload: dict, estado_loop: dict, estado: Path, raiz: Path) -> tuple[list[str], dict]:
    sid = payload.get("session_id")
    if estado_loop.get("sessao") != sid:
        estado_loop = {"sessao": sid}

    ev = payload.get("hook_event_name")
    tool = payload.get("tool_name")
    ti_raw = payload.get("tool_input")
    ti = ti_raw if isinstance(ti_raw, dict) else {}
    cmd = str(ti.get("command", ""))
    sub = str(ti.get("subagent_type", ""))
    resp = texto_da_resposta(payload.get("tool_response"))
    linhas: list[str] = []

    if ev == "PostToolUse" and tool == "Bash" and "backlog.py next" in cmd:
        estado_loop.pop("relatorio", None)
        m = re.search(r"^=== PRÓXIMA TAREFA: (\S+) — (.+?) \[", resp, re.M)
        if m:
            tid, titulo = m.group(1), m.group(2).strip()
            _, objetivo, titulo_plano = localizar_card(tid, raiz)
            if not estado_loop.get("aberta") and titulo_plano:
                linhas.append(frase("M-0", {"<título do plano>": titulo_plano}))
            if estado_loop.get("tarefa_fechada"):
                linhas.append(frase("M-11", {
                    "<título fechada>": estado_loop.get("titulo_fechada", ""),
                    "<título>": titulo,
                }))
                estado_loop.pop("tarefa_fechada", None)
                estado_loop.pop("titulo_fechada", None)
            linhas.append(frase("M-1", {"<título>": titulo}))
            estado_loop["tarefa"] = tid
            estado_loop["titulo"] = titulo
            estado_loop["objetivo"] = objetivo
            estado_loop["titulo_plano"] = titulo_plano
            estado_loop["aberta"] = True
        elif "nada delegável" in resp:
            if estado_loop.get("tarefa_fechada"):
                linhas.append(frase("M-12", {"<título fechada>": estado_loop.get("titulo_fechada", "")}))
                estado_loop.pop("tarefa_fechada", None)
                estado_loop.pop("titulo_fechada", None)
            else:
                linhas.append(frase("M-12b", {}))

    elif ev == "PreToolUse" and tool == "Bash":
        # `encerrar.py tarefa` (TK-88) materializa o `done` em processo — o comando
        # `backlog.py status <ID> done` não aparece mais na linha; a mesma frase `M-10` sai
        # da detecção do instrumento de fechamento. `encerrar.py plano` gera a `M-18`.
        # TK-88c: cada frase só sai quando o script é o programa da própria invocação —
        # lida invocação por invocação do comando encadeado (`&&`, `||`, `;`, `|`, quebra de
        # linha fora de aspas) —, e `--tarefa`/`--plano`/`--atribuir` se leem só nos
        # argumentos dessa invocação; texto de argumento que cite o script não gera frase.
        for invocacao in _dividir_invocacoes(cmd):
            prog = _programa(_tokens_da_invocacao(invocacao))
            if prog is None:
                continue
            script, resto = prog

            if script == "backlog.py" and resto[:1] == ["status"] and len(resto) >= 3:
                tid, st = resto[1], resto[2]
                if estado_loop.get("tarefa") == tid:
                    titulo = estado_loop.get("titulo", "")
                else:
                    titulo, _, _ = localizar_card(tid, raiz)
                if st == "in-progress":
                    if estado_loop.get("tarefa") != tid:
                        titulo, objetivo, _ = localizar_card(tid, raiz)
                        estado_loop["tarefa"] = tid
                        estado_loop["titulo"] = titulo
                        estado_loop["objetivo"] = objetivo
                    linhas.append(frase("M-2", {"<título>": titulo}))
                elif st == "done":
                    linhas.append(frase("M-10", {"<título>": titulo}))
                    estado_loop["tarefa_fechada"] = tid
                    estado_loop["titulo_fechada"] = titulo
                elif st in ("blocked", "cancelled"):
                    linhas.append(frase("M-10b", {"<título>": titulo, "<estado>": st}))

            elif script == "encerrar.py" and resto[:1] == ["tarefa"]:
                tid = _valor_opcao(resto, "--tarefa")
                if tid:
                    if estado_loop.get("tarefa") == tid:
                        titulo = estado_loop.get("titulo", "")
                    else:
                        titulo, _, _ = localizar_card(tid, raiz)
                    linhas.append(frase("M-10", {"<título>": titulo}))
                    estado_loop["tarefa_fechada"] = tid
                    estado_loop["titulo_fechada"] = titulo

            elif script == "encerrar.py" and resto[:1] == ["plano"]:
                caminho = _valor_opcao(resto, "--plano")
                titulo_plano = estado_loop.get("titulo_plano") or (
                    titulo_do_plano(caminho, raiz) if caminho else ""
                )
                if titulo_plano:
                    linhas.append(frase("M-18", {"<título do plano>": titulo_plano}))

            elif script == "review_evidence.py":
                tid = _valor_opcao(resto, "--tarefa")
                if tid:
                    if estado_loop.get("tarefa") == tid:
                        titulo = estado_loop.get("titulo", "")
                    else:
                        titulo, objetivo, _ = localizar_card(tid, raiz)
                        estado_loop["tarefa"] = tid
                        estado_loop["titulo"] = titulo
                        estado_loop["objetivo"] = objetivo
                    if "--atribuir" in resto:
                        linhas.append(frase("M-13", {"<título>": titulo}))
                    else:
                        linhas.append(frase("M-5", {"<título>": titulo}))

    elif ev == "PreToolUse" and tool == "Agent" and sub in PAPEIS:
        estado_loop.pop("relatorio", None)
        _, titulo, objetivo = tarefa_corrente(estado_loop, estado, raiz)
        if sub == "pantonic-executor":
            if objetivo:
                linhas.append(frase("M-3", {"<título>": titulo, "<objetivo>": objetivo}))
            else:
                linhas.append(frase("M-3b", {"<título>": titulo}))
        elif sub == "pantonic-reviewer":
            linhas.append(frase("M-6", {"<título>": titulo}))
        elif sub == "pantonic-consultant":
            linhas.append(frase("M-8", {"<título>": titulo}))
        elif sub == "pantonic-model-designer":
            m = re.search(r"Ato:\s*`?(autoria|emenda|conflito)", str(ti.get("prompt", "")))
            if m:
                linhas.append(frase("M-14", {"<título>": titulo, "<ato>": m.group(1)}))
            else:
                linhas.append(frase("M-14b", {"<título>": titulo}))
        elif sub == "pantonic-planner":
            linhas.append(frase("M-15", {"<título>": titulo}))

    elif ev == "PostToolUse" and tool == "Agent" and sub in PAPEIS:
        r = payload.get("tool_response")
        if isinstance(r, dict) and r.get("handback") == "send" and isinstance(r.get("agentId"), str):
            estado_loop.setdefault("pendentes", {})[r["agentId"]] = sub
        else:
            _, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)
            linhas = de_volta(sub, resp, titulo)

    elif ev == "UserPromptSubmit":
        p = str(payload.get("prompt") or "")
        m = re.match(r'<agent-message from="([^"]+)">', p)
        if m:
            sub2 = estado_loop.get("pendentes", {}).pop(m.group(1), "")
            if sub2 in PAPEIS:
                marca = "The report follows:"
                idx = p.find(marca)
                corpo = p[idx + len(marca):] if idx != -1 else ""
                fim = corpo.find("</agent-message>")
                if fim != -1:
                    corpo = corpo[:fim]
                _, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)
                linhas = de_volta(sub2, corpo, titulo)

    elif ev == "Stop":
        if estado_loop.get("aberta") and estado_loop.get("relatorio"):
            linhas.append(frase("M-17", {}))
            estado_loop.pop("relatorio", None)

    if ev == "PreToolUse" and tool == "Bash" and "modelo.py show" in cmd and "--drift" not in cmd and "--pendente" not in cmd and estado_loop.get("aberta"):
        estado_loop["relatorio"] = True

    return (linhas, estado_loop)


def main(argv: list[str] | None = None, entrada: str | None = None,
         estado: Path | None = None, raiz: Path | None = None, espera: float = 2.0) -> int:
    try:
        raw = entrada if entrada is not None else sys.stdin.buffer.read().decode("utf-8", errors="replace")
        payload = json.loads(raw)
        if not isinstance(payload, dict):
            return 0
        if payload.get("agent_type"):
            return 0

        estado = estado or KIT / "estado"
        raiz = raiz or REPO
        estado.mkdir(parents=True, exist_ok=True)
        capturar(payload, estado)

        trava = estado / "progresso.lock"
        inicio = time.monotonic()
        obtida = False
        while time.monotonic() - inicio <= espera:
            try:
                fd = os.open(trava, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.close(fd)
                obtida = True
                break
            except FileExistsError:
                try:
                    if time.time() - trava.stat().st_mtime > 30:
                        trava.unlink(missing_ok=True)
                        continue
                except OSError:
                    continue
                time.sleep(0.05)
        if not obtida:
            return 0

        try:
            try:
                estado_loop = json.loads((estado / ESTADO_ARQ).read_text(encoding="utf-8"))
                if not isinstance(estado_loop, dict):
                    estado_loop = {}
            except (OSError, ValueError):
                estado_loop = {}

            linhas, estado_loop = evento(payload, estado_loop, estado, raiz)

            if linhas:
                with (estado / "progresso.txt").open("a", encoding="utf-8", newline="\n") as f:
                    for linha in linhas:
                        f.write(linha + "\n")

            (estado / ESTADO_ARQ).write_text(
                json.dumps(estado_loop, ensure_ascii=False), encoding="utf-8"
            )
        finally:
            trava.unlink(missing_ok=True)

        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
