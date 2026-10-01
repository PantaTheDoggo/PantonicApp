# RDO — P-0754 · AUF-T12

# Humano

Tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano" concluída em 2026-09-28.
Quando o modelo ganha uma versão pendente, o planejador passa a reconferir as restrições das tarefas que citam o estado do plano.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 12/16 tarefas concluídas; próxima: "O planejador pergunta se o impedimento do papel é ajuste do kit".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T12` — A versão pendente do modelo reconfere a restrição que cita o estado do plano
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o planejador reconferir a restrição de card que cita o estado do plano sempre que o modelador grava uma versão pendente.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d]'%t.count('Versão pendente reconfere a restrição que cita o estado do plano'))"` → `[1]` — antes `[0]`, depois `[1]`

**Pronto quando:** - planejador.restrição que cita o estado do plano — quando o modelador grava uma versão pendente, o planejador reconfere toda restrição de card que cita o estado do plano — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-10`, `DAU-31`; `H-5` (§2.1).
- **Depende de:** `AUF-T11`
- **Operação do modelo:** `OP-12` - OP-12: Quem executa faz o planejador reconferir a restrição de card que cita o estado do plano sempre que o modelador grava uma versão pendente. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Passos:** 1. Na `## Rodada de replanejamento`, passo 4 (o que começa por `4. **Reescrever os cards**`), logo depois da linha que termina em `` dossiê `Ato de modelo` de `emenda`. `` e antes da linha que começa por `5. **Fechar o estado**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo): ```text **Versão pendente reconfere a restrição que cita o estado do plano:** quando o modelador grava uma versão pendente do modelo, toda `Restrição` de card que afirma estado do plano — seção que existe ou não, versão vigente, operação presente — se reconfere contra o plano gravado, no mesmo ato, e a que ficou falsa se reescreve (2026-09-27, `AE-20` do `P-0753`). ``` 2. Rodar a Verificação.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outra frase do passo 4 nem dos passos 1 a 3, 5 e 6 da rodada.
- **Contingências:** - se a linha âncora do passo 1 não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas do passo 4 da rodada.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Fora do escopo desta tarefa:** corrigir o parêntese da restrição da `AF-T14` do `P-0753` (card `done`).
- **Handover:** 2026-09-28 · para `AUF-T13` - **Entregue:** regra 'Versão pendente reconfere a restrição que cita o estado do plano' no passo 4 da Rodada de replanejamento de .claude/agents/pantonic-planner.md:539 - **Contrato:** versão pendente do modelo dispara a reconferência das Restrições de card que afirmam estado do plano - **Não refazer:** a regra da versão pendente - **Pendente:** nenhum

## Execução

**Consumo:** 9 tool uses, 48.1 k tokens, 94.5 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O teste de interrupção nomeia os três casos que passaram por ele" e vai pegar a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano".
Tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano" e vai executar: Quem executa faz o planejador reconferir a restrição de card que cita o estado do plano sempre que o modelador grava uma versão pendente.
Agente executor devolveu a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano": review — sem pendência.
Tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "A versão pendente do modelo reconfere a restrição que cita o estado do plano" como done: registrar estado, RDO e telemetria.
