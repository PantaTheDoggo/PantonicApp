"""EXA-T9a (`docs/plans/P-0734-execucao-autonoma.md` `### T9a`) — TF/TR de
`.claude/tools/review_evidence.py`: a metade `git` da evidência de revisão (diff, arquivos
tocados, confronto de escopo mecânico e trechos truncados). Padrão de carga do módulo idêntico a
`tests/test_rdo.py`/`tests/test_telemetria.py` (`.claude/` não é pacote importável).

Este arquivo introduz repositório de fixture `git` na suíte (sem precedente: os testes existentes
usam árvore estática ou TSV/RDO mínimo em `tmp_path`). Cada teste cria um repositório `git`
isolado em `tmp_path/repo` — `git init`, identidade local, commit de baseline com uma cópia do
`rdo.py` real em `<repo>/.claude/tools/rdo.py` (`review_evidence.montar_documento` usa o mesmo
`root` tanto para rodar `git` quanto para localizar o módulo irmão, espelhando o uso real onde a
raiz do repositório é as duas coisas ao mesmo tempo) — e então cria/edita arquivos para o cenário
sob teste. O `.md` do plano fica **fora** do repositório (`tmp_path/plano.md`, irmão de `repo/`)
para não poluir a lista de arquivos tocados com o próprio arquivo de plano."""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_REVIEW_EVIDENCE_PATH = _ROOT / ".claude" / "tools" / "review_evidence.py"
_RDO_REAL_PATH = _ROOT / ".claude" / "tools" / "rdo.py"

# Bateria fake (rápida, determinística) para os testes que não avaliam a bateria de guardas em
# si — a bateria real (`BATERIA_GUARDAS`) depende de infraestrutura do hub (`.claude/checks/*`,
# `pytest.ini`) ausente no repositório de fixture isolado.
_BATERIA_FAKE_VERDE = [("pytest", ["python", "-c", "import sys; sys.exit(0)"])]


