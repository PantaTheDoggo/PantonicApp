# RDO — DIARIO_DE_OBRAS · TK-62a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-62a` — `rdo.py` reconhece `TK-<n><letra>` como ID de tarefa
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** alargar `_ID_HEADER_RE` e `_HEADER_BRACKET_RE` em `.claude/tools/rdo.py` para reconhecer, além do `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` atual, a forma `TK-[0-9]+[a-z]?` da `DB-17`, sem alargar para nada além dessas duas. Regressão em `tests/test_rdo.py` e `tests/test_review_evidence.py` que discrimine ID de tíquete aceito de ID fora da gramática recusado. Caso medido que motivou: `TK-57a` em `docs/DIARIO_DE_OBRAS.md:1819`.

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `tests/test_rdo.py` - `tests/test_review_evidence.py`

**Verificação:** `python .claude/tools/review_evidence.py --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-57a --desde <ref> --out docs/RDO/evidencia/TK-57-TK-57a.md` sai **exit 0** e grava o arquivo — hoje sai exit 1 com `tarefa: 'TK-57a' não encontrada`. `python -m pytest` verde, sem queda do piso de **224**.

**Pronto quando:** `_ID_HEADER_RE` e `_HEADER_BRACKET_RE` aceitam `TK-<n>` e `TK-<n><letra>` além do `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` atual, e **nada além dessas duas** — `## TK-62 — …` (nível 2, tíquete-pai) continua não sendo reconhecido como tarefa, e `### 2.5 — …` continua fora. Regressão **par presença-ausência** nos dois arquivos de teste.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20

## Execução

**Consumo:** 21 tool uses, 91.0 k tokens, 369.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: kit_check_check_drift vermelho em README.md, atribuído por medida a TK-51a, fora dos alvos

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
