"""BKL-T2 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T2`) — TF/TR do núcleo
somente-leitura de `.claude/tools/backlog.py`: parser, `check` (violações `C-1..C-9`) e `show`
(dossiê verbatim truncado ao teto `DB-7`).

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_telemetria.py`
para `.claude/tools/telemetria.py`.

Todas as asserções trabalham sobre fixtures em `tests/fixtures/backlog/{verde,vermelho}/` copiadas
para `tmp_path` — nunca contra o repositório real (`docs/DIARIO_DE_OBRAS.md` e `docs/plans/` são
insumo, nunca alvo desta suíte)."""
from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_BACKLOG_PATH = _ROOT / ".claude" / "tools" / "backlog.py"
_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "backlog"
_FIXTURE_VERDE = _FIXTURES / "verde"
_FIXTURE_VERMELHO = _FIXTURES / "vermelho"
_FIXTURE_NEXT_TK90 = _FIXTURES / "next_tk90"
_FIXTURE_NEXT_TK90_SEM_INDICE = _FIXTURES / "next_tk90_sem_indice"
_FIXTURE_INBOX_PLANOS = _FIXTURES / "inbox_planos" / "_INBOX.md"


def _load_backlog():
    spec = importlib.util.spec_from_file_location("backlog", _BACKLOG_PATH)
    module = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via
    # `sys.modules[cls.__module__]` — precisa estar registrado antes do exec_module.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _copiar_fixture(origem: Path, destino: Path) -> Path:
    shutil.copytree(origem, destino)
    return destino


# --------------------------------------------------------------------------- #
# TF parser — 3 formas de ID (DB-14), campo Status com/sem razão, heading legado
# --------------------------------------------------------------------------- #


def test_tf_parser_tres_formas_de_id_db14():
    backlog = _load_backlog()
    linhas = [
        "### T7 — Tarefa sem prefixo [Sonnet · classe mecanica]",
        "- **Status:** `done` · 2026-01-01",
        "",
        "### BKL-T2 — Tarefa com prefixo [Sonnet · classe implementacao]",
        "- **Status:** `ready` · 2026-01-01",
        "",
        "### TK-54a — Subtarefa de tíquete [Opus · classe investigacao]",
        "- **Status:** `ready` · 2026-01-01",
    ]
    itens = backlog._scan_items(linhas, "arquivo.md")
    ids_e_tipos = {(it.id, it.tipo) for it in itens}
    assert ("T7", "tarefa") in ids_e_tipos
    assert ("BKL-T2", "tarefa") in ids_e_tipos
    assert ("TK-54a", "subtarefa") in ids_e_tipos
    assert all(it.header_valido for it in itens)


def test_tf_status_com_e_sem_razao():
    backlog = _load_backlog()
    linhas_com_razao = [
        "### T1 — X [Sonnet · classe mecanica]",
        "- **Status:** `blocked` · 2026-02-02 · aguardando dono",
    ]
    linhas_sem_razao = [
        "### T1 — X [Sonnet · classe mecanica]",
        "- **Status:** `ready` · 2026-02-02",
    ]
    item_com = backlog._scan_items(linhas_com_razao, "a.md")[0]
    item_sem = backlog._scan_items(linhas_sem_razao, "a.md")[0]
    assert item_com.status == "blocked"
    assert item_com.status_razao == "aguardando dono"
    assert item_sem.status == "ready"
    assert item_sem.status_razao is None


def test_tf_heading_legado_sem_bracket_e_c1():
    backlog = _load_backlog()
    linhas = [
        "### TK-54a — O extrato [classe investigacao]",  # sem <modelo> · — forma real do repo
        "- **Status:** `ready` · 2026-01-01",
    ]
    item = backlog._scan_items(linhas, "arquivo.md")[0]
    assert item.tipo == "subtarefa"
    assert item.id == "TK-54a"
    assert item.header_valido is False


# --------------------------------------------------------------------------- #
# TF check — vermelho dispara C-1..C-9 uma vez cada; verde não dispara nada
# --------------------------------------------------------------------------- #


def test_tf_check_vermelho_dispara_cada_codigo_uma_vez(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERMELHO, tmp_path / "repo")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo)

    codigos = [v.codigo for v in violacoes]
    esperados = [f"C-{n}" for n in range(1, 10)]
    assert sorted(codigos) == sorted(esperados)
    for v in violacoes:
        assert v.arquivo and v.linha > 0 and v.texto


