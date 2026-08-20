"""RPC-T2 (`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T2`) — TF/TR de
`.claude/tools/materializar.py`, o materializador/verificador do ponto de carga
(`.claude/projecoes.json` -> `settings.json`).

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é
carregado por caminho via `importlib.util.spec_from_file_location`, mesmo padrão de
`tests/test_telemetria.py` e `tests/test_dead_code.py`.

Todos os testes, exceto o de fechamento (item 12 do dossiê `### T2`), trabalham sobre
fixtures sintéticas em `tmp_path` — nunca contra `.claude/` real nem `~/.claude` real. O
teste de fechamento prova `drift` verde contra o repositório real depois de um `apply`
real (com defaults, sem `--kit-root`/`--home`), a prova de que a materialização real do
projeto está correta — sem tocar `~/.claude` (default `--alvo` é `projeto`)."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_MATERIALIZAR_PATH = _ROOT / ".claude" / "tools" / "materializar.py"


def _load_materializar():
    spec = importlib.util.spec_from_file_location("materializar", _MATERIALIZAR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


_DENY_PADRAO = [
    "Bash(git push --force*)",
    "Bash(git push -f*)",
    "Bash(git reset --hard*)",
    "Bash(git branch -D*)",
    "Bash(git clean -fdx*)",
    "Bash(gh repo delete*)",
]


def _manifesto_projeto(comando="python {KIT_ROOT}/tools/ocupacao.py", arquivos=None):
    return {
        "alvos": {
            "projeto": {
                "settings": "settings.json",
                "raiz": None,
                "chaves": {
                    "hooks": {
                        "PreToolUse": [
                            {
                                "matcher": ".*",
                                "hooks": [{"type": "command", "command": comando}],
                            }
                        ]
                    },
                    "permissions.deny": list(_DENY_PADRAO),
                },
                "arquivos": arquivos or [],
            }
        }
    }


def _manifesto_usuario(arquivos=None):
    return {
        "alvos": {
            "usuario": {
                "settings": "{HOME_CLAUDE}/settings.json",
                "raiz": "{HOME_CLAUDE}",
                "chaves": {"hooks": {}},
                "arquivos": arquivos or [],
            }
        }
    }


def test_tf_apply_hub_materializa_hook_do_canonico(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    mensagens, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads((kit_root / "settings.json").read_text(encoding="utf-8"))
    comando = destino["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    assert comando == f"python {kit_root.as_posix()}/tools/ocupacao.py"


def test_tf_apply_devolve_deny_declarado_e_preserva_allow(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    _write_json(
        kit_root / "settings.json",
        {"permissions": {"allow": ["Bash(ls*)"], "deny": ["regra-velha"]}},
    )
    home_claude = tmp_path / "home" / ".claude"

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads((kit_root / "settings.json").read_text(encoding="utf-8"))
    assert destino["permissions"]["deny"] == _DENY_PADRAO
    assert destino["permissions"]["allow"] == ["Bash(ls*)"]


def test_tf_apply_layout_consumidor_grava_prefixo_e_settings_do_pai(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "consumidor" / ".claude" / "kit"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino_path = kit_root.parent / "settings.json"
    assert destino_path.exists()
    destino = json.loads(destino_path.read_text(encoding="utf-8"))
    comando = destino["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    assert comando == f"python {kit_root.as_posix()}/tools/ocupacao.py"


def test_tf_apply_e_idempotente(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    materializar.apply(kit_root, home_claude, ["projeto"])
    destino_path = kit_root / "settings.json"
    conteudo_apos_primeira = destino_path.read_bytes()

    mensagens, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    assert destino_path.read_bytes() == conteudo_apos_primeira
    assert any("ja atualizado" in m for m in mensagens)


def test_tf_apply_nao_reescreve_destino_semanticamente_igual_com_formatacao_divergente(tmp_path):
    """RPC-T10 (`### T10`): destino com o mesmo conteúdo semântico do `apply`, mas
    formatado diferente (`indent=4` e ordem de chaves trocada), não é tocado —
    bytes idênticos antes e depois."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    materializar.apply(kit_root, home_claude, ["projeto"])
    destino_path = kit_root / "settings.json"
    canonico = json.loads(destino_path.read_text(encoding="utf-8"))

    divergente = json.dumps(
        {"permissions": canonico["permissions"], "hooks": canonico["hooks"]},
        indent=4,
        ensure_ascii=False,
    ) + "\n"
    destino_path.write_text(divergente, encoding="utf-8")
    conteudo_divergente = destino_path.read_bytes()

    mensagens, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    assert destino_path.read_bytes() == conteudo_divergente
    assert any("ja atualizado" in m for m in mensagens)


