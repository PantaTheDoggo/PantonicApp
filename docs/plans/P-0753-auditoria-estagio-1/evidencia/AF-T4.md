# Evidência de revisão — P-0753 AF-T4

## Diff (`git diff --stat`)
```
.claude/skills/scrum-master/SKILL.md               |  3 +-
 .claude/tools/encerrar.py                          | 47 ++++++++++++++
 docs/DIARIO_DE_OBRAS.md                            |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T4-medida.json             | 36 +++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_encerrar.py                             | 73 ++++++++++++++++++++++
 7 files changed, 161 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: `??`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T4-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `02e547425f17757e843f90c4340082a5a3617beb`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`, `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T4-medida.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T4-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
--- .claude/tools/encerrar.py@02e547425f17757e843f90c4340082a5a3617beb
+++ .claude/tools/encerrar.py
@@ -228,6 +228,44 @@
         m = AE_ID_RE.search(texto.splitlines()[0])
         if m:
             resultado.append((f"AE-{m.group(1)}", texto))
+    return resultado
+
+
+ACHADO_PROCESSO_HEADING = "## Achado de processo"
+_ACHADO_LINHA_RE = re.compile(r"^\|\s*(?P<alvo>[^|]+?)\s*\|\s*(?P<achado>.+?)\s*\|\s*$")
+
+
+def achados_do_laudo(texto_laudo: str) -> list[tuple[str, str]]:
+    """`(texto, rota)` por linha de dado da tabela `| alvo | achado |` da seção `## Achado de
+    processo` do laudo (`rdo.py laudo` grava a seção sempre — corpo `nenhum` ou seção ausente
+    devolve lista vazia). `texto` = `achado de processo (<alvo>): ` + o trecho antes da primeira
+    ocorrência de `Rota:`, com `strip()`; `rota` = o trecho depois, com `strip()`, ou `não
+    declarada no laudo` quando falta `Rota:` ou o trecho sai vazio."""
+    if ACHADO_PROCESSO_HEADING not in texto_laudo:
+        return []
+    corpo = texto_laudo.split(ACHADO_PROCESSO_HEADING, 1)[1]
+    m_fim = re.search(r"^## ", corpo, re.M)
+    corpo = corpo[: m_fim.start()] if m_fim else corpo
+    resultado: list[tuple[str, str]] = []
+    for linha in corpo.splitlines():
+        linha = linha.strip()
+        if not linha.startswith("|"):
+            continue
+        m = _ACHADO_LINHA_RE.match(linha)
+        if not m:
+            continue
+        alvo = m.group("alvo").strip()
+        achado = m.group("achado").strip()
+        if alvo.lower() == "alvo" or set(achado) <= {"-"}:
+            continue
+        if "Rota:" in achado:
+            antes, depois = achado.split("Rota:", 1)
+            texto = antes.strip()
+            rota = depois.strip() or "não declarada no laudo"
+        else:
+            texto = achado
+            rota = "não declarada no laudo"
+        resultado.append((f"achado de processo ({alvo}): {texto}", rota))
     return resultado
 
 
@@ -369,6 +407,7 @@
             else repo / "docs" / "RDO" / "laudos" / f"{plano_id}-{tarefa_id}.md"
         )
     pacote = ler_laudo(Path(laudo_path))
+    texto_laudo = Path(laudo_path).read_text(encoding="utf-8")
     if pacote["veredito"] not in ("aprovado", "ressalva"):
         raise EncerramentoError(
             f"laudo: veredito '{pacote['veredito']}' não é desfecho de RDO — materialize `blocked` "
@@ -510,6 +549,14 @@
     tiquete_id = pai.id if tipo_pai == "tiquete" else None
     for texto, rota in achados or []:
         ids_achados.append(apensar_achado(plano_path, tarefa_id, texto.strip(), rota.strip(), data, tiquete_id=tiquete_id))
+
+    textos_gravados = {texto.strip() for texto, _ in achados or []}
+    entradas_existentes = "\n".join(texto for _, texto in achados_do_plano(plano_path))
+    for texto, rota in achados_do_laudo(texto_laudo):
+        if texto in entradas_existentes or texto in textos_gravados:
+            continue
+        ids_achados.append(apensar_achado(plano_path, tarefa_id, texto, rota, data, tiquete_id=tiquete_id))
+        textos_gravados.add(texto)
 
     humano = "\n".join(humano_linhas)
     if ids_achados:

```