def test_tf_check_verde_sem_violacoes(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")

    modelo = backlog.carregar(repo)
    violacoes = backlog.check(modelo)

    assert violacoes == []


# --------------------------------------------------------------------------- #
# TF show — trunca em 8.000 chars / 120 linhas com ponteiro arquivo:l1-l2
# --------------------------------------------------------------------------- #


def test_tf_show_trunca_em_8000_chars_120_linhas_com_ponteiro():
    backlog = _load_backlog()
    linhas_geradas = [f"linha {i:03d} de conteúdo qualquer para encher o dossiê de teste" for i in range(1, 201)]
    texto = "\n".join(linhas_geradas)
    plano = backlog.Plano(
        id="P-9000",
        titulo="Longo",
        arquivo="docs/plans/P-9000-longo.md",
        linha_header=1,
        linha_fim=200,
        texto=texto,
        status="ready",
        prefixo="LNG",
    )
    modelo = backlog.Modelo(planos=[plano], tiquetes=[], indice=[], diario_arquivo="docs/DIARIO_DE_OBRAS.md")

    saida = backlog.show(modelo, "P-9000")

    assert len(saida) < len(texto)
    assert "linha 001" in saida
    assert "linha 200" not in saida
    assert "docs/plans/P-9000-longo.md:1-200" in saida
    assert len(saida) <= 8000 + 200
    assert len(saida.splitlines()) <= 121


def test_tf_show_id_desconhecido():
    backlog = _load_backlog()
    modelo = backlog.Modelo(planos=[], tiquetes=[], indice=[], diario_arquivo="docs/DIARIO_DE_OBRAS.md")
    assert "não encontrado" in backlog.show(modelo, "P-0000")


# --------------------------------------------------------------------------- #
# TR — carregar nunca abre *_HISTORICO.md
# --------------------------------------------------------------------------- #


def test_tr_carregar_nunca_abre_historico(tmp_path, monkeypatch):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")

    # Decoys que carregar() jamais deveria tocar (histórico é append-only e nunca lido, DB-9).
    (repo / "docs" / "DIARIO_HISTORICO.md").write_text("PROIBIDO", encoding="utf-8")
    (repo / "docs" / "plans" / "_INBOX_HISTORICO.md").write_text("PROIBIDO", encoding="utf-8")

    original_open = Path.open

    def _open_guardado(self, *args, **kwargs):
        if "_HISTORICO" in str(self):
            raise AssertionError(f"carregar() abriu um histórico proibido: {self}")
        return original_open(self, *args, **kwargs)

    monkeypatch.setattr(Path, "open", _open_guardado)

    modelo = backlog.carregar(repo)

    assert len(modelo.planos) == 2


# --------------------------------------------------------------------------- #
# BKL-T3 (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T3`) — TF/TR do verbo
# somente-leitura `next`: seleção determinística (§2.5) e renderização (§2.6).
#
# Os oito TFs de ramo abaixo constroem `Modelo`/`Plano`/`Item` diretamente (mesmo padrão de
# `test_tf_show_trunca_em_8000_chars_120_linhas_com_ponteiro`), sem tocar disco — não há
# residência real a computar para exercitar a ordem de seleção em si. Os quatro TFs da RP-5
# (worked examples A/B de §2.6) usam as fixtures em disco `next_tk90` e
# `next_tk90_sem_indice`, que carregam `- **Tipo:** bug` no tíquete `TK-90` (nenhuma fixture
# pré-existente tinha esse campo — confirmado por grep antes desta tarefa).
# --------------------------------------------------------------------------- #


def _fabricas(backlog):
    """Fábricas de dataclasses do módulo `backlog` carregado por `_load_backlog()` — o módulo
    não é importável estaticamente (carregado via importlib), então as fábricas só podem
    referenciar `backlog.Item`/`backlog.Plano`/`backlog.LinhaIndice`/`backlog.Modelo` depois de
    `_load_backlog()` ter rodado."""

    def item(id_, status, depende_de=None, campo_tipo=None, linha_header=10):
        return backlog.Item(
            id=id_,
            tipo="tarefa",
            titulo=f"Título de {id_}",
            arquivo="docs/plans/PLANO-x.md",
            linha_header=linha_header,
            linha_fim=linha_header + 1,
            texto=(
                f"### {id_} — Título de {id_} [Sonnet · classe mecanica]\n"
                f"- **Status:** `{status}` · 2026-01-01"
            ),
            modelo="Sonnet",
            classe="mecanica",
            header_valido=True,
            status=status,
            status_linha=linha_header + 1,
            status_razao=None,
            depende_de=depende_de or [],
            campo_tipo=campo_tipo,
        )

    def plano(id_, status, tarefas, ordem_execucao=None, linha_fim=50):
        return backlog.Plano(
            id=id_,
            titulo=f"Título de {id_}",
            arquivo=f"docs/plans/{id_}-x.md",
            linha_header=1,
            linha_fim=linha_fim,
            texto="conteúdo qualquer",
            status=status,
            tarefas=tarefas,
            ordem_execucao=ordem_execucao or [],
        )

    def linha_indice(id_, status_bruto="ready", linha=10):
        return backlog.LinhaIndice(
            id=id_,
            titulo=f"Título de {id_}",
            status_bruto=status_bruto,
            arquivo="docs/DIARIO_DE_OBRAS.md",
            linha=linha,
            ancora=f"docs/plans/{id_}-x.md",
        )

    def modelo(planos, indice, diretiva_ids=None):
        return backlog.Modelo(
            planos=planos,
            tiquetes=[],
            indice=indice,
            diario_arquivo="docs/DIARIO_DE_OBRAS.md",
            diario_linhas=[],
            diretiva_ids=diretiva_ids or [],
        )

    return item, plano, linha_indice, modelo


def test_tf_retomada_de_in_progress():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "in-progress")
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "ready", [t1, t2])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T1"


