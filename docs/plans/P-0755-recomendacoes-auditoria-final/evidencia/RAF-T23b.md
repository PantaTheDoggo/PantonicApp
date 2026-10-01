# Evidência de revisão — P-0755 RAF-T23b

## Diff (`git diff --stat`)
```
.claude/tools/encerrar.py                          | 16 ++++++--
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T23b-medida-depois.json   | 22 +++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_encerrar.py                             | 44 ++++++++++++++++++++++
 6 files changed, 82 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23b-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `89e8b2909057f5485b2c1467a333580adb65b7e9`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23b-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23b-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
diff --git a/.claude/tools/encerrar.py b/.claude/tools/encerrar.py
index 84efee4..fd7ae77 100644
--- a/.claude/tools/encerrar.py
+++ b/.claude/tools/encerrar.py
@@ -923,17 +923,19 @@ _SOMENTE_DIGITOS_RE = re.compile(r"^\d+$")
 
 
 def _dossie_emenda(
-    plano_path: Path, repo: Path, marco: int, frase: str, fato_novo: str, restricao: str
+    plano_path: Path, repo: Path, marco: int, frase: str, fato_novo: str, restricao: str,
+    devolver: str,
 ) -> str:
     """O dossiê `Ato: emenda` para o modelador (`OP-12`/`RAF-T23`): motivo do marco, o fato que
-    muda o modelo e a restrição que a emenda tem de respeitar."""
+    muda o modelo e a restrição que a emenda tem de respeitar. O `Devolver` difere entre a
+    recusa da versão e o conflito na promoção (`RAF-T23b`)."""
     return "\n".join([
         f"Plano: {_rel(plano_path, repo)}",
         "Ato: emenda",
         f'Motivo: Marco {marco}, veredito do dono: "{frase}"',
         f"Fato novo: {fato_novo}",
         f"Restrição: {restricao}",
-        "Devolver: a seção ## 1 depois do ato e a linha nova do registro de versões.",
+        f"Devolver: {devolver}",
     ])
 
 
@@ -1072,6 +1074,8 @@ def _checar_promocao(
             plano_path, repo, marco, frase,
             f"{fato_novo_base} Conflito na promoção: {razao}.",
             restricao,
+            "a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do "
+            "marco rodar de novo.",
         )
         return ConflitoDePromocao(f"conflito na promoção da versão {k} — {razao}", dossie)
 
@@ -1234,7 +1238,11 @@ def gravar_marco(
         "a versão recusada se refaz por card corretivo da operação afetada (GOVERNANCA.md §3.2)."
     )
 
-    return _dossie_emenda(plano_path, repo, marco, frase, fato_novo, restricao)
+    return _dossie_emenda(
+        plano_path, repo, marco, frase, fato_novo, restricao,
+        "a seção ## 1 depois do ato, com o registro de versões sem a linha da versão "
+        "recusada, e o plano sem a ## 1A.",
+    )
 
 
 # --------------------------------------------------------------------------- #

```

### `tests/test_encerrar.py`
```
diff --git a/tests/test_encerrar.py b/tests/test_encerrar.py
index 4a3e006..f163b9c 100644
--- a/tests/test_encerrar.py
+++ b/tests/test_encerrar.py
@@ -1165,3 +1165,47 @@ def test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente(tmp_path, ca
     assert exit_code == 1
     assert "marco: plano sem versão pendente (## 1A)" in capsys.readouterr().err
     assert plano.read_text(encoding="utf-8") == antes
+
+
+def test_tf_marco_conflito_devolver_pede_a_1_e_a_1a(tmp_path, capsys):
+    """TF (RAF-T23b, `AE-180`): no conflito da promoção o modelador acerta o que está (a
+    `## 1`, a `## 1A` e o registro de versões) para o comando rodar de novo; o `Devolver` do
+    dossiê não pede a seção depois do ato nem linha nova do registro, que o comando faz."""
+    repo = _montar_repo_promocao(tmp_path)
+
+    exit_code = encerrar.main(_argv_marco(
+        repo, **{
+            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 3",
+            "--aceita-versao": "3", "--consultor": "valido a versão 3",
+        },
+    ))
+
+    assert exit_code == 1
+    saida = capsys.readouterr().out
+    assert (
+        "Devolver: a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do "
+        "marco rodar de novo." in saida
+    )
+    assert "linha nova do registro" not in saida
+
+
+def test_tf_marco_recusa_devolver_sem_linha_nova_do_registro(tmp_path, capsys):
+    """TF (RAF-T23b, `AE-180`): na recusa a `## 1A` e a linha dela saem e a vigente fica sem
+    marca (`GOVERNANCA.md` §3.2); o `Devolver` do dossiê pede a `## 1` com o registro sem a linha
+    da versão recusada, não uma linha nova."""
+    repo = _montar_repo_marco(tmp_path)
+
+    exit_code = encerrar.main(_argv_marco(
+        repo, **{
+            "--marco": "1", "--resultado": "no-go", "--veredito": "Não aceito",
+            "--recusa-versao": "2",
+        },
+    ))
+
+    assert exit_code == 0
+    saida = capsys.readouterr().out
+    assert (
+        "Devolver: a seção ## 1 depois do ato, com o registro de versões sem a linha da versão "
+        "recusada, e o plano sem a ## 1A." in saida
+    )
+    assert "linha nova do registro" not in saida

```

## Linhas removidas dos testes
### `tests/test_encerrar.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T23b-medida-depois.json; mundo: depois; gerado em: 2026-09-29T22:47:24+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py -q -k devolver` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print('devolver=%d-%d'%(t.count('linha nova do registro'),t.count('rodar de novo')))"` | 0 | true |

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
