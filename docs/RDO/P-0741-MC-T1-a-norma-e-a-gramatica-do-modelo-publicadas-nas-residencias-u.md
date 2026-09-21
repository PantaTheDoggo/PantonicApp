# RDO — P-0741 · MC-T1

**Plano:** `docs/plans/P-0741-modelo-conceitual.md`
**Tarefa:** `MC-T1` — A norma e a gramática do modelo publicadas nas residências únicas
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` ganha a `### 3.2`, a rubrica ganha o alvo `modelo` e a fronteira nova, e a skill `diario-de-obras` ganha a gramática do modelo — os três com o texto literal das §4 e §5 deste plano.

**Arquivos-alvo:** - `GOVERNANCA.md` §3.1 (inserir a `### 3.2` **depois** do fim da `### 3.1 Residência e precedência da doutrina` e **antes** de `## 4. Fluxo de desenvolvimento`) - `docs/RUBRICA_DE_REVISAO.md` §6 (tabela de alvos) e §7 (parágrafo único) - `.claude/skills/diario-de-obras/SKILL.md` (depois de `### Inbox de planos`, antes de `### Máquina de transições (forma para o instrumento)`)

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern '### 3.2 O modelo conceitual do plano' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'seção do modelo conceitual' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'que a entrega tornou falsa ou ambígua' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -Pattern '### Modelo conceitual (seção do plano)' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern '## 4. Fluxo de desenvolvimento' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 1**. (invariância: a seção seguinte continua única.)

