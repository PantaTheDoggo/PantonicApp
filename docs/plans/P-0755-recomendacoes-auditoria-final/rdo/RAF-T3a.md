# RDO — P-0755 · RAF-T3a

# Humano

Tarefa "O pacote do despacho marca ausente só a linha citada que sumiu" concluída em 2026-09-28.
O pacote do despacho deixa de acusar âncora ausente que não sumiu e marca só a linha citada que mudou.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 5/42 tarefas concluídas; próxima: "Quem conduz repassa o texto pronto do despacho e não reconfere âncora".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T3a` — O pacote do despacho marca ausente só a linha citada que sumiu
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência de âncoras do despacho marcar como ausente só o texto que o card cita como linha de um arquivo e que não está mais nele, lendo o trecho entre crases como o Markdown o lê, sem tomar comando, nome novo ou rótulo de campo por âncora que sumiu.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q -k nao_marcam_ausente` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_backlog.py -q -k sem_extensao` → `exit 0` — antes `exit 5`, depois `exit 0` 3. `python -m pytest tests/test_backlog.py -q -k linha_citada_que_sumiu` → `exit 0` — antes `exit 5`, depois `exit 0` 4. `python -m pytest tests/test_backlog.py -q -k confere_as_ancoras` → `exit 0` — antes `exit 0`, depois `exit 0` (invariância: o teste da `RAF-T3`, com a linha do item 2, segue verde)

**Pronto quando:** - despacho de tarefa.âncoras conferidas — o pacote traz cada linha citada com o número atual e o texto dela, e marca como ausente o texto que não está mais no arquivo — Verificações 1, 2 e 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-45`; `AE-125` (laudo da `RAF-T3`, ressalva 91); `DRF-8`, `DRF-35`; relatório `R-03`.
- **Depende de:** `RAF-T3`
- **Operação do modelo:** `OP-3` - OP-3: Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit — só a função `conferir_ancoras_do_card` de `.claude/tools/backlog.py`, só biblioteca padrão; `despachar`, `_campos_do_card`, o pacote e o texto pronto ficam como a `RAF-T3` os gravou. A regra que o `card_check` já aplica a `Arquivos-alvo` e `Passos` (âncora `<caminho>:<n>` seguida do literal, separado por `—` ou `:`) é a mesma que esta regra usa para saber que um trecho é o texto de uma linha citada. Medida do consultor (2026-09-28) sobre os 41 cards do `P-0755`: a regra de hoje dá 1066 linhas de âncora, 573 delas `âncora ausente`; a regra desta tarefa, ensaiada em cópia, dá 501 linhas e nenhuma ausente.
- **Contratos/classes:** 1. `backlog.py`, `conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]` — assinatura, os campos lidos (`Arquivos-alvo` para os alvos; `Passos` e, depois, `Contratos/classes` para os trechos), a ordem dos alvos, o pulo do trecho com menos de 4 caracteres, do já visto e do que é um dos alvos, o item repetido que não se repete, o `["- nenhuma âncora citada"]` e a leitura UTF-8 com `errors="replace"` ficam como estão. Muda esta regra fechada (`DRF-45`), que a docstring passa a descrever, citando `DRF-45`: (g) trecho entre crases é o *code span* do Markdown, lido linha a linha do campo: uma sequência de N crases abre, a próxima sequência de exatamente N crases fecha, e o trecho é o que fica entre elas, sem espaços nas pontas; vale também para os alvos de `Arquivos-alvo`. A regex ensaiada, com o trecho no grupo 2 (as quebras são as do bloco): ```text (?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`) ``` (h) trecho de linha citada é o que casa a regex do bloco abaixo; o caminho resolve para ele mesmo quando é arquivo sob `repo` e, se não for, para o primeiro alvo, na ordem do card, cujo caminho termina em `/` mais o caminho citado; resolvido e com `1 <= n <= número de linhas` → `- <caminho resolvido>:<n> — <linha n sem espaços nas pontas>`; senão → `- âncora ausente: <trecho>`. ```text ^(?P<caminho>[^:\s`]+):(?P<linha>\d+)(?:-\d+)?$ ``` (i) trecho que, na mesma linha do card, vem logo depois de um trecho da forma (h), com só espaços e um `—` ou um `:` entre os dois, é o texto daquela linha citada: a primeira linha do arquivo resolvido que o contém → `- <caminho resolvido>:<k> — <texto da linha sem espaços nas pontas>`; caminho não resolvido ou nenhuma linha que o contenha → `- âncora ausente: <trecho>`. Um trecho da forma (h) pulado por já visto continua abrindo o (i) do trecho seguinte. (j) outro trecho → a primeira linha, do primeiro alvo em ordem, que o contém, como hoje; sem linha, o trecho **não entra** no pacote: não cita linha (comando, nome que a tarefa cria, rótulo de campo). 2. `tests/test_backlog.py`, em `test_tf_despachar_confere_as_ancoras_do_card`: a ausência passa a vir de uma linha citada. A linha do texto antigo vira as três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os oito espaços que já tem no arquivo); as asserções do teste não mudam. Texto antigo: ```text "  2. Trocar `return 1` e `texto que sumiu`.\n" ``` Texto novo: ```text "  2. Trocar `return 1`.\n" "- **Contratos/classes:**\n" "  1. `src/alvo.py:2` — `texto que sumiu`.\n" ```
- **Passos:** 1. Acrescentar ao fim de `tests/test_backlog.py` os três testes da seção `Testes`, no molde de `test_tf_despachar_confere_as_ancoras_do_card` (fixture `_montar_repo_despachar`, o card `GAM-T1` com o bullet do `Entregável` trocado pelos campos do teste, `backlog.main(["despachar", "GAM-T1", "--repo", str(repo)])` saindo 0, o pacote lido de `docs/plans/P-0-gama/despacho/GAM-T1.md`). 2. Rodar `python -m pytest tests/test_backlog.py -q -k "nao_marcam_ausente or sem_extensao"` e conferir que os dois testes TF falham. 3. Aplicar os itens 1 e 2 de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `530 passed`, 2026-09-28, entrega da `RAF-T3`). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5, `DRF-44`). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `despachar`, `_campos_do_card`, `destino_despacho`, o pacote nem o texto pronto; não mudar o `card_check.py` (a regra dele fica como está); não tirar asserção de teste existente.
- **Contingências:** - se um teste de `despachar` que já existia em `tests/test_backlog.py`, além do do item 2 de `Contratos/classes`, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_ancoras_nao_marcam_ausente_o_trecho_que_nao_cita_linha` — alvo `src/alvo.py` com as linhas `x = 1`, `def alvo():` e `    return 1`; `Passos` com `` 1. Rodar `python -m pytest -q` e preencher o campo `Testes`. `` e ``` 2. Conferir ``campo `Testes` do card`` e trocar `return 1`. ```; o pacote tem `- src/alvo.py:3 — return 1` e não tem `- âncora ausente` (a regra de hoje marca ausentes o comando, o rótulo e o fragmento da crase dupla). TF `test_tf_ancoras_leem_arquivo_sem_extensao_e_caminho_pelo_alvo` — alvos `src/alvo.py` (as mesmas linhas) e `.alvorc` (linhas `chave = 1` e `outra = 2`); `Contratos/classes` com `` 1. Editar `.alvorc:2` e `alvo.py:3`. ``; `Passos` com `1. Aplicar Contratos/classes.`; o pacote tem `- .alvorc:2 — outra = 2` e `- src/alvo.py:3 — return 1` e não tem `- âncora ausente` (a regra de hoje marca os dois ausentes). TR `test_tr_ancoras_marcam_ausente_a_linha_citada_que_sumiu` — alvo `src/alvo.py` (as mesmas linhas); `Contratos/classes` com `` 1. `src/alvo.py:2` — `texto que sumiu`; `src/alvo.py:9`. ``; `Passos` com `1. Aplicar Contratos/classes.`; o pacote tem `- src/alvo.py:2 — def alvo():`, `- âncora ausente: texto que sumiu` e `- âncora ausente: src/alvo.py:9` (a regra concorrente, que não marcasse ausente trecho nenhum, falharia; a de hoje passa). A âncora com linha fica em `Contratos/classes` porque o `card_check` do despacho recusa, em `Passos`, a âncora cujo literal não está na linha. Suíte `tests/test_backlog.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a regra de âncora do `card_check.py`; as linhas de âncora achadas que não são ponto de edição (o pacote segue trazendo a primeira linha que contém o trecho); a doutrina dos Passos 3 e 4 da skill `scrum-master` (`RAF-T4`).
- **Handover:** 2026-09-28 · para `RAF-T4` - **Entregue:** conferir_ancoras_do_card (.claude/tools/backlog.py) lê crases como o Markdown, aceita <caminho>:<n> sem extensão e por sufixo de alvo, e marca ausente só linha citada que sumiu ou texto citado depois dela; 3 testes novos, suíte 533 passed - **Contrato:** o pacote do despacho não traz mais âncora ausente falsa: comando, nome novo e rótulo de campo saem do pacote - **Não refazer:** a regra nova de âncoras e os testes - **Pendente:** o pacote ainda traz, por trecho, a primeira linha dos alvos que o contém mesmo quando não é ponto de edição (matéria inconclusiva no cenário)

## Execução

**Consumo:** 23 tool uses, 116.6 k tokens, 626.2 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor" e vai pegar a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu".
Tarefa "O pacote do despacho marca ausente só a linha citada que sumiu". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu" e vai executar: Quem executa faz a conferência de âncoras do despacho marcar como ausente só o texto que o card cita como linha de um arquivo e que não está mais nele, lendo o trecho entre crases como o Markdown o lê, sem tomar comando, nome novo ou rótul…
Agente executor devolveu a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu": review — sem pendência.
Tarefa "O pacote do despacho marca ausente só a linha citada que sumiu": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O pacote do despacho marca ausente só a linha citada que sumiu" como done: registrar estado, RDO e telemetria.
