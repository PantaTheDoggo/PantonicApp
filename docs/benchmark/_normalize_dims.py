import re, sys, pathlib

CANON = {
    1: "Identidade e escopo",
    2: "Vitalidade",
    3: "Ciclo de vida do trabalho",
    4: "Papéis e modelo por fase",
    5: "Unidade de trabalho e rastreabilidade",
    6: "Contexto e custo",
    7: "Memória e estado persistente",
    8: "Qualidade e testes",
    9: "Guardrails e enforcement",
    10: "Distribuição e versionamento do próprio framework",
    11: "Extensibilidade",
    12: "Observabilidade e métricas",
    13: "Segurança e permissões",
    14: "Onboarding humano e documentação",
    15: "Multi-projeto, multi-repo e equipe",
    16: "Interação com o humano",
}

HEAD = re.compile(r"^(#+)\s*D(\d{1,2})\b.*$")

for path in sys.argv[1:]:
    p = pathlib.Path(path)
    lines = p.read_text(encoding="utf-8").split("\n")
    changed = []
    for i, line in enumerate(lines):
        m = HEAD.match(line)
        if not m:
            continue
        n = int(m.group(2))
        if n not in CANON:
            continue
        new = f"{m.group(1)} D{n} — {CANON[n]}"
        if new != line:
            changed.append(f"  D{n}: {line.strip()!r} -> {CANON[n]!r}")
            lines[i] = new
    if changed:
        p.write_text("\n".join(lines), encoding="utf-8")
    print(f"{p.name}: {len(changed)} titulo(s) normalizado(s)")
    for c in changed:
        print(c)
