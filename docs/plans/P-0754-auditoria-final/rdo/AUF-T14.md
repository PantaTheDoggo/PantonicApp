# RDO — P-0754 · AUF-T14

# Humano

Tarefa "Os quatro herdados sem mudança fecham com a prova" concluída em 2026-09-28.
Os quatro itens herdados que não pedem mudança no kit ficaram encerrados no registro de origem, cada um com a prova.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 14/16 tarefas concluídas; próxima: "O guia de entrada descreve o kit com os herdados fechados".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T14` — Os quatro herdados sem mudança fecham com a prova
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa registra o encerramento dos quatro herdados que não pedem mudança no kit, cada um com a prova já levantada.

**Arquivos-alvo:** - `docs/plans/P-0753-auditoria-estagio-1/plano.md` - `docs/plans/P-0752-fato-no-ponto-de-uso.md` - `docs/DIARIO_DE_OBRAS.md`

**Verificação:** 1. `python -c "from pathlib import Path;c=[('docs/plans/P-0753-auditoria-estagio-1/plano.md','AE-21'),('docs/plans/P-0753-auditoria-estagio-1/plano.md','AE-22'),('docs/plans/P-0752-fato-no-ponto-de-uso.md','AE-51'),('docs/DIARIO_DE_OBRAS.md','AE-89')];print('[%s]'%'-'.join(str(sum(1 for l in Path(a).read_text(encoding='utf-8').splitlines() if l[4:9]==n and not l[9].isdigit() and 'Desfecho (P-0754, AUF-T14, 2026-09-28)' in l)) for a,n in c))"` → `[1-1-1-1]` — antes `[0-0-0-0]`, depois `[1-1-1-1]`

**Pronto quando:** - herdados que não pedem mudança.desfecho — os quatro estão encerrados, cada um com a prova de que não pede mudança no kit — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-7`, `DAU-28`; `H-6`, `H-7`, `H-11`, `H-17` (§2.1).
- **Operação do modelo:** `OP-14` - OP-14: Quem executa registra o encerramento dos quatro herdados que não pedem mudança no kit, cada um com a prova já levantada. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** registros de achado de planos fechados e do diário; nenhum código nem doutrina muda.
- **Passos:** cada passo acrescenta um sufixo ao **fim** de uma linha que já existe — a linha que começa pelo prefixo dado —, sem quebra nova e sem refluxo; cada linha de bloco perde o recuo da cerca, e o sufixo abre com um espaço. 1. Em `docs/plans/P-0753-auditoria-estagio-1/plano.md`, na linha que começa por ``- **AE-21** (`AF-T14`, fechamento, 2026-09-27)``, acrescentar: ```text · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — o teto de 4000 caracteres do trecho é conhecido do instrumento e sai marcado na evidência, como o laudo da `AF-T14` registrou. ``` 2. No mesmo arquivo, na linha que começa por ``- **AE-22** (`AF-T16`, fechamento, 2026-09-27)``, acrescentar: ```text · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a regra já existe: o ensaio dos cards em cópia, item 14 da Fase 4 de `.claude/agents/pantonic-planner.md`, e o critério (xii)(b) de `docs/RUBRICA_DE_REVISAO.md`. ``` 3. Em `docs/plans/P-0752-fato-no-ponto-de-uso.md`, na linha que começa por ``- **AE-51** (`FPU-T10`, fechamento, 2026-09-27)``, acrescentar: ```text · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: `docs/ACIONAMENTOS_CONSULTOR.tsv` é versionado desde o commit `2513964`, e `review_evidence.py` o trata como registro da condução. ``` 4. Em `docs/DIARIO_DE_OBRAS.md`, na linha que começa por ``- **AE-89** (`TK-90b`, fechamento, 2026-09-27)``, acrescentar: ```text · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: o card de tarefa é isento do teto do `backlog.py show`, e os oito cards do `P-0742` saem inteiros, sem marca de truncado. ``` 5. Rodar a Verificação e `python .claude/tools/backlog.py check`.
- **Restrições desta tarefa:** - `python .claude/tools/backlog.py check` sai 0 ao fim. - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28). - Só os `Arquivos-alvo` se editam, e neles só as quatro linhas dos passos; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a `**Rota:**` já escrita nas quatro linhas; não mexer no cabeçalho gerado do diário (entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->`); não mudar o `AE-50` nem o `AE-51` do `P-0740`, que repetem os ids.
- **Contingências:** - se o prefixo de um passo não casar exatamente uma linha do arquivo → parar e sinalizar `blocked` razão `premissa`, nomeando o passo e colando as linhas que casam.
- **Testes:** nenhum teste novo; a suíte inteira.
- **Fora do escopo desta tarefa:** o desfecho dos herdados que outros cards fecham com mudança no kit — eles fecham pela entrega do próprio card, e a §2.1 deste plano é a residência que os liga.
- **Handover:** 2026-09-28 · para `AUF-T15`, `AUF-T16` - **Entregue:** sufixo 'Desfecho (P-0754, AUF-T14, 2026-09-28)' nas linhas AE-21 e AE-22 de docs/plans/P-0753-auditoria-estagio-1/plano.md, AE-51 de docs/plans/P-0752-fato-no-ponto-de-uso.md e AE-89 de docs/DIARIO_DE_OBRAS.md - **Contrato:** os quatro herdados sem mudança estão encerrados na origem, cada um com a prova - **Não refazer:** os quatro desfechos - **Pendente:** nenhum

## Execução

**Consumo:** 16 tool uses, 52.7 k tokens, 113.7 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit" e vai pegar a tarefa "Os quatro herdados sem mudança fecham com a prova".
Tarefa "Os quatro herdados sem mudança fecham com a prova". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "Os quatro herdados sem mudança fecham com a prova" e vai executar: Quem executa registra o encerramento dos quatro herdados que não pedem mudança no kit, cada um com a prova já levantada.
Agente executor devolveu a tarefa "Os quatro herdados sem mudança fecham com a prova": review — sem pendência.
Tarefa "Os quatro herdados sem mudança fecham com a prova": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Os quatro herdados sem mudança fecham com a prova" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Os quatro herdados sem mudança fecham com a prova": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "Os quatro herdados sem mudança fecham com a prova" como done: registrar estado, RDO e telemetria.
