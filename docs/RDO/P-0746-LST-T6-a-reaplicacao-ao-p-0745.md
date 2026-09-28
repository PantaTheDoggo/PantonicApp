# RDO — P-0746 · LST-T6

**Plano:** `docs/plans/P-0746-lastro-do-modelo.md`
**Tarefa:** `LST-T6` — A reaplicação ao `P-0745`
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o modelo do `P-0745` é reautorado sob o conceito revisado — só elementos com lastro no enunciado daquele plano, sem propriedade promovida a objeto e sem ator inexistente —, o que não tem lastro migra para a seção de requisitos secundários dele, e o gate do Marco 1 dele ganha o ramo que faltava.

**Arquivos-alvo:** - `docs/plans/P-0745-planejador-modelo-operacao.md` — seção `## 1` reautorada; seção nova de requisitos secundários; tabela de marcos (ramo `no-go` do Marco 1, pela `DLS-5`)

**Verificação:** 1. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0745-planejador-modelo-operacao.md ``` → exit **0**. **Medido antes desta tarefa: exit 1** (as violações que a `LST-T5` instituiu). 2. O modelo reautorado declara lastro na sexta coluna de `### 1.1`, uma célula não vazia por linha, e todo objeto citado nas linhas de máquina de `### 1.2` existe em `### 1.1` — o que a `V5` já afere. **O teste de ator da versão anterior deste card saiu** (`AE-4`, `F-14`): "ator citado na prosa que não é objeto" não discrimina — o `P-0743`, cujo modelo está aceito, tem 6 dos 7 fora da tabela, e o modelo **deste** plano, 4 dos 4. O defeito que o dono recusou no `P-0745` é a **promoção indevida** (`F-11`), e a guarda dela é o Marco (`F-12`). 3. Nenhum dos elementos que o dono nomeou sem lastro permanece em `### 1.1` do `P-0745`; os que o plano ainda entrega aparecem na seção de requisitos secundários dele — **seção de nível 2 nomeada `Requisitos secundários`, em qualquer posição** (`DLS-15`). O `P-0745` já usa `## 2` para *Fatos estabelecidos*: a seção nova entra sem renumerar nada, e renumerar está fora de escopo. 4. ``` grep -c 'cancelled' docs/plans/P-0745-planejador-modelo-operacao.md ``` → o ramo `no-go = cancelled` do Marco 1 não existe mais na tabela de marcos (`DLS-5`). 5. ``` python -m pytest tests -q ``` → **≥ 262 passed** (`I-3`).

**Pronto quando:** as cinco verificações saem nos valores declarados e o plano está pronto para o Marco 3 — a nova medição do dono. Por propriedade: - `restrições do modelo conceitual.conformidade do modelo` — de não conforme para conforme: o modelo do `P-0745` reautorado sob as restrições construídas e devolvido à medição do dono — Verificação 1, 2 e 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T5`
- **Fundamento:** `DLS-1`, `DLS-2`, `DLS-5`, `DLS-7` (que caduca aqui); fatos `F-1`, `F-2`, `F-3`.
- **Operação do modelo:** `OP-6` - OP-6: O modelador reautora o modelo do plano do planejador sob as restrições construídas e o devolve à medição do dono, provando no caso que originou o enunciado que o modelo convergiu de não conforme para conforme. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** um plano, e só ele. **Executada pelo `pantonic-model-designer`** — todo ato sobre a seção `## 1` de um plano é dele (`F-4`), e a exceção de um ato da `DLS-7` já caducou. Nenhuma tarefa do `P-0745` é executada aqui; o plano dele segue `blocked`.
- **Domínio:** o enunciado de lastro é a `## 0` do **`P-0745`**, mais o prompt de origem dele (pedido do dono de 2026-09-21 transcrito lá) — **não** a `## 0` deste plano.
- **Fora do escopo desta tarefa:** executar qualquer tarefa do `P-0745`; alterar a `## 0` dele; mudar o status dele de `blocked` — quem o destrava é o `go` do dono.

## Execução

**Consumo:** 41 tool uses, 167.4 k tokens, 847.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: modelo do P-0745 reautorado na versao 2 - 3 objetos, 6 propriedades, 6 operacoes, check exit 0 (era 1 com 11 V21), grep cancelled 0, 269 passed; alem da secao 1, da nova secao Requisitos secundarios e da linha do Marco 1, editei tres coisas acopladas ao modelo: o campo Operacao do modelo dos 7 cards (sem isso a V4 dispara e a verificacao 1 nao sai 0), os bullets por propriedade do Pronto quando deles (copias do estado final, DPN-6, que citavam propriedades extintas) e a linha de Riscos que repetia o ramo caduco no-go = cancelled
laudo: Antes do Marco 3: o modelo v2 do P-0745 entrega 5 de 5 atores da secao 1.2 que nao sao objetos da secao 1.1 - exatamente a classe 'ator inedito na operacao' que o dono tipificou no TK-69 secao 3 e chamou de integralmente mecanica, medida por ele em zero de cinco. O loop decidiu nao construir a regra (AE-4, F-14, DLS-13) porque ela reprovaria 6 dos 7 atores do P-0743 aceito e 4 dos 4 do P-0746, e retirou o teste da Verificacao 2 deste card; a decisao esta certa como engenharia e nao e defeito da entrega, mas e uma classe que o dono nomeou e o loop dispensou sem ele. Manter ou dispensar a classe e decisao dele.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Exercicio ponta a ponta: modelo.py check P-0745 exit 0 (6 operacoes, 3 objetos, 6 propriedades, 7 tarefas, versao 2), P-0743 exit 0 (I-2), P-0746 exit 0, backlog.py check OK, show deriva estagio prevista em todas - correto para plano blocked sem tarefa iniciada - e pytest tests -q em 269 passed contra o piso 262. Medida que vale registrar, porque a Verificacao 2 e de juizo e o check so afere presenca: conferi os 23 fragmentos de lastro declarados (5 na 1.1, 12 na 1.2, 6 na 1.3) contra a secao 0 normalizada - 23 de 23 sao recorte verbatim do pedido do dono, inclusive com os erros de digitacao dele preservados. E o modelo do P-0745 declara lastro tambem na 1.2 e na 1.3, de modo que nasce na forma completa a frente do modelo do proprio P-0746, cujo AE-6 segue aberto. A parte dificil foi feita certo: os 11 objetos da versao 1 viraram 3 sem empurrar tudo para Requisitos secundarios - discriminou-se dentro do objeto promovido, em vez de descartar o objeto inteiro, e 21 estados finais viraram seis. Conduta que vale repetir: a pendencia de retorno nomeou os tres acoplamentos tocados alem do recorte, com razao de cada um, e o diff confirma a declaracao linha a linha - 15 hunks fora da secao 1 e nada mais.

## Fechamento

**Desdobramento:** aprovado
