# Evidência de revisão — P-0739 BKL-T2d

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-planner.md       |    6 +
 .claude/tools/rdo.py                     |   55 +-
 .claude/tools/review_evidence.py         |  206 ++++-
 CHANGELOG.md                             |   11 +
 docs/DIARIO_DE_OBRAS.md                  |    8 +-
 docs/plans/P-0739-backlog-instrumento.md | 1315 +++++++++++++++++++++++++++++-
 docs/telemetria.tsv                      |   12 +
 tests/test_rdo.py                        |  147 ++++
 tests/test_review_evidence.py            |  166 +++-
 9 files changed, 1871 insertions(+), 55 deletions(-)
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
- `docs/RDO/evidencia/P-0739-BKL-T2c.md`
- `docs/RDO/laudos/P-0739-BKL-T2.md`
- `docs/RDO/laudos/P-0739-BKL-T2a.md`
- `docs/RDO/laudos/P-0739-BKL-T2b.md`
- `docs/RDO/laudos/P-0739-BKL-T2c.md`
- `docs/plans/P-0739-backlog-instrumento.md`
- `docs/telemetria.tsv`
- `tests/test_rdo.py`
- `tests/test_review_evidence.py`

## Escopo
- Recorte: desde `6d7433c`
- Arquivos-alvo declarados: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `CHANGELOG.md`
- Literais não reconhecidos como caminho (7): `laudo`, `cmd_laudo`, `)`, `conteudo_final`, `laudo_parser.add_argument("--escalar", …)`, `## [Não lançado]`, `DB-13`
- Arquivos tocados: `.claude/agents/pantonic-planner.md`, `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py`, `CHANGELOG.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/evidencia/P-0739-BKL-T2.md`, `docs/RDO/evidencia/P-0739-BKL-T2a.md`, `docs/RDO/evidencia/P-0739-BKL-T2b.md`, `docs/RDO/evidencia/P-0739-BKL-T2c.md`, `docs/RDO/laudos/P-0739-BKL-T2.md`, `docs/RDO/laudos/P-0739-BKL-T2a.md`, `docs/RDO/laudos/P-0739-BKL-T2b.md`, `docs/RDO/laudos/P-0739-BKL-T2c.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`, `tests/test_rdo.py`, `tests/test_review_evidence.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/tools/review_evidence.py` → `BKL-T2b`, `docs/DIARIO_DE_OBRAS.md` → `BKL-T6`, `tests/test_review_evidence.py` → `BKL-T2b`
- Registro da orquestração (não atribuível a tarefa): `docs/RDO/evidencia/P-0739-BKL-T2.md`, `docs/RDO/evidencia/P-0739-BKL-T2a.md`, `docs/RDO/evidencia/P-0739-BKL-T2b.md`, `docs/RDO/evidencia/P-0739-BKL-T2c.md`, `docs/RDO/laudos/P-0739-BKL-T2.md`, `docs/RDO/laudos/P-0739-BKL-T2a.md`, `docs/RDO/laudos/P-0739-BKL-T2b.md`, `docs/RDO/laudos/P-0739-BKL-T2c.md`, `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`
- Fato: 1 arquivo(s) fora dos alvos e sem atribuição: `.claude/agents/pantonic-planner.md`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/rdo.py`
```
diff --git a/.claude/tools/rdo.py b/.claude/tools/rdo.py
index 62c64fe..5ade3e8 100644
--- a/.claude/tools/rdo.py
+++ b/.claude/tools/rdo.py
@@ -21,7 +21,7 @@ Plano legado (cabeçalho sem colchete algum — a gramática fixa da `DX-15` é
 flag nenhuma): `--esquema-legado` com `--modelo`/`--classe` explícitos é o único caminho para
 prosseguir (política de plano legado da `DP-C`, item 3) — o RDO registra `esquema=legado`.
 
