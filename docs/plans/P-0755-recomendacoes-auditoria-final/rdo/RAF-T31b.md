# RDO — P-0755 · RAF-T31b

# Humano

Tarefa "O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente" concluída em 2026-09-29.
A documentação e a ajuda do comando de telemetria passaram a ressalvar o caso com --agente.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 52/61 tarefas concluídas; próxima: "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T31b` — O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o primeiro parágrafo do docstring de `.claude/tools/telemetria.py` e o `help` do subcomando `append` dizerem que, com `--agente`, a linha do mesmo agente se troca em vez de só ganhar uma linha no final.

**Arquivos-alvo:** - `.claude/tools/telemetria.py`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/tools/telemetria.py').read_text(encoding='utf-8');print('texto=%d-%d-%d-%d linhas=%d'%(t.count('no final).'),t.count('no final;'),t.count('ver o par'),t.count('troca a do mesmo agente'),len(t.splitlines())))"` → `texto=0-1-1-1 linhas=317` — antes `texto=1-0-0-0 linhas=314`, depois `texto=0-1-1-1 linhas=317`

**Pronto quando:** - série de telemetria.linhas por agente — nenhuma frase do escritor afirma só o apêndice sem ressalvar o `--agente` — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-70`; `AE-191` (laudo da `RAF-T31a`, ressalva 91, achado 1); `DRF-69`; `DRF-18`, `DRF-39`.
- **Depende de:** `RAF-T31a`
- **Operação do modelo:** `OP-31` - OP-31: Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara. - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/telemetria.py` — o fim do primeiro parágrafo do docstring do módulo (linhas 5-6) e o `help` do subcomando `append` em `main` (linha 271); nenhum comportamento muda. A `RAF-T31a` reescreveu o segundo parágrafo do docstring (com `--agente`, a linha do mesmo agente é substituída) e deixou o primeiro dizendo que o conteúdo anterior só ganha uma linha no final, e o `help` do `append` dizendo que ele adiciona uma linha. São as duas frases do arquivo que ainda afirmam só o apêndice sem ressalva (medido: o `append_row` diz o mesmo só dele, o que é verdade; a `description` do parser nomeia o verbo). Nenhum teste lê o docstring nem o `help` (medido).
- **Passos:** 1. No docstring do módulo, trocar as duas linhas do texto antigo pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e o conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final). ``` Texto novo: ```text diretório + `os.replace`) — nenhum leitor concorrente vê um arquivo parcialmente escrito, e, sem `--agente`, o conteúdo anterior nunca é tocado por conteúdo (só ganha uma linha no final; com `--agente`, ver o parágrafo seguinte). ``` 2. Em `main`, trocar a linha do texto antigo pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda o recuo do código). Texto antigo: ```text append_parser = subparsers.add_parser("append", help="Adiciona uma linha validada ao TSV.") ``` Texto novo: ```text append_parser = subparsers.add_parser( "append", help="Adiciona uma linha validada ao TSV; com --agente, troca a do mesmo agente." ) ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `.claude/tools/telemetria.py` só mudam os dois trechos dos Passos 1 e 2: nenhum código além da quebra da chamada do Passo 2, nenhum nome, constante nem mensagem muda; o arquivo segue LF (hoje 0 CR). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os docstrings que a `RAF-T31a` reescreveu (segundo parágrafo e CLI do módulo, `checar_repetida`, `gravar_por_agente`, `append_row`) nem a `description` do parser; não tocar `.claude/tools/telemetria_hook.py` nem `.claude/tools/encerrar.py`.
- **Contingências:** - se o texto antigo de um passo não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring nem o `help`); `tests/test_telemetria.py`, `tests/test_telemetria_hook.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T31` e da `RAF-T31a` (`done`), que fica como executado; o vermelho do `dead_code` pela sonda (`DRF-44`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/telemetria.py: primeiro parágrafo do docstring do módulo ressalva 'sem --agente' e o help do append diz 'com --agente, troca a do mesmo agente' - **Contrato:** a família de frases do escritor da telemetria está coerente com a DRF-69 - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 16 tool uses, 55.5 k tokens, 181.5 s (fonte: `<usage>` do encerramento)

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

Tarefa "O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O primeiro parágrafo do docstring e o help do append da série de telemetria ressalvam o --agente" como done: registrar estado, RDO e telemetria.
