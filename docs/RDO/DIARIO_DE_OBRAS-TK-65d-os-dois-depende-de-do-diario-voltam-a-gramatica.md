# RDO — DIARIO_DE_OBRAS · TK-65d

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-65d` — Os dois `Depende de` do diário voltam à gramática
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** devolver `python .claude/tools/backlog.py check` a exit 0 saneando os dois campos `- **Depende de:**` do diário que a violação `C-12` do `TK-65a` acusa, sem perder texto.

**Arquivos-alvo:** - `docs/DIARIO_DE_OBRAS.md` (só as duas linhas abaixo, localizadas por conteúdo)

**Verificação:** antes, `python .claude/tools/backlog.py check` sai exit 1 com exatamente as três `C-12` (`TK-54a` ×2, `TK-78c` ×1); depois, exit 0 com `check: OK — nenhuma violação.`

**Pronto quando:** os dois bullets estão na forma do Reparo, sem palavra perdida (a proveniência mora em `Fundamento`, e o `Depende de` do `TK-78c` lista só `` `TK-78a` ``); `backlog.py check` sai exit 0 com `check: OK — nenhuma violação.`

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24 — aberto pelo loop no fechamento do `TK-65a` (laudo ressalva 94%, achado de processo roteado a subitem do `TK-65`).
- **Reparo, por linha:** 1. No `### TK-54a`, o bullet `- **Depende de:** decisões 1..7 de `` `## TK-54` `` (copiadas inline no que vinculam), a` e a continuação recuada logo abaixo: trocar só o rótulo `**Depende de:**` por `**Fundamento:**`, texto e continuação verbatim — é proveniência, não dependência de item (mesma convenção do `DMC-19` do `P-0741`). 2. No `### TK-78c`, o bullet `` - **Depende de:** `TK-78a` (as duas editam a skill scrum-master, em trechos distintos) ``: reduzir a `` - **Depende de:** `TK-78a` `` e apensar ao fim do bullet `- **Fundamento:**` do mesmo card a frase `` Depende do `TK-78a` porque as duas editam a skill scrum-master, em trechos distintos. ``
- **Não fazer:** não tocar `.claude/tools/backlog.py` — piso de dívida ou isenção de item terminal para `C-12` não foram adotados; o reparo é do corpus, não do lint.

## Execução

**Consumo:** 6 tool uses, 47.3 k tokens, 28.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Achado de processo roteado: nao rastreados pre-despacho no dossie -> TK-55 (ja indexado).

## Fechamento

**Desdobramento:** aprovado
