# RDO — DIARIO_DE_OBRAS · TK-59a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-59a` — Verificador do contador de id do inbox contra `docs/plans/`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** acrescentar ao `check` uma violação que confronte `**Próximo id de plano: P-NNNN.**` de `docs/plans/_INBOX.md` com o maior id presente em `docs/plans/P-*.md`, acusando quando o contador aponta para id **já usado**. Caso medido que a motivou: contador em `P-0742` com `P-0742-loop-fora-do-llm.md` já na árvore.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** `python .claude/tools/backlog.py check` acusa a divergência sobre fixture em que o contador de `docs/plans/_INBOX.md` aponta para id já presente em `docs/plans/P-*.md`, e **não** acusa sobre fixture em que o contador aponta para id livre. `python -m pytest tests/test_backlog.py` verde.

**Pronto quando:** `check` tem uma violação nova, de vocabulário fechado como as demais (`C-*`), que confronta `**Próximo id de plano: P-NNNN.**` com o maior id presente em `docs/plans/P-*.md`; e o teste é **par presença-ausência**, sobre corpus em que as duas leituras dariam resultados diferentes. Caso medido que motivou: contador em `P-0742` com `docs/plans/P-0742-loop-fora-do-llm.md` já na árvore.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20

## Execução

**Consumo:** 62 tool uses, 110.6 k tokens, 394.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
