# RDO — P-0755 · RAF-T20

# Humano

Tarefa "O despacho pede à conferência do modelo só a versão vigente" concluída em 2026-09-29.
O despacho passa a pedir à conferência do modelo só a versão vigente.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 32/52 tarefas concluídas; próxima: "A conferência do modelo recusa o card que copia a operação com outro texto".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T20` — O despacho pede à conferência do modelo só a versão vigente
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o despacho de tarefa pedir à conferência do modelo só o julgamento da versão vigente.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q -k versao_vigente` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - despacho de tarefa.versão do modelo julgada — o despacho julga só a versão vigente; a pendente fica para o marco — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-1`, `DRF-14`; `F-9` (o `despachar` roda `modelo.py check` por subprocesso e aceita exit 0 ou 2), `F-19` (emenda que cria operação sem card recusa o despacho por construção); relatório `R-04` (auditoria reg. 31 e 32: o ato do dono do plano fictício travou o despacho da tarefa seguinte).
- **Depende de:** `RAF-T19`
- **Operação do modelo:** `OP-20` - OP-20: Quem executa faz o despacho de tarefa pedir à conferência do modelo só o julgamento da versão vigente. - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/backlog.py`, função `despachar`; só biblioteca padrão. O `modelo.py` roda como subprocesso do irmão (`irmao / "modelo.py"`), nunca por `import`, e carrega o `backlog.py` da raiz dada por `--root`. A opção `--so-vigente` do `modelo.py check` existe desde a `RAF-T19`: julga só a `## 1`, não acrescenta as violações `1A: ` e não acusa `V4` do card cuja operação só existe na `## 1A`. O contrato do objeto é: "Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor."
- **Contratos/classes:** `despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus` — assinatura inalterada. Uma regra: a lista de argumentos do `subprocess.run` do `modelo.py check` (a que hoje é `[sys.executable, str(irmao / "modelo.py"), "check", "--plano", plano_abs, "--root", str(repo)]`) ganha `"--so-vigente"` depois de `str(repo)`, com o comentário `` # `R-04` (`DRF-14` do `P-0755`): o despacho julga só a `## 1`; a `## 1A` fica para o marco. `` na linha de cima. O teste do exit (0 ou 2 seguem, outro recusa com `despachar: recusado — modelo: <última linha do stderr>`) não muda.
- **Passos:** 1. Acrescentar ao fim de `tests/test_backlog.py`, nesta ordem: o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0); o helper `_montar_repo_despachar_com_pendente(tmp_path: Path, operacao_gam_t2: str) -> Path`, que chama `_montar_repo_despachar(tmp_path)`, copia `.claude/tools/backlog.py` do repositório (`_ROOT`) para `.claude/tools/` da cópia (o `modelo.py check` carrega o `backlog.py` da raiz dada), grava em `docs/plans/P-0-gama/plano.md` da cópia o `_GAM_PLANO_COM_PENDENTE_TEXTO` com `@OPERACAO_GAM_T2@` trocado por `operacao_gam_t2`, roda `_run_git_despachar(["add", "-A"], repo)` e `_run_git_despachar(["commit", "-m", "plano com versão pendente"], repo)` e devolve a cópia; e os dois testes da seção `Testes`. ```python _GAM_PLANO_COM_PENDENTE_TEXTO = """# P-0 — Plano gama **Prefixo das tarefas no diário:** `GAM-T<n>` ## 1. Modelo conceitual **Estado do modelo:** versão 1 · 2026-01-01 · autor: modelador · 1 operações · 2 propriedades · situação: vigente ### 1.1 Objetos | objeto | o que é | propriedades | contrato | origem | lastro | |---|---|---|---|---|---| | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture | | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture | ### 1.2 Fluxo de operações - **OP-1** — Primeira operação da fixture. - `precisa de: insumo` · `altera: produto.status` · `tarefas: GAM-T1, GAM-T2` ### 1.3 Estado inicial e estado final | propriedade | estado inicial | estado final | |---|---|---| | insumo.status | lido | lido | | produto.status | rascunho | validado | ### 1.4 Registro de versões | versão | data | situação | por | |---|---|---|---| | 1 | 2026-01-01 | vigente | modelador | | 2 | 2026-01-02 | pendente | modelador, emenda | ## 1A. Modelo conceitual — versão pendente de validação **Estado do modelo:** versão 2 · 2026-01-02 · autor: modelador · 2 operações · 3 propriedades · situação: pendente ### 1.1 Objetos | objeto | o que é | propriedades | contrato | origem | lastro | |---|---|---|---|---|---| | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture | | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture | | resultado | o produto da segunda operação | nível | um relatório derivado | OP-2 | lastro da fixture | ### 1.2 Fluxo de operações - **OP-1** — Primeira operação da fixture. - `precisa de: insumo` · `altera: produto.status` · `tarefas: GAM-T1, GAM-T2` - **OP-2** — Segunda operação, nova na versão pendente. - `precisa de: produto` · `altera: resultado.nível` · `tarefas: ` ### 1.3 Estado inicial e estado final | propriedade | estado inicial | estado final | |---|---|---| | insumo.status | lido | lido | | produto.status | rascunho | validado | | resultado.nível | inicial | alto | ## 5. Tarefas ### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao] - **Objetivo:** fixture. - **Operação do modelo:** `OP-1` - OP-1: Primeira operação da fixture. - precisa de: insumo — um registro por rodada - **Entregável:** nenhum — fixture sintética, não é card vivo de plano. - **Verificação:** 1. `python -c "print('a')"` → `b` — antes `a`, depois `b` - **Pronto quando:** fixture existe. ### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao] - **Objetivo:** fixture. @OPERACAO_GAM_T2@- **Entregável:** nenhum — fixture sintética, não é card vivo de plano. - **Verificação:** 1. `python -c "print('a')"` → `b` — antes `a`, depois `b` - **Pronto quando:** fixture existe. """ _OPERACAO_GAM_T2 = """- **Operação do modelo:** `OP-1` - OP-1: Primeira operação da fixture. - precisa de: insumo — um registro por rodada """ ``` 2. Rodar `python -m pytest tests/test_backlog.py -q -k versao_vigente` e conferir que o TF falha (`despachar: recusado — modelo:`) e o TR passa. 3. Aplicar a regra de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_backlog.py` sai ou muda: o card só acrescenta ao fim do arquivo; a fixture `tests/fixtures/backlog/pasta/` não muda (só a cópia em `tmp_path`). - Os testes gravam só em `tmp_path`; o `git` roda só no repositório da cópia. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/tools/modelo.py` (a flag é da `RAF-T19`); não mudar o gate do modelo de `encerrar.py` (o fechamento roda o `check` completo, que desde a `RAF-T19` não acusa `V4` do card da operação nova); não mudar a ordem dos gates do `despachar` nem o que ele imprime ou grava.
- **Contingências:** - se um teste que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se `python .claude/tools/modelo.py check --help` não listar `--so-vigente` → parar e sinalizar `blocked` razão `dependencia`, nomeando a `RAF-T19`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_despachar_versao_vigente_segue_com_pendente_incompleta` — plano gama com a `## 1A` cuja `OP-2` não tem card e o `GAM-T2` com o campo: `despachar GAM-T1` sai 0, sem `despachar: recusado` no stderr (hoje sai 1 com `despachar: recusado — modelo: modelo: FALHOU — 1 violação(ões)`, pela `1A: V1 OP-2 — operação sem tarefa`). TR `test_tr_despachar_versao_vigente_recusa_defeito_da_vigente` — o mesmo plano com `operacao_gam_t2` vazio (o `GAM-T2` sem `Operação do modelo`, `V2` da `## 1`): sai 1 com `despachar: recusado — modelo:` no stderr (a regra concorrente, tirar o gate do modelo, sairia 0). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o `--so-vigente` do `modelo.py` (`RAF-T19`); a doutrina da rota do modelador com operação nova (`RAF-T24`); o card da operação nova (`RAF-T25`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** backlog.py despachar chama modelo.py check --so-vigente (a ## 1A fica para o marco); 2 testes novos, suíte 590 - **Contrato:** versão pendente incompleta não trava o despacho; defeito da vigente continua recusando - **Não refazer:** a flag no despachar e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 30 tool uses, 78.7 k tokens, 356.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Discriminacao conferida em copia descartavel: sem o --so-vigente em despachar, o TF cai com 'despachar: recusado - modelo: modelo: FALHOU - 1 violacao(oes)' e o TR segue verde; com a flag, 2 passed. O check completo segue so no fechamento (encerrar.py:325), coerente com o card.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência" e vai pegar a tarefa "O despacho pede à conferência do modelo só a versão vigente".
Tarefa "O despacho pede à conferência do modelo só a versão vigente". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O despacho pede à conferência do modelo só a versão vigente" e vai executar: Quem executa faz o despacho de tarefa pedir à conferência do modelo só o julgamento da versão vigente.
Agente executor devolveu a tarefa "O despacho pede à conferência do modelo só a versão vigente": review — sem pendência.
Tarefa "O despacho pede à conferência do modelo só a versão vigente": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O despacho pede à conferência do modelo só a versão vigente" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O despacho pede à conferência do modelo só a versão vigente": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O despacho pede à conferência do modelo só a versão vigente" como done: registrar estado, RDO e telemetria.
