# P-0741 — O modelo conceitual do plano: a interface entre o dono e o loop

**Data:** 2026-09-19 · **Origem:** pedido do dono, 2026-09-19 ("melhoramento do agente de
planejamento — agregar o modelo conceitual do DDD") · **Status:** `ready` ·
**Prefixo das tarefas no diário:** `MC-T<n>` · **Prefixo das decisões:** `DMC-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`DE-7`), nada a comparar.
**Ordem de execução:** MC-T1 → MC-T2 → MC-T2a → MC-T3 → MC-T4 → MC-T4a → MC-T2b → MC-T5
**Modelo de planejamento:** Fable 5.1, por decisão explícita do dono nesta sessão (tabela de
`GOVERNANCA.md` §3, linha *Planejamento*).

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | a seção `## 1. Modelo conceitual` deste plano, e só ela | `go` = aprovar este plano; `no-go` = plano `cancelled`, nada executado |
| **Marco 2** | a visão do modelo gerada por `modelo.py show` sobre este mesmo plano, depois de `MC-T5`, mais o `README.md` revisado | aceite registrado no diário (`GOVERNANCA.md` §4.5) |

**Tarefas:** 5 (`MC-T1`..`MC-T5`), todas em fila única; nenhuma roda em paralelo.

---

## 0. O problema, verbatim

> Inicie uma etapa de planejamento do melhoramento do agente de planejamento.
> Neste plano, vamos agregar ao agente de planejamento um dos conceitos do DDD, que é o modelo
> conceitual, que consegue agregar tanto do design como a intuição do plano.
> Eu entendo importante que o modelo seja um objeto único durante todo o plano, que sempre estará
> no corpo desse plano, aceitando atualizações pontuais e ajustes, mas sempre deverá refletir o
> desenvolvimento sendo realizado.
> Ele será a interface de comunicação entre o usuario e o agente.
> Isso é importante porque muitas vezes em me perco no trabalho atual dos agentes, e fico perdido
> quando sou demandado para responder, e recebo muitas siglas e informações descontextualizada.
> Como eu penso nesse modelo: por exemplo, o modelo conceitual deste plano seria a descrição de
> tudo o que esse modelo deverá fazer, como os agentes o utilizarão, como ele será atualizado,
> como ele será consumido.
> Por exemplo, eu vejo esse texto no corpo do plano, cada oração desse modelo será desmembrado em
> tarefas pelo agente de planejamento. Os executores vão performar. E, na entrega, o reviewer irá
> conferir o trabalho e atualizar o modelo conceitual. por exemplo, eu estabeleci que no modelo
> que o agente reviewer vai atualizar o modelo a cada iteração, mas o agente entende que deve
> atualizar apenas em trechos de mudança sem ambiguidade, consolidadas. Então esse novo mecanismo
> deverá ser atualizado no modelo
> O objetivo final é que eu consiga me inteirar do plano inteiro só lendo o modelo previsto nesta
> tarefa.
> Esse plano deverá especificar as diretrizes, os mecanismos de operação, as estruturas de dados
> usadas para consumo, as rotinas, as localidades onde essas rotinas estarão especificadas. O
> primeiro marco será a geração desse modelo de como funcionará o modelo.
> Se eu conseguir compreender o trabalho com base apenas nesse modelo proposto, eu darei o "go".
> Do contrário, se eu achar muito confuso, muito oneroso, com pouca validade, será "no-go".

**O que o plano entrega quando termina:** todo plano novo nasce com um modelo conceitual no
corpo, escrito antes das tarefas; o executor recebe as orações no card; o revisor confirma ou
emenda o modelo ao aprovar cada entrega; um instrumento confere a integridade do modelo e gera a
leitura do dono; e o dono se inteira de qualquer plano lendo só essa leitura.

---

## 1. Modelo conceitual

> **Como ler esta seção (Marco 1).** Ela descreve, em linguagem corrente, o que é o modelo
> conceitual, quem o escreve, quem o lê, como ele muda e como se confere que está íntegro. É o
> próprio mecanismo aplicado a si mesmo: esta seção **é** o modelo conceitual deste plano, e será
> confirmada e emendada pelas regras que ela mesma descreve, tarefa a tarefa. Se você entende o
> trabalho lendo só esta seção, o plano está pronto para o `go`.

**Estado do modelo:** versão 9 · 2026-09-20 · autor: planejador · 20 orações · última mudança: MD-9

### 1.1 Vocabulário

| termo | o que significa aqui |
|---|---|
| plano | o documento que descreve uma entrega completa: o pedido, o modelo, as decisões e as tarefas |
| tarefa (ou card) | a menor unidade de trabalho do plano, executada inteira por um executor, num contexto só |
| oração | uma frase numerada do modelo, afirmando um comportamento observável do que está sendo construído |
| dono | você: quem pede, quem valida e quem dá `go` ou `no-go` |
| planejador | o agente que escreve o plano, o modelo e as tarefas, no modelo de linguagem mais caro |
| executor | o agente barato que implementa uma tarefa lendo só o card dela; não decide nem pergunta |
| revisor | o agente que julga a entrega de uma tarefa e emite o laudo; é o único que confirma que algo foi entregue |
| consultor | o agente que fica de standby durante a execução de um plano e desbloqueia impedimentos, reparando o plano |
| orquestrador | o procedimento que conduz o plano tarefa a tarefa (despacha executor e revisor, fecha cada tarefa, relata ao dono) |
| laudo | o documento que o revisor emite sobre uma entrega: veredito calculado e achados |
| achado | um problema registrado com rota de solução; nunca fica só em prosa |
| instrumento | um programa do kit que executa uma rotina mecânica com saída fixa e código de saída |
| marco de validação | o ponto em que o loop para e o dono valida o entregável |
| janela | uma sessão contínua de execução do loop, que termina por decisão de coesão ou por ocupação de contexto |
| replanejamento | a rodada em que o planejador altera o plano por causa de um achado da execução |
| escalonamento | o ato de mandar um impedimento ao consultor durante a execução |

### 1.2 As orações do modelo

**A. O que o modelo é**

- **M-1** — Todo plano carrega, logo depois do pedido do dono, uma seção chamada "Modelo conceitual": um texto curto, em linguagem corrente, que diz o que o plano entrega e como o resultado funciona, sem siglas, sem nomes de arquivo e sem identificadores técnicos no corpo das frases.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T1, MC-T3`
- **M-2** — O modelo é formado por orações numeradas, cada uma afirmando um comportamento observável do que está sendo construído, e por um vocabulário que define cada papel e cada artefato que as orações citam.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T1, MC-T3`
- **M-3** — O modelo é um objeto único: existe uma cópia só, dentro do plano, e ela acompanha o plano do primeiro rascunho ao fechamento; não há versão paralela em outro arquivo.
  - `estado: confirmada · 2026-09-20 · MC-T1` · `tarefas: MC-T1`
- **M-4** — O modelo é a interface entre o dono e o loop: quem lê só o modelo entende o que o plano faz, o que já está pronto, o que está em andamento e o que mudou desde a última leitura.
  - `estado: confirmada · 2026-09-20 · MC-T5` · `tarefas: MC-T1, MC-T5`

**B. Quem escreve o modelo, e quando**

- **M-5** — O planejador escreve o modelo antes de decompor o plano em tarefas: primeiro diz o que o resultado faz, depois desmembra cada oração em tarefas.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T3`
- **M-6** — Cada oração é materializada por pelo menos uma tarefa, e cada tarefa materializa pelo menos uma oração; o card da tarefa cita as orações que materializa e copia o texto delas.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T1, MC-T2, MC-T3`
- **M-7** — O dono lê o modelo e dá o "go" ou o "no-go" antes de qualquer tarefa ser executada: essa leitura é o primeiro marco de todo plano.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T1, MC-T3`

**C. Quem lê o modelo durante a execução**

- **M-8** — O executor lê só o card da tarefa, e o card já traz o texto das orações que ele materializa; o executor nunca edita o modelo.
  - `estado: confirmada · 2026-09-20 · MC-T4` · `tarefas: MC-T3, MC-T4`
- **M-9** — O orquestrador mostra o modelo ao dono no relatório de encerramento de cada janela e em cada marco de validação, usando a leitura gerada pelo instrumento: cada oração com o estado atual e as mudanças desde a última leitura.
  - `estado: confirmada · 2026-09-20 · MC-T4` · `tarefas: MC-T4`
- **M-10** — O dono se inteira de qualquer plano em andamento pedindo a leitura do modelo, sem abrir tarefas, achados ou laudos.
  - `estado: confirmada · 2026-09-20 · MC-T4` · `tarefas: MC-T2, MC-T4`

**D. Como o modelo muda**

- **M-11** — Toda oração tem um estado que o dono vê: prevista (ainda não entregue), em curso (alguma tarefa dela em execução), entregue (o revisor confirmou que a oração é verdadeira no repositório) ou emendada (o texto mudou por decisão e a entrega ainda não confirmou o texto novo).
  - `estado: confirmada · 2026-09-20 · MC-T2` · `tarefas: MC-T1, MC-T2`
- **M-12** — Ao aprovar a última tarefa que materializa uma oração, o revisor confirma a oração no modelo, registrando a data e a tarefa, se o que foi entregue corresponde ao que a oração afirma.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T1, MC-T3`
- **M-13** — O revisor só altera o texto de uma oração quando a entrega tornou a mudança inequívoca e consolidada, como quando o mecanismo entregue difere do descrito e a entrega foi aprovada assim; na dúvida, ele não altera: registra um achado com alvo "modelo", e a mudança fica para quem replaneja.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T1, MC-T2, MC-T3`
- **M-14** — O planejador, em rodada de replanejamento, e o consultor, em escalonamento, emendam o modelo sempre que uma decisão nova muda o que o plano entrega ou como funciona; a emenda cita a decisão que a motivou.
  - `estado: confirmada · 2026-09-20 · MC-T3` · `tarefas: MC-T3`
- **M-15** — Toda mudança no modelo fica registrada numa lista de mudanças dentro da própria seção, com data, autor, orações afetadas e o que mudou; o dono lê essa lista para saber o que mudou desde a última leitura.
  - `estado: confirmada · 2026-09-20 · MC-T2` · `tarefas: MC-T1, MC-T2`
- **M-16** — O modelo tem um escritor por ato: quem o altera é sempre o papel que acabou de decidir ou de confirmar algo, no mesmo ato da decisão ou da confirmação; nenhum papel altera o modelo por iniciativa própria.
  - `estado: confirmada · 2026-09-20 · MC-T1` · `tarefas: MC-T1`

**E. Como se confere que o modelo está íntegro**

- **M-17** — Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico; o orquestrador roda esse instrumento antes de despachar cada tarefa e ao fechar cada tarefa, e modelo inválido bloqueia o despacho e o fechamento.
  - `estado: confirmada · 2026-09-20 · MC-T2b` · `tarefas: MC-T2, MC-T2a, MC-T2b, MC-T4, MC-T4a`
- **M-18** — O mesmo instrumento gera a leitura do dono, com estados e mudanças, para que a leitura seja sempre derivada do modelo real e nunca redigida à mão.
  - `estado: confirmada · 2026-09-20 · MC-T2` · `tarefas: MC-T2`
- **M-19** — Planos anteriores a esta regra não ganham modelo retroativamente; o instrumento os reconhece como anteriores e não os bloqueia.
  - `estado: confirmada · 2026-09-20 · MC-T2` · `tarefas: MC-T2`
- **M-20** — Este plano é o primeiro a usar o modelo: a seção que você está lendo é o modelo dele, e ela é confirmada e emendada pelas próprias regras que descreve, tarefa a tarefa, até o segundo marco, quando o dono lê a leitura gerada pelo instrumento e valida.
  - `estado: confirmada · 2026-09-20 · MC-T5` · `tarefas: MC-T5`

### 1.3 Mudanças do modelo

| id | data | autor | orações | o que mudou e por quê |
|---|---|---|---|---|
| MD-1 | 2026-09-20 | consultor · ESC-2 | M-17 | "confirmada com tarefa ainda aberta" passou a "confirmada com tarefa que ainda não foi entregue para revisão": a confirmação é ato do revisor, e no instante do laudo a tarefa está em revisão, não fechada (`DMC-20`) |
| MD-2 | 2026-09-20 | consultor · ESC-2 | M-3, M-16 | gravada a confirmação retroativa das duas orações materializadas só pela `MC-T1`, com base no laudo `aprovado 100 bloqueante=nenhuma` já emitido; ato excepcional do regime transitório, porque o revisor daquela tarefa ainda não tinha a ferramenta de escrita (`DMC-21`) |
| MD-3 | 2026-09-20 | consultor · ESC-3 | M-17 | a lista de tarefas ganhou a `MC-T2a`, card novo que remove da dataclass do instrumento o campo sem consumidor; o texto da oração não mudou (`DMC-26`) |
| MD-4 | 2026-09-20 | revisor · MC-T3 | M-11, M-15, M-18, M-19 | confirmadas as quatro orações vencidas pela `MC-T2` e pela `MC-T1`, que nenhum revisor pôde gravar porque a ferramenta de escrita só passou a existir nesta tarefa; ato do regime transitório `DMC-21`, sem alteração de texto. As orações da `MC-T3` seguem `prevista`: `V6` recusa `confirmada` enquanto o card estiver `in-progress`, e o campo `Status` fica fora da única escrita do revisor |
| MD-5 | 2026-09-20 | revisor · MC-T3 | M-1, M-2, M-5, M-6, M-7, M-12, M-13, M-14 | confirmadas as oito orações do campo `Oração do modelo` da `MC-T3`, com a entrega conferida no repositório (esqueleto do planejador com a seção do modelo na posição 1, parágrafo do modelo antes das tarefas, item de rastreabilidade, campo `Oração do modelo` na anatomia do card, `Edit` e passo `5a` no revisor, emenda em escalonamento no consultor e na rodada de replanejamento); nenhum texto alterado. Gravação represada pelo `MD-4`: a `V6` recusava `confirmada` com o card em `in-progress`, e o loop pôs a `MC-T3` em `review` pelo passo 5 da `scrum-master` |
| MD-6 | 2026-09-20 | consultor · ESC-4 | M-17 | a lista de tarefas ganhou a `MC-T2b`, card que fecha a cadeia sem consumidor deixada pela `MC-T2a`; o texto da oração não mudou (`DMC-29`) |
| MD-7 | 2026-09-20 | consultor · ESC-5 | M-17 | a lista de tarefas ganhou a `MC-T4a`, card que corrige o desfecho do gate de fechamento no `scrum-master`; o texto da oração não mudou (`DMC-30`) |
| MD-8 | 2026-09-20 | revisor · MC-T5 | M-4, M-20 | confirmadas as duas últimas orações previstas, com a entrega conferida no repositório: a subseção do modelo entrou verbatim na documentação pública, a frase do fluxo remete a ela, a região gerada do inventário do kit foi reescrita por instrumento e as quatro conferências do card saem no esperado. Nenhum texto alterado. Com esta gravação as vinte orações estão `confirmada` e o regime transitório de confirmação (`DMC-21`) expira. Ressalva registrada no laudo: a última cláusula da `M-20` só se completa quando o dono ler a leitura do instrumento e validar o segundo marco — ato posterior a esta revisão |
| MD-9 | 2026-09-20 | planejador · RP-1 | M-2, M-11, M-12, M-13, M-16, M-17 | **supersessão de doutrina, sem alteração de texto.** A diretiva do dono no Marco 2 (`AE-18`) substituiu a forma que estas seis orações descrevem: a oração independente com estado por frase dá lugar a objetos com contrato e operações encadeadas (`D-1` do `P-0743`); o estado gravado dá lugar a estágio derivado do andamento das tarefas, e nenhum papel grava (`D-2`); a escrita no modelo passa a ser ato único do `pantonic-model-designer` (`D-5`), e o revisor deixa de gravar e de emendar (`D-8`). O texto das vinte orações **não muda** e o estado delas continua `confirmada`: elas afirmam o que este plano entregou, e o que entregou está de pé — palavras do dono no `AE-18`. A forma nova não retroage sobre este plano (`D-3`, `D-10` do `P-0743`): a partir da `DOM-T3` daquele plano, `modelo.py check` reconhece este arquivo como forma anterior e sai `2` sem bloquear nada. Plano sucessor: `docs/plans/P-0743-modelo-de-dominio.md` |

---

## 2. Fatos estabelecidos

Todos apurados nesta sessão por leitura direta (o planejador rodou no contexto principal, sem
scout disponível por decisão do harness), com fonte nomeada.

- **F-1** — O esqueleto fixo do plano no planner tem nove seções, `## 0. O problema, verbatim`
  até `## 8. Achados da execução`, e a anatomia do card tem treze campos, de `Objetivo` a `Fora
  do escopo desta tarefa`; não existe campo que ligue card a uma frase do modelo
  (`.claude/agents/pantonic-planner.md`, seções *Fase 3 — Autoria* e *Anatomia do card*).
- **F-2** — O revisor tem `tools: Read, Glob, Grep, Bash` e a fronteira do papel diz que ele
  "não edita os arquivos da tarefa" (`.claude/agents/pantonic-reviewer.md` linha 5;
  `docs/RUBRICA_DE_REVISAO.md` §7). O laudo é "consumido e descartado" (`rdo.py close` apaga o
  laudo, `scrum-master` passo 9).
- **F-3** — O achado de processo do laudo tem três alvos fechados, `dossiê`, `doutrina`,
  `rubrica`, validados por `_ALVOS_ACHADO` em `.claude/tools/rdo.py` (linhas 506-538) e
  normatizados em `docs/RUBRICA_DE_REVISAO.md` §6.
- **F-4** — O consultor "repara o modelo funcional do plano" (expressão solta, duas ocorrências
  em `.claude/agents/pantonic-consultant.md`, sem artefato definido); a
  `docs/consultant-spec.md` §4 registra que a fronteira medida com o planejador é "nunca reabrir
  o objetivo do plano", e §10 deixa a norma de autoria de card em aberto.
- **F-5** — `backlog.py` classifica todo heading `## X — Y` e `### X — Y` por `HEADING_RE`
  (`.claude/tools/backlog.py:72`) e **ignora** os que não casam `TK-<n>` ou `<PFX>-T<n>`
  (`_classify_item_heading`, linhas 179-195): um heading de nível 2 ou 3 cujo id não é de
  tíquete nem de tarefa devolve `None`. Consequência: a seção do modelo pode usar headings
  `## 1. Modelo conceitual` e `### 1.2 As orações do modelo` sem colidir com o corpus do
  instrumento, desde que **nenhuma oração seja heading** — orações são bullets.
- **F-6** — `backlog._parse_plano(caminho: Path, repo: Path) -> Plano` devolve `Plano.tarefas:
  list[Item]`, e cada `Item` tem `id`, `status`, `linha_header`, `linha_fim`
  (`.claude/tools/backlog.py:112-147, 319`). `tests/test_backlog.py:30` carrega o módulo por
  `importlib.util.spec_from_file_location`; `card_check.py` carrega `rdo.py` do mesmo modo
  (`.claude/tools/card_check.py:38-45`) — `.claude/` não é pacote importável.
- **F-7** — `rdo._parsear_campos` lê campos de card como `- **Rótulo:** conteúdo`
  (`_CAMPO_RE`, `.claude/tools/rdo.py:95`) e junta linhas de continuação com espaço
  (`card_check.py`, comentário da linha 70). Um rótulo novo é um campo a mais no dicionário;
  nenhum dos três parsers rejeita rótulo desconhecido (não há lista fechada de rótulos em
  `rdo.py`, `review_evidence.py` ou `backlog.py` — `grep -n "Objetivo" .claude/tools/*.py`
  devolve só docstrings).
- **F-8** — A forma normativa do bloco `Verificação` é: item `N.` seguido imediatamente do
  comando em bloco cercado, linha `→ **<esperado>**. **Medido antes: <valor>**.`
  (`docs/RUBRICA_DE_REVISAO.md` §8.1); `card_check.py` a lê e roda o comando, aceitando
  primeiro token `python` ou `pwsh` e a forma `exit <n>` como valor. O gate está suspenso em
  efeito (`AE-33` do `P-0740`), e a conferência é manual por quem despacha.
- **F-9** — Valores medidos em 2026-09-19, todos com `Select-String -SimpleMatch` (contagem de
  linhas) ou `Test-Path`:

  | arquivo | literal | antes |
  |---|---|---|
  | `GOVERNANCA.md` | `### 3.2 O modelo conceitual do plano` | 0 |
  | `docs/RUBRICA_DE_REVISAO.md` | `seção do modelo conceitual` | 0 |
  | `.claude/skills/diario-de-obras/SKILL.md` | `### Modelo conceitual (seção do plano)` | 0 |
  | `.claude/agents/pantonic-planner.md` | `## 1. Modelo conceitual` | 0 |
  | `.claude/agents/pantonic-planner.md` | `**Oração do modelo:**` | 0 |
  | `.claude/agents/pantonic-reviewer.md` | `tools: Read, Glob, Grep, Bash, Edit` | 0 |
  | `.claude/agents/pantonic-reviewer.md` | `modelo conceitual` | 0 |
  | `.claude/agents/pantonic-consultant.md` | `modelo funcional` | 2 |
  | `.claude/agents/pantonic-consultant.md` | `modelo conceitual` | 0 |
  | `.claude/skills/scrum-master/SKILL.md` | `modelo.py show` | 0 |
  | `.claude/skills/passagem-de-bastao/SKILL.md` | `modelo.py check` | 0 |
  | `README.md` | `modelo conceitual` | 1 (linha 393, o artefato *Architecture* — não é este conceito) |
  | `.claude/tools/modelo.py` | `Test-Path` | False |
  | `tests/test_modelo.py` | `Test-Path` | False |
  | `tests/fixtures/modelo` | `Test-Path` | False |

- **F-10** — `git check-ignore -q` sobre `.claude/tools/modelo.py`, `tests/test_modelo.py` e
  `tests/fixtures/modelo/plano-exemplo.md` sai **1** (não ignorados) em 2026-09-19. Nenhum
  instrumento do kit é registrado em manifesto: `card_check` não aparece em nenhum `.ps1`,
  `.json`, `.toml` ou `.ini` do repositório; `kit_check.ps1` gera tabelas a partir de
  `.claude/agents/*.md` e `.claude/skills/*/SKILL.md` e cita só `tools/materializar.py`.
- **F-11** — `python -m pytest tests --co -q` coletou **201** testes em 2026-09-19 (referência
  datada; o piso é relação, `DM-23`).
- **F-12** — `check-readme.ps1` compara a contagem de agentes e de skills declarada na frase de
  *Anatomia do kit* com o disco (`.claude/checks/check-readme.ps1:160-167`); este plano não cria
  agente nem skill, então as contagens não mudam. O `README.md` tem as seções `## 5. O fluxo
  plano → execução`, `## 6. O loop de execução` e `## 8. Planos: o que é um plano fechado`
  (linhas 376, 446, 594 em 2026-09-19), sem subseções.
- **F-13** — O prefixo de decisão `DC-` tem 36 ocorrências em `docs/plans/*.md`, diário e
  `GOVERNANCA.md`; `DMC-` tem zero; `MC-T` tem zero. Próximo id de plano declarado no
  `_INBOX.md`: **P-0741**.
- **F-14** — O `scrum-master` tem dez passos; o passo 3 roda os gates herdados antes de
  materializar `in-progress`; o passo 9 fecha por `rdo.py close`; o relatório de encerramento é
  "ponteiros e números, nunca conteúdo" (`.claude/skills/scrum-master/SKILL.md` linhas 51-63,
  140-171, 250-261). A `passagem-de-bastao` Parte 3 item 1 é o gate de fechamento
  (`guardrails-check` verde antes de `done`) e a Parte 2 monta o dossiê copiando o card
  (`.claude/skills/passagem-de-bastao/SKILL.md` linhas 69-72, 142-146).
- **F-15** — Diretiva do dono de 2026-09-19 (diário, *Diretiva de execução do P-0739*, item 2):
  o `scrum-master` roda em Opus durante o `P-0739`; exceção limitada àquele plano. Para este
  plano vale a tabela: orquestração em Sonnet.

---

## 3. Decisões (fechadas neste ato; o executor não as reabre)

| id | decisão | razão em uma linha |
|---|---|---|
| `DMC-1` | O modelo mora **dentro do plano**, na seção `## 1. Modelo conceitual`, imediatamente depois de `## 0. O problema, verbatim`; um por plano; nunca em arquivo separado | pedido do dono ("sempre estará no corpo desse plano"); objeto único (`M-3`) |
| `DMC-2` | Forma: linha `**Estado do modelo:**`, `### 1.1 Vocabulário` (tabela), `### 1.2 As orações do modelo` (bullets `- **M-<n>** — <texto>` + sub-bullet de metadados), `### 1.3 Mudanças do modelo` (tabela `MD-<n>`); gramática completa na §5 | legível por humano em ordem (vocabulário → orações → mudanças) e por máquina (`F-5`, `F-7`) |
| `DMC-3` | Texto da oração: português corrente, presente do indicativo, um comportamento observável por oração, **sem crase e sem barra** no texto; todo termo de papel ou artefato citado está no vocabulário; máximo de 40 orações por plano | é a interface do dono (`M-1`, `M-4`); a regra "sem crase/barra" é a única parte da linguagem corrente que um instrumento discrimina (`V8`) |
| `DMC-4` | Estados **gravados** de uma oração: `prevista`, `confirmada · <AAAA-MM-DD> · <ID da tarefa>`, `emendada · <AAAA-MM-DD> · <ref da decisão>`; estados **derivados** pelo instrumento na leitura do dono: `entregue`, `em curso`, `emendada`, `prevista` (regra de precedência na §6) | o dono vê quatro estados (`M-11`); o modelo grava só o que um papel afirmou; "em curso" é calculado do kanban, nunca escrito à mão |
| `DMC-5` | Quem escreve: **planejador** (cria; emenda em rodada de replanejamento), **consultor** (emenda em escalonamento), **revisor** (confirma; emenda só o inequívoco). **Executor** e **orquestrador** nunca escrevem. Um escritor por ato (`M-16`) | pedido do dono (revisor atualiza na entrega) + doutrina (executor não decide; orquestrador não revisa plano) |
| `DMC-6` | O revisor ganha a ferramenta `Edit`, com escrita **restrita à seção `## 1. Modelo conceitual` do plano da tarefa**; a fronteira em `docs/RUBRICA_DE_REVISAO.md` §7 passa a dizer isso | sem `Edit` a confirmação passaria pelo laudo, que é apagado no fechamento (`F-2`) — a informação se perderia ou exigiria um relé pelo orquestrador |
| `DMC-7` | Regra do inequívoco (`M-13`): o revisor emenda o texto de uma oração só quando (a) o veredito da tarefa é `aprovado` ou `ressalva` **e** (b) a divergência entre a oração e o que está no repositório é fato verificável no diff, não interpretação. Fora disso: achado de processo com alvo novo **`modelo`**, rota = consultor (plano em execução) ou planejador (rodada de replanejamento) | é a distinção que o dono descreveu no pedido; o alvo novo dá residência e rota ao caso ambíguo |
| `DMC-8` | `rdo.py laudo --achado-processo` aceita o quarto alvo `modelo`; `docs/RUBRICA_DE_REVISAO.md` §6 ganha a linha correspondente | `F-3`: alvo fora da lista é recusado pelo gerador — a rota de `DMC-7` não existe sem isso |
| `DMC-9` | Instrumento novo `.claude/tools/modelo.py`, verbos `check` e `show`; reutiliza `backlog._parse_plano` por importação de caminho (`F-6`); exit `0`/`1`/`2`; violações `V1`..`V9`; forma de saída fixa (§6) | `M-17`, `M-18`, `M-19`; padrão de carga e de fixtures já existente (`card_check`) |
| `DMC-10` | Gates: `modelo.py check` roda no `scrum-master` passo 3 (antes de materializar `in-progress`) e na `passagem-de-bastao` Parte 3 item 1 (antes de `done`); exit `1` bloqueia (`B3` no despacho; `blocked` no fechamento); exit `2` (plano sem modelo) segue com a nota "plano anterior à doutrina" | `M-17`, `M-19` |
| `DMC-11` | O relatório de encerramento do `scrum-master` e cada marco de validação **começam** pela saída de `modelo.py show --plano <plano> --desde <data de abertura da janela>`, colada integral — exceção declarada à regra "ponteiros e números, nunca conteúdo" | `M-9`: o modelo **é** o conteúdo que o dono lê; ponteiro para ele seria mais uma sigla |
| `DMC-12` | Card ganha o campo obrigatório `- **Oração do modelo:**` (ids em crase, sub-bullets com o texto de cada oração copiado); posição: logo depois de `Depende de` | `M-6`, `M-8`: o executor lê só o card |
| `DMC-13` | Esqueleto do planner renumerado: `## 0` pedido, `## 1` modelo, `## 2` fatos, `## 3` decisões, `## 4` invariantes, `## 5` tarefas, `## 6` ordem, `## 7` fora de escopo, `## 8` riscos, `## 9` achados; Fase 3 ganha o passo "escrever o modelo antes de decompor"; Fase 4 ganha a auditoria de rastreabilidade oração↔card; Fase 5 declara o Marco 1 | `M-5`, `M-7`; seções normativas extras (gramática, superfície) continuam permitidas entre decisões e tarefas, como no `P-0739` |
| `DMC-14` | Sem retroatividade: `P-0739` e anteriores não ganham modelo; `check` sai `2` para eles | `M-19`; retrofitar planos em curso é escopo de outro plano, se o dono quiser |
| `DMC-15` | Este plano é o piloto (`M-20`): seu `## 1` é confirmado/emendado pela execução, e o Marco 2 é o dono lendo `modelo.py show` sobre ele | é a única prova de que o mecanismo funciona sem o dono precisar imaginar |
| `DMC-16` | Ordem: norma (`MC-T1`) → instrumento (`MC-T2`) → papéis (`MC-T3`) → loop (`MC-T4`) → README e aferição (`MC-T5`) | "gramática nova não se aplica antes de o parser aprender" (`AE-5`/`AE-6` do `P-0739`); protocolo cita chamada de instrumento já medida |
| `DMC-17` | Residências: norma em `GOVERNANCA.md` §3.2 (nova); gramática na skill `diario-de-obras` (*Gramática legível por máquina*); alvo e fronteira em `docs/RUBRICA_DE_REVISAO.md` §6/§7; **como** em cada agente; procedimento nas skills `scrum-master` e `passagem-de-bastao`; explicação ao leitor externo no `README.md` §5 e §8. Nenhum guardrail `G-*` novo: o guarda é o instrumento | `G-SURFACE`: superfície inteira no mesmo plano; §7.1 desaconselha guardrail sem caso medido |
| `DMC-18` | Modelos das tarefas: `MC-T1`, `MC-T3`, `MC-T4` Sonnet · classe redacao (texto literal no card); `MC-T2` Sonnet · esforço high · classe implementacao; `MC-T5` Opus + dono · classe redacao | tabela de `GOVERNANCA.md` §3; a autoria intelectual já está nas §4-§6 deste plano |
| `DMC-19` | **(consultor, `ESC-1`, 2026-09-20 — tática)** O campo `- **Depende de:**` do card carrega **só ids de item** (tarefa ou tíquete), entre crases, sem prosa e sem faixa `..`; a proveniência (decisões `DMC-<n>`, fatos `F-<n>`, seções deste plano) migra para o campo novo `- **Fundamento:**`, posto **imediatamente antes** de `Depende de` e não lido por instrumento nenhum. Card sem tarefa anterior **omite** `Depende de` (o campo é opcional na gramática) e aí `Oração do modelo` (`DMC-12`) vem logo depois de `Fundamento`. Os cinco cards deste plano já estão nessa forma; a `MC-T3` publica a forma na *Anatomia do card* do `pantonic-planner.md` (passo 4) | `AE-1`: `backlog.py next` lê esse campo como lista de dependências e exigia `done` de `DMC-*`/`F-*`, que não são itens — as cinco tarefas ficavam inselecionáveis e a janela travava no gate. A gramática publicada (`diario-de-obras`, *Item e residência*) já dizia "só ids de item"; quem ensinava o desvio era o gabarito do planner (`AE-5`) |
| `DMC-20` | **(consultor, `ESC-2`, 2026-09-20 — tática)** O deadlock da confirmação se resolve na `V6`, não na ordem dos atos: oração `confirmada` exige **toda** tarefa citada em `done`, `cancelled` ou `review`, e **ao menos uma** em `done` ou `review`. `in-progress`, `ready`, `triage` e `blocked` continuam violação. Emendas no mesmo ato: a `V6` da §6 e da §5 deste plano, a linha correspondente na residência (skill `diario-de-obras`, pela `MC-T2` — quem codifica a regra também publica a gramática dela, `DMC-16`), e a oração `M-17` (`MD-1`) | `AE-11`. O revisor confirma **no mesmo ato do laudo** (`### 3.2`), e nesse instante a tarefa está `review` — estado que o próprio loop materializa antes de despachar o revisor (`scrum-master` passo 5, saída "status materializado (`review` ou `blocked`)", e passo 6, despacho do revisor; transições `("in-progress","review")` e `("review","done")` em `.claude/tools/backlog.py:1174-1176`), e `done` só existe **depois** do `close`, que é o que o gate guarda. O deadlock não é só das orações de tarefa única: vale para **toda** oração no ato da sua última tarefa. Descartadas: "confirmar depois do `close`" (o laudo é apagado no `close`, `F-2`, e o revisor não vive depois dele — a confirmação passaria pelo orquestrador, que a `### 3.2` proíbe de escrever) e um flag `--fechando <ID>` (deixaria o plano num estado que o `check` sem flag recusa entre a gravação e o `close`: janela que terminasse nesse intervalo bloquearia o despacho seguinte por não-defeito) |
| `DMC-21` | **(consultor, `ESC-2`, 2026-09-20 — tática)** Regime transitório de confirmação. O revisor só grava no modelo a partir da revisão em que as duas condições existem no disco: o instrumento (`MC-T2`) e o `Edit` mais o passo `5a` (`MC-T3`). Até lá a `### 3.2` é **inerte** para este plano. As confirmações vencidas no intervalo são gravadas em dois atos declarados: (i) **neste ato do `ESC-2`**, pelo consultor, as de `M-3` e `M-16` — as únicas cujo conjunto de tarefas é só a `MC-T1` —, com base no laudo já emitido (`MD-2`); (ii) as demais, pelo primeiro revisor que puder escrever, por instrução no campo `Nota ao revisor` das `MC-T3`, `MC-T4` e `MC-T5`: *confirme, além das orações do card, toda oração da §1.2 ainda `prevista` cujas tarefas estejam todas em `done`, `cancelled` ou `review`*. A cláusula é auto-sanável: se o revisor da `MC-T3` não tiver `Edit` (definição de agente carregada antes da edição), o da `MC-T4` recolhe o acumulado. O regime **expira** quando a `MC-T5` fechar | a `### 3.2` publicada pela `MC-T1` manda o revisor gravar, mas o `Edit` só chega na `MC-T3` e o instrumento só na `MC-T2` — é a inversão do `AE-5`/`AE-6` que a `DMC-16` queria evitar, e sem regra explícita as onze orações da `MC-T1` ficariam `prevista` até o Marco 2, esvaziando o piloto (`M-20`) |
| `DMC-22` | **(consultor, `ESC-2`, 2026-09-20 — tática)** A linha `Pronto quando` não se apoia em `git diff --stat`: o aceite de escopo passa a ser a atribuição medida por `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde HEAD --atribuir` — resumo com `0 sem atribuicao` **e** contagem de `-> alvo-do-card` igual ao número de arquivos-alvo do card. As duas expressões entram no bloco `Verificação` (residência de comando, `F-8`); `--desde HEAD` vale para o plano inteiro porque o `I-7` mantém `HEAD` parado. Vale para `MC-T2`, `MC-T3` e `MC-T4`; a `MC-T1` está `done` e **não** é retrofitada | `AE-10`: sob o `I-7` ninguém commita e a materialização de status do loop (diário, RDO, índice, telemetria, o próprio plano) vive na mesma árvore suja — `git diff --stat` nunca listará só os alvos. Medido em 2026-09-20: 9 arquivos tocados desde `HEAD`, **0 sem atribuição** |
| `DMC-23` | **(consultor, `ESC-2`, 2026-09-20 — tática)** As duas enumerações "três alvos possíveis", agora falsas, fecham no mesmo card que muda o parser correspondente: `docs/RUBRICA_DE_REVISAO.md` (§6, frase de abertura da tabela) na `MC-T2`, junto de `_ALVOS_ACHADO`; `.claude/agents/pantonic-reviewer.md` na `MC-T3`, que já é dona do arquivo. Nenhuma das duas vira tíquete | `DMC-16`: a frase e o parser mudam juntos. As duas são a mesma entrega da `MC-T1` deixada incompleta, não defeito de instrumento vizinho (`AE-2`) |
| `DMC-24` | **(consultor, `ESC-2`, 2026-09-20 — tática)** `V8` recusa dois caracteres nomeados por codepoint: **backtick** (U+0060) e **barra** (U+002F). Letra acentuada do português — inclusive `à` — **não** é violação. A linha da `V8` na §6 passa a nomear os codepoints; a prosa "sem crase e sem barra" da §4, da §5 e da `DMC-3` continua como está, porque no idioma do kit "crase" é o backtick (`DMC-12`: "ids em crase"; `DMC-19`: "entre crases") | medido em 2026-09-20: a oração `M-18` deste plano termina em "nunca redigida à mão". Lida "crase" como acento grave, `modelo.py check` sobre o corpus real (`I-6`) sairia `1` por `V8`, e a contingência 2 da `MC-T2` mandaria `blocked premissa` — o plano piloto reprovaria a si mesmo na primeira execução do instrumento |
| `DMC-25` | **(consultor, `ESC-3`, 2026-09-20 — tática)** Verificação deste plano obedece a três regras: (a) padrão recortado de **saída canalizada** de instrumento é **ASCII puro** — acento só via `Select-String -Path` sobre arquivo; (b) cabendo o fato num **exit code** ou num `-Path`, é essa a forma, não o pipe; (c) toda forma canalizada precisa ter, na série do plano, ao menos uma medição **não-zero** que prove o pipe vivo — `0` antes e `0` depois não é aceite, é linha morta. Varridas as verificações das três tarefas abertas, nenhuma repete o defeito: as quatro canalizadas (`MC-T3` 10 e 11, `MC-T4` 5 e 6) recortam literais ASCII de `review_evidence.py --atribuir`, que é ASCII por desenho | `AE-13` item 1: o padrão acentuado `plano anterior à doutrina` vindo por pipe de `python` nunca casou, porque o PowerShell decodifica o pipe em `ibm850` e a §6 exige stdout UTF-8 forçado. O pipe vivo está provado na mesma máquina e no mesmo dia: a verificação 8 da `MC-T2` mediu **2** e a 10 da `MC-T3` mediu **1** com a mesma forma |
| `DMC-26` | **(consultor, `ESC-3`, 2026-09-20 — tática)** O campo `linha` da dataclass `Oracao` **sai**; não ganha consumidor na `MC-T4`. A remoção é o card novo `MC-T2a`, que não toca mais nada de `modelo.py` | medido em 2026-09-20: `.claude/tools/modelo.py:61` declara `linha: int = 0`, `:150` o atribui, e nenhuma outra linha do módulo ou de `tests/test_modelo.py` o lê. Consumidor não existe porque a §6 congela a forma dos dois verbos: `show` é prosa para o dono (`DMC-11` — ponteiro seria "mais uma sigla") e `check` identifica o sujeito por `M-<n>`; a ordem das violações é a de varredura, não uma ordenação por posição. Dar consumidor seria inventar fato para justificar símbolo, que é o avesso do achado |
| `DMC-27` | **(consultor, `ESC-4`, 2026-09-20 — tática)** O contrato do estado `review` passa a estar dito nos **três** lugares que dependem dele, com a mesma frase: no passo `5a` do `pantonic-reviewer.md` (a tarefa que você julga está em `review`, e é por isso que a oração pode ser confirmada), no passo 6 do `scrum-master` (conferir a materialização **antes** de invocar o revisor) e na `V6`, que já o diz. Quem publica é a `MC-T4`, que ganha `.claude/agents/pantonic-reviewer.md` nos arquivos-alvo. Revisor que encontre `V6` citando a própria tarefa julgada **não force**: desfaz a gravação e registra achado de processo de alvo `doutrina` — é defeito de condução do loop, não do plano | `AE-15` item 2. A `DMC-20` decidiu certo e o instrumento a codificou certo; o que faltou foi **escrever a premissa** onde o revisor lê. Texto que descreve a tarefa revisada como "aberta" convida o revisor a não confirmar, ou a forçar, e a `MC-T4` herdaria o descasamento por ser dona do passo do `scrum-master`. O alvo `doutrina` é o único dos quatro que cobre procedimento em conflito (`docs/RUBRICA_DE_REVISAO.md` §6) |
| `DMC-28` | **(consultor, `ESC-4`, 2026-09-20 — tática)** A `MC-T5` **regenera** a região marcada do `README.md` com `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e fecha a janela com `check-drift` em exit `0`. A restrição "nenhuma outra seção do README muda" passa a excluir, explicitamente, as regiões entre `<!-- kit:agents:begin -->` e `<!-- kit:agents:end -->` e entre os marcadores de skills, que são **geradas** e não redigidas | `AE-15` item 1: a `MC-T3` trocou a `description` do consultor e virou a guarda; medido em 2026-09-20 que a `MC-T5`, como estava escrita, **não** a consertaria — ela só roda `check-readme.ps1`, que já sai exit `0` e não olha a coluna de descrição, e a própria restrição do card proibia mexer no resto do README. `-Mode generate` reescreve só as duas regiões marcadas (`.claude/checks/kit_check.ps1:266-285`), então a correção é cirúrgica |
| `DMC-29` | **(consultor, `ESC-4`, 2026-09-20 — tática)** A `AE-14` fecha por **remoção da cadeia**, não de mais duas linhas: card novo `MC-T2b`, cujo aceite é o **fechamento de consumidor** — nenhum símbolo de `modelo.py` fica sem leitor por causa da remoção do campo `linha` —, e não uma lista de posições. Entram nele o parâmetro `offset` de `_extrair_oracoes` e o argumento `inicio` no chamador, e o que mais a mesma cadeia tiver deixado; o card declara na volta o que removeu. Ordem: depois da `MC-T4`, antes da `MC-T5` | o defeito é meu: a `DMC-26` delimitou a deleção a duas posições medidas, e a `MC-T2a` fez exatamente o que o card mandou — o símbolo sem consumidor mudou de forma em vez de sumir. Card recortado por posição repete o erro na próxima casca; card recortado por propriedade, não. `dead_code.py` não alcança parâmetro de função, então o aceite tem de ser autoral e declarado |
| `DMC-30` | **(consultor, `ESC-5`, 2026-09-20 — tática)** O gate do modelo no passo 9 do `scrum-master` roda **antes** de materializar o status, e o desfecho de exit `1` é **a tarefa permanecer em `review`** — não `in-progress`. Não materializa, não fecha, escala ao consultor, o fechamento espera o reparo. Exit `0` ou `2`: materializa e fecha. O reparo mora no card novo `MC-T4a`, despachado **antes** da `MC-T2b` | `AE-16` item 1. Três fatos contra o texto vigente: (i) `review` é um dos três estados que a `V6` conta como fechados e é aquele em que o reviewer julgou a tarefa, então segurá-la ali não cria vermelho novo, enquanto `in-progress` **cria** — inclusive para orações confirmadas por outras tarefas que citem esta; (ii) a materialização é a **primeira** ação do passo 9, então no texto vigente a tarefa já está `done` quando o gate roda, e `done` → `in-progress` **não existe** em `_TRANSICOES` (`.claude/tools/backlog.py:1170-1178`): a instrução é inexecutável, `backlog.py status` a recusa; (iii) rodar o gate antes da materialização é o que torna o instante do `check` igual ao instante em que o reviewer gravou, que é a premissa da `DMC-27`. A ordem vai **antes** da `MC-T2b` porque a `MC-T2b` edita o próprio `modelo.py`: é o card com mais chance de produzir o exit `1` que dispara a rota defeituosa |
| `DMC-31` | **(consultor, `ESC-5`, 2026-09-20 — tática)** As duas frases que contam gates acompanham o terceiro: "Aprovados os **dois**" vira "os **três**" no passo 3, e a condição da linha `B3` do Bloco B passa a enumerar também o `modelo.py check` do passo 3. Mesmo card `MC-T4a`. A tabela de roteamento é tocada **só** nessa célula de condição | `AE-16` item 2: a `MC-T4` acrescentou o terceiro gate e o card proibiu tocar as tabelas de roteamento, então o executor não podia fechar — defeito de decomposição, não de entrega. Contagem de gates que não bate com o número de gates é a mesma classe da `AE-12`: texto que o leitor seguinte usa para decidir |

---

## 4. Norma do modelo conceitual (texto literal para `GOVERNANCA.md` `### 3.2`)

> Residência única **depois** da transcrição pela `MC-T1`: `GOVERNANCA.md` §3.2. Este plano não
> recopia o texto após a transcrição; o bloco abaixo é o insumo literal do card.

```markdown
### 3.2 O modelo conceitual do plano

**O que é.** Todo plano carrega, logo depois de `## 0. O problema, verbatim`, a seção
`## 1. Modelo conceitual`: um texto curto, em linguagem corrente, que diz o que o plano entrega e
como o resultado funciona. É formado por um **vocabulário** (cada papel e cada artefato que as
orações citam, com significado em uma linha), por **orações numeradas** `M-<n>` (cada uma um
comportamento observável do que está sendo construído) e por uma **lista de mudanças** `MD-<n>`.
É um objeto único: uma cópia, dentro do plano, do primeiro rascunho ao fechamento. A gramática
que o instrumento lê mora na skill `diario-de-obras` (*Gramática legível por máquina*, "Modelo
conceitual (seção do plano)").

**Para quem é.** O modelo é a interface entre o dono e o loop. Quem lê só o modelo entende o que
o plano faz, o que está pronto, o que está em andamento e o que mudou desde a última leitura. Por
isso o texto de uma oração não carrega crase, barra, caminho de arquivo, sigla nem identificador
técnico — o instrumento recusa crase e barra (`V8`); o resto é dever de autoria. Máximo de 40
orações por plano.

**Quem escreve, e quando** — um escritor por ato, sempre o papel que acabou de decidir ou de
confirmar algo:

| papel | ato sobre o modelo | quando |
|---|---|---|
| planejador | escreve o modelo **antes** de decompor em tarefas; cada oração é materializada por ≥ 1 card e cada card cita ≥ 1 oração no campo `Oração do modelo`, com o texto copiado | autoria do plano (Fase 3) e rodada de replanejamento (`RP-<n>`): emenda com `MD-<n>` citando a decisão |
| consultor | emenda o modelo quando a decisão do escalonamento muda o que o plano entrega ou como funciona; `MD-<n>` cita a decisão | escalonamento (`ESC-<n>`) |
| revisor | ao aprovar a última tarefa que materializa uma oração, grava `confirmada · <data> · <ID>` se o que foi entregue corresponde ao texto; emenda o texto **só** quando a divergência é inequívoca — veredito `aprovado`/`ressalva` **e** divergência verificável no diff; na dúvida, achado de processo com alvo `modelo` (`docs/RUBRICA_DE_REVISAO.md` §6) e o texto fica como está | revisão de cada tarefa, no mesmo ato do laudo |
| executor | **nunca** escreve; lê as orações no card | — |
| orquestrador | **nunca** escreve; roda `modelo.py check` antes de despachar e antes de fechar cada tarefa (exit `1` bloqueia; exit `2` = plano anterior a esta regra, segue com nota) e abre o relatório de encerramento e cada marco com `modelo.py show` | passos 3 e 9 do `scrum-master`; Parte 3 da `passagem-de-bastao` |
| dono | lê o modelo no Marco 1 de todo plano (`go`/`no-go` antes de qualquer tarefa) e a leitura gerada pelo instrumento em cada marco e relatório | marcos de validação (§4.5) |

**Estados.** Gravados: `prevista`, `confirmada · <AAAA-MM-DD> · <ID>`, `emendada · <AAAA-MM-DD> ·
<ref>`. Derivados por `modelo.py show`, nesta precedência: `entregue` (gravada `confirmada`);
`em curso` (alguma tarefa citada em `in-progress` ou `review`); `emendada` (gravada `emendada`);
`prevista`. O instrumento é a única fonte da leitura do dono — ninguém redige a leitura à mão.

**Retroatividade.** Planos criados antes desta seção não ganham modelo; `modelo.py check` sai `2`
para eles e o loop segue. Caso medido de origem: pedido do dono de 2026-09-19, plano `P-0741`.
```

**Emendas a `docs/RUBRICA_DE_REVISAO.md` (texto literal para a `MC-T1`):**

Linha nova na tabela de alvos da §6, depois da linha `rubrica`:

```markdown
| `modelo` | oração do modelo conceitual do plano que a entrega tornou falsa ou ambígua sem que a mudança seja inequívoca (`GOVERNANCA.md` §3.2); rota: emenda pelo consultor (plano em execução) ou pelo planejador (rodada de replanejamento) — nunca pelo revisor |
```

Parágrafo da §7, substituição integral (o texto vigente está em `F-2`):

```markdown
O reviewer marca dimensões, anexa achados e emite o laudo pelo gerador. O reviewer não corrige o que
aponta, não replaneja, não edita os arquivos da tarefa e não escreve percentual nem veredito. A
correção do que o laudo aponta pertence a uma execução seguinte, com o laudo em mãos. **Uma
escrita, e só uma, é do reviewer:** a seção do modelo conceitual do plano da tarefa
(`GOVERNANCA.md` §3.2) — confirmar oração materializada e emendar o inequívoco, no mesmo ato do
laudo; qualquer outra linha do plano continua fora do seu alcance.
```

---

## 5. Gramática do modelo (texto literal para a skill `diario-de-obras`)

> Residência única **depois** da transcrição pela `MC-T1`: `.claude/skills/diario-de-obras/SKILL.md`,
> subseção nova de *Gramática legível por máquina*, inserida depois de `### Inbox de planos`. É a
> gramática que `.claude/tools/modelo.py` lê (§6).
>
> **Emenda do `ESC-2` (2026-09-20, `DMC-20`):** a célula de regra da linha *orações* mudou — a
> `V6` passou a aceitar `review`. O bloco abaixo já está na forma nova; a residência ainda está na
> forma antiga, e quem a transcreve é a `MC-T2` (passo 7b), no mesmo ato em que codifica a regra.
> Até esse passo rodar, a residência e este bloco divergem numa célula, e é ele que vale.

```markdown
### Modelo conceitual (seção do plano)

Seção `## 1. Modelo conceitual` do plano (`GOVERNANCA.md` §3.2), delimitada pelo próximo heading
de nível 2. Dentro dela, nesta ordem:

| elemento | forma | regra |
|---|---|---|
| cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> orações · última mudança: <MD-<n> \| nenhuma>` | linha única; obrigatória (`V9`) |
| vocabulário | `### 1.1 Vocabulário` + tabela `\| termo \| o que significa aqui \|` | obrigatório; conteúdo livre |
| orações | `### 1.2 As orações do modelo`; cada oração é o par de linhas: `- **M-<n>** — <texto>` e, na linha seguinte, `  - \`estado: <estado>\` · \`tarefas: <ID>[, <ID>]\`` | `<n>` único (`V7`); `<texto>` sem crase e sem `/` (`V8`); `<estado>` ∈ `prevista` \| `confirmada · AAAA-MM-DD · <ID>` \| `emendada · AAAA-MM-DD · <ref>` (`V5`); toda `<ID>` existe como `### <ID> — …` no plano (`V3`); lista de tarefas não vazia (`V1`); `confirmada` exige toda `<ID>` citada em `done`, `cancelled` ou `review`, com ao menos uma em `done` ou `review` (`V6`) — `review` é o estado da tarefa no ato do laudo, que é quando o revisor confirma. Subtítulos `**A. …**` entre orações são livres e ignorados |
| mudanças | `### 1.3 Mudanças do modelo` + tabela `\| id \| data \| autor \| orações \| o que mudou e por quê \|`; linha `\| MD-<n> \| AAAA-MM-DD \| <papel> · <ref> \| M-<a>, M-<b> \| <texto> \|`; sem mudança, uma linha com `—` nas quatro primeiras células | obrigatória (`V9`) |
| campo do card | `- **Oração do modelo:** \`M-<a>\`[, \`M-<b>\`]` como campo de todo `### <ID> — …` do plano, seguido de um sub-bullet `  - M-<a>: <texto copiado>` por oração | obrigatório em toda tarefa do plano (`V2`); toda `M-<a>` citada existe (`V4`) |

Plano sem a seção `## 1. Modelo conceitual` é **plano anterior à doutrina**: `modelo.py check`
sai `2` e nada se exige dele.
```

---

## 6. Superfície do instrumento `modelo.py` (normativa; a `MC-T2` a implementa)

**Chamadas:**

```
python .claude/tools/modelo.py check --plano <caminho do plano> [--root <raiz do repo>]
python .claude/tools/modelo.py show  --plano <caminho do plano> [--desde AAAA-MM-DD] [--root <raiz do repo>]
```

`--root` default: `Path(__file__).resolve().parent.parent.parent` (mesmo de `card_check.py`).
Ambos os verbos carregam `backlog.py` por `importlib.util.spec_from_file_location` e chamam
`backlog._parse_plano(Path(plano), Path(root))` para obter `Plano.tarefas` (`F-6`); nada de
`backlog.py` é reescrito. Saída em UTF-8 forçado (`_forcar_utf8`, duplicado como em `card_check`).

**Exit codes e forma de saída de `check`:**

| condição | exit | stdout / stderr |
|---|---|---|
| seção `## 1. Modelo conceitual` ausente | `2` | stdout: `modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')` |
| seção presente, zero violações | `0` | stdout: `modelo: OK — <k> orações, <t> tarefas, <m> mudanças` |
| seção presente, ≥ 1 violação | `1` | stderr: `modelo: FALHOU — <n> violação(ões)` e, uma por linha, `V<k> <sujeito> — <texto>` (sujeito = `M-<n>`, `<ID>` ou `secao`) |

**Vocabulário fechado de violações (cada uma com a substring literal que a linha imprime e o TF que a afirma):**

| código | condição | substring literal | TF |
|---|---|---|---|
| `V1` | oração com lista `tarefas:` vazia ou ausente | `V1 M-<n> — oração sem tarefa` | `TF-MC-2` |
| `V2` | tarefa do plano sem campo `Oração do modelo` ou com lista vazia | `V2 <ID> — tarefa sem oração` | `TF-MC-2` |
| `V3` | oração cita `<ID>` que não é heading de tarefa do plano | `V3 M-<n> — tarefa inexistente <ID>` | `TF-MC-2` |
| `V4` | card cita `M-<n>` que não existe na §1.2 | `V4 <ID> — oração inexistente M-<n>` | `TF-MC-2` |
| `V5` | `estado:` fora da gramática (token, data ou ref malformados) | `V5 M-<n> — estado inválido '<literal>'` | `TF-MC-2` |
| `V6` | oração `confirmada` com tarefa citada fora de `done`, `cancelled` e `review`, ou sem nenhuma em `done` ou `review` (`DMC-20`) | `V6 M-<n> — confirmada com tarefa aberta <ID>` | `TF-MC-2` |
| `V7` | `M-<n>` repetido | `V7 M-<n> — identificador duplicado` | `TF-MC-2` |
| `V8` | texto da oração contém **backtick** (U+0060) ou **barra** (U+002F) — e só esses dois caracteres; letra acentuada do português, inclusive `à`, não é violação (`DMC-24`) | `V8 M-<n> — literal técnico no texto` | `TF-MC-2` |
| `V9` | cabeçalho `**Estado do modelo:**` ausente, ou `### 1.3 Mudanças do modelo` ausente | `V9 secao — cabeçalho ou lista de mudanças ausente` | `TF-MC-3` |

Fronteira contra o instrumento vizinho: `backlog.py check` julga cabeçalho e status das
**tarefas**; `modelo.py check` julga só a seção do modelo e o campo `Oração do modelo` dos cards.
Nenhum dos dois repete a checagem do outro. Forma fora da gramática que não está na tabela acima
não bloqueia: é `V5` (estado) ou é ignorada (subtítulo, prosa entre orações).

**Forma de saída de `show` (fixa; `--desde` ausente = todas as mudanças):**

```
# Modelo conceitual — <P-NNNN> — <título do plano>
Estado do modelo: versão <n> · <data> · <k> orações: <a> entregues · <b> em curso · <c> emendadas · <d> previstas

## Vocabulário
<tabela da §1.1, copiada verbatim>

## Orações
[entregue]  M-1 — <texto>  (confirmada AAAA-MM-DD por <ID>)
[em curso]  M-2 — <texto>  (<ID> in-progress)
[emendada]  M-3 — <texto>  (emendada AAAA-MM-DD por <ref>)
[prevista]  M-4 — <texto>

## Mudanças desde <AAAA-MM-DD | o início>
<linhas da tabela da §1.3 com data ≥ --desde, verbatim; sem nenhuma: `nenhuma`>
```

Regra de derivação do estado (precedência, `DMC-4`): gravada `confirmada` → `entregue`; senão,
alguma tarefa citada com `status` ∈ {`in-progress`, `review`} → `em curso`, com a primeira dessas
tarefas e o status dela entre parênteses; senão gravada `emendada` → `emendada`; senão
`prevista`. Os quatro casos são os que as regras admitem, e a fixture `tests/fixtures/modelo/
plano-valido.md` instancia os quatro (`TF-MC-4`). Subtítulos `**A. …**` da §1.2 são reproduzidos
como linhas em branco seguidas do subtítulo, para preservar a leitura por blocos.

---

## 7. Invariantes de execução

Valem para todas as tarefas; cada card repete a parte que o vincula.

- **I-1** — Regra de dependência `infracore ← contracts ← services ← plugins` não é tocada:
  todas as tarefas vivem em `.claude/`, `docs/`, `tests/` e `README.md`.
- **I-2** — Piso de regressão é relação (`DM-23`): a suíte inteira (`python -m pytest tests -q`)
  não reduz o total re-medido no despacho e soma os testes novos do card. Referência datada:
  201 coletados em 2026-09-19 (`F-11`).
- **I-3** — Nenhum card edita `.claude/tools/backlog.py`, `.claude/tools/review_evidence.py` ou
  `.claude/tools/card_check.py`. `rdo.py` é editado só pela `MC-T2`, só em `_ALVOS_ACHADO` e no
  texto de ajuda que enumera os alvos.
- **I-4** — Texto normativo entra **verbatim** dos blocos cercados deste plano (§4, §5, §6, e os
  blocos "Texto novo, literal" dos cards). O executor não parafraseia norma.
- **I-5** — Contingência acionada é devolvida na linha de retorno como `contingência <n>
  acionada: <o que mudou>`; a orquestração a materializa na linha `**Status:**` do card.
- **I-6** — Todo card deste plano carrega `Oração do modelo` (`DMC-12`), e é esse campo que a
  `MC-T2` usa como primeiro corpus real de `check`.
- **I-7** — Nenhuma tarefa commita: commit no Marco 2, por ato do loop (diretiva do dono de
  2026-09-18, item 3).

---

## 8. Tarefas

### MC-T1 — A norma e a gramática do modelo publicadas nas residências únicas [Sonnet · classe redacao]
- **Status:** `done` · 2026-09-20
- **Objetivo:** `GOVERNANCA.md` ganha a `### 3.2`, a rubrica ganha o alvo `modelo` e a fronteira
  nova, e a skill `diario-de-obras` ganha a gramática do modelo — os três com o texto literal
  das §4 e §5 deste plano.
- **Fundamento:** decisões `DMC-1`, `DMC-2`, `DMC-3`, `DMC-4`, `DMC-5`, `DMC-6`, `DMC-7`, `DMC-8`, `DMC-17`; fatos `F-2`, `F-3`, `F-9`. Nenhuma tarefa anterior — por isso o campo `Depende de` está ausente (`DMC-19`).
- **Oração do modelo:** `M-1`, `M-2`, `M-3`, `M-4`, `M-6`, `M-7`, `M-11`, `M-12`, `M-13`, `M-15`, `M-16`
  - M-1: Todo plano carrega, logo depois do pedido do dono, uma seção chamada "Modelo conceitual": um texto curto, em linguagem corrente, que diz o que o plano entrega e como o resultado funciona, sem siglas, sem nomes de arquivo e sem identificadores técnicos no corpo das frases.
  - M-2: O modelo é formado por orações numeradas, cada uma afirmando um comportamento observável do que está sendo construído, e por um vocabulário que define cada papel e cada artefato que as orações citam.
  - M-3: O modelo é um objeto único: existe uma cópia só, dentro do plano, e ela acompanha o plano do primeiro rascunho ao fechamento; não há versão paralela em outro arquivo.
  - M-4: O modelo é a interface entre o dono e o loop: quem lê só o modelo entende o que o plano faz, o que já está pronto, o que está em andamento e o que mudou desde a última leitura.
  - M-6: Cada oração é materializada por pelo menos uma tarefa, e cada tarefa materializa pelo menos uma oração; o card da tarefa cita as orações que materializa e copia o texto delas.
  - M-7: O dono lê o modelo e dá o "go" ou o "no-go" antes de qualquer tarefa ser executada: essa leitura é o primeiro marco de todo plano.
  - M-11: Toda oração tem um estado que o dono vê: prevista, em curso, entregue ou emendada.
  - M-12: Ao aprovar a última tarefa que materializa uma oração, o revisor confirma a oração no modelo, registrando a data e a tarefa, se o que foi entregue corresponde ao que a oração afirma.
  - M-13: O revisor só altera o texto de uma oração quando a entrega tornou a mudança inequívoca e consolidada; na dúvida, registra um achado com alvo "modelo", e a mudança fica para quem replaneja.
  - M-15: Toda mudança no modelo fica registrada numa lista de mudanças dentro da própria seção, com data, autor, orações afetadas e o que mudou.
  - M-16: O modelo tem um escritor por ato: quem o altera é sempre o papel que acabou de decidir ou de confirmar algo, no mesmo ato.
- **Camada e fronteira:** documentação de governança do hub; nenhum código. Não toca
  `.claude/agents/`, `.claude/skills/scrum-master/`, `.claude/skills/passagem-de-bastao/` nem
  `.claude/tools/`.
- **Arquivos-alvo:**
  - `GOVERNANCA.md` §3.1 (inserir a `### 3.2` **depois** do fim da `### 3.1 Residência e precedência da doutrina` e **antes** de `## 4. Fluxo de desenvolvimento`)
  - `docs/RUBRICA_DE_REVISAO.md` §6 (tabela de alvos) e §7 (parágrafo único)
  - `.claude/skills/diario-de-obras/SKILL.md` (depois de `### Inbox de planos`, antes de `### Máquina de transições (forma para o instrumento)`)
- **Contratos/classes:** nenhum.
- **Passos:**
  1. Em `GOVERNANCA.md`, localizar a linha `## 4. Fluxo de desenvolvimento`; inserir imediatamente
     antes dela o bloco cercado da §4 deste plano (o conteúdo, sem as três crases de abertura e
     fechamento), seguido de uma linha em branco.
  2. Em `docs/RUBRICA_DE_REVISAO.md` §6, localizar a linha da tabela que começa com
     `| \`rubrica\` |`; inserir imediatamente depois dela a linha `| \`modelo\` | … |` da §4
     ("Emendas a docs/RUBRICA_DE_REVISAO.md").
  3. Em `docs/RUBRICA_DE_REVISAO.md` §7, substituir o parágrafo inteiro que começa com `O reviewer
     marca dimensões, anexa achados` pelo parágrafo literal da §4.
  4. Em `.claude/skills/diario-de-obras/SKILL.md`, localizar a linha `### Máquina de transições
     (forma para o instrumento)`; inserir imediatamente antes dela o bloco cercado da §5 (o
     conteúdo, sem as crases de abertura e fechamento), seguido de uma linha em branco.
  5. Em `.claude/skills/diario-de-obras/SKILL.md`, no parágrafo de abertura de `## Gramática
     legível por máquina` (começa com `Transcrição normativa de`), acrescentar ao final a frase:
     `A subseção "Modelo conceitual (seção do plano)" transcreve
     \`docs/plans/P-0741-modelo-conceitual.md\` §5 e é lida por \`.claude/tools/modelo.py\`.`
- **Restrições desta tarefa:** texto verbatim dos blocos (`I-4`); nenhuma outra linha dos três
  arquivos muda; o nome do arquivo do plano citado no passo 5 é `docs/plans/P-0741-modelo-conceitual.md`.
- **Não fazer:** não renumerar seções existentes de `GOVERNANCA.md`; não tocar a linha
  *Revisão* da matriz §3 (fica para a `MC-T3`, junto com o agente); não editar `DOC_MAP.md`
  (`GOVERNANCA.md` já está acima de 500 linhas e sem entrada — o mapa diz que ele dispensa
  entrada; manter).
- **Contingências:**
  1. se `## 4. Fluxo de desenvolvimento` não ocorrer exatamente uma vez em `GOVERNANCA.md` →
     parar e sinalizar `blocked` razão `premissa`.
  2. se a linha `| \`rubrica\` |` não ocorrer exatamente uma vez em `docs/RUBRICA_DE_REVISAO.md` →
     parar e sinalizar `blocked` razão `premissa`.
  3. se `### Máquina de transições (forma para o instrumento)` não ocorrer exatamente uma vez na
     skill → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum executável; aceite por inspeção mecânica (abaixo).
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern '### 3.2 O modelo conceitual do plano' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'seção do modelo conceitual' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'que a entrega tornou falsa ou ambígua' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -Pattern '### Modelo conceitual (seção do plano)' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern '## 4. Fluxo de desenvolvimento' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 1**. (invariância: a seção seguinte continua única.)
- **Pronto quando:** as cinco linhas acima devolvem o esperado e `git diff --stat` lista
  exatamente os três arquivos-alvo.
- **Fora do escopo desta tarefa:** matriz §3 linhas *Planejamento*/*Revisão*/*Orquestração*
  (`MC-T3`); README (`MC-T5`).

### MC-T2 — `modelo.py`: `check` e `show`, e o alvo `modelo` no gerador de laudo [Sonnet · esforço high · classe implementacao]
- **Status:** `done` · 2026-09-20
- **Fundamento:** a gramática publicada pela `MC-T1`; decisões `DMC-4`, `DMC-8`, `DMC-9`, e do `ESC-2` as `DMC-20` (a `V6` aceita `review`, e este card a codifica e publica a gramática dela), `DMC-22` (o aceite de escopo é a atribuição medida), `DMC-23` (a frase da rubrica) e `DMC-24` (a `V8` recusa backtick e barra, não acento); fatos `F-5`, `F-6`, `F-7`, `F-8`, `F-10`, `F-11`; §5 e §6 deste plano.
- **Depende de:** `MC-T1`
- **Objetivo:** existe `.claude/tools/modelo.py` com os verbos `check` e `show` na superfície
  exata da §6, com testes funcionais sobre fixtures sintéticas, e `rdo.py laudo` aceita
  `--achado-processo modelo "<linha>"`.
- **Oração do modelo:** `M-6`, `M-10`, `M-11`, `M-13`, `M-15`, `M-17`, `M-18`, `M-19`
  - M-6: Cada oração é materializada por pelo menos uma tarefa, e cada tarefa materializa pelo menos uma oração; o card da tarefa cita as orações que materializa e copia o texto delas.
  - M-10: O dono se inteira de qualquer plano em andamento pedindo a leitura do modelo, sem abrir tarefas, achados ou laudos.
  - M-11: Toda oração tem um estado que o dono vê: prevista, em curso, entregue ou emendada.
  - M-13: O revisor só altera o texto de uma oração quando a mudança é inequívoca; na dúvida, registra um achado com alvo "modelo".
  - M-15: Toda mudança no modelo fica registrada numa lista de mudanças dentro da própria seção.
  - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico.
  - M-18: O mesmo instrumento gera a leitura do dono, com estados e mudanças, para que a leitura seja sempre derivada do modelo real.
  - M-19: Planos anteriores a esta regra não ganham modelo retroativamente; o instrumento os reconhece como anteriores e não os bloqueia.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`, Python 3 padrão, sem
  dependência externa; importa `backlog.py` por caminho (`F-6`) e **não** o edita (`I-3`).
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py` (novo)
  - `.claude/tools/rdo.py` (`_ALVOS_ACHADO` e a docstring/ajuda que enumera `dossiê`, `doutrina`, `rubrica`)
  - `docs/RUBRICA_DE_REVISAO.md` — só a frase de abertura da tabela de alvos da §6 (`DMC-23`)
  - `.claude/skills/diario-de-obras/SKILL.md` — só a célula de regra da linha *orações* da subseção do modelo (`DMC-20`)
  - `tests/test_modelo.py` (novo)
  - `tests/test_rdo.py` (um TF novo ao final)
  - `tests/fixtures/modelo/plano-valido.md` (novo)
  - `tests/fixtures/modelo/plano-invalido.md` (novo)
  - `tests/fixtures/modelo/plano-sem-cabecalho.md` (novo)
  - `tests/fixtures/modelo/plano-sem-modelo.md` (novo)
- **Contratos/classes:**
  - `def main(argv: list[str] | None = None) -> int` em `modelo.py`, com `argparse` e
    subcomandos `check` e `show`; `check` devolve `0|1|2`; `show` devolve `0`, ou `2` se a
    seção não existir (mesma mensagem do `check`).
  - `def extrair_modelo(linhas: list[str]) -> Modelo | None` — `None` quando não há
    `## 1. Modelo conceitual`; `Modelo` é `dataclass` com `cabecalho: str | None`,
    `vocabulario: list[str]` (linhas da tabela, verbatim), `oracoes: list[Oracao]`,
    `mudancas: list[str]` (linhas da tabela, verbatim), `subtitulos: dict[int, str]`
    (posição da oração → subtítulo `**A. …**` que a precede).
  - `Oracao` é `dataclass` com `id: str`, `texto: str`, `estado: str`, `estado_data: str |
    None`, `estado_ref: str | None`, `tarefas: list[str]`, `linha: int`.
  - `def validar(modelo: Modelo, plano) -> list[str]` — devolve as linhas `V<k> …` na ordem
    em que ocorrem no arquivo; `plano` é o `backlog.Plano` (`F-6`).
  - `def derivar_estado(oracao: Oracao, status_por_id: dict[str, str | None]) -> tuple[str,
    str]` — devolve `(rótulo, sufixo entre parênteses)` pela precedência da §6.
  - `def campo_oracoes(item_texto: str) -> list[str] | None` — ids `M-<n>` do campo
    `- **Oração do modelo:**` do card; `None` se o campo não existe.
- **Passos:**
  1. Criar `tests/fixtures/modelo/plano-valido.md`: cabeçalho `# EX-0001 — Plano de exemplo`,
     linhas 2-3 com `**Status:** \`in-progress\`` e `**Prefixo das tarefas no diário:**
     \`EX-T<n>\``; `## 0. O problema, verbatim` (uma linha); `## 1. Modelo conceitual` com
     cabeçalho `**Estado do modelo:** versão 2 · 2026-09-20 · autor: revisor · 4 orações ·
     última mudança: MD-1`, `### 1.1 Vocabulário` (tabela com duas linhas), `### 1.2 As orações
     do modelo` com o subtítulo `**A. Bloco**` e quatro orações: `M-1` `confirmada · 2026-09-20 ·
     EX-T1` tarefas `EX-T1`; `M-2` `prevista` tarefas `EX-T2`; `M-3` `emendada · 2026-09-20 ·
     ESC-1` tarefas `EX-T3`; `M-4` `prevista` tarefas `EX-T3`; `### 1.3 Mudanças do modelo`
     com uma linha `| MD-1 | 2026-09-20 | consultor · ESC-1 | M-3 | texto trocado por decisão |`;
     `## 4. Tarefas` com três cards `### EX-T1 — Um [Sonnet · classe mecanica]` (`- **Status:**
     \`done\` · 2026-09-20`), `### EX-T2 — Dois [Sonnet · classe mecanica]` (`in-progress`),
     `### EX-T3 — Três [Sonnet · classe mecanica]` (`ready`), cada um com
     `- **Oração do modelo:**` citando, respectivamente, `M-1`; `M-2`; `M-3`, `M-4`, e o
     sub-bullet de texto. Resultado esperado de `show`: `M-1` `[entregue]`, `M-2` `[em curso]`
     (`EX-T2 in-progress`), `M-3` `[emendada]`, `M-4` `[prevista]`.
  2. Criar `tests/fixtures/modelo/plano-invalido.md` com a mesma moldura e violações, uma por
     oração/card, nesta ordem de ocorrência: `M-1` sem `tarefas:` (`V1`); `M-2` citando `EX-T9`
     (`V3`); `M-3` com `estado: pronta` (`V5`); `M-4` `confirmada · 2026-09-20 · EX-T2` citando
     `EX-T2` que está `in-progress` (`V6`); `M-4` repetida (`V7`); `M-5` com texto `usa o
     arquivo docs/x.md` (`V8`); card `EX-T1` sem `Oração do modelo` (`V2`); card `EX-T2` citando
     `M-9` (`V4`). Esperado de `check`: exit `1`, stderr com **oito** linhas `V<k>` nesta ordem
     `V1, V3, V5, V6, V7, V8, V2, V4` e a linha `modelo: FALHOU — 8 violação(ões)`.
  3. Criar `tests/fixtures/modelo/plano-sem-cabecalho.md`: igual ao válido, sem a linha
     `**Estado do modelo:**` e sem `### 1.3 Mudanças do modelo`. Esperado: exit `1`, uma linha
     `V9 secao — cabeçalho ou lista de mudanças ausente`.
  4. Criar `tests/fixtures/modelo/plano-sem-modelo.md`: moldura sem `## 1. Modelo conceitual`.
     Esperado de `check` e de `show`: exit `2`, stdout `modelo: ausente — plano anterior à
     doutrina (sem '## 1. Modelo conceitual')`.
  5. Escrever `tests/test_modelo.py` (padrão de carga de `tests/test_card_check.py:1-25`), com:
     `TF-MC-1` `test_tf_check_valido_sai_zero` (exit 0, stdout `modelo: OK — 4 orações, 3
     tarefas, 1 mudanças`); `TF-MC-2` `test_tf_check_invalido_lista_oito_violacoes_na_ordem`
     (exit 1; as oito substrings literais da §6, na ordem; `V6` cita `EX-T2`); `TF-MC-3`
     `test_tf_check_sem_cabecalho_v9` (exit 1; substring `V9 secao`); `TF-MC-4`
     `test_tf_show_quatro_estados_derivados` (exit 0; as quatro linhas `[entregue]  M-1`,
     `[em curso]  M-2`, `[emendada]  M-3`, `[prevista]  M-4` presentes, e o sufixo
     `(EX-T2 in-progress)` na de `M-2`); `TF-MC-5` `test_tf_show_desde_filtra_mudancas`
     (`--desde 2026-09-21` → seção `## Mudanças desde 2026-09-21` com `nenhuma`; sem `--desde`
     → a linha `| MD-1 |` presente); `TF-MC-6` `test_tf_sem_modelo_sai_dois_nos_dois_verbos`
     (exit 2 em `check` e em `show`, stdout com `plano anterior à doutrina`). Poder
     discriminante de `TF-MC-2`: regra concorrente "qualquer status ≠ done" marcaria `V6` também
     para tarefa `cancelled` e para tarefa `review` — a fixture não tem nenhum dos dois, e por
     isso `TF-MC-2` inclui uma oração extra `M-6` `confirmada · 2026-09-20 · EX-T1` citando
     `EX-T1` (`done`), `EX-T4` (card `cancelled`) e `EX-T5` (card `review`), acrescentados à
     fixture inválida, que **não** deve gerar `V6` (`DMC-20`); os cards `EX-T4` e `EX-T5` levam
     `- **Oração do modelo:** \`M-6\`` com o sub-bullet de texto, senão disparam `V2` e a
     contagem muda. A contagem esperada continua **oito**.
  6. Implementar `.claude/tools/modelo.py`: docstring de módulo citando este card
     (`docs/plans/P-0741-modelo-conceitual.md` `### MC-T2`) e a gramática (skill
     `diario-de-obras`, "Modelo conceitual (seção do plano)"); `_load_backlog(root)` por
     `spec_from_file_location`; `extrair_modelo`, `campo_oracoes`, `validar`, `derivar_estado`,
     `verbo_check`, `verbo_show`, `main`. Recorte da seção: da linha `## 1. Modelo conceitual`
     até a próxima linha que casa `^## `. Regex das orações: `^- \*\*(M-\d+)\*\* — (.+)$` e, na
     linha seguinte, `^  - \`estado: ([^\`]+)\` · \`tarefas: ([^\`]*)\`$`; estado por
     `^(prevista)$|^(confirmada|emendada) · (\d{4}-\d{2}-\d{2}) · (\S+)$`. Campo do card por
     `^- \*\*Oração do modelo:\*\* (.+)$` sobre `Item.texto`, ids por `` `(M-\d+)` ``.
  7. Em `rdo.py`: acrescentar `"modelo"` a `_ALVOS_ACHADO` e a palavra `modelo` à enumeração
     dos alvos na ajuda/docstring (`F-3`, linhas 33-36 e 506-538). Acrescentar ao final de
     `tests/test_rdo.py` o `TF-MC-7` `test_tf_laudo_aceita_alvo_modelo`: chamada de `laudo` com
     `--achado-processo modelo "oração M-3 divergente"` sai `0` e o laudo contém a linha de
     tabela `| modelo | oração M-3 divergente |` (use os mesmos argumentos mínimos que o TF
     vizinho de `--achado-processo` já usa em `tests/test_rdo.py`, trocando só o alvo).
  7a. Em `docs/RUBRICA_DE_REVISAO.md` §6, substituir o literal `com três alvos possíveis:` por
     `com quatro alvos possíveis:` (`DMC-23`; uma ocorrência, contada pelo consultor em
     2026-09-20: **1**). Nenhuma outra linha do arquivo muda.
  7b. Em `.claude/skills/diario-de-obras/SKILL.md`, subseção `### Modelo conceitual (seção do
     plano)`, linha da tabela que começa com `| orações |`, substituir o literal
     `` `confirmada` exige toda `<ID>` citada em `done` ou `cancelled`, com ≥ 1 `done` (`V6`). ``
     por
     `` `confirmada` exige toda `<ID>` citada em `done`, `cancelled` ou `review`, com ao menos uma em `done` ou `review` (`V6`) — `review` é o estado da tarefa no ato do laudo, que é quando o revisor confirma. ``
     (`DMC-20`; é a transcrição da célula já emendada na §5 deste plano — `I-4`, texto verbatim;
     uma ocorrência, contada pelo consultor em 2026-09-20: **1**). Nenhuma outra linha da skill
     muda.
  8. Rodar a suíte inteira e `python .claude/tools/modelo.py check --plano
     docs/plans/P-0741-modelo-conceitual.md` (o corpus real, `I-6`).
- **Restrições desta tarefa:** `backlog.py`, `review_evidence.py` e `card_check.py` intocados
  (`I-3`); nenhum caminho de plano vivo em teste (`DM-38` (ii)); UTF-8 forçado na saída;
  `subprocess` não é usado (o instrumento só lê arquivos); em `docs/RUBRICA_DE_REVISAO.md` e em
  `.claude/skills/diario-de-obras/SKILL.md` muda **uma linha em cada**, a dos passos 7a e 7b, e
  nenhuma outra.
- **Não fazer:** não acrescentar verbo de escrita (`marcar`, `emendar`) — a escrita é por `Edit`
  dos papéis (`DMC-5`); não validar o conteúdo do vocabulário; não checar siglas no texto (só
  crase e barra, `V8`).
- **Contingências:**
  1. se `backlog._parse_plano` levantar exceção sobre uma fixture → a fixture está fora da
     gramática de item da skill `diario-de-obras`; corrigir **a fixture** (cabeçalho `#`,
     `**Status:**`, `**Prefixo…**`, headings `### EX-T<n> — … [Sonnet · classe mecanica]`) e
     registrar `contingência 1 acionada: fixture ajustada à gramática de item`.
  2. se `check` sobre `docs/plans/P-0741-modelo-conceitual.md` sair `1` → não editar o plano;
     parar e sinalizar `blocked` razão `premissa` com o stderr integral na razão.
  3. se `tests/test_rdo.py` não tiver TF de `--achado-processo` para copiar os argumentos →
     usar `python .claude/tools/rdo.py laudo --help` e montar a chamada mínima com todas as
     dimensões `conforme`; registrar `contingência 3 acionada: chamada montada pelo --help`.
  4. se o literal do passo 7a ou o do passo 7b não ocorrer exatamente uma vez no arquivo →
     parar e sinalizar `blocked` razão `premissa`, nomeando o passo (as duas âncoras foram
     contadas pelo consultor em 2026-09-20: uma ocorrência cada).
- **Testes:** `TF-MC-1`..`TF-MC-7` (acima); `TR`: `tests/test_rdo.py`, `tests/test_backlog.py`,
  `tests/test_card_check.py` seguem verdes; suíte inteira não reduz o total (`I-2`).
- **Verificação:**
  1. ```
     python -m pytest tests/test_modelo.py -q -p no:cacheprovider
     ```
     → **exit 0**. **Medido antes: exit 4**. (arquivo inexistente em 2026-09-19.)
  2. ```
     python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-valido.md
     ```
     → **exit 0**. **Medido antes: exit 2**. (`python` sem o arquivo sai 2: "can't open file".)
  3. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
     ```
     → **exit 0**. **Medido antes: exit 2**.
  4. ```
     pwsh -NoProfile -Command "python .claude/tools/modelo.py check --plano docs/plans/P-0739-backlog-instrumento.md | Select-String -Pattern 'plano anterior à doutrina' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 0**. (o exit code sozinho não discrimina — `python` sem o script
     também sai `2`; a substring da §6 discrimina.)
  5. ```
     python -m pytest tests -q -p no:cacheprovider
     ```
     → **exit 0**. **Medido antes: exit 0**. Piso: total coletado ≥ 201 + 7 (`I-2`).
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path docs/RUBRICA_DE_REVISAO.md -Pattern 'quatro alvos possíveis' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-23`, passo 7a.)
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -Pattern 'o estado da tarefa no ato do laudo' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-20`, passo 7b.)
  8. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T2 --desde HEAD --atribuir | Select-String -Pattern '-> alvo-do-card' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **10**. **Medido antes: 2**. (`DMC-22`: os dez arquivos-alvo deste card saem
     `alvo-do-card`; medido pelo consultor em 2026-09-20 — dois já contam antes da tarefa,
     porque a `MC-T1` deixou a rubrica e a skill sujas na árvore e este card os re-declara.)
  9. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T2 --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 1**. (invariância: nenhum arquivo tocado fica sem atribuição —
     é o critério de escopo que substitui `git diff --stat`, `DMC-22`.)
