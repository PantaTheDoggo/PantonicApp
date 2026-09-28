# Evidência de revisão — P-0753 AF-T8

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md                 |  6 ++-
 .claude/skills/diario-de-obras/SKILL.md            |  6 ++-
 .claude/tools/backlog.py                           | 14 +++++-
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T8-medida.json             | 50 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 .../backlog/esqueleto/docs/DIARIO_DE_OBRAS.md      |  6 +++
 .../esqueleto/docs/plans/P-0-esboco/estado.tsv     |  2 +
 .../esqueleto/docs/plans/P-0-esboco/plano.md       |  3 ++
 .../backlog/esqueleto/docs/plans/_INBOX.md         |  1 +
 tests/test_backlog.py                              | 33 ++++++++++++++
 12 files changed, 118 insertions(+), 8 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T8-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/esqueleto/docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/estado.tsv` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/plano.md` — atribuição: da entrega; estado git: `??`
- `tests/fixtures/backlog/esqueleto/docs/plans/_INBOX.md` — atribuição: da entrega; estado git: `??`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `20a8373692039fc23f867e08b5577459ca03fd10`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`, `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/plano.md`, `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/estado.tsv`, `tests/fixtures/backlog/esqueleto/docs/plans/_INBOX.md`, `tests/fixtures/backlog/esqueleto/docs/DIARIO_DE_OBRAS.md`, `.claude/agents/pantonic-planner.md`, `.claude/skills/diario-de-obras/SKILL.md`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T8-medida.json`, `docs/telemetria.tsv`, `tests/fixtures/backlog/esqueleto/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/estado.tsv`, `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/plano.md`, `tests/fixtures/backlog/esqueleto/docs/plans/_INBOX.md`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T8-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 6744b40..ce4e73d 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -594,6 +594,13 @@ def _celula_indice(bruto: str) -> tuple[str, bool, str | None]:
     return primeiro, True, None
 
 
+def _plano_em_esboco(plano: Plano, texto_inbox: str) -> bool:
+    """Domínio (`AF-T8`): plano em pasta cujo `estado.tsv` tem, depois do cabeçalho, uma linha
+    só — a do plano, `blocked` — e nenhuma linha de `docs/plans/_INBOX.md` cita o caminho dele.
+    É o estado entre a Fase 3a e a Fase 5 do planejador."""
+    return plano.status == "blocked" and not plano.estado_ids and plano.arquivo not in texto_inbox
+
+
 def _status_do_id(modelo: Modelo, id_: str) -> str | None:
     for plano in modelo.planos:
         if plano.id == id_:
