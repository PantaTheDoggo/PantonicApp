# RDO — P-0750 · CAH-T5

**Plano:** `docs/plans/P-0750-comunicacao-agente-humano.md`
**Tarefa:** `CAH-T5` — Os textos que mandavam citar sigla ao dono passam a mandar o título
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor das superfícies troca, nos textos que hoje mandam citar identificador ao dono, a sigla sozinha pelo título entre aspas, e marca a fronteira do documento publicado.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md` - `.claude/agents/pantonic-planner.md` - `.claude/skills/redacao-doc/SKILL.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command '(@(foreach ($f in ".claude/skills/scrum-master/SKILL.md",".claude/agents/pantonic-planner.md",".claude/skills/redacao-doc/SKILL.md") { @(Select-String -LiteralPath $f -SimpleMatch -Pattern "Mensagem legível ao dono").Count })) -join " / "' ``` → **1 / 1 / 1**. **Medido antes: 0 / 0 / 0**. 2. ``` pwsh -NoProfile -Command '"id=" + @(Select-String -LiteralPath .claude/skills/scrum-master/SKILL.md -SimpleMatch -Pattern "pelo identificador).").Count' ``` → **id=0**. **Medido antes: id=1**. 3. ``` python -m pytest tests -q ``` → **nenhuma falha**, total igual ao da véspera.

**Pronto quando:** - kit.textos que mandam citar sigla — os dois mandam o título entre aspas; o documento publicado aponta para a regra — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DCH-2, DCH-9; F-3; I-2, I-3.
- **Depende de:** `CAH-T1`, `CAH-T4`
- **Operação do modelo:** `OP-5` - OP-5: O mantenedor das superfícies troca, nos textos que hoje mandam citar identificador ao dono, a sigla sozinha pelo título entre aspas, e marca a fronteira do documento publicado. - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje. - precisa de: próxima mensagem ao dono — Quem implementa não a escreve. Ela mostra se a regra pegou.
- **Camada e fronteira:** skills e agente do kit, só nos trechos dirigidos ao dono; a superfície agente↔agente fica intocada (I-3).
- **Passos:** 1. Rodar a Verificação 1 e conferir os valores "antes". 2. Aplicar `S1`, `S2`, `P1`, `R1` com `Edit`. 3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — só ponteiro para a regra; I-3 — nada muda nas tabelas dos blocos A e B nem no repertório do painel.
- **Não fazer:** não tocar `passagem-de-bastao`, a tabela `M-*`, os blocos A e B, nem o formato das pendências ao dono (`:295-296`); não reescrever outro trecho do `pantonic-planner`.
- **Contingências:** 1. se algum texto antigo não aparecer exatamente uma vez no arquivo → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Fora do escopo desta tarefa:** a próxima mensagem ao dono (medição, não escrita); o painel (já conforme).

## Execução

**Consumo:** 20 tool uses, 55.8 k tokens, 77.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
