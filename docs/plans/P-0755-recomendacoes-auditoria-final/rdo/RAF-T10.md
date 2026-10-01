# RDO — P-0755 · RAF-T10

# Humano

Tarefa "O caminho acentuado chega inteiro ao dossiê de evidência" concluída em 2026-09-29.
O caminho acentuado que o git status lista passa a chegar inteiro ao dossiê de evidência.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 17/47 tarefas concluídas; próxima: "A evidência mostra as linhas que a entrega tirou dos testes".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T10` — O caminho acentuado chega inteiro ao dossiê de evidência
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k acento_z` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.caminho acentuado — chega com a sua diferença, como qualquer outro — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-32`; `F-17` (as duas leituras do porcelain sem `-z`); relatório `R-31` (`AE-99` do `P-0754`).
- **Depende de:** `RAF-T9a`
- **Operação do modelo:** `OP-10` - OP-10: Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. Com `-z`, o `git status` entrega o caminho cru (sem aspas nem escape octal), qualquer que seja o `core.quotepath` da máquina.
- **Contratos/classes:** 1. `_extrair_caminho_status(linha: str) -> str` sai e, no lugar dela, entra `_entradas_status(root: Path) -> list[tuple[str, str]]`: roda `_git(["status", "--porcelain=v1", "-z", "--untracked-files=all"], root)`, separa a saída por NUL e devolve, na ordem do `git`, `(código XY, caminho)` de cada campo com 4 caracteres ou mais (`campo[:2]`, `campo[3:]`); quando o código contém `R` ou `C`, o campo seguinte (o caminho de origem) se consome sem virar entrada. 2. `coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]` e `coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]` — assinaturas inalteradas — trocam a leitura por linha da saída de `git status --porcelain=v1 --untracked-files=all` por `_entradas_status(root)`: sem `desde`, todo caminho entra nos tocados; com `desde`, o filtro dos não rastreados passa a ser `código == "??"`; em `coletar_estado_git`, a chave é o caminho e o valor é o código. O resto das duas funções (recorte por `<ref>`, `git diff <ref> --name-only`, `git diff <ref> --name-status`) não muda; o docstring de `coletar_estado_git` troca `_extrair_caminho_status` por `_entradas_status`.
- **Passos:** 1. Em `tests/test_review_evidence.py`, no teste `test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente` (o nome fica), trocar a única asserção do teste (a que compara `tocados` com a lista do caminho em escape octal) por `assert tocados == ["ação.txt"]` e o docstring pelas três linhas do bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do corpo da função): o significado do teste mudou pela `R-31`, e ele se reescreve, não se remove. ```text """AUF-T2, reescrito pela RAF-T10 (`R-31`): com `core.quotepath` ligado, o `git status` sem `-z` devolveria o caminho acentuado entre aspas com escape octal; com `-z` (`_entradas_status`) o caminho chega cru, e o não rastreado criado depois do `ref` entra nos tocados como `ação.txt`.""" ``` 2. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`. 3. Rodar `python -m pytest tests/test_review_evidence.py -q -k "acento_z or caminho_acentuado"` e conferir que o TF novo e o teste reescrito falham e o TR passa. 4. Aplicar os itens 1 e 2 de `Contratos/classes`. 5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5); `_extrair_caminho_status` sai por inteiro, sem sobrar sem chamador. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `tests/test_review_evidence.py`, as únicas linhas que já existiam e mudam são a asserção e o docstring do passo 1; o resto só se acrescenta ao fim. - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline` e ligam `core.quotepath` só nele; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_eh_nao_rastreado` (ele só lê o código `??` do caminho que recebe); não mudar as leituras de `git diff <ref> --name-only` e `git diff <ref> --name-status`; não depender do `core.quotepath` global da máquina.
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py`, fora o reescrito no passo 1, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_acento_z_nao_rastreado_chega_com_o_diff` — `core.quotepath` ligado no repositório do teste, `ação.txt` com a linha `linha-1` criado depois do `ref`: `coletar_arquivos_tocados(repo, desde=ref)` é `["ação.txt"]`, o trecho de `montar_trechos(repo, ["ação.txt"], 4000, tocados, desde=ref)` contém `+linha-1`, e `coletar_estado_git(repo)["ação.txt"]` é `??` (hoje o caminho chega em escape octal e o trecho sai `arquivo ausente`). TR `test_tr_acento_z_renomeado_usa_o_caminho_novo` — `git mv src/b.py src/c.py` no repositório do teste: `coletar_estado_git(repo)["src/c.py"]` é `R ` (R e espaço), `src/b.py` não é chave, e `coletar_arquivos_tocados(repo)` é `["src/c.py"]` (a regra concorrente que tratasse a origem da renomeação como entrada daria `src/b.py` também). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o caminho acentuado de arquivo rastreado nas saídas de `git diff <ref> --name-only` e `--name-status` (não pedido pela `R-31`; se a revisão o julgar defeito, vira `AE-<n>` na §9); as linhas removidas dos testes (`RAF-T11`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** review_evidence.py: _entradas_status(root) lê git status --porcelain=v1 -z (substitui _extrair_caminho_status) em coletar_arquivos_tocados e coletar_estado_git; 2 testes novos, suíte 556 - **Contrato:** arquivo acentuado não rastreado ou alterado na árvore chega com o nome inteiro pelo git status - **Não refazer:** _entradas_status e os testes - **Pendente:** as leituras git diff <ref> --name-only/--name-status (review_evidence.py:395, :421) e _CAMINHO_RE ASCII (:124) ainda não cobrem acento; modelo v2 pendente da OP-10; em triagem do consultor

## Execução

**Consumo:** 30 tool uses, 82.6 k tokens, 354.7 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo" e vai pegar a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência".
Tarefa "O caminho acentuado chega inteiro ao dossiê de evidência". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência" e vai executar: Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente.
Agente executor devolveu a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência": review — sem pendência.
Tarefa "O caminho acentuado chega inteiro ao dossiê de evidência": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Agente modelador recebe a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência" e vai atualizar o modelo.
Agente modelador devolveu a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência": Ato de conflito sobre a OP-10 feito, versão 2 pendente de validação. O `modelo.py check` sai 0..
Scrum master vai fechar a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência" como done: registrar estado, RDO e telemetria.
