# Evidência de revisão — P-0755 RAF-T27

## Diff (`git diff --stat`)
```
.claude/tools/prevoo.py                            | 48 ++++++++++++-
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T27-medida-depois.json    | 22 ++++++
 docs/telemetria.tsv                                |  1 +
 tests/test_prevoo.py                               | 80 ++++++++++++++++++++++
 6 files changed, 151 insertions(+), 6 deletions(-)
```

## Arquivos tocados
- `.claude/tools/prevoo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T27-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_prevoo.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `643d75d5120589297b20cb8a193795f9ae5d80e5`
- Arquivos-alvo declarados: `.claude/tools/prevoo.py`, `tests/test_prevoo.py`
- Arquivos tocados: `.claude/tools/prevoo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T27-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_prevoo.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T27-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/prevoo.py`
```
diff --git a/.claude/tools/prevoo.py b/.claude/tools/prevoo.py
index 1f85551..02ebdce 100644
--- a/.claude/tools/prevoo.py
+++ b/.claude/tools/prevoo.py
@@ -54,8 +54,20 @@ def _normalizar(token: str) -> str:
     return token
 
 
+_RE_EXTENSAO_CURTA = re.compile(r"\.[A-Za-z0-9]{1,5}$")
+
+
 def _e_caminho(token: str) -> bool:
-    return token.endswith(_EXTENSOES_CAMINHO) or token.endswith("/")
+    """`R-17` (auditoria reg. 2) e `DRF-19` do `P-0755`: extensão solta sem `/` não é caminho —
+    verdadeiro quando `token` termina em `/`; ou quando tem `/` e o último segmento (depois da
+    última `/`) casa `_RE_EXTENSAO_CURTA` (qualquer extensão curta, não só as nove conhecidas);
+    ou quando não tem `/`, termina numa das nove `_EXTENSOES_CAMINHO` e não começa por `.`."""
+    if token.endswith("/"):
+        return True
+    if "/" in token:
+        ultimo_segmento = token.rsplit("/", 1)[1]
+        return bool(_RE_EXTENSAO_CURTA.search(ultimo_segmento))
+    return token.endswith(_EXTENSOES_CAMINHO) and not token.startswith(".")
 
 
 def _e_flag(token: str) -> bool:
@@ -99,6 +111,30 @@ def _extrair(texto: str) -> tuple[list[str], list[str], list[str]]:
     return caminhos, simbolos, flags
 
 
+_VERBOS_DE_CRIACAO = {"crie", "criar", "grave", "gravar", "escreva", "escrever", "gere", "gerar"}
+_RE_FIM_DE_FRASE = re.compile(r"\. |\n")
+
+
+def _caminhos_a_criar(texto: str) -> set[str]:
+    """Caminhos que o pedido manda criar: `texto` se divide em frases por `_RE_FIM_DE_FRASE`; em
+    cada frase, os tokens (normalizados por `_normalizar`) depois do primeiro cujo `lower()` é um
+    dos `_VERBOS_DE_CRIACAO` entram no conjunto devolvido quando são caminho por `_e_caminho`."""
+    resultado: set[str] = set()
+    for frase in _RE_FIM_DE_FRASE.split(texto):
+        verbo_visto = False
+        for bruto in frase.split():
+            token = _normalizar(bruto)
+            if not token:
+                continue
+            if not verbo_visto:
+                if token.lower() in _VERBOS_DE_CRIACAO:
+                    verbo_visto = True
+                continue
+            if _e_caminho(token):
+                resultado.add(token)
+    return resultado
+
+
 def _achar_simbolo(root: Path, nome: str) -> str | None:
     """Procura `def <nome>(` ou `class <nome>` em todo `.py` sob `root` (fora de `.git` e
     `__pycache__`); devolve `<arquivo>:<linha>` (com `/`) da primeira ocorrência, ou `None`."""
@@ -155,10 +191,16 @@ def main(argv: list[str] | None = None) -> int:
     linhas: list[tuple[str, str, str]] = [("citado", "existe", "onde")]
     tudo_existe = True
 
+    a_criar = _caminhos_a_criar(args.texto)
     for caminho in caminhos:
         existe = (root / caminho).exists()
-        tudo_existe = tudo_existe and existe
-        linhas.append((caminho, "sim" if existe else "não", caminho if existe else "—"))
+        if existe:
+            linhas.append((caminho, "sim", caminho))
+        elif caminho in a_criar:
+            linhas.append((caminho, "criar", "—"))
+        else:
+            tudo_existe = False
+            linhas.append((caminho, "não", "—"))
 
     for simbolo in simbolos:
         onde = _achar_simbolo(root, simbolo)

