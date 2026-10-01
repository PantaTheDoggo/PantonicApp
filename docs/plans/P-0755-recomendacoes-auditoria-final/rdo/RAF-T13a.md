# RDO — P-0755 · RAF-T13a

# Humano

Tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1" concluída em 2026-09-29.
A ajuda e o docstring da conferência do card passam a descrever o mundo depois como ele funciona.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 24/51 tarefas concluídas; próxima: "A conferência do card roda o git de leitura contra o recorte do despacho".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T13a` — O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o docstring do módulo e a ajuda da opção `--mundo` da conferência de verificação do card dizerem o que a regra 1 da `RAF-T13` entregou: no mundo `depois` a forma 8.1 compara com o literal do esperado, e o mundo vale nas duas formas.

**Arquivos-alvo:** - `.claude/tools/card_check.py`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/tools/card_check.py').read_text(encoding='utf-8');print('docstring=%d-%d help=%d-%d'%(t.count('declarado — divergência'),t.count('para o mundo comparado ('),t.count('comparar na forma inline'),t.count('comparar nas duas formas')))"` → `docstring=0-1 help=0-1` — antes `docstring=1-0 help=1-0`, depois `docstring=0-1 help=0-1`

**Pronto quando:** - conferência de verificação do card.resultado esperado no bloco cercado — o docstring do módulo e a ajuda de `--mundo` dizem que o mundo `depois` da forma 8.1 compara com o literal do esperado e que o mundo vale nas duas formas — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-55`; `AE-155` (laudo da `RAF-T13`, ressalva 91); relatório `R-09`.
- **Depende de:** `RAF-T13`
- **Operação do modelo:** `OP-13` - OP-13: Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/card_check.py` — o docstring do módulo (linhas 5-7) e o `help` da opção `--mundo` em `main`; nenhum comportamento muda. A `RAF-T13` trocou só o docstring de `verificar_tarefa` (a regra 3 do card nomeou só ele); os outros dois textos seguiram dizendo que a conferência compara com o `Medido antes` e que o mundo só vale na forma inline.
- **Passos:** 1. No docstring do módulo de `.claude/tools/card_check.py`, trocar as três linhas do texto antigo pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text item e **roda** cada comando publicado, comparando a saída medida agora com o `Medido antes` declarado — divergência é falha nomeada, porque significa que o card descreve um mundo que não é o que está na árvore. ``` Texto novo: ```text item e **roda** cada comando publicado, comparando a saída medida agora com o valor declarado para o mundo comparado (`--mundo`, RAF-T13: `antes` lê o `Medido antes`, `depois` o literal do esperado) — divergência é falha nomeada, porque significa que o card descreve um mundo que não é o que está na árvore. ``` 2. No `help` da opção `--mundo`, em `main`, trocar as duas linhas do texto antigo pelas duas do texto novo (o recuo de 12 espaços fica; cada linha perde o recuo deste card). Texto antigo: ```text "Mundo do card a comparar na forma inline (DFP-14); ausente deriva do bullet " "- **Status:** (done -> depois; demais -> antes)." ``` Texto novo: ```text "Mundo do card a comparar nas duas formas, 8.1 e inline (DFP-14, RAF-T13); " "ausente deriva do bullet - **Status:** (done -> depois; demais -> antes)." ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `573 passed`, 2026-09-29, revisão da `RAF-T13`). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `.claude/tools/card_check.py` só mudam as cinco linhas dos dois textos antigos: nenhum código, nome, regex nem outro comentário muda; o arquivo segue em LF. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar o docstring de `verificar_tarefa` (a `RAF-T13` já o acertou) nem os comentários das regex; não mudar `choices`, `default` nem a derivação do mundo pelo `Status`; não tocar o que é da `RAF-T14` (`git` de leitura, `<ref>`, invariância).
- **Contingências:** - se o texto antigo do passo 1 ou do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring do módulo nem a ajuda de `--mundo`); `tests/test_card_check.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T13` (`done`), que fica como executado; a restrição de `card_check` sobre o próprio card (`AE-157`), que não se repete em card aberto.
- **Handover:** 2026-09-29 · para `RAF-T14` - **Entregue:** card_check.py: docstring do módulo e help de --mundo descrevem o mundo depois da forma 8.1 (compara com o literal do esperado) - **Contrato:** nenhum texto do card_check contradiz a regra do mundo depois - **Não refazer:** as duas trocas de texto - **Pendente:** nenhum

## Execução

**Consumo:** 12 tool uses, 51.9 k tokens, 151.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta em leitura: diff de card_check.py = exatamente as 5 linhas antigas trocadas pelas 6 novas do card (numstat 6/5), arquivo segue LF (0 CRLF antes e depois), ast valido; --help renderiza o texto novo de --mundo; card_check RAF-T13a sai 0 em --mundo depois e 1 em --mundo antes (divergencia nomeada 'docstring=1-0 help=1-0' contra 'docstring=0-1 help=0-1'), o que prova o card discriminante nos dois mundos; card_check RAF-T13 (done) segue 0. O texto novo diz 'depois o literal do esperado' no contexto da forma 8.1 do docstring, coerente com a regra 1 da RAF-T13; na forma inline com par o depois le o valor do par, e o docstring nao afirma o contrario.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação" e vai pegar a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1".
Tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1" e vai executar: Quem executa faz o docstring do módulo e a ajuda da opção `--mundo` da conferência de verificação do card dizerem o que a regra 1 da `RAF-T13` entregou: no mundo `depois` a forma 8.1 compara com o literal do esperado, e o mundo vale nas du…
Agente executor devolveu a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1": review — sem pendência.
Tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O docstring do módulo e a ajuda de --mundo da conferência do card dizem o mundo depois da forma 8.1" como done: registrar estado, RDO e telemetria.
