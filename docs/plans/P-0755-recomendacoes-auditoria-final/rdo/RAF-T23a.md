# RDO — P-0755 · RAF-T23a

# Humano

Tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py" concluída em 2026-09-29.
O comando do marco passa a reconhecer a versão pendente pela mesma regra do modelo.py.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 36/53 tarefas concluídas; próxima: "Quem conduz segue a janela quando o modelador cria operação nova e enfileira a rodada".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T23a` — O comando do marco reconhece a versão pendente pela mesma regra do modelo.py
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o comando do marco reconhecer a `## 1A` pela mesma regra que o `modelo.py` usa, recusando com a mensagem de erro do marco o cabeçalho que ele não lê, em vez de cair em exceção não tratada.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py -q -k cabecalho_1a` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - fechamento.promoção da versão aceita — havendo conflito, o comando do marco recusa antes de escrever; a `## 1A` que o `modelo.py` não lê sai com a mensagem de erro do marco, não com exceção não tratada — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-62`; `AE-176` (laudo da `RAF-T23`, ressalva 91: a pré-checagem de `gravar_marco` aceita a `## 1A` por prefixo, com `_MARCO_VERSAO_PENDENTE_RE`, e o `_checar_promocao` a lê por igualdade exata, com `_modelo._HEADING_PENDENTE` via `_localizar_secao`; o cabeçalho com texto a mais passa a pré-checagem e derruba `_checar_promocao` em `AttributeError`). Medido pelo consultor em cópia (2026-09-29): com o teste abaixo e sem a regra, o teste sai `1 failed` com `AttributeError: 'NoneType' object has no attribute 'versao'`; com a regra, `1 passed`, e `tests/test_encerrar.py` inteiro `43 passed`.
- **Depende de:** `RAF-T23`
- **Operação do modelo:** `OP-23` - OP-23: Quem executa faz o fechamento do marco promover sozinho a versão aceita, cobrando a linha de validação do consultor e acertando o texto da operação em cada card. - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `marco` (`gravar_marco`); só biblioteca padrão. A regra que fica é a do `modelo.py` (`_localizar_secao`: linha igual a `_HEADING_PENDENTE`), que o `check`, o `show` e a promoção já usam; a pré-checagem de `gravar_marco` passa a usá-la, e a regra do prefixo sai do arquivo. Vale para `--aceita-versao` e para `--recusa-versao`: a `## 1A` que o `modelo.py` não lê não é versão pendente para o marco.
- **Contratos/classes:** assinaturas inalteradas. Duas regras em `.claude/tools/encerrar.py`: 1. A linha da constante `_MARCO_VERSAO_PENDENTE_RE = re.compile(...)` sai (seu único uso é o da regra 2). 2. `gravar_marco`, a checagem `if (aceita_versao is not None or recusa_versao is not None) and not any(...)`: o gerador `_MARCO_VERSAO_PENDENTE_RE.match(l) for l in linhas` passa a `l == _modelo._HEADING_PENDENTE for l in linhas`; logo acima do `if`, um comentário de três linhas no máximo diz que a `## 1A` se reconhece pela mesma regra do `modelo.py` (igualdade exata com `_HEADING_PENDENTE`) e cita `AE-176` e `RAF-T23a` do `P-0755`. A mensagem `plano sem versão pendente (## 1A)` não muda.
- **Passos:** 1. Acrescentar ao fim de `tests/test_encerrar.py` o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0; duas linhas vazias antes do `def`). ```python def test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente(tmp_path, capsys): """TF (RAF-T23a, `AE-176`): a `## 1A` cujo cabeçalho tem texto a mais não é a versão pendente que o `modelo.py` lê (igualdade exata com `_modelo._HEADING_PENDENTE`); a pré-checagem do marco usa a mesma regra e recusa antes de escrever, em vez de passar pelo prefixo e cair em `AttributeError` dentro de `_checar_promocao`.""" texto = PLANO_MARCO_PROMOCAO.replace("@TAREFAS_OP1@", "MRC-T2").replace( "## 1A. Modelo conceitual — versão pendente de validação", "## 1A. Modelo conceitual — versão pendente de validação (rascunho)", ) repo = _montar_repo_marco(tmp_path, texto) plano = repo / "docs" / "plans" / "P-0001-marco.md" antes = plano.read_text(encoding="utf-8") exit_code = encerrar.main(_argv_marco( repo, **{ "--marco": "2", "--resultado": "go", "--veredito": "Aceito a versão 2", "--aceita-versao": "2", "--consultor": "valido a versão 2", }, )) assert exit_code == 1 assert "marco: plano sem versão pendente (## 1A)" in capsys.readouterr().err assert plano.read_text(encoding="utf-8") == antes ``` 2. Rodar `python -m pytest tests/test_encerrar.py -q -k cabecalho_1a` e conferir que o teste falha com `AttributeError`. 3. Aplicar as duas regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o teste novo (referência datada: `601 passed`, 2026-09-29, revisão da `RAF-T23`). Os testes de `marco` que já existem, inclusive `test_tf_marco_recusa_versao_imprime_dossie_de_emenda` e os cinco da `RAF-T23`, continuam passando sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - `grep -c _MARCO_VERSAO_PENDENTE_RE .claude/tools/encerrar.py` sai `0` ao fim. - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Os testes gravam só em `tmp_path`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_checar_promocao`, `promover_versao` nem `_dossie_emenda`; não mudar `_HEADING_PENDENTE` nem nada do `.claude/tools/modelo.py`; não mudar a mensagem `plano sem versão pendente (## 1A)`; não mexer nos testes que já existem.
- **Contingências:** - se o teste novo não falhar no Passo 2 → parar e sinalizar `blocked` razão `premissa`, com a saída do teste (a pré-checagem não está como o card a descreve). - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_marco_cabecalho_1a_com_texto_a_mais_recusa_sem_pendente` — plano da promoção com o cabeçalho da `## 1A` seguido de ` (rascunho)`, `--aceita-versao 2 --consultor "valido a versão 2"`: sai 1 com `marco: plano sem versão pendente (## 1A)` no stderr e o plano byte a byte igual (a regra concorrente, o prefixo, deixa passar e derruba `_checar_promocao` em `AttributeError`). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a promoção e a cobrança do consultor (`RAF-T23`, entregues); a doutrina da promoção (`RAF-T26`); o verbo `tarefa` (`RAF-T30`).
- **Handover:** 2026-09-29 · para `RAF-T30` - **Entregue:** encerrar.py: pré-checagem de gravar_marco reconhece a ## 1A por igualdade com _modelo._HEADING_PENDENTE (constante _MARCO_VERSAO_PENDENTE_RE removida); 1 teste novo - **Contrato:** cabeçalho de 1A com texto a mais sai 'marco: plano sem versão pendente (## 1A)', exit 1, plano intacto - **Não refazer:** a regra única do cabeçalho e o teste - **Pendente:** nenhum

