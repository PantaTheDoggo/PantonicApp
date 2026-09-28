# RDO — P-0753 · AF-T8

# Humano

Tarefa "A conferência do backlog aceita o plano em esboço, e o planejador o registra no esboço" concluída em 2026-09-27.
A conferência do backlog passa a aceitar o plano em esboço, e o planejador grava o estado do plano já no esboço; ficou uma ressalva sobre plano legado.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 8/21 tarefas concluídas; próxima: "O `next` e o `show` entregam o card inteiro".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T8` — A conferência do backlog aceita o plano em esboço, e o planejador o registra no esboço
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** A conferência do backlog passa a aceitar o plano que o planejador registra já no esboço, antes de ele entrar na fila.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/plano.md` - `tests/fixtures/backlog/esqueleto/docs/plans/P-0-esboco/estado.tsv` - `tests/fixtures/backlog/esqueleto/docs/plans/_INBOX.md` - `tests/fixtures/backlog/esqueleto/docs/DIARIO_DE_OBRAS.md` - `.claude/agents/pantonic-planner.md` - `.claude/skills/diario-de-obras/SKILL.md`

**Verificação:** 1. `python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` → `exit 0` — antes `exit 1`, depois `exit 0` (esperado, não ensaiado) 2. `python -m pytest tests/test_backlog.py -q -k "esqueleto"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 3. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('no mesmo ato, '+c+'estado.tsv'+c),t.count('a linha do plano já está lá desde a Fase 3a'))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado) 4. `python -c "from pathlib import Path;t=Path('.claude/skills/diario-de-obras/SKILL.md').read_text(encoding='utf-8');print(t.count('O planejador grava o arquivo ao registrar'),t.count('O planejador grava o arquivo na Fase 3a'))"` → `0 1` — antes `1 0`, depois `0 1` (esperado, não ensaiado) 5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - conferência do backlog.aceite do plano em esboço — aceita o plano esboçado que tem o estado registrado e ainda não está na fila — Verificações 1 e 2 - planejador.registro do plano em esboço — o roteiro manda gravar o estado do plano junto do esboço — Verificações 3 e 4

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-1`, `DAF-10`, `F-8`, `F-22`.
- **Operação do modelo:** `OP-8` - OP-8: A conferência do backlog passa a aceitar o plano que o planejador registra já no esboço, antes de ele entrar na fila. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit `.claude/tools/backlog.py` (lint `check`) e o texto de dois papéis do kit: o agente planejador e a skill `diario-de-obras`; não importa de `tests/`.
- **Domínio:** *plano em esboço* — plano em pasta (`docs/plans/P-<n>-<slug>/plano.md`) cujo `estado.tsv` existe e tem, depois do cabeçalho, uma linha só: a do plano, com status `blocked`; e nenhuma linha de `docs/plans/_INBOX.md` cita o caminho dele. É o estado entre a Fase 3a e a Fase 5 do planejador.
- **Contratos/classes:** no bloco `C-10` de `check`, o conjunto de ids comparado com o contador deixa de fora o plano em esboço cujo id é igual ao do contador; o resto do `C-10` não muda (contador menor que o id de um plano que não está em esboço segue acusado). `C-8` e `C-13` não mudam (medido na `F-22`: não disparam nesse estado).
- **Passos:** 1. Em `backlog.py`, no bloco `C-10`, excluir de `ids_planos` o plano em esboço (predicado de `Domínio`) cujo id é o do contador. 2. Criar a fixture `tests/fixtures/backlog/esqueleto/`: `docs/plans/P-0-esboco/plano.md` com as três linhas `# P-0 — Plano em esboço`, linha vazia, `**Prefixo das tarefas no diário:** `` `ESB-T<n>` ``; `docs/plans/P-0-esboco/estado.tsv` com o cabeçalho `id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota` e a linha `P-0<TAB>plano<TAB>blocked<TAB>dependencia<TAB>2026-09-27<TAB>aguarda o modelo` (cada `<TAB>` é uma tabulação); `docs/plans/_INBOX.md` com a linha `**Próximo id de plano: P-0.**`; `docs/DIARIO_DE_OBRAS.md` igual a `tests/fixtures/backlog/pasta/docs/DIARIO_DE_OBRAS.md` sem a linha de índice `| P-0-GAM | Plano gama | ready | docs/plans/P-0-gama/plano.md |`. 3. Escrever os dois testes da seção `Testes`. 4. Em `.claude/agents/pantonic-planner.md`, Fase 3a, a linha depois de `antigo:` vira as três depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1 e sem a §5**, com o esqueleto fixo, nesta ordem: novo: Grave `docs/plans/P-<n>-<slug>/plano.md` **sem a §1 e sem a §5**, com o esqueleto fixo abaixo, e, no mesmo ato, `estado.tsv` na mesma pasta com o cabeçalho e só a linha do plano, `blocked`, razão `dependencia` — a linha do `_INBOX.md` e o contador ficam para a Fase 5. O esqueleto, nesta ordem: ``` 5. No mesmo arquivo, Fase 5, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo): ```text antigo: grave `estado.tsv` na pasta do plano (linha do plano e uma linha por card, esquema da skill `diario-de-obras`) novo: complete o `estado.tsv` da pasta do plano com uma linha por card (esquema da skill `diario-de-obras`; a linha do plano já está lá desde a Fase 3a) ``` 6. Em `.claude/skills/diario-de-obras/SKILL.md`, seção *Estado do plano em pasta*, as duas linhas depois de `antigo:` viram as quatro depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: `data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo ao registrar o plano; depois só `backlog.py status` o reescreve. `check` acusa `C-13` (card sem linha, linha novo: `data` `AAAA-MM-DD`; `nota` uma linha sem TAB, ou `-`. O planejador grava o arquivo na Fase 3a, junto do esqueleto, só com a linha do plano (`blocked`, razão `dependencia`), e acrescenta uma linha por card ao registrar o plano; depois só `backlog.py status` o reescreve. `check` acusa `C-13` (card sem linha, linha ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o texto do agente muda no corpo, não no frontmatter). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - `python .claude/tools/backlog.py check` sobre o repositório real segue saindo 0.
- **Não fazer:** não mudar `C-8`, `C-13` nem outro código de violação; não mudar o formato do contador; não tocar outra fase do arquivo do planejador; não mudar o frontmatter do agente.
- **Contingências:** - se, antes da mudança do passo 1, `python .claude/tools/backlog.py check --repo tests/fixtures/backlog/esqueleto` acusar violação além do `C-10` → parar e sinalizar `blocked` razão `premissa`, colando a saída. - se um teste existente de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_check_aceita_plano_em_esqueleto` — `check` sobre cópia da fixture `esqueleto` sai 0 (a regra de hoje sai 1 com `C-10`). TR `test_tr_check_esqueleto_com_linha_de_tarefa_segue_acusando_c10` — a mesma cópia com uma linha de tarefa acrescentada ao `estado.tsv` (o plano deixou de ser esboço) sai 1 com `C-10`.
- **Fora do escopo desta tarefa:** o card inteiro no `next` e no `show` (`AF-T9`); o pré-voo do pedido na Fase 0 (`AF-T17`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** _plano_em_esboco em .claude/tools/backlog.py:597 e o C-10 (:838-849) deixam de fora o plano em esboço cujo id é o do contador; fixture tests/fixtures/backlog/esqueleto/; planner Fases 3a e 5 e skill diario-de-obras (Estado do plano em pasta) mandam gravar estado.tsv com a linha do plano na Fase 3a - **Contrato:** backlog.py check aceita o plano em pasta em esboço (estado.tsv só com a linha do plano, blocked, fora do inbox); o predicado ainda não exige plano em pasta (ressalva do laudo, com o consultor) - **Não refazer:** nada a declarar - **Pendente:** predicado _plano_em_esboco omite a cláusula 'plano em pasta': plano legado blocked com id = contador fora do inbox é silenciado no C-10 (ressalva do laudo)

## Execução

**Consumo:** 56 tool uses, 122.7 k tokens, 444.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master vai fechar a tarefa "A conferência do backlog aceita o plano em esboço, e o planejador o registra no esboço" como done: registrar estado, RDO e telemetria.