def _load_review_evidence():
    spec = importlib.util.spec_from_file_location("review_evidence", _REVIEW_EVIDENCE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run_git(args: list[str], cwd: Path) -> str:
    resultado = subprocess.run(
        ["git", *args], cwd=str(cwd), capture_output=True, text=True
    )
    assert resultado.returncode == 0, f"git {args}: {resultado.stderr}"
    return resultado.stdout


def _init_repo_com_baseline(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    _run_git(["init"], root)
    _run_git(["config", "user.email", "teste@example.com"], root)
    _run_git(["config", "user.name", "Teste"], root)
    (root / "src").mkdir()
    (root / "src" / "b.py").write_text("def b():\n    return 1\n", encoding="utf-8")
    # Espelha o .gitignore real do PantonicApp (`__pycache__/`): sem isso, carregar rdo.py por
    # importlib (que escreve bytecode cache ao lado do .py) sujaria a lista de arquivos tocados
    # com um artefato de build que o repositório real já ignora.
    (root / ".gitignore").write_text("__pycache__/\n", encoding="utf-8")
    destino_rdo = root / ".claude" / "tools" / "rdo.py"
    destino_rdo.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(_RDO_REAL_PATH, destino_rdo)
    _run_git(["add", "-A"], root)
    _run_git(["commit", "-m", "baseline"], root)


def _escrever_plano(caminho: Path, arquivos_alvo_texto: str) -> None:
    texto = (
        "# Plano de teste\n\n"
        "### T1 — Tarefa sintética de teste [Sonnet · classe implementação padrão]\n"
        "- **Objetivo:** validar review_evidence.py.\n"
        f"- **Arquivos-alvo:** {arquivos_alvo_texto}\n"
        "- **Verificação:** bateria do §3.\n"
        "- **Pronto quando:** o teste passa.\n"
    )
    caminho.write_text(texto, encoding="utf-8")


def test_tf_escopo_respeitado_quando_tocados_sao_subconjunto_dos_alvos(tmp_path):
    """TF da EXA-T9a: arquivo novo (untracked) e arquivo modificado (tracked), ambos dentro dos
    arquivos-alvo declarados, produzem veredito mecânico 'conforme'; a lista de arquivos tocados
    enxerga o arquivo novo mesmo sem 'git add' (via 'git status', não só 'git diff --stat', que
    ignora untracked). A seção de guardas nasce nomeada e vazia, marcada como não coletada."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py` e edita `src/b.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "b.py").write_text(
        "def b():\n    return 1\n\n\ndef c():\n    return 3\n", encoding="utf-8"
    )

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Veredito mecânico: conforme" in documento
    assert "`src/a.py`" in documento
    assert "`src/b.py`" in documento
    assert "fora dos alvos" not in documento
    assert "## Guardas (bateria de `GOVERNANCA.md` §3)" in documento
    assert "não coletado" not in documento
    assert "Veredito mecânico (`guardas`): conforme" in documento
    assert "Veredito mecânico (`testes`): conforme" in documento


def test_escopo_violado_gera_fato_sem_inventar_parcial(tmp_path):
    """Arquivo fora dos alvos tocado: a saída relata o fato mecânico ('N arquivo(s) fora dos
    alvos') e deixa o veredito em aberto — nunca resolve sozinha para 'parcial' (a faixa
    'parcial' de RUBRICA_DE_REVISAO.md:63-77 depende de declaração de desvio no pacote de
    retorno, insumo que este script não recebe)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "nota.txt").write_text("fora do escopo\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Veredito mecânico: conforme" not in documento
    assert "parcial" not in documento
    assert "1 arquivo(s) fora dos alvos e sem atribuição: `docs/nota.txt`" in documento


def test_trechos_truncados_pelo_teto_marcam_truncamento_visivel(tmp_path):
    """Trecho de diff de arquivo-alvo maior que o teto declarado é cortado e a saída marca o
    corte de forma explícita — nunca trunca em silêncio."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/grande.py`.")

    conteudo_grande = "x = 1\n" * 200
    (repo / "src" / "grande.py").write_text(conteudo_grande, encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, teto_diff_chars=50, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "[truncado em 50 caracteres]" in documento
    trechos = review_evidence.montar_trechos(repo, ["src/grande.py"], 50)
    assert trechos["src/grande.py"]["truncado"] is True
    assert len(trechos["src/grande.py"]["texto"]) == 50


def test_tr_extrair_arquivos_alvo_ignora_texto_sem_barra_e_referencia_de_linha():
    """Regressão: crases sem '/' (código inline citado em prosa, não caminho) são ignoradas; um
    sufixo ':N' ou ':N-M' de referência de linha/trecho (padrão usado no campo 'Conteúdo' de
    tarefas do plano, ex. 'rdo.py:186') é removido do caminho extraído."""
    review_evidence = _load_review_evidence()
    campos = {
        "arquivos-alvo": (
            "cria `src/a.py`, reusa `extrair_dossie` (`.claude/tools/rdo.py:186`) e cita "
            "`docs/RUBRICA_DE_REVISAO.md:63-77`."
        )
    }
    resultado = review_evidence.extrair_arquivos_alvo(campos)
    assert resultado == ["src/a.py", ".claude/tools/rdo.py", "docs/RUBRICA_DE_REVISAO.md"]


def test_cli_main_ok_e_falhou(tmp_path, capsys):
    """`main()`: stdout de sucesso prefixado 'review_evidence: OK', exit 0; tarefa inexistente no
    plano produz stderr prefixado 'review_evidence: FALHOU' e exit 1 (nada escrito em --out)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    # CLI não expõe flag de bateria injetável (uso real sempre roda a bateria de produção) — o
    # teste sobrescreve a constante do módulo para não depender de `.claude/checks/*`/pwsh
    # ausentes no repositório de fixture.
    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE

    codigo = review_evidence.main(["--plano", str(plano), "--tarefa", "T1", "--root", str(repo)])
    saida = capsys.readouterr()
    assert codigo == 0
    assert "review_evidence: OK" in saida.out

    codigo_falho = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T-inexistente", "--root", str(repo)]
    )
    saida_falha = capsys.readouterr()
    assert codigo_falho == 1
    assert "review_evidence: FALHOU" in saida_falha.err


def test_tf_veredito_guardas_e_testes_travam_conforme_quando_bateria_toda_verde():
    """TF da EXA-T9b: veredito mecânico das dimensões `guardas` (`RUBRICA_DE_REVISAO.md:94-106`)
    e `testes` (`RUBRICA_DE_REVISAO.md:79-92`) resolve para `conforme` quando todos os comandos
    da bateria fecham em exit 0 — teste de unidade sobre a lógica de veredito, sem subprocess."""
    review_evidence = _load_review_evidence()
    resultados = [
        {"nome": "pytest", "comando": "python -m pytest -q", "exit_code": 0, "saida": ""},
        {
            "nome": "dead_code",
            "comando": "python .claude/checks/dead_code.py",
            "exit_code": 0,
            "saida": "",
        },
    ]
    assert review_evidence.veredito_guardas(resultados) == "conforme"
    assert review_evidence.veredito_testes(resultados) == "conforme"


def test_tr_comando_guarda_vermelho_trava_guardas_sem_travar_testes():
    """Regressão: comando não-`pytest` em exit não-zero trava a dimensão `guardas` em `não
    conforme` (`DA-7`, sem faixa de juízo — nunca degrada para `parcial` sozinha) mas não a
    `testes`, que só reage ao exit code do próprio comando `pytest` da bateria."""
    review_evidence = _load_review_evidence()
    resultados = [
        {"nome": "pytest", "comando": "python -m pytest -q", "exit_code": 0, "saida": ""},
        {
            "nome": "dead_code",
            "comando": "python .claude/checks/dead_code.py",
            "exit_code": 1,
            "saida": "achado orfao",
        },
    ]
    assert review_evidence.veredito_guardas(resultados) == "não conforme"
    assert review_evidence.veredito_testes(resultados) == "conforme"


def test_tr_pytest_vermelho_trava_testes_e_guardas():
    """Regressão: comando `pytest` em exit não-zero trava as duas dimensões em `não conforme` —
    `testes` porque a evidência dela é o próprio exit code do `pytest`, `guardas` porque `pytest`
    também é um dos comandos da bateria."""
    review_evidence = _load_review_evidence()
    resultados = [{"nome": "pytest", "comando": "python -m pytest -q", "exit_code": 1, "saida": "1 failed"}]
    assert review_evidence.veredito_guardas(resultados) == "não conforme"
    assert review_evidence.veredito_testes(resultados) == "não conforme"


def test_tr_bateria_sem_comando_pytest_trava_testes_nao_conforme():
    """Regressão defensiva: bateria injetada sem comando nomeado `pytest` trava `testes` em `não
    conforme` (sem evidência mecânica, nunca silêncio) mesmo com todos os demais comandos verdes."""
    review_evidence = _load_review_evidence()
    resultados = [
        {
            "nome": "dead_code",
            "comando": "python .claude/checks/dead_code.py",
            "exit_code": 0,
            "saida": "",
        }
    ]
    assert review_evidence.veredito_testes(resultados) == "não conforme"


def test_tf_secao_guardas_renderiza_exit_code_e_veredito_end_to_end(tmp_path):
    """TF end-to-end da `EXA-T9b`: `montar_documento` roda a bateria injetada, cola exit code de
    cada comando na seção `## Guardas` e estampa os dois vereditos travados — sem o placeholder
    'não coletado' da `T9a`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")

    comandos_fake = [
        ("pytest", ["python", "-c", "import sys; sys.exit(0)"]),
        ("dead_code", ["python", "-c", "import sys; sys.exit(1)"]),
    ]
    documento = review_evidence.montar_documento(plano, "T1", repo, comandos_guardas=comandos_fake)

    assert "## Guardas (bateria de `GOVERNANCA.md` §3)" in documento
    assert "`pytest` (`python -c import sys; sys.exit(0)`): exit 0" in documento
    assert "`dead_code` (`python -c import sys; sys.exit(1)`): exit 1" in documento
    assert "Veredito mecânico (`guardas`): não conforme" in documento
    assert "Veredito mecânico (`testes`): conforme" in documento
    assert "não coletado" not in documento


def test_alvo_diretorio_casa_por_prefixo_com_arquivo_tocado_dentro(tmp_path):
    """AUT-T5b: um `Arquivos-alvo` declarado como diretório (ex.: `.claude/tools/`) casa por
    prefixo com um arquivo tocado dentro dele — não aparece em 'fora dos alvos' e o documento
    traz o trecho de diff do arquivo real, nunca mais o fallback 'arquivo ausente na árvore de
    trabalho' só porque o alvo é um diretório."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "toca `.claude/tools/`.")

    (repo / ".claude" / "tools" / "novo.py").write_text(
        "def novo():\n    return 1\n", encoding="utf-8"
    )

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Veredito mecânico: conforme" in documento
    assert "fora dos alvos" not in documento
    assert "arquivo ausente na árvore de trabalho" not in documento
    assert "### `.claude/tools/novo.py`" in documento


def test_desde_recorta_tocados_a_partir_da_referencia(tmp_path):
    """AUT-T5b: `--desde <ref>` recorta o conjunto de tocados — só arquivos rastreados alterados
    **depois** de `<ref>` entram; um arquivo que já divergia do HEAD anterior mas não mudou depois
    do `<ref>` fica de fora. Untracked sempre entra, com ou sem `--desde` (não existe no histórico,
    então nunca é "desde um ref")."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "c.py").write_text("def c():\n    return 3\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "segunda rodada"], repo)
    ref = _run_git(["rev-parse", "HEAD"], repo).strip()

    (repo / "src" / "b.py").write_text("def b():\n    return 4\n", encoding="utf-8")
    (repo / "src" / "d.py").write_text("def d():\n    return 5\n", encoding="utf-8")

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)

    assert tocados == ["src/b.py", "src/d.py"]


def test_escopo_declara_recorte_arvore_inteira_sem_desde(tmp_path):
    """AUT-T5b: sem `--desde`, a seção `## Escopo` declara explicitamente que o recorte medido é a
    árvore de trabalho inteira — o dossiê nunca afirma escopo que não mediu."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert (
        "- Recorte: árvore de trabalho inteira (nenhum `--desde` informado)" in documento
    )