- **Pronto quando:** as nove linhas acima devolvem o esperado (`DMC-22` — o `I-7` deixa a árvore
  suja com a materialização de status do loop, então nenhuma forma de `git diff --stat` ou
  `git status --short` é satisfazível; o critério de escopo é a atribuição medida).
- **Fora do escopo desta tarefa:** chamada do instrumento pelas skills (`MC-T4`); qualquer
  verbo de escrita (não planejado).

### MC-T2a — O campo sem consumidor sai da dataclass do instrumento [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Fundamento:** `AE-13` item 3 e a decisão `DMC-26` do `ESC-3`; a §6 deste plano, que congela a
  forma de saída dos dois verbos e não pede posição de linha em lugar nenhum.
- **Depende de:** `MC-T2`
- **Objetivo:** `.claude/tools/modelo.py` não declara nem atribui o campo `linha` da dataclass
  `Oracao`, e a suíte segue verde sem reduzir o total.
- **Oração do modelo:** `M-17`
  - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`; só `modelo.py`. Nenhum teste
  muda de expectativa — se algum precisar mudar, a premissa caiu (contingência 1).
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py` — a dataclass `Oracao` e a construção dela em `_extrair_oracoes`
- **Contratos/classes:** `Oracao` passa a ter `id`, `texto`, `estado`, `estado_data`,
  `estado_ref` e `tarefas` — e nada mais.
