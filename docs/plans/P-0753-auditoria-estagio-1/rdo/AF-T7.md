# RDO — P-0753 · AF-T7

# Humano

Tarefa "A conferência do card lê a situação da tarefa no estado do plano em pasta" concluída em 2026-09-27.
A conferência do card passa a ler a situação da tarefa no estado do plano em pasta, e não só no card.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 7/21 tarefas concluídas; próxima: "A conferência do backlog aceita o plano em esboço, e o planejador o registra no esboço".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T7` — A conferência do card lê a situação da tarefa no estado do plano em pasta
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** A conferência do card passa a ler a situação da tarefa no estado do plano em pasta quando o card não a declara.

**Arquivos-alvo:** - `.claude/tools/card_check.py` - `tests/test_card_check.py` - `tests/fixtures/card_check/P-0-pasta/plano.md` - `tests/fixtures/card_check/P-0-pasta/estado.tsv`

**Verificação:** 1. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/P-0-pasta/plano.md --tarefa CP-T1` → `exit 0` — antes `exit 1`, depois `exit 0` (medido pelo consultor, `DAF-39`) 2. `python -m pytest tests/test_card_check.py -q -k "estado_tsv"` → `exit 0` — antes `exit 5`, depois `exit 0` (medido pelo consultor, `DAF-39`) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor, `DAF-39`; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (medido pelo consultor, `DAF-39`; trava)

**Pronto quando:** - conferência do card.situação do card em plano em pasta — lida do estado do plano; card concluído é comparado contra o mundo de depois — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-18`, `DAF-39`, `F-17`, `F-29`.
- **Operação do modelo:** `OP-7` - OP-7: A conferência do card passa a ler a situação da tarefa no estado do plano em pasta quando o card não a declara. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit `.claude/tools/card_check.py`; reusa `rdo._status_atual` (carregado por caminho) e `caminhos.pasta_do_plano`; não importa de `tests/`.
- **Contratos/classes:** em `verificar_tarefa`, a chamada `rdo._status_atual(plano_path, dossie.tarefa_id, dossie, None)` passa a `rdo._status_atual(plano_path, dossie.tarefa_id, dossie, _caminhos.pasta_do_plano(plano_path))`. `_status_atual` já lê a linha da tarefa em `estado.tsv` quando recebe a pasta (`F-29`). Status ausente continua imprimindo `status ausente: comparando antes`.
- **Passos:** 1. Trocar o quarto argumento da chamada de `_status_atual`, como em `Contratos/classes`. 2. Criar a fixture `tests/fixtures/card_check/P-0-pasta/plano.md` com o conteúdo abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo). O bullet `Entregável` de cada card é exigido por `rdo.extrair_dossie`: todo card tem exatamente um entre `Arquivos-alvo` e `Entregável` (`DAF-39`): ```text # P-0 — Fixture de card_check em plano em pasta **Prefixo das tarefas no diário:** `CP-T<n>` ### CP-T1 — Card concluído de plano em pasta [Sonnet · classe mecanica] - **Objetivo:** fixture de `card_check`: o status `done` mora só em `estado.tsv`. - **Entregável:** nenhum — fixture sintética, não é card vivo de plano. - **Verificação:** 1. `python -c "print('b')"` → `b` — antes `a`, depois `b` - **Pronto quando:** `card_check.py --tarefa CP-T1` sai 0, comparando `depois`. ### CP-T2 — Card pronto de plano em pasta [Sonnet · classe mecanica] - **Objetivo:** fixture de `card_check`: o status `ready` mora só em `estado.tsv`. - **Entregável:** nenhum — fixture sintética, não é card vivo de plano. - **Verificação:** 1. `python -c "print('a')"` → `b` — antes `a`, depois `b` - **Pronto quando:** `card_check.py --tarefa CP-T2` sai 0, comparando `antes`. ``` 3. Criar `tests/fixtures/card_check/P-0-pasta/estado.tsv` com as quatro linhas abaixo, campos separados por TAB (cada `<TAB>` é um caractere de tabulação): ```text id<TAB>tipo<TAB>status<TAB>razao<TAB>data<TAB>nota P-0<TAB>plano<TAB>in-progress<TAB>-<TAB>2026-09-27<TAB>- CP-T1<TAB>tarefa<TAB>done<TAB>-<TAB>2026-09-27<TAB>- CP-T2<TAB>tarefa<TAB>ready<TAB>-<TAB>2026-09-27<TAB>- ``` 4. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `468 passed`, 2026-09-27, `DAF-39`). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar `rdo._status_atual`; não mudar a regra de mundo por status (`done` → `depois`; demais → `antes`); não mudar `--mundo`.
- **Contingências:** - se um teste existente de `tests/test_card_check.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_estado_tsv_done_compara_depois` — `CP-T1` sai 0 (a regra de hoje compara `antes`, `a` contra a saída `b`, e sai 1). TR `test_tr_estado_tsv_ready_compara_antes` — `CP-T2` sai 0 comparando `antes`.
- **Fora do escopo desta tarefa:** o verbo `despachar`, que chama esta conferência (`AF-T10`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** verificar_tarefa (.claude/tools/card_check.py:363) passa _caminhos.pasta_do_plano(plano_path) a rdo._status_atual; fixture tests/fixtures/card_check/P-0-pasta/ (plano.md + estado.tsv); testes test_tf_estado_tsv_done_compara_depois e test_tr_estado_tsv_ready_compara_antes em tests/test_card_check.py - **Contrato:** em plano em pasta, card_check le a situacao da tarefa em estado.tsv (done compara 'depois'); versao 2 pendente do modelo diz que a fonte e incondicional em plano em pasta (a validar no Marco 2) - **Não refazer:** a leitura de estado.tsv pelo card_check - **Pendente:** copias do texto de OP-7 no card AF-T7 (plano.md:726 e :729) defasadas em relacao a versao 2 pendente do modelo; atualizam-se se o dono aceitar a versao 2 no marco

## Execução

**Consumo:** 27 tool uses, 88.4 k tokens, 242.3 s (fonte: `<usage>` do encerramento)

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

Scrum master vai marcar a tarefa "A conferência do card lê a situação da tarefa no estado do plano em pasta" como blocked, sem RDO.
Scrum master vai fechar a tarefa "A conferência do card lê a situação da tarefa no estado do plano em pasta" como done: registrar estado, RDO e telemetria.
