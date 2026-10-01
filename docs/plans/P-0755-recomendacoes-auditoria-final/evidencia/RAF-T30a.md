# Evidência de revisão — P-0755 RAF-T30a

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-reviewer.md                |  5 ++--
 .claude/tools/rdo.py                               | 15 ++++++++----
 docs/DIARIO_DE_OBRAS.md                            |  4 ++--
 docs/RUBRICA_DE_REVISAO.md                         |  3 ++-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T30a-medida-depois.json   | 22 +++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_rdo.py                                  | 28 ++++++++++++++++++++++
 8 files changed, 69 insertions(+), 11 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-reviewer.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/rdo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T30a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_rdo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `033cd4ebd4972068f50707f7dbb05d651e5988f4`
- Arquivos-alvo declarados: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `docs/RUBRICA_DE_REVISAO.md`, `.claude/agents/pantonic-reviewer.md`
- Arquivos tocados: `.claude/agents/pantonic-reviewer.md`, `.claude/tools/rdo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T30a-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_rdo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T30a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 9b376ed..e29c010 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -40,7 +40,7 @@ diretório se preciso. `--vermelho-mecanico <dimensao>` (repetível) declara o q
 já reportou vermelho; marcar `conforme` contra uma dimensão declarada vermelha é recusado (`DA-7`).
 `--escalar "<uma linha>"` força `recomendacao=escalar` independentemente da tabela, e a linha
 gravada é a pendência que a regra `B1` consome. `--achado-processo <alvo> "<uma linha>"`
-(repetível; alvo em `dossie` — ou `dossiê` —, `doutrina`, `rubrica` ou `modelo`) grava a seção `## Achado de processo` e
+(repetível; alvo em `dossie` — ou `dossiê` —, `doutrina`, `rubrica`, `modelo` ou `instrumento`) grava a seção `## Achado de processo` e
 **não** altera percentual, veredito, bloqueante nem recomendação — invariante 1 de
 `docs/RUBRICA_DE_REVISAO.md` §6; `--escalar` fica reservado ao achado que invalida a rota (decisão
 de arquitetura ou de requisito). `--motivo <dimensao> "<uma linha>"` (repetível, só para dimensão
@@ -572,13 +572,18 @@ def calcular_laudo(
     )
 
 
-_ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo"}
+# O quinto alvo, `instrumento`, é o que o aviso `B1` do `encerrar.py tarefa` lê (RAF-T30a, `DRF-68`
+# do P-0755).
+_ALVOS_ACHADO = {
+    "dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo",
+    "instrumento": "instrumento",
+}
 # Grafia acentuada aceita na entrada e normalizada antes da validação (TK-85a).
 _SINONIMOS_ALVO = {"dossiê": "dossie"}
 
 
 def _formatar_achados_processo(pares: list[list[str]] | None) -> str:
-    """`docs/RUBRICA_DE_REVISAO.md` §6: campo próprio, quatro alvos. Invariante 1 — o achado não
+    """`docs/RUBRICA_DE_REVISAO.md` §6: campo próprio, cinco alvos. Invariante 1 — o achado não
     rebaixa dimensão de entrega e não muda recomendação; por isso nada disto passa por
     `calcular_laudo`. Sem achado, o corpo é `nenhum` (a seção existe sempre)."""
     if not pares:
@@ -997,8 +1002,8 @@ def main(argv: list[str] | None = None) -> int:
         metavar=("ALVO", "LINHA"),
         default=None,
         help=(
-            "Achado de processo (repetivel): ALVO e dossie (ou dossiê), doutrina, rubrica ou modelo, "
-            "seguido de uma linha. Nao altera percentual, veredito, bloqueante nem recomendacao "
+            "Achado de processo (repetivel): ALVO e dossie (ou dossiê), doutrina, rubrica, modelo "
+            "ou instrumento, seguido de uma linha. Nao altera percentual, veredito, bloqueante nem recomendacao "
             "(RUBRICA §6)."
         ),
     )

```

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index bcb1290..a79567e 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -1373,3 +1373,31 @@ def test_laudo_achado_dossie_acentuado(tmp_path):
     assert exit_code == 0
     conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
     assert "| dossiê | linha do achado |" in conteudo
+
+
+# --- laudo · achado de processo, alvo instrumento (RAF-T30a do P-0755, `DRF-68`) --------------
+
+
+def test_tf_laudo_alvo_instrumento_chega_ao_aviso_b1_do_fechamento(tmp_path):
+    """TF (RAF-T30a, `DRF-68`): `--achado-processo instrumento "<linha>"` sai 0, o laudo tem a
+    linha `| instrumento | <linha> |`, e o `achados_do_laudo` do `encerrar.py` a devolve como o
+    achado que o aviso `B1` da `RAF-T30` casa — o caminho do gerador ao fechamento, que o card
+    da `RAF-T30` montava à mão. Hoje o alvo é recusado (exit 1) e nenhum laudo o escreve."""
+    rdo = _load_rdo()
+    laudos_dir = tmp_path / "laudos"
+    linha = "o card_check caiu com Traceback no item 2. Rota: tíquete"
+
+    exit_code = rdo.main(_argv_laudo(laudos_dir) + ["--achado-processo", "instrumento", linha])
+
+    assert exit_code == 0
+    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
+    assert f"| instrumento | {linha} |" in conteudo
+    spec = importlib.util.spec_from_file_location(
+        "encerrar_do_rdo", _ROOT / ".claude" / "tools" / "encerrar.py"
+    )
+    encerrar = importlib.util.module_from_spec(spec)
+    sys.modules[spec.name] = encerrar
+    spec.loader.exec_module(encerrar)
+    textos = [texto for texto, _rota in encerrar.achados_do_laudo(conteudo)]
+    assert textos == ["achado de processo (instrumento): o card_check caiu com Traceback no item 2."]
+    assert encerrar._ACHADO_INSTRUMENTO_RE.search(textos[0])

```

### `docs/RUBRICA_DE_REVISAO.md`
```
diff --git a/docs/RUBRICA_DE_REVISAO.md b/docs/RUBRICA_DE_REVISAO.md
index 4a6ce86..4db4c20 100644
--- a/docs/RUBRICA_DE_REVISAO.md
+++ b/docs/RUBRICA_DE_REVISAO.md
@@ -254,7 +254,7 @@ critério de pronto inverificável, dossiê que empurra a execução contra a ar
 exigida que não discrimina nada: corrigir o sintoma na entrega deixa a causa de pé, e a tarefa
 seguinte reincide.
 
-O laudo carrega um campo próprio para esse achado, com quatro alvos possíveis:
+O laudo carrega um campo próprio para esse achado, com cinco alvos possíveis:
 
 | alvo | o que o achado denuncia |
 |---|---|
@@ -262,6 +262,7 @@ O laudo carrega um campo próprio para esse achado, com quatro alvos possíveis:
 | `doutrina` | guardrail ausente, ambíguo ou em conflito com outro |
 | `rubrica` | dimensão mal formulada, nível sem fronteira clara, peso desalinhado com o dano real |
 | `modelo` | operação do modelo de domínio do plano que a entrega tornou falsa ou ambígua (`GOVERNANCA.md` §3.2); rota: dossiê `Ato de modelo` de conflito, devolvido junto com o laudo e despachado ao `pantonic-model-designer` por quem conduz a sessão — nunca corrigido pelo reviewer |
+| `instrumento` | instrumento do kit que caiu, devolveu saída errada ou recusou entrada válida na execução ou na revisão; o `encerrar.py tarefa` avisa, na linha `encerrar: B1 —`, o achado deste alvo que relata queda, traceback, exceção ou erro |
 
 Três invariantes governam a via:
 

```

### `.claude/agents/pantonic-reviewer.md`
```
diff --git a/.claude/agents/pantonic-reviewer.md b/.claude/agents/pantonic-reviewer.md
index fce5827..6799717 100644
--- a/.claude/agents/pantonic-reviewer.md
+++ b/.claude/agents/pantonic-reviewer.md
@@ -25,8 +25,9 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
   travado no dossiê de evidência, e marcar `conforme` contra um vermelho declarado é recusado
   pelo gerador. O juízo opera nas dimensões de fonte de juízo e nas faixas que a evidência
   mecânica deixa em aberto.
-- Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e quatro alvos possíveis —
-  `dossiê`, `doutrina`, `rubrica`, `modelo`. Ele nunca rebaixa dimensão de entrega e sempre sai com rota.
+- Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e cinco alvos possíveis —
+  `dossiê`, `doutrina`, `rubrica`, `modelo`, `instrumento`. Ele nunca rebaixa dimensão de entrega
+  e sempre sai com rota.
 - **Decisão tomada pela entrega que o card não fechou** (nome, rota, valor, teste inventado) e
   **parada por dúvida que o card não previu** são a mesma classe: defeito do dossiê, não da
   execução (G-NOASK, `GOVERNANCA.md` §7 item 18). Saem como achado de processo de alvo `dossiê`,

```

## Linhas removidas dos testes
### `tests/test_rdo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T30a-medida-depois.json; mundo: depois; gerado em: 2026-09-30T01:34:08+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_rdo.py -q -k alvo_instrumento` | 0 | true |
| 2 | `python -c "from pathlib import Path;b=chr(96);r=Path('.claude/tools/rdo.py').read_text(encoding='utf-8');u=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');v=Path('.claude/agents/pantonic-reviewer.md').read_text(encoding='utf-8');print('alvos=%d-%d-%d rdo=%d-%d-%d'%(r.count('quatro alvos')+u.count('quatro alvos')+v.count('quatro alvos'),u.count('\| '+b+'instrumento'+b+' \|'),v.count(b+'modelo'+b+', '+b+'instrumento'+b),r.count('ou '+b+'instrumento'+b),r.count('ou instrumento, seguido'),r.count('cinco alvos')))"` | 0 | true |

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