def test_tr_apply_reescreve_destino_com_diferenca_semantica_real(tmp_path):
    """Regressão: destino a que falta uma entrada de hook canônica continua sendo
    escrito pelo `apply`, e o resultado sai no formato do `_dump` (indent=2)."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    materializar.apply(kit_root, home_claude, ["projeto"])
    destino_path = kit_root / "settings.json"
    canonico = json.loads(destino_path.read_text(encoding="utf-8"))
    faltando = {"permissions": canonico["permissions"], "hooks": {}}
    _write_json(destino_path, faltando)

    mensagens, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads(destino_path.read_text(encoding="utf-8"))
    assert destino["hooks"]["PreToolUse"][0]["hooks"][0]["command"] == f"python {kit_root.as_posix()}/tools/ocupacao.py"
    assert any("] settings: atualizado" in m for m in mensagens)


def test_tf_apply_preserva_hook_local_e_remove_kit_obsoleto(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    _write_json(
        kit_root / "settings.json",
        {
            "hooks": {
                "PreToolUse": [
                    {
                        "matcher": "Foo",
                        "hooks": [{"type": "command", "command": "python .claude/tools/hook_antigo.py"}],
                    },
                    {
                        "matcher": "Bar",
                        "hooks": [{"type": "command", "command": "echo local"}],
                    },
                ]
            }
        },
    )
    home_claude = tmp_path / "home" / ".claude"

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads((kit_root / "settings.json").read_text(encoding="utf-8"))
    entradas = destino["hooks"]["PreToolUse"]
    comandos = [e["hooks"][0]["command"] for e in entradas]
    assert comandos == [f"python {kit_root.as_posix()}/tools/ocupacao.py", "echo local"]


def test_tf_apply_grava_command_absoluto_e_arquivo_referenciado_existe(tmp_path):
    """RPC-T11 (`### T11`): o `command` gravado pelo `apply` é caminho absoluto
    (POSIX), independente do cwd da chamada de ferramenta que dispara o hook, e o
    arquivo que ele referencia existe em disco."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    (kit_root / "tools").mkdir(parents=True)
    (kit_root / "tools" / "ocupacao.py").write_text("print('ocupacao')\n", encoding="utf-8")
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads((kit_root / "settings.json").read_text(encoding="utf-8"))
    comando = destino["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    assert comando == f"python {kit_root.as_posix()}/tools/ocupacao.py"
    caminho_referenciado = Path(comando.split(" ", 1)[1])
    assert caminho_referenciado.is_absolute()
    assert caminho_referenciado.exists()


def test_tr_apply_substitui_entrada_de_kit_relativa_antiga_por_absoluta_unica(tmp_path):
    """Regressão TK-49: destino que já traz a entrada de kit gravada na forma
    relativa antiga (anterior à RPC-T11) sai do `apply` com uma única entrada — a
    absoluta — sem duplicar o hook."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    _write_json(
        kit_root / "settings.json",
        {
            "hooks": {
                "PreToolUse": [
                    {
                        "matcher": ".*",
                        "hooks": [{"type": "command", "command": "python .claude/tools/ocupacao.py"}],
                    }
                ]
            }
        },
    )
    home_claude = tmp_path / "home" / ".claude"

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads((kit_root / "settings.json").read_text(encoding="utf-8"))
    entradas = destino["hooks"]["PreToolUse"]
    assert len(entradas) == 1
    assert entradas[0]["hooks"][0]["command"] == f"python {kit_root.as_posix()}/tools/ocupacao.py"


def test_tf_apply_preserva_chave_de_topo_nao_declarada(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    _write_json(
        kit_root / "settings.json",
        {"model": "sonnet", "statusLine": {"type": "command", "command": "echo oi"}},
    )
    home_claude = tmp_path / "home" / ".claude"

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads((kit_root / "settings.json").read_text(encoding="utf-8"))
    assert destino["model"] == "sonnet"
    assert destino["statusLine"] == {"type": "command", "command": "echo oi"}


def test_tf_apply_settings_ausente_cria_arquivo_so_com_chaves_declaradas(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"
    destino_path = kit_root / "settings.json"
    assert not destino_path.exists()

    _, problemas = materializar.apply(kit_root, home_claude, ["projeto"])

    assert problemas == []
    destino = json.loads(destino_path.read_text(encoding="utf-8"))
    assert set(destino.keys()) == {"hooks", "permissions"}


def test_tf_apply_alvo_usuario_copia_arquivo_e_nao_remove_nao_declarado(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    (kit_root / "hooks").mkdir(parents=True)
    (kit_root / "hooks" / "meu_hook.py").write_text("print('kit')\n", encoding="utf-8")
    manifesto = _manifesto_projeto()
    manifesto["alvos"].update(
        _manifesto_usuario(arquivos=[{"de": "hooks/meu_hook.py", "para": "hooks/meu_hook.py"}])["alvos"]
    )
    _write_json(kit_root / "projecoes.json", manifesto)

    home_claude = tmp_path / "home" / ".claude"
    (home_claude / "hooks").mkdir(parents=True)
    (home_claude / "hooks" / "outro.py").write_text("print('outro')\n", encoding="utf-8")

    _, problemas = materializar.apply(kit_root, home_claude, ["usuario"])

    assert problemas == []
    assert (home_claude / "hooks" / "meu_hook.py").read_text(encoding="utf-8") == "print('kit')\n"
    assert (home_claude / "hooks" / "outro.py").read_text(encoding="utf-8") == "print('outro')\n"


def test_tf_apply_alvo_usuario_cria_diretorio_intermediario_e_nao_toca_irmao(tmp_path):
    """RPC-T6 (`### T6`): quando o `para` do manifesto é `skills/<nome>/SKILL.md` e o
    diretório `skills/<nome>/` ainda não existe no destino, `apply` cria o diretório
    intermediário e grava o arquivo, sem tocar em outro subdiretório de `skills/` que já
    exista no destino e não esteja declarado no manifesto."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    (kit_root / "skills" / "nova-skill").mkdir(parents=True)
    (kit_root / "skills" / "nova-skill" / "SKILL.md").write_text("# nova\n", encoding="utf-8")
    manifesto = _manifesto_projeto()
    manifesto["alvos"].update(
        _manifesto_usuario(
            arquivos=[{"de": "skills/nova-skill/SKILL.md", "para": "skills/nova-skill/SKILL.md"}]
        )["alvos"]
    )
    _write_json(kit_root / "projecoes.json", manifesto)

    home_claude = tmp_path / "home" / ".claude"
    (home_claude / "skills" / "skill-existente").mkdir(parents=True)
    (home_claude / "skills" / "skill-existente" / "SKILL.md").write_text(
        "# existente\n", encoding="utf-8"
    )

    assert not (home_claude / "skills" / "nova-skill").exists()

    _, problemas = materializar.apply(kit_root, home_claude, ["usuario"])

    assert problemas == []
    assert (home_claude / "skills" / "nova-skill" / "SKILL.md").read_text(
        encoding="utf-8"
    ) == "# nova\n"
    assert (home_claude / "skills" / "skill-existente" / "SKILL.md").read_text(
        encoding="utf-8"
    ) == "# existente\n"


def test_tf_apply_alvo_usuario_preserva_chaves_de_topo_e_grava_hooks_declarados(tmp_path):
    """RPC-T5 (`### T5`): `apply --alvo usuario` preserva `model`, `effortLevel`,
    `switchModelsOnFlag`, `statusLine` e `permissions.allow` de um `settings.json` de
    destino pré-existente com essas chaves, ao mesmo tempo em que grava os hooks
    declarados em `chaves.hooks` (comando resolvido por `{HOME_CLAUDE}`)."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    manifesto = {
        "alvos": {
            "usuario": {
                "settings": "{HOME_CLAUDE}/settings.json",
                "raiz": "{HOME_CLAUDE}",
                "chaves": {
                    "hooks": {
                        "PreToolUse": [
                            {
                                "matcher": "Bash|PowerShell",
                                "hooks": [
                                    {
                                        "type": "command",
                                        "command": "python {HOME_CLAUDE}/hooks/pytest_pretooluse.py",
                                        "timeout": 15,
                                    }
                                ],
                            }
                        ],
                        "UserPromptSubmit": [
                            {
                                "hooks": [
                                    {
                                        "type": "command",
                                        "command": "python {HOME_CLAUDE}/hooks/modelo_por_fase_userpromptsubmit.py",
                                        "timeout": 15,
                                    }
                                ]
                            }
                        ],
                    }
                },
                "arquivos": [],
            }
        }
    }
    _write_json(kit_root / "projecoes.json", manifesto)
    home_claude = tmp_path / "home" / ".claude"
    _write_json(
        home_claude / "settings.json",
        {
            "model": "sonnet",
            "effortLevel": "high",
            "switchModelsOnFlag": True,
            "statusLine": {"type": "command", "command": "python statusline.py"},
            "permissions": {"allow": ["Bash(ls*)"]},
        },
    )

    _, problemas = materializar.apply(kit_root, home_claude, ["usuario"])

    assert problemas == []
    destino = json.loads((home_claude / "settings.json").read_text(encoding="utf-8"))
    assert destino["model"] == "sonnet"
    assert destino["effortLevel"] == "high"
    assert destino["switchModelsOnFlag"] is True
    assert destino["statusLine"] == {"type": "command", "command": "python statusline.py"}
    assert destino["permissions"] == {"allow": ["Bash(ls*)"]}
    comando_pretool = destino["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    assert comando_pretool == f"python {home_claude.as_posix()}/hooks/pytest_pretooluse.py"
    comando_prompt = destino["hooks"]["UserPromptSubmit"][0]["hooks"][0]["command"]
    assert comando_prompt == f"python {home_claude.as_posix()}/hooks/modelo_por_fase_userpromptsubmit.py"


def test_tf_drift_alvo_usuario_acusa_arquivo_ausente_e_fica_verde_apos_apply(tmp_path):
    """RPC-T4 (`### T4`): `drift --alvo usuario --home <tmp>` acusa o arquivo do
    ponto de carga ausente no destino, e sai 0 depois do `apply` correspondente —
    prova de que a promoção do canônico (`global/CLAUDE.md` -> `CLAUDE.md`) é
    reproduzível a partir do manifesto, tudo contra fixture em `tmp_path`."""
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    (kit_root / "global").mkdir(parents=True)
    (kit_root / "global" / "CLAUDE.md").write_text("doutrina global\n", encoding="utf-8")
    manifesto = _manifesto_usuario(arquivos=[{"de": "global/CLAUDE.md", "para": "CLAUDE.md"}])
    _write_json(kit_root / "projecoes.json", manifesto)
    home_claude = tmp_path / "home" / ".claude"

    exit_antes = materializar.main(
        ["drift", "--alvo", "usuario", "--kit-root", str(kit_root), "--home", str(home_claude)]
    )

    assert exit_antes == 1

    exit_apply = materializar.main(
        ["apply", "--alvo", "usuario", "--kit-root", str(kit_root), "--home", str(home_claude)]
    )

    assert exit_apply == 0

    exit_depois = materializar.main(
        ["drift", "--alvo", "usuario", "--kit-root", str(kit_root), "--home", str(home_claude)]
    )

    assert exit_depois == 0


def test_tr_check_falha_quando_comando_aponta_arquivo_inexistente(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    (kit_root / "tools").mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto(comando="python {KIT_ROOT}/tools/nao_existe.py"))
    home_claude = tmp_path / "home" / ".claude"

    problemas = materializar.check(kit_root, home_claude, ["projeto"])

    assert problemas
    assert any("nao_existe.py" in p for p in problemas)


def test_tr_drift_falha_com_destino_ausente_e_mensagem_traz_remedio(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    home_claude = tmp_path / "home" / ".claude"

    problemas = materializar.drift(kit_root, home_claude, ["projeto"])

    assert problemas
    assert any("apply" in p for p in problemas)


def test_tr_drift_falha_com_hook_de_kit_ausente_do_canonico(tmp_path):
    materializar = _load_materializar()
    kit_root = tmp_path / "hub" / ".claude"
    kit_root.mkdir(parents=True)
    _write_json(kit_root / "projecoes.json", _manifesto_projeto())
    _write_json(
        kit_root / "settings.json",
        {
            "hooks": {
                "PreToolUse": [
                    {
                        "matcher": "Y",
                        "hooks": [{"type": "command", "command": "python .claude/tools/obsoleto.py"}],
                    }
                ]
            },
            "permissions": {"deny": list(_DENY_PADRAO)},
        },
    )
    home_claude = tmp_path / "home" / ".claude"

    problemas = materializar.drift(kit_root, home_claude, ["projeto"])

    assert any("residuo" in p for p in problemas)


def test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply():
    """Item 12 do dossiê `### T2`: prova de fechamento contra o repositório real (não
    `tmp_path`) — `apply` real seguido de `drift` real, ambos com defaults (sem
    `--kit-root`/`--home`), sem tocar `~/.claude` (default `--alvo` é `projeto`)."""
    materializar = _load_materializar()

    exit_apply = materializar.main(["apply"])
    exit_drift = materializar.main(["drift"])

    assert exit_apply == 0
    assert exit_drift == 0
