# Evidência de revisão — P-0753 AF-T9

## Diff (`git diff --stat`)
```
.claude/skills/passagem-de-bastao/SKILL.md         |  5 ++
 .claude/tools/backlog.py                           | 39 +++++++--
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T9-medida.json             | 36 ++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_backlog.py                              | 98 ++++++++++++++++++++++
 7 files changed, 172 insertions(+), 11 deletions(-)
```

## Arquivos tocados
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T9-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `7afd7eb5d0217dba795080b1d5e0fcae3e0ed3a9`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`, `.claude/skills/passagem-de-bastao/SKILL.md`
- Arquivos tocados: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T9-medida.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T9-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 28ebce9..d4f4699 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -5,7 +5,7 @@ definido no card) com `arquivo:linha`; `resolver_citacao_secao` (`TK-60a`) resol
 `` `<arquivo>.md` §<N>[.<N>]* `` contra o arquivo citado, acusando `C-11` quando a seção não
 existe; `C-12` (`TK-65a`) acusa `Depende de:` fora da gramática ou citando id que não é item —
 vocabulário do instrumento fechado em `C-1..C-17`; `show` emite o dossiê verbatim de um item,
-truncado ao teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta).
+inteiro no card de tarefa; o teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta) vale para plano, notas de execução e achados.
 
 Gramática implementada (residência canônica: skill `diario-de-obras`, seção "Gramática legível
 por máquina" — replicada aqui igual, `DB-17`/`DB-18`):
@@ -1118,15 +1118,36 @@ def _bloco_achados(texto_plano: str, tarefa_id: str) -> str:
     return "\n".join(["**Achados roteados a este card:**", *entradas])
 
 
+def _card_inteiro(item: Item) -> str:
+    """AF-T9 — o card de um `Item` sai inteiro até a linha anterior a
+    `- **Notas de execução:**`; o trecho que começa nessa linha (quando existe) passa por
+    `_truncar` (teto `DB-7`)."""
+    linhas = item.texto.splitlines()
+    idx = next((i for i, l in enumerate(linhas) if NOTAS_BULLET_RE.match(l)), None)
+    if idx is None:
+        return item.texto
+    antes = "\n".join(linhas[:idx])
+    notas = "\n".join(linhas[idx:])
+    notas_truncadas = _truncar(notas, item.arquivo, item.linha_header + idx, item.linha_fim)
+    if antes:
+        return antes + "\n" + notas_truncadas
+    return notas_truncadas
+
+
 def show(modelo: Modelo, id_: str) -> str:
     alvo = _localizar(modelo, id_)
     if alvo is None:
         return f"id não encontrado: {id_}"
-    texto = _truncar(alvo.texto, alvo.arquivo, alvo.linha_header, alvo.linha_fim)
-    if isinstance(alvo, Item) and alvo.tipo == "tarefa":
-        plano = next(p for p in modelo.planos if p.id == alvo.pai)
-        return texto + "\n\n" + _bloco_achados(plano.texto, alvo.id)
-    return texto
+    if isinstance(alvo, Item):
+        texto = _card_inteiro(alvo)
+        if alvo.tipo == "tarefa":
+            plano = next(p for p in modelo.planos if p.id == alvo.pai)
+            bloco = _truncar(
+                _bloco_achados(plano.texto, alvo.id), plano.arquivo, plano.linha_header, plano.linha_fim
+            )
+            return texto + "\n\n" + bloco
+        return texto
+    return _truncar(alvo.texto, alvo.arquivo, alvo.linha_header, alvo.linha_fim)
 
 
 # --------------------------------------------------------------------------- #
@@ -1544,10 +1565,10 @@ def renderizar_next(
         linhas_saida.append(f"=== HANDOVER DE {autor.id} — {autor.titulo} ({autor.status}; {autor.arquivo})")
         linhas_saida.append(texto_handover)
 
-    linhas_saida.append("--- dossiê (verbatim, teto DB-7) ---")
-    linhas_saida.append(_truncar(item.texto, item.arquivo, item.linha_header, item.linha_fim))
+    linhas_saida.append("--- dossiê (verbatim, card inteiro) ---")
+    linhas_saida.append(_card_inteiro(item))
     if tipo_pai == "plano":
-        linhas_saida.append(_bloco_achados(pai.texto, item.id))
+        linhas_saida.append(_truncar(_bloco_achados(pai.texto, item.id), pai.arquivo, pai.linha_header, pai.linha_fim))
     linhas_saida.append("--- pendências mecânicas ---")
 
     n_inbox_planos = _contar_inbox_planos(inbox_planos) if inbox_planos is not None else 0

```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index 516490b..9a036a5 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -1133,6 +1133,104 @@ def test_tr_saida_do_next_cabe_no_teto(tmp_path):
     assert len(saida) <= 8200
 
 
