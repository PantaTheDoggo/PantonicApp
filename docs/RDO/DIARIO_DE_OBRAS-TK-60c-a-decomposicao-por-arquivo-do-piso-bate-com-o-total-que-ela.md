# RDO — DIARIO_DE_OBRAS · TK-60c

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-60c` — A decomposição por arquivo do piso bate com o total que ela declara
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** corrigir o comentário de origem de `_PISO_C11` em `.claude/tools/backlog.py`, cuja decomposição por arquivo soma **13** sob um cabeçalho que declara **15** — o comentário contradiz a si mesmo dentro do próprio guarda que existe para pegar derivado que erra sem sinal.

**Arquivos-alvo:** - `.claude/tools/backlog.py`

**Verificação:** a soma das parcelas da decomposição é **15**, igual ao total do cabeçalho da mesma frase. `python .claude/tools/backlog.py check` sai **exit 0**; `python -m pytest` verde, sem queda do piso de **236**.

**Pronto quando:** a decomposição lista os cinco arquivos com as contagens **medidas pelo próprio instrumento** em 2026-09-20 (`check` com `_PISO_C11` vazio, em processo, sem tocar a árvore): `docs/plans/P-0741-modelo-conceitual.md` **6**, `docs/DIARIO_HISTORICO.md` **6**, `docs/DIARIO_DE_OBRAS.md` **1**, `docs/plans/P-0730-v2-identidade.md` **1**, `docs/plans/P-0731-v2-extracao-modalidade.md` **1**. A redação anterior omitia `docs/DIARIO_DE_OBRAS.md` e contava 5 em vez de 6 no histórico. **Só o comentário muda** — nenhuma linha de código, nenhuma entrada do piso, nenhum teste.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-60b` (ressalva 91%), roteada pelo `A8a`.
- **Não fazer:** não corrigir nenhuma das 15 ocorrências de dívida; não alterar as duas entradas de `_PISO_C11`; não editar `docs/plans/P-0741-modelo-conceitual.md`, plano vivo de outra janela de orquestração ativa neste repositório.

## Execução

**Consumo:** 7 tool uses, 44.5 k tokens, 39.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
