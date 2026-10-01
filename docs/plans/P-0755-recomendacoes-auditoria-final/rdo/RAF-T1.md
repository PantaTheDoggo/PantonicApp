# RDO — P-0755 · RAF-T1

# Humano

Tarefa "O loop de plano recém-planejado abre em janela nova" concluída em 2026-09-28.
O gerente do loop passa a saber que plano recém-planejado se executa numa janela nova, com o plano gravado como único insumo.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 1/40 tarefas concluídas; próxima: "O medidor de custo da sessão vira comando do kit".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T1` — O loop de plano recém-planejado abre em janela nova
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('janela-nova=%d'%t.count('- **Janela:** o loop de um plano recém-planejado abre numa janela nova'))"` → `janela-nova=1` — antes `janela-nova=0`, depois `janela-nova=1`

**Pronto quando:** - gerente do loop.janela em que o loop abre — o planejamento encerra a sua janela no primeiro marco, e o loop de um plano recém-planejado abre numa janela nova, com o plano gravado como único insumo — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-4`, `DRF-6` (a doutrina mora no Passo 1 da skill `scrum-master`); `F-6`, `F-8`; relatório `R-01`.
- **Operação do modelo:** `OP-1` - OP-1: Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`, rotina de quem conduz o loop; nenhum código muda. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só." A regra nova mora só no Passo 1 da skill (residência única, `DRF-6`); nenhum outro arquivo a repete.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, no `### Passo 1 — Gate de modelo do contexto principal`, logo depois da linha `  gate.` (a última linha do bullet `- **Ação:**`) e antes da linha que começa por `- **Saída:** modelo conferido`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde os dois espaços do recuo deste card): ```text - **Janela:** o loop de um plano recém-planejado abre numa janela nova, separada da que o planejou, com o plano gravado como único insumo; a janela do planejamento encerra no Marco 1 (`R-01` da auditoria final, `P-0755`). Quem conduz e planejou o plano na janela corrente não despacha tarefa dele: encerra pelo relatório de janela, com a regra "loop de plano recém-planejado abre em janela nova", e o dono abre a janela do loop. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que o bloco não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no texto do `- **Ação:**` nem do `- **Saída:**` do Passo 1; não acrescentar a regra a `GOVERNANCA.md`, a outra skill ou a agente (a regra mora num lugar só); não criar o medidor de custo (é da `RAF-T2`).
- **Contingências:** - se a linha `  gate.` seguida da linha que começa por `- **Saída:** modelo conferido` não existir em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas 32 a 45 do arquivo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** o instrumento que mede o custo por turno (`RAF-T2`); a medida do ganho sobre o transcript do loop, que é da condução no relatório do Marco 6 (§7).
- **Handover:** 2026-09-28 · para quem vier depois - **Entregue:** campo '- **Janela:**' no Passo 1 da skill scrum-master, .claude/skills/scrum-master/SKILL.md:43-47 (hoje recuado 3 espaços, aninhado sob '- **Ação:**') - **Contrato:** a regra 'loop de plano recém-planejado abre em janela nova' mora só no Passo 1 da skill scrum-master; nenhum outro arquivo a repete - **Não refazer:** o texto do bloco; suíte 521 passed e check-drift 0 já medidos - **Pendente:** o recuo do campo (sub-item em vez de campo irmão de Gatilho/Entrada/Ação/Saída) vai à triagem do consultor

## Execução

**Consumo:** 14 tool uses, 79.6 k tokens, 300.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Instrucao de recuo relativa ('perde N espacos') e fragil quando o bloco vive dentro de item numerado; a forma absoluta ('perde o recuo deste card', usada no item 4 da RAF-T3) nao deixa margem. A Verificacao por count de substring e cega a recuo.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O loop de plano recém-planejado abre em janela nova". Passo: conferir os gates e preparar o despacho.
Tarefa "O loop de plano recém-planejado abre em janela nova". Passo: conferir os gates e preparar o despacho.
Tarefa "O loop de plano recém-planejado abre em janela nova". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O loop de plano recém-planejado abre em janela nova" e vai executar: Quem executa ensina o gerente do loop a abrir a execução de um plano recém-planejado numa janela nova, separada da que o planejou, com o plano gravado como único insumo.
Agente executor devolveu a tarefa "O loop de plano recém-planejado abre em janela nova": review — sem pendência.
Tarefa "O loop de plano recém-planejado abre em janela nova": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O loop de plano recém-planejado abre em janela nova" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O loop de plano recém-planejado abre em janela nova": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O loop de plano recém-planejado abre em janela nova" como done: registrar estado, RDO e telemetria.
