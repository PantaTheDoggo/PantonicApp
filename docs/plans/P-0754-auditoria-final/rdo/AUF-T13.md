# RDO — P-0754 · AUF-T13

# Humano

Tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit" concluída em 2026-09-28.
Diante de um papel que 'não consegue' algo, o planejador passa a perguntar primeiro se é só configuração do kit antes de contornar.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 13/16 tarefas concluídas; próxima: "Os quatro herdados sem mudança fecham com a prova".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T13` — O planejador pergunta se o impedimento do papel é ajuste do kit
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o planejador perguntar, diante de um papel que não consegue algo, se o impedimento é ajuste do kit ou limite da plataforma.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d]'%t.count('Impedimento de papel é pergunta antes de ser dado'))"` → `[1]` — antes `[0]`, depois `[1]`

**Pronto quando:** - planejador.pergunta sobre o impedimento do papel — antes de contornar, o planejador pergunta se o impedimento é ajuste do kit, que se corrige, ou limite da plataforma — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-11`, `DAU-31`; `H-9` (§2.1); `F-11`.
- **Depende de:** `AUF-T12`
- **Operação do modelo:** `OP-13` - OP-13: Quem executa faz o planejador perguntar, diante de um papel que não consegue algo, se o impedimento é ajuste do kit ou limite da plataforma. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Passos:** 1. Na `### Fase 1 — Levantamento delegado (nunca próprio)`, logo depois da linha que termina em `` de memória (2026-09-18, `RP-2`). `` (fim do bullet que começa por `` - **Todo comando que vai aparecer numa linha de `Verificação` ``) e antes da linha vazia que precede `Orçamento: no máximo **duas** rodadas`, inserir o bullet abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os dois espaços que sobram nas linhas de continuação entram no arquivo): ```text - **Impedimento de papel é pergunta antes de ser dado**: diante de "o papel X não consegue Y", a campanha pergunta primeiro se o impedimento é **configuração do kit** — frontmatter `tools:` do agente, `.claude/settings*.json` — ou **limite da plataforma**. Configuração do kit se corrige como tarefa do plano; só o limite da plataforma se contorna, com a razão registrada na §2 (2026-09-27, `RP-1` do `P-0753`). ``` 2. Rodar a Verificação.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a linha `Orçamento: no máximo **duas** rodadas de levantamento.` nem outro bullet da Fase 1; não editar o frontmatter do agente.
- **Contingências:** - se a linha âncora do passo 1 não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas finais da Fase 1.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Fora do escopo desta tarefa:** mudar a configuração de qualquer papel (nenhuma operação a pede).
- **Handover:** 2026-09-28 · para `AUF-T15` - **Entregue:** bullet 'Impedimento de papel é pergunta antes de ser dado' na Fase 1 de .claude/agents/pantonic-planner.md:137 - **Contrato:** diante de 'o papel X não consegue Y', a campanha pergunta primeiro se é configuração do kit (tools:, settings) ou limite da plataforma - **Não refazer:** o bullet do impedimento de papel - **Pendente:** nenhum

## Execução

**Consumo:** 7 tool uses, 46.3 k tokens, 85.5 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano" e vai pegar a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit".
Tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit" e vai executar: Quem executa faz o planejador perguntar, diante de um papel que não consegue algo, se o impedimento é ajuste do kit ou limite da plataforma.
Agente executor devolveu a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit": review — sem pendência.
Tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O planejador pergunta se o impedimento do papel é ajuste do kit" como done: registrar estado, RDO e telemetria.
