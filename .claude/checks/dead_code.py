"""Check executável de código morto testado — G-DEADCODE (`GOVERNANCA.md` §7 item 9).

V2M-T5 (`docs/plans/P-0729-v2-melhoria.md` T5; herdado de `P-0722` Fase 3; DK-7 do
Estágio 3B fixa "três scripts, um só ponto de invocação" — este cobre alcançabilidade
de símbolo Python; `kit_check.ps1` valida a *forma* do kit; `ratchet_piso.py` — quando
existir — valida o piso de regressão da suíte).

Falha (exit != 0) quando existe um símbolo de produção (função/classe/módulo fora de
`tests/`) sem nenhum chamador de produção alcançável a partir de um entry point real.
Cobertura por teste **não** confere "vivo": um símbolo referenciado só de dentro de
`tests/` é exatamente o caso que este check existe para pegar (o episódio que originou
G-DEADCODE — ~300 linhas de produção sem chamador, vivas só pela suíte verde).

Método — alcançabilidade por AST, não por execução:
  1. Descobre todo `.py` de produção sob `--root` (exclui `tests/`, `.venv/`, `venv/`,
     `build/`, `dist/`, `__pycache__/`, `.git/`). `tests/` fica fora do grafo inteiro —
     nem contribui referência, nem é alvo de achado (é exatamente a garantia de que
     "só chamado por teste" não conta como vivo).
  2. Marca como **entry point de módulo** (semente de alcançabilidade): qualquer
     arquivo com guarda `if __name__ == "__main__":` no escopo do módulo; qualquer
     `__main__.py`; o bootstrap convencional (`infracore/app.py`, `.../bootstrap.py`,
     `.../main.py`); todo arquivo sob `contracts/` (superfície de serviço declarada —
     é entry point por construção, com ou sem consumidor ainda); e todo módulo alvo de
     um `entry_point` "modulo:Classe" resolvido a partir de qualquer `manifest.json`
     (plugin registrado — mesmo padrão do `PluginRegistryComponent` do PantonicVideo,
     que resolve `entry_point` desse jeito).
  3. Propaga alcançabilidade de módulo por `import`/`from...import` (resolução best
     effort: absoluta e relativa: import que não resolve para um arquivo do próprio
     `--root` é ignorado silenciosamente — nunca derruba o check).
  4. Um símbolo de produção (função/classe em escopo de módulo, ou método de classe)
     é "vivo" se: (a) é ele próprio um entry point — dunder (`__init__` etc.), símbolo
     sob `contracts/`, função `main`, classe alvo de `entry_point` de `manifest.json`,
     ou decorado com um hook de despacho invisível ao AST (`field_validator`/
     `model_validator`/`validator`/`root_validator` — Pydantic invoca via metaclasse,
     nunca por `.nome()` explícito em lugar nenhum); para método (não função/classe),
     conta também como entry point próprio o override de uma virtual de framework
     declarada em `<root>/.claude/framework-virtuals.txt` (seções `[bases]`/
     `[metodos]`, ver ponto de extensão abaixo) numa classe cuja base — direta ou
     transitiva, resolvida globalmente sobre todas as classes do `--root` varrido,
     por nome simples (o caminho totalmente qualificado não importa, só o atributo
     terminal) — casa alguma entrada de `[bases]`. Motivo estrutural, não allowlist
     de conveniência (V2M-T5, rodada 3; mecanismo de declaração trocado na V2E-T5b):
     um framework de UI/plugin despacha certos métodos por convenção do próprio
     runtime, nunca por uma chamada `.nome()` explícita em lugar nenhum do AST —
     mesma lacuna estrutural do decorador Pydantic acima, só que por herança em vez
     de decorador; OU (b) seu nome simples aparece
     como `Name`/`Attribute.attr`/decorator/base em algum módulo alcançável (inclui
     anotação de tipo, já que `ast.walk` atravessa `arg.annotation`).
     Casamento é por nome simples, não por resolução de tipo — é a mesma aproximação
     que o `_scan_allowlist` do `PluginRegistryComponent` usa para import (top-level
     module, não caminho totalmente qualificado); superestima alcançabilidade em
     colisão de nome (dois métodos `commit` em classes diferentes), o que é viés
     conservador (menos falso positivo), não o contrário.
  5. Achado sobrevivente a isso e ainda sem chamador é o caso real de G-DEADCODE.

Ponto de extensão para virtuais despachadas por framework (V2E-T5b, `DE-5`): este check
não conhece nenhum framework de UI/plugin específico. `<root>/.claude/
framework-virtuals.txt` é um arquivo opcional do projeto varrido — `[bases]` lista
nomes terminais de classe-base cujas subclasses são instanciadas/despachadas pelo
runtime do framework; `[metodos]` lista os nomes de método invocados por esse
despacho (um nome por linha em cada seção, `#` comenta o resto da linha; arquivo
ausente, ou seção ausente, ⇒ lista vazia ⇒ nenhuma exceção concedida). O parser é do
hub; o conteúdo é do projeto — cada consumidor declara o próprio framework.

Lacuna conhecida (documentada, não implementada nesta versão): despacho por convenção
de nome (um método vinculado a um evento pelo próprio nome, sem chamada explícita nem
menção em `[metodos]`) não é capturado; se aparecer, é candidato a nova categoria de
despacho dinâmico (ajuste de regra, não allowlist) antes de virar falso positivo.

CLI: ``python .claude/checks/dead_code.py [--root <caminho>]``. Sem `--root`, resolve
a raiz do repositório a partir do próprio script (``checks/../.. = raiz``), o mesmo
desenho do `-KitRoot` do `kit_check.ps1` — permite provar contra uma fixture sintética
fora da árvore real sem nunca escrever nela.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Allowlist — API de contrato ainda sem consumidor (uma entrada por linha, com
# justificativa). NÃO é para esconder código morto real; é só para o caso legítimo
# de uma superfície publicada antes do primeiro consumidor existir. Formato da
# entrada: dotted qualname resolvido pelo próprio check (ver mensagem de achado).
# ---------------------------------------------------------------------------
ALLOWLIST: set[str] = {
    # Exemplo (vazio no baseline atual — ver Veredito da V2M-T5 no diário de obras):
    # "contracts.some_future_surface.SomeAPI": "declarado, sem consumidor ainda (D-XXX)",
}

EXCLUDED_DIR_NAMES = {"tests", ".venv", "venv", "build", "dist", "__pycache__", ".git"}

# Decoradores que despacham por baixo do AST (metaclasse/framework), nunca por uma
# chamada `.nome()` explícita em algum lugar do código — só esses; property/
# staticmethod/classmethod/abstractmethod continuam pegos pelo casamento de nome
# comum (`obj.nome()` já é um Attribute reference).
_INVISIBLE_DISPATCH_DECORATORS = {"field_validator", "model_validator", "validator", "root_validator"}

_BOOTSTRAP_BASENAMES = {"app.py", "bootstrap.py", "main.py", "__main__.py"}

_FRAMEWORK_VIRTUALS_RELPATH = Path(".claude") / "framework-virtuals.txt"


def _parse_framework_virtuals(text: str) -> tuple[set[str], set[str]]:
    """Parse o conteúdo de `framework-virtuals.txt`: seções `[bases]` e `[metodos]`,
    um nome por linha, `#` comenta o resto da linha. Seção desconhecida ou ausente
    ⇒ conjunto vazio para ela — nunca levanta em entrada malformada (mesma postura
    best-effort de `_resolve_import_targets`)."""
    bases: set[str] = set()
    methods: set[str] = set()
    current: set[str] | None = None
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        if line == "[bases]":
            current = bases
            continue
        if line == "[metodos]":
            current = methods
            continue
        if line.startswith("[") and line.endswith("]"):
            current = None
            continue
        if current is not None:
            current.add(line)
    return bases, methods


def _load_framework_virtuals(root: Path) -> tuple[set[str], set[str]]:
    """Carrega `<root>/.claude/framework-virtuals.txt`. Arquivo ausente ⇒
    `(set(), set())` — nenhuma exceção é concedida sem declaração explícita do
    projeto varrido."""
    path = root / _FRAMEWORK_VIRTUALS_RELPATH
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return set(), set()
    return _parse_framework_virtuals(text)


def _iter_py_files(root: Path):
    for p in root.rglob("*.py"):
        rel_parts = p.relative_to(root).parts[:-1]
        if set(rel_parts) & EXCLUDED_DIR_NAMES:
            continue
        yield p


def _module_dotted_name(root: Path, path: Path) -> str:
    rel = path.relative_to(root).with_suffix("")
    parts = list(rel.parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _has_main_guard(tree: ast.Module) -> bool:
    for node in tree.body:
        if not isinstance(node, ast.If):
            continue
        test = node.test
        if not isinstance(test, ast.Compare) or len(test.ops) != 1 or not isinstance(test.ops[0], ast.Eq):
            continue
        operands = [test.left, test.comparators[0]]
        names = {n.id for n in operands if isinstance(n, ast.Name)}
        consts = {n.value for n in operands if isinstance(n, ast.Constant)}
        if "__name__" in names and "__main__" in consts:
            return True
    return False


def _decorator_terminal_names(decorator_list) -> set[str]:
    names: set[str] = set()
    for dec in decorator_list:
        node = dec.func if isinstance(dec, ast.Call) else dec
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            names.add(node.attr)
    return names


def _base_terminal_names(bases) -> set[str]:
    """Nome terminal de cada base de classe — mesma aproximação de
    `_decorator_terminal_names`: `Base` e `pkg.Base` casam igual (só o atributo/nome
    terminal importa, não o caminho totalmente qualificado)."""
    names: set[str] = set()
    for base in bases:
        node = base.func if isinstance(base, ast.Call) else base
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            names.add(node.attr)
    return names


def _is_framework_derived(
    cls_name: str,
    class_bases: dict[str, set[str]],
    framework_bases: set[str],
    _seen: set[str] | None = None,
) -> bool:
    """True se `cls_name` (ou alguma base transitiva) casa por nome simples uma
    entrada de `framework_bases` — a seção `[bases]` do `framework-virtuals.txt` do
    projeto varrido (`_load_framework_virtuals`). Sem declaração, `framework_bases`
    é vazio e isto sempre retorna False (nenhuma exceção concedida).

    Resolução é global ao repositório varrido (o `class_bases` passado cobre todas
    as `trees` de `check()`, não só o arquivo do achado) — uma classe derivada do
    framework por duas camadas de herança dentro do próprio projeto
    (`class Foo(BaseWidget)` onde `BaseWidget(FrameworkBase)` mora em outro arquivo)
    ainda resolve. `_seen` protege contra ciclo de herança (não deveria existir em
    código real, mas não pode travar o check)."""
    if not framework_bases:
        return False
    seen = _seen if _seen is not None else set()
    if cls_name in seen:
        return False
    seen.add(cls_name)
    for base in class_bases.get(cls_name, ()):
        if base in framework_bases:
            return True
        if _is_framework_derived(base, class_bases, framework_bases, seen):
            return True
    return False


class _Definition:
    __slots__ = ("qualname", "simple_name", "kind", "file", "lineno", "auto_alive")

    def __init__(self, qualname, simple_name, kind, file, lineno, auto_alive):
        self.qualname = qualname
        self.simple_name = simple_name
        self.kind = kind
        self.file = file
        self.lineno = lineno
        self.auto_alive = auto_alive


def _collect_manifest_entry_classes(root: Path, module_map: dict[str, Path]) -> tuple[set[Path], set[tuple[str, str]]]:
    """Return (seed_files, {(module_dotted, class_name)}) from every manifest.json's entry_point."""
    seeds: set[Path] = set()
    entry_classes: set[tuple[str, str]] = set()
    for manifest_path in root.rglob("manifest.json"):
        rel_parts = manifest_path.relative_to(root).parts[:-1]
        if set(rel_parts) & EXCLUDED_DIR_NAMES:
            continue
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        entry = data.get("entry_point") if isinstance(data, dict) else None
        if not isinstance(entry, str) or ":" not in entry:
            continue
        module_suffix, class_name = entry.rsplit(":", 1)
        prefix_parts = list(manifest_path.parent.relative_to(root).parts)
        dotted = ".".join(prefix_parts + [module_suffix]) if prefix_parts else module_suffix
        target_file = module_map.get(dotted)
        if target_file is not None:
            seeds.add(target_file)
            entry_classes.add((dotted, class_name))
    return seeds, entry_classes


