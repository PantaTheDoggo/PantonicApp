# RDO — P-0755 · RAF-T1a

# Humano

Tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo" concluída em 2026-09-28.
A regra da janela nova passa a ser campo próprio do Passo 1 do loop, ao lado de Gatilho, Entrada, Ação e Saída.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 2/41 tarefas concluídas; próxima: "O medidor de custo da sessão vira comando do kit".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T1a` — O campo Janela do Passo 1 fica irmão dos outros campos do passo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa sobe à coluna 0 o campo `- **Janela:**` que a `RAF-T1` gravou no Passo 1 da skill `scrum-master`, para ele ser campo do passo como `Gatilho`, `Entrada`, `Ação` e `Saída`, e não sub-item do `- **Ação:**`.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('coluna0=%d aninhado=%d continua=%d'%(t.count('  gate.\n- **Janela:** o loop de um plano recém-planejado abre numa janela nova'),t.count('   - **Janela:**'),sum(t.count('\n  '+s) for s in ('planejou, com o plano gravado','despacha tarefa dele: encerra','recém-planejado abre em janela nova'))))"` → `coluna0=1 aninhado=0 continua=3` — antes `coluna0=0 aninhado=1 continua=0`, depois `coluna0=1 aninhado=0 continua=3` 2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('janela-nova=%d'%t.count('- **Janela:** o loop de um plano recém-planejado abre numa janela nova'))"` → `janela-nova=1` — antes `janela-nova=1`, depois `janela-nova=1` (invariância: o texto do campo não muda)

**Pronto quando:** - gerente do loop.janela em que o loop abre — a regra da janela nova é campo próprio do Passo 1, irmão de `Gatilho`, `Entrada`, `Ação` e `Saída` — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-43`; `AE-122` (laudo da `RAF-T1`, ressalva 88); `DRF-4`, `DRF-6`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-1` - OP-1: Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, rotina de quem conduz o loop; nenhum código muda. Muda só o recuo das cinco linhas do campo; o texto delas fica como a `RAF-T1` o gravou.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, no `### Passo 1 — Gate de modelo do contexto principal`, o campo `- **Janela:**` (hoje as linhas 43 a 47: a primeira começa por três espaços e `- **Janela:**`, as quatro de continuação por cinco espaços) perde três espaços de recuo em cada linha: a primeira passa a começar na coluna 0 por `- **Janela:**`, logo depois da linha `  gate.`, e as quatro de continuação por dois espaços, como as do `- **Ação:**`. O texto e as quebras não mudam; o número de linhas do arquivo não muda. 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que a edição não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (medido 0 antes, 2026-09-28). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar palavra do campo `- **Janela:**`, do `- **Ação:**` nem do `- **Saída:**`; não mexer em outro passo da skill (os Passos 3 e 4 são da `RAF-T4`).
- **Contingências:** - se a Verificação 1 não imprimir `coluna0=0 aninhado=1 continua=0` antes da edição → parar e sinalizar `blocked` razão `premissa`, colando a saída e as linhas 36 a 50 do arquivo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** regra nova de recuo no planejador (`DRF-43`); o vermelho do `dead_code.py` sobre a sonda (`DRF-44`).
- **Handover:** 2026-09-28 · para `RAF-T4` - **Entregue:** campo '- **Janela:**' do Passo 1 na coluna 0, continuações com 2 espaços, .claude/skills/scrum-master/SKILL.md:43-47 - **Contrato:** Passo 1 da skill scrum-master tem cinco campos irmãos: Gatilho, Entrada, Ação, Janela, Saída; a regra da janela nova mora só ali - **Não refazer:** recuo e texto do campo Janela; suíte 521 passed e check-drift 0 - **Pendente:** nenhum

## Execução

**Consumo:** 8 tool uses, 50.5 k tokens, 114.7 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O loop de plano recém-planejado abre em janela nova" e vai pegar a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo".
Tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo" e vai executar: Quem executa sobe à coluna 0 o campo `- **Janela:**` que a `RAF-T1` gravou no Passo 1 da skill `scrum-master`, para ele ser campo do passo como `Gatilho`, `Entrada`, `Ação` e `Saída`, e não sub-item do `- **Ação:**`.
Agente executor devolveu a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo": review — sem pendência.
Tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo" como done: registrar estado, RDO e telemetria.
