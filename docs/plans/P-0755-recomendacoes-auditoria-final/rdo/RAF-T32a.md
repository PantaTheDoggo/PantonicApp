# RDO — P-0755 · RAF-T32a

# Humano

Tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back" concluída em 2026-09-29.
O painel do gerente passou a mostrar a tarefa despachada também quando o agente devolve por hand-back.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 54/62 tarefas concluídas; próxima: "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T32a` — O painel do gerente mostra a tarefa despachada também no retorno por hand-back
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a frase de volta do subagente que devolve por hand-back nomear a tarefa que a linha de abertura do despacho declarou, como já fazem a frase de despacho e a de volta síncrona.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py` - `tests/test_progresso_hook.py`

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q -k retorno_do_despacho` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - painel do gerente.tarefa mostrada — a frase de volta do hand-back mostra a tarefa que a linha de abertura do despacho declara — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-72`; `AE-193` (laudo da `RAF-T32`, ressalva 91, achado 2); `DRF-71`; `DRF-18`; relatório `R-16`.
- **Depende de:** `RAF-T32`
- **Operação do modelo:** `OP-32` - OP-32: Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop. - precisa de: série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/progresso_hook.py`, função `evento`: o ramo `PostToolUse` · `Agent` com `handback` `send` (hoje só grava `pendentes[agentId] = sub`, linha 495) e o ramo `UserPromptSubmit` com `<agent-message from="…">` (a atribuição `_, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)` da linha 516). A `RAF-T32` levou a linha de abertura ao `PreToolUse` e ao `PostToolUse` síncrono e excluiu o `UserPromptSubmit`, onde mora a frase de volta do hand-back — o caminho real quando o subagente devolve por `SubagentHandback`: hoje o painel diz `Agente consultor recebe a tarefa "Outro título"` e, na volta, `Agente consultor devolveu a tarefa "Um título de teste"` (medido). O ID sem card segue mostrando o ID (`DRF-72`): não muda. O estado do loop (`tarefa`, `titulo`, `objetivo`, `pendentes`) não muda pela linha. As frases `M-3`..`M-16` não mudam de texto. O contrato do objeto é: "Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente."
- **Contratos/classes:** duas regras em `evento`, sem função nova: 1. Ramo `PostToolUse` · `Agent` com `handback` `send`: depois de `pendentes[agentId] = sub` (que fica como está), quando `tarefa_do_despacho(str(ti.get("prompt", "")), raiz)` devolve o trio, grava o título dele em `estado_loop["titulos_pendentes"][agentId]` (chave nova, criada com `setdefault`); sem a linha, não grava nada. O valor de `pendentes` segue string (os testes de hoje comparam `pendentes` inteiro). 2. Ramo `UserPromptSubmit` com `<agent-message from="<agentId>">`: tira `titulos_pendentes[agentId]` junto com `pendentes[agentId]` (os dois `pop`, sempre, antes do teste do papel); o título da frase de volta é o tirado de `titulos_pendentes` e, sem ele, o de `tarefa_corrente(estado_loop, estado, raiz)`, como hoje.
- **Passos:** 1. Acrescentar ao fim de `tests/test_progresso_hook.py`, depois da última linha de hoje (o `)` que fecha o último `assert` de `test_tr_tarefa_do_despacho_ausente_segue_a_corrente`), o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card). ```python def _devolver_agente(estado, raiz, sub, prompt, resposta, agent_id=None): if agent_id is None: r = {"content": [{"type": "text", "text": resposta}]} else: r = {"status": "completed", "agentId": agent_id, "handback": "send", "content": [{"type": "text", "text": "ptr"}]} rodar(P(hook_event_name="PostToolUse", tool_name="Agent", tool_input={"subagent_type": sub, "prompt": prompt}, tool_response=r), estado, raiz) if agent_id is not None: rodar(P(hook_event_name="UserPromptSubmit", prompt=( f'<agent-message from="{agent_id}">\n' "[Subagent hand-back] The text below is the final report of a subagent this " "session delegated to. The report follows:\n" f"  {resposta}\n" "</agent-message>" )), estado, raiz) return progresso(estado)[-1] def test_tf_retorno_do_despacho_assincrono_mostra_a_tarefa_despachada(estado, raiz): rodar(payload_next( "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n" "- **Objetivo:** Fazer x.\n" ), estado, raiz) ultima = _devolver_agente( estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x", "rota=resolve", agent_id="c9", ) assert ultima == 'Agente consultor devolveu a tarefa "Outro título": rota resolve.' estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8")) assert estado_loop["tarefa"] == "TLG-T9" assert estado_loop["pendentes"] == {} assert estado_loop.get("titulos_pendentes", {}) == {} def test_tr_retorno_do_despacho_sincrono_mostra_a_tarefa_despachada(estado, raiz): rodar(payload_next( "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n" "- **Objetivo:** Fazer x.\n" ), estado, raiz) assert _devolver_agente( estado, raiz, "pantonic-consultant", "despacho: P-9999 TLG-T10\ncenario=x", "rota=resolve", ) == 'Agente consultor devolveu a tarefa "Outro título": rota resolve.' assert _devolver_agente( estado, raiz, "pantonic-consultant", "cenario=x", "rota=resolve", ) == 'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.' ``` 2. Rodar `python -m pytest tests/test_progresso_hook.py -q -k retorno_do_despacho` e conferir `1 failed, 1 passed`: o TF falha (a volta diz "Um título de teste") e o TR passa (o ramo síncrono já lê a linha, `RAF-T32`). 3. Aplicar as duas regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `tests/test_progresso_hook.py` com `47 passed`, 2026-09-29). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_progresso_hook.py` sai ou muda: o card só acrescenta ao fim do arquivo. Os dois arquivos seguem LF (hoje 0 CR). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não importar o `telemetria_hook.py`; não gravar a tarefa da linha em `estado_loop["tarefa"]`, `titulo` ou `objetivo`; não mudar a forma do valor de `pendentes`; não mudar `tarefa_do_despacho`, `tarefa_corrente` nem `localizar_card`; não mudar o texto de nenhuma frase do repertório nem a tabela da skill `scrum-master`.
- **Contingências:** - se um teste que já existia em `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_retorno_do_despacho_assincrono_mostra_a_tarefa_despachada` — com a `TLG-T9` como corrente, o consultor despachado com `despacho: P-9999 TLG-T10` devolve por hand-back `rota=resolve`: a última linha do painel é `Agente consultor devolveu a tarefa "Outro título": rota resolve.`, o estado segue com `tarefa` `TLG-T9` e sem pendência (hoje a volta diz "Um título de teste"). TR `test_tr_retorno_do_despacho_sincrono_mostra_a_tarefa_despachada` — a volta síncrona com a linha diz "Outro título" e sem ela "Um título de teste" (cobre o ramo que a `RAF-T32` mudou sem teste). Suíte `tests/test_progresso_hook.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T32` (`done`), que fica como executado; o ID sem card na linha (`DRF-72`); a regra da linha de abertura (`RAF-T33`) e o despacho do consultor com ela (`RAF-T34`); o vermelho do `dead_code` pela sonda (`AE-192`, `DRF-44`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/progresso_hook.py: PostToolUse · Agent com hand-back grava titulos_pendentes[agentId] e o UserPromptSubmit <agent-message> usa esse título; tests/test_progresso_hook.py com TF assíncrono e TR síncrono - **Contrato:** pendentes segue string; sem título guardado, recorre a tarefa_corrente - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 21 tool uses, 67.2 k tokens, 227.2 s (fonte: `<usage>` do encerramento)

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

Agente executor recebe a tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back" e vai executar: Quem executa faz a frase de volta do subagente que devolve por hand-back nomear a tarefa que a linha de abertura do despacho declarou, como já fazem a frase de despacho e a de volta síncrona.
Agente executor devolveu a tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back": review — sem pendência.
Tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O painel do gerente mostra a tarefa despachada também no retorno por hand-back" como done: registrar estado, RDO e telemetria.
