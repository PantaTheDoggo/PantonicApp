# RDO — P-0748 · TLG-T4

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T4` — O condutor narra: uma linha do repertório antes de cada ato, na forma que o gancho grava
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do loop faz o condutor narrar a execução: a cada transição ele escreve, antes de agir, a linha do repertório que a descreve, na forma que o gancho leva ao arquivo de progresso, e é essa linha, e não a saída das ferramentas, que chega ao dono.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:50` — a linha que começa por - **Ação:** no Passo 2; os nove bullets entram um por passo, imediatamente antes da linha que começa por - **Ação:** de cada passo 2 a 10 (linhas 50, 61, 79, 108, 126, 149, 159, 175 e 217 em 2026-09-24; localizar pelo cabeçalho do passo) - `.claude/skills/scrum-master/SKILL.md:344` — cabeçalho ## Guardrails, última seção do arquivo; o bullet novo entra depois do último bullet dela - `.claude/skills/passagem-de-bastao/SKILL.md:12` — as linhas 12 e 13, que terminam em e só lá.

**Verificação:** 1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` → antes `1` (medido 2026-09-24: a frase de abertura da seção do repertório cita o bullet), depois `10`. 2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "[gerente] " | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 3. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "progresso.txt" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 4. `(Select-String -SimpleMatch -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern "e só lá" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`. 5. `(Select-String -SimpleMatch -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern "arquivo de progresso" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 6. `git diff --numstat -- .claude/skills/scrum-master/SKILL.md` → com a base `<a> <r>` do passo 1: removidas `= <r>` e adicionadas `≥ <a> + 10` (delta contra a base re-medida no despacho, `DTG-28`; nunca o total contra `HEAD`). 7. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.

**Pronto quando:** `stream de dados.o que as mensagens narram` — *ligado à tarefa e à intenção dos agentes: uma linha em linguagem humana por transição, escrita pelo condutor antes de agir, e é ela que chega ao arquivo de progresso, sem saída de comando entre duas delas* — Verificação 1, 2, 3, 4, 5 e 6.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-7` (intenção, não raciocínio), `DTG-10` (a residência vigente do repertório é a seção da skill), `DTG-15` (colateral na `passagem-de-bastao`), `DTG-20`, `DTG-23` (marcador `[gerente] ` e os sete inícios), `DTG-24` (caminho do arquivo), `DTG-26` (não há `loop.py`), `DTG-28` (`numstat` como delta), `F-8`, `F-23`, `I-2`, `I-5`, `I-11`.
- **Depende de:** `TLG-T2a`
- **Operação do modelo:** `OP-4` - OP-4: O mantenedor do loop faz o condutor narrar a execução: a cada transição ele escreve, antes de agir, a linha do repertório que a descreve, na forma que o gancho leva ao arquivo de progresso, e é essa linha, e não a saída das ferramentas, que chega ao dono. - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop, isto é, o que ele escreve ao dono a cada passo, e o arquivo de progresso que um gancho do próprio kit alimenta com essas linhas. A ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos: o que ele pediu ao agente e o que o agente devolveu. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — skill `scrum-master` (um bullet `**Narra:**` por passo, do 2 ao 10, e um bullet em `## Guardrails`) e skill `passagem-de-bastao` (a frase das linhas 12-13). Nenhum agente, instrumento, teste ou arquivo de configuração. O gancho que lê a forma prescrita aqui é o `.claude/tools/progresso_hook.py` da `TLG-T3`, que este card não edita.
- **Domínio:** *narrar* = escrever, como texto do agente e **antes** do ato que ela anuncia, a linha `M-<n>` da seção `## Repertório de mensagens ao gerente` da própria skill, preenchida, **sozinha numa linha** e começando pelo marcador literal `[gerente] ` (`DTG-23`, `I-2`, `I-5`). *Forma que o gancho leva ao arquivo* = o gancho copia para `.claude/estado/progresso.txt` só as linhas que, sem espaços nas pontas, começam por `[gerente] ` e cujo resto começa por `Abrindo a janela do plano `, `Tarefa `, `Agente executor `, `Agente revisor `, `Agente consultor `, `Agente modelador ` ou `Scrum master `, e grava o resto, sem o marcador.
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** em cada passo, o bullet entra imediatamente **antes** da linha que começa por `- **Ação:**` daquele passo (a narração precede o ato). O rótulo à esquerda (`Passo 2:` e os seguintes) não entra na skill: ``` Passo 2:  - **Narra:** na abertura da janela, `M-0` antes do `backlog.py next`; na volta seguinte a um "segue" do passo 10, `M-11` logo depois do `backlog.py next`, ou `M-12` se ele devolve `nada delegável`; com a tarefa selecionada, `M-1`. Na abertura com `nada delegável`, nenhuma linha além do `M-0`. Passo 3:  - **Narra:** aprovados os três gates, `M-2` antes de materializar `in-progress`. Passo 4:  - **Narra:** `M-3` antes de invocar o `pantonic-executor`, com o `<objetivo>` copiado da linha `- **Objetivo:**` do dossiê. Passo 5:  - **Narra:** `M-4` assim que a linha de retorno é lida, antes de qualquer ato do passo 6 ou 8. Passo 6:  - **Narra:** `M-5` antes do `review_evidence.py`; `M-6` antes de invocar o `pantonic-reviewer`. Passo 7:  - **Narra:** `M-7` assim que as duas linhas de retorno são lidas. Passo 8:  - **Narra:** `M-8` antes de invocar o `pantonic-consultant`; `M-9` assim que a rota é lida; `M-14` antes de invocar o `pantonic-model-designer`. Passo 9:  - **Narra:** `M-10` antes do `modelo.py check` que abre o fechamento. Passo 10: - **Narra:** em `B0`, `M-13` antes do `review_evidence.py --atribuir`; com encerramento, `M-12` antes do relatório; com "segue", nenhuma linha neste passo — o `M-11` sai no passo 2 seguinte. ``` Em `## Guardrails`, acrescentar como último bullet, numa linha só: ``` - Toda linha do repertório (seção *Repertório de mensagens ao gerente*) é escrita como texto do agente, **sozinha numa linha**, começando pelo marcador literal `[gerente] ` seguido da frase-modelo preenchida — por exemplo `[gerente] Agente revisor devolveu a tarefa TLG-T2: aprovado 100%, bloqueante nenhuma.` — e antes do ato que ela anuncia. O gancho `.claude/tools/progresso_hook.py` (eventos `PostToolUse` e `Stop`) copia para `.claude/estado/progresso.txt`, sem o marcador, só as linhas marcadas cujo resto começa por `Abrindo a janela do plano `, `Tarefa `, `Agente executor `, `Agente revisor `, `Agente consultor `, `Agente modelador ` ou `Scrum master `; é esse arquivo que o gerente lê, no painel fora da extensão, e nenhuma saída de ferramenta chega a ele. O loop nunca escreve no arquivo diretamente (`P-0748`, `DTG-23`, `I-2`, `I-5`, `I-11`). ``` Em `passagem-de-bastao/SKILL.md`, substituir as duas linhas 12-13, hoje exatamente assim: ``` acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelo **relatório de encerramento** do `scrum-master`, e só lá. ``` por estas três linhas: ``` acompanha. Não é skill de comunicação com humano; o que chega ao dono chega pelas linhas do **repertório de mensagens ao gerente**, que o gancho do kit grava no arquivo de progresso, e pelo **relatório de encerramento** do `scrum-master`, e só por eles. ```
- **Passos:** 1. Medir a base: `git diff --numstat -- .claude/skills/scrum-master/SKILL.md` → anotar `<a> <r>` (linhas adicionadas e removidas) para a Verificação 6. 2. Na `scrum-master`, inserir o bullet `**Narra:**` de cada passo, 2 a 10, imediatamente antes da linha `- **Ação:**` daquele passo — nove bullets, uma linha cada. 3. Acrescentar o bullet de `## Guardrails` depois do último bullet da seção. 4. Na `passagem-de-bastao`, substituir as linhas 12-13 pelas três linhas dadas. 5. Rodar a Verificação 1 a 7.
- **Restrições desta tarefa:** `I-2` — a linha narrada é texto do agente, nunca saída de comando; `I-5` — a linha que anuncia um ato vem antes dele; `I-11` — a skill não manda o loop escrever no arquivo de progresso; `DTG-10` — o card cita `M-<n>` e **não** recopia frases do repertório; `DTG-23` — o marcador é exatamente `[gerente] ` e os sete inícios são exatamente os do `Domínio`. Na `scrum-master`, só inserções (dez linhas); na `passagem-de-bastao`, só a troca das duas linhas pelas três.
- **Não fazer:** não editar bullets `**Ação:**` nem nenhuma outra linha existente da `scrum-master`; não editar a tabela do repertório (é `TLG-T2a`); não acrescentar proibição de leitura no topo (a antiga `I-10` foi revogada, `DTG-26`); não citar `loop.py`; não editar agente, instrumento, `progresso_hook.py`, `projecoes.json` ou `README.md` (é `TLG-T5`); não acrescentar frase nova ao repertório (frase que faltar é a contingência 1).
- **Contingências:** - se algum passo precisar de uma frase que não existe entre `M-0` e `M-14` → parar e sinalizar `blocked` razão `premissa` com o passo e a transição sem frase; - se a skill ainda contém `loop.py` → parar e sinalizar `blocked` razão `dependencia` (`TLG-T2a` não entregou); - se algum dos passos 2 a 10 não tem exatamente uma linha que começa por `- **Ação:**` → parar e sinalizar `blocked` razão `premissa` com a lista das linhas da skill que começam por `- **Ação:**` (número e texto); - se as linhas 12-13 da `passagem-de-bastao` não contêm `e só lá` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "só lá" .claude/skills/passagem-de-bastao/SKILL.md`.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho.
- **Fora do escopo desta tarefa:** a descrição pública e o painel (`TLG-T5`); a leitura do painel pelo dono (Marco 3, aceite de marco e não de card, `I-6`).

## Execução

**Consumo:** 20 tool uses, 81.2 k tokens, 137.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
