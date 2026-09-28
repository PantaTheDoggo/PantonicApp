# RDO — P-0753 · AF-T5

# Humano

Tarefa "O gancho de telemetria grava todo papel do kit, e a soma do plano os separa" concluída em 2026-09-27.
O gancho de telemetria passa a gravar o consumo de todos os papéis do kit — revisor, consultor, planejador — e a soma do plano os separa.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 5/21 tarefas concluídas; próxima: "A recomendação do laudo viaja na primeira linha do revisor".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T5` — O gancho de telemetria grava todo papel do kit, e a soma do plano os separa
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O gancho de telemetria passa a gravar o consumo de todo papel do kit, que a soma do plano conta por inteiro.

**Arquivos-alvo:** - `.claude/tools/telemetria_hook.py` - `tests/test_telemetria_hook.py` - `.claude/tools/encerrar.py` - `tests/test_encerrar.py` - `GOVERNANCA.md` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -m pytest tests/test_telemetria_hook.py -q -k "papel"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python -m pytest tests/test_encerrar.py -q -k "consumo_por_papel"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 3. `python -c "from pathlib import Path;c=chr(96);t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print(t.count('só grava a linha do '+c+'pantonic-executor'+c),t.count('grava a rodada de todo papel'))"` → `0 1` — antes `1 0`, depois `0 1` (esperado, não ensaiado) 4. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('da notificação, como a de qualquer subagente'))"` → `0` — antes `1`, depois `0` (esperado, não ensaiado) 5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - série de telemetria.papéis gravados — toda rodada de agente do kit grava sozinha, com o papel no identificador — Verificações 1, 3 e 4 - série de telemetria.consumo do plano — o total soma todas as rodadas do plano, de todos os papéis — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-15`, `DAF-25`, `F-13`, `F-30`.
- **Depende de:** `AF-T4`
- **Operação do modelo:** `OP-5` - OP-5: O gancho de telemetria passa a gravar o consumo de todo papel do kit, que a soma do plano conta por inteiro. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** gancho `SubagentStop` em `.claude/tools/telemetria_hook.py` (cliente do CLI `.claude/tools/telemetria.py append`, por subprocesso; nunca reimplementa validação de coluna); falha aberta total; `encerrar.py` carrega irmãos por caminho; nada importa de `tests/`.
- **Contratos/classes:** - `processar(payload, estado_path, telemetria_cli, tsv_path=None, data=None) -> bool` — assinatura inalterada. Age para todo `agent_type` iniciado por `pantonic-`; outro `agent_type` (ou vazio) é silêncio, sem escrever e sem apagar nada. Sem `agent_transcript_path` legível, silêncio. O estado `tarefa-corrente.json` **não se apaga mais**: vale até o despacho seguinte do executor, que o sobrescreve. - Tarefa da linha, por papel: `pantonic-executor` → `estado["tarefa"]` (sem estado: silêncio, como hoje); `pantonic-reviewer` → `<tarefa>-revisao`; `pantonic-consultant` → `<tarefa>-consultor-<n>`, `<n>` = 1 + número de linhas da série cuja coluna `tarefa` começa por `<tarefa>-consultor-`; `pantonic-planner` → `<P-n>-planejador`; `pantonic-model-designer` → `<P-n>-modelador`; `pantonic-scout` → `<P-n>-scout`; outro `pantonic-<nome>` → `<P-n>-<nome>`. `<tarefa>` = `estado["tarefa"]`; `<P-n>` = a primeira ocorrência de `P-` seguido de dígitos no texto da primeira entrada `type == "user"` do transcript (conteúdo em texto ou lista de blocos `text`). Sem o id que o papel pede: `sem-id-<sufixo>` (`sem-id-revisao`, `sem-id-consultor`, `sem-id-planejador`, `sem-id-modelador`, `sem-id-scout`, `sem-id-<nome>`). - Modelo da linha: executor → `estado["modelo"]` em minúsculas (como hoje); demais papéis → o campo `message.model` da última entrada `assistant` do transcript, normalizado: contém `opus` → `opus`, `sonnet` → `sonnet`, `haiku` → `haiku`, outro texto → ele mesmo em minúsculas, ausente → `nao-informado`. - Projeto da linha: `estado["projeto"]` quando há estado; senão o nome da pasta `estado_path.parents[2]`. A série lida para contar `<n>` é `tsv_path` quando dado; senão `estado_path.parents[2] / "docs" / "telemetria.tsv"`. - `encerrar._consumo_do_plano(tsv, plano_id, ids)` ganha os grupos `planejador`, `modelador` e `scout` (linha cuja `tarefa` termina em `-planejador`, `-modelador`, `-scout`), na ordem `executor`, `revisor`, `consultor`, `planejador`, `modelador`, `scout`, `outros`; a regra de pertença ao plano não muda (id de tarefa do plano, ou prefixo `<plano_id>-`).
- **Passos:** 1. Reescrever `processar` e a docstring do módulo (parágrafo **Filtro**) pela regra de `Contratos/classes`; apagar `_AGENT_TYPE_EXECUTOR` se ficar sem uso. 2. Em `tests/test_telemetria_hook.py`: renomear `test_tr_hook_so_executor_consome_estado` para `test_tf_hook_grava_revisor_com_papel` e trocar as asserções para a linha `EXA-T55-revisao` gravada e o estado preservado; em `test_tf_processar_payload_de_fixture_grava_linha_esperada_no_tsv`, a asserção `assert not estado_path.exists()` passa a `assert estado_path.exists()`; em `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia` (`DAF-37`), as asserções `assert estado_rh is False`, `assert estado_rs is False` e `assert estado_vs is False` passam a `is True` (`assert estado_vh is True` fica), e na docstring o trecho ``main` apagaria o `.claude/estado/tarefa-corrente.json` real` passa a ``main` gravaria na `docs/telemetria.tsv` real` e o trecho `o transcript não é encontrado, o estado sobrevive e o TSV não é criado` passa a `o transcript não é encontrado e o TSV não é criado`; `test_tr_processar_agent_type_fora_do_filtro_e_silencio_e_preserva_o_estado` e `test_tr_processar_sem_estado_e_silencio_sem_escrita` ficam como estão. 3. Escrever os testes novos da seção `Testes`. 4. Em `encerrar._consumo_do_plano`, os três grupos novos. 5. Em `GOVERNANCA.md` §4.2, as quatro linhas depois de `antigo:` viram as seis depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: revisor sair com `--desde`. O `.claude/estado/tarefa-corrente.json` se grava só no despacho do executor, e o hook `SubagentStop` só grava a linha do `pantonic-executor`; a rodada de outro papel gravada sob o id da tarefa (caso medido, 2026-09-26: a do revisor da `TK-88a`) sai da série por card corretivo que a cita. novo: revisor sair com `--desde`. O `.claude/estado/tarefa-corrente.json` se grava só no despacho do executor e vale até o despacho seguinte; o hook `SubagentStop` grava a rodada de todo papel `pantonic-*`, com o papel no identificador da tarefa: `<ID>` do executor, `<ID>-revisao` do revisor, `<ID>-consultor-<n>` do consultor, `<P-n>-planejador`, `<P-n>-modelador` e `<P-n>-scout` pelo primeiro id de plano da primeira mensagem do subagente, e `sem-id-<papel>` quando não há id a derivar. ``` 6. Em `.claude/skills/scrum-master/SKILL.md`, seção *Acionamento do consultor*, a frase depois de `antigo:` vira a frase depois de `novo:` (sem quebra nova e sem refluxo; os rótulos não entram no arquivo): ```text antigo: A linha de telemetria de cada instância vem do bloco `<usage>` da notificação, como a de qualquer subagente, com a tarefa `<ID>-consultor-<n>`. novo: A linha de telemetria de cada instância é gravada pelo hook `SubagentStop`, com a tarefa `<ID>-consultor-<n>`. ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os testes novos (referência datada: `452 passed`, 2026-09-27); a renomeação do passo 2 não reduz o total. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - O gancho sai sempre 0 e nunca bloqueia; nenhum `print` no gancho.
- **Não fazer:** não mudar `calcular_consumo` nem `montar_args_append` além do modelo e da tarefa; não editar `.claude/settings.json` nem `.claude/projecoes.json` (o gancho já está registrado em `SubagentStop`); não reescrever linhas antigas de `docs/telemetria.tsv`.
- **Contingências:** - se um teste existente de `tests/test_telemetria_hook.py` ou de `tests/test_encerrar.py` cair, fora dos três que o passo 2 altera → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_hook_grava_revisor_com_papel` (passo 2) — payload `pantonic-reviewer` com estado de `EXA-T55` e transcript cujo `message.model` é `claude-opus-4`: a série ganha a linha com tarefa `EXA-T55-revisao` e modelo `opus`, e o estado continua no disco (a regra de hoje não grava). TF `test_tf_hook_grava_consultor_numerado_por_papel` — série que já tem `EXA-T55-consultor-1`: o consultor grava `EXA-T55-consultor-2`. TF `test_tf_hook_grava_planejador_pelo_id_do_plano_papel` — transcript cuja primeira mensagem de usuário cita `docs/plans/P-0753-auditoria-estagio-1/plano.md`: tarefa `P-0753-planejador`. TR `test_tr_hook_sem_id_derivavel_grava_sem_id_papel` — `pantonic-scout` sem `P-<n>` na primeira mensagem: tarefa `sem-id-scout`. TF `test_tf_consumo_por_papel_separa_planejador_modelador_scout` (em `tests/test_encerrar.py`) — série com `P-0001-planejador` e `P-0001-scout`: a tabela de consumo da entrega traz as linhas `| planejador | 1 |` e `| scout | 1 |` (a regra de hoje as somaria em `outros`).
- **Fora do escopo desta tarefa:** a primeira linha do revisor (`AF-T6`); o arquivo `tarefa-corrente.json` gravado por comando (`AF-T10`); a revisão do `README.md` (`AF-T18`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** processar em .claude/tools/telemetria_hook.py:294 grava a rodada de todo pantonic-* com o papel no id (<ID>, <ID>-revisao, <ID>-consultor-<n>, <P-n>-planejador/-modelador/-scout, sem-id-<papel>) e nao apaga mais tarefa-corrente.json; _consumo_do_plano (.claude/tools/encerrar.py:676) separa planejador, modelador e scout; GOVERNANCA.md §4.2 e scrum-master (Acionamento do consultor) atualizados - **Contrato:** a serie docs/telemetria.tsv recebe a linha de revisor, consultor e demais papeis pelo hook SubagentStop, sem --tool-uses do condutor; tarefa-corrente.json vale ate o proximo despacho do executor - **Não refazer:** a gravacao por papel no hook; os grupos novos da soma do plano - **Pendente:** nenhum

## Execução

**Consumo:** 39 tool uses, 128.7 k tokens, 645.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O efeito do reparo DAF-37, que o cenario registrava como deduzido e nao rodado, esta agora medido: test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia passa com o estado preservado nos dois mundos, e o poder discriminante do teste continua no TSV (revertido no mundo hostil nao cria a serie). Suite 466 passed = piso 462 + 4 testes novos (a renomeacao do revisor nao somou nem tirou). Exercicio ponta a ponta do modulo (gancho -> serie -> encerrar._consumo_do_plano), numa arvore temporaria: executor sem estado e agent_type vazio ou fora de pantonic- ficam em silencio; revisor e consultor sem estado gravam sem-id-revisao/sem-id-consultor; consultor numera 1 e 2 pela serie; model-designer com conteudo em lista de blocos text grava P-0753-modelador/opus; papel nao nomeado grava P-<n>-<nome>; o estado sobrevive; o agregado do plano P-0753 separa executor 1, revisor 1, consultor 2, planejador 1, modelador 1. Linhas sem-id-* nao pertencem a plano nenhum pela regra de pertenca que o card manteve: a soma do plano conta tudo o que o id permite atribuir, nao a rodada sem id. A primeira execucao (blocked por premissa, teste fora dos tres do passo 2) custou uma rodada inteira de executor e uma de consultor a um defeito de autoria do card.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai marcar a tarefa "O gancho de telemetria grava todo papel do kit, e a soma do plano os separa" como blocked, sem RDO.
Scrum master vai fechar a tarefa "O gancho de telemetria grava todo papel do kit, e a soma do plano os separa" como done: registrar estado, RDO e telemetria.
