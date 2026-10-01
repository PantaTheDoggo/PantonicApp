"""TK-88 (`docs/DIARIO_DE_OBRAS.md` `## TK-88`) — TF/TR de `.claude/tools/encerrar.py`, o
instrumento de fechamento de tarefa e de plano. Repositório sintético em `tmp_path` com diário,
plano legado, laudo, série de telemetria e painel do gerente; nenhum teste toca a árvore real.
Padrão de carga por caminho igual ao de `tests/test_backlog.py` (`.claude/` não é pacote)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_ENCERRAR_PATH = _ROOT / ".claude" / "tools" / "encerrar.py"


def _load_encerrar():
    spec = importlib.util.spec_from_file_location("encerrar", _ENCERRAR_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


encerrar = _load_encerrar()

TITULO_T1 = "Primeira tarefa do plano"
TITULO_T2 = "Segunda tarefa, cancelada"
TITULO_PLANO = "Plano alfa"

DIARIO = (
    "# Diário de Obras — Teste\n"
    "**Diretiva de priorização:** Priorize `P-0001`.\n"
    "\n"
    "<!-- fila:gerada -->\n"
    "**Fila corrente:** —\n"
    "<!-- /fila:gerada -->\n"
    "\n"
    "## Índice\n"
    "\n"
    "| ID | Título | Status | Âncora |\n"
    "|---|---|---|---|\n"
    "| P-0001 | Plano alfa | ready 0/1 | docs/plans/P-0001-alfa.md |\n"
)

PLANO = (
    f"# P-0001 — {TITULO_PLANO}\n"
    "\n"
    "**Status:** `ready` · **Prefixo das tarefas no diário:** `ALF-T<n>`\n"
    "\n"
    "## 5. Tarefas\n"
    "\n"
    f"### ALF-T1 — {TITULO_T1} [Sonnet · classe implementacao]\n"
    "- **Status:** `{status_t1}` · 2026-09-20\n"
    "- **Objetivo:** entregar a primeira coisa.\n"
    "- **Arquivos-alvo:** `a.py`.\n"
    "- **Verificação:** `pytest -q`.\n"
    "- **Pronto quando:** o teste passa.\n"
    "\n"
    f"### ALF-T2 — {TITULO_T2} [Sonnet · classe implementacao]\n"
    "- **Status:** `cancelled` · 2026-09-20 · absorvida\n"
    "- **Objetivo:** nada.\n"
    "- **Arquivos-alvo:** `b.py`.\n"
    "- **Verificação:** nenhuma.\n"
    "- **Pronto quando:** nunca.\n"
    "\n"
    "## 8. Achados da execução\n"
    "\n"
    "- **AE-1** (`ALF-T1`, laudo, 2026-09-21) — achado antigo. **Rota:** registrado, sem ação.\n"
)

LAUDO = (
    "# Laudo — P-0001 · ALF-T1\n"
    "\n"
    "**Percentual:** 91%\n"
    "**Veredito:** ressalva\n"
    "**Dimensão bloqueante:** nenhuma\n"
    "**Recomendação:** seguir com ressalva\n"
    "**Pendência:** o teste novo não cobre o ramo vazio\n"
    "\n"
    "## Lições aprendidas na tarefa\n"
    "\n"
    "Observação qualitativa do revisor.\n"
)


def _laudo_com_achado(linhas_tabela: list[str]) -> str:
    """`LAUDO` acrescida da seção `## Achado de processo` (tabela `| alvo | achado |`), antes de
    `## Lições aprendidas na tarefa` — a forma que `rdo.py laudo` grava."""
    tabela = "\n".join(["| alvo | achado |", "|---|---|"] + linhas_tabela)
    return LAUDO.replace(
        "## Lições aprendidas na tarefa",
        f"## Achado de processo\n\n{tabela}\n\n## Lições aprendidas na tarefa",
    )


TELEMETRIA = (
    "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"
    "2026-09-25\trepo\tALF-T1\tsonnet\t21\t77.5\t300.2\tusage\n"
    "2026-09-25\trepo\tALF-T1-revisao\topus\t9\t40.0\t120.0\tusage\n"
)

PAINEL = (
    f'Abrindo a janela do plano "{TITULO_PLANO}".\n'
    f'Tarefa "{TITULO_T1}". Passo: conferir os gates e preparar o despacho.\n'
    'Tarefa "Outra coisa de outro plano". Passo: conferir os gates e preparar o despacho.\n'
    f'Agente revisor devolveu a tarefa "{TITULO_T1}": ressalva 91%, bloqueante nenhuma.\n'
)


def _montar_repo(tmp_path: Path, status_t1: str = "review") -> Path:
    repo = tmp_path / "repo"
    (repo / "docs" / "plans").mkdir(parents=True)
    (repo / "docs" / "RDO" / "laudos").mkdir(parents=True)
    (repo / ".claude" / "estado").mkdir(parents=True)
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text(DIARIO, encoding="utf-8")
    (repo / "docs" / "plans" / "P-0001-alfa.md").write_text(PLANO.format(status_t1=status_t1), encoding="utf-8")
    (repo / "docs" / "plans" / "_INBOX.md").write_text("**Próximo id de plano: P-0002.**\n", encoding="utf-8")
    (repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md").write_text(LAUDO, encoding="utf-8")
    (repo / "docs" / "telemetria.tsv").write_text(TELEMETRIA, encoding="utf-8")
    (repo / ".claude" / "estado" / "progresso.txt").write_text(PAINEL, encoding="utf-8")
    return repo


def _argv_tarefa(repo: Path, **extra: str) -> list[str]:
    argv = [
        "tarefa", "--plano", str(repo / "docs" / "plans" / "P-0001-alfa.md"), "--tarefa", "ALF-T1",
        "--repo", str(repo), "--data", "2026-09-26", "--rdo-dir", str(repo / "docs" / "RDO"),
    ]
    for flag, valor in extra.items():
        argv += [flag, valor]
    return argv


def _rdos(repo: Path) -> list[Path]:
    return [p for p in (repo / "docs" / "RDO").glob("*.md") if p.name != "INDEX.md"]


# --- tarefa ----------------------------------------------------------------------------------


def test_tf_tarefa_fecha_num_ato_status_rdo_tres_secoes_e_achado(tmp_path):
    """TF: um comando materializa o `done` (card, índice, fila), escreve o RDO nas três seções —
    humano em linguagem corrente, máquina com o pacote transcrito do laudo, histórico com as
    linhas do painel só desta tarefa — e apensa o achado com rota ao plano."""
    repo = _montar_repo(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"

    exit_code = encerrar.main(_argv_tarefa(
        repo, **{"--resumo": "A primeira coisa está entregue.", "--pendencia": "decidir o nome"},
    ) + ["--achado", "a fixture tinha dois status", "abrir tíquete"])

    assert exit_code == 0
    rdos = _rdos(repo)
    assert len(rdos) == 1 and rdos[0].name.startswith("P-0001-ALF-T1-")
    conteudo = rdos[0].read_text(encoding="utf-8")
    assert conteudo.index("# Humano") < conteudo.index("# Máquina") < conteudo.index("# Histórico")
    humano = conteudo.split("# Humano", 1)[1].split("# Máquina", 1)[0]
    assert f'Tarefa "{TITULO_T1}" concluída em 2026-09-26.' in humano
    assert "A primeira coisa está entregue." in humano
    assert "aprovada com ressalva (91%); pendência do laudo: o teste novo não cobre o ramo vazio" in humano
    assert "Pendência para o dono: decidir o nome." in humano
    assert f'Plano "{TITULO_PLANO}": 1/1 tarefas concluídas' in humano
    maquina = conteudo.split("# Máquina", 1)[1].split("# Histórico", 1)[0]
    assert "**Veredito:** ressalva" in maquina and "**Percentual:** 91%" in maquina
    assert "**Recomendação:** seguir com ressalva" in maquina
    assert "laudo: o teste novo não cobre o ramo vazio" in maquina
    assert "executor: decidir o nome" in maquina
    assert "21 tool uses, 77.5 k tokens, 300.2 s" in maquina
    assert "Observação qualitativa do revisor." in maquina
    historico = conteudo.split("# Histórico", 1)[1]
    assert f'Tarefa "{TITULO_T1}". Passo' in historico
    assert f'Agente revisor devolveu a tarefa "{TITULO_T1}"' in historico
    assert "Outra coisa de outro plano" not in historico
    assert "{{" not in conteudo

    texto_plano = plano.read_text(encoding="utf-8")
    assert "- **Status:** `done` ·" in texto_plano
    assert "`done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0001-ALF-T1-" in texto_plano
    assert "- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — a fixture tinha dois status **Rota:** abrir tíquete" in texto_plano
    assert texto_plano.index("AE-1") < texto_plano.index("AE-2")
    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert "| P-0001 | Plano alfa | ready 1/1 | docs/plans/P-0001-alfa.md |" in diario
    # Consumo veio da série: nenhuma linha nova.
    assert (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8") == TELEMETRIA


def test_tf_achado_do_laudo_vira_ae_com_rota(tmp_path):
    """TF (AF-T4): cada linha da tabela `| alvo | achado |` de `## Achado de processo` do laudo
    vira um `AE-<n>` no plano, com a rota transcrita do trecho depois de `Rota:` — sem nenhum
    `--achado` no comando."""
    repo = _montar_repo(tmp_path)
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    texto_plano = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    assert (
        "- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (dossiê): "
        "o card não citava o arquivo de teste. **Rota:** card corretivo ALF-T1a"
    ) in texto_plano


def test_tr_achado_do_laudo_repetido_nao_duplica(tmp_path):
    """TR (AF-T4): o plano já traz uma entrada com o mesmo texto do achado de processo do laudo —
    a regra concorrente ("grava toda linha do laudo") duplicaria; o fechamento pula o par."""
    repo = _montar_repo(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    entrada_existente = (
        "- **AE-2** (`ALF-T1`, laudo, 2026-09-21) — achado de processo (dossiê): "
        "o card não citava o arquivo de teste. **Rota:** registrado antes.\n"
    )
    plano.write_text(plano.read_text(encoding="utf-8") + entrada_existente, encoding="utf-8")
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    texto_plano = plano.read_text(encoding="utf-8")
    assert "AE-3" not in texto_plano
    assert texto_plano.count("achado de processo (dossiê): o card não citava o arquivo de teste.") == 1


def test_tf_achado_do_laudo_sem_rota_declarada(tmp_path):
    """TF (AF-T4): achado de processo do laudo sem `Rota:` grava `AE-<n>` com `**Rota:** não
    declarada no laudo`."""
    repo = _montar_repo(tmp_path)
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| doutrina | a skill não nomeia o gate. |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    texto_plano = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    assert (
        "- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (doutrina): "
        "a skill não nomeia o gate. **Rota:** não declarada no laudo"
    ) in texto_plano


def test_tf_tarefa_consumo_por_argumento_apensa_a_serie(tmp_path):
    """TF: com o trio do bloco `<usage>` por argumento, a linha entra em `docs/telemetria.tsv`
    (fonte `usage`) no mesmo ato e o RDO usa esse número, não o da série."""
    repo = _montar_repo(tmp_path)
    (repo / "docs" / "telemetria.tsv").write_text(TELEMETRIA.splitlines()[0] + "\n", encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(
        repo, **{"--tool-uses": "33", "--tokens-k": "120.4", "--duracao-s": "410.0", "--modelo-agente": "sonnet"},
    ))

    assert exit_code == 0
    tsv = (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8").splitlines()
    assert tsv[-1] == "2026-09-26\trepo\tALF-T1\tsonnet\t33\t120.4\t410.0\tusage"
    assert "33 tool uses, 120.4 k tokens, 410.0 s" in _rdos(repo)[0].read_text(encoding="utf-8")


def test_tf_tarefa_nao_medido_fecha_com_linha_nao_medido(tmp_path):
    """TF (`TK-88b`): sem linha medida na série, `--nao-medido "<razão>"` fecha a tarefa em
    `done`, o RDO traz `**Consumo:** não medido — <razão>` e a série ganha uma linha `nao_medido`
    com as três células de consumo vazias."""
    repo = _montar_repo(tmp_path)
    (repo / "docs" / "telemetria.tsv").write_text(TELEMETRIA.splitlines()[0] + "\n", encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(
        repo, **{"--nao-medido": "executada fora do loop", "--modelo-agente": "sonnet"},
    ))

    assert exit_code == 0
    conteudo = _rdos(repo)[0].read_text(encoding="utf-8")
    assert "**Consumo:** não medido — executada fora do loop" in conteudo
    tsv = (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8").splitlines()
    assert tsv[-1] == "2026-09-26\trepo\tALF-T1\tsonnet\t\t\t\tnao_medido"


def test_tr_nao_medido_com_medida_na_serie_recusa(tmp_path, capsys):
    """TR (`TK-88b`): a série já tem linha medida (`fonte usage`) da tarefa — `--nao-medido`
    recusa (exit != 0) sem escrever nada, e a medida existente não se descarta."""
    repo = _montar_repo(tmp_path)

    exit_code = encerrar.main(_argv_tarefa(repo, **{"--nao-medido": "executada fora do loop"}))

    assert exit_code == 1
    assert "medida existente não se descarta" in capsys.readouterr().err
    assert _rdos(repo) == []
    assert (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8") == PLANO.format(status_t1="review")
    assert (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8") == TELEMETRIA


def test_tr_nao_medido_com_trio_recusa(tmp_path, capsys):
    """TR (`TK-88b`): `--nao-medido` junto do trio `--tool-uses/--tokens-k/--duracao-s` recusa
    (exit != 0) sem escrever nada."""
    repo = _montar_repo(tmp_path)

    exit_code = encerrar.main(_argv_tarefa(
        repo,
        **{
            "--nao-medido": "executada fora do loop",
            "--tool-uses": "5", "--tokens-k": "10", "--duracao-s": "60",
        },
    ))

    assert exit_code == 1
    assert "não vêm juntos" in capsys.readouterr().err
    assert _rdos(repo) == []
    assert (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8") == TELEMETRIA


def test_tr_tarefa_trio_repetido_recusa_sem_escrever(tmp_path, capsys):
    """TR (DFP-24/FPU-T7): o trio por argumento repete `modelo`/`tool_uses`/`tokens_k` da última
    linha de `ALF-T1` na série (`duracao_s` difere e não entra na comparação) — `checar_repetida`
    recusa antes da primeira escrita: exit 1, `linha repetida` em stderr, nenhum RDO criado,
    plano e série intactos."""
    repo = _montar_repo(tmp_path)

    exit_code = encerrar.main(_argv_tarefa(
        repo, **{"--tool-uses": "21", "--tokens-k": "77.5", "--duracao-s": "999.0", "--modelo-agente": "sonnet"},
    ))

    assert exit_code == 1
    assert "linha repetida" in capsys.readouterr().err
    assert _rdos(repo) == []
    assert (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8") == PLANO.format(status_t1="review")
    assert (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8") == TELEMETRIA


@pytest.mark.parametrize(
    "preparar, trecho",
    [
        (lambda repo: (repo / "docs" / "plans" / "P-0001-alfa.md").write_text(
            PLANO.format(status_t1="ready"), encoding="utf-8"), "exigido 'review'"),
        (lambda repo: (repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md").unlink(), "laudo: arquivo não encontrado"),
        (lambda repo: (repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md").write_text(
            LAUDO.replace("**Veredito:** ressalva", "**Veredito:** reprovado"), encoding="utf-8"),
         "não é desfecho de RDO"),
        (lambda repo: (repo / "docs" / "telemetria.tsv").write_text(
            TELEMETRIA.splitlines()[0] + "\n", encoding="utf-8"), "número não medido não fecha tarefa"),
    ],
    ids=["status-nao-review", "sem-laudo", "reprovado", "sem-consumo"],
)
def test_tr_tarefa_recusa_sem_escrever(tmp_path, preparar, trecho, capsys):
    """TR: cada checagem recusa antes de qualquer escrita — nenhum RDO, plano e diário intactos."""
    repo = _montar_repo(tmp_path)
    preparar(repo)
    plano_antes = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    diario_antes = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 1
    assert trecho in capsys.readouterr().err
    assert _rdos(repo) == []
    assert (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8") == plano_antes
    assert (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8") == diario_antes


def test_tr_checar_close_recusa_antes_do_done(tmp_path, capsys):
    """TR (`TK-88d`): `rdo.checar_close` é quem recusa, e a recusa sai antes do `done` — a
    tarefa fica em `review`, sem RDO novo. Recusa escolhida: o destino que `checar_close`
    computaria para `ALF-T1` já existe em `docs/RDO/` — hoje só o `rdo.py close` faz essa
    checagem; `encerrar.py tarefa` deixa de ter cópia própria dela."""
    repo = _montar_repo(tmp_path)
    colisao = repo / "docs" / "RDO" / "P-0001-ALF-T1-primeira-tarefa-do-plano.md"
    colisao.write_text("# RDO de outra tentativa\n", encoding="utf-8")
    plano_antes = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 1
    assert "já existe — tarefa já fechada" in capsys.readouterr().err
    assert (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8") == plano_antes
    assert [p.name for p in _rdos(repo)] == [colisao.name]


def test_tf_ler_laudo_transcreve_o_pacote_e_as_licoes(tmp_path):
    laudo = tmp_path / "laudo.md"
    laudo.write_text(LAUDO, encoding="utf-8")
    pacote = encerrar.ler_laudo(laudo)
    assert pacote == {
        "percentual": "91", "veredito": "ressalva", "bloqueante": "nenhuma",
        "recomendacao": "seguir com ressalva", "pendencia": "o teste novo não cobre o ramo vazio",
        "licoes": "Observação qualitativa do revisor.",
    }
    laudo.write_text(LAUDO.replace("**Recomendação:** seguir com ressalva\n", ""), encoding="utf-8")
    with pytest.raises(encerrar.EncerramentoError, match="recomendacao"):
        encerrar.ler_laudo(laudo)


# --- plano -----------------------------------------------------------------------------------


def _argv_plano(repo: Path, **extra: str) -> list[str]:
    argv = [
        "plano", "--plano", str(repo / "docs" / "plans" / "P-0001-alfa.md"), "--repo", str(repo),
        "--data", "2026-09-26", "--rdo-dir", str(repo / "docs" / "RDO"),
        "--veredito", "Pode concluir o plano",
    ]
    for flag, valor in extra.items():
        argv += [flag, valor]
    return argv


def _fechar_tarefa_e_preparar_plano(repo: Path) -> None:
    assert encerrar.main(_argv_tarefa(repo)) == 0
    (repo / "docs" / "OPERACOES_AS_IS_P-0001.md").write_text("# Operações as-is\n", encoding="utf-8")


def test_tf_consumo_por_papel_separa_planejador_modelador_scout(tmp_path):
    """TF (`DAF-15`/`DAF-25`): a série do plano ganha rodadas de `planejador` e `scout` — papéis
    que a regra de hoje somaria em `outros`, por não terminarem em `-revisao` nem conterem
    `-consultor` — e a tabela de consumo da entrega os separa em grupos próprios."""
    repo = _montar_repo(tmp_path)
    (repo / "docs" / "telemetria.tsv").write_text(
        TELEMETRIA
        + "2026-09-24\trepo\tP-0001-planejador\tsonnet\t3\t12.0\t60.0\tusage\n"
        + "2026-09-24\trepo\tP-0001-scout\thaiku\t2\t4.0\t20.0\tusage\n",
        encoding="utf-8",
    )
    _fechar_tarefa_e_preparar_plano(repo)

    exit_code = encerrar.main(_argv_plano(repo))

    assert exit_code == 0
    entrega = (repo / "docs" / "plans" / "_ENTREGA-P-0001.md").read_text(encoding="utf-8")
    maquina = entrega.split("# Máquina", 1)[1].split("# Histórico", 1)[0]
    assert "| planejador | 1 | 3 | 12.0 |" in maquina
    assert "| scout | 1 | 2 | 4.0 |" in maquina


def test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario(tmp_path):
    """TF: o plano sem tarefa aberta fecha num comando — `done` no plano e no índice, relatório
    de entrega nas três seções (tabela das tarefas com o veredito lido do RDO, achados verbatim,
    consumo agregado por papel, painel filtrado pelos títulos do plano) e uma linha no cabeçalho do
    diário com o veredito do dono verbatim."""
    repo = _montar_repo(tmp_path)
    _fechar_tarefa_e_preparar_plano(repo)

    exit_code = encerrar.main(_argv_plano(repo, **{"--resumo": "O plano entregou a primeira coisa."}))

    assert exit_code == 0
    entrega = repo / "docs" / "plans" / "_ENTREGA-P-0001.md"
    conteudo = entrega.read_text(encoding="utf-8")
    assert conteudo.startswith(f"# Entrega — P-0001 · {TITULO_PLANO}")
    assert conteudo.index("# Humano") < conteudo.index("# Máquina") < conteudo.index("# Histórico")
    humano = conteudo.split("# Humano", 1)[1].split("# Máquina", 1)[0]
    assert f'Plano "{TITULO_PLANO}" fechado em 2026-09-26, pelo aceite do dono: "Pode concluir o plano".' in humano
    assert "O plano entregou a primeira coisa." in humano
    assert "Tarefas: 1 concluídas de 2, 1 cancelada; aprovadas sem ressalva: 0; com ressalva: 1." in humano
    assert "Achados da execução: 1, todos com rota." in humano
    assert "Documento de validação: `docs/OPERACOES_AS_IS_P-0001.md`." in humano
    assert "sem modelo (plano anterior à doutrina)" in humano
    assert "117.5 mil tokens em 2 linha(s)" in humano
    maquina = conteudo.split("# Máquina", 1)[1].split("# Histórico", 1)[0]
    assert f"| `ALF-T1` | {TITULO_T1} | done | ressalva | 91% | aprovado com ressalva | `docs/RDO/P-0001-ALF-T1-" in maquina
    assert f"| `ALF-T2` | {TITULO_T2} | cancelled | — | — | — | — |" in maquina
    assert "- **AE-1** (`ALF-T1`, laudo, 2026-09-21) — achado antigo. **Rota:** registrado, sem ação." in maquina
    assert "| executor | 1 | 21 | 77.5 |" in maquina and "| revisor | 1 | 9 | 40.0 |" in maquina
    historico = conteudo.split("# Histórico", 1)[1]
    assert f'Abrindo a janela do plano "{TITULO_PLANO}".' in historico
    assert "Outra coisa de outro plano" not in historico

    assert "**Status:** `done` ·" in (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8").splitlines()
    assert "| P-0001 | Plano alfa | done 1/1 | docs/plans/P-0001-alfa.md |" in diario
    assert diario[1].startswith("**Diretiva de priorização:**")
    assert diario[3] == (
        "**`P-0001` — FECHADO `done` 1/1 em 2026-09-26, pelo aceite do dono** (*\"Pode concluir o plano\"*). "
        "Entrega: `docs/plans/_ENTREGA-P-0001.md` · validação: `docs/OPERACOES_AS_IS_P-0001.md`."
    )


def test_tf_fechado_conta_como_o_indice(tmp_path, capsys):
    """TF (`TK-88d`): a linha `FECHADO` conta as tarefas como o índice conta (`_done_total`,
    que tira as `cancelled` do total) — fixture com uma `done` (`ALF-T1`) e uma `cancelled`
    (`ALF-T2`) fecha com `1/1`, não `1/2`, e o stdout do fechamento diz `comando 'plano' concluído`."""
    repo = _montar_repo(tmp_path)
    _fechar_tarefa_e_preparar_plano(repo)

    exit_code = encerrar.main(_argv_plano(repo))

    assert exit_code == 0
    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8").splitlines()
    assert any("FECHADO `done` 1/1 em 2026-09-26" in l for l in diario)
    assert "encerrar: OK - comando 'plano' concluído;" in capsys.readouterr().out


@pytest.mark.parametrize(
    "preparar, trecho",
    [
        (lambda repo: None, "não terminal(is): ALF-T1"),
        (lambda repo: (_fechar_tarefa_e_preparar_plano(repo), (repo / "docs" / "OPERACOES_AS_IS_P-0001.md").unlink()),
         "documento de validação não encontrado"),
        (lambda repo: (_fechar_tarefa_e_preparar_plano(repo), (repo / "docs" / "plans" / "P-0001-alfa.md").write_text(
            (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8").replace(" **Rota:** registrado, sem ação.", ""),
            encoding="utf-8")), "sem `**Rota:**`: AE-1"),
        (lambda repo: (_fechar_tarefa_e_preparar_plano(repo), [p.unlink() for p in _rdos(repo)]), "done sem RDO: ALF-T1"),
    ],
    ids=["tarefa-aberta", "sem-operacoes", "achado-sem-rota", "done-sem-rdo"],
)
def test_tr_plano_recusa_sem_escrever(tmp_path, preparar, trecho, capsys):
    """TR: o plano não fecha com tarefa aberta, sem documento de validação, com achado sem rota
    ou com tarefa `done` sem RDO — e nada é escrito."""
    repo = _montar_repo(tmp_path)
    preparar(repo)
    plano_antes = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    diario_antes = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_plano(repo))

    assert exit_code == 1
    assert trecho in capsys.readouterr().err
    assert not (repo / "docs" / "plans" / "_ENTREGA-P-0001.md").exists()
    assert (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8") == plano_antes
    assert (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8") == diario_antes


def test_tf_achados_do_plano_e_linhas_do_painel(tmp_path):
    repo = _montar_repo(tmp_path)
    achados = encerrar.achados_do_plano(repo / "docs" / "plans" / "P-0001-alfa.md")
    assert [a for a, _ in achados] == ["AE-1"]
    assert encerrar.ROTA_RE.search(achados[0][1])
    linhas = encerrar.linhas_do_painel(repo / ".claude" / "estado" / "progresso.txt", [TITULO_T1])
    assert len(linhas) == 2 and all(TITULO_T1 in l for l in linhas)
    assert encerrar.linhas_do_painel(repo / "nao-existe.txt", [TITULO_T1]) == []


# --- handover --------------------------------------------------------------------------------


def _argv_handover(repo: Path, **extra: str) -> list[str]:
    argv = [
        "handover", "--plano", str(repo / "docs" / "plans" / "P-0001-alfa.md"), "--tarefa", "ALF-T1",
        "--repo", str(repo), "--data", "2026-09-26",
        "--entregue", "`a.py:12` expõe `fechar()`", "--contrato", "`fechar()` devolve exit 0 ou levanta",
    ]
    for flag, valor in extra.items():
        argv += [flag, valor]
    return argv


def test_tf_handover_registra_no_card_substitui_e_chega_ao_rdo(tmp_path, capsys):
    """TF: o handover é um campo de máquina no próprio card — rótulos fixos, destinatário entre
    crases —, substituído (não acumulado) na segunda escrita; o `rdo.py close` o transcreve no RDO
    e a seção humana do fechamento avisa que ele existe."""
    repo = _montar_repo(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"

    assert encerrar.main(_argv_handover(repo, **{"--para": "ALF-T2", "--nao-refazer": "a fixture já está montada"})) == 0
    texto = plano.read_text(encoding="utf-8")
    esperado = (
        "- **Handover:** 2026-09-26 · para `ALF-T2`\n"
        "  - **Entregue:** `a.py:12` expõe `fechar()`\n"
        "  - **Contrato:** `fechar()` devolve exit 0 ou levanta\n"
        "  - **Não refazer:** a fixture já está montada\n"
        "  - **Pendente:** nenhum\n"
    )
    assert esperado in texto
    assert texto.index("- **Pronto quando:** o teste passa.") < texto.index("- **Handover:**") < texto.index("### ALF-T2")
    assert esperado.rstrip("\n") in capsys.readouterr().out

    assert encerrar.main(_argv_handover(repo, **{"--pendente": "o ramo vazio"})) == 0
    texto2 = plano.read_text(encoding="utf-8")
    assert texto2.count("- **Handover:**") == 1
    assert "para quem vier depois" in texto2 and "  - **Pendente:** o ramo vazio" in texto2
    assert "a fixture já está montada" not in texto2

    assert encerrar.main(_argv_tarefa(repo)) == 0
    rdo = _rdos(repo)[0].read_text(encoding="utf-8")
    assert "- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** `a.py:12` expõe `fechar()`" in rdo
    assert "Handover para quem vem depois: registrado no card" in rdo.split("# Máquina", 1)[0]


def test_tr_handover_recusa_tarefa_sem_entrega(tmp_path, capsys):
    """TR: tarefa `ready` não tem o que entregar — recusa sem escrever; campo vazio também."""
    repo = _montar_repo(tmp_path, status_t1="ready")
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    antes = plano.read_text(encoding="utf-8")

    assert encerrar.main(_argv_handover(repo)) == 1
    assert "handover exige entrega na árvore" in capsys.readouterr().err
    assert plano.read_text(encoding="utf-8") == antes

    with pytest.raises(encerrar.EncerramentoError, match="contrato"):
        encerrar.montar_handover("2026-09-26", "x", "  ")


# --- marco -------------------------------------------------------------------------------------


DIARIO_MARCO = (
    "# Diário de Obras — Teste\n"
    "**Diretiva de priorização:** Priorize `P-0001`.\n"
    "\n"
    "<!-- fila:gerada -->\n"
    "**Fila corrente:** —\n"
    "<!-- /fila:gerada -->\n"
    "\n"
    "## Índice\n"
    "\n"
    "| ID | Título | Status | Âncora |\n"
    "|---|---|---|---|\n"
    "| P-0001 | Plano marco | blocked 0/1 | docs/plans/P-0001-marco.md |\n"
)

PLANO_MARCO = (
    "# P-0001 — Plano marco\n"
    "\n"
    "**Status:** `blocked` · **Prefixo das tarefas no diário:** `MRC-T<n>`\n"
    "\n"
    "**Marcos de validação pelo dono:**\n"
    "\n"
    "| marco | o que o dono lê | veredito |\n"
    "|---|---|---|\n"
    "| **Marco 1** | a seção 1 | pendente |\n"
    "\n"
    "## 0. O problema, verbatim\n"
    "\n"
    "Texto do problema, verbatim.\n"
    "\n"
    "## 1A. Modelo conceitual — versão pendente de validação\n"
    "\n"
    "Rascunho da versão pendente.\n"
    "\n"
    "## 5. Tarefas\n"
    "\n"
    "### MRC-T1 — Tarefa única [Sonnet · classe implementacao]\n"
    "- **Status:** `review` · 2026-09-20\n"
    "- **Objetivo:** entregar algo.\n"
    "- **Arquivos-alvo:** `a.py`.\n"
    "- **Verificação:** `pytest -q`.\n"
    "- **Pronto quando:** o teste passa.\n"
)


def _montar_repo_marco(tmp_path: Path, plano_texto: str = PLANO_MARCO) -> Path:
    repo = tmp_path / "repo"
    (repo / "docs" / "plans").mkdir(parents=True)
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text(DIARIO_MARCO, encoding="utf-8")
    (repo / "docs" / "plans" / "P-0001-marco.md").write_text(plano_texto, encoding="utf-8")
    return repo


def _argv_marco(repo: Path, **extra: str) -> list[str]:
    argv = [
        "marco", "--plano", str(repo / "docs" / "plans" / "P-0001-marco.md"),
        "--repo", str(repo), "--data", "2026-09-26",
    ]
    for flag, valor in extra.items():
        argv += [flag, valor]
    return argv


def test_tf_marco_go_grava_celula_zero_e_tira_de_blocked(tmp_path):
    """TF (AF-T12): `marco --marco 1 --resultado go` grava a última célula da linha do marco,
    acrescenta o veredito ao fim da `## 0.` e, achando o plano em `blocked`, tira-o para `ready` —
    tudo num comando só, sem interpretar a frase do dono."""
    repo = _montar_repo_marco(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"

    exit_code = encerrar.main(_argv_marco(
        repo, **{"--marco": "1", "--resultado": "go", "--veredito": "Pode seguir"},
    ))

    assert exit_code == 0
    texto = plano.read_text(encoding="utf-8")
    assert '| **Marco 1** | a seção 1 | go · 2026-09-26 — "Pode seguir" |' in texto
    assert "**Marco 1, 2026-09-26 — veredito do dono (go):**" in texto
    assert "> Pode seguir" in texto
    assert texto.index("## 0.") < texto.index("> Pode seguir") < texto.index("## 1A.")
    assert "**Status:** `ready`" in texto
    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
    assert "| P-0001 | Plano marco | ready 0/1 | docs/plans/P-0001-marco.md |" in diario


def test_tr_marco_no_go_nao_muda_status(tmp_path):
    """TR (AF-T12): a mesma escrita das duas células com `--resultado no-go` não tira o plano de
    `blocked` — a regra concorrente ('todo marco 1 libera o plano') faria isso."""
    repo = _montar_repo_marco(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"

    exit_code = encerrar.main(_argv_marco(
        repo, **{"--marco": "1", "--resultado": "no-go", "--veredito": "Ainda não"},
    ))

    assert exit_code == 0
    texto = plano.read_text(encoding="utf-8")
    assert '| **Marco 1** | a seção 1 | no-go · 2026-09-26 — "Ainda não" |' in texto
    assert "**Marco 1, 2026-09-26 — veredito do dono (no-go):**" in texto
    assert "> Ainda não" in texto
    assert "**Status:** `blocked`" in texto


def test_tf_marco_recusa_versao_imprime_dossie_de_emenda(tmp_path, capsys):
    """TF (AF-T12): com `--recusa-versao`, o comando imprime no stdout o dossiê `Ato: emenda`
    para o modelador, com o motivo do marco e a frase do dono, verbatim."""
    repo = _montar_repo_marco(tmp_path)

    exit_code = encerrar.main(_argv_marco(
        repo, **{"--marco": "1", "--resultado": "no-go", "--veredito": "Não aceito", "--recusa-versao": "2"},
    ))

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert "Ato: emenda" in saida
    assert 'Motivo: Marco 1, veredito do dono: "Não aceito"' in saida
    assert "Fato novo: o dono recusou a versão 2 do modelo no Marco 1." in saida


def test_tr_marco_recusa_sem_linha_do_marco_sem_escrever(tmp_path, capsys):
    """TR (AF-T12): `--marco 2` num plano que só tem a linha do Marco 1 recusa antes de escrever
    qualquer coisa — o plano sai byte a byte igual."""
    repo = _montar_repo_marco(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"
    antes = plano.read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_marco(
        repo, **{"--marco": "2", "--resultado": "go", "--veredito": "Pode seguir"},
    ))

    assert exit_code == 1
    assert "linha do Marco 2 ausente" in capsys.readouterr().err
    assert plano.read_text(encoding="utf-8") == antes


def test_tr_marco_regravar_celula_com_pipe_escapado_nao_deixa_resto(tmp_path):
    """TR (AF-T12, reparo do consultor `DAF-43`): a célula é reescrita pelas colunas da tabela
    GFM, onde `\\|` não separa coluna. Gravar de novo um marco cuja frase anterior tinha `|`
    (que o próprio verbo emite como `\\|`) troca a célula inteira — o split ingênuo no `|`
    deixava pedaço do veredito velho na linha."""
    repo = _montar_repo_marco(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"

    assert encerrar.main(_argv_marco(
        repo, **{"--marco": "1", "--resultado": "no-go", "--veredito": "falta a | b"},
    )) == 0
    assert '| **Marco 1** | a seção 1 | no-go · 2026-09-26 — "falta a \\| b" |' in plano.read_text(encoding="utf-8")

    assert encerrar.main(_argv_marco(
        repo, **{"--marco": "1", "--resultado": "no-go", "--veredito": "Ainda não"},
    )) == 0
    linha = next(l for l in plano.read_text(encoding="utf-8").splitlines() if l.startswith("| **Marco 1** |"))
    assert linha == '| **Marco 1** | a seção 1 | no-go · 2026-09-26 — "Ainda não" |'


def test_tr_marco_go_com_transicao_recusada_nao_escreve(tmp_path, capsys):
    """TR (AF-T12, reparo do consultor `DAF-43`): Marco 1 `go` cuja transição `blocked → ready`
    o backlog recusa (aqui, linha de índice ausente) sai exit 1 antes de escrever — a checagem
    da transição (`backlog.checar_transicao`, `TK-88d`) corre com as demais, antes da escrita (1)."""
    repo = _montar_repo_marco(tmp_path)
    diario = repo / "docs" / "DIARIO_DE_OBRAS.md"
    diario.write_text(
        DIARIO_MARCO.replace("| P-0001 | Plano marco | blocked 0/1 | docs/plans/P-0001-marco.md |\n", ""),
        encoding="utf-8",
    )
    plano = repo / "docs" / "plans" / "P-0001-marco.md"
    antes_plano = plano.read_bytes()
    antes_diario = diario.read_bytes()

    exit_code = encerrar.main(_argv_marco(
        repo, **{"--marco": "1", "--resultado": "go", "--veredito": "Pode seguir"},
    ))

    assert exit_code == 1
    assert "marco: status:" in capsys.readouterr().err
    assert plano.read_bytes() == antes_plano
    assert diario.read_bytes() == antes_diario


# --- operacoes ---------------------------------------------------------------------------------


def _argv_operacoes(repo: Path, **extra: str) -> list[str]:
    argv = [
        "operacoes", "--plano", str(repo / "docs" / "plans" / "P-0001-alfa.md"), "--repo", str(repo),
    ]
    for flag, valor in extra.items():
        argv += [flag, valor]
    return argv


def test_tf_esqueleto_de_operacoes_uma_secao_por_card(tmp_path):
    """TF (AF-T13): `operacoes --plano <legado>` grava o esqueleto com exatamente uma seção
    `## `<ID>`` — a de ALF-T1; ALF-T2 (`cancelled`) não ganha seção, mas a tabela do arco cita
    as duas."""
    repo = _montar_repo(tmp_path)

    exit_code = encerrar.main(_argv_operacoes(repo))

    assert exit_code == 0
    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
    texto = destino.read_text(encoding="utf-8")
    secoes = [l for l in texto.splitlines() if l.startswith("## `")]
    assert secoes == [f"## `ALF-T1` — {TITULO_T1}"]
    assert f"| `ALF-T1` | {TITULO_T1} | review |" in texto
    assert f"| `ALF-T2` | {TITULO_T2} | cancelled |" in texto


def test_tr_esqueleto_de_operacoes_nao_sobrescreve(tmp_path, capsys):
    """TR (AF-T13): destino já existente é recusa — exit 1, nada escrito."""
    repo = _montar_repo(tmp_path)
    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
    destino.write_text("conteúdo prévio\n", encoding="utf-8")

    exit_code = encerrar.main(_argv_operacoes(repo))

    assert exit_code == 1
    assert "operacoes: já existe" in capsys.readouterr().err
    assert destino.read_text(encoding="utf-8") == "conteúdo prévio\n"


def test_tf_esqueleto_de_operacoes_checar_cobertura(tmp_path, capsys):
    """TF (AF-T13): `--checar` sobre o esqueleto recém-gerado sai 0 com as duas linhas `nenhum`;
    apagando o bloco `**Protege contra:**` da seção de ALF-T1, sai 1 e nomeia a tarefa."""
    repo = _montar_repo(tmp_path)
    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
    assert encerrar.main(_argv_operacoes(repo)) == 0
    capsys.readouterr()

    exit_code = encerrar.main(_argv_operacoes(repo) + ["--checar"])

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert "nao citados: nenhum" in saida
    assert "sem seção: nenhum" in saida
    assert "sem os quatro blocos: nenhum" in saida

    destino.write_text(
        destino.read_text(encoding="utf-8").replace("**Protege contra:**\n\n", ""),
        encoding="utf-8",
    )

    exit_code = encerrar.main(_argv_operacoes(repo) + ["--checar"])

    assert exit_code == 1
    saida = capsys.readouterr().out
    assert "nao citados: nenhum" in saida
    assert "sem os quatro blocos: ALF-T1" in saida


def test_tr_esqueleto_de_operacoes_checar_secao_apagada(tmp_path, capsys):
    """TR (`DAF-44`, `AE-19`): com a seção inteira de ALF-T1 apagada, `--checar` sai 1 e nomeia a
    tarefa em `sem seção:` — a tabela do arco segue citando o ID (`nao citados: nenhum`) e não há
    seção para `sem os quatro blocos` iterar, então só a linha nova discrimina."""
    repo = _montar_repo(tmp_path)
    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
    assert encerrar.main(_argv_operacoes(repo)) == 0
    texto = destino.read_text(encoding="utf-8")
    inicio = texto.index("## `ALF-T1`")
    fim = texto.index("\n## ", inicio) + 1
    destino.write_text(texto[:inicio] + texto[fim:], encoding="utf-8")
    capsys.readouterr()

    exit_code = encerrar.main(_argv_operacoes(repo) + ["--checar"])

    assert exit_code == 1
    saida = capsys.readouterr().out
    assert "nao citados: nenhum" in saida
    assert "sem seção: ALF-T1" in saida
    assert "sem os quatro blocos: nenhum" in saida


def test_tr_esqueleto_de_operacoes_plano_relativo(tmp_path, monkeypatch, capsys):
    """TR (`AE-29` do `P-0753`): `--plano` relativo, como a skill `entrega-de-encerramento` o
    escreve, grava o esqueleto e o `--checar` o confere — antes saía exit 1 com `ValueError` de
    `relative_to` no parser do plano."""
    repo = _montar_repo(tmp_path)
    monkeypatch.chdir(repo)
    argv = ["operacoes", "--plano", "docs/plans/P-0001-alfa.md", "--repo", str(repo)]

    assert encerrar.main(argv) == 0
    assert (repo / "docs" / "OPERACOES_AS_IS_P-0001.md").is_file()
    capsys.readouterr()

    exit_code = encerrar.main(argv + ["--checar"])

    saida = capsys.readouterr().out
    assert exit_code == 0
    assert "nao citados: nenhum" in saida
    assert "sem seção: nenhum" in saida


def test_tf_conclusao_da_tarefa_sem_erro_de_concordancia(tmp_path, capsys):
    """TF: a frase final do fechamento serve a todos os comandos — para `tarefa` ela diz
    `comando 'tarefa' concluído`, nunca `tarefa fechado` (a regra antiga imprimia
    `encerrar: OK - tarefa fechado;`)."""
    repo = _montar_repo(tmp_path)

    exit_code = encerrar.main(_argv_tarefa(
        repo, **{"--resumo": "A primeira coisa está entregue.", "--pendencia": "nomear a função"},
    ))

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert "encerrar: OK - comando 'tarefa' concluído;" in saida
    assert "tarefa fechado" not in saida


# --- marco --aceita-versao (RAF-T23) ------------------------------------------------------------


PLANO_MARCO_PROMOCAO = """# P-0001 — Plano marco

