# RDO — P-0754 · AUF-T5

# Humano

Tarefa "O recorte parte de tudo o que já está versionado" concluída em 2026-09-28.
O ponto de partida da evidência agora inclui arquivos versionados que o .gitignore também cobre, então mudanças neles deixam de sumir.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 5/16 tarefas concluídas; próxima: "O arquivo novo que não é texto se julga pelo conteúdo bruto".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T5` — O recorte parte de tudo o que já está versionado
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o instrumento de evidência incluir no recorte o arquivo já versionado que a lista de ignorados também cobre.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "versionado"` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -c "from pathlib import Path;t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('def _gravar_arvore_de_trabalho'),t.count('_gravar_arvore_de_trabalho(root)'),t.count(chr(34)+'read-tree'+chr(34))))"` → `[1-2-1]` — antes `[0-0-0]`, depois `[1-2-1]`

**Pronto quando:** - dossiê de evidência.arquivo versionado e ignorado — o recorte parte de tudo o que já está versionado, e esse arquivo entra como qualquer outro — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-18`, `DAU-25`; `H-19` (§2.1); `F-13`, `F-14` (o resumo de diferenças grava a árvore pelo mesmo molde e tem o mesmo defeito).
- **Depende de:** `AUF-T4`
- **Operação do modelo:** `OP-5` - OP-5: Quem executa faz o instrumento de evidência incluir no recorte o arquivo já versionado que a lista de ignorados também cobre. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por `subprocess` com índice temporário (`GIT_INDEX_FILE`), sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Contratos/classes:** função nova `_gravar_arvore_de_trabalho(root: Path) -> str` — residência única da gravação da árvore de trabalho: cria o índice temporário como `capturar_ref` já cria (arquivo de `tempfile.mkstemp`, apagado antes do uso e no `finally`), e, quando `git rev-parse --verify HEAD` sai 0, roda `git read-tree HEAD` nesse índice antes do `git add -A`; sem commit ainda, o índice parte vazio como hoje; devolve o hash de `git write-tree`. `capturar_ref(root: Path) -> str` e `coletar_diff_stat(root: Path, desde: str | None = None) -> str` passam a obter a árvore só por `_gravar_arvore_de_trabalho(root)` — o bloco de índice temporário de cada uma sai —, e o resto delas não muda (pai, `commit-tree`, mensagem, `git diff --stat`). Docstring da função nova diz que ela é chamada pelas duas.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` o auxiliar e os dois testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "versionado"` e conferir que os dois falham. 3. Criar `_gravar_arvore_de_trabalho` e fazer `capturar_ref` e `coletar_diff_stat` a chamarem, pela regra de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não usar `git stash create` nem o índice real; não mudar `coletar_arquivos_tocados`, que passa a acertar pelo `<ref>` novo sem mudança própria.
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** auxiliar `_repo_com_versionado_ignorado(tmp_path: Path) -> Path` — repositório de `_init_repo_com_baseline`; `.gitignore` reescrito com `__pycache__/` e `versionado.log`; `versionado.log` criado com `v1`, adicionado com `git add -f` e commitado junto do `.gitignore`. TF `test_tf_capturar_ref_inclui_versionado_que_o_gitignore_cobre` — `versionado.log` reescrito com `v2`; depois de `ref = capturar_ref(repo)`, `git show <ref>:versionado.log` sai 0 com a saída `v2` e a quebra (a regra antiga sai diferente de 0: o `<ref>` não tem o arquivo). TF `test_tf_versionado_ignorado_intocado_fica_fora_dos_tocados_e_alterado_entra` — logo depois do `ref`, `coletar_arquivos_tocados(repo, desde=ref)` é `[]` (a regra antiga devolve `["versionado.log"]`); com o arquivo reescrito com `v3`, é `["versionado.log"]` e `coletar_diff_stat(repo, desde=ref)` contém `versionado.log` (a regra antiga devolve o resumo vazio). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o arquivo que não é texto (`AUF-T6`).
- **Handover:** 2026-09-28 · para `AUF-T6` - **Entregue:** _gravar_arvore_de_trabalho em .claude/tools/review_evidence.py (read-tree HEAD antes do add -A no índice temporário), chamada por capturar_ref e coletar_diff_stat; auxiliar _repo_com_versionado_ignorado e 2 TF no fim de tests/test_review_evidence.py - **Contrato:** o <ref> e o resumo de diferenças partem de tudo o que está versionado; versionado que o .gitignore cobre entra como qualquer outro - **Não refazer:** a gravação da árvore em função única - **Pendente:** nenhum

## Execução

**Consumo:** 20 tool uses, 66.8 k tokens, 215.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Reconciliacao sem divergencia: suite re-rodada 516 passed (514 no despacho + 2), Verificacoes 1 e 2 reproduzidas ([1-2-1]). Poder discriminante conferido fora do card: o review_evidence.py de 2ab46ca, num repositorio descartavel com versionado.log rastreado e ignorado, da git show rc 128, tocados ['versionado.log'] com o arquivo intocado e resumo de diferencas vazio com ele alterado - exatamente o que os dois testes novos negam. Ponta a ponta em repositorio descartavel: --capturar-ref com e sem HEAD, indice real (hash de ls-files -s) e lista de stash identicos antes e depois, com mudanca staged, rm --cached e nao rastreado presentes; --atribuir e o dossie completo (--out) coerentes entre si sobre o versionado ignorado (intocado fora, alterado dentro, estado git ' M'). commit-tree em capturar_ref deixou de receber o env do indice temporario - consequencia do recorte, sem efeito (commit-tree nao le indice).

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução" e vai pegar a tarefa "O recorte parte de tudo o que já está versionado".
Tarefa "O recorte parte de tudo o que já está versionado". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O recorte parte de tudo o que já está versionado" e vai executar: Quem executa faz o instrumento de evidência incluir no recorte o arquivo já versionado que a lista de ignorados também cobre.
Agente executor devolveu a tarefa "O recorte parte de tudo o que já está versionado": review — sem pendência.
Tarefa "O recorte parte de tudo o que já está versionado": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O recorte parte de tudo o que já está versionado" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O recorte parte de tudo o que já está versionado": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O recorte parte de tudo o que já está versionado" como done: registrar estado, RDO e telemetria.
