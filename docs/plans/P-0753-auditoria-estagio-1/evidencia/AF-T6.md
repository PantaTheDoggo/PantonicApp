# Evidência de revisão — P-0753 AF-T6

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-reviewer.md                |  2 +-
 .claude/skills/scrum-master/SKILL.md               | 11 ++---
 .claude/tools/progresso_hook.py                    |  5 ++-
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |  1 +
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/cenario.md   | 20 +++++++--
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T6-medida.json             | 50 ++++++++++++++++++++++
 docs/plans/P-0753-auditoria-estagio-1/plano.md     |  6 ++-
 docs/telemetria.tsv                                |  3 ++
 tests/test_progresso_hook.py                       | 39 +++++++++++++++--
 11 files changed, 121 insertions(+), 20 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-reviewer.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/progresso_hook.py` — atribuição: da entrega; estado git: `??`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: alheio; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/cenario.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T6-medida.json` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/plano.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_progresso_hook.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `543229bfad447cd6e899c3db8ddde29f7628cc37`
- Arquivos-alvo declarados: `.claude/agents/pantonic-reviewer.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/progresso_hook.py`, `tests/test_progresso_hook.py`
- Arquivos tocados: `.claude/agents/pantonic-reviewer.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/progresso_hook.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T6-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`, `tests/test_progresso_hook.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/cenario.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T6-medida.json`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `docs/ACIONAMENTOS_CONSULTOR.tsv`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-reviewer.md`
```
diff --git a/.claude/agents/pantonic-reviewer.md b/.claude/agents/pantonic-reviewer.md
index f27207f..fce5827 100644
--- a/.claude/agents/pantonic-reviewer.md
+++ b/.claude/agents/pantonic-reviewer.md
@@ -130,7 +130,7 @@ fazer.
 7. **Retorno ao chamador** — as duas linhas fixas e, quando houver, o dossiê:
 
    ```
-   <tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>
+   <tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma> recomendacao=<seguir|seguir com ressalva|refazer|escalar>
    laudo=<caminho>
    ```
 

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 2c6dabd..b92f951 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -151,13 +151,14 @@ Dez passos, nesta ordem.
 
 - **Gatilho:** retorno do `reviewer`.
 - **Entrada:** as duas linhas fixas e, quando houver, o dossiê anexo abaixo delas:
-  `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
+  `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma> recomendacao=<seguir|seguir com ressalva|refazer|escalar>`
   `laudo=<caminho>`
   Dossiê presente: são os seis campos do `Ato de modelo` (`GOVERNANCA.md` §3.2). O loop não o
   reescreve, não o resume e não o interpreta — passa-o inteiro ao passo 8.
-- **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do
-  laudo — calculados pelo gerador, não recalculados pelo loop. Colher a `recomendação` **do
-  laudo**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`,
+- **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante`, `recomendacao` e o
+  caminho do laudo — calculados pelo gerador e transcritos pelo revisor, não recalculados pelo
+  loop. A `recomendação` vem **da primeira linha**, campo fechado (`seguir`, `seguir com
+  ressalva`, `refazer`, `escalar`), lido por `A6`,
   `A6a`, `A8a`, `A8`, `A9` e `B1`.
 - **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.
 
@@ -377,7 +378,7 @@ ao gerente (`I-12`). Outras ferramentas, outros comandos e outros `subagent_type
 | `M-4b` | o mesmo evento, primeira linha casa `^(\S+) blocked motivo=(\S+)\s*(.*)$` | `Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.` | `<motivo>` ← grupo 2; `<razão>` ← grupo 3 |
 | `M-5` | evidência coletada — `PreToolUse` · `Bash` · numa invocação do comando o programa é `review_evidence.py`, com `--tarefa <ID>` e sem `--atribuir` nos argumentos dessa mesma invocação (`TK-88c`) | `Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.` | `<ID>` ← `--tarefa` da própria invocação; `<título>` ← estado ou `localizar_card` |
 | `M-6` | agente despachado, revisor — `PreToolUse` · `Agent` · `pantonic-reviewer` | `Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.` | `<título>` ← tarefa corrente |
-| `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · primeira linha casa `^(\S+) (\S+) (\d+)%? bloqueante=(.*)$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4 |
+| `M-7` | agente de volta, revisor — `PostToolUse` · `Agent` · `pantonic-reviewer`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · primeira linha casa `^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$` | `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>, recomendação <recomendação>.` | `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4; `<recomendação>` ← grupo 5, ou `não informada` sem o campo |
 | `M-8` | agente despachado, consultor — `PreToolUse` · `Agent` · `pantonic-consultant` | `Agente consultor recebe a tarefa "<título>" e vai triar.` | `<título>` ← tarefa corrente. A regra A-n/B-n saiu (`DTG-34`); "a parada" saiu (`DTG-48`): o consultor também é despachado por laudo, por instrumento e no marco, e o evento não diz por qual |
 | `M-9` | agente de volta, consultor — `PostToolUse` · `Agent` · `pantonic-consultant`, ou o `UserPromptSubmit` da volta em hand-back, como em `M-4` · uma linha da resposta começa, depois de brancos, por `rota=(\S+)`, e nenhuma
```
[truncado em 4000 caracteres]

