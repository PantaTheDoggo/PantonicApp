# RDO — P-0755 · RAF-T22

# Humano

Tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova" concluída em 2026-09-29.
A diferença entre versões do modelo passa a mostrar a operação inserida, a renumerada e a propriedade nova.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 34/52 tarefas concluídas; próxima: "O comando do marco promove a versão aceita e cobra a validação do consultor".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T22` — A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - `tests/test_modelo.py`

**Verificação:** 1. `python -m pytest tests/test_modelo.py -q -k drift_versoes` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência do modelo.diferença entre versões — casa primeiro pelo texto, mostra operação nova, renumerada e alterada, e lista a propriedade que só uma das versões tem — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-16`; `F-19` (`_diff_fluxo` casa só por número e emite `[+]`, `[-]`, `[~]`; `_diff_estado` só mostra chave presente nas duas versões); relatório `R-07` (auditoria reg. 34: a inserção de uma operação apareceu como alterações em cascata, e a propriedade nova não apareceu).
- **Depende de:** `RAF-T21`
- **Operação do modelo:** `OP-22` - OP-22: Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem. - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, funções `_diff_fluxo` e `_diff_estado`, chamadas por `montar_drift` (verbo `show --drift`); só biblioteca padrão. A seção de objetos do drift (`_diff_objetos`) e o cabeçalho não mudam; `sem drift` continua saindo quando nenhuma das três seções tem linha. O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Contratos/classes:** `_diff_fluxo(vigente: Modelo, pendente: Modelo) -> list[str]` e `_diff_estado(vigente: Modelo, pendente: Modelo) -> list[str]` — assinaturas inalteradas. Duas regras: 1. `_diff_fluxo` passa a casar em duas rodadas, e ganha docstring que cita `R-07` e `DRF-16` do `P-0755`. Rodada 1, por texto: para cada operação da pendente, na ordem, o par é a primeira operação da vigente, na ordem, com o mesmo texto (igualdade exata de `texto`) e ainda sem par. Rodada 2, por número: para cada operação da pendente ainda sem par, o par é a operação da vigente de mesmo número, se ela ainda não tem par. Saída, nesta ordem: percorrendo a pendente, a operação sem par sai `[+] OP-<k> — <texto da pendente>`; com par de mesmo texto e outro número, `[=] OP-<k> (era OP-<j>)`; com par de outro texto, `[~] OP-<k> — <texto da vigente> => <texto da pendente>`; com par de mesmo texto e mesmo número, nenhuma linha. Depois, percorrendo a vigente, a operação que não virou par de ninguém sai `[-] OP-<j> — <texto da vigente>`. 2. `_diff_estado` emite, antes das linhas `[~]` de hoje: `[+] <chave> — <estado final da pendente>` para cada chave da pendente, na ordem dela, que a vigente não tem; e `[-] <chave> — <estado final da vigente>` para cada chave da vigente, na ordem dela, que a pendente não tem; as linhas `[~]` seguem como hoje. O comentário acima das duas voltas cita `DRF-16` do `P-0755`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_modelo.py` o helper `_modelo_drift(modelo, textos: list[str], estado: list[tuple[str, str, str]], versao: int)` (um `modelo.Modelo` com as operações `OP-1`..`OP-n` dos `textos`, na ordem, `precisa_de`, `altera` e `tarefas` vazios, o `estado` dado e `data="2026-09-28"`) e os três testes da seção `Testes`, que chamam `modelo.montar_drift(vigente, pendente)` direto. 2. Rodar `python -m pytest tests/test_modelo.py -q -k drift_versoes` e conferir que os dois TF falham e o TR passa. 3. Aplicar as duas regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de drift que já existem (`test_tf_show_drift_tres_marcadores`, `test_tf_show_drift_sem_diferenca`, `test_tf_drift_mostra_contrato_alterado`) continuam passando sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_diff_objetos`, `montar_drift` nem o verbo `show`; não comparar texto com espaços colapsados no drift (a igualdade é exata, como hoje); não mexer em `validar` (`RAF-T19`, `RAF-T21`).
- **Contingências:** - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_drift_versoes_insercao_mostra_nova_e_renumerada` — vigente `Primeira.`, `Segunda.`; pendente `Primeira.`, `Nova.`, `Segunda.`; mesmo estado: as linhas do drift contêm `[+] OP-2 — Nova.` e `[=] OP-3 (era OP-2)` e nenhuma começa por `[~] OP-` nem por `[-] OP-` (hoje saem `[+] OP-3 — Segunda.` e `[~] OP-2 — Segunda. => Nova.`). TR `test_tr_drift_versoes_texto_alterado_segue_por_numero` — vigente `Primeira.`; pendente `Primeira, reescrita.`: contém `[~] OP-1 — Primeira. => Primeira, reescrita.` e nenhuma linha `[+] OP-` nem `[-] OP-` (a regra concorrente, casar só por texto, daria `[+]` e `[-]`). TF `test_tf_drift_versoes_propriedade_de_uma_versao_so` — estado vigente `x.a` (final `fim`) e `x.c` (final `baixo`), pendente `x.a` (final `fim`) e `x.b` (final `alto`): contém `[+] x.b — alto` e `[-] x.c — baixo` (hoje nenhuma das duas). Suíte `tests/test_modelo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a promoção da versão aceita e a reescrita dos cards (`RAF-T23`); o drift de objetos, que já mostra `[+]`, `[-]` e `[~]`.
- **Handover:** 2026-09-29 · para `RAF-T23` - **Entregue:** modelo.py show --drift mostra operação inserida, operação renumerada e propriedade nova entre vigente e pendente (ver RDO RAF-T22) - **Contrato:** a diferença entre versões nomeia inserção, renumeração e propriedade nova - **Não refazer:** o drift novo e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 37 tool uses, 86.0 k tokens, 393.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta nesta revisao, em memoria, sem escrever no repositorio: remocao (A,B,C -> A,C) sai [=] OP-2 (era OP-3) e [-] OP-2 — B; insercao com alteracao (A,B -> A2,N,B) sai [~] OP-1, [+] OP-2, [=] OP-3 (era OP-2), sem cascata; troca de ordem sai dois [=]; texto duplicado na vigente sobra como [-]; versoes iguais seguem saindo 'sem drift'; estado com chave so-pendente, so-vigente e alterada sai [+], [-] e [~] nessa ordem. Plano real: show --drift sobre P-0755 sai exit 0 com so a linha de contrato do objeto e a linha de estado da versao 3, como a DRF-60 mediu; check sai 0 (versao 2, 52 tarefas). Os tres testes de drift pre-existentes seguem verdes sem mudanca e nenhuma linha de teste saiu. OP-22 confere com a entrega: sem conflito de modelo.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" e vai pegar a tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova".
Tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova" e vai executar: Quem executa faz a conferência do modelo mostrar, entre duas versões, a operação inserida, a renumerada e a propriedade que só uma delas tem.
Agente executor devolveu a tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova": review — sem pendência.
Tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova" como done: registrar estado, RDO e telemetria.
