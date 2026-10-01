# RDO — P-0755 · RAF-T26a

# Humano

Tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede" concluída em 2026-09-29.
O modelador passa a conhecer os quatro conflitos da promoção de versão e a devolver o que o dossiê do marco pede.
Revisão: aprovada com ressalva (90%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 42/56 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T26a` — O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa acerta no modelador a frase do conflito na promoção de versão: os quatro conflitos que o comando do marco recusa e o que o modelador devolve, o mesmo que o campo `Devolver` do dossiê pede.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-model-designer.md').read_text(encoding='utf-8');print('conflito=%d-%d'%(t.count('e o registro acertados para o'),t.count('(o plano sem a ')))"` → `conflito=0-1` — antes `conflito=1-0`, depois `conflito=0-1`

**Pronto quando:** - modelador.papel na promoção de versão — o modelador só é chamado quando o comando do marco encontra conflito, e a doutrina nomeia os quatro conflitos e o que ele devolve, o mesmo que o dossiê pede — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-64`; `AE-180` (laudo da `RAF-T26`, ressalva 90: o texto que a `RAF-T26` fixou enumera três conflitos, e `_checar_promocao` de `.claude/tools/encerrar.py` tem um quarto que também imprime o dossiê, `o plano não tem a ## 1`; e diz que o modelador devolve "a `## 1A` e o registro acertados", enquanto o dossiê, depois da `RAF-T23b`, pede a `## 1` e a `## 1A` acertadas, com o registro de versões). Medido pelo consultor em cópia (2026-09-29): trecho antigo único no arquivo, LF (0 CR); Verificação 1 antes `conflito=1-0`, depois `conflito=0-1`; `tests/test_doutrina_unidade.py` `8 passed` depois.
- **Depende de:** `RAF-T26`, `RAF-T23b`
- **Operação do modelo:** `OP-26` - OP-26: Quem executa reescreve no modelador e no consultor a doutrina da promoção de versão, que passa ao comando do marco e só chama o modelador no conflito. - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.
- **Camada e fronteira:** doutrina do kit — a definição do agente modelador (`.claude/agents/pantonic-model-designer.md`, ato **Emenda**, parágrafo `**No marco**`, as seis últimas linhas); nenhum código muda. O comportamento descrito é o do comando depois da `RAF-T23b`: `_checar_promocao` recusa com o dossiê `Ato: emenda` quando o plano não tem a `## 1`, quando a `## 1A` é outra versão, quando o registro de versões não tem uma única linha vigente e quando não tem a linha pendente da versão; o `Devolver` do conflito pede `a ## 1 e a ## 1A acertadas, com o registro de versões, para o comando do marco rodar de novo.` O contrato do objeto "fechamento" é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Passos:** 1. Em `.claude/agents/pantonic-model-designer.md`, trocar as seis linhas do texto antigo pelas seis do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os dois espaços iniciais que já tem no arquivo). Texto antigo: ```text Você só é chamado na promoção quando o comando encontra **conflito** (a `## 1A` com outra versão, registro de versões sem vigente único ou sem a linha pendente da versão): o comando imprime o dossiê `Ato: emenda`, e você devolve a `## 1A` e o registro acertados para o comando rodar de novo. Recusada: o desfecho chega em dossiê `Ato: emenda`, com o ato do dono em `Motivo`; a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*). ``` Texto novo: ```text Você só é chamado na promoção quando o comando encontra **conflito** (o plano sem a `## 1`, a `## 1A` com outra versão, registro de versões sem vigente único ou sem a linha pendente da versão): o comando imprime o dossiê `Ato: emenda`, e você devolve a `## 1` e a `## 1A` acertadas, com o registro de versões, para o comando rodar de novo. Recusada: o desfecho chega em dossiê `Ato: emenda`, com o ato do dono em `Motivo`; a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*). ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `602 passed`, 2026-09-29, revisão da `RAF-T26`). `tests/test_doutrina_unidade.py` lê `pantonic-model-designer.md`. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - O arquivo fica em LF, sem CR. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mexer nas seis primeiras linhas do parágrafo `**No marco**`, nos atos **Autoria**, **Conflito** e **Leitura** nem no resto do ato **Emenda**; não editar `GOVERNANCA.md` nem `.claude/agents/pantonic-consultant.md`; não editar `.claude/tools/encerrar.py` (é da `RAF-T23b`).
- **Contingências:** - se o texto antigo do passo 1 não existir verbatim, uma única vez, no arquivo → parar e sinalizar `blocked` razão `premissa`. - se o sistema de permissão negar a edição do arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê o arquivo.
- **Fora do escopo desta tarefa:** o `Devolver` do dossiê no comando (`RAF-T23b`); a forma da linha de validação do consultor (`RAF-T26`, entregue).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/agents/pantonic-model-designer.md, parágrafo No marco: nomeia os quatro conflitos de _checar_promocao (inclui 'o plano não tem a ## 1') e devolve o que o dossiê do marco pede em cada ramo - **Contrato:** a doutrina do modelador e o dossiê do encerrar.py marco pedem a mesma devolução - **Não refazer:** a troca do parágrafo - **Pendente:** nenhum

## Execução

**Consumo:** 12 tool uses, 52.5 k tokens, 179.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta feito contra o codigo, nao so contra o card: as quatro razoes que a frase nova enumera casam uma a uma com os quatro raise _conflito de _checar_promocao (encerrar.py:1084, 1088, 1095, 1102), e o 'devolve a ## 1 e a ## 1A acertadas, com o registro de versoes, para o comando rodar de novo' casa com o Devolver do ramo de conflito (encerrar.py:1077-1078); a frase da recusa, intocada, segue coerente com o Devolver da recusa (encerrar.py:1243-1244). Nenhum resto do texto antigo no .claude (grep 'acertad'). Verificacao 1 re-rodada conflito=0-1; arquivo em LF (0 CR); tests/test_doutrina_unidade.py 8 passed; recorte desde a ref so 6+/6- no alvo, com as seis primeiras linhas do paragrafo No marco intocadas.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O dossiê do comando do marco pede ao modelador o que ele de fato devolve, no conflito e na recusa" e vai pegar a tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede".
Tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede" e vai executar: Quem executa acerta no modelador a frase do conflito na promoção de versão: os quatro conflitos que o comando do marco recusa e o que o modelador devolve, o mesmo que o campo `Devolver` do dossiê pede.
Agente executor devolveu a tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede": review — sem pendência.
Tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede": ressalva 90%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O modelador conhece os quatro conflitos da promoção e devolve o que o dossiê pede" como done: registrar estado, RDO e telemetria.
