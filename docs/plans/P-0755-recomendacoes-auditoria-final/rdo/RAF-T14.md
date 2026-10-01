# RDO — P-0755 · RAF-T14

# Humano

Tarefa "A conferência do card roda o git de leitura contra o recorte do despacho" concluída em 2026-09-29.
A conferência do card passa a rodar git de leitura contra o recorte do despacho e a pular a medida antes do item de invariância.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 25/51 tarefas concluídas; próxima: "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T14` — A conferência do card roda o git de leitura contra o recorte do despacho
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência de verificação do card rodar a leitura do versionador contra o recorte do despacho, inclusive a linha que prova que o alvo ficou igual.

**Arquivos-alvo:** - `.claude/tools/card_check.py` - `tests/test_card_check.py`

**Verificação:** 1. `python -m pytest tests/test_card_check.py -q -k git_leitura` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_card_check.py -q -k ref_do_despacho` → `exit 0` — antes `exit 5`, depois `exit 0` 3. `python -m pytest tests/test_card_check.py -q -k invariancia` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência de verificação do card.comandos de leitura do versionador — o versionador roda nos subcomandos de leitura, e outro subcomando é recusado com mensagem que o nomeia — Verificação 1 - conferência de verificação do card.recorte do despacho no comando — a marca do recorte no comando é trocada pelo recorte que o despacho gravou para a tarefa — Verificação 2 - conferência de verificação do card.linha de invariância — a linha declarada de invariância não é medida antes da entrega e é medida depois dela — Verificação 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-13` (iii) e (iv), `DRF-36`; `F-14` (só `python` e `pwsh` rodam; sem `shell=True`); relatório `R-11` (e o suporte que a `R-27` pede, `DRF-28`).
- **Depende de:** `RAF-T3`, `RAF-T13`, `RAF-T13a`
- **Operação do modelo:** `OP-14` - OP-14: Quem executa faz a conferência de verificação do card rodar a leitura do versionador contra o recorte do despacho, inclusive a linha que prova que o alvo ficou igual. - precisa de: conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/card_check.py`, só biblioteca padrão; o comando segue rodando por `subprocess.run` sem `shell=True`, decidido por token depois de `shlex.split`. O `git` entra só para ler: nenhum subcomando que escreve no índice, na árvore ou nas referências roda. O recorte vem de `.claude/estado/tarefa-corrente.json` sob o `--root`, que o `despachar` grava com `tarefa` e `ref` desde antes deste plano (e continua gravando depois da `RAF-T3`); como o despacho roda o `card_check` antes de gravar o recorte da tarefa nova, a linha com `<ref>` serve ao mundo `depois` (revisão e redespacho) e à linha de invariância.
- **Contratos/classes:** assinaturas públicas inalteradas. Quatro regras: 1. `_COMANDOS_PERMITIDOS` ganha `git`; tupla nova `_GIT_LEITURA = ("status", "diff", "show", "ls-files", "check-ignore")`; `_validar_comando`, depois da checagem do primeiro token, recusa `git` sem segundo token ou com segundo token fora de `_GIT_LEITURA`, com a razão `subcomando git '<segundo token>' fora da lista de leitura <_GIT_LEITURA>` (o segundo token vazio quando falta), que o item reporta como hoje: `item <n>: comando recusado - <razão>`. 2. Função nova `_ref_do_despacho(root: Path, tarefa_id: str) -> str | None`: lê `<root>/.claude/estado/tarefa-corrente.json`; devolve o `ref` só quando o JSON é objeto, o `tarefa` dele é `tarefa_id` e o `ref` não é vazio; arquivo ausente, ilegível ou de outra tarefa → `None`. 3. `ItemVerificacao` ganha o parâmetro `invariancia: bool = False`; `_parsear_itens` o liga, nas duas formas, quando o resto do item depois do comando contém o literal `(invariância)` (regex `_INVARIANCIA_RE`, `r"\(invariância\)"`). 4. Em `verificar_tarefa`, para cada item, logo depois de o registro entrar em `registros` e antes das regras de forma: item de invariância com `mundo == "antes"` → `registro["saida"] = "não medida (invariância)"`, sem falha, e o item não roda; comando com o literal `<ref>` → troca cada `<ref>` pelo valor de `_ref_do_despacho(root, dossie.tarefa_id)` (e o `registro["comando"]` passa a ser o comando trocado); com `None`, falha `item <n>: <ref> sem recorte do despacho para '<ID>' em .claude/estado/tarefa-corrente.json` e o item não roda. Na forma de bloco cercado, o item de invariância dispensa o `Medido antes` (a checagem de presença só o cobra de item sem invariância); no mundo `depois`, o item de invariância segue a comparação de hoje (inline: `depois` do par ou, sem par, a primeira crase do esperado; bloco: o esperado da `RAF-T13`). A forma da linha de invariância que os cards passam a publicar (`DRF-36`) é `` `git diff --exit-code <ref> --numstat -- <alvo>` → `exit 0` (invariância) ``: `--exit-code` faz o `git diff` sair 1 quando o alvo mudou desde o recorte, e 0 quando a saída é vazia.
- **Passos:** 1. Acrescentar ao fim de `tests/test_card_check.py` o helper `_raiz_com_despacho(tmp_path: Path, tarefa: str, ref: str) -> Path` (raiz temporária com cópias de `rdo.py` e `caminhos.py` em `.claude/tools/` e `.claude/estado/tarefa-corrente.json` com `tarefa` e `ref`) e os cinco testes da seção `Testes`, usando os helpers `_plano_com_item` e `_rodar` da `RAF-T13`. 2. Rodar `python -m pytest tests/test_card_check.py -q -k "git_leitura or ref_do_despacho or invariancia"` e conferir que os quatro TF falham e o TR passa. 3. Aplicar as quatro regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_card_check.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Nenhum teste roda subcomando `git` que escreve: o teste da recusa só confere a razão, e o comando recusado nunca roda. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não passar `shell=True`; não aceitar `git` com opção global antes do subcomando (`git -C`, `git -c`); não gravar nem capturar `ref` no `card_check` (o recorte é do `despachar`); não mudar `--gravar` nem o nome da medida (é da `RAF-T15`); não editar a doutrina do planejador (é da `RAF-T17`).
- **Contingências:** - se um teste que já existia em `tests/test_card_check.py` ou um teste de `despachar` em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_git_leitura_roda_ls_files` — item `` `git ls-files tests/test_card_check.py` `` com `antes` e `depois` iguais a `tests/test_card_check.py`, `--root` na raiz do repositório: `--mundo antes` sai 0 (hoje sai 1, `primeiro token fora da lista fechada`). TF `test_tf_git_leitura_recusa_subcomando_de_escrita` — item `` `git commit -m x` ``: sai 1 com `subcomando git 'commit' fora da lista de leitura` no stderr (hoje a razão é a do primeiro token). TF `test_tf_ref_do_despacho_entra_no_comando` — raiz com `tarefa-corrente.json` de `RX-T1` e `ref` `abc123`, item que imprime o primeiro argumento com `<ref>` como argumento, `depois` `abc123`: `--mundo depois` sai 0 (hoje imprime `<ref>` e sai 1). TR `test_tr_ref_do_despacho_de_outra_tarefa_falha` — o JSON é de `OUTRA-T1`: sai 1 com `item 1: <ref> sem recorte do despacho para 'RX-T1'`. TF `test_tf_invariancia_nao_medida_antes_e_medida_depois` — item `` `python -c "import sys;sys.exit(1)"` → `exit 0` (invariância) ``, sem par: `--mundo antes` com `--gravar` sai 0 e o JSON gravado tem `não medida (invariância)` na `saida` do item 1 (hoje sai 1, `sem valor antes`); `--mundo depois` sai 1 (o item roda e o exit 1 não é o `exit 0` esperado). Suíte `tests/test_card_check.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a pasta e o nome da medida gravada (`RAF-T15`); a regra do planejador para o card que deixa o alvo igual (`RAF-T17`).
- **Handover:** 2026-09-29 · para `RAF-T15` - **Entregue:** card_check.py: roda git de leitura (_GIT_LEITURA status/diff/show/ls-files/check-ignore; outro subcomando recusado); <ref> do comando vem de .claude/estado/tarefa-corrente.json (_ref_do_despacho); item marcado (invariância) não se mede no mundo antes; 5 testes novos, suíte 578 - **Contrato:** Verificação de card pode usar git de leitura contra o <ref> do despacho; subcomando de escrita é recusado - **Não refazer:** _GIT_LEITURA, _ref_do_despacho, invariancia e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 34 tool uses, 124.7 k tokens, 636.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta (plano sintetico fora do repo, --root no repo, tarefa-corrente.json real de RAF-T14): git diff --exit-code <ref> --numstat na forma inline e na de bloco cercado com (invariancia) fica 'nao medida' em antes, sem exigir Medido antes, e em depois sai 0 para rdo.py (inalterado) e 1 para card_check.py (alterado) - a linha de invariancia discrimina; git show com <ref> troca pelo ref de 40 caracteres nos dois mundos; git -C, git sozinho e git stash sao recusados nomeando o segundo token; tarefa diferente da do tarefa-corrente.json falha nomeada em todo item com <ref>; --gravar registra o comando ja trocado. card_check sobre os 41 cards do P-0755 sai 0 em todos menos o proprio RAF-T14 no mundo antes (status review, antes exit 5 consumido - sai 0 em --mundo depois), mesmo padrao do RAF-T13. O TDD pulado pelo executor foi reposto por reproducao: os 4 TF falham no codigo do ref pelas razoes que os docstrings declaram.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1" e vai pegar a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho".
Tarefa "A conferência do card roda o git de leitura contra o recorte do despacho". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho" e vai executar: Quem executa faz a conferência de verificação do card rodar a leitura do versionador contra o recorte do despacho, inclusive a linha que prova que o alvo ficou igual.
Agente executor devolveu a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho": review — sem pendência.
Tarefa "A conferência do card roda o git de leitura contra o recorte do despacho": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho" como done: registrar estado, RDO e telemetria.
