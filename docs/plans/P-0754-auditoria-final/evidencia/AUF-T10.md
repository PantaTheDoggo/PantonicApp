# Evidência de revisão — P-0754 AUF-T10

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/RUBRICA_DE_REVISAO.md                                |  1 +
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T10-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 20 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T10-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `2f4b87c16e31dddc855cfe57829016389149254c`
- Arquivos-alvo declarados: `docs/RUBRICA_DE_REVISAO.md`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T10-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T10-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/RUBRICA_DE_REVISAO.md`
```
diff --git a/docs/RUBRICA_DE_REVISAO.md b/docs/RUBRICA_DE_REVISAO.md
index 54fe3e3..b6b2d3d 100644
--- a/docs/RUBRICA_DE_REVISAO.md
+++ b/docs/RUBRICA_DE_REVISAO.md
@@ -309,6 +309,7 @@ processo de alvo `modelo`, e o texto fica como está até o modelador agir.
 | (xvi) | **rótulo de campo termina na mesma linha em que começa.** Decoração no rótulo (data, `ESC-n`, `DM-n`, ressalva) é permitida enquanto o `:**` couber na primeira linha; o parser de campos do kit lê **linha a linha**, de modo que rótulo quebrado faz o campo **desaparecer**, não apenas ficar feio | `AE-34` |
 | (xvii) | **o aceite cobre o mundo que o próprio produto cria.** Quando o módulo **emite** uma forma, a `Verificação` exercita **essa** forma, e não só a que ele consome: produto que escreve num formato e é aferido noutro deixa o ramo que ele mesmo produz sem nenhuma linha que o discrimine | `AE-35` |
 | (xviii) | **o valor publicado no literal `Medido antes` é invariante ao que outras entregas movem.** Ele mede o que **este** card possui — exit code do comando, veredito binário, recorte do arquivo-alvo —, nunca um total de corpus que qualquer outra entrega desloca (total de suíte, contagem de módulo compartilhado, contagem de cards ou de insumos do próprio plano); quando a pergunta é sobre corpus, o comando publica o **veredito** (`exit 0`, `iguais`, `1`) e o número absoluto desce para a prosa como referência **datada**, fora do literal | `AE-49` |
+| (xix) | **a contingência é parte ensaiada do card, e não o contradiz.** A ação `seguir com <X>` de cada contingência foi aplicada no ensaio, quando o plano ensaia, e as linhas de `Verificação` re-rodadas depois dela; ela não contraria nenhuma `Restrição` do mesmo card; e todo arquivo que ela escreve está nos `Arquivos-alvo`, seguido de `(condicional: contingência <n>)` | pendência 1 e `AE-24` do `P-0753` |
 
 ### 8.1 A forma normativa do bloco `Verificação`
 

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T10-medida.json; mundo: depois; gerado em: 2026-09-28T14:59:20+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('a contingência é parte ensaiada do card, e não o contradiz'),t.count('\| (xix) \|')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
