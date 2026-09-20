# Evidência de revisão — DIARIO_DE_OBRAS TK-62a

## Diff (`git diff --stat`)
```
.claude/projecoes.json                           |   10 +
 .claude/skills/passagem-de-bastao/SKILL.md       |   35 +-
 .claude/skills/scrum-master/SKILL.md             |   23 +-
 .claude/tools/backlog.py                         |  289 ++-
 .claude/tools/rdo.py                             |    6 +-
 CHANGELOG.md                                     |   15 +-
 GOVERNANCA.md                                    |    2 +-
 README.md                                        |   33 +-
 docs/CUSTO_DO_PICKUP.md                          |   31 +
 docs/DIARIO_DE_OBRAS.md                          |  520 ++++-
 docs/DOC_MAP.md                                  |    2 +
 docs/RDO/INDEX.md                                |    6 +
 docs/consultant-spec.md                          |   66 +
 docs/plans/P-0735-residencia-e-ponto-de-carga.md |    2 +-
 docs/plans/P-0737-loop-autonomo.md               |    2 +-
 docs/plans/P-0738-contexto-esgotado.md           |    2 +-
 docs/plans/P-0739-backlog-instrumento.md         | 2526 +++++++++++++++++++++-
 docs/plans/_INBOX.md                             |    2 +-
 docs/plans/_INBOX_HISTORICO.md                   |    1 +
 docs/telemetria.tsv                              |   40 +
 tests/test_backlog.py                            |  635 +++++-
 tests/test_rdo.py                                |   34 +
 tests/test_review_evidence.py                    |   37 +
 23 files changed, 4149 insertions(+), 170 deletions(-)
```

## Arquivos tocados
- `.claude/projecoes.json` — atribuição: alheio; estado git: ` M`
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: alheio; estado git: `??`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog.py` — atribuição: alheio; estado git: ` M`
- `.claude/tools/backlog_hook.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `CHANGELOG.md` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/CUSTO_DO_PICKUP.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/DOC_MAP.md` — atribuição: alheio; estado git: ` M`
- `docs/Entregas Aceitas/Entregas - P-0739.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T10b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T11.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T11a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T12.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0739-BKL-T9a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/TK-57-TK-57a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/laudos/P-0739-BKL-T12.md` — atribuição: alheio; estado git: `??`
- `docs/consultant-spec.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0735-residencia-e-ponto-de-carga.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0737-loop-autonomo.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0738-contexto-esgotado.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0739-backlog-instrumento.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0742-loop-fora-do-llm.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_VIABILIDADE-agente-leitor.md` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md` — atribuição: alheio; estado git: `??`
- `tests/test_backlog.py` — atribuição: alheio; estado git: ` M`
- `tests/test_rdo.py` — atribuição: da entrega; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `eb93490c23e2964d1cd865a683a7d9969809c0a0`
- Arquivos-alvo declarados: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog.py`, `.claude/tools/backlog_hook.py`, `.claude/tools/rdo.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `README.md`, `docs/CUSTO_DO_PICKUP.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/consultant-spec.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`, `tests/test_backlog.py`, `tests/test_rdo.py`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/tools/backlog.py` → `TK-59a`, `README.md` → `TK-51a`, `docs/CUSTO_DO_PICKUP.md` → `TK-58a`, `tests/test_backlog.py` → `TK-57a`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0739-BKL-T10-corpus-do-instrumento-e-a-migracao-do-diario-ate-check-verde.md`, `docs/RDO/P-0739-BKL-T10a-drain-o-inbox-de-planos-sai-do-contexto.md`, `docs/RDO/P-0739-BKL-T10b-o-bloco-gerado-da-2-3-e-projetado-inteiro-e-dentro-do-corpus.md`, `docs/RDO/P-0739-BKL-T11-o-hook-o-ponto-de-carga-e-as-skills-que-invocam-o-instrument.md`, `docs/RDO/P-0739-BKL-T11a-o-hook-fala-no-ponto-de-carga-real-stdin-em-utf-8-explicito.md`, `docs/RDO/P-0739-BKL-T9a-rodada-de-transcricao-os-tres-modulos-bkl-t10-bkl-t12.md`, `docs/RDO/evidencia/P-0739-BKL-T10.md`, `docs/RDO/evidencia/P-0739-BKL-T10a.md`, `docs/RDO/evidencia/P-0739-BKL-T10b.md`, `docs/RDO/evidencia/P-0739-BKL-T11.md`, `docs/RDO/evidencia/P-0739-BKL-T11a.md`, `docs/RDO/evidencia/P-0739-BKL-T12.md`, `docs/RDO/evidencia/P-0739-BKL-T9a.md`, `docs/RDO/evidencia/TK-57-TK-57a.md`, `docs/RDO/laudos/P-0739-BKL-T12.md`, `docs/plans/P-0735-residencia-e-ponto-de-carga.md`, `docs/plans/P-0737-loop-autonomo.md`, `docs/plans/P-0738-contexto-esgotado.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0742-loop-fora-do-llm.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/plans/_VIABILIDADE-agente-leitor.md`, `docs/telemetria.tsv`
- Fato: 13 arquivo(s) fora dos alvos e sem atribuição: `.claude/projecoes.json`, `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/backlog_hook.py`, `CHANGELOG.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, `docs/Entregas Aceitas/Entregas - P-0739.md`, `docs/consultant-spec.md`, `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0777-gama.md`, `tests/fixtures/backlog/corpus/docs/plans/P-0900-legado.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index faff493..b14d879 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -81,10 +81,12 @@ _CLASSE_ALIASES: dict[str, str] = {
     "redacao/planejamento": "redacao",
 }
 
