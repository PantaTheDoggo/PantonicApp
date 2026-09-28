# RDO — DIARIO_DE_OBRAS · TK-74a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-74a` — O alvo-diretório de outra tarefa casa por prefixo
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** arquivo tocado sob um alvo-diretório declarado por **outra** tarefa do mesmo plano sai `alvo-de-outra-tarefa (<ID>)`, como já sai `alvo-do-card` o arquivo sob o alvo-diretório do próprio card.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-25. 1. `python -m pytest tests/test_review_evidence.py -q` — antes `42 passed`; depois `44 passed`, `0 failed` 2. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 2`, `0 failed` 3. `(Select-String -Path .claude/tools/review_evidence.py -SimpleMatch '_tarefa_dona(').Count` — antes `0`, depois `2` 4. `(Select-String -Path .claude/tools/review_evidence.py -SimpleMatch 'if tocado_norm in outros:').Count` — antes `1`, depois `0`

**Pronto quando:** arquivo sob alvo-diretório de outra tarefa sai atribuído a ela e arquivo sob nenhum alvo segue `sem-atribuicao` — Verificações 1 a 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** `AE-22` do `P-0746` (10 fixtures sob `tests/fixtures/modelo/`, alvo da `LST-T5`, chegaram à revisão da `LST-T6` como `sem-atribuicao`); `DT-1` e `DT-2` acima.
- **Contratos/classes:** - função nova `_tarefa_dona(tocado_norm: str, outros: dict[str, str], root: Path) -> str | None`, logo antes de `confrontar_escopo`: se `tocado_norm` é chave de `outros` → devolve o valor; senão, entre as chaves `chave` de `outros` com `_eh_alvo_diretorio(root, chave)` verdadeiro e `tocado_norm.startswith(_normalizar_separador(chave).rstrip("/") + "/")`, devolve o valor da de prefixo mais longo; nenhuma → `None`. - em `confrontar_escopo`, o ramo `if tocado_norm in outros:` / `de_outra_tarefa[tocado] = outros[tocado_norm]` passa a ser `dona = _tarefa_dona(tocado_norm, outros, root)` / `if dona is not None:` / `de_outra_tarefa[tocado] = dona`. Os demais ramos e a ordem de precedência dos baldes não mudam. - na docstring de `confrontar_escopo`, o trecho `a atribuição a outra tarefa casa por caminho exato, depois de normalizar` passa a dizer que ela casa por caminho exato e, sem ele, pelo alvo-diretório de prefixo mais longo (`TK-74`), depois de normalizar.
- **Passos:** 1. Escreva os dois TF abaixo em `tests/test_review_evidence.py`, reusando `_load_review_evidence`, `_init_repo_com_baseline` e `_escrever_plano_duas_tarefas`; rode-os e veja-os falhar. 2. Implemente os contratos; rode o arquivo de teste inteiro. 3. Rode as Verificações.
- **Testes:** - TF `test_tf_atribuir_alvo_diretorio_de_outra_tarefa_casa_por_prefixo(tmp_path, capsys)` — par presença-ausência: repositório de `_init_repo_com_baseline`; plano de `` _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `tests/fixtures/modelo/`.") ``; cria `tests/fixtures/modelo/a.md` e `tests/fixtures/outro/b.md` no repositório; `main(["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"])` devolve `0` e a saída contém `atribuicao: tests/fixtures/modelo/a.md -> alvo-de-outra-tarefa (T2)` **e** `atribuicao: tests/fixtures/outro/b.md -> sem-atribuicao`. - TF `test_tf_tarefa_dona_exato_vence_e_prefixo_mais_longo_desempata(tmp_path)` — `confrontar_escopo(["tests/fixtures/modelo/a.md", "tests/fixtures/modelo/c.md", "tests/x.md"], [], tmp_path, {"tests/": "T2", "tests/fixtures/modelo/": "T3", "tests/fixtures/modelo/a.md": "T4"})["de_outra_tarefa"]` é igual a `{"tests/fixtures/modelo/a.md": "T4", "tests/fixtures/modelo/c.md": "T3", "tests/x.md": "T2"}`. - TR: `tests/test_review_evidence.py` inteiro verde, inclusive `test_tf_arquivo_alvo_de_outra_tarefa_sai_atribuido_e_nao_pesa_no_veredito` e `test_tf_atribuir_alvo_diretorio_casa_por_prefixo`.
- **Restrições desta tarefa:** - Não renomear nem mudar a assinatura de `mapear_alvos_de_outras_tarefas`, `confrontar_escopo`, `formatar_atribuicoes` e `_init_repo_com_baseline` (âncoras da `SAN-T1` do `P-0749`). - Não filtrar por `status` — é a `TK-66a`. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho sobe em exatamente `2`.
- **Não fazer:** não mudar a gramática de caminho da `DB-27`; não mudar os baldes `registro-da-orquestracao` e `ato-do-dono`.
- **Contingências:** - se `confrontar_escopo` não tiver exatamente uma ocorrência de `if tocado_norm in outros:` → parar e sinalizar `blocked` razão `premissa`, colando a linha encontrada - se algum teste preexistente de `tests/test_review_evidence.py` ficar vermelho → parar e sinalizar `blocked` razão `premissa`, colando o nome do teste
- **Fora do escopo desta tarefa:** o filtro por `status` (`TK-66a`); o `modelo.py` (`TK-74b`).
- **Notas de execução:** - 2026-09-25 `review` — V1 44 passed; V2 324 passed (322+2); V3 2; V4 0

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