- **Passos:**
  1. Apagar a linha `linha: int = 0` da dataclass `Oracao` (`.claude/tools/modelo.py:61` em
     2026-09-20).
  2. Apagar o argumento `linha=offset + i + 1` da construção de `Oracao` em `_extrair_oracoes`
     (`.claude/tools/modelo.py:150` em 2026-09-20), preservando os demais argumentos.
  3. Rodar a suíte inteira e o `check` sobre o corpus real.
- **Restrições desta tarefa:** nenhum outro símbolo de `modelo.py` muda; nenhum arquivo de teste
  muda; `backlog.py`, `review_evidence.py` e `card_check.py` intocados (`I-3`).
- **Não fazer:** não aproveitar a passagem para refatorar `modelo.py`; não criar consumidor para
  o campo — a `DMC-26` decidiu o contrário, e inventar leitor para justificar símbolo é o avesso
  do achado.
- **Contingências:**
  1. se a busca por leitura de `.linha` encontrar consumidor em qualquer arquivo do repositório →
     a premissa da `DMC-26` caiu: parar e sinalizar `blocked` razão `premissa`, com a linha
     encontrada na razão.
- **Testes:** `TR`: `tests/test_modelo.py` e a suíte inteira seguem verdes, sem redução de total
  (`I-2`; piso medido em 245 no fechamento da `MC-T2`).
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern 'linha: int' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern 'linha=offset' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  3. ```
     python -m pytest tests -q -p no:cacheprovider
     ```
     → **exit 0**. **Medido antes: exit 0**. Piso: total coletado ≥ 245 (`I-2`).
  4. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
     ```
     → **exit 0**. **Medido antes: exit 0**. (invariância: a limpeza não quebra o corpus real.)
  5. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T2a --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)
- **Pronto quando:** as cinco linhas acima devolvem o esperado.
- **Fora do escopo desta tarefa:** qualquer outra limpeza de `modelo.py`; os papéis (`MC-T3`).

### MC-T3 — Os três papéis que escrevem o modelo: planejador, revisor e consultor [Sonnet · classe redacao]
- **Status:** `done` · 2026-09-20
- **Fundamento:** decisões `DMC-5`, `DMC-6`, `DMC-7`, `DMC-12`, `DMC-13`, `DMC-19`, e do `ESC-2` as `DMC-21` (regime transitório de confirmação), `DMC-22` e `DMC-23`; fatos `F-1`, `F-2`, `F-4`, `F-9`.
- **Depende de:** `MC-T1`, `MC-T2`
- **Objetivo:** o planner escreve o modelo antes das tarefas e audita a rastreabilidade; o
  reviewer tem `Edit` e o passo de confirmar/emendar; o consultor emenda o modelo em
  escalonamento; a matriz §3 de `GOVERNANCA.md` diz isso em uma cláusula por linha.
- **Oração do modelo:** `M-1`, `M-2`, `M-5`, `M-6`, `M-7`, `M-8`, `M-12`, `M-13`, `M-14`
  - M-1: Todo plano carrega, logo depois do pedido do dono, uma seção chamada "Modelo conceitual".
  - M-2: O modelo é formado por orações numeradas e por um vocabulário.
  - M-5: O planejador escreve o modelo antes de decompor o plano em tarefas.
  - M-6: Cada oração é materializada por pelo menos uma tarefa, e cada tarefa materializa pelo menos uma oração; o card cita as orações e copia o texto delas.
  - M-7: O dono lê o modelo e dá o "go" ou o "no-go" antes de qualquer tarefa ser executada.
  - M-8: O executor lê só o card da tarefa, e o card já traz o texto das orações; o executor nunca edita o modelo.
  - M-12: Ao aprovar a última tarefa que materializa uma oração, o revisor confirma a oração no modelo.
  - M-13: O revisor só altera o texto de uma oração quando a mudança é inequívoca; na dúvida, achado com alvo "modelo".
  - M-14: O planejador, em replanejamento, e o consultor, em escalonamento, emendam o modelo quando uma decisão nova muda o que o plano entrega; a emenda cita a decisão.
- **Camada e fronteira:** definições de agente (`.claude/agents/*.md`) e a matriz de
  `GOVERNANCA.md` §3. Nenhum código.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md` (Fatos estáveis; Fase 3; Fase 4; Fase 5; Anatomia do card)
  - `.claude/agents/pantonic-reviewer.md` (linha 5 `tools:`; Fatos estáveis; Protocolo passo 6; Proibições)
  - `.claude/agents/pantonic-consultant.md` (item 3 de *O que você faz*; descrição do frontmatter)
  - `GOVERNANCA.md` §3 (linhas da matriz *Planejamento*, *Revisão*, *Orquestração*)
- **Contratos/classes:** nenhum.
- **Passos (cada um é um `Edit` com `old_string` único; o `old_string` é o literal citado):**
  1. `pantonic-planner.md`, esqueleto da Fase 3: substituir o bloco cercado inteiro que começa em
     `# P-NNNN — <título>` e termina em `## 8. Achados da execução        (vazio; apensado por quem executa/orquestra)` por:
     ```
     # P-NNNN — <título>            (cabeçalho: data de origem, iniciativa, plano de origem se derivado)
     ## 0. O problema, verbatim
     ## 1. Modelo conceitual          (GOVERNANCA.md §3.2 — escrito ANTES de decompor: vocabulário,
                                       orações M-<n> com estado e tarefas, lista de mudanças MD-<n>;
                                       é o que o dono lê no Marco 1 e dá go/no-go)
     ## 2. Fatos estabelecidos        (cada fato com a fonte: dossiê, doc §, decisão anterior)
     ## 3. Decisões                   (tabela id → valor → razão; toda decisão consumida por ≥ 1 tarefa)
     ## 4. Invariantes de execução    (regras que valem para todas as tarefas — e que cada card repete
                                       na parte que o vincula: o executor não é obrigado a ler esta seção)
     ## 5. Tarefas                    (cards, anatomia abaixo; ordem = ordem de dependência)
     ## 6. Ordem de execução          (grafo explícito: quem depende de quem; o que roda em paralelo)
     ## 7. Fora de escopo (explícito) (o que este plano não faz e onde isso mora, se mora)
     ## 8. Riscos                     (cada risco com resposta pré-decidida: o que o executor faz se ocorrer)
     ## 9. Achados da execução        (vazio; apensado por quem executa/orquestra)
     ```
  2. `pantonic-planner.md`, logo depois desse bloco, antes de `Regras de autoria: fatias`, inserir
     o parágrafo:
     `**O modelo antes das tarefas.** A §1 se escreve antes da §5, na gramática da skill
     \`diario-de-obras\` ("Modelo conceitual (seção do plano)"): vocabulário de todo papel e
     artefato citado; uma oração por comportamento observável, em português corrente, sem crase,
     barra, sigla ou identificador no texto; cada oração com \`estado: prevista\` e a lista das
     tarefas que a materializam; lista de mudanças com a linha \`—\`. Só então decompor: cada
     oração vira ≥ 1 card, e cada card cita ≥ 1 oração no campo \`Oração do modelo\`, com o
     texto copiado. O Marco 1 de todo plano é o dono lendo só a §1 — \`go\` aprova o plano,
     \`no-go\` o cancela antes da primeira tarefa.`
  3. `pantonic-planner.md`, Fase 4: inserir, depois do item `4. **Rastreabilidade**: …` (o item
     inteiro, até `(2026-09-18, \`RP-6\`).`) e antes de `5. **Dimensionamento**`, o item:
     `4a. **Rastreabilidade do modelo** (\`GOVERNANCA.md\` §3.2): toda oração \`M-<n>\` é citada
     por ≥ 1 card e todo card cita ≥ 1 oração existente; nenhuma oração tem crase, barra ou
     identificador no texto; a auto-auditoria roda \`python .claude/tools/modelo.py check
     --plano <plano>\` e só publica com exit \`0\`. Renumeração da Fase 4 não é necessária:
     o item entra como \`4a\`.`
  4. `pantonic-planner.md`, Anatomia do card: **substituir** a linha
     `- **Depende de:** decisões (\`D-n\`) e fatos (\`F-n\`) das §1/§2; tarefas anteriores cujo produto usa.`
     pelas três linhas, nesta ordem (`DMC-19`):
     `- **Fundamento:** decisões (\`D-n\`) e fatos (\`F-n\`) das §1/§2 que o card aplica, e as seções normativas que ele transcreve. Prosa livre: nenhum instrumento lê este campo.`
     `- **Depende de:** \`ID\`[, \`ID\`] — **só ids de tarefa ou de tíquete**, entre crases, separados por vírgula, sem prosa e sem faixa \`..\` (escreva \`\`MC-T1\`, \`MC-T2\`\`, nunca \`\`MC-T1\`..\`MC-T2\`\`). É o campo que \`backlog.py next\` lê para decidir elegibilidade: id que não é item deixa a tarefa inselecionável para sempre. Omitir a linha inteira quando não há tarefa anterior.`
     `- **Oração do modelo:** \`M-<a>\`[, \`M-<b>\`] — as orações da §1 que este card materializa; um sub-bullet \`  - M-<a>: <texto copiado>\` por oração. Obrigatório (\`modelo.py check\`, \`V2\`).`
  5. `pantonic-planner.md`, Rodada de replanejamento, passo 3: substituir
     `3. **Decidir com id novo** na tabela de decisões e **repor o fato que faltou** (inventário,
   medição, contrato) na §1 — o bloqueio quase sempre denuncia um fato que a fase 1 não pediu.`
     por
     `3. **Decidir com id novo** na tabela de decisões e **repor o fato que faltou** (inventário,
   medição, contrato) na §2 — o bloqueio quase sempre denuncia um fato que a fase 1 não pediu.
   Se a decisão muda o que o plano entrega ou como funciona, **emendar o modelo** (§1) no mesmo
   ato: texto da oração, \`estado: emendada · <data> · RP-<n>\`, linha \`MD-<n>\` citando a
   decisão; card novo cita a oração no campo \`Oração do modelo\`.`
  6. `pantonic-reviewer.md`, linha 5: substituir `tools: Read, Glob, Grep, Bash` por
     `tools: Read, Glob, Grep, Bash, Edit`.
  6a. `pantonic-reviewer.md`, Fatos estáveis: substituir o literal (duas linhas do arquivo, com a
     quebra que o arquivo tem entre `possíveis —` e `  \`dossiê\``)
     `três alvos possíveis —` ⏎ `  \`dossiê\`, \`doutrina\`, \`rubrica\`.`
     por
     `quatro alvos possíveis —` ⏎ `  \`dossiê\`, \`doutrina\`, \`rubrica\`, \`modelo\`.`
     (`DMC-23`; a tabela da §6 da rubrica tem quatro linhas desde a `MC-T1`, e a `MC-T2` já
     corrigiu a frase gêmea na rubrica e `_ALVOS_ACHADO`.)
  7. `pantonic-reviewer.md`, Fatos estáveis: inserir, antes do bullet `- Saída: duas linhas de
     veredito ao chamador`, o bullet:
     `- **O modelo conceitual do plano é a única escrita sua** (\`GOVERNANCA.md\` §3.2;
     \`docs/RUBRICA_DE_REVISAO.md\` §7): a seção \`## 1. Modelo conceitual\` do plano da tarefa.
     Confirmar oração é gravar \`estado: confirmada · <data> · <ID>\` na linha de metadados dela;
     emendar é trocar o texto **e** apensar uma linha \`MD-<n>\` em \`### 1.3 Mudanças do
     modelo\` com autor \`revisor · <ID>\`. Nenhuma outra linha do plano.`
  8. `pantonic-reviewer.md`, Protocolo: inserir, depois do passo `5. **Achados de processo** — …`
     (parágrafo inteiro) e antes de `6. **Laudo**`, o passo:
     `5a. **Modelo conceitual** — leia o campo \`Oração do modelo\` do card. Para cada oração
     citada: se esta é a última tarefa aberta que a materializa (as demais estão \`done\` ou
     \`cancelled\` no plano) **e** o veredito que você vai emitir é \`aprovado\` ou \`ressalva\`
     **e** o que está no repositório corresponde ao texto — grave \`estado: confirmada · <data>
     · <ID>\`. Se a entrega tornou o texto inequivocamente falso (fato verificável no diff, com o
     veredito aprovado/ressalva) — emende o texto, grave o mesmo \`confirmada\` e apense
     \`MD-<n>\` com o que mudou. Em qualquer dúvida — texto fica como está, e o laudo leva
     \`--achado-processo modelo "<oração e a divergência>"\`. Plano sem \`## 1. Modelo
     conceitual\`: nada a fazer. Depois de gravar, rode \`python .claude/tools/modelo.py check
     --plano <plano>\` e só emita o laudo com exit \`0\` ou \`2\`.`
  9. `pantonic-reviewer.md`, Proibições: inserir ao final o bullet:
     `- Não escreve fora da seção \`## 1. Modelo conceitual\` do plano, e não emenda oração por
     interpretação: divergência que não é fato do diff vai como achado de alvo \`modelo\`.`
  10. `pantonic-consultant.md`, frontmatter `description`: substituir `reparar o modelo funcional
      do plano` por `reparar o plano e emendar o modelo conceitual dele`.
  11. `pantonic-consultant.md`, item 3: substituir `3. **Repara o modelo funcional do plano.**
      Você edita o plano:` por `3. **Repara o plano e emenda o modelo conceitual.** Você edita o
      plano — e, quando a decisão muda o que o plano entrega ou como funciona, a seção \`## 1.
      Modelo conceitual\` no mesmo ato: texto da oração, \`estado: emendada · <data> · ESC-<n>\`,
      linha \`MD-<n>\` citando a decisão (\`GOVERNANCA.md\` §3.2). Você edita o plano:`.
  12. `GOVERNANCA.md` §3, matriz: na linha `| **Planejamento** |`, acrescentar ao final da
      terceira célula (antes do ` | ` que abre a quarta) o texto `; **o modelo conceitual do
      plano** (§3.2), escrito antes da decomposição e emendado em rodada de replanejamento`. Na
      linha `| **Revisão** |`, acrescentar ao final da terceira célula `; **confirma e emenda o
      modelo conceitual** do plano (§3.2) — sua única escrita fora do laudo`. Na linha
      `| **Orquestração** |`, acrescentar ao final da terceira célula `; roda \`modelo.py check\`
      antes de despachar e antes de fechar cada tarefa e abre o relatório e cada marco com
      \`modelo.py show\` (§3.2)`.
- **Restrições desta tarefa:** cada `Edit` com `old_string` ocorrendo exatamente uma vez
  (todas as âncoras deste card foram contadas em 2026-09-19: uma ocorrência cada; a âncora do
  passo 4, reescrita pelo `DMC-19`, foi recontada em 2026-09-20 pelo consultor: **1**; a do
  passo 6a, `três alvos possíveis —`, foi contada no mesmo dia: **1**); o
  `old_string` é copiado do arquivo **com as quebras de linha que o arquivo tem** — o literal
  do card mostra o texto, a quebra vem do arquivo (o passo 5 atravessa uma quebra); texto
  novo verbatim (`I-4`); o frontmatter dos três agentes continua válido (YAML entre `---`).
- **Não fazer:** não tocar `pantonic-executor.md` (o executor não muda: lê o card); não
  reescrever a linha *Execução* da matriz; não alterar `model:` de nenhum agente; não reescrever
  a verificação 1 para agradar `card_check.py` — a reprovação `item 1: fora da forma da 8.1`
  deste card é falso positivo do instrumento, medido e registrado na `AE-12`.
- **Contingências:**
  1. se qualquer `old_string` dos passos não ocorrer exatamente uma vez → parar e sinalizar
     `blocked` razão `premissa`, nomeando o passo.
  2. se o passo 12 encontrar a célula terminando em texto diferente do lido nesta data → aplicar
     o acréscimo ao final da mesma célula, sem apagar nada, e registrar `contingência 2
     acionada: célula da matriz acrescida ao final`.
- **Testes:** nenhum executável; inspeção mecânica.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '## 1. Modelo conceitual' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '**Oração do modelo:**' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-reviewer.md -Pattern 'tools: Read, Glob, Grep, Bash, Edit' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-reviewer.md -Pattern 'modelo conceitual' -SimpleMatch | Measure-Object).Count"
     ```
     → **3**. **Medido antes: 0**. (passos 7, 8 e 9: uma ocorrência cada.)
  5. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-consultant.md -Pattern 'modelo funcional' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 2**.
  6. ```
     pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern 'modelo.py show' -SimpleMatch | Measure-Object).Count"
     ```
     → **3**. **Medido antes: 2**. (re-derivada pelo consultor em 2026-09-20, `ESC-2`: a norma
     publicada pela `MC-T1` já cita `modelo.py show` duas vezes — o zero de 2026-09-19 media a
     árvore antes daquela entrega, e `card_check` acusou a divergência. O passo 12 acrescenta a
     terceira ocorrência, na linha *Orquestração* da matriz.)
  7. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
     ```
     → **exit 0**. **Medido antes: exit 0**. (re-derivada pelo consultor em 2026-09-20, `ESC-3`:
     a `MC-T2` fechou, o instrumento existe e o `exit 2` de 2026-09-19 caducou; `card_check`
     acusou a divergência. A linha é invariância — afirma que a `MC-T3` não quebra o modelo.)
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-planner.md -Pattern '- **Fundamento:**' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (medido pelo consultor em 2026-09-20, `ESC-1`; afirma o passo 4
     de `DMC-19` — a linha nova existe e o campo de proveniência saiu de `Depende de`.)
  9. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-reviewer.md -Pattern 'quatro alvos possíveis' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-23`, passo 6a.)
  10. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T3 --desde HEAD --atribuir | Select-String -Pattern '-> alvo-do-card' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **4**. **Medido antes: 1**. (`DMC-22`; o 1 anterior é `GOVERNANCA.md`, alvo deste card já
     sujo pela `MC-T1` — medido pelo consultor em 2026-09-20.)
  11. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T3 --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)
- **Pronto quando:** as onze linhas acima devolvem o esperado (`DMC-22` — sob o `I-7` a árvore
  fica suja com a materialização de status do loop, e o critério de escopo é a atribuição
  medida, não `git diff --stat`).
- **Nota ao revisor (regime transitório, `DMC-21` — não é tarefa do executor):** esta é a
  primeira revisão em que o arquivo do agente revisor já traz `Edit` e o passo `5a`. Além das
  orações deste card, **confirme toda oração da §1.2 deste plano que ainda esteja `prevista` e
  cujas tarefas estejam todas em `done`, `cancelled` ou `review`** — são as vencidas pela
  `MC-T2`, que ninguém pôde gravar porque o instrumento e a ferramenta de escrita ainda não
  existiam. Se a sua definição de agente não tiver `Edit`, não force: devolva a pendência na
  linha de retorno; a `MC-T4` recolhe o acumulado pela mesma cláusula.
- **Fora do escopo desta tarefa:** skills do loop (`MC-T4`); README (`MC-T5`).

### MC-T4 — O loop lê, confere e mostra o modelo: `scrum-master` e `passagem-de-bastao` [Sonnet · classe redacao]
- **Status:** `done` · 2026-09-20
- **Fundamento:** decisões `DMC-10`, `DMC-11`, a `DMC-27` do `ESC-4` (o contrato do estado `review` dito nos três lugares), e do `ESC-2` as `DMC-20` (o gate do passo 2 deste card só funciona porque a `V6` aceita `review`), `DMC-21` e `DMC-22`; fatos `F-9`, `F-14`.
- **Depende de:** `MC-T2`, `MC-T3`
- **Objetivo:** o `scrum-master` roda `modelo.py check` no passo 3, abre o relatório de
  encerramento e cada marco com `modelo.py show`; a `passagem-de-bastao` roda `check` no gate de
  fechamento e garante que o dossiê leva o campo `Oração do modelo`.
- **Oração do modelo:** `M-8`, `M-9`, `M-10`, `M-17`
  - M-8: O executor lê só o card da tarefa, e o card já traz o texto das orações que ele materializa.
  - M-9: O orquestrador mostra o modelo ao dono no relatório de encerramento de cada janela e em cada marco de validação, usando a leitura gerada pelo instrumento.
  - M-10: O dono se inteira de qualquer plano em andamento pedindo a leitura do modelo.
  - M-17: O orquestrador roda o instrumento antes de despachar cada tarefa e ao fechar cada tarefa, e modelo inválido bloqueia o despacho e o fechamento.
- **Camada e fronteira:** skills de orquestração; nenhum código.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md` (Passo 3; Passo 6; Passo 9; Relatório de encerramento)
  - `.claude/skills/passagem-de-bastao/SKILL.md` (Parte 2, parágrafo "Fonte do contexto"; Parte 3 item 1)
  - `.claude/agents/pantonic-reviewer.md` — só o passo `5a`, em dois pontos (`DMC-27`)
- **Contratos/classes:** nenhum.
- **Passos (cada um um `Edit` com `old_string` único):**
  1. `scrum-master`, Passo 3, depois do parágrafo que termina em `vai ao passo 10 por \`B3\`.`
     e antes de `Aprovados os dois, e **antes** de delegar`, inserir:
     `Terceiro gate, mecânico: \`python .claude/tools/modelo.py check --plano <plano>\`
     (\`GOVERNANCA.md\` §3.2). Exit \`1\`: **não delega** — o stderr vai à razão e a tarefa cai em
     \`B3\`. Exit \`2\`: plano anterior à doutrina do modelo; segue, com a nota "sem modelo" no
     relatório. Exit \`0\`: segue.`
  2. `scrum-master`, Passo 9, ao final do bloco **Ação** (depois de `entre uma chamada e outra
     (\`DM-11\` do \`P-0740\`).`), inserir o parágrafo:
     `Antes de \`rdo.py close\`, rodar de novo \`python .claude/tools/modelo.py check --plano
     <plano>\`: o reviewer acabou de gravar confirmação ou emenda na \`## 1. Modelo conceitual\`
     (\`GOVERNANCA.md\` §3.2), e exit \`1\` aqui é defeito dessa gravação — a tarefa fica
     \`in-progress\`, o stderr vai ao consultor como escalonamento, e o fechamento espera o
     reparo. Exit \`0\` ou \`2\`: fecha.`
  3. `scrum-master`, `## Relatório de encerramento`: substituir a linha `Uma vez por janela, na
     parada. Ponteiros e números, nunca conteúdo:` por
     `Uma vez por janela, na parada. Abre com a saída integral de \`python
     .claude/tools/modelo.py show --plano <plano> --desde <data de abertura da janela>\` — a
     única exceção à regra de conteúdo, porque o modelo **é** o que o dono lê
     (\`GOVERNANCA.md\` §3.2); plano sem modelo, a linha "sem modelo (plano anterior à
     doutrina)". Depois, ponteiros e números, nunca conteúdo:`
  4. `passagem-de-bastao`, Parte 2, no parágrafo `**Fonte do contexto, em ordem de
     preferência:**`, substituir `(1) dossiê pré-autorado (\`sprint_plan.md\`, card de
     plano) copiado verbatim — exceto números de aceite, ver gate abaixo;` por `(1) dossiê
     pré-autorado (\`sprint_plan.md\`, card de plano) copiado verbatim, **inclusive o campo
     \`Oração do modelo\` com os sub-bullets de texto** (é a única forma de o executor ler o
     modelo — \`GOVERNANCA.md\` §3.2) — exceto números de aceite, ver gate abaixo;`.
  5. `passagem-de-bastao`, Parte 3 item 1, substituir `Sem gate verde, o destino é \`blocked\` ou
     permanece \`in-progress\`, nunca \`done\`.` por `Sem gate verde, o destino é \`blocked\` ou
     permanece \`in-progress\`, nunca \`done\`. No mesmo gate, \`python .claude/tools/modelo.py
     check --plano <plano>\` sai \`0\` ou \`2\` (\`GOVERNANCA.md\` §3.2); exit \`1\` mantém
     \`in-progress\` e escala ao consultor com o stderr.`
  6. `scrum-master`, Passo 6, substituir o bullet inteiro (duas linhas do arquivo, com a quebra
     entre `passa` e `  por aqui`)
     `- **Gatilho:** **gatilho 1** da \`DP-E\` — a tarefa entrou em \`review\`. Tarefa \`blocked\` **não** passa` ⏎ `  por aqui (\`DP-G\` item 4): não há entregável a julgar.`
     pelo mesmo bullet acrescido, ao final, de:
     ` **Confira, antes de invocar, que o status materializado da tarefa no plano é mesmo
     \`review\`** — é essa materialização do passo 5 que torna a confirmação de oração possível:
     a \`V6\` do \`modelo.py\` conta \`done\`, \`cancelled\` e \`review\` como fechados, e com a
     tarefa ainda em \`in-progress\` o revisor não consegue gravar \`confirmada\` sem que o
     \`check\` recuse (\`GOVERNANCA.md\` §3.2). Status diferente de \`review\` aqui é defeito de
     condução do passo 5, não do revisor: materialize e só então invoque.`
  7. `pantonic-reviewer.md`, passo `5a`, dois `Edit` no mesmo parágrafo:
     (i) substituir `se esta é a última tarefa aberta que a materializa (as demais estão \`done\` ou \`cancelled\` no plano)`
     por `se esta é a última tarefa da oração a fechar — as **demais** que a materializam estão \`done\` ou \`cancelled\` no plano, e a que você julga está em \`review\`, estado que o loop materializa na recepção do retorno do executor, antes de invocar você (\`scrum-master\` passos 5 e 6), e que a \`V6\` conta como fechado`;
     (ii) substituir `só emita o laudo com exit \`0\` ou \`2\`.`
     por `só emita o laudo com exit \`0\` ou \`2\`. Se o \`check\` acusar \`V6\` citando a própria tarefa que você julga, ela não foi materializada em \`review\`: **não force** — desfaça a gravação, deixe a oração como estava e registre \`--achado-processo doutrina\` com a linha "a tarefa nao estava em review no ato da revisao". É defeito de condução do loop, e a oração fica para o revisor seguinte.`
     (as duas âncoras foram contadas pelo consultor em 2026-09-20: **1** cada.)
- **Restrições desta tarefa:** texto verbatim (`I-4`); `old_string` único por passo (contado
  em 2026-09-19: uma ocorrência cada; as três âncoras dos passos 6 e 7, em 2026-09-20) e copiado do arquivo **com as quebras de linha que o
  arquivo tem** — os passos 4 e 5 atravessam uma quebra (`card de` ⏎ `plano)`; `ou` ⏎
  `permanece`); nenhuma outra linha das duas skills muda; as tabelas de roteamento (`Bloco A`,
  `Bloco B`) não mudam.
- **Não fazer:** não criar regra nova de roteamento (`B3` e escalonamento já existem); não
  editar `diario-de-obras` (feito na `MC-T1`); em `pantonic-reviewer.md` mexer **só** no passo
  `5a`, nos dois pontos do passo 7 — nenhuma outra linha do agente muda; não tentar consertar a
  guarda `check-drift` (ver `Nota ao revisor`).
- **Contingências:**
  1. se qualquer `old_string` não ocorrer exatamente uma vez → parar e sinalizar `blocked`
     razão `premissa`, nomeando o passo.
- **Testes:** nenhum executável; inspeção mecânica.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'modelo.py show' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'modelo.py check' -SimpleMatch | Measure-Object).Count"
     ```
     → **2**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern 'modelo.py check' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/passagem-de-bastao/SKILL.md -Pattern 'Oração do modelo' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  5. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T4 --desde HEAD --atribuir | Select-String -Pattern '-> alvo-do-card' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **3**. **Medido antes: 1**. (`DMC-22`; re-derivada no `ESC-4` depois de o card ganhar o
     terceiro alvo: `pantonic-reviewer.md` já conta antes, porque a `MC-T3` o deixou sujo na
     árvore, e as duas skills entram com a entrega.)
  6. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T4 --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)
  7. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'Status diferente de' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-27`, passo 6 deste card.)
  8. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-reviewer.md -Pattern 'a que você julga está em' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-27`, passo 7 (i).)
  9. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/agents/pantonic-reviewer.md -Pattern 'achado-processo doutrina' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-27`, passo 7 (ii).)
- **Pronto quando:** as nove linhas acima devolvem o esperado (`DMC-22` — sob o `I-7` a árvore
  fica suja com a materialização de status do loop, e o critério de escopo é a atribuição
  medida, não `git diff --stat`).
- **Nota ao revisor (não é tarefa do executor):**
  1. **Regime transitório (`DMC-21`):** além das orações deste card, **confirme toda oração da
     §1.2 deste plano que ainda esteja `prevista` e cujas tarefas estejam todas em `done`,
     `cancelled` ou `review`** — inclusive as que o revisor da `MC-T3` não tenha conseguido
     gravar. `M-17` só fecha depois da `MC-T2b`, então não a force aqui.
  2. **A guarda `check-drift` chega vermelha, e não é desta tarefa (`AE-15` item 1, `DMC-28`).**
     O vermelho foi criado pela `MC-T3` ao trocar a `description` do consultor, espelhada numa
     tabela **gerada** do `README.md`; o remédio é `kit_check.ps1 -Mode generate`, e está escrito
     como passo da `MC-T5`, dona nomeada do README. Medido em 2026-09-20 no `ESC-4`: exit `1`,
     três linhas de um achado só, todas na linha do `pantonic-consultant`. Não rebaixe `guardas`
     por isso e não peça à `MC-T4` que conserte — o card a proíbe de tocar o README.
- **Fora do escopo desta tarefa:** README (`MC-T5`).

### MC-T4a — O gate do modelo no fechamento para de criar o vermelho que devia reparar [Sonnet · classe redacao]
- **Status:** `done` · 2026-09-20
- **Fundamento:** `AE-16` e as decisões `DMC-30` e `DMC-31` do `ESC-5`; a `DMC-27`, cuja premissa
  (o instante do `check` é o instante em que o reviewer gravou) é o que o passo 9 tinha quebrado.
- **Depende de:** `MC-T4`
- **Objetivo:** no `scrum-master`, o gate do modelo do passo 9 roda **antes** da materialização e
  exit `1` segura a tarefa em `review`; e as duas frases que contam gates passam a contar três.
- **Oração do modelo:** `M-17`
  - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico; o orquestrador roda esse instrumento antes de despachar cada tarefa e ao fechar cada tarefa, e modelo inválido bloqueia o despacho e o fechamento.
- **Camada e fronteira:** skill de orquestração; nenhum código. Um arquivo só.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md` (Passo 3, frase de contagem; Passo 9, linha de `Ação` e parágrafo do gate; Bloco B, célula de condição da linha `B3`)
- **Contratos/classes:** nenhum.
- **Passos (cada um um `Edit` com `old_string` único; as quatro âncoras foram contadas pelo consultor em 2026-09-20: uma ocorrência cada):**
  1. Passo 9, substituir a linha
     `- **Ação:** materializar o status com \`python .claude/tools/backlog.py status <ID> <estado>\`.`
     por
     `- **Ação:** **primeiro o gate do modelo** (parágrafo ao final desta ação, \`DMC-30\`), e só então materializar o status com \`python .claude/tools/backlog.py status <ID> <estado>\`.`
  2. Passo 9, substituir o parágrafo inteiro (cinco linhas do arquivo, com as quebras que ele tem)
     que começa em `Antes de \`rdo.py close\`, rodar de novo` e termina em
     `reparo. Exit \`0\` ou \`2\`: fecha.` por:
     `**Antes de materializar o status**, e portanto antes de \`rdo.py close\`, rodar de novo
     \`python .claude/tools/modelo.py check --plano <plano>\`: o reviewer acabou de gravar
     confirmação ou emenda na \`## 1. Modelo conceitual\` (\`GOVERNANCA.md\` §3.2), e exit \`1\`
     aqui é defeito dessa gravação. Exit \`1\`: **não materializa e não fecha** — a tarefa
     **permanece em \`review\`**, o stderr vai ao consultor como escalonamento, e o fechamento
     espera o reparo. \`review\` é o estado em que o reviewer a julgou e um dos três que a \`V6\`
     conta como fechados, então segurar a tarefa ali não cria vermelho novo; mandá-la a
     \`in-progress\` criaria — inclusive para oração confirmada por outra tarefa que cite esta —
     e ainda é transição que não existe (\`done\` para \`in-progress\` não está em \`_TRANSICOES\`).
     Exit \`0\` ou \`2\`: materializa e fecha.`
  3. Passo 3, substituir `Aprovados os dois, e **antes** de delegar, materializar` por
     `Aprovados os três, e **antes** de delegar, materializar`.
  4. Bloco B, substituir a linha inteira
     `| \`B3\` | a próxima tarefa é recusada pelo \`G-PLANREADY\` ou pelo gate de delegação | não delega: **PARA**, com o que falta fechar |`
     por
     `| \`B3\` | a próxima tarefa é recusada pelo \`G-PLANREADY\`, pelo gate de delegação ou pelo \`modelo.py check\` do passo 3 (exit \`1\`) | não delega: **PARA**, com o que falta fechar |`
- **Restrições desta tarefa:** texto verbatim (`I-4`); um arquivo só; da tabela do Bloco B muda
  **uma** célula, a de condição da linha `B3` — nenhuma outra linha, nenhuma outra tabela, e a
  precedência do bloco não muda; `passagem-de-bastao` **não** é tocada (lá o `in-progress` está
  certo: é o estado em que a tarefa já está, e nenhuma oração foi confirmada ainda).
- **Não fazer:** não reescrever o gate do passo 3, que está correto; não mexer nos blocos `A`;
  não renumerar passos.
- **Contingências:**
  1. se qualquer `old_string` não ocorrer exatamente uma vez → parar e sinalizar `blocked` razão
     `premissa`, nomeando o passo.
- **Testes:** nenhum executável; inspeção mecânica.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'permanece em' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'Aprovados os três' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  3. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'a tarefa fica' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**. (a frase defeituosa some; era ela que mandava a tarefa a `in-progress`.)
  4. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'do passo 3 (exit' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**. (`DMC-31`, quarto passo.)
  5. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T4a --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)
- **Pronto quando:** as cinco linhas acima devolvem o esperado.
- **Fora do escopo desta tarefa:** `passagem-de-bastao`; README e Marco 2 (`MC-T5`); qualquer
  outra linha das tabelas de roteamento.

### MC-T2b — A cadeia sem consumidor sai inteira do instrumento [Sonnet · classe mecanica]
- **Status:** `done` · 2026-09-20
- **Fundamento:** `AE-14` e a decisão `DMC-29` do `ESC-4`. A `MC-T2a` removeu o campo `linha` e,
  com ele, o único leitor de `offset`; o aceite deste card é **propriedade**, não lista de
  posições — é isso que impede a terceira casca.
- **Depende de:** `MC-T2a`
- **Objetivo:** nenhum símbolo de `.claude/tools/modelo.py` fica sem leitor por causa da remoção
  do campo `linha`, e a saída dos dois verbos continua idêntica.
- **Oração do modelo:** `M-17`
  - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`; só `modelo.py`. Nenhum arquivo
  de teste muda de expectativa.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py` — a assinatura de `_extrair_oracoes` e a chamada dela
- **Contratos/classes:** `_extrair_oracoes(secao: list[str]) -> tuple[list[Oracao], dict[int, str]]`
  — um parâmetro a menos. Nenhuma outra assinatura do módulo muda.
- **Passos:**
  1. Remover o parâmetro `offset` da assinatura de `_extrair_oracoes`
     (`.claude/tools/modelo.py:106` em 2026-09-20) e o argumento `inicio` da chamada
     (`:172` em 2026-09-20). A variável `inicio` **permanece**: ela ainda recorta a seção.
  2. **Fechar a cadeia:** procurar no módulo inteiro todo parâmetro, atributo ou variável que
     tenha ficado sem leitor por essa remoção, e removê-lo também. A busca é do executor e o
     resultado vai na linha de retorno como `cadeia fechada: <o que saiu>` — se nada mais saiu,
     `cadeia fechada: nada além de offset e inicio`.
  3. Rodar a suíte inteira e o `check` sobre o corpus real.
- **Restrições desta tarefa:** nenhuma assinatura pública muda além da de `_extrair_oracoes`; a
  saída dos dois verbos é byte a byte a de antes; nenhum arquivo de teste muda; `backlog.py`,
  `review_evidence.py` e `card_check.py` intocados (`I-3`).
- **Não fazer:** não renomear nada; não reorganizar funções; não acrescentar teste para o que
  foi removido — o que some não se testa.
- **Contingências:**
  1. se remover `offset` exigir mudar `tests/test_modelo.py` → há consumidor em teste e a
     premissa da `DMC-29` caiu: parar e sinalizar `blocked` razão `premissa`.
  2. se o passo 2 encontrar símbolo sem leitor que **não** vem da remoção do campo `linha` →
     deixar como está e registrar na linha de retorno: é achado, não escopo deste card.
- **Testes:** `TR`: `tests/test_modelo.py` e a suíte inteira seguem verdes, sem redução de total
  (`I-2`).
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern 'def _extrair_oracoes(secao: list[str], offset: int)' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  2. ```
     pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern '_extrair_oracoes(secao, inicio)' -SimpleMatch | Measure-Object).Count"
     ```
     → **0**. **Medido antes: 1**.
  3. ```
     python -m pytest tests -q -p no:cacheprovider
     ```
     → **exit 0**. **Medido antes: exit 0**. Piso: total coletado não reduz (`I-2`).
  4. ```
     python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md
     ```
     → **exit 0**. **Medido antes: exit 0**. (invariância: a limpeza não quebra o corpus real.)
  5. ```
     pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T2b --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count"
     ```
     → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)
- **Pronto quando:** as cinco linhas acima devolvem o esperado e a linha de retorno declara a
  cadeia fechada (passo 2).
- **Fora do escopo desta tarefa:** qualquer outra limpeza de `modelo.py`; README e Marco 2
  (`MC-T5`).

### MC-T5 — O README explica o modelo, a aferição sobre o próprio plano e o veredito do dono (Marco 2) [Opus + dono · classe redacao]
- **Status:** `review` · 2026-09-20
- **Fundamento:** decisões `DMC-11`, `DMC-15`, a `DMC-28` do `ESC-4` (esta tarefa regenera a região marcada do README e devolve `check-drift` a exit 0), e do `ESC-2` a `DMC-21` (o regime transitório de confirmação expira nesta tarefa); fato `F-12`.
- **Depende de:** `MC-T1`, `MC-T2`, `MC-T2a`, `MC-T2b`, `MC-T3`, `MC-T4`, `MC-T4a`
- **Objetivo:** o `README.md` explica o modelo conceitual em §5 e §8 para o leitor externo; o
  loop gera `modelo.py show` sobre este plano e o dono lê; o aceite do dono fecha o Marco 2.
- **Oração do modelo:** `M-4`, `M-20`
  - M-4: O modelo é a interface entre o dono e o loop: quem lê só o modelo entende o que o plano faz, o que já está pronto, o que está em andamento e o que mudou desde a última leitura.
  - M-20: Este plano é o primeiro a usar o modelo: a seção é confirmada e emendada pelas próprias regras que descreve, tarefa a tarefa, até o segundo marco, quando o dono lê a leitura gerada pelo instrumento e valida.
- **Camada e fronteira:** documentação pública do hub (`README.md`); leitura do dono.
- **Arquivos-alvo:**
  - `README.md` §5 (`## 5. O fluxo plano → execução`), §8 (`## 8. Planos: o que é um plano fechado`) e a região **gerada** entre `<!-- kit:agents:begin -->` e `<!-- kit:agents:end -->`, reescrita por instrumento e não à mão (`DMC-28`)
- **Contratos/classes:** nenhum.
- **Passos:**
  1. Em `README.md` §8, ao final da seção (antes de `## 9. O fechamento de tarefa`), inserir a
     subseção literal:
     ```
     ### 8.1 O modelo conceitual — o que o dono lê

     Todo plano carrega, logo depois do pedido, a seção **Modelo conceitual**: um vocabulário, orações
     numeradas que afirmam o que o resultado faz em linguagem corrente, e uma lista de mudanças. O
     planejador escreve o modelo antes das tarefas e cada tarefa cita as orações que materializa; o
     executor as recebe no card; o revisor confirma cada oração ao aprovar a última tarefa dela, e só
     emenda o texto quando a divergência é inequívoca — na dúvida, abre achado de alvo `modelo`; o
     consultor e o planejador emendam o modelo quando uma decisão muda o que o plano entrega. O
     instrumento `modelo.py` confere a integridade (`check`) e gera a leitura do dono (`show`), que
     abre todo relatório de encerramento e todo marco. Quem lê só essa leitura sabe o que o plano
     faz, o que está pronto, o que está em curso e o que mudou. Norma: `GOVERNANCA.md` §3.2;
     gramática: skill `diario-de-obras`. O primeiro plano com modelo foi o `P-0741`.
     ```
  2. Em `README.md` §5, no parágrafo que começa com `Planejador e executor são papéis
     distintos` e termina com a linha `**sinaliza** \`blocked\` com a razão tipada e escala — não
     improvisa uma alternativa própria.` (linhas 416-420 em 2026-09-19), acrescentar ao final
     dessa última linha, na mesma linha, a frase: ` O plano nasce com o **modelo conceitual**
     (§8.1), e o dono dá go ou no-go lendo só ele — é o Marco 1 de todo plano.`
  3. Rodar `pwsh .claude/checks/check-readme.ps1` e corrigir o que ele apontar **no README**
     (nunca no checker).
  3a. Rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (`DMC-28`): o
     instrumento reescreve as duas regiões marcadas do `README.md` a partir de
     `.claude/agents/*.md` e `.claude/skills/*/SKILL.md`. A linha do `pantonic-consultant` está
     defasada desde a `MC-T3` (`AE-15` item 1) e é isso que a guarda `check-drift` acusa. Não
     editar a tabela à mão: ela é gerada. Depois, rodar `check-readme.ps1` de novo — as duas
     conferências têm de sair exit 0 ao mesmo tempo.
  4. Rodar `python .claude/tools/modelo.py show --plano docs/plans/P-0741-modelo-conceitual.md`
     e colar a saída integral na linha de retorno da entrega, depois da linha de status, para
     que o orquestrador a leve ao dono no relatório (é a leitura do Marco 2). Nesta execução
     `M-4` e `M-20` ainda saem `[prevista]`: quem as confirma é o revisor desta tarefa, depois
     do passo 4 — não é defeito, e o `show` que o orquestrador roda no Marco 2 (`DMC-11`) já
     sai com as vinte confirmadas.
  5. O aceite do dono (leitura da saída do passo 4 e do README) é registrado pelo orquestrador
     no diário (`GOVERNANCA.md` §4.5); a tarefa só fecha `done` com o veredito escrito.
- **Restrições desta tarefa:** texto do passo 1 verbatim; `check-readme.ps1` e `kit_check.ps1`
  intocados; nenhuma outra seção do README muda além de §5, §8 e das regiões **geradas** entre
  os marcadores `kit:agents` e `kit:skills`, que só mudam por `-Mode generate` (`DMC-28`).
- **Não fazer:** não alterar contagens de agentes/skills na frase de *Anatomia do kit* (não
  mudam, `F-12`); não editar o modelo deste plano (é o revisor que confirma); não reescrever a
  verificação 1 para agradar `card_check.py` — a reprovação `item 8: fora da forma da 8.1` deste
  card é falso positivo do instrumento, medido e registrado na `AE-12`.
- **Contingências:**
  1. se `check-readme.ps1` apontar divergência fora de §5/§8 → corrigir só se for consequência
     direta do texto inserido; caso contrário parar e sinalizar `blocked` razão `premissa`.
  2. se `modelo.py show` sair diferente de `0` → parar e sinalizar `blocked` razão
     `dependencia` (a `MC-T2`/`MC-T3` deixaram o modelo inválido).
  3. se `kit_check.ps1 -Mode generate` alterar linha fora das duas regiões marcadas, ou se
     `check-drift` continuar exit `1` depois dele → parar e sinalizar `blocked` razão
     `premissa`, com a saída integral na razão: a causa não é a `description` da `MC-T3` e o
     diagnóstico da `AE-15` item 1 caiu.
- **Testes:** nenhum executável.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '### 8.1 O modelo conceitual' -SimpleMatch | Measure-Object).Count"
     ```
     → **1**. **Medido antes: 0**.
  2. ```
     pwsh -NoProfile -File .claude/checks/check-readme.ps1
     ```
     → **exit 0**. **Medido antes: exit 0**.
  3. ```
     python .claude/tools/modelo.py show --plano docs/plans/P-0741-modelo-conceitual.md
     ```
     → **exit 0**. **Medido antes: exit 0**. (re-derivada pelo consultor em 2026-09-20, `ESC-3`:
     o instrumento passou a existir com a `MC-T2` e o `exit 2` de 2026-09-19 caducou; é
     invariância.)
  4. ```
     pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift
     ```
     → **exit 0**. **Medido antes: exit 1**. (`DMC-28`; medido pelo consultor em 2026-09-20 —
     três linhas de um achado só, todas na linha do `pantonic-consultant`. É a guarda que a
     `MC-T3` virou e que esta tarefa fecha; o plano não termina com ela vermelha.)