def _resolve_import_targets(current_dotted: str, is_init: bool, node) -> list[str]:
    targets: list[str] = []
    try:
        if isinstance(node, ast.Import):
            for alias in node.names:
                targets.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level and node.level > 0:
                base_parts = current_dotted.split(".") if current_dotted else []
                if not is_init:
                    base_parts = base_parts[:-1] if base_parts else base_parts
                up = node.level - 1
                if up > 0:
                    if up >= len(base_parts):
                        return []
                    base_parts = base_parts[: len(base_parts) - up]
                pkg = ".".join(base_parts)
                # `from .adhoc.repository import X` (level=1) tem `node.module ==
                # "adhoc.repository"` — o dotted completo é pacote-resolvido-por-nível
                # + esse submódulo, não só o pacote. Perder essa parte (bug corrigido
                # na V2M-T5) deixava todo `from .sub.mod import X` dentro de um pacote
                # de serviço/plugin sem alvo resolvido, e o submódulo nunca entrava em
                # `reachable_modules` — falso positivo em massa (`*/adhoc/*`).
                if node.module:
                    base = f"{pkg}.{node.module}" if pkg else node.module
                else:
                    base = pkg
            else:
                base = node.module or ""
            if base:
                targets.append(base)
            for alias in node.names:
                if base:
                    targets.append(f"{base}.{alias.name}")
                else:
                    targets.append(alias.name)
    except Exception:  # noqa: BLE001 — resolução é best-effort, nunca derruba o check
        return []
    return targets


