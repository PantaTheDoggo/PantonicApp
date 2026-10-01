# RDO — P-0754 · AUF-T3

# Humano

Tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo" concluída em 2026-09-28.
A evidência do revisor agora entende alvos escritos com curinga e marca os arquivos que não existiam antes.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 3/16 tarefas concluídas; próxima: "O que quem conduz escreve nos próprios registros conta como registro da condução".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T3` — O alvo com curinga casa, e o alvo que não existia chega marcado como novo
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o instrumento de evidência reconhecer, entre os alvos do card, o nome escrito com curinga e o arquivo que ainda não existia.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "curinga or marcado_como_novo or marca_de_novo"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.leitura dos alvos do card — o alvo com curinga casa com os arquivos da árvore, e o alvo que não existia antes chega marcado como novo — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-14`, `DAU-22`, `DAU-23`; `H-13` (§2.1); `F-13`, `F-14`.
- **Depende de:** `AUF-T2`
- **Operação do modelo:** `OP-3` - OP-3: Quem executa faz o instrumento de evidência reconhecer, entre os alvos do card, o nome escrito com curinga e o arquivo que ainda não existia. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão (`fnmatch` entra no `import`); não importa de `tests/` nem de projeto consumidor; roda `git` por `subprocess` sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Contratos/classes:** assinaturas públicas inalteradas. Cinco regras: 1. `_CAMINHO_RE` aceita `*` nas duas classes de caractere: `re.compile(r"^[A-Za-z0-9_.*][A-Za-z0-9_./\\*-]*$")`; o resto de `_eh_caminho` não muda. 2. Função nova `_eh_alvo_curinga(alvo: str) -> bool` — verdadeiro quando o alvo contém `*`. 3. `montar_trechos(root, arquivos_alvo, teto_chars, tocados=None, desde=None)`: alvo com curinga, testado antes do alvo-diretório, casa por `fnmatch.fnmatchcase(_normalizar_separador(arquivo), _normalizar_separador(alvo))` contra cada item de `tocados` (lista vazia quando `tocados` é `None`); cada tocado que casa ganha a própria entrada, com o texto de `_diff_para_arquivo(root, arquivo, desde)` e o mesmo truncamento das demais; curinga sem tocado que case ganha uma entrada só, com a chave igual ao próprio alvo, `truncado` falso e o texto exato `(nenhum arquivo tocado casa com o curinga)`. 4. `confrontar_escopo`: a função interna `coberto` dá por coberto também o tocado que, com separador normalizado, casa por `fnmatch.fnmatchcase` com algum alvo com curinga do card; a atribuição a outra tarefa (`_tarefa_dona`) não muda. 5. `_diff_para_arquivo`: o trecho de arquivo não rastreado (`_eh_nao_rastreado`) ausente da base abre com uma linha de marca e a quebra dela, antes do resto do texto. Com `desde`, no ramo da `AUF-T1`, a base é `<ref>`; sem `desde`, no ramo final que lê o conteúdo integral do arquivo que existe na árvore, a base é `HEAD`, e a marca só entra quando o arquivo é não rastreado — o rastreado sem diferença segue como hoje. As duas linhas de marca, exatas (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco; `<ref>` é o valor de `desde`): ```text (arquivo novo — ausente em `<ref>`) (arquivo novo — ausente em `HEAD`) ```
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` os quatro testes da seção `Testes`, no molde de `test_tf_nao_rastreado_no_ref_mostra_so_o_hunk`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "curinga or marcado_como_novo"` e conferir que os três primeiros falham. 3. Aplicar em `.claude/tools/review_evidence.py` as cinco regras de `Contratos/classes`, com `import fnmatch` na lista de imports. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não expandir o curinga contra a árvore inteira (só contra os tocados, `DAU-22`); não mudar `_tarefa_dona` nem `mapear_alvos_de_outras_tarefas`; não mudar o ramo do `TK-93a`; não marcar como novo o arquivo rastreado.
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_alvo_com_curinga_casa_os_tocados` — `ref = capturar_ref(repo)`, depois `relatorios/a.md` e `relatorios/b.md` criados; `` extrair_arquivos_alvo({"arquivos-alvo": "- `relatorios/*.md`"}) `` devolve `["relatorios/*.md"]`; com `tocados = coletar_arquivos_tocados(repo, desde=ref)`, as chaves de `montar_trechos(repo, alvos, 4000, tocados, desde=ref)` são exatamente `relatorios/a.md` e `relatorios/b.md`, e `confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"]` é `[]` (a regra antiga descartava o literal, dava uma entrada só com a chave do padrão e punha os dois arquivos fora dos alvos). TR `test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa` — `montar_trechos(repo, ["relatorios/*.md"], 4000, [], desde=ref)` é exatamente o dicionário de uma entrada, chave `relatorios/*.md`, texto `(nenhum arquivo tocado casa com o curinga)`, `truncado` falso. TF `test_tf_alvo_nao_rastreado_sem_antes_sai_marcado_como_novo` — `novo.md` criado depois do `ref`: o texto com `desde=ref` começa pela marca de `<ref>` com o valor do `ref` e a quebra; sem `desde`, começa pela marca de `HEAD` e a quebra. TR `test_tr_alvo_rastreado_alterado_nao_leva_a_marca_de_novo` — `src/b.py` alterado depois do `ref`: o texto com `desde=ref` traz a linha nova com `+` e não contém `(arquivo novo`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o curinga no alvo de outra tarefa do mesmo plano (`_tarefa_dona`, não pedido pela operação); a diferença do arquivo novo contra o recorte (`AUF-T1`, já entregue).
- **Handover:** 2026-09-28 · para `AUF-T4`, `AUF-T5`, `AUF-T6` - **Entregue:** review_evidence.py: _CAMINHO_RE aceita '*'; _eh_alvo_curinga (:404); montar_trechos casa curinga contra os tocados, com '(nenhum arquivo tocado casa com o curinga)' (:674); confrontar_escopo.coberto aceita curinga; marca '(arquivo novo — ausente em <ref>/HEAD)' em _diff_para_arquivo (:626, :643); 4 testes em tests/test_review_evidence.py:1458-1518+ - **Contrato:** alvo com curinga casa só contra os tocados (fnmatchcase: '*' atravessa '/'); não rastreado ausente da base abre com a linha de marca; rastreado não leva marca - **Não refazer:** curinga em montar_trechos/confrontar_escopo e a marca de arquivo novo - **Pendente:** nenhum

## Execução

**Consumo:** 32 tool uses, 88.8 k tokens, 267.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Exercicio ponta a ponta em repo temporario (extrair_arquivos_alvo -> coletar_arquivos_tocados -> confrontar_escopo -> formatar_atribuicoes -> montar_trechos, com e sem desde, com e sem tocados, alvo com barra invertida, curinga mais literal sobreposto, truncamento): coerente em todos os caminhos. O AE-96 fica fechado de fato por esta entrega: o arquivo novo vazio depois do recorte agora abre com a marca de arquivo novo, nao sai mais como bloco em branco.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código" e vai pegar a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo".
Tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo" e vai executar: Quem executa faz o instrumento de evidência reconhecer, entre os alvos do card, o nome escrito com curinga e o arquivo que ainda não existia.
Agente executor devolveu a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo": review — sem pendência.
Tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo" como done: registrar estado, RDO e telemetria.