- **Pronto quando:** as quatro linhas devolvem o esperado e o veredito do dono está escrito no
  diário.
- **Nota ao revisor (regime transitório, `DMC-21` — não é tarefa do executor):** esta é a última
  tarefa do plano. Além de `M-4` e `M-20`, **confirme toda oração da §1.2 que ainda esteja
  `prevista` e cujas tarefas estejam todas em `done`, `cancelled` ou `review`**: ao fim desta
  revisão as vinte orações têm de estar `confirmada`, e é isso que o Marco 2 mostra ao dono. O
  regime transitório expira aqui.
- **Fora do escopo desta tarefa:** retrofit de planos anteriores; verbos de escrita do
  instrumento.

---

## 9. Ordem de execução

```
MC-T1 (norma + gramática)
  └─► MC-T2 (instrumento; lê a gramática; corpus real = este plano)
        └─► MC-T2a (tira do instrumento o campo sem consumidor; ESC-3, DMC-26)
              └─► MC-T3 (papéis; citam a chamada já medida)
                    └─► MC-T4 (loop; cita a chamada já medida)
                          └─► MC-T4a (o gate do fechamento para de criar vermelho; ESC-5, DMC-30 e DMC-31)
                          └─► MC-T2b (fecha a cadeia sem consumidor; ESC-4, DMC-29)
                                └─► MC-T5 (README regenerado + show sobre este plano + veredito do dono = Marco 2)
```

