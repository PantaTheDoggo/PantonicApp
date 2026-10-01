# Evidência de revisão — P-0755 RAF-T12a

## Diff (`git diff --stat`)
```
.claude/tools/review_evidence.py                          | 14 +++++++-------
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 docs/RUBRICA_DE_REVISAO.md                                |  5 +++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T12a-medida.json                 | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 tests/test_review_evidence.py                             |  6 +++---
 7 files changed, 33 insertions(+), 16 deletions(-)
```

## Arquivos tocados
- `.claude/tools/review_evidence.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T12a-medida.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_review_evidence.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `675c429cb633f71e216e43446cd33b1bb77c1399`
- Arquivos-alvo declarados: `docs/RUBRICA_DE_REVISAO.md`, `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`
- Arquivos tocados: `.claude/tools/review_evidence.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T12a-medida.json`, `docs/telemetria.tsv`, `tests/test_review_evidence.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T12a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/RUBRICA_DE_REVISAO.md`
```
diff --git a/docs/RUBRICA_DE_REVISAO.md b/docs/RUBRICA_DE_REVISAO.md
index d9ed439..4a6ce86 100644
--- a/docs/RUBRICA_DE_REVISAO.md
+++ b/docs/RUBRICA_DE_REVISAO.md
@@ -94,8 +94,9 @@ essa obrigação é **capacidade**, não card: atribuição por **hunk**.
 ### `testes`
 
 - **Pergunta:** os testes que o dossiê exige existem e passam?
-- **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados, exit code da suíte
-  da área tocada e a seção `## Linhas removidas dos testes` da evidência.
+- **Fonte da evidência:** mista — presença dos arquivos de teste declarados e exit code da suíte
+  da área tocada, mecânicos e travados; juízo sobre cada linha da seção
+  `## Linhas removidas dos testes` da evidência, confrontada com o que o card manda remover.
 - **Bloqueante:** sim.
 - **`conforme`:** o teste funcional e o teste de regressão exigidos existem e a suíte fecha em
   exit 0.

```

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 171b488..710818b 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -11,7 +11,7 @@ um teto de caracteres (truncamento sempre visível na saída, nunca silencioso).
 
 Invariante (`DA-7`): a saída é fato com veredito mecânico, sem interpretação — a camada mecânica é
 autoridade sobre o que ela mede, quem interpreta é o reviewer. A dimensão `escopo`
-(`docs/RUBRICA_DE_REVISAO.md:63-77`) tem uma faixa `parcial` que depende de declaração de desvio
+(`docs/RUBRICA_DE_REVISAO.md` §4) tem uma faixa `parcial` que depende de declaração de desvio
 na entrega — insumo que este script não recebe. Por isso, quando há arquivo tocado fora
 dos alvos, a saída relata o **fato** ("N arquivo(s) fora dos alvos: ...") e deixa o veredito em
 aberto; nunca resolve sozinha para `parcial`.
@@ -30,9 +30,9 @@ A seção `## Guardas` (`EXA-T9b`) invoca a bateria de seis comandos de `GOVERNA
 mesma que fechou a `T9a`: `python -m pytest -q`, `dead_code.py`, `ratchet_piso.py`,
 `kit_check.ps1 -Mode validate`, `kit_check.ps1 -Mode check-drift`, `check-readme.ps1`), cola exit
 code e saída de cada um, e trava o veredito mecânico das dimensões `guardas`
