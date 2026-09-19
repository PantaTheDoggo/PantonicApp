# RDO — P-0740 · LM-T5a

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T5a` — A decisão de reagrupamento do `P-0739` e o mapa de herança das superfícies mortas
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — deixar o `P-0739` com a **decisão** de reagrupamento e o **mapa de herança** escritos no próprio arquivo, para que a retomada não redecida nada e não tropece de novo em alvo morto. A **transcrição** dos três módulos **não** é desta tarefa: ela é o primeiro ato da retomada, com a árvore estável.

**Arquivos-alvo:** - `docs/plans/P-0739-backlog-instrumento.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern 'BKL-T10' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1**: a partição está escrita no arquivo que a consome. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern 'herdeira da matéria' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1**: o mapa de herança está escrito. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern 'Absorvida por' -SimpleMatch | Measure-Object).Count" ``` → **5**: um ponteiro por card absorvido, nem mais nem menos. **Medido antes: 0**. 4. ``` python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog as b;from pathlib import Path;m=b.carregar(Path('.'));p=[x for x in m.planos if x.id=='P-0739'][0];print(sorted(t.id for t in p.tarefas if t.status=='ready'))" ``` → `['BKL-T5', 'BKL-T6', 'BKL-T7', 'BKL-T8', 'BKL-T9']`, **inalterado**: esta tarefa **não** transcreve card nenhum, e é esta linha que o prova. **Medido antes: ['BKL-T5', 'BKL-T6', 'BKL-T7', 'BKL-T8', 'BKL-T9']**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path docs/plans/P-0739-backlog-instrumento.md -Pattern '- **Objetivo:**' -SimpleMatch | Measure-Object).Count" ``` → **18**, **inalterado**: nenhum card entra nem sai do arquivo. **Medido antes: 18**. 6. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não toca código. **Medido antes: exit 0** — veredito invariante; referência **datada**: `201 passed` em 2026-09-19.

