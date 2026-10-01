# RDO — P-0754 · AUF-T4

# Humano

Tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução" concluída em 2026-09-28.
O que o condutor escreve no diário e nos próprios registros deixa de ser atribuído, na evidência, a um tíquete que não o escreveu.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 4/16 tarefas concluídas; próxima: "O recorte parte de tudo o que já está versionado".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T4` — O que quem conduz escreve nos próprios registros conta como registro da condução
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o instrumento de evidência atribuir à condução, e não a um tíquete, o que quem conduz escreve nos próprios registros.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "escrita_da_conducao or fora_do_registro_segue"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.atribuição das escritas da condução — essa escrita conta como registro da condução antes de se procurar um tíquete dono — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-17`; `H-18` (§2.1); `F-9`, `F-13`.
- **Depende de:** `AUF-T3`
- **Operação do modelo:** `OP-4` - OP-4: Quem executa faz o instrumento de evidência atribuir à condução, e não a um tíquete, o que quem conduz escreve nos próprios registros. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; não importa de `tests/` nem de projeto consumidor.
- **Contratos/classes:** `confrontar_escopo(tocados, arquivos_alvo, root, alvos_de_outras_tarefas=None) -> dict` — assinatura e chaves do dicionário inalteradas. No laço sobre os tocados não cobertos, `_eh_registro_orquestracao(tocado)` se testa **antes** de `_tarefa_dona(tocado_norm, outros, root)`: o tocado que é registro da condução vai para `registro_orquestracao` e não chega à busca de tarefa dona. A precedência nova, que a docstring de `confrontar_escopo` passa a enunciar no lugar da antiga: coberto pelos alvos do card > registro da orquestração > alvo de outra tarefa do mesmo plano > ato do dono fora do ciclo de tarefa > fora dos alvos sem atribuição. `_REGISTRO_ORQUESTRACAO` não muda: `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/plans/`, `docs/RDO/`, `docs/audits/`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "escrita_da_conducao"` e conferir que o TF falha. 3. Trocar a ordem dos dois testes em `confrontar_escopo` e a frase de precedência da docstring, pela regra de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_REGISTRO_ORQUESTRACAO`, `_tarefa_dona`, `formatar_atribuicoes` nem a cobertura pelos alvos do próprio card, que segue em primeiro.
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_escrita_da_conducao_vence_o_alvo_de_outra_tarefa` — `confrontar_escopo(["docs/DIARIO_DE_OBRAS.md"], ["src/b.py"], repo, {"docs/DIARIO_DE_OBRAS.md": "TK-1a"})` devolve `registro_orquestracao == ["docs/DIARIO_DE_OBRAS.md"]` e `de_outra_tarefa == {}` (a regra antiga devolve `{"docs/DIARIO_DE_OBRAS.md": "TK-1a"}` e `[]`). TR `test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido` — `confrontar_escopo(["src/c.py"], ["src/b.py"], repo, {"src/c.py": "TK-1a"})` devolve `de_outra_tarefa == {"src/c.py": "TK-1a"}` e `registro_orquestracao == []`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o recorte do arquivo versionado e ignorado (`AUF-T5`).
- **Handover:** 2026-09-28 · para `AUF-T5` - **Entregue:** confrontar_escopo testa _eh_registro_orquestracao antes de _tarefa_dona (.claude/tools/review_evidence.py, laço de confrontar_escopo) e a docstring enuncia a precedência nova; TF/TR test_tf_escrita_da_conducao_vence_o_alvo_de_outra_tarefa e test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido no fim de tests/test_review_evidence.py - **Contrato:** precedência: coberto pelos alvos > registro da orquestração > alvo de outra tarefa > ato do dono > fora dos alvos - **Não refazer:** a ordem registro-antes-de-tarefa-dona - **Pendente:** nenhum

## Execução

**Consumo:** 17 tool uses, 65.2 k tokens, 152.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O alvo com curinga casa, e o alvo que não existia chega marcado como novo" e vai pegar a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução".
Tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução" e vai executar: Quem executa faz o instrumento de evidência atribuir à condução, e não a um tíquete, o que quem conduz escreve nos próprios registros.
Agente executor devolveu a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução": review — sem pendência.
Tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O que quem conduz escreve nos próprios registros conta como registro da condução" como done: registrar estado, RDO e telemetria.
