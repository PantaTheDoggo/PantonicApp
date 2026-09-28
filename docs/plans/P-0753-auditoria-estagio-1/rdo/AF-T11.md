# RDO — P-0753 · AF-T11

# Humano

Tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase" concluída em 2026-09-27.
O consultor passa a ler só as três entradas do acionamento, e a linha estratégica dele fica limitada a uma frase.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: relato de verificação do executor (SKILL.md em CRLF preservado; verificações 1 e 2, drift, 478 passed, card_check OK) — sem matéria pendente.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 11/21 tarefas concluídas; próxima: "O veredito do marco é um comando".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T11` — O consultor lê só as três entradas, e `estrategico=` é uma frase
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O consultor passa a responder cada acionamento lendo só as três entradas do despacho, com a avaliação estratégica numa frase.

**Arquivos-alvo:** - `.claude/agents/pantonic-consultant.md` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print(t.count('Lê só as três entradas.'),t.count('A linha '+c+'estrategico='+c+' tem **uma frase**'))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('cenario=docs/plans/P-<n>-<slug>/cenario.md'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - consultor.leitura por acionamento — lê só o cenário, o card, a evidência e a doutrina que o cenário aponta — Verificações 1 e 2 - consultor.avaliação estratégica — vem em uma frase — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-17`, `F-16`.
- **Depende de:** `AF-T10`
- **Operação do modelo:** `OP-11` - OP-11: O consultor passa a responder cada acionamento lendo só as três entradas do despacho, com a avaliação estratégica numa frase. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; despacho de tarefa — Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar.
- **Camada e fronteira:** texto de doutrina: o arquivo do agente `pantonic-consultant` (corpo, não o frontmatter) e a skill `scrum-master`, seção *Acionamento do consultor*.
- **Passos:** 1. Em `.claude/agents/pantonic-consultant.md`, seção *O que você faz*, inserir depois da linha do item `1. **Lê o cenário, não o plano.**` a linha abaixo, recuada três espaços, como continuação do item 1 (uma linha só): ```text **Lê só as três entradas.** O despacho traz três entradas — o caminho do cenário, o id do card e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento) —, e você lê só elas e, da doutrina, só a seção que o cenário aponta: relatório de auditoria, diário, RDO de outra tarefa e plano inteiro ficam fora, e fato que só eles teriam vai ao cenário como matéria inconclusiva. Caso medido (2026-09-27): o acionamento que leu o relatório de auditoria fora do cenário custou 131,2k tokens; o seguinte, com a instrução de não ler fora dele, 67,4k. ``` 2. No mesmo arquivo, inserir depois do terceiro sub-bullet do item 2 (a linha que começa por `   - ` + `` `rota=planejador` ``) e antes do item `3.` a linha abaixo, recuada três espaços, como continuação do item 2 (uma linha só): ```text A linha `estrategico=` tem **uma frase**, sem ponto no meio: o que o impedimento muda no escopo ou no objetivo do plano, ou qual decisão do dono ele revoga; o detalhe vai ao cenário, nunca à linha (caso medido, 2026-09-27: três frases num acionamento do plano fictício da auditoria). ``` 3. Em `.claude/skills/scrum-master/SKILL.md`, seção *Acionamento do consultor*, inserir depois do parágrafo que começa por `Forma **efêmera com cenário persistido**` o bloco abaixo, precedido e seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo, e as quatro linhas do molde ficam com quatro espaços, bloco de código por recuo): ```text Molde do despacho — as três entradas, e nada além delas: cenario=docs/plans/P-<n>-<slug>/cenario.md card=<ID> evidencia=<a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento, verbatim> Leia só o cenário, o card e a evidência acima e, da doutrina, só o que o cenário aponta. ```
- **Restrições desta tarefa:** - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda). - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar o frontmatter do agente; não mudar as regras de rota nem a tabela de estatística de acionamentos; não tocar a linha de telemetria da seção *Acionamento do consultor* (é da `AF-T5`).
- **Contingências:** - se o frontmatter do agente sair recusado por `python .claude/checks/frontmatter_yaml.py .claude/agents/pantonic-consultant.md` → a edição tocou o frontmatter: parar e sinalizar `blocked` razão `premissa`, colando o erro.
- **Testes:** nenhum teste novo (texto de doutrina); suítes a rodar: a inteira, como trava.
- **Fora do escopo desta tarefa:** a medida de tokens do consultor depois da mudança (lê-se na série `docs/telemetria.tsv`, com a gravação da `AF-T5`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** pantonic-consultant.md: item 1 ganha 'Lê só as três entradas' (:24) e o item 2 a regra de uma frase para estrategico= (:29); scrum-master seção Acionamento do consultor ganha o bloco do card - **Contrato:** o consultor lê só o cenário, o card e a evidência; estrategico= é uma frase sem ponto no meio - **Não refazer:** as duas regras do consultor - **Pendente:** nenhum

## Execução

**Consumo:** 9 tool uses, 47.7 k tokens, 156.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: relato de verificação do executor (SKILL.md em CRLF preservado; verificações 1 e 2, drift, 478 passed, card_check OK) — sem matéria pendente

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

scrum-master/SKILL.md e CRLF inteiro (433/433) e pantonic-consultant.md e LF: a primeira escrita do executor partiu por LF e abortou no assert antes de gravar; a reaplicacao preservou CRLF, verificado no bytes do arquivo. Card que insere bloco multilinha em arquivo alvo pode declarar o fim de linha do alvo e poupar a rodada.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar" e vai pegar a tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase".
Tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase" e vai executar: O consultor passa a responder cada acionamento lendo só as três entradas do despacho, com a avaliação estratégica numa frase.
Agente executor devolveu a tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase": review — scrum-master/SKILL.md era CRLF (a 1a escrita via split LF abortou no assert antes de gravar; reaplicado preservando CRLF); pantonic-consultant.md e LF; verif 1=1 1, 2=1, drift exit 0, pytest 478 passed, card_check OK.
Agente revisor recebe a tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase": aprovado 100%, bloqueante nenhuma, recomendação não informada.
Scrum master vai fechar a tarefa "O consultor lê só as três entradas, e `estrategico=` é uma frase" como done: registrar estado, RDO e telemetria.