Fila única, sem paralelismo: cada tarefa cita o produto da anterior. Marco 1 = aprovação deste
plano pelo dono; Marco 2 = fim da `MC-T5`. Commit único no Marco 2 (`I-7`).

## 10. Fora de escopo (explícito)

- **Retrofit** do modelo em `P-0739` ou em qualquer plano anterior (`DMC-14`); se o dono quiser,
  é plano derivado.
- **Verbos de escrita** em `modelo.py` (`marcar`, `emendar`): a escrita é por `Edit` dos papéis;
  se a prática mostrar erro de forma recorrente, vira tíquete.
- **Checagem de siglas** no texto das orações: só crase e barra são mecânicas (`V8`); o resto é
  dever de autoria auditado pelo revisor na `criterio-de-pronto` quando o card prometer.
- **A spec do consultor** (`docs/consultant-spec.md`) e a norma de autoria de card novo: fora;
  este plano só troca a expressão "modelo funcional" pela emenda do modelo conceitual.
- **Executor**: nenhuma mudança em `pantonic-executor.md`.

## 11. Riscos

| risco | resposta pré-decidida |
|---|---|
| O revisor, com `Edit`, toca linha fora da `## 1` | `modelo.py check` no passo 9 não pega isso; a proibição está no agente (`MC-T3` passo 9) e o `review_evidence` da tarefa seguinte mostra o diff do plano — achado de alvo `doutrina` se ocorrer |
| `backlog._parse_plano` muda de assinatura em plano futuro | `modelo.py` importa por caminho e falha ruidosamente no `_load_backlog`; corrigir em tíquete, nunca em card de outro plano |
| Oração com `/` legítimo (ex.: "go/no-go") cai em `V8` | o texto usa "go ou no-go"; a regra é do texto, não do instrumento — já aplicada nas 20 orações deste plano |
| `card_check` suspenso (`AE-33`): as linhas de `Verificação` deste plano não são aferidas por máquina antes do despacho | conferência manual dos três elementos por quem despacha (rubrica §8.1); todas as linhas foram medidas em 2026-09-19 (`F-9`, `F-10`). O `card_check` **rodou** sobre os cinco cards em 2026-09-19: `MC-T2` e `MC-T4` fecham; `MC-T1` (itens 1 e 5), `MC-T3` (item 1) e `MC-T5` (item 1) acusam só o **item fantasma** do `AE-33` — os padrões `### 3.2`, `## 4.`, `## 1.` e `### 8.1` contêm dígito-ponto, que o marcador de item lê como "N." — e nenhuma divergência de medida. Quem despacha ignora só essas quatro linhas fantasma, nada mais |
| O modelo deste plano fica com 20 orações `prevista` até a `MC-T1` fechar e o revisor começar a confirmar | é o comportamento previsto (`M-11`); a primeira confirmação acontece no fechamento da `MC-T1` (orações `M-3`, `M-16`, que só ela materializa) |

