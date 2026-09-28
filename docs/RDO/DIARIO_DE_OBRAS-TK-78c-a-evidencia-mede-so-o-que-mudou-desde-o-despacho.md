# RDO — DIARIO_DE_OBRAS · TK-78c

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-78c` — A evidência mede só o que mudou desde o despacho
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o dossiê de evidência passa a mostrar, para cada arquivo-alvo, só o diff desde um instantâneo da árvore tirado no despacho — sem os hunks que outras frentes já tinham deixado —, e reconhece como caminho o alvo declarado com sufixo de seção (`<arquivo> §<n>`).

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-24. 1. `python -m pytest tests/test_review_evidence.py -q` — depois, os três TF novos verdes e `0 failed` 2. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 3`, `0 failed` 3. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'git stash create').Count` — antes `0`, depois `1` 4. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'Capturar `git rev-parse HEAD` como `<ref>`').Count` — antes `1`, depois `0`

**Pronto quando:** o trecho de diff de um arquivo-alvo mostra só o que mudou desde o instantâneo do despacho, e alvo com sufixo de seção é caminho — Verificações 1 e 2; o loop captura o instantâneo no passo 4 — Verificações 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Depende de:** `TK-78a` (as duas editam a skill scrum-master, em trechos distintos)
- **Fundamento:** `AE-1` (inconclusivo: `--desde` recolhe a árvore suja), `AE-2` (iii) e `AE-3` (ii) do `P-0748`. Medido em 2026-09-24: com `--desde d75e7a6` sobre árvore com 40+ arquivos modificados de outros planos, o trecho da skill-alvo da `TLG-T2` truncou em 4000 caracteres dentro de hunks do `P-0747` sem chegar à seção entregue; e `docs/plans/P-0748-tela-do-gerente.md §2.1` saiu como literal descartado, não como alvo.
- **Contratos/classes:** - `review_evidence.py`: constante nova `_SECAO_REF_RE = re.compile(r"\s+§\S*$")`, aplicada em `_classificar_campo_alvos` **antes** de `_LINHA_REF_RE`: `candidato = _LINHA_REF_RE.sub("", _SECAO_REF_RE.sub("", bruto))`. - `_diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -> str`: sem `desde`, comportamento atual intacto. Com `desde`: texto = `git diff <desde> -- <caminho_rel>`; não vazio → devolve; vazio e o caminho existe na árvore do `<desde>` (`git cat-file -e <desde>:<caminho_rel>` com exit `0`) → devolve a linha `(sem alteração desde <desde>)`, com `<desde>` entre crases; vazio e não existe no `<desde>` → o fallback atual (conteúdo integral do arquivo novo, ou a mensagem de ausente). - `montar_trechos(root, arquivos_alvo, teto_chars, tocados=None, desde=None)`: repassa `desde` às duas chamadas de `_diff_para_arquivo`; `montar_documento` passa o seu `desde` a `montar_trechos`. - `scrum-master` passo 4: a `<ref>` passa a ser a saída de `git stash create` (instantâneo dos arquivos rastreados, que não altera árvore, índice nem a lista de stash), ou `git rev-parse HEAD` quando a saída vem vazia (árvore limpa) — **Texto atual 1** → **Texto novo 1**.
- **Passos:** 1. Escreva os três TF abaixo em `tests/test_review_evidence.py`, reusando os ajudantes do arquivo (`_load_review_evidence`, `_init_repo_com_baseline`, `_run_git`); rode-os e veja-os falhar. 2. Implemente os contratos em `.claude/tools/review_evidence.py`; rode o arquivo de teste inteiro. 3. Em `.claude/skills/scrum-master/SKILL.md`, substitua o **Texto atual 1** pelo **Texto novo 1**. 4. Rode as Verificações.
- **Testes:** - TF `test_tf_alvo_com_sufixo_de_secao_e_caminho`: `extrair_arquivos_alvo` sobre um campo `arquivos-alvo` cujo único literal entre crases é `docs/x.md §2.1` devolve `["docs/x.md"]`. - TF `test_tf_trecho_desde_instantaneo_mostra_so_o_delta`: repositório com `a.md` commitado; edita `a.md` acrescentando a linha `linha-velha`; `snap = git stash create`; edita de novo acrescentando `linha-nova`; `montar_trechos(repo, ["a.md"], 4000, desde=snap)["a.md"]["texto"]` contém `+linha-nova` e não contém `+linha-velha`. - TF `test_tf_trecho_desde_sem_alteracao_nao_despeja_o_arquivo`: mesmo arranjo, sem a segunda edição; o texto é exatamente a linha `(sem alteração desde <snap>)`, com `<snap>` entre crases. - TR: o arquivo inteiro `tests/test_review_evidence.py` verde, inclusive `test_tr_sem_desde_nada_muda`; a suíte inteira.
- **Restrições desta tarefa:** - Sem `--desde`, a saída do gerador é byte a byte a de antes (TR `test_tr_sem_desde_nada_muda`). - `git stash create` só lê: nenhum passo roda `git stash push`, `git stash apply` nem altera a lista de stash. - Não tocar `coletar_arquivos_tocados` nem `coletar_estado_git` (já aceitam `desde`), nem o atribuidor `--atribuir` (`TK-66`). - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho sobe em exatamente `3`.
- **Não fazer:** não mudar o teto de 4000 caracteres; não mudar a gramática de caminho da `DB-27` além do sufixo de seção.
- **Contingências:** - se o **Texto atual 1** não for encontrado **exatamente uma vez** → parar e sinalizar `blocked` razão `premissa` - se `git stash create` sair diferente de `0` numa árvore suja → parar e sinalizar `blocked` razão `ferramenta`, colando a linha de erro - se algum teste preexistente de `tests/test_review_evidence.py` ficar vermelho → parar e sinalizar `blocked` razão `premissa`, colando o nome do teste
- **Fora do escopo desta tarefa:** a atribuição por `status` do `--atribuir` (`TK-66`); a atribuição por hunk. `docs/telemetria.tsv`. Capturar `git rev-parse HEAD` como `<ref>` (schema `DP-S`), usada no passo 6 (`AUT-T5b`). `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `git stash create` — instantâneo dos arquivos rastreados no despacho, que não altera árvore, índice nem a lista de stash —, ou `git rev-parse HEAD` quando ela vier vazia (árvore limpa); usada no passo 6 (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho.

## Execução

**Consumo:** 31 tool uses, 79.1 k tokens, 274.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
