"""Mede a sessão principal pelo transcript: uma linha por resposta do assistente com uso e ferramenta."""
import json, sys, re
from pathlib import Path
src = Path(sys.argv[1]); out = Path(sys.argv[2])
rows = []
for line in src.read_text(encoding="utf-8").splitlines():
    try: e = json.loads(line)
    except Exception: continue
    if e.get("type") != "assistant": continue
    m = e.get("message", {}); u = m.get("usage") or {}
    if not u: continue
    ctx = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
    outk = u.get("output_tokens", 0)
    tools = []
    for b in m.get("content", []):
        if b.get("type") == "tool_use":
            i = b.get("input", {})
            if b["name"] == "Agent": tools.append("Agent:" + i.get("subagent_type", "?") + ":" + i.get("description", ""))
            elif b["name"] in ("Bash", "PowerShell"): tools.append("Bash:" + re.sub(r"\s+", " ", i.get("command", ""))[:220])
            else: tools.append(b["name"] + ":" + str(i.get("file_path", i.get("pattern", "")))[:120])
        elif b.get("type") == "text" and b.get("text", "").strip():
            tools.append("TEXT")
    rows.append((e.get("timestamp", ""), m.get("id", ""), ctx, outk, " | ".join(tools)))
with out.open("w", encoding="utf-8") as f:
    for r in rows: f.write("\t".join(map(str, r)) + "\n")
print(len(rows), "linhas")