## 12. Registro (após aprovação, Controle 1.1 — não é execução)

1. Gravar `docs/plans/P-0741-modelo-conceitual.md` com este conteúdo integral.
2. Apensar a `docs/plans/_INBOX.md` a linha
   `- docs/plans/P-0741-modelo-conceitual.md — modelo conceitual do plano (interface dono↔loop); 5 tarefas MC-T1..MC-T5; Marco 1 = go do dono sobre a §1` e atualizar `**Próximo id de plano: P-0742.**`.
3. Invocar `checar-versao-kit` (modo hub, congelada — nada a comparar).
4. Encerrar o turno sem executar (Regra 1 global).

## Achados da execução

- **AE-1 — as cinco tarefas deste plano são inselecionáveis pelo instrumento de fila (bloqueia a
  janela).** `python .claude/tools/backlog.py next`, com a diretiva do dono apontando para
  `P-0741`, devolve `nada delegável — 0 elegível(is) · blocked 0` (medido 2026-09-20). Causa
  medida: `_extrair_depende` (`.claude/tools/backlog.py:221`) colhe **todo** id entre crases da
  linha `- **Depende de:**`, e `_eh_elegivel` (`:762`) exige `status == done` para cada um. Os
  cinco cards citam decisões e fatos nessa linha (`MC-T1`: `DMC-1`..`DMC-8`, `DMC-17`, `F-2`,
  `F-3`, `F-9`), que não são itens e não têm status: `_status_do_id` devolve `None` para todos, e
  nenhuma tarefa fica elegível — nem a `MC-T1`, que não depende de tarefa alguma. A gramática
  publicada (`.claude/skills/diario-de-obras/SKILL.md:141`) declara o campo como
  `- **Depende de:** \`ID\`[, \`ID\`]` — lista de ids de item, sem prosa e sem referência a
  decisão ou fato. O `P-0740` tem a mesma deformação em seis cards (ex.: `:3936`
  `**Depende de:** \`DM-16\` (iv) e \`DM-17\``), fechados antes de a seleção passar a ser do
  instrumento. Rota: escalonamento ao consultor de plano (gatilho 3 da `docs/consultant-spec.md`
  §2 — impedimento de instrumento que nenhum card cobre).
