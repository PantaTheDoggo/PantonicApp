# RDO — P-0755 · RAF-T35

# Humano

Tarefa "O consultor cita no achado a linha do laudo de onde ele veio" concluída em 2026-09-30.
O consultor passou a citar, em cada achado, a linha do laudo de onde ele veio.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 57/62 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T35` — O consultor cita no achado a linha do laudo de onde ele veio
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa ensina o consultor a citar a origem no laudo de todo achado que ele registra ou reescreve a partir dele.

**Arquivos-alvo:** - `.claude/agents/pantonic-consultant.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print('origem=%d'%t.count('cita a origem no fim da entrada'))"` → `origem=1` — antes `origem=0`, depois `origem=1`

**Pronto quando:** - consultor.origem citada no achado — o achado cita a mesma origem no laudo que o fechamento usa — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-21` (o consultor, ao registrar ou reescrever `AE-` a partir de achado de laudo, cita a mesma origem); `F-25` (nenhuma `AE-` traz origem; a reescrita do consultor escapa da dedupe por texto); relatório `R-19` (auditoria reg. 39).
- **Depende de:** `RAF-T30`
- **Operação do modelo:** `OP-35` - OP-35: Quem executa ensina o consultor a citar a origem no laudo de todo achado que ele registra ou reescreve a partir dele. - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; consultor — Quem implementa acrescenta à definição do agente as duas formas de linha que as operações pedem, sem mudar a triagem.
- **Camada e fronteira:** doutrina do kit — a definição do agente consultor, `.claude/agents/pantonic-consultant.md`, item 3 (*Repara o plano e devolve o dossiê de modelo*); nenhum código muda. O mecanismo que a regra usa já existe desde a `RAF-T30`: o `encerrar.py tarefa` grava no fim de cada `AE-` que vem do laudo ` **Origem:** ` seguido de `laudo:<TAREFA>#<n>` entre crases (`<n>` = posição da linha na tabela `## Achado de processo`) e pula o achado cuja origem, entre crases, já aparece em alguma `AE-` do plano. A regra mora só neste item do consultor; nenhum outro arquivo a repete. O contrato do objeto é: "Quem implementa acrescenta à definição do agente as duas formas de linha que as operações pedem, sem mudar a triagem."
- **Passos:** 1. No item 3 de `.claude/agents/pantonic-consultant.md` (uma linha só no arquivo), trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text fila reordenada, achado absorvido com ponteiro. ``` Trecho novo: ```text fila reordenada, achado absorvido com ponteiro. Achado que você registra ou reescreve a partir de um laudo cita a origem no fim da entrada `AE-<n>`: ` **Origem:** ` seguido de `laudo:<TAREFA>#<n>` entre crases, com `<n>` a posição da linha na tabela `## Achado de processo` do laudo — a mesma origem que o `encerrar.py tarefa` grava e confere para não registrar o achado de novo (`R-19` da auditoria final, `P-0755`). ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_frontmatter_yaml.py` lê o frontmatter deste arquivo, que o passo não toca. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer na frase da validação no marco (`RAF-T26`) nem nas rotas da triagem; não reescrever `AE-` já registradas em plano nenhum; não editar `.claude/tools/encerrar.py` (`RAF-T30`).
- **Contingências:** - se o trecho antigo não existir verbatim, uma única vez, em `.claude/agents/pantonic-consultant.md` → parar e sinalizar `blocked` razão `premissa`, colando o item 3. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_frontmatter_yaml.py` lê o arquivo.
- **Fora do escopo desta tarefa:** a gravação e a conferência da origem no fechamento (`RAF-T30`); a forma da validação no marco (`RAF-T26`).
- **Handover:** 2026-09-30 · para quem vier depois - **Entregue:** .claude/agents/pantonic-consultant.md, item 3: o consultor cita no achado a linha do laudo de onde ele veio - **Contrato:** achado absorvido pelo consultor carrega a origem no laudo - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 11 tool uses, 51.3 k tokens, 146.5 s (fonte: `<usage>` do encerramento)

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

Agente executor recebe a tarefa "O consultor cita no achado a linha do laudo de onde ele veio" e vai executar: Quem executa ensina o consultor a citar a origem no laudo de todo achado que ele registra ou reescreve a partir dele.
Agente executor devolveu a tarefa "O consultor cita no achado a linha do laudo de onde ele veio": review — sem pendência.
Tarefa "O consultor cita no achado a linha do laudo de onde ele veio": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O consultor cita no achado a linha do laudo de onde ele veio" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O consultor cita no achado a linha do laudo de onde ele veio": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O consultor cita no achado a linha do laudo de onde ele veio" como done: registrar estado, RDO e telemetria.
