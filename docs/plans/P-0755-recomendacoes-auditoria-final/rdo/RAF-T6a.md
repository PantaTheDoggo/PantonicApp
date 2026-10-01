# RDO — P-0755 · RAF-T6a

# Humano

Tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha" concluída em 2026-09-29.
O filtro da saída dos testes passa a alcançar comando encadeado por OU lógico e por quebra de linha.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 10/44 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T6a` — O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o hook do filtro da saída dos testes alcançar também o comando encadeado por `||` ou por quebra de linha: a `RAF-T6` já divide esses segmentos, mas o `main()` do hook ainda devolve o comando sem filtro, porque lê o `||` como pipe e porque o pré-filtro não acha o pytest depois de `||` nem de quebra de linha.

**Arquivos-alvo:** - `.claude/global/hooks/pytest_pretooluse.py` - `tests/test_pytest_pretooluse.py`

**Verificação:** 1. `python -m pytest tests/test_pytest_pretooluse.py::test_tf_hook_reescreve_o_pytest_antes_do_ou_logico -q` → `exit 0` — antes `exit 4`, depois `exit 0` 2. `python -m pytest tests/test_pytest_pretooluse.py::test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha -q` → `exit 0` — antes `exit 4`, depois `exit 0` 3. `python -m pytest tests/test_pytest_pretooluse.py::test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough -q` → `exit 0` — antes `exit 4`, depois `exit 0`

**Pronto quando:** - filtro da saída dos testes.código de saída devolvido — o pytest antes do `||` entra no bloco filtrado, e o `||` lê o exit dos testes — Verificação 1 - filtro da saída dos testes.código de saída devolvido — o pytest depois do `||` e depois da quebra de linha entra no bloco filtrado — Verificação 2 - filtro da saída dos testes.código de saída devolvido — o pipe simples e o redirecionamento seguem sem filtro — Verificação 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-47`; `AE-130` (laudo da `RAF-T6`, ressalva 91); `DRF-10`; `F-7`; relatório `R-24`.
- **Depende de:** `RAF-T6`
- **Operação do modelo:** `OP-6` - OP-6: Quem executa faz o filtro da saída dos testes devolver o código de saída dos próprios testes, mesmo quando o comando encadeia outros passos depois deles. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** fonte canônica dos hooks globais do kit, em `.claude/global/hooks/`, só biblioteca padrão; o hook e o filtro não importam um ao outro. A projeção para a pasta do usuário (`~/.claude/hooks/`, declarada em `.claude/projecoes.json`) é ato do dono (`python .claude/tools/materializar.py apply`) e fica fora do card: a sessão segue com a projeção antiga até o dono aplicar (§8 risco 6). O contrato do objeto é: "Quem implementa corrige o filtro na cópia que o kit guarda; levá-lo à máquina do dono é ato do próprio dono."
- **Contratos/classes:** 1. `pytest_pretooluse.py` — o que fica verdade: `main()` segue devolvendo `{}` (`passthrough()`) para o comando com pipe simples (`|` que não é metade de `||`) ou com redirecionamento (`<`, `>`); o `||` deixa de contar como pipe; e o pré-filtro `PYTEST_RE` acha o pytest também no começo do segmento que vem depois de `||` ou de quebra de linha. `FILTER_PATH`, `SEGMENTO_PYTEST_RE`, `dividir_segmentos()`, `reescrever()`, `passthrough()` e as demais condições de passthrough (`#nofilter`, `pytest_filter`, `--collect-only`/`--co`) ficam inalterados. O docstring do módulo passa a dizer que a recusa é do pipe simples e do redirecionamento. A técnica é do executor; a ensaiada pelo consultor em cópia (2026-09-28) foi uma constante nova de módulo, usada no lugar do `any(...)` da primeira condição de passthrough de `main()`, e o prefixo de `PYTEST_RE` com `|` e quebra de linha na classe de separadores (as quebras são as do bloco): ```text PIPE_OU_REDIRECIONAMENTO_RE = re.compile(r"(?<!\|)\|(?!\|)|[<>]") PYTEST_RE, primeira linha:  r"(?:^|[;&|\n]\s*)" ```
- **Passos:** 1. Acrescentar a `tests/test_pytest_pretooluse.py` os três testes da seção `Testes`, com os auxiliares que o arquivo já tem (`_rodar_hook`, `_filtro_path_esperado`). 2. Rodar `python -m pytest tests/test_pytest_pretooluse.py -q` e conferir que os dois TF falham e os cinco testes da `RAF-T6` passam. 3. Aplicar o item 1 de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `541 passed`, 2026-09-28, handover da `RAF-T6`). - Os cinco testes da `RAF-T6` em `tests/test_pytest_pretooluse.py` seguem verdes e sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - `.claude/global/hooks/pytest_pretooluse.py` segue com fim de linha LF (`git ls-files --eol` mostra `w/lf` antes e depois). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não rodar `python .claude/tools/materializar.py apply` nem copiar os arquivos para `~/.claude/hooks/` (ato do dono); não mudar `FILTER_PATH`, `.claude/projecoes.json` nem `.claude/global/hooks/pytest_filter.py`; não mudar `dividir_segmentos()` nem `reescrever()`; não deixar de recusar o pipe simples e o redirecionamento.
- **Contingências:** - se um dos cinco testes da `RAF-T6` cair depois do passo 3 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se um teste de `tests/test_materializar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_hook_reescreve_o_pytest_antes_do_ou_logico` — ferramenta `Bash`, comando `pytest -q || echo falhou`: o comando reescrito é exatamente `{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>" || echo falhou` (hoje o hook devolve `{}`). TF `test_tf_hook_reescreve_o_pytest_depois_do_ou_logico_e_da_quebra_de_linha` — ferramenta `Bash`: `false || pytest -q` reescrito exatamente `false || <bloco>`, e `cd x`, quebra de linha, `pytest -q` reescrito exatamente `cd x`, quebra de linha, `<bloco>`, sendo `<bloco>` o `{ pytest -q; echo "__PYTEST_EXIT__=$?"; } 2>&1 | python "<filtro>"` (hoje os dois devolvem `{}`). TR `test_tr_hook_pipe_simples_e_redirecionamento_seguem_passthrough` — ferramenta `Bash`: `pytest -q | tail -5` e `pytest -q > out.txt` devolvem `{}`. `<filtro>` é o `FILTER_PATH` lido do hook, como nos testes da `RAF-T6`. Suíte `tests/test_pytest_pretooluse.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** levar o hook corrigido a `~/.claude/hooks/` (ato do dono, §4 invariante 8); pipe ou redirecionamento dentro de aspas (segue recusado, como na `RAF-T6`); o filtro `pytest_filter.py` (`RAF-T6`, entregue).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** pytest_pretooluse.py recusa só pipe simples e redirecionamento (PIPE_OU_REDIRECIONAMENTO_RE) e PYTEST_RE acha o pytest depois de ||, | e quebra de linha; 3 testes novos, suíte 544 - **Contrato:** comando encadeado por || ou quebra de linha com pytest é filtrado e devolve o exit dos testes; projeção em ~/.claude/hooks é ato do dono (materializar.py apply) - **Não refazer:** a regex nova e os 3 testes - **Pendente:** pipe ou redirecionamento dentro de aspas ainda recusa o filtro (matéria inconclusiva no cenário); contorno de ferramenta negada em triagem do consultor

## Execução

**Consumo:** 25 tool uses, 75.8 k tokens, 568.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta na revisao: 17 variantes de comando pelo hook da arvore (||, quebra de linha LF e CRLF, &&, ;, pipe com e sem espaco, <, >, 2>&1, --co, #nofilter) casam com o contrato; no Bash, o || depois do bloco filtrado dispara com o exit 1 do teste e nao dispara com exit 0 (filtro do kit). Borda sem efeito pratico: 'pytest -q ||| x' e reescrito e segue erro de sintaxe como o original. A projecao ~/.claude/hooks/pytest_pretooluse.py segue a antiga (2026-07-03), como o card manda: o filtro corrigido so vale na sessao depois do materializar.py apply do dono.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O filtro do pytest devolve o exit dos testes no comando encadeado" e vai pegar a tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha".
Tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha" e vai executar: Quem executa faz o hook do filtro da saída dos testes alcançar também o comando encadeado por `||` ou por quebra de linha: a `RAF-T6` já divide esses segmentos, mas o `main()` do hook ainda devolve o comando sem filtro, porque lê o `||` co…
Agente executor devolveu a tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha": This agent's report was delivered to you as a message from "ab3a2bfc664487c8b" (its SubagentHandback call), under a SECURITY WARNING from auto mode — the warnin….
Tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O filtro do pytest alcança o comando encadeado por OU lógico e por quebra de linha" como done: registrar estado, RDO e telemetria.