- **AE-2 — o lint aprova um plano estruturalmente inselecionável.** `backlog.py check` devolve
  `check: OK — nenhuma violação` sobre a árvore que produziu a `AE-1` (medido 2026-09-20).
  Não existe regra que recuse id de `Depende de:` sem item correspondente, nem que recuse prosa no
  campo. A consequência é que o defeito só aparece na hora do despacho, com a janela já aberta.
  Atribuição: `.claude/tools/backlog.py` — arquivo fora dos `Arquivos-alvo` de toda tarefa deste
  plano e vedado pelo `I-3`; é matéria de tíquete, não deste plano.
- **AE-3 — o ponto de carga do instrumento lê utf-8 mas não escreve.** `backlog.py --help` morre
  com `UnicodeEncodeError: 'charmap' codec can't encode character '→'` em console cp1252
  (medido 2026-09-20): `main()` só chama `fluxo.reconfigure(encoding="utf-8")` **depois** de
  `parse_args` (`.claude/tools/backlog.py:1411` vs `:1415`), e o `--help` escreve antes disso —
  como escreve toda mensagem de erro de argparse, que imprime o mesmo `usage` com `→`. É a metade
  de escrita do defeito que o `TK-56a` fechou na leitura. Atribuição: `.claude/tools/backlog.py`,
  mesma residência da `AE-2`.
- **AE-4 — o verbo `diretiva` descarta ids em silêncio.** `_parse_diretiva`
  (`.claude/tools/backlog.py:326`) corta o texto no primeiro `" — "` e só colhe ids do trecho
  anterior. Diretiva escrita como `Priorize o \`P-0741\` — … \`TK-57\`, \`TK-56\`, …` entra sem
  erro e produz `diretiva_ids == ['P-0741']`, filtrando da fila os seis tíquetes que a própria
  diretiva manda priorizar (medido 2026-09-20; corrigido no mesmo ato reescrevendo a linha com os
  ids antes do travessão). O verbo aceita qualquer texto e não avisa quantos ids reconheceu.
  Atribuição: `.claude/tools/backlog.py`, mesma residência da `AE-2`.
- **AE-5 — a deformação foi ensinada pelo gabarito do planner, e é a causa comum do `P-0740` e
  deste plano.** `.claude/agents/pantonic-planner.md:335`, na *Anatomia do card*, manda escrever
  `- **Depende de:** decisões (\`D-n\`) e fatos (\`F-n\`) das §1/§2; tarefas anteriores cujo
  produto usa.` — exatamente a forma que `backlog.py next` não consegue ler (`AE-1`), e o oposto
  da gramática publicada em `.claude/skills/diario-de-obras/SKILL.md:141`. Enquanto a seleção era
  humana, o desvio era inócuo; desde que a seleção é do instrumento, ele torna inselecionável todo
  plano nascido do gabarito. **Reparo (`ESC-1`, consultor, 2026-09-20, decisão `DMC-19`):** (i) os
  cinco cards deste plano passaram à gramática publicada — `Depende de` só com id de tarefa,
  proveniência preservada no campo novo `- **Fundamento:**`, e a faixa `\`MC-T1\`..\`MC-T4\`` da
  `MC-T5` expandida para os quatro ids (a faixa também não era lida: `_extrair_depende` colhia só
  as pontas); (ii) a `MC-T3` absorveu a correção do gabarito no passo 4, que passa de "inserir" a
  "substituir", com a verificação 8 nova. Medido depois do reparo: `MC-T1` elegível com
  `depende_de == []`, `MC-T2`..`MC-T5` na cadeia correta, `backlog.py check` exit 0. O `P-0740`
  **não** é retrofitado: está fechado, e nenhuma tarefa dele volta à fila.
- **AE-6 — o campo `Oração do modelo` é o único acoplamento de card que os instrumentos vão ler;
  o `Fundamento` é inerte por construção.** Verificado em 2026-09-20 antes de criar o campo:
  nenhum de `card_check.py`, `review_evidence.py` e `rdo.py` enumera campos de card (nenhum casa
  `- **<Campo>:**`), e `backlog.py` só lê `Status`, `Depende de`, `Tipo` e `Notas de execução`.
  Logo `- **Fundamento:**` não exige parser novo — a regra "gramática nova não se aplica antes de
  o parser aprender" (`AE-5`/`AE-6` do `P-0739`) está satisfeita por vacuidade, e a `MC-T2` não
  ganha trabalho: `modelo.py check` continua olhando só `Oração do modelo` (`V2`, `V4`).
- **AE-7 — os três achados de instrumento viraram o tíquete `TK-65`.** `AE-2`, `AE-3` e `AE-4`
  foram abertos como `TK-65` (`docs/DIARIO_DE_OBRAS.md`, `## TK-65`), com as subtarefas `TK-65a`
  (o `check` recusa id de `Depende de:` que não é item), `TK-65b` (o ponto de carga escreve em
  utf-8 antes de argparse) e `TK-65c` (o verbo `diretiva` não descarta id em silêncio), as três
  `ready` e nenhuma na diretiva corrente — não competem com este plano. `backlog.py check` exit 0
  depois da abertura. Quem os executa é a fila, não este plano (`I-3`).
- **AE-8 — duas janelas de loop rodando sobre a mesma árvore ao mesmo tempo; a doutrina não tem
  regra para isso, e foi o que encerrou esta janela sem despacho.** Medido 2026-09-20 entre 10:05 e
  10:07: `ListAgents` lista três sessões locais vivas além desta; `.claude/tools/backlog.py`
  (10:06:26) e `tests/test_backlog.py` (10:06:58) foram escritos **um minuto antes** da medida, por
  nenhum ato desta janela, e o que entrou no `backlog.py` é a checagem `C-10` do contador
  `**Próximo id de plano:**` do inbox — o objeto exato da `TK-59a`. No diário, `TK-59a` está
  `in-progress` e `TK-58a` `blocked` com a razão "Fila reordenada pelo loop (regra A3a)", escrita em
  ASCII sem acento (grafia que esta janela não usa). Três consequências medidas ou estruturais:
  (i) `selecionar_next` devolve o único item `in-progress` **antes** de avaliar elegibilidade
  (`.claude/tools/backlog.py:779-784`), então enquanto a `TK-59a` da outra janela não fechar, `next`
  nunca devolve `MC-T1` — a fila deste plano fica atrás de um slot que não é dele;
  (ii) `transacionar_status` reescreve `docs/DIARIO_DE_OBRAS.md` **inteiro** por
  `_escrever_atomico` (`:1091`), sobre o conteúdo que carregou no início da transação: duas janelas
  materializando status no mesmo arquivo perdem a escrita da primeira sem erro e sem aviso —
  o `TK-65` recém-aberto e a linha de diretiva desta janela estão expostos a isso até uma das duas
  fechar;
  (iii) `.claude/estado/tarefa-corrente.json` é **um só por repositório**, não um por sessão, e é o
  insumo do hook `SubagentStop` — daí a `AE-9`.
  Nenhuma regra do bloco A ou do bloco B da `scrum-master` cobre a condição; ela não é poluição de
  contexto (`Regra 2`: o cenário desta janela continua sendo só o `P-0741`) nem plano não-pronto
  (`B3`: depois da `DMC-19` o plano está pronto). É estado de árvore, e a decisão de qual janela
  cede é do dono.
