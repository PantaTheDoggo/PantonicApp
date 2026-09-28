# Evidência de revisão — P-0753 AF-T12

## Diff (`git diff --stat`)
```
.claude/tools/encerrar.py                          | 133 +++++++++++++++++++-
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T12-medida.json            |  36 ++++++
 docs/telemetria.tsv                                |   1 +
 tests/test_encerrar.py                             | 138 +++++++++++++++++++++
 6 files changed, 310 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T12-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `a72cc670d277cc2ac4b22beafa3f6e3cdcd9491d`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T12-medida.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T12-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
--- .claude/tools/encerrar.py@a72cc670d277cc2ac4b22beafa3f6e3cdcd9491d
+++ .claude/tools/encerrar.py
@@ -902,6 +902,116 @@
 
 
 # --------------------------------------------------------------------------- #
+# marco — OP-12: o veredito do dono em todos os lugares onde o marco aparece
+# --------------------------------------------------------------------------- #
+
+
+_MARCO_SECAO0_RE = re.compile(r"^## 0\.")
+_MARCO_HEADING_RE = re.compile(r"^## ")
+_MARCO_VERSAO_PENDENTE_RE = re.compile(r"^## 1A\. Modelo conceitual — versão pendente de validação")
+
+
+def gravar_marco(
+    repo: Path,
+    plano_path: Path,
+    *,
+    marco: int,
+    resultado: str,
+    veredito: str,
+    data: str,
+    aceita_versao: str | None = None,
+    recusa_versao: str | None = None,
+) -> str | None:
+    """OP-12 — grava o veredito do dono nos lugares do marco (`DAF-27`): a última célula da
+    linha `| **Marco <n>** |` da tabela de marcos, o fim da seção `## 0.` e, só quando
+    `--marco 1 --resultado go` encontra o plano em `blocked`, a transição para `ready`. Todas
+    as checagens correm antes de qualquer escrita. Devolve o dossiê `Ato: emenda` (com
+    `--aceita-versao`/`--recusa-versao`) ou `None`."""
+    plano_path = Path(plano_path)
+    if not plano_path.is_file():
+        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")
+
+    linhas = plano_path.read_text(encoding="utf-8").splitlines()
+
+    padrao_marco = re.compile(rf"^\|\s*\*\*Marco {marco}\*\*\s*\|")
+    idx_marco = next((i for i, l in enumerate(linhas) if padrao_marco.match(l)), None)
+    if idx_marco is None:
+        raise EncerramentoError(f"linha do Marco {marco} ausente na tabela de marcos")
+
+    idx_secao0 = next((i for i, l in enumerate(linhas) if _MARCO_SECAO0_RE.match(l)), None)
+    if idx_secao0 is None:
+        raise EncerramentoError("seção ## 0 ausente")
+
+    if (aceita_versao is not None or recusa_versao is not None) and not any(
+        _MARCO_VERSAO_PENDENTE_RE.match(l) for l in linhas
+    ):
+        raise EncerramentoError("plano sem versão pendente (## 1A)")
+
+    idx_prox_heading = next(
+        (i for i in range(idx_secao0 + 1, len(linhas)) if _MARCO_HEADING_RE.match(linhas[i])),
+        len(linhas),
+    )
+
+    plano_id = _caminhos.id_do_plano(plano_path)
+    if plano_id is None:
+        raise EncerramentoError(f"plano: '{plano_path}' não tem id de plano no nome (P-<n>)")
+    modelo = _backlog.carregar(repo)
+    plano = _backlog._localizar(modelo, plano_id)
+    if not isinstance(plano, _backlog.Plano):
+        raise EncerramentoError(f"plano: '{plano_id}' não está no backlog carregado de '{repo}'")
+
+    # --- checagens concluídas; escritas a partir daqui -----------------------------------
+    frase = veredito.strip()
+    frase_celula = frase.replace("|", "\\|")
+    partes = linhas[idx_marco].split("|")
+    partes[-2] = f' {resultado} · {data} — "{frase_celula}" '
+    linhas[idx_marco] = "|".join(partes)
+
+    bloco_secao0 = [
+        f"**Marco {marco}, {data} — veredito do dono ({resultado}):**",
+        "",
+        f"> {frase}",
+        "",
+    ]
+    linhas[idx_prox_heading:idx_prox_heading] = bloco_secao0
+
+    _escrever_atomico(plano_path, "\n".join(linhas) + "\n")
+
+    if marco == 1 and resultado == "go" and plano.status == "blocked":
+        resultado_status = _backlog.transacionar_status(
+            repo, modelo, plano_id, "ready", nota=f"Marco {marco} go em {data}"
+        )
+        if resultado_status.exit_code != 0:
+            raise EncerramentoError(f"status: {resultado_status.mensagem}")
+
+    if aceita_versao is None and recusa_versao is None:
+        return None
+
+    k = aceita_versao if aceita_versao is not None else recusa_versao
+    if aceita_versao is not None:
+        fato_novo = f"o dono aceitou a versão {k} do modelo no Marco {marco}."
+        restricao = (
+            f"a versão {k} passa a vigente e a anterior a obsoleta; o conteúdo da obsoleta sa
```
[truncado em 4000 caracteres]

### `tests/test_encerrar.py`
```
--- tests/test_encerrar.py@a72cc670d277cc2ac4b22beafa3f6e3cdcd9491d
+++ tests/test_encerrar.py
@@ -590,3 +590,141 @@
 
     with pytest.raises(encerrar.EncerramentoError, match="contrato"):
         encerrar.montar_handover("2026-09-26", "x", "  ")
+
+
+# --- marco -------------------------------------------------------------------------------------
+
+
+DIARIO_MARCO = (
+    "# Diário de Obras — Teste\n"
+    "**Diretiva de priorização:** Priorize `P-0001`.\n"
+    "\n"
+    "<!-- fila:gerada -->\n"
+    "**Fila corrente:** —\n"
+    "<!-- /fila:gerada -->\n"
+    "\n"
+    "## Índice\n"
+    "\n"
+    "| ID | Título | Status | Âncora |\n"
+    "|---|---|---|---|\n"
+    "| P-0001 | Plano marco | blocked 0/1 | docs/plans/P-0001-marco.md |\n"
+)
+
+PLANO_MARCO = (
+    "# P-0001 — Plano marco\n"
+    "\n"
+    "**Status:** `blocked` · **Prefixo das tarefas no diário:** `MRC-T<n>`\n"
+    "\n"
+    "**Marcos de validação pelo dono:**\n"
+    "\n"
+    "| marco | o que o dono lê | veredito |\n"
+    "|---|---|---|\n"
+    "| **Marco 1** | a seção 1 | pendente |\n"
+    "\n"
+    "## 0. O problema, verbatim\n"
+    "\n"
+    "Texto do problema, verbatim.\n"
+    "\n"
+    "## 1A. Modelo conceitual — versão pendente de validação\n"
+    "\n"
+    "Rascunho da versão pendente.\n"
+    "\n"
+    "## 5. Tarefas\n"
+    "\n"
+    "### MRC-T1 — Tarefa única [Sonnet · classe implementacao]\n"
+    "- **Status:** `review` · 2026-09-20\n"
+    "- **Objetivo:** entregar algo.\n"
+    "- **Arquivos-alvo:** `a.py`.\n"
+    "- **Verificação:** `pytest -q`.\n"
+    "- **Pronto quando:** o teste passa.\n"
+)
+
+
+def _montar_repo_marco(tmp_path: Path, plano_texto: str = PLANO_MARCO) -> Path:
+    repo = tmp_path / "repo"
+    (repo / "docs" / "plans").mkdir(parents=True)
+    (repo / "docs" / "DIARIO_DE_OBRAS.md").write_text(DIARIO_MARCO, encoding="utf-8")
+    (repo / "docs" / "plans" / "P-0001-marco.md").write_text(plano_texto, encoding="utf-8")
+    return repo
+
+
+def _argv_marco(repo: Path, **extra: str) -> list[str]:
+    argv = [
+        "marco", "--plano", str(repo / "docs" / "plans" / "P-0001-marco.md"),
+        "--repo", str(repo), "--data", "2026-09-26",
+    ]
+    for flag, valor in extra.items():
+        argv += [flag, valor]
+    return argv
+
+
+def test_tf_marco_go_grava_celula_zero_e_tira_de_blocked(tmp_path):
+    """TF (AF-T12): `marco --marco 1 --resultado go` grava a última célula da linha do marco,
+    acrescenta o veredito ao fim da `## 0.` e, achando o plano em `blocked`, tira-o para `ready` —
+    tudo num comando só, sem interpretar a frase do dono."""
+    repo = _montar_repo_marco(tmp_path)
+    plano = repo / "docs" / "plans" / "P-0001-marco.md"
+
+    exit_code = encerrar.main(_argv_marco(
+        repo, **{"--marco": "1", "--resultado": "go", "--veredito": "Pode seguir"},
+    ))
+
+    assert exit_code == 0
+    texto = plano.read_text(encoding="utf-8")
+    assert '| **Marco 1** | a seção 1 | go · 2026-09-26 — "Pode seguir" |' in texto
+    assert "**Marco 1, 2026-09-26 — veredito do dono (go):**" in texto
+    assert "> Pode seguir" in texto
+    assert texto.index("## 0.") < texto.index("> Pode seguir") < texto.index("## 1A.")
+    assert "**Status:** `ready`" in texto
+    diario = (repo / "docs" / "DIARIO_DE_OBRAS.md").read_text(encoding="utf-8")
+    assert "| P-0001 | Plano marco | ready 0/1 | docs/plans/P-0001-marco.md |" in diario
+
+
+def test_tr_marco_no_go_nao_muda_status(tmp_path):
+    """TR (AF-T12): a mesma escrita das duas células com `--resultado no-go` não tira o plano de
+    `blocked` — a regra concorrente ('todo marco 1 libera o plano') faria isso."""
+    repo = _montar_repo_marco(tmp_path)
+    plano = repo / "docs" / "plans" / "P-0001-marco.md"
+
+    exit_code = encerrar.main(_argv_marco(
+        repo, **{"--marco": "1", "--resultado": "no-go", "--veredito": "Ainda não"},
+    ))
+
+    assert exit_code == 0
+    texto = plano.read_text(encoding="utf-8")
+    assert '| **Marco 1**
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T12-medida.json; mundo: depois; gerado em: 2026-09-27T15:22:38+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/encerrar.py marco --help` | 0 | true |
| 2 | `python -m pytest tests/test_encerrar.py -q -k "marco"` | 0 | true |
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
