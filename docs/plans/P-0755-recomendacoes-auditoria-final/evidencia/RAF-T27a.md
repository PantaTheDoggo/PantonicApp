# Evidência de revisão — P-0755 RAF-T27a

## Diff (`git diff --stat`)
```
.claude/tools/prevoo.py                                   | 11 ++++++++---
 docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T27a-medida-depois.json          | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 28 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `.claude/tools/prevoo.py` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T27a-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `9ef5bdcdc0965788be340348662d7c8d5d971a4a`
- Arquivos-alvo declarados: `.claude/tools/prevoo.py`
- Arquivos tocados: `.claude/tools/prevoo.py`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T27a-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T27a-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/prevoo.py`
```
diff --git a/.claude/tools/prevoo.py b/.claude/tools/prevoo.py
index 02ebdce..1faf989 100644
--- a/.claude/tools/prevoo.py
+++ b/.claude/tools/prevoo.py
@@ -10,9 +10,14 @@ pontuação de frase (`,` `.` `;` `:` `!` `?`) e fecha-parêntese/colchete/chave
 Assim `` `ler_texto_utf8` ``, `` `.claude/tools/caminhos.py`, ``, `--plano;` e `nome()` citam o mesmo
 que `ler_texto_utf8`, `.claude/tools/caminhos.py`, `--plano` e `nome(`.
 
-- **caminhos** — token terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml`
-  ou `.toml`, ou terminado em `/`; existe quando `(<root> / <token>)` existe; `onde` é o próprio
-  caminho.
+- **caminhos** — token terminado em `/`; ou com `/` e o último segmento terminado numa extensão
+  de 1 a 5 letras ou dígitos; ou, sem `/`, terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`,
+  `.txt`, `.yml`, `.yaml` ou `.toml` e não começado por `.` (`R-17` e `DRF-19` do `P-0755`);
+  existe (`sim`) quando `(<root> / <token>)` existe, e `onde` é o próprio caminho; o que não
+  existe sai `criar` quando a mesma frase (texto entre `. ` ou quebra de linha) o traz depois de
+  um verbo de criação (`crie`, `criar`, `grave`, `gravar`, `escreva`, `escrever`, `gere`, `gerar`,
+  sem distinção de caixa), e `criar` não derruba o exit 0; o que não existe e o pedido não manda
+  criar sai `não` e, como o símbolo e a flag ausentes, faz o exit ser 1.
 - **símbolos** — nome seguido de `(` (com ou sem argumentos até o `)`), ou identificador com `_` que não é caminho nem flag; existe
   quando algum `.py` sob `<root>` (fora de `.git` e `__pycache__`) tem a linha `def <nome>(` ou
   `class <nome>`; `onde` é `<arquivo>:<linha>` da primeira ocorrência, com `/`.

```

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T27a-medida-depois.json; mundo: depois; gerado em: 2026-09-29T23:49:30+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/tools/prevoo.py').read_text(encoding='utf-8');print('docstring=%d-%d-%d linhas=%d'%(t.count('ou terminado em'),t.count('de 1 a 5 letras ou dígitos'),t.count('não derruba o exit 0'),len(t.splitlines())))"` | 0 | true |

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