**Prefixo das tarefas no diário:** `MRC-T<n>`

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a seção 1 | go |
| **Marco 2** | a etapa A | pendente |

## 0. O problema, verbatim

Texto do problema, verbatim.

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
| produto | o produto da operação | status | um registro validado | OP-1 | lastro da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação da fixture.
  - `precisa de: insumo` · `altera: produto.status` · `tarefas: MRC-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo.status | lido | lido |
| produto.status | rascunho | validado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-10 | vigente | modelador |
| 2 | 2026-09-21 | pendente | modelador, emenda |

## 1A. Modelo conceitual — versão pendente de validação

**Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
| esboço | o esboço da operação nova | estado | um esboço revisado | OP-1 | lastro da fixture |
| produto | o produto da operação | status | um registro validado | OP-2 | lastro da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Operação nova, inserida antes.
  - `precisa de: insumo` · `altera: esboço.estado` · `tarefas: @TAREFAS_OP1@`
- **OP-2** — Primeira operação da fixture.
  - `precisa de: esboço` · `altera: produto.status` · `tarefas: MRC-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo.status | lido | lido |
| esboço.estado | vazio | revisado |
| produto.status | rascunho | validado |

## 5. Tarefas

### MRC-T1 — Tarefa da operação antiga [Sonnet · classe implementacao]
- **Objetivo:** entregar algo.
- **Operação do modelo:** `OP-1`
  - OP-1: Primeira operação da fixture.
  - precisa de: insumo — um registro por rodada
