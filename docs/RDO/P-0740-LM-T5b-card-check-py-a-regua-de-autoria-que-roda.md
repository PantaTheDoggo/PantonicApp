# RDO — P-0740 · LM-T5b

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T5b` — `card_check.py`: a régua de autoria que roda
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o autor de um card roda **um comando** contra o card que acabou de escrever e ele **falha ruidosamente** quando o aceite não mede o que diz medir.

**Arquivos-alvo:** - `.claude/tools/card_check.py` - `tests/test_card_check.py` - `tests/fixtures/card_check/` (os três cards sintéticos do aceite, `ESC-15`)

**Verificação:** (forma normativa da `### 8.1` da `docs/RUBRICA_DE_REVISAO.md`; baselines medidas pelo consultor no `ESC-15`) 1. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T1 ``` → **exit 0**. **Medido antes: exit 2** (`card_check.py` não existe; `python` sai 2 em `can't open file`). 2. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T2 ``` → **exit 1**, com a linha do item nomeando o elemento ausente (`Medido antes`). **Medido antes: exit 2** (o instrumento não existe). 3. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T3 ``` → **exit 1**, com a linha do item nomeando a divergência entre o valor declarado e a saída medida. **Medido antes: exit 2** (o instrumento não existe). 4. ``` python -m pytest tests/ -q ``` → verde, com **três testes a mais** que o total re-medido no despacho (`DM-23`). **Medido antes: 175 passed** (2026-09-19 — relação, **re-medir no despacho**, critério (xiii)).

**Pronto quando:** `card_check.py` existe com o verbo único; sai **0** em `EX-T1` e **1** em `EX-T2` e `EX-T3`, nomeando em cada caso o elemento ausente ou o valor divergente; recusa comando fora da lista fechada; os três testes existem; e a suíte fica verde.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (despachada em 2026-09-19) — card novo do `ESC-14` (2026-09-19), residência única do passo mecânico que o `DM-37` prescreve. **Sem ele a rubrica da `LM-T5` continua sendo leitura**, e a classe já provou que leitura não a fecha: oito defeitos numa janela, doze critérios em vigor, e o `AE-30` produzido **no mesmo ato** que escreveu o critério contra ele.
- **Esforço:** low
- **Depende de:** `LM-T5` — é ela que fixa a **forma normativa** do bloco `Verificação` (produto (b)) que este instrumento lê. **Precede** o despacho da `LM-T4b` e da `LM-T4`: a re-varredura que o `DM-36` (vi) me atribuiu passa a ser **mecânica**, rodada pelo loop, em vez de leitura de consultor.
- **Produto do módulo:** um verbo só — `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` —, que: (a) recorta o bloco `Verificação` do card pelo mesmo parser de campos que o kit já usa (`rdo._parsear_campos`, **importado, nunca reescrito**); (b) para cada item, exige os **três elementos** da forma normativa — comando em bloco cercado, linha `→` com o esperado, e o literal `**Medido antes: <valor>**`; item incompleto é **falha nomeada**; (c) **roda** cada comando publicado e compara a saída com o `Medido antes` declarado — divergência é falha nomeada, porque significa que o card descreve um mundo que não é o que está na árvore; (d) sai **0** quando todos os itens fecham e **1** com uma linha por item que falhou, dizendo qual dos três elementos falta ou qual valor divergiu.
- **Contrato de segurança (não é detalhe — é o que torna (c) aceitável):** o instrumento só executa comando cujo primeiro token esteja numa **lista fechada** (`python`, `pwsh`) e recusa, com falha nomeada, qualquer linha com `;`, `&&`, `|` fora do bloco cercado, redirecionamento ou substituição de comando. Comando que ele recusa é reportado, **nunca** executado — e o autor o reescreve ou o declara fora do aceite mecânico. sintético cujo `Medido antes` não bate com a saída do comando); `TR-card-integro-sai-zero`. *Concorrentes:* sem (b) o instrumento aprovaria item sem baseline — o `AE-21` inteiro; sem (c) aprovaria baseline envelhecida — o `AE-23`, o `AE-25` e o `AE-30`.
- **Entregável de fixture (acrescentado pelo `ESC-15`, `DM-38` (ii)):** três cards sintéticos em `tests/fixtures/card_check/plano-exemplo.md`, escritos **por esta tarefa**: `EX-T1` conforme à `### 8.1` (os três elementos em todos os itens, com um comando cujo valor bate com a árvore de teste); `EX-T2` com um item **sem** `**Medido antes:**`; `EX-T3` com `**Medido antes:**` cujo valor **não** bate com a saída do comando. São eles o aceite — **nenhum card vivo do plano é aceite deste instrumento** (`DM-38` (ii)).
- **Restrições desta tarefa:** o instrumento **não corrige** card — só afere e reporta; quem reescreve é o autor. Não julga conteúdo do card (objetivo, passos, restrições): só o bloco `Verificação`. Não substitui o `pantonic-reviewer`: roda **antes** do despacho, não depois da entrega. `rdo.py`, `backlog.py` e `review_evidence.py` ficam **intocados** — este é instrumento novo, e a única importação é o parser de campos.
- **Não fazer:** não estender `backlog.py check` (é instrumento do `P-0739`, estacionado, e já sai vermelho com 315 violações pré-existentes, `AE-1`); não rodar comando fora da lista fechada; não tocar card nenhum do plano; não commitar.
- **Contingências:** 1. se a forma normativa que a `LM-T5` publicou divergir dos três elementos citados aqui → parar e sinalizar `blocked` razão `premissa`, citando a forma publicada: quem manda é a rubrica, e o instrumento se ajusta a ela, nunca o contrário; 2. se a `Verificação` 1 sair **1** por baseline envelhecida do próprio `LM-T3b` (o plano mudou entre a autoria e o despacho) → **não** é falha desta tarefa: reportar a divergência ao loop, que a devolve ao consultor — é exatamente o defeito que o instrumento existe para pegar.

## Execução

**Consumo:** 26 tool uses, 106.0 k tokens, 393.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Falso verde residual do card_check: item numerado cujo bloco cercado nao vem logo apos 'N.' e descartado em silencio e o card sai exit 0 com baseline envelhecida por conferir (reproduzido: item com prosa de abertura declarando 'Medido antes: 42' contra comando que imprime 999 -> exit 0); como a 8.1 ja faz do exit 0 o gate de despacho, a correcao e o mecanismo de 'fora do aceite mecanico' precisam de rota de planejamento antes de o gate valer.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