-`laudo` (EXA-T8b/T18) não é tocado por esta rodada: `python .claude/tools/rdo.py laudo --plano
+`laudo` (EXA-T8b/T18, estendido pela `BKL-T2d` do `P-0739`): `python .claude/tools/rdo.py laudo --plano
 <id> --tarefa <id> [--laudos-dir <dir>] --<dimensao> <nivel> ...` (as sete dimensões de
 `docs/RUBRICA_DE_REVISAO.md` §4, na ordem canônica de §5) **calcula** percentual, veredito,
 dimensão bloqueante e recomendação de domínio fechado (`seguir` | `seguir com ressalva` | `refazer`
@@ -30,7 +30,11 @@ argumento (`DA-6`) — e grava documento próprio em `docs/RDO/laudos/<plano>-<t
 diretório se preciso. `--vermelho-mecanico <dimensao>` (repetível) declara o que a camada mecânica
 já reportou vermelho; marcar `conforme` contra uma dimensão declarada vermelha é recusado (`DA-7`).
 `--escalar "<uma linha>"` força `recomendacao=escalar` independentemente da tabela, e a linha
-gravada é a pendência que a regra `B1` consome.
+gravada é a pendência que a regra `B1` consome. `--achado-processo <alvo> "<uma linha>"`
+(repetível; alvo em `dossie`, `doutrina` ou `rubrica`) grava a seção `## Achado de processo` e
+**não** altera percentual, veredito, bloqueante nem recomendação — invariante 1 de
+`docs/RUBRICA_DE_REVISAO.md` §6; `--escalar` fica reservado ao achado que invalida a rota (decisão
+de arquitetura ou de requisito).
 
 Escrita atômica (arquivo temporário no mesmo diretório de destino + `os.replace`) e falha ruidosa
 (exit != 0, mensagem em stderr, nada escrito) no mesmo padrão de `.claude/tools/telemetria.py`."""
@@ -76,11 +80,11 @@ _CLASSE_ALIASES: dict[str, str] = {
     "redacao/planejamento": "redacao",
 }
 
-_ID_HEADER_RE = re.compile(r"^### (T[0-9]+[a-z]?)(?=[\s—])")
+_ID_HEADER_RE = re.compile(r"^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?)(?=[\s—])")
 _ID_LAUDO_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")  # identificador, nunca caminho
 _HEADER_BRACKET_RE = re.compile(
-    r"^### (?P<id>T[0-9]+[a-z]?) — (?P<titulo>.+?) "
-    r"\[(?P<modelo>Opus|Sonnet|Haiku) · classe (?P<classe>.+?)"
+    r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) "
+    r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)? · classe (?P<classe>.+?)"
     r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$"
 )
 _HEADER_LEGADO_TITULO_FMT = r"^### {id} — (?P<titulo>.+)$"
@@ -447,6 +451,21 @@ def calcular_laudo(
     )
 
 
+_ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica"}
+
+
+def _formatar_achados_processo(pares: list[list[str]] | None) -> str:
+    """`docs/RUBRICA_DE_REVISAO.md` §6: campo próprio, três alvos. Invariante 1 — o achado não
+    rebaixa dimensão de entrega e não muda recomendação; por isso nada disto passa por
+    `calcular_laudo`. Sem achado, o corpo é `nenhum` (a seção existe sempre)."""
+    if not pares:
+        return "nenhum"
+    linhas = ["| alvo | achado |", "|---|---|"]
+    for alvo, texto in pares:
+        linhas.append(f"| {_ALVOS_ACHADO[alvo]} | {texto.strip()} |")
+    return "\n".join(linhas)
+
+
 def cmd_laudo(args: argparse.Namespace) -> Path:
     """EXA-T18: laudo grava documento próprio em `docs/RDO/laudos/<plano>-<tarefa>.md` — não
     depende de RDO nenhum aberto, e o `close` (EXA-T19) não o lê: o `pacote` chega a `close` por
@@ -457,6 +476,18 @@ def cmd_laudo(args: argparse.Namespace) -> Path:
                 f"{flag} é identificador (ex.: P-0734, T18), não caminho: {valor!r}. "
                 "Laudo de sonda vai para --laudos-dir <scratchpad>."
             )
