"""RPC-T2 (`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T2`) — o canônico
declarado que o harness lê (`.claude/projecoes.json`) e o materializador/verificador
idempotente que o projeta em `.claude/settings.json`. Absorve o desenho da `EXA-T53`
(cancelada por absorção na `DP-R` do `P-0734`): manifesto único em vez de duas
declarações lado a lado, `apply`/`check`/`drift`, preservação de `permissions.deny` e
de hook não-kit, ancoragem hub × consumidor.

Duas topologias, resolvidas sem pergunta a partir do próprio caminho do script
(`<KIT_ROOT>/tools/materializar.py`): no hub `KIT_ROOT = <repo>/.claude`; no
consumidor `KIT_ROOT = <repo>/.claude/kit`. Regra única: se o diretório-raiz do kit se
chama `kit`, o `settings.json` alvo do projeto é o do **pai** de `KIT_ROOT`; senão, é o
próprio `KIT_ROOT`. O placeholder `{KIT_ROOT}` usado dentro de um `command` de hook
resolve para o caminho físico **absoluto** (POSIX) da raiz do kit (RPC-T11,
`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11`): `.claude/settings.json`
é gitignorado — nunca viaja entre clones — e o cwd da chamada de ferramenta que
dispara o hook não é garantido, então o comando gravado não pode depender dele. A
classificação "é hook de kit" (usada por `apply`/`drift` para decidir resíduo) segue
por um marcador **relativo** (`_kit_marker_prefix`), que casa tanto a forma absoluta
gravada de agora em diante quanto a forma relativa gravada por versões anteriores do
comando. `{HOME_CLAUDE}` resolve para o caminho absoluto (POSIX) do `~/.claude` do
usuário corrente, já que não há forma portátil equivalente fora do repositório.

"Entrada de kit" (usada para decidir o que `apply` remove como resíduo e o que `drift`
acusa como registro fora do canônico): um hook cujo `command` referencia caminho sob
`<KIT_ROOT>/tools/`, `<KIT_ROOT>/checks/` ou `<KIT_ROOT>/global/hooks/` — ou, no alvo
`usuario`, sob `<HOME_CLAUDE>/hooks/`. Todo o resto é configuração de quem opera a
máquina e é intocável.

Superfície testável: as funções `apply`/`check`/`drift` recebem `kit_root`/
`home_claude`/`alvos` já resolvidos (nunca leem `sys.argv`) — `tests/test_materializar.py`
exercita todas contra fixtures em `tmp_path`, nunca contra o repositório real ou o
`~/.claude` real, exceto o teste de fechamento que prova `drift` verde contra o
repositório real depois de um `apply` real (item 12 do dossiê `### T2`).

CLI: ``python .claude/tools/materializar.py {apply,check,drift} [--alvo
projeto|usuario|todos] [--kit-root <caminho>] [--home <caminho>]``. Sem `--alvo`,
default `projeto`. Sem `--kit-root`/`--home`, resolve a partir do próprio script e de
`Path.home()/".claude"` — mesmo desenho de `--root` (`dead_code.py`) e `-KitRoot`
(`kit_check.ps1`): permite provar contra uma fixture sintética sem nunca escrever no
repositório real nem no `~/.claude` real.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_MANIFESTO_BASENAME = "projecoes.json"
_KIT_MARKERS = ("tools/", "checks/", "global/hooks/")


class ManifestoInvalido(Exception):
    """Manifesto ausente, JSON malformado, ou sem a chave `alvos` como objeto."""


# --------------------------------------------------------------------------- #
# Resolução de topologia e placeholders
# --------------------------------------------------------------------------- #


def resolve_kit_root(kit_root_arg: str | None) -> Path:
    if kit_root_arg:
        return Path(kit_root_arg).resolve()
    return Path(__file__).resolve().parent.parent


def resolve_home_claude(home_arg: str | None) -> Path:
    if home_arg:
        return Path(home_arg).resolve()
    return Path.home() / ".claude"


def kit_root_placeholder(kit_root: Path) -> str:
    """Caminho físico **absoluto** (POSIX) que `{KIT_ROOT}` vira dentro de um
    `command` de hook — não mais o texto portátil `.claude`/`.claude/kit`:
    `.claude/settings.json` é local de máquina (gitignorado, nunca versionado) e o
    cwd da chamada de ferramenta que dispara o hook não é garantido, então o
    comando gravado não pode depender dele (RPC-T11). `kit_root` já chega resolvido
    em caminho absoluto (`resolve_kit_root`)."""
    return kit_root.as_posix()


def _kit_marker_prefix(kit_root: Path) -> str:
    """Marcador **relativo** usado só para classificar um `command` (já resolvido)
    como pertencente ao kit por substring: `.claude/kit` quando o diretório-raiz do
    kit se chama `kit` (layout consumidor), senão `.claude` (hub). Precisa ser
    relativo, não o `kit_root_placeholder` absoluto: casa tanto a forma absoluta
    gravada de agora em diante (que o contém como sufixo do caminho) quanto a forma
    relativa gravada por versões anteriores do comando — sem isso, `apply`
    classificaria uma entrada relativa já instalada como hook não-kit, preservando-a
    ao lado da nova em vez de substituí-la (regressão TK-49)."""
    return ".claude/kit" if kit_root.name == "kit" else ".claude"


def settings_root(kit_root: Path) -> Path:
    """Diretório onde vive o `settings.json` do alvo `projeto` — o pai de `KIT_ROOT`
    quando o kit mora em `.../.claude/kit` (consumidor), o próprio `KIT_ROOT` quando
    mora em `.../.claude` (hub). Mesma regra de `kit_root_placeholder`."""
    return kit_root.parent if kit_root.name == "kit" else kit_root


def resolve_placeholders(raw: str, kit_root: Path, home_claude: Path) -> str:
    return raw.replace("{KIT_ROOT}", kit_root_placeholder(kit_root)).replace(
        "{HOME_CLAUDE}", home_claude.as_posix()
    )


def is_kit_command(command: str, alvo_nome: str, kit_root: Path, home_claude: Path) -> bool:
    """True quando `command` (já resolvido, como aparece gravado em disco) referencia
    caminho sob a raiz do kit resolvida, ou (alvo `usuario`) sob `<HOME_CLAUDE>/hooks/`."""
    prefixo = _kit_marker_prefix(kit_root)
    if any(f"{prefixo}/{marcador}" in command for marcador in _KIT_MARKERS):
        return True
    if alvo_nome == "usuario" and f"{home_claude.as_posix()}/hooks/" in command:
        return True
    return False


def _referenced_file(raw_command: str, kit_root: Path, home_claude: Path) -> Path | None:
    """Caminho físico (para checagem de existência) referenciado por um `command`
    ainda não resolvido (`{KIT_ROOT}`/`{HOME_CLAUDE}` literais) — pega o primeiro
    token separado por espaço que contém um placeholder."""
    for token in raw_command.split():
        if "{KIT_ROOT}" in token:
            rel = token.replace("{KIT_ROOT}", "").lstrip("/")
            return kit_root / rel
        if "{HOME_CLAUDE}" in token:
            rel = token.replace("{HOME_CLAUDE}", "").lstrip("/")
            return home_claude / rel
    return None


# --------------------------------------------------------------------------- #
# Manifesto
# --------------------------------------------------------------------------- #


def carregar_manifesto(kit_root: Path) -> dict:
    caminho = kit_root / _MANIFESTO_BASENAME
    if not caminho.exists():
        raise ManifestoInvalido(f"manifesto ausente: {caminho}")
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ManifestoInvalido(f"manifesto invalido (JSON malformado): {caminho} - {exc}") from exc
    if not isinstance(dados.get("alvos"), dict):
        raise ManifestoInvalido(f"manifesto invalido: chave 'alvos' ausente ou nao e objeto em {caminho}")
    return dados


def resolve_settings_destino(cfg: dict, kit_root: Path, home_claude: Path) -> Path:
    raiz = cfg.get("raiz")
    base = Path(resolve_placeholders(raiz, kit_root, home_claude)) if raiz else settings_root(kit_root)
    settings_path = Path(resolve_placeholders(cfg["settings"], kit_root, home_claude))
    if settings_path.is_absolute():
        return settings_path
    return base / settings_path


def _arquivos_base(cfg: dict, kit_root: Path, home_claude: Path) -> Path:
    raiz = cfg.get("raiz")
    return Path(resolve_placeholders(raiz, kit_root, home_claude)) if raiz else settings_root(kit_root)


# --------------------------------------------------------------------------- #
# Hooks — resolução, classificação de kit, materialização
# --------------------------------------------------------------------------- #


def _resolve_hook_entries(entradas: list[dict], kit_root: Path, home_claude: Path) -> list[dict]:
    resolvidas = []
    for entrada in entradas:
        nova = dict(entrada)
        nova_hooks = []
        for h in entrada.get("hooks", []):
            h2 = dict(h)
            if "command" in h2:
                h2["command"] = resolve_placeholders(h2["command"], kit_root, home_claude)
            nova_hooks.append(h2)
        nova["hooks"] = nova_hooks
        resolvidas.append(nova)
    return resolvidas


def _entry_is_kit(entrada: dict, alvo_nome: str, kit_root: Path, home_claude: Path) -> bool:
    for h in entrada.get("hooks", []):
        if is_kit_command(h.get("command", ""), alvo_nome, kit_root, home_claude):
            return True
    return False


# --------------------------------------------------------------------------- #
# apply
# --------------------------------------------------------------------------- #


def build_settings(existing: dict, cfg: dict, alvo_nome: str, kit_root: Path, home_claude: Path) -> dict:
    """Constrói o `settings.json` novo a partir do atual (`existing`) e do declarado
    (`cfg`). Chave de topo não declarada em `cfg['chaves']`: preservada intacta.
    `hooks`: canônicas primeiro (ordem declarada, comando resolvido), locais não-kit
    preservadas depois, locais de kit ausentes do canônico removidas (resíduo).
    `permissions.deny`: substituída pela declarada; `permissions.allow` e demais
    subchaves de `permissions` intocadas."""
    resultado = dict(existing)
    chaves = cfg.get("chaves", {})

    if "hooks" in chaves:
        hooks_canonicos = chaves["hooks"] or {}
        hooks_destino = existing.get("hooks", {}) if isinstance(existing.get("hooks"), dict) else {}
        eventos = list(hooks_canonicos.keys()) + [e for e in hooks_destino if e not in hooks_canonicos]
        novos_hooks: dict = {}
        for evento in eventos:
            canon = _resolve_hook_entries(hooks_canonicos.get(evento, []), kit_root, home_claude)
            preservados = [
                e for e in hooks_destino.get(evento, []) if not _entry_is_kit(e, alvo_nome, kit_root, home_claude)
            ]
            combinado = canon + preservados
            if combinado:
                novos_hooks[evento] = combinado
        if novos_hooks:
            resultado["hooks"] = novos_hooks
        elif "hooks" in resultado:
            del resultado["hooks"]

    if "permissions.deny" in chaves:
        deny = [resolve_placeholders(v, kit_root, home_claude) for v in chaves["permissions.deny"]]
        permissions = dict(existing.get("permissions", {})) if isinstance(existing.get("permissions"), dict) else {}
        permissions["deny"] = deny
        resultado["permissions"] = permissions

    return resultado


def _dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def write_settings(path: Path, obj: dict) -> bool:
    """Escreve só se o conteúdo mudou (idempotente). UTF-8 sem BOM, indentação de 2,
    newline final, `\\n` sempre (independente de plataforma). Caminho rápido: texto
    idêntico ao `_dump` canônico. Caminho semântico: se o texto difere só por
    formatação (indentação, ordem de chaves) mas o JSON decodificado é igual ao
    `obj` canônico, não reescreve — destino ausente ou com JSON ilegível cai no
    comportamento de escrita normal."""
    novo_texto = _dump(obj)
    if path.exists():
        atual = path.read_text(encoding="utf-8")
        if atual == novo_texto:
            return False
        try:
            if json.loads(atual) == obj:
                return False
        except json.JSONDecodeError:
            pass
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(novo_texto)
    return True


def _materializar_arquivos(cfg: dict, alvo_nome: str, kit_root: Path, home_claude: Path) -> list[str]:
    """Copia byte a byte todo item declarado em `arquivos`. Nunca remove nada no
    destino — só o caminho declarado é escrito."""
    problemas = []
    base = _arquivos_base(cfg, kit_root, home_claude)
    for item in cfg.get("arquivos", []):
        de = kit_root / item["de"]
        para = base / item["para"]
        if not de.exists():
            problemas.append(f"[{alvo_nome}] arquivo declarado ausente sob a raiz do kit: {item['de']}")
            continue
        conteudo = de.read_bytes()
        if not para.exists() or para.read_bytes() != conteudo:
            para.parent.mkdir(parents=True, exist_ok=True)
            para.write_bytes(conteudo)
    return problemas


def apply(kit_root: Path, home_claude: Path, alvos_selecionados: list[str]) -> tuple[list[str], list[str]]:
    """Devolve `(mensagens, problemas)`. `problemas` não-vazio ⇒ exit 1 em `main`."""
    try:
        manifesto = carregar_manifesto(kit_root)
    except ManifestoInvalido as exc:
        return [], [str(exc)]

    alvos = manifesto["alvos"]
    mensagens: list[str] = []
    problemas: list[str] = []
    for nome in alvos_selecionados:
        cfg = alvos.get(nome)
        if not isinstance(cfg, dict):
            problemas.append(f"alvo '{nome}' ausente do manifesto")
            continue
        destino = resolve_settings_destino(cfg, kit_root, home_claude)
        existing = json.loads(destino.read_text(encoding="utf-8")) if destino.exists() else {}
        novo = build_settings(existing, cfg, nome, kit_root, home_claude)
        alterado = write_settings(destino, novo)
        mensagens.append(f"[{nome}] settings: {'atualizado' if alterado else 'ja atualizado'} - {destino}")
        problemas.extend(_materializar_arquivos(cfg, nome, kit_root, home_claude))
    return mensagens, problemas


# --------------------------------------------------------------------------- #
# check — valida o canônico, não olha a máquina
# --------------------------------------------------------------------------- #


def check(kit_root: Path, home_claude: Path, alvos_selecionados: list[str]) -> list[str]:
    try:
        manifesto = carregar_manifesto(kit_root)
    except ManifestoInvalido as exc:
        return [str(exc)]

    alvos = manifesto["alvos"]
    problemas: list[str] = []
    for nome in alvos_selecionados:
        cfg = alvos.get(nome)
        if not isinstance(cfg, dict):
            problemas.append(f"alvo '{nome}' ausente do manifesto")
            continue

        for item in cfg.get("arquivos", []):
            de = item.get("de")
            if not de or not (kit_root / de).exists():
                problemas.append(f"[{nome}] arquivo declarado ausente sob a raiz do kit: {de}")

        hooks_cfg = cfg.get("chaves", {}).get("hooks", {}) or {}
        for evento, entradas in hooks_cfg.items():
            for entrada in entradas:
                lista = entrada.get("hooks")
                if not lista:
                    problemas.append(f"[{nome}] evento '{evento}': entrada sem lista 'hooks' nao vazia")
                    continue
                for h in lista:
                    if h.get("type") != "command":
                        problemas.append(f"[{nome}] evento '{evento}': hook sem type='command'")
                    comando = h.get("command")
                    if not comando:
                        problemas.append(f"[{nome}] evento '{evento}': hook com 'command' vazio")
                        continue
                    if "{" in comando:
                        referenciado = _referenced_file(comando, kit_root, home_claude)
                        if referenciado is not None and not referenciado.exists():
                            problemas.append(
                                f"[{nome}] evento '{evento}': command referencia arquivo inexistente "
                                f"'{comando}' -> {referenciado}"
                            )
    return problemas


# --------------------------------------------------------------------------- #
# drift — compara destino x canônico
# --------------------------------------------------------------------------- #


def drift(kit_root: Path, home_claude: Path, alvos_selecionados: list[str]) -> list[str]:
    try:
        manifesto = carregar_manifesto(kit_root)
    except ManifestoInvalido as exc:
        return [str(exc)]

    alvos = manifesto["alvos"]
    problemas: list[str] = []
    for nome in alvos_selecionados:
        cfg = alvos.get(nome)
        if not isinstance(cfg, dict):
            problemas.append(f"alvo '{nome}' ausente do manifesto")
            continue

        destino = resolve_settings_destino(cfg, kit_root, home_claude)
        remedio = f"rode: python .claude/tools/materializar.py apply --alvo {nome}"
        if not destino.exists():
            problemas.append(f"[{nome}] destino ausente: {destino} ({remedio})")
            continue
        existing = json.loads(destino.read_text(encoding="utf-8"))
        chaves = cfg.get("chaves", {})

        if "hooks" in chaves:
            hooks_canonicos = chaves["hooks"] or {}
            hooks_destino = existing.get("hooks", {}) if isinstance(existing.get("hooks"), dict) else {}
            eventos = list(hooks_canonicos.keys()) + [e for e in hooks_destino if e not in hooks_canonicos]
            for evento in eventos:
                canon = _resolve_hook_entries(hooks_canonicos.get(evento, []), kit_root, home_claude)
                entradas_destino = hooks_destino.get(evento, [])
                if canon and entradas_destino[: len(canon)] != canon:
                    problemas.append(
                        f"[{nome}] evento '{evento}': entrada canonica ausente do destino, ou com "
                        f"comando diferente do resolvido ({remedio})"
                    )
                for entrada in entradas_destino:
                    if entrada not in canon and _entry_is_kit(entrada, nome, kit_root, home_claude):
                        problemas.append(
                            f"[{nome}] evento '{evento}': hook de kit no destino ausente do canonico "
                            f"(residuo) - {entrada} ({remedio})"
                        )

        if "permissions.deny" in chaves:
            deny_canonico = [resolve_placeholders(v, kit_root, home_claude) for v in chaves["permissions.deny"]]
            permissions_destino = existing.get("permissions", {})
            deny_destino = permissions_destino.get("deny", []) if isinstance(permissions_destino, dict) else []
            if deny_destino != deny_canonico:
                problemas.append(f"[{nome}] permissions.deny do destino diverge da declarada ({remedio})")

        base = _arquivos_base(cfg, kit_root, home_claude)
        for item in cfg.get("arquivos", []):
            de = kit_root / item["de"]
            para = base / item["para"]
            if not para.exists():
                problemas.append(f"[{nome}] arquivo declarado ausente no destino: {para} ({remedio})")
            elif de.exists() and para.read_bytes() != de.read_bytes():
                problemas.append(f"[{nome}] arquivo declarado com conteudo diferente no destino: {para} ({remedio})")

    return problemas


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--alvo", choices=["projeto", "usuario", "todos"], default="projeto")
    parser.add_argument("--kit-root", dest="kit_root", default=None)
    parser.add_argument("--home", dest="home", default=None)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Materializador/verificador do ponto de carga (.claude/projecoes.json -> settings.json)."
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)
    _add_common_args(subparsers.add_parser("apply", help="Materializa o canonico no settings.json alvo."))
    _add_common_args(subparsers.add_parser("check", help="Valida o canonico (nao olha a maquina)."))
    _add_common_args(subparsers.add_parser("drift", help="Compara o destino materializado x o canonico."))

    args = parser.parse_args(argv)
    kit_root = resolve_kit_root(args.kit_root)
    home_claude = resolve_home_claude(args.home)
    alvos_selecionados = ["projeto", "usuario"] if args.alvo == "todos" else [args.alvo]

    if args.comando == "apply":
        mensagens, problemas = apply(kit_root, home_claude, alvos_selecionados)
        for m in mensagens:
            print(m)
        for p in problemas:
            print(p)
        if problemas:
            print(f"materializar: FALHOU - {len(problemas)} problema(s).")
            return 1
        print("materializar: OK - apply concluido.")
        return 0

    if args.comando == "check":
        problemas = check(kit_root, home_claude, alvos_selecionados)
        for p in problemas:
            print(p)
        if problemas:
            print(f"materializar: FALHOU - {len(problemas)} problema(s) no manifesto.")
            return 1
        print("materializar: OK - manifesto valido.")
        return 0

    if args.comando == "drift":
        problemas = drift(kit_root, home_claude, alvos_selecionados)
        for p in problemas:
            print(p)
        if problemas:
            print(f"materializar: FALHOU - {len(problemas)} problema(s) de drift.")
            return 1
        print("materializar: OK - sem drift.")
        return 0

    parser.error(f"comando desconhecido: {args.comando}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
