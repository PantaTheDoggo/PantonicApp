# RDO — P-0755 · RAF-T7

# Humano

Tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava" concluída em 2026-09-29.
O dossiê de evidência do revisor passa a chegar ao fim nos três casos em que quebrava.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 11/44 tarefas concluídas; próxima: "O binário novo leva a marca de novo e o registro da orquestração tem um nome só".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T7` — O dossiê de evidência chega ao fim nos três casos em que quebrava
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k quebra` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.casos em que hoje quebra — compara o conteúdo bruto, falha com mensagem que nomeia o módulo ausente e acha a medida também na pasta do plano — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-11`; `F-17`; relatório `R-13` (auditoria reg. 25 e 26: `AE-105` e `AE-106` do `P-0754`).
- **Depende de:** `RAF-T3`
- **Operação do modelo:** `OP-7` - OP-7: Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; carrega `rdo.py` e `caminhos.py` por caminho; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. Primeira tarefa da etapa B: nasce `blocked` até o `go` do Marco 2 (`DRF-5`). O contrato do objeto é: "Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável."
- **Contratos/classes:** assinaturas públicas inalteradas. Cinco regras: 1. `_texto_do_ref(root: Path, ref: str, caminho: str) -> str` sai (os dois chamadores dela são os das regras 2 e 3) e, no lugar dela, entra `_texto_do_ref_ou_none(root: Path, ref: str, caminho: str) -> str | None`: os bytes de `_bytes_do_ref(root, ref, caminho)` decodificados em UTF-8; `None` quando não decodificam. 2. `_nao_rastreado_mudou_desde_ref`: no ramo em que o arquivo de hoje se lê como texto, a linha `return _texto_do_ref(root, ref, caminho).splitlines() != texto_atual.splitlines()` passa a usar `_texto_do_ref_ou_none`; com `None`, devolve `_bytes_do_ref(root, ref, caminho) != (root / caminho).read_bytes()`; com texto, a comparação por linha de hoje. 3. `_diff_para_arquivo`, no bloco do `TK-93a` (o que começa por `if _eh_nao_rastreado(root, caminho_rel) and _existe_no_ref(root, desde, caminho_rel):`): a linha `linhas_ref = _texto_do_ref(root, desde, caminho_rel).splitlines()` passa a usar `_texto_do_ref_ou_none`; com `None`, bytes iguais aos do disco devolvem `` (sem alteração desde `<ref>`) `` (a mesma linha que o bloco já usa, com o valor de `desde`) e bytes diferentes devolvem `(arquivo binário ou não-UTF-8 — trecho omitido)`; com texto, o diff de hoje. 4. `main`, verbo `--atribuir`: a linha `rdo = _load_rdo(args.root)` entra num `try` próprio, antes do `try` que já existe; `ReviewEvidenceValidationError` imprime em stderr `review_evidence: FALHOU - <mensagem>` e devolve 1 — a mensagem é a de `_load_rdo`, `rdo.py: módulo não encontrado em '<caminho>'`. Com `rdo.py` presente, o segundo carregamento (dentro de `mapear_alvos_de_outras_tarefas`) acha o mesmo arquivo e não muda. 5. `montar_documento`, com `dir_evidencia` dado: quando `Path(dir_evidencia) / f"{plano_id}-{dossie.tarefa_id}-medida.json"` não é arquivo, `caminho_medida` passa a ser `_caminhos.destino_medida(root, plano_path, dossie.tarefa_id)`; a medida ao lado do `--out` continua vencendo quando existe.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` o helper `_plano_em_pasta_com_medida(repo: Path, exit_medido: int) -> Path` e os cinco testes da seção `Testes`, no molde de `test_tf_nao_rastreado_binario_intocado_fica_fora_dos_tocados` e de `test_tf_evidencia_incorpora_medida` (fixture `_init_repo_com_baseline`, `review_evidence.capturar_ref`, `review_evidence.main`). 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k quebra` e conferir que os três TF falham e os dois TR passam. 3. Aplicar as cinco regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5); `_texto_do_ref` sai por inteiro, sem sobrar sem chamador. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_git` (os outros chamadores dependem da leitura em texto); não mudar o nome do arquivo de medida nem `caminhos.destino_medida` (é da `RAF-T15`); não mexer na marca de arquivo novo nem nos rótulos da lista (é da `RAF-T8`).
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_quebra_ref_binario_hoje_texto_compara_bytes` — `dados.txt` não rastreado com os bytes `FF FE 00 81` no `ref`, regravado depois como texto `ola`: `coletar_arquivos_tocados(repo, desde=ref)` devolve `["dados.txt"]` e o trecho de `montar_trechos(repo, ["dados.txt"], 4000, tocados, desde=ref)` é exatamente `(arquivo binário ou não-UTF-8 — trecho omitido)` (hoje a leitura do `ref` em texto cai com exceção). TR `test_tr_quebra_ref_texto_segue_por_linha` — `dados.txt` com `ola` e quebra `\n` no `ref`, regravado com `\r\n`: `coletar_arquivos_tocados` devolve `[]` (a regra concorrente que comparasse sempre os bytes daria `["dados.txt"]`). TF `test_tf_quebra_atribuir_sem_rdo_falha_nomeado` — `--root` numa pasta sem `.claude/tools/rdo.py`, com `--atribuir`: `main` devolve 1 e o stderr contém `review_evidence: FALHOU - rdo.py: módulo não encontrado em` (hoje a exceção escapa sem essa linha). TF `test_tf_quebra_out_fora_acha_medida_na_pasta_do_plano` — plano em `docs/plans/P-0999-teste/plano.md` dentro do repositório, medida `P-0999-T1-medida.json` na `evidencia/` dele com `exit` 7, `--out` em `tmp_path/fora/T1.md`: exit 0 e o documento gravado contém `` | 1 | `python -c "print('a')"` | 7 | true | `` (hoje a seção diz `ausente`). TR `test_tr_quebra_out_com_medida_ao_lado_usa_a_do_lado` — o mesmo, com outra `P-0999-T1-medida.json` ao lado do `--out` com `exit` 3: o documento contém a linha com `3`, não a com `7`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o diff de arquivo rastreado cujo conteúdo não é UTF-8 (não pedido pela `R-13`; se a revisão o julgar defeito, vira `AE-<n>` na §9); a marca do binário novo e o rótulo único (`RAF-T8`); o nome da medida com o mundo (`RAF-T15`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** review_evidence.py: _texto_do_ref_ou_none substitui _texto_do_ref (chamadores _nao_rastreado_mudou_desde_ref e _diff_para_arquivo); main --atribuir isola _load_rdo no próprio try; montar_documento cai para caminhos.destino_medida quando a medida ao lado de dir_evidencia não existe; 5 testes novos, suíte 549 - **Contrato:** o dossiê de evidência chega ao fim nos três casos que quebravam - **Não refazer:** as cinco regras e os 5 testes - **Pendente:** nenhum

## Execução

**Consumo:** 39 tool uses, 109.2 k tokens, 469.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta na arvore real: --atribuir e o caminho padrao sem rdo.py devolvem a mesma linha 'review_evidence: FALHOU - rdo.py: modulo nao encontrado em <caminho>' com exit 1 (contrato de erro coerente entre os verbos); a geracao real com --out fora da pasta do plano (tmp) achou evidencia/P-0755-RAF-T7-medida.json e preencheu a Medida do executor em vez de 'ausente'.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava" e vai executar: Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta.
Agente executor devolveu a tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava": review — sem pendência.
Tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava" como done: registrar estado, RDO e telemetria.
