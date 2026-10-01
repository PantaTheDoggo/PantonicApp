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
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

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
    shutil.copy2(_RDO_REAL_PATH.parent / "caminhos.py", destino_rdo.parent / "caminhos.py")
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
    'parcial' de RUBRICA_DE_REVISAO.md §4 depende de declaração de desvio no pacote de
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


def test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica(tmp_path, capsys):
    """TK-62a (`DB-17`/`DB-22`): a gramática de ID mora em `rdo.py` só, e `review_evidence` reusa
    `extrair_dossie` de lá — `--tarefa TK-62a` (subtarefa, cabeçalho `### … [modelo · classe …]`)
    localiza e sai OK; `--tarefa TK-62` (cabeçalho de nível 2 do tíquete-pai, sem bracket) não é
    ID de tarefa e continua recusado."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    plano.write_text(
        "# Plano de teste\n\n"
        "## TK-62 — Tíquete pai de teste\n\n"
        "### TK-62a — Subtarefa sintética de teste [Sonnet · classe implementacao]\n"
        "- **Objetivo:** validar review_evidence.py.\n"
        "- **Arquivos-alvo:** cria `src/a.py`.\n"
        "- **Verificação:** bateria do §3.\n"
        "- **Pronto quando:** o teste passa.\n",
        encoding="utf-8",
    )
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "TK-62a", "--root", str(repo)]
    )
    saida = capsys.readouterr()
    assert codigo == 0
    assert "review_evidence: OK" in saida.out

    codigo_falho = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "TK-62", "--root", str(repo)]
    )
    saida_falha = capsys.readouterr()
    assert codigo_falho == 1
    assert "review_evidence: FALHOU" in saida_falha.err


def test_tf_san_15_evidencia_na_pasta_do_plano(tmp_path, capsys):
    """TF da SAN-T3: sem `--out`, `main` sobre um plano em pasta grava a evidência dentro de
    `<pasta-do-plano>/evidencia/<tarefa>.md`; sobre um plano legado (arquivo solto em
    `docs/plans/`), nenhum arquivo é criado (o legado segue sem destino default até `--out`
    explícito — só `docs/plans` ganha os dois planos usados neste teste, nada mais)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE

    plano = tmp_path / "docs" / "plans" / "P-0-gama" / "plano.md"
    plano.parent.mkdir(parents=True)
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")

    codigo = review_evidence.main(["--plano", str(plano), "--tarefa", "T1", "--root", str(repo)])
    capsys.readouterr()
    assert codigo == 0
    assert (plano.parent / "evidencia" / "T1.md").is_file()

    plano_legado = tmp_path / "docs" / "plans" / "P-0749-legado.md"
    _escrever_plano(plano_legado, "cria `src/a.py`.")

    codigo2 = review_evidence.main(
        ["--plano", str(plano_legado), "--tarefa", "T1", "--root", str(repo)]
    )
    capsys.readouterr()
    assert codigo2 == 0
    assert sorted(p.name for p in (tmp_path / "docs" / "plans").iterdir()) == [
        "P-0-gama",
        "P-0749-legado.md",
    ]


def test_tf_veredito_guardas_e_testes_travam_conforme_quando_bateria_toda_verde():
    """TF da EXA-T9b: veredito mecânico das dimensões `guardas` (`RUBRICA_DE_REVISAO.md` §4)
    e `testes` (`RUBRICA_DE_REVISAO.md` §4) resolve para `conforme` quando todos os comandos
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
    do `<ref>` fica de fora. Untracked criado depois do `<ref>` entra (o anterior sai pela data —
    TK-84a)."""
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


