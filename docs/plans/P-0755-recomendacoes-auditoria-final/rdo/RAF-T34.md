# RDO — P-0755 · RAF-T34

# Humano

Tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem" concluída em 2026-09-30.
A skill de condução passou a levar ao consultor a falha de instrumento que o fechamento avisa, com a linha do card em triagem no despacho.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 56/62 tarefas concluídas; próxima: "O consultor cita no achado a linha do laudo de onde ele veio".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T34` — Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o gerente do loop a levar ao consultor a falha de instrumento que o fechamento avisa e a linha do card que ele vai triar.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('b1=%d'%t.count('qualquer que seja a recomendação do laudo'))"` → `b1=1` — antes `b1=0`, depois `b1=1` 2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('molde=%d'%t.count('    despacho: P-<n> <ID do card em triagem>'))"` → `molde=1` — antes `molde=0`, depois `molde=1`

**Pronto quando:** - gerente do loop.falha de instrumento levada ao consultor — o aviso de falha que o fechamento imprime também leva a tarefa ao consultor — Verificação 1 - gerente do loop.card entregue ao consultor — o consultor é despachado com a linha que declara o card em triagem — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-18` (o consultor é despachado com a linha do card em triagem), `DRF-22` (a condição da `B1` ganha a linha `encerrar: B1 —` da saída do fechamento); `F-25` (a `B1` mora só na skill), `F-26` (o consultor recebe o card pelo texto da skill); relatório `R-20` (auditoria reg. 47) e `R-16` (reg. 54).
- **Depende de:** `RAF-T30`, `RAF-T30a`, `RAF-T33`
- **Operação do modelo:** `OP-34` - OP-34: Quem executa ensina o gerente do loop a levar ao consultor a falha de instrumento que o fechamento avisa e a linha do card que ele vai triar. - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; norma de consumo do kit — Quem implementa escreve a regra num lugar só, e os demais textos apontam para ela.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — a skill `scrum-master`: a linha da regra `B1` na tabela `### Bloco B — continuar ou encerrar a janela` e o molde do despacho na seção `## Acionamento do consultor`; nenhum código muda. O comportamento que a doutrina descreve já está nos instrumentos: o `encerrar.py tarefa` imprime, antes da linha final, `encerrar: B1 — achado de instrumento com falha: <texto>` para cada achado de laudo de alvo `instrumento` que relata queda, traceback, exceção ou erro (`RAF-T30`); o hook de telemetria e o painel leem a linha `despacho: <P-id>[ <ID>]` da primeira mensagem (`RAF-T31`, `RAF-T32`), cuja regra mora em `GOVERNANCA.md` §4.2 (`RAF-T33`). A skill remete à governança e não repete a regra. O contrato do objeto é: "Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só."
- **Passos:** 1. Na linha da regra `B1` (a que começa por `` | `B1` | **pendência substantiva**: ``), trocar o trecho antigo 1 pelo novo 1, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo 1: ```text integralmente atribuível a arquivo fora dos alvos por `B0` | ``` Trecho novo 1: ```text integralmente atribuível a arquivo fora dos alvos por `B0`, **ou** linha `encerrar: B1 — achado de instrumento com falha: <texto>` na saída do `encerrar.py tarefa`, qualquer que seja a recomendação do laudo (`R-20` da auditoria final, `P-0755`) | ``` 2. Na seção `## Acionamento do consultor`, trocar as três linhas do texto antigo 2 pelas quatro do texto novo 2 (as quebras são as do bloco; cada linha perde o recuo deste card, e a linha do molde guarda os quatro espaços iniciais que tem no bloco). Texto antigo 2: ```text Molde do despacho — as três entradas, e nada além delas: cenario=docs/plans/P-<n>-<slug>/cenario.md ``` Texto novo 2: ```text Molde do despacho — a linha de abertura com o card em triagem (`GOVERNANCA.md` §4.2, *Linha de abertura do despacho*; `R-16` da auditoria final, `P-0755`) e as três entradas, e nada além delas: despacho: P-<n> <ID do card em triagem> cenario=docs/plans/P-<n>-<slug>/cenario.md ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_progresso_hook.py` lê esta skill (tabela do repertório `M-0`..`M-18`), que os passos não tocam. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas outras regras dos blocos A e B nem no resto do molde; não repetir a regra da linha de abertura (ela mora em `GOVERNANCA.md` §4.2); não mexer no repertório de mensagens; não editar `.claude/tools/encerrar.py` (`RAF-T30`).
- **Contingências:** - se o trecho antigo 1 ou o texto antigo 2 não existir verbatim, uma única vez, em `.claude/skills/scrum-master/SKILL.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill.
- **Fora do escopo desta tarefa:** o aviso no fechamento (`RAF-T30`); a regra da linha de abertura (`RAF-T33`); a origem citada pelo consultor (`RAF-T35`).
- **Handover:** 2026-09-30 · para quem vier depois - **Entregue:** .claude/skills/scrum-master/SKILL.md: quem conduz leva ao consultor a falha de instrumento que o fechamento avisa (encerrar: B1) e o molde do despacho do consultor abre com 'despacho: P-<n> <ID do card em triagem>' - **Contrato:** o aviso B1 do encerrar.py vira acionamento do consultor; a linha de abertura atribui a telemetria e o painel - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 16 tool uses, 63.8 k tokens, 190.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta: o literal da B1 casa com o f-string de encerrar.py:588 ('encerrar: B1 — achado de instrumento com falha: ...') e a linha do molde casa com a regex do telemetria_hook.py:78 (despacho: P-n + ID de card); o molde remete a GOVERNANCA.md 4.2 'Linha de abertura do despacho' (linha 658) sem repetir a regra. Operacao OP-34 corresponde a entrega.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Agente executor recebe a tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem" e vai executar: Quem executa ensina o gerente do loop a levar ao consultor a falha de instrumento que o fechamento avisa e a linha do card que ele vai triar.
Agente executor devolveu a tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem": review — sem pendência.
Tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "Quem conduz leva ao consultor a falha de instrumento que o fechamento avisa e a linha do card em triagem" como done: registrar estado, RDO e telemetria.