def test_tf_extrair_arquivos_alvo_aceita_arquivo_de_raiz_e_recusa_literal_de_regex():
    """TF da BKL-T2b: arquivo de raiz (`CHANGELOG.md`, sem barra, com extensão) passa a ser
    reconhecido como alvo; literal de trecho de regex (`_ID_HEADER_RE = re.compile(x)`, com
    espaço) é recusado pela gramática de caminho da `DB-27`."""
    review_evidence = _load_review_evidence()
    campos = {
        "arquivos-alvo": (
            "- `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` "
            "- `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)"
        )
    }
    resultado = review_evidence.extrair_arquivos_alvo(campos)
    assert resultado == [".claude/tools/rdo.py", "CHANGELOG.md"]


def test_tr_extrair_literais_nao_caminho_lista_o_descartado():
    """Regressão: os literais entre crases que não casam a gramática de caminho (cabeçalho de
    seção, trecho de regex) saem em `extrair_literais_nao_caminho`, não silenciosamente."""
    review_evidence = _load_review_evidence()
    campos = {
        "arquivos-alvo": (
            "- `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` "
            "- `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)"
        )
    }
    resultado = review_evidence.extrair_literais_nao_caminho(campos)
    assert "## [Não lançado]" in resultado
    assert any("re.compile" in item for item in resultado)


