# RDO — P-0754 · AUF-T6

# Humano

Tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto" concluída em 2026-09-28.
Arquivo novo que não é texto deixa de aparecer sempre como alterado: agora só entra na evidência quando os bytes mudaram.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 6/16 tarefas concluídas; próxima: "O painel mostra o título do tíquete em curso".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T6` — O arquivo novo que não é texto se julga pelo conteúdo bruto
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o instrumento de evidência comparar pelo conteúdo bruto o arquivo novo que não é texto, em vez de dá-lo sempre por tocado.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "binario"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.arquivo novo que não é texto — ele entra só quando o conteúdo mudou desde o recorte — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-19`; `H-20` (§2.1); `F-13`.
- **Depende de:** `AUF-T5`
- **Operação do modelo:** `OP-6` - OP-6: Quem executa faz o instrumento de evidência comparar pelo conteúdo bruto o arquivo novo que não é texto, em vez de dá-lo sempre por tocado. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por `subprocess` sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Contratos/classes:** `_nao_rastreado_mudou_desde_ref(root: Path, ref: str, caminho: str) -> bool` — assinatura inalterada. Quando `_texto_do_disco(root, caminho)` devolve `None`: lê os bytes de `root / caminho`; `FileNotFoundError` devolve `True`, como hoje; senão devolve se os bytes diferem do conteúdo bruto de `<ref>:<caminho>`, obtido por `git show <ref>:<caminho>` rodado com `subprocess.run(..., cwd=str(root), capture_output=True)` sem decodificar a saída, numa função nova `_bytes_do_ref(root: Path, ref: str, caminho: str) -> bytes`. O julgamento do arquivo que se lê como texto não muda.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "binario"` e conferir que o TF falha. 3. Criar `_bytes_do_ref` e mudar o ramo `None` de `_nao_rastreado_mudou_desde_ref`, pela regra de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a linha `(arquivo binário ou não-UTF-8 — trecho omitido)` de `_diff_para_arquivo` (o trecho do alvo não é a propriedade desta operação); não mudar `_texto_do_disco`.
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_nao_rastreado_binario_intocado_fica_fora_dos_tocados` — `imagem.bin` gravado com os bytes `FF FE 00 81` antes do `ref = capturar_ref(repo)` e não tocado depois: `coletar_arquivos_tocados(repo, desde=ref)` é `[]` (a regra antiga devolve `["imagem.bin"]`). TR `test_tr_nao_rastreado_binario_alterado_entra_nos_tocados` — o mesmo arquivo regravado com `FF FE 00 82` depois do `ref`: a lista é `["imagem.bin"]`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o painel do gerente (`AUF-T7`).
- **Handover:** 2026-09-28 · para `AUF-T15` - **Entregue:** _bytes_do_ref em .claude/tools/review_evidence.py (git show <ref>:<caminho> sem decodificar) e o ramo None de _nao_rastreado_mudou_desde_ref compara bytes; TF/TR de binário no fim de tests/test_review_evidence.py - **Contrato:** não rastreado que não é texto entra nos tocados só quando os bytes mudaram desde o <ref> - **Não refazer:** a comparação por bytes - **Pendente:** nenhum

## Execução

**Consumo:** 30 tool uses, 73.1 k tokens, 217.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O TF discrimina de verdade: rodado contra o review_evidence.py do recorte 55123364 (numa copia em pasta temporaria), o arquivo binario intocado sai ['imagem.bin']; contra a entrega, sai []. Tambem se exercitaram, alem dos dois testes, o binario apagado depois do recorte e o que passou de texto a binario: os dois entram nos tocados e no diff-stat, como devem. O teste final da AUF-T5 segue integro, com a assercao coletar_diff_stat dentro dele; o numstat e 15/2 e 33/0, so acrescimo ao fim do arquivo de testes; a suite fecha 518 passed.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O recorte parte de tudo o que já está versionado" e vai pegar a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto".
Tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto" e vai executar: Quem executa faz o instrumento de evidência comparar pelo conteúdo bruto o arquivo novo que não é texto, em vez de dá-lo sempre por tocado.
Agente executor devolveu a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto": review — sem pendência.
Tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto" como done: registrar estado, RDO e telemetria.
