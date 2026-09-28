# RDO — P-0748 · TLG-T2a

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T2a` — O repertório deixa de citar o comando que não vai existir
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:323` — as linhas 323 a 326 e 333 a 335 de 2026-09-24, as sete da tabela do repertório que contêm loop.py (localizar pelo texto)

**Verificação:** 1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "loop.py" | Measure-Object).Count` → antes `7` (medido 2026-09-24), depois `0`. 2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "backlog.py next" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `6`. 3. Igualdade linha a linha com a `### 4.1` do plano, bloco cercado por conter barra invertida: ``` python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))" ``` → antes `iguais 8 de 15 15` (medido 2026-09-24, em `pwsh` e em `powershell`), depois `iguais 15 de 15 15`. 4. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.

**Pronto quando:** `stream de dados.repertório de mensagens` — *fechado: uma frase-modelo por transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —; nenhuma lacuna pede ao condutor uma busca nova para ser preenchida* — Verificação 1 e 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-20` (card corretivo da `OP-2`), `DTG-26` (não há `loop.py`: a próxima tarefa e o dossiê vêm do `backlog.py next`), `DTG-10` (a tabela da skill é cópia da `### 4.1`, que esta rodada corrigiu), `DTG-28` (aceite por conteúdo, não por `numstat`), `F-12`, `F-23`, `I-3`.
- **Depende de:** `TLG-T3`
- **Operação do modelo:** `OP-2` - OP-2: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo. - precisa de: stream de dados — Quem implementa recebe o comportamento do condutor do loop, isto é, o que ele escreve ao dono a cada passo, e o arquivo de progresso que um gancho do próprio kit alimenta com essas linhas. A ferramenta que roda os agentes e a extensão que desenha a tela ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos: o que ele pediu ao agente e o que o agente devolveu. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit, skill `scrum-master`, seção `## Repertório de mensagens ao gerente`: só as sete linhas da tabela que citam `loop.py` (`M-0`, `M-1`, `M-2`, `M-3`, `M-10`, `M-11`, `M-12`), e nelas só as colunas *momento* e *lacunas*. A terceira coluna (a frase-modelo, forma `A` aceita pelo dono no Marco 1) fica idêntica. Nenhum passo, agente ou instrumento muda.
- **Domínio:** *lacuna* = `<…>` na frase-modelo, preenchida por dado que o condutor já recebeu (`I-3`); com `loop.py` fora do plano, a próxima tarefa, o título e o objetivo chegam pela saída do `python .claude/tools/backlog.py next` do passo 2 (`F-12`: primeira linha `=== PRÓXIMA TAREFA: <ID> — <título> [<cabeçalho>]`, depois o card inteiro, inclusive a linha `- **Objetivo:**`; fila vazia imprime `nada delegável`).
- **Contratos/classes:** nenhum código.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, localizar as sete linhas da tabela que contêm `loop.py`. 2. Substituir cada uma, inteira, pela linha de mesmo id de `Texto novo, literal`, sem recuo. 3. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** a terceira coluna de cada linha (a frase-modelo) fica idêntica à de antes — é a forma aceita no Marco 1; `DTG-10` — divergência de um caractere entre as quinze linhas da skill e as da `### 4.1` é defeito (Verificação 3); `DTG-28` — nada de `git diff --numstat` como aceite: as linhas trocadas já são alteração não commitada da `TLG-T2`, e o `numstat` dá o mesmo valor antes e depois. Só estas sete linhas mudam.
- **Não fazer:** não editar a terceira coluna de nenhuma linha; não mexer nas outras oito linhas (`M-4` a `M-9`, `M-13`, `M-14`); não editar passo nenhum da skill nem acrescentar bullet `**Narra:**` (é `TLG-T4`); não editar a `passagem-de-bastao`, agente ou instrumento; não editar o plano.
- **Contingências:** - se o número de linhas da skill que contêm `loop.py` for diferente de `7` antes da edição → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "loop.py" .claude/skills/scrum-master/SKILL.md`; - se alguma das sete linhas com `loop.py` não é linha da tabela `M-<n>` → parar e sinalizar `blocked` razão `premissa` com essa linha.
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho (referência histórica `277 passed`, 2026-09-23).
- **Fora do escopo desta tarefa:** onde cada linha entra no fluxo e a forma com o marcador (`TLG-T4`); o gancho (`TLG-T3`).

## Execução

**Consumo:** 14 tool uses, 54.6 k tokens, 94.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