- **AE-9 — o hook de telemetria atribuiu ao `TK-59a` o consumo de um subagente desta janela.** A
  linha `2026-09-20 PantonicApp TK-59a sonnet 54 98.0 458.8 usage` de `docs/telemetria.tsv` carrega,
  campo a campo, o `<usage>` do consultor deste plano (`tool_uses` 54, 98.026k, 459.073s) — medido
  na notificação de conclusão dele. O hook lê `.claude/estado/tarefa-corrente.json`, que é global do
  repositório e naquele instante trazia a tarefa **da outra janela**; nem o modelo bate (o consultor
  é Opus, a linha saiu `sonnet`). Corrigida à mão por esta janela para
  `P-0741-ESC-1` / `opus`, conforme o passo 9 da `scrum-master` ("linha do hook que divergir do
  `<usage>` é corrigida à mão pelo loop"). Sem a correção, 98k de um escalonamento do `P-0741`
  entrariam na série da `TK-59a` e no custo do plano errado. A causa é a mesma da `AE-8` (iii) e
  **não** está coberta pelo `TK-65`.
- **AE-10 — a linha `Pronto quando` de quatro cards deste plano é insatisfazível como está escrita,
  e o `B0` o mediu.** O `MC-T1` fechou com a pendência autoral `git diff --stat lista 5 arquivos,
  não 3`. Atribuição **medida** em 2026-09-20 por
  `review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T1 --desde e0efcf6 --atribuir`:
  10 arquivos, **0 sem atribuição** — `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md` e
  `.claude/skills/diario-de-obras/SKILL.md` saem `alvo-do-card`; `docs/DIARIO_DE_OBRAS.md`,
  o próprio plano, `docs/telemetria.tsv`, `docs/RDO/INDEX.md` e os três artefatos de
  `docs/RDO/` saem `registro-da-orquestracao`. Logo a pendência é integralmente atribuível a
  arquivo fora dos alvos e **não rebaixa a entrega** (`B0` da `scrum-master`). A causa é do texto
  do card, não da execução: sob o `I-7` (ninguém commita) a materialização de status do loop vive
  na mesma árvore suja, e `git diff --stat` nunca listará três arquivos. O revisor achou a mesma
  cláusula nos cards das linhas 531, 853 e 934. **Rota:** re-derivar a linha nos quatro cards como
  "nenhum arquivo além dos três atribuído à entrega pelo `--atribuir`" — matéria do `ESC-2`.
  **Reparo (`ESC-2`, consultor, 2026-09-20, decisão `DMC-22`):** a cláusula de `git diff --stat` e
  a de `git status --short` saíram do `Pronto quando` das `MC-T2`, `MC-T3` e `MC-T4` e viraram
  duas linhas de `Verificação` cada uma — contagem de `-> alvo-do-card` igual ao número de
  arquivos-alvo do card, e `0 sem atribuicao` como invariância —, com `--desde HEAD`, que o `I-7`
  mantém parado durante o plano inteiro. Todas as quatro linhas foram rodadas pelo consultor antes
  de serem publicadas (`DM-12`): `MC-T2` antes = 2, `MC-T3` antes = 1, `MC-T4` antes = 0, e
  `0 sem atribuicao` = 1 nos três. A `MC-T1` está `done` e não é retrofitada: a pendência autoral
  dela fica registrada aqui.
- **AE-11 — a norma que a `MC-T1` publicou tranca o próprio fechamento (`escalar`, `B1`).** Laudo
  de 2026-09-20: `aprovado 100 bloqueante=nenhuma`, transcrição literal impecável nas três
  residências (cinco verificações `1/1/1/1/1`, nenhuma outra linha tocada) — e recomendação
  `escalar`, por deadlock **de autoria do texto-fonte**, não de execução. A `### 3.2` de
  `GOVERNANCA.md` manda o revisor gravar `confirmada` no mesmo ato do laudo; a `V6` da gramática
  publicada na mesma entrega exige que toda tarefa citada esteja `done` ou `cancelled`. Para
  oração de tarefa única (`M-3`, `M-16` — só a `MC-T1` as materializa), `modelo.py check` sairia
  `1` **antes** do `rdo.py close`, e o gate do passo 27-28 da `MC-T4` bloquearia o `close` que
  produziria o `done`. A decisão — confirmar **depois** do `close`, ou a `V6` aceitar tarefa em
  `review` — tem de existir **antes** da `MC-T2`, que é quem codifica a `V6`. Mais quatro achados
  de processo, todos alvo `dossiê`, colhidos no mesmo laudo e roteados junto: (i) a linha 253 de
  `docs/RUBRICA_DE_REVISAO.md` ainda diz "três alvos possíveis" com a tabela da §6 agora em quatro
  linhas, e nenhum card do plano fecha essa frase; (ii) `.claude/agents/pantonic-reviewer.md:28`
  repete a mesma enumeração de três alvos e a `MC-T3` toca o arquivo sem corrigi-la; (iii) janela
  norma-antes-do-parser, que inverte o `AE-5`/`AE-6` citados na `DMC-16` — a §6 publica o alvo
  `modelo` e a `### 3.2` manda usá-lo, mas `rdo.py --achado-processo` o recusa hoje (medido:
  `modelo` fora de `['dossie','doutrina','rubrica']`), e a §7 atribui ao revisor uma escrita que o
  agente não pode fazer sem `Edit`; (iv) o `AE-10` acima. **Rota:** escalonamento `ESC-2` ao
  consultor de plano, que decide a ordem do deadlock e emenda os cards; a janela segue com o que
  ele devolver (`B1`). **Reparo (`ESC-2`, consultor, 2026-09-20 — tático, decisões `DMC-20` a
  `DMC-24`):** (i) o deadlock se resolve na `V6`, que passa a aceitar `review` — o estado em que o
  loop materializa a tarefa antes de despachar o revisor (`scrum-master` passo 5; transições em
  `.claude/tools/backlog.py:1174-1176`) —, e `M-17` foi emendada (`MD-1`); o deadlock não era só
  das orações de tarefa única: valia para toda oração no ato da sua última tarefa; (ii) regime
  transitório `DMC-21`: `M-3` e `M-16` foram confirmadas neste ato pelo consultor (`MD-2`), e as
  demais confirmações vencidas ficam a cargo do primeiro revisor que puder escrever, por cláusula
  auto-sanável no campo `Nota ao revisor` das `MC-T3`, `MC-T4` e `MC-T5`; (iii) as duas
  enumerações "três alvos possíveis" fecham na `MC-T2` (rubrica, passo 7a) e na `MC-T3` (agente,
  passo 6a); (iv) a `AE-10` fechou pela `DMC-22`; (v) achado novo do próprio reparo, não visto
  pelo revisor: a oração `M-18` termina em "nunca redigida à mão", e "crase" lida como acento
  grave em vez de backtick faria a `V8` reprovar o corpus real na primeira execução do instrumento
  — a `V8` da §6 passou a nomear os codepoints (`DMC-24`). A janela **segue** e despacha a
  `MC-T2`.
- **AE-12 — `card_check.py` lê como marcador de item um número que está dentro do comando
  publicado, e reprova a `MC-T3` por falso positivo.** Medido 2026-09-20 pelo consultor no
  `ESC-2`, rodando a régua sobre os três cards abertos: `MC-T2` e `MC-T4` saem
  `card_check: OK`; `MC-T3` sai `item 1: fora da forma da 8.1 (bloco cercado não vem logo após
  "1.")`. Causa: `_ITEM_MARKER_RE` (`.claude/tools/card_check.py:71`) varre o texto do campo já
  achatado por `rdo._parsear_campos` e casa **qualquer** `N.` precedido de espaço — inclusive o
  `1.` dentro do literal `'## 1. Modelo conceitual'`, que é o padrão que a própria verificação 1
  da `MC-T3` procura. O marcador falso não tem bloco cercado depois, vira `falhas_forma` e
  reprova o card inteiro. O gate está suspenso em efeito (`AE-33` do `P-0740`), então não
  bloqueia nada; o que ele produz é ruído que o loop precisa saber ignorar nesta tarefa.
  **Segunda ocorrência, medida no `ESC-3` (2026-09-20):** a `MC-T5` sai `item 8: fora da forma
  da 8.1` pela mesma causa — o literal `'### 8.1 O modelo conceitual'` dentro do comando da
  verificação 1 dela. `MC-T2`, `MC-T2a` e `MC-T4` saem `card_check: OK`.
  Atribuição: `.claude/tools/card_check.py`, arquivo vedado pelo `I-3` e fora dos alvos de toda
  tarefa deste plano — é matéria de tíquete, mesma residência da `AE-2`, e **não** é do `TK-65`
  (que é de `backlog.py`). Usar a mesma régua no corpus real foi o que expôs, no mesmo ato, a
  verificação 6 da `MC-T3` com `Medido antes` defasado pela entrega da `MC-T1` — essa foi
  corrigida (`ESC-2`).
- **AE-13 — três achados do laudo da `MC-T2` (`ressalva 91`, `bloqueante=nenhuma`,
  `seguir com ressalva`, `A8`), cada um com rota.** A entrega passou: `modelo.py` existe com os
  dois verbos, as oito violações saem na ordem, `EX-T4` (`cancelled`) e `EX-T5` (`review`) não
  disparam `V6`, o corpus real sai exit 0, o piso fechou em 245 e as guardas todas exit 0. Os três
  achados são de **texto de card e de rubrica**, não de código:
  1. **(alvo `dossiê`) A verificação 4 do card é linha morta.** O padrão acentuado
     `plano anterior à doutrina`, canalizado por pipe de `python`, **nunca casa**: o card exige
     stdout em UTF-8 forçado (`_forcar_utf8`, §6) e o PowerShell decodifica o pipe em `ibm850` —
     a linha devolve 0 nos dois mundos. O comportamento que ela visava **está entregue e coberto**
     (exit 2 mais a substring literal, conferidos direto pelo `TF-MC-6` e pela varredura dos 22
     planos reais). **Rota:** emenda das verificações remanescentes pelo consultor — trocar o
     padrão por recorte ASCII ou medir o exit code; a da `MC-T2` já se consumiu.
  2. **(alvo `rubrica`) A §8 não tem critério contra esse padrão.** Os critérios (xi) e (xii)(c)
     exigem `-SimpleMatch` e recorte do literal da fonte, mas nada proíbe recortar literal
     **acentuado** de saída que chega por pipe de instrumento com codificação forçada — o recorte
     fiel da fonte produz linha morta. **Rota:** emenda à §8 (padrão canalizado de instrumento com
     saída UTF-8 forçada é ASCII-only; acento só via `Select-String -Path` sobre arquivo, como nas
     verificações 6 e 7 do mesmo card, que passam).
  3. **(alvo `dossiê`) O campo `linha: int` da dataclass `Oracao` não tem consumidor.** O bloco
     `Contratos/classes` do card o impõe; `_extrair_oracoes` o atribui e ninguém o lê — símbolo
     sem consumidor criado por fidelidade à rota (`G-PLANFIDELITY`), fora do alcance do
     `dead_code.py`. **Rota:** decidir antes da `MC-T4` — remover o campo ou dar-lhe consumidor
     lá.
  **Reparo (`ESC-3`, consultor, 2026-09-20 — tático, decisões `DMC-25` e `DMC-26`):**
  (i) varridas as onze verificações da `MC-T3`, as seis da `MC-T4` e as três da `MC-T5`: **nenhuma
  repete o defeito**. As quatro canalizadas que existem (`MC-T3` 10 e 11, `MC-T4` 5 e 6) recortam
  literal **ASCII** de `review_evidence.py --atribuir`, que é ASCII por desenho, e o pipe está
  provado vivo por medição não-zero no mesmo dia e no mesmo console (verificação 8 da `MC-T2`
  mediu 2; a 10 da `MC-T3` mediu 1). As acentuadas restantes são todas `Select-String -Path` sobre
  arquivo, forma que a própria `MC-T2` validou nas verificações 6 e 7. A regra que faltava ficou
  escrita na `DMC-25`, para que nenhuma emenda futura acentue um padrão canalizado;
  (ii) o campo `linha` sai, sem consumidor novo (`DMC-26`), pelo card `MC-T2a`, que remove a
  declaração e a atribuição e não toca mais nada — `M-17` ganhou a tarefa na lista (`MD-3`);
  (iii) a §8 da rubrica **não** é emendada por este plano: concordo com a rota de tíquete no
  fechamento da janela. O que o tíquete precisa carregar são dois critérios, não um: *padrão
  recortado de saída canalizada de instrumento é ASCII* **e** *verificação que mede o mesmo valor
  antes e depois não discrimina e não é aceite* — o segundo é o que teria pegado esta linha morta
  sem depender de codificação;
  (iv) dois achados do próprio reparo, nenhum visto pelo laudo: o `Medido antes` da verificação 7
  da `MC-T3` e o da 3 da `MC-T5` declaravam `exit 2` de 2026-09-19 e caducaram quando a `MC-T2`
  criou o instrumento — `card_check` acusou as duas, e as duas foram re-derivadas para `exit 0`
  como invariância (é a terceira vez que uma entrega irmã caduca um `Medido antes` neste plano:
  antes foi a verificação 6 da `MC-T3`, no `ESC-2`); e o campo de máquina
  `**Ordem de execução:**` do cabeçalho terminava em `MC-T5.` — com o ponto colado, o token nunca
  casava o id, e `_irmaos_ordenados` mandava a tarefa para o fim por desempate posicional em vez
  de por ordem declarada. Corrigido no mesmo ato, junto com a inserção da `MC-T2a`; sem isso,
  `backlog.py next` devolvia a `MC-T3` com a `MC-T2a` elegível e à frente dela.
  Observação do revisor, sem rota: o cabeçalho de `show` sai `plano-valido — plano-valido` nas
  fixtures porque `backlog._parse_plano` cai no fallback `caminho.stem` quando o H1 não é
  `P-NNNN`; no corpus real sai correto. É propriedade do id sintético das fixtures, não defeito do
  instrumento — mas nenhum `TF` olha essa linha do gabarito da §6.
- **AE-14 — a deleção da `MC-T2a` mudou o símbolo sem consumidor de forma, em vez de eliminá-lo.**
  Laudo de 2026-09-20: `aprovado 100 bloqueante=nenhuma`, `seguir` — a entrega está correta e a
  saída dos dois verbos é idêntica à de antes. Mas, apagado o argumento `linha=offset + i + 1`, o
  parâmetro `offset` de `_extrair_oracoes` (`.claude/tools/modelo.py:106`) e o argumento `inicio`
  no chamador (`:172`) ficaram **sem leitor**, e seguem fora do alcance do `dead_code.py`
  (exit 0). O executor **não podia** fechar isso: a linha `Restrições desta tarefa` do card proíbe
  tocar qualquer outro símbolo de `modelo.py`, e a `DMC-26` delimitou a deleção aos dois pontos.
  O defeito é da **decomposição**, não da entrega — o card recortou o sintoma e não a cadeia.
  **Rota:** card irmão da `MC-T2a` que remova o parâmetro e o argumento, ou decisão do consultor
  que os preserve por razão declarada. Não bloqueia a `MC-T3`, que é `classe redacao` e não toca
  `modelo.py`; fica para o próximo contato com o consultor ou para o relatório de janela.
  **Reparo (`ESC-4`, consultor, 2026-09-20, decisão `DMC-29`):** preservar está fora de questão —
  não há fato que peça o parâmetro, e a razão declarada seria generalidade especulativa, o mesmo
  vício da `DMC-26`. Fecha pelo card novo `MC-T2b`, colocado entre a `MC-T4` e a `MC-T5`, cujo
  aceite é **propriedade e não posição**: "nenhum símbolo de `modelo.py` fica sem leitor por
  causa da remoção do campo `linha`", com um passo explícito de fechamento de cadeia e uma linha
  de retorno que declara o que saiu. O defeito de decomposição é meu: a `DMC-26` delimitou a
  deleção a duas posições medidas e a `MC-T2a` fez exatamente o que o card mandou. Card recortado
  por posição repete o erro na casca seguinte; recortado por propriedade, não.
- **AE-15 — a `MC-T3` publicou um contrato que o instrumento da `MC-T2` não aceita, e uma guarda
  ficou vermelha sem remédio executável.** Laudo de 2026-09-20: `ressalva 88 bloqueante=nenhuma`,
  recomendação `escalar` (`A8a`). A entrega está limpa — os doze `Edit` saíram literais, as onze
  verificações bateram na primeira passagem quando o revisor as re-rodou (`1, 1, 1, 3, 0, 3,
  exit 0, 1, 1, 4, 1`), frontmatter YAML válido nos três agentes, `pantonic-executor.md` intocado.
  Três achados:
  1. **(alvo `dossiê`) `kit_check -Mode check-drift` virou exit 1 e não tem estado verde
     alcançável dentro do escopo do card.** O passo 10 troca a `description` de
     `.claude/agents/pantonic-consultant.md`, e o `README.md` espelha esse campo numa tabela
     **gerada**; o mesmo card põe o README em `Fora do escopo`, com dono nomeado. Medido: a guarda
     estava exit 0 no fechamento da `MC-T2a` e foi esta tarefa que a virou; os "3 problemas" do
     instrumento são três linhas de um achado só. O revisor recusou tratar como bloqueante pelo
     critério (xii)(d) da §8 da rubrica — "inválido por construção" —, marcou `guardas` como
     `parcial`, passou `--vermelho-mecanico guardas` para que o vermelho constasse do laudo, e
     **rota:** `MC-T5`, que já é a dona nomeada do README. **A guarda segue vermelha até lá, e o
     dossiê de evidência da `MC-T4` vai trazê-la vermelha pela mesma causa.**
  2. **(alvo `dossiê`) O passo `5a` que esta tarefa escreveu não fecha com a `V6` que a `MC-T2`
     codificou.** O texto do `5a` manda o revisor confirmar quando "as demais estão `done` ou
     `cancelled`" — descrevendo a tarefa revisada como **aberta** —, enquanto a `V6`
     (`_ESTADOS_FECHADOS = {"done", "cancelled", "review"}`) recusa `confirmada` se **qualquer**
     tarefa da oração, inclusive a revisada, estiver fora do conjunto. A `DMC-20` tentou fechar
     isso admitindo `review`, mas nada no texto põe a tarefa em `review` antes de o revisor
     escrever. **Metade operacional resolvida no mesmo ato:** o loop vinha materializando `review`
     só no fechamento, e o passo 5 da `scrum-master` sempre mandou materializar na **recepção do
     retorno do executor** — defeito de condução desta janela, corrigido; com o card em `review`,
     as oito orações entraram sem recusa. **Metade normativa aberta:** a frase do `5a` continua
     dizendo outra coisa. **Rota:** `MC-T4`, dona do passo 3 do `scrum-master`, que herdaria o
     mesmo descasamento.
  3. **(alvo `rubrica`) A dimensão `guardas` não tem faixa para o vermelho do item 1.** O nível
     `parcial` só contempla vermelho de **causa anterior** à tarefa; vermelho que a própria tarefa
     cria e cuja correção o card declarou fora de escopo, nomeando o card irmão, não tem nível.
     Marcado por aproximação. **Rota:** emenda à §4 de `docs/RUBRICA_DE_REVISAO.md` — tíquete, não
     matéria deste plano (a §4 está fora da superfície delimitada pela `DMC-17`).
  **Estado do modelo ao fim da `MC-T3`:** versão 5, `20 orações, 6 tarefas, 5 mudanças`,
  `modelo.py check` exit 0; `show` lê `14 entregues · 1 em curso · 1 emendadas · 4 previstas`.
  **Reparo (`ESC-4`, consultor, 2026-09-20 — tático, decisões `DMC-27` e `DMC-28`):**
  (i) item 2 — a `DMC-20` decidiu certo e a `MC-T2` codificou certo; o que faltou foi **escrever a
  premissa onde o revisor lê**. A `MC-T4` ganha `.claude/agents/pantonic-reviewer.md` nos alvos e
  dois passos novos: o 6 põe no passo 6 do `scrum-master` a conferência explícita de que o status
  materializado é `review` **antes** de invocar o revisor, e o 7 reescreve o `5a` em dois pontos —
  a tarefa julgada deixa de ser descrita como "aberta" e passa a ser nomeada como a que está em
  `review`, com a `V6` citada, mais a saída para o caso de o `check` acusar `V6` na própria tarefa
  julgada: não forçar, desfazer a gravação e registrar achado de alvo `doutrina`, porque aí o
  defeito é de condução do loop. As três âncoras foram contadas: **1** cada;
  (ii) item 1 — **confirmado por medição que a `MC-T5`, como estava escrita, não consertaria a
  guarda**: ela só roda `check-readme.ps1`, que sai exit 0 e não olha a coluna de descrição, e a
  própria linha `Restrições` proibia mexer no resto do README. A `MC-T5` ganhou o passo 3a
  (`kit_check.ps1 -Mode generate`, que reescreve só as duas regiões marcadas —
  `.claude/checks/kit_check.ps1:266-285`), a região gerada nos `Arquivos-alvo`, a restrição
  reescrita, a contingência 3 e a verificação 4 (`check-drift` → exit 0, **medido antes: exit 1**).
  A `MC-T4` recebe a guarda vermelha já reconciliada na `Nota ao revisor`, com a causa, o dono e a
  instrução de não rebaixar `guardas` por ela;
  (iii) item 3 — **concordo com a rota de tíquete**: a §4 da rubrica está fora da superfície da
  `DMC-17` e emendá-la aqui estouraria o `G-SURFACE`. Dois conteúdos para o tíquete, não um: a
  dimensão `guardas` precisa de faixa para *vermelho que a própria tarefa cria e cuja correção o
  card declarou fora de escopo, com dono nomeado*; e, a montante, vale perguntar se o planejamento
  deve **permitir** card assim sem card irmão declarado — se não permitir, a faixa nova quase
  nunca é usada, que é o desfecho melhor.
- **AE-16 — a `MC-T4` publicou dois gates no loop e o texto ditado pelo card ficou incoerente com
  o que já estava lá.** Laudo de 2026-09-20: `ressalva 88 bloqueante=nenhuma`,
  `seguir com ressalva` (`A8`). Entrega exemplar — sete `Edit` literais, as nove verificações
  medidas pelo revisor (`1,2,1,1,3,1,1,1,1`), nenhuma linha fora dos três alvos, nenhuma
  contingência. O circuito ponta a ponta fechou: o passo 6 do `scrum-master` e o passo `5a` do
  revisor passaram a dizer a mesma coisa nos dois lados, com a `V6` contando `review` como fechado
  (`.claude/tools/modelo.py:83`) — a `DMC-27` está provada. Os dois achados são de **autoria do
  card**, e o executor estava proibido de corrigi-los:
  1. **(alvo `dossiê`) O passo 3 do `scrum-master` ganhou um terceiro gate sem fechar as frases da
     mesma seção que contam gates.** O parágrafo seguinte continua dizendo "Aprovados os **dois**,
     e **antes** de delegar", e a condição da linha `B3` do Bloco B ainda enumera só
     `G-PLANREADY` e o gate de delegação. Critério (viii) da §8 da rubrica, mesma classe da
     `AE-12`. O card proibiu tocar as tabelas de roteamento e as demais linhas.
  2. **(alvo `doutrina`, o mais grave) O parágrafo do passo 2, já gravado no passo 9 do
     `scrum-master`, manda a tarefa para `in-progress` quando `modelo.py check` sai 1 antes do
     `rdo.py close` — e esse estado é um poço.** Nenhum dos dois estados do passo 9 é
     `in-progress` (o gatilho é tarefa em `done`; a primeira ação é materializar o status), e
     `in-progress` **não** está em `_ESTADOS_FECHADOS` (`done`, `cancelled`, `review`). Logo,
     diante de um `V6` de confirmação gravada pelo revisor, mandar a tarefa a `in-progress`
     **perpetua o vermelho que o parágrafo tenta reparar** e trava o próximo despacho pelo gate
     do passo 3 recém-criado.
  **Rota dos dois:** escalonamento ao consultor (`ESC-5`), com reparo junto da `MC-T5`.
  **Reparo (`ESC-5`, consultor, 2026-09-20 — tático, decisões `DMC-30` e `DMC-31`):** os dois
  fecham no card novo `MC-T4a`, **não** na `MC-T5`. Três razões: a `MC-T5` é o Marco 2 e não deve
  misturar emenda de doutrina com a leitura do dono; o alvo é a skill do loop, não o README; e o
  reparo precisa valer **antes** da `MC-T2b`, que edita o próprio `modelo.py` e é, de todos os
  cards que restam, o mais capaz de produzir o exit `1` que dispara a rota defeituosa. Por isso a
  `MC-T4a` entra na fila entre a `MC-T4` e a `MC-T2b`.
  Sobre o item 2, o diagnóstico do revisor está certo e o consultor mediu mais um fato que o
  agrava: como a materialização é a **primeira** ação do passo 9, no texto vigente a tarefa já
  está `done` quando o gate roda, e a transição de `done` para `in-progress` **não existe** em
  `_TRANSICOES` (`.claude/tools/backlog.py:1170-1178`) — `backlog.py status` recusaria a
  instrução. O reparo é duplo: o gate passa a rodar **antes** da materialização, e o desfecho de
  exit `1` passa a ser a tarefa **permanecer em `review`** — estado legal, estável, aquele em que
  o reviewer a julgou, e um dos três que a `V6` conta como fechados, de modo que segurar a tarefa
  ali não cria vermelho novo. Que o gate do passo 3 continue bloqueando o despacho seguinte deixa
  de ser defeito e passa a ser o comportamento correto: o modelo está quebrado e nada deve ser
  despachado até o reparo. A `passagem-de-bastao` **não** é tocada: lá o `in-progress` é o estado
  em que a tarefa já está, nenhuma oração foi confirmada ainda, e "mantém `in-progress`" significa
  "não avança para `done`", que é o certo.
  **Estado do modelo ao fim da `MC-T4`:** versão 6, `20 orações, 7 tarefas, 6 mudanças`,
  `check` exit 0; `show` lê `17 entregues · 1 em curso · 0 emendadas · 2 previstas`.
- **AE-17 — a `MC-T5` fechou a guarda vermelha do plano e deixou dois achados de texto de card.**
  Laudo de 2026-09-20: `ressalva 91 bloqueante=nenhuma`, `seguir com ressalva`. **`kit_check
  -Mode check-drift` voltou a exit 0** — a guarda que a `MC-T3` virou, e o `Veredito mecânico
  (guardas)` do dossiê de evidência saiu `conforme` pela primeira vez desde a `MC-T2a`. Os dois
  achados são de autoria do card:
  1. **(alvo `dossiê`) O card trata raiz e kit como o mesmo README.** O passo 3a e os
     `Arquivos-alvo` dizem "as duas regiões marcadas do `README.md`", mas os marcadores
     `kit:agents`/`kit:skills` moram em `.claude/README.md` — a raiz não os tem — e
     `kit_check.ps1` resolve `KitRoot` como `.claude/`. O executor leu certo, não acionou
     contingência e entregou nos dois lugares corretos: `### 8.1` e a frase de §5 no `README.md`
     da raiz, alvo do `check-readme.ps1`; a região gerada em `.claude/README.md`, uma linha
     alterada, dentro de `kit:agents`, nenhuma fora. **Rota:** emenda do card em rodada de
     replanejamento, nomeando os dois arquivos.
  2. **(alvo `dossiê`) O `Pronto quando` de card de marco é insatisfazível no ato da revisão.**
     Ele conjuga as quatro conferências com "o veredito do dono está escrito no diário" — ato do
     passo 5, **posterior** ao laudo. Nenhuma entrega e nenhuma revisão podem satisfazê-lo quando
     são julgadas, e é por isso que `criterio-de-pronto` saiu `parcial`. **Rota:** a gramática do
     card de marco separa o que a **entrega** responde (conferências re-deriváveis) do que é
     **gate de fechamento** `done` (aceite do dono, registrado pelo orquestrador).
  **Estado do modelo ao fim da `MC-T5`:** versão 8, **20 orações: 20 entregues, 0 em curso,
  0 emendadas, 0 previstas**; `check` exit 0. O regime transitório da `DMC-21` expirou aqui.
  **A tarefa permanece em `review`:** o card exige o veredito do dono escrito no diário para
  fechar `done`, e o RDO dela nasce nessa transição.
- **AE-18 — Marco 2: o dono leu e apontou que o plano operacionalizou o modelo sem materializar o
  que o modelo é.** Leitura de 2026-09-20 sobre `OPERACOES_AS_IS.md` e a saída de `show`. O
  veredito não foi `go` limpo nem `no-go`: a entrega fica de pé e a rota se estende. Quatro
  apontamentos, nas palavras do dono:
  1. **A forma prescrita não é o modelo conceitual do DDD.** O modelo deve ser fidedigno à
     **intuição do objetivo** do plano, descrito **em objetos e operações**. Exemplo dado: um plano
     que copia de uma pasta para outra teria como modelo "agente lê pasta de origem, executa
     operação de cópia em memória, localiza a pasta de destino, executa operação de colagem". O que
     o `P-0741` prescreveu — orações independentes afirmando comportamento observável, cada uma com
     estado próprio — **não** é isso: falta o encadeamento de operações sobre objetos.
  2. **O estado tem de ser posição no fluxo, não status por frase.** O dono quer ler "o estágio
     atual é a leitura da pasta de origem" e opinar sobre esse fato; o agente, lendo o mesmo,
     deriva o que precisa ("então preciso de um caminho e de um toolset de leitura"). Hoje o
     `show` devolve 20 estados paralelos, não uma posição.
  3. **A `MC-T2` é responsabilidade herdada de outro papel.** O instrumento de conferência é
     atribuição do revisor e do planejador, não coisa intrínseca do modelo conceitual. Pede
     varredura dos artefatos já gerados atrás do que pertence a outros módulos — e cita como caso
     a operacionalização de tarefas a partir do plano, que é do agente de planejamento e deveria
     ter **spec própria**, a ser criada se não houver iniciativa de melhoramento desse agente.
  4. **O ensinamento não pode ficar pulverizado dentro dos agentes.** Duas alternativas postas
     pelo dono: centralizar numa **skill** que os agentes recebem por derivação da governança, ou
     criar um agente **model-designer** dono de todas as operações do modelo, acionado pelos demais
     para resolver conflito, entender contexto e propor mudança. Pediu avaliação de qual
     instrumento é o melhor.
  **Consequência:** a `MC-T5` permanece em `review` — o `Pronto quando` dela exige veredito escrito
  no diário, e o que chegou é diretiva de continuação. Nada foi commitado (`I-7`); 35 arquivos na
  árvore. Os três alvos de planejamento derivados desta diretiva são matéria do **planejador**, em
  contexto novo: o `scrum-master` não revisa plano (`GOVERNANCA.md` §3).

### RP-1 — Rodada de replanejamento de 2026-09-20 (escalada do Marco 2, `AE-18`)

**Classificação.** Técnica e tática, fechadas no mesmo contexto: a forma nova do modelo, o destino
da forma anterior, a mitigação da fenda entre julgar e escrever, a residência do ensinamento e a
decomposição em dois planos. A parte estratégica — **um agente único dono do modelo** — já vinha
decidida pelo dono no próprio `AE-18`, contra a recomendação do planejamento e com o critério dele
declarado; não foi reaberta. Nenhuma questão nova subiu ao dono: o que resta dele são os dois
Marcos 1, que são gates que já existiam.

**Efeito.** Dois planos gravados, com fronteira de arquivos declarada e disjunta:
`docs/plans/P-0743-modelo-de-dominio.md` (a forma nova, o instrumento, o modelador, os papéis e a
porta de entrada) e `docs/plans/P-0744-spec-do-planejador.md` (a especificação do agente de
planejamento). Este plano **não** é reescrito e **não** vira `superseded`: a premissa não caiu —
"a entrega fica de pé e a rota se estende", palavras do dono. A supersessão de doutrina está
registrada como `MD-9` na `### 1.3 Mudanças do modelo`. A `MC-T5` permanece em `review`, porque o
`Pronto quando` dela exige veredito do dono escrito no diário, e o que chegou foi diretiva de
continuação.

**Causa-raiz na autoria, e a fase que falhou.** Fase 2 do protocolo do planejador (*Decisões*). A
forma do modelo foi tratada como **decisão técnica** — rota e decomposição, que são do planejador —
quando ela é a **interface de leitura do dono**. Pelo teste de legitimidade ela passava nos três
critérios: duas formas levavam a planos materialmente diferentes; nenhum default se derivava de
PRD, doutrina ou decisão anterior, porque não havia forma anterior nenhuma; e o dono não a havia
respondido. A consequência foi medida: o plano entregou os cinco estratos, 20 orações confirmadas e
três guardas verdes, e mesmo assim levou `no-go` de forma no Marco 2 — o dono queria objetos e
operações encadeadas, com estado como posição no fluxo.

**A verificação que teria evitado.** Submeter, na rodada de decisões, um **worked example** da
leitura pronta — a saída do instrumento preenchida com dado do próprio plano, em poucas linhas,
com a alternativa ao lado — em vez de descrever a forma em prosa normativa. O `P-0743` já nasce com
esse instrumento embutido: a `## 7` dele é a leitura nova renderizada nos três momentos do plano, e
o Marco 1 dele é o dono julgando **a forma**, não só o escopo.

**Classe de erro nova → a verificação entra no protocolo.** Item novo na Fase 2 de
`.claude/agents/pantonic-planner.md`, gravado no mesmo ato desta rodada: *forma de artefato que o
dono lê é decisão dele, não do planejador*.
