# Evidência de revisão — P-0755 RAF-T23

## Diff (`git diff --stat`)
```
.claude/tools/encerrar.py                          | 270 ++++++++++++++++++---
 docs/DIARIO_DE_OBRAS.md                            |   4 +-
 .../estado.tsv                                     |   2 +-
 .../evidencia/P-0755-RAF-T23-medida-depois.json    |  22 ++
 docs/telemetria.tsv                                |   1 +
 tests/test_encerrar.py                             | 239 ++++++++++++++++++
 6 files changed, 508 insertions(+), 30 deletions(-)
```

## Arquivos tocados
- `.claude/tools/encerrar.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`
- `tests/test_encerrar.py` — atribuição: da entrega; estado git: ` M`

## Escopo
- Recorte: desde `2db279d7495198b52ff0a003feac14775cbd1bee`
- Arquivos-alvo declarados: `.claude/tools/encerrar.py`, `tests/test_encerrar.py`
- Arquivos tocados: `.claude/tools/encerrar.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23-medida-depois.json`, `docs/telemetria.tsv`, `tests/test_encerrar.py`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T23-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/encerrar.py`
```
diff --git a/.claude/tools/encerrar.py b/.claude/tools/encerrar.py
index 0196278..7975f28 100644
--- a/.claude/tools/encerrar.py
+++ b/.claude/tools/encerrar.py
@@ -101,12 +101,22 @@ _caminhos = _carregar("caminhos")
 _backlog = _carregar("backlog")
 _rdo = _carregar("rdo")
 _telemetria = _carregar("telemetria")
+_modelo = _carregar("modelo")
 
 
 class EncerramentoError(ValueError):
     """Checagem que recusa o fechamento — a mensagem nomeia o que falta; nada foi escrito."""
 
 
+class ConflitoDePromocao(EncerramentoError):
+    """`--aceita-versao` em conflito com o estado do plano (`RAF-T23`, `DRF-38`) — carrega o
+    dossiê `Ato: emenda` para o modelador, no atributo `dossie`."""
+
+    def __init__(self, mensagem: str, dossie: str) -> None:
+        super().__init__(mensagem)
+        self.dossie = dossie
+
+
 ACHADOS_HEADING_RE = re.compile(r"^## .*Achados da execução")
 AE_ID_RE = re.compile(r"\bAE-(\d+)\b")
 ROTA_RE = re.compile(r"\*\*Rota:?\*\*|\bRota:")
@@ -910,6 +920,195 @@ _MARCO_SECAO0_RE = re.compile(r"^## 0\.")
 _MARCO_HEADING_RE = re.compile(r"^## ")
 _MARCO_VERSAO_PENDENTE_RE = re.compile(r"^## 1A\. Modelo conceitual — versão pendente de validação")
 _MARCO_COLUNA_RE = re.compile(r"(?<!\\)\|")
+_SOMENTE_DIGITOS_RE = re.compile(r"^\d+$")
+
+
+def _dossie_emenda(
+    plano_path: Path, repo: Path, marco: int, frase: str, fato_novo: str, restricao: str
+) -> str:
+    """O dossiê `Ato: emenda` para o modelador (`OP-12`/`RAF-T23`): motivo do marco, o fato que
+    muda o modelo e a restrição que a emenda tem de respeitar."""
+    return "\n".join([
+        f"Plano: {_rel(plano_path, repo)}",
+        "Ato: emenda",
+        f'Motivo: Marco {marco}, veredito do dono: "{frase}"',
+        f"Fato novo: {fato_novo}",
+        f"Restrição: {restricao}",
+        "Devolver: a seção ## 1 depois do ato e a linha nova do registro de versões.",
+    ])
+
+
+def _faixa_do_campo_operacao(linhas: list[str], tarefa_id: str) -> tuple[int, int] | None:
+    """O card vai do cabeçalho `### <ID> — ` até a linha antes do próximo `### ` ou `## `.
+    Devolve `(linha do campo Operação do modelo, primeira linha depois dos sub-bullets)`, ou
+    `None` sem card ou sem campo (`RAF-T23`)."""
+    prefixo = f"### {tarefa_id} — "
+    idx_card = next((i for i, l in enumerate(linhas) if l.startswith(prefixo)), None)
+    if idx_card is None:
+        return None
+    fim_card = next(
+        (
+            i
+            for i in range(idx_card + 1, len(linhas))
+            if linhas[i].startswith("### ") or linhas[i].startswith("## ")
+        ),
+        len(linhas),
+    )
+    idx_campo = next(
+        (
+            i
+            for i in range(idx_card + 1, fim_card)
+            if linhas[i].startswith("- **Operação do modelo:**")
+        ),
+        None,
+    )
+    if idx_campo is None:
+        return None
+    fim_campo = idx_campo + 1
+    while fim_campo < fim_card and linhas[fim_campo].startswith("  "):
+        fim_campo += 1
+    return idx_campo, fim_campo
+
+
+def promover_versao(linhas: list[str], k: int, data: str) -> tuple[list[str], int]:
+    """`DRF-38` (`RAF-T23`) — promove a versão pendente (`## 1A`) a vigente (`## 1`): no
+    registro de versões, a linha `vigente` cai a `obsoleta` (com o motivo na célula `por`) e a
+    linha da versão `k` sobe a `vigente`; a `## 1` vira o conteúdo da `## 1A` (cabeçalho
+    `situação: vigente`) e a `## 1A` sai do plano; o campo `Operação do modelo` de cada card
+    citado nas `tarefas:` da pendente é reescrito com as operações e contratos dela. Devolve as
+    linhas e o número de cards distintos reescritos."""
+    linhas = list(linhas)
+
+    modelo_pendente = _modelo.extrair_modelo(linhas, _modelo._HEADING_PENDENTE)
+    obj_por_nome = {o.nome: o for o in modelo_pendente.objetos}
+
+    idx_h1 = linhas.index(_modelo._HEADING_VIGENTE)
+    fim_h1 = next(
+        (i for i in range(idx_h1 + 1, len(linhas)) if linhas[i].startswith("## ")), len(linhas)
+    )
+    idx_h
```
[truncado em 4000 caracteres]

### `tests/test_encerrar.py`
```
diff --git a/tests/test_encerrar.py b/tests/test_encerrar.py
index d595dc3..bd5449e 100644
--- a/tests/test_encerrar.py
+++ b/tests/test_encerrar.py
@@ -901,3 +901,242 @@ def test_tf_conclusao_da_tarefa_sem_erro_de_concordancia(tmp_path, capsys):
     saida = capsys.readouterr().out
     assert "encerrar: OK - comando 'tarefa' concluído;" in saida
     assert "tarefa fechado" not in saida
