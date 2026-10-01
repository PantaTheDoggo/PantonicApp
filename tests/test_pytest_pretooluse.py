"""RAF-T6 (`docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` `### RAF-T6`) — o filtro da
saída dos testes devolve o código de saída dos próprios testes, mesmo quando o comando encadeia
outros passos depois deles.

Carrega o hook e o filtro por caminho (`.claude/global/hooks/` não é pacote importável) e roda
cada um por subprocesso: o hook recebe o JSON do evento no stdin e devolve JSON no stdout; o
filtro recebe o texto da saída do pytest no stdin, com `TMPDIR`/`TEMP`/`TMP` apontando para
`tmp_path`, para o log não cair na pasta temporária do usuário."""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_HOOK_PATH = _ROOT / ".claude" / "global" / "hooks" / "pytest_pretooluse.py"
_FILTER_PATH = _ROOT / ".claude" / "global" / "hooks" / "pytest_filter.py"


def _load_hook_module():
    spec = importlib.util.spec_from_file_location("pytest_pretooluse_raf_t6", _HOOK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _filtro_path_esperado() -> str:
    return _load_hook_module().FILTER_PATH


def _rodar_hook(tool_name: str, command: str) -> str:
    payload = json.dumps({"tool_name": tool_name, "tool_input": {"command": command}})
    resultado = subprocess.run(
        [sys.executable, str(_HOOK_PATH)],
        input=payload,
        capture_output=True,
        text=True,
        check=True,
    )
    return resultado.stdout


def _rodar_filtro(texto: str, tmp_path: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["TMPDIR"] = str(tmp_path)
    env["TEMP"] = str(tmp_path)
    env["TMP"] = str(tmp_path)
    return subprocess.run(
        [sys.executable, str(_FILTER_PATH)],
        input=texto,
        capture_output=True,
        text=True,
        env=env,
    )


def test_tf_hook_reescreve_so_o_segmento_do_pytest_no_bash():
    filtro = _filtro_path_esperado()
    stdout = _rodar_hook("Bash", 'cd x && pytest -q; echo "exit=$?"')
    saida = json.loads(stdout)

    esperado = (
        'cd x && { pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s"; echo "exit=$?"'
        % filtro
    )
    assert saida["hookSpecificOutput"]["updatedInput"]["command"] == esperado


def test_tf_hook_reescreve_so_o_segmento_do_pytest_no_powershell():
    filtro = _filtro_path_esperado()
    stdout = _rodar_hook("PowerShell", 'python -m pytest -q; Write-Output "fim"')
    saida = json.loads(stdout)

    esperado = (
        '& { python -m pytest -q; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "%s"; '
        'Write-Output "fim"' % filtro
    )
    assert saida["hookSpecificOutput"]["updatedInput"]["command"] == esperado


def test_tr_hook_sem_pytest_segue_passthrough():
    stdout = _rodar_hook("Bash", "git status")

    assert stdout.strip() == "{}"


def test_tf_hook_reescreve_o_pytest_antes_do_ou_logico():
    filtro = _filtro_path_esperado()
    stdout = _rodar_hook("Bash", "pytest -q || echo falhou")
    saida = json.loads(stdout)

    esperado = (
        '{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s" || echo falhou'
        % filtro
    )
    assert saida["hookSpecificOutput"]["updatedInput"]["command"] == esperado


def test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha():
    filtro = _filtro_path_esperado()
    bloco = '{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "%s"' % filtro

    stdout_ou_logico = _rodar_hook("Bash", "false || pytest -q")
    saida_ou_logico = json.loads(stdout_ou_logico)
    assert saida_ou_logico["hookSpecificOutput"]["updatedInput"]["command"] == (
        "false || %s" % bloco
    )

    stdout_quebra_de_linha = _rodar_hook("Bash", "cd x\npytest -q")
    saida_quebra_de_linha = json.loads(stdout_quebra_de_linha)
    assert saida_quebra_de_linha["hookSpecificOutput"]["updatedInput"]["command"] == (
        "cd x\n%s" % bloco
    )


def test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough():
    assert _rodar_hook("Bash", "pytest -q | tail -5").strip() == "{}"
    assert _rodar_hook("Bash", "pytest -q > out.txt").strip() == "{}"


def test_tf_filtro_sai_com_o_exit_do_marcador(tmp_path):
    entrada = "3 passed in 0.10s\n__PYTEST_EXIT__=5\n"

    resultado = _rodar_filtro(entrada, tmp_path)

    assert resultado.returncode == 5
    assert "__PYTEST_EXIT__" not in resultado.stdout
    assert "3 passed in 0.10s" in resultado.stdout


def test_tr_filtro_sem_marcador_segue_pelo_sumario(tmp_path):
    falhou = _rodar_filtro("1 failed, 2 passed in 0.10s\n", tmp_path)
    assert falhou.returncode == 1

    passou = _rodar_filtro("3 passed in 0.10s\n", tmp_path)
    assert passou.returncode == 0
