# RDO — P-0749 · SAN-T4

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T4` — A doutrina ensina a pasta, o estado.tsv e a contagem em zero
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator da doutrina reescreve o que o kit ensina sobre plano: pasta própria com nomes fixos, estado na tabela que o planejador cria ao registrar o plano, e projeto novo nascendo com a contagem em zero.

**Arquivos-alvo:** - `GOVERNANCA.md` - `.claude/skills/diario-de-obras/SKILL.md` - `.claude/agents/pantonic-planner.md` - `.claude/skills/bootstrap-pantonic/SKILL.md` - `.claude/agents/pantonic-reviewer.md` - `.claude/skills/scrum-master/SKILL.md` - `.claude/agents/pantonic-consultant.md` - `.claude/skills/entrega-de-encerramento/SKILL.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/agents/pantonic-planner.md",".claude/skills/bootstrap-pantonic/SKILL.md",".claude/agents/pantonic-consultant.md",".claude/skills/scrum-master/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "P-<MMDD>-<slug>","P-NNNN","a materializa na linha","criado vazio.","docs/RDO/<plano>-<tarefa>-<slug>.md","docs/plans/_CENARIO").Count })) -join " / "' ``` → **1 / 0 / 0 / 0 / 0** (o `1` é a menção ao legado da troca `G2`). **Medido antes: 7 / 4 / 2 / 2 / 1**. 2. ``` pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/agents/pantonic-planner.md",".claude/agents/pantonic-reviewer.md",".claude/agents/pantonic-consultant.md",".claude/skills/diario-de-obras/SKILL.md",".claude/skills/bootstrap-pantonic/SKILL.md",".claude/skills/scrum-master/SKILL.md",".claude/skills/entrega-de-encerramento/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "P-<n>-<slug>/").Count })) -join " / "' ``` → **4 / 2 / 2 / 2 / 5 / 1 / 2 / 1**. **Medido antes: 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0**. 3. ``` pwsh -NoProfile -Command '(@(foreach ($f in "GOVERNANCA.md",".claude/agents/pantonic-planner.md",".claude/skills/diario-de-obras/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "estado.tsv").Count }) + @(@(Select-String -LiteralPath .claude/skills/bootstrap-pantonic/SKILL.md -SimpleMatch -Pattern "P-0.**").Count)) -join " / "' ``` → **≥ 1 em cada um dos quatro**. **Medido antes: 0 / 0 / 0 / 0**. 4. ``` python -m pytest tests -q ``` → **o total do despacho, nenhuma falha**. **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24).

**Pronto quando:** - kit.o que a doutrina ensina — pasta por plano, estado na tabela, contagem em zero no projeto novo — Verificação 1, 2, 3 - kit.número do plano — projeto novo começa em zero e soma um; aqui a contagem segue de onde está — Verificação 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-3, DSA-4, DSA-6, DSA-13, DSA-14; §3.1, §3.2, §3.4; F-6; I-4.
- **Depende de:** `SAN-T3a`
- **Operação do modelo:** `OP-4` - OP-4: O redator da doutrina reescreve o que o kit ensina sobre plano: pasta própria com nomes fixos, estado na tabela que o planejador cria ao registrar o plano, e projeto novo nascendo com a contagem em zero. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** doutrina do kit, só residências (I-4: nada em `~/.claude/`). Cada texto antigo abaixo aparece uma vez no seu arquivo, salvo onde indicado (medido em 2026-09-24), e se troca com `Edit`.
- **Passos:** 1. Rodar a Verificação 1 e 2 e conferir os valores "antes". 2. Aplicar as trocas `G1`..`N1`, na ordem, com `Edit`. 3. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** I-4 — nenhum arquivo em `~/.claude/`; só as trocas listadas; menção que descreve o legado fica (é o que as trocas marcam `legado`).
- **Não fazer:** não editar `README.md` (`SAN-T6`) nem escrever a regra do artefato de humano (`SAN-T5`); não reescrever menção a plano histórico (`P-0747`, `P-0722`); não renumerar seção.
- **Contingências:** 1. se um texto antigo não aparecer, ou aparecer mais vezes que o indicado, no arquivo da troca (editado por `TK-72`/`TK-73` no intervalo) → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca; 2. se a Verificação 4 falhar num teste que confere texto de agente ou skill → parar e sinalizar `blocked` razão `premissa`, devolvendo o teste.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Fora do escopo desta tarefa:** a regra do artefato de humano (`SAN-T5`); o `README.md` (`SAN-T6`); a cópia `~/.claude/CLAUDE.md` (Controle 1.1, `TK-68`).

## Execução

**Consumo:** 55 tool uses, 76.5 k tokens, 263.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; achado de processo (C-10 falso no estado de bootstrap P-0 sem plano) com rota em AE-4 do P-0749

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
