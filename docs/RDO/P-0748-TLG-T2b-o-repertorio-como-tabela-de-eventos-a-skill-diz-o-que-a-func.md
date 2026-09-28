# RDO — P-0748 · TLG-T2b

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T2b` — O repertório como tabela de eventos: a skill diz o que a função gera
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:322` — cabeçalho ## Repertório de mensagens ao gerente (única linha que começa assim); a seção vai até a linha anterior à linha em branco que precede ## Proibições (linha 348 em 2026-09-24; localizar pelo texto)

**Verificação:** 1. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "**Narra:**" | Measure-Object).Count` → antes `10` (medido 2026-09-24, `F-26`), depois `9` (some a frase do parágrafo antigo; os nove bullets ficam para `TLG-T4a`). 2. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `2`. 3. Igualdade linha a linha com a `### 4.1` do plano, bloco cercado por conter barra invertida: ``` python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))" ``` → antes `iguais 0 de 15 23` (medido 2026-09-24, depois desta rodada gravar a `### 4.1`), depois `iguais 23 de 23 23`. 4. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "evidência mecânica" | Measure-Object).Count` → antes `2` (medido 2026-09-24: a linha `M-5` e a `- **Ação:**` do passo 6, `:131`), depois `1` (só a do passo 6, que este card não toca). 5. `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "M-17" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 6. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` ≥ o total re-medido no despacho.

**Pronto quando:** `stream de dados.repertório de mensagens` — *fechado e embutido na função que gera a linha: uma frase por evento de transição do loop, no molde do exemplo do dono — "Tarefa X, passo Y.", "Agente executor recebe o passo Y e vai executar Z.", "Agente consultor aceitou a entrega." —, em que cada frase diz o que o ato faz, sem termo que o dono não consiga antecipar: a da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit —, e cada lacuna se preenche pelo campo do evento, não pela mão do condutor* — Verificação 3, 4 e 5 (a parte "embutido na função" é medida por `TLG-T3b`, `TF-GER-18`, contra esta tabela).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-29` (ato do dono: função, agregação, frase da evidência), `DTG-33` (título entre aspas), `DTG-34` (lacunas sem campo), `DTG-35` (a frase da evidência), `DTG-36` (`DTG-10` reescrita: a seção da skill é cópia legível da `### 4.1`), `DTG-37` (ordem: roda antes de `TLG-T3b`, que confere o código contra esta tabela no `TF-GER-18`), `DTG-28` (aceite por conteúdo, não por `numstat`), `F-26`, `I-2`, `I-3`, `I-12`.
- **Depende de:** `TLG-T3a`
- **Operação do modelo:** `OP-2` - OP-2: O redator do loop escreve o repertório fechado de mensagens: uma frase-modelo para cada transição do loop — tarefa e passo, agente despachado e o que vai fazer, veredito recebido, próxima tarefa —, no molde do exemplo do dono, com cada lacuna preenchida só pelo que o condutor já tem em mãos naquele passo. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit, skill `scrum-master`, **só** a seção `## Repertório de mensagens ao gerente` — do primeiro parágrafo depois do cabeçalho até a última linha da tabela, antes da linha em branco que precede `## Proibições`. Os bullets `- **Narra:**` dos passos, o bullet de `## Guardrails` com o marcador e a `passagem-de-bastao` são de `TLG-T4a`; o código é de `TLG-T3b`. Nenhum passo, agente, instrumento, teste ou configuração muda.
- **Domínio:** *frase gerada* = a linha que `progresso_hook.py` grava em `.claude/estado/progresso.txt` no evento nomeado, com as lacunas `<…>` preenchidas por campo do evento ou por leitura local da função (`I-3`); `<título>` = título do card entre aspas duplas, `<título do plano>` = título do plano (`I-12`). *Evento* = disparo de `PreToolUse`, `PostToolUse` ou `Stop` na sessão principal, com a ferramenta e a detecção da coluna 2. O condutor não escreve nenhuma dessas linhas (`I-2`).
- **Contratos/classes:** nenhum código.
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, localizar o cabeçalho `## Repertório de mensagens ao gerente` e o cabeçalho `## Proibições`. 2. Substituir tudo entre a linha em branco depois do primeiro e a linha em branco antes do segundo pelo bloco de `Texto novo, literal`, sem recuo, mantendo uma linha em branco antes e depois. 3. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `DTG-36` — divergência de um caractere entre as 23 linhas da tabela na skill e as da `### 4.1` do plano é defeito (Verificação 3); o parágrafo não cita `**Narra:**`, `[gerente] ` nem `loop.py`; `DTG-28` — nada de `git diff --numstat` como aceite (a seção já é alteração não commitada de `TLG-T2`/`TLG-T2a`): o aceite é por conteúdo, antes e depois. Só esta seção muda.
- **Não fazer:** não editar nenhum bullet `- **Narra:**` nem o bullet de `## Guardrails` (é `TLG-T4a`); não editar passo, `## Proibições`, `## Guardrails`, `passagem-de-bastao`, agente, instrumento, teste, `README.md` ou o plano; não reescrever frase da tabela por conta própria — a tabela é cópia; não acrescentar nem remover linha da tabela.
- **Contingências:** 1. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "## Repertório de mensagens ao gerente" | Measure-Object).Count` não for `1` → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída de `grep -n "Repertório de mensagens ao gerente" .claude/skills/scrum-master/SKILL.md`; 2. se `(Select-String -SimpleMatch -Path .claude/skills/scrum-master/SKILL.md -Pattern "## Proibições" | Measure-Object).Count` não for `1` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "Proibições" .claude/skills/scrum-master/SKILL.md`; 3. se a skill contém `loop.py` → parar e sinalizar `blocked` razão `dependencia` (`TLG-T2a` não entregou).
- **Testes:** nenhum TF (texto de skill); TR: `python -m pytest tests/ -q` não reduz o total re-medido no despacho.
- **Fora do escopo desta tarefa:** o código que gera as frases (`TLG-T3b`); os bullets `**Narra:**`, o guardrail do marcador e a `passagem-de-bastao` (`TLG-T4a`); o `README.md` (`TLG-T5`).

## Execução

**Consumo:** 19 tool uses, 75.2 k tokens, 175.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
