# RDO — P-0751 · EBK-T6

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T6` — Nenhuma fixture carrega nome que o harness descobre
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um teste falha, nomeando o arquivo, quando existe sob `tests/fixtures/` um arquivo chamado `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `settings.json` ou `settings.local.json`.

**Arquivos-alvo:** - `tests/test_fixtures_higiene.py` (novo)

**Verificação:** 1. `python -m pytest tests/test_fixtures_higiene.py -q` → verde. 2. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.

**Pronto quando:** o TR acusa fixture com nome de descoberta, provado pelo par.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-55f` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-6` - OP-6: O card que impede fixture de teste com nome que o harness descobre sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Caso medido (2026-09-20):** uma fixture do `TK-60a` continha `SKILL.md`, e o harness passou a listá-la como skill invocável real. Hoje há `0` arquivos com esses nomes sob `tests/fixtures/` (medido em 2026-09-25).
- **Testes:** função pura `nomes_de_descoberta(raiz: Path) -> list[Path]`; TF par — diretório sob `tmp_path` com `a/SKILL.md` → 1 caminho; sem ele → 0; TR — `tests/fixtures/` real → 0.

## Execução

**Consumo:** 6 tool uses, 48.0 k tokens, 68.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
