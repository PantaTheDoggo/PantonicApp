# RDO — P-0755 · RAF-T30a

# Humano

Tarefa "O laudo aceita o alvo instrumento que o aviso do fechamento lê" concluída em 2026-09-29.
O laudo do revisor passou a aceitar o achado de instrumento, e ele chega ao aviso do fechamento.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 49/59 tarefas concluídas; próxima: "A série de telemetria atribui pela linha de abertura do despacho e guarda uma linha por agente".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T30a` — O laudo aceita o alvo instrumento que o aviso do fechamento lê
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o gerador do laudo aceitar o quinto alvo de achado de processo, `instrumento`, com a rubrica e o revisor nomeando-o, para que o aviso `B1` do fechamento tenha o achado que lê.

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `tests/test_rdo.py` - `docs/RUBRICA_DE_REVISAO.md` - `.claude/agents/pantonic-reviewer.md`

**Verificação:** 1. `python -m pytest tests/test_rdo.py -q -k alvo_instrumento` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -c "from pathlib import Path;b=chr(96);r=Path('.claude/tools/rdo.py').read_text(encoding='utf-8');u=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');v=Path('.claude/agents/pantonic-reviewer.md').read_text(encoding='utf-8');print('alvos=%d-%d-%d rdo=%d-%d-%d'%(r.count('quatro alvos')+u.count('quatro alvos')+v.count('quatro alvos'),u.count('| '+b+'instrumento'+b+' |'),v.count(b+'modelo'+b+', '+b+'instrumento'+b),r.count('ou '+b+'instrumento'+b),r.count('ou instrumento, seguido'),r.count('cinco alvos')))"` → `alvos=0-1-1 rdo=1-1-1` — antes `alvos=3-0-0 rdo=0-0-0`, depois `alvos=0-1-1 rdo=1-1-1`