### `tests/test_encerrar.py`
```
--- tests/test_encerrar.py@02e547425f17757e843f90c4340082a5a3617beb
+++ tests/test_encerrar.py
@@ -82,6 +82,17 @@
     "\n"
     "Observação qualitativa do revisor.\n"
 )
+
+
+def _laudo_com_achado(linhas_tabela: list[str]) -> str:
+    """`LAUDO` acrescida da seção `## Achado de processo` (tabela `| alvo | achado |`), antes de
+    `## Lições aprendidas na tarefa` — a forma que `rdo.py laudo` grava."""
+    tabela = "\n".join(["| alvo | achado |", "|---|---|"] + linhas_tabela)
+    return LAUDO.replace(
+        "## Lições aprendidas na tarefa",
+        f"## Achado de processo\n\n{tabela}\n\n## Lições aprendidas na tarefa",
+    )
+
 
 TELEMETRIA = (
     "data\tprojeto\ttarefa\tmodelo\ttool_uses\ttokens_k\tduracao_s\tfonte\n"
@@ -174,6 +185,68 @@
     assert (repo / "docs" / "telemetria.tsv").read_text(encoding="utf-8") == TELEMETRIA
 
 
+def test_tf_achado_do_laudo_vira_ae_com_rota(tmp_path):
+    """TF (AF-T4): cada linha da tabela `| alvo | achado |` de `## Achado de processo` do laudo
+    vira um `AE-<n>` no plano, com a rota transcrita do trecho depois de `Rota:` — sem nenhum
+    `--achado` no comando."""
+    repo = _montar_repo(tmp_path)
+    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
+    laudo.write_text(_laudo_com_achado([
+        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
+    ]), encoding="utf-8")
+
+    exit_code = encerrar.main(_argv_tarefa(repo))
+
+    assert exit_code == 0
+    texto_plano = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
+    assert (
+        "- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (dossiê): "
+        "o card não citava o arquivo de teste. **Rota:** card corretivo ALF-T1a"
+    ) in texto_plano
+
+
+def test_tr_achado_do_laudo_repetido_nao_duplica(tmp_path):
+    """TR (AF-T4): o plano já traz uma entrada com o mesmo texto do achado de processo do laudo —
+    a regra concorrente ("grava toda linha do laudo") duplicaria; o fechamento pula o par."""
+    repo = _montar_repo(tmp_path)
+    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
+    entrada_existente = (
+        "- **AE-2** (`ALF-T1`, laudo, 2026-09-21) — achado de processo (dossiê): "
+        "o card não citava o arquivo de teste. **Rota:** registrado antes.\n"
+    )
+    plano.write_text(plano.read_text(encoding="utf-8") + entrada_existente, encoding="utf-8")
+    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
+    laudo.write_text(_laudo_com_achado([
+        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
+    ]), encoding="utf-8")
+
+    exit_code = encerrar.main(_argv_tarefa(repo))
+
+    assert exit_code == 0
+    texto_plano = plano.read_text(encoding="utf-8")
+    assert "AE-3" not in texto_plano
+    assert texto_plano.count("achado de processo (dossiê): o card não citava o arquivo de teste.") == 1
+
+
+def test_tf_achado_do_laudo_sem_rota_declarada(tmp_path):
+    """TF (AF-T4): achado de processo do laudo sem `Rota:` grava `AE-<n>` com `**Rota:** não
+    declarada no laudo`."""
+    repo = _montar_repo(tmp_path)
+    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
+    laudo.write_text(_laudo_com_achado([
+        "| doutrina | a skill não nomeia o gate. |",
+    ]), encoding="utf-8")
+
+    exit_code = encerrar.main(_argv_tarefa(repo))
+
+    assert exit_code == 0
+    texto_plano = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
+    assert (
+        "- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (doutrina): "
+        "a skill não nomeia o gate. **Rota:** não declarada no laudo"
+    ) in texto_plano
+
+
 def test_tf_tarefa_consumo_por_argumento_apensa_a_serie(tmp_path):
     """TF: com o trio do bloco `<usage>` por argumento, a linha entra em `docs/telemetria.tsv`
     (fonte `usage`) no mesmo ato e o RDO usa esse número, não o da série."""

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 01b5e38..8f7a247 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -225,7 +225,8 @@ Dez passos, nesta ordem.
   passa o trio conferido, e a linha do hook fica na série como está. O hook **não dispara** quando
   um subagente é retomado por `SendMessage` — a retomada do executor pela `A1` — e nesse caso o
   trio vem sempre por argumento; o consultor nunca é retomado (seção *Acionamento do consultor*);
-  (5) cada `--achado` vira `AE-<n>` com `**Rota:**` em `## Achados da execução` do plano. O
+  (5) cada linha da tabela `## Achado de processo` do laudo e cada `--achado` viram `AE-<n>` com
+  `**Rota:**` em `## Achados da execução` do plano, sem repetir achado do laudo já registrado. O
   `<tokens_k>` é o literal do `<usage>`, decimal de uma casa (ex.: `203.7`), sem conversão nem
   arredondamento (`DM-11` do `P-0740`). A saída do comando é a seção `# Humano` — o handover da
   tarefa, em ≤ 8 linhas. O laudo permanece no disco como fonte do pacote (`DP-H` item 3 deixa de

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T4-medida.json; mundo: depois; gerado em: 2026-09-27T12:30:04+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py -q -k "achado_do_laudo"` | 0 | true |
| 2 | `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('cada linha da tabela'))"` | 0 | true |
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
