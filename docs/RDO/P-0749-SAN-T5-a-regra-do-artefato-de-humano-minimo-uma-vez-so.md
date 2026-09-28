# RDO — P-0749 · SAN-T5

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T5` — A regra do artefato de humano mínimo, uma vez só
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator da doutrina escreve, uma vez só, a regra de que todo artefato de humano é o menor possível, e os limites de tamanho que já existem passam a apontar para ela.

**Arquivos-alvo:** - `GOVERNANCA.md` - `.claude/skills/diario-de-obras/SKILL.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/skills/diario-de-obras/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "Artefato de humano mínimo").Count })) -join " / "' ``` → **2 / 1**. **Medido antes: 0 / 0**. 2. ``` pwsh -NoProfile -Command '"total=" + @(Select-String -Path "GOVERNANCA.md","README.md",".claude/agents/*.md",".claude/skills/*/SKILL.md" -SimpleMatch -Pattern "não repete dado cuja residência é artefato de máquina").Count' ``` → **total=1** (a linha da regra em `GOVERNANCA.md`). **Medido antes: total=0**. 3. ``` python -m pytest tests -q ``` → **o total do despacho, nenhuma falha**. **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).

**Pronto quando:** - kit.regra do artefato de humano — uma regra única: texto para o dono é o menor possível e não repete o que já está em tabela de máquina — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-11; §3.3; F-7; I-5.
- **Depende de:** `SAN-T4`
- **Operação do modelo:** `OP-5` - OP-5: O redator da doutrina escreve, uma vez só, a regra de que todo artefato de humano é o menor possível, e os limites de tamanho que já existem passam a apontar para ela. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.
- **Camada e fronteira:** doutrina do kit; a regra reside em `GOVERNANCA.md` §4.2, logo depois do bullet *Fechamento enxuto*, e em nenhum outro lugar; os dois limites locais recebem ponteiro.
- **Passos:** 1. Rodar a Verificação 1 e 2 e conferir os valores "antes". 2. Aplicar `H1`, `H2`, `H3` com `Edit`. 3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-5 — o texto da regra entra uma vez; em outro lugar, só o ponteiro.
- **Não fazer:** não criar item novo em `GOVERNANCA.md` §7; não copiar a regra para agente, skill ou `README.md`; não alterar o número `≤ 8`.
- **Contingências:** 1. se um texto antigo não aparecer exatamente uma vez no arquivo → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Fora do escopo desta tarefa:** a menção no `README.md` (`SAN-T6`).

## Execução

**Consumo:** 12 tool uses, 53.1 k tokens, 69.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
