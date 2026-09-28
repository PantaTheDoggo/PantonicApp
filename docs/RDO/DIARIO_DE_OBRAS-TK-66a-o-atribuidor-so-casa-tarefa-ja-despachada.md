# RDO — DIARIO_DE_OBRAS · TK-66a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-66a` — O atribuidor só casa tarefa já despachada
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `mapear_alvos_de_outras_tarefas` passa a pular toda tarefa cujo `status` não seja `in-progress`, `review` ou `done`; alvo de tarefa não despachada deixa de virar `alvo-de-outra-tarefa`.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** no PowerShell, na raiz do repositório. 1. `python -m pytest tests/test_review_evidence.py -q` — depois, o medido no despacho `+ 7`, `0 failed` 2. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 7`, `0 failed` 3. `(Select-String -Path .claude/tools/review_evidence.py -SimpleMatch '_STATUS_DESPACHADO').Count` — antes `0`, depois `2`

**Pronto quando:** tarefa em `ready`, `blocked`, `cancelled` ou sem status não recebe atribuição, e tarefa em `in-progress`, `review` ou `done` segue recebendo — Verificações 1 a 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Depende de:** `TK-74a`
- **Fundamento:** `AE-3` do `P-0743` (14 arquivos de janela paralela rotulados `alvo-de-outra-tarefa (DOM-T3/T4/T5)`, tarefas em `ready`); `DT-1` e `DT-2` acima. Depende da `TK-74a` porque as duas editam a atribuição a outra tarefa em `review_evidence.py`, e o TF dela usa o ajudante que este card altera.
- **Contratos/classes:** - constante nova, junto de `_BACKTICK_RE`: `_STATUS_DESPACHADO = frozenset({"in-progress", "review", "done"})`. - função nova `_status_do_dossie(dossie) -> str | None`, logo antes de `mapear_alvos_de_outras_tarefas`: percorre `dossie.extras` (lista de pares `[rotulo, conteudo]`); no primeiro par cujo `rotulo.strip().lower() == "status"`, devolve o primeiro literal entre crases de `conteudo` (`_BACKTICK_RE.search`), sem espaços em volta, ou `None` se não houver literal; sem o par → `None`. - em `mapear_alvos_de_outras_tarefas`, logo depois do `try/except` que extrai o dossiê: `if _status_do_dossie(dossie) not in _STATUS_DESPACHADO:` → `continue`. Assinatura e retorno inalterados. A docstring ganha uma frase: tarefa não despachada (`status` fora de `in-progress`/`review`/`done`, ou ausente) é pulada, porque alvo declarado sem despacho é previsão, não autoria (`TK-66`). - em `tests/test_review_evidence.py`, `_escrever_plano_duas_tarefas` ganha o parâmetro `status_t2: str | None = "done"`: não sendo `None`, escreve ``f"- **Status:** `{status_t2}` · 2026-09-25\n"`` como primeira linha depois do heading de T2; `None` omite a linha. O default `"done"` mantém verdes os nove usos existentes.
- **Passos:** 1. Altere o ajudante e escreva o TF abaixo; rode-o e veja falharem os casos `ready`, `blocked`, `cancelled` e `None`. 2. Implemente os contratos; rode o arquivo de teste inteiro. 3. Rode as Verificações.
- **Testes:** - TF `test_tf_atribuir_so_tarefa_despachada_casa` parametrizado em `status_t2` com os sete casos `in-progress`, `review`, `done` (esperado `atribuicao: src/a.py -> alvo-de-outra-tarefa (T2)`) e `ready`, `blocked`, `cancelled`, `None` (esperado `atribuicao: src/a.py -> sem-atribuicao`): repositório de `_init_repo_com_baseline`; plano de `` _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.", status_t2=<caso>) ``; `src/a.py` criado no repositório; `main([... "--atribuir"])` devolve `0` e a saída contém a linha esperada. - TR: `tests/test_review_evidence.py` inteiro verde, inclusive os dois TF da `TK-74a`.
- **Restrições desta tarefa:** - Não renomear nem mudar a assinatura de `mapear_alvos_de_outras_tarefas`, `confrontar_escopo`, `formatar_atribuicoes` e `_init_repo_com_baseline` (âncoras da `SAN-T1` do `P-0749`). - Não carregar `backlog.py` nem criar carregador novo. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho sobe em exatamente `7`.
- **Não fazer:** não criar balde novo de atribuição; não usar `--desde` na decisão; não ler `estado.tsv`.
- **Contingências:** - se `dossie.extras` não trouxer o par de rótulo `Status` para um card que tem a linha `- **Status:**` → parar e sinalizar `blocked` razão `premissa`, colando o `extras` impresso - se algum teste preexistente de `tests/test_review_evidence.py` ficar vermelho com o default `"done"` → parar e sinalizar `blocked` razão `premissa`, colando o nome do teste
- **Fora do escopo desta tarefa:** a leitura do `estado.tsv` de plano em pasta (`SAN-T3` do `P-0749`, achado acima); o alvo-diretório (`TK-74a`).
- **Notas de execução:** - 2026-09-25 `review` — V1 51 passed (44+7); V2 333 passed (326+7); V3 2

## Execução

**Consumo:** 0 tool uses, 0.0 k tokens, 0.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: executor: consumo do executor nao medido: execucao inline no contexto principal, sem notificacao de subagente (os zeros deste RDO sao ausencia de medida, nao medida zero)

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