def test_coletar_nao_rastreado_anterior_ao_desde_sai_dos_tocados(tmp_path):
    """TF da TK-84a: com `desde=<ref>`, o não rastreado com `st_mtime` anterior à data de commit
    de `<ref>` sai dos tocados e o posterior entra; sem `desde`, o anterior continua na lista."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = _run_git(["rev-parse", "HEAD"], repo).strip()
    ct = int(_run_git(["show", "-s", "--format=%ct", ref], repo).strip())

    velho = repo / "src" / "velho.py"
    velho.write_text("def velho():\n    return 1\n", encoding="utf-8")
    os.utime(velho, (ct - 60, ct - 60))
    novo = repo / "src" / "novo.py"
    novo.write_text("def novo():\n    return 2\n", encoding="utf-8")
    os.utime(novo, (ct + 60, ct + 60))

    tocados_desde = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
    assert "src/novo.py" in tocados_desde
    assert "src/velho.py" not in tocados_desde

    assert "src/velho.py" in review_evidence.coletar_arquivos_tocados(repo)


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
            "- `.claude/tools/rdo.py` — `_ID_HEADER_RE = re.compile(x)` "
            "- `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)"
        )
    }
    resultado = review_evidence.extrair_literais_nao_caminho(campos)
    assert "## [Não lançado]" in resultado
    assert any("re.compile" in item for item in resultado)


def test_tf_alvo_ancorado_com_literal_e_um_alvo():
    """TF da TK-89a: âncora `caminho:linha` seguida do literal dela (mesmo com crase escapada
    dentro do literal) é cortada antes da varredura por crase — o literal não vai para os
    descartados e a âncora conta como um alvo só."""
    review_evidence = _load_review_evidence()
    campos = {"arquivos-alvo": "- `a/b.md:3` — `x \\` y` - `c/d.py`"}
    resultado = review_evidence._classificar_campo_alvos(campos)
    assert resultado == (["a/b.md", "c/d.py"], [])


def test_tr_alvo_sem_ancora_nao_muda():
    """Regressão da TK-89a: campo sem âncora `caminho:linha` (só caminhos entre crases e um
    literal não caminho) não é afetado pelo corte — mesmo resultado de antes da TK-89a."""
    review_evidence = _load_review_evidence()
    campos = {"arquivos-alvo": "- `src/app.py` - `BKL-T9` - `docs/readme.md`"}
    resultado = review_evidence._classificar_campo_alvos(campos)
    assert resultado == (["src/app.py", "docs/readme.md"], ["BKL-T9"])


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
    caminho: Path,
    alvo_t1: str,
    alvo_t2: str,
    verificacao_t2: str | None = "bateria do §3.",
    status_t2: str | None = "done",
) -> None:
    """Plano sintético com duas tarefas; `verificacao_t2=None` omite um campo obrigatório de T2
    para exercitar o ramo 'dossiê inválido é pulado' de `mapear_alvos_de_outras_tarefas`;
    `status_t2=None` omite a linha `**Status:**` de T2."""
    linha_verificacao = f"- **Verificação:** {verificacao_t2}\n" if verificacao_t2 else ""
    linha_status = f"- **Status:** `{status_t2}` · 2026-09-25\n" if status_t2 is not None else ""
    texto = (
        "# Plano de teste\n\n"
        "### T1 — Tarefa sintética de teste [Sonnet · classe implementacao]\n"
        "- **Objetivo:** validar review_evidence.py.\n"
        f"- **Arquivos-alvo:** {alvo_t1}\n"
        "- **Verificação:** bateria do §3.\n"
        "- **Pronto quando:** o teste passa.\n\n"
        "### T2 — Outra tarefa sintética [Sonnet · classe implementacao]\n"
        f"{linha_status}"
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


def test_tf_relatorio_de_auditoria_sai_como_registro_da_orquestracao(tmp_path):
    """TF da AF-T2: `docs/audits/` entra no balde de registro da orquestração — o relatório de
    auditoria de quem conduz, tocado fora dos alvos do card, não pesa no veredito mecânico."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `src/b.py`.")

    (repo / "src" / "b.py").write_text("def b():\n    return 9\n", encoding="utf-8")
    (repo / "docs" / "audits").mkdir(parents=True, exist_ok=True)
    (repo / "docs" / "audits" / "AUDITORIA_X.md").write_text("# Auditoria\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Registro da orquestração (não atribuível a tarefa)" in documento
    assert "Veredito mecânico: conforme" in documento


def test_tr_acionamentos_do_consultor_sai_como_registro_da_orquestracao(tmp_path):
    """TR (`AE-4` do `P-0753`): `docs/ACIONAMENTOS_CONSULTOR.tsv`, que o consultor apensa em cada
    triagem, tocado fora dos alvos do card, sai no balde de registro da orquestração e não pesa no
    veredito mecânico — antes saía `fora dos alvos e sem atribuição`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `src/b.py`.")

    (repo / "src" / "b.py").write_text("def b():\n    return 9\n", encoding="utf-8")
    (repo / "docs").mkdir(parents=True, exist_ok=True)
    (repo / "docs" / "ACIONAMENTOS_CONSULTOR.tsv").write_text("linha\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "Registro da orquestração (não atribuível a tarefa): `docs/ACIONAMENTOS_CONSULTOR.tsv`" in documento
    assert "Veredito mecânico: conforme" in documento


def test_tr_relatorio_de_auditoria_alvo_do_card_segue_coberto(tmp_path):
    """Regressão: quando `docs/audits/AUDITORIA_X.md` é o próprio alvo declarado do card, a
    cobertura pelos `Arquivos-alvo` tem precedência sobre o balde de registro da orquestração —
    a atribuição sai `da entrega`, nunca `registro da orquestração` (a regra concorrente, 'tudo em
    `docs/audits/` é registro', daria registro da orquestração)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `docs/audits/AUDITORIA_X.md`.")

    (repo / "docs" / "audits").mkdir(parents=True, exist_ok=True)
    (repo / "docs" / "audits" / "AUDITORIA_X.md").write_text("# Auditoria\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "- `docs/audits/AUDITORIA_X.md` — atribuição: da entrega; estado git: `" in documento
    assert "Registro da orquestração" not in documento


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
    `fora_dos_alvos`, sai marcado com o nome do balde, `registro da orquestração` (`R-14`, RAF-T8)."""
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

    assert "- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: `??`" in documento


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


def test_tf_atribuir_alvo_diretorio_de_outra_tarefa_casa_por_prefixo(tmp_path, capsys):
    """TF da TK-74a (`AE-22` do `P-0746`): arquivo tocado sob o alvo-diretório declarado por
    **outra** tarefa do mesmo plano sai `alvo-de-outra-tarefa (<ID>)`. Par presença-ausência:
    o arquivo fora de qualquer alvo segue `sem-atribuicao`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `tests/fixtures/modelo/`.")

    (repo / "tests" / "fixtures" / "modelo").mkdir(parents=True)
    (repo / "tests" / "fixtures" / "outro").mkdir(parents=True)
    (repo / "tests" / "fixtures" / "modelo" / "a.md").write_text("# a\n", encoding="utf-8")
    (repo / "tests" / "fixtures" / "outro" / "b.md").write_text("# b\n", encoding="utf-8")

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "atribuicao: tests/fixtures/modelo/a.md -> alvo-de-outra-tarefa (T2)" in saida.out
    assert "atribuicao: tests/fixtures/outro/b.md -> sem-atribuicao" in saida.out


def test_tf_tarefa_dona_exato_vence_e_prefixo_mais_longo_desempata(tmp_path):
    """TF da TK-74a: na atribuição a outra tarefa, o caminho exato vence o alvo-diretório e, entre
    alvos-diretório, o de prefixo mais longo desempata."""
    review_evidence = _load_review_evidence()

    escopo = review_evidence.confrontar_escopo(
        ["tests/fixtures/modelo/a.md", "tests/fixtures/modelo/c.md", "tests/x.md"],
        [],
        tmp_path,
        {"tests/": "T2", "tests/fixtures/modelo/": "T3", "tests/fixtures/modelo/a.md": "T4"},
    )

    assert escopo["de_outra_tarefa"] == {
        "tests/fixtures/modelo/a.md": "T4",
        "tests/fixtures/modelo/c.md": "T3",
        "tests/x.md": "T2",
    }


@pytest.mark.parametrize(
    ("status_t2", "esperado"),
    [
        ("in-progress", "alvo-de-outra-tarefa (T2)"),
        ("review", "alvo-de-outra-tarefa (T2)"),
        ("done", "alvo-de-outra-tarefa (T2)"),
        ("ready", "sem-atribuicao"),
        ("blocked", "sem-atribuicao"),
        ("cancelled", "sem-atribuicao"),
        (None, "sem-atribuicao"),
    ],
)
def test_tf_atribuir_so_tarefa_despachada_casa(tmp_path, capsys, status_t2, esperado):
    """TF da TK-66a (`AE-3` do `P-0743`): alvo declarado por tarefa não despachada é previsão,
    não autoria — só tarefa em `in-progress`, `review` ou `done` recebe a atribuição."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano_duas_tarefas(
        plano, "edita `src/b.py`.", "cria `src/a.py`.", status_t2=status_t2
    )

    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert f"atribuicao: src/a.py -> {esperado}" in saida.out


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


def test_tf_alvo_com_sufixo_de_secao_e_caminho():
    """TF da TK-78c: `extrair_arquivos_alvo` sobre um campo `arquivos-alvo` cujo único literal
    entre crases é `docs/x.md §2.1` devolve `["docs/x.md"]` — sufixo de seção é removido do
    caminho extraído, igual ao sufixo de referência de linha (`_LINHA_REF_RE`)."""
    review_evidence = _load_review_evidence()
    campos = {"arquivos-alvo": "edita `docs/x.md §2.1`."}
    resultado = review_evidence.extrair_arquivos_alvo(campos)
    assert resultado == ["docs/x.md"]


def test_tf_trecho_desde_instantaneo_mostra_so_o_delta(tmp_path):
    """TF da TK-78c: com `desde=<snap>` (instantâneo de `git stash create`), o trecho de diff de
    um arquivo-alvo mostra só o que mudou depois do instantâneo — a edição anterior ao snapshot
    não aparece."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "a.md").write_text("linha-base\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "a.md baseline"], repo)

    (repo / "a.md").write_text("linha-base\nlinha-velha\n", encoding="utf-8")
    snap = _run_git(["stash", "create"], repo).strip()

    (repo / "a.md").write_text("linha-base\nlinha-velha\nlinha-nova\n", encoding="utf-8")

    trechos = review_evidence.montar_trechos(repo, ["a.md"], 4000, desde=snap)

    assert "+linha-nova" in trechos["a.md"]["texto"]
    assert "+linha-velha" not in trechos["a.md"]["texto"]


def test_tf_capturar_ref_carrega_nao_rastreado(tmp_path):
    """TF da TK-93a: `capturar_ref` grava um commit cuja árvore inclui o não rastreado — `git show
    <ref>:<arquivo>` devolve o conteúdo dele — sem alterar árvore de trabalho, índice real nem
    lista de stash (`git status` e `git stash list` saem iguais aos de antes da captura)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "novo.txt").write_text("conteudo novo\n", encoding="utf-8")

    status_antes = _run_git(["status", "--porcelain=v1", "--untracked-files=all"], repo)
    stash_antes = _run_git(["stash", "list"], repo)

    ref = review_evidence.capturar_ref(repo)

    assert _run_git(["show", f"{ref}:novo.txt"], repo) == "conteudo novo\n"
    assert _run_git(["status", "--porcelain=v1", "--untracked-files=all"], repo) == status_antes
    assert _run_git(["stash", "list"], repo) == stash_antes


def test_tf_nao_rastreado_no_ref_mostra_so_o_hunk(tmp_path):
    """TF da TK-93a: não rastreado de 400 linhas já presente no `<ref>` (capturado por
    `capturar_ref`), com uma linha editada depois — o trecho traz a linha nova com `+` e não é
    truncado no teto de 4000, e `coletar_arquivos_tocados` devolve só ele; outro não rastreado, sem
    mudança desde `<ref>`, fica de fora."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    linhas = [f"linha-{i}\n" for i in range(400)]
    (repo / "grande.txt").write_text("".join(linhas), encoding="utf-8")
    (repo / "estavel.txt").write_text("sem mudanca\n", encoding="utf-8")

    ref = review_evidence.capturar_ref(repo)

    linhas[200] = "linha-200-editada\n"
    (repo / "grande.txt").write_text("".join(linhas), encoding="utf-8")

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
    assert tocados == ["grande.txt"]

    trechos = review_evidence.montar_trechos(repo, ["grande.txt"], 4000, desde=ref)
    texto = trechos["grande.txt"]["texto"]
    assert "+linha-200-editada" in texto
    assert "-linha-200" in texto
    assert "linha-399" not in texto
    assert trechos["grande.txt"]["truncado"] is False


def test_tf_trecho_desde_sem_alteracao_nao_despeja_o_arquivo(tmp_path):
    """TF da TK-78c: com `desde=<snap>`, um arquivo-alvo sem alteração desde o instantâneo não
    despeja o conteúdo integral — o texto é exatamente a linha `(sem alteração desde <snap>)`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "a.md").write_text("linha-base\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "a.md baseline"], repo)

    (repo / "a.md").write_text("linha-base\nlinha-velha\n", encoding="utf-8")
    snap = _run_git(["stash", "create"], repo).strip()

    trechos = review_evidence.montar_trechos(repo, ["a.md"], 4000, desde=snap)

    assert trechos["a.md"]["texto"] == f"(sem alteração desde `{snap}`)"


def test_tf_diff_stat_desde_recorta_como_os_tocados(tmp_path):
    """TF da AF-T1 (`TK-94a`): com `desde=<ref>`, o bloco `## Diff` de `montar_documento` resume
    só o recorte que `coletar_arquivos_tocados(..., desde=ref)` já dá para a `## Arquivos
    tocados` — a entrega, rastreada e não rastreada —, nunca o trabalho alheio já embutido na
    árvore de `<ref>` (a regra antiga, `git diff HEAD --stat`, citaria o alheio e não citaria o
    não rastreado)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `src/c.py` e cria `src/novo.py`.")

    (repo / "src" / "c.py").write_text("def c():\n    return 1\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "add c.py"], repo)

    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")
    ref = review_evidence.capturar_ref(repo)

    (repo / "src" / "c.py").write_text("def c():\n    return 2\n", encoding="utf-8")
    (repo / "src" / "novo.py").write_text("def novo():\n    return 3\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    bloco = documento.split("## Diff (`git diff --stat`)")[1].split("## Arquivos tocados")[0]
    assert "src/c.py" in bloco
    assert "src/novo.py" in bloco
    assert "src/b.py" not in bloco


def test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas(tmp_path):
    """TR da AF-T1: `<ref>` capturado e nada mudado depois — `coletar_diff_stat(repo, desde=ref)`
    devolve string vazia (nunca roda `git diff --stat` sem caminho, que devolveria a árvore
    inteira), e o bloco `## Diff` do documento traz `(sem diferenças)`, mesma convenção do diff
    vazio sem `--desde`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `src/b.py`.")

    ref = review_evidence.capturar_ref(repo)

    assert review_evidence.coletar_diff_stat(repo, desde=ref) == ""

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )
    bloco = documento.split("## Diff (`git diff --stat`)")[1].split("## Arquivos tocados")[0]
    assert "(sem diferenças)" in bloco


def test_tr_diff_stat_desde_tocados_vazio_com_arvore_diferente_nao_resume_a_arvore(
    tmp_path, monkeypatch
):
    """TR (`AE-3` do `P-0753`): a árvore difere de `<ref>` e o recorte de tocados sai vazio —
    `coletar_diff_stat` devolve string vazia. É o caso que discrimina a guarda "tocados vazio não
    roda `git diff --stat` sem caminho": sem ela, `git diff --stat <ref> <árvore> --` resumiria a
    árvore inteira (aqui, `src/b.py`); o TR acima (árvore igual a `<ref>`) sai vazio com ou sem a
    guarda."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)
    (repo / "src" / "b.py").write_text("def b():\n    return 7\n", encoding="utf-8")
    monkeypatch.setattr(review_evidence, "coletar_arquivos_tocados", lambda root, desde=None: [])

    assert review_evidence.coletar_diff_stat(repo, desde=ref) == ""


# --- FPU-T5 (DFP-17): o executor devolve a medida como arquivo, e a evidência a incorpora -------


def test_tf_evidencia_incorpora_medida(tmp_path, capsys):
    """`main` com `--out` deriva `<dir da evidência>` do pai de `--out`; quando
    `<plano>-<ID>-medida.json` existe ali (`plano` sem id de plano → `stem`), a evidência gravada
    incorpora `## Medida do executor` com a tabela do JSON."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE

    pasta_ev = tmp_path / "ev"
    pasta_ev.mkdir()
    medida = {
        "plano": str(plano),
        "tarefa": "T1",
        "mundo": "antes",
        "gerado_em": "2026-09-26T00:00:00+00:00",
        "itens": [
            {"indice": 1, "comando": "python -c \"print('a')\"", "exit": 0, "saida": "a", "bate": True}
        ],
    }
    (pasta_ev / "plano-T1-medida.json").write_text(
        json.dumps(medida, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    destino_out = pasta_ev / "plano-T1.md"

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--out", str(destino_out)]
    )
    capsys.readouterr()

    assert codigo == 0
    conteudo = destino_out.read_text(encoding="utf-8")
    assert "## Medida do executor" in conteudo
    assert '| 1 | `python -c "print(\'a\')"` | 0 | true |' in conteudo


def test_tr_evidencia_sem_medida_diz_ausente(tmp_path):
    """Regressão: sem o JSON de medida no `<dir da evidência>` derivado, a seção `## Medida do
    executor` diz `ausente`, nunca inventa nem lança exceção."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "## Medida do executor" in documento
    assert "ausente" in documento


def test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca(tmp_path):
    """TF da AUF-T1: arquivo novo (não rastreado, ausente do `<ref>` capturado antes dele existir)
    chega ao revisor como diferença — diff unificado contra o vazio, com as linhas marcadas `+` —
    e não como o conteúdo integral do arquivo."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    ref = review_evidence.capturar_ref(repo)

    (repo / "novo.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")

    trechos = review_evidence.montar_trechos(repo, ["novo.md"], 4000, desde=ref)
    texto = trechos["novo.md"]["texto"]

    assert "+linha-1" in texto
    assert "+linha-2" in texto


def test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral(tmp_path):
    """Regressão: sem `ref`/`desde`, o mesmo arquivo novo continua chegando como conteúdo
    integral (comportamento antigo, preservado no caminho sem recorte)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    (repo / "novo.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")

    trechos = review_evidence.montar_trechos(repo, ["novo.md"], 4000)
    texto = trechos["novo.md"]["texto"]

    assert "linha-1\nlinha-2\n" in texto
    assert "+linha-1" not in texto


def test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente(tmp_path):
    """AUF-T2, reescrito pela RAF-T10 (`R-31`): com `core.quotepath` ligado, o `git status` sem `-z`
    devolveria o caminho acentuado entre aspas com escape octal; com `-z` (`_entradas_status`) o
    caminho chega cru, e o não rastreado criado depois do `ref` entra nos tocados como `ação.txt`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    _run_git(["config", "core.quotepath", "true"], repo)

    ref = review_evidence.capturar_ref(repo)

    (repo / "ação.txt").write_text("linha-1\n", encoding="utf-8")

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)

    assert tocados == ["ação.txt"]


def test_tf_alvo_com_curinga_casa_os_tocados(tmp_path):
    """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `_casa_curinga` (RAF-T9), cada
    tocado que bate com o padrão — não a regra antiga, que descartava o literal e dava os dois
    arquivos como fora dos alvos com uma entrada só sob a chave do padrão."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    (repo / "relatorios").mkdir()
    (repo / "relatorios" / "a.md").write_text("linha-a\n", encoding="utf-8")
    (repo / "relatorios" / "b.md").write_text("linha-b\n", encoding="utf-8")

    alvos = review_evidence.extrair_arquivos_alvo({"arquivos-alvo": "- `relatorios/*.md`"})
    assert alvos == ["relatorios/*.md"]

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
    trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)

    assert set(trechos.keys()) == {"relatorios/a.md", "relatorios/b.md"}
    assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == []


def test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa(tmp_path):
    """Regressão: alvo com curinga sem nenhum tocado que case ganha uma entrada só, com a chave
    igual ao próprio alvo, sem truncamento e com o texto fixo de aviso."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    trechos = review_evidence.montar_trechos(repo, ["relatorios/*.md"], 4000, [], desde=ref)

    assert trechos == {
        "relatorios/*.md": {
            "texto": "(nenhum arquivo tocado casa com o curinga)",
            "truncado": False,
        }
    }


def test_tf_alvo_nao_rastreado_sem_antes_sai_marcado_como_novo(tmp_path):
    """AUF-T3: arquivo não rastreado criado depois do `<ref>` abre com a linha de marca antes do
    diff (com `desde`, marca de `<ref>`; sem `desde`, marca de `HEAD`)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    (repo / "novo.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")

    texto_com_desde = review_evidence.montar_trechos(repo, ["novo.md"], 4000, desde=ref)["novo.md"][
        "texto"
    ]
    texto_sem_desde = review_evidence.montar_trechos(repo, ["novo.md"], 4000)["novo.md"]["texto"]

    assert texto_com_desde.startswith(f"(arquivo novo — ausente em `{ref}`)\n")
    assert texto_sem_desde.startswith("(arquivo novo — ausente em `HEAD`)\n")


def test_tr_alvo_rastreado_alterado_nao_leva_a_marca_de_novo(tmp_path):
    """Regressão: arquivo rastreado alterado depois do `<ref>` continua trazendo a linha `+` de
    sempre, sem a marca de arquivo novo."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    (repo / "src" / "b.py").write_text("def b():\n    return 2\n", encoding="utf-8")

    texto = review_evidence.montar_trechos(repo, ["src/b.py"], 4000, desde=ref)["src/b.py"]["texto"]

    assert "+    return 2" in texto
    assert "(arquivo novo" not in texto


def test_tf_escrita_da_conducao_vence_o_alvo_de_outra_tarefa(tmp_path):
    """AUF-T4 (`DAU-17`, `H-18` §2.1, `F-9`, `F-13`): tocado que é registro da orquestração
    (`docs/DIARIO_DE_OBRAS.md`) e também está mapeado como alvo de outra tarefa do mesmo plano
    vai para `registro_orquestracao`, não para `de_outra_tarefa` — a nova precedência testa
    `_eh_registro_orquestracao` antes de `_tarefa_dona`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    escopo = review_evidence.confrontar_escopo(
        ["docs/DIARIO_DE_OBRAS.md"],
        ["src/b.py"],
        repo,
        {"docs/DIARIO_DE_OBRAS.md": "TK-1a"},
    )

    assert escopo["registro_orquestracao"] == ["docs/DIARIO_DE_OBRAS.md"]
    assert escopo["de_outra_tarefa"] == {}


def test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido(tmp_path):
    """Regressão: tocado que não é registro da orquestração e está mapeado como alvo de outra
    tarefa do mesmo plano continua saindo em `de_outra_tarefa`, sem cair em `registro_orquestracao`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    escopo = review_evidence.confrontar_escopo(
        ["src/c.py"],
        ["src/b.py"],
        repo,
        {"src/c.py": "TK-1a"},
    )

    assert escopo["de_outra_tarefa"] == {"src/c.py": "TK-1a"}
    assert escopo["registro_orquestracao"] == []


def _repo_com_versionado_ignorado(tmp_path: Path) -> Path:
    """Repositório de `_init_repo_com_baseline` com um arquivo já versionado que o `.gitignore`
    também cobre (`AUF-T5`): `.gitignore` reescrito com `__pycache__/` e `versionado.log`,
    `versionado.log` criado com `v1`, adicionado com `git add -f` e commitado junto do
    `.gitignore`."""
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / ".gitignore").write_text("__pycache__/\nversionado.log\n", encoding="utf-8")
    (repo / "versionado.log").write_text("v1", encoding="utf-8")
    _run_git(["add", "-f", ".gitignore", "versionado.log"], repo)
    _run_git(["commit", "-m", "versionado ignorado"], repo)
    return repo


def test_tf_capturar_ref_inclui_versionado_que_o_gitignore_cobre(tmp_path):
    """AUF-T5 (`DAU-18`, `DAU-25`, `H-19` §2.1): arquivo já versionado que o `.gitignore` também
    cobre entra na árvore de `<ref>` como qualquer outro rastreado — a regra antiga (`git add -A`
    sozinho, num índice recém-criado vazio) deixava esse arquivo fora da árvore gravada, porque
    `git add -A` respeita `.gitignore` e não vê um rastreado ignorado sem o índice já o conhecer."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_versionado_ignorado(tmp_path)

    (repo / "versionado.log").write_text("v2", encoding="utf-8")

    ref = review_evidence.capturar_ref(repo)

    resultado = subprocess.run(
        ["git", "show", f"{ref}:versionado.log"], cwd=str(repo), capture_output=True, text=True
    )
    assert resultado.returncode == 0
    assert resultado.stdout == "v2"


def test_tf_versionado_ignorado_intocado_fica_fora_dos_tocados_e_alterado_entra(tmp_path):
    """AUF-T5 (`DAU-18`, `DAU-25`, `F-13`, `F-14`): com `<ref>` gravando o versionado ignorado
    (teste anterior), o arquivo intocado desde `<ref>` não aparece mais em
    `coletar_arquivos_tocados` nem em `coletar_diff_stat` — a regra antiga, por não ter o arquivo
    em `<ref>`, o enxergava sempre como apagado/tocado."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_versionado_ignorado(tmp_path)

    ref = review_evidence.capturar_ref(repo)

    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == []

    (repo / "versionado.log").write_text("v3", encoding="utf-8")

    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["versionado.log"]
    assert "versionado.log" in review_evidence.coletar_diff_stat(repo, desde=ref)


def test_tf_nao_rastreado_binario_intocado_fica_fora_dos_tocados(tmp_path):
    """AUF-T6 (`DAU-19`, `H-20` §2.1, `F-13`): não rastreado binário já presente na árvore de
    `<ref>` — o julgamento por conteúdo cai para os bytes brutos quando o arquivo não se lê como
    texto UTF-8; intocado desde `<ref>`, ele não entra em `coletar_arquivos_tocados` (a regra
    antiga, por dar `_texto_do_disco` como `None` e tratar isso como "mudou", devolvia
    `["imagem.bin"]`)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))

    ref = review_evidence.capturar_ref(repo)

    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == []


def test_tr_nao_rastreado_binario_alterado_entra_nos_tocados(tmp_path):
    """AUF-T6 (`DAU-19`, `H-20` §2.1, `F-13`): o mesmo não rastreado binário, regravado com bytes
    diferentes depois de `<ref>`, entra em `coletar_arquivos_tocados` — trava o comportamento
    novo contra regressão para a regra antiga (que sempre devolvia o binário como tocado, mudado
    ou não)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))

    ref = review_evidence.capturar_ref(repo)

    (repo / "imagem.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x82]))

    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["imagem.bin"]


# --- RAF-T7 (R-13, AE-105/AE-106 do P-0754): o dossiê chega ao fim nos três casos em que quebrava


def _plano_em_pasta_com_medida(repo: Path, exit_medido: int) -> Path:
    """Plano em layout de pasta (`docs/plans/P-0999-teste/plano.md`) dentro do repositório de
    fixture, com a medida do executor já gravada em `evidencia/` ao lado dele (`P-0999-T1-medida.json`,
    no molde de `test_tf_evidencia_incorpora_medida`)."""
    pasta_plano = repo / "docs" / "plans" / "P-0999-teste"
    pasta_plano.mkdir(parents=True, exist_ok=True)
    plano = pasta_plano / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")
    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
    pasta_evidencia = pasta_plano / "evidencia"
    pasta_evidencia.mkdir(parents=True, exist_ok=True)
    medida = {
        "plano": str(plano),
        "tarefa": "T1",
        "mundo": "antes",
        "gerado_em": "2026-09-26T00:00:00+00:00",
        "itens": [
            {
                "indice": 1,
                "comando": "python -c \"print('a')\"",
                "exit": exit_medido,
                "saida": "a",
                "bate": True,
            }
        ],
    }
    (pasta_evidencia / "P-0999-T1-medida.json").write_text(
        json.dumps(medida, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return plano


def test_tf_quebra_ref_binario_hoje_texto_compara_bytes(tmp_path):
    """RAF-T7 (R-13): não rastreado binário no `<ref>`, regravado depois como texto — o julgamento
    por conteúdo cai para os bytes brutos (que divergem) e o trecho relatado nomeia o binário/
    não-UTF-8 em vez de deixar a leitura em texto do `<ref>` lançar exceção."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "dados.txt").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))

    ref = review_evidence.capturar_ref(repo)

    (repo / "dados.txt").write_text("ola", encoding="utf-8")

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
    assert tocados == ["dados.txt"]

    trechos = review_evidence.montar_trechos(repo, ["dados.txt"], 4000, tocados, desde=ref)
    assert trechos["dados.txt"]["texto"] == "(arquivo binário ou não-UTF-8 — trecho omitido)"


def test_tr_quebra_ref_texto_segue_por_linha(tmp_path):
    """Regressão: não rastreado texto no `<ref>` (quebra `\\n`), regravado com `\\r\\n` — a
    comparação por linha (`str.splitlines`) segue vencendo quando os dois lados decodificam como
    UTF-8, mesmo com bytes brutos diferentes (uma regra que comparasse sempre os bytes daria
    `["dados.txt"]`)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "dados.txt").write_text("ola\n", encoding="utf-8")

    ref = review_evidence.capturar_ref(repo)

    (repo / "dados.txt").write_bytes(b"ola\r\n")

    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == []


def test_tf_quebra_atribuir_sem_rdo_falha_nomeado(tmp_path, capsys):
    """RAF-T7 (R-13): `--atribuir` com `--root` sem `.claude/tools/rdo.py` falha nomeada pelo
    canal do módulo (`review_evidence: FALHOU - rdo.py: módulo não encontrado em`), em vez de
    deixar a exceção escapar sem essa linha."""
    review_evidence = _load_review_evidence()
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(tmp_path), "--atribuir"]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "review_evidence: FALHOU - rdo.py: módulo não encontrado em" in saida.err


def test_tf_quebra_out_fora_acha_medida_na_pasta_do_plano(tmp_path, capsys):
    """RAF-T7 (R-13): plano em layout de pasta com a medida gravada em `evidencia/` dele — com
    `--out` fora da pasta do plano (sem medida ao lado), `montar_documento` também acha a medida na
    pasta do plano em vez de relatar `ausente`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE
    plano = _plano_em_pasta_com_medida(repo, 7)
    destino_out = tmp_path / "fora" / "T1.md"

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--out", str(destino_out)]
    )
    capsys.readouterr()

    assert codigo == 0
    conteudo = destino_out.read_text(encoding="utf-8")
    assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' in conteudo


def test_tr_quebra_out_com_medida_ao_lado_usa_a_do_lado(tmp_path, capsys):
    """Regressão: com uma medida também ao lado do `--out`, ela continua vencendo sobre a
    encontrada na pasta do plano."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE
    plano = _plano_em_pasta_com_medida(repo, 7)
    pasta_fora = tmp_path / "fora"
    pasta_fora.mkdir()
    medida_ao_lado = {
        "plano": str(plano),
        "tarefa": "T1",
        "mundo": "antes",
        "gerado_em": "2026-09-26T00:00:00+00:00",
        "itens": [
            {
                "indice": 1,
                "comando": "python -c \"print('a')\"",
                "exit": 3,
                "saida": "a",
                "bate": True,
            }
        ],
    }
    (pasta_fora / "P-0999-T1-medida.json").write_text(
        json.dumps(medida_ao_lado, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    destino_out = pasta_fora / "T1.md"

    codigo = review_evidence.main(
        ["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--out", str(destino_out)]
    )
    capsys.readouterr()

    assert codigo == 0
    conteudo = destino_out.read_text(encoding="utf-8")
    assert '| 1 | `python -c "print(\'a\')"` | 3 | true |' in conteudo
    assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' not in conteudo


# --- RAF-T8 (R-14, AE-135 do P-0755): a marca de arquivo novo abre também o retorno binário, e o
# registro da orquestração leva o mesmo nome na lista e no resumo


def test_tf_marca_e_rotulo_binario_novo_abre_com_a_marca(tmp_path):
    """TF do RAF-T8 (R-14): `img.bin` não rastreado, criado depois do `<ref>` — a marca `(arquivo
    novo — ausente em ...)` que hoje só abre o diff de texto passa a abrir também o retorno do
    arquivo que não se lê como texto, seguida de `(arquivo binário ou não-UTF-8 — trecho
    omitido)` (hoje os dois retornos são só a linha do binário, sem marca)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    ref = review_evidence.capturar_ref(repo)

    (repo / "img.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))

    assert review_evidence._diff_para_arquivo(repo, "img.bin", desde=ref) == (
        f"(arquivo novo — ausente em `{ref}`)\n"
        "(arquivo binário ou não-UTF-8 — trecho omitido)"
    )
    assert review_evidence._diff_para_arquivo(repo, "img.bin") == (
        "(arquivo novo — ausente em `HEAD`)\n"
        "(arquivo binário ou não-UTF-8 — trecho omitido)"
    )


def test_tr_marca_e_rotulo_binario_rastreado_alterado_sem_marca(tmp_path):
    """Regressão do RAF-T8: `img.bin` rastreado (existe no `<ref>`) e alterado depois dele — o
    retorno com `desde=ref` não ganha a marca de arquivo novo; ela é exclusiva do não rastreado."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "img.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x81]))
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "img.bin"], repo)

    ref = review_evidence.capturar_ref(repo)

    (repo / "img.bin").write_bytes(bytes([0xFF, 0xFE, 0x00, 0x82]))

    assert "(arquivo novo" not in review_evidence._diff_para_arquivo(repo, "img.bin", desde=ref)


def test_tf_marca_e_rotulo_registro_da_orquestracao_na_lista(tmp_path):
    """TF do RAF-T8 (R-14, `F-17`): `docs/DIARIO_DE_OBRAS.md` (balde `registro_orquestracao`) e
    `docs/nota.txt` (balde `fora_dos_alvos`) não rastreados, fora dos `Arquivos-alvo` — a seção
    `## Arquivos tocados` passa a nomear o balde do primeiro em vez do genérico `alheio` que hoje
    os dois recebem, igualando o rótulo ao da seção `## Escopo` (`Registro da orquestração`)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "cria `src/a.py`.")

    (repo / "src" / "a.py").write_text("def a():\n    return 1\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text("kanban\n", encoding="utf-8")
    (repo / "docs" / "nota.txt").write_text("fora do escopo\n", encoding="utf-8")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert (
        "- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: `??`"
        in documento
    )
    assert "- `docs/nota.txt` — atribuição: alheio; estado git: `??`" in documento


def test_tf_glob_estrela_nao_atravessa_pasta(tmp_path):
    """RAF-T9 (`DRF-31`): a estrela simples do curinga do alvo casa como na linha de comando —
    presa a uma pasta. `relatorios/*.md` cobre `relatorios/a.md`, mas não `relatorios/sub/x.md`
    (hoje o `fnmatch` casa os dois, porque `*` também atravessa `/`)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    (repo / "relatorios").mkdir()
    (repo / "relatorios" / "sub").mkdir()
    (repo / "relatorios" / "a.md").write_text("linha-a\n", encoding="utf-8")
    (repo / "relatorios" / "sub" / "x.md").write_text("linha-x\n", encoding="utf-8")

    alvos = ["relatorios/*.md"]
    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)

    assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == [
        "relatorios/sub/x.md"
    ]
    trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)
    assert set(trechos.keys()) == {"relatorios/a.md"}


def test_tf_glob_estrela_dupla_alcanca_subpastas(tmp_path):
    """RAF-T9 (`DRF-31`): a estrela dupla do curinga do alvo alcança as subpastas, como na linha
    de comando. `relatorios/**/*.md` cobre `relatorios/a.md` e `relatorios/sub/x.md` (hoje o
    `fnmatch` deixa `relatorios/a.md` de fora, porque exige uma `/` depois de `relatorios/`)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    (repo / "relatorios").mkdir()
    (repo / "relatorios" / "sub").mkdir()
    (repo / "relatorios" / "a.md").write_text("linha-a\n", encoding="utf-8")
    (repo / "relatorios" / "sub" / "x.md").write_text("linha-x\n", encoding="utf-8")

    alvos = ["relatorios/**/*.md"]
    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)

    assert review_evidence.confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"] == []
    trechos = review_evidence.montar_trechos(repo, alvos, 4000, tocados, desde=ref)
    assert set(trechos.keys()) == {"relatorios/a.md", "relatorios/sub/x.md"}


def test_tf_acento_z_nao_rastreado_chega_com_o_diff(tmp_path):
    """RAF-T10 (`DRF-32`, `R-31`): com `core.quotepath` ligado, `_entradas_status` (via `-z`) lê o
    caminho acentuado cru — hoje (sem `-z`) o caminho chega em escape octal e o trecho sai
    `arquivo ausente`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    _run_git(["config", "core.quotepath", "true"], repo)

    ref = review_evidence.capturar_ref(repo)

    (repo / "ação.txt").write_text("linha-1\n", encoding="utf-8")

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
    assert tocados == ["ação.txt"]

    trechos = review_evidence.montar_trechos(repo, ["ação.txt"], 4000, tocados, desde=ref)
    assert "+linha-1" in trechos["ação.txt"]["texto"]

    assert review_evidence.coletar_estado_git(repo)["ação.txt"] == "??"


def test_tr_acento_z_renomeado_usa_o_caminho_novo(tmp_path):
    """Regressão: renomeação (`git mv`) usa o caminho novo como chave — a origem, consumida como
    o campo seguinte ao código `R` por `_entradas_status`, nunca vira entrada própria."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)

    _run_git(["mv", "src/b.py", "src/c.py"], repo)

    estados = review_evidence.coletar_estado_git(repo)
    assert estados["src/c.py"] == "R "
    assert "src/b.py" not in estados

    assert review_evidence.coletar_arquivos_tocados(repo) == ["src/c.py"]


def test_tf_acento_diff_commitado_chega_com_um_nome_so(tmp_path):
    """RAF-T10a (`DRF-52`; `AE-142`-`AE-145` da `RAF-T10`): com `core.quotepath` ligado, o arquivo
    acentuado já rastreado e alterado **depois** do `ref` (só `git diff` o vê, árvore de trabalho
    limpa) chega com um nome só nos tocados, no estado, no resumo e no cabeçalho do trecho — hoje
    (`git diff <ref> --name-only`/`--name-status` sem `-z`, `--stat` e diff unificado sem
    `-c core.quotepath=false`) ele chega em escape octal."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    _run_git(["config", "core.quotepath", "true"], repo)

    (repo / "ação.md").write_text("linha-1\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "adiciona ação.md"], repo)

    ref = review_evidence.capturar_ref(repo)

    (repo / "ação.md").write_text("linha-1\nlinha-2\n", encoding="utf-8")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "altera ação.md"], repo)

    tocados = review_evidence.coletar_arquivos_tocados(repo, desde=ref)
    assert tocados == ["ação.md"]

    assert review_evidence.coletar_estado_git(repo, desde=ref) == {
        "ação.md": f"M (commitado desde {ref})"
    }

    trecho = review_evidence.montar_trechos(repo, ["ação.md"], 4000, tocados, desde=ref)["ação.md"][
        "texto"
    ]
    resumo = review_evidence.coletar_diff_stat(repo, desde=ref)

    assert "+linha-2" in trecho
    assert r"\303" not in trecho
    assert r"\303" not in resumo
    assert "ação.md" in resumo


def test_tf_acento_alvo_acentuado_e_caminho(tmp_path):
    """RAF-T10a (`DRF-52`; `AE-144` da `RAF-T10`): `_CAMINHO_RE` aceita letra acentuada —
    `docs/ação.md` declarado em `Arquivos-alvo` vira alvo reconhecido, não literal descartado
    (hoje `_CAMINHO_RE` é ASCII-only e o descarta)."""
    review_evidence = _load_review_evidence()
    campos = {"arquivos-alvo": "- `docs/ação.md`"}

    assert review_evidence.extrair_arquivos_alvo(campos) == ["docs/ação.md"]
    assert review_evidence.extrair_literais_nao_caminho(campos) == []


def test_tr_acento_diff_renomeado_commitado_usa_o_caminho_novo(tmp_path):
    """Regressão: renomeação commitada depois do `ref` usa o caminho novo como chave em
    `coletar_estado_git` e em `coletar_arquivos_tocados` — a origem, consumida como o segundo
    campo da letra `R`/`C` por `_entradas_diff`, nunca vira entrada própria (a regra concorrente
    que tratasse a origem como entrada daria `src/b.py` também)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    ref = review_evidence.capturar_ref(repo)

    _run_git(["mv", "src/b.py", "src/c.py"], repo)
    _run_git(["commit", "-m", "renomeia src/b.py"], repo)

    assert review_evidence.coletar_estado_git(repo, desde=ref) == {
        "src/c.py": f"R100 (commitado desde {ref})"
    }
    assert review_evidence.coletar_arquivos_tocados(repo, desde=ref) == ["src/c.py"]


# --- RAF-T11 (DRF-33; F-17, F-18; R-12 do P-0754, AE-97/AE-98): a evidência mostra as linhas que
# a entrega tirou dos testes -----------------------------------------------------------------


def _repo_com_teste_versionado(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    (repo / "tests").mkdir(parents=True, exist_ok=True)
    (repo / "tests" / "test_a.py").write_text(
        "def test_a():\n    assert 1 == 1\n    assert 2 == 2\n", encoding="utf-8"
    )
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "adiciona tests/test_a.py"], repo)
    return repo