def test_tf_diretiva_restringe_candidatos():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "ready", [t1])
    p2 = plano("P-0002", "ready", [t2])
    indice = [linha_indice("P-0001", linha=10), linha_indice("P-0002", linha=11)]

    sem_diretiva = backlog.selecionar_next(modelo([p1, p2], indice))
    assert sem_diretiva.vencedor.item.id == "T1"  # P-0001 vence por FIFO (linha 10 < 11)

    com_diretiva = backlog.selecionar_next(modelo([p1, p2], indice, diretiva_ids=["P-0002"]))
    assert com_diretiva.exit_code == 0
    assert com_diretiva.vencedor.item.id == "T2"


def test_tf_depende_de_nao_done_segura_candidato():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t9 = item("T9", "ready")  # dependência ainda não done
    t1 = item("T1", "ready", depende_de=["T9"])
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "ready", [t9, t1, t2])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T9"  # T1 fica preso por Depende de; T9 é elegível primeiro


def test_tf_plano_blocked_nao_contribui():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")
    t2 = item("T2", "ready")
    p1 = plano("P-0001", "blocked", [t1])
    p2 = plano("P-0002", "ready", [t2])
    m = modelo([p1, p2], [linha_indice("P-0001", linha=10), linha_indice("P-0002", linha=11)])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T2"


def test_tf_ordem_de_execucao_vence_ordem_dos_cabecalhos():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")  # primeiro no cabeçalho
    t2 = item("T2", "ready")  # primeiro na Ordem de execução
    p1 = plano("P-0001", "ready", [t1, t2], ordem_execucao=["T2", "T1"])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "T2"


def test_tf_fila_vazia_exit2():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "blocked")
    p1 = plano("P-0001", "ready", [t1])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 2


def test_tf_dois_in_progress_exit3():
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "in-progress")
    t2 = item("T2", "in-progress")
    p1 = plano("P-0001", "ready", [t1, t2])
    m = modelo([p1], [linha_indice("P-0001")])

    selecao = backlog.selecionar_next(m)

    assert selecao.exit_code == 3
    assert "T1" in selecao.mensagem and "T2" in selecao.mensagem


def test_tf_rodape_lista_blocked_e_conta_memoria_inbox(tmp_path):
    backlog = _load_backlog()
    item, plano, linha_indice, modelo = _fabricas(backlog)

    t1 = item("T1", "ready")
    t_blocked = item("T2", "blocked")
    t_blocked.status_razao = "dependencia"
    p1 = plano("P-0001", "ready", [t1, t_blocked])
    m = modelo([p1], [linha_indice("P-0001")])

    inbox = tmp_path / "_INBOX.md"
    inbox.write_text(
        "\n".join(
            [
                "- 2026-01-01 — a — feedback — candidato 1 — **origem:** x",
                "- 2026-01-02 — b — feedback — candidato 2 — **origem:** y [promovido]",
                "- 2026-01-03 — c — feedback — candidato 3 — **origem:** z",
            ]
        ),
        encoding="utf-8",
    )

    selecao = backlog.selecionar_next(m)
    assert selecao.exit_code == 0
    saida = backlog.renderizar_next(m, selecao, memoria_inbox=inbox)

    assert "fila de memória: 2 candidato(s)" in saida
    assert "T2 (dependencia)" in saida


