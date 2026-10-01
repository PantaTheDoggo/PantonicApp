# RDO — P-0755 · RAF-T38

# Humano

Tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho" concluída em 2026-09-30.
A checagem de versão do kit passou a ser rodada por quem conduz, antes do planejador, que só a registra no cabeçalho.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 61/63 tarefas concluídas; próxima: "A mensagem de marco abre nomeando a entrega e o pedido do dono que a originou".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T38` — Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa passa a quem conduz, antes do despacho do planejador, a checagem de versão do kit que o planejador hoje é mandado invocar.

**Arquivos-alvo:** - `.claude/skills/checar-versao-kit/SKILL.md` - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/checar-versao-kit/SKILL.md').read_text(encoding='utf-8');print('momento=%d'%t.count('a roda antes de despachar o planejador'))"` → `momento=1` — antes `momento=0`, depois `momento=1` 2. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('versao=%d-%d'%(t.count('invoque'),t.count('Checagem de versão do kit:')))"` → `versao=0-1` — antes `versao=1-0`, depois `versao=0-1`

**Pronto quando:** - checagem de versão do kit.momento em que roda — a rotina diz que quem conduz a roda antes de despachar o planejador e passa o resultado no pedido — Verificação 1 - planejador.checagem de versão registrada — o planejador registra no cabeçalho a checagem que recebe pronta no pedido, e nenhuma fase manda invocar rotina — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-25`, `DRF-42`; `F-27` (a Fase 5 manda o planejador invocar a skill; nenhum agente lista `Skill` no `tools:`; se a plataforma bloqueia skill em subagente não se verifica pelo repositório); relatório `R-23` (auditoria reg. 15).
- **Depende de:** `RAF-T37`
- **Operação do modelo:** `OP-38` - OP-38: Quem executa passa a quem conduz, antes do despacho do planejador, a checagem de versão do kit que o planejador hoje é mandado invocar. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — duas residências, uma regra cada: a seção `## Quando roda` da skill `.claude/skills/checar-versao-kit/SKILL.md` (quando a checagem roda e quem a roda: a residência do momento, `DRF-25`) e a `### Fase 5 — Registro e parada` de `.claude/agents/pantonic-planner.md` (o que o planejador faz com o resultado); nenhum código muda. O frontmatter da skill (`description`) fica como está: o índice derivado `.claude/README.md` o espelha, e o `kit_check.ps1 -Mode check-drift` compara os dois. O `tools:` do planejador não ganha `Skill` (`DRF-25`). Os contratos dos objetos são: "Quem implementa escreve na própria rotina que quem conduz a roda antes de despachar o planejador e passa o resultado no pedido." e "Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão."
- **Passos:** 1. Em `.claude/skills/checar-versao-kit/SKILL.md`, seção `## Quando roda`, trocar o trecho antigo (a primeira linha da seção) pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano"). ``` Trecho novo: ```text Na criação de todo plano novo: quem conduz a sessão a roda antes de despachar o planejador (`pantonic-planner`) e passa o resultado no pedido a ele, e o planejador o registra no campo `**Checagem de versão do kit:**` do cabeçalho do plano — subagente, o planejador não invoca skill (`R-23` da auditoria final, `P-0755`). Plano registrado sem planejador roda a checagem no registro (skill `diario-de-obras`, operação "1. Registrar plano"). ``` 2. Em `.claude/agents/pantonic-planner.md`, `### Fase 5 — Registro e parada`, trocar o trecho antigo pelo novo, na mesma linha, sem quebra nova e sem refluxo. Trecho antigo: ```text atualize o próximo id no mesmo ato; invoque `checar-versao-kit`; se o plano é derivado de outro ``` Trecho novo: ```text atualize o próximo id no mesmo ato; registre no cabeçalho do plano, no campo `**Checagem de versão do kit:**`, o resultado da checagem de versão que o pedido de quem conduz traz (quem conduz roda a skill `checar-versao-kit` antes de despachar o planejador, e nenhuma fase deste roteiro a chama; sem o resultado no pedido, o campo registra `não recebida no pedido`, `R-23` da auditoria final, `P-0755`); se o plano é derivado de outro ``` 3. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `521 passed`, 2026-09-28, antes da etapa A). `tests/test_doutrina_unidade.py` lê o planejador. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer no frontmatter da skill (o `description` que o `.claude/README.md` espelha) nem no resto da seção `## Quando roda`; não acrescentar `Skill` ao `tools:` de agente nenhum; não editar a skill `diario-de-obras`; não mexer no bloco **Árvore do** da Fase 5 (`RAF-T16`).
- **Contingências:** - se algum dos dois trechos antigos não existir verbatim, uma única vez, no seu arquivo → parar e sinalizar `blocked` razão `premissa`, colando a seção `## Quando roda` da skill e o primeiro parágrafo da Fase 5 do planejador. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o planejador.
- **Fora do escopo desta tarefa:** a régua de profundidade e o pedido ao modelador (`RAF-T36`, `RAF-T37`); a linha da skill na tabela de skills do `README.md` (`RAF-T40`).
- **Handover:** 2026-09-30 · para quem vier depois - **Entregue:** .claude/skills/checar-versao-kit/SKILL.md e .claude/agents/pantonic-planner.md (Fase 5): quem conduz roda a checagem de versão do kit antes do planejador, que registra o resultado no cabeçalho do plano - **Contrato:** o planejador recebe a checagem de versão pronta e a registra no cabeçalho - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 13 tool uses, 52.7 k tokens, 133.1 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O pedido do planejador ao modelador deixa de exigir caminho, linha e nome de comando" e vai pegar a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho".
Tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho" e vai executar: Quem executa passa a quem conduz, antes do despacho do planejador, a checagem de versão do kit que o planejador hoje é mandado invocar.
Agente executor devolveu a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho": review — sem pendência.
Tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "Quem conduz roda a checagem de versão do kit antes do planejador, que a registra no cabeçalho" como done: registrar estado, RDO e telemetria.
