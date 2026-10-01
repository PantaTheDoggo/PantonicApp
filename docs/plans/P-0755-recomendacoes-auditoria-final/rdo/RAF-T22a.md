# RDO — P-0755 · RAF-T22a

# Humano

Tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto" concluída em 2026-09-30.
A diferença entre versões do modelo passou a mostrar a operação que muda o que precisa ou o que altera sem mudar o texto.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 59/63 tarefas concluídas; próxima: "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T22a` — A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação de mesmo texto cujo `precisa de:` ou `altera:` mudou, que hoje sai do drift sem linha nenhuma.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - `tests/test_modelo.py`

**Verificação:** 1. `python -m pytest tests/test_modelo.py -q -k drift_contrato_da_operacao` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência do modelo.diferença entre versões — casa primeiro pelo texto, mostra operação nova, renumerada e alterada, e lista a propriedade que só uma das versões tem — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-73`; `AE-187` (emenda do modelador da `DRF-68`: na versão 4 pendente, a `OP-30` ganha `rubrica de revisão` em `precisa de:` e a propriedade nova em `altera:`, e o `show --drift` não mostra nada disso, medido 2026-09-30); `DRF-16`; relatório `R-07`.
- **Depende de:** `RAF-T36`
- **Operação do modelo:** `OP-22` - OP-22: Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem. - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede e mantém o que ela já julga quando chamada como hoje, com uma só mudança: enquanto houver versão pendente, o card que cita uma operação que só ela tem deixa de ser recusado.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, função `_diff_fluxo`, chamada por `montar_drift` (verbo `show --drift`); só biblioteca padrão. A `RAF-T22` escreveu, pelo card, "com par de mesmo texto e mesmo número, nenhuma linha", e o casamento compara só `texto`: a mudança do contrato de uma operação (listas `precisa_de` e `altera` da `Operacao`) fica fora do que o dono lê no marco. O casamento em duas rodadas, as linhas `[+]`, `[=]`, `[~]` de texto e `[-]` de hoje, `_diff_objetos`, `_diff_estado`, o cabeçalho e o `sem drift` não mudam. O docstring do módulo e o `help` de `--drift` dizem só "a diferença entre a versão vigente e a pendente" (medido): não mudam. O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Contratos/classes:** `_diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]`, assinatura inalterada. Uma regra: para todo par (operação da pendente com a da vigente que casou com ela, por texto ou por número), depois da linha de texto que o par já emite hoje (ou de nenhuma), sai `[~] OP-<k> — precisa de: <lista da vigente> => <lista da pendente>` quando as listas `precisa_de` diferem, e depois `[~] OP-<k> — altera: <lista da vigente> => <lista da pendente>` quando as listas `altera` diferem; `<k>` é o número da pendente, cada lista unida por `, ` e a comparação é de lista, exata e na ordem. A lista `tarefas` não entra (é lastro, não modelo). O docstring de `_diff_fluxo` passa a dizer isso e a citar `AE-187` e `DRF-73` do `P-0755`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_modelo.py`, depois da última linha de hoje (`    assert "[-] x.c — baixo" in linhas`, fim de `test_tf_drift_versoes_propriedade_de_uma_versao_so`), o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card). ```python def test_tf_drift_contrato_da_operacao_mostra_precisa_e_altera(): """TF (RAF-T22a, AE-187/DRF-73): `OP-1` tem o mesmo texto e o mesmo número nas duas versões e muda só `precisa de:` e `altera:` — o drift mostra as duas listas; hoje o par de texto igual não emite linha nenhuma e `montar_drift` devolve `sem drift`.""" modelo = _load_modelo() vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[ modelo.Operacao(numero=1, texto="Única.", precisa_de=["a"], altera=["x.a"]), ]) pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[ modelo.Operacao(numero=1, texto="Única.", precisa_de=["a", "b"], altera=["x.a", "x.b"]), ]) linhas = modelo.montar_drift(vigente, pendente).splitlines() assert "[~] OP-1 — precisa de: a => a, b" in linhas assert "[~] OP-1 — altera: x.a => x.a, x.b" in linhas def test_tr_drift_contrato_da_operacao_ignora_tarefas(): """TR (RAF-T22a, DRF-73): `OP-1` muda só `tarefas:`, que é lastro e não modelo — o drift segue `sem drift`; a regra concorrente, comparar todo o sub-bullet, daria uma linha de `tarefas:`.""" modelo = _load_modelo() vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[ modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1"]), ]) pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[ modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1", "EX-T1a"]), ]) assert modelo.montar_drift(vigente, pendente) == "sem drift" ``` 2. Rodar `python -m pytest tests/test_modelo.py -q -k drift_contrato_da_operacao` e conferir `1 failed, 1 passed`: o TF falha (hoje `sem drift`) e o TR passa. 3. Aplicar a regra de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `tests/test_modelo.py` com `46 passed`, 2026-09-30). Os testes de drift que já existem (`test_tf_show_drift_tres_marcadores`, `test_tf_show_drift_sem_diferenca`, `test_tf_drift_mostra_contrato_alterado` e os três `drift_versoes`) continuam passando sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam. A edição não troca a quebra de linha de nenhum dos dois arquivos (hoje `modelo.py` em CRLF, `test_modelo.py` em LF, 0 CR). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não comparar a lista `tarefas`; não mudar o casamento das duas rodadas nem as linhas que ele já emite; não mudar `_diff_objetos`, `_diff_estado`, `montar_drift` nem o verbo `show`; não mexer em `validar`.
- **Contingências:** - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_drift_contrato_da_operacao_mostra_precisa_e_altera` — `OP-1` `Única.` nas duas versões, `precisa de:` `a` → `a, b` e `altera:` `x.a` → `x.a, x.b`: as linhas do drift contêm `[~] OP-1 — precisa de: a => a, b` e `[~] OP-1 — altera: x.a => x.a, x.b` (hoje `sem drift`). TR `test_tr_drift_contrato_da_operacao_ignora_tarefas` — `OP-1` `Única.` muda só `tarefas:`: o drift é `sem drift` (a regra concorrente, comparar todo o sub-bullet, daria linha). Suíte `tests/test_modelo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T22` (`done`), que fica como executado; a mensagem do Marco 5 ao dono, que carrega a mudança da `OP-30` à mão (`AE-187`); o drift do estado inicial (matéria inconclusiva do cenário, desenho do verbo).
- **Handover:** 2026-09-30 · para `RAF-T40` - **Entregue:** .claude/tools/modelo.py, _diff_fluxo: todo par de operações emite [~] OP-<k> — precisa de: <vigente> => <pendente> e [~] OP-<k> — altera: <vigente> => <pendente> quando a lista difere; tests/test_modelo.py com TF e TR novos - **Contrato:** show --drift mostra a mudança de precisa de/altera de operação com o mesmo texto; tarefas: não entra - **Não refazer:** nada a declarar - **Pendente:** lista vazia sai como lado em branco (achado do laudo, sem ação)

## Execução

**Consumo:** 29 tool uses, 73.4 k tokens, 214.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

O exercicio ponta a ponta pelo verbo (show --drift sobre tests/fixtures/modelo/fluxo-pendente.md e fluxo-pendente-contrato.md) mostra que o parser alimenta a regra nova: as duas fixtures agora ganham linha de contrato no Fluxo ([~] OP-1 — altera: ... e [~] OP-3 — precisa de: ...), e os testes de CLI existentes seguem verdes porque aferem so os marcadores, nao essas linhas. Casos combinados (renumeracao + contrato, texto novo + contrato, ordem invertida da lista) conferidos em memoria e coerentes com a regra do card; o TF/TR do card cobrem so o par de texto e numero iguais.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O planejador ganha a régua de profundidade pelo tamanho do plano" e vai pegar a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto".
Tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto" e vai executar: Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação de mesmo texto cujo `precisa de:` ou `altera:` mudou, que hoje sai do drift sem linha nenhuma.
Agente executor devolveu a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto": review — sem pendência.
Tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A diferença entre versões mostra a operação que muda o que precisa ou o que altera sem mudar o texto" como done: registrar estado, RDO e telemetria.