def check(root: Path) -> list[str]:
    root = root.resolve()
    files = list(_iter_py_files(root))

    trees: dict[Path, ast.Module] = {}
    dotted_of: dict[Path, str] = {}
    module_map: dict[str, Path] = {}
    is_init_of: dict[Path, bool] = {}

    for f in files:
        try:
            source = f.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(f))
        except (OSError, SyntaxError, UnicodeDecodeError):
            continue
        trees[f] = tree
        dotted = _module_dotted_name(root, f)
        dotted_of[f] = dotted
        module_map[dotted] = f
        is_init_of[f] = f.name == "__init__.py"

    manifest_seeds, manifest_entry_classes = _collect_manifest_entry_classes(root, module_map)
    framework_bases, framework_methods = _load_framework_virtuals(root)

    # Mapa global classe -> {bases}, sobre todas as `trees` do repositório varrido
    # (não por arquivo) — herança de framework costuma atravessar arquivo/pacote
    # (ex.: um mixin de projeto entre a classe concreta e a base do framework).
    # `ast.walk` pega ClassDef em qualquer nível de aninhamento, não só top-level.
    class_bases: dict[str, set[str]] = {}
    for tree in trees.values():
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_bases.setdefault(node.name, set()).update(_base_terminal_names(node.bases))

    seeds: set[Path] = set(manifest_seeds)
    for f in trees:
        rel_parts = f.relative_to(root).parts
        if rel_parts and rel_parts[0] == "contracts":
            seeds.add(f)
        if len(rel_parts) >= 2 and rel_parts[0] == "integrations" and rel_parts[1] == "poc":
            # POC standalone sob `integrations/poc/**` é executada à mão, módulo a
            # módulo — não há um único bootstrap comum. Cada módulo ali é raiz de
            # alcançabilidade por si (mesmo desenho de `contracts/`: entry point por
            # construção de diretório, não por guarda de execução).
            seeds.add(f)
        if f.name in _BOOTSTRAP_BASENAMES:
            seeds.add(f)
        if _has_main_guard(trees[f]):
            seeds.add(f)

    # Tier A — module reachability via import graph, BFS from seeds.
    reachable_modules: set[Path] = set(seeds)
    frontier = list(seeds)
    while frontier:
        current = frontier.pop()
        tree = trees[current]
        current_dotted = dotted_of[current]
        is_init = is_init_of[current]
        # Diretório do próprio arquivo (para o fallback de import "chato" abaixo).
        own_package = current_dotted.rsplit(".", 1)[0] if "." in current_dotted else ""
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for target in _resolve_import_targets(current_dotted, is_init, node):
                    target_file = module_map.get(target)
                    if target_file is None and own_package:
                        # Script standalone (ex.: POC executado como
                        # `python arquivo.py`) tem o próprio diretório implícito no
                        # sys.path — `import sibling` sem pacote resolve para o
                        # módulo irmão no mesmo diretório, nunca para a raiz do
                        # repo. Sem este fallback, todo POC com esse padrão vira
                        # ilha "inalcançável" por engano (falso positivo em massa,
                        # não um caso real de G-DEADCODE).
                        target_file = module_map.get(f"{own_package}.{target}")
                    if target_file is not None and target_file not in reachable_modules:
                        reachable_modules.add(target_file)
                        frontier.append(target_file)

    # Reference set — every Name/Attribute/decorator/base-class occurrence in every
    # reachable module (annotations included, since ast.walk descends into them).
    referenced_names: set[str] = set()
    for f in reachable_modules:
        for node in ast.walk(trees[f]):
            if isinstance(node, ast.Name):
                referenced_names.add(node.id)
            elif isinstance(node, ast.Attribute):
                referenced_names.add(node.attr)

    # Collect production definitions.
    definitions: list[_Definition] = []
    for f, tree in trees.items():
        dotted = dotted_of[f]
        rel_parts = f.relative_to(root).parts
        under_contracts = bool(rel_parts) and rel_parts[0] == "contracts"

        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                auto = (
                    under_contracts
                    or node.name in ("main", "__main__")
                    or (node.name.startswith("__") and node.name.endswith("__"))
                    or bool(_decorator_terminal_names(node.decorator_list) & _INVISIBLE_DISPATCH_DECORATORS)
                )
                definitions.append(
                    _Definition(f"{dotted}.{node.name}", node.name, "function", f, node.lineno, auto)
                )
            elif isinstance(node, ast.ClassDef):
                class_auto = under_contracts or (dotted, node.name) in manifest_entry_classes
                definitions.append(
                    _Definition(f"{dotted}.{node.name}", node.name, "class", f, node.lineno, class_auto)
                )
                for member in node.body:
                    if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        method_auto = (
                            class_auto
                            or (member.name.startswith("__") and member.name.endswith("__"))
                            or bool(
                                _decorator_terminal_names(member.decorator_list)
                                & _INVISIBLE_DISPATCH_DECORATORS
                            )
                            or (
                                member.name in framework_methods
                                and _is_framework_derived(node.name, class_bases, framework_bases)
                            )
                        )
                        definitions.append(
                            _Definition(
                                f"{dotted}.{node.name}.{member.name}",
                                member.name,
                                "method",
                                f,
                                member.lineno,
                                method_auto,
                            )
                        )

    findings: list[str] = []
    for d in definitions:
        if d.auto_alive:
            continue
        if d.file not in reachable_modules:
            alive = False
        else:
            alive = d.simple_name in referenced_names
        if not alive:
            if d.qualname in ALLOWLIST:
                continue
            rel = d.file.relative_to(root)
            findings.append(f"{rel}:{d.lineno}: {d.qualname} ({d.kind}) - sem chamador de producao alcancavel")

    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="G-DEADCODE — símbolo de produção órfão (alcançabilidade por AST).")
    default_root = Path(__file__).resolve().parent.parent.parent
    parser.add_argument("--root", type=Path, default=default_root, help="Raiz do repositório a checar.")
    args = parser.parse_args(argv)

    findings = check(args.root)
    if not findings:
        print(f"dead_code: OK - 0 achado(s) sob '{args.root}'.")
        return 0

    for line in findings:
        print(line)
    print(f"dead_code: FALHOU - {len(findings)} achado(s) de simbolo de producao sem chamador.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