+    for alvo, texto in (args.achado_processo or []):
+        if alvo not in _ALVOS_ACHADO:
+       
```
[truncado em 4000 caracteres]

### `tests/test_rdo.py`
```
diff --git a/tests/test_rdo.py b/tests/test_rdo.py
index 7f2d51c..55d4d4e 100644
--- a/tests/test_rdo.py
+++ b/tests/test_rdo.py
@@ -560,3 +560,150 @@ def test_tr_laudo_recusa_plano_e_tarefa_em_forma_de_caminho(tmp_path, capsys):
     assert exit_code != 0
     assert "--plano" in capsys.readouterr().err
     assert not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []
+
+
+def test_tf_extrair_dossie_id_prefixado(tmp_path):
+    """TF da BKL-T2a (`DB-22`): ID de tarefa com prefixo de plano (`BKL-T2`) é localizado pelo
+    cabeçalho e casado por igualdade exata, prefixo incluído."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### BKL-T2 — Tarefa sintética [Sonnet · classe implementacao]")
+
+    dossie = rdo.extrair_dossie(
+        plano, "BKL-T2", esquema_legado=False, modelo_legado=None, classe_legado=None,
+    )
+
+    assert dossie.tarefa_id == "BKL-T2"
+    assert dossie.modelo == "Sonnet"
+    assert dossie.classe == "implementacao"
+    assert dossie.esquema == "padrao"
+
+
+def test_tf_extrair_dossie_id_prefixado_com_letra_e_teto_legado(tmp_path):
+    """TF da BKL-T2a (`DB-22`): ID prefixado com letra de subtarefa (`CTX-T1d`) e segmento de
+    teto histórico (`· teto 30`), aceito e descartado."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### CTX-T1d — Tarefa sintética [Opus · classe redacao · teto 30]")
+
+    dossie = rdo.extrair_dossie(
+        plano, "CTX-T1d", esquema_legado=False, modelo_legado=None, classe_legado=None,
+    )
+
+    assert dossie.tarefa_id == "CTX-T1d"
+    assert dossie.classe == "redacao"
+    assert dossie.esquema == "padrao"
+
+
+def test_tf_extrair_dossie_bracket_com_aceite_do_dono(tmp_path):
+    """TF da BKL-T2a (`DB-20`): segmento ` + dono` no bracket é aceito e descartado."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### BKL-T9 — Tarefa sintética [Opus + dono · classe redacao]")
+
+    dossie = rdo.extrair_dossie(
+        plano, "BKL-T9", esquema_legado=False, modelo_legado=None, classe_legado=None,
+    )
+
+    assert dossie.modelo == "Opus"
+    assert dossie.classe == "redacao"
+    assert dossie.esquema == "padrao"
+
+
+def test_tr_extrair_dossie_id_casa_por_igualdade_exata(tmp_path):
+    """TR da BKL-T2a: prefixo nunca casa por sufixo nem por ID parcial — `T1` não encontra
+    `BKL-T1`, e `BKL-T2` não encontra `BKL-T1`."""
+    rdo = _load_rdo()
+    plano = tmp_path / "plano.md"
+    _escrever_plano_sintetico(plano, "### BKL-T1 — Tarefa sintética [Sonnet · classe redacao]")
+
+    with pytest.raises(rdo.RdoValidationError):
+        rdo.extrair_dossie(
+            plano, "T1", esquema_legado=False, modelo_legado=None, classe_legado=None,
+        )
+
+    with pytest.raises(rdo.RdoValidationError):
+        rdo.extrair_dossie(
+            plano, "BKL-T2", esquema_legado=False, modelo_legado=None, classe_legado=None,
+        )
+
+
+# --- laudo · achado de processo (BKL-T2d, RUBRICA_DE_REVISAO.md §6) ------------------------------
+
+
+def test_tf_laudo_achado_de_processo_grava_secao_com_os_tres_alvos(tmp_path):
+    """TF da BKL-T2d: `--achado-processo` repetível grava a seção `## Achado de processo` com uma
+    linha de tabela por alvo."""
+    rdo = _load_rdo()
+    laudos_dir = tmp_path / "laudos"
+
+    exit_code = rdo.main(
+        _argv_laudo(laudos_dir)
+        + [
+            "--achado-processo", "dossie", "criterio de pronto exige registro fora dos alvos",
+            "--achado-processo", "doutrina", "sem guardrail de atribuicao por tarefa",
+        ]
+    )
+
+    assert exit_code == 0
+    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
+    assert "## Achado de processo" in conteudo
+    assert "| dossiê | criterio de pronto exige registro fora dos alvos |" in conteudo
+    assert "| doutrina | sem guardrail de atribuicao por tarefa |" in conteudo
+
+
+def test_t
```
[truncado em 4000 caracteres]

### `CHANGELOG.md`
```
diff --git a/CHANGELOG.md b/CHANGELOG.md
index d06abb5..3f1acde 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -16,6 +16,7 @@ reescritas nem revogadas.
 
 ## [Não lançado]
 
+- `review_evidence.py`: confronto de escopo atribui arquivo tocado a outra tarefa do plano e separa o registro da orquestração, em vez de reportar tudo como fora-de-alvo (`P-0739` `BKL-T2c`, `DB-25`).
 - `G-NOASK` (`GOVERNANCA.md` §7 item 18, 2026-09-16, decisão do dono): interrupção para escalar
   ao dono durante a execução é falha de planejamento — quem executa (executor e orquestração)
   não fica com dúvida e não escala direto: para, registra `AE-<n>`, bloqueia `premissa` e
@@ -36,6 +37,14 @@ reescritas nem revogadas.
   `scrum-master` `A3b`, `proximo-passo` e `diario-de-obras` alinhados. `pantonic-planner` ganha
   inventário de corpus (fase 1), teste do parser frio (fase 4) e `idem`/`análogo` no léxico
   proibido. Origem: `P-0739` `AE-1`/`RP-1`.
+- `pantonic-planner` fase 1 ganha a verificação dos **instrumentos do gate de aceite**
+  (2026-09-16): plano que introduz ou usa convenção de identificador, caminho ou nome de artefato
+  confere ainda na fase 1 que `review_evidence.py`, `rdo.py close` e `backlog check` aceitam essa
+  convenção; se não aceitam, corrigir o instrumento é tarefa do plano, nunca achado adiado.
+  Origem: `P-0739` `AE-2`/`RP-2`.
+- `rdo.py laudo`: campo `--achado-processo <alvo> "<linha>"` com os três alvos da
+  `RUBRICA_DE_REVISAO.md` §6, sem mexer em percentual, veredito nem recomendação — `--escalar`
+  volta a ser só pendência de arquitetura ou de requisito (`P-0739` `BKL-T2d`, `DB-28`).
 - `.claude/agents/pantonic-planner.md` reescrito como doutrina operacional do papel de planejamento (2026-09-15): protocolo em cinco fases com duas saídas antes do plano (campanha de investigação delegada ao `pantonic-scout`/tarefa `investigacao`; rodada única de decisões ao dono), anatomia do card autossuficiente para executor frio (camada, domínio, restrições inline, contingências fechadas), auto-auditoria G-PLANREADY + teste do executor frio + léxico proibido, e proibição de publicar plano com questão aberta. Motivo: executores ignorando restrições e decidindo sob plano com dúvida pendurada; sessões de planejamento longas com medição própria. `.claude/README.md` regenerado.
 - `GOVERNANCA.md` §4.3 reconciliada (`DX-10`/`G-SURFACE`): a doutrina deixa inequívoco que a
   janela de orquestração atravessa as tarefas atômicas do mesmo plano e só encerra na troca de
@@ -147,6 +156,8 @@ reescritas nem revogadas.
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
