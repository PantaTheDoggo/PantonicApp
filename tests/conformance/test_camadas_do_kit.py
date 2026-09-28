"""Teste de camadas do kit — instrumentos do kit não importam de `tests` nem de
`caminhos` por `import`/`from ... import ...` (`caminhos` é carregado por
`importlib.util.spec_from_file_location`, nunca por `import`).

AF-T15 (`docs/plans/P-0753-auditoria-estagio-1/plano.md`)."""
from __future__ import annotations

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent

MODULOS_PROIBIDOS = {"tests", "caminhos"}


def violacoes_de_camada(arquivos: list[Path]) -> list[str]:
    """Para cada arquivo, faz `ast.parse` e devolve uma linha
    `<arquivo>:<linha> importa <módulo>` para todo `Import`/`ImportFrom` cujo primeiro
    componente do módulo importado é `tests` ou `caminhos`."""
    achados: list[str] = []
    for arquivo in arquivos:
        arvore = ast.parse(arquivo.read_text(encoding="utf-8"), filename=str(arquivo))
        for node in ast.walk(arvore):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    primeiro = alias.name.split(".")[0]
                    if primeiro in MODULOS_PROIBIDOS:
                        achados.append(f"{arquivo}:{node.lineno} importa {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    primeiro = node.module.split(".")[0]
                    if primeiro in MODULOS_PROIBIDOS:
                        achados.append(f"{arquivo}:{node.lineno} importa {node.module}")
    return achados


def test_tf_instrumentos_do_kit_nao_importam_tests_nem_caminhos():
    arquivos = sorted((RAIZ / ".claude" / "tools").glob("*.py")) + sorted(
        (RAIZ / ".claude" / "checks").glob("*.py")
    )
    assert violacoes_de_camada(arquivos) == []


def test_tr_camada_acusa_import_de_tests_e_de_caminhos(tmp_path):
    arquivo = tmp_path / "exemplo.py"
    arquivo.write_text("from tests import x\nimport caminhos\n", encoding="utf-8")
    assert len(violacoes_de_camada([arquivo])) == 2
