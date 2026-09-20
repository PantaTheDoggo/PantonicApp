# RDO — DIARIO_DE_OBRAS · TK-58c

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-58c` — O título e o lead da `## 15` dizem o que a seção mede
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** alinhar o **cabeçalho** da `## 15` de `docs/CUSTO_DO_PICKUP.md` ao **corpo** dela. O título diz *"Par completo do método `DC-4`"* e o lead diz *"Fecha a aferição da `## 14`"* e *"as duas estão medidas"* — mas o próprio corpo, três parágrafos abaixo, declara que a metade `usage_1` **não isola o pickup** e que o par fica **aberto por declaração**. O cabeçalho promete o que o texto desmente, e é o cabeçalho que se lê primeiro.

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md`

**Verificação:** - A `## 15` **não** contém mais os literais `Par completo`, `Fecha a aferição` nem `as duas estão medidas`. - O título da `## 15` nomeia **abertura de janela com pickup**, não *par completo*. - O lead declara, em uma frase, que a metade em chars está medida e que a metade `usage_1` **fica aberta** à espera de controle pareado. - O **corpo** da seção não muda: os parágrafos de proveniência, correção de rótulo, fronteira, pickups distintos e emenda ao `DC-4` ficam **byte a byte** como estão. - `python -m pytest` verde, coletando **238**.

**Pronto quando:** quem lê só o título e o lead da `## 15` chega à mesma conclusão de quem lê a seção inteira — que a redução de **−65,5%** em chars está medida e de pé, e que o custo do pickup **não** foi isolado. É o critério inteiro desta tarefa.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-58b` (ressalva 88%), roteada pelo `A8a`. Sem decisão de rota: o corpo da seção já está aprovado e dita o conteúdo.
- **Não fazer:** não alterar nenhum número; não tocar a `## 14`; não abrir `docs/plans/P-0741-modelo-conceitual.md`; não tocar `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md` nem `.claude/skills/diario-de-obras/SKILL.md` — a outra janela de orquestração está editando os três agora.

## Execução

**Consumo:** 5 tool uses, 45.2 k tokens, 35.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
