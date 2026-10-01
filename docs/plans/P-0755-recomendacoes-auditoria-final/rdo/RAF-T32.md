# RDO — P-0755 · RAF-T32

# Humano

Tarefa "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara" concluída em 2026-09-29.
O painel do gerente passou a mostrar a tarefa que a linha de abertura do despacho declara.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 53/61 tarefas concluídas; próxima: "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T32` — O painel do gerente mostra a tarefa que a linha de abertura do despacho declara
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py` - `tests/test_progresso_hook.py`

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q -k tarefa_do_despacho` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - painel do gerente.tarefa mostrada — mostra a tarefa que a linha de abertura do despacho declara — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-18`; `F-26` (`tarefa_corrente` usa o cache do loop e, sem ele, `tarefa-corrente.json` e `localizar_card`; o consultor e o painel ficaram com a tarefa corrente em vez da despachada); relatório `R-16` (auditoria reg. 54).
- **Depende de:** `RAF-T31`
- **Operação do modelo:** `OP-32` - OP-32: Quem executa faz o painel do gerente mostrar a tarefa que a abertura do despacho declara, e não a tarefa corrente do loop. - precisa de: série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/progresso_hook.py`, os ramos `PreToolUse` e `PostToolUse` da ferramenta `Agent` em `evento` (a função que trata os eventos do hook, linhas 334-497; o arquivo não define `processar`, que é de `backlog_hook.py` e `telemetria_hook.py`, `DRF-71`); só biblioteca padrão; o hook não importa o `telemetria_hook.py` (a gramática da linha é a mesma da `RAF-T31`, repetida com comentário que diz isso). O estado do loop (`estado_loop["tarefa"]`) não muda pela linha: ela só escolhe o título mostrado. As frases `M-3`..`M-16` não mudam de texto. O contrato do objeto é: "Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente."
- **Contratos/classes:** função nova `tarefa_do_despacho(prompt: str, raiz: Path) -> tuple[str, str, str] | None`, logo antes de `tarefa_corrente`. Três regras: 1. Constante nova `_RE_LINHA_DESPACHO`, multilinha, que casa a linha inteira `despacho: P-<dígitos> <ID>` — `ID` = tarefa (maiúscula, maiúsculas ou dígitos, `-T`, dígitos, uma minúscula opcional) ou tíquete (`TK-`, dígitos, uma minúscula opcional) —, com espaço opcional no fim; a linha sem `ID` não casa. Comentário cita `R-16` e `DRF-18` do `P-0755` e diz que a gramática é a do `telemetria_hook.py`, sem import cruzado. 2. `tarefa_do_despacho`: sem casamento no `prompt` → `None`; com ele, `(ID, título, objetivo)` pelo `localizar_card(ID, raiz)` (que devolve título, objetivo e título do plano); não escreve no estado do loop. 3. `evento`: no ramo `PreToolUse` · `Agent` (a atribuição `_, titulo, objetivo = tarefa_corrente(estado_loop, estado, raiz)`, linha 447 medida em 2026-09-29) e no ramo `PostToolUse` · `Agent` que chama `de_volta` (a atribuição `_, titulo, _ = tarefa_corrente(estado_loop, estado, raiz)` do `else`, linha 471; a do ramo `UserPromptSubmit`, linha 486, não muda), o trio `(_, titulo, objetivo)` passa a vir de `tarefa_do_despacho(str(ti.get("prompt", "")), raiz)` e, quando ela devolve `None`, de `tarefa_corrente(estado_loop, estado, raiz)`, como hoje.
- **Passos:** 1. Acrescentar ao fim de `tests/test_progresso_hook.py` o helper `_despachar_agente(estado, raiz, sub, prompt)` (roda o payload `PreToolUse` · `Agent` com `subagent_type` e `prompt` dados, pelo `rodar`, e devolve a última linha de `progresso(estado)`) e os dois testes da seção `Testes`, com as fixtures `estado` e `raiz` do arquivo (o plano `P-9999` tem `TLG-T9` "Um título de teste" e `TLG-T10` "Outro título"). 2. Rodar `python -m pytest tests/test_progresso_hook.py -q -k tarefa_do_despacho` e conferir que o TF falha e o TR passa. 3. Aplicar as três regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_progresso_hook.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não importar o `telemetria_hook.py`; não gravar a tarefa da linha em `estado_loop`; não mudar o texto de nenhuma frase do repertório nem a tabela da skill `scrum-master`; não mexer no ramo `UserPromptSubmit`.
- **Contingências:** - se um teste que já existia em `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_tarefa_do_despacho_no_painel_vence_a_corrente` — com a `TLG-T9` como corrente (payload do `backlog.py next`), o consultor despachado com o prompt `despacho: P-9999 TLG-T10`, quebra, `cenario=x`: a última linha do painel é `Agente consultor recebe a tarefa "Outro título" e vai triar.` e o estado do loop segue com `tarefa` `TLG-T9` (hoje o painel mostra "Um título de teste"). TR `test_tr_tarefa_do_despacho_ausente_segue_a_corrente` — o revisor com o prompt `Revise.` e o planejador com `despacho: P-9999`, quebra, `Planeje.`: as linhas são `Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.` e `Agente planejador recebe a tarefa "Um título de teste" e vai replanejar.` (a regra concorrente, exigir a linha com tarefa, perderia o título). Suíte `tests/test_progresso_hook.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a série de telemetria (`RAF-T31`); a regra da linha de abertura (`RAF-T33`) e o despacho do consultor com ela (`RAF-T34`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/progresso_hook.py:202 tarefa_do_despacho; os ramos PreToolUse e PostToolUse síncrono · Agent de evento tiram a tarefa da linha de abertura do despacho - **Contrato:** o ramo UserPromptSubmit segue com tarefa_corrente - **Não refazer:** nada a declarar - **Pendente:** o retorno assíncrono (hand-back) ainda usa tarefa_corrente; o ramo PostToolUse síncrono sem teste; ID sem card mostra o ID (achado do laudo, ao consultor)

## Execução

**Consumo:** 30 tool uses, 82.6 k tokens, 297.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Os dois testes do card so exercitam o PreToolUse; o defeito de coerencia (recebe uma tarefa, devolve outra no retorno assincrono) so aparece exercitando o ciclo recebe/devolve inteiro do mesmo agente.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master vai marcar a tarefa "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara" como blocked, sem RDO.
Tarefa "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara" como done: registrar estado, RDO e telemetria.