+# --------------------------------------------------------------------------- #
+# AF-T9 — `next` e `show` entregam o card inteiro; só notas de execução e achados
+# seguem truncados ao teto `DB-7`.
+# --------------------------------------------------------------------------- #
+
+
+def test_tf_card_inteiro_no_next_e_no_show(tmp_path):
+    backlog = _load_backlog()
+    linhas_card = [f"- linha {i:03d} do card" for i in range(1, 151)]
+    texto = (
+        "### T1 — Título de T1 [Sonnet · classe mecanica]\n"
+        "- **Status:** `ready` · 2026-01-01\n" + "\n".join(linhas_card)
+    )
+    t1 = backlog.Item(
+        id="T1",
+        tipo="tarefa",
+        titulo="Título de T1",
+        arquivo="docs/plans/P-0001-x.md",
+        linha_header=10,
+        linha_fim=10 + len(texto.splitlines()) - 1,
+        texto=texto,
+        modelo="Sonnet",
+        classe="mecanica",
+        status="ready",
+        status_linha=11,
+        pai="P-0001",
+    )
+    p1 = backlog.Plano(
+        id="P-0001",
+        titulo="Título de P-0001",
+        arquivo="docs/plans/P-0001-x.md",
+        linha_header=1,
+        linha_fim=200,
+        texto="conteúdo qualquer",
+        status="ready",
+        tarefas=[t1],
+    )
+    indice = [
+        backlog.LinhaIndice(
+            id="P-0001",
+            titulo="Título de P-0001",
+            status_bruto="ready",
+            arquivo="docs/DIARIO_DE_OBRAS.md",
+            linha=10,
+            ancora="docs/plans/P-0001-x.md",
+        )
+    ]
+    modelo = backlog.Modelo(planos=[p1], tiquetes=[], indice=indice, diario_arquivo="docs/DIARIO_DE_OBRAS.md")
+
+    selecao = backlog.selecionar_next(modelo)
+    assert selecao.exit_code == 0
+    saida_next = backlog.renderizar_next(modelo, selecao)
+    assert "linha 150 do card" in saida_next
+    assert "… truncado (" not in saida_next
+
+    saida_show = backlog.show(modelo, "T1")
+    assert "linha 150 do card" in saida_show
+    assert "… truncado (" not in saida_show
+
+
+def test_tr_card_inteiro_notas_de_execucao_seguem_com_teto():
+    backlog = _load_backlog()
+    linhas_notas = [f"  - `in-progress` — nota {i:03d} de execução" for i in range(1, 201)]
+    texto = (
+        "### T1 — Título de T1 [Sonnet · classe mecanica]\n"
+        "- **Status:** `ready` · 2026-01-01\n"
+        "- **Notas de execução:**\n" + "\n".join(linhas_notas)
+    )
+    t1 = backlog.Item(
+        id="T1",
+        tipo="tarefa",
+        titulo="Título de T1",
+        arquivo="docs/plans/P-0001-x.md",
+        linha_header=10,
+        linha_fim=10 + len(texto.splitlines()) - 1,
+        texto=texto,
+        modelo="Sonnet",
+        classe="mecanica",
+        status="ready",
+        status_linha=11,
+        pai="P-0001",
+    )
+    p1 = backlog.Plano(
+        id="P-0001",
+        titulo="Título de P-0001",
+        arquivo="docs/plans/P-0001-x.md",
+        linha_header=1,
+        linha_fim=250,
+        texto="conteúdo qualquer",
+        status="ready",
+        tarefas=[t1],
+    )
+    modelo = backlog.Modelo(planos=[p1], tiquetes=[], indice=[], diario_arquivo="docs/DIARIO_DE_OBRAS.md")
+
+    saida = backlog.show(modelo, "T1")
+    assert "… truncado (" in saida
+
+
 # --------------------------------------------------------------------------- #
 # RP-5 — os quatro TFs fechados pela rodada de replanejamento: forma por tipo de pai
 # (DB-33), faixa de bug sobre itens elegíveis (DB-35) e antecessora omitida no primeiro

```

### `.claude/skills/passagem-de-bastao/SKILL.md`
```
diff --git a/.claude/skills/passagem-de-bastao/SKILL.md b/.claude/skills/passagem-de-bastao/SKILL.md
index 4f913aa..a53540e 100644
--- a/.claude/skills/passagem-de-bastao/SKILL.md
+++ b/.claude/skills/passagem-de-bastao/SKILL.md
@@ -76,6 +76,11 @@ vai para o papel barato — `pantonic-scout` (agente Pantonic* do projeto) ou, f
 (`.claude/global/skills/context-prep/SKILL.md`) —, nunca para leitura direta do modelo principal.
 O orquestrador monta o prompt de delegação a partir só do dossiê compacto devolvido pelo scout.
 
+**O card chega inteiro.** `backlog.py next` e `backlog.py show <ID>` imprimem o card inteiro, sem
+corte; o teto `DB-7` (8.000 caracteres ou 120 linhas, com o ponteiro `arquivo:l1-l2` de onde
+cortou) vale só para o bloco de achados roteados ao card e para as notas de execução do plano
+legado. O dossiê se copia da saída do instrumento, sem reler o plano.
+
 **Fonte do contexto, em ordem de preferência:** (1) dossiê pré-autorado (`sprint_plan.md`, card de
 plano) copiado verbatim, **inclusive o campo `Oração do modelo` com os sub-bullets de texto** (é a única forma de o executor ler o
 modelo — `GOVERNANCA.md` §3.2) — exceto números de aceite, ver gate abaixo; (2) **herança de contexto** da

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T9-medida.json; mundo: depois; gerado em: 2026-09-27T14:13:22+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog.py -q -k "card_inteiro"` | 0 | true |
| 2 | `python -c "from pathlib import Path;print(Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8').count('O card chega inteiro.'))"` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