def test_tr_extrair_arquivos_alvo_recusa_id_de_tarefa_e_de_decisao():
    """Regressão: identificador de tarefa/decisão entre crases (sem barra e sem extensão) não é
    caminho pela gramática da `DB-27` e não vira alvo declarado."""
    review_evidence = _load_review_evidence()
    campos = {"arquivos-alvo": "ver `BKL-T9` e `DB-13`."}
    resultado = review_evidence.extrair_arquivos_alvo(campos)
    assert resultado == []


def test_tf_secao_escopo_lista_literais_nao_reconhecidos_como_caminho(tmp_path):
    """TF de ponta a ponta da BKL-T2b: um literal de trecho de regex citado no campo
    `Arquivos-alvo` aparece na seção `## Escopo` como literal não reconhecido como caminho."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`; ver `_RE = re.compile(x)`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Literais não reconhecidos como caminho (1)" in documento


def _escrever_plano_duas_tarefas(
    caminho: Path, alvo_t1: str, alvo_t2: str, verificacao_t2: str | None = "bateria do §3."
) -> None:
    """Plano sintético com duas tarefas; `verificacao_t2=None` omite um campo obrigatório de T2
    para exercitar o ramo 'dossiê inválido é pulado' de `mapear_alvos_de_outras_tarefas`."""
    linha_verificacao = f"- **Verificação:** {verificacao_t2}\n" if verificacao_t2 else ""
    texto = (
        "# Plano de teste\n\n"
        "### T1 — Tarefa sintética de teste [Sonnet · classe implementacao]\n"
        "- **Objetivo:** validar review_evidence.py.\n"
        f"- **Arquivos-alvo:** {alvo_t1}\n"
        "- **Verificação:** bateria do §3.\n"
        "- **Pronto quando:** o teste passa.\n\n"
        "### T2 — Outra tarefa sintética [Sonnet · classe implementacao]\n"
        "- **Objetivo:** ser a dona de outro arquivo.\n"
        f"- **Arquivos-alvo:** {alvo_t2}\n"
        f"{linha_verificacao}"
        "- **Pronto quando:** o teste passa.\n"
    )
    caminho.write_text(texto, encoding="utf-8")


def test_tf_arquivo_alvo_de_outra_tarefa_sai_atribuido_e_nao_pesa_no_veredito(tmp_path):
    """TF da BKL-T2c: arquivo tocado que não é alvo de T1 mas é alvo declarado de T2 (mesmo plano)
    sai atribuído a T2 na seção `## Escopo` e não pesa no veredito mecânico de T1."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "b.py").write_text(
        "def b():\n    return 1\n\n\ndef c():\n    return 3\n", encoding="utf-8"
    )

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "`src/a.py` → `T2`" in documento
    assert "Veredito mecânico: conforme" in documento


