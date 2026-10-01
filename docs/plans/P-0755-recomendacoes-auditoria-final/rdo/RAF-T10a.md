# RDO — P-0755 · RAF-T10a

# Humano

Tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência" concluída em 2026-09-29.
O arquivo acentuado já rastreado passa a chegar ao dossiê de evidência com a sua diferença e um nome só.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 18/48 tarefas concluídas; próxima: "A evidência mostra as linhas que a entrega tirou dos testes".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T10a` — O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o dossiê de evidência receber inteiro, e com um nome só, o arquivo acentuado já rastreado que a entrega alterou ou commitou depois do `ref` — na lista dos tocados, no estado do versionador, no resumo e no cabeçalho do trecho —, e reconhecer como caminho o alvo acentuado declarado no card — o que a `RAF-T10` deixou de fora ao corrigir só a leitura do `git status`.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "acento_diff or acento_alvo"` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -c "import pathlib,sys; t=pathlib.Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8'); q=chr(96); p=chr(34); a=t.count(p+'--name-only'+p); b=t.count('escape octal, por')+t.count('o último campo da linha'); c=t.count(p+'--name-status'+p+', '+p+'-z'+p); d=t.count('-z --untracked-files=all'+q+' por caminho'); e=t.count(p+'-c'+p+', '+p+'core.quotepath=false'+p); print('diff=%d-%d-%d-%d-%d'%(a,b,c,d,e)); sys.exit(0 if (a,b,c,d,e)==(0,0,1,1,1) else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `diff=1-2-0-0-0` antes e `diff=0-0-1-1-1` depois)