**Pronto quando:** as cinco linhas acima devolvem o esperado e `git diff --stat` lista exatamente os três arquivos-alvo.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Fundamento:** decisões `DMC-1`, `DMC-2`, `DMC-3`, `DMC-4`, `DMC-5`, `DMC-6`, `DMC-7`, `DMC-8`, `DMC-17`; fatos `F-2`, `F-3`, `F-9`. Nenhuma tarefa anterior — por isso o campo `Depende de` está ausente (`DMC-19`).
- **Oração do modelo:** `M-1`, `M-2`, `M-3`, `M-4`, `M-6`, `M-7`, `M-11`, `M-12`, `M-13`, `M-15`, `M-16` - M-1: Todo plano carrega, logo depois do pedido do dono, uma seção chamada "Modelo conceitual": um texto curto, em linguagem corrente, que diz o que o plano entrega e como o resultado funciona, sem siglas, sem nomes de arquivo e sem identificadores técnicos no corpo das frases. - M-2: O modelo é formado por orações numeradas, cada uma afirmando um comportamento observável do que está sendo construído, e por um vocabulário que define cada papel e cada artefato que as orações citam. - M-3: O modelo é um objeto único: existe uma cópia só, dentro do plano, e ela acompanha o plano do primeiro rascunho ao fechamento; não há versão paralela em outro arquivo. - M-4: O modelo é a interface entre o dono e o loop: quem lê só o modelo entende o que o plano faz, o que já está pronto, o que está em andamento e o que mudou desde a última leitura. - M-6: Cada oração é materializada por pelo menos uma tarefa, e cada tarefa materializa pelo menos uma oração; o card da tarefa cita as orações que materializa e copia o texto delas. - M-7: O dono lê o modelo e dá o "go" ou o "no-go" antes de qualquer tarefa ser executada: essa leitura é o primeiro marco de todo plano. - M-11: Toda oração tem um estado que o dono vê: prevista, em curso, entregue ou emendada. - M-12: Ao aprovar a última tarefa que materializa uma oração, o revisor confirma a oração no modelo, registrando a data e a tarefa, se o que foi entregue corresponde ao que a oração afirma. - M-13: O revisor só altera o texto de uma oração quando a entrega tornou a mudança inequívoca e consolidada; na dúvida, registra um achado com alvo "modelo", e a mudança fica para quem replaneja. - M-15: Toda mudança no modelo fica registrada numa lista de mudanças dentro da própria seção, com data, autor, orações afetadas e o que mudou. - M-16: O modelo tem um escritor por ato: quem o altera é sempre o papel que acabou de decidir ou de confirmar algo, no mesmo ato.
- **Camada e fronteira:** documentação de governança do hub; nenhum código. Não toca `.claude/agents/`, `.claude/skills/scrum-master/`, `.claude/skills/passagem-de-bastao/` nem `.claude/tools/`.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Em `GOVERNANCA.md`, localizar a linha `## 4. Fluxo de desenvolvimento`; inserir imediatamente antes dela o bloco cercado da §4 deste plano (o conteúdo, sem as três crases de abertura e fechamento), seguido de uma linha em branco. 2. Em `docs/RUBRICA_DE_REVISAO.md` §6, localizar a linha da tabela que começa com `| \`rubrica\` |`; inserir imediatamente depois dela a linha `| \`modelo\` | … |` da §4 ("Emendas a docs/RUBRICA_DE_REVISAO.md"). 3. Em `docs/RUBRICA_DE_REVISAO.md` §7, substituir o parágrafo inteiro que começa com `O reviewer marca dimensões, anexa achados` pelo parágrafo literal da §4. 4. Em `.claude/skills/diario-de-obras/SKILL.md`, localizar a linha `### Máquina de transições (forma para o instrumento)`; inserir imediatamente antes dela o bloco cercado da §5 (o conteúdo, sem as crases de abertura e fechamento), seguido de uma linha em branco. 5. Em `.claude/skills/diario-de-obras/SKILL.md`, no parágrafo de abertura de `## Gramática legível por máquina` (começa com `Transcrição normativa de`), acrescentar ao final a frase: `A subseção "Modelo conceitual (seção do plano)" transcreve \`docs/plans/P-0741-modelo-conceitual.md\` §5 e é lida por \`.claude/tools/modelo.py\`.`
- **Restrições desta tarefa:** texto verbatim dos blocos (`I-4`); nenhuma outra linha dos três arquivos muda; o nome do arquivo do plano citado no passo 5 é `docs/plans/P-0741-modelo-conceitual.md`.
- **Não fazer:** não renumerar seções existentes de `GOVERNANCA.md`; não tocar a linha *Revisão* da matriz §3 (fica para a `MC-T3`, junto com o agente); não editar `DOC_MAP.md` (`GOVERNANCA.md` já está acima de 500 linhas e sem entrada — o mapa diz que ele dispensa entrada; manter).
- **Contingências:** 1. se `## 4. Fluxo de desenvolvimento` não ocorrer exatamente uma vez em `GOVERNANCA.md` → parar e sinalizar `blocked` razão `premissa`. 2. se a linha `| \`rubrica\` |` não ocorrer exatamente uma vez em `docs/RUBRICA_DE_REVISAO.md` → parar e sinalizar `blocked` razão `premissa`. 3. se `### Máquina de transições (forma para o instrumento)` não ocorrer exatamente uma vez na skill → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum executável; aceite por inspeção mecânica (abaixo).
- **Fora do escopo desta tarefa:** matriz §3 linhas *Planejamento*/*Revisão*/*Orquestração* (`MC-T3`); README (`MC-T5`).

## Execução

**Consumo:** 12 tool uses, 67.3 k tokens, 90.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: git diff --stat lista 5 arquivos, nao 3 - os 2 extras (docs/DIARIO_DE_OBRAS.md, docs/plans/P-0741-modelo-conceitual.md) sao materializacao de status do loop, proibida ao executor pelo card, nao edicao dele
laudo: A norma publicada tranca o proprio fechamento: oracao de tarefa unica confirmada pelo revisor no ato do laudo viola V6 enquanto a tarefa nao e done, e o gate de modelo.py check antes do rdo.py close impede que ela chegue a done - decidir a ordem (confirmar depois do close, ou V6 aceitar a tarefa em review) antes da MC-T2, que codifica V6.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Transcricao literal impecavel: os quatro blocos das 4/5 do plano batem caractere a caractere nas tres residencias, as cinco verificacoes devolvem 1/1/1/1/1 e nenhuma outra linha dos tres arquivos mudou - card de classe redacao com texto literal no proprio card entrega fidelidade sem juizo do executor. Todo o defeito achado e de autoria do texto-fonte, nao de execucao: a coerencia interna do modulo (3.2 x V6 x 6 x 7) nao foi objeto de nenhuma linha de aceite do card.

## Fechamento

**Desdobramento:** aprovado
