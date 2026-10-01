"""Agrupa turnos por mensagem e classifica cada turno da orquestração pelo passo P1..P10 do scrum-master."""
import sys, re
from collections import OrderedDict, defaultdict
src, ini_pat, fim_pat = sys.argv[1], sys.argv[2], sys.argv[3]
msgs = OrderedDict()
for l in open(src, encoding="utf-8"):
    ts, mid, ctx, out, tools = (l.rstrip("\n").split("\t") + [""])[:5]
    d = msgs.setdefault(mid, {"ts": ts, "ctx": int(ctx), "out": int(out), "tools": []})
    if tools: d["tools"].append(tools)
lst = list(msgs.values())
i0 = next(i for i, m in enumerate(lst) if re.search(ini_pat, " ".join(m["tools"])))
i1 = max(i for i, m in enumerate(lst) if re.search(fim_pat, " ".join(m["tools"])))
def passo(t):
    if "pantonic-executor" in t: return "P4"
    if "pantonic-reviewer" in t: return "P6"
    if "pantonic-consultant" in t: return "P8"
    if "encerrar.py handover" in t or "encerrar.py tarefa" in t: return "P9"
    if "status (AUF|SA)" in t and "review" in t: return "P5+P6"
    if "despachar" in t: return "P2+P3"
    if "backlog.py next" in t: return "P2"
    if re.search(r"grep -n|--co -q|wc -l", t) and "laudo" not in t: return "P3"
    if "laudos/" in t or "Achado de processo" in t: return "P7+P8"
    if "SendMessage" in t or "ToolSearch" in t: return "outro"
    if t.strip() in ("TEXT", ""): return "texto"
    return "outro"
agg = defaultdict(lambda: [0, 0, 0])
por_tarefa = defaultdict(lambda: [0, 0, 0])
tarefa = None
for m in lst[i0:i1 + 1]:
    t = " | ".join(m["tools"])
    mm = re.search(r"despachar (AUF-T\d+)", t)
    if mm: tarefa = mm.group(1)
    p = passo(t.replace("TEXT | ", "").replace(" | TEXT", ""))
    a = agg[p]; a[0] += 1; a[1] += m["ctx"]; a[2] += m["out"]
    b = por_tarefa[tarefa]; b[0] += 1; b[1] += m["ctx"]; b[2] += m["out"]
tot = [sum(v[k] for v in agg.values()) for k in range(3)]
print("janela:", lst[i0]["ts"], "->", lst[i1]["ts"], "turnos", tot[0], "ctx_k %.1f" % (tot[1]/1000), "out_k %.1f" % (tot[2]/1000))
for p in sorted(agg): print("%-7s turnos=%3d ctx_k=%8.1f out_k=%6.1f" % (p, agg[p][0], agg[p][1]/1000, agg[p][2]/1000))
ts = [v for k, v in por_tarefa.items() if k]
print("por tarefa: n=%d turnos medio=%.1f ctx_k medio=%.1f min_turnos=%d max_turnos=%d" % (len(ts), sum(v[0] for v in ts)/len(ts), sum(v[1] for v in ts)/len(ts)/1000, min(v[0] for v in ts), max(v[0] for v in ts)))