**Pronto quando:** - fechamento.aviso de falha de instrumento — o fechamento avisa, numa linha própria, cada achado de instrumento que relata queda ou erro — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-68`; `AE-186` (laudo da `RAF-T30`, reprovado 74, achado de processo de alvo `dossiê`); `DRF-22`; relatório `R-20`.
- **Depende de:** `RAF-T30`
- **Operação do modelo:** `OP-30` - OP-30: Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento. - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit `.claude/tools/rdo.py`, verbo `laudo` (`_ALVOS_ACHADO`, o docstring de `_formatar_achados_processo`, o docstring do módulo e o `help` de `--achado-processo`), e a doutrina que conta o vocabulário dos alvos: `docs/RUBRICA_DE_REVISAO.md` §6 e `.claude/agents/pantonic-reviewer.md`; só biblioteca padrão. A `RAF-T30` fez o `encerrar.py tarefa` avisar o achado de alvo `instrumento` (`_ACHADO_INSTRUMENTO_RE` sobre o texto `achado de processo (instrumento): …` que `achados_do_laudo` monta da célula `alvo` do laudo), mas o gerador recusa esse alvo (`rdo: FALHOU - alvo instrumento fora de [...]`, exit 1) e nenhum laudo real escreve a linha. O `encerrar.py` não muda: a célula `instrumento` já casa o aviso. Ficam como atribuição datada os docstrings de `test_tr_laudo_recusa_alvo_fora_dos_tres_e_linha_com_pipe` (`BKL-T2d`) e de `test_tf_laudo_aceita_alvo_modelo` (`MC-T2`), e o arquivo `.claude/estado/dossie-AF-T4.md`.
- **Contratos/classes:** `_ALVOS_ACHADO` ganha a chave `"instrumento"` com o rótulo `"instrumento"`; `_formatar_achados_processo`, `cmd_laudo` e o parser do verbo `laudo` — assinaturas inalteradas. A recusa de alvo fora do vocabulário continua como está (a mensagem lista o vocabulário por `sorted(_ALVOS_ACHADO)`).
- **Passos:** 1. Acrescentar ao fim de `tests/test_rdo.py`, depois da última linha que já existe (hoje `    assert "| dossiê | linha do achado |" in conteudo`, que fica onde está e como está), o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card; as duas linhas em branco do começo separam o bloco da função anterior). ```python # --- laudo · achado de processo, alvo instrumento (RAF-T30a do P-0755, `DRF-68`) -------------- def test_tf_laudo_alvo_instrumento_chega_ao_aviso_b1_do_fechamento(tmp_path): """TF (RAF-T30a, `DRF-68`): `--achado-processo instrumento "<linha>"` sai 0, o laudo tem a linha `| instrumento | <linha> |`, e o `achados_do_laudo` do `encerrar.py` a devolve como o achado que o aviso `B1` da `RAF-T30` casa — o caminho do gerador ao fechamento, que o card da `RAF-T30` montava à mão. Hoje o alvo é recusado (exit 1) e nenhum laudo o escreve.""" rdo = _load_rdo() laudos_dir = tmp_path / "laudos" linha = "o card_check caiu com Traceback no item 2. Rota: tíquete" exit_code = rdo.main(_argv_laudo(laudos_dir) + ["--achado-processo", "instrumento", linha]) assert exit_code == 0 conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8") assert f"| instrumento | {linha} |" in conteudo spec = importlib.util.spec_from_file_location( "encerrar_do_rdo", _ROOT / ".claude" / "tools" / "encerrar.py" ) encerrar = importlib.util.module_from_spec(spec) sys.modules[spec.name] = encerrar spec.loader.exec_module(encerrar) textos = [texto for texto, _rota in encerrar.achados_do_laudo(conteudo)] assert textos == ["achado de processo (instrumento): o card_check caiu com Traceback no item 2."] assert encerrar._ACHADO_INSTRUMENTO_RE.search(textos[0]) ``` 2. Rodar `python -m pytest tests/test_rdo.py -q -k alvo_instrumento` e conferir que o TF falha (`exit 1`). 3. Em `.claude/tools/rdo.py`, trocar a linha antiga 3 pelas seis linhas novas 3 (as quebras são as do bloco; cada linha perde o recuo deste card). Linha antiga 3: ```text _ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo"} ``` Linhas novas 3: ```text # O quinto alvo, `instrumento`, é o que o aviso `B1` do `encerrar.py tarefa` lê (RAF-T30a, `DRF-68` # do P-0755). _ALVOS_ACHADO = { "dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica", "modelo": "modelo", "instrumento": "instrumento", } ``` 4. Ainda em `.claude/tools/rdo.py`, três trocas de texto, cada uma na mesma linha, sem refluxo: no docstring do módulo, `` `doutrina`, `rubrica` ou `modelo`) grava a seção `` por `` `doutrina`, `rubrica`, `modelo` ou `instrumento`) grava a seção ``; no docstring de `_formatar_achados_processo`, `§6: campo próprio, quatro alvos.` por `§6: campo próprio, cinco alvos.`; e, no `help` de `--achado-processo`, as duas linhas do texto antigo 4 pelas duas do texto novo 4 (cada linha perde o recuo deste card e guarda os doze espaços iniciais que tem no arquivo). Texto antigo 4: ```text "Achado de processo (repetivel): ALVO e dossie (ou dossiê), doutrina, rubrica ou modelo, " "seguido de uma linha. Nao altera percentual, veredito, bloqueante nem recomendacao " ``` Texto novo 4: ```text "Achado de processo (repetivel): ALVO e dossie (ou dossiê), doutrina, rubrica, modelo " "ou instrumento, seguido de uma linha. Nao altera percentual, veredito, bloqueante nem recomendacao " ``` 5. Em `docs/RUBRICA_DE_REVISAO.md` §6, trocar `com quatro alvos possíveis:` por `com cinco alvos possíveis:` e acrescentar, logo depois da linha da tabela que começa por `` | `modelo` | ``, a linha nova 5, sem mudar as demais. Linha nova 5: ```text | `instrumento` | instrumento do kit que caiu, devolveu saída errada ou recusou entrada válida na execução ou na revisão; o `encerrar.py tarefa` avisa, na linha `encerrar: B1 —`, o achado deste alvo que relata queda, traceback, exceção ou erro | ``` 6. Em `.claude/agents/pantonic-reviewer.md`, trocar as duas linhas do texto antigo 6 pelas três do texto novo 6 (cada linha perde o recuo deste card; as de continuação guardam os dois espaços iniciais que têm no arquivo). Texto antigo 6: ```text - Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e quatro alvos possíveis — `dossiê`, `doutrina`, `rubrica`, `modelo`. Ele nunca rebaixa dimensão de entrega e sempre sai com rota. ``` Texto novo 6: ```text - Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e cinco alvos possíveis — `dossiê`, `doutrina`, `rubrica`, `modelo`, `instrumento`. Ele nunca rebaixa dimensão de entrega e sempre sai com rota. ``` 7. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o teste novo. `tests/test_rdo.py`, `tests/test_encerrar.py` e `tests/test_doutrina_unidade.py` inteiros passam (medida do consultor, 2026-09-29: `127 passed` nos três juntos, antes do card). - Nenhuma linha que já existia em `tests/test_rdo.py` sai ou muda: o card só acrescenta depois da última linha do arquivo, e a asserção `| dossiê | linha do achado |` continua a última do teste a que pertence (`AE-186`: a `RAF-T30` inseriu antes da última linha e deslocou uma asserção). - Os quatro arquivos-alvo seguem LF (hoje 0 CR em cada um). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `.claude/tools/encerrar.py` nem `achados_do_laudo`; não mudar a mensagem de recusa de alvo nem o sinônimo `dossiê`; não mudar os docstrings dos testes que já existem; não mexer em outra seção da rubrica nem em outra linha do revisor.
- **Contingências:** - se um texto antigo de um passo não existir verbatim, uma única vez, no arquivo do passo → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se um teste que já existia em `tests/test_rdo.py`, `tests/test_encerrar.py` ou `tests/test_doutrina_unidade.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_laudo_alvo_instrumento_chega_ao_aviso_b1_do_fechamento` — `rdo.py laudo --achado-processo instrumento "o card_check caiu com Traceback no item 2. Rota: tíquete"` sai 0, o laudo tem a linha `| instrumento | … |`, e `achados_do_laudo` do `encerrar.py` a devolve como `achado de processo (instrumento): o card_check caiu com Traceback no item 2.`, que `_ACHADO_INSTRUMENTO_RE` casa (hoje o gerador sai 1). Suítes `tests/test_rdo.py`, `tests/test_encerrar.py`, `tests/test_doutrina_unidade.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a leitura da linha `B1` pela skill e a entrega do card ao consultor (`RAF-T34`); a comparação de asserções por função no dossiê de evidência (`AE-186` item 3, rota auditoria final).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/rdo.py _ALVOS_ACHADO com o quinto alvo instrumento (docstrings e help acertados); docs/RUBRICA_DE_REVISAO.md §6 com cinco alvos; .claude/agents/pantonic-reviewer.md com os cinco alvos; tests/test_rdo.py com o TF ponta a ponta laudo → aviso B1 - **Contrato:** rdo.py laudo --achado-processo instrumento grava a linha que o aviso B1 do encerrar.py lê - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 30 tool uses, 68.6 k tokens, 269.6 s (fonte: `<usage>` do encerramento)

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

Tarefa "O laudo aceita o alvo instrumento que o aviso do fechamento lê": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O laudo aceita o alvo instrumento que o aviso do fechamento lê" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O laudo aceita o alvo instrumento que o aviso do fechamento lê": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O laudo aceita o alvo instrumento que o aviso do fechamento lê" como done: registrar estado, RDO e telemetria.
