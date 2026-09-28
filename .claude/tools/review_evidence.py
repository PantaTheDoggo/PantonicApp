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

Forma canônica do campo `Arquivos-alvo` (`P-0739` `DB-26`/`DB-27`): um caminho por bullet, o
caminho como primeiro literal entre crases do bullet, com sufixo opcional `:<linha>`. A extração
é mecânica e por **literal**, não por linha — `_parsear_campos_com_linhas` (`.claude/tools/rdo.py:212-272`)
junta as linhas de um campo com espaço, e a estrutura de bullets não chega até aqui. Todo literal
entre crases é candidato; vira alvo só quando casa `_CAMINHO_RE` e tem extensão, barra ou termina
em `/`. Literal descartado (trecho de regex, cabeçalho de seção) sai na seção `## Escopo` como
"não reconhecido como caminho", nunca como bloqueio. Limitação que permanece e é do revisor, não
deste script: caminho citado em prosa negativa dentro do campo ("não editar `x/y.py`") conta como
alvo declarado — por isso a forma canônica manda a citação negativa para `Não fazer`.

A seção `## Guardas` (`EXA-T9b`) invoca a bateria de seis comandos de `GOVERNANCA.md` §3 (a
mesma que fechou a `T9a`: `python -m pytest -q`, `dead_code.py`, `ratchet_piso.py`,
`kit_check.ps1 -Mode validate`, `kit_check.ps1 -Mode check-drift`, `check-readme.ps1`), cola exit
code e saída de cada um, e trava o veredito mecânico das dimensões `guardas`
(`docs/RUBRICA_DE_REVISAO.md:94-106` — autoridade integral, sem faixa de juízo: qualquer comando
fora de exit 0 resolve para `não conforme`, nunca para `parcial` sozinha) e `testes`
(`docs/RUBRICA_DE_REVISAO.md:79-92` — evidência mecânica é o exit code do comando `pytest` da
bateria). A bateria de produção (`BATERIA_GUARDAS`) é injetável (`comandos_guardas` em
`montar_documento`/`rodar_bateria_guardas`) para permitir teste determinístico sem depender da
infraestrutura real do hub num repositório de fixture.

`AUT-T5b` corrige dois defeitos medidos: (i) um `Arquivos-alvo` que declara um **diretório**
(ex.: `.claude/tools/`) agora casa por prefixo contra os arquivos tocados dentro dele, em vez de
comparar como caminho literal e cair no fallback "arquivo ausente na árvore de trabalho"; (ii) o
conjunto de arquivos tocados agora aceita `--desde <ref>` (`coletar_arquivos_tocados`) para
recortar só o que mudou a partir de uma referência git, em vez de sempre varrer a árvore de
trabalho inteira — necessário quando outras tarefas têm mudanças soltas, não commitadas, no mesmo
repositório. Ausência de `--desde` preserva o comportamento anterior integralmente, e a seção
`## Escopo` sempre declara explicitamente qual recorte foi medido.

A seção `## Escopo` classifica o arquivo tocado em cinco baldes (`P-0739` `DB-25`): coberto
pelos alvos do card; alvo declarado por outra tarefa do mesmo plano; registro da orquestração
(`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/plans/`,
`docs/RDO/`, `docs/audits/`); ato do dono fora
do ciclo de tarefa (`.claude/agents/`); fora dos alvos
sem atribuição. Só o último resolve o veredito — `git` não sabe qual tarefa tocou qual arquivo,
e o plano sabe qual tarefa declarou qual alvo.

