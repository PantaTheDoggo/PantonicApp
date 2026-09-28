"""TK-77a (`docs/DIARIO_DE_OBRAS.md` `### TK-77a`) — TF/TR de `.claude/checks/frontmatter_yaml.py`
e da seção `2b` de `.claude/checks/kit_check.ps1`: o `validate` recusa frontmatter de agente ou
skill que o YAML estrito recusa. Padrão de carga do módulo idêntico a `tests/test_rdo.py`/
`tests/test_review_evidence.py` (`.claude/` não é pacote importável)."""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_FRONTMATTER_YAML_PATH = _ROOT / ".claude" / "checks" / "frontmatter_yaml.py"
_KIT_CHECK_PATH = _ROOT / ".claude" / "checks" / "kit_check.ps1"


def _load_frontmatter_yaml():
    spec = importlib.util.spec_from_file_location("frontmatter_yaml", _FRONTMATTER_YAML_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _pwsh_disponivel() -> bool:
    return shutil.which("pwsh") is not None


def test_frontmatter_com_dois_pontos_extra_gera_um_problema_nomeando_o_arquivo(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\ndescription: A: b\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert len(resultado) == 1
    assert str(caminho) in resultado[0]


def test_frontmatter_com_hifen_no_lugar_dos_dois_pontos_nao_gera_problema(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\ndescription: A - b\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert resultado == []


def test_frontmatter_que_carrega_lista_gera_um_problema(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\n- um\n- dois\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert len(resultado) == 1
    assert "não é mapeamento" in resultado[0]


def test_frontmatter_que_carrega_escalar_gera_um_problema(tmp_path):
    modulo = _load_frontmatter_yaml()
    caminho = tmp_path / "agente.md"
    caminho.write_text("---\napenas um texto solto\n---\ncorpo\n", encoding="utf-8")

    resultado = modulo.problemas([caminho])

    assert len(resultado) == 1
    assert "não é mapeamento" in resultado[0]


def _copiar_kit(tmp_path: Path) -> Path:
    """Cópia de `.claude/` + `VERSION` sob `tmp_path`, ignorando `__pycache__` (mesmo padrão do
    card: `shutil.copytree`)."""
    destino = tmp_path / "cópia"
    shutil.copytree(
        _ROOT / ".claude",
        destino / ".claude",
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    shutil.copy2(_ROOT / "VERSION", destino / "VERSION")
    return destino


def test_kit_check_valida_frontmatter_ponta_a_ponta(tmp_path):
    if not _pwsh_disponivel():
        pytest.skip("pwsh não está no PATH")

    copia = _copiar_kit(tmp_path)

    resultado_ok = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(copia / ".claude" / "checks" / "kit_check.ps1"),
            "-Mode",
            "validate",
            "-KitRoot",
            str(copia / ".claude"),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert resultado_ok.returncode == 0, resultado_ok.stdout + resultado_ok.stderr

    consultor = copia / ".claude" / "agents" / "pantonic-consultant.md"
    conteudo = consultor.read_text(encoding="utf-8")
    conteudo_quebrado = conteudo.replace(
        "Efêmero - cada acionamento", "Efêmero: cada acionamento"
    )
    assert conteudo_quebrado != conteudo
    consultor.write_text(conteudo_quebrado, encoding="utf-8")

    resultado_falho = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(copia / ".claude" / "checks" / "kit_check.ps1"),
            "-Mode",
            "validate",
            "-KitRoot",
            str(copia / ".claude"),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert resultado_falho.returncode != 0
    assert "pantonic-consultant.md" in resultado_falho.stdout + resultado_falho.stderr
