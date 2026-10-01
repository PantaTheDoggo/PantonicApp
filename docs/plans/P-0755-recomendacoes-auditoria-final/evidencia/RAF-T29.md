# Evidência de revisão — P-0755 RAF-T29

## Diff (`git diff --stat`)
```
.claude/tools/backlog.py                           | 52 +++++++++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T29-medida-depois.json    | 15 ++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_backlog.py                              | 60 ++++++++++++++++++++++
 6 files changed, 131 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/tools/backlog.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T29-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_backlog.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `57a8d0e3202e35cd8291fff6747224f234e9a4e1`
- Arquivos-alvo declarados: `.claude/tools/backlog.py`, `tests/test_backlog.py`
- Arquivos tocados: `.claude/tools/backlog.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T29-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_backlog.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T29-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/backlog.py`
```
diff --git a/.claude/tools/backlog.py b/.claude/tools/backlog.py
index 63ef637..40b395e 100644
--- a/.claude/tools/backlog.py
+++ b/.claude/tools/backlog.py
@@ -110,6 +110,9 @@ _BRACKET_DETALHE_RE = re.compile(
 PLANO_HEADER_RE = _caminhos.PLANO_HEADER_RE
 STATUS_CAMPO_RE = re.compile(r"\*\*Status:\*\* `([a-z-]+)`")
 PREFIXO_CAMPO_RE = re.compile(r"\*\*Prefixo das tarefas no diário:\*\* `([A-Za-z0-9]+)-T<n>`")
+# R-28 / DRF-29 (`P-0755`) — prefixo de decisão declarado no cabeçalho do plano; citar prefixo
+# alheio no corpo do texto não casa este padrão (exige o rótulo do campo, não a ocorrência).
+PREFIXO_DECISOES_RE = re.compile(r"\*\*Prefixo das decisões:\*\* `([A-Za-z0-9]+)-<n>`")
 ORDEM_CAMPO_RE = re.compile(r"\*\*Ordem de execução:\*\* (.+)$")
 
 HEADING_RE = re.compile(r"^(#{2,3}) (\S+) — (.*)$")
@@ -199,6 +202,8 @@ class Plano:
     estado_ids: list[tuple[str, int]] = field(default_factory=list)
     estado_defeitos: list[tuple[int, str]] = field(default_factory=list)
     status_no_texto: int | None = None
+    prefixo_decisoes: str | None = None
+    prefixo_decisoes_linha: int | None = None
 
 
 @dataclass
@@ -481,6 +486,8 @@ def _parse_plano(caminho: Path, repo: Path) -> Plano:
     status: str | None = None
     status_linha: int | None = None
     prefixo: str | None = None
+    prefixo_decisoes: str | None = None
+    prefixo_decisoes_linha: int | None = None
     ordem: list[str] = []
     for i, linha in enumerate(linhas[:20], start=1):
         if linha.lstrip().startswith("-"):
@@ -495,6 +502,10 @@ def _parse_plano(caminho: Path, repo: Path) -> Plano:
             mp = PREFIXO_CAMPO_RE.search(linha)
             if mp:
                 prefixo = mp.group(1)
+        if prefixo_decisoes is None:
+            mpd = PREFIXO_DECISOES_RE.search(linha)
+            if mpd:
+                prefixo_decisoes, prefixo_decisoes_linha = mpd.group(1), i
         if not ordem:
             mo = ORDEM_CAMPO_RE.search(linha)
             if mo:
@@ -514,6 +525,8 @@ def _parse_plano(caminho: Path, repo: Path) -> Plano:
         status=status,
         status_linha=status_linha,
         prefixo=prefixo,
+        prefixo_decisoes=prefixo_decisoes,
+        prefixo_decisoes_linha=prefixo_decisoes_linha,
         ordem_execucao=ordem,
         tarefas=tarefas,
     )
