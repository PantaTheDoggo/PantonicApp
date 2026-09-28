# RDO — P-0750 · CAH-T4a

**Plano:** `docs/plans/P-0750-comunicacao-agente-humano.md`
**Tarefa:** `CAH-T4a` — O título de tarefa na skill da mensagem ao dono para antes da etiqueta
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `CAH-T4` (`AE-7`): a linha da §2 da skill `mensagem-ao-dono` que diz onde achar o título de tarefa, tíquete e plano passa a cortar a etiqueta `[modelo · esforço · classe]` que o cabeçalho de tarefa traz depois do título.

**Arquivos-alvo:** - `.claude/skills/mensagem-ao-dono/SKILL.md` (uma célula da tabela da §2)

**Verificação:** 1. ``` pwsh -NoProfile -Command '"novo=" + @(Select-String -LiteralPath .claude/skills/mensagem-ao-dono/SKILL.md -SimpleMatch -Pattern "entre `` — `` e `` [``").Count + " antigo=" + @(Select-String -LiteralPath .claude/skills/mensagem-ao-dono/SKILL.md -SimpleMatch -Pattern "o texto depois de").Count' ``` → **novo=1 antigo=0**. **Medido antes: novo=0 antigo=1**; medido pelo consultor numa cópia com `T1` aplicado: `novo=1 antigo=0`. 2. ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` → **exit 0**. Medido antes, na árvore: exit 0. Numa cópia de `.claude/` o comando falha só pela materialização (caminho absoluto do destino, 13 problemas) com e sem `T1` — a troca não acrescenta problema. 3. ``` python -m pytest tests -q ``` → **nenhuma falha**, total igual ao da véspera.

**Pronto quando:** - kit.procedimento da mensagem — a busca do título de tarefa corta a etiqueta — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DCH-4; AE-7. Medido pelo consultor (2026-09-25): `backlog.py show CAH-T4` → `### CAH-T4 — A skill da mensagem ao dono [Sonnet · esforço medium · classe redacao]`; `show TK-72` → `## TK-72 — A régua de autoria de card do kit`; `show P-0750` → `# P-0750 — Comunicação agente↔humano: …` — só a tarefa traz ` [`.
- **Depende de:** `CAH-T4`
- **Operação do modelo:** `OP-4` - OP-4: O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit. - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
- **Camada e fronteira:** corpo da skill; o frontmatter não muda, então `.claude/README.md` não muda (o gerador lê só `name` e `description`).
- **Passos:** 1. Rodar a Verificação 1 e conferir o valor "antes". 2. Aplicar `T1` com `Edit`. 3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — a skill segue só apontando para a regra.
- **Não fazer:** não tocar outra linha da skill nem o `README.md`; não rodar `kit_check.ps1 -Mode generate`; não editar o card da `CAH-T4`.
- **Contingências:** 1. se o texto antigo de `T1` não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Fora do escopo desta tarefa:** resolvedor sigla→título por função (DCH-10); propagação aos derivados (`TK-81`).

## Execução

**Consumo:** 10 tool uses, 49.3 k tokens, 61.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
