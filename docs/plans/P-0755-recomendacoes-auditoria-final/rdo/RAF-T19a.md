# RDO — P-0755 · RAF-T19a

# Humano

Tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência" concluída em 2026-09-29.
O teste passa a distinguir o check com e sem a flag de versão vigente pela versão pendente fora de sequência.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 31/52 tarefas concluídas; próxima: "O despacho pede à conferência do modelo só a versão vigente".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T19a` — O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa acrescenta à suíte do `modelo.py` o caso que distingue a regra 3 da `RAF-T19`: com a versão pendente fora de sequência, o `check --so-vigente` não emite a `V20` e o `check` sem a flag a emite.

**Arquivos-alvo:** - `tests/test_modelo.py`

**Verificação:** 1. `python -m pytest tests/test_modelo.py -q -k "so_vigente and fora_de_sequencia"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência do modelo.versões julgadas — pedida só a vigente, a versão pendente fora de sequência não recusa a conferência; sem o pedido, a `V20` a recusa — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-59`; `AE-169` (laudo da `RAF-T19`, ressalva 91: os quatro testes da `RAF-T19` montam a pendente em versão 2 contra a vigente 1, a `V20` nunca dispara, e tirar a guarda `not so_vigente` de `validar` deixa os quatro verdes, critério (ix) da rubrica §8); relatório `R-04`. Medido pelo consultor em cópia (2026-09-29): com os dois testes abaixo, tirar a linha `and not so_vigente` de `validar` faz o TF sair `1 failed`.
- **Depende de:** `RAF-T19`
- **Operação do modelo:** `OP-19` - OP-19: Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco. - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** teste do instrumento `.claude/tools/modelo.py`; nenhum código de produção muda. O caso reusa o helper `_raiz_modelo_pendente` da `RAF-T19` (com o card da `OP-2`, para que a `## 1A` saia limpa) e só troca a versão da pendente de 2 para 3 no plano gravado, de modo que a `V20` seja a única violação e a única diferença entre o `check` com e sem a flag.
- **Passos:** 1. Acrescentar ao fim de `tests/test_modelo.py` o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0; duas linhas vazias antes de cada `def`). ```python def _raiz_pendente_fora_de_sequencia(tmp_path: Path) -> tuple[Path, Path]: """RAF-T19a: a raiz de `_raiz_modelo_pendente` com o card da `OP-2` e a `## 1A` em versão 3 contra a vigente 1, para que só a `V20` distinga o `check` com e sem `--so-vigente`.""" raiz, plano = _raiz_modelo_pendente(tmp_path, tarefas_op2="EX-T2", card_op2=True) texto = plano.read_text(encoding="utf-8") plano.write_text( texto.replace("**Estado do modelo:** versão 2 ·", "**Estado do modelo:** versão 3 ·"), encoding="utf-8", ) return raiz, plano def test_tf_so_vigente_pendente_fora_de_sequencia_nao_e_v20(tmp_path, capsys): """TF (RAF-T19a): pendente em versão 3 contra a vigente 1 — `check --so-vigente` sai 0 sem `V20` no stderr (sem a guarda `not so_vigente` sairia 1 com a `V20`).""" modelo = _load_modelo() raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path) codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"]) saida = capsys.readouterr() assert codigo == 0 assert "V20" not in saida.err def test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20(tmp_path, capsys): """TR (RAF-T19a): o mesmo plano, sem a flag, sai 1 com `V20 secao — versão pendente fora de sequência` no stderr.""" modelo = _load_modelo() raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path) codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)]) saida = capsys.readouterr() assert codigo == 1 assert "V20 secao — versão pendente fora de sequência" in saida.err ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `586 passed`, 2026-09-29, revisão da `RAF-T19`). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; `.claude/tools/modelo.py` e as fixtures de `tests/fixtures/modelo/` não mudam. - Os testes gravam só em `tmp_path`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `validar` nem `verbo_check` (a regra 3 já está entregue pela `RAF-T19`); não mudar `_raiz_modelo_pendente`, `_MODELO_PENDENTE_TEXTO` nem `_CARD_OP2_TEXTO`; não mexer nos quatro testes da `RAF-T19` nem no `test_tf_check_pendente_fora_de_sequencia_v20`.
- **Contingências:** - se um dos dois testes novos falhar → parar e sinalizar `blocked` razão `premissa`, nomeando o teste e a violação que saiu (a regra 3 da `RAF-T19` não está como o card a descreve). - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_so_vigente_pendente_fora_de_sequencia_nao_e_v20` — card `EX-T2` da `OP-2` presente e a `## 1A` em versão 3 contra a vigente 1: `check --so-vigente --root <raiz>` sai 0 sem `V20` no stderr (sem a guarda `not so_vigente`, sai 1 com a `V20`). TR `test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20` — o mesmo plano, sem a flag: sai 1 com `V20 secao — versão pendente fora de sequência` no stderr (a regra concorrente, o `check` sem a flag também calar a `V20`, sairia 0). Suíte `tests/test_modelo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T19` (`done`), que fica como executado; o contrato do objeto `conferência do modelo` (versão 3 pendente, `DRF-60`); o despacho com a flag (`RAF-T20`).
- **Handover:** 2026-09-29 · para `RAF-T21` - **Entregue:** tests/test_modelo.py: 2 testes novos (pendente em versão 3 contra vigente 1): check --so-vigente sai 0 sem V20; sem a flag sai 1 com V20; suíte 588 - **Contrato:** a regra 3 da RAF-T19 (so_vigente não emite V20) tem teste que a discrimina - **Não refazer:** os dois testes e o helper - **Pendente:** nenhum

## Execução

**Consumo:** 15 tool uses, 57.5 k tokens, 196.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

O card corretivo fecha o AE-169 com poder discriminante medido nesta revisao: numa copia temporaria fora do repositorio, trocar 'and not so_vigente' por 'and True' em validar (modelo.py:362) faz o TF novo sair 1 (1 failed, 5 passed no recorte so_vigente), e o TR tranca a regra concorrente. Verificacao 1 exit 0, tests/test_modelo.py 40 passed, modelo.py e fixtures sem diff desde o ref, nenhuma linha removida dos testes. OP-19 confere com a entrega: sem conflito de modelo novo.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A conferência do modelo julga só a versão vigente quando pedida" e vai pegar a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência".
Tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência" e vai executar: Quem executa acrescenta à suíte do `modelo.py` o caso que distingue a regra 3 da `RAF-T19`: com a versão pendente fora de sequência, o `check --so-vigente` não emite a `V20` e o `check` sem a flag a emite.
Agente executor devolveu a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência": review — sem pendência.
Tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O teste distingue o check com e sem --so-vigente pela versão pendente fora de sequência" como done: registrar estado, RDO e telemetria.