def test_tf_removidas_de_teste_aparecem_na_evidencia(tmp_path):
    """RAF-T11 (`DRF-33`; `F-17`, `F-18`; `R-12` do `P-0754`, `AE-97`/`AE-98`): a remoção de uma
    asserção vizinha, que hoje passa verde sem aparecer em lugar nenhum do dossiê, chega como
    seção própria mostrando a linha exata que saiu do teste."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_teste_versionado(tmp_path)
    ref = review_evidence.capturar_ref(repo)

    (repo / "tests" / "test_a.py").write_text(
        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
    )

    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `tests/test_a.py`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "## Linhas removidas dos testes" in documento
    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in documento
    assert "-    assert 2 == 2" in documento


def test_tr_removidas_de_teste_so_acrescimo_diz_nenhuma(tmp_path):
    """Regressão: arquivo de teste que só ganha linha (nenhuma remoção) diz 'nenhuma linha
    removida' — e um alvo que não é arquivo de teste (`src/b.py`) não ganha entrada na seção; a
    regra concorrente que listasse todo alvo daria uma entrada para ele também."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_teste_versionado(tmp_path)
    ref = review_evidence.capturar_ref(repo)

    with (repo / "tests" / "test_a.py").open("a", encoding="utf-8") as arquivo:
        arquivo.write("    assert 3 == 3\n")

    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `tests/test_a.py` e `src/b.py`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    secao = documento.split("## Linhas removidas dos testes", 1)[1]
    secao = secao.split("## Medida do executor", 1)[0]
    assert "### `tests/test_a.py` — nenhuma linha removida" in secao
    assert "src/b.py" not in secao


