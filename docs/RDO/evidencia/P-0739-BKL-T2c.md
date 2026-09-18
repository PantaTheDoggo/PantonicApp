# Evidência de revisão — P-0739 BKL-T2c

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md       |   6 +
 .claude/tools/rdo.py                     |   6 +-
 .claude/tools/review_evidence.py         | 206 ++++++-
 CHANGELOG.md                             |   8 +
 docs/DIARIO_DE_OBRAS.md                  |   8 +-
 docs/plans/P-0739-backlog-instrumento.md | 961 ++++++++++++++++++++++++++++++-
 docs/telemetria.tsv                      |   9 +
 tests/test_rdo.py                        |  66 +++
 tests/test_review_evidence.py            | 166 +++++-
 9 files changed, 1383 insertions(+), 53 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-planner.md`
- `.claude/tools/rdo.py`
- `.claude/tools/review_evidence.py`
- `CHANGELOG.md`
- `docs/DIARIO_DE_OBRAS.md`
- `docs/RDO/evidencia/P-0739-BKL-T2.md`
- `docs/RDO/evidencia/P-0739-BKL-T2a.md`
- `docs/RDO/evidencia/P-0739-BKL-T2b.md`
- `docs/RDO/laudos/P-0739-BKL-T2.md`
- `docs/RDO/laudos/P-0739-BKL-T2a.md`
- `docs/plans/P-0739-backlog-instrumento.md`
- `docs/telemetria.tsv`
- `tests/test_rdo.py`
- `tests/test_review_evidence.py`

## Escopo
- Recorte: desde `6d7433c`
- Arquivos-alvo declarados: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`, `CHANGELOG.md`
- Literais não reconhecidos como caminho (7): `def confrontar_escopo(`, `return {"fora_dos_alvos": fora, "veredito": None}`, `## Escopo`, `_renderizar`, `escopo = confrontar_escopo(tocados, arquivos_alvo, root)`, `## [Não lançado]`, `DB-13`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py`, `CHANGELOG.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/P-0739-BKL-T2.md`, `docs/RDO/evidencia/P-0739-BKL-T2a.md`, `docs/RDO/evidencia/P-0739-BKL-T2b.md`, `docs/RDO/laudos/P-0739-BKL-T2.md`, `docs/RDO/laudos/P-0739-BKL-T2a.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`, `tests/test_rdo.py`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/tools/rdo.py` → `BKL-T2a`, `docs/DIARIO_DE_OBRAS.md` → `BKL-T6`, `tests/test_rdo.py` → `BKL-T2a`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/P-0739-BKL-T2.md`, `docs/RDO/evidencia/P-0739-BKL-T2a.md`, `docs/RDO/evidencia/P-0739-BKL-T2b.md`, `docs/RDO/laudos/P-0739-BKL-T2.md`, `docs/RDO/laudos/P-0739-BKL-T2a.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `.claude/agents/pantonic-planner.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/review_evidence.py`
```
diff --git a/.claude/tools/review_evidence.py b/.claude/tools/review_evidence.py
index 6feefbd..92b09ac 100644
--- a/.claude/tools/review_evidence.py
+++ b/.claude/tools/review_evidence.py
@@ -16,12 +16,15 @@ na entrega — insumo que este script não recebe. Por isso, quando há arquivo
 dos alvos, a saída relata o **fato** ("N arquivo(s) fora dos alvos: ...") e deixa o veredito em
 aberto; nunca resolve sozinha para `parcial`.
 
-Limitação conhecida e aceita da extração de arquivos-alvo: o campo `Arquivos-alvo`/`Entregável` do
-dossiê é prosa livre: a extração é puramente textual (todo caminho entre crases é tratado como
-alvo declarado), então uma frase como "não editar `x.py`" também cita `x.py` entre crases e o
-script o inclui como se fosse alvo. Interpretar a negação é trabalho do reviewer, não deste
-script — resolver isso aqui seria reinterpretar prosa, não medir fato (fora do escopo desta
-fatia).
+Forma canônica do campo `Arquivos-alvo` (`P-0739` `DB-26`/`DB-27`): um caminho por bullet, o
+caminho como primeiro literal entre crases do bullet, com sufixo opcional `:<linha>`. A extração
+é mecânica e por **literal**, não por linha — `_parsear_campos` (`.claude/tools/rdo.py:151-183`)
+junta as linhas de um campo com espaço, e a estrutura de bullets não chega até aqui. Todo literal
+entre crases é candidato; vira alvo só quando casa `_CAMINHO_RE` e tem extensão, barra ou termina
+em `/`. Literal descartado (trecho de regex, cabeçalho de seção) sai na seção `## Escopo` como
+"não reconhecido como caminho", nunca como bloqueio. Limitação que permanece e é do revisor, não
+deste script: caminho citado em prosa negativa dentro do campo ("não editar `x/y.py`") conta como
+alvo declarado — por isso a forma canônica manda a citação negativa para `Não fazer`.
 
 A seção `## Guardas` (`EXA-T9b`) invoca a bateria de seis comandos de `GOVERNANCA.md` §3 (a
 mesma que fechou a `T9a`: `python -m pytest -q`, `dead_code.py`, `ratchet_piso.py`,
@@ -41,7 +44,13 @@ conjunto de arquivos tocados agora aceita `--desde <ref>` (`coletar_arquivos_toc
 recortar só o que mudou a partir de uma referência git, em vez de sempre varrer a árvore de
 trabalho inteira — necessário quando outras tarefas têm mudanças soltas, não commitadas, no mesmo
 repositório. Ausência de `--desde` preserva o comportamento anterior integralmente, e a seção
-`## Escopo` sempre declara explicitamente qual recorte foi medido."""
+`## Escopo` sempre declara explicitamente qual recorte foi medido.
+
+A seção `## Escopo` classifica o arquivo tocado em quatro baldes (`P-0739` `DB-25`): coberto
+pelos alvos do card; alvo declarado por outra tarefa do mesmo plano; registro da orquestração
+(`docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/`, `docs/RDO/`); fora dos alvos
+sem atribuição. Só o último resolve o veredito — `git` não sabe qual tarefa tocou qual arquivo,
+e o plano sabe qual tarefa declarou qual alvo."""
 from __future__ import annotations
 
 import argparse
@@ -75,19 +84,58 @@ def _load_rdo(root: Path):
     return modulo
 
 
-def extrair_arquivos_alvo(campos: dict) -> list[str]:
-    """Extrai os caminhos declarados no campo `Arquivos-alvo`/`Entregável` do dossiê — extração
-    textual mecânica (tudo entre crases que contém `/`), sem interpretar prosa negativa. Ver
-    limitação conhecida no docstring do módulo."""
+_CAMINHO_RE = re.compile(r"^[A-Za-z0-9_.][A-Za-z0-9_./\\-]*$")
+_EXTENSAO_RE = re.compile(r"\.[A-Za-z0-9]+$")
+
+
+def _eh_caminho(candidato: str) -> bool:
+    """Gramática de caminho da `DB-27` (`P-0739`): sem espaço e sem metacaractere de regex, e
+    com extensão, barra, ou barra final. Recusa `_ID_HEADER_RE = re.compile(...)` (espaço) e
+    `BKL-T9` (sem extensão e sem barra); aceita `CHANGELOG.md` e `tests/fixtures/backlog/`."""
+    if not _CAMINHO_RE.fullmatch(candidato):
+        return False
+    return (
+        "/" in candidato
+        or "\\" in candidato
+        or candidato.endswith("/")
+        or bool(_EXTENSAO_RE.searc
```
[truncado em 4000 caracteres]

### `tests/test_review_evidence.py`
```
diff --git a/tests/test_review_evidence.py b/tests/test_review_evidence.py
index afc9964..6c5f659 100644
--- a/tests/test_review_evidence.py
+++ b/tests/test_review_evidence.py
@@ -124,7 +124,7 @@ def test_escopo_violado_gera_fato_sem_inventar_parcial(tmp_path):
 
     assert "Veredito mecânico: conforme" not in documento
     assert "parcial" not in documento
-    assert "1 arquivo(s) fora dos alvos: `docs/nota.txt`" in documento
+    assert "1 arquivo(s) fora dos alvos e sem atribuição: `docs/nota.txt`" in documento
 
 
 def test_trechos_truncados_pelo_teto_marcam_truncamento_visivel(tmp_path):
@@ -342,3 +342,167 @@ def test_escopo_declara_recorte_arvore_inteira_sem_desde(tmp_path):
     assert (
         "- Recorte: árvore de trabalho inteira (nenhum `--desde` informado)" in documento
     )
+
+
+def test_tf_extrair_arquivos_alvo_aceita_arquivo_de_raiz_e_recusa_literal_de_regex():
+    """TF da BKL-T2b: arquivo de raiz (`CHANGELOG.md`, sem barra, com extensão) passa a ser
+    reconhecido como alvo; literal de trecho de regex (`_ID_HEADER_RE = re.compile(x)`, com
+    espaço) é recusado pela gramática de caminho da `DB-27`."""
+    review_evidence = _load_review_evidence()
+    campos = {
+        "arquivos-alvo": (
+            "- `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` "
+            "- `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)"
+        )
+    }
+    resultado = review_evidence.extrair_arquivos_alvo(campos)
+    assert resultado == [".claude/tools/rdo.py", "CHANGELOG.md"]
+
+
+def test_tr_extrair_literais_nao_caminho_lista_o_descartado():
+    """Regressão: os literais entre crases que não casam a gramática de caminho (cabeçalho de
+    seção, trecho de regex) saem em `extrair_literais_nao_caminho`, não silenciosamente."""
+    review_evidence = _load_review_evidence()
+    campos = {
+        "arquivos-alvo": (
+            "- `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` "
+            "- `CHANGELOG.md` — uma linha sob `## [Não lançado]` (`CHANGELOG.md:17`)"
+        )
+    }
+    resultado = review_evidence.extrair_literais_nao_caminho(campos)
+    assert "## [Não lançado]" in resultado
+    assert any("re.compile" in item for item in resultado)
+
+
+def test_tr_extrair_arquivos_alvo_recusa_id_de_tarefa_e_de_decisao():
+    """Regressão: identificador de tarefa/decisão entre crases (sem barra e sem extensão) não é
+    caminho pela gramática da `DB-27` e não vira alvo declarado."""
+    review_evidence = _load_review_evidence()
+    campos = {"arquivos-alvo": "ver `BKL-T9` e `DB-13`."}
+    resultado = review_evidence.extrair_arquivos_alvo(campos)
+    assert resultado == []
+
+
+def test_tf_secao_escopo_lista_literais_nao_reconhecidos_como_caminho(tmp_path):
+    """TF de ponta a ponta da BKL-T2b: um literal de trecho de regex citado no campo
+    `Arquivos-alvo` aparece na seção `## Escopo` como literal não reconhecido como caminho."""
+    review_evidence = _load_review_evidence()
+    repo = tmp_path / "repo"
+    _init_repo_com_baseline(repo)
+    plano = tmp_path / "plano.md"
+    _escrever_plano(plano, "cria `src/a.py`; ver `_RE = re.compile(x)`.")
+    (repo / "src" / "a.py").write_text("def a():\n    return 2\n", encoding="utf-8")
+
+    documento = review_evidence.montar_documento(
+        plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE
+    )
+
+    assert "Literais não reconhecidos como caminho (1)" in documento
+
+
+def _escrever_plano_duas_tarefas(
+    caminho: Path, alvo_t1: str, alvo_t2: str, verificacao_t2: str | None = "bateria do §3."
+) -> None:
+    """Plano sintético com duas tarefas; `verificacao_t2=None` omite um campo obrigatório de T2
+    para exercitar o ramo 'dossiê inválido é pulado' de `mapear_alvos_de_outras_tarefas`."""
+    linha_verificacao = f"- **Verificação:** {verificacao_t2}\n" if verificacao_t2 else ""
+    texto = (
+        "# Plano de teste\n\n"
+        "### T1 — Tarefa sintética de teste [Sonnet · clas
```
[truncado em 4000 caracteres]

### `CHANGELOG.md`
```
diff --git a/CHANGELOG.md b/CHANGELOG.md
index d06abb5..093f005 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -16,6 +16,7 @@ reescritas nem revogadas.
 
 ## [Não lançado]
 
+- `review_evidence.py`: confronto de escopo atribui arquivo tocado a outra tarefa do plano e separa o registro da orquestração, em vez de reportar tudo como fora-de-alvo (`P-0739` `BKL-T2c`, `DB-25`).
 - `G-NOASK` (`GOVERNANCA.md` §7 item 18, 2026-09-16, decisão do dono): interrupção para escalar
   ao dono durante a execução é falha de planejamento — quem executa (executor e orquestração)
   não fica com dúvida e não escala direto: para, registra `AE-<n>`, bloqueia `premissa` e
@@ -36,6 +37,11 @@ reescritas nem revogadas.
   `scrum-master` `A3b`, `proximo-passo` e `diario-de-obras` alinhados. `pantonic-planner` ganha
   inventário de corpus (fase 1), teste do parser frio (fase 4) e `idem`/`análogo` no léxico
   proibido. Origem: `P-0739` `AE-1`/`RP-1`.
+- `pantonic-planner` fase 1 ganha a verificação dos **instrumentos do gate de aceite**
+  (2026-09-16): plano que introduz ou usa convenção de identificador, caminho ou nome de artefato
+  confere ainda na fase 1 que `review_evidence.py`, `rdo.py close` e `backlog check` aceitam essa
+  convenção; se não aceitam, corrigir o instrumento é tarefa do plano, nunca achado adiado.
+  Origem: `P-0739` `AE-2`/`RP-2`.
 - `.claude/agents/pantonic-planner.md` reescrito como doutrina operacional do papel de planejamento (2026-09-15): protocolo em cinco fases com duas saídas antes do plano (campanha de investigação delegada ao `pantonic-scout`/tarefa `investigacao`; rodada única de decisões ao dono), anatomia do card autossuficiente para executor frio (camada, domínio, restrições inline, contingências fechadas), auto-auditoria G-PLANREADY + teste do executor frio + léxico proibido, e proibição de publicar plano com questão aberta. Motivo: executores ignorando restrições e decidindo sob plano com dúvida pendurada; sessões de planejamento longas com medição própria. `.claude/README.md` regenerado.
 - `GOVERNANCA.md` §4.3 reconciliada (`DX-10`/`G-SURFACE`): a doutrina deixa inequívoco que a
   janela de orquestração atravessa as tarefas atômicas do mesmo plano e só encerra na troca de
@@ -147,6 +153,8 @@ reescritas nem revogadas.
   materialização (`-Mode check-drift`). Os treze artefatos que só existiam em `~/.claude/` (4 hooks
   registrados, 6 skills, 1 agente, 2 docs de doutrina) mais o `CLAUDE.md` global são promovidos a
   projeção de canônico versionado (`RPC-T1..T7`).
+- `rdo.py`: `extrair_dossie` aceita ID de tarefa prefixado (`(?:[A-Z0-9]+-)?T[0-9]+[a-z]?`, `DB-14`) e bracket com ` + dono` (`DB-20`) — `review_evidence.py` e `rdo.py close` passam a funcionar para `AUT-*`/`CTX-*`/`BKL-*` (`P-0739` `BKL-T2a`, `DB-22`).
+- `review_evidence.py`: campo `Arquivos-alvo` lido por gramática de caminho (`DB-27`) — arquivo de raiz volta a ser alvo, literal de regex deixa de ser; `stdout`/`stderr` forçados a UTF-8 (`P-0739` `BKL-T2b`).
 
 ## 2.0.0 — 2026-08-05
 

```

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