def test_tf_registro_da_orquestracao_sai_em_balde_proprio(tmp_path):
    """TF da BKL-T2c: arquivo de registro da orquestração (`docs/DIARIO_DE_OBRAS.md`,
    `docs/telemetria.tsv`) tocado fora dos alvos sai em balde próprio, sem pesar no veredito."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "b.py").write_text(
        "def b():\n    return 1\n\n\ndef c():\n    return 3\n", encoding="utf-8"
    )
    (repo / "docs").mkdir()
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text("# Diário\n", encoding="utf-8")
    (repo / "docs" / "telemetria.tsv").write_text("a\tb\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Registro da orquestração (não atribuível a tarefa)" in documento
    assert "Veredito mecânico: conforme" in documento


def test_tr_arquivo_sem_atribuicao_continua_fora_dos_alvos_com_veredito_aberto(tmp_path):
    """Regressão: arquivo que não é alvo de T1, não é alvo de nenhuma outra tarefa do plano e não é
    registro da orquestração continua caindo em 'fora dos alvos', com veredito aberto."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "b.py").write_text(
        "def b():\n    return 1\n\n\ndef c():\n    return 3\n", encoding="utf-8"
    )
    (repo / "src" / "c.py").write_text("def c():\n    return 4\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "1 arquivo(s) fora dos alvos e sem atribuição" in documento
    assert "(aberto" in documento


def test_tr_tarefa_com_dossie_invalido_e_pulada_pela_atribuicao(tmp_path):
    """Regressão: tarefa cujo dossiê não extrai (campo obrigatório ausente) é pulada pela
    atribuição a outra tarefa, sem subir exceção."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(
        plano, "edita `src/b.py`.", "cria `src/a.py`.", verificacao_t2=None
    )

    mapa = review_evidence.mapear_alvos_de_outras_tarefas(plano, "T1", repo)

    assert mapa == {}


def test_tf_ato_do_dono_sai_em_balde_proprio_e_nao_pesa_no_veredito(tmp_path):
    """TF da BKL-T2e: arquivo sob `.claude/agents/` tocado fora dos alvos sai em balde próprio
    ('ato do dono'), sem pesar no veredito mecânico."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "b.py").write_text(
        "def b():\n    return 1\n\n\ndef c():\n    return 3\n", encoding="utf-8"
    )
    (repo / ".claude" / "agents").mkdir(parents=True, exist_ok=True)
    (repo / ".claude" / "agents" / "pantonic-planner.md").write_text(
        "# Agente\n", encoding="utf-8"
    )

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "- Ato do dono, fora do ciclo de tarefa: `.claude/agents/pantonic-planner.md`" in documento
    assert "Veredito mecânico: conforme" in documento