def test_tr_removidas_de_teste_sem_alvo_de_teste(tmp_path):
    """Regressão: nenhum alvo de arquivo de teste na declaração — a seção diz o fato em vez de
    ficar vazia ou listar arquivo que não é teste."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `src/b.py`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert "- nenhum arquivo de teste entre os alvos" in documento


# --- RAF-T11a (DRF-53; AE-149 da RAF-T11): a seção cobre o teste sob curinga ou diretório e a
# linha removida que começa por dois hífens --------------------------------------------------


def _secao_removidas(documento: str) -> str:
    secao = documento.split("## Linhas removidas dos testes", 1)[1]
    return secao.split("## Medida do executor", 1)[0]


def test_tf_removidas_de_teste_curinga_cobre_teste_tocado(tmp_path):
    """RAF-T11a (`DRF-53`; `AE-149`): alvo curinga (`tests/test_*.py`) cobre o arquivo de teste
    tocado que casa por `_casa_curinga` — hoje o curinga é pulado e a seção diz que nenhum arquivo
    de teste está entre os alvos, apagando a remoção."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_teste_versionado(tmp_path)
    ref = review_evidence.capturar_ref(repo)

    (repo / "tests" / "test_a.py").write_text(
        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
    )

    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `tests/test_*.py`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    secao = _secao_removidas(documento)
    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in secao
    assert "-    assert 2 == 2" in secao
    assert "- nenhum arquivo de teste entre os alvos" not in secao


