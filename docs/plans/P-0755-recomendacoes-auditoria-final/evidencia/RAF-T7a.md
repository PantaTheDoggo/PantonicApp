# Evidência de revisão — P-0755 RAF-T7a

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                          |  4 +---
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T7a-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 21 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T7a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `0ac4f751ce75860a4b34f2d4a5ce450919752bcd`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T7a-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T7a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index c58da13..91d109a 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -332,7 +332,7 @@ def _nao_rastreado_mudou_desde_ref(root: Path, ref: str, caminho: str) -> bool:
         return _bytes_do_ref(root, ref, caminho) != bytes_atuais
     texto_ref = _texto_do_ref_ou_none(root, ref, caminho)
     if texto_ref is None:
-        return _bytes_do_ref(root, ref, caminho) != (root / caminho).read_bytes()
+        return True
     return texto_ref.splitlines() != texto_atual.splitlines()
 
 
@@ -627,8 +627,6 @@ def _diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -
                 return "(arquivo binário ou não-UTF-8 — trecho omitido)"
             texto_ref = _texto_do_ref_ou_none(root, desde, caminho_rel)
             if texto_ref is None:
-                if _bytes_do_ref(root, desde, caminho_rel) == (root / caminho_rel).read_bytes():
-                    return f"(sem alteração desde `{desde}`)"
                 return "(arquivo binário ou não-UTF-8 — trecho omitido)"
             linhas_ref = texto_ref.splitlines()
             linhas_atual = texto_atual.splitlines()

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T7a-medida.json; mundo: depois; gerado em: 2026-09-29T07:13:48+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "import pathlib,sys; t=pathlib.Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8'); n=t.count('_bytes_do_ref('); print(n); sys.exit(0 if n==3 else 1)"` | 0 | true |

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
