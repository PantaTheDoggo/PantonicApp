# RDO — P-0755 · RAF-T12

# Humano

Tarefa "A rubrica reprova a asserção de teste removida sem ordem do card" concluída em 2026-09-29.
A rubrica de revisão passa a reprovar a asserção de teste removida sem ordem do card.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 21/49 tarefas concluídas; próxima: "A conferência do card compara o depois com o esperado e lê o literal com pontuação".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T12` — A rubrica reprova a asserção de teste removida sem ordem do card
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la.

**Arquivos-alvo:** - `docs/RUBRICA_DE_REVISAO.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');print('rubrica=%d-%d'%(t.count('removido em vez de reescrito.'),t.count('asserção de teste existente removida sem que o card mande')))"` → `rubrica=0-1` — antes `rubrica=1-0`, depois `rubrica=0-1`

**Pronto quando:** - rubrica de revisão.critério da asserção removida — a régua reprova a asserção de teste removida sem que o card mande removê-la — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-33`; `F-18` (a dimensão `testes` não cobre a asserção existente removida); relatório `R-12` (`AE-97` e `AE-98` do `P-0754`).
- **Depende de:** `RAF-T11a`, `RAF-T8a`
- **Operação do modelo:** `OP-12` - OP-12: Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.
- **Camada e fronteira:** doutrina do kit — a régua do revisor, `docs/RUBRICA_DE_REVISAO.md`, dimensão `testes`; nenhum código muda. O critério se apoia na seção `## Linhas removidas dos testes` que o dossiê de evidência passou a trazer na `RAF-T11` (uma entrada por arquivo de teste — sob `tests/`, com nome `test_*.py` — entre os alvos, com alvo curinga ou diretório expandido contra os tocados pela `RAF-T11a`, com as linhas que a entrega removeu desde o recorte do despacho). A regra mora só na rubrica; nenhum agente nem skill a repete.
- **Passos:** 1. Na seção da dimensão `testes` (o cabeçalho de nível 3 que abre a dimensão), trocar as duas linhas do bullet `- **Fonte da evidência:**` pelas duas do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text - **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados e exit code da suíte da área tocada. ``` Texto novo: ```text - **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados, exit code da suíte da área tocada e a seção `## Linhas removidas dos testes` da evidência. ``` 2. Na mesma seção, trocar as duas linhas do bullet `` - **`não conforme`:** `` pelas quatro do texto novo (mesma regra de quebra e recuo). Texto antigo: ```text - **`não conforme`:** teste exigido ausente, suíte em exit não-zero, ou teste cujo significado mudou removido em vez de reescrito. ``` Texto novo: ```text - **`não conforme`:** teste exigido ausente, suíte em exit não-zero, teste cujo significado mudou removido em vez de reescrito, ou asserção de teste existente removida sem que o card mande removê-la — a linha aparece na seção `## Linhas removidas dos testes` da evidência (`R-12`, `P-0755`). ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os bullets `conforme`, `parcial` e `não se aplica` da dimensão; não mudar a tabela de pesos; não editar `.claude/agents/pantonic-reviewer.md` (a régua mora na rubrica).
- **Contingências:** - se o texto antigo de um dos passos 1 e 2 não existir verbatim em `docs/RUBRICA_DE_REVISAO.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira.
- **Fora do escopo desta tarefa:** a seção da evidência (`RAF-T11`); a linha de invariância do card de revisão (`RAF-T17`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** docs/RUBRICA_DE_REVISAO.md, dimensão testes: Fonte da evidência inclui a seção '## Linhas removidas dos testes' e 'não conforme' cobre asserção de teste existente removida sem ordem do card (R-12) - **Contrato:** o revisor reprova na dimensão testes a asserção removida sem ordem do card, lendo a seção do dossiê - **Não refazer:** os dois bullets da rubrica - **Pendente:** nenhum

## Execução

**Consumo:** 14 tool uses, 55.5 k tokens, 168.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens" e vai pegar a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card".
Tarefa "A rubrica reprova a asserção de teste removida sem ordem do card". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card" e vai executar: Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la.
Agente executor devolveu a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card": review — sem pendência.
Tarefa "A rubrica reprova a asserção de teste removida sem ordem do card": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card" como done: registrar estado, RDO e telemetria.
