# RDO — P-0740 · LM-T10

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T10` — A escrita mecânica em definição de agente: o instrumento e a prova da rota
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — tornar a escrita em `.claude/agents/**` uma **aplicação mecânica de literais declarados**, feita por instrumento, e **provar em campo** que essa via funciona a partir de um contexto de executor. Enquanto a prova não existir, a rota da `DM-50` é hipótese.

**Arquivos-alvo:** - `.claude/tools/agentdef.py` (novo) - `tests/test_agentdef.py` (novo) - `.claude/agents/pantonic-planner.md` - `.claude/README.md`

**Verificação:** (forma normativa publicada pela `LM-T5`; todo valor abaixo foi rodado na autoria, 2026-09-19 — `DM-12`, `DM-24`) 1. ``` python -m pytest tests/test_agentdef.py -q ``` → verde, com os **seis** testes nomeados acima. **Medido antes: exit 4** (o arquivo de teste não existe; `pytest` sai 4 em *file or directory not found*). 2. ``` python .claude/tools/agentdef.py apply --arquivo README.md --de a --para b ``` → **exit 1**, nomeando a recusa de alvo fora do diretório de agentes. **Medido antes: exit 2** (o instrumento não existe; `python` sai 2 em *can't open file*). 3. ``` python .claude/tools/agentdef.py apply --arquivo .claude/agents/pantonic-planner.md --de Fase --para Etapa ``` → **exit 1**, nomeando a ocorrência não-única, **sem alterar o arquivo**. **Medido antes: exit 2** (o instrumento não existe). O literal `Fase` foi escolhido por ser medidamente não-único no alvo: 19 ocorrências em 2026-09-19. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'não mede nada por conta própria' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. (A afirmação falsa sai da `description`.) 5. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern 'não sonda codebase por conta própria' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. (E entra a verdadeira, no lugar dela.) 6. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/README.md -Pattern 'não sonda codebase por conta própria' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. (A projeção foi regenerada no mesmo ato — `DM-16` (iv). Sem esta linha, a tarefa fecharia verde deixando o `check-drift` vermelho para a tarefa seguinte.) 7. ``` pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE" ``` → **exit 0**. **Medido antes: exit 0** (2026-09-19). Regressão, não discriminante — e aqui ela só continua verde **porque** o passo 4 rodou; é a guarda que pega o esquecimento. 8. ``` python -m pytest tests/ -q ``` → verde, **somando** os seis testes novos ao total re-medido no despacho e **sem reduzi-lo** (`DM-23`). **Medido antes: 191 passed** (2026-09-19, re-medido no `ESC-27` — o reparo do instrumento de índice somou 4 TF ao piso de 187; relação, **re-medir no despacho**).

**Pronto quando:** as oito linhas de `Verificação` saem nos valores declarados; o instrumento existe com o verbo único e a borda de residência única; os seis testes existem com os nomes fixados; a `description` do `pantonic-planner` deixou de afirmar o falso **por aplicação do instrumento**, e a projeção `.claude/README.md` fechou no mesmo ato. Se a contingência 1 casar, o critério de pronto é **a medida da recusa**, registrada com o comando literal — e a tarefa fecha `blocked`, que é desfecho e não fracasso.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — primeira tarefa da fila da próxima janela (`DM-50`).
- **Esforço:** medium
- **Depende de:** `DM-50`, que a decide. Nenhuma tarefa aberta.
- **Passos:** 1. Escrever `.claude/tools/agentdef.py` conforme o contrato acima. 2. Escrever `tests/test_agentdef.py` com os seis testes nomeados. 3. Aplicar o par literal **rodando o instrumento pelo `Bash`**, com o alvo `.claude/agents/pantonic-planner.md`. 4. Regenerar a projeção no **mesmo ato** (`DM-16` (iv)): `kit_check.ps1 -Mode generate` — a `description` alimenta `.claude/README.md`, e sem isso o `check-drift` abre vermelho.
- **Restrições desta tarefa:** o par literal é aplicado **rodando o instrumento**, nunca por `Edit` ou `Write` sobre o arquivo de agente. É essa execução que constitui a prova da rota: aplicar por edição direta deixa o arquivo igual e a prova **inexistente**, e a tarefa fica sem entregar o que o `DM-50` pediu. O instrumento **não** decide conteúdo: ele aplica literal declarado no card.
- **Não fazer:** não tocar `.claude/agents/pantonic-executor.md` nem `.claude/skills/scrum-master/SKILL.md` — o motivo `ferramenta` e a guarda `G-TOOLDENY` são a `LM-T11`, e esta tarefa existe justamente para tornar aquela executável; não alterar `model` nem `name` de agente nenhum; não estender `rdo.py`, `backlog.py`, `review_evidence.py` nem `card_check.py`; não criar verbo além de `apply`; não commitar.
- **Contingências:** 1. se o `Bash` que roda o instrumento for **recusado** ao executor → **essa medida é o entregável**, não uma falha: devolver `blocked motivo=premissa` colando a **linha literal da recusa** e o **comando exato** que a produziu, e registrar no corpo da tarefa qual ferramenta foi recusada sobre qual caminho. **Não** contornar por outra ferramenta, **não** pedir ao loop que aplique. É com esse dado que a `DM-50` decide entre as saídas (b) e (d), e é ele que impede a quarta repetição do problema; 2. se o par literal já estiver aplicado no arquivo (o `de` não for encontrado) → **seguir** com o restante da tarefa e registrar o fato: o instrumento e os testes são o entregável principal, e a `Verificação` 4 e 5 continuam discriminando; 3. se `kit_check.ps1 -Mode generate` alterar mais que a linha da `description` no `.claude/README.md` → parar e sinalizar `blocked` razão `premissa`, colando o diff: projeção que se move além do esperado é achado, não resíduo.

## Execução

**Consumo:** 17 tool uses, 82.1 k tokens, 281.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O exercicio ponta a ponta pagou: os seis testes de fixture cobrem os itens 1, 3, 4 e 5 do contrato e nenhum deles alcanca os dois modos de falha achados na revisao - so a execucao do verbo fora das fixtures os expos. A prova da rota (a razao de ser da tarefa, DM-50) foi confirmada por dois registros mecanicos independentes: a invocacao do instrumento pelo Bash com o par literal exato as 18:25:25Z e o mtime do .claude/agents/pantonic-planner.md as 18:25:26Z, posterior a criacao do agentdef.py (18:24:52Z), sem nenhuma chamada de Edit ou Write sobre o arquivo de agente na janela. A divergencia do card (19 ocorrencias de Fase contra 6 medidas hoje, case-sensitive) nao afetou aceite algum porque a propriedade exigida pela Verificacao 3 - literal nao-unico no alvo - sobrevive a diferenca.

## Fechamento

**Desdobramento:** aprovado
