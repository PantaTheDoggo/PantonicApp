# RDO — P-0754 · AUF-T1

# Humano

Tarefa "O arquivo criado depois do recorte chega ao revisor como diferença" concluída em 2026-09-28.
A evidência que o revisor recebe agora mostra só as linhas acrescentadas quando um arquivo é criado depois do despacho, em vez do arquivo inteiro.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 1/16 tarefas concluídas; próxima: "Um teste exercita o caminho com acento que o versionador devolve em código".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T1` — O arquivo criado depois do recorte chega ao revisor como diferença
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o instrumento de evidência mostrar como diferença, e não como conteúdo inteiro, o arquivo novo criado depois do recorte do despacho.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "arquivo_novo_depois_do_recorte or arquivo_novo_sem_desde"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.arquivo novo depois do recorte — o arquivo novo chega ao revisor como diferença contra o recorte, com um teste que o prova; se já chegava assim, o item fecha como resolvido antes e o teste fica de guarda — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-12`, `DAU-24`; `H-10` (§2.1); `F-13` (o TF falha em HEAD: o item não foi absorvido pelo `TK-93a`).
- **Operação do modelo:** `OP-1` - OP-1: Quem executa faz o instrumento de evidência mostrar como diferença, e não como conteúdo inteiro, o arquivo novo criado depois do recorte do despacho. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; não importa de `tests/` nem de projeto consumidor; roda `git` por `subprocess` sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Contratos/classes:** `_diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -> str` — assinatura inalterada. Regra nova, dentro do ramo `if desde is not None:`, depois do bloco do `TK-93a` (o que começa em `if _eh_nao_rastreado(root, caminho_rel) and _existe_no_ref(root, desde, caminho_rel):`) e antes da chamada `_git(["diff", desde, "--", caminho_rel], root)`: arquivo com `_eh_nao_rastreado(root, caminho_rel)` verdadeiro — ali ele já é ausente de `<ref>`, porque o bloco anterior devolveu o presente — tem o texto lido por `_texto_do_disco(root, caminho_rel)`; texto `None` devolve a linha que o bloco do `TK-93a` já usa, `(arquivo binário ou não-UTF-8 — trecho omitido)`; texto lido devolve o diff unificado contra o vazio, no molde do bloco do `TK-93a`: `difflib.unified_diff([], texto_atual.splitlines(), fromfile=f"{caminho_rel}@{desde}", tofile=caminho_rel, lineterm="")`, linhas unidas por quebra de linha e uma quebra final. Sem `desde`, nada muda.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`, no molde de `test_tf_nao_rastreado_no_ref_mostra_so_o_hunk` (fixture `_init_repo_com_baseline`, `review_evidence.capturar_ref`, `review_evidence.montar_trechos`). 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "arquivo_novo_depois_do_recorte"` e conferir que o TF falha. 3. Acrescentar em `_diff_para_arquivo` o ramo de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar o bloco do `TK-93a` nem o caminho sem `desde` de `_diff_para_arquivo`; não mudar `coletar_arquivos_tocados`, `capturar_ref` nem `montar_trechos`; não acrescentar marca de arquivo novo ao trecho (é da `AUF-T3`).
- **Contingências:** - se o TF `test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca` passar no passo 2, antes de qualquer mudança em `.claude/tools/review_evidence.py` → seguir sem o passo 3, com o TF como guarda, e devolver `contingência 1 acionada: absorvido em HEAD`. - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca` — repositório de `_init_repo_com_baseline`, `ref = review_evidence.capturar_ref(repo)`, depois `novo.md` criado com as linhas `linha-1` e `linha-2`; o texto de `montar_trechos(repo, ["novo.md"], 4000, desde=ref)["novo.md"]` contém `+linha-1` e `+linha-2` (a regra antiga devolve o conteúdo integral, sem `+`). TR `test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral` — o mesmo arquivo, sem `ref` e sem `desde`: o texto contém as duas linhas seguidas, com a quebra de cada uma, e não contém `+linha-1`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a marca de arquivo novo e o alvo com curinga (`AUF-T3`); o arquivo versionado e ignorado (`AUF-T5`); o arquivo que não é texto (`AUF-T6`).
- **Handover:** 2026-09-28 · para `AUF-T2`, `AUF-T3` - **Entregue:** ramo novo em _diff_para_arquivo (.claude/tools/review_evidence.py:601-614): não rastreado ausente do <ref> sai como diff unificado contra o vazio; TF test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca (tests/test_review_evidence.py:1403) e TR test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral (:1422) - **Contrato:** com desde, arquivo novo depois do recorte chega ao revisor com linhas '+'; sem desde, conteúdo integral como antes; bloco do TK-93a e assinatura intactos - **Não refazer:** o ramo de arquivo novo em _diff_para_arquivo - **Pendente:** arquivo novo VAZIO sai como bloco em branco (achado do laudo, a fechar com a marca de arquivo novo da AUF-T3)

## Execução

**Consumo:** 19 tool uses, 61.4 k tokens, 132.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O TF discrimina de fato: a versao de HEAD do modulo, rodada no mesmo cenario em repo temporario, devolve o conteudo integral; a nova devolve o hunk '@@ -0,0 +1,2 @@' com '+linha-1' e '+linha-2', na mesma forma do bloco do TK-93a e coerente com o --stat (novo.md 2 ++). Suite reconciliada: 507 passed (505 do despacho + 2).

## Fechamento

**Desdobramento:** aprovado

# Histórico

Tarefa "O arquivo criado depois do recorte chega ao revisor como diferença": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O arquivo criado depois do recorte chega ao revisor como diferença" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O arquivo criado depois do recorte chega ao revisor como diferença": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O arquivo criado depois do recorte chega ao revisor como diferença" como done: registrar estado, RDO e telemetria.