## Execução

**Consumo:** 18 tool uses, 61.9 k tokens, 193.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta do verbo marco em repositorios temporarios (fixture PLANO_MARCO_PROMOCAO, fora da arvore): com a regra nova, --recusa-versao com cabecalho '(rascunho)', --aceita-versao com espaco final no cabecalho e plano sem ## 1A saem todos exit 1 com 'marco: plano sem versao pendente (## 1A)' e o plano byte a byte igual; cabecalho exato segue exit 0 no aceite e na recusa. A pre-checagem, o _checar_promocao e o _dossie_emenda leem agora a ## 1A pela mesma igualdade com _modelo._HEADING_PENDENTE; grep de _MARCO_VERSAO_PENDENTE_RE em encerrar.py sai 0; tests/test_encerrar.py 43 passed.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O comando do marco promove a versão aceita e cobra a validação do consultor" e vai pegar a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py".
Tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py" e vai executar: Quem executa faz o comando do marco reconhecer a `## 1A` pela mesma regra que o `modelo.py` usa, recusando com a mensagem de erro do marco o cabeçalho que ele não lê, em vez de cair em exceção não tratada.
Agente executor devolveu a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py": review — sem pendência.
Tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O comando do marco reconhece a versão pendente pela mesma regra do modelo.py" como done: registrar estado, RDO e telemetria.