def test_tr_arquivo_em_claude_fora_de_agents_continua_sem_atribuicao(tmp_path):
    """Regressão: arquivo sob `.claude/` que não é `.claude/agents/` continua caindo em 'fora dos
    alvos', sem entrar no balde de ato do dono."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "b.py").write_text(
        "def b():\n    return 1\n\n\ndef c():\n    return 3\n", encoding="utf-8"
    )
    (repo / ".claude" / "settings.json").write_text("{}\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "1 arquivo(s) fora dos alvos e sem atribuição" in documento
    assert "(aberto" in documento


def test_tr_agente_declarado_como_alvo_do_card_fica_no_balde_de_cobertura(tmp_path):
    """Regressão: a cobertura pelos alvos do card tem precedência sobre o balde de ato do dono
    (`DB-32`) — arquivo sob `.claude/agents/` declarado como alvo não aparece nomeado ali."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(
        plano, "edita `.claude/agents/pantonic-planner.md`.", "cria `src/a.py`."
    )

    (repo / ".claude" / "agents").mkdir(parents=True, exist_ok=True)
    (repo / ".claude" / "agents" / "pantonic-planner.md").write_text(
        "# Agente\n", encoding="utf-8"
    )

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Veredito mecânico: conforme" in documento
    assert "Ato do dono" not in documento


def test_tf_confrontar_escopo_devolve_a_chave_ato_do_dono_com_separador_do_windows(tmp_path):
    """TF da BKL-T2e: `confrontar_escopo` normaliza separador do Windows e classifica arquivo sob
    `.claude/agents/` no balde `ato_do_dono`, sem pesar no veredito."""
    review_evidence = _load_review_evidence()

    resultado = review_evidence.confrontar_escopo(
        [".claude\\agents\\pantonic-planner.md"], [], tmp_path
    )

    assert resultado["ato_do_dono"] == [".claude\\agents\\pantonic-planner.md"]
    assert resultado["fora_dos_alvos"] == []
    assert resultado["veredito"] == "conforme"


def test_tf_arquivo_tocado_dentro_dos_alvos_sai_marcado_como_da_entrega(tmp_path):
    """TF da LM-T3 (`AE-13`): na seção `## Arquivos tocados`, um arquivo coberto pelos
    `Arquivos-alvo` do card sai com a atribuição `da entrega` — derivada por diferença de
    conjuntos sobre o que `confrontar_escopo` já devolve, sem segundo laço de cobertura."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `src/b.py`.")

    (repo / "src" / "b.py").write_text("def b():\n    return 9\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "- `src/b.py` — atribuição: da entrega; estado git: `" in documento


def test_tf_arquivo_tocado_fora_dos_alvos_sai_marcado_como_alheio_com_estado_git(tmp_path):
    """TF da LM-T3 (`AE-13`): arquivo tocado fora dos `Arquivos-alvo` sai com a atribuição
    `alheio` e o estado `git` (`??` — untracked) que a comprova, sem exigir injeção manual de
    contexto do orquestrador para o reviewer não reprovar a entrega correta."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 1\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "nota.txt").write_text("fora do escopo\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "- `docs/nota.txt` — atribuição: alheio; estado git: `??`" in documento