+
+
+# --- marco --aceita-versao (RAF-T23) ------------------------------------------------------------
+
+
+PLANO_MARCO_PROMOCAO = """# P-0001 — Plano marco
+
+**Prefixo das tarefas no diário:** `MRC-T<n>`
+
+**Marcos de validação pelo dono:**
+
+| marco | o que o dono lê | veredito |
+|---|---|---|
+| **Marco 1** | a seção 1 | go |
+| **Marco 2** | a etapa A | pendente |
+
+## 0. O problema, verbatim
+
+Texto do problema, verbatim.
+
+## 1. Modelo conceitual
+
+**Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente
+
+### 1.1 Objetos
+
+| objeto | o que é | propriedades | contrato | origem | lastro |
+|---|---|---|---|---|---|
+| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
+| produto | o produto da operação | status | um registro validado | OP-1 | lastro da fixture |
+
+### 1.2 Fluxo de operações
+
+- **OP-1** — Primeira operação da fixture.
+  - `precisa de: insumo` · `altera: produto.status` · `tarefas: MRC-T1`
+
+### 1.3 Estado inicial e estado final
+
+| propriedade | estado inicial | estado final |
+|---|---|---|
+| insumo.status | lido | lido |
+| produto.status | rascunho | validado |
+
+### 1.4 Registro de versões
+
+| versão | data | situação | por |
+|---|---|---|---|
+| 1 | 2026-09-10 | vigente | modelador |
+| 2 | 2026-09-21 | pendente | modelador, emenda |
+
+## 1A. Modelo conceitual — versão pendente de validação
+
+**Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente
+
+### 1.1 Objetos
+
+| objeto | o que é | propriedades | contrato | origem | lastro |
+|---|---|---|---|---|---|
+| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
+| esboço | o esboço da operação nova | estado | um esboço revisado | OP-1 | lastro da fixture |
+| produto | o produto da operação | status | um registro validado | OP-2 | lastro da fixture |
+
+### 1.2 Fluxo de operações
+
+- **OP-1** — Operação nova, inserida antes.
+  - `precisa de: insumo` · `altera: esboço.estado` · `tarefas: @TAREFAS_OP1@`
+- **OP-2** — Primeira operação da fixture.
+  - `precisa de: esboço` · `altera: produto.status` · `tarefas: MRC-T1`
+
+### 1.3 Estado inicial e estado final
+
+| propriedade | estado inicial | estado final |
+|---|---|---|
+| insumo.status | lido | lido |
+| esboço.estado | vazio | revisado |
+| produto.status | rascunho | validado |
+
+## 5. Tarefas
+
+### MRC-T1 — Tarefa da operação antiga [Sonnet · classe implementacao]
+- **Objetivo:** entregar algo.
+- **Operação do modelo:** `OP-1`
+  - OP-1: Primeira operação da fixture.
+  - precisa de: insumo — um registro por rodada
+- **Arquivos-alvo:** `a.py`.
+- **Verificação:** `pytest -q`.
+- **Pronto quando:** o teste passa.
+
+### MRC-T2 — Tarefa da operação nova [Sonnet · classe implementacao]
+- **Objetivo:** entregar outra coisa.
+- **Operação do modelo:** `OP-1`
+  - OP-1: Operação nova, inserida antes.
+  - precisa de: insumo — um registro por rodada
+- **Arquivos-alvo:** `b.py`.
+- **Verificação:** `pytest -q`.
+- **Pronto quando:** o teste passa.
+"""
+
+
+def _montar_repo_promocao(tmp_path: Path, tarefas_op1: str = "MRC-T2") -> Path:
+    return _montar_repo_marco(tmp_path, PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", tarefas_op1))
+
+
+def _card(texto: str, tarefa: str) -> str:
+    prefixo = f"### {tarefa} — "
+    idx = texto.index(prefixo)
+    fim = texto.find("\n### ", idx)
+    return texto[idx:] if fim == -1 else texto[idx:fim]
+
+
+def test_tf_marco_promove_versao_aceita_e_reescreve_
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
### `tests/test_encerrar.py` — nenhuma linha removida

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T23-medida-depois.json; mundo: depois; gerado em: 2026-09-29T21:20:23+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -m pytest tests/test_encerrar.py -q -k promove_versao` | 0 | true |
| 2 | `python -m pytest tests/test_encerrar.py -q -k validacao_do_consultor` | 0 | true |

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