- **Arquivos-alvo:** `a.py`.
- **Verificação:** `pytest -q`.
- **Pronto quando:** o teste passa.

### MRC-T2 — Tarefa da operação nova [Sonnet · classe implementacao]
- **Objetivo:** entregar outra coisa.
- **Operação do modelo:** `OP-1`
  - OP-1: Operação nova, inserida antes.
  - precisa de: insumo — um registro por rodada
- **Arquivos-alvo:** `b.py`.
- **Verificação:** `pytest -q`.
- **Pronto quando:** o teste passa.
"""


def _montar_repo_promocao(tmp_path: Path, tarefas_op1: str = "MRC-T2") -> Path:
    return _montar_repo_marco(tmp_path, PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", tarefas_op1))


def _card(texto: str, tarefa: str) -> str:
    prefixo = f"### {tarefa} — "
    idx = texto.index(prefixo)
    fim = texto.find("\n### ", idx)
    return texto[idx:] if fim == -1 else texto[idx:fim]


def test_tf_marco_promove_versao_aceita_e_reescreve_os_cards(tmp_path, capsys):
    """TF (RAF-T23, `DRF-38`): `--aceita-versao` promove a versão pendente a vigente — a linha
    vigente do registro cai a obsoleta com o motivo na célula `por`, a linha da versão aceita
    sobe a vigente, a `## 1A` sai do plano e o campo `Operação do modelo` de cada card citado
    pela pendente é reescrito com as operações e contratos dela."""
    repo = _montar_repo_promocao(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2",
            "--aceita-versao": "2", "--consultor": "valido a versão 2",
        },
    ))

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert "marco: versão 2 promovida — 2 card(s) com a operação reescrita" in saida
    assert "Ato: emenda" not in saida

    texto = plano.read_text(encoding="utf-8")
    assert "## 1A." not in texto
    assert "versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: vigente" in texto
    assert "| 1 | 2026-09-10 | obsoleta | modelador; Caiu pelo aceite da versão 2 em 2026-09-26 |" in texto
    assert "| 2 | 2026-09-21 | vigente | modelador, emenda |" in texto

    card_t1 = _card(texto, "MRC-T1")
    assert "`OP-2`" in card_t1.splitlines()[next(
        i for i, l in enumerate(card_t1.splitlines()) if l.startswith("- **Operação do modelo:**")
    )]
    idx_campo_t1 = card_t1.index("- **Operação do modelo:**")
    trecho_t1 = card_t1[idx_campo_t1:]
    assert trecho_t1.splitlines()[0:3] == [
        "- **Operação do modelo:** `OP-2`",
        "  - OP-2: Primeira operação da fixture.",
        "  - precisa de: esboço — um esboço revisado",
    ]

    card_t2 = _card(texto, "MRC-T2")
    idx_campo_t2 = card_t2.index("- **Operação do modelo:**")
    trecho_t2 = card_t2[idx_campo_t2:]
    assert trecho_t2.splitlines()[0:3] == [
        "- **Operação do modelo:** `OP-1`",
        "  - OP-1: Operação nova, inserida antes.",
        "  - precisa de: insumo — um registro por rodada",
    ]


def test_tf_marco_promove_versao_conflito_imprime_dossie(tmp_path, capsys):
    """TF (RAF-T23): `--aceita-versao` que não bate com a versão da `## 1A` recusa antes de
    escrever e imprime, no stdout, o dossiê `Ato: emenda` para o modelador."""
    repo = _montar_repo_promocao(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"
    antes = plano.read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 3",
            "--aceita-versao": "3", "--consultor": "valido a versão 3",
        },
    ))

    assert exit_code == 1
    err = capsys.readouterr()
    assert "marco: conflito na promoção da versão 3 — a ## 1A é a versão 2" in err.err
    assert "Ato: emenda" in err.out
    assert plano.read_text(encoding="utf-8") == antes


def test_tr_marco_promove_versao_recusa_pendente_com_violacao(tmp_path, capsys):
    """TR (RAF-T23): a versão pendente com violação (aqui, `OP-1` sem tarefa) recusa a promoção
    antes de escrever — a mesma checagem de `_modelo.validar(pendente=True)`, prefixada `1A: `."""
    repo = _montar_repo_promocao(tmp_path, tarefas_op1="")
    plano = repo / "docs" / "plans" / "P-0001-marco.md"
    antes = plano.read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2",
            "--aceita-versao": "2", "--consultor": "valido a versão 2",
        },
    ))

    assert exit_code == 1
    assert "marco: versão pendente com violação — 1A: V1 OP-1 — operação sem tarefa" in capsys.readouterr().err
    assert plano.read_text(encoding="utf-8") == antes


def test_tf_marco_validacao_do_consultor_na_celula(tmp_path):
    """TF (RAF-T23, `R-08`): a linha de validação do consultor grava ao lado do veredito do
    dono, na mesma célula do marco, com `|` escapado como o resto da célula."""
    repo = _montar_repo_promocao(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito",
            "--aceita-versao": "2", "--consultor": "valido a versão 2 | sem ressalva",
        },
    ))

    assert exit_code == 0
    texto = plano.read_text(encoding="utf-8")
    assert (
        '| **Marco 2** | a etapa A | go · 2026-09-26 — "Aceito" · '
        'consultor: "valido a versão 2 \\| sem ressalva" |'
    ) in texto


def test_tr_marco_validacao_do_consultor_obrigatoria_no_aceite(tmp_path, capsys):
    """TR (RAF-T23, `R-08`): `--aceita-versao` sem `--consultor` recusa sem escrever — a regra
    concorrente (consultor opcional) promoveria a versão sem validação registrada."""
    repo = _montar_repo_promocao(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"
    antes = plano.read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2",
            "--aceita-versao": "2",
        },
    ))

    assert exit_code == 1
    assert (
        "marco: --aceita-versao exige --consultor com a linha de validação do consultor"
        in capsys.readouterr().err
    )
    assert plano.read_text(encoding="utf-8") == antes


def test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente(tmp_path, capsys):
    """TF (RAF-T23a, `AE-176`): a `## 1A` cujo cabeçalho tem texto a mais não é a versão pendente
    que o `modelo.py` lê (igualdade exata com `_modelo._HEADING_PENDENTE`); a pré-checagem do
    marco usa a mesma regra e recusa antes de escrever, em vez de passar pelo prefixo e cair em
    `AttributeError` dentro de `_checar_promocao`."""
    texto = PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", "MRC-T2").replace(
        "## 1A. Modelo conceitual — versão pendente de validação",
        "## 1A. Modelo conceitual — versão pendente de validação (rascunho)",
    )
    repo = _montar_repo_marco(tmp_path, texto)
    plano = repo / "docs" / "plans" / "P-0001-marco.md"
    antes = plano.read_text(encoding="utf-8")

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2",
            "--aceita-versao": "2", "--consultor": "valido a versão 2",
        },
    ))

    assert exit_code == 1
    assert "marco: plano sem versão pendente (## 1A)" in capsys.readouterr().err
    assert plano.read_text(encoding="utf-8") == antes


def test_tf_marco_conflito_devolver_pede_a_1_e_a_1a(tmp_path, capsys):
    """TF (RAF-T23b, `AE-180`): no conflito da promoção o modelador acerta o que está (a
    `## 1`, a `## 1A` e o registro de versões) para o comando rodar de novo; o `Devolver` do
    dossiê não pede a seção depois do ato nem linha nova do registro, que o comando faz."""
    repo = _montar_repo_promocao(tmp_path)

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 3",
            "--aceita-versao": "3", "--consultor": "valido a versão 3",
        },
    ))

    assert exit_code == 1
    saida = capsys.readouterr().out
    assert (
        "Devolver: a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do "
        "marco rodar de novo." in saida
    )
    assert "linha nova do registro" not in saida


def test_tf_marco_recusa_devolver_sem_linha_nova_do_registro(tmp_path, capsys):
    """TF (RAF-T23b, `AE-180`): na recusa a `## 1A` e a linha dela saem e a vigente fica sem
    marca (`GOVERNANCA.md` §3.2); o `Devolver` do dossiê pede a `## 1` com o registro sem a linha
    da versão recusada, não uma linha nova."""
    repo = _montar_repo_marco(tmp_path)

    exit_code = encerrar.main(_argv_marco(
        repo, **{
            "--marco": "1", "--resultado": "no-go", "--veredito": "Não aceito",
            "--recusa-versao": "2",
        },
    ))

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert (
        "Devolver: a seção ## 1 depois do ato, com o registro de versões sem a linha da versão "
        "recusada, e o plano sem a ## 1A." in saida
    )
    assert "linha nova do registro" not in saida


# --- RAF-T30: origem do achado e aviso de falha de instrumento -------------------------------


def test_tf_origem_do_achado_gravada_na_linha(tmp_path):
    """TF (RAF-T30, `R-19`/`DRF-21`): cada achado do laudo grava a linha de origem
    `laudo:<TAREFA>#<n>`, numerada a partir de 1 na ordem da tabela."""
    repo = _montar_repo(tmp_path)
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
        "| doutrina | a skill não nomeia o gate. Rota: tíquete |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    texto_plano = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
    assert (
        "- **AE-3** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (doutrina): "
        "a skill não nomeia o gate. **Rota:** tíquete **Origem:** `laudo:ALF-T1#2`"
    ) in texto_plano


def test_tf_origem_do_achado_ja_registrada_pula(tmp_path):
    """TF (RAF-T30, `R-19`): a origem `laudo:ALF-T1#1` já está registrada no plano com outro
    texto; a regra concorrente (dedupe só por texto) gravaria de novo — o fechamento pula."""
    repo = _montar_repo(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    entrada_existente = (
        "- **AE-2** (`ALF-T1`, laudo, 2026-09-21) — achado de processo (dossiê): "
        "outro texto qualquer. **Rota:** outra rota. **Origem:** `laudo:ALF-T1#1`\n"
    )
    plano.write_text(plano.read_text(encoding="utf-8") + entrada_existente, encoding="utf-8")
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    texto_plano = plano.read_text(encoding="utf-8")
    assert "AE-3" not in texto_plano


def test_tr_origem_do_achado_de_outra_linha_nao_pula(tmp_path):
    """TR (RAF-T30): a `AE-2` existente cita `laudo:ALF-T1#11`; a regra concorrente (casar
    `laudo:ALF-T1#1` como substring sem as crases) pularia a linha 1 por engano — não pula."""
    repo = _montar_repo(tmp_path)
    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
    entrada_existente = (
        "- **AE-2** (`ALF-T1`, laudo, 2026-09-21) — achado de processo (dossiê): "
        "outro texto qualquer. **Rota:** outra rota. **Origem:** `laudo:ALF-T1#11`\n"
    )
    plano.write_text(plano.read_text(encoding="utf-8") + entrada_existente, encoding="utf-8")
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    texto_plano = plano.read_text(encoding="utf-8")
    assert (
        "- **AE-3** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (dossiê): "
        "o card não citava o arquivo de teste. **Rota:** card corretivo ALF-T1a **Origem:** "
        "`laudo:ALF-T1#1`"
    ) in texto_plano


def test_tf_falha_de_instrumento_avisa_b1(tmp_path, capsys):
    """TF (RAF-T30, `R-20`): achado de processo do alvo `instrumento` que relata queda ou erro
    ganha, no stdout, a linha `encerrar: B1` antes da linha final de conclusão."""
    repo = _montar_repo(tmp_path)
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| instrumento | o card_check caiu com Traceback no item 2. Rota: tíquete |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert (
        "encerrar: B1 — achado de instrumento com falha: o card_check caiu com Traceback no "
        "item 2." in saida
    )
    assert saida.index("encerrar: B1") < saida.index("encerrar: OK - comando 'tarefa' concluído")


def test_tr_falha_de_instrumento_sem_termo_ou_de_outro_alvo_cala(tmp_path, capsys):
    """TR (RAF-T30): achado de instrumento sem termo de falha, e achado com termo de falha de
    outro alvo — a regra concorrente (qualquer achado de instrumento, ou qualquer termo em
    qualquer alvo) avisaria; nenhum dos dois casa a regra e o `B1` não sai."""
    repo = _montar_repo(tmp_path)
    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
    laudo.write_text(_laudo_com_achado([
        "| instrumento | a saída do card_check é longa. |",
        "| dossiê | o teste deu error no ramo vazio. |",
    ]), encoding="utf-8")

    exit_code = encerrar.main(_argv_tarefa(repo))

    assert exit_code == 0
    saida = capsys.readouterr().out
    assert "encerrar: B1" not in saida