def test_tr_atribuicao_de_arquivos_tocados_cobre_os_quatro_baldes_alheios_de_confrontar_escopo(
    tmp_path,
):
    """Regressão da LM-T3: a atribuição `alheio` da seção `## Arquivos tocados` cobre os quatro
    baldes alheios que `confrontar_escopo` devolve (`fora_dos_alvos`, `de_outra_tarefa`,
    `registro_orquestracao`, `ato_do_dono`) — não só `fora_dos_alvos`. Prova que a seção lê o
    dicionário que `confrontar_escopo` já calcula em vez de reimplementar uma segunda checagem de
    cobertura (`DM-19`): um arquivo do balde `registro_orquestracao`, que nunca aparece em
    `fora_dos_alvos`, ainda assim sai marcado `alheio`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 1\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "telemetria.tsv").write_text("t\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "- `docs/telemetria.tsv` — atribuição: alheio; estado git: `??`" in documento


def test_tf_atribuir_classifica_nos_cinco_baldes(tmp_path, capsys):
    """TF da LM-T2a: com `--atribuir`, a saída traz uma linha por arquivo tocado com o balde certo
    dos cinco da `DB-25`/`DB-32`, inclusive `alvo-do-card` para o arquivo coberto pelos
    `Arquivos-alvo` do próprio card. *Concorrente:* hoje o argumento nem é reconhecido (exit 2)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "cria `src/a.py`.", "cria `src/z.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 1\n", encoding="utf-8")
    (repo / "src" / "z.py").write_text("def z():\n    return 1\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "telemetria.tsv").write_text("t\n", encoding="utf-8")
    (repo / "docs" / "nota.txt").write_text("fora do escopo\n", encoding="utf-8")
    (repo / ".claude" / "agents").mkdir(parents=True)
    (repo / ".claude" / "agents" / "foo.md").write_text("agente\n", encoding="utf-8")

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    linhas_atribuicao = [l for l in saida.out.splitlines() if l.startswith("atribuicao:")]
    assert linhas_atribuicao == [
        "atribuicao: .claude/agents/foo.md -> ato-do-dono",
        "atribuicao: docs/nota.txt -> sem-atribuicao",
        "atribuicao: docs/telemetria.tsv -> registro-da-orquestracao",
        "atribuicao: src/a.py -> alvo-do-card",
        "atribuicao: src/z.py -> alvo-de-outra-tarefa (T2)",
        "atribuicao: OK - 5 arquivo(s), 1 sem atribuicao.",
    ]


def test_tf_atribuir_sai_0_mesmo_com_arquivo_sem_atribuicao(tmp_path, capsys):
    """TF da LM-T2a: `--atribuir` sai exit 0 mesmo havendo arquivo `sem-atribuicao` na saída — o
    verbo informa, quem julga é o reviewer pela rubrica. *Concorrente:* uma implementação que
    tratasse o balde como falha (exit 1) faria o `B0` do loop encerrar janela por informação, o
    defeito 4 da §3."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 1\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "nota.txt").write_text("fora do escopo\n", encoding="utf-8")

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "atribuicao: docs/nota.txt -> sem-atribuicao" in saida.out


def test_tr_atribuir_nao_monta_dossie(tmp_path, capsys):
    """Regressão da LM-T2a: com `--atribuir`, nenhum documento é montado nem impresso e o caminho
    de `--out` não é criado. *Concorrente:* implementar a flag depois da montagem do documento
    gravaria o dossiê como efeito colateral."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 1\n", encoding="utf-8")
    saida_out = tmp_path / "saida.md"

    codigo = review_evidence.main(
        [
            "--plano",
            str(plano),
            "--tarefa",
            "T1",
            "--root",
            str(repo),
            "--atribuir",
            "--out",
            str(saida_out),
        ]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "# Evidência de revisão" not in saida.out
    assert "## Arquivos tocados" not in saida.out
    assert not saida_out.exists()


def test_tf_atribuir_alvo_diretorio_casa_por_prefixo(tmp_path, capsys):
    """TF da LM-T2a (`ESC-4`, `DM-21` (ii)(a)): `Arquivos-alvo` declarado como diretório casa por
    prefixo com arquivo tocado dentro dele e sai `alvo-do-card`. *Concorrente:* é este o caso em
    que uma segunda implementação por caminho exato — a reimplementação que a `Restrição` da
    `LM-T2a` proíbe — devolveria `sem-atribuicao`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "toca `.claude/tools/`.")

    (repo / ".claude" / "tools" / "novo.py").write_text(
        "def novo():\n    return 1\n", encoding="utf-8"
    )

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "atribuicao: .claude/tools/novo.py -> alvo-do-card" in saida.out
    assert "sem-atribuicao" not in saida.out


def test_tf_estado_git_de_arquivo_commitado_desde_a_ref(tmp_path):
    """LM-T3a: `coletar_estado_git(root, desde=<ref>)` compõe a evidência `git` de duas fontes —
    um arquivo alterado e **commitado** depois da `ref` sai marcado `M (commitado desde <ref>)`,
    lido de `git diff <ref> --name-status`. *Concorrente:* hoje (sem `desde`) essa entrada não
    existe no mapa, e o renderizador imprime `(sem entrada em `git status`)`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = _run_git(["rev-parse", "HEAD"], repo).strip()

    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "segunda rodada"], repo)

    estados = review_evidence.coletar_estado_git(repo, desde=ref)

    assert estados["src/b.py"] == f"M (commitado desde {ref})"


