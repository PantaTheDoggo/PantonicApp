# RDO — P-0755 · RAF-T33

# Humano

Tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa" concluída em 2026-09-29.
A norma de consumo passou a mandar todo despacho de subagente abrir com a linha que declara plano e tarefa.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 55/62 tarefas concluídas; próxima: "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T33` — A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa escreve na norma de consumo do kit a regra de que todo despacho de subagente abre com a linha que declara o plano e a tarefa.

**Arquivos-alvo:** - `GOVERNANCA.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print('abertura=%d-%d'%(t.count('pelo primeiro id de plano da primeira mensagem do subagente'),t.count('todo despacho de subagente abre com a')))"` → `abertura=0-1` — antes `abertura=1-0`, depois `abertura=0-1`

**Pronto quando:** - norma de consumo do kit.linha de abertura do despacho — todo despacho de subagente abre com uma linha que declara o plano e, quando houver, a tarefa ou o tíquete; a regra mora num lugar só — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-18` (a regra da linha mora em `GOVERNANCA.md` §4.2, residência da doutrina de telemetria), `DRF-39`; `F-26`; relatório `R-16` (auditoria reg. 41 e 54).
- **Depende de:** `RAF-T31`, `RAF-T32`
- **Operação do modelo:** `OP-33` - OP-33: Quem executa escreve na norma de consumo do kit a regra de que todo despacho de subagente abre com a linha que declara o plano e a tarefa. - precisa de: série de telemetria — Quem implementa faz o registro ler o plano e a tarefa na primeira linha do despacho e ganhar uma coluna que identifica o agente, completando as linhas antigas.; painel do gerente — Quem implementa faz o painel ler a mesma linha de abertura do despacho antes de recorrer à tarefa corrente.
- **Camada e fronteira:** doutrina do kit — `GOVERNANCA.md`, §4.2 (*Diário de obras*), bullet `- **Fonte única da série**`; nenhum código muda. O comportamento que a norma descreve já está nos instrumentos: o hook `SubagentStop` lê a linha `despacho: <P-id>[ <ID>]` da primeira mensagem antes de `tarefa-corrente.json` e antes do primeiro id de plano citado, e grava uma linha por agente com a coluna `agente` (`RAF-T31`); o painel mostra a tarefa que a linha declara (`RAF-T32`); o `despachar` já imprime a linha no texto pronto ao executor (`RAF-T3`). A regra mora só neste bullet; a skill `scrum-master` passa a despachar o consultor com ela na `RAF-T34`, remetendo a este bullet. O contrato do objeto é: "Quem implementa escreve a regra num lugar só, e os demais textos apontam para ela."
- **Passos:** 1. No bullet `- **Fonte única da série**` do §4.2 de `GOVERNANCA.md`, trocar o trecho antigo 1 pelo novo 1, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo 1: ```text (append-only, colunas `data`, `projeto`, ``` Trecho novo 1: ```text (colunas `data`, `projeto`, ``` 2. No mesmo bullet, trocar o trecho antigo 2 pelo novo 2, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo 2: ```text nao_medido}`) ``` Trecho novo 2: ```text nao_medido}`, `agente`) ``` 3. No fim do mesmo bullet, trocar as duas linhas do texto antigo pelas oito do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo). Texto antigo: ```text `<P-n>-scout` pelo primeiro id de plano da primeira mensagem do subagente, e `sem-id-<papel>` quando não há id a derivar. ``` Texto novo: ```text `<P-n>-scout`, e `sem-id-<papel>` quando não há id a derivar. **Linha de abertura do despacho** (`R-16` da auditoria final, `P-0755`): todo despacho de subagente abre com a linha `despacho: <P-id>`, seguida de um espaço e do id da tarefa ou do tíquete quando houver; o hook lê o plano e a tarefa nela antes de `tarefa-corrente.json` e antes do primeiro id de plano citado na primeira mensagem, que só valem sem ela, e o painel do gerente mostra a tarefa que ela declara. A série guarda uma linha por agente, a última e acumulada, com o nome do agente na coluna `agente` (`-` nas linhas anteriores à coluna e nas gravadas sem agente). ``` 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê `GOVERNANCA.md`. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nos outros bullets do §4.2 nem nas outras frases do bullet; não repetir a regra na skill `scrum-master`, em agente ou no `README.md` (a skill remete a este bullet na `RAF-T34`); não editar `docs/telemetria.tsv`.
- **Contingências:** - se um dos três textos antigos não existir verbatim, uma única vez, em `GOVERNANCA.md` → parar e sinalizar `blocked` razão `premissa`, colando o bullet `- **Fonte única da série**` inteiro. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** a mecânica do hook e do painel (`RAF-T31`, `RAF-T32`); o despacho do consultor com a linha e o aviso `B1` na skill (`RAF-T34`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** GOVERNANCA.md, bullet Fonte única da série: sem 'append-only', coluna agente no esquema e o parágrafo 'Linha de abertura do despacho' - **Contrato:** todo despacho de subagente abre com a linha que declara plano e tarefa; a telemetria e o painel a leem - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 19 tool uses, 56.7 k tokens, 177.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Agente executor recebe a tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa" e vai executar: Quem executa escreve na norma de consumo do kit a regra de que todo despacho de subagente abre com a linha que declara o plano e a tarefa.
Agente executor devolveu a tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa": review — sem pendência.
Tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A norma de consumo manda todo despacho de subagente abrir com a linha que declara plano e tarefa" como done: registrar estado, RDO e telemetria.
