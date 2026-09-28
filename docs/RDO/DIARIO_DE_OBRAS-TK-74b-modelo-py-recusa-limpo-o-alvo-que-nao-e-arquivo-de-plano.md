# RDO — DIARIO_DE_OBRAS · TK-74b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-74b` — `modelo.py` recusa limpo o alvo que não é arquivo de plano
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `modelo.py check` e `modelo.py show` com `--plano` que não é arquivo saem com uma linha e exit `2`, sem traceback.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - `tests/test_modelo.py`

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-25. 1. `python .claude/tools/modelo.py check --plano TK-74; $LASTEXITCODE` — antes traceback `FileNotFoundError`; depois a linha `modelo: plano não encontrado 'TK-74' — sem modelo a julgar` e `2` 2. `python -m pytest tests/test_modelo.py -q` — os dois TF novos verdes, `0 failed` 3. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 2`, `0 failed`

**Pronto quando:** alvo que não é arquivo sai em uma linha com exit `2` nos dois verbos — Verificações 1 a 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** `AE-2` do `TK-78` e `DT-3` acima. Exit `2` porque é o código que o passo 9 da skill `scrum-master` já lê como *sem modelo a julgar — materializa e fecha*, o mesmo que `_checar_forma` devolve a plano sem a seção do modelo; o tíquete do diário é esse caso.
- **Contratos/classes:** - constante nova, junto das demais `_MSG_*`: `_MSG_PLANO_AUSENTE = "modelo: plano não encontrado '{}' — sem modelo a julgar"`. - em `verbo_check` e em `verbo_show`, logo depois de `plano_path = _resolver_plano(args)`: `if not plano_path.is_file():` → `print(_MSG_PLANO_AUSENTE.format(args.plano))` e `return 2`. Mesmo canal (`print` em stdout) das mensagens de `_checar_forma`.
- **Passos:** 1. Escreva os dois TF abaixo em `tests/test_modelo.py`, reusando `_load_modelo`; rode-os e veja-os falhar. 2. Implemente os contratos; rode o arquivo de teste inteiro. 3. Rode as Verificações.
- **Testes:** - TF `test_tf_check_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys)`: `_load_modelo().main(["check", "--plano", "TK-74", "--root", str(tmp_path)])` devolve `2` e a saída padrão contém `modelo: plano não encontrado 'TK-74'`. - TF `test_tf_show_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys)`: o mesmo com `["show", "--plano", "TK-74", "--root", str(tmp_path)]`. - TR: `tests/test_modelo.py` inteiro verde.
- **Restrições desta tarefa:** - Não mudar exit nem mensagem de nenhum caminho em que o plano existe. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho sobe em exatamente `2`.
- **Não fazer:** não ensinar o `modelo.py` a ler tíquete do diário; não tocar `backlog.py`.
- **Contingências:** - se `verbo_check` ou `verbo_show` não tiver exatamente uma linha `plano_path = _resolver_plano(args)` → parar e sinalizar `blocked` razão `premissa`, colando o que encontrou
- **Fora do escopo desta tarefa:** o `review_evidence.py` (`TK-74a`, `TK-66a`).
- **Notas de execução:** - 2026-09-25 `review` — V1 linha + exit 2 (check e show); V2 32 passed; V3 326 passed (324+2)

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