def test_tr_estado_da_arvore_de_trabalho_vence(tmp_path):
    """LM-T3a: quando o mesmo caminho tem mudança commitada desde a `ref` **e** mudança na árvore
    de trabalho ainda não commitada, o código de duas letras do `git status` vence — a entrada
    permanece ` M`, nunca a forma `(commitado desde ...)`, porque `setdefault` só preenche o que o
    `git status` ainda não tinha marcado."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = _run_git(["rev-parse", "HEAD"], repo).strip()

    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "segunda rodada"], repo)
    (repo / "src" / "b.py").write_text("def b():\n    return 3\n", encoding="utf-8")

    estados = review_evidence.coletar_estado_git(repo, desde=ref)

    assert estados["src/b.py"] == " M"


def test_tr_sem_desde_nada_muda(tmp_path, monkeypatch):
    """LM-T3a: sem `desde`, `coletar_estado_git` devolve exatamente o mapa do `git status` e
    nenhuma chamada de `git diff` acontece — a assinatura permanece compatível com a chamada de
    um só argumento que já existia."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")

    original_git = review_evidence._git

    def _git_sem_diff(args, root):
        assert args[0] != "diff", "coletar_estado_git sem `desde` não deve chamar git diff"
        return original_git(args, root)

    monkeypatch.setattr(review_evidence, "_git", _git_sem_diff)

    estados = review_evidence.coletar_estado_git(repo)

    assert estados == {"src/b.py": " M"}


def test_tf_atribuir_com_plano_inexistente_falha_pelo_canal_do_modulo(tmp_path, capsys):
    """LM-T3a (`AE-17`): `--atribuir` com `--plano` inexistente falha pelo mesmo canal que o
    caminho sem `--atribuir` — `ReviewEvidenceValidationError` impressa como `review_evidence:
    FALHOU - ...` no stderr, exit 1. *Concorrente:* hoje esse caminho estoura `FileNotFoundError`
    cru, sem passar por `_exigir_plano`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano_inexistente = tmp_path / "NAO-EXISTE.md"

    codigo = review_evidence.main(
        ["--plano", str(plano_inexistente), "--tarefa", "T1", "--root", str(repo), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "review_evidence: FALHOU - plano: arquivo não encontrado" in saida.err


def test_tr_dossie_com_plano_inexistente_nao_muda(tmp_path, capsys):
    """Regressão: o mesmo caso do teste acima, sem `--atribuir`, continua saindo exit 1 com a
    mesma mensagem — `_exigir_plano` não muda a forma já publicada da falha do caminho do
    dossiê."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano_inexistente = tmp_path / "NAO-EXISTE.md"

    codigo = review_evidence.main(
        ["--plano", str(plano_inexistente), "--tarefa", "T1", "--root", str(repo)]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "review_evidence: FALHOU - plano: arquivo não encontrado" in saida.err


def test_tr_atribuir_com_tarefa_inexistente_continua_igual(tmp_path, capsys):
    """Regressão: com plano válido e `--tarefa` inexistente, `--atribuir` continua saindo exit 1
    com `review_evidence: FALHOU - tarefa: '<ID>' não encontrada em` — comportamento já correto
    hoje, que o alargamento do `except` para `ReviewEvidenceValidationError` não pode quebrar."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    codigo = review_evidence.main(
        [
            "--plano",
            str(plano),
            "--tarefa",
            "T-inexistente",
            "--root",
            str(repo),
            "--atribuir",
        ]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "review_evidence: FALHOU - tarefa: 'T-inexistente' não encontrada em" in saida.err
