# RDO — DIARIO_DE_OBRAS · TK-58d

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-58d` — Nenhum lugar do corpus afirma que o par do `DC-4` está fechado
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a afirmação aposentada — *o par do `DC-4` está fechado / as duas metades estão medidas* — deixa de existir em **todo** o corpus vivo. Ela sobrevive em dois lugares medidos, e os dois são lidos **antes** da `## 15`.

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md` - `docs/DOC_MAP.md`

**Verificação:** - `grep -rn "par completo\|Par completo\|as duas metades do" docs/CUSTO_DO_PICKUP.md docs/DOC_MAP.md` → **nenhuma** ocorrência. - `docs/CUSTO_DO_PICKUP.md` não contém mais o literal `fecha o par`. - A entrada da `## 15` no `DOC_MAP` traz o **título atual** da seção, que começa com `Abertura de janela com pickup`. - `python -m pytest` verde, coletando **238**.

**Pronto quando:** as duas ocorrências medidas em 2026-09-20 estão corrigidas, e cada uma passa a dizer o que a `## 15` de fato sustenta — metade em chars medida e de pé (**−65,5%**), metade `usage_1` medindo **abertura de janela com pickup**, sem isolar o pickup, **aberta** à espera de controle pareado: 1. **Fecho da `## 14`** (parágrafo `**Metade em \`usage_1\`: medida.**`): hoje afirma que a `## 15` *"fecha o par do `DC-4`"*. Passa a remeter à `## 15` dizendo que a metade foi **medida** e que o **par segue aberto**, pelo motivo que a `## 15` declara. 2. **Entradas do `DOC_MAP`** (linhas 131-135): a da `## 14` diz `a metade usage_1 declarada não medida` — defasada, o número existe desde 2026-09-20. A da `## 15` repete o **título antigo** (`Par completo do método DC-4…`) e afirma `as duas metades do DC-4 medidas`. As duas passam a descrever o estado atual, e a da `## 15` cita o título vigente.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-58c` (aprovado 100%, recomendação `escalar`), roteada pelo `A8a`. **Escopo por afirmação, não por local** — é a correção do defeito que produziu três rodadas seguidas de rastro: `TK-58b` e `TK-58c` foram escopados por arquivo e por seção, então cada um corrigiu uma instância e deixou as outras vivas.
- **Não fazer:** não alterar nenhum número; não editar o **corpo** da `## 15`, aprovado em `TK-58b`/`TK-58c`; não editar o texto histórico dos cards `TK-58`/`TK-58a` no diário — card fechado não retroage (`DB-23`); não abrir `docs/plans/P-0741-modelo-conceitual.md`; não tocar `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md` nem `.claude/skills/diario-de-obras/SKILL.md` — a outra janela de orquestração está editando os três agora.

## Execução

**Consumo:** 10 tool uses, 53.9 k tokens, 96.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