-(`docs/RUBRICA_DE_REVISAO.md:94-106` — autoridade integral, sem faixa de juízo: qualquer comando
+(`docs/RUBRICA_DE_REVISAO.md` §4 — autoridade integral, sem faixa de juízo: qualquer comando
 fora de exit 0 resolve para `não conforme`, nunca para `parcial` sozinha) e `testes`
-(`docs/RUBRICA_DE_REVISAO.md:79-92` — evidência mecânica é o exit code do comando `pytest` da
+(`docs/RUBRICA_DE_REVISAO.md` §4 — evidência mecânica é o exit code do comando `pytest` da
 bateria). A bateria de produção (`BATERIA_GUARDAS`) é injetável (`comandos_guardas` em
 `montar_documento`/`rodar_bateria_guardas`) para permitir teste determinístico sem depender da
 infraestrutura real do hub num repositório de fixture.
@@ -593,7 +593,7 @@ def confrontar_escopo(
     root: Path,
     alvos_de_outras_tarefas: dict[str, str] | None = None,
 ) -> dict:
-    """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`) com os cinco
+    """Veredito mecânico da dimensão `escopo` (`docs/RUBRICA_DE_REVISAO.md` §4) com os cinco
     baldes da `DB-25` e da `DB-32`, nesta precedência: coberto pelos alvos do card > registro da
     orquestração > alvo de outra tarefa do mesmo plano > ato do dono fora do ciclo de tarefa >
     fora dos alvos sem atribuição. Só o último resolve o
@@ -828,7 +828,7 @@ def rodar_bateria_guardas(root: Path, comandos: list[tuple[str, list[str]]] | No
 
 
 def veredito_guardas(resultados: list[dict]) -> str:
-    """Veredito mecânico travado da dimensão `guardas` (`docs/RUBRICA_DE_REVISAO.md:94-106`) —
+    """Veredito mecânico travado da dimensão `guardas` (`docs/RUBRICA_DE_REVISAO.md` §4) —
     autoridade integral, sem faixa de juízo (`DA-7`): qualquer comando fora de exit 0 trava em
     `não conforme`; só quando todos os comandos fecham em exit 0 resolve para `conforme`. Nunca
     resolve para `parcial` sozinha (a faixa `parcial` da rubrica depende de julgar se a causa é
@@ -839,7 +839,7 @@ def veredito_guardas(resultados: list[dict]) -> str:
 
 
 def veredito_testes(resultados: list[dict]) -> str:
-    """Veredito mecânico travado da dimensão `testes` (`docs/RUBRICA_DE_REVISAO.md:79-92`) —
+    """Veredito travado da parte mecânica da dimensão `testes` (`docs/RUBRICA_DE_REVISAO.md` §4) —
     evidência mecânica é o exit code do comando `pytest` da bateria: exit 0 trava `conforme`,
     exit não-zero ou comando `pytest` ausente da bateria trava `não conforme` (nunca silêncio)."""
     pytest_resultado = next((r for r in resultados if r["nome"] == "pytest"), None)
@@ -1076,7 +1076,7 @@ def _renderizar(
         )
         linhas.append(
             "- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, "
-            "não coletada por este script; ver docs/RUBR
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index fc48831..78f9c6f 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -111,7 +111,7 @@ def test_tf_escopo_respeitado_quando_tocados_sao_subconjunto_dos_alvos(tmp_path)
 def test_escopo_violado_gera_fato_sem_inventar_parcial(tmp_path):
     """Arquivo fora dos alvos tocado: a saída relata o fato mecânico ('N arquivo(s) fora dos
     alvos') e deixa o veredito em aberto — nunca resolve sozinha para 'parcial' (a faixa
-    'parcial' de RUBRICA_DE_REVISAO.md:63-77 depende de declaração de desvio no pacote de
+    'parcial' de RUBRICA_DE_REVISAO.md §4 depende de declaração de desvio no pacote de
     retorno, insumo que este script não recebe)."""
     review_evidence = _load_review_evidence()
     repo = tmp_path / "repo"
@@ -268,8 +268,8 @@ def test_tf_san_15_evidencia_na_pasta_do_plano(tmp_path, capsys):
 
 
 def test_tf_veredito_guardas_e_testes_travam_conforme_quando_bateria_toda_verde():
-    """TF da EXA-T9b: veredito mecânico das dimensões `guardas` (`RUBRICA_DE_REVISAO.md:94-106`)
-    e `testes` (`RUBRICA_DE_REVISAO.md:79-92`) resolve para `conforme` quando todos os comandos
+    """TF da EXA-T9b: veredito mecânico das dimensões `guardas` (`RUBRICA_DE_REVISAO.md` §4)
+    e `testes` (`RUBRICA_DE_REVISAO.md` §4) resolve para `conforme` quando todos os comandos
     da bateria fecham em exit 0 — teste de unidade sobre a lógica de veredito, sem subprocess."""
     review_evidence = _load_review_evidence()
     resultados = [

```

## Linhas removidas dos testes
### `tests/test_review_evidence.py` — 3 linha(s) removida(s)
```
-    'parcial' de RUBRICA_DE_REVISAO.md:63-77 depende de declaração de desvio no pacote de
-    """TF da EXA-T9b: veredito mecânico das dimensões `guardas` (`RUBRICA_DE_REVISAO.md:94-106`)
-    e `testes` (`RUBRICA_DE_REVISAO.md:79-92`) resolve para `conforme` quando todos os comandos
```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T12a-medida.json; mundo: depois; gerado em: 2026-09-29T09:40:05+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;r=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');e=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');t=Path('tests/test_review_evidence.py').read_text(encoding='utf-8');a=lambda s:sum(s.count('.md:'+n) for n in ('63-77','79-92','94-106'));print('testes=%d-%d ancoras=%d-%d docstring=%d'%(r.count('da área tocada e a seção'),r.count('da área tocada, mecânicos e travados'),a(e),a(t),e.count('Veredito travado da parte mecânica')))"` | 0 | true |

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
