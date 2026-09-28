# RDO — DIARIO_DE_OBRAS · TK-89b

# Humano

Tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa" concluída em 2026-09-26.
A doutrina do gate do card passou a dizer o que o gate de fato confere: oito itens, o card_check na parada B3 e o literal contido na faixa de linhas.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Tíquete "O gate do card religado deixou atrás o leitor de alvos e a doutrina": 2/2 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-89b` — A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o `scrum-master` diz "oito itens" do Gate de delegação e cita o `card_check` do passo 3 na linha `B3`; a rubrica `### 8.1` diz que o literal da âncora confere quando está contido em alguma linha da faixa `linha..fim`, como a `DFP-16` do `P-0752` e o `card_check`.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:62` — `seção "Gate de delegação", sete itens` - `.claude/skills/scrum-master/SKILL.md:285` — `pelo gate de delegação ou pelo` - `docs/RUBRICA_DE_REVISAO.md:340-341` — `contra a linha citada` - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('sete itens'),t.count('oito itens'))"` → `0 1` — antes `1 0`, depois `0 1`. 2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(sum(1 for l in t.splitlines() if l.startswith('| ') and 'B3' in l[:8] and 'card_check' in l))"` → `1` — antes `0`, depois `1`. 3. `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('contra a linha citada'))"` → `0` — antes `1`, depois `0`. 4. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava).

**Pronto quando:** as três frases da doutrina do gate batem com o gate que roda — Verificações 1 a 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Caso medido que motivou:** ver `## TK-89`, itens (2) e (3).
- **Passos:** 1. `.claude/skills/scrum-master/SKILL.md:62`: `sete itens` → `oito itens`. 2. `.claude/skills/scrum-master/SKILL.md:285`: `pelo gate de delegação ou pelo \`modelo.py check\` do passo 3` → `pelo gate de delegação, pelo \`modelo.py check\` ou pelo \`card_check\` do passo 3`. 3. Rubrica, na âncora do alvo (o trecho quebra entre as duas linhas): `desescapado e comparado por` + `strip()` + `contra a linha citada` → `desescapado e com \`strip()\`, e confere quando está contido em alguma linha (\`strip()\`) da faixa \`linha..fim\``.
- **Não fazer:** não tocar o bloco A do `scrum-master`; não mudar a ordem nem o texto dos gates do Passo 3; não tocar a `passagem-de-bastao`.
- **Contingências:** - se a linha `B3` ou a frase da rubrica tiver mudado de texto antes do despacho (o gate de âncora acusa) → aplicar a mesma troca de sentido sobre o texto novo e registrar em `pendencia=`.
- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** scrum-master/SKILL.md:62 'oito itens'; :285 B3 cita card_check; RUBRICA_DE_REVISAO.md §8.1 literal contido na faixa linha..fim - **Contrato:** a doutrina do gate do card bate com o gate que roda - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-89b-a-doutrina-do-gate-do-card-conta-oito-itens-cita-o-card-chec.md`, veredito aprovado 100%

## Execução

**Consumo:** 19 tool uses, 61.0 k tokens, 234.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Exercício ponta a ponta: as três frases batem com o gate que roda — 8 itens numerados no Gate de delegação da passagem-de-bastao (o 8º é o card_check), quarto gate card_check no passo 3 do scrum-master agora coberto por B3, e a rubrica 8.1 descreve exatamente o 'any(literal in linha.strip() for linha in faixa)' do card_check.py. O card_check sobre o próprio card, em status review, sai 1 por comparar mundo antes — comportamento documentado (DFP-2/DFP-4), não defeito da entrega. Cosmético sem rebaixamento: a linha 341 da rubrica ficou com ~140 colunas, fora do quebra-linha do parágrafo; o passo 3 do card não prescrevia rebobinar a quebra.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" e vai pegar a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa".
Tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa". Passo: conferir os gates e preparar o despacho.
Agente consultor recebe a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa" e vai triar.
Agente consultor devolveu a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa": rota resolve.
Agente executor recebe a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa" e vai executar: o `scrum-master` diz "oito itens" do Gate de delegação e cita o `card_check` do passo 3 na linha `B3`; a rubrica `### 8.1` diz que o literal da âncora confere quando está contido em alguma linha da faixa `linha..fim`, como a `DFP-16` do `P…
Agente executor devolveu a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa": review — sem pendência.
Agente revisor recebe a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa" como done: registrar estado, RDO e telemetria.
