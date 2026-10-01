# Evidência de revisão — P-0755 RAF-T4a

## Diff (`git diff --stat`)
```
.claude/skills/passagem-de-bastao/SKILL.md         |  8 +++---
 .claude/skills/scrum-master/SKILL.md               |  2 +-
 docs/DIARIO_DE_OBRAS.md                            |  6 ++---
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T4a-medida.json           | 29 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 6 files changed, 39 insertions(+), 9 deletions(-)
```

## Arquivos tocados
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T4a-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `f57eb5d471a116cdcc576672acf0c22b6bde4f4c`
- Arquivos-alvo declarados: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T4a-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T4a-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/passagem-de-bastao/SKILL.md`
```
diff --git a/.claude/skills/passagem-de-bastao/SKILL.md b/.claude/skills/passagem-de-bastao/SKILL.md
index 4d8770a..cc7b2db 100644
--- a/.claude/skills/passagem-de-bastao/SKILL.md
+++ b/.claude/skills/passagem-de-bastao/SKILL.md
@@ -113,10 +113,10 @@ decisão para o executor, no modelo mais barato e sem o contexto de quem decidiu
 3. Números de aceite (piso, contagem de suíte, call sites) re-derivados por 1 comando barato agora —
    nunca copiados do plano (contagens envelhecem com a própria sprint). String destinada a assert é
    citação colada do output de verificação, nunca paráfrase — token negativo errado passa em
-   silêncio. Junto dos números vão as **âncoras** (arquivo, linha e texto do ponto a editar)
-   re-derivadas no ato e, quando a tarefa fecha em plano em andamento, o **range de linhas do bullet
-   de fechamento anterior**: sem isso o dossiê não é autossuficiente e quem executa precisa
-   redescobrir a localização — trabalho que a tarefa não pediu.
+   silêncio. As **âncoras** (arquivo, linha e texto do ponto a editar) da tarefa de plano chegam
+   conferidas no pacote do `despachar` (`scrum-master`, passo 3) e não se re-derivam à mão; só o
+   card de tíquete, despachado à mão, as leva re-derivadas no ato. Tarefa que fecha em plano em
+   andamento leva ainda o **range de linhas do bullet de fechamento anterior** (`scrum-master`, passo 4).
 4. Afirmação negativa de escopo ("não toca contracts/services") com campo novo persistido exige 1
    grep pelo gate de ESCRITA (`extra.*forbid`, validador) antes de ser afirmada. Rename/move de
    símbolo público: grep também em docs vivos (`docs/*.md`, excluindo históricos).

```

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 7a59b06..e4ad929 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -96,7 +96,7 @@ Dez passos, nesta ordem.
 ### Passo 4 — Despacho do executor
 
 - **Gatilho:** gates do passo 3 aprovados e tarefa materializada em `in-progress`.
-- **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho.
+- **Entrada:** texto pronto impresso pelo `despachar` (tíquete: dossiê à mão); modelo do cabeçalho.
 - **Ação:** garantir o diretório `.claude/estado/` (ele viaja versionado com `.gitkeep`, `DM-10`
   do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar
   `.claude/estado/tarefa-corrente.json` (objeto único: `tarefa`, `projeto`,

```

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T4a-medida.json; mundo: depois; gerado em: 2026-09-29T02:36:46+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8');print('gate=%d-%d'%(t.count('Junto dos números vão as'),t.count('e não se re-derivam à mão; só o')))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('entrada=%d-%d'%(t.count('dossiê da tarefa copiado do plano'),t.count('(tíquete: dossiê à mão); modelo do cabeçalho')))"` | 0 | true |
| 3 | `python -c "from pathlib import Path;a=Path('.claude/skills/passagem-de-bastao/SKILL.md');b=Path('.claude/skills/scrum-master/SKILL.md');print('linhas=%d-%d cr=%d-%d'%(len(a.read_text(encoding='utf-8').splitlines()),len(b.read_text(encoding='utf-8').splitlines()),a.read_bytes().count(bytes([13])),b.read_bytes().count(bytes([13]))))"` | 0 | true |

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
