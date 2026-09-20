# RDO — DIARIO_DE_OBRAS · TK-58a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-58a` — Medir o `usage_1` em janela nova e fechar o método `DC-4`
**Modelo:** Opus · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** abrir uma janela principal nova, ler o **primeiro `usage`** dela e publicar o par completo na `## 15` de `docs/CUSTO_DO_PICKUP.md`, substituindo a lacuna declarada na `## 14`. A metade em caracteres já está publicada: **26.760**, **−65,5%** contra 77.457. **Não estimar** — o valor ou é medido em sessão nova, ou a lacuna continua declarada.

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md`

**Verificação:** a `## 15` de `docs/CUSTO_DO_PICKUP.md` passa a conter o par completo, e a lacuna declarada na `## 14` é substituída por remissão a ele. O valor de `usage_1` é **lido** do primeiro `usage` de uma janela principal nova, não derivado de nenhuma outra medida do documento.

**Pronto quando:** o par (**caracteres** e **`usage_1`**) está publicado com as duas medidas ancoradas em observação, a metade em caracteres preservando os números já publicados (**26.760**, **−65,5%** contra 77.457), e a `## 14` não declara mais lacuna. **Não estimar:** sem sessão nova que produza o número, a tarefa devolve `blocked motivo=premissa` e a lacuna continua declarada — número inventado aqui seria publicado como fato num documento usado para decidir custo.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20

## Execução

**Consumo:** 16 tool uses, 54.8 k tokens, 164.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: verificacao 4 do despacho inaplicavel em arvore suja com janela concorrente; defeito de aceite do loop, nao da entrega
laudo: As duas metades do DC-4 podem nao ser do mesmo pickup: a secao 14 mede additionalContext em 6.122 ch e a secao 15 publica 16.459 bytes na sessao que produziu o usage_1. Se forem o mesmo objeto, a metade em chars daquela sessao seria ~36.140, nao 26.760.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