def test_tf_removidas_de_teste_diretorio_cobre_teste_tocado(tmp_path):
    """RAF-T11a (`DRF-53`; `AE-149`): alvo diretório (`tests/`) cobre o arquivo de teste tocado
    sob o prefixo — hoje o diretório não é arquivo de teste e é pulado."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_teste_versionado(tmp_path)
    ref = review_evidence.capturar_ref(repo)

    (repo / "tests" / "test_a.py").write_text(
        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
    )

    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `tests/`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    secao = _secao_removidas(documento)
    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in secao
    assert "-    assert 2 == 2" in secao
    assert "- nenhum arquivo de teste entre os alvos" not in secao


def test_tf_removidas_de_teste_linha_que_comeca_por_dois_hifens(tmp_path):
    """RAF-T11a (`DRF-53`; `AE-149`): linha removida cujo conteúdo começa por `--` não pode sumir
    atrás do filtro de cabeçalho `---` — hoje o filtro de `---` a apaga junto com o cabeçalho e a
    seção diz 'nenhuma linha removida'."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_teste_versionado(tmp_path)
    with (repo / "tests" / "test_a.py").open("a", encoding="utf-8") as arquivo:
        arquivo.write("--sep--\n")
    _run_git(["add", "-A"], repo)
    _run_git(["commit", "-m", "acrescenta linha de dois hifens"], repo)
    ref = review_evidence.capturar_ref(repo)

    conteudo = (repo / "tests" / "test_a.py").read_text(encoding="utf-8")
    (repo / "tests" / "test_a.py").write_text(
        conteudo.replace("--sep--\n", ""), encoding="utf-8"
    )

    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `tests/test_a.py`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    secao = _secao_removidas(documento)
    assert "### `tests/test_a.py` — 1 linha(s) removida(s)" in secao
    assert "---sep--" in secao


