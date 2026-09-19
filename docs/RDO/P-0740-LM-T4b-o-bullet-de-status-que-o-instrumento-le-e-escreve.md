# RDO — P-0740 · LM-T4b

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T4b` — O bullet de `Status` que o instrumento lê e escreve
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o loop volta a materializar estado **pelo instrumento**, como o `DM-34` determinou, em vez de à mão.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `tests/fixtures/backlog/` (a fixture nova do aceite de escrita, `ESC-13`)

**Verificação:** (`DM-12`, medido no `ESC-12`) 1. ``` python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog;from pathlib import Path;L=[l for l in Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8').splitlines() if l.startswith('- **Status:**')];print(len(L),sum(1 for l in L if backlog.STATUS_BULLET_RE.match(l)))" ``` → os **dois números iguais** (`<N> <N>`): todo bullet de `Status` do plano é lido. **Medido no `ESC-12`, com o comando publicado: `21 0`** — o segundo número é o que a entrega muda; o primeiro é o total do plano no despacho, **re-medido** por quem despacha e não fixado aqui (`DM-23`, `AE-21`: o total mudou de 18 para 21 durante o próprio `ESC-12`, quando os três cards novos entraram). 2. `python -m pytest tests/test_backlog.py -q` → verde, com **três testes a mais** que o total re-medido no despacho. O aceite do caminho de **escrita** é o teste `TF-escrita-preserva-a-cauda`, que copia a fixture `tests/fixtures/backlog/verde` para o `tmp_path`, troca o bullet de `ALF-T1` pela forma em prosa ``- **Status:** `ready` (2026-01-01) — cauda em prosa que precisa sobreviver``, chama `transacionar_status(... 'ALF-T1', 'in-progress')` e exige **exit 0** com a cauda **preservada** na linha reescrita. **Medido no `ESC-13`, no mundo de hoje, com esse mesmo arranjo:** exit **3**, `linha de status ausente para ALF-T1` — a linha discrimina. **Por que sobre fixture e não sobre o plano real (`AE-28`, `AE-29`):** (a) comando de aceite não altera o estado do plano que o loop está conduzindo; (b) a transição escolhida é `ready → in-progress`, que **está** na tabela de `_TRANSICOES` — a que o card publicava antes (`LM-T2f` para `ready`, sendo ela já `ready`) é um **self-loop fora da tabela**, e exit 1 garantido; (c) medido no `ESC-13`, `backlog.py status` **não alcança tarefa nenhuma deste plano** nem com o parser corrigido, por causa do `AE-29` — que **não** é matéria deste card. 3. `python -m pytest tests/ -q` → verde, com **três testes a mais** que o total re-medido no despacho (`DM-23`).

**Pronto quando:** o campo vizinho que a emenda do `ESC-13` deixou para trás. **Todos** os bullets de `Status` do plano são lidos (os dois números da `Verificação` 1 iguais); `backlog.py status` transita a tarefa da **fixture** (`tests/fixtures/backlog/verde`, cópia em `tmp_path`, `ready → in-progress`) preservando a cauda em prosa — **não** um card real, que o `AE-29` torna inalcançável e que aceite nenhum pode mutar preservando a cauda, os três testes existem e a suíte fica verde.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (re-despachada em 2026-09-19, card reparado pelo `ESC-13`/`DM-35` e pelo `ESC-15`/`DM-38` (ii)) — o `blocked` anterior foi `A3b` com o executor parando **antes de editar qualquer arquivo-alvo** (`AE-28`), e **não consumiu retentativa**. Card novo do `ESC-12` (2026-09-19), residência única do `AE-26`.
- **Esforço:** low
- **Depende de:** `DM-35` (i). **Precede a `LM-T4`**, pela mesma razão da `LM-T4a` (`DM-13` (ii), `AE-5`/`AE-6`): a doutrina não publica gramática que o parser ainda não lê. **Sem exclusão mútua com a `LM-T4`** — arquivos diferentes.
- **O defeito, medido no `ESC-12`:** `python .claude/tools/backlog.py status LM-T2b review` devolve `linha de status ausente`. `STATUS_BULLET_RE` (`:70`) exige ``- **Status:** `<estado>` · AAAA-MM-DD``; o corpus usa a forma em prosa com travessão. Contagem: **0 de 21** bullets de `Status` do `P-0740` casam (eram 18 antes de este mesmo escalonamento acrescentar três cards — o total é **re-medido no despacho**, nunca literal histórico, `AE-21`), e **15 de 34** no repositório inteiro. O `DM-34` mandou materializar estado pelo instrumento e o instrumento não alcança card nenhum deste plano.
- **Produto do módulo:** (a) a **leitura** passa a aceitar a forma em prosa — o estado entre crases é obrigatório; `· AAAA-MM-DD` e a razão viram **opcionais**; tudo que vier depois de ` — ` é **cauda livre**, lida e preservada, nunca interpretada; (b) a **escrita** (`transacionar_status`) reescreve **só o prefixo de máquina** (estado, data, razão) e **preserva a cauda** a partir de ` — `, para não apagar a prosa que o consultor e o loop escrevem ali; (c) o docstring enuncia as duas regras com a contagem medida. ``` - **Status:** `ready` - **Status:** `done` (2026-09-19) — **aprovado 100%**, bloqueante `nenhuma` - **Status:** `blocked` razão `premissa` (2026-09-19, `A3b`) — o executor parou antes de entregar - **Status:** `ready` · 2026-09-19 - **Status:** `ready` · 2026-09-19 · destravada pelo dono ``` **E recusar** (continua sendo `linha de status ausente`): linha sem estado entre crases (`- **Status:** pendente`) e estado fora de minúsculas (`- **Status:** `Ready``). `TR-status-canonico-continua-lido` (a forma estrita com `· data · razão` não regride); `TF-escrita-preserva-a-cauda` (transição de estado sobre um bullet com ` — prosa` mantém a prosa e troca só o prefixo). *Concorrentes:* hoje os cinco literais devolvem `linha de status ausente`, e a escrita substituiria o bullet inteiro.
- **Restrições desta tarefa:** a tabela `_TRANSICOES` fica **intocada** — `('ready','ready')` continuar fora dela é decisão de `DP-F`, não de um card que ensina o instrumento a **ler e escrever um bullet**; inventar self-loop para satisfazer aceite é o inverso do `DM-26` (iii) e do `DM-32`. O vocabulário de estados **não** muda (`ready`, `in-progress`, `review`, `done`, `blocked`, `cancelled` — `DP-F`); `blocked` continua exigindo `--razao`; a forma **canônica** continua sendo a que a escrita produz. Nenhum card do plano é reescrito para caber no parser — é o parser que aprende (`DM-35` (i)).
- **Não fazer:** não tocar `.claude/tools/rdo.py` (é a `LM-T3b`); não tocar `GOVERNANCA.md` (a publicação é a `LM-T4`, item (d)); não tocar os cards do plano; não commitar.
- **Contingências:** 1. se `STATUS_BULLET_RE` ou `transacionar_status` não estiverem na forma citada → parar e sinalizar `blocked` razão `premissa`, citando a encontrada; 2. se a `Verificação` 1 não fechar com os **dois números iguais**, **parar** e sinalizar `blocked` razão `premissa`, citando o par obtido: aceitar um bullet ilegível é deixar o instrumento sem alcançar o plano de novo.

## Execução

**Consumo:** 39 tool uses, 111.8 k tokens, 422.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Decidir a residencia do reparo da fronteira razao/cauda no bullet de Status: o modulo entregue reescreve razao e cauda no mesmo campo e perde a prosa no round trip blocked->ready (P-0740 ou P-0739, que o dono estacionou).

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
