# RDO — P-0755 · RAF-T8

# Humano

Tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só" concluída em 2026-09-29.
O dossiê de evidência marca como novo o binário que o despacho não tinha e dá nome único ao registro da orquestração.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 13/45 tarefas concluídas; próxima: "O curinga do alvo casa como na linha de comando".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T8` — O binário novo leva a marca de novo e o registro da orquestração tem um nome só
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k marca_e_rotulo_binario` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_review_evidence.py -q -k marca_e_rotulo_registro` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.marca do arquivo novo que não é texto — os dois chegam com a mesma marca de arquivo novo — Verificação 1 - dossiê de evidência.rótulo do registro da orquestração — a lista e o resumo usam o mesmo nome — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-12`; `F-17` (dois rótulos para o mesmo fato: `atribuição: alheio` na lista, `Registro da orquestração` no resumo); relatório `R-14` (auditoria reg. 23 e 24).
- **Depende de:** `RAF-T7a`
- **Operação do modelo:** `OP-8` - OP-8: Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. A mudança é de texto do dossiê de evidência; os baldes de `confrontar_escopo` e o veredito mecânico não mudam.
- **Contratos/classes:** assinaturas inalteradas. Três regras: 1. `_diff_para_arquivo`, ramo da `AUF-T1` (com `desde`, não rastreado ausente de `<ref>`): a marca `` (arquivo novo — ausente em `<ref>`) `` e a quebra dela, que hoje só abrem o diff do texto, abrem também o retorno do arquivo que não se lê como texto, seguida de `(arquivo binário ou não-UTF-8 — trecho omitido)`. 2. `_diff_para_arquivo`, ramo final sem `desde` (o `except UnicodeDecodeError:` da leitura do arquivo que existe na árvore): não rastreado devolve `` (arquivo novo — ausente em `HEAD`) ``, a quebra e `(arquivo binário ou não-UTF-8 — trecho omitido)`; rastreado segue com a linha de hoje, sem marca. 3. `_renderizar`, seção `## Arquivos tocados`: arquivo que está em `escopo["registro_orquestracao"]` sai `atribuição: registro da orquestração`; os outros baldes alheios seguem `atribuição: alheio`; o coberto pelos alvos segue `atribuição: da entrega`. Os dois retornos das regras 1 e 2, exatos (as quebras são as do bloco; `<ref>` é o valor de `desde`): ```text (arquivo novo — ausente em `<ref>`) (arquivo binário ou não-UTF-8 — trecho omitido) ``` ```text (arquivo novo — ausente em `HEAD`) (arquivo binário ou não-UTF-8 — trecho omitido) ```
- **Passos:** 1. Em `tests/test_review_evidence.py`, no teste `test_tr_atribuicao_de_arquivos_tocados_cobre_os_quatro_baldes_alheios_de_confrontar_escopo`, trocar a asserção `` assert "- `docs/telemetria.tsv` — atribuição: alheio; estado git: `??`" in documento `` por `` assert "- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: `??`" in documento `` e, no docstring dele, o fim `ainda assim sai marcado` seguido de `` `alheio`. `` por `sai marcado com o nome do balde,` seguido de `` `registro da orquestração` (`R-14`, RAF-T8). `` — o significado da asserção mudou pela `R-14`, e ela se reescreve, não se remove. 2. Acrescentar ao fim de `tests/test_review_evidence.py` os três testes da seção `Testes`. 3. Rodar `python -m pytest tests/test_review_evidence.py -q -k "marca_e_rotulo or quatro_baldes_alheios"` e conferir que os dois TF e o teste reescrito falham. 4. Aplicar as três regras de `Contratos/classes`. 5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `tests/test_review_evidence.py`, as únicas linhas que já existiam e mudam são a asserção e as duas linhas do docstring do passo 1; o resto só se acrescenta ao fim. - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `confrontar_escopo`, `formatar_atribuicoes` (o `--atribuir` já usa `registro-da-orquestracao`) nem a linha `- Registro da orquestração (não atribuível a tarefa):` do resumo; não marcar como novo o arquivo rastreado; não mudar o curinga (é da `RAF-T9`).
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py`, fora o reescrito no passo 1, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marca_e_rotulo_binario_novo_abre_com_a_marca` — `img.bin` com os bytes `FF FE 00 81` criado depois do `ref`: `_diff_para_arquivo(repo, "img.bin", desde=ref)` é exatamente o primeiro bloco de `Contratos/classes` com o valor do `ref`, e `_diff_para_arquivo(repo, "img.bin")` é exatamente o segundo (hoje os dois devolvem só a linha do binário, sem marca). TR `test_tr_marca_e_rotulo_binario_rastreado_alterado_sem_marca` — `img.bin` versionado e alterado depois do `ref`: o retorno com `desde=ref` não contém `(arquivo novo`. TF `test_tf_marca_e_rotulo_registro_da_orquestracao_na_lista` — `docs/DIARIO_DE_OBRAS.md` e `docs/nota.txt` não rastreados, fora dos alvos: o documento de `montar_documento` contém `` - `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: `??` `` e `` - `docs/nota.txt` — atribuição: alheio; estado git: `??` `` (hoje o primeiro sai `alheio`). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o curinga do alvo (`RAF-T9`); o caminho acentuado (`RAF-T10`); as linhas removidas dos testes (`RAF-T11`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** review_evidence.py: binário novo abre com a marca (arquivo novo — ausente em <ref>/HEAD) antes do rótulo binário; arquivo do registro da orquestração sai 'atribuição: registro da orquestração' em Arquivos tocados; 3 testes novos, suíte 552 - **Contrato:** rastreado alterado binário segue sem marca; demais baldes alheios seguem 'alheio' - **Não refazer:** as três regras e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 30 tool uses, 80.2 k tokens, 344.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta pela CLI num repositorio descartavel (com e sem --desde, e --atribuir) confirmou coerencia do modulo: binario novo abre com a marca nos dois ramos, a lista por arquivo e o resumo '## Escopo' usam o mesmo nome para o registro da orquestracao, e o --atribuir segue com registro-da-orquestracao, como o card manda preservar. O ramo TK-93a (nao rastreado ja presente no ref, binario) segue sem marca, correto por nao ser arquivo novo.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência" e vai pegar a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só".
Tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só" e vai executar: Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo.
Agente executor devolveu a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só": review — sem pendência.
Tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só" como done: registrar estado, RDO e telemetria.