def test_tr_removidas_de_teste_alvo_e_curinga_uma_entrada(tmp_path):
    """Regressão: alvo exato e alvo curinga que cobrem o mesmo arquivo de teste não duplicam a
    entrada — a regra concorrente que expandisse o curinga sem conferir as chaves já postas daria
    duas ocorrências de `### \\`tests/test_a.py\\``."""
    review_evidence = _load_review_evidence()
    repo = _repo_com_teste_versionado(tmp_path)
    ref = review_evidence.capturar_ref(repo)

    (repo / "tests" / "test_a.py").write_text(
        "def test_a():\n    assert 1 == 1\n", encoding="utf-8"
    )

    plano = tmp_path / "plano.md"
    _escrever_plano(plano, "edita `tests/test_a.py` e `tests/test_*.py`.")

    documento = review_evidence.montar_documento(
        plano, "T1", repo, desde=ref, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    secao = _secao_removidas(documento)
    assert secao.count("### `tests/test_a.py`") == 1


# --- RAF-T15 (R-05): a medida gravada fica na pasta do plano da árvore medida, com o mundo no nome


def _gravar_medida(caminho: Path, exit_medido: int) -> None:
    """Grava uma medida no molde de `_plano_em_pasta_com_medida` (RAF-T7) em `caminho` (RAF-T15),
    mesmo formato de item, variando só o destino e o `exit`."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    medida = {
        "plano": str(caminho),
        "tarefa": "T1",
        "mundo": "antes",
        "gerado_em": "2026-09-26T00:00:00+00:00",
        "itens": [
            {
                "indice": 1,
                "comando": "python -c \"print('a')\"",
                "exit": exit_medido,
                "saida": "a",
                "bate": True,
            }
        ],
    }
    caminho.write_text(json.dumps(medida, ensure_ascii=False, indent=2), encoding="utf-8")


def test_tf_medida_com_mundo_lida_na_ordem(tmp_path):
    """`RAF-T15` (`R-05`) — sem medida com mundo, `montar_documento` lê a sem mundo (`exit 7`,
    gravada por `_plano_em_pasta_com_medida`); gravando também `-medida-antes.json` (`exit 5`), a
    leitura passa a essa; gravando também `-medida-depois.json` (`exit 6`), a leitura passa a
    essa — a de depois vence sobre a de antes, que vence sobre a sem mundo (hoje sempre lia a
    sem mundo, `exit 7`, nos três casos)."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = _plano_em_pasta_com_medida(repo, 7)
    pasta_evidencia = plano.parent / "evidencia"

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )
    assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' in documento

    _gravar_medida(pasta_evidencia / "P-0999-T1-medida-antes.json", 5)
    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )
    assert '| 1 | `python -c "print(\'a\')"` | 5 | true |' in documento

    _gravar_medida(pasta_evidencia / "P-0999-T1-medida-depois.json", 6)
    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )
    assert '| 1 | `python -c "print(\'a\')"` | 6 | true |' in documento


def test_tr_medida_com_mundo_sem_mundo_ainda_lida(tmp_path):
    """Regressão: só a medida sem mundo (formato das vinte já gravadas do `P-0753`) continua lida
    quando não há `-medida-antes.json` nem `-medida-depois.json`."""
    review_evidence = _load_review_evidence()
    repo = tmp_path / "repo"
    _init_repo_com_baseline(repo)
    plano = _plano_em_pasta_com_medida(repo, 7)

    documento = review_evidence.montar_documento(
        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
    )

    assert '| 1 | `python -c "print(\'a\')"` | 7 | true |' in documento
