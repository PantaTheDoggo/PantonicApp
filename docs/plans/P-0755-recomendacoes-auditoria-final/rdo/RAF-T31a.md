# RDO — P-0755 · RAF-T31a

# Humano

Tarefa "O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca" concluída em 2026-09-29.
A documentação do escritor da telemetria passou a dizer quem recusa a linha repetida e que a linha do agente se substitui.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 51/60 tarefas concluídas; próxima: "O painel do gerente mostra a tarefa que a linha de abertura do despacho declara".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T31a` — O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz os docstrings de `.claude/tools/telemetria.py` dizerem que a recusa da linha repetida vale para o escritor sem agente e que a linha do mesmo agente se troca.

**Arquivos-alvo:** - `.claude/tools/telemetria.py`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/tools/telemetria.py').read_text(encoding='utf-8');print('docstring=%d-%d-%d-%d-%d linhas=%d'%(t.count('valha para todo escritor.'),t.count('para todo escritor, n'),t.count('reordenada ou normalizada;'),t.count('DRF-69'),t.count('[--agente A]'),len(t.splitlines())))"` → `docstring=0-0-0-3-1 linhas=314` — antes `docstring=1-1-1-0-0 linhas=305`, depois `docstring=0-0-0-3-1 linhas=314`

**Pronto quando:** - série de telemetria.linhas por agente — o texto do escritor diz que a linha do mesmo agente se troca e que a recusa da linha repetida vale para o escritor sem agente — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-69`; `AE-190` (laudo da `RAF-T31`, ressalva 91, achado 2); `DRF-18`, `DRF-39`; `DFP-8` do `P-0752`.
- **Depende de:** `RAF-T31`
- **Operação do modelo:** `OP-31` - OP-31: Quem executa faz a série de telemetria guardar uma linha por agente, atribuída ao plano e à tarefa que a abertura do despacho declara. - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/telemetria.py` — o docstring do módulo (o parágrafo da série histórica, linhas 8-11, e o do CLI, linhas 18-22) e os de `checar_repetida` (linhas 150-152), `gravar_por_agente` (linhas 178-182) e `append_row` (linhas 225-229); nenhum comportamento muda. A `RAF-T31` pôs o `append --agente` em `gravar_por_agente`, que troca a linha do mesmo agente e migra a série sem passar por `checar_repetida`, e deixou os textos dizendo que o script só apende e que a recusa vale para todo escritor. Pela `DRF-69`, a `DFP-8` segue no escritor sem agente (`append_row` e a pré-checagem do `encerrar.py`), e no escritor por agente a mesma rodada é a linha do mesmo agente. Nenhum teste lê esses docstrings (medido).
- **Passos:** 1. No docstring do módulo, trocar as quatro linhas do texto antigo pelas sete do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text A série histórica é insumo — nenhuma linha existente é reescrita, reordenada ou normalizada; o script só apende. Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte`. O mapeamento é sempre por nome de coluna (nunca por posição), o que elimina o risco de "coluna trocada em silêncio" que a edição manual admitia. ``` Texto novo: ```text A série histórica é insumo — sem `--agente`, nenhuma linha existente é reescrita, reordenada ou normalizada, e o script só apende; com `--agente` (`DRF-18`, `DRF-39` do `P-0755`), a linha do mesmo agente é substituída, e a série sem a coluna `agente` a ganha, com `-` nas linhas antigas. Colunas na ordem do header real do TSV: `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte` e, na série migrada, `agente`. O mapeamento é sempre por nome de coluna (nunca por posição), o que elimina o risco de "coluna trocada em silêncio" que a edição manual admitia. ``` 2. No docstring do módulo, trocar as três últimas linhas do parágrafo do CLI pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text [--file caminho/para/telemetria.tsv]``. Sem `--file`, resolve `docs/telemetria.tsv` a partir da raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a raiz é derivada da posição do próprio script, não do diretório de trabalho). ``` Texto novo: ```text [--file caminho/para/telemetria.tsv] [--agente A]``. Sem `--file`, resolve `docs/telemetria.tsv` a partir da raiz do repositório (mesmo desenho do `--root` de `.claude/checks/dead_code.py`: a raiz é derivada da posição do próprio script, não do diretório de trabalho). ``` 3. No docstring de `checar_repetida`, trocar a última linha pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do docstring). Texto antigo: ```text (DFP-8) — chamada antes de qualquer escrita, para que a recusa valha para todo escritor.""" ``` Texto novo: ```text (DFP-8) — chamada antes de qualquer escrita sem agente (`append_row` e o `encerrar.py`), para que a recusa valha para todo escritor sem agente; o escritor por agente não a chama: nele a mesma rodada é a linha do mesmo agente, que `gravar_por_agente` substitui (`DRF-69` do `P-0755`).""" ``` 4. No docstring de `gravar_por_agente`, trocar a última linha pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do docstring). Texto antigo: ```text arquivo temporário no mesmo diretório e `os.replace`, como `append_row`.""" ``` Texto novo: ```text arquivo temporário no mesmo diretório e `os.replace`, como `append_row`. Não chama `checar_repetida` (DFP-8): a linha do mesmo agente é a mesma rodada, e a troca a deixa idempotente (`DRF-69` do `P-0755`).""" ``` 5. No docstring de `append_row`, trocar a última linha pelas duas do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do docstring). Texto antigo: ```text antes de ler os bytes — a recusa vale para todo escritor, não só o CLI.""" ``` Texto novo: ```text antes de ler os bytes — a recusa vale para todo escritor sem agente, não só o CLI; a linha com agente vai a `gravar_por_agente`, que não recusa (`DRF-69` do `P-0755`).""" ``` 6. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `.claude/tools/telemetria.py` só mudam os cinco trechos dos Passos 1 a 5: nenhum código, nome, constante, mensagem nem `help` muda; o arquivo segue LF (hoje 0 CR). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar o código de `checar_repetida`, `gravar_por_agente`, `append_row` nem do CLI; não tocar `.claude/tools/telemetria_hook.py`, `.claude/tools/encerrar.py` nem o texto da `DFP-8` no `P-0752`.
- **Contingências:** - se o texto antigo de um passo não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê os docstrings do escritor); `tests/test_telemetria.py`, `tests/test_telemetria_hook.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T31` (`done`), que fica como executado; o texto da `DFP-8` no `P-0752`; o vermelho do `dead_code` pela sonda (`AE-189`, `DRF-44`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/telemetria.py: cinco trechos de docstring (módulo, checar_repetida, gravar_por_agente, append_row) dizem quem recusa a linha repetida e que a linha do agente se troca - **Contrato:** nenhum código mudou; docstrings coerentes com a DRF-69 - **Não refazer:** nada a declarar - **Pendente:** a frase de telemetria.py:5-6 ('só ganha uma linha no final') segue falsa para append --agente (achado do laudo, ao consultor)

## Execução

**Consumo:** 17 tool uses, 59.0 k tokens, 190.6 s (fonte: `<usage>` do encerramento)

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

Tarefa "O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O escritor da série de telemetria diz nos docstrings quem recusa a linha repetida e que a linha do agente se troca" como done: registrar estado, RDO e telemetria.