@@ -828,7 +835,10 @@ def check(
         # todo arquivo do glob, vivo ou não — DB-38). Nunca contra os ids mencionados no
         # próprio texto do inbox: plano criado sem linha de inbox não aparece lá, e é
         # exatamente esse o caso medido que motivou a violação.
-        for i, linha_inbox in enumerate(inbox_planos.read_text(encoding="utf-8").splitlines(), start=1):
+        # AF-T8: o plano em esboço cujo id é o do contador não entra em `ids_planos` — ele
+        # ainda não tem linha no inbox nem tarefa registrada (Domínio, `_plano_em_esboco`).
+        texto_inbox = inbox_planos.read_text(encoding="utf-8")
+        for i, linha_inbox in enumerate(texto_inbox.splitlines(), start=1):
             m = _CONTADOR_INBOX_ID_RE.search(linha_inbox)
             if m is None:
                 continue
@@ -836,7 +846,7 @@ def check(
             ids_planos: list[int] = []
             for p in modelo.planos:
                 mid = _ID_PLANO_RE.match(p.id)
-                if mid:
+                if mid and not (int(mid.group(1)) == contador and _plano_em_esboco(p, texto_inbox)):
                     ids_planos.append(int(mid.group(1)))
             # Sem plano presente (projeto novo, `DSA-14`), todo contador vale, `P-0` inclusive.
             if ids_planos and contador <= max(ids_planos):

```

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index abf89e2..63c9fdc 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -37,6 +37,7 @@ _FIXTURE_CONTADOR_INBOX = _FIXTURES / "contador_inbox"
 _FIXTURE_CITACAO_SECAO = _FIXTURES / "citacao_secao"
 _FIXTURE_CANDIDATO_A_FECHAMENTO = _FIXTURES / "candidato_a_fechamento"
 _FIXTURE_PASTA = _FIXTURES / "pasta"
+_FIXTURE_ESQUELETO = _FIXTURES / "esqueleto"
 
 
 def _load_backlog():
@@ -444,6 +445,38 @@ def test_tr_c10_contador_do_inbox_aponta_para_id_livre_nao_dispara(tmp_path):
     assert not any(v.codigo == "C-10" for v in violacoes)
 
 
+# --------------------------------------------------------------------------- #
+# TF/TR AF-T8 — plano em esboço (fixture `esqueleto`): `estado.tsv` só com a linha do
+# plano, `blocked`, e nenhuma linha do inbox citando o caminho dele. O contador do
+# `_INBOX.md` aponta para o mesmo id do plano em esboço — `C-10` não acusa enquanto o
+# plano segue nesse estado; volta a acusar assim que uma linha de tarefa entra no
+# `estado.tsv` (o plano deixou de ser esboço).
+# --------------------------------------------------------------------------- #
+
+
+def test_tf_check_aceita_plano_em_esqueleto(tmp_path):
+    backlog = _load_backlog()
+    repo = _copiar_fixture(_FIXTURE_ESQUELETO, tmp_path / "repo")
+
+    modelo = backlog.carregar(repo)
+    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md", repo=repo)
+
+    assert violacoes == []
+
+
+def test_tr_check_esqueleto_com_linha_de_tarefa_segue_acusando_c10(tmp_path):
+    backlog = _load_backlog()
+    repo = _copiar_fixture(_FIXTURE_ESQUELETO, tmp_path / "repo")
+    estado_path = repo / "docs" / "plans" / "P-0-esboco" / "estado.tsv"
+    with estado_path.open("a", encoding="utf-8", newline="\n") as f:
+        f.write("ESB-T1\ttarefa\tblocked\tdependencia\t2026-09-27\t-\n")
+
+    modelo = backlog.carregar(repo)
+    violacoes = backlog.check(modelo, inbox_planos=repo / "docs" / "plans" / "_INBOX.md", repo=repo)
+
+    assert any(v.codigo == "C-10" for v in violacoes)
+
+
 # --------------------------------------------------------------------------- #
 # TF/TR C-12 (TK-65a) — `Depende de:` só com ids de item, na gramática publicada
 # `` `ID`[, `ID`] ``. Caso medido: o `P-0741` com `Depende de` citando ids de decisão do

```

### `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/plano.md`
```
# P-0 — Plano em esboço

**Prefixo das tarefas no diário:** `ESB-T<n>`

```

### `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/estado.tsv`
```
id	tipo	status	razao	data	nota
P-0	plano	blocked	dependencia	2026-09-27	aguarda o modelo

```

### `tests/fixtures/backlog/esqueleto/docs/plans/_INBOX.md`
```
**Próximo id de plano: P-0.**

```

### `tests/fixtures/backlog/esqueleto/docs/DIARIO_DE_OBRAS.md`
```
# Diário de Obras (fixture pasta)

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|

```

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index e4ce940..4d328d7 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -173,7 +173,9 @@ que chega ao dono durante a execução é sintoma dessa falha. Respondida a roda
 
 ### Fase 3a — Esqueleto e dossiê (SAÍDA 3)
 
-Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1 e sem a §5**, com o esqueleto fixo, nesta ordem:
+Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1 e sem a §5**, com o esqueleto fixo abaixo, e,
+no mesmo ato, `estado.tsv` na mesma pasta com o cabeçalho e só a linha do plano, `blocked`, razão
+`dependencia` — a linha do `_INBOX.md` e o contador ficam para a Fase 5. O esqueleto, nesta ordem:
 
 ```
 # P-<n> — <título>            (cabeçalho: data de origem, iniciativa, plano de origem se derivado)
@@ -419,7 +421,7 @@ rebase que absorve fase de outro plano mapeia **tarefa a tarefa**, nunca fase a
 
 Com a §1 e a §5 na árvore, rode `python .claude/tools/modelo.py check --plano <plano>` (exit `0`)
 e, para todo card, `card_check` exit `0` como condição de registro, ao lado de `modelo.py check`;
-grave `estado.tsv` na pasta do plano (linha do plano e uma linha por card, esquema da skill `diario-de-obras`), apense a linha ao `_INBOX.md` e atualize o próximo id no mesmo ato; invoque `checar-versao-kit`; se o plano é derivado de outro, classifique (A/B/C) e
+complete o `estado.tsv` da pasta do plano com uma linha por card (esquema da skill `diario-de-obras`; a linha do plano já está lá desde a Fase 3a), apense a linha ao `_INBOX.md` e atualize o próximo id no mesmo ato; invoque `checar-versao-kit`; se o plano é derivado de outro, classifique (A/B/C) e
 aplique o efeito ao plano de origem (skill `diario-de-obras`, "Planos derivados"). Então **pare**:
 plano registrado é fim do turno (Regra 1 global) — a execução começa em outro contexto, por
 instrução explícita do dono.

```

### `.claude/skills/diario-de-obras/SKILL.md`
```
diff --git a/.claude/skills/diario-de-obras/SKILL.md b/.claude/skills/diario-de-obras/SKILL.md
index 6f1f613..b4a8a29 100644
--- a/.claude/skills/diario-de-obras/SKILL.md
+++ b/.claude/skills/diario-de-obras/SKILL.md
@@ -203,8 +203,10 @@ Contador: `**Próximo id de plano: P-<n>.**` — `drain` o recalcula como `max(i
 `id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota`; depois uma linha por item, estado corrente,
 reescrita no lugar. `id` = `P-<n>` na linha do plano (a primeira) ou o id da tarefa; `tipo` ∈
 {`plano`, `tarefa`}; `status` no vocabulário acima; `razao` ∈ {`-`, `dependencia`, `premissa`};
-`data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo ao registrar
-o plano; depois só `backlog.py status` o reescreve. `check` acusa `C-13` (card sem linha, linha
+`data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo na Fase 3a,
+junto do esqueleto, só com a linha do plano (`blocked`, razão `dependencia`), e acrescenta uma
+linha por card ao registrar o plano; depois só `backlog.py status` o reescreve. `check` acusa
+`C-13` (card sem linha, linha
 sem card, arquivo ausente ou fora do esquema) e `C-14` (linha `**Status:**` em `plano.md`).
 Busca sem leitura: `rg "^<id>\t" docs/plans/*/estado.tsv`.
 

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T8-medida.json; mundo: depois; gerado em: 2026-09-27T13:54:18+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` | 0 | true |
| 2 | `python -m pytest tests/test_backlog.py -q -k "esqueleto"` | 0 | true |
| 3 | `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('no mesmo ato, '+c+'estado.tsv'+c),t.count('a linha do plano já está lá desde a Fase 3a'))"` | 0 | true |
| 4 | `python -c "from pathlib import Path;t=Path('.claude/skills/diario-de-obras/SKILL.md').read_text(encoding='utf-8');print(t.count('O planejador grava o arquivo ao registrar'),t.count('O planejador grava o arquivo na Fase 3a'))"` | 0 | true |
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