`--capturar-ref` (`TK-93a`) imprime o `<ref>` do despacho (`capturar_ref`) e sai, sem exigir
`--plano` nem `--tarefa`: um commit cuja árvore é a árvore de trabalho inteira no instante da
captura, rastreados e não rastreados não ignorados, sem alterar árvore, índice real nem lista de
stash. Com `--desde <esse ref>`, o não rastreado que já existia na árvore dele é julgado por
conteúdo (linha a linha, fim de linha normalizado) em vez de por `st_mtime`, e o trecho dele é o
diff unificado contra o conteúdo em `<ref>` — nunca o de `git diff <ref>`, que o daria como
apagado por estar fora do índice atual."""
from __future__ import annotations

import argparse
import difflib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def _carregar_caminhos():
    caminho = Path(__file__).resolve().parent / "caminhos.py"
    spec = importlib.util.spec_from_file_location("caminhos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


_caminhos = _carregar_caminhos()

_BACKTICK_RE = re.compile(r"`([^`]+)`")
_STATUS_DESPACHADO = frozenset({"in-progress", "review", "done"})
_LINHA_REF_RE = re.compile(r":\d+(-\d+)?$")
_SECAO_REF_RE = re.compile(r"\s+§\S*$")
_LITERAL_APOS_ANCORA_RE = re.compile(
    r"(`[^`\s]+:\d+(?:-\d+)?`)\s*(?:—|:)\s*`(?:\\`|[^`\\])+`"
)


class ReviewEvidenceValidationError(ValueError):
    """Dossiê, plano, tarefa ou repositório git inválido (mensagem já nomeia o problema)."""


def _exigir_plano(plano_path: Path) -> None:
    """Guarda única da borda: caminho de plano que não existe falha pelo canal do módulo
    (`ReviewEvidenceValidationError` → `review_evidence: FALHOU - …`), em **todos** os verbos
    (`DM-22`, `AE-17`)."""
    if not plano_path.is_file():
        raise ReviewEvidenceValidationError(f"plano: arquivo não encontrado '{plano_path}'")


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


_CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.][A-Za-z0-9_./\\-]*$")
_EXTENSAO_RE = re.compile(r"\.[A-Za-z0-9]+$")


def _eh_caminho(candidato: str) -> bool:
    """Gramática de caminho da `DB-27` (`P-0739`): sem espaço e sem metacaractere de regex, e
    com extensão, barra, ou barra final. Recusa `_ID_HEADER_RE = re.compile(...)` (espaço) e
    `BKL-T9` (sem extensão e sem barra); aceita `CHANGELOG.md` e `tests/fixtures/backlog/`."""
    if not _CAMINHO_RE.fullmatch(candidato):
        return False
    return (
        "/" in candidato
        or "\\" in candidato
        or candidato.endswith("/")
        or bool(_EXTENSAO_RE.search(candidato))
    )


def _classificar_campo_alvos(campos: dict) -> tuple[list[str], list[str]]:
    """Parte o campo `Arquivos-alvo`/`Entregável` em (alvos, literais descartados), por literal
    entre crases (`DB-27`). Descartado é fato impresso, nunca bloqueio (`DB-19`)."""
    texto = campos.get("arquivos-alvo") or campos.get("entregavel") or ""
    texto = _LITERAL_APOS_ANCORA_RE.sub(r"\1", texto)
    alvos: dict[str, None] = {}
    descartados: list[str] = []
    for match in _BACKTICK_RE.finditer(texto):
        bruto = match.group(1).strip()
        candidato = _LINHA_REF_RE.sub("", _SECAO_REF_RE.sub("", bruto))
        if _eh_caminho(candidato):
            alvos.setdefault(candidato, None)
        else:
            descartados.append(bruto)
    return list(alvos.keys()), descartados


def extrair_arquivos_alvo(campos: dict) -> list[str]:
    """Caminhos declarados no campo `Arquivos-alvo`/`Entregável` do dossiê, na ordem em que
    aparecem, sem repetição."""
    return _classificar_campo_alvos(campos)[0]


def extrair_literais_nao_caminho(campos: dict) -> list[str]:
    """Literais entre crases do mesmo campo que não são caminho pela `DB-27` — vão para a seção
    `## Escopo` como transparência da extração."""
    return _classificar_campo_alvos(campos)[1]


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `→` do documento; o
    arquivo de `--out` já é gravado em UTF-8. `reconfigure` só existe em stream de texto real."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def _git(args: list[str], root: Path, env: dict[str, str] | None = None) -> str:
    try:
        resultado = subprocess.run(
            ["git", *args],
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
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


def capturar_ref(root: Path) -> str:
    """`<ref>` do despacho (`TK-93a`, flag `--capturar-ref`): commit cujo pai é `HEAD` (sem pai em
    repositório sem commit ainda) e cuja árvore é a árvore de trabalho inteira — rastreados e não
    rastreados não ignorados —, gravado por um índice temporário (`GIT_INDEX_FILE`); a árvore de
    trabalho, o índice real e a lista de stash saem exatamente como entraram, porque nada aqui
    escreve nele."""
    fd, indice_tmp = tempfile.mkstemp(prefix=".review-evidence-index-", suffix=".tmp")
    os.close(fd)
    Path(indice_tmp).unlink()
    env = dict(os.environ)
    env["GIT_INDEX_FILE"] = indice_tmp
    try:
        _git(["add", "-A"], root, env=env)
        arvore = _git(["write-tree"], root, env=env).strip()
        try:
            pai = _git(["rev-parse", "--verify", "HEAD"], root).strip()
        except ReviewEvidenceValidationError:
            pai = None
        args_commit = ["commit-tree", arvore, "-m", "review_evidence: captura de <ref> (TK-93a)"]
        if pai is not None:
            args_commit += ["-p", pai]
        return _git(args_commit, root, env=env).strip()
    finally:
        Path(indice_tmp).unlink(missing_ok=True)


def coletar_diff_stat(root: Path, desde: str | None = None) -> str:
    """Sem `desde`: `git diff HEAD --stat` (comportamento de sempre). Com `desde=<ref>` (`AF-T1`,
    `TK-94a`): recorta o resumo para o mesmo conjunto que `coletar_arquivos_tocados(root, desde)`
    devolve — rastreados e não rastreados da entrega, nunca o trabalho em andamento de outra
    tarefa na mesma árvore. Sem tocado nenhum, devolve string vazia (o chamador já renderiza
    `(sem diferenças)` para diff vazio); com tocado, grava a árvore de trabalho num índice
    temporário (`GIT_INDEX_FILE`, mesmo molde de `capturar_ref`) para obter o hash da árvore
    inteira — rastreados e não rastreados —, e roda `git diff --stat <desde> <árvore> --
    <tocados>` fora do índice temporário (comparação de dois tree-ish, não precisa mais dele).
    Árvore de trabalho, índice real e lista de stash saem como entraram: nada aqui escreve
    neles. Nunca roda `git diff --stat` sem caminho quando `tocados` é vazio — sem `--`, ele
    devolveria a árvore inteira."""
    if desde is None:
        return _diff(["--stat"], root).strip()
    tocados = coletar_arquivos_tocados(root, desde)
    if not tocados:
        return ""
    fd, indice_tmp = tempfile.mkstemp(prefix=".review-evidence-index-", suffix=".tmp")
    os.close(fd)
    Path(indice_tmp).unlink()
    env = dict(os.environ)
    env["GIT_INDEX_FILE"] = indice_tmp
    try:
        _git(["add", "-A"], root, env=env)
        arvore = _git(["write-tree"], root, env=env).strip()
    finally:
        Path(indice_tmp).unlink(missing_ok=True)
    return _git(["diff", "--stat", desde, arvore, "--", *tocados], root).strip()


def _extrair_caminho_status(linha: str) -> str:
    caminho = linha[3:]
    if " -> " in caminho:
        caminho = caminho.split(" -> ", 1)[1]
    return caminho.strip().strip('"')


def _existe_no_ref(root: Path, ref: str, caminho: str) -> bool:
    """`git cat-file -e <ref>:<caminho>` — existe como blob na árvore do commit `<ref>`."""
    return (
        subprocess.run(
            ["git", "cat-file", "-e", f"{ref}:{caminho}"],
            cwd=str(root),
            capture_output=True,
        ).returncode
        == 0
    )


def _eh_nao_rastreado(root: Path, caminho: str) -> bool:
    """`??` no `git status` de hoje para este caminho — fora do índice atual, mesmo que presente
    na árvore do commit de `--capturar-ref` (que grava não rastreados também)."""
    saida = _git(["status", "--porcelain=v1", "--untracked-files=all", "--", caminho], root)
    return saida.startswith("??")


def _texto_do_ref(root: Path, ref: str, caminho: str) -> str:
    return _git(["show", f"{ref}:{caminho}"], root)


def _texto_do_disco(root: Path, caminho: str) -> str | None:
    try:
        return (root / caminho).read_text(encoding="utf-8")
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def _nao_rastreado_mudou_desde_ref(root: Path, ref: str, caminho: str) -> bool:
    """Julgamento por conteúdo (linha a linha, fim de linha normalizado por `str.splitlines`) do
    não rastreado que já existia na árvore de `<ref>` — em vez do recorte por `st_mtime` usado
    para o não rastreado ausente de `<ref>` (esse permanece intocado)."""
    texto_atual = _texto_do_disco(root, caminho)
    if texto_atual is None:
        return True
    return _texto_do_ref(root, ref, caminho).splitlines() != texto_atual.splitlines()


def coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]:
    """Sem `desde`: `git status --porcelain=v1 --untracked-files=all` sozinho, árvore de trabalho
    inteira — ao contrário de `git diff --stat`, também enxerga arquivo novo ainda não rastreado
    (o caso comum de uma tarefa que *cria* arquivo-alvo). `--untracked-files=all` é necessário:
    sem ele, um diretório inteiramente novo aparece colapsado como `dir/` em vez de listar cada
    arquivo dentro dele.

    Com `desde=<ref>` (AUT-T5b): recorta o conjunto de rastreados para só os alterados **desde**
    `<ref>` (`git diff <ref> --name-only`), em vez da árvore de trabalho inteira — necessário
    quando outras tarefas têm mudanças soltas, não commitadas, no mesmo repositório. Untracked
    presente na árvore de `<ref>` (`TK-93a`: `<ref>` de `--capturar-ref` grava não rastreados
    também) é julgado por conteúdo (`_nao_rastreado_mudou_desde_ref`), não por data — ele não
    aparece em `git diff <ref> --name-only` (que o dá como apagado, já que está fora do índice
    atual). Untracked ausente de `<ref>` (ex.: `<ref>` de `git stash create`, que não grava
    não rastreados) segue pelo recorte por data: a entrada `??` cujo arquivo tem `st_mtime` menor
    que a data de commit de `<ref>` (`%ct`) fica de fora; a de data igual ou maior entra, e também
    a que não existe no disco como veio do `git status` (nome entre aspas com escape octal, por
    exemplo)."""
    saida_status = _git(["status", "--porcelain=v1", "--untracked-files=all"], root)
    tocados: dict[str, None] = {}
    if desde is None:
        for linha in saida_status.splitlines():
            if not linha:
                continue
            tocados.setdefault(_extrair_caminho_status(linha), None)
        return sorted(tocados.keys())

    corte = int(_git(["show", "-s", "--format=%ct", desde], root).strip())
    nao_rastreados: set[str] = set()
    for linha in saida_status.splitlines():
        if not linha.startswith("??"):
            continue
        caminho = _extrair_caminho_status(linha)
        nao_rastreados.add(caminho)
        if _existe_no_ref(root, desde, caminho):
            if _nao_rastreado_mudou_desde_ref(root, desde, caminho):
                tocados.setdefault(caminho, None)
            continue
        arquivo = root / caminho
        if arquivo.exists() and arquivo.stat().st_mtime < corte:
            continue
        tocados.setdefault(caminho, None)
    saida_diff = _git(["diff", desde, "--name-only"], root)
    for linha in saida_diff.splitlines():
        linha = linha.strip()
        # não rastreado presente em <ref> sai como apagado aqui (está fora do índice atual); o
        # julgamento dele já foi feito acima, por conteúdo — este loop não o reintroduz (TK-93a).
        if linha and linha not in nao_rastreados:
            tocados.setdefault(linha, None)
    return sorted(tocados.keys())


def coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]:
    """Código `XY` de `git status --porcelain=v1 --untracked-files=all` por caminho (mesma chave
    que `coletar_arquivos_tocados` já extrai via `_extrair_caminho_status`) — a evidência `git`
    que comprova a atribuição de cada arquivo na seção `## Arquivos tocados` (`LM-T3`, `AE-13`).
    Não classifica nada: só devolve o estado bruto que o `git` já relata.

    Com `desde=<ref>` (`LM-T3a`): a árvore de trabalho vence sempre; na ausência dela, e só então,
    entra a letra de `git diff <ref> --name-status`, marcada como commitada (`<letra> (commitado
    desde <ref>)`) via `setdefault` — é o `setdefault`, e não uma atribuição, que materializa essa
    precedência. Para renomeação (`R100\t<velho>\t<novo>`), a chave é o último campo da linha e a
    letra é o primeiro campo inteiro (`R100`)."""
    saida_status = _git(["status", "--porcelain=v1", "--untracked-files=all"], root)
    estados: dict[str, str] = {}
    for linha in saida_status.splitlines():
        if not linha:
            continue
        estados.setdefault(_extrair_caminho_status(linha), linha[:2])
    if desde is not None:
        saida_diff = _git(["diff", desde, "--name-status"], root)
        for linha in saida_diff.splitlines():
            if not linha.strip():
                continue
            campos = linha.split("\t")
            letra = campos[0]
            caminho = campos[-1]
            estados.setdefault(caminho, f"{letra} (commitado desde {desde})")
    return estados


def _normalizar_separador(caminho: str) -> str:
    return caminho.replace("\\", "/")


def _eh_alvo_diretorio(root: Path, alvo: str) -> bool:
    """Um item de `arquivos_alvo` é alvo-diretório quando termina em `/` (declaração explícita)
    ou, após normalizar separador, aponta para um diretório existente na árvore (`root / alvo`)."""
    if _normalizar_separador(alvo).endswith("/"):
        return True
    return (root / alvo).is_dir()


_REGISTRO_ORQUESTRACAO = (
    "docs/DIARIO_DE_OBRAS.md",
    "docs/telemetria.tsv",
    "docs/ACIONAMENTOS_CONSULTOR.tsv",
    "docs/plans/",
    "docs/RDO/",
    "docs/audits/",
)


def _eh_registro_orquestracao(caminho: str) -> bool:
    """Balde (3) da `DB-25` (`P-0739`): arquivo que a orquestração escreve por ofício — kanban,
    telemetria, acionamentos do consultor, plano, RDO, relatório de auditoria. Não é atribuível a tarefa nenhuma e por isso não pesa no veredito;
    aparece nomeado na seção `## Escopo`. Item terminado em `/` casa por prefixo."""
    alvo = _normalizar_separador(caminho)
    for item in _REGISTRO_ORQUESTRACAO:
        if item.endswith("/"):
            if alvo.startswith(item):
                return True
        elif alvo == item:
            return True
    return False


_ATO_DO_DONO = (".claude/agents/",)


def _eh_ato_do_dono(caminho: str) -> bool:
    """Balde (4) da `DB-32` (`P-0739`): arquivo que só o dono edita, fora do ciclo de qualquer
    tarefa — definição de agente. A árvore de trabalho é compartilhada, então essa edição aparece
    em toda tarefa executada enquanto estiver pendente; sai nomeada na seção `## Escopo` e não
    pesa no veredito. Item terminado em `/` casa por prefixo."""
    alvo = _normalizar_separador(caminho)
    return any(alvo.startswith(item) for item in _ATO_DO_DONO)


def _status_do_dossie(dossie) -> str | None:
    """Primeiro literal entre crases do par `Status` de `dossie.extras`; sem par ou sem literal →
    `None`."""
    for rotulo, conteudo in dossie.extras:
        if rotulo.strip().lower() == "status":
            m = _BACKTICK_RE.search(conteudo)
            return m.group(1).strip() if m else None
    return None


def mapear_alvos_de_outras_tarefas(plano_path: Path, tarefa_id: str, root: Path) -> dict[str, str]:
    """Balde (2) da `DB-25`: `git` não sabe qual tarefa tocou qual arquivo, mas o plano sabe qual
    tarefa declarou qual alvo. Percorre os cabeçalhos `### <ID>` do mesmo plano com a gramática
    de ID que mora em `rdo.py` (residência única, `DB-22`), extrai o dossiê de cada tarefa que
    não seja `tarefa_id` e devolve `caminho -> primeiro ID que o declara`, na ordem do arquivo.
    Tarefa cujo dossiê não extrai é pulada: atribuição ausente nunca bloqueia (`DB-19`). Tarefa não
    despachada (`status` fora de `in-progress`/`review`/`done`, ou ausente) é pulada, porque alvo
    declarado sem despacho é previsão, não autoria (`TK-66`)."""
    rdo = _load_rdo(root)
    mapa: dict[str, str] = {}
    for linha in Path(plano_path).read_text(encoding="utf-8").splitlines():
        m = rdo._ID_HEADER_RE.match(linha)
        if not m or m.group(1) == tarefa_id:
            continue
        try:
            dossie = rdo.extrair_dossie(
                plano_path,
                m.group(1),
                esquema_legado=False,
                modelo_legado=None,
                classe_legado=None,
            )
        except rdo.RdoValidationError:
            continue
        if _status_do_dossie(dossie) not in _STATUS_DESPACHADO:
            continue
        for caminho in extrair_arquivos_alvo(dossie.campos):
            mapa.setdefault(_normalizar_separador(caminho), m.group(1))
    return mapa


def _tarefa_dona(tocado_norm: str, outros: dict[str, str], root: Path) -> str | None:
    """Tarefa do mesmo plano que declarou `tocado_norm` como alvo (`TK-74`): o caminho exato vence;
    sem ele, o alvo-diretório de prefixo mais longo; nenhum dos dois → `None`."""
    exato = outros.get(tocado_norm)
    if exato is not None:
        return exato
    melhor: tuple[int, str] | None = None
    for chave, tarefa in outros.items():
        if not _eh_alvo_diretorio(root, chave):
            continue
        prefixo = _normalizar_separador(chave).rstrip("/") + "/"
        if tocado_norm.startswith(prefixo) and (melhor is None or len(prefixo) > melhor[0]):
            melhor = (len(prefixo), tarefa)
    return melhor[1] if melhor else None


def confrontar_escopo(
    tocados: list[str],
    arquivos_alvo: list[str],
    root: Path,
    alvos_de_outras_tarefas: dict[str, str] | None = None,
) -> dict:
    """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`) com os cinco
    baldes da `DB-25` e da `DB-32`, nesta precedência: coberto pelos alvos do card > alvo de outra
    tarefa do mesmo plano > registro da orquestração > ato do dono fora do ciclo de tarefa > fora
    dos alvos sem atribuição. Só o último resolve o
    veredito: vazio → `conforme`; não vazio → `None` (aberto), porque a faixa `parcial` depende de
    desvio declarado na entrega, insumo que este script não recebe.

    Alvo-diretório (`_eh_alvo_diretorio`) casa por prefixo (AUT-T5b); a atribuição a outra tarefa
    casa por caminho exato e, sem ele, pelo alvo-diretório de prefixo mais longo (`TK-74`), depois
    de normalizar `\\`→`/` nos dois lados."""
    alvo_set = set(arquivos_alvo)
    prefixos_dir = [
        _normalizar_separador(alvo).rstrip("/") + "/"
        for alvo in arquivos_alvo
        if _eh_alvo_diretorio(root, alvo)
    ]
    outros = alvos_de_outras_tarefas or {}

    def coberto(tocado: str) -> bool:
        if tocado in alvo_set:
            return True
        tocado_norm = _normalizar_separador(tocado)
        return any(tocado_norm.startswith(prefixo) for prefixo in prefixos_dir)

    de_outra_tarefa: dict[str, str] = {}
    registro: list[str] = []
    ato_do_dono: list[str] = []
    fora: list[str] = []
    for tocado in sorted(tocados):
        if coberto(tocado):
            continue
        tocado_norm = _normalizar_separador(tocado)
        dona = _tarefa_dona(tocado_norm, outros, root)
        if dona is not None:
            de_outra_tarefa[tocado] = dona
        elif _eh_registro_orquestracao(tocado):
            registro.append(tocado)
        elif _eh_ato_do_dono(tocado):
            ato_do_dono.append(tocado)
        else:
            fora.append(tocado)
    return {
        "fora_dos_alvos": fora,
        "de_outra_tarefa": de_outra_tarefa,
        "registro_orquestracao": registro,
        "ato_do_dono": ato_do_dono,
        "veredito": "conforme" if not fora else None,
    }


def formatar_atribuicoes(tocados: list[str], escopo: dict) -> list[str]:
    """Verbo `--atribuir` (`LM-T2a`): uma linha `atribuicao: <caminho> -> <balde>` por arquivo
    tocado, na ordem de `sorted()`, mais a linha de resumo por último. O balde `alvo-do-card` sai
    por **diferença de conjuntos** sobre os quatro baldes alheios que `confrontar_escopo` já
    devolve (`de_outra_tarefa`, `registro_orquestracao`, `ato_do_dono`, `fora_dos_alvos`) — nunca
    por uma segunda checagem de cobertura. Informa, não julga: não há exit diferente por balde."""
    de_outra = escopo.get("de_outra_tarefa", {})
    registro = set(escopo.get("registro_orquestracao", []))
    ato_do_dono = set(escopo.get("ato_do_dono", []))
    fora = set(escopo.get("fora_dos_alvos", []))

    linhas: list[str] = []
    sem_atribuicao = 0
    for caminho in sorted(tocados):
        if caminho in de_outra:
            linhas.append(f"atribuicao: {caminho} -> alvo-de-outra-tarefa ({de_outra[caminho]})")
        elif caminho in registro:
            linhas.append(f"atribuicao: {caminho} -> registro-da-orquestracao")
        elif caminho in ato_do_dono:
            linhas.append(f"atribuicao: {caminho} -> ato-do-dono")
        elif caminho in fora:
            linhas.append(f"atribuicao: {caminho} -> sem-atribuicao")
            sem_atribuicao += 1
        else:
            linhas.append(f"atribuicao: {caminho} -> alvo-do-card")
    linhas.append(f"atribuicao: OK - {len(tocados)} arquivo(s), {sem_atribuicao} sem atribuicao.")
    return linhas


def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -> str:
    if desde is not None:
        if _eh_nao_rastreado(root, caminho_rel) and _existe_no_ref(root, desde, caminho_rel):
            # TK-93a: `git diff <ref> -- caminho` daria este não rastreado como apagado (está fora
            # do índice atual) — o diff unificado é montado à mão contra o conteúdo em `<ref>`.
            texto_atual = _texto_do_disco(root, caminho_rel)
            if texto_atual is None:
                return "(arquivo binário ou não-UTF-8 — trecho omitido)"
            linhas_ref = _texto_do_ref(root, desde, caminho_rel).splitlines()
            linhas_atual = texto_atual.splitlines()
            if linhas_ref == linhas_atual:
                return f"(sem alteração desde `{desde}`)"
            diff_linhas = difflib.unified_diff(
                linhas_ref,
                linhas_atual,
                fromfile=f"{caminho_rel}@{desde}",
                tofile=caminho_rel,
                lineterm="",
            )
            return "\n".join(diff_linhas) + "\n"
        texto = _git(["diff", desde, "--", caminho_rel], root)
        if texto.strip():
            return texto
        if _existe_no_ref(root, desde, caminho_rel):
            return f"(sem alteração desde `{desde}`)"
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


def montar_trechos(
    root: Path,
    arquivos_alvo: list[str],
    teto_chars: int,
    tocados: list[str] | None = None,
    desde: str | None = None,
) -> dict[str, dict]:
    """Trecho de diff (ou conteúdo integral, se o arquivo é novo e sem diff registrável) de cada
    arquivo-alvo, truncado em `teto_chars` — truncamento sempre marcado na saída (nunca
    silencioso).

    Alvo-diretório (AUT-T5b): em vez de diffar o path do diretório direto (que sempre cairia no
    fallback "arquivo ausente"), expande para os `tocados` que casam pelo mesmo prefixo e gera uma
    entrada de trecho por arquivo real dentro dele. `tocados` é opcional — só é preciso quando
    algum item de `arquivos_alvo` é diretório; alvo-arquivo comum segue o caminho de sempre."""
    trechos: dict[str, dict] = {}
    for caminho in arquivos_alvo:
        if tocados and _eh_alvo_diretorio(root, caminho):
            prefixo = _normalizar_separador(caminho).rstrip("/") + "/"
            for arquivo in tocados:
                if not _normalizar_separador(arquivo).startswith(prefixo):
                    continue
                texto = _diff_para_arquivo(root, arquivo, desde)
                truncado = len(texto) > teto_chars
                trechos[arquivo] = {
                    "texto": texto[:teto_chars] if truncado else texto,
                    "truncado": truncado,
                }
            continue
        texto = _diff_para_arquivo(root, caminho, desde)
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


def secao_medida_do_executor(caminho_json: Path) -> list[str]:
    """`## Medida do executor` (`FPU-T5`, DFP-17): a medida que o executor gravou via
    `card_check.py --gravar` (`verificar_tarefa` -> `medida`), incorporada como tabela — registro,
    não prosa (a régua executável não aceita prosa como verde). Arquivo ausente ou JSON
    ilegível/incompleto nomeia o fato como uma linha, sem lançar exceção."""
    caminho_json = Path(caminho_json)
    linhas: list[str] = ["## Medida do executor"]
    if not caminho_json.is_file():
        linhas.append(f"- ausente: {caminho_json} não existe")
        return linhas

    try:
        dados = json.loads(caminho_json.read_text(encoding="utf-8"))
        mundo = dados["mundo"]
        gerado_em = dados["gerado_em"]
        linhas_itens: list[str] = []
        for item in dados["itens"]:
            indice = item["indice"]
            comando = item["comando"]
            exit_valor = item["exit"]
            bate = item["bate"]
            if comando is not None:
                comando_escapado = comando.replace("|", "\\|")
                comando_txt = f"`{comando_escapado}`"
            else:
                comando_txt = "-"
            exit_txt = "-" if exit_valor is None else str(exit_valor)
            bate_txt = "true" if bate else "false"
            linhas_itens.append(f"| {indice} | {comando_txt} | {exit_txt} | {bate_txt} |")
    except (ValueError, KeyError, TypeError) as exc:
        linhas.append(f"- ilegível: {caminho_json} ({exc})")
        return linhas

    linhas.append(f"- Arquivo: {caminho_json}; mundo: {mundo}; gerado em: {gerado_em}")
    linhas.append("")
    linhas.append("| item | comando | exit | bate |")
    linhas.append("|---|---|---|---|")
    linhas.extend(linhas_itens)
    return linhas


def _renderizar(
    *,
    plano_id: str,
    tarefa_id: str,
    diff_stat: str,
    arquivos_tocados: list[str],
    arquivos_alvo: list[str],
    literais_descartados: list[str] | None = None,
    escopo: dict,
    estado_git: dict[str, str] | None = None,
    trechos: dict[str, dict],
    teto_diff_chars: int,
    resultados_guardas: list[dict],
    veredito_guardas_valor: str,
    veredito_testes_valor: str,
    teto_guarda_chars: int,
    desde: str | None = None,
    linhas_medida: list[str] | None = None,
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
        estados = estado_git or {}
        alheio = (
            set(escopo.get("fora_dos_alvos", []))
            | set(escopo.get("de_outra_tarefa", {}).keys())
            | set(escopo.get("registro_orquestracao", []))
            | set(escopo.get("ato_do_dono", []))
        )
        for caminho in arquivos_tocados:
            atribuicao = "alheio" if caminho in alheio else "da entrega"
            codigo = estados.get(caminho)
            estado_txt = f"`{codigo}`" if codigo is not None else "(sem entrada em `git status`)"
            linhas.append(f"- `{caminho}` — atribuição: {atribuicao}; estado git: {estado_txt}")
    else:
        linhas.append("- nenhum arquivo tocado")
    linhas.append("")
    linhas.append("## Escopo")
    if desde is not None:
        linhas.append(f"- Recorte: desde `{desde}`")
    else:
        linhas.append("- Recorte: árvore de trabalho inteira (nenhum `--desde` informado)")
    alvos_txt = ", ".join(f"`{c}`" for c in arquivos_alvo) if arquivos_alvo else "(nenhum declarado)"
    tocados_txt = ", ".join(f"`{c}`" for c in arquivos_tocados) if arquivos_tocados else "(nenhum)"
    linhas.append(f"- Arquivos-alvo declarados: {alvos_txt}")
    if literais_descartados:
        descartados_txt = ", ".join(f"`{c}`" for c in literais_descartados)
        linhas.append(
            f"- Literais não reconhecidos como caminho "
            f"({len(literais_descartados)}): {descartados_txt}"
        )
    linhas.append(f"- Arquivos tocados: {tocados_txt}")
    if escopo.get("de_outra_tarefa"):
        pares = ", ".join(
            f"`{caminho}` → `{tarefa}`"
            for caminho, tarefa in sorted(escopo["de_outra_tarefa"].items())
        )
        linhas.append(f"- Atribuídos a outra tarefa do mesmo plano: {pares}")
    if escopo.get("registro_orquestracao"):
        reg_txt = ", ".join(f"`{c}`" for c in escopo["registro_orquestracao"])
        linhas.append(f"- Registro da orquestração (não atribuível a tarefa): {reg_txt}")
    if escopo.get("ato_do_dono"):
        dono_txt = ", ".join(f"`{c}`" for c in escopo["ato_do_dono"])
        linhas.append(f"- Ato do dono, fora do ciclo de tarefa: {dono_txt}")
    if escopo["veredito"] == "conforme":
        linhas.append("- Veredito mecânico: conforme")
    else:
        fora_txt = ", ".join(f"`{c}`" for c in escopo["fora_dos_alvos"])
        linhas.append(
            f"- Fato: {len(escopo['fora_dos_alvos'])} arquivo(s) fora dos alvos e sem "
            f"atribuição: {fora_txt}"
        )
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
    if linhas_medida is not None:
        linhas.extend(linhas_medida)
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
    desde: str | None = None,
    dir_evidencia: Path | None = None,
) -> str:
    plano_path = Path(plano_path)
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
        raise ReviewEvidenceValidationError(str(exc)) from exc

    arquivos_alvo = extrair_arquivos_alvo(dossie.campos)
    literais_descartados = extrair_literais_nao_caminho(dossie.campos)
    diff_stat = coletar_diff_stat(root, desde)
    tocados = coletar_arquivos_tocados(root, desde)
    alvos_de_outras = mapear_alvos_de_outras_tarefas(plano_path, dossie.tarefa_id, root)
    escopo = confrontar_escopo(tocados, arquivos_alvo, root, alvos_de_outras)
    estado_git = coletar_estado_git(root, desde)
    trechos = montar_trechos(root, arquivos_alvo, teto_diff_chars, tocados, desde)
    resultados_guardas = rodar_bateria_guardas(root, comandos_guardas)
    veredito_guardas_valor = veredito_guardas(resultados_guardas)
    veredito_testes_valor = veredito_testes(resultados_guardas)

    plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem

    if dir_evidencia is not None:
        caminho_medida = Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"
    else:
        caminho_medida = _caminhos.destino_medida(root, plano_path, dossie.tarefa_id)

    return _renderizar(
        plano_id=plano_id,
        tarefa_id=dossie.tarefa_id,
        diff_stat=diff_stat,
        arquivos_tocados=tocados,
        arquivos_alvo=arquivos_alvo,
        literais_descartados=literais_descartados,
        escopo=escopo,
        estado_git=estado_git,
        trechos=trechos,
        teto_diff_chars=teto_diff_chars,
        resultados_guardas=resultados_guardas,
        veredito_guardas_valor=veredito_guardas_valor,
        veredito_testes_valor=veredito_testes_valor,
        teto_guarda_chars=teto_guarda_chars,
        desde=desde,
        linhas_medida=secao_medida_do_executor(caminho_medida),
    )


def main(argv: list[str] | None = None) -> int:
    _forcar_utf8(sys.stdout)
    _forcar_utf8(sys.stderr)
    parser = argparse.ArgumentParser(
        description=(
            "Evidência de revisão (metade git) — diff, arquivos tocados e confronto de escopo, "
            "mecânico e sem interpretação (EXA-T9a)."
        )
    )
    parser.add_argument("--plano", type=Path, default=None, help="Caminho do .md do plano.")
    parser.add_argument("--tarefa", default=None, help="Identificador da tarefa (ex.: T9a).")
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
        "--out",
        type=Path,
        default=None,
        help="Também grava o documento neste caminho (escrita atômica); sem ele, plano em pasta grava em <pasta-do-plano>/evidencia/<tarefa>.md.",
    )
    parser.add_argument(
        "--desde",
        default=None,
        help=(
            "Ref git (ex.: SHA capturado no despacho) para recortar arquivos tocados a partir "
            "dela, em vez da árvore de trabalho inteira (AUT-T5b)."
        ),
    )
    parser.add_argument(
        "--atribuir",
        action="store_true",
        help=(
            "Imprime a atribuição de cada arquivo tocado desde --desde nos cinco baldes de "
            "confrontar_escopo e sai (LM-T2a); não monta nem grava o dossiê."
        ),
    )
    parser.add_argument(
        "--capturar-ref",
        dest="capturar_ref",
        action="store_true",
        help=(
            "Imprime o <ref> (SHA de um commit cuja árvore é a árvore de trabalho inteira, "
            "rastreados e não rastreados, sem alterar árvore, índice nem lista de stash) e sai "
            "(TK-93a); não exige --plano nem --tarefa."
        ),
    )
    args = parser.parse_args(argv)

    if args.capturar_ref:
        print(capturar_ref(args.root))
        return 0

    if args.plano is None or args.tarefa is None:
        parser.error("--plano e --tarefa são obrigatórios (exceto com --capturar-ref).")

    if args.atribuir:
        rdo = _load_rdo(args.root)
        try:
            _exigir_plano(args.plano)
            dossie = rdo.extrair_dossie(
                args.plano,
                args.tarefa,
                esquema_legado=False,
                modelo_legado=None,
                classe_legado=None,
            )
        except (ReviewEvidenceValidationError, rdo.RdoValidationError) as exc:
            print(f"review_evidence: FALHOU - {exc}", file=sys.stderr)
            return 1
        arquivos_alvo = extrair_arquivos_alvo(dossie.campos)
        tocados = coletar_arquivos_tocados(args.root, args.desde)
        alvos_de_outras = mapear_alvos_de_outras_tarefas(args.plano, dossie.tarefa_id, args.root)
        escopo = confrontar_escopo(tocados, arquivos_alvo, args.root, alvos_de_outras)
        for linha in formatar_atribuicoes(tocados, escopo):
            print(linha)
        return 0

    if args.out is None:
        pasta_plano = _caminhos.pasta_do_plano(args.plano)
        if pasta_plano is not None:
            args.out = _caminhos.destino_evidencia(pasta_plano, args.tarefa)

    try:
        documento = montar_documento(
            args.plano,
            args.tarefa,
            args.root,
            teto_diff_chars=args.max_diff_chars,
            desde=args.desde,
            dir_evidencia=args.out.parent if args.out is not None else None,
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