def test_tr_saida_do_next_cabe_no_teto(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    saida = backlog.renderizar_next(modelo, selecao)

    assert len(saida) <= 8200


# --------------------------------------------------------------------------- #
# RP-5 — os quatro TFs fechados pela rodada de replanejamento: forma por tipo de pai
# (DB-33), faixa de bug sobre itens elegíveis (DB-35) e antecessora omitida no primeiro
# irmão (DB-34). Usam a fixture em disco `next_tk90` (com `TK-90` marcado `- **Tipo:** bug`)
# e `next_tk90_sem_indice` (mesmo `TK-90`, sem linha de índice).
# --------------------------------------------------------------------------- #


def test_tf_bug_antes_de_fifo(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "TK-90a"

    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()
    assert (
        linhas[1]
        == "tíquete: TK-90 — Relatório diário sai com data trocada (0/2) · "
        "residência: docs/DIARIO_DE_OBRAS.md:10-18 · índice: docs/DIARIO_DE_OBRAS.md#tk-90"
    )
    assert "antecessora:" not in saida  # TK-90a é o primeiro irmão sob TK-90 (DB-34)


def test_tf_linha_do_pai_plano(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    modelo.diretiva_ids = ["P-0090"]  # restringe a P-0090 (DB-1: campo já resolvido, sem parsear diretiva aqui)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0
    assert selecao.vencedor.item.id == "FFO-T2"

    num_linhas_plano = len((repo / "docs" / "plans" / "P-0090-fifo.md").read_text(encoding="utf-8").splitlines())
    saida = backlog.renderizar_next(modelo, selecao)
    linhas = saida.splitlines()

    assert linhas[1].startswith("plano: ")
    assert "P-0090" in linhas[1]
    assert "Plano fifo perdedor" in linhas[1]
    assert "(1/2)" in linhas[1]  # DB-36: FFO-T1 done, FFO-T2 ready — 1 done de 2 vivos
    assert f"residência: docs/plans/P-0090-fifo.md:1-{num_linhas_plano}" in linhas[1]
    assert "índice: docs/plans/P-0090-fifo.md" in linhas[1]


def test_tf_antecessora_omitida_no_primeiro_irmao(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")

    # sub-caso 1: vencedor (TK-90a) é o primeiro irmão sob TK-90 — sem linha `antecessora:`.
    modelo1 = backlog.carregar(repo)
    selecao1 = backlog.selecionar_next(modelo1)
    saida1 = backlog.renderizar_next(modelo1, selecao1)
    assert "antecessora:" not in saida1

    # sub-caso 2: vencedor (FFO-T2) não é o primeiro irmão — FFO-T1 é a antecessora, sem
    # bloco `Notas de execução`, então a linha 3 termina em "sem notas" (DB-34).
    modelo2 = backlog.carregar(repo)
    modelo2.diretiva_ids = ["P-0090"]
    selecao2 = backlog.selecionar_next(modelo2)
    saida2 = backlog.renderizar_next(modelo2, selecao2)
    linhas2 = saida2.splitlines()
    assert linhas2[2] == "antecessora: FFO-T1 (done; sem notas)"


def test_tf_pai_sem_linha_de_indice_sai_exit_3(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90_SEM_INDICE, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert "linha de índice ausente para TK-90" in selecao.mensagem


# --------------------------------------------------------------------------- #
# BKL-T3a (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T3a`) — substrings
# obrigatórias das três condições de exit 3 de `next` (§2.5 item 6) e gramática por
# arquivo do contador de pendências do rodapé (§2.4 / DB-38).
# --------------------------------------------------------------------------- #


def test_tf_contador_do_inbox_de_planos_ignora_drenada_e_linha_sem_plano(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0

    saida = backlog.renderizar_next(modelo, selecao, inbox_planos=_FIXTURE_INBOX_PLANOS)

    assert "inbox de planos: 1 por drenar" in saida
    assert "inbox de planos: 3 por drenar" not in saida


def test_tf_exit_3_dois_in_progress_nomeia_os_ids(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    alvo = "- **Status:** `ready` · 2026-01-01"
    secao_atual = None
    for i, linha in enumerate(linhas):
        if linha.startswith("### TK-90a"):
            secao_atual = "TK-90a"
            continue
        if linha.startswith("### TK-90b"):
            secao_atual = "TK-90b"
            continue
        if secao_atual in ("TK-90a", "TK-90b") and linha.strip() == alvo:
            linhas[i] = "- **Status:** `in-progress` · 2026-01-01"
            secao_atual = None
    diario.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert "dois ou mais itens in-progress: TK-90a, TK-90b" in selecao.mensagem


def test_tf_exit_3_item_sem_linha_de_status(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    alvo = "- **Status:** `ready` · 2026-01-01"
    secao_atual = None
    saida_linhas = []
    for linha in linhas:
        if linha.startswith("### TK-90a"):
            secao_atual = "TK-90a"
            saida_linhas.append(linha)
            continue
        if secao_atual == "TK-90a" and linha.strip() == alvo:
            secao_atual = None
            continue  # remove a linha de Status de TK-90a — vencedor da fixture intacta
        saida_linhas.append(linha)
    diario.write_text("\n".join(saida_linhas) + "\n", encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert "linha de status ausente para TK-90a" in selecao.mensagem


# --------------------------------------------------------------------------- #
# BKL-T3b (`docs/plans/P-0739-backlog-instrumento.md` `### BKL-T3b`) — E-2 sobre o
# pai do candidato (`DB-37`/`DB-40`) e prefixo `- ` do contador de memória (`DB-41`).
# --------------------------------------------------------------------------- #


def test_tf_exit_3_pai_de_candidato_sem_linha_de_status(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")

    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    linhas = diario.read_text(encoding="utf-8").splitlines()
    alvo = "- **Status:** `ready` · 2026-01-01"
    saida_linhas = []
    aguardando_status_tk90 = False
    for linha in linhas:
        if linha.startswith("## TK-90 —"):
            saida_linhas.append(linha)
            aguardando_status_tk90 = True
            continue
        if aguardando_status_tk90 and linha.strip() == alvo:
            aguardando_status_tk90 = False
            continue  # remove a linha de Status do pai TK-90
        saida_linhas.append(linha)
    diario.write_text("\n".join(saida_linhas) + "\n", encoding="utf-8")

    plano = repo / "docs" / "plans" / "P-0090-fifo.md"
    texto_plano = plano.read_text(encoding="utf-8")
    alvo_plano = "**Status:** `ready` · **Prefixo das tarefas no diário:** `FFO-T<n>`"
    substituto_plano = "**Prefixo das tarefas no diário:** `FFO-T<n>`"
    texto_plano = texto_plano.replace(alvo_plano, substituto_plano)
    plano.write_text(texto_plano, encoding="utf-8")

    modelo = backlog.carregar(repo)
    selecao = backlog.selecionar_next(modelo)

    assert selecao.exit_code == 3
    assert selecao.mensagem.count("linha de status ausente para TK-90") == 1
    assert "linha de status ausente para P-0090" in selecao.mensagem
    assert selecao.mensagem.index("P-0090") < selecao.mensagem.index("TK-90")


def test_tf_contador_de_memoria_ignora_regua_e_marcadas(tmp_path):
    backlog = _load_backlog()
    repo = _copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")
    modelo = backlog.carregar(repo)

    selecao = backlog.selecionar_next(modelo)
    assert selecao.exit_code == 0

    inbox = tmp_path / "_INBOX.md"
    inbox.write_text(
        "# Inbox de memória (fixture)\n"
        "\n"
        "- 2026-01-01 — a — feedback — candidato 1 — **origem:** x\n"
        "- 2026-01-02 — b — feedback — candidato 2 — **origem:** y [promovido]\n"
        "\n"
        "---\n"
        "\n"
        "- 2026-01-03 — c — feedback — candidato 3 — **origem:** z\n",
        encoding="utf-8",
    )

    saida = backlog.renderizar_next(modelo, selecao, memoria_inbox=inbox)

    assert "fila de memória: 2 candidato(s)" in saida
    assert "fila de memória: 3 candidato(s)" not in saida
