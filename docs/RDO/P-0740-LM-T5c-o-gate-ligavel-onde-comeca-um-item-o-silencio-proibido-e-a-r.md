# RDO — P-0740 · LM-T5c

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T5c` — O gate ligável: onde começa um item, o silêncio proibido e a recusa por token
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o `card_check` deixa de dar verde a item que ele não leu, e deixa de recusar a forma de comando que o kit usa; com isso o gate da `### 8.1` pode ser ligado.

**Arquivos-alvo:** - `.claude/tools/card_check.py` - `docs/RUBRICA_DE_REVISAO.md` - `tests/test_card_check.py` - `tests/fixtures/card_check/`

**Verificação:** (forma da `### 8.1`, já na gramática que esta tarefa fixa; baselines medidas pelo consultor no `ESC-16`) 1. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T4 ``` → **exit 1**, com a linha `item 1: fora da forma da 8.1`. **Medido antes: tarefa: 'EX-T4'** — **recorte** da saída de hoje (`card_check: FALHOU - tarefa: 'EX-T4' não encontrada em …`), não o código de saída: `exit 1` valeria **nos dois mundos** (antes por fixture ausente, depois por item fora da forma) e seria vacuoso (`DM-24`). O `card_check` confere valor não-`exit N` como **substring da saída**, então esta linha deixa de bater no instante em que a fixture nasce — que é o que ela precisa medir. O recorte **para antes do acento** por causa da matéria 5 abaixo, e volta a poder tê-lo quando ela fechar; cortar antes do acento é recorte do literal, não reescrita dele (`AE-23`). 2. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T5 ``` → **exit 0**: `|` dentro de argumento citado deixa de ser recusa. **Medido antes: tarefa: 'EX-T5'** — pela mesma razão do item 1, a baseline é o literal da saída, não o código. 3. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T6 ``` → **exit 1**, nomeando o marcador `Aferição: manual` sobre comando executável. **Medido antes: tarefa: 'EX-T6'** — literal da saída, pela razão do item 1. 4. ``` python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-exemplo.md --tarefa EX-T1 ``` → **exit 0**, **inalterado**: a fixture conforme continua passando. **Medido antes: exit 0**. 5. ``` python -m pytest tests/ -q ``` → verde, com **cinco testes a mais** que o total re-medido no despacho (`DM-23`). **Medido antes: 178 passed** (2026-09-19 — relação, **re-medir no despacho**, critério (xiii)).

**Pronto quando:** a `### 8.1` diz onde o item começa; nenhum item numerado é descartado em silêncio; `|` e `;` dentro de argumento citado executam; `**Aferição: manual**` existe e é rejeitado sobre comando executável; saída acentuada de subprocesso é comparável; os **cinco** testes existem; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (despachada em 2026-09-19) — card novo do `ESC-16` (2026-09-19), residência única das **quatro** matérias do `AE-32` — **mais a quinta matéria** que o `ESC-16` mediu ao rodar o instrumento contra este próprio card (codificação da saída capturada). Elas vêm num card só porque são **um assunto só** (`DM-2`): tornar o `card_check` confiável o bastante para virar gate. Partir em dois criaria exclusão mútua sobre os **mesmos dois arquivos** e entregaria, no meio do caminho, um instrumento que ainda não pode ser ligado.
- **Esforço:** low
- **Depende de:** `LM-T5b` (fechada — é o instrumento dela que esta tarefa corrige) e `LM-T5` (fechada — é a `### 8.1` dela que esta tarefa emenda). **Precede o despacho da `LM-T4b`, da `LM-T4`, da `LM-T3b` e da `LM-T6`**: enquanto ela não fecha, o loop re-deriva baseline à mão, que é o custo que esta tarefa elimina.
- **As quatro matérias, medidas no `ESC-16` sobre o código entregue:** 1. **Falso verde por descarte silencioso.** `_ITEM_HEAD_RE = re.compile(r"\d+\.\s*```")` (`:66`) só enxerga item cujo bloco cercado venha **imediatamente** após `N.`; item com prosa de abertura **não entra** na lista `heads` e portanto não é reportado. Quando **nenhum** item casa, o instrumento diz *"nenhum item reconhecido"* e falha (medido: `--tarefa LM-T3b` → **exit 1**); quando **alguns** casam, os demais somem sem uma linha sequer — que é o caso que o reviewer reproduziu (`Medido antes: 42` contra saída `999` → exit 0). 2. **A norma não define onde começa o item.** A `### 8.1` diz *"o comando, em bloco cercado"* e não diz que ele abre o item; prosa antes é legítima pela letra, e é a forma do item 1 da `LM-T3b`, card que a `### 8.2` julga **"passa"**. 3. **Recusa por substring, sobre execução sem shell.** `_METACARACTERE_RECUSADO_RE` (`:71`) varre a **string crua**, mas `_rodar_comando` executa `subprocess.run(tokens)` **sem `shell=True`** (`:136`, medido): `;`, `|` e `$` **dentro de um argumento citado** não são operadores, são texto. Efeito medido: os **4** itens da `LM-T2e` saem *"comando recusado"* (exit 1), e o item 1 da `LM-T5a` também — a forma canônica do kit, `pwsh -NoProfile -Command "(Select-String … | Measure-Object).Count"`, é recusada por segurança que o modo de execução já garante. 4. **O contrato de segurança não tem teste** — só a verificação em execução do reviewer. 5. **A saída capturada vem com a codificação trocada, e isso inviabiliza baseline por texto.** Medido no `ESC-16`, rodando o próprio instrumento: `_rodar_comando` chama `subprocess.run(tokens, …, text=True)` **sem `encoding`**, de modo que o Windows decide pela `cp1252` e a saída chega como `tarefa: 'EX-T4' nÃ£o encontrada`. Consequência direta: **nenhum `Medido antes` com acento pode bater**, e o autor é empurrado a reescrever o literal da fonte sem acento — que é exatamente o `AE-23`, agora induzido pelo instrumento. O arquivo já tem `_forcar_utf8` para os próprios fluxos; falta aplicá-lo ao que ele lê do subprocesso.
- **Produto do módulo:** (a) `### 8.1` emendada: **o item começa em `N.` seguido imediatamente do bloco cercado**; prosa explicativa vai **depois** do `**Medido antes:**`, nunca antes do comando; (b) o instrumento varre `^\s*\d+\.` e **nomeia todo item numerado que não casar a forma** — `item N: fora da forma da 8.1 (bloco cercado não vem logo após "N.")` — e falha; **descarte silencioso é proibido**, e é esta metade que fecha o falso verde; (c) `_validar_comando` passa a decidir **por token**, depois de `shlex.split`: recusa quando um **token isolado** é operador de shell (`;`, `&&`, `||`, `|`, `>`, `>>`, `<`) ou começa por `$(`/crase, e **não** recusa pelo conteúdo de argumento citado — a justificativa é o modo de execução, e o docstring passa a dizê-la; (d) marcador **`**Aferição: manual**`**, na mesma linha do `**Medido antes:**`, aceito **somente** quando o comando é recusado por (c) ou quando o item não tem comando executável: o item é reportado como `manual`, **não** é executado, e continua exigindo os elementos 2 e 3. Se o comando **for** executável, o marcador é **rejeitado** com falha nomeada — senão vira porta dos fundos; (e) teste do contrato de segurança (matéria 4); (f) `_rodar_comando` decodifica a saída do subprocesso como **UTF-8** (`encoding="utf-8", errors="replace"`), de modo que `Medido antes` com acento volte a ser comparável (matéria 5). `EX-T4` com item de prosa antes do bloco; `EX-T5` com `pwsh -NoProfile -Command "(… | Measure-Object).Count"` cujo valor bate; `EX-T6` com `**Aferição: manual**` sobre comando **executável**. (e o contrato de segurança travado, matéria 4); `TR-pipe-dentro-de-argumento-citado-executa`; `TF-afericao-manual-sobre-comando-executavel-e-rejeitada`; `TF-saida-acentuada-do-subprocesso-e-comparavel` (matéria 5: comando que imprime texto acentuado, `Medido antes` com acento, tem de bater).
- **Restrições desta tarefa:** a lista fechada de executáveis (`python`, `pwsh`) **não** se alarga. O instrumento continua **sem** `shell=True` — é essa propriedade que justifica (c), e perdê-la invalidaria a decisão inteira. A `### 8.2` (o julgamento dos 20 cards) fica **intocada**: o veredito da `LM-T3b` como *"passa"* é registro do que a rubrica dizia **naquele dia**, e re-julgar card é tarefa de auditoria, não desta. Nenhum card do plano é reautorado aqui (`DM-38` (i): normaliza-se no ato do despacho).
- **Não fazer:** não ligar o gate por conta própria — o `Status` do gate é decisão do loop, registrada no `DM-39` (ii); não tocar `.claude/tools/rdo.py`; não tocar os outros cards do plano; não commitar.
- **Contingências:** 1. se `_rodar_comando` não estiver sem `shell=True` no despacho → parar e sinalizar `blocked` razão `premissa`: a premissa de (c) caiu; 2. se a emenda à `### 8.1` tornar **qualquer** das fixtures `EX-T1`..`EX-T3` inválida → parar e sinalizar `blocked` razão `premissa`, citando qual: norma nova que invalida o aceite vigente é decisão de consultor.

## Execução

**Consumo:** 46 tool uses, 134.7 k tokens, 618.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: O gate da 8.1 nao pode ser ligado com o instrumento como entregue: ele reprova card conforme a norma que ele mede (falso vermelho por numero com ponto na prosa legitima, medido no proprio card LM-T5c e num card sintetico integral), e a materia 5 so fechou para filho que emite utf-8, tendo regredido o filho cp1252 - decisao de rota sobre o marcador de item e sobre a politica de decodificacao.

## Laudo

**Veredito:** ressalva

**Percentual:** 76%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
