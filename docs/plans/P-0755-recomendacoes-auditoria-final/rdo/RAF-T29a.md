# RDO — P-0755 · RAF-T29a

# Humano

Tarefa "O cabeçalho do controle do backlog conta o vocabulário do check até C-18" concluída em 2026-09-29.
A documentação do controle do backlog passou a contar as violações do check até a C-18.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 47/58 tarefas concluídas; próxima: "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T29a` — O cabeçalho do controle do backlog conta o vocabulário do check até C-18
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz as três frases de `.claude/tools/backlog.py` que contam o vocabulário do `check` dizerem `C-1..C-18`, com a `C-18` nomeada no comentário da seção do `check`.

**Arquivos-alvo:** - `.claude/tools/backlog.py`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/tools/backlog.py').read_text(encoding='utf-8');print('vocabulario=%d-%d-%d linhas=%d'%(t.count('C-1..C-17'),t.count('C-1..C-18'),t.count('via _prefixo_decisoes_checks'),len(t.splitlines())))"` → `vocabulario=0-3-1 linhas=2613` — antes `vocabulario=3-0-0 linhas=2612`, depois `vocabulario=0-3-1 linhas=2613`

**Pronto quando:** - controle do backlog.prefixo de decisão repetido — o cabeçalho do instrumento conta o vocabulário do check até C-18 e nomeia quem acusa o prefixo repetido — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-67`; `AE-184` (laudo da `RAF-T29`, ressalva 91, critério (viii) da rubrica); `DRF-29`; relatório `R-28`.
- **Depende de:** `RAF-T29`
- **Operação do modelo:** `OP-29` - OP-29: Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo. - precisa de: controle do backlog — Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/backlog.py` — as linhas 3 e 7 do docstring do módulo e o comentário da seção do `check` (linhas 592-595); nenhum comportamento muda. A `RAF-T29` acrescentou a violação `C-18` (`_prefixo_decisoes_checks`) e deixou as três frases que contam o vocabulário em `C-1..C-17`. Fora do módulo, nenhuma enumeração viva conta o vocabulário: `tests/test_backlog.py` linha 2 é o docstring atribuído à `BKL-T2` (`C-1..C-9`, o que aquele card testou) e `docs/OPERACOES_AS_IS_P-0751.md` linha 412 é medida datada; os dois ficam.
- **Passos:** 1. No docstring do módulo de `.claude/tools/backlog.py`, trocar `` (`C-1..C-17`, vocabulário fechado `` por `` (`C-1..C-18`, vocabulário fechado `` (linha 3) e `` fechado em `C-1..C-17`; `` por `` fechado em `C-1..C-18`; `` (linha 7); o resto das duas linhas fica. 2. No comentário da seção do `check`, trocar as quatro linhas do texto antigo pelas cinco do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text # check — violações C-1..C-17 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a: # check é o chamador de produção, nenhum subcomando novo; C-12 via _depende_checks — TK-65a; # C-15 acusa tíquete vivo sem subtarefa — EBK-T1; C-16 confronta card vivo com a leitura de # dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2) ``` Texto novo: ```text # check — violações C-1..C-18 (C-11 via resolver_citacao_secao, definido abaixo — TK-60a: # check é o chamador de produção, nenhum subcomando novo; C-12 via _depende_checks — TK-65a; # C-15 acusa tíquete vivo sem subtarefa — EBK-T1; C-16 confronta card vivo com a leitura de # dossiê do rdo.py e C-17 acusa entrada órfã de piso_c11 — EBK-T2; C-18 acusa o prefixo de # decisão que dois planos declaram, via _prefixo_decisoes_checks — RAF-T29 do P-0755) ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `.claude/tools/backlog.py` só mudam as linhas 3 e 7 e o comentário das linhas 592-595: nenhum código, nome, regex, constante nem outro docstring muda; o arquivo segue LF (hoje 0 CR). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não tocar `tests/test_backlog.py` nem `docs/OPERACOES_AS_IS_P-0751.md`; não mudar o texto das violações nem os docstrings de `_prefixo_decisoes_checks` e `_numero_do_plano`.
- **Contingências:** - se o texto antigo de um passo não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring do módulo nem o comentário); `tests/test_backlog.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T29` (`done`), que fica como executado; o docstring do teste atribuído à `BKL-T2`.
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/backlog.py linhas 3 e 7 do docstring e o comentário da seção check (592-596) contam C-1..C-18 e nomeiam _prefixo_decisoes_checks - **Contrato:** o cabeçalho do backlog.py conta o vocabulário do check como o código o tem - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 17 tool uses, 54.9 k tokens, 321.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O cabeçalho do controle do backlog conta o vocabulário do check até C-18": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O cabeçalho do controle do backlog conta o vocabulário do check até C-18" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O cabeçalho do controle do backlog conta o vocabulário do check até C-18": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O cabeçalho do controle do backlog conta o vocabulário do check até C-18" como done: registrar estado, RDO e telemetria.
