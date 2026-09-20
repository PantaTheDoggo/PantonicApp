# Evidência de revisão — P-0739 BKL-T9a

## Diff (`git diff --stat`)
```
docs/plans/P-0739-backlog-instrumento.md | 783 ++++++++++++++++++++++++++++++-
 docs/telemetria.tsv                      |   2 +
 2 files changed, 773 insertions(+), 12 deletions(-)
```

## Arquivos tocados
- `docs/plans/P-0739-backlog-instrumento.md` — atribuição: da entrega; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `eb93490`
- Arquivos-alvo declarados: `docs/plans/P-0739-backlog-instrumento.md`
- Arquivos tocados: `docs/plans/P-0739-backlog-instrumento.md`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/plans/P-0739-backlog-instrumento.md`
```
diff --git a/docs/plans/P-0739-backlog-instrumento.md b/docs/plans/P-0739-backlog-instrumento.md
index d033212..267ba55 100644
--- a/docs/plans/P-0739-backlog-instrumento.md
+++ b/docs/plans/P-0739-backlog-instrumento.md
@@ -5,10 +5,11 @@
 com a forma completa de E-2 e a tarefa `BKL-T3b` autorada) ·
 **Prefixo das tarefas no diário:** `BKL-T<n>` · **Prefixo das decisões:**
 `DB-<n>` · **Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`DE-7`), nada a comparar.
-**Ordem de execução:** BKL-T3b → BKL-T4 → BKL-T5 → BKL-T6 → BKL-T7 →
-BKL-T8 → BKL-T9 (`BKL-T2b`, `BKL-T2c` `done` em 2026-09-16; `BKL-T2d`, `BKL-T2e` `done` em
-2026-09-17; `BKL-T3` `done` com ressalva em 2026-09-17; `BKL-T3a` `done` com ressalva em
-2026-09-18) · **Rodadas de replanejamento:** `RP-1`
+**Ordem de execução:** BKL-T9a → BKL-T10 → BKL-T11 → BKL-T12 (`BKL-T2b`, `BKL-T2c` `done` em
+2026-09-16; `BKL-T2d`, `BKL-T2e` `done` em 2026-09-17; `BKL-T3` `done` com ressalva em 2026-09-17;
+`BKL-T3a` `done` com ressalva em 2026-09-18; `BKL-T3b` e `BKL-T4` `done` em 2026-09-18; `BKL-T5`,
+`BKL-T6`, `BKL-T7`, `BKL-T8` e `BKL-T9` `cancelled` em 2026-09-19, absorvidas pelos três módulos)
+· **Rodadas de replanejamento:** `RP-1`
 (2026-09-16, sobre `AE-1`) · `RP-2` (2026-09-16,
 sobre `AE-2` — fechada) · `RP-3` (2026-09-16, sobre `AE-3` — fechada) · `RP-4` (2026-09-16, sobre
 `AE-4` — fechada) · `RP-5` (2026-09-17, sobre `AE-6`, com a emenda do `AE-5` — fechada) · `RP-6`
@@ -107,6 +108,7 @@ não A nem B — registrado como apenso em `P-0737` `## 9` no ato do registro).
 | **`DB-40`** | **E-2** vale para o pai tanto quanto para o item, e a mensagem lista ID distinto uma vez, em ordem alfabética (`RP-7`) | `next` aplica **E-2** sobre a união de dois conjuntos — o item de cada candidato **e** o pai de cada candidato —, e o ID sem a linha `- **Status:**` produz uma ocorrência de `linha de status ausente para <ID>`. **Três cláusulas fechadas:** (i) **ID distinto uma vez** — pai com dois filhos candidatos aparece uma única vez na mensagem; (ii) **ordem alfabética crescente do `<ID>`**, ocorrências separadas por `, ` (a mesma ordenação que a `DB-37` já fixou para **E-1**); (iii) **E-2 é avaliada antes de E-1 e de E-3**, ordem que a `BKL-T3` entregou e esta decisão preserva. Residência da regra: §2.5 item 6 (`DB-37`), emendada no mesmo ato — esta célula remete a ela e não a reenuncia. Fronteira contra o instrumento vizinho: a ausência da linha é violação `C-2` (tarefa, tíquete, subtarefa) ou `C-8` (plano vivo) do verbo `check`; `next` recusa a seleção e não classifica a violação. Mede o desvio do achado 1 do `AE-8`: com `sem_status` filtrando só `c.item.status is None`, o pai sem `Status` cai no filtro de elegibilidade (`c.pai.status in ("ready", "in-progress")`) e os candidatos dele somem **em silêncio**. Rotas descartadas: (a) manter E-2 só sobre o item — é o desvio medido, e desempatar por heurística é o que `DB-6` proíbe; (b) tratar pai sem `Status` como pai `ready` — inventa estado que o dado não tem, contra `DB-2` (fonte única) e `DB-3` (vocabulário fechado); (c) repetir o ID do pai uma vez por filho candidato — a mesma mensagem n vezes num verbo com teto de dossiê (`DB-7`), sem informação nova; (d) registrar e não agir — `next` sai no hook a cada prompt (`DB-8`) e a seleção silenciosa é exatamente o que este plano existe para eliminar |
 | **`DB-41`** | O prefixo de candidato do contador de fila de memória inclui o espaço; régua `---` não é candidato (`RP-7`) | `_contar_inbox_memoria` conta a linha cujo texto, depois de `strip()`, **começa com `- `** (hífen **e** espaço) e não traz `[promovido]` nem `[descartado`. A norma **não muda**: §2.6 e a residência dela (`~/.claude/docs/GOVERNANCA_MEMORIAS.md` §8) já escrevem `- `; o que desviou foi o código (`s.startswith("-")`, sem o espaço), que faz a régua markdown `---` contar como candidato por prefixo. O contador **não ganha nenhum outro filtro** — nem indentação, nem data, nem campo `**origem:**`: o que exclui linh
```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