### `.claude/tools/progresso_hook.py`
```
--- .claude/tools/progresso_hook.py@543229bfad447cd6e899c3db8ddde29f7628cc37
+++ .claude/tools/progresso_hook.py
@@ -53,7 +53,7 @@
     'M-4b': 'Agente executor devolveu a tarefa "<título>": blocked — motivo <motivo>: <razão>.',
     'M-5': 'Tarefa "<título>": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.',
     'M-6': 'Agente revisor recebe a tarefa "<título>" e vai confrontar a entrega com o card.',
-    'M-7': 'Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>.',
+    'M-7': 'Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>, recomendação <recomendação>.',
     'M-8': 'Agente consultor recebe a tarefa "<título>" e vai triar.',
     'M-9': 'Agente consultor devolveu a tarefa "<título>": rota <rota>.',
     'M-9b': 'Agente consultor devolveu a tarefa "<título>": rota <rota>; estratégico: <frase>.',
@@ -221,13 +221,14 @@
         if m:
             return [frase("M-4b", {"<título>": titulo, "<motivo>": m.group(2), "<razão>": m.group(3)})]
     elif sub == "pantonic-reviewer":
-        m = re.match(r"^(\S+) (\S+) (\d+)%? bloqueante=(.*)$", l1)
+        m = re.match(r"^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$", l1)
         if m:
             return [frase("M-7", {
                 "<título>": titulo,
                 "<veredito>": m.group(2),
                 "<percentual>": m.group(3),
                 "<bloqueante>": m.group(4),
+                "<recomendação>": (m.group(5) or "").strip() or "não informada",
             })]
     elif sub == "pantonic-consultant":
         mr = re.search(r"^\s*rota=(\S+)", texto, re.M)

```

### `tests/test_progresso_hook.py`
```
--- tests/test_progresso_hook.py@543229bfad447cd6e899c3db8ddde29f7628cc37
+++ tests/test_progresso_hook.py
@@ -296,15 +296,46 @@
           tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100 bloqueante=nenhuma"}]})
     rodar(p, estado, raiz)
     assert progresso(estado)[-1] == (
-        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.'
+        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.'
     )
     rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
             tool_input={"subagent_type": "pantonic-reviewer"},
             tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100% bloqueante=nenhuma"}]}),
           estado, raiz)
     assert progresso(estado)[-2:] == [
-        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.'
+        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.'
     ] * 2
+
+
+def test_tf_m7_revisor_com_recomendacao(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+    p = P(hook_event_name="PostToolUse", tool_name="Agent",
+          tool_input={"subagent_type": "pantonic-reviewer"},
+          tool_response={"content": [{"type": "text",
+                                       "text": "TLG-T9 ressalva 91 bloqueante=nenhuma recomendacao=seguir com ressalva"}]})
+    rodar(p, estado, raiz)
+    assert progresso(estado)[-1] == (
+        'Agente revisor devolveu a tarefa "Um título de teste": ressalva 91%, bloqueante nenhuma, '
+        'recomendação seguir com ressalva.'
+    )
+
+
+def test_tr_m7_revisor_sem_recomendacao_diz_nao_informada(estado, raiz):
+    rodar(payload_next(
+        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
+        "- **Objetivo:** Fazer x.\n"
+    ), estado, raiz)
+    p = P(hook_event_name="PostToolUse", tool_name="Agent",
+          tool_input={"subagent_type": "pantonic-reviewer"},
+          tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100 bloqueante=nenhuma"}]})
+    rodar(p, estado, raiz)
+    assert progresso(estado)[-1] == (
+        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, '
+        'recomendação não informada.'
+    )
 
 
 # --- TF-GER-8 -------------------------------------------------------------------------
@@ -693,7 +724,7 @@
     ))
     rodar(p3, estado, raiz)
     assert progresso(estado) == [
-        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.'
+        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.'
     ]
 
     e2 = raiz / "estado_consultor"
@@ -966,7 +997,7 @@
         n17,
         'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.',
         'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.',
-        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.',
+        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.',
         'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, '
         "RDO e telemetria.",
         'Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. '

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T6-medida.json; mundo: depois; gerado em: 2026-09-27T13:18:56+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_progresso_hook.py -q -k "recomendacao"` | 0 | true |
| 2 | `python -c "from pathlib import Path;print(sum(Path(p).read_text(encoding='utf-8').count('recomendacao=<') for p in ['.claude/agents/pantonic-reviewer.md','.claude/skills/scrum-master/SKILL.md']))"` | 0 | true |
| 3 | `python -c "from pathlib import Path;t=sum(Path(p).read_text(encoding='utf-8').count('recomendação <recomendação>') for p in ['.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md']);print(t)"` | 0 | true |
| 4 | `python -m pytest tests/test_encerrar.py -q -k "tarefa_fecha_num_ato"` | 0 | true |
| 5 | `python -m pytest -q` | 0 | true |
| 6 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
