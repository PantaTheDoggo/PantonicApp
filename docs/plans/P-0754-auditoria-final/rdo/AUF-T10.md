# RDO — P-0754 · AUF-T10

# Humano

Tarefa "A rubrica cobra a contingência pela regra do planejador" concluída em 2026-09-28.
A régua do revisor ganhou o critério que cobra, do plano de contingência de cada tarefa, a mesma regra que o planejador passou a seguir.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 10/16 tarefas concluídas; próxima: "O teste de interrupção nomeia os três casos que passaram por ele".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T10` — A rubrica cobra a contingência pela regra do planejador
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa acrescenta à rubrica de revisão o critério que cobra da contingência do card a regra que o planejador passou a seguir.

**Arquivos-alvo:** - `docs/RUBRICA_DE_REVISAO.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('a contingência é parte ensaiada do card, e não o contradiz'),t.count('| (xix) |')))"` → `[1-1]` — antes `[0-0]`, depois `[1-1]`

**Pronto quando:** - rubrica de revisão.critério de contingência — a rubrica cobra da contingência a mesma regra que o planejador segue ao escrevê-la — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-8` (iii), `DAU-31`; `H-1`, `H-8` (§2.1); `F-12`.
- **Depende de:** `AUF-T9`
- **Operação do modelo:** `OP-10` - OP-10: Quem executa acrescenta à rubrica de revisão o critério que cobra da contingência do card a regra que o planejador passou a seguir. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — régua de revisão; nenhum código muda.
- **Passos:** 1. Na `## 8. Rubrica de criação de tarefa`, na tabela `| # | o card passa quando | caso medido |`, logo depois da linha que começa por `| (xviii) |` e antes da linha vazia que fecha a tabela, inserir a linha abaixo (as quebras são as do bloco: uma linha só, sem o recuo da cerca do bloco): ```text | (xix) | **a contingência é parte ensaiada do card, e não o contradiz.** A ação `seguir com <X>` de cada contingência foi aplicada no ensaio, quando o plano ensaia, e as linhas de `Verificação` re-rodadas depois dela; ela não contraria nenhuma `Restrição` do mesmo card; e todo arquivo que ela escreve está nos `Arquivos-alvo`, seguido de `(condicional: contingência <n>)` | pendência 1 e `AE-24` do `P-0753` | ``` 2. Rodar a Verificação.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar as linhas `(i)`..`(xviii)`; não mudar a frase `dezoito critérios em vigor` da `### 8.1` — ela registra a medida de uma data e não conta a tabela.
- **Contingências:** - se a linha `| (xviii) |` não existir em `docs/RUBRICA_DE_REVISAO.md` ou já existir uma linha `| (xix) |` → parar e sinalizar `blocked` razão `premissa`, colando a linha encontrada.
- **Testes:** nenhum teste novo; a suíte inteira.
- **Fora do escopo desta tarefa:** o texto do planejador (`AUF-T9`, já entregue).
- **Handover:** 2026-09-28 · para `AUF-T15` - **Entregue:** critério (xix) na tabela da ## 8 de docs/RUBRICA_DE_REVISAO.md:312 — a contingência é parte ensaiada do card e não o contradiz - **Contrato:** o revisor cobra da contingência a regra do planejador (AUF-T9) - **Não refazer:** o critério (xix) - **Pendente:** nenhum

## Execução

**Consumo:** 8 tool uses, 49.1 k tokens, 90.2 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O planejador ensaia a contingência e a faz caber no card" e vai pegar a tarefa "A rubrica cobra a contingência pela regra do planejador".
Tarefa "A rubrica cobra a contingência pela regra do planejador". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A rubrica cobra a contingência pela regra do planejador" e vai executar: Quem executa acrescenta à rubrica de revisão o critério que cobra da contingência do card a regra que o planejador passou a seguir.
Agente executor devolveu a tarefa "A rubrica cobra a contingência pela regra do planejador": review — sem pendência.
Tarefa "A rubrica cobra a contingência pela regra do planejador": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A rubrica cobra a contingência pela regra do planejador" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A rubrica cobra a contingência pela regra do planejador": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "A rubrica cobra a contingência pela regra do planejador" como done: registrar estado, RDO e telemetria.
