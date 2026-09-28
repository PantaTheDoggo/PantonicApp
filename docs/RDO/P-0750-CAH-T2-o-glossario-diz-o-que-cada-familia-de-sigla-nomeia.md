# RDO — P-0750 · CAH-T2

**Plano:** `docs/plans/P-0750-comunicacao-agente-humano.md`
**Tarefa:** `CAH-T2` — O glossário diz o que cada família de sigla nomeia
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor da porta de entrada escreve no glossário o que cada família de sigla do kit nomeia, e diz com franqueza que as letras depois do D das decisões não abreviam palavra.

**Arquivos-alvo:** - `README.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command '(@(foreach ($t in "**Identificadores de trabalho**","As letras depois do ``D`` não abreviam palavra","Relatório Diário de Obra") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $t).Count })) -join " / "' ``` → **1 / 1 / 1**. **Medido antes: 0 / 0 / 0**. 2. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0**. 3. ``` python -m pytest tests -q ``` → **nenhuma falha**, total igual ao da véspera.

**Pronto quando:** - kit.glossário das siglas — todas as famílias do kit com o que nomeiam; as letras das decisões declaradas como sem expansão — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DCH-5, DCH-6; F-1; I-1, I-2.
- **Depende de:** `CAH-T1`
- **Operação do modelo:** `OP-2` - OP-2: O mantenedor da porta de entrada escreve no glossário o que cada família de sigla do kit nomeia, e diz com franqueza que as letras depois do D das decisões não abreviam palavra. - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
- **Camada e fronteira:** porta de entrada (`README.md`, seção do glossário, parte *Metadados*); documento publicado — segue a skill `redacao-doc` (nenhum id de plano ou de processo no texto novo).
- **Passos:** 1. Rodar a Verificação 1 e conferir os valores "antes". 2. Aplicar `G1` com `Edit` (o texto antigo são as quatro linhas do bullet, exatas). 3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — o bullet novo aponta para a regra, não a reescreve.
- **Não fazer:** não renumerar seção do `README.md`; não citar id de plano, de tarefa ou de decisão concreta no texto novo; não mexer nos demais bullets do glossário.
- **Contingências:** 1. se o texto antigo de `G1` não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo o trecho encontrado.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Fora do escopo desta tarefa:** a linha da skill nova na tabela *Skills* (`CAH-T4`).

## Execução

**Consumo:** 10 tool uses, 51.8 k tokens, 73.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
