# RDO — DIARIO_DE_OBRAS · TK-57a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-57a` — O teste do hook fixa o ambiente e afirma a invariância
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** emendar `test_tf_hook_executavel_*` em `tests/test_backlog.py` para montar `env=` explícito de dicionário mínimo — nunca copiado de `os.environ` — e afirmar que o executável correto devolve a **mesma** saída com e sem `PYTHONUTF8`, enquanto o quebrado devolve saídas diferentes. Referência medida: pré-reparo dá **0** bytes com `env={SYSTEMROOT, PATH}` e **59** com `PYTHONUTF8=1`.

**Arquivos-alvo:** - `tests/test_backlog.py`

**Verificação:** `python -m pytest tests/test_backlog.py` verde, coletando **≥72** testes; `python -m pytest` verde, coletando **≥224**.

**Pronto quando:** os dois `test_tf_hook_executavel_*` montam `env=` explícito de dicionário mínimo (ler `SYSTEMROOT`/`PATH` individualmente é permitido; `dict(os.environ)` ou `os.environ.copy()` é o que fica vedado); existe asserção de **invariância** do executável correto — mesma saída sem e com `PYTHONUTF8=1` —; e existe o **par negativo**, um executável deliberadamente quebrado escrito em `tmp_path` que devolve saídas diferentes nos dois mundos.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-20

## Execução

**Consumo:** 14 tool uses, 62.8 k tokens, 284.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
