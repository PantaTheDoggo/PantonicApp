# RDO — P-0755 · RAF-T5

# Humano

Tarefa "O gatilho do próximo passo responde só ao dono" concluída em 2026-09-28.
O gatilho do próximo passo passa a responder só à mensagem do dono, sem reagir a relato de subagente nem a aviso do sistema.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 8/43 tarefas concluídas; próxima: "O filtro do pytest devolve o exit dos testes no comando encadeado".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T5` — O gatilho do próximo passo responde só ao dono
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o gatilho do próximo passo responder só à mensagem do dono, sem reagir ao relato de subagente nem ao aviso do sistema.

**Arquivos-alvo:** - `.claude/tools/backlog_hook.py` - `tests/test_backlog_hook.py`

**Verificação:** 1. `python -m pytest tests/test_backlog_hook.py -q` → `exit 0` — antes `exit 4`, depois `exit 0`

**Pronto quando:** - gatilho do próximo passo.mensagens que o disparam — só a mensagem do dono dispara; o relato de subagente e o aviso do sistema não injetam nada — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-9`; `F-11` (o gatilho casou em relato de subagente e injetou 15,3 KB três vezes); relatório `R-15` (que também fecha a causa da `R-29`, `DRF-3`).
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-5` - OP-5: Quem executa faz o gatilho do próximo passo responder só à mensagem do dono, sem reagir ao relato de subagente nem ao aviso do sistema. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit — o hook `UserPromptSubmit` `.claude/tools/backlog_hook.py`, só biblioteca padrão; a mudança é só na decisão de disparar; a saída quando dispara (`additionalContext` com a saída de `next`) não muda. Os testes novos moram em arquivo próprio, `tests/test_backlog_hook.py`, fora da série de `tests/test_backlog.py` (que é de `backlog.py`, `DRF-9`).
- **Contratos/classes:** `processar(payload: dict, repo: Path | None = None, backlog_module=None) -> dict | None` — assinatura inalterada. Regra nova em `_casa_gatilho(prompt) -> bool`: devolve verdadeiro só quando `prompt` é `str`, o prompt depois de `lstrip()` **não** começa por `<agent-message` nem por `[SYSTEM NOTIFICATION` (prefixos exatos, com distinção de caixa, numa tupla de módulo) e a frase `proximo passo` está em `_norm(prompt)` como hoje. Prompt fora do dono → `processar` devolve `None`, sem carregar `backlog.py`.
- **Passos:** 1. Criar `tests/test_backlog_hook.py` com os três testes da seção `Testes`, carregando o hook por `importlib.util.spec_from_file_location` a partir de `.claude/tools/backlog_hook.py` e passando a `processar` `repo=tmp_path` e um `backlog_module` falso cujo `carregar(repo)` levanta `RuntimeError("backlog falso")`. 2. Rodar `python -m pytest tests/test_backlog_hook.py -q` e conferir que os dois TF falham. 3. Aplicar a regra de `Contratos/classes` em `_casa_gatilho`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A); os testes do hook que já moram em `tests/test_backlog.py` (`test_tf_hook_*`) seguem verdes. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Os testes não leem o repositório real: o `backlog_module` é falso e `repo` é `tmp_path`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mover para `tests/test_backlog_hook.py` os testes do hook que já existem em `tests/test_backlog.py`; não mudar `_GATILHO` nem `_norm`; não mudar `.claude/projecoes.json` (o registro do hook não muda).
- **Contingências:** - se um teste `test_tf_hook_*` de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_relato_de_subagente_com_proximo_passo_nao_injeta` — prompt `<agent-message from="pantonic-planner">Próximo passo de quem conduz: despachar.</agent-message>`: `processar` devolve `None` (hoje devolve o dicionário com o contexto da falha do backlog falso). TF `test_tf_aviso_do_sistema_com_proximo_passo_nao_injeta` — prompt com dois espaços iniciais, `  [SYSTEM NOTIFICATION] tarefa concluída; próximo passo do loop.`: devolve `None` (hoje, o dicionário). TR `test_tr_mensagem_do_dono_com_proximo_passo_segue_injetando` — prompt `execute o próximo passo`: devolve o dicionário com `hookEventName` `UserPromptSubmit` e `additionalContext` exatamente `backlog_hook: falha ao rodar next: backlog falso`. Suíte `tests/test_backlog_hook.py`, `tests/test_backlog.py -k hook` e a suíte inteira.
- **Fora do escopo desta tarefa:** o `next` limitado ao plano corrente (`R-29`, registrada sem ação, `DRF-3`); o hook do pytest (`RAF-T6`).
- **Handover:** 2026-09-28 · para quem vier depois - **Entregue:** _casa_gatilho em .claude/tools/backlog_hook.py só casa prompt do dono: recusa relato de subagente (<agent-message) e aviso do sistema; 3 testes novos em tests/test_backlog_hook.py, suíte 536 - **Contrato:** processar() com assinatura inalterada; o gatilho do próximo passo não injeta o dossiê em relato de subagente - **Não refazer:** a regra nova de _casa_gatilho e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 18 tool uses, 58.2 k tokens, 170.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta na revisao: a versao do ref (9f93ad4) injeta nos seis prompts com a frase; a entregue injeta so no do dono e nos que nao comecam pelos prefixos exatos (caixa distinta e prefixo no meio seguem disparando, como o contrato fixa); main por stdin sai 0 com stdout vazio para relato de subagente, aviso do sistema, payload vazio, lista e JSON invalido. A parte do contrato 'sem carregar backlog.py' e garantida pelo codigo (retorno antes de _carregar_backlog) mas nao e discriminada pelos testes, que injetam o backlog falso.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar" e vai pegar a tarefa "O gatilho do próximo passo responde só ao dono".
Tarefa "O gatilho do próximo passo responde só ao dono". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O gatilho do próximo passo responde só ao dono" e vai executar: Quem executa faz o gatilho do próximo passo responder só à mensagem do dono, sem reagir ao relato de subagente nem ao aviso do sistema.
Agente executor devolveu a tarefa "O gatilho do próximo passo responde só ao dono": review — sem pendência.
Tarefa "O gatilho do próximo passo responde só ao dono": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O gatilho do próximo passo responde só ao dono" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O gatilho do próximo passo responde só ao dono": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O gatilho do próximo passo responde só ao dono" como done: registrar estado, RDO e telemetria.
