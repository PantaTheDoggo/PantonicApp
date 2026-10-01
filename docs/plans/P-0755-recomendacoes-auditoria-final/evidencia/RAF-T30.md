# Evidência de revisão — P-0755 RAF-T30

## Diff (`git diff --stat`)
```
.claude/tools/encerrar.py                          |  22 +-
 docs/ACIONAMENTOS_CONSULTOR.tsv                    |   1 +
 docs/DIARIO_DE_OBRAS.md                            |   6 +-
 .../cenario.md                                     |  36 ++-
 .../estado.tsv                                     |   3 +-
 .../evidencia/P-0755-RAF-T30-medida-depois.json    |  29 ++
 .../evidencia/RAF-T30.md                           | 210 +++++++++++++
 .../laudos/RAF-T30.md                              |  35 +++
 .../P-0755-recomendacoes-auditoria-final/plano.md  | 344 ++++++++++++++++++++-
 docs/telemetria.tsv                                |   5 +
 tests/test_encerrar.py                             | 109 +++++++
 11 files changed, 784 insertions(+), 16 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: ` M`
- `docs/ACIONAMENTOS_CONSULTOR.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T30-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/RAF-T30.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/laudos/RAF-T30.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `9e5bf2e2b1105091bca091a6f71ff95b18a2d72d`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T30-medida-depois.json`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/RAF-T30.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/laudos/RAF-T30.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/cenario.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T30-medida-depois.json`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/RAF-T30.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/laudos/RAF-T30.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
diff --git a/.claude/tools/encerrar.py b/.claude/tools/encerrar.py
index fd7ae77..8d90436 100644
--- a/.claude/tools/encerrar.py
+++ b/.claude/tools/encerrar.py
@@ -242,6 +242,8 @@ def achados_do_plano(plano_path: Path) -> list[tuple[str, str]]:
 
 
 ACHADO_PROCESSO_HEADING = "## Achado de processo"
+_ACHADO_INSTRUMENTO_RE = re.compile(r"achado de processo \(instrumento\):\s*(?P<resto>.+)", re.IGNORECASE)
+_TERMOS_DE_FALHA = ("queda", "traceback", "exceção", "excecao", "exception", "error")
 _ACHADO_LINHA_RE = re.compile(r"^\|\s*(?P<alvo>[^|]+?)\s*\|\s*(?P<achado>.+?)\s*\|\s*$")
 
 