@@ -699,6 +712,43 @@ def _dossie_check(item: Item, repo: Path | None, dossie: bool, violacoes: list[V
         violacoes.append(Violacao("C-16", item.arquivo, item.linha_header, str(exc)))
 
 
+def _numero_do_plano(plano: Plano) -> tuple[int, str]:
+    """Chave de ordenação de dono de prefixo (`C-18`, `R-28`/`DRF-29` do `P-0755`): plano com id
+    `P-<n>` ordena pelo número; id fora desse formato (legado sem numeração `P-`) vai para o
+    fim, desempatado pelo próprio id."""
+    m = re.match(r"^P-(\d+)", plano.id)
+    if m:
+        return int(m.group(1)), plano.id
+    return 10**9, plano.id
+
+
+def _prefixo_decisoes_checks(modelo: Modelo, violacoes: list[Violacao]) -> None:
+    """C-18 (`R-28`, `DRF-29` do `P-0755`): dois ou mais planos que declaram o mesmo
+    `**Prefixo das decisões:**` colidem — o dono do prefixo é o plano de menor `_numero_do_plano`,
+    e cada outro plano vivo do grupo é acusado, nomeando o dono. Citar o prefixo de outro plano
+    no corpo do texto não é declará-lo: só a linha do campo, casada por `PREFIXO_DECISOES_RE`,
+    conta aqui."""
+    grupos: dict[str, list[Plano]] = {}
+    for plano in modelo.planos:
+        if plano.prefixo_decisoes is not None:
+            grupos.setdefault(plano.prefixo_decisoes, []).append(plano)
+    for prefixo, planos_grupo in grupos.items():
+        if len(planos_grupo) < 2:
+            continue
+        dono = min(planos_grupo, key=_numero_do_plano)
+        for plano in planos_grupo:
+            if plano is dono or plano.fora_do_corpus:
+                continue
+            violacoes.append(
+                Violacao(
+                    "C-18",
+                    plano.arquivo,
+     
```
[truncado em 4000 caracteres]

### `tests/test_backlog.py`
```
diff --git a/tests/test_backlog.py b/tests/test_backlog.py
index b3552ea..68daf96 100644
--- a/tests/test_backlog.py
+++ b/tests/test_backlog.py
@@ -3524,3 +3524,63 @@ def test_tr_drain_aviso_diretiva_com_id_vivo_ou_drenado_cala(tmp_path, capsys):
     repo_drenado = _repo_drain_com_diretiva(tmp_path / "drenado", "`P-0800`")
     assert backlog.main(["drain", "--repo", str(repo_drenado), "--data", "2026-09-28"]) == 0
     assert "drain: aviso" not in capsys.readouterr().err
+
+
+# --------------------------------------------------------------------------- #
+# RAF-T29 (`DRF-29`, `F-23`/`F-24` do `P-0755`) — `check` recusa o plano que declara o mesmo
+# `**Prefixo das decisões:**` já declarado por outro plano do corpus, nomeando o plano dono (o
+# de menor id); citar o prefixo de outro plano no corpo do texto continua permitido.
+# --------------------------------------------------------------------------- #
+
+
+def _repo_prefixos_de_decisao(tmp_path: Path, prefixo_beta: str, texto_beta: str = "") -> Path:
+    repo = _copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")
+    plans_dir = repo / "docs" / "plans"
+    alfa = (
+        "# P-0800 — Plano P-0800-alfa.md\n"
+        "\n"
+        "**Status:** `ready` · **Prefixo das tarefas no diário:** `ALF-T<n>` · "
+        "**Prefixo das decisões:** `DSA-<n>`\n"
+    )
+    (plans_dir / "P-0800-alfa.md").write_text(alfa, encoding="utf-8")
+    beta_linhas = [
+        "# P-0801 — Plano P-0801-beta.md",
+        "",
+        "**Status:** `ready` · **Prefixo das tarefas no diário:** `BET-T<n>` · "
+        f"**Prefixo das decisões:** `{prefixo_beta}-<n>`",
+        "",
+    ]
+    if texto_beta:
+        beta_linhas.append(texto_beta)
+    (plans_dir / "P-0801-beta.md").write_text("\n".join(beta_linhas) + "\n", encoding="utf-8")
+    return repo
+
+
+def test_tf_check_prefixo_de_decisao_repetido_recusa(tmp_path, capsys):
+    """TF da RAF-T29: `P-0801` declara `DSA`, o mesmo prefixo já declarado por `P-0800` — `check`
+    sai 1 com uma linha `C-18` no `P-0801` nomeando o dono `P-0800`; o dono não é acusado."""
+    backlog = _load_backlog()
+    repo = _repo_prefixos_de_decisao(tmp_path, "DSA")
+
+    assert backlog.main(["check", "--repo", str(repo)]) == 1
+
+    linhas = capsys.readouterr().out.splitlines()
+    assert any(
+        l.startswith("C-18 docs/plans/P-0801-beta.md:3 — ")
+        and "P-0801: prefixo de decisão 'DSA' já declarado por P-0800" in l
+        for l in linhas
+    )
+    assert not any(l.startswith("C-18 docs/plans/P-0800-alfa.md") for l in linhas)
+
+
+def test_tr_check_prefixo_de_decisao_citado_nao_e_colisao(tmp_path, capsys):
+    """TR da RAF-T29: `P-0801` declara `DSB` (prefixo próprio, sem colisão) e cita `` `DSA-3` ``
+    de `P-0800` no corpo — nenhuma linha `C-18`; a regra concorrente, contar ocorrência de
+    prefixo no texto, acusaria aqui."""
+    backlog = _load_backlog()
+    repo = _repo_prefixos_de_decisao(tmp_path, "DSB", texto_beta="Aplica a `DSA-3` do P-0800.")
+
+    backlog.main(["check", "--repo", str(repo)])
+
+    saida = capsys.readouterr().out
+    assert "C-18" not in saida

```

## Linhas removidas dos testes
### `tests/test_backlog.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T29-medida-depois.json; mundo: depois; gerado em: 2026-09-30T00:26:09+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_backlog.py -q -k prefixo_de_decisao` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 1
  ```
  docs\audits\sonda-2026-09-28\passos.py:13: docs.audits.sonda-2026-09-28.passos.passo (function) - sem chamador de producao alcancavel
  dead_code: FALHOU - 1 achado(s) de simbolo de producao sem chamador.
  ```
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
