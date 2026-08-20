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
        "### T1 — Tarefa sintética de teste [Sonnet · classe implementação padrão · teto 40]\n"
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
    assert "1 arquivo(s) fora dos alvos: `docs/nota.txt`" in documento


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
