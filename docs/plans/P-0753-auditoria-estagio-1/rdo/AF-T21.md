# RDO — P-0753 · AF-T21

# Humano

Tarefa "A auto-auditoria do planejador se dosa pela classe do plano" concluída em 2026-09-27.
A auto-auditoria do planejador passa a ter a profundidade dosada pela classe do plano, declarada no cabeçalho.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 20/21 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T21` — A auto-auditoria do planejador se dosa pela classe do plano
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O planejador passa a dosar a própria auto-auditoria pela classe do plano, declarada no cabeçalho dele.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('Profundidade pela classe do plano'),t.count('plano de origem se derivado, classe do plano)'))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado) 2. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - planejador.profundidade da auto-auditoria — proporcional à classe do plano declarada no cabeçalho — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-5`, `DAF-8`, `DAF-29`, `F-15`. **Espera o veredito do dono no Marco 1** (card nasce `blocked` razão `dependencia`). Opções registradas: classe do plano no cabeçalho e tabela item × classe, recomendada e escrita neste card; ou protocolo inalterado. Veredito na segunda → rodada de replanejamento, card corretivo `AF-T21a` da `OP-21` (que cancela esta).
- **Depende de:** `AF-T19`
- **Operação do modelo:** `OP-21` - OP-21: O planejador passa a dosar a própria auto-auditoria pela classe do plano, declarada no cabeçalho dele. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.; escolha do dono no primeiro marco — Ninguém altera: o dono as dá no primeiro marco, e a operação que depende de cada uma espera por ela.
- **Camada e fronteira:** texto de doutrina: o esqueleto da Fase 3a e a abertura da Fase 4 do arquivo do agente planejador (corpo, não o frontmatter).
- **Passos:** 1. Fase 3a, no bloco do esqueleto, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo): ```text antigo: (cabeçalho: data de origem, iniciativa, plano de origem se derivado) novo: (cabeçalho: data de origem, iniciativa, plano de origem se derivado, classe do plano) ``` 2. Fase 4, inserir entre a linha `### Fase 4 — Auto-auditoria (antes de gravar, uma passada)` e o item `1.` o bloco abaixo, com uma linha vazia antes e depois (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo): ```text **Profundidade pela classe do plano.** O cabeçalho do plano declara `**Classe do plano:**` com um de três valores: `ferramentaria` (o produto é instrumento do kit — código, teste, fixture), `doutrina` (o produto é texto normativo — agente, skill, `GOVERNANCA.md`, rubrica) ou `produto` (o produto é código do projeto consumidor). A passada aplica os itens pela tabela; item que a tabela dispensa não se aplica, e a razão é a própria classe. | itens | ferramentaria | doutrina | produto | |---|---|---|---| | 1 a 6 e 8 a 12 | aplicam | aplicam | aplicam | | 7 (parser frio) e 13 (segunda leva) | só com gramática ou tabela normativa no plano | só com gramática ou tabela normativa no plano | aplicam | | 14 (ensaio em cópia) | só com arquivo compartilhado tocado por dois cards | só com arquivo compartilhado tocado por dois cards | aplica | ```
- **Restrições desta tarefa:** - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda). - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo). - Só o `Arquivos-alvo` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar o texto dos itens 1 a 14 da Fase 4; não tocar a Fase 1 (é da `AF-T19`); não escrever a classe no cabeçalho de plano nenhum.
- **Contingências:** - se o trecho `antigo:` do passo 1 não existir verbatim → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum teste novo; a suíte inteira como trava.
- **Fora do escopo desta tarefa:** a medida de tokens do planejador por classe na série (`§7`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** pantonic-planner.md: esqueleto da Fase 3a declara a classe do plano no cabeçalho (:189); Fase 4 abre com 'Profundidade pela classe do plano' e a tabela item × classe (:238) - **Contrato:** a auto-auditoria do planejador se dosa pela classe declarada no cabeçalho do plano - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 8 tool uses, 45.2 k tokens, 161.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "A auto-auditoria do planejador se dosa pela classe do plano" como done: registrar estado, RDO e telemetria.
