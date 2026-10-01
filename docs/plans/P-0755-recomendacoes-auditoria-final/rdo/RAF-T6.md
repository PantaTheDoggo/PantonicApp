# RDO — P-0755 · RAF-T6

# Humano

Tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado" concluída em 2026-09-28.
O filtro da saída dos testes passa a devolver o código de saída dos próprios testes mesmo com passos encadeados depois deles.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 9/43 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T6` — O filtro do pytest devolve o exit dos testes no comando encadeado
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles.

**Arquivos-alvo:** - `.claude/global/hooks/pytest_pretooluse.py` - `.claude/global/hooks/pytest_filter.py` - `tests/test_pytest_pretooluse.py`

**Verificação:** 1. `python -m pytest tests/test_pytest_pretooluse.py -q` → `exit 0` — antes `exit 4`, depois `exit 0`

**Pronto quando:** - filtro da saída dos testes.código de saída devolvido — volta o código de saída dos testes, também no comando encadeado, nas duas linhas de comando que o kit usa — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-10`; `F-7` (a fonte é `.claude/global/hooks/`; a projeção em `~/.claude/hooks/` é ato do dono), `F-12`; relatório `R-24`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-6` - OP-6: Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** fonte canônica dos hooks globais do kit, em `.claude/global/hooks/`, só biblioteca padrão; o hook e o filtro não importam um ao outro. A projeção para a pasta do usuário (`~/.claude/hooks/`, declarada em `.claude/projecoes.json`) é ato do dono (`python .claude/tools/materializar.py apply`) e fica fora do card: a sessão segue com a projeção antiga até o dono aplicar (§8 risco 6). O contrato do objeto é: "Quem implementa corrige o filtro na cópia que o kit guarda; levá-lo à máquina do dono é ato do próprio dono."
- **Contratos/classes:** 1. `pytest_pretooluse.py` — `FILTER_PATH`, `PYTEST_RE`, `passthrough()` e as cinco condições de passthrough de `main()` inalterados. Três nomes novos de módulo: `SEGMENTO_PYTEST_RE` = `PYTEST_RE` sem o prefixo de início ou separador, ancorado no começo (`^(?:\S*python(?:3)?(?:\.exe)?\s+-m\s+)?(?:\S*[/\\])?pytest(?:\.exe)?(?:\s|$)`); `dividir_segmentos(cmd: str) -> list[str]` — as partes do comando alternando segmento e separador, com separador `&&`, `||`, `;` ou quebra de linha, reconhecido só fora de aspas simples ou duplas (a primeira e a última parte são segmentos; `"".join(partes) == cmd`); `reescrever(cmd: str, ferramenta: str) -> str | None` — cada segmento cujo texto sem espaços nas pontas casa `SEGMENTO_PYTEST_RE` troca o texto (espaços das pontas preservados) pelo bloco abaixo, conforme a ferramenta, e o resto do comando fica como está; nenhum segmento do pytest → `None`. Em `main()`, a linha `new_cmd = f'{cmd} 2>&1 | python "{FILTER_PATH}"'` vira `new_cmd = reescrever(cmd, data.get("tool_name"))`, e `None` cai em `passthrough()`. Blocos exatos (as quebras são as do bloco; `<segmento>` é o texto do segmento sem espaços nas pontas; `<filtro>` é o valor de `FILTER_PATH`): ```text Bash:       { <segmento>; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>" PowerShell: & { <segmento>; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "<filtro>" ``` 2. `pytest_filter.py` — constante nova `MARCADOR_EXIT_RE = re.compile(r"^__PYTEST_EXIT__=(-?\d+)$")`; a leitura do stdin tira de `lines` toda linha que, sem espaços nas pontas, casa o marcador (guardando o último exit lido); o log e o que se imprime não trazem o marcador; com marcador lido, o filtro sai com esse exit (`sys.exit(<exit>)`) no lugar da regra do sumário; sem marcador, a regra de hoje (0 se passou; 1 com falha, erro ou saída irreconhecível) não muda. Os docstrings dos dois arquivos passam a descrever a regra nova.
- **Passos:** 1. Criar `tests/test_pytest_pretooluse.py` com os cinco testes da seção `Testes`: o hook roda por subprocesso (`sys.executable` e o caminho do hook, o JSON no stdin, o stdout lido como JSON); o `FILTER_PATH` esperado se lê carregando o hook por `importlib.util.spec_from_file_location`; o filtro roda por subprocesso com o texto no stdin e com `TMPDIR`, `TEMP` e `TMP` apontando para `tmp_path`, para o log não cair na pasta temporária do usuário. 2. Rodar `python -m pytest tests/test_pytest_pretooluse.py -q` e conferir que os três TF falham. 3. Aplicar os itens 1 e 2 de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhum teste lê nem escreve a pasta do usuário: o filtro grava o log em `tmp_path`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não rodar `python .claude/tools/materializar.py apply` nem copiar os arquivos para `~/.claude/hooks/` (ato do dono); não mudar `FILTER_PATH`; não mudar `.claude/projecoes.json`; não mudar as condições de passthrough (pipe ou redirecionamento no comando, `#nofilter`, `--collect-only`).
- **Contingências:** - se um teste de `tests/test_materializar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_hook_reescreve_so_o_segmento_do_pytest_no_bash` — ferramenta `Bash`, comando `cd x && pytest -q; echo "exit=$?"`: o comando reescrito é exatamente `cd x && { pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>"; echo "exit=$?"` (hoje o pipe vai ao fim do comando inteiro e o `echo` final lê o exit do filtro). TF `test_tf_hook_reescreve_so_o_segmento_do_pytest_no_powershell` — ferramenta `PowerShell`, comando `python -m pytest -q; Write-Output "fim"`: reescrito exatamente `& { python -m pytest -q; "__PYTEST_EXIT__=$LASTEXITCODE" } 2>&1 | python "<filtro>"; Write-Output "fim"`. TR `test_tr_hook_sem_pytest_segue_passthrough` — ferramenta `Bash`, comando `git status`: stdout é `{}`. TF `test_tf_filtro_sai_com_o_exit_do_marcador` — stdin `3 passed in 0.10s` e `__PYTEST_EXIT__=5`, uma por linha: exit 5, stdout sem `__PYTEST_EXIT__` e com `3 passed in 0.10s` (hoje o filtro sai 0, pelo sumário). TR `test_tr_filtro_sem_marcador_segue_pelo_sumario` — stdin `1 failed, 2 passed in 0.10s`: exit 1; stdin `3 passed in 0.10s`: exit 0. Suíte `tests/test_pytest_pretooluse.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** levar o hook e o filtro corrigidos a `~/.claude/hooks/` (ato do dono, §4 invariante 8); o gatilho do próximo passo (`RAF-T5`).
- **Handover:** 2026-09-28 · para quem vier depois - **Entregue:** filtro do pytest (.claude/global/hooks/pytest_pretooluse.py e pytest_filter.py) devolve o exit dos testes quando o comando encadeia passos depois deles; 5 testes novos em tests/test_pytest_pretooluse.py, suíte 541 - **Contrato:** o exit do comando reescrito é o dos testes; a projeção em ~/.claude/hooks é ato do dono (materializar.py apply) - **Não refazer:** dividir_segmentos e a reescrita do exit, com os testes - **Pendente:** comando encadeado por || não chega a reescrever(): o passthrough de main() recusa qualquer pipe (em triagem do consultor)

## Execução

**Consumo:** 30 tool uses, 86.9 k tokens, 341.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O gatilho do próximo passo responde só ao dono" e vai pegar a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado".
Tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado" e vai executar: Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles.
Agente executor devolveu a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado": review — sem pendência.
Tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado" como done: registrar estado, RDO e telemetria.