```

### `tests/test_prevoo.py`
```
diff --git a/tests/test_prevoo.py b/tests/test_prevoo.py
index cb4aeb7..a33d33a 100644
--- a/tests/test_prevoo.py
+++ b/tests/test_prevoo.py
@@ -159,3 +159,83 @@ def test_tr_prevoo_flag_com_pontuacao(tmp_path, capsys):
         "citado | existe | onde",
         "--plano | sim | .claude/tools/x.py:1",
     ]
+
+
+_PEDIDO_MEDIDO_R17 = (
+    "Crie em scratch_sonda/ duas coisas: (1) as amostras scratch_sonda/amostras/a.txt, "
+    "scratch_sonda/amostras/b.txt e o binário scratch_sonda/amostras/c.bin; (2) o utilitário "
+    "scratch_sonda/contar.py, que recebe caminhos de arquivo e imprime, por arquivo .txt, o "
+    "número de linhas, recusando com mensagem o caminho que não existe, com os testes em "
+    "tests/test_sonda_auditoria_final.py. Tudo só com biblioteca padrão."
+)
+
+
+def test_tf_prevoo_conta_como_caminho_sem_extensao_solta(tmp_path, capsys):
+    """`F-22`/`R-17`: extensão solta sem `/` (`.txt`) não é caminho — o binário `dados/c.bin`,
+    citado com `/`, é (hoje: `.txt | não | —` e nenhuma linha de `dados/c.bin`)."""
+    prevoo = _load_prevoo()
+    codigo = prevoo.main([
+        "leia, por arquivo .txt, o binário dados/c.bin",
+        "--root",
+        str(tmp_path),
+    ])
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert saida.out.splitlines() == [
+        "citado | existe | onde",
+        "dados/c.bin | não | —",
+    ]
+
+
+def test_tr_prevoo_conta_como_caminho_nome_solto_conhecido(tmp_path, capsys):
+    """Nome solto sem `/` com uma das nove extensões conhecidas continua caminho — a regra
+    concorrente, exigir `/`, o perderia."""
+    (tmp_path / "notas.md").write_text("nota\n", encoding="utf-8")
+
+    prevoo = _load_prevoo()
+    codigo = prevoo.main(["leia notas.md antes", "--root", str(tmp_path)])
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert saida.out.splitlines() == [
+        "citado | existe | onde",
+        "notas.md | sim | notas.md",
+    ]
+
+
+def test_tf_prevoo_caminho_a_criar_no_pedido_medido(tmp_path, capsys):
+    """`R-17`: pedido medido do plano fictício — os seis caminhos citados depois de `Crie` na
+    mesma frase saem como `criar`, sem derrubar o exit (hoje: seis linhas `não` e exit 1)."""
+    prevoo = _load_prevoo()
+    codigo = prevoo.main([_PEDIDO_MEDIDO_R17, "--root", str(tmp_path)])
+    saida = capsys.readouterr()
+
+    assert codigo == 0
+    assert saida.out.splitlines() == [
+        "citado | existe | onde",
+        "scratch_sonda/ | criar | —",
+        "scratch_sonda/amostras/a.txt | criar | —",
+        "scratch_sonda/amostras/b.txt | criar | —",
+        "scratch_sonda/amostras/c.bin | criar | —",
+        "scratch_sonda/contar.py | criar | —",
+        "tests/test_sonda_auditoria_final.py | criar | —",
+    ]
+
+
+def test_tr_prevoo_caminho_a_criar_so_na_mesma_frase(tmp_path, capsys):
+    """O verbo de criação vale só na própria frase — a regra concorrente, verbo em qualquer
+    ponto do texto, daria `criar` para `docs/x.md`."""
+    prevoo = _load_prevoo()
+    codigo = prevoo.main([
+        "Crie o módulo novo. Leia docs/x.md depois",
+        "--root",
+        str(tmp_path),
+    ])
+    saida = capsys.readouterr()
+
+    assert codigo == 1
+    assert saida.out.splitlines() == [
+        "citado | existe | onde",
+        "docs/x.md | não | —",
+    ]

```

## Linhas removidas dos testes
### `tests/test_prevoo.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T27-medida-depois.json; mundo: depois; gerado em: 2026-09-29T23:29:06+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_prevoo.py -q -k conta_como_caminho` | 0 | true |
| 2 | `python -m pytest tests/test_prevoo.py -q -k caminho_a_criar` | 0 | true |

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
