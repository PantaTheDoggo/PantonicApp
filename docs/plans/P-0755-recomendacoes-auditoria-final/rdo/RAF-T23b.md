# RDO — P-0755 · RAF-T23b

# Humano

Tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa" concluída em 2026-09-29.
O dossiê do comando do marco passa a pedir ao modelador o que ele de fato devolve, no conflito e na recusa.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 41/56 tarefas concluídas; próxima: "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T23b` — O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o campo `Devolver` do dossiê `Ato: emenda` que o comando do marco imprime pedir ao modelador, no conflito da promoção, a `## 1` e a `## 1A` acertadas para o comando rodar de novo, e, na recusa da versão, a `## 1` sem a linha da versão recusada e o plano sem a `## 1A`.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py -q -k devolver` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print('devolver=%d-%d'%(t.count('linha nova do registro'),t.count('rodar de novo')))"` → `devolver=0-1` — antes `devolver=1-0`, depois `devolver=0-1`

**Pronto quando:** - fechamento.promoção da versão aceita — havendo conflito, o comando do marco recusa e prepara o pedido ao modelador com o que o modelador acerta: a `## 1` e a `## 1A`, com o registro de versões, para o comando rodar de novo — Verificação 1, Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-64`; `AE-180` (laudo da `RAF-T26`, ressalva 90: o dossiê de conflito que `_dossie_emenda` monta pede "a seção ## 1 depois do ato e a linha nova do registro de versões", que é o que o próprio comando faz na promoção, e não o que o modelador acerta no conflito). O mesmo texto serve hoje à recusa, onde a `## 1A` e a linha dela saem e nenhuma linha nova entra no registro (`GOVERNANCA.md` §3.2; ato **Emenda** do modelador). Medido pelo consultor em cópia (2026-09-29): árvore real `-k devolver` `exit 5`; com os dois testes abaixo e sem a regra, `2 failed`; com a regra, `2 passed`, e `tests/test_encerrar.py` inteiro `45 passed`.
- **Depende de:** `RAF-T23a`
- **Operação do modelo:** `OP-23` - OP-23: Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card. - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `marco`; só biblioteca padrão. `_dossie_emenda` é chamada em dois lugares, o `_conflito` de `_checar_promocao` e o fim de `gravar_marco` no ramo `--recusa-versao`, e hoje fixa o mesmo `Devolver` para os dois; o texto passa a vir de quem chama. As linhas `Plano`, `Ato`, `Motivo`, `Fato novo` e `Restrição` não mudam, nem as razões de conflito, nem a ordem das checagens.
- **Contratos/classes:** Três regras em `.claude/tools/encerrar.py`: 1. `_dossie_emenda` ganha o parâmetro posicional `devolver: str`, depois de `restricao` (um parâmetro por linha na assinatura); a linha fixa `"Devolver: a seção ## 1 depois do ato e a linha nova do registro de versões.",` passa a `f"Devolver: {devolver}",`; o docstring acrescenta que o `Devolver` difere entre a recusa da versão e o conflito na promoção e cita `RAF-T23b`. 2. O `_conflito` de `_checar_promocao` passa a `_dossie_emenda`, depois de `restricao`, o texto `"a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do marco rodar de novo."` 3. O ramo `--recusa-versao` de `gravar_marco` passa a `_dossie_emenda`, depois de `restricao`, o texto `"a seção ## 1 depois do ato, com o registro de versões sem a linha da versão recusada, e o plano sem a ## 1A."`
- **Passos:** 1. Acrescentar ao fim de `tests/test_encerrar.py` o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0; duas linhas vazias antes de cada `def`). ```python def test_tf_marco_conflito_devolver_pede_a_1_e_a_1a(tmp_path, capsys): """TF (RAF-T23b, `AE-180`): no conflito da promoção o modelador acerta o que está (a `## 1`, a `## 1A` e o registro de versões) para o comando rodar de novo; o `Devolver` do dossiê não pede a seção depois do ato nem linha nova do registro, que o comando faz.""" repo = _montar_repo_promocao(tmp_path) exit_code = encerrar.main(_argv_marco( repo, **{ "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 3", "--aceita-versao": "3", "--consultor": "valido a versão 3", }, )) assert exit_code == 1 saida = capsys.readouterr().out assert ( "Devolver: a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do " "marco rodar de novo." in saida ) assert "linha nova do registro" not in saida def test_tf_marco_recusa_devolver_sem_linha_nova_do_registro(tmp_path, capsys): """TF (RAF-T23b, `AE-180`): na recusa a `## 1A` e a linha dela saem e a vigente fica sem marca (`GOVERNANCA.md` §3.2); o `Devolver` do dossiê pede a `## 1` com o registro sem a linha da versão recusada, não uma linha nova.""" repo = _montar_repo_marco(tmp_path) exit_code = encerrar.main(_argv_marco( repo, **{ "--marco": "1", "--resultado": "no-go", "--veredito": "Não aceito", "--recusa-versao": "2", }, )) assert exit_code == 0 saida = capsys.readouterr().out assert ( "Devolver: a seção ## 1 depois do ato, com o registro de versões sem a linha da versão " "recusada, e o plano sem a ## 1A." in saida ) assert "linha nova do registro" not in saida ``` 2. Rodar `python -m pytest tests/test_encerrar.py -q -k devolver` e conferir que os dois testes falham. 3. Aplicar as três regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os dois testes novos (referência datada: `602 passed`, 2026-09-29, revisão da `RAF-T26`). Os testes de `marco` que já existem, inclusive `test_tf_marco_recusa_versao_imprime_dossie_de_emenda` e `test_tf_marco_promove_versao_conflito_imprime_dossie`, continuam passando sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Os testes gravam só em `tmp_path`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar as razões de conflito nem a ordem das checagens de `_checar_promocao`; não mudar `promover_versao` nem as linhas `Plano`, `Ato`, `Motivo`, `Fato novo` e `Restrição` do dossiê; não editar a doutrina do modelador (é da `RAF-T26a`); não mexer nos testes que já existem.
- **Contingências:** - se os testes novos não falharem os dois no Passo 2 → parar e sinalizar `blocked` razão `premissa`, com a saída do teste (o dossiê não está como o card o descreve). - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marco_conflito_devolver_pede_a_1_e_a_1a` — plano da promoção com a `## 1A` na versão 2 e `--aceita-versao 3 --consultor "valido a versão 3"`: sai 1 e o stdout traz o `Devolver` do conflito, sem `linha nova do registro`. TF `test_tf_marco_recusa_devolver_sem_linha_nova_do_registro` — plano do marco com `--resultado no-go --recusa-versao 2`: sai 0 e o stdout traz o `Devolver` da recusa, sem `linha nova do registro`. Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a doutrina do modelador sobre o conflito na promoção (`RAF-T26a`); o verbo `tarefa` (`RAF-T30`).
- **Handover:** 2026-09-29 · para `RAF-T26a` - **Entregue:** encerrar.py: _dossie_emenda ganhou o parâmetro devolver; o conflito pede a ## 1 e a ## 1A acertadas com o registro para o marco rodar de novo, e a recusa pede a ## 1 depois do ato sem a linha da versão recusada e sem a ## 1A; 2 testes novos - **Contrato:** o dossiê do comando do marco pede ao modelador o que ele devolve em cada ramo - **Não refazer:** o parâmetro devolver e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 34 tool uses, 75.1 k tokens, 367.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta do verbo marco em repositorios temporarios (fixture PLANO_MARCO_PROMOCAO, fora da arvore): os quatro ramos de conflito de _checar_promocao (a ## 1A em outra versao, plano sem ## 1, registro sem vigente unico, registro sem a linha pendente) saem todos exit 1, plano byte a byte intacto, com o mesmo Devolver do conflito; a recusa sai exit 0 com o Devolver da recusa; a promocao valida sai exit 0 sem dossie. Isso fecha tambem a parte (b) do AE-180 do lado do comando: o quarto conflito ('o plano nao tem a ## 1') imprime o dossie com o Devolver novo. tests/test_encerrar.py 45 passed; Verificacao 2 re-rodada devolver=0-1.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa" e vai executar: Quem executa faz o campo `Devolver` do dossiê `Ato: emenda` que o comando do marco imprime pedir ao modelador, no conflito da promoção, a `## 1` e a `## 1A` acertadas para o comando rodar de novo, e, na recusa da versão, a `## 1` sem a lin…
Agente executor devolveu a tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa": review — sem pendência.
Tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa" como done: registrar estado, RDO e telemetria.