@@ -292,7 +294,7 @@ def _escrever_atomico(caminho: Path, texto: str) -> None:
 
 
 def apensar_achado(plano_path: Path, tarefa_id: str, texto: str, rota: str, data: str,
-                   tiquete_id: str | None = None) -> str:
+                   tiquete_id: str | None = None, origem: str | None = None) -> str:
     """Registro único do achado (`GOVERNANCA.md` §4.2): uma entrada `AE-<n>` com `**Rota:**`, ao
     fim de `## Achados da execução` do plano (a seção nasce se não existir). No diário, o achado
     de um card de tíquete entra no corpo da seção `## TK-<n>` do tíquete-pai, antes do primeiro
@@ -301,6 +303,10 @@ def apensar_achado(plano_path: Path, tarefa_id: str, texto: str, rota: str, data
     numeros = [int(n) for n in AE_ID_RE.findall("\n".join(linhas))]
     ae_id = f"AE-{max(numeros, default=0) + 1}"
     entrada = f"- **{ae_id}** (`{tarefa_id}`, fechamento, {data}) — {texto} **Rota:** {rota}"
+    # Origem do achado, para o fechamento pular o já registrado pela linha do laudo e o
+    # consultor citar a origem ao reescrever (R-19, DRF-21 do P-0755).
+    if origem is not None:
+        entrada += f" **Origem:** `{origem}`"
 
     if tiquete_id is not None:
         ini = next((i for i, l in enumerate(linhas) if l.startswith(f"## {tiquete_id} ")), None)
@@ -562,16 +568,24 @@ def fechar_tarefa(
 
     textos_gravados = {texto.strip() for texto, _ in achados or []}
     entradas_existentes = "\n".join(texto for _, texto in achados_do_plano(plano_path))
-    for texto, rota in achados_do_laudo(texto_laudo):
-        if texto in entradas_existentes or texto in textos_gravados:
+    achados_laudo = achados_do_laudo(texto_laudo)
+    for n, (texto, rota) in enumerate(achados_laudo, start=1):
+        origem = f"laudo:{tarefa_id}#{n}"
+        if f"`{origem}`" in entradas_existentes or texto in entradas_existentes or texto in textos_gravados:
             continue
-        ids_achados.append(apensar_achado(plano_path, tarefa_id, texto, rota, data, tiquete_id=tiquete_id))
+        ids_achados.append(
+            apensar_achado(plano_path, tarefa_id, texto, rota, data, tiquete_id=tiquete_id, origem=origem)
+        )
         textos_gravados.add(texto)
 
     humano = "\n".join(humano_linhas)
     if ids_achados:
         humano += f"\nAchados: {', '.join(ids_achados)}."
     humano += f"\nDetalhe: `{rdo_rel}`."
+    for texto, _rota in achados_laudo:
+        m = _ACHADO_INSTRUMENTO_RE.search(texto)
+        if m and any(termo in m.group("resto").lower() for termo in _TERMOS_DE_FALHA):
+            humano += f"\nencerrar: B1 — achado de instrumento com falha: {m.group('resto')}"
     return destino, humano
 
 

```

### `tests/test_encerrar.py`
```
diff --git a/tests/test_encerrar.py b/tests/test_encerrar.py
index f163b9c..843f4ae 100644
--- a/tests/test_encerrar.py
+++ b/tests/test_encerrar.py
@@ -1209,3 +1209,112 @@ def test_tf_marco_recusa_devolver_sem_linha_nova_do_registro(tmp_path, capsys):
         "recusada, e o plano sem a ## 1A." in saida
     )
     assert "linha nova do registro" not in saida
+
+
+# --- RAF-T30: origem do achado e aviso de falha de instrumento -------------------------------
+
+
+def test_tf_origem_do_achado_gravada_na_linha(tmp_path):
+    """TF (RAF-T30, `R-19`/`DRF-21`): cada achado do laudo grava a linha de origem
+    `laudo:<TAREFA>#<n>`, numerada a partir de 1 na ordem da tabela."""
+    repo = _montar_repo(tmp_path)
+    laudo = repo / "docs" / "RDO" / "laudos" / "P-0001-ALF-T1.md"
+    laudo.write_text(_laudo_com_achado([
+        "| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |",
+        "| doutrina | a skill não nomeia o gate. Rota: tíquete |",
+    ]), encoding="utf-8")
+
+    exit_code = encerrar.main(_argv_tarefa(repo))
+
+    assert exit_code == 0
+    texto_plano = (repo / "docs" / "plans" / "P-0001-alfa.md").read_text(encoding="utf-8")
+    assert (
+        "- **AE-3** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (doutrina): "
+        "a skill não nomeia o gate. **Rota:** tíquete **Origem:** `laudo:ALF-T1#2`"
+    ) in texto_plano
+
+
+def test_tf_origem_do_achado_ja_registrada_pula(tmp_path):
+    """TF (RAF-T30, `R-19`): a origem `laudo:ALF-T1#1` já está registrada no plano com outro
+    texto; a regra concorrente (dedupe só por texto) gravaria de novo — o fechamento pula."""
+    repo = _montar_repo(tmp_path)
+    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
+    entrada_existente = (
+        "- **AE-2** (`ALF-T1`, laudo, 2026-09-21) — achado de processo (dossiê): "
+        "outro texto qualquer. **Rota:** outra rota. **Origem:** `laudo:ALF-T1#1`\n"
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
+
+
+def test_tr_origem_do_achado_de_outra_linha_nao_pula(tmp_path):
+    """TR (RAF-T30): a `AE-2` existente cita `laudo:ALF-T1#11`; a regra concorrente (casar
+    `laudo:ALF-T1#1` como substring sem as crases) pularia a linha 1 por engano — não pula."""
+    repo = _montar_repo(tmp_path)
+    plano = repo / "docs" / "plans" / "P-0001-alfa.md"
+    entrada_existente = (
+        "- **AE-2** (`ALF-T1`, laudo, 2026-09-21) — achado de processo (dossiê): "
+        "outro texto qualquer. **Rota:** outra rota. **Origem:** `laudo:ALF-T1#11`\n"
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
+    assert (
+        "- **AE-3** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (dossiê): "
+        "o card não citava o arquivo de teste. **Rota:** card corretivo ALF-T1a **Origem:** "
+        "`laudo:ALF-T1#1`"
+    ) in texto_plano
+
+
+def test_tf_falha_de_instrumento_avisa_b1(tmp_path, capsys):
+    """TF (RAF-T30, `R-20`): achado de processo do alvo `instrumento` que relata queda ou erro
+    ganha, no stdout, a linha `encerrar: B1` antes da linha final de conclusão."""
+    repo = _montar_repo(tmp_path)
+    laudo = rep
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_encerrar.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T30-medida-depois.json; mundo: depois; gerado em: 2026-09-30T01:23:49+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py -q -k origem_do_achado` | 0 | true |
| 2 | `python -m pytest tests/test_encerrar.py -q -k falha_de_instrumento` | 0 | true |
| 3 | `python -c "from pathlib import Path;t=Path('tests/test_encerrar.py').read_text(encoding='utf-8');a=chr(34)+'linha nova do registro'+chr(34)+' not in saida';m=t.split('def test_tf_origem_do_achado_gravada_na_linha')[0];print('marco=%d total=%d'%(m.count(a),t.count(a)))"` | 0 | true |

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
