# RDO — P-0748 · TLG-T2

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T2` — O repertório de mensagens na skill do loop
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:306` — âncora `## Proibições` (a seção nova entra imediatamente **antes** desta linha, separada por uma linha em branco)

**Verificação:** 1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "## Repertório de mensagens ao gerente" | Measure-Object).Count` → antes `0` (medido 2026-09-23), depois `1`. 2. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern "^\| ``M-\d+`` \|" | Measure-Object).Count` (regex deliberado: linha de tabela cujo id é `M-<n>` entre crases; em PowerShell a crase dobrada dentro de aspas duplas é uma crase literal) → antes `0` na skill (medido 2026-09-23), depois `15` — o mesmo padrão rodado sobre `docs/plans/P-0748-tela-do-gerente.md` devolve `15` (medido 2026-09-23), que é o valor de referência. 3. `git diff --numstat -- .claude/skills/scrum-master/SKILL.md` → segunda coluna (linhas removidas) `0`; primeira coluna ≥ `24`. 4. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.

**Pronto quando:** `stream de dados.repertório de mensagens` — *fechado: uma frase-modelo por transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —; nenhuma lacuna pede ao condutor uma busca nova para ser preenchida* — Verificação 1, 2 e 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-5`, `DTG-7` (intenção, não raciocínio), `DTG-10` (residência: `### 4.1` → seção da skill), `F-2`, `F-11` (linhas de retorno que preenchem as lacunas), `F-12` (saída do `backlog.py next`), `I-2`, `I-3`, `R-3`.
- **Depende de:** `TLG-T1`
- **Operação do modelo:** `OP-2` - OP-2: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo. - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop: o que ele escreve ao dono e o que ele mesmo executa entre um despacho e outro. Só isso muda; a ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos: o que ele pediu ao agente e o que o agente devolveu. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit, skill `scrum-master`. Só inserção de uma seção nova; nenhuma linha existente da skill muda. Nenhum agente é editado.
- **Domínio:** *transição do loop* = mudança de passo da `scrum-master` (seleção, despacho, retorno, veredito, roteamento, fechamento, próxima); *lacuna* = `<…>` na frase-modelo, preenchida por dado que o condutor já recebeu (`I-3`).
- **Contratos/classes:** nenhum código.
- **Passos:** 1. Abrir `.claude/skills/scrum-master/SKILL.md` e localizar a linha `## Proibições`. 2. Inserir, antes dela, o texto de `Texto novo, literal`, com a tabela colada da `### 4.1` do plano. 3. Rodar a Verificação 1–4.
- **Restrições desta tarefa:** `I-2` — nenhuma frase do repertório é saída de comando; `I-3` — nenhuma lacuna exige chamada nova; `DTG-10` — a tabela é cópia, não reescrita: divergência de uma palavra entre a `### 4.1` e a seção da skill é defeito. Inserção pura: `git diff --numstat` da skill tem `0` na coluna de linhas removidas.
- **Não fazer:** não editar nenhum passo da skill (é `TLG-T3` e `TLG-T4`); não acrescentar, remover ou reordenar linhas do repertório; não editar `passagem-de-bastao` (é `TLG-T4`); não editar agentes; não "melhorar" as frases.
- **Contingências:** - se a `### 4.1` do plano tiver mais ou menos de quinze linhas `M-<n>` → parar e sinalizar `blocked` razão `premissa` com a contagem encontrada; - se `## Proibições` não existir na skill → parar e sinalizar `blocked` razão `premissa` com as três primeiras linhas de `grep -n "^## " .claude/skills/scrum-master/SKILL.md`.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho (referência histórica `277 passed`, 2026-09-23, `F-14`).
- **Fora do escopo desta tarefa:** ligar as frases aos passos (`TLG-T4`); qualquer comando do kit (`TLG-T3`).

## Execução

**Consumo:** 12 tool uses, 53.1 k tokens, 103.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

A copia verbatim foi conferida por diff textual das linhas M-n entre a ### 4.1 do plano e a skill: 15 x 15, identicas byte a byte (fora o CRLF da copia de trabalho). As referencias a loop.py e ao bullet Narra apontam para o que TLG-T3/TLG-T4 ainda vao criar - previsto no card.

## Fechamento

**Desdobramento:** aprovado