**Pronto quando:** a nota datada com a partição e o mapa de herança está no `P-0739`, os cinco ponteiros existem, **nenhum card foi criado, reescrito ou teve `Status` mudado** — e as **seis** linhas de `Verificação` saem nos valores declarados, três delas como `inalterado`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — devolvida de `blocked` razão `premissa` pela **segunda** vez, agora com o **produto trocado** (`ESC-35`, saída (c) do `G-REPLAN`). Os dois bloqueios foram conduta correta e mediram coisas diferentes: o primeiro, que a **partição** não estava decidida (fechada no `ESC-34`); o segundo, que a **transcrição** depende de uma árvore que este plano ainda está mudando. **O loop não roda `status`** — o card já está `ready`.
- **Esforço:** low
- **Depende de:** nada. Nada depende desta. O `P-0739` segue **estacionado** por ato do dono.
- **Por que o produto mudou, e por que isto não perde matéria:** a `BKL-T8` tem por alvos `.claude/skills/proximo-passo/SKILL.md` e `.claude/skills/handover/SKILL.md`, que a **`LM-T4` deste plano aposentou e removeu da árvore** (`f1afbd3`); o aceite herdado dela — *Grep `backlog.py` em `.claude/skills/` ≥ 3 arquivos* — ficou **inalcançável** (`AE-64`). Transcrever alvo morto produz card que bloqueia no despacho; suprimir a matéria perde entrega. A saída é **separar decisão de transcrição**: decisão carrega o contexto desta janela e se escreve agora; transcrição mede a árvore e se escreve quando a árvore parar. Os cinco cards ficam **intactos e `ready`** — nada se perde, e o plano estacionado não despacha nenhum deles.
- **Varredura já feita pelo consultor (`ESC-35`), e é ela que fecha a classe:** todos os caminhos citados nos cinco cards foram confrontados com a árvore de hoje. **Mortos: exatamente dois**, e os dois pela mesma `LM-T4` — `.claude/skills/proximo-passo/SKILL.md` e `.claude/skills/handover/SKILL.md`. Não são alvo morto, apesar de ausentes: `backlog_hook.py` (arquivo **a criar** pela matéria da `BKL-T7`), `GOVERNANCA_MEMORIAS.md` (doc global, fora do repo) e os padrões de nome de plano em prosa. **Não há terceira superfície morta**: a varredura não se repete na retomada.
- **Produto do módulo:** - **(a) A nota de replanejamento, datada, no `P-0739`**, com a partição decidida no `ESC-34` transcrita **sem re-decisão**: três módulos — `BKL-T10` (absorve `BKL-T5` + `BKL-T6`), `BKL-T11` (absorve `BKL-T7` + `BKL-T8`), `BKL-T12` (absorve `BKL-T9` sozinha) —, a ordem `BKL-T10` → `BKL-T11` → `BKL-T12`, o encerramento do `AE-10` pelo `AE-47` (a guarda de `transacionar_status` dissolveu a dependência de ordem com os marcadores `<!-- fila:gerada -->`), e a declaração de que **a transcrição dos três cards é o primeiro ato da retomada**, não desta tarefa. - **(b) O mapa de herança**, no mesmo bloco, contendo o literal `herdeira da matéria`: `proximo-passo` e `handover` → **`passagem-de-bastao`** é a **herdeira da matéria** de skill da `BKL-T8`, com `scrum-master` recebendo a parte de condução do loop. Isto **ratifica** o que a `LM-T4` já fez (ela criou a skill nova com o mesmo conteúdo) — não inventa sucessão. No mesmo parágrafo, a regra do número: o aceite herdado *"≥ 3 arquivos"* **não se transcreve**; ele se **re-deriva na retomada** sobre a árvore de então, pela relação *"toda skill que invoca o instrumento o cita"*, nunca por constante copiada (critério (xiii)/(xviii)). - **(c) Um bullet de ponteiro em cada um dos cinco cards**, na forma `- **Absorvida por:** <ID do módulo> na retomada (ESC-34/ESC-35)`, logo abaixo do bullet de `Status`. **O corpo dos cinco não se toca e o `Status` dos cinco não muda** — eles seguem `ready`, porque o plano está estacionado e a transcrição é da retomada.
- **Restrições desta tarefa:** **nenhuma tarefa do `P-0739` é executada**, e **nenhum card dele é reescrito** — nem o corpo, nem o `Status`. A partição **não se re-decide**: ela está fechada no `ESC-34` e aqui só se transcreve. O número do aceite da matéria da `BKL-T8` **não se escreve**: escreve-se a **regra** de re-derivação. Nenhum arquivo de `.claude/` é tocado. Nenhum card do `P-0740` é tocado.
- **Não fazer:** não criar os cards `BKL-T10`..`BKL-T12` (é a retomada que os escreve); não mudar o `Status` dos cinco; não apontar nada para `.claude/skills/proximo-passo/` nem `.claude/skills/handover/`, que não existem; não tratar `backlog.py check` como aceite (`AE-1`); não commitar.
- **Contingências:** 1. se os cinco cards `BKL-T5`..`BKL-T9` não estiverem todos `ready` no despacho → parar e sinalizar `blocked` razão `premissa`, citando os estados encontrados; 2. se a varredura do card não bater com a árvore no despacho — isto é, se aparecer **terceira** superfície morta entre os caminhos citados pelos cinco → **parar** e sinalizar `blocked` razão `premissa`, nomeando-a: decidir herança é do consultor.

## Execução

**Consumo:** 20 tool uses, 72.5 k tokens, 124.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: A retomada do P-0739 abre com dois itens vivos e divergentes na mesma secao - AE-12 (6 cards ready, reescrita pela LM-T5) contra AE-13 desta entrega (5 cards ready, transcricao pela retomada) - e com AE-13 colidindo com o AE-13 vivo do P-0740: reconciliar e ato de autoria em plano estacionado, fora do alcance da execucao e da revisao.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Tres despachos para um card: dois bloqueios em opus (67.1k e 119.8k tk, fonte usage) e a execucao limpa em sonnet (72.5k tk, 20 tool uses). O que destravou nao foi refinar o card e sim trocar o PRODUTO - decisao em vez de transcricao -, e os dois bloqueios mediram coisas diferentes, ambos conduta correta. A revisao saiu barata por uma escolha de autoria: tres das seis linhas de Verificacao provam o que a tarefa NAO fez (conjunto ready, contagem de Objetivo, suite), por comando re-derivavel em vez de prosa - e foram elas que dispensaram varredura manual do diff para atestar que nenhum card foi criado ou reescrito.

## Fechamento

**Desdobramento:** aprovado
