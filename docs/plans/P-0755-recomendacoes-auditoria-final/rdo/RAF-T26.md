# RDO — P-0755 · RAF-T26

# Humano

Tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação" concluída em 2026-09-29.
O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 40/54 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T26` — O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md` - `.claude/agents/pantonic-consultant.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-model-designer.md').read_text(encoding='utf-8');print('promocao=%d-%d'%(t.count('o desfecho da pendente chega em novo dossiê'),t.count('Você só é chamado na promoção quando o comando encontra')))"` → `promocao=0-1` — antes `promocao=1-0`, depois `promocao=0-1` 2. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print('validacao=%d'%t.count('numa linha só, na forma'))"` → `validacao=1` — antes `validacao=0`, depois `validacao=1`

**Pronto quando:** - modelador.papel na promoção de versão — o modelador só é chamado quando o comando do marco encontra conflito — Verificação 1 - consultor.forma da validação da versão pendente — a definição do consultor dá a forma da linha de validação que o comando do marco cobra — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-17`, `DRF-38`; `F-21` (a promoção da `## 1A` é hoje do modelador, `pantonic-model-designer.md`; a validação prévia do consultor está em `pantonic-consultant.md` sem forma de linha); relatório `R-08` (auditoria reg. 37 e 38).
- **Depende de:** `RAF-T23`
- **Operação do modelo:** `OP-26` - OP-26: Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito. - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.
- **Camada e fronteira:** doutrina do kit — as definições do agente modelador (`.claude/agents/pantonic-model-designer.md`, lista de atos, ato **Emenda**, parágrafo `**No marco**`) e do agente consultor (`.claude/agents/pantonic-consultant.md`, a frase da validação no marco); nenhum código muda. O comportamento que a doutrina descreve já está no comando desde a `RAF-T23`: `encerrar.py marco --aceita-versao <k> --consultor "<linha>"` exige a linha do consultor, grava-a na célula do marco ao lado do veredito do dono, promove a `## 1A` (registro de versões com a anterior `obsoleta` e a frase `Caiu pelo aceite da versão <k> em <data>`) e reescreve o campo `Operação do modelo` dos cards das listas `tarefas:`; em conflito (a `## 1A` com outra versão, registro sem vigente único ou sem a linha pendente da versão), recusa e imprime o dossiê `Ato: emenda` para o modelador. A regra da promoção mora só no modelador, e a forma da linha só no consultor. O contrato do objeto "fechamento" é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Passos:** 1. Em `.claude/agents/pantonic-model-designer.md`, trocar as seis linhas do texto antigo pelas doze do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo). Texto antigo: ```text **No marco**, o desfecho da pendente chega em novo dossiê `Ato: emenda`, com a validação do consultor e o ato do dono em `Motivo`. Aceita: o conteúdo da `## 1A` passa à `## 1`, com o cabeçalho em `situação: vigente`; a `## 1A` sai do plano; no registro de versões a pendente passa a `vigente` e a anterior a `obsoleta`, com a frase `Caiu pelo aceite da versão <N> em <data>` — a linha fica, o conteúdo da obsoleta não. Recusada: a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*). ``` Texto novo: ```text **No marco**, a versão aceita é promovida pelo comando do marco, não por você (`R-08` da auditoria final, `P-0755`): `encerrar.py marco --aceita-versao <k> --consultor "<linha>"` passa o conteúdo da `## 1A` à `## 1`, com o cabeçalho em `situação: vigente`; tira a `## 1A` do plano; no registro de versões põe a pendente em `vigente` e a anterior em `obsoleta`, com a frase `Caiu pelo aceite da versão <N> em <data>` — a linha fica, o conteúdo da obsoleta não —; e reescreve o campo `Operação do modelo` dos cards das listas `tarefas:`. Você só é chamado na promoção quando o comando encontra **conflito** (a `## 1A` com outra versão, registro de versões sem vigente único ou sem a linha pendente da versão): o comando imprime o dossiê `Ato: emenda`, e você devolve a `## 1A` e o registro acertados para o comando rodar de novo. Recusada: o desfecho chega em dossiê `Ato: emenda`, com o ato do dono em `Motivo`; a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*). ``` 2. Em `.claude/agents/pantonic-consultant.md`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text No marco, você valida a versão pendente do modelo antes do dono (`GOVERNANCA.md` §3.2). ``` Trecho novo: ```text No marco, você valida a versão pendente do modelo antes do dono (`GOVERNANCA.md` §3.2), numa linha só, na forma `valido a versão <k>: <razão em uma frase>` ou `não valido a versão <k>: <razão em uma frase>`; só a primeira segue ao dono, e quem conduz a passa verbatim a `encerrar.py marco --aceita-versao <k> --consultor "<linha>"`, que a grava na célula do marco, ao lado do veredito do dono (`R-08` da auditoria final, `P-0755`). ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê `pantonic-model-designer.md`, e `tests/test_frontmatter_yaml.py` lê o frontmatter de `pantonic-consultant.md`, que o passo 2 não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nos atos **Autoria**, **Conflito** e **Leitura** do modelador nem no resto do ato **Emenda**; não editar `GOVERNANCA.md` (a ordem consultor → dono em §3.2 não muda); não mexer na triagem nem nas rotas do consultor; não acrescentar a origem do achado ao consultor (é da `RAF-T35`).
- **Contingências:** - se o texto antigo do passo 1 ou o trecho antigo do passo 2 não existir verbatim, uma única vez, no arquivo dele → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` e `tests/test_frontmatter_yaml.py` leem os dois arquivos.
- **Fora do escopo desta tarefa:** a promoção por comando e a cobrança da linha (`RAF-T23`); a origem citada no achado do consultor (`RAF-T35`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/agents/pantonic-model-designer.md sem a promoção de versão (agora do comando do marco); .claude/agents/pantonic-consultant.md com a forma da linha de validação da versão pendente (R-08) - **Contrato:** a promoção de versão é do encerrar.py marco; o consultor valida a pendente numa linha de forma fixa - **Não refazer:** as trocas nos dois agentes - **Pendente:** nenhum

## Execução

**Consumo:** 12 tool uses, 57.7 k tokens, 204.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Card de redacao com bloco cercado verbatim: a entrega bate byte a byte com o texto novo (12 linhas no modelador, contagem 1) e com o trecho novo do consultor (word-diff de uma unica troca), e as duas Verificacoes saem promocao=0-1 e validacao=1. O exercicio ponta a ponta das afirmacoes contra encerrar.py marco fechou para --aceita-versao, --consultor obrigatorio e de uma linha, escape de | na celula, frase 'Caiu pelo aceite' e reescrita do campo Operacao do modelo; e expos o que o card nao conferiu ao fixar o texto: o campo Devolver do dossie de conflito e o quarto caso de conflito.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "Quem conduz dá destino, no marco, ao card da operação nova que a rodada deixou bloqueado" e vai pegar a tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação".
Tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação" e vai executar: Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito.
Agente executor devolveu a tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação": review — sem pendência.
Tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O modelador sai da promoção de versão e o consultor ganha a forma da linha de validação" como done: registrar estado, RDO e telemetria.
