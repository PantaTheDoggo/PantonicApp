# CARD — Revisão crítica do pickup de 2026-09-16 (janela Opus, `BKL-T2` → `AE-2`)

**Data:** 2026-09-16 · **Autor:** revisão feita em Fable 5.1 a pedido do dono, sobre a janela Opus 5
que executou `proximo-passo` e terminou em `AE-2` · **Destino:** insumo da próxima rodada §7.1
(`GOVERNANCA.md`) e da revisão das skills `proximo-passo`/`handover` · **Status:** `absorvido`
(2026-09-16) — achados 1-7 aplicados: `G-NOASK` (`GOVERNANCA.md` §7 item 18), §3 disciplina de
instrumento, §4.2 registro único e `contado`; detalhe em `CHANGELOG.md` [Não lançado].

## Fato medido

A janela consumiu **29 tool uses** (contados no transcript) até o handover; a linha gravada em
`docs/telemetria.tsv` (`BKL-AE2-pickup`, `contado`) diz **14**. O hook de ocupação (~50%) disparou
na 27ª chamada. Distribuição: diagnóstico 18 chamadas (1–18) · decisão do dono 1 · **registro e
fechamento 10 chamadas (20–29)** — um terço da janela para escrever um bloqueio.

## Achados, por peso

1. **Fechamento caro por escrita redundante.** O mesmo fato (`review_evidence.py` não casa ID
   prefixado; causa em `rdo.py:79-81`; entregável intacto; `RP-2` é a próxima) foi escrito **cinco
   vezes**: `AE-2` no plano (~40 linhas), bullet de nota da `BKL-T2`, `Fila corrente`, célula do
   índice (aumentando a prosa que a `C-4` já acusa e a `BKL-T6` terá de limpar) e o handover final
   (~25 linhas). Regra 7 pede *um registro canônico + ponteiros*. Rota: `handover` e `proximo-passo`
   fixarem que o achado mora **só** no `## Achados da execução`; nota, fila e índice recebem
   `AE-<n>` + linha:range; o handover ao dono é ≤ 8 linhas com ponteiro.
2. **Sondas diagnósticas com efeito colateral e chute.** (a) `rdo.py laudo` com sete `conforme` e
   `--plano <caminho>` quase gravou um laudo falso em `docs/RDO/laudos/docs/plans/...` — só falhou
   porque a pasta não existia. Sonda de escrita deve ir para `--laudos-dir <scratchpad>` ou não
   existir. (b) Retentativa com `--tarefa T2` antes de ler o regex — chute em vez de leitura
   (1 turno). (c) `grep … && ls` encadeado com `&&`: o `grep` sem match saiu 1 e a checagem de tmp
   não rodou, exigindo uma chamada extra. Três turnos perdidos por método.
3. **Turnos de correção evitáveis no registro.** (a) Range `487-528` citado no diário antes de ser
   calculado → chamada de conserto (`494-536`). (b) `telemetria.py append` com nomes de flag errados
   → chamada extra. (c) Script de edição inseriu texto e depois removeu a duplicata que ele mesmo
   criou, e ainda motivou uma leitura de verificação (Regra 7 proíbe) — a âncora certa era o fim da
   nota. Regra: calcular o número **na mesma chamada** que o consome; `--help` antes do primeiro
   uso de um instrumento numa janela.
4. **Leitura antecipada que não serviu.** O protocolo do `pantonic-reviewer` (140 linhas) foi
   lido antes de tentar gerar a evidência; quando a evidência falhou, o protocolo não foi usado.
   Ordem barata: rodar o instrumento primeiro, ler o protocolo só se ele produzir.
5. **Deliberação repetida no raciocínio.** O modelo re-derivou três vezes, em blocos longos, se o
   obstáculo era "owner-gated" ou "evento intrínseco" — o plano já dizia (§6: "tíquete só se o dono
   pedir"). Custo invisível no diário, visível no contexto. Sintoma do que o dono descreve como
   "contexto que aumenta indiscriminadamente com Opus": não são as saídas de ferramenta (bem
   filtradas com `sed -n`/`tail`), é o raciocínio e a prosa autorada.
6. **Pergunta ao dono com opções enviesadas para agir.** As três opções eram corrigir / fechar sem
   laudo / revisar sem evidência; faltou a mais barata — *anotar e adiar* —, que foi a escolhida via
   "Other". Regra: toda `AskUserQuestion` de rota inclui a opção de **registrar e não agir** quando
   ela existir.
7. **Telemetria auto-relatada errada por metade.** `tool_uses=14` contra 29 reais. `fonte contado`
   exige contagem, não estimativa; se a contagem não for feita, o campo é `nao_medido`.

## O que estava correto (não mexer)

Batching das leituras iniciais (2 por turno); filtragem de saída na origem; diagnóstico da causa
com evidência colada; parada sem substituir a rota (Regra 8); nenhuma releitura de decisão após a
resposta do dono; `AE-2` completo o bastante para a `RP-2` partir a frio.

## Sobre a comparação Opus × Fable

Não medível a partir daqui: a janela Opus não deixou `<usage>`; o único dado é o hook disparando
na 27ª chamada de uma janela com leituras curtas. A hipótese consistente com os achados 1 e 5 é
que o crescimento vem de **prosa autorada e raciocínio**, não de ingestão — logo a alavanca é o
achado 1 (registro único) e não mais filtro de saída. Confirmar exige uma janela Opus com o mesmo
fluxo e `<usage>` capturado por subagente — matéria para a `RP-2` ou para a rodada §7.1.
