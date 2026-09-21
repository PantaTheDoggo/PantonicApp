# RDO — P-0741 · MC-T4a

**Plano:** `docs/plans/P-0741-modelo-conceitual.md`
**Tarefa:** `MC-T4a` — O gate do modelo no fechamento para de criar o vermelho que devia reparar
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** no `scrum-master`, o gate do modelo do passo 9 roda **antes** da materialização e exit `1` segura a tarefa em `review`; e as duas frases que contam gates passam a contar três.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md` (Passo 3, frase de contagem; Passo 9, linha de `Ação` e parágrafo do gate; Bloco B, célula de condição da linha `B3`)

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'permanece em' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'Aprovados os três' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'a tarefa fica' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. (a frase defeituosa some; era ela que mandava a tarefa a `in-progress`.) 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'do passo 3 (exit' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. (`DMC-31`, quarto passo.) 5. ``` pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T4a --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count" ``` → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)

**Pronto quando:** as cinco linhas acima devolvem o esperado.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Fundamento:** `AE-16` e as decisões `DMC-30` e `DMC-31` do `ESC-5`; a `DMC-27`, cuja premissa (o instante do `check` é o instante em que o reviewer gravou) é o que o passo 9 tinha quebrado.
- **Depende de:** `MC-T4`
- **Oração do modelo:** `M-17` - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico; o orquestrador roda esse instrumento antes de despachar cada tarefa e ao fechar cada tarefa, e modelo inválido bloqueia o despacho e o fechamento.
- **Camada e fronteira:** skill de orquestração; nenhum código. Um arquivo só.
- **Contratos/classes:** nenhum.
- **Passos (cada um um `Edit` com `old_string` único; as quatro âncoras foram contadas pelo consultor em 2026-09-20: uma ocorrência cada):** 1. Passo 9, substituir a linha `- **Ação:** materializar o status com \`python .claude/tools/backlog.py status <ID> <estado>\`.` por `- **Ação:** **primeiro o gate do modelo** (parágrafo ao final desta ação, \`DMC-30\`), e só então materializar o status com \`python .claude/tools/backlog.py status <ID> <estado>\`.` 2. Passo 9, substituir o parágrafo inteiro (cinco linhas do arquivo, com as quebras que ele tem) que começa em `Antes de \`rdo.py close\`, rodar de novo` e termina em `reparo. Exit \`0\` ou \`2\`: fecha.` por: `**Antes de materializar o status**, e portanto antes de \`rdo.py close\`, rodar de novo \`python .claude/tools/modelo.py check --plano <plano>\`: o reviewer acabou de gravar confirmação ou emenda na \`## 1. Modelo conceitual\` (\`GOVERNANCA.md\` §3.2), e exit \`1\` aqui é defeito dessa gravação. Exit \`1\`: **não materializa e não fecha** — a tarefa **permanece em \`review\`**, o stderr vai ao consultor como escalonamento, e o fechamento espera o reparo. \`review\` é o estado em que o reviewer a julgou e um dos três que a \`V6\` conta como fechados, então segurar a tarefa ali não cria vermelho novo; mandá-la a \`in-progress\` criaria — inclusive para oração confirmada por outra tarefa que cite esta — e ainda é transição que não existe (\`done\` para \`in-progress\` não está em \`_TRANSICOES\`). Exit \`0\` ou \`2\`: materializa e fecha.` 3. Passo 3, substituir `Aprovados os dois, e **antes** de delegar, materializar` por `Aprovados os três, e **antes** de delegar, materializar`. 4. Bloco B, substituir a linha inteira `| \`B3\` | a próxima tarefa é recusada pelo \`G-PLANREADY\` ou pelo gate de delegação | não delega: **PARA**, com o que falta fechar |` por `| \`B3\` | a próxima tarefa é recusada pelo \`G-PLANREADY\`, pelo gate de delegação ou pelo \`modelo.py check\` do passo 3 (exit \`1\`) | não delega: **PARA**, com o que falta fechar |`
- **Restrições desta tarefa:** texto verbatim (`I-4`); um arquivo só; da tabela do Bloco B muda **uma** célula, a de condição da linha `B3` — nenhuma outra linha, nenhuma outra tabela, e a precedência do bloco não muda; `passagem-de-bastao` **não** é tocada (lá o `in-progress` está certo: é o estado em que a tarefa já está, e nenhuma oração foi confirmada ainda).
- **Não fazer:** não reescrever o gate do passo 3, que está correto; não mexer nos blocos `A`; não renumerar passos.
- **Contingências:** 1. se qualquer `old_string` não ocorrer exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
- **Testes:** nenhum executável; inspeção mecânica.
- **Fora do escopo desta tarefa:** `passagem-de-bastao`; README e Marco 2 (`MC-T5`); qualquer outra linha das tabelas de roteamento.

## Execução

**Consumo:** 14 tool uses, 53.0 k tokens, 63.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
