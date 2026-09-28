"""EBK-T5 (docs/plans/P-0751-esgotar-backlog.md) — o `kit_check` conta defeito, não linha: uma
divergência de README com N linhas diferentes conta 1 problema em `-Mode check-drift`, e as linhas
`[versionado]`/`[regenerado]` que a detalham continuam impressas sem entrar na contagem. Padrão de
carga/cópia idêntico a `tests/test_frontmatter_yaml.py` (`.claude/` não é pacote importável).

A contagem-base (antes da divergência de README) não é assumida como zero: a cópia sob `tmp_path`
preserva o `settings.json` real do repositório, materializado com caminhos absolutos do repositório
de origem, o que por si só já pode acusar drift de materialização (alvo 'projeto') alheio a esta
tarefa. O teste isola o efeito da divergência de README pela diferença entre a contagem antes e
depois de introduzi-la."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_CONTAGEM_RE = re.compile(r"check-drift FALHOU \((\d+) problema\(s\)\)")
_VALIDATE_CONTAGEM_RE = re.compile(r"kit_check: FALHOU \((\d+) problema\(s\)\)")
_ITEM_RE = re.compile(r"^  - ", re.MULTILINE)


def _pwsh_disponivel() -> bool:
    return shutil.which("pwsh") is not None


def _copiar_kit(tmp_path: Path) -> Path:
    """Cópia de `.claude/` + `VERSION` sob `tmp_path`, ignorando `__pycache__` (mesmo padrão de
    `tests/test_frontmatter_yaml.py::_copiar_kit`)."""
    destino = tmp_path / "cópia"
    shutil.copytree(
        _ROOT / ".claude",
        destino / ".claude",
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    shutil.copy2(_ROOT / "VERSION", destino / "VERSION")
    return destino


def _rodar_check_drift(copia: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(copia / ".claude" / "checks" / "kit_check.ps1"),
            "-Mode",
            "check-drift",
            "-KitRoot",
            str(copia / ".claude"),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _rodar_validate(copia: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
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
        errors="replace",
    )


def test_divergencia_de_readme_conta_um_problema_e_detalha_as_duas_linhas(tmp_path):
    if not _pwsh_disponivel():
        pytest.skip("pwsh não está no PATH")

    copia = _copiar_kit(tmp_path)

    resultado_base = _rodar_check_drift(copia)
    saida_base = resultado_base.stdout + resultado_base.stderr
    match_base = _CONTAGEM_RE.search(saida_base)
    contagem_base = int(match_base.group(1)) if match_base else 0
    assert "README.md diverge do regenerado" not in saida_base, saida_base

    readme = copia / ".claude" / "README.md"
    conteudo = readme.read_text(encoding="utf-8")
    trecho_original = "preservam o contexto dos agentes de planejamento e execução. |"
    trecho_divergente = (
        "preservam o contexto dos agentes de planejamento e execução. Frase extra. |"
    )
    assert trecho_original in conteudo
    readme.write_text(conteudo.replace(trecho_original, trecho_divergente), encoding="utf-8")

    resultado = _rodar_check_drift(copia)
    saida = resultado.stdout + resultado.stderr

    assert resultado.returncode != 0, saida
    assert "README.md diverge do regenerado (2 linha(s) diferente(s)):" in saida, saida
    assert "[versionado]" in saida, saida
    assert "[regenerado]" in saida, saida

    match = _CONTAGEM_RE.search(saida)
    assert match is not None, saida
    contagem = int(match.group(1))
    assert contagem == contagem_base + 1, saida


def test_check_drift_nao_conta_nem_imprime_o_sumario_do_materializar(tmp_path):
    """EBK-T5a — a cópia intacta tem drift de materialização (o `settings.json` copiado aponta
    para o repositório de origem), então `check-drift` falha e a saída traz o item prefixado
    `materializar drift:`; a linha de sumário que o `materializar.py` imprime por último
    (`materializar: FALHOU - ...`) não entra na lista nem é impressa, e o número do cabeçalho é
    igual ao número de linhas de item (`  - `)."""
    if not _pwsh_disponivel():
        pytest.skip("pwsh não está no PATH")

    copia = _copiar_kit(tmp_path)

    resultado = _rodar_check_drift(copia)
    saida = resultado.stdout + resultado.stderr

    assert resultado.returncode != 0, saida
    assert "materializar drift:" in saida, saida
    assert "materializar: FALHOU" not in saida, saida

    match = _CONTAGEM_RE.search(saida)
    assert match is not None, saida
    contagem = int(match.group(1))
    assert len(_ITEM_RE.findall(saida)) == contagem, saida


def test_validate_nao_conta_nem_imprime_o_sumario_do_materializar(tmp_path):
    """EBK-T5a — uma entrada a mais em `arquivos` de um alvo de `projecoes.json`, com `de`
    apontando para um caminho inexistente, faz `materializar check` falhar com 1 problema; a
    linha de sumário do `materializar.py` não entra na lista nem é impressa."""
    if not _pwsh_disponivel():
        pytest.skip("pwsh não está no PATH")

    copia = _copiar_kit(tmp_path)
    projecoes_path = copia / ".claude" / "projecoes.json"
    projecoes = json.loads(projecoes_path.read_text(encoding="utf-8"))
    projecoes["alvos"]["projeto"]["arquivos"].append(
        {"de": "nao/existe.md", "para": "nao/existe.md"}
    )
    projecoes_path.write_text(
        json.dumps(projecoes, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    resultado = _rodar_validate(copia)
    saida = resultado.stdout + resultado.stderr

    assert resultado.returncode != 0, saida
    assert "kit_check: FALHOU (1 problema(s))" in saida, saida
    assert "materializar: FALHOU" not in saida, saida


def test_check_drift_detalhe_do_readme_sai_sob_o_item_indentado_sem_marcador(tmp_path):
    """EBK-T5a — no `check-drift`, as duas linhas de detalhe da divergência de README saem logo
    abaixo do item que começa por `  - README.md diverge do regenerado`, indentadas com quatro
    espaços e sem o marcador `- `; nenhuma linha de item (`  - `) contém `[versionado]` ou
    `[regenerado]`, e o número do cabeçalho é igual ao número de linhas de item."""
    if not _pwsh_disponivel():
        pytest.skip("pwsh não está no PATH")

    copia = _copiar_kit(tmp_path)
    readme = copia / ".claude" / "README.md"
    conteudo = readme.read_text(encoding="utf-8")
    trecho_original = "preservam o contexto dos agentes de planejamento e execução. |"
    trecho_divergente = (
        "preservam o contexto dos agentes de planejamento e execução. Frase extra. |"
    )
    assert trecho_original in conteudo
    readme.write_text(conteudo.replace(trecho_original, trecho_divergente), encoding="utf-8")

    resultado = _rodar_check_drift(copia)
    saida = resultado.stdout + resultado.stderr

    assert resultado.returncode != 0, saida

    linhas = saida.splitlines()
    idx_item_readme = next(
        i for i, l in enumerate(linhas) if l.startswith("  - README.md diverge do regenerado")
    )
    detalhe = linhas[idx_item_readme + 1 : idx_item_readme + 3]
    assert len(detalhe) == 2, saida
    for linha in detalhe:
        assert re.match(r"^    \[(versionado|regenerado)\] ", linha), saida

    for l in linhas:
        if l.startswith("  - "):
            assert "[versionado]" not in l, saida
            assert "[regenerado]" not in l, saida

    match = _CONTAGEM_RE.search(saida)
    assert match is not None, saida
    contagem = int(match.group(1))
    assert len(_ITEM_RE.findall(saida)) == contagem, saida