**Pronto quando:** - dossiê de evidência.caminho acentuado — o arquivo acentuado, novo ou já rastreado, chega com a sua diferença e com um nome só, como qualquer outro — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-52`; `AE-142`, `AE-143`, `AE-144`, `AE-145` (laudo da `RAF-T10`, ressalva 91); `DRF-32`; relatório `R-31`; versão 2 pendente do modelo (§1A, propriedade `dossiê de evidência.caminho acentuado`).
- **Depende de:** `RAF-T10`
- **Operação do modelo:** `OP-10` - OP-10: Quem executa faz o dossiê de evidência receber inteiro o nome de arquivo acentuado que o versionador lista, em vez de dá-lo por ausente. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. Sem `-z`, o `git diff` põe o caminho acentuado entre aspas com escape octal quando o `core.quotepath` está ligado (medido no laudo da `RAF-T10` e no ensaio do consultor); com `-z`, o caminho chega cru.
- **Contratos/classes:** 1. Entra `_entradas_diff(root: Path, ref: str) -> list[tuple[str, str]]`, ao lado de `_entradas_status`: roda `git diff <ref> --name-status -z` e devolve, na ordem do `git`, `(letra, caminho)` de cada arquivo; quando a letra começa por `R` ou `C`, vêm dois caminhos, o caminho é o segundo (o novo) e a origem não vira entrada. 2. `coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]` e `coletar_estado_git(root: Path, desde: str | None = None) -> dict[str, str]` — assinaturas inalteradas — trocam as leituras por linha de `git diff <ref> --name-only` e de `git diff <ref> --name-status` por `_entradas_diff(root, desde)`; ficam o filtro dos não rastreados já julgados por conteúdo (`nao_rastreados`) e o `setdefault` com o valor `<letra> (commitado desde <ref>)`. 3. `_CAMINHO_RE` aceita letra acentuada onde hoje aceita letra ASCII; o resto da gramática da `DB-27` fica (sem espaço, e com extensão, barra ou barra final). 4. `_git` roda o `git` com `-c core.quotepath=false` antes dos argumentos: o texto do `git` que o dossiê cola (o resumo `--stat` e o cabeçalho do diff unificado de cada trecho) mostra o nome acentuado cru; as leituras que a revisão confronta seguem por `-z` (`_entradas_status` e o item 1). 5. Nos docstrings das duas funções do item 2, cada trecho antigo do bloco abaixo sai e o novo entra no lugar (o trecho antigo pode atravessar uma quebra de linha do docstring; o novo entra no lugar dele sem quebra nova, e o resto do parágrafo não reflui): ```text coletar_arquivos_tocados: antigo: `<ref>` (`git diff <ref> --name-only`), em vez novo:   `<ref>` (`_entradas_diff`), em vez antigo: aparece em `git diff <ref> --name-only` (que o dá novo:   aparece como tocado de `_entradas_diff` (que o dá antigo: a que não existe no disco como veio do `git status` (nome entre aspas com escape octal, por exemplo). novo:   a que não existe no disco como veio do `git status`. coletar_estado_git: antigo: Código `XY` de `git status --porcelain=v1 --untracked-files=all` por caminho novo:   Código `XY` de `git status --porcelain=v1 -z --untracked-files=all` por caminho antigo: entra a letra de `git diff <ref> --name-status`, marcada novo:   entra a letra de `_entradas_diff`, marcada antigo: Para renomeação (`R100\t<velho>\t<novo>`), a chave é o último campo da linha e a letra é o primeiro campo inteiro (`R100`). novo:   Para renomeação, a chave é o caminho novo e a letra é o campo inteiro (`R100`). ```
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` os três testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "acento_diff or acento_alvo"` e conferir que os dois TF falham e o TR passa. 3. Aplicar os itens 1 a 5 de `Contratos/classes`. 4. Rodar as Verificações e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `90 passed` em `tests/test_review_evidence.py`, 2026-09-29, depois da `RAF-T10`). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `tests/test_review_evidence.py`, nenhuma linha que já existia muda; os testes novos só se acrescentam ao fim. - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline` e ligam `core.quotepath` só nele; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_entradas_status` nem `_eh_nao_rastreado`; não mudar `_EXTENSAO_RE`; não depender do `core.quotepath` global da máquina.
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_acento_diff_commitado_chega_com_um_nome_so` — `ação.md` (linha `linha-1`) commitado sobre o repositório de `_init_repo_com_baseline`, `core.quotepath` ligado, `ref` capturado, depois `ação.md` ganha `linha-2` e se commita (árvore limpa, só o `git diff` o vê): `coletar_arquivos_tocados(repo, desde=ref)` é `["ação.md"]`, `coletar_estado_git(repo, desde=ref)` é `{"ação.md": f"M (commitado desde {ref})"}` e o trecho de `montar_trechos(repo, ["ação.md"], 4000, tocados, desde=ref)` contém `+linha-2`; nem esse trecho nem `coletar_diff_stat(repo, desde=ref)` trazem o escape octal `\303`, e o resumo contém `ação.md` (hoje o tocado, o cabeçalho do trecho e o resumo chegam entre aspas com escape octal). TF `test_tf_acento_alvo_acentuado_e_caminho` — com o campo `arquivos-alvo` igual a `` - `docs/ação.md` `` (o caminho entre crases): `extrair_arquivos_alvo(campos)` é `["docs/ação.md"]` e `extrair_literais_nao_caminho(campos)` é `[]` (hoje `[]` e o literal descartado). TR `test_tr_acento_diff_renomeado_commitado_usa_o_caminho_novo` — `ref` capturado, `git mv src/b.py src/c.py` e commit: `coletar_estado_git(repo, desde=ref)` é `{"src/c.py": f"R100 (commitado desde {ref})"}` e `coletar_arquivos_tocados(repo, desde=ref)` é `["src/c.py"]` (a regra concorrente que tratasse a origem como entrada daria `src/b.py` também). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a extensão acentuada (`_EXTENSAO_RE`); as linhas removidas dos testes (`RAF-T11`).
- **Handover:** 2026-09-29 · para `RAF-T11` - **Entregue:** review_evidence.py: _entradas_diff(root, ref) lê git diff <ref> --name-status -z (chave = caminho novo na renomeação); _git roda com -c core.quotepath=false; _CAMINHO_RE aceita letra acentuada; docstrings acertados; 3 testes novos, suíte 559 - **Contrato:** arquivo acentuado, novo ou já rastreado, chega com a sua diferença e com um nome só (estado final da v2 pendente da OP-10) - **Não refazer:** _entradas_diff, o quotepath no _git, o _CAMINHO_RE e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 42 tool uses, 110.0 k tokens, 476.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta na revisao (repo descartavel, core.quotepath ligado, main com --desde e --out e --atribuir): rastreado acentuado commitado depois do ref, renomeacao acentuada commitada, rastreado acentuado alterado so na arvore e nao rastreado acentuado chegam todos com um nome so, atribuidos da entrega, com trecho e resumo --stat sem escape octal; OP-10 e o estado final da propriedade na versao 2 pendente (§1A) conferem com a entrega. Observacao sem rota: o trecho de uma renomeacao sai como arquivo novo (diff por pathspec do caminho novo), comportamento anterior e igual ao do nome ASCII.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O caminho acentuado chega inteiro ao dossiê de evidência" e vai pegar a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência".
Tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência" e vai executar: Quem executa faz o dossiê de evidência receber inteiro, e com um nome só, o arquivo acentuado já rastreado que a entrega alterou ou commitou depois do `ref` — na lista dos tocados, no estado do versionador, no resumo e no cabeçalho do trec…
Agente executor devolveu a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência": review — sem pendência.
Tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência" como done: registrar estado, RDO e telemetria.