-_ID_HEADER_RE = re.compile(r"^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?)(?=[\s—])")
+_ID_HEADER_RE = re.compile(
+    r"^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?|TK-[0-9]+[a-z]?)(?=[\s—])"
+)
 _ID_LAUDO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")  # identificador, nunca caminho
 _HEADER_BRACKET_RE = re.compile(
-    r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) "
+    r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?|TK-[0-9]+[a-z]?) — (?P<titulo>.+?) "
     r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)?"
     r"(?: · esforço (?:low|medium|high|xhigh|max))?"
     r" · classe (?P<classe>.+?)"

```

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index 3b3978a..c674741 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -747,6 +747,40 @@ def test_tr_extrair_dossie_id_casa_por_igualdade_exata(tmp_path):
         )
 
 
+def test_id_header_re_aceita_tk_subtarefa_e_recusa_nivel_dois():
+    """TK-62a (`DB-17`): `_ID_HEADER_RE` passa a reconhecer a forma `TK-<n><letra>` de subtarefa
+    de tíquete, além da gramática `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` já aceita — e continua recusando
+    o cabeçalho de nível 2 do tíquete-pai (`##`, sem bracket), que não é ID de tarefa."""
+    rdo = _load_rdo()
+
+    assert rdo._ID_HEADER_RE.match("### TK-57a — Título").group(1) == "TK-57a"
+    assert rdo._ID_HEADER_RE.match("### TK-62a — Título").group(1) == "TK-62a"
+    assert rdo._ID_HEADER_RE.match("### TK-54b — Título").group(1) == "TK-54b"
+    assert rdo._ID_HEADER_RE.match("### TK-57 — Título").group(1) == "TK-57"
+    assert rdo._ID_HEADER_RE.match("## TK-62 — Título") is None
+
+
+def test_header_bracket_re_aceita_tk_e_recusa_id_fora_da_gramatica():
+    """TK-62a (`DB-17`): `_HEADER_BRACKET_RE` reconhece `TK-<n><letra>` no grupo `id` e continua
+    recusando cabeçalho cujo texto não é ID de tarefa (`2.5`, `Achados`)."""
+    rdo = _load_rdo()
+
+    aceito = rdo._HEADER_BRACKET_RE.match(
+        "### TK-62a — Título [Sonnet · classe implementacao]"
+    )
+    recusado_numeral = rdo._HEADER_BRACKET_RE.match(
+        "### 2.5 — Título [Sonnet · classe implementacao]"
+    )
+    recusado_achados = rdo._HEADER_BRACKET_RE.match(
+        "### Achados — Título [Sonnet · classe implementacao]"
+    )
+
+    assert aceito is not None
+    assert aceito.group("id") == "TK-62a"
+    assert recusado_numeral is None
+    assert recusado_achados is None
+
+
 # --- laudo · achado de processo (BKL-T2d, RUBRICA_DE_REVISAO.md §6) ------------------------------
 
 

```

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index 8b04281..338cd73 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -191,6 +191,43 @@ def test_cli_main_ok_e_falhou(tmp_path, capsys):
     assert "review_evidence: FALHOU" in saida_falha.err
 
 
+def test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica(tmp_path, capsys):
+    """TK-62a (`DB-17`/`DB-22`): a gramática de ID mora em `rdo.py` só, e `review_evidence` reusa
+    `extrair_dossie` de lá — `--tarefa TK-62a` (subtarefa, cabeçalho `### … [modelo · classe …]`)
+    localiza e sai OK; `--tarefa TK-62` (cabeçalho de nível 2 do tíquete-pai, sem bracket) não é
+    ID de tarefa e continua recusado."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    plano.write_text(
+        "# Plano de teste\n\n"
+        "## TK-62 — Tíquete pai de teste\n\n"
+        "### TK-62a — Subtarefa sintética de teste [Sonnet · classe implementacao]\n"
+        "- **Objetivo:** validar review_evidence.py.\n"
+        "- **Arquivos-alvo:** cria `src/a.py`.\n"
+        "- **Verificação:** bateria do §3.\n"
+        "- **Pronto quando:** o teste passa.\n",
+        encoding="utf-8",
+    )
+    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
+    review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE
+
+    codigo = review_evidence.main(
+        ["--plano", str(plano), "--tarefa", "TK-62a", "--root", str(repo)]
+    )
+    saida = capsys.readouterr()
+    assert codigo == 0
+    assert "review_evidence: OK" in saida.out
+
+    codigo_falho = review_evidence.main(
+        ["--plano", str(plano), "--tarefa", "TK-62", "--root", str(repo)]
+    )
+    saida_falha = capsys.readouterr()
+    assert codigo_falho == 1
+    assert "review_evidence: FALHOU" in saida_falha.err
+
+
 def test_tf_veredito_guardas_e_testes_travam_conforme_quando_bateria_toda_verde():
     """TF da EXA-T9b: veredito mecânico das dimensões `guardas` (`RUBRICA_DE_REVISAO.md:94-106`)
     e `testes` (`RUBRICA_DE_REVISAO.md:79-92`) resolve para `conforme` quando todos os comandos

```

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 1
  ```
  kit_check: check-drift FALHOU (2 problema(s)):
    - README.md diverge do regenerado (1 linha(s) diferente(s)):
    -   [regenerado] | `entrega-de-encerramento` | Produz o documento de encerramento de um plano Pantonic* - o modelo "as-is" que mapeia cada tarefa ao contexto que a motivou, ao artefato concreto que ela criou, a um exemplo real de funcionamento e ao que ela protege, mais o estado honesto do que ficou aberto. � o artefato pelo qual o dono valida o plano. Usar ao fechar qualquer plano, antes de pedir o veredito. |
  ```
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
