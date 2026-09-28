# Evidência de revisão — P-0753 AF-T13

## Diff (`git diff --stat`)
```
.claude/skills/entrega-de-encerramento/SKILL.md    |  23 +---
 .claude/tools/encerrar.py                          | 121 +++++++++++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T13-medida.json            |  43 ++++++++
 docs/telemetria.tsv                                |   1 +
 tests/test_encerrar.py                             |  70 ++++++++++++
 7 files changed, 244 insertions(+), 20 deletions(-)
```

## Arquivos tocados
- `.claude/skills/entrega-de-encerramento/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T13-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `fff4317466ab40c7f1de9dc773dec041f9cd8513`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`, `.claude/skills/entrega-de-encerramento/SKILL.md`
- Arquivos tocados: `.claude/skills/entrega-de-encerramento/SKILL.md`, `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T13-medida.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T13-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
--- .claude/tools/encerrar.py@fff4317466ab40c7f1de9dc773dec041f9cd8513
+++ .claude/tools/encerrar.py
@@ -1025,6 +1025,115 @@
 
 
 # --------------------------------------------------------------------------- #
+# operacoes — OP-13: o esqueleto do relatório de operações sai por comando
+# --------------------------------------------------------------------------- #
+
+
+BLOCOS_OPERACAO = [
+    "**Contexto que a motivou:**",
+    "**O que é o artefato:**",
+    "**Como funciona na prática:**",
+    "**Protege contra:**",
+]
+_SECAO_OPERACAO_ID_RE = re.compile(r"^## `([^`]+)` — .*$", re.M)
+_HEADING2_RE = re.compile(r"^## ", re.M)
+
+
+def esqueleto_operacoes(plano: "_backlog.Plano") -> str:
+    """O esqueleto do relatório de operações (`OP-13`): uma seção por tarefa não `cancelled`, na
+    ordem do plano, com os quatro blocos vazios que a skill `entrega-de-encerramento` preenche
+    depois. A tabela do arco cita toda tarefa, inclusive `cancelled`."""
+    linhas = [
+        f"# Operações — {plano.titulo}",
+        "",
+        "## Abertura",
+        "",
+        "**O problema:**",
+        "",
+        "**A solução, em uma frase:**",
+        "",
+        "| termo | o que é |",
+        "|---|---|",
+        "",
+        "## O arco",
+        "",
+        "| estrato | pergunta que responde | tarefas |",
+        "|---|---|---|",
+        "",
+        "| tarefa | título | status |",
+        "|---|---|---|",
+    ]
+    for t in plano.tarefas:
+        linhas.append(f"| `{t.id}` | {t.titulo} | {t.status} |")
+    linhas.append("")
+    for t in plano.tarefas:
+        if t.status == "cancelled":
+            continue
+        linhas.append(f"## `{t.id}` — {t.titulo}")
+        linhas.append("")
+        for bloco in BLOCOS_OPERACAO:
+            linhas.append(bloco)
+            linhas.append("")
+    linhas += [
+        "## O que vale além deste plano",
+        "",
+        "| regra | o que resolve | residência |",
+        "|---|---|---|",
+        "",
+        "## Os ganhos, medidos",
+        "",
+        "| medida | antes | depois |",
+        "|---|---|---|",
+        "",
+        "## O padrão que a execução revelou",
+        "",
+        "## Pendências abertas ao fim do plano",
+        "",
+        "| pendência | por que ficou aberta | o que a fecha | bloqueia algo? |",
+        "|---|---|---|---|",
+    ]
+    return "\n".join(linhas) + "\n"
+
+
+def escrever_esqueleto_operacoes(repo: Path, plano_path: Path) -> Path:
+    """Grava o esqueleto em `caminhos.destino_operacoes`; arquivo já existente é recusa — nada
+    escrito."""
+    plano_path = Path(plano_path)
+    if not plano_path.is_file():
+        raise EncerramentoError(f"plano: arquivo não encontrado '{plano_path}'")
+    plano = _backlog._parse_plano(plano_path, repo)
+    destino = _caminhos.destino_operacoes(repo, plano_path)
+    if destino.exists():
+        raise EncerramentoError(f"operacoes: já existe {_rel(destino, repo)}")
+    _escrever_atomico(destino, esqueleto_operacoes(plano))
+    return destino
+
+
+def checar_esqueleto_operacoes(repo: Path, plano_path: Path) -> tuple[list[str], list[str]]:
+    """Confere a cobertura do esqueleto já gravado: `nao_citados` (todo `<ID>` de card do plano
+    que não aparece no documento como `` `<ID>` ``) e `sem_blocos` (toda seção `` `<ID>` `` sem
+    uma das quatro linhas de bloco)."""
+    plano_path = Path(plano_path)
+    destino = _caminhos.destino_operacoes(repo, plano_path)
+    if not destino.is_file():
+        raise EncerramentoError(f"operacoes: arquivo ausente {_rel(destino, repo)}")
+    plano = _backlog._parse_plano(plano_path, repo)
+    texto = destino.read_text(encoding="utf-8")
+
+    nao_citados = [t.id for t in plano.tarefas if f"`{t.id}`" not in texto]
+
+    todas_headings = [m.start() for m in _HEADING2_RE.finditer(texto)]
+    sem_blocos = []
+    for m in _SECAO_OPERACAO_ID_RE.finditer(texto):
+        inicio = m.end()
+        fim = next((h for h in todas_headings if h > m.st
```
[truncado em 4000 caracteres]

### `tests/test_encerrar.py`
```
--- tests/test_encerrar.py@fff4317466ab40c7f1de9dc773dec041f9cd8513
+++ tests/test_encerrar.py
@@ -772,3 +772,73 @@
     assert "marco: status:" in capsys.readouterr().err
     assert plano.read_bytes() == antes_plano
     assert diario.read_bytes() == antes_diario
+
+
+# --- operacoes ---------------------------------------------------------------------------------
+
+
+def _argv_operacoes(repo: Path, **extra: str) -> list[str]:
+    argv = [
+        "operacoes", "--plano", str(repo / "docs" / "plans" / "P-0001-alfa.md"), "--repo", str(repo),
+    ]
+    for flag, valor in extra.items():
+        argv += [flag, valor]
+    return argv
+
+
+def test_tf_esqueleto_de_operacoes_uma_secao_por_card(tmp_path):
+    """TF (AF-T13): `operacoes --plano <legado>` grava o esqueleto com exatamente uma seção
+    `## `<ID>`` — a de ALF-T1; ALF-T2 (`cancelled`) não ganha seção, mas a tabela do arco cita
+    as duas."""
+    repo = _montar_repo(tmp_path)
+
+    exit_code = encerrar.main(_argv_operacoes(repo))
+
+    assert exit_code == 0
+    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
+    texto = destino.read_text(encoding="utf-8")
+    secoes = [l for l in texto.splitlines() if l.startswith("## `")]
+    assert secoes == [f"## `ALF-T1` — {TITULO_T1}"]
+    assert f"| `ALF-T1` | {TITULO_T1} | review |" in texto
+    assert f"| `ALF-T2` | {TITULO_T2} | cancelled |" in texto
+
+
+def test_tr_esqueleto_de_operacoes_nao_sobrescreve(tmp_path, capsys):
+    """TR (AF-T13): destino já existente é recusa — exit 1, nada escrito."""
+    repo = _montar_repo(tmp_path)
+    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
+    destino.write_text("conteúdo prévio\n", encoding="utf-8")
+
+    exit_code = encerrar.main(_argv_operacoes(repo))
+
+    assert exit_code == 1
+    assert "operacoes: já existe" in capsys.readouterr().err
+    assert destino.read_text(encoding="utf-8") == "conteúdo prévio\n"
+
+
+def test_tf_esqueleto_de_operacoes_checar_cobertura(tmp_path, capsys):
+    """TF (AF-T13): `--checar` sobre o esqueleto recém-gerado sai 0 com as duas linhas `nenhum`;
+    apagando o bloco `**Protege contra:**` da seção de ALF-T1, sai 1 e nomeia a tarefa."""
+    repo = _montar_repo(tmp_path)
+    destino = repo / "docs" / "OPERACOES_AS_IS_P-0001.md"
+    assert encerrar.main(_argv_operacoes(repo)) == 0
+    capsys.readouterr()
+
+    exit_code = encerrar.main(_argv_operacoes(repo) + ["--checar"])
+
+    assert exit_code == 0
+    saida = capsys.readouterr().out
+    assert "nao citados: nenhum" in saida
+    assert "sem os quatro blocos: nenhum" in saida
+
+    destino.write_text(
+        destino.read_text(encoding="utf-8").replace("**Protege contra:**\n\n", ""),
+        encoding="utf-8",
+    )
+
+    exit_code = encerrar.main(_argv_operacoes(repo) + ["--checar"])
+
+    assert exit_code == 1
+    saida = capsys.readouterr().out
+    assert "nao citados: nenhum" in saida
+    assert "sem os quatro blocos: ALF-T1" in saida

```

### `.claude/skills/entrega-de-encerramento/SKILL.md`
```
diff --git a/.claude/skills/entrega-de-encerramento/SKILL.md b/.claude/skills/entrega-de-encerramento/SKILL.md
index 5ba3b37..2d28cc8 100644
--- a/.claude/skills/entrega-de-encerramento/SKILL.md
+++ b/.claude/skills/entrega-de-encerramento/SKILL.md
@@ -151,24 +151,13 @@ aponta para a pendência da segunda, pelo número.
    erra: numa redação de referência, o autor contou "quatro categorias" onde o código tinha cinco.
 3. **Colha saídas reais.** Rode os comandos e copie a saída. Onde a saída já existe no registro da
    execução, cite-a de lá.
-4. **Escreva as seções por tarefa**, aplicando os três testes da regra de leitura.
+4. **Escreva as seções por tarefa** sobre o esqueleto que `python .claude/tools/encerrar.py operacoes --plano <plano>` gera (uma seção por tarefa viva, com os quatro blocos vazios), aplicando os três testes da regra de leitura.
 5. **Classifique cada defeito e cada pendência** pelos três estados.
-6. **Verifique a cobertura por comando**, não por leitura — todo card do plano citado no documento:
-
-   ```
-   python - <<'EOF'
-   import re
-   from pathlib import Path
-   doc = Path('<documento>').read_text(encoding='utf-8')
-   plano = Path('<plano>').read_text(encoding='utf-8')
-   cards = set(re.findall(r'^### (\S+-T\S+) ', plano, re.M))
-   citados = set(re.findall(r'`(\S+-T[0-9]+[a-z]?)`', doc))
-   print('nao citados:', sorted(cards - citados) or 'nenhum')
-   EOF
-   ```
-
-7. **Verifique a estrutura por comando** — toda seção de tarefa com os quatro blocos obrigatórios.
-8. **Apresente ao dono** e colha o veredito.
+6. **Verifique a cobertura e a estrutura por comando**, não por leitura — todo card do plano citado
+   no documento e toda seção de tarefa com os quatro blocos obrigatórios:
+   `python .claude/tools/encerrar.py operacoes --plano <plano> --checar`, exit `0` com as linhas
+   `nao citados: nenhum` e `sem os quatro blocos: nenhum`.
+7. **Apresente ao dono** e colha o veredito.
 
 ---
 

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T13-medida.json; mundo: depois; gerado em: 2026-09-27T15:46:10+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/tools/encerrar.py operacoes --help` | 0 | true |
| 2 | `python -m pytest tests/test_encerrar.py -q -k "esqueleto_de_operacoes"` | 0 | true |
| 3 | `python -c "from pathlib import Path;t=Path('.claude/skills/entrega-de-encerramento/SKILL.md').read_text(encoding='utf-8');print(t.count('encerrar.py operacoes --plano'),t.count('citados = set(re.findall'))"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
