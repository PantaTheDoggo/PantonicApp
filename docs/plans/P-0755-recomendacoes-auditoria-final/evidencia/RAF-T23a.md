# Evidência de revisão — P-0755 RAF-T23a

## Diff (`git diff --stat`)
```
.claude/tools/encerrar.py                          |  5 +++--
 docs/DIARIO_DE_OBRAS.md                            |  6 +++---
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T23a-medida-depois.json   | 15 +++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_encerrar.py                             | 25 ++++++++++++++++++++++
 6 files changed, 48 insertions(+), 6 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `6151155f7e25ee108ac486df65389fac5ada6552`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23a-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
diff --git a/.claude/tools/encerrar.py b/.claude/tools/encerrar.py
index 7975f28..84efee4 100644
--- a/.claude/tools/encerrar.py
+++ b/.claude/tools/encerrar.py
@@ -918,7 +918,6 @@ def fechar_plano(
 
 _MARCO_SECAO0_RE = re.compile(r"^## 0\.")
 _MARCO_HEADING_RE = re.compile(r"^## ")
-_MARCO_VERSAO_PENDENTE_RE = re.compile(r"^## 1A\. Modelo conceitual — versão pendente de validação")
 _MARCO_COLUNA_RE = re.compile(r"(?<!\\)\|")
 _SOMENTE_DIGITOS_RE = re.compile(r"^\d+$")
 
@@ -1144,8 +1143,10 @@ def gravar_marco(
     if idx_secao0 is None:
         raise EncerramentoError("seção ## 0 ausente")
 
+    # A `## 1A` se reconhece pela mesma regra do `modelo.py` (igualdade exata com
+    # `_HEADING_PENDENTE`), não por prefixo — `AE-176`, `RAF-T23a` do `P-0755`.
     if (aceita_versao is not None or recusa_versao is not None) and not any(
-        _MARCO_VERSAO_PENDENTE_RE.match(l) for l in linhas
+        l == _modelo._HEADING_PENDENTE for l in linhas
     ):
         raise EncerramentoError("plano sem versão pendente (## 1A)")
 

```

### `tests/test_encerrar.py`
```
diff --git a/tests/test_encerrar.py b/tests/test_encerrar.py
index bd5449e..4a3e006 100644
--- a/tests/test_encerrar.py
+++ b/tests/test_encerrar.py
@@ -1140,3 +1140,28 @@ def test_tr_marco_validacao_do_consultor_obrigatoria_no_aceite(tmp_path, capsys)
         in capsys.readouterr().err
     )
     assert plano.read_text(encoding="utf-8") == antes
+
+
+def test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente(tmp_path, capsys):
+    """TF (RAF-T23a, `AE-176`): a `## 1A` cujo cabeçalho tem texto a mais não é a versão pendente
+    que o `modelo.py` lê (igualdade exata com `_modelo._HEADING_PENDENTE`); a pré-checagem do
+    marco usa a mesma regra e recusa antes de escrever, em vez de passar pelo prefixo e cair em
+    `AttributeError` dentro de `_checar_promocao`."""
+    texto = PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", "MRC-T2").replace(
+        "## 1A. Modelo conceitual — versão pendente de validação",
+        "## 1A. Modelo conceitual — versão pendente de validação (rascunho)",
+    )
+    repo = _montar_repo_marco(tmp_path, texto)
+    plano = repo / "docs" / "plans" / "P-0001-marco.md"
+    antes = plano.read_text(encoding="utf-8")
+
+    exit_code = encerrar.main(_argv_marco(
+        repo, **{
+            "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2",
+            "--aceita-versao": "2", "--consultor": "valido a versão 2",
+        },
+    ))
+
+    assert exit_code == 1
+    assert "marco: plano sem versão pendente (## 1A)" in capsys.readouterr().err
+    assert plano.read_text(encoding="utf-8") == antes

```

## Linhas removidas dos testes
### `tests/test_encerrar.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T23a-medida-depois.json; mundo: depois; gerado em: 2026-09-29T21:34:52+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py -q -k cabecalho_1a` | 0 | true |

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
